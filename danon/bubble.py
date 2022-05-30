from copy import deepcopy
from my_compar import my_compar


class Bubble:
    def __init__(self, given_list):
        self.given_list = deepcopy(given_list)
        self.counter = 0
        self.sorted = []

    def bench(self):
        list_len = len(self.given_list)
        arr = self.given_list

        for i in range(list_len - 1):
            for j in range(0, list_len - i - 1):
                if my_compar(self, arr[j], arr[j + 1]) > 0:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        self.sorted = arr
        return self.counter
