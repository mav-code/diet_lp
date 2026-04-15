"""
diet_lp/main.py

Diet LP toy using OR-Tools/GLOP.
Minimizes weighted deviation from macro targets (goal programming)
subject to hard bounds on calories, sodium, cholesterol, fiber,
and micronutrient minimums.

Usage:
    python main.py

All .py files in the foods/ subdirectory are loaded automatically.
Drop any file defining INGREDIENTS and/or RECIPES lists into foods/ and
it will be picked up on the next run. See README for details.

Note: the INGREDIENTS/RECIPES list names are organizational conventions only.
What actually controls solver behavior is each entry's "unit" field:
  "100g"      — nutrients are per 100g; solver variable is grams consumed.
  "1 serving" — nutrients are per serving; solver variable is servings consumed.
"""

from ortools.linear_solver import pywraplp

from loader import load_foods_dir
from validate import validate_foods
from settings import (
    CALORIE_MIN, CALORIE_MAX,
    MACRO_TARGETS, MACRO_BOUNDS, MACRO_WEIGHTS,
    SODIUM_MAX, CHOLESTEROL_MAX,
    FIBER_MIN,
    MICRONUTRIENT_MINS,
)

# ------------------------------------------------------------------------------
# Solver
# ------------------------------------------------------------------------------

def solve(foods):
    solver = pywraplp.Solver.CreateSolver("GLOP")
    if not solver:
        raise RuntimeError("Could not create GLOP solver.")

    inf = solver.infinity()

    # --- Decision variables: amount of each food ---
    # For INGREDIENTS: variable = grams consumed (per 100g nutrient scaling)
    # For RECIPES:     variable = number of servings
    food_vars = []
    for food in foods:
        lo = food.get("min_amount", 0.0)
        hi = food.get("max_amount", inf)
        var = solver.NumVar(lo, hi, food["name"])
        food_vars.append(var)

    # Helper: compute total of a nutrient across all foods
    # For ingredients, nutrients are per 100g so we divide by 100.
    # For recipes, nutrients are per serving so no scaling needed.
    def nutrient_total(key):
        terms = []
        for var, food in zip(food_vars, foods):
            val = food["nutrients"].get(key) or 0.0
            if food.get("unit", "100g") == "1 serving":
                scale = 1.0
            else:
                scale = 1.0 / 100.0
            terms.append((var, val * scale))
        return terms

    def add_linear_constraint(terms, lo, hi, name):
        c = solver.Constraint(lo, hi, name)
        for var, coef in terms:
            c.SetCoefficient(var, coef)
        return c

    # --- Calorie bounds (hard) ---
    add_linear_constraint(nutrient_total("calories"), CALORIE_MIN, CALORIE_MAX, "calories")

    # --- Macro hard bounds ---
    for macro, (lo, hi) in MACRO_BOUNDS.items():
        add_linear_constraint(nutrient_total(macro), lo, hi, f"{macro}_bounds")

    # --- Harmful nutrient ceilings (hard) ---
    add_linear_constraint(nutrient_total("sodium"),      0, SODIUM_MAX,      "sodium")
    add_linear_constraint(nutrient_total("cholesterol"), 0, CHOLESTEROL_MAX, "cholesterol")

    # --- Fiber floor (hard) ---
    add_linear_constraint(nutrient_total("fiber"), FIBER_MIN, inf, "fiber")

    # --- Micronutrient floors (hard) ---
    for nutrient, minimum in MICRONUTRIENT_MINS.items():
        add_linear_constraint(nutrient_total(nutrient), minimum, inf, nutrient)

    # --- Goal programming: macro deviation variables ---
    # For each macro m: actual_m - target_m = over_m - under_m
    # Both over_m and under_m >= 0.
    over_vars  = {}
    under_vars = {}

    for macro, target in MACRO_TARGETS.items():
        over_vars[macro]  = solver.NumVar(0.0, inf, f"{macro}_over")
        under_vars[macro] = solver.NumVar(0.0, inf, f"{macro}_under")

        # actual - target = over - under
        # => actual - over + under = target
        c = solver.Constraint(target, target, f"{macro}_goal")
        for var, coef in nutrient_total(macro):
            c.SetCoefficient(var, coef)
        c.SetCoefficient(over_vars[macro],  -1.0)
        c.SetCoefficient(under_vars[macro],  1.0)

    # --- Objective: minimize weighted macro deviations ---
    objective = solver.Objective()
    for macro in MACRO_TARGETS:
        w_over, w_under = MACRO_WEIGHTS[macro]
        objective.SetCoefficient(over_vars[macro],  w_over)
        objective.SetCoefficient(under_vars[macro], w_under)
    objective.SetMinimization()

    status = solver.Solve()
    return solver, status, food_vars, over_vars, under_vars


# ------------------------------------------------------------------------------
# Output
# ------------------------------------------------------------------------------

def print_results(solver, status, food_vars, foods, over_vars, under_vars):
    if status == solver.OPTIMAL:
        print("Status: OPTIMAL\n")
    elif status == solver.FEASIBLE:
        print("Status: FEASIBLE (suboptimal)\n")
    else:
        print("No solution found. The constraints may be infeasible.")
        print("Try relaxing calorie bounds, macro bounds, or micronutrient minimums.")
        return

    nutrient_keys = [
        "calories", "carbs", "fat", "protein",
        "sodium", "cholesterol", "fiber",
        "vitamin_c", "calcium", "iron", "potassium", "magnesium",
        "zinc", "b12", "folate", "thiamine", "riboflavin", "niacin",
    ]

    # --- Collect active foods, compute gram weight, sort descending ---
    active = []
    for var, food in zip(food_vars, foods):
        amt = var.solution_value()
        if amt < 0.01:
            continue
        is_recipe = food.get("unit") == "1 serving"
        scale = 1.0 if is_recipe else 1.0 / 100.0
        weight_g = amt * food.get("grams", 100) if is_recipe else amt
        nutrients = {k: (food["nutrients"].get(k) or 0.0) * amt * scale
                     for k in nutrient_keys}
        active.append(dict(name=food["name"], amt=amt, is_recipe=is_recipe,
                           weight_g=weight_g, nutrients=nutrients))
    active.sort(key=lambda x: x["weight_g"], reverse=True)

    totals = {k: sum(a["nutrients"][k] for a in active) for k in nutrient_keys}

    # --- Table helpers ---
    # Foods are rows; nutrients are columns.
    # Two tables: main nutrients (col_w=9) and micronutrients (col_w=7).
    NAME_W = 20
    AMT_W  = 8

    def print_table(col_w, cols):
        """
        cols: list of (key, header, unit, target_str), or None to insert a '|' divider.
        Prints header, one row per food, a TOTAL row, and a Target row.
        """
        real_cols = [c for c in cols if c is not None]
        n_dividers = sum(1 for c in cols if c is None)
        sep = "-" * (NAME_W + 1 + AMT_W + len(real_cols) * (col_w + 1) + n_dividers * 2)

        # Header line 1: "Amount" label + column abbreviations
        h1 = f"{'':>{NAME_W}} {'Amount':>{AMT_W}}"
        for c in cols:
            h1 += " |" if c is None else f" {c[1]:>{col_w}}"
        print(h1)

        # Header line 2: column units
        h2 = f"{'':>{NAME_W}} {'':>{AMT_W}}"
        for c in cols:
            h2 += " |" if c is None else f" {c[2]:>{col_w}}"
        print(h2)

        print(sep)

        for a in active:
            amt_str = f"{a['amt']:.1f}srv" if a["is_recipe"] else f"{a['amt']:.0f}g"
            line = f"{a['name'][:NAME_W]:<{NAME_W}} {amt_str:>{AMT_W}}"
            for c in cols:
                line += " |" if c is None else f" {a['nutrients'][c[0]]:{col_w}.1f}"
            print(line)

        print(sep)

        total_line = f"{'TOTAL':<{NAME_W}} {'':>{AMT_W}}"
        for c in cols:
            total_line += " |" if c is None else f" {totals[c[0]]:{col_w}.1f}"
        print(total_line)

        target_line = f"{'Target':<{NAME_W}} {'':>{AMT_W}}"
        for c in cols:
            target_line += " |" if c is None else f" {c[3]:>{col_w}}"
        print(target_line)

        print(sep)

    # --- Table 1: calories, macros, constrained nutrients ---
    lo_c, hi_c = MACRO_BOUNDS["carbs"]
    lo_f, hi_f = MACRO_BOUNDS["fat"]
    lo_p, hi_p = MACRO_BOUNDS["protein"]
    main_cols = [
        ("calories",    "Cal",     "kcal", f"{CALORIE_MIN}-{CALORIE_MAX}"),
        None,
        ("carbs",       "Carbs",   "g",    f"{lo_c}-{hi_c}"),
        ("fat",         "Fat",     "g",    f"{lo_f}-{hi_f}"),
        ("protein",     "Protein", "g",    f"{lo_p}-{hi_p}"),
        None,
        ("sodium",      "Sodium",  "mg",   f"max {SODIUM_MAX}"),
        ("cholesterol", "Cholest", "mg",   f"max {CHOLESTEROL_MAX}"),
        ("fiber",       "Fiber",   "g",    f"min {FIBER_MIN}"),
    ]
    print_table(col_w=9, cols=main_cols)

    # --- Table 2: micronutrients ---
    print()
    micro_cols = [
        ("vitamin_c",  "Vit C",   "mg",  f"min {MICRONUTRIENT_MINS['vitamin_c']}"),
        ("calcium",    "Calcium", "mg",  f"min {MICRONUTRIENT_MINS['calcium']}"),
        ("iron",       "Iron",    "mg",  f"min {MICRONUTRIENT_MINS['iron']}"),
        ("potassium",  "Potass.", "mg",  f"min {MICRONUTRIENT_MINS['potassium']}"),
        ("magnesium",  "Magnes.", "mg",  f"min {MICRONUTRIENT_MINS['magnesium']}"),
        ("zinc",       "Zinc",    "mg",  f"min {MICRONUTRIENT_MINS['zinc']}"),
        ("b12",        "B12",     "mcg", f"min {MICRONUTRIENT_MINS['b12']}"),
        ("folate",     "Folate",  "mcg", f"min {MICRONUTRIENT_MINS['folate']}"),
        ("thiamine",   "Thiamin", "mg",  f"min {MICRONUTRIENT_MINS['thiamine']}"),
        ("riboflavin", "Riboflv", "mg",  f"min {MICRONUTRIENT_MINS['riboflavin']}"),
        ("niacin",     "Niacin",  "mg",  f"min {MICRONUTRIENT_MINS['niacin']}"),
    ]
    print_table(col_w=7, cols=micro_cols)

    # --- Macro deviation summary ---
    print()
    for macro in ["carbs", "fat", "protein"]:
        target = MACRO_TARGETS[macro]
        over  = over_vars[macro].solution_value()
        under = under_vars[macro].solution_value()
        print(f"  {macro.capitalize():<10} target {target}g   +{over:.1f} / -{under:.1f}")

    obj_val = sum(
        MACRO_WEIGHTS[m][0] * over_vars[m].solution_value() +
        MACRO_WEIGHTS[m][1] * under_vars[m].solution_value()
        for m in MACRO_TARGETS
    )
    print(f"\n  Objective (weighted macro deviation): {obj_val:.3f}")


# ------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    INGREDIENTS, RECIPES = load_foods_dir()
    all_foods = INGREDIENTS + RECIPES

    if not all_foods:
        print("No foods loaded. Check the foods/ directory.")
        exit(1)

    errors = validate_foods(all_foods)
    if errors:
        print(f"Found {len(errors)} error(s) in food data — aborting:\n")
        for err in errors:
            print(f"  {err}")
        exit(1)

    print(f"Loaded {len(all_foods)} foods.")
    print(f"Solving...\n")

    solver, status, food_vars, over_vars, under_vars = solve(all_foods)
    print_results(solver, status, food_vars, all_foods, over_vars, under_vars)
