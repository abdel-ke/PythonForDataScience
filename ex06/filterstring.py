# import sys
from ft_filter import ft_filter


def is_even(n):
    """ check if the number is even """
    return n % 2 == 0


if __name__ == "__main__":
    """ Main function """
    try:
        list = [2, 4, 5, 6]
        z = ft_filter(is_even, list)
        for y in z:
            print(y)
    except Exception as e:
        print('TypeError:', e)
