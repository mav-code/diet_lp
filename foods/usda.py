"""
diet_lp/foods/usda.py

Additional ingredients from USDA FoodData Central SR Legacy.
Nutrient values per 100g.
"""

INGREDIENTS = [

    # --- Proteins ---
    {
        "name": "Chicken breast, skinless, boneless, raw",
        # USDA: Chicken, broiler or fryers, breast, skinless, boneless, meat only, raw (FDC 171077)
        "link": "https://fdc.nal.usda.gov/food-details/171077/nutrients",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 120.0, "carbs": 0.0, "fat": 2.62, "protein": 22.5,
            "sodium": 45.0, "cholesterol": 73.0, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 5.0, "iron": 0.37, "potassium": 334.0,
            "magnesium": 28.0, "zinc": 0.68, "b12": 0.21, "folate": 9.0,
            "thiamine": 0.094, "riboflavin": 0.177, "niacin": 9.6,
        },
    },
    {
        "name": "Salmon, Atlantic, farmed, raw",
        # USDA: Fish, salmon, Atlantic, farmed, raw (FDC 175167)
        "link": "https://fdc.nal.usda.gov/food-details/175167/nutrients",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 208.0, "carbs": 0.0, "fat": 13.42, "protein": 20.42,
            "sodium": 59.0, "cholesterol": 55.0, "fiber": 0.0,
            "vitamin_c": 3.9, "calcium": 9.0, "iron": 0.34, "potassium": 363.0,
            "magnesium": 27.0, "zinc": 0.36, "b12": 3.23, "folate": 26.0,
            "thiamine": 0.207, "riboflavin": 0.155, "niacin": 8.672,
        },
    },
    {
        "name": "Tuna, light, canned in water, drained",
        # USDA: Fish, tuna, light, canned in water, drained solids (Includes foods for USDA's Food Distribution Program) (FDC 173709)
        "link": "https://fdc.nal.usda.gov/food-details/173709/nutrients",
        "unit": "100g",
        "grams": 100,
        "max_amount": 85,  # ~1 can, 3x/week mercury limit
        "nutrients": {
            "calories": 86.0, "carbs": 0.0, "fat": 0.96, "protein": 19.44,
            "sodium": 247.0, "cholesterol": 36.0, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 17.0, "iron": 1.63, "potassium": 179.0,
            "magnesium": 23.0, "zinc": 0.69, "b12": 2.55, "folate": 4.0,
            "thiamine": 0.03, "riboflavin": 0.084, "niacin": 10.136,
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
        "name": "Tofu, regular, raw",
        # USDA: Tofu, raw, regular, prepared with calcium sulfate (FDC 172476)
        "link": "https://fdc.nal.usda.gov/food-details/172476/nutrients",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 76.0, "carbs": 1.87, "fat": 4.78, "protein": 8.08,
            "sodium": 7.0, "cholesterol": 0.0, "fiber": 0.3,
            "vitamin_c": 0.1, "calcium": 350.0, "iron": 5.36, "potassium": 121.0,
            "magnesium": 30.0, "zinc": 0.8, "b12": 0.0, "folate": 15.0,
            "thiamine": 0.081, "riboflavin": 0.052, "niacin": 0.195,
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
        # USDA: Cheese, cottage, lowfat, 1% milkfat (FDC 173417)
        "link": "https://fdc.nal.usda.gov/food-details/173417/nutrients",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 72.0, "carbs": 2.72, "fat": 1.02, "protein": 12.39,
            "sodium": 406.0, "cholesterol": 4.0, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 61.0, "iron": 0.14, "potassium": 86.0,
            "magnesium": 5.0, "zinc": 0.38, "b12": 0.63, "folate": 12.0,
            "thiamine": 0.021, "riboflavin": 0.165, "niacin": 0.128,
        },
    },
    {
        "name": "Lentils, raw",
        # USDA: Lentils, raw (FDC 172420)
        "link": "https://fdc.nal.usda.gov/food-details/172420/nutrients",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 352.0, "carbs": 63.35, "fat": 1.06, "protein": 24.63,
            "sodium": 6.0, "cholesterol": 0.0, "fiber": 10.7,
            "vitamin_c": 4.5, "calcium": 35.0, "iron": 6.51, "potassium": 677.0,
            "magnesium": 47.0, "zinc": 3.27, "b12": 0.0, "folate": 479.0,
            "thiamine": 0.873, "riboflavin": 0.211, "niacin": 2.605,
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
        # USDA: Kale, raw (FDC 168421)
        "link": "https://fdc.nal.usda.gov/food-details/168421/nutrients",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 35.0, "carbs": 4.42, "fat": 1.49, "protein": 2.92,
            "sodium": 53.0, "cholesterol": 0.0, "fiber": 4.1,
            "vitamin_c": 93.4, "calcium": 254.0, "iron": 1.6, "potassium": 348.0,
            "magnesium": 33.0, "zinc": 0.39, "b12": 0.0, "folate": 62.0,
            "thiamine": 0.113, "riboflavin": 0.347, "niacin": 1.18,
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

    # --- Grains ---
    {
        "name": "Brown rice, medium-grain, raw",
        # USDA: Rice, brown, medium-grain, raw (Includes foods for USDA's Food Distribution Program) (FDC 169706)
        "link": "https://fdc.nal.usda.gov/food-details/169706/nutrients",
        "unit": "100g",
        "grams": 100,
        "nutrients": {
            "calories": 362.0, "carbs": 76.17, "fat": 2.68, "protein": 7.5,
            "sodium": 4.0, "cholesterol": 0.0, "fiber": 3.4,
            "vitamin_c": 0.0, "calcium": 33.0, "iron": 1.8, "potassium": 268.0,
            "magnesium": 143.0, "zinc": 2.02, "b12": 0.0, "folate": 20.0,
            "thiamine": 0.413, "riboflavin": 0.043, "niacin": 4.308,
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
    # Disabled: unrealistic ingredient. Home-cooking dry lupins means soaking
    # them for ~5-14 days with daily water changes to remove toxic alkaloids.
    # For the practical version, see the brined lupini in local_example.py.
    # {
    #     "name": 'Lupins, mature seeds, cooked, boiled, with salt', "unit": "100g", "grams": 100,
    #     "link": 'https://fdc.nal.usda.gov/food-details/173804/nutrients',
    #     "nutrients": {
    #         "calories": 116.0,
    #         "carbs": 9.29,
    #         "fat": 2.92,
    #         "protein": 15.57,
    #         "sodium": 240.0,
    #         "cholesterol": 0.0,
    #         "fiber": 2.8,
    #         "vitamin_c": 1.1,
    #         "calcium": 51.0,
    #         "iron": 1.2,
    #         "potassium": 245.0,
    #         "magnesium": 54.0,
    #         "zinc": 1.38,
    #         "b12": 0.0,
    #         "folate": 59.0,
    #         "thiamine": 0.134,
    #         "riboflavin": 0.053,
    #         "niacin": 0.495,
    #     },
    # },
    # {
    #     "name": 'Lupins, mature seeds, cooked, boiled, without salt', "unit": "100g", "grams": 100,
    #     "link": 'https://fdc.nal.usda.gov/food-details/172424/nutrients',
    #     "nutrients": {
    #         "calories": 119.0,
    #         "carbs": 9.88,
    #         "fat": 2.92,
    #         "protein": 15.57,
    #         "sodium": 4.0,
    #         "cholesterol": 0.0,
    #         "fiber": 2.8,
    #         "vitamin_c": 1.1,
    #         "calcium": 51.0,
    #         "iron": 1.2,
    #         "potassium": 245.0,
    #         "magnesium": 54.0,
    #         "zinc": 1.38,
    #         "b12": 0.0,
    #         "folate": 59.0,
    #         "thiamine": 0.134,
    #         "riboflavin": 0.053,
    #         "niacin": 0.495,
    #     },
    # },
    {
        "name": 'Beverages, Coconut water, ready-to-drink, unsweetened', "unit": "100g", "grams": 100,
        "link": 'https://fdc.nal.usda.gov/food-details/174831/nutrients',
        "nutrients": {
            "calories": 18.0,
            "carbs": 4.24,
            "fat": 0.0,
            "protein": 0.22,
            "sodium": 26.0,
            "cholesterol": 0.0,
            "fiber": 0.0,
            "vitamin_c": 9.9,
            "calcium": 7.0,
            "iron": 0.03,
            "potassium": 165.0,
            "magnesium": 6.0,
            "zinc": 0.02,
            "b12": 0.0,
            "folate": 0.0,
            "thiamine": 0.03,
            "riboflavin": 0.0,
            "niacin": 0.0,
        },
    },
    {
        "name": 'Nuts, coconut water (liquid from coconuts)', "unit": "100g", "grams": 100,
        "link": 'https://fdc.nal.usda.gov/food-details/170174/nutrients',
        "nutrients": {
            "calories": 19.0,
            "carbs": 3.71,
            "fat": 0.2,
            "protein": 0.72,
            "sodium": 105.0,
            "cholesterol": 0.0,
            "fiber": 1.1,
            "vitamin_c": 2.4,
            "calcium": 24.0,
            "iron": 0.29,
            "potassium": 250.0,
            "magnesium": 25.0,
            "zinc": 0.1,
            "b12": 0.0,
            "folate": 3.0,
            "thiamine": 0.03,
            "riboflavin": 0.057,
            "niacin": 0.08,
        },
    },
]
