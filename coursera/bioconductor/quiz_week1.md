Use the AnnotationHub package to obtain data on "CpG Islands" in the human genome.
```R
> ah = AnnotationHub()
> ah_cpg_islands = query(ah, c("hg19", "CpG Islands"))
> cpg_islands = ah_cpg_islands[[1]]
```

1. How many islands exists on the autosomes?
```R
> cpg_islands_autosomes = keepStandardChromosomes(cpg_islands, pruning.mode = "coarse")
> cpg_islands_autosomes = dropSeqlevels(cpg_islands_autosomes, c("chrX", "chrY", "chrM"), pruning.mode = "coarse")
> length(cpg_islands_autosomes)
[1] 26641
```

2. How many CpG Islands exists on chromosome 4.
```R
> cpg_islands_chr4 = keepSeqlevels(cpg_islands, c("chr4"), pruning.mode = "coarse")
> length(cpg_islands_chr4)
[1] 1031
```

Obtain the data for the H3K4me3 histone modification for the H1 cell line from Epigenomics Roadmap, using AnnotationHub. Subset these regions to only keep regions mapped to the autosomes (chromosomes 1 to 22).
```R
> ah_h3k4me3 = query(ah, c("hg19", "H3K4me3", "H1 Cell"))
> ah_h3k4me3
> h3k4me3 = ah_h3k4me3[[2]]
> h3k4me3_autosomes = keepStandardChromosomes(h3k4me3, pruning.mode = "coarse")
> h3k4me3_autosomes = dropSeqlevels(h3k4me3_autosomes, c("chrX", "chrY", "chrM"), pruning.mode = "coarse")
```

3. How many bases does these regions cover?
```R
> sum(width(reduce(h3k4me3_autosomes, ignore.strand = TRUE)))
[1] 41135164
```

Obtain the data for the H3K27me3 histone modification for the H1 cell line from Epigenomics Roadmap, using the AnnotationHub package. Subset these regions to only keep regions mapped to the autosomes. In the return data, each region has an associated "signalValue".
```R
> ah_h3k27me3 = query(ah, c("hg19", "H3K27me3", "H1 Cell"))
> ah_h3k27me3
> h3k27me3 = ah_h3k27me3[[2]]
> h3k27me3_autosomes = keepStandardChromosomes(h3k27me3, pruning.mode = "coarse")
> h3k27me3_autosomes = dropSeqlevels(h3k27me3_autosomes, c("chrX", "chrY", "chrM"), pruning.mode = "coarse")
```

4. What is the mean signalValue across all regions on the standard chromosomes?
```R
> mean(h3k27me3_autosomes$signalValue)
[1] 4.770728
```

Bivalent regions are bound by both H3K4me3 and H3K27me3.
```R
> bivalent = intersect(h3k27me3_autosomes, h3k4me3_autosomes, ignore.strand = TRUE)
```

5. Using the regions we have obtained above, how many bases on the standard chromosomes are bivalently marked?
```R
> sum(width(bivalent))
[1] 10289096
```

We will examine the extent to which bivalent regions overlap CpG Islands.

6. how big a fraction (expressed as a number between 0 and 1) of the bivalent regions, overlap one or more CpG Islands?
```R
> length(subsetByOverlaps(bivalent, cpg_islands_autosomes)) / length(bivalent)
[1] 0.5383644
```

7. How big a fraction (expressed as a number between 0 and 1) of the bases which are part of CpG Islands, are also bivalent marked
```R
> sum(width(intersect(bivalent, cpg_islands_autosomes))) / sum(width(cpg_islands_autosomes))
[1] 0.241688
```

8. How many bases are bivalently marked within 10kb of CpG Islands?
```R
> cpg_islands_autosomes_10k = resize(cpg_islands_autosomes, width = 20000 + width(cpg_islands_autosomes), fix = "center")
> sum(width(intersect(bivalent, cpg_islands_autosomes_10k)))
[1] 9782086
```

9. How big a fraction (expressed as a number between 0 and 1) of the human genome is contained in a CpG Island?  
**Tip 1:** the object returned by AnnotationHub contains "seqlengths".  
**Tip 2:** you may encounter an integer overflow. As described in the session on R Basic Types, you can address this by converting integers to numeric before summing them, "as.numeric()".
```R
hg19 = ah[["AH5018"]]
hg19_autosomes = keepStandardChromosomes(hg19, pruning.mode = "coarse")
hg19_autosomes = dropSeqlevels(hg19_autosomes, c("chrX", "chrY", "chrM"), pruning.mode = "coarse")
sum(width(cpg_islands_autosomes)) / sum(as.numeric(seqlengths(hg19_autosomes)))
[1] 0.007047481
```

10. Compute an odds-ratio for the overlap of bivalent marks with CpG islands.
```R
```
