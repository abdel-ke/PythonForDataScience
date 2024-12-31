import sys
import string


def display(upper, lower, digits, spaces, punctuation):
    """
    display the number of upper-case characters, lower-case characters,
    punctuation characters, digits and spaces.
    """
    print("The text contains", len(str), "characters:")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punctuation, "punctuation marks")
    print(spaces, "spaces")
    print(digits, "digits")


def building(str):
    """ this function is to count the sums of its upper-case characters,
        lower-case characters, punctuation characters,
        digits and spaces.
    """
    upper = 0
    lower = 0
    digits = 0
    spaces = 0
    punctuation = 0
    for c in str:
        if c.islower():
            lower += 1
        elif c.isupper():
            upper += 1
        elif c.isnumeric():
            digits += 1
        elif c in string.punctuation:
            punctuation += 1
        elif c == ' ' or c == '\t':
            spaces += 1
    display(upper, lower, digits, spaces, punctuation)


def main(argv):
    """
    main function to count the sums of its upper-case characters,
    lower-case characters, punctuation characters, digits and spaces.

    raise AssertionError if too many arguments provided.
    """
    try:
        if len(argv) == 1:
            text = input('What is the text to count?\n')
            building(text)
        elif len(argv) != 2:
            raise AssertionError("AssertionError: Too many arguments provided")
        else:
            building(argv[1])
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main(sys.argv)
