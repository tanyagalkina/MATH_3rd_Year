import copy

from errors import patch_argument_errors
import numpy as np
import sys
#from tabulate import tabulate


def save_relations(args):
    patch_argument_errors(args)
    return Relations(args)


def get_pivot_row(tab, column):
    minimum = 99999999999
    i = 0
    row = -1
    for i in range(0, 4):
        if tab[i][10]:
            if tab[i][column] > 0 and (minimum > tab[i][10] / tab[i][column] > 0):
                minimum = tab[i][10] / tab[i][column]
                row = i
        elif minimum > tab[i][column] > 0:
            row = i
            minimum = tab[i][10] / tab[i][column]
    return row


def find_pivot_point(tab):
    indicators = []
    i = 0
    for i in range(0, 9):
        indicators.append(tab[4][i])
    minimal = min(indicators)
    # if there are no negative indicators ...
    if minimal >= 0:
        return -1, -1
    column = indicators.index(minimal)
    row = get_pivot_row(tab, column)
    return row, column


def elimin(array, coord, tab, row):
    pivot = tab[coord[0]][coord[1]]
    row_point = copy.deepcopy(array[coord[1]])

    for i in range(0, 11):
        array[i] -= row_point * tab[coord[0]][i]


def eliminate(coord, tab):
    i = 0

    pivot = tab[coord[0]][coord[1]]
    j = 0
    for j in range(0, 11):
        if tab[coord[0]][j] != 0:
            tab[coord[0]][j] = tab[coord[0]][j] / pivot
    for i in range(0, 5):
        if i != coord[0]:
            elimin(tab[i], coord, tab, i)


def output_string(name, amount):
    print(name + ': {:.2f}'.format(amount), end='') if amount != 0 else print(name + ' : 0', end='')


def set_amount(tab, index):
    tmp = []
    for i in range(0, 4):
        if tab[i][index]:
            tmp.append(tab[i][10] / tab[i][index])
    if len(tmp) == 1:
        return tmp[0]
    else:
        return 0


class Relations:
    def __init__(self, args):
        self.n1 = args[0]
        self.n2 = args[1]
        self.n3 = args[2]
        self.n4 = args[3]
        self.po = args[4]
        self.pw = args[5]
        self.pc = args[6]
        self.pb = args[7]
        self.ps = args[8]
        self.ao = 5
        self.aw = 0
        self.ac = 0
        self.ab = 0
        self.aso = 0
        self.total = 1
        self.tab = np.zeros((5, 11))
        self.tab_init()
        self.headers = ["Oat", "Wheat", "Corn", "Barley", "Soy", "Slack1", "Slack2", "Slack3", "Slack4", "Volume",
                        "Values"]
        #self.table = tabulate(self.tab, self.headers, tablefmt="fancy_grid")
        #print(self.table)

    def show(self):
        print('Resources: {} F1, {} F2, {} F3, {} F4'.format(self.n1, self.n2, self.n3, self.n4))
        print()
        output_string("Oat", self.ao)
        print(' units at ${}/unit'.format(self.po))
        output_string("Wheat", self.aw)
        print(' units at ${}/unit'.format(self.pw))
        output_string("Corn", self.ac)
        print(' units at ${}/unit'.format(self.pc))
        output_string("Barley", self.ab)
        print(' units at ${}/unit'.format(self.pb))
        output_string("Soy", self.aso)
        print(' units at ${}/unit'.format(self.ps))
        print()
        print('Total production value: ', end='')
        print('${:.2f}'.format(self.total))
            #if self.total is not 0 else print('$0')

    def tab_init(self):
        self.tab[0] = [1, 0, 1, 0, 2, 1, 0, 0, 0, 0, self.n1]
        self.tab[1] = [1, 2, 0, 1, 0, 0, 1, 0, 0, 0, self.n2]
        self.tab[2] = [2, 1, 0, 1, 0, 0, 0, 1, 0, 0, self.n3]
        self.tab[3] = [0, 0, 3, 1, 2, 0, 0, 0, 1, 0, self.n4]
        self.tab[4] = [-self.po, -self.pw, -self.pc, -self.pb, -self.ps, 0, 0, 0, 0, 1, 0]

    def run(self):
        while 1:
            p_coord = find_pivot_point(self.tab)
            if (p_coord[0] or p_coord[1]) == -1:
                break
            eliminate(p_coord, self.tab)
            #table = tabulate(self.tab, self.headers, tablefmt="fancy_grid")
            #print(table)

        self.set_result_values()

    def set_result_values(self):

        self.ao = set_amount(self.tab, 0)
        self.aw = set_amount(self.tab, 1)
        self.ac = set_amount(self.tab, 2)
        self.ab = set_amount(self.tab, 3)
        self.aso = set_amount(self.tab, 4)
        self.total = self.tab[4][10]

