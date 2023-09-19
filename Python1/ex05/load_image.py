from PIL import Image


def ft_load(path: str) -> list:
    """
        Load an image from path
        Return a list of pixel data
    """
    try:
        with Image.open(path) as img:
            pixel_data = list(img.getdata())
            print("The shape of image is:"
                  f" ({img.height}, {img.width}, {len(img.getbands())})")
            ret_list = []
            for x in range(img.height):
                ret_list.append(pixel_data[x * img.width:(x + 1) * img.width])
            return ret_list
    except Exception as err:
        print(err)
        return []
