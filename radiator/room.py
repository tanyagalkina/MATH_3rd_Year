import math
import numpy as np

from errors import patch_argument_errors


def math_round(n, decimals=0):
    n *= 10 ** decimals
    n = math.floor(n) if n - math.floor(n) < 0.5 else math.ceil(n)
    return n / 10 ** decimals


def construction_controller(args):
    # print('we have {} args'.format(len(args)))
    patch_argument_errors(args)
    if len(args) is 3:
        room_matrix = Room(args, 'matrix')
    else:
        room_matrix = Room(args, 'spot')

    return room_matrix


class Room:
    def __init__(self, args, query):
        self.room = args[0]
        self.mrx_size = self.room * self.room
        self.i_radiator = args[1]
        self.j_radiator = args[2]
        self.boundary_h = 0.5
        self.boundary_f = -300
        self.matrix = list()
        self.vector_coeff = list()
        self.values = list()
        self.x_vector = list()
        if query is 'spot':
            self.i_room = args[3]
            self.j_room = args[4]
            self.query = 'spot'
        else:
            self.query = 'matrix'
        self.make_matrix()
        self.make_vector_coeff()
        self.process()

    def show(self):
        print('room: {}'.format(self.room))
        print('i_radiator: {}'.format(self.i_radiator))
        print('j_radiator: {}'.format(self.j_radiator))
        print('query: {}'.format(self.query))
        print('boundaries: {} {}'.format(self.boundary_h, self.boundary_f))
        if self.query is 'spot':
            print('i_room: {}'.format(self.i_room))
            print('j_room: {}'.format(self.j_room))

    def run(self):
        if self.query is 'matrix':
            self.show_matrix()
            self.show_vector()
        else:
            self.show_spot()

    def make_vector_coeff(self):
        for j in range(self.room):
            for i in range(self.room):
                if i == self.i_radiator and j == self.j_radiator:
                    self.vector_coeff.append(self.boundary_f)
                else:
                    self.vector_coeff.append(0)

    def make_matrix(self):
        for y in range(0, self.room):
            for x in range(0, self.room):
                if y == 0 or y == self.room - 1 or x == 0 or x == self.room - 1:
                    self.matrix.append(self.boundary(x, y))
                else:
                    self.matrix.append(self.formula(x, y))

    def process(self):
        self.values = np.linalg.inv(self.matrix)
        self.x_vector = np.matmul(self.values, self.vector_coeff)

    def boundary(self, x, y):
        line = list()
        d = x + y * self.room
        for T in range(self.mrx_size):
            if T != d:
                line.append(0)
            else:
                line.append(1)
        return line

    def formula(self, x, y):
        line = list()
        for T in range(self.mrx_size):
            if (T == x - 1 + y * self.room or T == x + 1 + y * self.room or T == x + (
                    y - 1) * self.room or T == x + (y + 1) * self.room):
                line.append(int(1 / self.boundary_h * 2))
            elif T == x + y * self.room:
                line.append(int(- 4 / self.boundary_h * 2))
            else:
                line.append(0)
        return line

    def show_matrix(self):
        for line in self.matrix:
            # print(line)
            print(*line, sep='\t')

    def show_spot(self):
        print(round(self.x_vector[self.room * self.j_room + self.i_room], 1))
        # print(3.1)

    def show_vector(self):
        print()

        for each in self.x_vector:
            if round(each, 1) is -0.0:
                print(0.0)
            else:
                print('%.1f' % math_round(each, 1))
        # print(*self.vector_coeff, sep='\n')
