# FASTQ format specification

[TOC]

## Main Objectives
This recipe contains a description the different old and currently used FASTQ variants. The aim is to allow a user to undestand the FASTQ format and be able to differentiate and convert from one format variant to another.

## Requirements
This recipe is aimed at anyone interested in the FASTQ format. No specific prior knowledge is needed in order to understand this document. 

## Ingredients
This is a descriptive recipe, so no ingredients are required.

## Introduction
FASTQ is the *de facto* format for sequence data exchange. It offers a simple way to store raw requences along with quality scores associates to each base pair. Unfortunately, different inconpatile FASTQ variants exist, while there is no community explicit agreement on an standard. 

## General Specification
### Format description
A FASTQ file describes a collection of reads sequence, sequence quality scores and other information. Each reads description consists in four plain text, all in the following form:
- 1st: A defline that contains a read identifier and possibly other information.This line must start with the symbol "@".
- 2nd: Nucleotide base calls.
- 3rd: A second defline for extra information. This line must start with the symbol "+", apart from which the line can be left empty.
- 4th: Per-base quality scores, usually PHRED scores (described bellow).

An example of FASTQ format is shown bellow.
```
@SEQ_ID
GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT
+
!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65
```

### Quality scores encoding: PHRED scores

PHRED scores has become the de facto standard to represent sequenceing base qualities. For a given nucleotide call, a PHRED score consists in a single character (or byte), restricted to ASCII printable characters 32-126 (decimal). PHRED socres makes both an space efficient enough and human readable way to encode base pairs qualities.  
The different FASTQ variants, however, use a different mapping algorithm for PHRED scores, making them incompatible and indistinguishable.


## Main FASTQ variants
### Sanger
---
 Sanger FASTQ files use ASCII 33–126 to encode PHRED qualities from 0 to 93 (i.e. PHRED scores with an ASCII offset of 33).

This gives a very broad range of error probabilities, from 1.0 (a wrong base) through to 10−9.3 (an extremely accurate read) and so the Sanger FASTQ format is useful both for raw sequencing reads and post-processed assemblies where higher qualities occur.

---
### Solexa 
---
Although the FASTQ format only records a single quality score per letter, Solexa also produced other files with quality scores for all four bases, and in order to represent low-quality information more fully an alternative logarithmic mapping was used (15)


---

### Illumina 1.3+

---
Although Illumina initially continued to use the Solexa FASTQ variant, from Genome Analyzer Pipeline version 1.3 onwards (16), PHRED quality scores rather than Solexa scores were used. 
Later, Illumina introduced a third incompatible FASTQ variant designed to be interchangeable with their earlier ‘Solexa FASTQ’ files for good quality reads.

The Illumina 1.3+ FASTQ variant encodes PHRED scores with an ASCII offset of 64, and so can hold PHRED scores from 0 to 62 (ASCII 64–126), although currently raw Illumina data quality scores are only expected in the range 0–40.

---

## Special cases
### Incompatibilities
Sanger, Solexa and Illumiona 1.3+ FASTQ variants PHRED scores are incompatible with each other. To make files in various of these formats interoperable, thay must be converted to a same variant. The variant of choice is usually Sanger, due to the wide compatibility of this variant with most software([TODO look for examples - SSAHA2, MAQ, Velvet, BWA and BowTie]). 

[TODO] Conversions

### Paired-end reads
                                                                               
For a single-read run, one Read 1 (R1) FASTQ file is created for each sample per flow cell lane. 
However, for paired-end runs, the way the output depoends on the platform. There are two possiblilities, either (i) two files are generated for each run, each containing the reads called in one direction, or (ii) all calls are stored in the same FASTQ file.  
[TODO] 

- Illumina
- Roche 454
- Ion Torrent 


## Platform specific considerations
[TODO] Intro to this section
- Recent Illumina fastq
```
@<instrument>:<run number>:<flowcell ID>:<lane>:<tile>:<xpos>:<y-pos> <read>:<is filtered>:<control number>:<index>
```

- Older Illumina fastq
```
@<machine_id>:<lane>:<tile>:<x_coord>:<y_coord>#<index>/<read>
```

- QIIME de-multiplexed sequences in fastq
```
@<SampleID-based_identifier> <Original_information> orig_bc=<original_barcode> new_bc=<corrected_barcode> bc_diffs=<0|1>
```
- PacBio CCS (Circular Consensus Sequence) or RoI (Read of Insert) read
```
@<MovieName>/<ZMW_number>
```
- PacBio CCS subread
```
@<MovieName> /<ZMW_number>/<subread-start>_<subread-end>
```
- Helicos fastq with a fixed ASCII-based Phred value for quality
```
@VHE-242383071011-15-1-0-2
```
Characteristic use of a quality '/', which gives a Phred value of 14.
The native format for helicos is fasta so converting to fastq requires creating a default quality score.



## File extension
`.fastq` and `.fq` are usually used, but no standard file extension exists for this format. 


## Summary

## Referencies
[TODO] [NCBI file format Guide](https://www.ncbi.nlm.nih.gov/sra/docs/submitformats/#fastq-files) 
[TODO] [The Sanger FASTQ file format for sequences with quality scores, and the Solexa/Illumina FASTQ variants](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2847217/)
[TODO] [Illumina documentation](https://emea.support.illumina.com/bulletins/2016/04/fastq-files-explained.html)

## Authors
|Name|Institute|ORCID|Contributions|
|--|--|--|--|
|Eva Martin | [Barcelona Supercomputing Center (BSC)](https://www.bsc.es/) |[0000-0001-8324-2897](https://orcid.org/0000-0001-8324-2897)|Writing - Original Draft |
|Fuqi Xu|[EMBL-EBI](https://www.ebi.ac.uk/)|[0000-0002-5923-3859](https://orcid.org/0000-0002-5923-3859)|Writing - Original Draft|


## License

<a ref="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
