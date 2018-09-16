## Questions 1 - 5
For the original set of alignments (file `athal_wu_0_A.bam`):

1. How many alignments does the set contain?
```console
$ samtools view athal_wu_0_A.bam | wc -l
221372
```

2. How many alignments show the read's mate unmapped?
```console
$ samtools view athal_wu_0_A.bam | cut -f7 | grep "*" | wc -l
65521
```

3. How many alignments contain a deletion (D)?
```console
$ samtools view athal_wu_0_A.bam | cut -f6 | grep "D" | wc -l
2451
```

4. How many alignments show the read’s mate mapped to the same chromosome?
```console
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
```console
$ samtools view athal_wu_0_A.bam "Chr3:11,777,000-11,794,000" | wc -l
7081
```

7. How many alignments show the read's mate unmapped?
```console
$ samtools view athal_wu_0_A.bam "Chr3:11,777,000-11,794,000" | cut -f7 | grep "*" | wc -l
1983
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

11. How many sequences are in the genome file?
```console
$ samtools view -H athal_wu_0_A.bam | grep "@SQ" | wc -l
7
```

12. What is the length of the first sequence in the genome file?
```console
$ samtools view -H athal_wu_0_A.bam | grep "@SQ" | head -n1 | cut -f3
LN:29923332
# answer: 29923332
```

13. What alignment tool was used?
```console
$ samtools view -H athal_wu_0_A.bam | grep "@PG" | cut -f2
ID:stampy
# answer: stampy
```

14. What is the read identifier (name) for the first alignment?
```console
$ samtools view athal_wu_0_A.bam | head -n1 | cut -f1
GAII05_0002:1:113:7822:3886#0
```

15. What is the start position of this read’s mate on the genome? Give this as ‘chrom:pos’ if the read was mapped, or * if unmapped.
```console
$ samtools view athal_wu_0_A.bam | head -n1 | cut -f3,7,8
Chr3	=	11700332
# answer: Chr3:11700332
```

## Questions 16 - 20
Using BEDtools, examine how many of the alignments at point 2 overlap exons at the locus of interest. Use the BEDtools `-wo` option to only report non-zero overlaps. The list of exons is given in the included `athal_wu_0_A_annot.gtf` GTF file.

16. How many overlaps (each overlap is reported on one line) are reported?
```console
$ bedtools intersect -wo -a athal_wu_0_A_annot.gtf -b athal_wu_0_A.bam | wc -l
3101
```

17. How many of these are 10 bases or longer?
```console
$ bedtools intersect -wo -a athal_wu_0_A_annot.gtf -b athal_wu_0_A.bam | cut -f16 | grep -E "^[0-9]{2,}$" | wc -l
2899
```

18. How many alignments overlap the annotations?
```console
$ bedtools intersect -wo -a athal_wu_0_A_annot.gtf -b athal_wu_0_A.bam | wc -l
3101
```

19. Conversely, how many exons have reads mapped to them?
```console
$ bedtools intersect -u -a athal_wu_0_A_annot.gtf -b athal_wu_0_A.bam | wc -l
21
```

20. If you were to convert the transcript annotations in the file `athal_wu_0_A_annot.gtf` into BED format, how many BED records would be generated?
```console
$ cut -f9 athal_wu_0_A_annot.gtf | cut -d ';' -f2 | uniq -c | wc -l
4
```
