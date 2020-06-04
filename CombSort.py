#********************************************************************
# Filename:  CombSort.py
# Author:    Javier Montenegro (https://javiermontenegro.github.io/)
# Copyright:
# Details:   This code is the implementation of the comb sort algorithm.
#*********************************************************************

from math import floor

def comb_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(floor(gap / shrink))
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True

        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                swap(i, i + gap)
                sorted = False
            i = i + 1


if __name__ == "__main__":

    collection = [1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100,
         4, 423, 2, 564, 9, 0, 10, 43, 64, 32, 1, 999]
    print("List numbers: %s\n" % repr(collection))

    comb_sort(collection)
    print("Ordered list: %s" % collection)
