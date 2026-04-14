"""
diet_lp/foods/local_example.py

Template for a personal food database.

Copy this file to foods/local.py (or any name starting with local_) and add
your own entries. Files named local_*.py are gitignored; this example is the
exception and stays tracked so it's available after cloning.

Both INGREDIENTS and RECIPES are optional — omit either list if unused.
The list names are organizational conventions; what actually controls solver
behavior is each entry's "unit" field:
  "100g"      — nutrients per 100g; solver variable is grams consumed.
  "1 serving" — nutrients per serving; solver variable is servings consumed.

See foods/usda.py or foods/stigler.py for full examples.
"""

INGREDIENTS = [
    # Add your personal ingredients here, e.g.:
    # {
    #     "name": "My food",
    #     "unit": "100g",
    #     "grams": 100,
    #     "nutrients": {
    #         "calories": 0, "carbs": 0, "fat": 0, "protein": 0,
    #         "sodium": 0, "cholesterol": 0, "fiber": 0,
    #         "vitamin_c": 0, "calcium": 0, "iron": 0, "potassium": 0,
    #         "magnesium": 0, "zinc": 0, "b12": 0, "folate": 0,
    #         "thiamine": 0, "riboflavin": 0, "niacin": 0,
    #     },
    # },
]

RECIPES = [
    # Add your personal recipes here, e.g.:
    # {
    #     "name": "My recipe (1 serving ~300g)",
    #     "unit": "1 serving",
    #     "grams": 300,
    #     "nutrients": {
    #         "calories": 0, "carbs": 0, "fat": 0, "protein": 0,
    #         "sodium": 0, "cholesterol": 0, "fiber": 0,
    #         "vitamin_c": 0, "calcium": 0, "iron": 0, "potassium": 0,
    #         "magnesium": 0, "zinc": 0, "b12": 0, "folate": 0,
    #         "thiamine": 0, "riboflavin": 0, "niacin": 0,
    #     },
    # },
]
