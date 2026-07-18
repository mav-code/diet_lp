"""
diet_lp/loader.py

Loads food entries from all .py files in the foods/ subdirectory, then
deduplicates them before they reach the solver.

INGREDIENTS and RECIPES are organizational conventions; what actually controls
solver behavior is each entry's "unit" field. Both lists are concatenated and
treated identically from this point on.
"""

import glob
import os


def load_foods_dir():
    ingredients, recipes = [], []
    foods_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "foods")
    for path in sorted(glob.glob(os.path.join(foods_dir, "*.py"))):
        # Compile fresh instead of importing: importlib can serve stale
        # __pycache__ bytecode when a source edit lands within the same
        # mtime second, silently ignoring the edit.
        with open(path) as f:
            source = f.read()
        namespace = {}
        exec(compile(source, path, "exec"), namespace)
        mod_ingredients = namespace.get("INGREDIENTS", [])
        mod_recipes     = namespace.get("RECIPES", [])
        # Tag each entry with its source file so name conflicts can be
        # auto-disambiguated in deduplicate_foods().
        stem = os.path.splitext(os.path.basename(path))[0]
        for entry in (*mod_ingredients, *mod_recipes):
            if isinstance(entry, dict):
                entry.setdefault("_source", stem)
        ingredients += mod_ingredients
        recipes     += mod_recipes
    return ingredients, recipes


# ------------------------------------------------------------------------------
# Deduplication
# ------------------------------------------------------------------------------

def _norm_nutrients(nutrients):
    """Normalize nutrients for equivalence comparison: None → 0.0, sorted tuple."""
    return tuple(sorted(
        (k, v if v is not None else 0.0)
        for k, v in nutrients.items()
    ))

def _equiv_key(food):
    """Hashable key capturing everything the solver sees about a food entry."""
    return (
        food.get("unit"),
        food.get("grams"),
        food.get("min_amount", 0.0),
        food.get("max_amount"),
        _norm_nutrients(food.get("nutrients", {})),
    )

def _merge_names(names):
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} / {names[1]}"
    return f"{names[0]} / {names[1]} / ..."


def deduplicate_foods(foods):
    """
    Returns (deduped_foods, warnings).

    Rules:
      - Same name, same solver data   → keep one silently (multi-source files)
      - Same name, different data     → keep all variants, auto-disambiguated
                                        by source file, e.g. "Coffee, brewed
                                        [local_travel]", and warn
      - Different name, same data     → merge into one entry with concatenated
                                        name, e.g. "Bluefruit / Redfruit"
    """
    warnings = []

    # Find names that appear with more than one distinct set of solver data.
    keys_by_name = {}
    for food in foods:
        keys_by_name.setdefault(food.get("name"), set()).add(_equiv_key(food))
    conflicted = {name for name, keys in keys_by_name.items() if len(keys) > 1}

    # Rename conflicting entries after their source file; conflicting variants
    # within the same file get a counter suffix.
    if conflicted:
        foods = [dict(food) for food in foods]
        assigned = {}  # original name → {new name: equiv_key}
        for food in foods:
            name = food.get("name")
            if name not in conflicted:
                continue
            key = _equiv_key(food)
            slot = assigned.setdefault(name, {})
            src = food.get("_source", "unknown")
            new_name = f"{name} [{src}]"
            n = 2
            while new_name in slot and slot[new_name] != key:
                new_name = f"{name} [{src} #{n}]"
                n += 1
            slot[new_name] = key
            food["name"] = new_name
        for name in sorted(conflicted):
            variants = ", ".join(repr(v) for v in sorted(assigned[name]))
            warnings.append(
                f"Name conflict: {name!r} appears with different nutrient data; "
                f"kept as {variants}"
            )

    # Merge solver-equivalent entries, concatenating distinct names.
    groups = {}  # equiv_key → list of distinct names
    first  = {}  # equiv_key → first food dict seen (carries the data)
    order  = []  # preserves insertion order for deterministic output

    for food in foods:
        key  = _equiv_key(food)
        name = food.get("name")
        if key not in groups:
            groups[key] = [name]
            first[key]  = food
            order.append(key)
        elif name not in groups[key]:
            groups[key].append(name)

    return [dict(first[k], name=_merge_names(groups[k])) for k in order], warnings
