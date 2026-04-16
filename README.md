# diet-lp

Given a set of foods and nutritional targets, the solver finds the quantities of each food that minimize deviation from your macro targets while satisfying hard constraints on calories, sodium, cholesterol, fiber, and a set of micronutrients.

This is a toy for exploring Google's Linear Programming solver [OR-Tools](https://developers.google.com/optimization) (GLOP solver) by expanding on their implementation of the [Stigler diet problem](https://developers.google.com/optimization/lp/stigler_diet), towards a functionality resembling that of [Eat This Much](https://www.eatthismuch.com/).

The example database contains all the foods in the Stigler problem, plus many more, and is set up to allow you to enter more foods manually or even [fetch them](#usda-importer). The tool's results are not serious (let alone optimal) nutritional advice, just as the original Stigler problem wasn't; but it moves in that direction. Neither Claude Code nor myself are trustworthy nutrition experts, and I don't know which of us is worse.

The specific number targets in here are just whatever I happen to have been playing around with. Customize them for your own needs in `settings.py`.

## Requirements

- Python 3.8+

```bash
pip install -r requirements.txt
```

## Usage

```bash
python3 main.py
```

<details>

<summary>Here's what the solution will look like if you don't edit any targets in the [settings file](#settings), or add or remove any foods from the `foods` directory.</summary>

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

<details>
<summary>File tree</summary>

```
diet-lp/
├── main.py          # solver and output
├── settings.py      # all nutritional targets and bounds — edit this to configure
├── loader.py        # food file loading and deduplication
├── validate.py      # input validation
├── requirements.txt
├── foods/
│   ├── stigler.py         # Stigler (1945) commodity set
│   ├── usda.py            # additional USDA SR Legacy ingredients
│   ├── recipes.py         # example recipes
│   └── local_example.py   # template for a personal food file (optional)
└── tools/
    └── usda_fetch.py      # interactive USDA FoodData Central importer
```

</details>
<br>
Every `.py` file in `foods/` is loaded automatically. Drop any file defining `INGREDIENTS` and/or `RECIPES` lists there and it will be picked up on the next run — no changes to any other file needed. For instance, you can put more foods in `local_example.py`, or a renamed copy of it. Conversely, to exclude foods you could delete them or comment them out of these files.

### Settings

All nutritional targets and bounds live in `settings.py`:

- **Calorie bounds** — hard min/max
- **Macro targets** — the solver minimizes weighted deviation from these
- **Macro bounds** — hard min/max per macro regardless of target
- **Macro weights** — tune over/undershoot penalties per macro; asymmetric weights are supported
- **Sodium, cholesterol** — hard upper bounds
- **Fiber** — hard lower bound
- **Micronutrient minimums** — hard lower bounds for Vitamin C, Calcium, Iron, Potassium, Magnesium, Zinc, B12, Folate, Thiamine, Riboflavin, and Niacin

### Food database

The `foods/` directory contains the food database. Each entry is a Python dict. The `INGREDIENTS`/`RECIPES` list names are organizational conventions only — what actually controls solver behavior is the `"unit"` field:

- `"unit": "100g"` — nutrients per 100g; solver variable is grams consumed
- `"unit": "1 serving"` — nutrients per serving; solver variable is servings consumed

<details>
<summary>Examples</summary>

```python
# Ingredient
{"name": "Chicken breast, raw", "unit": "100g", "grams": 100,
 "nutrients": {"calories": 120, "carbs": 0, "fat": 2.6, "protein": 22.5, ...}}

# Recipe
{"name": "Lentil soup (1 serving ~400g)", "unit": "1 serving", "grams": 400,
 "nutrients": {"calories": 220, "carbs": 38.0, "fat": 3.5, "protein": 13.0, ...}}
```

</details>
<br>
Nutrient values can be sourced from [USDA FoodData Central](https://fdc.nal.usda.gov/), or imported directly with `tools/usda_fetch.py` (see below).

#### Per-food bounds

You can specify minima and maxima for the solver to abide by:

```python
{"name": "Tuna, canned in water", "max_amount": 85, ...}   # ~1 can/day mercury limit
{"name": "Oats, rolled, dry", "min_amount": 200, "max_amount": 200, ...}  # fixed staple
```

#### Validation and deduplication

On load, all entries are validated (malformed entries abort the run with a clear error message). Entries that are nutritionally identical but differently named are merged into a single solver variable with a combined name (e.g. `"Bluefruit / Redfruit"`), reflecting that either option satisfies the solution. Same-name entries with conflicting nutrient data are an error.

### USDA importer

This repo includes a helper tool, `tools/usda_fetch.py`, which looks up foods in [USDA FoodData Central](https://fdc.nal.usda.gov/) by name and generates ready-to-use INGREDIENTS entries. It always outputs per-100g entries.

<details>
<summary>Importer Setup and Use </summary>

get a free API key at <https://fdc.nal.usda.gov/api-guide.html>, then add it to a `.env` file in the project root:

```
FDC_API_KEY=your_key_here
```

**Look up a single ingredient and print it in our data format:**
```bash
python3 tools/usda_fetch.py "chicken breast"
```

**Look up a single ingredient and append its return to a specified file destination:**
```bash
python3 tools/usda_fetch.py "chicken breast" --dest foods/usda.py
```

**Look up a batch of ingredients from a text file, one name per line:**
```bash
python3 tools/usda_fetch.py --batch queries.txt --dest foods/usda.py
```

Each flow is interactive: you pick from up to 10 search results, preview the generated entry, and accept or skip.

</details>