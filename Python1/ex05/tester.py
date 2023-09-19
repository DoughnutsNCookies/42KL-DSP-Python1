from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


def main():
    """
        Test main function
    """
    pixel_data = ft_load("landscape.jpeg")
    print(pixel_data)

    ft_invert(pixel_data)
    ft_red(pixel_data)
    ft_green(pixel_data)
    ft_blue(pixel_data)
    ft_grey(pixel_data)


if __name__ == "__main__":
    main()
