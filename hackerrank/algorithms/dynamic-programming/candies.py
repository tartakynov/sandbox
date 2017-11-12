#!/usr/bin/env python

"""
https://www.hackerrank.com/challenges/candies/problem
"""


def solution(n, ratings):
    result = [0] * n

    # up trends
    candies, prev_rating = 0, 0
    for i in xrange(n):
        candies = candies + 1 if ratings[i] > prev_rating else 1
        result[i] = candies
        prev_rating = ratings[i]

    # down trends
    candies, prev_rating = 0, 0
    for i in xrange(n - 1, -1, -1):
        candies = candies + 1 if ratings[i] > prev_rating else 1
        result[i] = max(result[i], candies)
        prev_rating = ratings[i]

    return result


def main():
    n = int(raw_input().strip())
    arr = [int(raw_input().strip()) for _ in range(n)]
    print sum(solution(n, arr))


if __name__ == "__main__":
    main()
