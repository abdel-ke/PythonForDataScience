import numpy as np
from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt


def center_zoom(data, zoom_factor=2):
    """
    Zoom into the center of an image (NumPy array) without resizing.
    zoom_factor > 1 means zooming in (smaller crop).
    """
    h, w = data.shape[:2]

    new_h = int(h / zoom_factor)
    new_w = int(w / zoom_factor)

    start_y = int((h - new_h) / 2)
    start_x = int((w - new_w) / 2)
    end_y = start_y + new_h
    end_x = start_x + new_w
    return data[start_y:end_y, start_x:end_x]


def main():
    try:
        data = ft_load("../animal.jpeg")
        start_x, end_x = 460, 850
        start_y, end_y = 70, 500
        zoomed = data[start_y:end_y, start_x:end_x]
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
