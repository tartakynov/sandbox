#!/usr/bin/env python

X = -1

class UnionFind(object):
    def __init__(self, n):
        self.components = n
        self.sz = [1] * n
        self.id = range(n)

    def union(self, a, b):
        root1, root2 = self.find(a), self.find(b)
        if (root1 == root2):
            return
        if (self.sz[root1] < self.sz[root2]):
            root1, root2 = root2, root1
        self.id[root2] = self.id[root1]
        self.sz[root1] += self.sz[root2]
        self.components -= 1

    def find(self, a):
        if (self.id[a] != a):
            self.id[a] = self.find(self.id[a])
        return self.id[a]

def kruskal(graph):
    """
    Returns min-span tree weights
    """
    n = len(graph)
    edges = []
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] != X:
                edges.append((i, j, graph[i][j]))
    edges.sort(key=lambda edge: edge[2])

    total = 0
    for a, b, w in edges:
        if uf.find(a) != uf.find(b):
            uf.union(a, b)
            total += w
    return total

def main():
    graph = [
        #A  B  C  D  E  F  G  H  I  J
        [X, 5, X, 4, 1, X, X, X, X, X], # A
        [5, 2, 4, 2, X, X, X, X, X, X], # B
        [X, 4, X, X, X, X, X, 4, 1, 2], # C
        [4, 2, X, X, 2, 5,11, 2, X, X], # D
        [1, X, X, 2, X, 1, X, X, X, X], # E
        [X, X, X, 5, 1, X, 7, X, X, X], # F
        [X, X, X,11, X, 7, X, 1, 4, X], # G
        [X, X, 4, 2, X, X, 1, X, 6, X], # H
        [X, X, 1, X, X, X, 4, 6, X, 0], # I
        [X, X, 2, X, X, X, X, X, 0, X]  # J
    ]

    print kruskal(graph)

if __name__ == "__main__":
    main()
