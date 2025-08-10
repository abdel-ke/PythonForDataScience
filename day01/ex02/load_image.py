import numpy as np
import PIL as pil


def ft_load(path: str) -> np.array:  # (you can return to the desired format)
    try:
        img = pil.Image.open(path)
        arr = np.array(img)
        print(f"The shape of image is: {arr.shape}")
        print(arr)
        img.close()
        return arr
    except Exception as e:
        print(f"An error occured: {e}")
        return []
