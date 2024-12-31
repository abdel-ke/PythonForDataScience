import sys
import string


def display(s1, upper, lower, digits, spaces, punctuation):
    """
    display the number of upper-case characters, lower-case characters,
    punctuation characters, digits and spaces.
    """
    print("The text contains", len(s1), "characters:")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punctuation, "punctuation marks")
    print(spaces, "spaces")
    print(digits, "digits")


def building(s1):
    """ this function is to count the sums of its upper-case characters,
        lower-case characters, punctuation characters,
        digits and spaces.
    """
    upper = 0
    lower = 0
    digits = 0
    spaces = 0
    punctuation = 0
    for c in s1:
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
    display(s1, upper, lower, digits, spaces, punctuation)


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
            raise AssertionError(
                "AssertionError: more than one argument are provided")
        else:
            building(argv[1])
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main(sys.argv)
