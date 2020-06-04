#********************************************************************
# Filename:  SelectionSort.py
# Author:    Javier Montenegro (https://javiermontenegro.github.io/)
# Copyright:
# Details:   This code is the implementation of the selection sort algorithm.
#*********************************************************************

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    
    for i in range(1, len(arr)):
        
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []

    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    
    return new_arr


if __name__ == "__main__":

    collection = [100, 5, 72, 41, 80, 1, 99, 36, 27, 78]
    print("List numbers: %s\n" % repr(collection))

    result = selection_sort(collection)
    print("Ordered list: %s" % result)

