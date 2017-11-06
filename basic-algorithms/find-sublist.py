#!/usr/bin/env python


def find_sublist(lst, sub):
    for i in xrange(len(lst) - len(sub)):
        is_sublist = True
        for j in xrange(len(sub)):
            if lst[i + j] != sub[j]:
                is_sublist = False
                break
        if is_sublist:
            return i
    return -1


def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print find_sublist(lst, [3, 4, 5])
    print find_sublist(lst, [0, 1, 2])


if __name__ == "__main__":
    main()

