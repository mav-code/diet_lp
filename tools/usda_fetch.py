#!/usr/bin/env python3
"""
tools/usda_fetch.py

Look up foods in USDA FoodData Central and generate diet-lp INGREDIENTS entries.
All entries are output as per-100g ingredients (unit: "100g", grams: 100).

Modes
-----
Single (print to stdout):
    python3 tools/usda_fetch.py "chicken breast"

Single (append to file):
    python3 tools/usda_fetch.py "chicken breast" --dest foods/usda.py

Batch (text file of queries, one per line; append each accepted entry):
    python3 tools/usda_fetch.py --batch queries.txt --dest foods/usda.py

Requirements
------------
FDC_API_KEY must be set in .env or the environment.
See README for how to get a free API key.
"""

import argparse
import os
import sys

from dotenv import load_dotenv
from usda_fdc import FdcClient
from usda_fdc.exceptions import FdcApiError

load_dotenv()

# ---------------------------------------------------------------------------
# Nutrient mapping: USDA nutrient_nbr → our key
# ---------------------------------------------------------------------------

NUTRIENT_MAP = {
    1008: "calories",     # Energy (kcal)
    1005: "carbs",        # Carbohydrate, by difference
    1004: "fat",          # Total lipid (fat)
    1003: "protein",      # Protein
    1093: "sodium",       # Sodium, Na
    1253: "cholesterol",  # Cholesterol
    1079: "fiber",        # Fiber, total dietary
    1162: "vitamin_c",    # Vitamin C, total ascorbic acid
    1087: "calcium",      # Calcium, Ca
    1089: "iron",         # Iron, Fe
    1092: "potassium",    # Potassium, K
    1090: "magnesium",    # Magnesium, Mg
    1095: "zinc",         # Zinc, Zn
    1178: "b12",          # Vitamin B-12
    1177: "folate",       # Folate, total
    1165: "thiamine",     # Thiamin
    1166: "riboflavin",   # Riboflavin
    1167: "niacin",       # Niacin
}

NUTRIENT_ORDER = [
    "calories", "carbs", "fat", "protein",
    "sodium", "cholesterol", "fiber",
    "vitamin_c", "calcium", "iron", "potassium", "magnesium",
    "zinc", "b12", "folate", "thiamine", "riboflavin", "niacin",
]

NUTRIENT_UNITS = {
    "calories": "kcal", "carbs": "g", "fat": "g", "protein": "g",
    "sodium": "mg", "cholesterol": "mg", "fiber": "g",
    "vitamin_c": "mg", "calcium": "mg", "iron": "mg",
    "potassium": "mg", "magnesium": "mg", "zinc": "mg",
    "b12": "mcg", "folate": "mcg",
    "thiamine": "mg", "riboflavin": "mg", "niacin": "mg",
}

FDC_URL = "https://fdc.nal.usda.gov/food-details/{fdc_id}/nutrients"

# Data types to include in searches (excludes Branded to favour whole foods)
SEARCH_DATA_TYPES = ["Foundation", "SR Legacy", "Survey (FNDDS)"]

# ---------------------------------------------------------------------------
# Core helpers
# ---------------------------------------------------------------------------

def extract_nutrients(food):
    """Return dict of our nutrient keys from a fully-fetched Food object."""
    result = {}
    for n in food.nutrients:
        nbr = n.nutrient_nbr
        if nbr is None:
            continue
        key = NUTRIENT_MAP.get(int(nbr))
        if key:
            result[key] = round(n.amount, 3) if n.amount is not None else None
    return result


def format_entry(food, nutrients):
    """Format a food+nutrients dict as a Python literal string."""
    name = food.description
    link = FDC_URL.format(fdc_id=food.fdc_id)

    nutrient_pairs = []
    for key in NUTRIENT_ORDER:
        val = nutrients.get(key)
        nutrient_pairs.append(f'        "{key}": {val}')

    nutrients_block = ",\n".join(nutrient_pairs)

    return (
        "{\n"
        f'    "name": {name!r}, "unit": "100g", "grams": 100,\n'
        f'    "link": {link!r},\n'
        "    \"nutrients\": {\n"
        f"{nutrients_block},\n"
        "    },\n"
        "}"
    )


def search_and_pick(client, query, page_size=10):
    """
    Search USDA for query, show results, prompt user to pick one or skip.
    Returns (Food, nutrients) or None if skipped.
    """
    print(f"\nSearching: {query!r}")
    try:
        results = client.search(query, data_type=SEARCH_DATA_TYPES, page_size=page_size)
    except FdcApiError as e:
        print(f"  API error: {e}")
        return None

    foods = results.foods
    if not foods:
        print("  No results.")
        return None

    print()
    for i, f in enumerate(foods, 1):
        cat = f.food_category or f.data_type or ""
        print(f"  [{i:2}] {f.description}  ({cat})")
    print(f"  [ s] Skip\n")

    while True:
        raw = input("Pick: ").strip().lower()
        if raw == "s":
            return None
        if raw.isdigit() and 1 <= int(raw) <= len(foods):
            chosen = foods[int(raw) - 1]
            break
        print(f"  Enter 1–{len(foods)} or s.")

    print(f"  Fetching details for FDC ID {chosen.fdc_id}…")
    try:
        food = client.get_food(chosen.fdc_id)
    except FdcApiError as e:
        print(f"  API error: {e}")
        return None

    return food, extract_nutrients(food)


def preview_and_confirm(food, nutrients):
    """Print a preview and ask the user to accept or skip. Returns True if accepted."""
    print("\n--- Preview ---")
    print(format_entry(food, nutrients))
    print("---")
    missing = [k for k in NUTRIENT_ORDER if nutrients.get(k) is None]
    if missing:
        print(f"  Note: missing nutrients (will be None): {', '.join(missing)}")
    while True:
        ans = input("Accept? [y/n]: ").strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no", "s", "skip"):
            return False
        print("  Enter y or n.")

# ---------------------------------------------------------------------------
# File I/O
# ---------------------------------------------------------------------------

_BOILERPLATE = '''\
"""
{filename}  (auto-generated by tools/usda_fetch.py)

USDA FoodData Central ingredients. All nutrients are per 100g.
"""

INGREDIENTS = [
]
'''


def _ensure_file(path):
    """Create path with boilerplate if it does not exist."""
    if not os.path.exists(path):
        filename = os.path.basename(path)
        with open(path, "w") as f:
            f.write(_BOILERPLATE.format(filename=filename))
        print(f"  Created {path}")


def append_to_file(dest_path, entry_str):
    """Insert entry_str just before the closing ] of the INGREDIENTS list."""
    _ensure_file(dest_path)

    with open(dest_path, "r") as f:
        content = f.read()

    insert_at = content.rfind("]")
    if insert_at == -1:
        # Fallback: just append
        with open(dest_path, "a") as f:
            f.write("\n" + entry_str + ",\n")
        print(f"  Appended to {dest_path} (fallback — no ']' found)")
        return

    indented = "\n".join(
        "    " + line if line.strip() else ""
        for line in entry_str.split("\n")
    )
    new_content = content[:insert_at] + indented + ",\n" + content[insert_at:]
    with open(dest_path, "w") as f:
        f.write(new_content)
    print(f"  Written to {dest_path}")

# ---------------------------------------------------------------------------
# Modes
# ---------------------------------------------------------------------------

def run_single(client, query, dest=None):
    result = search_and_pick(client, query)
    if result is None:
        print("Skipped.")
        return
    food, nutrients = result
    if dest:
        if preview_and_confirm(food, nutrients):
            append_to_file(dest, format_entry(food, nutrients))
        else:
            print("Skipped.")
    else:
        print("\n" + format_entry(food, nutrients))


def run_batch(client, batch_file, dest):
    with open(batch_file) as f:
        queries = [
            line.strip() for line in f
            if line.strip() and not line.strip().startswith("#")
        ]

    total = len(queries)
    print(f"Batch: {total} queries from {batch_file!r} → {dest!r}")
    accepted = 0

    for i, query in enumerate(queries, 1):
        print(f"\n[{i}/{total}]", end="")
        result = search_and_pick(client, query)
        if result is None:
            print("Skipped.")
            continue
        food, nutrients = result
        if preview_and_confirm(food, nutrients):
            append_to_file(dest, format_entry(food, nutrients))
            accepted += 1
        else:
            print("Skipped.")

    print(f"\nDone: {accepted}/{total} entries written to {dest}")

# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Fetch USDA FoodData Central entries and output diet-lp INGREDIENTS."
    )
    parser.add_argument("query", nargs="?", help="Food name to search for")
    parser.add_argument(
        "--dest", metavar="FILE",
        help="Append accepted entry to this .py file (created if absent)",
    )
    parser.add_argument(
        "--batch", metavar="FILE",
        help="Text file of food queries, one per line (requires --dest)",
    )
    args = parser.parse_args()

    if args.batch and not args.dest:
        parser.error("--batch requires --dest")
    if not args.batch and not args.query:
        parser.error("Provide a query or use --batch FILE --dest FILE")

    api_key = os.environ.get("FDC_API_KEY")
    if not api_key:
        sys.exit(
            "Error: FDC_API_KEY not set.\n"
            "Add it to a .env file in the project root (see README)."
        )

    client = FdcClient(api_key=api_key)

    if args.batch:
        run_batch(client, args.batch, args.dest)
    else:
        run_single(client, args.query, args.dest)


if __name__ == "__main__":
    main()
