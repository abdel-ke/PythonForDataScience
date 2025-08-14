import numpy as np
from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt


def crop_center_image(data):
    """Crop the center of a 3D NumPy array (RGB image)
    Args:
        data (np.array): The input image as a 3D NumPy array with shape
        (height, width, channels).
    Returns:
        np.array: The cropped image as a 3D NumPy array."""
    height, width = data.shape[:2]
    start_x = int(width / 2.2)
    end_x = int((width / 2.6) + start_x)
    start_y = int(height / 10)
    end_y = int((height / 1.8) + start_y)
    zoomed = data[start_y:end_y, start_x:end_x]
    return zoomed


def main():
    """Main function to load an image, crop it, and display the result."""
    try:
        data = ft_load("../animal.jpeg")
        zoomed = crop_center_image(data)
        img = Image.fromarray(zoomed).convert('L')
        arr = np.array(img)[:, :, np.newaxis]
        print(f"New shape after slicing: {arr.shape}")
        print(arr)
        plt.imshow(arr, cmap='gray')
        plt.show()
        plt.close()
    except Exception as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":
    main()
