import random
import sys

"""
Solves N-queens problem with Min-conflicts algorithm
https://en.wikipedia.org/wiki/Min-conflicts_algorithm
"""


def are_diagonal(x1, y1, x2, y2):
    """
    Check if the line between the two points is at a 45 degree angle to the horizontal
    """

    return abs(x1 - x2) == abs(y1 - y2)


def cell_hits(n, solution, cell_x, cell_y):
    """
    Number of queens hitting the given cell
    """

    total = 0
    for queen_x in range(n):
        queen_y = solution[queen_x]
        if queen_y == cell_y or are_diagonal(cell_x, cell_y, queen_x, queen_y):
            total += 1
    return total


def random_threatened_queen(n, solution, tmp):
    """
    Select a random threatened queen

    :param n: The size of the solution array
    :param solution: Solution array
    :param tmp: Intermediate data storage
    :return: Position of random threatened queen in solution array, or -1 if there's no threatened queens
    """

    threatened_queens_count = 0
    for i in xrange(n):
        if cell_hits(n, solution, i, solution[i]) > 1:  # 1 because the queen hits the cell it is standing on
            tmp[threatened_queens_count] = i
            threatened_queens_count += 1

    if threatened_queens_count == 0:
        return -1

    return tmp[random.randint(0, threatened_queens_count - 1)]


def random_min_conflict_position(queen, n, solution, tmp):
    """
    Best possible position for the given queen. It is the position that minimizes number of other
    queens threatening the given queen.

    :param queen: The queen for which we're calculating the position
    :param n: The size of the solution array
    :param solution: Solution array
    :param tmp: Intermediate data storage
    :return:
    """

    # calculate number of threats for the queen at position i
    min_threats = n * n
    for i in xrange(n):
        tmp[i] = cell_hits(n, solution, queen, i)
        if tmp[i] < min_threats:
            min_threats = tmp[i]

    # move the queen to a square where number of threats is minimal
    count = 0
    for i in xrange(n):
        if tmp[i] == min_threats:
            tmp[count] = i
            count += 1

    return tmp[random.randint(0, count - 1)]


def minimize_conflicts(n, solution, max_iterations=1000):
    """
    Solves an N-queens problem with https://en.wikipedia.org/wiki/Min-conflicts_algorithm

    :param n: The size of the solution array
    :param solution: Solution array
    :param max_iterations: Total number of iterations before giving up
    :return: None
    """

    tmp = [0] * n  # intermediate storage
    for k in range(max_iterations):
        queen = random_threatened_queen(n, solution, tmp)
        if queen < 0:
            return

        solution[queen] = random_min_conflict_position(queen, n, solution, tmp)
    raise Exception("Incomplete solution: try more iterations.")


def print_grid(n, solution, out=sys.stdout):
    """
    Print the solution grid for debug
    """

    for i in xrange(n):
        for j in xrange(n):
            out.write('1  ' if solution[i] == j else '0  ')
        out.write('\n')


def main():
    n = 5
    solution = range(n)
    minimize_conflicts(n, solution)
    print_grid(n, solution)


if __name__ == "__main__":
    main()

