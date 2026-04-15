"""
diet_lp/loader.py

Loads food entries from all .py files in the foods/ subdirectory.
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
