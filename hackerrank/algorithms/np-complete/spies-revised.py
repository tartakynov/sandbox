#!/usr/bin/env python

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


def number_of_blown_covers(solution):
    """
    Total number of blown covers
    """
    return 0


def hill_climber(n):
    """
    Runs until either solution is found (no blown covers) or we are stuck at a local optima
    """
    solution = random_solution(n)
    current_score = number_of_blown_covers(solution)
    while current_score > 0:
        stuck = True
        for i in xrange(n):
            for j in xrange(i + 1, n):
                transition = solution[:]
                transition[i], transition[j] = solution[j], solution[i]
                next_score = number_of_blown_covers(transition)
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
    print hill_climber(11)


if __name__ == "__main__":
    main()
