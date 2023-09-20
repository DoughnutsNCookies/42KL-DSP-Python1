import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
        Calculate BMI from height and weight

        Raise ValueError if:
            - Length of height and weight are not the same
            - Height or weight is not a positive integer or float

        Return a list of BMI
    """
    try:
        if len(height) != len(weight):
            raise ValueError("Length of height and weight must be the same")

        height = np.array(height, dtype=float)
        weight = np.array(weight, dtype=float)

        if not np.all((height > 0) & (weight > 0)):
            raise ValueError("Height and weight must be positive values")

        return (weight / (height ** 2)).tolist()
    except Exception as err:
        print(err)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
        Apply limit to BMI

        Raise ValueError if:
            - BMI is not a integer or float
            - Limit is not a integer or float

        Return a list of boolean
    """
    try:
        bmi = np.array(bmi, dtype=float)
        limit = np.array(limit, dtype=float)

        if not np.issubdtype(bmi.dtype, np.floating):
            raise ValueError("BMI must be floating-point values")
        if not np.issubdtype(limit.dtype, np.floating):
            raise ValueError("Limit must be floating-point values")
        return (bmi > limit).tolist()
    except Exception as err:
        print(err)
        return []
