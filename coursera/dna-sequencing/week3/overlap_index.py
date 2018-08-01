#!/usr/bin/env python

"""
DNA overlap graph with basic k-mer indexing
"""

def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()  # skip name line
            seq = fh.readline().rstrip()  # read base sequence
            fh.readline()  # skip placeholder line
            qual = fh.readline().rstrip() # base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities

def overlap(a, b, min_length=3):
    start = 0
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a) - start
        start += 1

def create_index(reads, k):
    index = {}
    for read in reads:
        for i in range(len(read) - k + 1):
            kmer = read[i:i+k]
            if kmer in index:
                index[kmer].add(read)
            else:
                index[kmer] = set([read])
    return index

def create_overlap_map(index, reads, min_length):
    overlaps = {}
    for a in reads:
        for b in index.get(a[-min_length:], set()):
            if a == b:
                continue
            overlap_length = overlap(a, b, min_length)
            if overlap_length > 0:
                overlaps[(a, b)] = overlap_length
    return overlaps

def main():
    min_length = 30
    reads, _ = readFastq('ERR266411_1.for_asm.fastq')
    index = create_index(reads, min_length)
    omap = create_overlap_map(index, reads, min_length)
    print len(omap)
    print len(set([a for a, b in omap.keys()]))

if __name__ == '__main__':
    main()
