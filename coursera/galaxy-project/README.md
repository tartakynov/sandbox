# Write Up

I decided to upload the reads into Galaxy as a list of pairs. I got a collection of 3 pairs represented as a single dataset in my history and I can run each step on the whole dataset rather than individually for each read.Then I did QC for the dataset and combined the result into a single report with MultiQC. Although qualities go down on the ends, overall they're still good and stay above 30, so I decided not to trim the ends.
Then I ran Bowtie2 to align the reads to the reference genome. It took very long so I got bored with waiting and decided to try HISAT2 instead. HISAT2 was very fast so I decided to keep it.
For variant calling I used FreeBayes. After filtering out the low-quality sites I ran SnpEff to annotate the variants.
To get the top 5 genes with the largest number of polymorphic sites I broke compound variants into multiple independent variants with VcfAllelicPrimitives. Then I extracted the annotations and grouped them by gene names. It gave me the count of variants per gene, and I could easily identify 5 most polymorphic genes.

Finally, the results are
1. The number of SNPs is 2124.
2. The number of insertions 101, deletions 94.
3. The number of multi-nucleotide variants is 44.
4. The number of variants with multiple alternate alleles is 6.
5. Top five genes with the largest number of polymorphic sites sorted down from largest: RBFOX1, USP7, ABAT, LMF1, TSC2
