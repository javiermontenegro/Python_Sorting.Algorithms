#********************************************************************
# Filename:  ShellSort.py
# Author:    Javier Montenegro (https://javiermontenegro.github.io/)
# Copyright:
# Details:   This code is the implementation of the shell sort algorithm.
#*********************************************************************

def shell_sort(arr):

    n = len(arr)
    gap = int(n / 2)

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap = int(gap / 2)


if __name__ == "__main__":

    collection = [12, 34, 54, 2, 3]
    print("List numbers: %s\n" % repr(collection))

    shell_sort(collection)
    print("Ordered list: %s" % collection)
