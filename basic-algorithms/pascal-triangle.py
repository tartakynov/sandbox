#!/usr/bin/env python

"""
https://en.wikipedia.org/wiki/Pascal%27s_triangle
"""


import numpy as np
from math import factorial


def triangle_formula(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def triangle_dp(memo, n, k):
    if memo[n][k] == 0:
        if k == 0 or k == n:
            memo[n][k] = 1
        else:
            memo[n][k] = triangle_dp(memo, n - 1, k - 1) + triangle_dp(memo, n - 1, k)
    return memo[n][k]


def main():
    n, k = 16, 3
    memo_size = max(n, k) + 1
    memo = np.zeros(shape=(memo_size, memo_size), dtype=int)
    print "binomial coefficient =", triangle_formula(n, k)
    print "dynamic programming =", triangle_dp(memo, n, k)
    print memo


if __name__ == "__main__":
    main()
