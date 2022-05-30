#!/usr/bin/env python3

import sys
import operator
from usage import *
from errors import *
from room import Room, construction_controller


def main_func(av):
    if len(av) == 2 and (av[1] == '-h' or av[1] == '--help'):
        display_help()
        return
    if len(av) is not 4 and len(av) is not 6:
        display_error('Wrong number of args, please try with -h ...')
    args = []
    try:
        for i in range(1, len(sys.argv)):
            args.append(int(sys.argv[i]))
    except ValueError:
        display_help()
        display_error("only int arguments are valid!")

    room_matrix = construction_controller(args)
    #room_matrix.show()
    #room_matrix.show_matrix()
    #print(room_matrix.vector)
    room_matrix.run()


if __name__ == '__main__':
    #print(sys.path)
    argv = sys.argv
    main_func(argv)

    sys.exit(0)
