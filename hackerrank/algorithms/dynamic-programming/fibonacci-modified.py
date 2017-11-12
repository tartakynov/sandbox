#!/usr/bin/env python

"""
https://www.hackerrank.com/challenges/fibonacci-modified/problem
"""


def fib_mod(t1, t2, n):
    memo = [0] * n
    memo[0] = t1
    memo[1] = t2
    for i in xrange(2, n):
        memo[i] = memo[i - 2] + memo[i - 1] * memo[i - 1]
    return memo[n - 1]


def main():
    t1, t2, n = map(int, raw_input().strip().split(" "))
    print fib_mod(t1, t2, n)


if __name__ == "__main__":
    main()
