"""
diet_lp/settings.py

All user-configurable solver parameters. Edit this file to adjust targets,
bounds, and weights without touching solver or output code.
"""

# Calorie bounds (hard constraints)
CALORIE_MIN = 1600
CALORIE_MAX = 1795

# Macro targets for goal programming.
# The solver minimizes weighted deviation from these targets.
# Targets are set to the midpoint of each range by default;
# adjust to bias toward one end.
MACRO_TARGETS = {
    "carbs":   122,   # g  (range 20–225)
    "fat":      80,   # g  (range 61–100)
    "protein": 203,   # g  (range 71–225, adjusted upwards based on advice)
}

# Macro hard bounds (the solver may not exceed/fall below these regardless)
MACRO_BOUNDS = {
    "carbs":   (20,  225),
    "fat":     (61,  100),
    "protein": (71,  225),
}

# Objective weights for over/under deviation per macro.
# Higher weight = solver tries harder to avoid that deviation.
# Asymmetric: e.g. undershooting protein is penalized more than overshooting.
MACRO_WEIGHTS = {
    #              (over, under)
    "carbs":       (1.0,  1.0),
    "fat":         (2.0,  2.0),   # tighter range, penalize deviation more
    "protein":     (1.0,  3.0),   # undershooting protein costs more
}

# Hard upper bounds on harmful nutrients
SODIUM_MAX      = 1500  # mg
CHOLESTEROL_MAX = 200   # mg

# Hard lower bound on fiber
FIBER_MIN = 31  # g

# Micronutrient minimums (RDA/AI values, NIH Office of Dietary Supplements)
# These are hard lower bounds — the solver must satisfy all of them.
MICRONUTRIENT_MINS = {
    "vitamin_c":  90,    # mg   (RDA adult male; 75 for female)
    "calcium":    1000,  # mg
    "iron":       8,     # mg   (RDA adult male; 18 for premenopausal female)
    "potassium":  3400,  # mg   (AI)
    "magnesium":  420,   # mg   (RDA adult male; 320 for female)
    "zinc":       11,    # mg   (RDA adult male; 8 for female)
    "b12":        2.4,   # mcg
    "folate":     400,   # mcg  (DFE)
    "thiamine":   1.2,   # mg
    "riboflavin": 1.3,   # mg
    "niacin":     16,    # mg   (NE)
}
