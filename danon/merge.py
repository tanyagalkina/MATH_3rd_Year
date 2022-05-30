from copy import deepcopy
from my_compar import my_compar


def merge(ob, left, right):
    merged = []
    while left and right:
        diff = my_compar(ob, left[0], right[0])
        if diff < 0:
            merged.append(left[0])
            left = left[1:]
        else:
            merged.append(right[0])
            right = right[1:]
    merged += left
    merged += right
    return merged


def merge_sort(ob, array):
    list_len = len(array)
    if list_len <= 1:
        return array
    left, right = [], []
    for i in range(0, list_len):
        if i < list_len // 2:
            left.append(array[i])
        else:
            right.append(array[i])
    left = merge_sort(ob, left)
    right = merge_sort(ob, right)
    ret = merge(ob, left, right)
    return ret


class Merge:
    def __init__(self, given_list):
        self.given_list = deepcopy(given_list)
        self.counter = 0
        self.sorted = merge_sort(self, self.given_list)

    def bench(self):
        return self.counter
