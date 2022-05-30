import sys
import shlex


def if_list_is_valid(file_content):
    try:
        my_list = shlex.split(file_content)
    except ValueError:
        print("I dont understand french, or other special chars, my bad ...", file=sys.stderr)
        sys.exit(84)



    my_float_list = []
    for number in my_list:
        try:
            new_number = float(number)
        except ValueError:
            print("The list that was in your file is not valid..((( we apologize", file=sys.stderr)
            sys.exit(84)
        my_float_list.append(new_number)
    if len(my_float_list) == 0:
        print("There were no numbers given", file=sys.stderr)
        sys.exit(84)

    return my_float_list


def look_what_we_got(av):
    if len(av) == 1:
        print("Please, give us some file to read", file=sys.stderr)
        sys.exit(84)
    if len(av) == 2 and av[1] == '-h':
        print_usage()
        sys.exit(0)
    if len(av) != 2:
        print("Please, give us only one(!) file to read", file=sys.stderr)
        sys.exit(84)


def print_usage():
    print("USAGE")
    print("    ./301dannon file")
    print("DESCRIPTION")
    print("file    file that contains the numbers to be sorted, separated by spaces")


def get_array_from_file(av):
    look_what_we_got(av)
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
    file_content = f.read()
    f.close()
    if not file_content:
        print("Unfortunately, the file you provided is empty..(((", file=sys.stderr)
        sys.exit(84)
    return if_list_is_valid(file_content)
