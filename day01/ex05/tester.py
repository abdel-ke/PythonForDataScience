from pimp_image import ft_blue, ft_green, ft_grey, ft_invert, ft_red
from load_image import ft_load

if __name__ == "__main__":
    array = ft_load("../landscape.jpg")
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)
    print(ft_invert.__doc__)
