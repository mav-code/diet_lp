"""
diet_lp/foods/stigler.py

Stigler (1945) commodity set — 77 ingredients.

The food list is the one from George Stigler's 1945 diet problem (as used in
https://developers.google.com/optimization/lp/stigler_diet). The nutrient
values are not Stigler's: every value comes from USDA FoodData Central
SR Legacy, per 100g, and each entry links to its FDC record.

Foods are matched in their as-purchased form, like Stigler's commodities:
raw meat and produce, dry grains and legumes, canned goods as packed
(solids and liquids unless noted). Judgment calls on ambiguous 1939 items:
  - "Chocolate" is unsweetened baking chocolate (sold in 8-oz packages then).
  - "Plate (beef)" is plate short ribs, the fatty cut "plate" meant.
  - "Roasting Chicken" is whole bird as sold: meat, skin, giblets, neck.
  - "Peanut Butter" is ordinary salted peanut butter.
Coffee and Tea are brewed beverages (100ml ≈ 100g).
"""

INGREDIENTS = [

    # --- Grains ---
    {
        # USDA: Wheat flour, white, all-purpose, enriched, bleached
        "name": "Wheat Flour (Enriched)",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/168894/nutrients",
        "nutrients": {
            "calories": 364, "carbs": 76.31, "fat": 0.98, "protein": 10.33,
            "sodium": 2.0, "cholesterol": 0.0, "fiber": 2.7,
            "vitamin_c": 0.0, "calcium": 15, "iron": 4.64, "potassium": 107,
            "magnesium": 22, "zinc": 0.7, "b12": 0.0, "folate": 183,
            "thiamine": 0.785, "riboflavin": 0.494, "niacin": 5.904,
        },
    },
    {
        # USDA: Pasta, dry, enriched
        "name": "Macaroni",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/169736/nutrients",
        "nutrients": {
            "calories": 371, "carbs": 74.67, "fat": 1.51, "protein": 13.04,
            "sodium": 6.0, "cholesterol": 0.0, "fiber": 3.2,
            "vitamin_c": 0.0, "calcium": 21, "iron": 3.3, "potassium": 223,
            "magnesium": 53, "zinc": 1.41, "b12": 0.0, "folate": 237,
            "thiamine": 0.891, "riboflavin": 0.4, "niacin": 7.177,
        },
    },
    {
        # USDA: Cereals, farina, enriched, assorted brands including CREAM OF WHEAT, quick (1-3 minutes), dry
        "name": "Wheat Cereal (Enriched)",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/171658/nutrients",
        "nutrients": {
            "calories": 360, "carbs": 73.19, "fat": 1.41, "protein": 11.6,
            "sodium": 124, "cholesterol": 0.0, "fiber": 4.2,
            "vitamin_c": 0.0, "calcium": 711, "iron": 33.39, "potassium": 153,
            "magnesium": 45, "zinc": 1.32, "b12": 0.0, "folate": 121,
            "thiamine": 1.009, "riboflavin": 0.563, "niacin": 13.7,
        },
    },
    {
        # USDA: Cereals ready-to-eat, RALSTON Corn Flakes
        "name": "Corn Flakes",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/174648/nutrients",
        "nutrients": {
            "calories": 384, "carbs": 88.01, "fat": 0.91, "protein": 5.9,
            "sodium": 571, "cholesterol": 0.0, "fiber": 2.7,
            "vitamin_c": 65, "calcium": 2.0, "iron": 19.4, "potassium": 107,
            "magnesium": 7.0, "zinc": 0.2, "b12": 5.36, "folate": 714,
            "thiamine": 4.483, "riboflavin": 1.74, "niacin": 21.033,
        },
    },
    {
        # USDA: Cornmeal, whole-grain, yellow
        "name": "Corn Meal",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/169697/nutrients",
        "nutrients": {
            "calories": 362, "carbs": 76.89, "fat": 3.59, "protein": 8.12,
            "sodium": 35, "cholesterol": 0.0, "fiber": 7.3,
            "vitamin_c": 0.0, "calcium": 6.0, "iron": 3.45, "potassium": 287,
            "magnesium": 127, "zinc": 1.82, "b12": 0.0, "folate": 25,
            "thiamine": 0.385, "riboflavin": 0.201, "niacin": 3.632,
        },
    },
    {
        # USDA: Cereals, corn grits, white, regular and quick, enriched, dry
        "name": "Hominy Grits",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/171654/nutrients",
        "nutrients": {
            "calories": 370, "carbs": 79.09, "fat": 1.75, "protein": 7.65,
            "sodium": 1.0, "cholesterol": 0.0, "fiber": 4.6,
            "vitamin_c": 0.0, "calcium": 4.0, "iron": 3.05, "potassium": 141,
            "magnesium": 36, "zinc": 0.72, "b12": 0.0, "folate": 171,
            "thiamine": 1.271, "riboflavin": 0.339, "niacin": 4.465,
        },
    },
    {
        # USDA: Rice, white, long-grain, regular, raw, enriched
        "name": "Rice",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/168877/nutrients",
        "nutrients": {
            "calories": 365, "carbs": 79.95, "fat": 0.66, "protein": 7.13,
            "sodium": 5.0, "cholesterol": 0.0, "fiber": 1.3,
            "vitamin_c": 0.0, "calcium": 28, "iron": 4.31, "potassium": 115,
            "magnesium": 25, "zinc": 1.09, "b12": 0.0, "folate": 231,
            "thiamine": 0.576, "riboflavin": 0.049, "niacin": 4.192,
        },
    },
    {
        # USDA: Cereals, oats, regular and quick, not fortified, dry
        "name": "Rolled Oats",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/173904/nutrients",
        "nutrients": {
            "calories": 379, "carbs": 67.7, "fat": 6.52, "protein": 13.15,
            "sodium": 6.0, "cholesterol": 0.0, "fiber": 10.1,
            "vitamin_c": 0.0, "calcium": 52, "iron": 4.25, "potassium": 362,
            "magnesium": 138, "zinc": 3.64, "b12": 0.0, "folate": 32,
            "thiamine": 0.46, "riboflavin": 0.155, "niacin": 1.125,
        },
    },
    {
        # USDA: Bread, white, commercially prepared (includes soft bread crumbs)
        "name": "White Bread (Enriched)",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/174924/nutrients",
        "nutrients": {
            "calories": 266, "carbs": 49.42, "fat": 3.33, "protein": 8.85,
            "sodium": 490, "cholesterol": 0.0, "fiber": 2.7,
            "vitamin_c": 0.0, "calcium": 144, "iron": 3.61, "potassium": 126,
            "magnesium": 23, "zinc": 0.74, "b12": 0.0, "folate": 111,
            "thiamine": 0.533, "riboflavin": 0.243, "niacin": 4.78,
        },
    },
    {
        # USDA: Bread, whole-wheat, commercially prepared
        "name": "Whole Wheat Bread",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/172688/nutrients",
        "nutrients": {
            "calories": 252, "carbs": 42.71, "fat": 3.5, "protein": 12.45,
            "sodium": 455, "cholesterol": 0.0, "fiber": 6.0,
            "vitamin_c": 0.0, "calcium": 161, "iron": 2.47, "potassium": 254,
            "magnesium": 75, "zinc": 1.77, "b12": 0.0, "folate": 42,
            "thiamine": 0.394, "riboflavin": 0.167, "niacin": 4.438,
        },
    },
    {
        # USDA: Bread, rye
        "name": "Rye Bread",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/172684/nutrients",
        "nutrients": {
            "calories": 259, "carbs": 48.3, "fat": 3.3, "protein": 8.5,
            "sodium": 603, "cholesterol": 0.0, "fiber": 5.8,
            "vitamin_c": 0.4, "calcium": 73, "iron": 2.83, "potassium": 166,
            "magnesium": 40, "zinc": 1.14, "b12": 0.0, "folate": 110,
            "thiamine": 0.434, "riboflavin": 0.335, "niacin": 3.805,
        },
    },
    {
        # USDA: Cake, pound, commercially prepared, other than all butter, enriched
        "name": "Pound Cake",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/174940/nutrients",
        "nutrients": {
            "calories": 389, "carbs": 52.5, "fat": 17.9, "protein": 5.2,
            "sodium": 400, "cholesterol": 58, "fiber": 1.0,
            "vitamin_c": 0.1, "calcium": 64, "iron": 1.62, "potassium": 106,
            "magnesium": 13, "zinc": 0.39, "b12": 0.14, "folate": 36,
            "thiamine": 0.143, "riboflavin": 0.26, "niacin": 1.349,
        },
    },
    {
        # USDA: Crackers, saltines (includes oyster, soda, soup)
        "name": "Soda Crackers",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/172746/nutrients",
        "nutrients": {
            "calories": 418, "carbs": 74.05, "fat": 8.64, "protein": 9.46,
            "sodium": 941, "cholesterol": 0.0, "fiber": 2.8,
            "vitamin_c": 0.0, "calcium": 19, "iron": 5.57, "potassium": 152,
            "magnesium": 23, "zinc": 0.69, "b12": 0.09, "folate": 134,
            "thiamine": 0.702, "riboflavin": 0.487, "niacin": 6.442,
        },
    },

    # --- Dairy & Fats ---
    {
        # USDA: Milk, whole, 3.25% milkfat, with added vitamin D
        "name": "Milk",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/171265/nutrients",
        "nutrients": {
            "calories": 61, "carbs": 4.8, "fat": 3.25, "protein": 3.15,
            "sodium": 43, "cholesterol": 10, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 113, "iron": 0.03, "potassium": 132,
            "magnesium": 10, "zinc": 0.37, "b12": 0.45, "folate": 5.0,
            "thiamine": 0.046, "riboflavin": 0.169, "niacin": 0.089,
        },
    },
    {
        # USDA: Milk, canned, evaporated, with added vitamin D and without added vitamin A
        "name": "Evaporated Milk (can)",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/171276/nutrients",
        "nutrients": {
            "calories": 134, "carbs": 10.04, "fat": 7.56, "protein": 6.81,
            "sodium": 106, "cholesterol": 29, "fiber": 0.0,
            "vitamin_c": 1.9, "calcium": 261, "iron": 0.19, "potassium": 303,
            "magnesium": 24, "zinc": 0.77, "b12": 0.16, "folate": 8.0,
            "thiamine": 0.047, "riboflavin": 0.316, "niacin": 0.194,
        },
    },
    {
        # USDA: Butter, salted
        "name": "Butter",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/173410/nutrients",
        "nutrients": {
            "calories": 717, "carbs": 0.06, "fat": 81.11, "protein": 0.85,
            "sodium": 643, "cholesterol": 215, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 24, "iron": 0.02, "potassium": 24,
            "magnesium": 2.0, "zinc": 0.09, "b12": 0.17, "folate": 3.0,
            "thiamine": 0.005, "riboflavin": 0.034, "niacin": 0.042,
        },
    },
    {
        # USDA: Margarine, regular, 80% fat, composite, stick, with salt
        "name": "Oleomargarine",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/172346/nutrients",
        "nutrients": {
            "calories": 717, "carbs": 0.7, "fat": 80.71, "protein": 0.16,
            "sodium": 751, "cholesterol": 0.0, "fiber": 0.0,
            "vitamin_c": 0.2, "calcium": 3.0, "iron": 0.06, "potassium": 18,
            "magnesium": 3.0, "zinc": 0.0, "b12": 0.1, "folate": 1.0,
            "thiamine": 0.01, "riboflavin": 0.037, "niacin": 0.023,
        },
    },
    {
        # USDA: Egg, whole, raw, fresh
        "name": "Eggs",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/171287/nutrients",
        "nutrients": {
            "calories": 143, "carbs": 0.72, "fat": 9.51, "protein": 12.56,
            "sodium": 142, "cholesterol": 372, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 56, "iron": 1.75, "potassium": 138,
            "magnesium": 12, "zinc": 1.29, "b12": 0.89, "folate": 47,
            "thiamine": 0.04, "riboflavin": 0.457, "niacin": 0.075,
        },
    },
    {
        # USDA: Cheese, cheddar (Includes foods for USDA's Food Distribution Program)
        "name": "Cheese (Cheddar)",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/173414/nutrients",
        "nutrients": {
            "calories": 403, "carbs": 3.37, "fat": 33.31, "protein": 22.87,
            "sodium": 653, "cholesterol": 99, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 710, "iron": 0.14, "potassium": 76,
            "magnesium": 27, "zinc": 3.64, "b12": 1.1, "folate": 27,
            "thiamine": 0.029, "riboflavin": 0.428, "niacin": 0.059,
        },
    },
    {
        # USDA: Cream, fluid, light (coffee cream or table cream)
        "name": "Cream",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/170857/nutrients",
        "nutrients": {
            "calories": 195, "carbs": 3.66, "fat": 19.1, "protein": 2.96,
            "sodium": 72, "cholesterol": 59, "fiber": 0.0,
            "vitamin_c": 0.8, "calcium": 91, "iron": 0.05, "potassium": 136,
            "magnesium": 9.0, "zinc": 0.32, "b12": 0.14, "folate": 2.0,
            "thiamine": 0.023, "riboflavin": 0.19, "niacin": 0.09,
        },
    },
    {
        # USDA: Peanut butter, smooth style, with salt (Includes foods for USDA's Food Distribution Program)
        "name": "Peanut Butter",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/174266/nutrients",
        "nutrients": {
            "calories": 598, "carbs": 22.31, "fat": 51.36, "protein": 22.21,
            "sodium": 426, "cholesterol": 0.0, "fiber": 5.0,
            "vitamin_c": 0.0, "calcium": 49, "iron": 1.74, "potassium": 558,
            "magnesium": 168, "zinc": 2.51, "b12": 0.0, "folate": 87,
            "thiamine": 0.15, "riboflavin": 0.192, "niacin": 13.112,
        },
    },
    {
        # USDA: Salad dressing, mayonnaise, regular
        "name": "Mayonnaise",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/171009/nutrients",
        "nutrients": {
            "calories": 680, "carbs": 0.57, "fat": 74.85, "protein": 0.96,
            "sodium": 635, "cholesterol": 42, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 8.0, "iron": 0.21, "potassium": 20,
            "magnesium": 1.0, "zinc": 0.15, "b12": 0.12, "folate": 5.0,
            "thiamine": 0.01, "riboflavin": 0.019, "niacin": 0.0,
        },
    },
    {
        # USDA: Shortening, vegetable, household, composite
        "name": "Crisco",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/173584/nutrients",
        "nutrients": {
            "calories": 884, "carbs": 0.0, "fat": 99.97, "protein": 0.0,
            "sodium": 4.0, "cholesterol": 0.0, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 1.0, "iron": 0.07, "potassium": 0.0,
            "magnesium": 0.0, "zinc": 0.0, "b12": 0.0, "folate": 0.0,
            "thiamine": 0.02, "riboflavin": 0.0, "niacin": 0.0,
        },
    },
    {
        # USDA: Lard
        "name": "Lard",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/171401/nutrients",
        "nutrients": {
            "calories": 902, "carbs": 0.0, "fat": 100, "protein": 0.0,
            "sodium": 0.0, "cholesterol": 95, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 0.0, "iron": 0.0, "potassium": 0.0,
            "magnesium": 0.0, "zinc": 0.11, "b12": 0.0, "folate": 0.0,
            "thiamine": 0.0, "riboflavin": 0.0, "niacin": 0.0,
        },
    },

    # --- Meats & Fish ---
    {
        # USDA: Beef, top sirloin, steak, separable lean and fat, trimmed to 1/8" fat, all grades, raw
        "name": "Sirloin Steak",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/168726/nutrients",
        "nutrients": {
            "calories": 201, "carbs": 0.0, "fat": 12.71, "protein": 20.3,
            "sodium": 52, "cholesterol": 75, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 24, "iron": 1.48, "potassium": 315,
            "magnesium": 21, "zinc": 3.55, "b12": 1.05, "folate": 11,
            "thiamine": 0.063, "riboflavin": 0.098, "niacin": 5.986,
        },
    },
    {
        # USDA: Beef, round, full cut, separable lean and fat, trimmed to 1/8" fat, choice, raw
        "name": "Round Steak",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/168694/nutrients",
        "nutrients": {
            "calories": 195, "carbs": 0.0, "fat": 11.92, "protein": 20.56,
            "sodium": 54, "cholesterol": 62, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 4.0, "iron": 1.99, "potassium": 342,
            "magnesium": 22, "zinc": 3.24, "b12": 2.82, "folate": 8.0,
            "thiamine": 0.1, "riboflavin": 0.17, "niacin": 3.74,
        },
    },
    {
        # USDA: Beef, rib, whole (ribs 6-12), separable lean and fat, trimmed to 1/8" fat, all grades, raw
        "name": "Rib Roast",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/169498/nutrients",
        "nutrients": {
            "calories": 306, "carbs": 0.0, "fat": 26.1, "protein": 16.53,
            "sodium": 55, "cholesterol": 70, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 9.0, "iron": 1.74, "potassium": 272,
            "magnesium": 16, "zinc": 3.73, "b12": 2.82, "folate": 5.0,
            "thiamine": 0.08, "riboflavin": 0.13, "niacin": 2.8,
        },
    },
    {
        # USDA: Beef, chuck, arm pot roast, separable lean and fat, trimmed to 1/8" fat, all grades, raw
        "name": "Chuck Roast",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/169491/nutrients",
        "nutrients": {
            "calories": 244, "carbs": 0.0, "fat": 17.98, "protein": 19.23,
            "sodium": 62, "cholesterol": 91, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 17, "iron": 1.67, "potassium": 290,
            "magnesium": 19, "zinc": 4.54, "b12": 1.65, "folate": 10,
            "thiamine": 0.07, "riboflavin": 0.139, "niacin": 4.331,
        },
    },
    {
        # USDA: Beef, rib, shortribs, separable lean and fat, choice, raw
        "name": "Plate (beef)",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/169439/nutrients",
        "nutrients": {
            "calories": 390, "carbs": 0.4, "fat": 36.23, "protein": 14.4,
            "sodium": 49, "cholesterol": 76, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 9.0, "iron": 1.55, "potassium": 232,
            "magnesium": 14, "zinc": 3.16, "b12": 2.56, "folate": 5.0,
            "thiamine": 0.071, "riboflavin": 0.118, "niacin": 2.556,
        },
    },
    # Commenting out at my doctor's suggestion
    # {
    #     # USDA: Beef, variety meats and by-products, liver, raw
    #     "name": "Liver (Beef)",
    #     "unit": "100g",
    #     "grams": 100,
    #     "link": "https://fdc.nal.usda.gov/food-details/169451/nutrients",
    #     "nutrients": {
    #         "calories": 135, "carbs": 3.89, "fat": 3.63, "protein": 20.36,
    #         "sodium": 69, "cholesterol": 275, "fiber": 0.0,
    #         "vitamin_c": 1.3, "calcium": 5.0, "iron": 4.9, "potassium": 313,
    #         "magnesium": 18, "zinc": 4.0, "b12": 59.3, "folate": 290,
    #         "thiamine": 0.189, "riboflavin": 2.755, "niacin": 13.175,
    #     },
    # },
    {
        # USDA: Lamb, leg, whole (shank and sirloin), separable lean and fat, trimmed to 1/8" fat, choice, raw
        "name": "Leg of Lamb",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/174372/nutrients",
        "nutrients": {
            "calories": 209, "carbs": 0.0, "fat": 14.42, "protein": 18.47,
            "sodium": 57, "cholesterol": 68, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 8.0, "iron": 1.7, "potassium": 258,
            "magnesium": 24, "zinc": 3.43, "b12": 2.54, "folate": 20,
            "thiamine": 0.13, "riboflavin": 0.24, "niacin": 6.25,
        },
    },
    {
        # USDA: Lamb, rib, separable lean and fat, trimmed to 1/8" fat, choice, raw
        "name": "Lamb Chops (Rib)",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/174377/nutrients",
        "nutrients": {
            "calories": 342, "carbs": 0.0, "fat": 30.71, "protein": 15.32,
            "sodium": 58, "cholesterol": 74, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 14, "iron": 1.43, "potassium": 201,
            "magnesium": 19, "zinc": 2.87, "b12": 2.14, "folate": 15,
            "thiamine": 0.1, "riboflavin": 0.19, "niacin": 6.06,
        },
    },
    {
        # USDA: Pork, fresh, loin, center rib (chops or roasts), bone-in, separable lean and fat, raw
        "name": "Pork Chops",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/168242/nutrients",
        "nutrients": {
            "calories": 186, "carbs": 0.0, "fat": 11.04, "protein": 20.28,
            "sodium": 56, "cholesterol": 58, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 25, "iron": 0.59, "potassium": 337,
            "magnesium": 23, "zinc": 1.85, "b12": 0.54, "folate": 0.0,
            "thiamine": 0.456, "riboflavin": 0.177, "niacin": 6.331,
        },
    },
    {
        # USDA: Pork, fresh, loin, whole, separable lean and fat, raw
        "name": "Pork Loin Roast",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/167818/nutrients",
        "nutrients": {
            "calories": 198, "carbs": 0.0, "fat": 12.58, "protein": 19.74,
            "sodium": 50, "cholesterol": 63, "fiber": 0.0,
            "vitamin_c": 0.6, "calcium": 18, "iron": 0.79, "potassium": 356,
            "magnesium": 21, "zinc": 1.74, "b12": 0.53, "folate": 1.0,
            "thiamine": 0.901, "riboflavin": 0.248, "niacin": 4.58,
        },
    },
    {
        # USDA: Pork, cured, bacon, unprepared
        "name": "Bacon",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/168277/nutrients",
        "nutrients": {
            "calories": 393, "carbs": 0.0, "fat": 37.13, "protein": 13.66,
            "sodium": 751, "cholesterol": 66, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 6.0, "iron": 0.38, "potassium": 201,
            "magnesium": 13, "zinc": 1.14, "b12": 0.5, "folate": 0.0,
            "thiamine": 0.276, "riboflavin": 0.081, "niacin": 4.022,
        },
    },
    {
        # USDA: Pork, cured, ham, whole, separable lean and fat, unheated
        "name": "Ham, smoked",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/167875/nutrients",
        "nutrients": {
            "calories": 246, "carbs": 0.06, "fat": 18.52, "protein": 18.49,
            "sodium": 1284, "cholesterol": 56, "fiber": 0.0,
            "vitamin_c": 34.9, "calcium": 7.0, "iron": 0.71, "potassium": 310,
            "magnesium": 15, "zinc": 1.76, "b12": 0.74, "folate": 1.0,
            "thiamine": 0.777, "riboflavin": 0.189, "niacin": 4.463,
        },
    },
    {
        # USDA: Pork, cured, salt pork, raw
        "name": "Salt Pork",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/168287/nutrients",
        "nutrients": {
            "calories": 748, "carbs": 0.0, "fat": 80.5, "protein": 5.05,
            "sodium": 2684, "cholesterol": 86, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 6.0, "iron": 0.44, "potassium": 66,
            "magnesium": 7.0, "zinc": 0.9, "b12": 0.29, "folate": 1.0,
            "thiamine": 0.215, "riboflavin": 0.061, "niacin": 1.62,
        },
    },
    {
        # USDA: Chicken, roasting, meat and skin and giblets and neck, raw
        "name": "Roasting Chicken",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/172394/nutrients",
        "nutrients": {
            "calories": 213, "carbs": 0.09, "fat": 15.46, "protein": 17.09,
            "sodium": 69, "cholesterol": 86, "fiber": 0.0,
            "vitamin_c": 2.4, "calcium": 10, "iron": 1.37, "potassium": 196,
            "magnesium": 19, "zinc": 1.28, "b12": 0.99, "folate": 26,
            "thiamine": 0.059, "riboflavin": 0.171, "niacin": 6.427,
        },
    },
    {
        # USDA: Veal, leg, top round, cap off, cutlet, boneless, raw
        "name": "Veal Cutlets",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/172643/nutrients",
        "nutrients": {
            "calories": 107, "carbs": 0.0, "fat": 2.07, "protein": 22.07,
            "sodium": 86, "cholesterol": 56, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 4.0, "iron": 0.81, "potassium": 273,
            "magnesium": 30, "zinc": 1.97, "b12": 2.08, "folate": 4.0,
            "thiamine": 0.1, "riboflavin": 0.34, "niacin": 9.28,
        },
    },
    {
        # USDA: Fish, salmon, pink, canned, total can contents
        "name": "Salmon, Pink (can)",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/173690/nutrients",
        "nutrients": {
            "calories": 129, "carbs": 0.0, "fat": 4.97, "protein": 19.68,
            "sodium": 403, "cholesterol": 55, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 215, "iron": 0.64, "potassium": 344,
            "magnesium": 30, "zinc": 0.76, "b12": 4.4, "folate": 15,
            "thiamine": 0.023, "riboflavin": 0.186, "niacin": 6.536,
        },
    },

    # --- Fruits ---
    {
        # USDA: Apples, raw, with skin (Includes foods for USDA's Food Distribution Program)
        "name": "Apples",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/171688/nutrients",
        "nutrients": {
            "calories": 52, "carbs": 13.81, "fat": 0.17, "protein": 0.26,
            "sodium": 1.0, "cholesterol": 0.0, "fiber": 2.4,
            "vitamin_c": 4.6, "calcium": 6.0, "iron": 0.12, "potassium": 107,
            "magnesium": 5.0, "zinc": 0.04, "b12": 0.0, "folate": 3.0,
            "thiamine": 0.017, "riboflavin": 0.026, "niacin": 0.091,
        },
    },
    {
        # USDA: Bananas, raw
        "name": "Bananas",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/173944/nutrients",
        "nutrients": {
            "calories": 89, "carbs": 22.84, "fat": 0.33, "protein": 1.09,
            "sodium": 1.0, "cholesterol": 0.0, "fiber": 2.6,
            "vitamin_c": 8.7, "calcium": 5.0, "iron": 0.26, "potassium": 358,
            "magnesium": 27, "zinc": 0.15, "b12": 0.0, "folate": 20,
            "thiamine": 0.031, "riboflavin": 0.073, "niacin": 0.665,
        },
    },
    {
        # USDA: Lemons, raw, without peel
        "name": "Lemons",
        "unit": "100g",
        "grams": 100,
        "max_amount": 92, # too much is bad for teeth. max_amount crudely copied from lemon juice max_amount, 
        "link": "https://fdc.nal.usda.gov/food-details/167746/nutrients", # although strictly they shouldn't
        "nutrients": {                                                    # be the same. Also, their max should
            "calories": 29, "carbs": 9.32, "fat": 0.3, "protein": 1.1,    # be treated as combined; the max of
            "sodium": 2.0, "cholesterol": 0.0, "fiber": 2.8,              # both would be twice as much as you
            "vitamin_c": 53, "calcium": 26, "iron": 0.6, "potassium": 138, # should have.
            "magnesium": 8.0, "zinc": 0.06, "b12": 0.0, "folate": 11,
            "thiamine": 0.04, "riboflavin": 0.02, "niacin": 0.1,
        },
    },
    {
        # USDA: Oranges, raw, all commercial varieties
        "name": "Oranges",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/169097/nutrients",
        "nutrients": {
            "calories": 47, "carbs": 11.75, "fat": 0.12, "protein": 0.94,
            "sodium": 0.0, "cholesterol": 0.0, "fiber": 2.4,
            "vitamin_c": 53.2, "calcium": 40, "iron": 0.1, "potassium": 181,
            "magnesium": 10, "zinc": 0.07, "b12": 0.0, "folate": 30,
            "thiamine": 0.087, "riboflavin": 0.04, "niacin": 0.282,
        },
    },
    {
        # USDA: Peaches, canned, heavy syrup pack, solids and liquids
        "name": "Peaches (can)",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/169112/nutrients",
        "nutrients": {
            "calories": 74, "carbs": 19.94, "fat": 0.1, "protein": 0.45,
            "sodium": 6.0, "cholesterol": 0.0, "fiber": 1.3,
            "vitamin_c": 2.8, "calcium": 3.0, "iron": 0.27, "potassium": 92,
            "magnesium": 5.0, "zinc": 0.09, "b12": 0.0, "folate": 3.0,
            "thiamine": 0.011, "riboflavin": 0.024, "niacin": 0.614,
        },
    },
    {
        # USDA: Pears, canned, heavy syrup pack, solids and liquids
        "name": "Pears (can)",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/169939/nutrients",
        "nutrients": {
            "calories": 74, "carbs": 19.17, "fat": 0.13, "protein": 0.2,
            "sodium": 5.0, "cholesterol": 0.0, "fiber": 1.6,
            "vitamin_c": 1.1, "calcium": 5.0, "iron": 0.22, "potassium": 65,
            "magnesium": 4.0, "zinc": 0.08, "b12": 0.0, "folate": 1.0,
            "thiamine": 0.01, "riboflavin": 0.022, "niacin": 0.242,
        },
    },
    {
        # USDA: Pineapple, canned, heavy syrup pack, solids and liquids
        "name": "Pineapple (can)",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/169944/nutrients",
        "nutrients": {
            "calories": 78, "carbs": 20.2, "fat": 0.11, "protein": 0.35,
            "sodium": 1.0, "cholesterol": 0.0, "fiber": 0.8,
            "vitamin_c": 7.4, "calcium": 14, "iron": 0.38, "potassium": 104,
            "magnesium": 16, "zinc": 0.12, "b12": 0.0, "folate": 5.0,
            "thiamine": 0.09, "riboflavin": 0.025, "niacin": 0.287,
        },
    },
    {
        # USDA: Peaches, dried, sulfured, uncooked
        "name": "Peaches, Dried",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/169934/nutrients",
        "nutrients": {
            "calories": 239, "carbs": 61.33, "fat": 0.76, "protein": 3.61,
            "sodium": 7.0, "cholesterol": 0.0, "fiber": 8.2,
            "vitamin_c": 4.8, "calcium": 28, "iron": 4.06, "potassium": 996,
            "magnesium": 42, "zinc": 0.57, "b12": 0.0, "folate": 0.0,
            "thiamine": 0.002, "riboflavin": 0.212, "niacin": 4.375,
        },
    },
    {
        # USDA: Plums, dried (prunes), uncooked
        "name": "Prunes, Dried",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/168162/nutrients",
        "nutrients": {
            "calories": 240, "carbs": 63.88, "fat": 0.38, "protein": 2.18,
            "sodium": 2.0, "cholesterol": 0.0, "fiber": 7.1,
            "vitamin_c": 0.6, "calcium": 43, "iron": 0.93, "potassium": 732,
            "magnesium": 41, "zinc": 0.44, "b12": 0.0, "folate": 4.0,
            "thiamine": 0.051, "riboflavin": 0.186, "niacin": 1.882,
        },
    },
    {
        # USDA: Raisins, dark, seedless (Includes foods for USDA's Food Distribution Program)
        "name": "Raisins, Dried",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/168165/nutrients",
        "nutrients": {
            "calories": 299, "carbs": 79.32, "fat": 0.25, "protein": 3.3,
            "sodium": 26, "cholesterol": 0.0, "fiber": 4.5,
            "vitamin_c": 2.3, "calcium": 62, "iron": 1.79, "potassium": 744,
            "magnesium": 36, "zinc": 0.36, "b12": 0.0, "folate": 5.0,
            "thiamine": 0.106, "riboflavin": 0.125, "niacin": 0.766,
        },
    },

    # --- Vegetables ---
    {
        # USDA: Beans, snap, green, raw
        "name": "Green Beans",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/169961/nutrients",
        "nutrients": {
            "calories": 31, "carbs": 6.97, "fat": 0.22, "protein": 1.83,
            "sodium": 6.0, "cholesterol": 0.0, "fiber": 2.7,
            "vitamin_c": 12.2, "calcium": 37, "iron": 1.03, "potassium": 211,
            "magnesium": 25, "zinc": 0.24, "b12": 0.0, "folate": 33,
            "thiamine": 0.082, "riboflavin": 0.104, "niacin": 0.734,
        },
    },
    {
        # USDA: Cabbage, raw
        "name": "Cabbage",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/169975/nutrients",
        "nutrients": {
            "calories": 25, "carbs": 5.8, "fat": 0.1, "protein": 1.28,
            "sodium": 18, "cholesterol": 0.0, "fiber": 2.5,
            "vitamin_c": 36.6, "calcium": 40, "iron": 0.47, "potassium": 170,
            "magnesium": 12, "zinc": 0.18, "b12": 0.0, "folate": 43,
            "thiamine": 0.061, "riboflavin": 0.04, "niacin": 0.234,
        },
    },
    {
        # USDA: Carrots, raw
        "name": "Carrots",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/170393/nutrients",
        "nutrients": {
            "calories": 41, "carbs": 9.58, "fat": 0.24, "protein": 0.93,
            "sodium": 69, "cholesterol": 0.0, "fiber": 2.8,
            "vitamin_c": 5.9, "calcium": 33, "iron": 0.3, "potassium": 320,
            "magnesium": 12, "zinc": 0.24, "b12": 0.0, "folate": 19,
            "thiamine": 0.066, "riboflavin": 0.058, "niacin": 0.983,
        },
    },
    {
        # USDA: Celery, raw
        "name": "Celery",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/169988/nutrients",
        "nutrients": {
            "calories": 14, "carbs": 2.97, "fat": 0.17, "protein": 0.69,
            "sodium": 80, "cholesterol": 0.0, "fiber": 1.6,
            "vitamin_c": 3.1, "calcium": 40, "iron": 0.2, "potassium": 260,
            "magnesium": 11, "zinc": 0.13, "b12": 0.0, "folate": 36,
            "thiamine": 0.021, "riboflavin": 0.057, "niacin": 0.32,
        },
    },
    {
        # USDA: Lettuce, iceberg (includes crisphead types), raw
        "name": "Lettuce",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/169248/nutrients",
        "nutrients": {
            "calories": 14, "carbs": 2.97, "fat": 0.14, "protein": 0.9,
            "sodium": 10, "cholesterol": 0.0, "fiber": 1.2,
            "vitamin_c": 2.8, "calcium": 18, "iron": 0.41, "potassium": 141,
            "magnesium": 7.0, "zinc": 0.15, "b12": 0.0, "folate": 29,
            "thiamine": 0.041, "riboflavin": 0.025, "niacin": 0.123,
        },
    },
    {
        # USDA: Onions, raw
        "name": "Onions",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/170000/nutrients",
        "nutrients": {
            "calories": 40, "carbs": 9.34, "fat": 0.1, "protein": 1.1,
            "sodium": 4.0, "cholesterol": 0.0, "fiber": 1.7,
            "vitamin_c": 7.4, "calcium": 23, "iron": 0.21, "potassium": 146,
            "magnesium": 10, "zinc": 0.17, "b12": 0.0, "folate": 19,
            "thiamine": 0.046, "riboflavin": 0.027, "niacin": 0.116,
        },
    },
    {
        # USDA: Potatoes, flesh and skin, raw
        "name": "Potatoes",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/170026/nutrients",
        "nutrients": {
            "calories": 77, "carbs": 17.49, "fat": 0.09, "protein": 2.05,
            "sodium": 6.0, "cholesterol": 0.0, "fiber": 2.1,
            "vitamin_c": 19.7, "calcium": 12, "iron": 0.81, "potassium": 425,
            "magnesium": 23, "zinc": 0.3, "b12": 0.0, "folate": 15,
            "thiamine": 0.081, "riboflavin": 0.032, "niacin": 1.061,
        },
    },
    {
        # USDA: Spinach, raw
        "name": "Spinach",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/168462/nutrients",
        "nutrients": {
            "calories": 23, "carbs": 3.63, "fat": 0.39, "protein": 2.86,
            "sodium": 79, "cholesterol": 0.0, "fiber": 2.2,
            "vitamin_c": 28.1, "calcium": 99, "iron": 2.71, "potassium": 558,
            "magnesium": 79, "zinc": 0.53, "b12": 0.0, "folate": 194,
            "thiamine": 0.078, "riboflavin": 0.189, "niacin": 0.724,
        },
    },
    {
        # USDA: Sweet potato, raw, unprepared (Includes foods for USDA's Food Distribution Program)
        "name": "Sweet Potatoes",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/168482/nutrients",
        "nutrients": {
            "calories": 86, "carbs": 20.12, "fat": 0.05, "protein": 1.57,
            "sodium": 55, "cholesterol": 0.0, "fiber": 3.0,
            "vitamin_c": 2.4, "calcium": 30, "iron": 0.61, "potassium": 337,
            "magnesium": 25, "zinc": 0.3, "b12": 0.0, "folate": 11,
            "thiamine": 0.078, "riboflavin": 0.061, "niacin": 0.557,
        },
    },
    {
        # USDA: Asparagus, canned, regular pack, solids and liquids
        "name": "Asparagus (can)",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/169206/nutrients",
        "nutrients": {
            "calories": 15, "carbs": 2.48, "fat": 0.18, "protein": 1.8,
            "sodium": 284, "cholesterol": 0.0, "fiber": 1.0,
            "vitamin_c": 16.5, "calcium": 15, "iron": 0.6, "potassium": 172,
            "magnesium": 9.0, "zinc": 0.47, "b12": 0.0, "folate": 85,
            "thiamine": 0.054, "riboflavin": 0.089, "niacin": 0.851,
        },
    },
    {
        # USDA: Beans, snap, green, canned, regular pack, solids and liquids
        "name": "Green Beans (can)",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/169142/nutrients",
        "nutrients": {
            "calories": 15, "carbs": 3.27, "fat": 0.17, "protein": 0.72,
            "sodium": 192, "cholesterol": 0.0, "fiber": 1.5,
            "vitamin_c": 2.2, "calcium": 29, "iron": 1.02, "potassium": 92,
            "magnesium": 13, "zinc": 0.36, "b12": 0.0, "folate": 26,
            "thiamine": 0.015, "riboflavin": 0.02, "niacin": 0.2,
        },
    },
    {
        # USDA: Corn, sweet, yellow, canned, brine pack, regular pack, solids and liquids
        "name": "Corn (can)",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/170409/nutrients",
        "nutrients": {
            "calories": 61, "carbs": 13.86, "fat": 0.77, "protein": 1.95,
            "sodium": 195, "cholesterol": 0.0, "fiber": 1.7,
            "vitamin_c": 2.6, "calcium": 4.0, "iron": 0.36, "potassium": 136,
            "magnesium": 15, "zinc": 0.39, "b12": 0.0, "folate": 38,
            "thiamine": 0.015, "riboflavin": 0.015, "niacin": 0.884,
        },
    },
    {
        # USDA: Peas, green, canned, regular pack, solids and liquids
        "name": "Peas (can)",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/170421/nutrients",
        "nutrients": {
            "calories": 58, "carbs": 10.6, "fat": 0.48, "protein": 3.01,
            "sodium": 185, "cholesterol": 0.0, "fiber": 3.3,
            "vitamin_c": 7.8, "calcium": 20, "iron": 1.29, "potassium": 106,
            "magnesium": 19, "zinc": 0.72, "b12": 0.0, "folate": 24,
            "thiamine": 0.077, "riboflavin": 0.024, "niacin": 0.995,
        },
    },
    {
        # USDA: Tomatoes, red, ripe, canned, packed in tomato juice
        "name": "Tomatoes (can)",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/170051/nutrients",
        "nutrients": {
            "calories": 16, "carbs": 3.47, "fat": 0.25, "protein": 0.79,
            "sodium": 115, "cholesterol": 0.0, "fiber": 1.9,
            "vitamin_c": 12.6, "calcium": 33, "iron": 0.57, "potassium": 191,
            "magnesium": 10, "zinc": 0.12, "b12": 0.0, "folate": 8.0,
            "thiamine": 0.575, "riboflavin": 0.055, "niacin": 0.712,
        },
    },
    {
        # USDA: Soup, tomato, canned, condensed
        "name": "Tomato Soup (can)",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/172882/nutrients",
        "nutrients": {
            "calories": 66, "carbs": 15.22, "fat": 0.44, "protein": 1.46,
            "sodium": 377, "cholesterol": 0.0, "fiber": 1.1,
            "vitamin_c": 12.9, "calcium": 13, "iron": 0.59, "potassium": 562,
            "magnesium": 14, "zinc": 0.18, "b12": 0.0, "folate": 0.0,
            "thiamine": 0.042, "riboflavin": 0.015, "niacin": 0.858,
        },
    },

    # --- Legumes ---
    {
        # USDA: Beans, baked, canned, with pork
        "name": "Pork and Beans (can)",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/175185/nutrients",
        "nutrients": {
            "calories": 106, "carbs": 19.99, "fat": 1.55, "protein": 5.19,
            "sodium": 414, "cholesterol": 7.0, "fiber": 5.5,
            "vitamin_c": 2.0, "calcium": 53, "iron": 1.7, "potassium": 309,
            "magnesium": 34, "zinc": 1.46, "b12": 0.0, "folate": 36,
            "thiamine": 0.053, "riboflavin": 0.038, "niacin": 0.447,
        },
    },
    {
        # USDA: Peas, green, split, mature seeds, raw
        "name": "Peas, Dried",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/172428/nutrients",
        "nutrients": {
            "calories": 364, "carbs": 61.63, "fat": 3.89, "protein": 23.12,
            "sodium": 5.0, "cholesterol": 0.0, "fiber": 22.2,
            "vitamin_c": 1.8, "calcium": 46, "iron": 4.73, "potassium": 852,
            "magnesium": 63, "zinc": 3.49, "b12": 0.0, "folate": 15,
            "thiamine": 0.719, "riboflavin": 0.244, "niacin": 3.608,
        },
    },
    {
        # USDA: Lima beans, large, mature seeds, raw
        "name": "Lima Beans, Dried",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/174252/nutrients",
        "nutrients": {
            "calories": 338, "carbs": 63.38, "fat": 0.69, "protein": 21.46,
            "sodium": 18, "cholesterol": 0.0, "fiber": 19,
            "vitamin_c": 0.0, "calcium": 81, "iron": 7.51, "potassium": 1724,
            "magnesium": 224, "zinc": 2.83, "b12": 0.0, "folate": 395,
            "thiamine": 0.507, "riboflavin": 0.202, "niacin": 1.537,
        },
    },
    {
        # USDA: Beans, navy, mature seeds, raw
        "name": "Navy Beans, Dried",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/173745/nutrients",
        "nutrients": {
            "calories": 337, "carbs": 60.75, "fat": 1.5, "protein": 22.33,
            "sodium": 5.0, "cholesterol": None, "fiber": 15.3,
            "vitamin_c": None, "calcium": 147, "iron": 5.49, "potassium": 1185,
            "magnesium": 175, "zinc": 3.65, "b12": 0.0, "folate": 364,
            "thiamine": 0.775, "riboflavin": 0.164, "niacin": 2.188,
        },
    },

    # --- Miscellaneous ---
    {
        # USDA: Beverages, coffee, brewed, prepared with tap water
        "name": "Coffee",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/171890/nutrients",
        "nutrients": {
            "calories": 1.0, "carbs": 0.0, "fat": 0.02, "protein": 0.12,
            "sodium": 2.0, "cholesterol": 0.0, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 2.0, "iron": 0.01, "potassium": 49,
            "magnesium": 3.0, "zinc": 0.02, "b12": 0.0, "folate": 2.0,
            "thiamine": 0.014, "riboflavin": 0.076, "niacin": 0.191,
        },
    },
    {
        # USDA: Beverages, tea, black, brewed, prepared with tap water
        "name": "Tea",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/173227/nutrients",
        "nutrients": {
            "calories": 1.0, "carbs": 0.3, "fat": 0.0, "protein": 0.0,
            "sodium": 3.0, "cholesterol": 0.0, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 0.0, "iron": 0.02, "potassium": 37,
            "magnesium": 3.0, "zinc": 0.02, "b12": 0.0, "folate": 5.0,
            "thiamine": 0.0, "riboflavin": 0.014, "niacin": 0.0,
        },
    },
    {
        # USDA: Cocoa, dry powder, unsweetened
        "name": "Cocoa",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/169593/nutrients",
        "nutrients": {
            "calories": 228, "carbs": 57.9, "fat": 13.7, "protein": 19.6,
            "sodium": 21, "cholesterol": 0.0, "fiber": 37,
            "vitamin_c": 0.0, "calcium": 128, "iron": 13.86, "potassium": 1524,
            "magnesium": 499, "zinc": 6.81, "b12": 0.0, "folate": 32,
            "thiamine": 0.078, "riboflavin": 0.241, "niacin": 2.185,
        },
    },
    {
        # USDA: Baking chocolate, unsweetened, squares
        "name": "Chocolate",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/167568/nutrients",
        "nutrients": {
            "calories": 642, "carbs": 28.42, "fat": 52.31, "protein": 14.32,
            "sodium": 24, "cholesterol": 2.0, "fiber": 16.6,
            "vitamin_c": 0.0, "calcium": 101, "iron": 17.4, "potassium": 830,
            "magnesium": 327, "zinc": 9.63, "b12": 0.0, "folate": 28,
            "thiamine": 0.147, "riboflavin": 0.1, "niacin": 1.355,
        },
    },
    {
        # USDA: Sugars, granulated
        "name": "Sugar",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/169655/nutrients",
        "nutrients": {
            "calories": 387, "carbs": 99.98, "fat": 0.0, "protein": 0.0,
            "sodium": 1.0, "cholesterol": 0.0, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 1.0, "iron": 0.05, "potassium": 2.0,
            "magnesium": 0.0, "zinc": 0.01, "b12": 0.0, "folate": 0.0,
            "thiamine": 0.0, "riboflavin": 0.019, "niacin": 0.0,
        },
    },
    {
        # USDA: Syrups, corn, light
        "name": "Corn Syrup",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/168837/nutrients",
        "nutrients": {
            "calories": 283, "carbs": 76.79, "fat": 0.2, "protein": 0.0,
            "sodium": 62, "cholesterol": 0.0, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 13, "iron": 0.0, "potassium": 1.0,
            "magnesium": 1.0, "zinc": 0.44, "b12": 0.0, "folate": 0.0,
            "thiamine": 0.059, "riboflavin": 0.0, "niacin": 0.0,
        },
    },
    {
        # USDA: Molasses
        "name": "Molasses",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/168820/nutrients",
        "nutrients": {
            "calories": 290, "carbs": 74.73, "fat": 0.1, "protein": 0.0,
            "sodium": 37, "cholesterol": 0.0, "fiber": 0.0,
            "vitamin_c": 0.0, "calcium": 205, "iron": 4.72, "potassium": 1464,
            "magnesium": 242, "zinc": 0.29, "b12": 0.0, "folate": 0.0,
            "thiamine": 0.041, "riboflavin": 0.002, "niacin": 0.93,
        },
    },
    {
        # USDA: Jams and preserves
        "name": "Strawberry Preserves",
        "unit": "100g",
        "grams": 100,
        "link": "https://fdc.nal.usda.gov/food-details/169641/nutrients",
        "nutrients": {
            "calories": 278, "carbs": 68.86, "fat": 0.07, "protein": 0.37,
            "sodium": 32, "cholesterol": 0.0, "fiber": 1.1,
            "vitamin_c": 8.8, "calcium": 20, "iron": 0.49, "potassium": 77,
            "magnesium": 4.0, "zinc": 0.06, "b12": 0.0, "folate": 11,
            "thiamine": 0.016, "riboflavin": 0.076, "niacin": 0.036,
        },
    },
]
