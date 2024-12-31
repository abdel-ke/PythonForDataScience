# import sys
from ft_filter import ft_filter


def is_even(n):
    """ check if the number is even """
    return n % 2 == 0


if __name__ == "__main__":
    """ Main function """
    try:
        lst = [-3, -2, -1, 0, 1, 2, 4, 5, 6]
        ret = ft_filter(is_even, lst)
        for item in ret:
            print(item)
        print("________________")
        ret = ft_filter(None, lst)
        for item in ret:
            print(item)
    except Exception as e:
        print('TypeError:', e)
