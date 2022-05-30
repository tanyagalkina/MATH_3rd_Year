#!/usr/bin/env python

import sys
import colorama
from colorama import Fore, Style, init
import operator
from get_sources import get_sources, Source, is_in_sources
from print_matrix import print_matrix_and_strings



def find_by_name(name, src):
    for s in src:
        if s.name == name:
            return s



def recursive_search(name, src, build, objects, stage):
    obj = find_by_name(name, src)
    obj.stage = stage
    if obj not in objects:
        objects.append(obj)
        if not obj.slaves:
            return objects

        else:
            for slv in obj.slaves:
                    recursive_search(slv, src, build, objects, stage + 10)


#dont know what was it for ... only 0 level is working
def set_master_levels(srces):
    for s in srces:
        if s.masters and s.level is not -1:
            for m in s.masters:
                ob = find_by_name(m, srces)
                ob.level = s.level + 5
                #set_master_levels(srces)
    for s in srces:
        if s.level == -1:
            set_master_levels(srces)
    return            
    #else:
    #    return                


## if the file is exec .. maybe there are many??
def set_levels(src):
    for s in src:
        if not s.slaves:
            s.level = 0
    set_master_levels(src)
    #for s in src:'''



def print_one_build(name, src):

    print(Fore.GREEN + Style.BRIGHT + 'This would be done if ' + name + ' would have been changed' + Style.RESET_ALL)


    if not is_in_sources(name, src):
        print(Fore.RED + Style.BRIGHT + '[WARNING] The source you gave: "' + name + '",  is not a part of the project!' + Style.RESET_ALL, file=sys.stderr)
        return 84
    set_levels(src)
    file = find_by_name(name, src)
    if file.level is 0:
        print('')
        return 0
    source_objects = []
    build = []
    recursive_search(name, src, build, source_objects, 10)
    so_sr = sorted(source_objects, key=operator.attrgetter('stage'))

    for ob in so_sr:
        if name != ob.name:

            for b in ob.builds:
                print(b, end ='')

    for s in src:
        s.stage = -1



def print_build(av, src):
    name = av[2]
    #print('the names given were:')### in case of one name
    #print(av)

    av.pop(0)
    av.pop(0)
    names = av
    name = names[0]
    #print(names)
    i = 0
    for name in names:
        ret = print_one_build(name, src)

    sys.exit(ret)


def main_func(av):
    my_src = get_sources(av)
    if len(av) == 2:
        print_matrix_and_strings(my_src)
    else:
        print_build(argv, my_src)


if __name__ == '__main__':

    argv = sys.argv
    main_func(argv)

    sys.exit(0)
