"""
Genome sequences overlap
"""

def overlap(a, b, min_length=3):
    start = 0
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a) - start
        start += 1

def main():
    print overlap('ATTCGACCTATCCTTGCG', 'CTTGCGCAGCTCGAGA')

if __name__ == '__main__':
    main()
