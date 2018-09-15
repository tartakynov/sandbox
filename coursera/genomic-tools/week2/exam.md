## Questions 1 - 5
For the original set of alignments (file `athal_wu_0_A.bam`):

1. How many alignments does the set contain?
```console
$ samtools view athal_wu_0_A.bam | wc -l
221372
```

2. How many alignments show the read's mate unmapped?
```console
samtools view -f 0x08 athal_wu_0_A.bam | wc -l
2903
```

3. How many alignments contain a deletion (D)?
```console
$ samtools view athal_wu_0_A.bam | cut -f6 | grep "D" | wc -l
2451
```

4. How many alignments show the read’s mate mapped to the same chromosome?
```console
# $ samtools view -F 0x08 athal_wu_0_A.bam | cut -f7 | grep "=" | wc -l
# 148010
$ samtools view athal_wu_0_A.bam | cut -f7 | grep "=" | wc -l
150913
```

5. How many alignments are spliced?
```console
$ samtools view athal_wu_0_A.bam | cut -f6 | grep "N" | wc -l
0
```

## Questions 6 - 10
Extract only the alignments in the range `Chr3:11,777,000-11,794,000`, corresponding to a locus of interest. For this alignment set

6. How many alignments does the set contain?
```
$ samtools view athal_wu_0_A.bam "Chr3:11,777,000-11,794,000" | wc -l
7081
```

7. How many alignments show the read's mate unmapped?
```console
$ samtools view -f 0x08 athal_wu_0_A.bam "Chr3:11,777,000-11,794,000" | wc -l
483
```

8. How many alignments contain a deletion (D)?
```console
$ samtools view athal_wu_0_A.bam "Chr3:11,777,000-11,794,000" | cut -f6 | grep "D" | wc -l
31
```

9. How many alignments show the read’s mate mapped to the same chromosome?
```console
$ samtools view athal_wu_0_A.bam "Chr3:11,777,000-11,794,000" | cut -f7 | grep "=" | wc -l
4670
```

10. How many alignments are spliced?
```console
$ samtools view athal_wu_0_A.bam "Chr3:11,777,000-11,794,000" | cut -f6 | grep "N" | wc -l
0
```

## Questions 11 - 15
Determine general information about the alignment process from the original BAM file.

## Questions 16 - 20
Using BEDtools, examine how many of the alignments at point 2 overlap exons at the locus of interest. Use the BEDtools `-wo` option to only report non-zero overlaps. The list of exons is given in the included `athal_wu_0_A_annot.gtf` GTF file.
