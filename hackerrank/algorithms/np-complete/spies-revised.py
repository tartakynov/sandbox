#!/usr/bin/env python

import sys
from random import shuffle

"""
https://www.hackerrank.com/challenges/spies-revised/problem
Solved with hill climbing technique
"""


def random_solution(n):
    """
    Init random solution
    """
    solution = range(n)
    shuffle(solution)
    return solution


def collinear(x1, y1, x2, y2, x3, y3):
    """
    Check if three points are collinear
    """

    return (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2)


def diagonal(x1, y1, x2, y2):
    """
    Check if the line between the two points is at a 45 degree angle to the horizontal
    """

    return abs(x1 - x2) == abs(y1 - y2)


def number_of_blown_covers(n, solution):
    """
    Total number of blown covers
    """

    count = 0
    for x1 in xrange(n):
        for x2 in xrange(x1 + 1, n):
            y1, y2 = solution[x1], solution[x2]
            if diagonal(x1, y1, x2, y2):
                count += 1
            for x3 in xrange(x2 + 1, n):
                y3 = solution[x3]
                if collinear(x1, y1, x2, y2, x3, y3):
                    count += 1
    return count


def hill_climber(n):
    """
    Runs until either solution is found (no blown covers) or we are stuck at a local optima
    """
    solution = random_solution(n)
    current_score = number_of_blown_covers(n, solution)
    while current_score > 0:
        stuck = True
        for i in xrange(n):
            for j in xrange(i + 1, n):
                transition = solution[:]
                transition[i], transition[j] = solution[j], solution[i]
                next_score = number_of_blown_covers(n, transition)
                if next_score < current_score:
                    solution = transition
                    current_score = next_score
                    stuck = False
                    break
        if stuck:
            break

    return n, current_score, solution


def print_grid(out, n, solution):
    """
    Prints the grid for debug
    """
    for i in xrange(n):
        for j in xrange(n):
            out.write('S ' if solution[i] == j else '* ')
        out.write('\n')


def main():
    n, score, solution = hill_climber(9)
    print solution, score
    print_grid(sys.stdout, n, solution)


if __name__ == "__main__":
    main()
