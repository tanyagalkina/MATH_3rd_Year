import sys

def display_help():
    print("USAGE:\n\t./304pacman file c1 c2")
    print("DESCRIPTION:\n\tfile\tfile describing the board, using the following characters:")
    print("\t\t    'O' for an empty square,")
    print("\t\t    '1' for a wall,")
    print("\t\t    'F' for the ghost's position,")
    print("\t\t    'P' for Pacman's position.")
    print("\tc1\tcharacter to display for a wall")
    print("\tc2\tcharacter to display for an empty space.")

def check_walls_spaces(c1, c2):
    if len(c1) is not 1 or len(c2) is not 1:
        print(f"The characters for walls and spaces should be length one, I suppose", file=sys.stderr)
        sys.exit(84)

    if c1 == c2:
        print(f"The characters for walls and spaces should be different.", file=sys.stderr)
        sys.exit(84)

def check_inside_the_map(map):
    lent = len(map[0])
    #print("the length is", lent)
    valid = "01FP"

    for line in map:
        if len(line) != lent:
            print(f"Should the lines be same length?", file=sys.stderr)
            sys.exit(84)
    count_ghost = 0
    count_pacman = 0

    for line in map:
        line = line.replace('\n', '')
        for char in line:
            if char not in valid:
                print(f"Invalid char in the map", file=sys.stderr)
                sys.exit(84)

            if char == 'F':
                count_ghost = count_ghost + 1

            if char == 'P':
                count_pacman = count_pacman + 1
            #if char == '\n':
             #   print ('n!')
    if count_ghost is not 1 or count_pacman is not 1:
        print(f"we thought there can be only one ghost and only one pacman ...", file=sys.stderr)
        sys.exit(84)




def get_map(av):
    check_walls_spaces(av[2], av[3])
    map_lines = []
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
            map_lines.append(ln)
    if not map_lines:
        print("The file you provided is only spaces..(((", file=sys.stderr)
        sys.exit(84)

    check_inside_the_map(map_lines)

    return map_lines