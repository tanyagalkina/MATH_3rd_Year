import sys


###looks for errors in logic   (circle dependencies etc)
def check_src(src):
    count = 0
    count2 = 0
    for s in src:
        if s.masters:
            count = count + 1
        if s.slaves:
            count2 = count2 + 1   
    #print ('I am checking the sources and entire logic ...')
    if count is 0 or count2 is 0:
        print('Inconsistent content', file=sys.stderr)
        sys.exit(84)


def print_usage():
    print("USAGE")
    print("    ./303make makefile [file]")
    print("DESCRIPTION")
    print("makefile    name of the makefile")
    print("file        name of a recently modified file")

def look_what_we_got(av):
    if len(av) == 1:
        print("Please, give us some file to read", file=sys.stderr)
        sys.exit(84)

    if len(av) == 2 and av[1] == '-h':
        print_usage()
        sys.exit(0)

    if len(av) is not 2 and len(av) is not 3:
        print('Wrong number of args', file=sys.stderr)
        sys.exit(84)



def check_args(av):
    look_what_we_got(av)
    got_lines = []
    try:
        f = open(av[1], 'r')
    except FileNotFoundError:
        print(f"File {av[1]} not found.  Aborting", file=sys.stderr)
        sys.exit(84)
    except OSError:
        print(f"OS error occurred trying to open {av[1]}", file=sys.stderr)
        sys.exit(84)
    except Exception as err:
        print(f"Unexpected error opening {av[1]} is", repr(err))
        sys.exit(84)
    lines = f.readlines()
    f.close()

    if not lines:
        print("Unfortunately, the file you provided is empty..(((", file=sys.stderr)
        sys.exit(84)
    for ln in lines:
        if not ln.isspace():
            got_lines.append(ln)
    if not got_lines:
        print("The file you provided is only spaces..(((", file=sys.stderr)
        sys.exit(84)

    return got_lines