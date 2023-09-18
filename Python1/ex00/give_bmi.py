"""
    Normal weight = 18.5 - 24.9
"""


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
        Calculate BMI from height and weight

        Raise ValueError if:
            - Length of height and weight are not the same
            - Height or weight is not a positive integer or float

        Return a list of BMI
    """
    if len(height) != len(weight):
        raise ValueError("Length of height and weight must be the same")
    for h in height:
        if not (isinstance(h, float) or isinstance(h, int)):
            raise TypeError("Height must be a integer or float")
        if h <= 0:
            raise ValueError("Height must be a positive integer or float")
    for w in weight:
        if not (isinstance(w, float) or isinstance(w, int)):
            raise TypeError("Weight must be a integer or float")
        if w <= 0:
            raise ValueError("Weight must be a positive integer or float")

    return [w / (h * h) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
        Apply limit to BMI

        Raise ValueError if:
            - BMI is not a integer or float
            - Limit is not a integer or float

        Return a list of boolean
    """
    for b in bmi:
        if not (isinstance(b, float) or isinstance(b, int)):
            raise TypeError("BMI must be a integer or float")

    if not (isinstance(limit, int) or isinstance(limit, float)):
        raise TypeError("Limit must be a integer or float")

    return [b > limit for b in bmi]
