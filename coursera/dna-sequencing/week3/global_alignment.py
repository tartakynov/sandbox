"""
Global alignment
"""

from sys import stdout

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

def globalAlignment(a, b):
    alphabet = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    scores = [
       # A  C  G  T  -
        [0, 4, 2, 4, 8], # A
        [4, 0, 4, 2, 8], # C
        [2, 4, 0, 4, 8], # G
        [4, 2, 4, 0, 8], # T
        [8, 8, 8, 8, 8]  # -
    ]

    n, m = len(a), len(b)
    if n == 0 or m == 0:
        return n or m
    D = []
    for i in range(n + 1):
        D.append([0] * (m + 1))
    for i in range(1, n + 1): D[i][0] = D[i - 1][0] + scores[alphabet[a[i - 1]]][-1]
    for i in range(1, m + 1): D[0][i] = D[0][i - 1] + scores[-1][alphabet[b[i - 1]]]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(
                D[i - 1][j - 1] + scores[alphabet[a[i - 1]]][alphabet[b[j - 1]]],
                D[i - 1][j] + scores[alphabet[a[i - 1]]][-1],
                D[i][j - 1] + scores[-1][alphabet[b[j - 1]]]
            )
    printMatrix(a, b, D)
    return D[n][m]

def main():
    print globalAlignment('CGCTTC', 'CGCTC')

if __name__ == '__main__':
    main()