"""Helper utilities.

This module will hold reusable helper functions for math, formatting,
and common gameplay utilities.
"""


def clamp(value: float, min_value: float, max_value: float) -> float:
    """Clamp a number between min and max (placeholder utility)."""

    return max(min_value, min(value, max_value))
