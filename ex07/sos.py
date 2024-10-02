import sys

NESTED_MORSE = {
    'A': '.- ',
    'B': '-... ',
    'C': '-.-. ',
    'D': '-.. ',
    'E': '. ',
    'F': '..-. ',
    'G': '--. ',
    'H': '.... ',
    'I': '.. ',
    'J': '.--- ',
    'K': '-.- ',
    'L': '.-.. ',
    'M': '-- ',
    'N': '-. ',
    'O': '--- ',
    'P': '.--. ',
    'Q': '--.- ',
    'R': '.-. ',
    'S': '... ',
    'T': '- ',
    'U': '..- ',
    'V': '...- ',
    'W': '.-- ',
    'X': '-..- ',
    'Y': '-.-- ',
    'Z': '--.. ',
    '0': '----- ',
    '1': '.---- ',
    '2': '..--- ',
    '3': '...-- ',
    '4': '....- ',
    '5': '..... ',
    '6': '-.... ',
    '7': '--... ',
    '8': '---.. ',
    '9': '----. ',
    ' ': '/ '
}


def error_msg(error_message, error_number):
    '''show error message'''
    print(error_message)
    exit(error_number)


def is_valid_char(char):
    '''verify if char is alphanumeric'''
    if char.isalnum() or char == ' ':
        return True
    return False


def main():
    '''this is main'''
    argc = len(sys.argv)
    if argc != 2:
        error_msg("Assertion error: the arguments are bad", 1)
    string = sys.argv[1]
    morse_string = ''
    for letter in string:
        if is_valid_char(letter):
            morse_string += NESTED_MORSE[letter.upper()]
        else:
            error_msg("Assertion error: only alphanumeric chars allowed", 1)
    print(morse_string)


if __name__ == "__main__":
    main()
