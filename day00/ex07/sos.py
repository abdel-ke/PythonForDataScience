import sys


def print_sos(argv):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
    }
    for i, c in enumerate(argv.upper()):
        if c in morse_code_dict:
            if i == len(argv) - 1:
                print(morse_code_dict[c])
            else:
                print(morse_code_dict[c], end=" ")


def main():
    try:
        argv = sys.argv
        if len(sys.argv) != 2:
            raise AssertionError("AssertionError: the arguments are bad")
        argv1 = argv[1]
        for c in argv1:
            if not (c.isalpha() or c.isdigit() or c.isspace()):
                raise AssertionError("Unsupported character: " + c)
        print_sos(argv1)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
