class Pipes:
    def __init__(self, args):
        self.abs = [0, 5, 10, 15, 20]
        self.ord = [args[0], args[1], args[2], args[3], args[4]]
        self.points = args[5]
        self.vector = [0, 0, 0, 0, 0]
        self.result = []

    def run(self):
        a = 6 * (self.ord[2] - 2 * self.ord[1] + self.ord[0]) / 50
        b = 6 * (self.ord[3] - 2 * self.ord[2] + self.ord[1]) / 50
        c = 6 * (self.ord[4] - 2 * self.ord[3] + self.ord[2]) / 50

        self.vector[2] = (b - (a + c) / 4) * 4 / 7
        self.vector[1] = a / 2 - 0.25 * self.vector[2]
        self.vector[3] = c / 2 - 0.25 * self.vector[2]
        for i in range(self.points):
            x = 20 / (self.points - 1) * i
            y = int((x - 0.01) / 5) + 1
            self.result.append(self.calculate(x, y))

        for i in range(len(self.vector)):
            self.vector[i] = round(self.vector[i], 1)
            if self.vector[i] == -0.0:
                self.vector[i] = 0

    def calculate(self, x, y):
        res = (- self.vector[y - 1] / 30 * pow(x - self.abs[y], 3) + self.vector[y] / 30 * pow(x - self.abs[y - 1], 3)
               - (self.ord[y - 1] / 5 - 5 / 6 * self.vector[y - 1]) * (x - self.abs[y]) + (
                       self.ord[y] / 5 - 5 / 6 * self.vector[y]) * (x - self.abs[y - 1]))
        return res

    def show(self):
        print('vector result: [{:.1f}, {:.1f}, {:.1f}, {:.1f}, {:.1f}]'.format(self.vector[0],
                                                                               self.vector[1],
                                                                               self.vector[2],
                                                                               self.vector[3],
                                                                               self.vector[4]))
        for i in range(self.points):
            print('abscissa: {:.1f} cm \tradius: {:.1f} cm'.format(
                (20 / (self.points - 1) * i), self.result[i]))
