"""
Genome sequences overlap
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

def naive_overlap_map(reads, min_length=3):
    overlaps = {}
    for a, b in permutations(reads, 2):
        overlap_length = overlap(a, b, min_length)
        if overlap_length > 0:
            overlaps[(a, b)] = overlap_length
    return overlaps

def main():
    print overlap('ATTCGACCTATCCTTGCG', 'CTTGCGCAGCTCGAGA')
    print naive_overlap_map(['ATTCGACCT', 'GACCTATCCTT', 'CTTGCGCAGCTCGAGA'])

if __name__ == '__main__':
    main()
