# diet-lp

Given a set of foods and nutritional targets, the solver finds the quantities of each food that minimize deviation from your macro targets while satisfying hard constraints on calories, sodium, cholesterol, fiber, and a set of micronutrients.

This is a toy for exploring Google's Linear Programming solver [OR-Tools](https://developers.google.com/optimization) (GLOP solver) by expanding on their implementation of the [Stigler diet problem](https://developers.google.com/optimization/lp/stigler_diet), towards a functionality resembling that of [Eat This Much](https://www.eatthismuch.com/).

It's also a toy problem for testing genAI capabilites. The majority of the code and database entries are written by Claude Code and reviewed by myself.

The example database contains all the foods in the Stigler problem, plus many more, and is set up to allow you to enter more foods. The tool's results are not serious (let alone optimal) nutritional advice, just as the original Stigler problem wasn't; but it moves in that direction. Neither Claude Code nor myself are trustworthy nutrition experts.

The specific number targets in here are just whatever I happen to have been playing around with. Customize them for your own needs.

## Requirements

- Python 3.8+
- [OR-Tools](https://pypi.org/project/ortools/)

```bash
pip install ortools
```

## Usage

```bash
python3 main.py
```

<details>

<summary>Here's what the solution will look like if you don't edit anything.</summary>

```
Loaded 103 foods.
Solving...

Status: OPTIMAL

                       Amount       Cal |     Carbs       Fat   Protein |    Sodium   Cholest     Fiber
                                   kcal |         g         g         g |        mg        mg         g
-------------------------------------------------------------------------------------------------------
Greek yogurt, plain,    1163g     686.1 |      41.9       4.7     118.6 |     418.7      58.1       0.0
Mushrooms, white, ra     512g     112.6 |      16.9       1.5      15.9 |      25.6       0.0       5.1
Lemons                   248g      53.9 |      23.1       0.7       1.2 |       5.0       0.0       7.0
Lettuce                  228g      15.0 |       6.6       0.2       0.9 |      22.8       0.0       2.7
Roasting Chicken         122g     147.1 |       0.0      18.5      15.1 |      91.8      91.8       0.0
Almonds, raw              99g     572.5 |      21.4      49.3      21.0 |       1.0       0.0      12.4
Tuna, canned in wate      85g      98.6 |       0.0       2.2      21.7 |     336.6      39.1       0.0
Salmon with roasted    0.1srv      49.1 |       1.8       2.6       4.7 |      37.5      11.0       0.6
Navy Beans, Dried         10g      36.2 |       6.3       0.2       2.3 |       0.5       0.0       2.5
Lentils, raw               7g      23.9 |       4.1       0.1       1.7 |       0.4       0.0       0.7
-------------------------------------------------------------------------------------------------------
TOTAL                            1795.0 |     122.0      80.0     203.0 |     939.8     200.0      31.0
Target                        1600-1795 |    20-225    61-100    71-225 |  max 1500   max 200    min 31
-------------------------------------------------------------------------------------------------------

                       Amount   Vit C Calcium    Iron Potass. Magnes.    Zinc     B12  Folate Thiamin Riboflv  Niacin
                                   mg      mg      mg      mg      mg      mg     mcg     mcg      mg      mg      mg
---------------------------------------------------------------------------------------------------------------------
Greek yogurt, plain,    1163g     0.0  1279.2     1.2  1639.8   127.9     5.8     4.7    81.4     0.2     2.1     2.3
Mushrooms, white, ra     512g    10.7    15.4     2.6  1627.1    46.1     2.6     0.2    87.0     0.4     2.0    18.4
Lemons                   248g    51.2    27.3     0.7   342.9    19.9     0.2     0.0    27.3     0.0     0.0     0.2
Lettuce                  228g    16.9    41.0     0.8   321.4    16.0     0.5     0.0    66.1     0.1     0.1     0.4
Roasting Chicken         122g     3.8     8.6     2.4   272.9    24.5     1.6     0.4     9.8     0.1     0.1     5.6
Almonds, raw              99g     0.0   261.0     3.7   724.8   267.0     3.1     0.0    43.5     0.2     1.1     3.6
Tuna, canned in wate      85g     0.0     9.3     1.1   201.5    29.8     0.8     2.1     3.4     0.0     0.1    11.3
Salmon with roasted    0.1srv     7.1     8.4     0.2   115.0     9.3     0.2     0.5    11.4     0.0     0.1     1.4
Navy Beans, Dried         10g     0.0    15.3     1.1   122.6    18.1     0.4     0.0    37.7     0.1     0.0     0.3
Lentils, raw               7g     0.3     3.8     0.5    45.9     8.3     0.2     0.0    32.5     0.1     0.0     0.2
---------------------------------------------------------------------------------------------------------------------
TOTAL                            90.0  1669.4    14.3  5413.7   566.7    15.3     7.8   400.0     1.2     5.7    43.6
Target                         min 90 min 1000   min 8 min 3400 min 420  min 11 min 2.4 min 400 min 1.2 min 1.3  min 16
---------------------------------------------------------------------------------------------------------------------

  Carbs      target 122g   +0.0 / -0.0
  Fat        target 80g   +0.0 / -0.0
  Protein    target 203g   +0.0 / -0.0

  Objective (weighted macro deviation): 0.000
```
</details>
## Structure

```
diet-lp/
├── main.py          # solver, settings, and output
└── foods/
    ├── stigler.py         # Stigler (1945) commodity set
    ├── usda.py            # additional USDA SR Legacy ingredients
    ├── recipes.py         # example recipes
    └── local_example.py   # template for a personal food file (optional)
```

Every `.py` file in `foods/` is loaded automatically. Drop any file defining `INGREDIENTS` and/or `RECIPES` lists there and it will be picked up on the next run — no changes to `main.py` needed.

### Personal food database (optional)

To add your own foods, copy the template `local_example.py` and fill it in.

### Settings

All nutritional targets and bounds live at the top of `main.py`.

- **Calorie bounds** — hard min/max
- **Macro targets** — the solver minimizes weighted deviation from these
- **Macro bounds** — hard min/max per macro regardless of target
- **Macro weights** — tune how hard the solver tries to avoid over/undershooting each macro; asymmetric weights are supported (e.g. penalize undershooting protein more than overshooting)
- **Sodium, cholesterol** — hard upper bounds
- **Fiber** — hard lower bound
- **Micronutrient minimums** — hard lower bounds for Vitamin C, Calcium, Iron, Potassium, Magnesium, Zinc, B12, Folate, Thiamine, Riboflavin, and Niacin

### Food database

The `foods/` directory contains the food database. Each entry is a Python dict.

**Ingredients** — nutrient values per 100g; the solver variable is grams consumed:

```python
{
    "name": "Chicken breast, raw",
    "unit": "100g",
    "grams": 100,
    "nutrients": {
        "calories": 120, "carbs": 0, "fat": 2.6, "protein": 22.5,
        "sodium": 74, "cholesterol": 73, "fiber": 0,
        # ... micronutrients
    },
}
```

**Recipes** — nutrient values per serving; the solver variable is number of servings:

```python
{
    "name": "Lentil vegetable soup (1 serving ~400g)",
    "unit": "1 serving",
    "grams": 400,  # informational only
    "nutrients": {
        "calories": 220, "carbs": 38.0, "fat": 3.5, "protein": 13.0,
        # ...
    },
}
```

Nutrient values can be sourced from [USDA FoodData Central](https://fdc.nal.usda.gov/).

#### Per-food bounds

To cap or fix a food's quantity, add `min_amount` and/or `max_amount` to its entry:

```python
# Limit tuna to ~1 can/day due to mercury
{
    "name": "Tuna, canned in water",
    "max_amount": 85,  # grams
    # ...
}

# Fix 200g of oats as a daily staple; optimize the rest around it
{
    "name": "Oats, rolled, dry",
    "min_amount": 200,
    "max_amount": 200,
    # ...
}
```

### Including and excluding food groups

To exclude a file's foods entirely, remove or rename the file in `foods/`. To add a new themed group (e.g. `foods/staples.py`), create a new file there with `INGREDIENTS` and/or `RECIPES` lists — it will be picked up automatically.