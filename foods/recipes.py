"""
diet_lp/foods/recipes.py

Example recipes — nutrient values per 1 serving.
The solver variable for recipes is number of servings.
"""

RECIPES = [
    {
        "name": "Lentil vegetable soup (1 serving ~400g)",
        "unit": "1 serving",
        "grams": 400,
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
