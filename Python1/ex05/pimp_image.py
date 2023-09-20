import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array) -> list:
    """
        Invert an image
        Return a list of pixel data
    """
    try:
        inverted_pixel_value = 255 - array

        print("Inverted pixel value:")
        print(inverted_pixel_value)

        plt.imshow(inverted_pixel_value)
        plt.savefig("invert.png")
        return inverted_pixel_value
    except Exception as err:
        print(err)
        return []


def ft_color(array: np.ndarray, color: str) -> np.ndarray:
    """
    Color an image using NumPy.
    Return a NumPy array of pixel data.
    """
    try:
        if not isinstance(array, np.ndarray):
            raise TypeError("Input must be a NumPy array")

        if color not in ["red", "green", "blue"]:
            raise ValueError("Color must be 'red', 'green', or 'blue'")

        color_channel = {
            "red": [1, 2],
            "green": [0, 2],
            "blue": [0, 1]
        }[color]

        pixel_values = array.copy()
        pixel_values[:, :, color_channel] = 0

        print(color.capitalize() + " pixel value:")
        print(pixel_values)

        plt.imshow(pixel_values)
        plt.savefig(color + ".png")
        plt.show()

        return pixel_values
    except Exception as err:
        print(err)
        return np.array([])


def ft_red(array) -> list:
    """
        Red an image
        Return a list of pixel data
    """
    return ft_color(array, "red")


def ft_green(array) -> list:
    """
        Green an image
        Return a list of pixel data
    """
    return ft_color(array, "green")


def ft_blue(array) -> list:
    """
        Blue an image
        Return a list of pixel data
    """
    return ft_color(array, "blue")


def ft_grey(array) -> list:
    """
        Grey an image
        Return a list of pixel data
    """
    try:
        max_values = np.mean(array, axis=2, keepdims=True)
        grey_pixel_values = np.repeat(max_values, 3, axis=2)

        print("Grey pixel value:")
        print(grey_pixel_values)

        image_array = np.array(grey_pixel_values, dtype=np.uint8)
        plt.imshow(image_array)
        plt.savefig("grey.png")
        return grey_pixel_values
    except Exception as err:
        print(err)
        return []
