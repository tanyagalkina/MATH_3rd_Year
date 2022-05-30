#!/usr/bin/env python

import sys
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




def print_build(av, src):
    name = av[2]    ### in case of one name

    if not is_in_sources(name, src):
        print('The source you gave is not a part of the project', file=sys.stderr)
        sys.exit(84)
    set_levels(src)
    file = find_by_name(name, src)
    if file.level is 0:
        print('')
        sys.exit(0) 
    source_objects = []
    build = []
    recursive_search(name, src, build, source_objects, 10)
    so_sr = sorted(source_objects, key=operator.attrgetter('stage'))

    for ob in so_sr:
        if name != ob.name:

            for b in ob.builds:
                print(b, end ='')


def main_func(av):
    my_src = get_sources(av)
    if len(av) == 2:
        print_matrix_and_strings(my_src)
    else:
        print_build(av, my_src)


if __name__ == '__main__':

    argv = sys.argv
    main_func(argv)

    sys.exit(0)
