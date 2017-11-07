#!/usr/bin/env python


def binary_search(arr, elem):
    low, high = 0, len(arr)
    while low < high:
        print arr[low:high], elem
        m = (low + high) / 2
        if elem < arr[m]:
            high = m
        elif elem > arr[m]:
            low = m + 1
        else:
            return m
    return -1


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print binary_search(arr, 1)
    print binary_search(arr, 18)


if __name__ == "__main__":
    main()
