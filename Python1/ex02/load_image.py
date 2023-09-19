from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from path using NumPy.
    Return a NumPy array of pixel data.
    """
    try:
        with Image.open(path) as img:
            pixel_data = np.array(img)
            height, width, channels = pixel_data.shape
            print(f"The shape of image is: ({height}, {width}, {channels})")
            return pixel_data
    except Exception as err:
        print(err)
        return np.array([])
