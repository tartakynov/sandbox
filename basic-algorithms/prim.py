#!/usr/bin/env python


def min_span_tree(adjacency, vertices):
    n = len(adjacency)
    visited = [0]
    unvisited = range(1, n)
    total = 0
    edges = []
    while unvisited:
        u, v, m = 0, 0, 0
        for i in unvisited:
            for j in visited:
                if adjacency[i][j] == 0:
                    continue
                if adjacency[i][j] < m or m == 0:
                    u = i
                    v = j
                    m = adjacency[i][j]
        edges.append((vertices[u], vertices[v]))
        total += adjacency[u][v]
        unvisited.remove(u)
        visited.append(u)
    return total, edges


def main():
    adjacency = [
        [0, 7, 0, 5, 0, 0, 0],
        [7, 0, 8, 9, 7, 0, 0],
        [0, 8, 0, 0, 5, 0, 0],
        [5, 9, 0, 0, 15, 6, 0],
        [0, 7, 5, 15, 0, 8, 9],
        [0, 0, 0, 6, 8, 0, 11],
        [0, 0, 0, 0, 9, 11, 0]
    ]
    print min_span_tree(adjacency, ['A', 'B', 'C', 'D', 'E', 'F', 'G'])


if __name__ == "__main__":
    main()
