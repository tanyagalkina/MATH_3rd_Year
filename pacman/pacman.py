#!/usr/bin/env python

import sys
import operator
from get_map import *
from dijkstra import *


def print_node(n, wall, space):
    if n[1] == -42:
        print (wall, end='')
    elif n[1] == -84:
        print('P', end= '')
    elif n[1] == 0:
        print ('F', end='')
    elif 0 < n[1] < float('inf'):
        #print('x', end='')
        print (n[1] % 10, end='')
    elif not (n[1] < float('inf')):
        print (space, end='')
    else:
        print(n[1] % 10, end='')



def print_result(l_len, nodes, wall, space):
    #print('The total of nodes is:', len(nodes))
    i = 0
    for n in nodes:
        print_node(n, wall, space)
        i = i + 1
        if i % l_len == 0:
            print()



def main_func(av):
    if len(av) == 2 and (av[1] == '-h' or av[1] == '--help'):
        display_help()
        return
    if len(av) is not 4:
        print('Wrong number of args, please try with -h ...', file=sys.stderr)
        sys.exit(84)
    pac_map = get_map(av)
    result = run_dijkstra(pac_map)
    print_result(len(pac_map[0]) - 1, result, av[2], av[3])

if __name__ == '__main__':

    argv = sys.argv
    main_func(argv)

    sys.exit(0)
