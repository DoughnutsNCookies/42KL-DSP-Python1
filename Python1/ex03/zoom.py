from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_zoom(path: str, factor: int) -> list:
    """
        Zoom an image by a factor
        Return a list of pixel data
    """
    try:
        if not isinstance(factor, (int, float)):
            raise TypeError("Factor must be an integer or a float")

        if factor <= 0:
            raise ValueError("Factor must be greater than 0")

        pixel_data = ft_load(path)
        print(pixel_data)

        if factor == 1:
            new_pixel_data = pixel_data
            new_h, new_w = len(pixel_data), len(pixel_data[0])
        else:
            w, h = len(pixel_data[0]), len(pixel_data)
            new_w = int(w / factor)
            new_h = int(h / factor)
            if factor < 1:
                new_pixel_data = [(0, 0, 0)] * new_w
                new_pixel_data = [new_pixel_data.copy() for _ in range(new_h)]

                paste_x = (new_w - w) // 2
                paste_y = (new_h - h) // 2

                for y in range(h):
                    for x in range(w):
                        new_pixel_data[y + paste_y][x + paste_x] = pixel_data[y][x]
            else:
                x1 = (w - new_w) // 2
                x2 = x1 + new_w
                y1 = (h - new_h) // 2
                y2 = y1 + new_h

                new_pixel_data = [row[x1:x2] for row in pixel_data[y1:y2]]

        print(f"New shape after slicing: ({new_h}, {new_w}, 3)")
        print(new_pixel_data)
        image_array = np.array(new_pixel_data, dtype=np.uint8)

        plt.imshow(image_array)
        plt.savefig("zoom.png")  # plt.show()
        return new_pixel_data
    except Exception as err:
        print(err)
        return []


def main():
    """
        Main function
    """
    ft_zoom("animal.jpeg", 2)
    # ft_zoom("animal.jpeg", 1)
    # ft_zoom("animal.jpeg", 0)
    # ft_zoom("animal.jpeg", 0.5)
    # ft_zoom("1", 2)
    # ft_zoom(1, 2)
    # ft_zoom("animal.jpeg", "a")
    # ft_zoom("animal.jpeg", 0)
    # ft_zoom("animal.jpeg", -1)
    # ft_zoom("animal.jpeg", None)
    # ft_zoom(None, 1)


if __name__ == "__main__":
    main()
