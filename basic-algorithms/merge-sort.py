#!/usr/bin/env python


def merge_sort(arr):
    def merge(src, dst, low, middle, high):
        i, j = low, middle
        for c in xrange(low, high):
            if i < middle and (j >= high or src[i] <= src[j]):
                dst[c] = src[i]
                i += 1
            else:
                dst[c] = src[j]
                j += 1

    def recursion(src, dst, low, high):
        if (high - low) > 1:
            m = (low + high) / 2
            recursion(dst, src, low, m)
            recursion(dst, src, m, high)
            merge(src, dst, low, m, high)

    tmp = arr[:]
    recursion(tmp, arr, 0, len(arr))


def main():
    arr = [7, 2, 4, 5, 0, 3, 6, 8, 1, 9]
    merge_sort(arr)
    print arr


if __name__ == "__main__":
    main()
