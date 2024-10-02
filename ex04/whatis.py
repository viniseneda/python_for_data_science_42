import sys

argc = len(sys.argv)
if argc > 1:
    if argc != 2:
        print("AssertionError: more than one argument is provided")
        exit()
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        exit()
    if number % 2 != 0:
        print("I'm Odd.")
    else:
        print("I'm Even.")
