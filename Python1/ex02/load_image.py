from PIL import Image


def ft_load(path: str) -> list:
    """
        Load an image from path
        Return a list of pixel data
    """
    try:
        with Image.open(path) as img:
            pixel_data = list(img.getdata())
            print(f"The shape of the image is: ({img.height}, {img.width}, 3)")
            return pixel_data
    except FileNotFoundError:
        print("Image not found at path")
    except PermissionError:
        print("Error loading the image")
    return []
