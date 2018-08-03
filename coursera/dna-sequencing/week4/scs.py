#!/usr/bin/env python

"""
Shortest common superstring
"""

from itertools import permutations

def overlap(a, b, min_length=3):
    start = 0
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a) - start
        start += 1

def scs_bruteforce(ss):
    shortest_sup = None
    for ssperm in permutations(ss):
        sup = ssperm[0]
        for i in range(len(ss) - 1):
            olen = overlap(ssperm[i], ssperm[i + 1], min_length = 1)
            sup += ssperm[i + 1][olen:]
        if shortest_sup is None or len(sup) < len(shortest_sup):
            shortest_sup = sup
    return shortest_sup

def scs_bruteforce_multi(ss):
    shortest_length = 0
    shortest_sups = []
    for ssperm in permutations(ss):
        sup = ssperm[0]
        for i in range(len(ss) - 1):
            olen = overlap(ssperm[i], ssperm[i + 1], min_length = 1)
            sup += ssperm[i + 1][olen:]
        if shortest_length == 0:
            shortest_length = len(sup)
            shortest_sups.append(sup)
        elif len(sup) < shortest_length:
            shortest_length = len(sup)
            shortest_sups = [sup]
        elif len(sup) == shortest_length:
            shortest_length = len(sup)
            shortest_sups.append(sup)
    return shortest_sups

if __name__ == '__main__':
    print len(scs_bruteforce(['CCT', 'CTT', 'TGC', 'TGG', 'GAT', 'ATT']))
    print scs_bruteforce_multi(['CCT', 'CTT', 'TGC', 'TGG', 'GAT', 'ATT'])
