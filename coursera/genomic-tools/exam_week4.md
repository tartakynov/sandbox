You are performing an RNA-seq experiment to determine genes that are differentially expressed at different stages in the development of Arabidopsis thaliana shoot apical meristem. You collected samples at day 8 and day 16 (files `Day8.fastq` and `Day16.fastq`), extracted and sequenced the cellular mRNA, and are now set to perform the bioinformatics analysis. The reference genome you will need for the analysis is `athal_chr.fa` and the reference gene annotations are in `athal_genes.gtf`. Use default parameters unless otherwise specified. Sample command files that you can modify to create your own pipeline are provided in the file `commands.tar.gz`. All files are provided in the archive `gencommand_proj4.tar.gz`.

Create a bowtie index of the genome using bowtie2-build, with the prefix `athal`. Include a copy of the reference genome with the name `athal.fa` in the index directory.

```console
$ mkdir athal
$ cp athal_chr.fa athal/athal.fa
$ bowtie2-build athal/athal.fa athal/athal
```

## Apply to question 1-10.
Align both RNA-seq data sets to the reference genome using tophat. Analyze the results to answer the following questions. If multiple answers are required for one question, separate the answers with a space (e.g., 1000 2000).
```console
$ tophat2 -o Day8 -p 2 athal/athal Day8.fastq
$ tophat2 -o Day16 -p 2 athal/athal Day16.fastq
```

1. How many alignments were produced for the `Day8` RNA-seq data set?
```console
$ samtools view Day8/accepted_hits.bam | wc -l
63845
```

2. How many alignments were produced for the `Day16` RNA-seq data set?
```console
$ samtools view Day16/accepted_hits.bam | wc -l
58398
```

3. How many reads were mapped in `Day8` RNA-seq data set?
```console
$ samtools view Day8/accepted_hits.bam | cut -f1 | sort | uniq | wc -l
63489
```

4. How many reads were mapped in `Day16` RNA-seq data set?
```console
$ samtools view Day16/accepted_hits.bam | cut -f1 | sort | uniq | wc -l
57951
```

5. How many reads were uniquely aligned in `Day8` RNA-seq data set?
```console
$ samtools view Day8/accepted_hits.bam | cut -f1 | sort | uniq -u | wc -l
63133
```

6. How many reads were uniquely aligned in `Day16` RNA-seq data set?
```console
$ samtools view Day16/accepted_hits.bam | cut -f1 | sort | uniq -u | wc -l
57504
```

7. How many spliced alignments were reported for `Day8` RNA-seq data set?
```console
$ samtools view Day8/accepted_hits.bam | cut -f6 | grep -c N
8596
```

8. How many spliced alignments were reported for `Day16` RNA-seq data set?
```console
$ samtools view Day16/accepted_hits.bam | cut -f6 | grep -c N
10695
```

9. How many reads were left unmapped from `Day8` RNA-seq data set?
```console
$ samtools view Day8/unmapped.bam | cut -f1 | sort | uniq | wc -l
84
```

10. How many reads were left unmapped from `Day16` RNA-seq data set?
```console
$ samtools view Day16/unmapped.bam | cut -f1 | sort | uniq | wc -l
34
```

## Apply to question 11-20.
Assemble the aligned RNA-seq reads into genes and transcripts using cufflinks. Use the labels `Day8` and `Day16`, respectively, when creating identifiers. For this portion of the analysis, answer the following questions.
```console
cufflinks -o Day8/cufflinks -L Day8 -p 2 Day8/accepted_hits.bam
cufflinks -o Day16/cufflinks -L Day16 -p 2 Day16/accepted_hits.bam
```

11. How many genes were generated by cufflinks for Day8?
```console
$ tail -n +2 Day8/cufflinks/genes.fpkm_tracking | cut -f4 | sort | uniq | wc -l
186
```

12. How many genes were generated by cufflinks for Day16?
```console
$ tail -n +2 Day16/cufflinks/genes.fpkm_tracking | cut -f4 | sort | uniq | wc -l
80
```

13. How many transcripts were reported for Day8?
```console
$ cut -f3 Day8/cufflinks/transcripts.gtf | grep -c transcript
192
```

14. How many transcripts were reported for Day16?
```console
$ cut -f3 Day16/cufflinks/transcripts.gtf | grep -c transcript
92
```

15. How many single transcript genes were produced for Day8?
```console
$ cut -f9 Day8/cufflinks/transcripts.gtf | cut --delimiter ";" -f1,2 | sort | uniq | cut --delimiter ";" -f1 | uniq -u | wc -l
180
```

16. How many single transcript genes were produced for Day16?
```console
$ cut -f9 Day16/cufflinks/transcripts.gtf | cut --delimiter ";" -f1,2 | sort | uniq | cut --delimiter ";" -f1 | uniq -u | wc -l
69
```

17. How many single-exon transcripts were in the Day8 set?
```console
$ cut -f9 Day8/cufflinks/transcripts.gtf | grep "exon_number" | cut --delimiter=";" -f2,3 | sort | uniq | cut --delimiter=";" -f1 | uniq -u | wc -l
119
```

18. How many single-exon transcripts were in the Day16 set?
```console
$ cut -f9 Day16/cufflinks/transcripts.gtf | grep "exon_number" | cut --delimiter=";" -f2,3 | sort | uniq | cut --delimiter=";" -f1 | uniq -u | wc -l
24
```

19. How many multi-exon transcripts were in the Day8 set?
```console
$ cut -f9 Day8/cufflinks/transcripts.gtf | grep "exon_number" | cut --delimiter=";" -f2,3 | sort | uniq | cut --delimiter=";" -f1 | uniq -d | wc -l
73
```

20. How many multi-exon transcripts were in the Day16 set?
```console
$ cut -f9 Day16/cufflinks/transcripts.gtf | grep "exon_number" | cut --delimiter=";" -f2,3 | sort | uniq | cut --delimiter=";" -f1 | uniq -d | wc -l
68
```

## Apply to question 21-30.
Run cuffcompare on the resulting cufflinks transcripts, using the reference gene annotations provided and selecting the option '-R' to consider only the reference transcripts that overlap some input transfrag. For this step, using the \*.tmap files answer the following, for both sets.
```console
$ cuffcompare -R -r athal_genes.gtf Day8/cufflinks/transcripts.gtf -o Day8/cuffcompare
$ cuffcompare -R -r athal_genes.gtf Day16/cufflinks/transcripts.gtf -o Day16/cuffcompare
```

21. How many cufflinks transcripts fully reconstruct annotation transcripts in Day8?
```console
$ cut -f3 Day8/cufflinks/cuffcompare.transcripts.gtf.tmap | grep -c =
16
```

22. How many cufflinks transcripts fully reconstruct annotation transcripts in Day16?
```console
$ cut -f3 Day16/cufflinks/cuffcompare.transcripts.gtf.tmap | grep -c =
36
```

23. How many splice variants does the gene AT4G20240 have in the Day8 sample?
```console
$ grep -c AT4G20240 Day8/cufflinks/cuffcompare.transcripts.gtf.tmap
2
```

24. How many splice variants does the gene AT4G20240 have in the Day16 sample?
```console
$ grep -c AT4G20240 Day16/cufflinks/cuffcompare.transcripts.gtf.tmap
0
```

25. How many cufflinks transcripts are partial reconstructions of reference transcripts (`contained`)? (Day8)
```console
$ cut -f3 Day8/cufflinks/cuffcompare.transcripts.gtf.tmap | grep -c "^c$"
133
```

26. How many cufflinks transcripts are partial reconstructions of reference transcripts (`contained`)? (Day16)
```console
$ cut -f3 Day16/cufflinks/cuffcompare.transcripts.gtf.tmap | grep -c "^c$"
21
```

27. How many cufflinks transcripts are novel splice variants of reference genes? (Day8)
```console
$ cut -f3 Day8/cufflinks/cuffcompare.transcripts.gtf.tmap | grep -c "^j$"
14
```

28. How many cufflinks transcripts are novel splice variants of reference genes? (Day16)
```console
$ cut -f3 Day16/cufflinks/cuffcompare.transcripts.gtf.tmap | grep -c "^j$"
22
```

29. How many cufflinks transcripts were formed in the introns of reference genes? (Day8)
```console
$ cut -f3 Day8/cufflinks/cuffcompare.transcripts.gtf.tmap | grep -c "^i$"
4
```

30. How many cufflinks transcripts were formed in the introns of reference genes? (Day16)
```console
$ cut -f3 Day16/cufflinks/cuffcompare.transcripts.gtf.tmap | grep -c "^i$"
1
```

## Apply to question 31-35.
Perform the differential gene expression analysis. For this, in a first stage run cuffmerge using the provided annotation to merge and reconcile the two sets of cufflinks transcripts. Make a note of the resulting file, `merged.gtf`. In a second step, use cufdiff to perform the differential expression analysis.

```console
$ mkdir -p cuffmerge
$ echo `pwd`/Day8/cufflinks/transcripts.gtf > cuffmerge/GTFs.txt
$ echo `pwd`/Day16/cufflinks/transcripts.gtf >> cuffmerge/GTFs.txt
$ cuffmerge -g athal_genes.gtf -p 2 -o cuffmerge cuffmerge/GTFs.txt
$
$ mkdir cuffdiff
$ cuffdiff -o cuffdiff -p 2 cuffmerge/merged.gtf \
          Day8/accepted_hits.bam \
          Day16/accepted_hits.bam
```

NOTE: Note that in general at least three replicates per condition are required to establish statistical significance. The single replicate example is provided here only to illustrate the analysis.

31. How many genes (loci) were reported in the merged.gtf file?
```console
$ cut -f9 merged.gtf | cut --delimiter=";" -f1 | sort | uniq | wc -l
129
```

32. How many transcripts?
```console
$ cut -f9 merged.gtf | cut --delimiter=";" -f2 | sort | uniq | wc -l
200
```

33. How many genes total were included in the gene expression report from cuffdiff?
```console
$ cut -f2 gene_exp.diff | tail -n +2 | sort | uniq | wc -l
129
```

34. How many genes were detected as differentially expressed?
```console
$ grep yes -c gene_exp.diff
4
```

35. How many transcripts were differentially expressed between the two samples?
```console
$ grep yes -c tss_group_exp.diff
5
```
