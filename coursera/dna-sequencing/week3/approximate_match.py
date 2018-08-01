"""
Approximate match with dynamic programming
"""

from sys import stdout

def distance(x, y):
    if x == y:
        return 0
    return 1

def printMatrix(p, t, D):
    n, m = len(p), len(t)
    stdout.write("    ")
    for i in range(m + 1):
        stdout.write("%3s " % (t[i - 1] if i > 0 else "-"))
    print
    for i in range(n + 1):
        stdout.write("%3s " % (p[i - 1] if i > 0 else "-"))
        for j in range(m + 1):
            stdout.write("%3d " % D[i][j])
        print

def approximate_match(p, t):
    n, m = len(p), len(t)
    if n == 0 or m == 0:
        return n or m
    D = []
    for i in range(n + 1):
        D.append([0] * (m + 1))
    for i in range(0, n + 1): D[i][0] = i
    for i in range(0, m + 1): D[0][i] = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(
                D[i - 1][j - 1] + distance(p[i - 1], t[j - 1]),
                D[i - 1][j] + 1,
                D[i][j - 1] + 1
            )
    printMatrix(p, t, D)
    return min(D[-1])

def main():
    print approximate_match('GCGTATGC', 'TATTGGCTATACGGTT')

if __name__ == '__main__':
    main()