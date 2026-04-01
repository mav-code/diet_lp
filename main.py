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
"""

import glob
import os
import importlib.util

from ortools.linear_solver import pywraplp

# ------------------------------------------------------------------------------
# Food loading
# ------------------------------------------------------------------------------

def _load_foods_dir():
    ingredients, recipes = [], []
    foods_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "foods")
    for path in sorted(glob.glob(os.path.join(foods_dir, "*.py"))):
        spec = importlib.util.spec_from_file_location("_food", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        ingredients += getattr(mod, "INGREDIENTS", [])
        recipes     += getattr(mod, "RECIPES", [])
    return ingredients, recipes

INGREDIENTS, RECIPES = _load_foods_dir()

# ------------------------------------------------------------------------------
# Settings
# ------------------------------------------------------------------------------

# Calorie bounds (hard constraints)
CALORIE_MIN = 1600
CALORIE_MAX = 1795

# Macro targets for goal programming
# The solver minimizes weighted deviation from these targets.
# Targets are set to the midpoint of each range by default;
# adjust to bias toward one end.
MACRO_TARGETS = {
    "carbs":   122,   # g  (range 20–225)
    "fat":      80,   # g  (range 61–100)
    "protein": 203,   # g  (range 71–225, adjusted upwards based on advice)
}

# Macro hard bounds (the solver may not exceed/fall below these regardless)
MACRO_BOUNDS = {
    "carbs":   (20,  225),
    "fat":     (61,  100),
    "protein": (71,  225),
}

# Objective weights for over/under deviation per macro.
# Higher weight = solver tries harder to avoid that deviation.
# Asymmetric: e.g. undershooting protein is penalized more than overshooting.
MACRO_WEIGHTS = {
    #              (over, under)
    "carbs":       (1.0,  1.0),
    "fat":         (2.0,  2.0),   # tighter range, penalize deviation more
    "protein":     (1.0,  3.0),   # undershooting protein costs more
}

# Hard upper bounds on harmful nutrients
SODIUM_MAX      = 1500  # mg
CHOLESTEROL_MAX = 200   # mg

# Hard lower bound on fiber
FIBER_MIN = 31  # g

# Micronutrient minimums (RDA/AI values, NIH Office of Dietary Supplements)
# These are hard lower bounds — the solver must satisfy all of them.
MICRONUTRIENT_MINS = {
    "vitamin_c":  90,    # mg   (RDA adult male; 75 for female)
    "calcium":    1000,  # mg
    "iron":       8,     # mg   (RDA adult male; 18 for premenopausal female)
    "potassium":  3400,  # mg   (AI)
    "magnesium":  420,   # mg   (RDA adult male; 320 for female)
    "zinc":       11,    # mg   (RDA adult male; 8 for female)
    "b12":        2.4,   # mcg
    "folate":     400,   # mcg  (DFE)
    "thiamine":   1.2,   # mg
    "riboflavin": 1.3,   # mg
    "niacin":     16,    # mg   (NE)
}

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
            val = food["nutrients"].get(key, 0.0)
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

    print("=" * 60)
    print("FOODS IN SOLUTION")
    print("=" * 60)

    # Collect nutrients for summary
    totals = {k: 0.0 for k in [
        "calories", "carbs", "fat", "protein",
        "sodium", "cholesterol", "fiber",
        "vitamin_c", "calcium", "iron", "potassium", "magnesium",
        "zinc", "b12", "folate", "thiamine", "riboflavin", "niacin",
    ]}

    for var, food in zip(food_vars, foods):
        amt = var.solution_value()
        if amt < 0.01:
            continue
        is_recipe = food.get("unit") == "1 serving"
        scale = 1.0 if is_recipe else 1.0 / 100.0
        if is_recipe:
            print(f"  {food['name']}: {amt:.2f} servings")
        else:
            print(f"  {food['name']}: {amt:.1f}g")
        for key in totals:
            totals[key] += food["nutrients"].get(key, 0.0) * amt * scale

    print()
    print("=" * 60)
    print("NUTRIENT SUMMARY")
    print("=" * 60)

    def row(label, actual, target_str, unit):
        print(f"  {label:<22} {actual:>8.1f} {unit:<5}  (target: {target_str})")

    # Calories
    row("Calories", totals["calories"],
        f"{CALORIE_MIN}–{CALORIE_MAX}", "kcal")

    print()
    print("  -- Macros --")
    for macro in ["carbs", "fat", "protein"]:
        lo, hi = MACRO_BOUNDS[macro]
        target = MACRO_TARGETS[macro]
        over  = over_vars[macro].solution_value()
        under = under_vars[macro].solution_value()
        deviation = f"(+{over:.1f} / -{under:.1f} from target {target}g)"
        row(macro.capitalize(), totals[macro], f"{lo}–{hi}g", "g")
        print(f"  {'':22} {deviation}")

    print()
    print("  -- Constrained nutrients --")
    row("Sodium",      totals["sodium"],      f"max {SODIUM_MAX}",      "mg")
    row("Cholesterol", totals["cholesterol"], f"max {CHOLESTEROL_MAX}", "mg")
    row("Fiber",       totals["fiber"],       f"min {FIBER_MIN}",       "g")

    print()
    print("  -- Micronutrients --")
    micro_labels = {
        "vitamin_c":  ("Vitamin C",  "mg"),
        "calcium":    ("Calcium",    "mg"),
        "iron":       ("Iron",       "mg"),
        "potassium":  ("Potassium",  "mg"),
        "magnesium":  ("Magnesium",  "mg"),
        "zinc":       ("Zinc",       "mg"),
        "b12":        ("Vitamin B12","mcg"),
        "folate":     ("Folate",     "mcg"),
        "thiamine":   ("Thiamine",   "mg"),
        "riboflavin": ("Riboflavin", "mg"),
        "niacin":     ("Niacin",     "mg"),
    }
    for key, (label, unit) in micro_labels.items():
        minimum = MICRONUTRIENT_MINS[key]
        row(label, totals[key], f"min {minimum}", unit)

    print()
    obj_val = sum(
        MACRO_WEIGHTS[m][0] * over_vars[m].solution_value() +
        MACRO_WEIGHTS[m][1] * under_vars[m].solution_value()
        for m in MACRO_TARGETS
    )
    print(f"  Objective (weighted macro deviation): {obj_val:.3f}")
    print("=" * 60)


# ------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    # Combine all food groups
    all_foods = INGREDIENTS + RECIPES

    if not all_foods:
        print("No foods loaded. Check your imports in main.py.")
        exit(1)

    print(f"Loaded {len(all_foods)} foods.")
    print(f"Solving...\n")

    solver, status, food_vars, over_vars, under_vars = solve(all_foods)
    print_results(solver, status, food_vars, all_foods, over_vars, under_vars)
