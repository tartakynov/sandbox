#!/usr/bin/env python


def swap(a, first, second):
    tmp = a[first]
    a[first] = a[second]
    a[second] = tmp


def subsets(arr):
    """
    Prints all subsets (power set).
    The number of subsets in the power set is 2 ^ n.
    """
    print "subsets:", arr
    print "========================"
    print


def subsets_of_size(arr, k):
    """
    Prints all subsets of size k elements (k-combinations of n).
    The number of such combinations is binomial coefficient.
    """
    print "subsets of size %d:" % k, arr
    print "========================"
    print


def permutations(arr):
    """
    Prints all permutations.
    The number of permutations of n distinct objects is n factorial
    """

    def loop(a, index):
        if index <= 0:
            print a
        else:
            loop(a, index - 1)
            pos = len(a) - index
            for i in xrange(pos + 1, len(a)):
                swap(a, pos, i)
                loop(a, index - 1)
                swap(a, i, pos)

    print "permutations:", arr
    loop(arr, len(arr))
    print "========================"
    print


def permutations_of_size(arr, k):
    """
    Prints all permutations of give size (k-permutations of n).
    The number of such permutations is n!/(n-k)!
    """

    def loop(a, index):
        if index <= (len(a) - k):
            print a[:k]
        else:
            loop(a, index - 1)
            pos = len(a) - index
            for i in xrange(pos + 1, len(a)):
                swap(a, pos, i)
                loop(a, index - 1)
                swap(a, i, pos)

    print "permutations of size %d:" % k, arr
    loop(arr, len(arr))
    print "========================"
    print


def main():
    subsets([1, 2, 3, 4, 5])
    subsets_of_size([1, 2, 3, 4, 5], 3)
    permutations([1, 2, 3])
    permutations_of_size([1, 2, 3], 2)


if __name__ == "__main__":
    main()
