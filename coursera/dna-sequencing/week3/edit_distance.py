"""
Edit distance with dynamic programming
"""

from sys import stdout

def distance(x, y):
    if x == y:
        return 0
    return 1

def printMatrix(a, b, D):
    n, m = len(a), len(b)
    stdout.write("    ")
    for i in range(m + 1):
        stdout.write("%3s " % (b[i - 1] if i > 0 else "-"))
    print
    for i in range(n + 1):
        stdout.write("%3s " % (a[i - 1] if i > 0 else "-"))
        for j in range(m + 1):
            stdout.write("%3d " % D[i][j])
        print

def editDistanceRecursive(a, b):
    if len(a) == 0 or len(b) == 0:
        return len(a) or len(b)
    return min(
        editDistanceRecursive(a[:-1], b[:-1]) + distance(a[-1], b[-1]),
        editDistanceRecursive(a, b[:-1]) + 1,
        editDistanceRecursive(a[:-1], b) + 1
    )

def editDistanceDynamic(a, b):
    n, m = len(a), len(b)
    if n == 0 or m == 0:
        return n or m
    D = []
    for i in range(n + 1):
        D.append([0] * (m + 1))
    for i in range(0, n + 1): D[i][0] = i
    for i in range(0, m + 1): D[0][i] = i
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(
                D[i - 1][j - 1] + distance(a[i - 1], b[j - 1]),
                D[i - 1][j] + 1,
                D[i][j - 1] + 1
            )
    printMatrix(a, b, D)
    return D[n][m]

def main():
    print editDistanceDynamic('shake spea', 'Shakespear')

if __name__ == '__main__':
    main()