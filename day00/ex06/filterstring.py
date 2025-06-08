import sys


def filter_string(s, n):
    res = (lambda spltd, n: [s for s in spltd if len(s) >= n])(s, n)
    print(res)


if __name__ == '__main__':
    try:
        argv = sys.argv
        if (len(argv) != 3):
            raise AssertionError("AssertionError: the arguments are bad")
        try:
            n = int(argv[2])
        except ValueError:
            raise AssertionError("AssertionError: the arguments are bad")
        splitted = argv[1].split()
        filter_string(splitted, n)
    except AssertionError as e:
        print(e)
