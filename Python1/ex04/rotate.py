from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_rotate(path: str, angle: int) -> np.ndarray:
    """
    Rotate an image by an angle using NumPy.
    Return a NumPy array of pixel data.
    """
    try:
        if angle not in [0, 90, 180, 270]:
            raise ValueError("Angle must be 0, 90, 180, or 270")

        pixel_data = ft_load(path)
        print(pixel_data)

        if angle == 90:
            new_pixel_data = [list(rgb) for rgb in zip(*reversed(pixel_data))]
        elif angle == 180:
            new_pixel_data = [list(reversed(rgb)) for rgb in reversed(pixel_data)]
        elif angle == 270:
            new_pixel_data = [list(reversed(rgb)) for rgb in zip(*reversed(pixel_data))]

        new_pixel_data = np.array(new_pixel_data)
        print(f"New shape after rotation: {new_pixel_data.shape}")
        print(new_pixel_data)
        plt.imshow(new_pixel_data)
        plt.savefig("rotate.png")
        plt.show()

        return new_pixel_data
    except Exception as err:
        print(err)
        return np.array([])


def main():
    """
        Test function
    """
    # ft_rotate("animal.jpeg", 0)
    # ft_rotate("animal.jpeg", 90)
    # ft_rotate("animal.jpeg", 180)
    ft_rotate("animal.jpeg", 270)
    # ft_rotate("None", 0)
    # ft_rotate(None, 0)
    # ft_rotate("animal.jpeg", 1)
    # ft_rotate("animal.jpeg", "a")


if __name__ == "__main__":
    main()
