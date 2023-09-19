def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
        Calculate BMI from height and weight

        Raise ValueError if:
            - Length of height and weight are not the same
            - Height or weight is not a positive integer or float

        Return a list of BMI
    """
    if height is None or weight is None:
        print("Height and weight must not be None")
        return []
    if not isinstance(height, list) or not isinstance(weight, list):
        print("Height and weight must be a list")
        return []
    if len(height) != len(weight):
        print("Length of height and weight must be the same")
        return []
    ret = []
    for h, w in zip(height, weight):
        if not isinstance(h, (float, int)) or not isinstance(w, (float, int)):
            print("Height and eight must be a integer or float")
            return []
        if h <= 0 or w <= 0:
            print("Height and weight must be a positive integer or float")
            return []
        ret.append(w / (h * h))
        
    return ret


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
        Apply limit to BMI

        Raise ValueError if:
            - BMI is not a integer or float
            - Limit is not a integer or float

        Return a list of boolean
    """
    if bmi is None:
        print("BMI must not be None")
        return []
    if not isinstance(bmi, list):
        print("BMI must be a list")
        return []
    for b in bmi:
        if not isinstance(b, (float, int)):
            print("BMI must be a integer or float")
            return []

    if not isinstance(limit, (int, float)):
        print("Limit must be a integer or float")
        return []

    return [b > limit for b in bmi]
