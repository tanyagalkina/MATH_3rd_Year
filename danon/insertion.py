from copy import deepcopy
from my_compar import my_compar


class Insertion:
    def __init__(self, given_list):
        self.given_list = deepcopy(given_list)
        self.sorted = []
        self.counter = 0

    def bench(self):
        arr = self.given_list
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and my_compar(self, key, arr[j]) >= 0:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        self.sorted = arr

        return self.counter
        print(self.sorted)



