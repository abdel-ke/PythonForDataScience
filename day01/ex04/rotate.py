import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def transpose_image(data) -> np.array:
    """Transpose the given 2D NumPy array (image)
    by swapping its rows and columns.
    Args:
        data (np.array): The input image as a 2D NumPy array.
    Returns:
        np.array: The rotated image as a 2D NumPy array.
    """
    height, width = data.shape[:2]
    transposed = np.zeros((width, height), dtype=int)

    for y in range(height):
        for x in range(width):
            transposed[x][y] = data[y][x]
    return transposed


def main():
    try:
        data = ft_load("../a nimal.jpeg")
        start_x, end_x = 460, 850
        start_y, end_y = 70, 500
        clipped = data[start_y: end_y, start_x: end_x]
        # display shape and data of image
        print(f"The shape of image is: {clipped.shape}")
        print(clipped)
        # rotate image
        transposed = transpose_image(clipped)
        # print shape and data of the rotated image
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)
        plt.imshow(transposed, cmap='gray')
        plt.show()
        plt.close()
    except Exception as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":
    main()
