import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def crop_center_image(data):
    """Crop the center of a 2D NumPy array (grayscale image)
    Args:
        data (np.array): The input image as a 2D NumPy array with shape
        (height, width).
    Returns:
        np.array: The cropped image as a 2D NumPy array."""
    height, width = data.shape[:2]
    start_x = int(width / 2.2)
    end_x = int((width / 2.6) + start_x)
    start_y = int(height / 10)
    end_y = int((height / 1.8) + start_y)
    zoomed = data[start_y:end_y, start_x:end_x]
    return zoomed


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
    """Main function to demonstrate image loading, cropping
    , and transposing."""
    try:
        data = ft_load("../animal.jpeg")
        clipped = crop_center_image(data)
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
