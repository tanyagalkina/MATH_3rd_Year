import sys


def display_error(msg='unknown error'):
    sys.stderr.write(msg + '\n')
    sys.exit(84)


def patch_argument_errors(args):
    # print('we have {} args'.format(len(args)))
    size_of_the_room = args[0]
    i_coord_radiator = args[1]
    j_coord_radiator = args[2]

    if size_of_the_room <= 2:
        display_error("size of the room cannot be less then 3")
    elif i_coord_radiator < 1 or j_coord_radiator < 1 or \
            i_coord_radiator > size_of_the_room - 2 or j_coord_radiator > size_of_the_room - 2:
        display_error("[ERROR] radiator's coordinate is not valid!")
    if len(args) is 5:
        i_coord_room = args[3]
        j_coord_room = args[4]
        if i_coord_room < 1 or j_coord_room < 1 or \
                i_coord_room > size_of_the_room - 2 or j_coord_room > size_of_the_room - 2:
            display_error("[ERROR] room's coordinate is not valid!")
