import numpy as np
from PIL import Image


def ft_invert(array) -> np.array:
    """Inverts the colors of the image represented by the given array.
    Args:
        array (np.array): A numpy array representing the image.
    Returns:
        np.array: A new numpy array with the colors inverted.
    """
    if len(array.shape) != 3:
        raise TypeError("the array not corrected!!")
    height, width = array.shape[:2]
    inverted = np.zeros_like(array)
    for y in range(height):
        for x in range(width):
            r, g, b = array[y][x]
            inverted[y][x] = [255 - r, 255 - g, 255 - b]
    Image.fromarray(inverted).show()
    return inverted


def ft_red(array) -> np.array:
    """Displays the red channel of the image represented by the given array.
    Args:
        array (np.array): A numpy array representing the image.
    Returns:
        np.array: A new numpy array with only the red channel displayed.
    """
    if len(array.shape) != 3:
        raise TypeError("the array not corrected!!")
    red_only = (array * [1, 0, 0]).astype(np.uint8)
    Image.fromarray(red_only).show()
    return red_only


def ft_green(array) -> np.array:
    """Displays the green channel of the image represented by the given array.
    Args:
        array (np.array): A numpy array representing the image.
    Returns:
        np.array: A new numpy array with only the green channel displayed.
    """
    if len(array.shape) != 3:
        raise TypeError("the array not corrected!!")
    height, width = array.shape[:2]
    green_only = np.zeros_like(array)
    for y in range(height):
        for x in range(width):
            r, g, b = array[y][x]
            green_only[y][x] = [r - r, g, b - b]
    Image.fromarray(green_only).show()
    return green_only


def ft_blue(array) -> np.array:
    """Displays the blue channel of the image represented by the given array.
    Args:
        array (np.array): A numpy array representing the image.
    Returns:
        np.array: A new numpy array with only the blue channel displayed.
    """
    if len(array.shape) != 3:
        raise TypeError("the array not corrected!!")
    height, width = array.shape[:2]
    blue_only = np.zeros_like(array)
    for y in range(height):
        for x in range(width):
            r, g, b = array[y][x]
            blue_only[y][x] = [0, 0, b]
    Image.fromarray(blue_only).show()
    return blue_only


def ft_grey(array) -> np.array:
    """Converts the image represented by the given array to greyscale.
    Args:
        array (np.array): A numpy array representing the image.
    Returns:
        np.array: A new numpy array with the image converted to greyscale.
    """
    if len(array.shape) != 3:
        raise TypeError("the array not corrected!!")
    height, width = array.shape[:2]
    greyscale = np.zeros_like(array)
    for y in range(height):
        for x in range(width):
            r, g, b = array[y][x]
            greyscale[y][x] = [g, g, g]
    Image.fromarray(greyscale).show()
    return greyscale
