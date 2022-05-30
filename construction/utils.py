import sys

from colorama import Fore, Style, init

sys.path.insert(1, './tests')
from answers import HOUSE_ANSWER

USAGE = "USAGE\n\t./305construction file\n\nDESCRIPTION\n\tfile\tfile describing the tasks"



def display_error(string):

    print(Fore.RED + Style.BRIGHT + string + Style.RESET_ALL)
    print(USAGE)
    exit(84)


def display_help():
    print(USAGE)
    exit(0)