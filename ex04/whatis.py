import sys

try:
    argv = sys.argv
    if len(argv) > 2:
        raise AssertionError("more than one argument is provided")

    if len(argv) == 1:
        raise AssertionError("you must provide one argument")

    try:
        nbr = int(argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
    if nbr % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as e:
    print("AssertionError:", e)
