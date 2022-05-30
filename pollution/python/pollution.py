#!/usr/bin/env python3

import sys


from errors import *
from usage import display_help
from calc import *



def make_map(file, n):

    map = [[0 for x in range(n)] for y in range(n)]
    for each in file:
        map[each[0]][each[1]] = each[2]
    #print(map)
    return map


def main_func(av):
    if len(av) == 2 and (av[1] == '-h' or av[1] == '--help'):
        display_help()
        return
    if len(av) is not 5:
        display_error('Wrong number of args, please try with -h ...')
        return

    patch_argument_errors(av)
    file = try_read_file(av[1])
    n = int(av[0])
    x = float(av[2])
    y = float(av[3])
    heat_map = make_map(file, n)
    pollution = Pollution(n, x, y, heat_map)
    pollution.run()
    pollution.show()


if __name__ == '__main__':
    argv = sys.argv
    main_func(argv)

    sys.exit(0)
