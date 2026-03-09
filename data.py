"""
diet_lp/data.py

Food database for the diet LP optimizer.
Each entry is a dict with:
  - name: str
  - unit: str (display unit, e.g. "100g" or "1 serving")
  - grams: float (grams per unit — used for ingredients; set to 1.0 for recipes where nutrients are per serving)
  - nutrients: dict of nutrient values per unit

Nutrient keys (all per unit as defined above):
  calories        kcal
  carbs           g
  fat             g
  protein         g
  sodium          mg
  cholesterol     mg
  fiber           g
  vitamin_c       mg
  calcium         mg
  iron            mg
  potassium       mg
  magnesium       mg
  zinc            mg
  b12             mcg
  folate          mcg

For INGREDIENTS, the solver variable represents grams consumed.
Nutrient values should be per 100g so the solver can scale them.

For RECIPES, the solver variable represents number of servings.
Nutrient values should be per 1 serving (grams field is ignored for nutrient scaling).

Per-food bounds (optional):
  min_amount: float  (minimum grams/servings per day; default 0)
  max_amount: float  (maximum grams/servings per day; default unconstrained)
"""

# ------------------------------------------------------------------------------
# INGREDIENTS
# ------------------------------------------------------------------------------

INGREDIENTS = [

    # --- Stigler (1945) commodity set -----------------------------------------
    # Calories, protein, calcium, iron, thiamine, riboflavin, niacin, and
    # vitamin C are derived from the 1939 US price data used in Stigler's diet
    # problem (https://developers.google.com/optimization/lp/stigler_diet),
    # converted from per-dollar values: nutrient = value × price ÷ unit_weight × 100.
    # Carbs, fat, sodium, cholesterol, fiber, potassium, magnesium, zinc, b12,
    # and folate are from USDA FoodData Central SR Legacy (per 100g).
    # Foods already in the USDA SR Legacy section below are omitted to avoid
    # duplicates: Milk, Eggs, Cheese (Cheddar), Peanut Butter, Apples, Bananas,
    # Oranges, Rolled Oats, Sweet Potatoes, Spinach, Carrots, Onions.

    # --- Grains (Stigler) ---
    {
        "name": "Wheat Flour (Enriched)",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 354.8, "carbs": 76.3, "fat": 1.0, "protein": 11.2,
            "sodium": 2, "cholesterol": 0, "fiber": 2.7,
            "vitamin_c": 0.0, "calcium": 16, "iron": 2.9, "potassium": 107,
            "magnesium": 22, "zinc": 0.7, "b12": 0.0, "folate": 291,
            "thiamine": 0.44, "riboflavin": 0.264, "niacin": 3.5,
        },
    },
    {
        "name": "Macaroni",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 360.6, "carbs": 74.7, "fat": 1.5, "protein": 13.0,
            "sodium": 6, "cholesterol": 0, "fiber": 3.2,
            "vitamin_c": 0.0, "calcium": 22, "iron": 1.68, "potassium": 223,
            "magnesium": 53, "zinc": 1.4, "b12": 0.0, "folate": 391,
            "thiamine": 0.099, "riboflavin": 0.059, "niacin": 2.11,
        },
    },
    {
        "name": "Wheat Cereal (Enriched)",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 359.7, "carbs": 73.2, "fat": 1.4, "protein": 11.5,
            "sodium": 124, "cholesterol": 0, "fiber": 4.2,
            "vitamin_c": 0.0, "calcium": 439, "iron": 5.34, "potassium": 153,
            "magnesium": 45, "zinc": 1.3, "b12": 0.0, "folate": 182,
            "thiamine": 0.439, "riboflavin": 0.268, "niacin": 3.48,
        },
    },
    {
        "name": "Corn Flakes",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 356.9, "carbs": 88.0, "fat": 0.9, "protein": 7.9,
            "sodium": 571, "cholesterol": 0, "fiber": 2.7,
            "vitamin_c": 0.0, "calcium": 3, "iron": 1.75, "potassium": 107,
            "magnesium": 7, "zinc": 0.2, "b12": 5.4, "folate": 714,
            "thiamine": 0.423, "riboflavin": 0.072, "niacin": 2.13,
        },
    },
    {
        "name": "Corn Meal",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 365.1, "carbs": 76.9, "fat": 3.6, "protein": 9.1,
            "sodium": 35, "cholesterol": 0, "fiber": 7.3,
            "vitamin_c": 0.0, "calcium": 17, "iron": 1.0, "potassium": 287,
            "magnesium": 127, "zinc": 1.8, "b12": 0.0, "folate": 25,
            "thiamine": 0.176, "riboflavin": 0.08, "niacin": 1.07,
        },
    },
    {
        "name": "Hominy Grits",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 357.3, "carbs": 79.6, "fat": 1.2, "protein": 8.5,
            "sodium": 1, "cholesterol": 0, "fiber": 4.8,
            "vitamin_c": 0.0, "calcium": 10, "iron": 1.0, "potassium": 137,
            "magnesium": 27, "zinc": 0.4, "b12": 0.0, "folate": 205,
            "thiamine": 0.132, "riboflavin": 0.02, "niacin": 1.37,
        },
    },
    {
        "name": "Rice",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 350.5, "carbs": 80.0, "fat": 0.7, "protein": 7.6,
            "sodium": 5, "cholesterol": 0, "fiber": 1.3,
            "vitamin_c": 0.0, "calcium": 10, "iron": 0.68, "potassium": 115,
            "magnesium": 25, "zinc": 1.1, "b12": 0.0, "folate": 8,
            "thiamine": 0.033, "riboflavin": 0.079, "niacin": 0.99,
        },
    },
    {
        "name": "White Bread (Enriched)",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 261.2, "carbs": 48.7, "fat": 3.6, "protein": 8.5,
            "sodium": 491, "cholesterol": 0, "fiber": 2.3,
            "vitamin_c": 0.0, "calcium": 44, "iron": 2.0, "potassium": 115,
            "magnesium": 26, "zinc": 0.8, "b12": 0.0, "folate": 139,
            "thiamine": 0.24, "riboflavin": 0.148, "niacin": 2.19,
        },
    },
    {
        "name": "Whole Wheat Bread",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 244.8, "carbs": 43.1, "fat": 3.5, "protein": 9.7,
            "sodium": 400, "cholesterol": 0, "fiber": 6.0,
            "vitamin_c": 0.0, "calcium": 54, "iron": 2.51, "potassium": 248,
            "magnesium": 76, "zinc": 1.8, "b12": 0.0, "folate": 43,
            "thiamine": 0.279, "riboflavin": 0.128, "niacin": 3.21,
        },
    },
    {
        "name": "Rye Bread",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 248.8, "carbs": 48.3, "fat": 3.3, "protein": 8.8,
            "sodium": 603, "cholesterol": 0, "fiber": 5.8,
            "vitamin_c": 0.0, "calcium": 22, "iron": 1.65, "potassium": 166,
            "magnesium": 40, "zinc": 0.9, "b12": 0.0, "folate": 100,
            "thiamine": 0.199, "riboflavin": 0.06, "niacin": 1.32,
        },
    },
    {
        "name": "Pound Cake",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 437.4, "carbs": 53.3, "fat": 15.7, "protein": 7.1,
            "sodium": 424, "cholesterol": 146, "fiber": 0.7,
            "vitamin_c": 0.0, "calcium": 22, "iron": 1.69, "potassium": 88,
            "magnesium": 12, "zinc": 0.5, "b12": 0.3, "folate": 60,
            "thiamine": 0.153, "riboflavin": 0.164, "niacin": 0.93,
        },
    },
    {
        "name": "Soda Crackers",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 416.1, "carbs": 71.5, "fat": 8.6, "protein": 9.6,
            "sodium": 1076, "cholesterol": 0, "fiber": 2.5,
            "vitamin_c": 0.0, "calcium": 17, "iron": 1.66, "potassium": 137,
            "magnesium": 22, "zinc": 0.7, "b12": 0.0, "folate": 93,
            "thiamine": 0.0, "riboflavin": 0.0, "niacin": 0.0,
        },
    },

    # --- Dairy & Fats (Stigler) ---
    {
        "name": "Evaporated Milk (can)",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 136.9, "carbs": 10.0, "fat": 7.6, "protein": 6.9,
            "sodium": 106, "cholesterol": 29, "fiber": 0.0,
            "vitamin_c": 1.0, "calcium": 246, "iron": 0.15, "potassium": 303,
            "magnesium": 24, "zinc": 0.8, "b12": 0.2, "folate": 5,
            "thiamine": 0.049, "riboflavin": 0.383, "niacin": 0.18,
        },
    },
    {
        "name": "Butter",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 733.3, "carbs": 0.1, "fat": 81.1, "protein": 0.6,
            "sodium": 643, "cholesterol": 215, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 14, "iron": 0.2, "potassium": 24,
            "magnesium": 2, "zinc": 0.1, "b12": 0.2, "folate": 3,
            "thiamine": 0.0, "riboflavin": 0.014, "niacin": 0.14,
        },
    },
    {
        "name": "Oleomargarine",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 731.2, "carbs": 0.9, "fat": 80.7, "protein": 0.6,
            "sodium": 751, "cholesterol": 0, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 21, "iron": 0.21, "potassium": 42,
            "magnesium": 2, "zinc": 0.1, "b12": 0.0, "folate": 1,
            "thiamine": 0.007, "riboflavin": 0.0, "niacin": 0.0,
        },
    },
    {
        "name": "Cream",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 208.6, "carbs": 3.7, "fat": 19.3, "protein": 2.9,
            "sodium": 41, "cholesterol": 66, "fiber": 0.0,
            "vitamin_c": 1.0, "calcium": 101, "iron": 0.18, "potassium": 130,
            "magnesium": 9, "zinc": 0.3, "b12": 0.2, "folate": 3,
            "thiamine": 0.036, "riboflavin": 0.149, "niacin": 0.0,
        },
    },
    {
        "name": "Mayonnaise",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 607.0, "carbs": 3.1, "fat": 74.9, "protein": 1.3,
            "sodium": 636, "cholesterol": 60, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 14, "iron": 0.56, "potassium": 34,
            "magnesium": 5, "zinc": 0.4, "b12": 0.1, "folate": 8,
            "thiamine": 0.028, "riboflavin": 0.035, "niacin": 0.0,
        },
    },
    {
        "name": "Crisco",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 899.5, "carbs": 0.0, "fat": 100.0, "protein": 0.0,
            "sodium": 0, "cholesterol": 0, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 0, "iron": 0.0, "potassium": 0,
            "magnesium": 0, "zinc": 0.0, "b12": 0.0, "folate": 0,
            "thiamine": 0.0, "riboflavin": 0.0, "niacin": 0.0,
        },
    },
    {
        "name": "Lard",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 900.9, "carbs": 0.0, "fat": 100.0, "protein": 0.0,
            "sodium": 0, "cholesterol": 95, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 0, "iron": 0.0, "potassium": 0,
            "magnesium": 0, "zinc": 0.1, "b12": 0.0, "folate": 0,
            "thiamine": 0.0, "riboflavin": 0.011, "niacin": 0.11,
        },
    },

    # --- Meats & Fish (Stigler) ---
    {
        "name": "Sirloin Steak",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 253.2, "carbs": 0.0, "fat": 11.6, "protein": 14.5,
            "sodium": 57, "cholesterol": 64, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 9, "iron": 2.97, "potassium": 335,
            "magnesium": 22, "zinc": 4.0, "b12": 1.5, "folate": 8,
            "thiamine": 0.183, "riboflavin": 0.253, "niacin": 6.02,
        },
    },
    {
        "name": "Round Steak",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 176.5, "carbs": 0.0, "fat": 4.6, "protein": 17.2,
            "sodium": 57, "cholesterol": 68, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 8, "iron": 2.57, "potassium": 353,
            "magnesium": 26, "zinc": 4.7, "b12": 1.9, "folate": 8,
            "thiamine": 0.201, "riboflavin": 0.193, "niacin": 6.98,
        },
    },
    {
        "name": "Rib Roast",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 218.9, "carbs": 0.0, "fat": 22.0, "protein": 13.7,
            "sodium": 56, "cholesterol": 70, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 6, "iron": 2.12, "potassium": 302,
            "magnesium": 20, "zinc": 4.4, "b12": 1.8, "folate": 6,
            "thiamine": 0.0, "riboflavin": 0.129, "niacin": 0.0,
        },
    },
    {
        "name": "Chuck Roast",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 179.4, "carbs": 0.0, "fat": 13.8, "protein": 15.4,
            "sodium": 61, "cholesterol": 66, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 10, "iron": 2.29, "potassium": 310,
            "magnesium": 21, "zinc": 5.7, "b12": 2.3, "folate": 7,
            "thiamine": 0.05, "riboflavin": 0.199, "niacin": 5.98,
        },
    },
    {
        "name": "Plate (beef)",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 273.6, "carbs": 0.0, "fat": 30.0, "protein": 13.0,
            "sodium": 55, "cholesterol": 72, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 6, "iron": 2.0, "potassium": 270,
            "magnesium": 17, "zinc": 3.8, "b12": 1.4, "folate": 5,
            "thiamine": 0.029, "riboflavin": 0.0, "niacin": 0.0,
        },
    },
    {
        "name": "Liver (Beef)",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 130.0, "carbs": 3.9, "fat": 3.6, "protein": 19.7,
            "sodium": 69, "cholesterol": 275, "fiber": 0.0,
            "vitamin_c": 31.0, "calcium": 12, "iron": 8.21, "potassium": 313,
            "magnesium": 18, "zinc": 4.0, "b12": 59.3, "folate": 290,
            "thiamine": 0.378, "riboflavin": 3.001, "niacin": 18.67,
        },
    },
    {
        "name": "Leg of Lamb",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 188.6, "carbs": 0.0, "fat": 14.0, "protein": 14.9,
            "sodium": 64, "cholesterol": 72, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 6, "iron": 1.22, "potassium": 290,
            "magnesium": 22, "zinc": 3.4, "b12": 2.1, "folate": 18,
            "thiamine": 0.17, "riboflavin": 0.237, "niacin": 5.23,
        },
    },
    {
        "name": "Lamb Chops (Rib)",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 266.3, "carbs": 0.0, "fat": 23.6, "protein": 11.3,
            "sodium": 65, "cholesterol": 74, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 8, "iron": 1.21, "potassium": 268,
            "magnesium": 20, "zinc": 2.8, "b12": 2.1, "folate": 14,
            "thiamine": 0.137, "riboflavin": 0.218, "niacin": 4.36,
        },
    },
    {
        "name": "Pork Chops",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 236.9, "carbs": 0.0, "fat": 13.9, "protein": 13.3,
            "sodium": 51, "cholesterol": 67, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 14, "iron": 2.03, "potassium": 363,
            "magnesium": 24, "zinc": 1.7, "b12": 0.5, "folate": 4,
            "thiamine": 1.178, "riboflavin": 0.183, "niacin": 4.06,
        },
    },
    {
        "name": "Pork Loin Roast",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 234.7, "carbs": 0.0, "fat": 14.0, "protein": 13.3,
            "sodium": 48, "cholesterol": 68, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 16, "iron": 1.97, "potassium": 362,
            "magnesium": 25, "zinc": 2.0, "b12": 0.6, "folate": 4,
            "thiamine": 0.971, "riboflavin": 0.192, "niacin": 4.21,
        },
    },
    {
        "name": "Bacon",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 586.9, "carbs": 1.4, "fat": 45.0, "protein": 8.6,
            "sodium": 833, "cholesterol": 110, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 11, "iron": 1.3, "potassium": 312,
            "magnesium": 18, "zinc": 1.9, "b12": 0.7, "folate": 1,
            "thiamine": 0.102, "riboflavin": 0.102, "niacin": 4.01,
        },
    },
    {
        "name": "Ham, smoked",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 404.7, "carbs": 1.5, "fat": 14.3, "protein": 12.8,
            "sodium": 1203, "cholesterol": 54, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 12, "iron": 1.87, "potassium": 287,
            "magnesium": 16, "zinc": 2.0, "b12": 0.6, "folate": 3,
            "thiamine": 0.598, "riboflavin": 0.199, "niacin": 3.02,
        },
    },
    {
        "name": "Salt Pork",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 663.1, "carbs": 0.0, "fat": 72.0, "protein": 5.8,
            "sodium": 1717, "cholesterol": 99, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 4, "iron": 0.92, "potassium": 129,
            "magnesium": 7, "zinc": 0.8, "b12": 0.4, "folate": 1,
            "thiamine": 0.049, "riboflavin": 0.063, "niacin": 0.0,
        },
    },
    {
        "name": "Roasting Chicken",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 120.2, "carbs": 0.0, "fat": 15.1, "protein": 12.3,
            "sodium": 75, "cholesterol": 75, "fiber": 0.0,
            "vitamin_c": 3.1, "calcium": 7, "iron": 2.0, "potassium": 223,
            "magnesium": 20, "zinc": 1.3, "b12": 0.3, "folate": 8,
            "thiamine": 0.06, "riboflavin": 0.12, "niacin": 4.54,
        },
    },
    {
        "name": "Veal Cutlets",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 158.5, "carbs": 0.0, "fat": 2.4, "protein": 14.5,
            "sodium": 80, "cholesterol": 90, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 9, "iron": 2.24, "potassium": 339,
            "magnesium": 28, "zinc": 2.6, "b12": 1.3, "folate": 11,
            "thiamine": 0.131, "riboflavin": 0.224, "niacin": 5.32,
        },
    },
    {
        "name": "Salmon, Pink (can)",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 166.2, "carbs": 0.0, "fat": 5.1, "protein": 20.2,
            "sodium": 397, "cholesterol": 52, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 195, "iron": 1.29, "potassium": 338,
            "magnesium": 29, "zinc": 0.9, "b12": 3.2, "folate": 12,
            "thiamine": 0.029, "riboflavin": 0.14, "niacin": 5.99,
        },
    },

    # --- Fruits (Stigler) ---
    {
        "name": "Lemons",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 21.7, "carbs": 9.3, "fat": 0.3, "protein": 0.5,
            "sodium": 2, "cholesterol": 0, "fiber": 2.8,
            "vitamin_c": 20.6, "calcium": 11, "iron": 0.3, "potassium": 138,
            "magnesium": 8, "zinc": 0.1, "b12": 0.0, "folate": 11,
            "thiamine": 0.011, "riboflavin": 0.0, "niacin": 0.09,
        },
    },
    {
        "name": "Peaches (can)",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 78.4, "carbs": 19.5, "fat": 0.1, "protein": 0.4,
            "sodium": 5, "cholesterol": 0, "fiber": 1.2,
            "vitamin_c": 4.2, "calcium": 8, "iron": 0.21, "potassium": 81,
            "magnesium": 5, "zinc": 0.1, "b12": 0.0, "folate": 4,
            "thiamine": 0.011, "riboflavin": 0.021, "niacin": 0.66,
        },
    },
    {
        "name": "Pears (can)",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 77.2, "carbs": 19.0, "fat": 0.1, "protein": 0.2,
            "sodium": 7, "cholesterol": 0, "fiber": 1.7,
            "vitamin_c": 2.1, "calcium": 8, "iron": 0.21, "potassium": 45,
            "magnesium": 4, "zinc": 0.1, "b12": 0.0, "folate": 2,
            "thiamine": 0.021, "riboflavin": 0.021, "niacin": 0.13,
        },
    },
    {
        "name": "Pineapple (can)",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 64.5, "carbs": 15.1, "fat": 0.1, "protein": 0.4,
            "sodium": 1, "cholesterol": 0, "fiber": 0.7,
            "vitamin_c": 10.7, "calcium": 11, "iron": 0.21, "potassium": 101,
            "magnesium": 15, "zinc": 0.1, "b12": 0.0, "folate": 7,
            "thiamine": 0.075, "riboflavin": 0.021, "niacin": 0.19,
        },
    },
    {
        "name": "Peaches, Dried",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 294.2, "carbs": 61.3, "fat": 0.8, "protein": 3.0,
            "sodium": 2, "cholesterol": 0, "fiber": 8.2,
            "vitamin_c": 2.0, "calcium": 59, "iron": 5.99, "potassium": 996,
            "magnesium": 42, "zinc": 0.5, "b12": 0.0, "folate": 0,
            "thiamine": 0.042, "riboflavin": 0.149, "niacin": 1.9,
        },
    },
    {
        "name": "Prunes, Dried",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 254.0, "carbs": 63.9, "fat": 0.4, "protein": 2.0,
            "sodium": 2, "cholesterol": 0, "fiber": 7.1,
            "vitamin_c": 5.1, "calcium": 50, "iron": 3.06, "potassium": 732,
            "magnesium": 41, "zinc": 0.4, "b12": 0.0, "folate": 4,
            "thiamine": 0.077, "riboflavin": 0.085, "niacin": 1.29,
        },
    },
    {
        "name": "Raisins, Dried",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 298.4, "carbs": 79.2, "fat": 0.5, "protein": 2.3,
            "sodium": 28, "cholesterol": 0, "fiber": 3.7,
            "vitamin_c": 3.0, "calcium": 55, "iron": 3.01, "potassium": 749,
            "magnesium": 35, "zinc": 0.2, "b12": 0.0, "folate": 5,
            "thiamine": 0.139, "riboflavin": 0.031, "niacin": 0.53,
        },
    },

    # --- Vegetables (Stigler) ---
    {
        "name": "Green Beans",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 37.6, "carbs": 7.0, "fat": 0.1, "protein": 2.2,
            "sodium": 6, "cholesterol": 0, "fiber": 2.7,
            "vitamin_c": 13.5, "calcium": 58, "iron": 1.25, "potassium": 209,
            "magnesium": 25, "zinc": 0.2, "b12": 0.0, "folate": 33,
            "thiamine": 0.067, "riboflavin": 0.091, "niacin": 0.58,
        },
    },
    {
        "name": "Cabbage",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 21.2, "carbs": 5.8, "fat": 0.1, "protein": 1.0,
            "sodium": 18, "cholesterol": 0, "fiber": 2.5,
            "vitamin_c": 43.8, "calcium": 33, "iron": 0.29, "potassium": 170,
            "magnesium": 12, "zinc": 0.2, "b12": 0.0, "folate": 43,
            "thiamine": 0.073, "riboflavin": 0.037, "niacin": 0.21,
        },
    },
    {
        "name": "Celery",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 19.3, "carbs": 3.0, "fat": 0.2, "protein": 1.1,
            "sodium": 80, "cholesterol": 0, "fiber": 1.6,
            "vitamin_c": 6.7, "calcium": 64, "iron": 0.49, "potassium": 260,
            "magnesium": 11, "zinc": 0.1, "b12": 0.0, "folate": 36,
            "thiamine": 0.03, "riboflavin": 0.03, "niacin": 0.19,
        },
    },
    {
        "name": "Lettuce",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 6.6, "carbs": 2.9, "fat": 0.1, "protein": 0.4,
            "sodium": 10, "cholesterol": 0, "fiber": 1.2,
            "vitamin_c": 7.4, "calcium": 18, "iron": 0.36, "potassium": 141,
            "magnesium": 7, "zinc": 0.2, "b12": 0.0, "folate": 29,
            "thiamine": 0.03, "riboflavin": 0.056, "niacin": 0.18,
        },
    },
    {
        "name": "Potatoes",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 71.5, "carbs": 15.7, "fat": 0.1, "protein": 1.7,
            "sodium": 6, "cholesterol": 0, "fiber": 2.4,
            "vitamin_c": 12.6, "calcium": 9, "iron": 0.59, "potassium": 421,
            "magnesium": 23, "zinc": 0.3, "b12": 0.0, "folate": 15,
            "thiamine": 0.147, "riboflavin": 0.035, "niacin": 0.99,
        },
    },
    {
        "name": "Asparagus (can)",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 18.6, "carbs": 2.6, "fat": 0.8, "protein": 1.5,
            "sodium": 286, "cholesterol": 0, "fiber": 1.5,
            "vitamin_c": 12.7, "calcium": 14, "iron": 0.56, "potassium": 183,
            "magnesium": 12, "zinc": 0.5, "b12": 0.0, "folate": 88,
            "thiamine": 0.065, "riboflavin": 0.098, "niacin": 0.79,
        },
    },
    {
        "name": "Green Beans (can)",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 16.8, "carbs": 4.4, "fat": 0.1, "protein": 0.9,
            "sodium": 270, "cholesterol": 0, "fiber": 1.6,
            "vitamin_c": 7.2, "calcium": 34, "iron": 1.09, "potassium": 95,
            "magnesium": 13, "zinc": 0.2, "b12": 0.0, "folate": 21,
            "thiamine": 0.027, "riboflavin": 0.072, "niacin": 0.54,
        },
    },
    {
        "name": "Corn (can)",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 90.9, "carbs": 16.9, "fat": 1.2, "protein": 2.4,
            "sodium": 200, "cholesterol": 0, "fiber": 1.8,
            "vitamin_c": 3.8, "calcium": 3, "iron": 0.28, "potassium": 161,
            "magnesium": 22, "zinc": 0.5, "b12": 0.0, "folate": 26,
            "thiamine": 0.028, "riboflavin": 0.047, "niacin": 0.73,
        },
    },
    {
        "name": "Peas (can)",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 53.3, "carbs": 11.2, "fat": 0.4, "protein": 3.2,
            "sodium": 278, "cholesterol": 0, "fiber": 3.6,
            "vitamin_c": 8.6, "calcium": 14, "iron": 1.04, "potassium": 82,
            "magnesium": 18, "zinc": 0.8, "b12": 0.0, "folate": 31,
            "thiamine": 0.114, "riboflavin": 0.058, "niacin": 0.86,
        },
    },
    {
        "name": "Tomatoes (can)",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 18.8, "carbs": 4.1, "fat": 0.3, "protein": 0.9,
            "sodium": 167, "cholesterol": 0, "fiber": 1.5,
            "vitamin_c": 18.1, "calcium": 10, "iron": 0.55, "potassium": 220,
            "magnesium": 14, "zinc": 0.2, "b12": 0.0, "folate": 12,
            "thiamine": 0.049, "riboflavin": 0.036, "niacin": 0.52,
        },
    },
    {
        "name": "Tomato Soup (can)",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 40.8, "carbs": 15.8, "fat": 0.8, "protein": 1.8,
            "sodium": 679, "cholesterol": 0, "fiber": 0.7,
            "vitamin_c": 22.0, "calcium": 15, "iron": 1.1, "potassium": 220,
            "magnesium": 9, "zinc": 0.3, "b12": 0.0, "folate": 9,
            "thiamine": 0.089, "riboflavin": 0.061, "niacin": 1.71,
        },
    },

    # --- Legumes (Stigler) ---
    {
        "name": "Pork and Beans (can)",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 117.4, "carbs": 19.4, "fat": 1.8, "protein": 5.7,
            "sodium": 422, "cholesterol": 9, "fiber": 5.5,
            "vitamin_c": 0.0, "calcium": 63, "iron": 2.1, "potassium": 296,
            "magnesium": 36, "zinc": 1.1, "b12": 0.0, "folate": 15,
            "thiamine": 0.13, "riboflavin": 0.121, "niacin": 0.88,
        },
    },
    {
        "name": "Peas, Dried",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 348.3, "carbs": 60.0, "fat": 1.0, "protein": 23.8,
            "sodium": 15, "cholesterol": 0, "fiber": 25.5,
            "vitamin_c": 0.0, "calcium": 73, "iron": 6.01, "potassium": 981,
            "magnesium": 115, "zinc": 3.0, "b12": 0.0, "folate": 274,
            "thiamine": 0.5, "riboflavin": 0.32, "niacin": 2.82,
        },
    },
    {
        "name": "Lima Beans, Dried",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 341.4, "carbs": 63.4, "fat": 0.7, "protein": 20.7,
            "sodium": 18, "cholesterol": 0, "fiber": 19.0,
            "vitamin_c": 0.0, "calcium": 73, "iron": 9.01, "potassium": 1724,
            "magnesium": 224, "zinc": 2.8, "b12": 0.0, "folate": 395,
            "thiamine": 0.528, "riboflavin": 0.75, "niacin": 1.82,
        },
    },
    {
        "name": "Navy Beans, Dried",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 349.9, "carbs": 60.8, "fat": 1.5, "protein": 22.0,
            "sodium": 5, "cholesterol": 0, "fiber": 24.4,
            "vitamin_c": 0.0, "calcium": 148, "iron": 10.3, "potassium": 1185,
            "magnesium": 175, "zinc": 3.7, "b12": 0.0, "folate": 364,
            "thiamine": 0.499, "riboflavin": 0.32, "niacin": 2.82,
        },
    },

    # --- Miscellaneous (Stigler) ---
    # Coffee and Tea: Stigler-derived nutrient values are per brewed beverage
    # (0 kcal/100g confirms this). USDA values below are likewise for brewed.
    {
        "name": "Coffee",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 0.0, "carbs": 0.0, "fat": 0.0, "protein": 0.0,
            "sodium": 2, "cholesterol": 0, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 0, "iron": 0.0, "potassium": 49,
            "magnesium": 3, "zinc": 0.0, "b12": 0.0, "folate": 2,
            "thiamine": 0.198, "riboflavin": 0.252, "niacin": 2.47,
        },
    },
    {
        "name": "Tea",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 0.0, "carbs": 0.2, "fat": 0.0, "protein": 0.0,
            "sodium": 1, "cholesterol": 0, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 0, "iron": 0.0, "potassium": 37,
            "magnesium": 3, "zinc": 0.0, "b12": 0.0, "folate": 5,
            "thiamine": 0.0, "riboflavin": 0.353, "niacin": 6.44,
        },
    },
    {
        "name": "Cocoa",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 329.9, "carbs": 57.9, "fat": 13.7, "protein": 9.0,
            "sodium": 21, "cholesterol": 0, "fiber": 37.0,
            "vitamin_c": 0.0, "calcium": 114, "iron": 2.73, "potassium": 1524,
            "magnesium": 499, "zinc": 6.8, "b12": 0.0, "folate": 32,
            "thiamine": 0.076, "riboflavin": 0.451, "niacin": 1.52,
        },
    },
    {
        "name": "Chocolate",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 571.4, "carbs": 45.9, "fat": 42.6, "protein": 5.5,
            "sodium": 20, "cholesterol": 0, "fiber": 10.9,
            "vitamin_c": 0.0, "calcium": 93, "iron": 2.79, "potassium": 715,
            "magnesium": 228, "zinc": 3.3, "b12": 0.0, "folate": 8,
            "thiamine": 0.064, "riboflavin": 0.243, "niacin": 1.0,
        },
    },
    {
        "name": "Sugar",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 397.8, "carbs": 99.9, "fat": 0.0, "protein": 0.0,
            "sodium": 1, "cholesterol": 0, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 0, "iron": 0.0, "potassium": 2,
            "magnesium": 0, "zinc": 0.0, "b12": 0.0, "folate": 0,
            "thiamine": 0.0, "riboflavin": 0.0, "niacin": 0.0,
        },
    },
    {
        "name": "Corn Syrup",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 296.0, "carbs": 76.8, "fat": 0.0, "protein": 0.0,
            "sodium": 67, "cholesterol": 0, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 10, "iron": 1.49, "potassium": 6,
            "magnesium": 1, "zinc": 0.0, "b12": 0.0, "folate": 0,
            "thiamine": 0.0, "riboflavin": 0.0, "niacin": 0.1,
        },
    },
    {
        "name": "Molasses",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 239.9, "carbs": 74.7, "fat": 0.1, "protein": 0.0,
            "sodium": 37, "cholesterol": 0, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 275, "iron": 6.5, "potassium": 1464,
            "magnesium": 242, "zinc": 0.3, "b12": 0.0, "folate": 0,
            "thiamine": 0.051, "riboflavin": 0.2, "niacin": 3.89,
        },
    },
    {
        "name": "Strawberry Preserves",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 289.2, "carbs": 65.1, "fat": 0.1, "protein": 0.5,
            "sodium": 32, "cholesterol": 0, "fiber": 0.6,
            "vitamin_c": 0.0, "calcium": 18, "iron": 0.32, "potassium": 77,
            "magnesium": 5, "zinc": 0.1, "b12": 0.0, "folate": 5,
            "thiamine": 0.009, "riboflavin": 0.018, "niacin": 0.14,
        },
    },

    # --- Additional entries (USDA FoodData Central SR Legacy) -----------------
    # Nutrient values per 100g. Sources: USDA FoodData Central SR Legacy.

    # --- Proteins ---
    {
        "name": "Chicken breast, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 120, "carbs": 0, "fat": 2.6, "protein": 22.5,
            "sodium": 74, "cholesterol": 73, "fiber": 0,
            "vitamin_c": 0, "calcium": 11, "iron": 0.7, "potassium": 356,
            "magnesium": 29, "zinc": 0.9, "b12": 0.3, "folate": 4,
            "thiamine": 0.07, "riboflavin": 0.11, "niacin": 13.7,
        },
    },
    {
        "name": "Salmon, Atlantic, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 208, "carbs": 0, "fat": 13.4, "protein": 20.4,
            "sodium": 59, "cholesterol": 63, "fiber": 0,
            "vitamin_c": 0, "calcium": 12, "iron": 0.8, "potassium": 363,
            "magnesium": 29, "zinc": 0.6, "b12": 3.2, "folate": 25,
            "thiamine": 0.23, "riboflavin": 0.38, "niacin": 7.9,
        },
    },
    {
        "name": "Tuna, canned in water",
        "unit": "100g",
        "grams": 100,
        "max_amount": 85,  # ~1 can, 3x/week mercury limit
        "nutrients": {
            "calories": 116, "carbs": 0, "fat": 2.6, "protein": 25.5,
            "sodium": 396, "cholesterol": 46, "fiber": 0,
            "vitamin_c": 0, "calcium": 11, "iron": 1.3, "potassium": 237,
            "magnesium": 35, "zinc": 0.9, "b12": 2.5, "folate": 4,
            "thiamine": 0.03, "riboflavin": 0.1, "niacin": 13.3,
        },
    },
    {
        "name": "Eggs, whole, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 143, "carbs": 0.7, "fat": 9.5, "protein": 12.6,
            "sodium": 142, "cholesterol": 372, "fiber": 0,
            "vitamin_c": 0, "calcium": 56, "iron": 1.8, "potassium": 138,
            "magnesium": 12, "zinc": 1.3, "b12": 0.9, "folate": 47,
            "thiamine": 0.04, "riboflavin": 0.46, "niacin": 0.1,
        },
    },
    {
        "name": "Ground beef, 90% lean, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 176, "carbs": 0, "fat": 10.0, "protein": 20.0,
            "sodium": 72, "cholesterol": 70, "fiber": 0,
            "vitamin_c": 0, "calcium": 18, "iron": 2.2, "potassium": 318,
            "magnesium": 21, "zinc": 4.8, "b12": 2.3, "folate": 9,
            "thiamine": 0.05, "riboflavin": 0.18, "niacin": 5.1,
        },
    },
    {
        "name": "Tofu, firm, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 76, "carbs": 1.9, "fat": 4.3, "protein": 8.1,
            "sodium": 7, "cholesterol": 0, "fiber": 0.3,
            "vitamin_c": 0.1, "calcium": 350, "iron": 1.6, "potassium": 121,
            "magnesium": 30, "zinc": 0.8, "b12": 0, "folate": 15,
            "thiamine": 0.08, "riboflavin": 0.05, "niacin": 0.2,
        },
    },
    {
        "name": "Greek yogurt, plain, nonfat",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 59, "carbs": 3.6, "fat": 0.4, "protein": 10.2,
            "sodium": 36, "cholesterol": 5, "fiber": 0,
            "vitamin_c": 0, "calcium": 110, "iron": 0.1, "potassium": 141,
            "magnesium": 11, "zinc": 0.5, "b12": 0.4, "folate": 7,
            "thiamine": 0.02, "riboflavin": 0.18, "niacin": 0.2,
        },
    },
    {
        "name": "Cottage cheese, lowfat 1%",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 72, "carbs": 2.7, "fat": 1.0, "protein": 12.4,
            "sodium": 372, "cholesterol": 7, "fiber": 0,
            "vitamin_c": 0, "calcium": 86, "iron": 0.1, "potassium": 84,
            "magnesium": 11, "zinc": 0.4, "b12": 0.4, "folate": 12,
            "thiamine": 0.02, "riboflavin": 0.16, "niacin": 0.1,
        },
    },
    {
        "name": "Lentils, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 352, "carbs": 60.1, "fat": 1.1, "protein": 25.8,
            "sodium": 6, "cholesterol": 0, "fiber": 10.7,
            "vitamin_c": 4.4, "calcium": 56, "iron": 7.5, "potassium": 677,
            "magnesium": 122, "zinc": 3.3, "b12": 0, "folate": 479,
            "thiamine": 0.87, "riboflavin": 0.21, "niacin": 2.6,
        },
    },
    {
        "name": "Black beans, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 341, "carbs": 62.4, "fat": 1.4, "protein": 21.6,
            "sodium": 5, "cholesterol": 0, "fiber": 15.5,
            "vitamin_c": 0, "calcium": 123, "iron": 5.0, "potassium": 1483,
            "magnesium": 171, "zinc": 3.7, "b12": 0, "folate": 444,
            "thiamine": 0.9, "riboflavin": 0.19, "niacin": 1.9,
        },
    },

    # --- Vegetables ---
    {
        "name": "Spinach, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 23, "carbs": 3.6, "fat": 0.4, "protein": 2.9,
            "sodium": 79, "cholesterol": 0, "fiber": 2.2,
            "vitamin_c": 28.1, "calcium": 99, "iron": 2.7, "potassium": 558,
            "magnesium": 79, "zinc": 0.5, "b12": 0, "folate": 194,
            "thiamine": 0.08, "riboflavin": 0.19, "niacin": 0.7,
        },
    },
    {
        "name": "Broccoli, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 34, "carbs": 6.6, "fat": 0.4, "protein": 2.8,
            "sodium": 33, "cholesterol": 0, "fiber": 2.6,
            "vitamin_c": 89.2, "calcium": 47, "iron": 0.7, "potassium": 316,
            "magnesium": 21, "zinc": 0.4, "b12": 0, "folate": 63,
            "thiamine": 0.07, "riboflavin": 0.12, "niacin": 0.6,
        },
    },
    {
        "name": "Kale, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 49, "carbs": 8.8, "fat": 0.9, "protein": 4.3,
            "sodium": 38, "cholesterol": 0, "fiber": 3.6,
            "vitamin_c": 120, "calcium": 150, "iron": 1.5, "potassium": 491,
            "magnesium": 47, "zinc": 0.6, "b12": 0, "folate": 141,
            "thiamine": 0.11, "riboflavin": 0.13, "niacin": 1.0,
        },
    },
    {
        "name": "Sweet potato, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 86, "carbs": 20.1, "fat": 0.1, "protein": 1.6,
            "sodium": 55, "cholesterol": 0, "fiber": 3.0,
            "vitamin_c": 2.4, "calcium": 30, "iron": 0.6, "potassium": 337,
            "magnesium": 25, "zinc": 0.3, "b12": 0, "folate": 11,
            "thiamine": 0.08, "riboflavin": 0.06, "niacin": 0.6,
        },
    },
    {
        "name": "Bell pepper, red, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 31, "carbs": 6.0, "fat": 0.3, "protein": 1.0,
            "sodium": 4, "cholesterol": 0, "fiber": 2.1,
            "vitamin_c": 127.7, "calcium": 7, "iron": 0.4, "potassium": 211,
            "magnesium": 12, "zinc": 0.3, "b12": 0, "folate": 46,
            "thiamine": 0.05, "riboflavin": 0.09, "niacin": 1.0,
        },
    },
    {
        "name": "Carrots, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 41, "carbs": 9.6, "fat": 0.2, "protein": 0.9,
            "sodium": 69, "cholesterol": 0, "fiber": 2.8,
            "vitamin_c": 5.9, "calcium": 33, "iron": 0.3, "potassium": 320,
            "magnesium": 12, "zinc": 0.2, "b12": 0, "folate": 19,
            "thiamine": 0.07, "riboflavin": 0.06, "niacin": 1.0,
        },
    },
    {
        "name": "Cauliflower, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 25, "carbs": 5.0, "fat": 0.1, "protein": 1.9,
            "sodium": 30, "cholesterol": 0, "fiber": 2.0,
            "vitamin_c": 48.2, "calcium": 22, "iron": 0.4, "potassium": 299,
            "magnesium": 15, "zinc": 0.3, "b12": 0, "folate": 57,
            "thiamine": 0.05, "riboflavin": 0.06, "niacin": 0.5,
        },
    },
    {
        "name": "Tomatoes, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 18, "carbs": 3.9, "fat": 0.2, "protein": 0.9,
            "sodium": 5, "cholesterol": 0, "fiber": 1.2,
            "vitamin_c": 13.7, "calcium": 10, "iron": 0.3, "potassium": 237,
            "magnesium": 11, "zinc": 0.2, "b12": 0, "folate": 15,
            "thiamine": 0.04, "riboflavin": 0.02, "niacin": 0.6,
        },
    },
    {
        "name": "Onion, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 40, "carbs": 9.3, "fat": 0.1, "protein": 1.1,
            "sodium": 4, "cholesterol": 0, "fiber": 1.7,
            "vitamin_c": 7.4, "calcium": 23, "iron": 0.2, "potassium": 146,
            "magnesium": 10, "zinc": 0.2, "b12": 0, "folate": 19,
            "thiamine": 0.05, "riboflavin": 0.03, "niacin": 0.1,
        },
    },
    {
        "name": "Mushrooms, white, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 22, "carbs": 3.3, "fat": 0.3, "protein": 3.1,
            "sodium": 5, "cholesterol": 0, "fiber": 1.0,
            "vitamin_c": 2.1, "calcium": 3, "iron": 0.5, "potassium": 318,
            "magnesium": 9, "zinc": 0.5, "b12": 0.04, "folate": 17,
            "thiamine": 0.08, "riboflavin": 0.4, "niacin": 3.6,
        },
    },

    # --- Fruits ---
    {
        "name": "Blueberries, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 57, "carbs": 14.5, "fat": 0.3, "protein": 0.7,
            "sodium": 1, "cholesterol": 0, "fiber": 2.4,
            "vitamin_c": 9.7, "calcium": 6, "iron": 0.3, "potassium": 77,
            "magnesium": 6, "zinc": 0.2, "b12": 0, "folate": 6,
            "thiamine": 0.04, "riboflavin": 0.04, "niacin": 0.4,
        },
    },
    {
        "name": "Banana, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 89, "carbs": 22.8, "fat": 0.3, "protein": 1.1,
            "sodium": 1, "cholesterol": 0, "fiber": 2.6,
            "vitamin_c": 8.7, "calcium": 5, "iron": 0.3, "potassium": 358,
            "magnesium": 27, "zinc": 0.2, "b12": 0, "folate": 20,
            "thiamine": 0.03, "riboflavin": 0.07, "niacin": 0.7,
        },
    },
    {
        "name": "Apple, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 52, "carbs": 13.8, "fat": 0.2, "protein": 0.3,
            "sodium": 1, "cholesterol": 0, "fiber": 2.4,
            "vitamin_c": 4.6, "calcium": 6, "iron": 0.1, "potassium": 107,
            "magnesium": 5, "zinc": 0.0, "b12": 0, "folate": 3,
            "thiamine": 0.02, "riboflavin": 0.03, "niacin": 0.1,
        },
    },
    {
        "name": "Orange, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 47, "carbs": 11.8, "fat": 0.1, "protein": 0.9,
            "sodium": 0, "cholesterol": 0, "fiber": 2.4,
            "vitamin_c": 53.2, "calcium": 40, "iron": 0.1, "potassium": 181,
            "magnesium": 10, "zinc": 0.1, "b12": 0, "folate": 30,
            "thiamine": 0.09, "riboflavin": 0.04, "niacin": 0.3,
        },
    },

    # --- Grains ---
    {
        "name": "Oats, rolled, dry",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 389, "carbs": 66.3, "fat": 6.9, "protein": 16.9,
            "sodium": 2, "cholesterol": 0, "fiber": 10.6,
            "vitamin_c": 0, "calcium": 54, "iron": 4.7, "potassium": 429,
            "magnesium": 177, "zinc": 4.0, "b12": 0, "folate": 56,
            "thiamine": 0.76, "riboflavin": 0.14, "niacin": 1.1,
        },
    },
    {
        "name": "Brown rice, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 370, "carbs": 77.2, "fat": 2.7, "protein": 7.9,
            "sodium": 7, "cholesterol": 0, "fiber": 3.5,
            "vitamin_c": 0, "calcium": 33, "iron": 1.8, "potassium": 268,
            "magnesium": 143, "zinc": 2.0, "b12": 0, "folate": 20,
            "thiamine": 0.4, "riboflavin": 0.09, "niacin": 5.1,
        },
    },
    {
        "name": "Quinoa, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 368, "carbs": 64.2, "fat": 6.1, "protein": 14.1,
            "sodium": 5, "cholesterol": 0, "fiber": 7.0,
            "vitamin_c": 0, "calcium": 47, "iron": 4.6, "potassium": 563,
            "magnesium": 197, "zinc": 3.1, "b12": 0, "folate": 184,
            "thiamine": 0.36, "riboflavin": 0.32, "niacin": 1.5,
        },
    },

    # --- Dairy & Fats ---
    {
        "name": "Milk, whole",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 61, "carbs": 4.8, "fat": 3.3, "protein": 3.2,
            "sodium": 43, "cholesterol": 10, "fiber": 0,
            "vitamin_c": 0, "calcium": 113, "iron": 0.0, "potassium": 132,
            "magnesium": 10, "zinc": 0.4, "b12": 0.4, "folate": 5,
            "thiamine": 0.04, "riboflavin": 0.18, "niacin": 0.1,
        },
    },
    {
        "name": "Cheddar cheese",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 403, "carbs": 1.3, "fat": 33.1, "protein": 24.9,
            "sodium": 621, "cholesterol": 105, "fiber": 0,
            "vitamin_c": 0, "calcium": 721, "iron": 0.7, "potassium": 98,
            "magnesium": 28, "zinc": 3.1, "b12": 0.8, "folate": 18,
            "thiamine": 0.03, "riboflavin": 0.43, "niacin": 0.1,
        },
    },
    {
        "name": "Olive oil",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 884, "carbs": 0, "fat": 100.0, "protein": 0,
            "sodium": 2, "cholesterol": 0, "fiber": 0,
            "vitamin_c": 0, "calcium": 1, "iron": 0.6, "potassium": 1,
            "magnesium": 0, "zinc": 0, "b12": 0, "folate": 0,
            "thiamine": 0, "riboflavin": 0, "niacin": 0,
        },
    },
    {
        "name": "Avocado, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 160, "carbs": 8.5, "fat": 14.7, "protein": 2.0,
            "sodium": 7, "cholesterol": 0, "fiber": 6.7,
            "vitamin_c": 10.0, "calcium": 12, "iron": 0.6, "potassium": 485,
            "magnesium": 29, "zinc": 0.6, "b12": 0, "folate": 81,
            "thiamine": 0.07, "riboflavin": 0.13, "niacin": 1.7,
        },
    },
    {
        "name": "Almonds, raw",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 579, "carbs": 21.6, "fat": 49.9, "protein": 21.2,
            "sodium": 1, "cholesterol": 0, "fiber": 12.5,
            "vitamin_c": 0, "calcium": 264, "iron": 3.7, "potassium": 733,
            "magnesium": 270, "zinc": 3.1, "b12": 0, "folate": 44,
            "thiamine": 0.21, "riboflavin": 1.14, "niacin": 3.6,
        },
    },
    {
        "name": "Peanut butter, unsalted",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 588, "carbs": 20.0, "fat": 50.4, "protein": 25.1,
            "sodium": 17, "cholesterol": 0, "fiber": 6.0,
            "vitamin_c": 0, "calcium": 49, "iron": 1.7, "potassium": 558,
            "magnesium": 154, "zinc": 2.9, "b12": 0, "folate": 87,
            "thiamine": 0.15, "riboflavin": 0.19, "niacin": 13.7,
        },
    },
]


# ------------------------------------------------------------------------------
# RECIPES
# Nutrient values per 1 serving.
# The solver variable represents number of servings.
# ------------------------------------------------------------------------------

RECIPES = [
    {
        "name": "Lentil vegetable soup (1 serving ~400g)",
        "unit": "1 serving",
        "grams": 400,  # informational only for recipes
        "nutrients": {
            "calories": 220, "carbs": 38.0, "fat": 3.5, "protein": 13.0,
            "sodium": 480, "cholesterol": 0, "fiber": 9.5,
            "vitamin_c": 18.0, "calcium": 72, "iron": 4.2, "potassium": 680,
            "magnesium": 68, "zinc": 2.0, "b12": 0, "folate": 210,
            "thiamine": 0.35, "riboflavin": 0.14, "niacin": 2.2,
        },
    },
    {
        "name": "Chicken and brown rice bowl (1 serving ~350g)",
        "unit": "1 serving",
        "grams": 350,
        "nutrients": {
            "calories": 410, "carbs": 45.0, "fat": 8.0, "protein": 38.0,
            "sodium": 320, "cholesterol": 95, "fiber": 3.0,
            "vitamin_c": 5.0, "calcium": 40, "iron": 2.0, "potassium": 520,
            "magnesium": 60, "zinc": 3.2, "b12": 0.5, "folate": 28,
            "thiamine": 0.25, "riboflavin": 0.22, "niacin": 14.0,
        },
    },
    {
        "name": "Salmon with roasted vegetables (1 serving ~300g)",
        "unit": "1 serving",
        "grams": 300,
        "nutrients": {
            "calories": 380, "carbs": 14.0, "fat": 20.0, "protein": 36.0,
            "sodium": 290, "cholesterol": 85, "fiber": 4.5,
            "vitamin_c": 55.0, "calcium": 65, "iron": 1.8, "potassium": 890,
            "magnesium": 72, "zinc": 1.4, "b12": 3.8, "folate": 88,
            "thiamine": 0.35, "riboflavin": 0.52, "niacin": 10.5,
        },
    },
    {
        "name": "Greek yogurt parfait with berries (1 serving ~250g)",
        "unit": "1 serving",
        "grams": 250,
        "nutrients": {
            "calories": 215, "carbs": 28.0, "fat": 2.5, "protein": 20.0,
            "sodium": 75, "cholesterol": 10, "fiber": 3.5,
            "vitamin_c": 14.0, "calcium": 240, "iron": 0.5, "potassium": 380,
            "magnesium": 30, "zinc": 1.2, "b12": 0.8, "folate": 22,
            "thiamine": 0.06, "riboflavin": 0.38, "niacin": 0.4,
        },
    },
    {
        "name": "Black bean and vegetable stir-fry (1 serving ~300g)",
        "unit": "1 serving",
        "grams": 300,
        "nutrients": {
            "calories": 290, "carbs": 42.0, "fat": 7.0, "protein": 14.0,
            "sodium": 380, "cholesterol": 0, "fiber": 11.0,
            "vitamin_c": 62.0, "calcium": 95, "iron": 3.8, "potassium": 720,
            "magnesium": 90, "zinc": 2.2, "b12": 0, "folate": 195,
            "thiamine": 0.38, "riboflavin": 0.16, "niacin": 2.0,
        },
    },
]
