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
        return [w / (h * h) for h, w in zip(height, weight)]
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
        return [b > limit for b in bmi]
    except Exception as err:
        print(err)
        return []
