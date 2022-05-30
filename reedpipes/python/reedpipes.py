#!/usr/bin/env python3

import sys

from errors import *
from usage import display_help
from pipes import *


def main_func(av):
    if len(av) == 2 and (av[1] == '-h' or av[1] == '--help'):
        display_help()
        return
    if len(av) is not 7:
        display_error('Wrong number of args, please try with -h ...')
        return

    patch_argument_errors(av)
    args = []
    for i in range(0, 5):
        args.append(float(av[i]))
    args.append(int(av[5]))

    pipes = Pipes(args)
    pipes.run()
    pipes.show()


if __name__ == '__main__':
    argv = sys.argv
    main_func(argv)

    sys.exit(0)
