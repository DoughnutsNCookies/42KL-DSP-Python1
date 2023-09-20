import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
        Slice a 2D array (list of lists) from start to end
        Print the shape of the original array and the sliced array
        Return the sliced array
    """
    try:
        if len(family) == 0:
            return []

        family_array = np.array(family)
        x, y = family_array.shape

        if family_array.ndim != 2:
            raise ValueError("family must be a 2D array")

        print(f"My shape is: ({x}, {y})")
        sliced_array = family_array[start:end]
        x_sliced, y_sliced = sliced_array.shape
        print(f"My new shape is: ({x_sliced}, {y_sliced})")
        return sliced_array.tolist()
    except Exception as err:
        print(err)
        return []

