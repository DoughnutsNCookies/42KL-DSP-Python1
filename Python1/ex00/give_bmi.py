"""
    Normal weight = 18.5 - 24.9
"""


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight):
        raise ValueError("Length of height and weight must be the same")
    for h in height:
        if not (isinstance(h, float) or isinstance(h, int)) or h <= 0:
            raise ValueError("Height must be a positive integer or float")
    for w in weight:
        if not (isinstance(w, float) or isinstance(w, int)) or w <= 0:
            raise ValueError("Weight must be a positive integer or float")

    return [w / (h * h) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    for b in bmi:
        if not (isinstance(b, float) or isinstance(b, int)):
            raise ValueError("BMI must be a integer or float")

    if not (isinstance(limit, int) or isinstance(limit, float)):
        raise ValueError("Limit must be a integer or float")

    return [b > limit for b in bmi]
