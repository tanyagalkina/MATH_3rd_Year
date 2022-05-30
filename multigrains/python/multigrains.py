#!/usr/bin/env python3

import sys
import operator
from usage import display_help
from simplex import save_relations
from errors import display_error, patch_argument_errors


def main_func(av):
    if len(av) == 2 and (av[1] == '-h' or av[1] == '--help'):
        display_help()
        return
    if len(av) is not 10:
        display_error('Wrong number of args, please try with -h ...')
    args = []
    try:
        for i in range(1, len(sys.argv)):
            args.append(int(sys.argv[i]))
    except ValueError:
        display_help()
        display_error("only int arguments are valid!")

    simplex = save_relations(args)
    simplex.run()
    simplex.show()


if __name__ == '__main__':
    argv = sys.argv
    main_func(argv)

    sys.exit(0)
