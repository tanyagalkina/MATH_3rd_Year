from copy import deepcopy
from my_compar import my_compar


def quick_sort(ob, array):
    length = len(array)
    if length <= 1:
        return array
    pivot = array[0]
    left, right, equal = [], [], [pivot]
    for i in range(1, length):
        diff = my_compar(ob, pivot, array[i])
        if diff > 0:
            right.append(array[i])
        else:
            left.append(array[i])
    return quick_sort(ob, left) + equal + quick_sort(ob, right)


class Quick:
    def __init__(self, given_list):
        self.given_list = deepcopy(given_list)
        self.counter = 0
        self.sorted = quick_sort(self, self.given_list)

    def bench(self):
        return self.counter
