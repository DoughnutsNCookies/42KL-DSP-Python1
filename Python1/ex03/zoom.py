from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_zoom(path: str, factor: float) -> np.ndarray:
    """
    Zoom an image by a factor using NumPy.
    Return a NumPy array of pixel data.
    """
    try:
        pixel_data = ft_load(path)
        if factor == 1:
            new_pixel_data = pixel_data
        else:
            h, w, channels = pixel_data.shape

            if factor < 1:
                new_h = int(h / factor)
                new_w = int(w / factor)
                print(new_h, new_w)
                new_pixel_data = np.zeros((new_h, new_w, channels), dtype=np.uint8)

                paste_x = (new_w - w) // 2
                paste_y = (new_h - h) // 2

                new_pixel_data[paste_y:paste_y + h, paste_x:paste_x + w] = pixel_data
            else:
                x1 = (w - int(w / factor)) // 2
                x2 = x1 + int(w / factor)
                y1 = (h - int(h / factor)) // 2
                y2 = y1 + int(h / factor)

                new_pixel_data = pixel_data[y1:y2, x1:x2, :]

        print(f"New shape after slicing: {new_pixel_data.shape}")
        plt.imshow(new_pixel_data)
        plt.savefig("zoom.png")
        plt.show()

        return new_pixel_data
    except Exception as err:
        print(err)
        return np.array([])


def main():
    """
        Main function
    """
    # ft_zoom("animal.jpeg", 2)
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
