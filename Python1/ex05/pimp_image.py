import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array) -> list:
    """
        Invert an image
        Return a list of pixel data
    """
    try:
        inverted_pixel_value = [
            [tuple(255 - value for value in pixel) for pixel in row]
            for row in array
        ]

        print("Inverted pixel value:")
        print(inverted_pixel_value)

        image_array = np.array(inverted_pixel_value, dtype=np.uint8)
        plt.imshow(image_array)
        plt.savefig("invert.png")
        return inverted_pixel_value
    except Exception as err:
        print(err)
        return []


def ft_color(array, color: str) -> list:
    """
        Colors an image
        Return a list of pixel data
    """
    try:
        pixel_values = []

        color_map = {
            "red": 0,
            "green": 1,
            "blue": 2
        }

        pixel_values = [[tuple(pixel[i] if i == color_map[color] else 0
                        for i in range(3))
                        for pixel in row]
                        for row in array]

        print(color.capitalize() + " pixel value:")
        print(pixel_values)

        image_array = np.array(pixel_values, dtype=np.uint8)
        plt.imshow(image_array)
        plt.savefig(color + ".png")
        return pixel_values
    except Exception as err:
        print(err)
        return []


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
        grey_pixel_values = []

        grey_pixel_values = [
            [(max(pixel[0], pixel[1], pixel[2]),) * 3 for pixel in row]
            for row in array
        ]

        print("Grey pixel value:")
        print(grey_pixel_values)

        image_array = np.array(grey_pixel_values, dtype=np.uint8)
        plt.imshow(image_array)
        plt.savefig("grey.png")
        return grey_pixel_values
    except Exception as err:
        print(err)
        return []
