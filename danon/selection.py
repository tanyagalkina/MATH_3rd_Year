from copy import deepcopy
from my_compar import my_compar


class Selection:
    def __init__(self, given_list):
        self.given_list = deepcopy(given_list)
        self.counter = 0
        self.sorted = []

    def bench(self):
        arr = self.given_list
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if my_compar(self, arr[min_idx], arr[j]) > 0:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        self.sorted = arr
        return self.counter
