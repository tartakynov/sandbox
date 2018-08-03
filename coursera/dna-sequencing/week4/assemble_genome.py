#!/usr/bin/env python

"""
De Novo Assembly of the sample genome from the reads
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

def create_overlap_graph(index, reads, min_length):
    graph = {}
    for a in reads:
        for b in index.get(a[-min_length:], set()):
            if a == b:
                continue
            olen = overlap(a, b, min_length)
            if olen > 0:
                if a not in graph:
                    graph[a] = b
                elif olen > overlap(a, graph[a]):
                    graph[a] = b
    return graph

def scs(graph):
    queue = set(graph.keys()).difference(graph.values())
    if len(queue) != 1:
        return None
    genome = ''
    while queue:
        node = queue.pop()
        olen = overlap(genome, node, 0)
        genome += node[olen:]
        if node in graph:
            queue.add(graph[node])
    return genome

def main():
    # expected genome size is 15894
    min_length = 30
    reads, _ = readFastq('ads1_week4_reads.fq')
    index = create_index(reads, min_length)
    graph = create_overlap_graph(index, reads, min_length)
    genome = scs(graph)
    print len(genome)
    print genome.count('A')
    print genome.count('T')

if __name__ == '__main__':
    main()
