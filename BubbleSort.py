#********************************************************************
# Filename:  BubbleSort.py
# Author:    Javier Montenegro (https://javiermontenegro.github.io/)
# Copyright:
# Details:   This code is the implementation of the bubble sort algorithm.
#*********************************************************************

def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True


if __name__ == "__main__":

    collection = [1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100,
         4, 423, 2, 564, 9, 0, 10, 43, 64, 32, 1, 999]
    print("List numbers: %s\n" % repr(collection))

    bubble_sort(collection)
    print("Ordered list: %s" % collection)
