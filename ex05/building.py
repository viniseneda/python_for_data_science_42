import sys


def error_msg(error_message, error_number):
    '''show error message'''
    print(error_message)
    return (error_number)


def count_in(string, char_list) -> int:
    '''counts number of times characters in char_list\
    appear in the string parameter'''
    sum = 0
    for letter in string:
        if letter in char_list:
            sum += 1
    return sum


def main():
    '''this is main'''
    argc = len(sys.argv)
    if argc > 2:
        return (error_msg("Assertion error: wrong number of arguments", 1))
    elif argc == 1:
        try:
            print("What is the text to count?")
            string = sys.stdin.readline()
        except KeyboardInterrupt:
            return (error_msg("Assertion error: CTR-C detected", 1))
    else:
        string = sys.argv[1]

    num_whites = count_in(string, " 	\n")
    num_lower = count_in(string, "abcdefghijklmnoprstuvwxyz")
    num_upper = count_in(string, "ABCDEFGHIJKLMNOPRSTUVWXYZ")
    num_punct = count_in(string, "[!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]")
    num_digits = count_in(string, "0123456789")
    total = num_digits + num_lower + num_punct + num_whites + num_upper

    print(f"The text contains {total} characters:\
          \n {num_upper} upper letters\
          \n {num_lower} lower letters\
          \n {num_punct} punctuation marks\
          \n {num_whites} spaces\
          \n {num_digits} digits")


if __name__ == "__main__":
    main()
