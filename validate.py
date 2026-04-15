"""
diet_lp/validate.py

Validates food entries before they are passed to the solver.
Call validate_foods(foods) and check the returned list; if non-empty,
each item is a human-readable error string and the run should be aborted.
"""

VALID_UNITS = {"100g", "1 serving"}

KNOWN_NUTRIENT_KEYS = {
    "calories", "carbs", "fat", "protein",
    "sodium", "cholesterol", "fiber",
    "vitamin_c", "calcium", "iron", "potassium", "magnesium",
    "zinc", "b12", "folate", "thiamine", "riboflavin", "niacin",
}


def validate_foods(foods):
    """
    Returns a list of error strings. An empty list means all entries are valid.
    Collects all errors rather than stopping at the first.
    Note: duplicate-name conflicts are handled upstream by deduplicate_foods().
    """
    errors = []

    for i, food in enumerate(foods):
        # Use name for error messages if available, else fall back to index.
        raw_name = food.get("name")
        label = f"{raw_name!r}" if isinstance(raw_name, str) and raw_name.strip() \
                else f"entry #{i + 1}"

        # --- name ---
        if not isinstance(raw_name, str) or not raw_name.strip():
            errors.append(f"{label}: 'name' must be a non-empty string")

        # --- unit ---
        if food.get("unit") not in VALID_UNITS:
            errors.append(
                f"{label}: 'unit' is {food.get('unit')!r}; must be one of {VALID_UNITS}"
            )

        # --- grams ---
        grams = food.get("grams")
        if not isinstance(grams, (int, float)) or grams <= 0:
            errors.append(f"{label}: 'grams' must be a positive number (got {grams!r})")

        # --- min_amount / max_amount ---
        min_amt = food.get("min_amount")
        max_amt = food.get("max_amount")
        if min_amt is not None:
            if not isinstance(min_amt, (int, float)) or min_amt < 0:
                errors.append(
                    f"{label}: 'min_amount' must be a non-negative number (got {min_amt!r})"
                )
        if max_amt is not None:
            if not isinstance(max_amt, (int, float)) or max_amt < 0:
                errors.append(
                    f"{label}: 'max_amount' must be a non-negative number (got {max_amt!r})"
                )
        if isinstance(min_amt, (int, float)) and isinstance(max_amt, (int, float)):
            if max_amt < min_amt:
                errors.append(
                    f"{label}: 'max_amount' ({max_amt}) is less than 'min_amount' ({min_amt})"
                )

        # --- nutrients ---
        nutrients = food.get("nutrients")
        if not isinstance(nutrients, dict):
            errors.append(f"{label}: 'nutrients' must be a dict (got {type(nutrients).__name__})")
            continue  # can't inspect nutrient values without a dict

        unknown = set(nutrients.keys()) - KNOWN_NUTRIENT_KEYS
        if unknown:
            errors.append(f"{label}: unknown nutrient keys: {sorted(unknown)}")

        for key, val in nutrients.items():
            if val is None:
                continue  # treated as 0 by the solver
            if not isinstance(val, (int, float)):
                errors.append(
                    f"{label}: nutrient {key!r} has non-numeric value {val!r}"
                )
            elif val < 0:
                errors.append(
                    f"{label}: nutrient {key!r} is negative ({val})"
                )

    return errors
