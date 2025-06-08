import sys

try:
    argv = sys.argv
    if len(argv) > 2:
        raise AssertionError("more than one argument is provided")

    if len(argv) == 2:
        try:
            nbr = int(argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")
        if nbr % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    print()
except AssertionError as e:
    print("AssertionError: " + str(e))
