from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_rotate(path: str, angle: int) -> list:
    """
        Rotate an image by an angle
        Return a list of pixel data
    """
    if not isinstance(path, str):
        print("Path must be a string")
        return []

    if not isinstance(angle, (int, float)):
        print("Angle must be an integer or a float")
        return []

    if angle not in [0, 90, 180, 270]:
        print("Angle must be 0, 90, 180 or 270")
        return []

    pixel_data = ft_load(path)
    if not pixel_data:
        return []
    print(pixel_data)

    if angle == 0:
        new_pixel_data = pixel_data
    elif angle == 90:
        new_pixel_data = [list(rgb) for rgb in zip(*reversed(pixel_data))]
    elif angle == 180:
        new_pixel_data = [list(reversed(rgb)) for rgb in reversed(pixel_data)]
    elif angle == 270:
        new_pixel_data = [list(reversed(rgb))
                          for rgb in zip(*reversed(pixel_data))]
    image_array = np.array(new_pixel_data, dtype=np.uint8)

    print("New shape after Transpose:"
          f"({len(new_pixel_data)}, {len(new_pixel_data[0])}, 3)")
    print(new_pixel_data)
    plt.imshow(image_array)
    plt.savefig("rotate.png")
    return new_pixel_data


def main():
    """
        Test function
    """
    # ft_rotate("animal.jpeg", 0)
    # ft_rotate("animal.jpeg", 90)
    # ft_rotate("animal.jpeg", 180)
    ft_rotate("animal.jpeg", 270)


if __name__ == "__main__":
    main()
