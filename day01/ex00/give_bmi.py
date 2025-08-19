def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """Calculate the Body Mass Index (BMI)
    Args:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.
    Returns:
        list[int | float]: List of BMI values.
    """
    try:
        if not height or not weight:
            raise ValueError("Height and weight must not be empty!!")
        if not isinstance(height, list) or not isinstance(weight, list):
            raise ValueError("Height and weight must be a list!!")
        if not all(isinstance(h, (int, float)) for h in height):
            raise ValueError("Height must be a list of int or float!!")
        if not all(isinstance(w, (int, float)) for w in weight):
            raise ValueError("Weight must be a list of int or float!!")
        if len(height) != len(weight):
            raise ValueError(
                "Height and weight lists must have the same length."
                )
        bmi = []
        for i in range(len(height)):
            result = weight[i] / (height[i] ** 2)
            bmi.append(result)
        return bmi
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def apply_limit_checker(bmi: list[int | float], limit: int) -> bool:
    """Check if the input for apply_limit is valid.
    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): The limit to apply.
    Returns:
        bool: True if the input is valid, False otherwise.
    """
    if not bmi:
        print("Error: bmi must not be empty!!")
        return False
    if not isinstance(bmi, list):
        print("Error: bmi must be a list!!")
        return False
    if not all(isinstance(b, (int, float)) for b in bmi):
        print("Error: bmi must be a list of int or float!!")
        return False
    if limit <= 0:
        print("Error: limit must be a positive int!!")
        return False
    if len(bmi) == 0:
        print("Error: bmi must not be empty!!")
        return False
    return True


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply a limit to the BMI values.
    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): The limit to apply.
    Returns:
        list[bool]: List of booleans indicating if each BMI
        value exceeds the limit.
    """
    try:
        if not apply_limit_checker(bmi, limit):
            return []
        list_limit = []
        for x in bmi:
            list_limit.append(x > limit)
        return list_limit
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
