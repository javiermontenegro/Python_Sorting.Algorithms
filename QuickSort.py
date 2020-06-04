#********************************************************************
# Filename:  QuickSort.py
# Author:    Javier Montenegro (https://javiermontenegro.github.io/)
# Copyright:
# Details:   This code is the implementation of the quick sort algorithm.
#*********************************************************************

def quick_sort(arr, first, last):
    """ Quicksort
        Complexity: best O(n) avg O(n log(n)), worst O(N^2)
    """
    if first < last:
        pos = partition(arr, first, last)
        
        # Start our two recursive calls
        quick_sort(arr, first, pos - 1)
        quick_sort(arr, pos + 1, last)


def partition(arr, first, last):
    wall = first
    for pos in range(first, last):
        if arr[pos] < arr[last]:  # last is the pivot
            arr[pos], arr[wall] = arr[wall], arr[pos]
            wall += 1
    arr[wall], arr[last] = arr[last], arr[wall]
    return wall


if __name__ == "__main__":

    collection = [1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100, 4, 423, 2, 564, 9, 0, 10, 43, 64]
    print("List numbers: %s\n" % repr(collection))

    quick_sort(collection, 0, len(collection) - 1)
    print("Ordered list: %s" % collection)
