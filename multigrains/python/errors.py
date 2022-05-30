import sys


def display_error(msg='unknown error'):
    sys.stderr.write(msg + '\n')
    sys.exit(84)


def patch_argument_errors(args):
    for arg in args:
        if arg < 0:
            display_error("The value cannot be negative!")
    po = args[4]
    pw = args[5]
    pc = args[6]
    pb = args[7]
    ps = args[8]
    if po is 0 or pw is 0 or pc is 0 or pb is 0 or ps is 0:
        display_error("The price cannot be zero, right?")

