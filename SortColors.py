#********************************************************************
# Filename:  SortColors.py
# Author:    Javier Montenegro (https://javiermontenegro.github.io/)
# Copyright:
# Details:   This code is the implementation of the sort colors algorithm.
#*********************************************************************


def sort_colors(nums):
    i = j = 0
    for k in range(len(nums)):
        v = nums[k]
        nums[k] = 2
        if v < 2:
            nums[j] = 1
            j += 1
        if v == 0:
            nums[i] = 0
            i += 1


if __name__ == "__main__":

    collection = [0, 1, 1, 1, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 2, 2]
    print("List numbers: %s\n" % repr(collection))

    sort_colors(collection)
    print("Ordered list: %s" % collection)
