import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slices a 2D array (list of lists) from start to end indices.
    Args:
        family (list): A 2D list representing the family data.
        start (int): The starting index for slicing.
        end (int): The ending index for slicing.
    Returns:
        list: A new 2D list containing the sliced data.
    """
    try:
        # Checke args
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("'start' and 'end' must be int!!")
        try:
            family = np.array(family)
        except Exception as e:
            raise ValueError(f"Cannot convert 'family' to a 2D array: {e}")
        # print my shape
        print("My shape is :", family.shape)
        truncated = family[start:end]
        # print new shape
        print("My new shape is :", truncated.shape)
        return truncated.tolist()
    except TypeError as te:
        print("An error occured:", te)
        return []
    except Exception as e:
        print("An error occured:", e)
        return []
