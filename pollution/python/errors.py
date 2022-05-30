import sys
import csv


def display_error(msg='unknown error'):
    sys.stderr.write(msg + '\n')
    sys.exit(84)


def patch_argument_errors(args):
    args.pop(0)
    # pop file name
    n = 0
    x = y = -0.00
    try:
        n = int(args[0])
        x = float(args[2])
        y = float(args[3])
    except:
        display_error("invalid argument")

    if n <= 0 or x < 0 or x > n - 1 or y < 0 or y > n - 1:
        display_error("invalid argument")
    return


def try_read_file(path):
    lines = []
    try:
        reader = csv.reader(open(path), delimiter=";")
        reader = filter(None, reader)
        for row in reader:
            if len(row) == 3:
                lines.append([int(row[0]), int(row[1]), int(row[2])])
            else:
                raise Exception("Strange csv data")

    except IOError:
        display_error("Cannot read file")
    except BaseException as error:
        display_error("some data reading error")

    if len(lines) == 0:
        display_error("Empty file")
    lines = filter(None, lines)
    return lines
