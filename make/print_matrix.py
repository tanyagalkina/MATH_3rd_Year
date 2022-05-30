
def print_dependency(obj, src):

    if obj.slaves:
        for slv in obj.slaves:
            print(obj.name, '-> ', end='')
            for sr in src:
                if sr.name == slv:
                    print_dependency(sr, src)
    else: print(obj.name)



def print_matrix_and_strings(src):

    i = 0
    for sr in src:
        print('[', end='')
        for i in range (0, len(src)):
            if sr.name in src[i].masters:
                print('1', end='') if i == 0 else print (' 1', end='')
            else:
                print(0, end='') if i == 0 else print (' 0', end='')
        print(']')
        i = i + 1
    print('')

    for sr in src:
        if sr.slaves:
            print_dependency(sr, src)





