#********************************************************************
# Filename:  InsertionSort.py
# Author:    Javier Montenegro (https://javiermontenegro.github.io/)
# Copyright:
# Details:   This code is the implementation of the insertion sort algorithm.
#*********************************************************************

def insertion_sort(arr):
    for i, cursor in enumerate(arr):
        pos = i
        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos -= 1
        # Break and do the final swap
        arr[pos] = cursor
    return arr


if __name__ == "__main__":

    collection = [1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100,
         4, 423, 2, 564, 9, 0, 10, 43, 64, 32, 1, 999]
    print("List numbers: %s\n" % repr(collection))

    insertion_sort(collection)
    print("Ordered list: %s" % collection)
