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
import importlib.util


def load_foods_dir():
    ingredients, recipes = [], []
    foods_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "foods")
    for path in sorted(glob.glob(os.path.join(foods_dir, "*.py"))):
        spec = importlib.util.spec_from_file_location("_food", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        ingredients += getattr(mod, "INGREDIENTS", [])
        recipes     += getattr(mod, "RECIPES", [])
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

def _foods_are_equivalent(a, b):
    return _equiv_key(a) == _equiv_key(b)

def _merge_names(names):
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} / {names[1]}"
    return f"{names[0]} / {names[1]} / ..."


def deduplicate_foods(foods):
    """
    Returns (deduped_foods, errors).

    Rules:
      - Same name, same solver data   → keep one silently (multi-source files)
      - Same name, different data     → error (genuine conflict)
      - Different name, same data     → merge into one entry with concatenated
                                        name, e.g. "Bluefruit / Redfruit"
    """
    errors = []

    # Check for same-name, different-data conflicts.
    by_name = {}
    for food in foods:
        name = food.get("name")
        if name in by_name:
            if not _foods_are_equivalent(by_name[name], food):
                errors.append(
                    f"Name conflict: {name!r} appears with different nutrient data"
                )
        else:
            by_name[name] = food

    if errors:
        return foods, errors

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

    return [dict(first[k], name=_merge_names(groups[k])) for k in order], []
