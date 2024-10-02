import sys


def error_msg(error_message, error_number):
    '''show error message'''
    print(error_message)
    return (error_number)


def get_positive_integer(string):
    '''convert string to int, if negative or not a number returns -1'''
    try:
        number = int(string)
        if number < 0:
            return (-1)
    except ValueError:
        return (-1)
    return (number)


def main():
    '''this is main'''
    argc = len(sys.argv)
    n = get_positive_integer(sys.argv[-1])
    out_list = []
    if argc != 3:
        return (error_msg("Assertion error: the arguments are bad", 1))
    elif n == -1:
        return (error_msg("Assertion error: the arguments are bad", 1))
    in_list = sys.argv[1].split()
    for word in in_list:
        if (lambda a, b: len(a) < b)(word, n):
            out_list.append(word)
    print(out_list)


if __name__ == "__main__":
    main()
