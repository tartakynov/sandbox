#!/usr/bin/env python

"""
De Bruijn graph
"""

def debruijn(s, k):
    edges = []
    nodes = set()
    for i in range(len(s) - k + 1):
        edges.append((s[i:i+k-1], s[i+1:i+k]))
        nodes.add(s[i:i+k-1])
        nodes.add(s[i+1:i+k])
    return nodes, edges

if __name__ == '__main__':
    nodes, edges = debruijn('abacad', 3)
    print nodes
    print edges
