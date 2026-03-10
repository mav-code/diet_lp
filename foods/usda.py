"""
diet_lp/foods/usda.py

Additional ingredients from USDA FoodData Central SR Legacy.
Nutrient values per 100g.
"""

INGREDIENTS = [

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
