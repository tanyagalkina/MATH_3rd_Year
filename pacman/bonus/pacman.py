#!/usr/bin/env python3

import sys
import operator
from get_map import *
from dijkstra import *

def print_result(l_len, nodes, wall, space):
    #print('The total of nodes is:', len(nodes))
    pos = []
    i = 0
    for n in nodes:
        if 0 < n[1] < float('inf'):
            pos.append(n[0])
    with open("post", "w") as file:
	    file.write('\n'.join(str(e) for e in pos))



def main_func(av):
    if len(av) == 2 and (av[1] == '-h' or av[1] == '--help'):
        display_help()
        return
    if len(av) != 4:
        print('Wrong number of args, please try with -h ...', file=sys.stderr)
        sys.exit(84)
    pac_map = get_map(av)
    result = run_dijkstra(pac_map)
    print_result(len(pac_map[0]) - 1, result, av[2], av[3])

if __name__ == '__main__':

    argv = sys.argv
    main_func(argv)

    sys.exit(0)
