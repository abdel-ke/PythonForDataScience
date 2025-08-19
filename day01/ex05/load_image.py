import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:  # (you can return to the desired format)
    """Load an image from the specified path and return it as a numpy array.
    Args:
        path (str): The file path to the image.
    Returns:
        np.array: The image represented as a numpy array,
        or an empty listif an error occurs.
    """
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        img = Image.open(path)
        arr = np.array(img)
        print(f"The shape of image is: {arr.shape}")
        print(arr)
        img.close()
        return arr
    except Exception as e:
        print(f"An error occured: {e}")
        return []
