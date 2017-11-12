#!/usr/bin/env python


def shortest_path(adjacency, vertices, a, b):
    n = len(adjacency)
    start, finish = vertices.index(a), vertices.index(b)
    unvisited = range(n)
    parents = [0] * n
    distances = [1000000] * n
    distances[start] = 0
    u_prev = -1
    while unvisited:
        u = unvisited[0]
        for i in unvisited:
            if distances[i] < distances[u]:
                u = i
        parents[u] = u_prev
        for i in xrange(n):
            if adjacency[u][i] > 0 and i in unvisited:
                distances[i] = min(distances[u] + adjacency[u][i], distances[i])
        unvisited.remove(u)
        u_prev = u

    path = []
    p = finish
    while p != -1:
        path.insert(0, vertices[p])
        p = parents[p]
    return distances[finish], path


def main():
    adjacency = [
        [0, 14, 0, 0, 7, 9],
        [14, 0, 9, 0, 0, 2],
        [0, 9, 0, 6, 0, 0],
        [0, 0, 6, 0, 15, 11],
        [7, 0, 0, 15, 0, 10],
        [9, 2, 0, 11, 10, 0]
    ]
    print shortest_path(adjacency=adjacency, vertices=['A', 'B', 'C', 'D', 'E', 'F'], a='A', b='C')


if __name__ == "__main__":
    main()
