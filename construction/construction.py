#!/usr/bin/env python

import sys
import os
import operator
from utils import *
from get_graph import get_graph
from run_algo import run_algo


def main_func(av):
    if len(av) == 2 and (av[1] == '-h' or av[1] == '--help'):
        display_help()
        return
    if len(av) is not 2:
        print('Wrong number of args, please try with -h ...', file=sys.stderr)
        sys.exit(84)
    graph = get_graph(av[1])
    run_algo(graph)

if __name__ == '__main__':

    argv = sys.argv
    main_func(argv)

    sys.exit(0)