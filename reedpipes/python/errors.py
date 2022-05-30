import sys


def display_error(msg='unknown error'):
    sys.stderr.write(msg + '\n')
    sys.exit(84)


def patch_argument_errors(args):

    args.pop(0)
    for arg in args:
        try:
            value = float(arg)
        except ValueError:
            display_error("Argument is not a float")
        if value <= 0:
            display_error("The value should be positive")