#!/usr/bin/env python

"""
https://www.hackerrank.com/challenges/coin-change/problem
"""


def coin_change(memo, n, m, coin_types):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if m <= 0:
        return 0
    if memo[n][m] == -1:
        memo[n][m] = coin_change(memo, n, m - 1, coin_types) + coin_change(memo, n - coin_types[m - 1], m, coin_types)
    return memo[n][m]


def main():
    n, m = map(int, raw_input().strip().split(" "))
    coin_types = map(int, raw_input().strip().split(" "))
    memo = [[-1] * (m + 1) for _ in range(n + 1)]
    print coin_change(memo, n, m, coin_types)


if __name__ == "__main__":
    main()
