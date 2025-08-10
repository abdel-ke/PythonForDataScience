import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:  # (you can return to the desired format)
    """Load an image from the specified path and return it as a numpy array."""
    try:
        img = Image.open(path)
        arr = np.array(img)
        print(f"The shape of image is: {arr.shape}")
        print(arr)
        img.close()
        return arr
    except Exception as e:
        print(f"An error occured: {e}")
        return []
