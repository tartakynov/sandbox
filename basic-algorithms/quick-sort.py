#!/usr/bin/env python


def qsort(arr):
    def swap(pos1, pos2):
        tmp = arr[pos1]
        arr[pos1] = arr[pos2]
        arr[pos2] = tmp

    def partition(low, high):
        p = arr[high]
        i = low - 1
        for j in xrange(low, high):
            if arr[j] < p:
                i += 1
                swap(i, j)
        swap(i + 1, high)
        return i + 1

    def recursion(low, high):
        if low < high:
            p = partition(low, high)
            recursion(low, p - 1)
            recursion(p + 1, high)

    recursion(0, len(arr) - 1)


def main():
    arr = [7, 2, 4, 5, 0, 3, 6, 8, 1, 9]
    qsort(arr)
    print arr


if __name__ == "__main__":
    main()
