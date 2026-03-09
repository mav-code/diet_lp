# diet-lp

Given a set of foods and nutritional targets, the solver finds the quantities of each food that minimize deviation from your macro targets while satisfying hard constraints on calories, sodium, cholesterol, fiber, and a set of micronutrients.

This is a toy for exploring Google's Linear Programming solver [OR-Tools](https://developers.google.com/optimization) (GLOP solver) by expanding on their implementation of the [Stigler diet problem](https://developers.google.com/optimization/lp/stigler_diet), towards a functionality resembling that of [Eat This Much](https://www.eatthismuch.com/). 

The example database contains all the foods in the Stigler problem, plus a few more. The tool's results are not serious (let alone optimal) nutritional advice, just as the original Stigler problem wasn't; but it moves in that direction.

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

============================================================
FOODS IN SOLUTION
============================================================
  Wheat Cereal (Enriched): 5.7g
  Potatoes: 2.8g
  Navy Beans, Dried: 38.0g
  Tofu, firm, raw: 36.3g
  Greek yogurt, plain, nonfat: 390.3g
  Almonds, raw: 85.5g
  Chicken and brown rice bowl (1 serving ~350g): 0.73 servings
  Salmon with roasted vegetables (1 serving ~300g): 1.30 servings
  Black bean and vegetable stir-fry (1 serving ~300g): 0.23 servings

============================================================
NUTRIENT SUMMARY
============================================================
  Calories                 1772.1 kcal   (target: 1600–1795)

  -- Macros --
  Carbs                     122.0 g      (target: 20–225g)
                         (+0.0 / -0.0 from target 122g)
  Fat                        80.0 g      (target: 61–100g)
                         (+0.0 / -0.0 from target 80g)
  Protein                   148.0 g      (target: 71–225g)
                         (+0.0 / -0.0 from target 148g)

  -- Constrained nutrients --
  Sodium                    853.7 mg     (target: max 1500)
  Cholesterol               200.0 mg     (target: max 200)
  Fiber                      31.0 g      (target: min 31)

  -- Micronutrients --
  Vitamin C                  90.0 mg     (target: min 90)
  Calcium                  1000.0 mg     (target: min 1000)
  Iron                       13.1 mg     (target: min 8)
  Potassium                3400.0 mg     (target: min 3400)
  Magnesium                 513.2 mg     (target: min 420)
  Zinc                       11.1 mg     (target: min 11)
  Vitamin B12                 6.9 mcg    (target: min 2.4)
  Folate                    400.0 mcg    (target: min 400)
  Thiamine                    1.2 mg     (target: min 1.2)
  Riboflavin                  2.7 mg     (target: min 1.3)
  Niacin                     29.7 mg     (target: min 16)

  Objective (weighted macro deviation): 0.000
============================================================
```
</details>
## Structure

```
diet-lp/
├── main.py                # solver, settings, and output
├── data.py                # example food database (checked into git)
└── data_local.py.example  # template for a personal food database (optional)
```

`data_local.py` is gitignored and does not exist after cloning — the tool runs fine without it, using the foods in `data.py`.

### Personal food database (optional)

To use your own foods instead of or in addition to the examples in `data.py`, create `data_local.py`:

```bash
cp data_local.py.example data_local.py
```

Both files are loaded automatically whenever they exist — no changes to `main.py` needed. `data_local.py` only needs to define `INGREDIENTS` and/or `RECIPES` lists using the same dict format as `data.py`.

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

`data.py` contains example food group lists as a starting point. Add your own foods in `data_local.py` (see above). Each entry is a Python dict.

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

Food groups are loaded from both `data.py` and `data_local.py` at the top of `main.py`. To exclude a group entirely, comment out the corresponding import lines there.

To add a new food group (e.g. `STAPLES`), define it as a named list in either data file and add the matching import lines in `main.py`.

## Notes

- The solver will concentrate quantities on a small number of nutritionally efficient foods unless you add `max_amount` caps to individual foods. That's expected in LP.
- As far as I know you can't actually optimize nutrition in this way, so don't think you're solving anything. This is for fun and education and testing but I wouldn't build my life around it.