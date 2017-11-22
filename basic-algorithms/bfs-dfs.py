#!/usr/bin/env python


def bfs(graph, start):
    queue = [start]
    visited = []
    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.append(current)
            queue.extend(graph[current])
    return visited


def dfs(graph, start, visited=set(), result=[]):
    visited.add(start)
    for current in graph[start]:
        if current not in visited:
            dfs(graph, current, visited)
    result.append(start)
    return result


def adjacency_to_graph(matrix, vertices):
    graph = dict()
    for i, v1 in enumerate(vertices):
        for j, v2 in enumerate(vertices):
            if matrix[i][j] > 0:
                if v1 not in graph:
                    graph[v1] = set()
                if v2 not in graph:
                    graph[v2] = set()
                graph[v1].add(v2)
                graph[v2].add(v1)

    return graph


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
    graph = adjacency_to_graph(adjacency, ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    print dfs(graph, 'A')
    print bfs(graph, 'A')


if __name__ == "__main__":
    main()
