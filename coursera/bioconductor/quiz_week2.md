1. What is the GC content of `chr22` in the `hg19` build of the human genome?  
**Tip:** The reference genome includes `N` bases; you will need to exclude those.
```R
hello world
```

2. **Background:** In the previous assessment we studied H3K27me3 "narrowPeak" regions from the H1 cell line (recall that the Roadmap ID for this cell line is `E003`). We want to examine whether the GC content of the regions influence the signal; in other words wether the reported results appear biased by GC content.  
**Question:** What is mean GC content of H3K27me3 "narrowPeak" regions from Epigenomics Roadmap from the H1 stem cell line on chr 22.  
**Clarification:** Compute the GC content for each peak region as a percentage and then average those percentages to compute a number between 0 and 1.
```R
hello world
```

3. The "narrowPeak" regions includes information on a value they call "signalValue".  
**Question:** What is the correlation between GC content and "signalValue" of these regions (on chr22)?
```R
hello world
```

4. The "narrowPeak" regions are presumably reflective of a ChIP signal in these regions. To confirm this, we want to obtain the `fc.signal` data from AnnotationHub package on the same cell line and histone modification. This data represents a vector of fold-change enrichment of ChIP signal over input.  
**Question:** what is the correlation between the "signalValue" of the "narrowPeak" regions and the average `fc.signal` across the same regions?  
**Clarification:** First compute the average `fc.signal` for across each region, for example using "Views"; this yields a single number of each region. Next correlate these numbers with the "signalValue" of the "narrowPeaks".
```R
hello world
```

5. Referring to the objects made and defined in the previous question.  
**Question:** How many bases on chr22 have an fc.signal greater than or equal to 1?
```R
hello world
```

6. The H1 stem cell line is an embryonic stem cell line, a so-called pluripotent cell. Many epigenetic marks change upon differentiation. We will examine this. We choose the cell type with Roadmap ID `E055` which is foreskin fibroblast primary cells.  
We will use the `fc.signal` for this cell type for the H3K27me3 mark, on chr22. We now have a signal track for E003 and a signal track for E055. We want to identify regions of the genome which gain H3K27me3 upon differentiation. These are regions which have a higher signal in E055 than in E003. To do this properly, we would need to standardize (normalize) the signal across the two samples; we will ignore this for now.  
**Question:** Identify the regions of the genome where the signal in E003 is 0.5 or lower and the signal in E055 is 2 or higher.  
**Tip:** If you end up with having to intersect two different Views, note that you will need to convert the Views to IRanges or GRanges first with `ir <- as(vi, "IRanges")|ir<-as(vi,"IRanges")`.
```R
hello world
```

7. CpG Islands are dense clusters of CpGs. The classic definition of a CpG Island compares the observed to the expected frequencies of CpG dinucleotides as well as the GC content.  
Specifically, the observed CpG frequency is just the number of "CG" dinucleotides in a region. The expected CpG frequency is defined as the frequency of C multiplied by the frequency of G divided by the length of the region.  
**Question:** What is the average observed-to-expected ratio of CpG dinucleotides for CpG Islands on chromosome 22?
```R
hello world
```

8. A TATA box is a DNA element of the form "TATAAA". Around 25% of genes should have a TATA box in their promoter. We will examine this statement.  
**Question:** How many TATA boxes are there on chr 22 of build hg19 of the human genome?  
**Clarification:** You need to remember to search both forward and reverse strands.
```R
hello world
```

9. **Question:** How many promoters of transcripts on chromosome 22 containing a coding sequence, contains a TATA box on the same strand as the transcript?  
**Clarification:** Use the `TxDb.Hsapiens.UCSC.hg19.knownGene` package to define transcripts and coding sequence. Here, we defined a promoter to be 900bp upstream and 100bp downstream of the transcription start site.
```R
hello world
```

10. It is possible for two promoters from different transcripts to overlap, in which case the regulatory features inside the overlap might affect both transcripts. This happens frequently in bacteria.  
**Question:** How many bases on chr22 are part of more than one promoter of a coding sequence?  
**Clarification:** Use the TxDb.Hsapiens.UCSC.hg19.knownGene package to define transcripts and coding sequence. Here, we define a promoter to be 900bp upstream and 100bp downstream of the transcription start site. In this case, ignore strand in the analysis.
```R
hello world
```
