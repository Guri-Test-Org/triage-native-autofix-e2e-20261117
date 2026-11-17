"""Synthetic arithmetic functions for the public Auto-fix verification fixture."""
from statistics import mean


def clamp(value, lower, upper):
    """Clamp to inclusive bounds; reversed bounds are invalid."""
    if lower > upper:
        raise ValueError("lower must not exceed upper")
    return max(lower, min(value, upper))


def average(values):
    """Return the arithmetic mean, with zero for an empty sequence."""
    if not values:
        return 0
    return mean(values)
