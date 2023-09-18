def slice_me(family: list, start: int, end: int) -> list:
    """
        Slice a 2D array (list of lists) from start to end
        Print the shape of the original array and the sliced array
        Return the sliced array
    """
    if not isinstance(family, list):
        print("family is not a list")
        return []

    if not (isinstance(start, int) and isinstance(end, int)):
        print("start and end must be integers")
        return []

    x = len(family)
    y = len(family[0])
    for f in family:
        if len(f) != y:
            print("Not all rows have the same length")
            return []

    print(f"My shape is : ({x}, {y})")
    ret = slice(start, end)
    sliced_family = family[ret]

    x = len(sliced_family)
    print(f"My new shape is : ({x}, {y})")
    return sliced_family
