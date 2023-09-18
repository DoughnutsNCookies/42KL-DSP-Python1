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
        print("Length of height and weight must be the same")
        return []
    for h in height:
        if not (isinstance(h, float) or isinstance(h, int)):
            print("Height must be a integer or float")
            return []
        if h <= 0:
            print("Height must be a positive integer or float")
            return []
    for w in weight:
        if not (isinstance(w, float) or isinstance(w, int)):
            print("Weight must be a integer or float")
            return []
        if w <= 0:
            print("Weight must be a positive integer or float")
            return []

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
            print("BMI must be a integer or float")
            return []

    if not (isinstance(limit, int) or isinstance(limit, float)):
        print("Limit must be a integer or float")
        return []

    return [b > limit for b in bmi]
