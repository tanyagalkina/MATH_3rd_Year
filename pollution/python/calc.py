import math


def calculate(i, m):
    return math.factorial(m) / (math.factorial(i) * (math.factorial(m - i)))


class Pollution:
    def __init__(self, n, x, y, map):
        # self.abs =
        # self.ord =
        self.m1 = n - 1
        self.m2 = n - 1
        self.t1 = x / self.m1
        self.t2 = y / self.m2
        self.points = n
        self.map = map
        self.result = 0.00

    def run(self):
        for i in range(0, self.points):
            for j in range(0, self.points):
                value = calculate(i, self.m1) * calculate(j, self.m2) * (self.t1 ** i * ((1 - self.t1) ** (self.m1 - i)))
                value *= (self.t2 ** j * ((1 - self.t2) ** (self.m2 - j)))
                value *= self.map[i][j]
                self.result += value


    def show(self):
        print('{:.2f}'.format(self.result))
