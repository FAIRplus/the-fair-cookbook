>:bulb: __W.I.P__

# FASTQ file validation

## Summary
FASTQ file validation solutions. Available validators, how to select and how to use.

## Why validating FASTQ files
- FASTQ is de facto sequencing file format. 
- Downstream anlaysis are automated, time-consuming, error-prone.
- "FAIR by design"/best practice/recommendation/culture change

## When/why do I need this recipe (Scope)
:man: I need to work with FASTQ files and would like to know the ABC of FASTQ files to continue my work. But I don't care about the details.
:woman: I want to learn the general approach of how to get a validator and why I need to perform validation. "FAIR by design"

## Popular downstream analysis
- samtools
- fastqQC. (QC vs validation)
- BLAST
- & related formats
- .sam, .bam, .bai
- .fastq.gz, .fa 

### FASTQ file specification 
>TODO: Point to Eva's FASTQ specification recipe

FASTQ format "standard" definition [here](https://academic.oup.com/nar/article/38/6/1767/3112533)

" NCBI SRA makes all its data available as standard Sanger FASTQ files"

> TODO: summarize the common specification and highlight the differences


> TODO add mermaid graph

```mermaid
graph TB  

```

### Use cases
- :heavy_plus_sign: As a data owner, I want to validate my FASTQ file to make sure it is submittable to public archives.
- :heavy_plus_sign: As a data consumer, I want to validate the FASTQ file before running analysis to avoid wasting time on corrupted files.
- :heavy_plus_sign: As a data consumer, I want to check if the FASTQ file I got from unknown source is valid before depositing the file

### Challenges in FASTQ validation
- different variants
Example variants [here](https://academic.oup.com/view-large/82650903)

Difference between `fastq-sanger`, `fastq-illumina`, and `fastq-solexa`. Ignore format `ABI SOLID sequencing`: 
- how the quality score is calculated-
- How the quality score is represented.
> TODO: test how the validator handles ASCII 33, 59. (whether fastq-sanger and fastq-solexa compatiable)
> TODO: is fastq-solexa still in use?
- large size

### Common errors.

### Where to find the FASTQ validators
- bio.tools
- Archives, e.g SRA, ENA, ArrayExpress
- ? _forums, publications?_
- 

### Avaiable fastq validators
|Valiators| Users|
|---|---|
|FASTQ utils| Used by ENA|
|samtools htsjdk library| Used by ENA+EGA| 
| LibStatGen: FASTQ| [GH](https://github.com/statgen/fastQValidator) [documentaion](https://genome.sph.umich.edu/wiki/FastQValidator)
| Fqtools | [paper](https://academic.oup.com/bioinformatics/article/32/12/1883/1744334)

### What does it validate
:woman: What to pay attention when I get a validator

#### Basics
- "The ability to process the full range of valid FASTQ files;"
    - "a corresponding quality line with the same number of characters"
    - "correctly formatted, basically that it consists of groups of 4 lines"
    - ends with a new line, that it isn't truncated

- "The ability to detect the full range of FASTQ errors" 

test files provided [here](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/nar/38/6/10.1093_nar_gkp1137/2/gkp1137_Supplementary_Data.zip?Expires=1596783175&Signature=oXlAOGzTznD3Kpg3aRUJ3bkG8Xpe9ddYoEN0nVPt5i8e5vCFb0rxhj-qIMA4hV2mvkaN4uJu3Uh5zPfXqGqq0RebK~Z4lR7xhBrFZIvMfeSRE9-QZwkamwBc1thR5skoczq9h3zXh1qAuaXo-iOaHe7FzDHIrIYk9t9awAIG190JY8to8NYY0XUH0lnzu6SiIKyKj-N5du-DNk~q0t~bnd~PD656NIm-2~s91Js82AVJB5-PRUcP4GvIXq-v96yGXclhU2Ib70Hpu0t1PsLugpV75qHmZZ7bEabBBQj5iXsSJUVln~0dDA8Bs0wtI8nLQcaBW46OEI7ESsdGeHZOZQ__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)
- truncated reads, examples where the sequence
- quality lengths differ
- and invalid ASCII characters in the quality lines.
#### Advanced 

- "The ability to read and write compressed data"
- " The processing speed."
- paired-end reads: "The two files of a paired reads run have the same size and number of sequences"

### How to choose

|Validators| |FASTQ-utils|validatior_2|XX|XX|XX|
|--|--|--|--|--|--|--|
|basic validation*|line length |:heavy_check_mark:|:x:||
| | ascii code| ||| 
|FASTQ variants| fastq-illumina| :heavy_check_mark:|:x:|
| |fastq-sanger| :heavy_check_mark:|:x:|
| |fastq- solexa| :heavy_check_mark:|:x:|
|Paired end reads validation| paired-reads as seperate files| :heavy_check_mark:|:x:|
| |interleaved _"8-line"_ files|:heavy_check_mark:|:x:|
| |concatenated files| :heavy_check_mark:|:x:|
|interface| GUI|:heavy_check_mark:|:x:|
| | CLI| :heavy_check_mark:|:x:|
|by sequencing machine|illumina|:heavy_check_mark:|:x:|
| |nanopore| :heavy_check_mark:|:x:|
| |454 |:heavy_check_mark:|:x:|
| |pacbio| :heavy_check_mark:|:x:|
|performance| memory requirement| :heavy_check_mark:|:x:|
| |speed| :heavy_check_mark:|:x:|
|compressed files| gzip| :heavy_check_mark:|:x:|
| | bzip2|:heavy_check_mark:|:x:|
 

*what is basic validation

- Validation purpose: for personal use, for data submission, etc.
- Special requirement: paired ends, _.gz_ files 
- speed

["Benchmark data for various FASTQ processing tools."](https://academic.oup.com/view-large/84799791)

benchmarking details [here](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/bioinformatics/32/12/10.1093_bioinformatics_btw088/2/btw088_Supplementary_Data.zip?Expires=1595360722&Signature=yeN19WVt31E1zHxBBhgN9MHxvLMLOjozIUYAtZowqQVYjvWTTzEEq1Gx4PX8h5abHv7HQaGhZvzKZQ~FiM6ots3ODYx1ci7jm~nzwlK3-L5tXGKI6UFsTm1I-pZkw0aBVdJBUEHj666M59qbpPfnjZzjSlA9-lm3c-0CgzTPsv77hYwK7MMKVbZHNd8ccqEdiNAp174TOu6RMj~bJpUmhFr0yOFnXWSyUVStWZwp9dWa7hLaUWAlMUqoof~WE4JtPGXEf-AHY21B5~FR~odj2~oP3NzYYw9cQ7DaQKRzqA2nvkacPEiuq0wjrR5ThRTx0Tj6QKjdINuPUdq5cx0O3A__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)
|Tool| Valid | Invalid | Process .gz | Plain (reads/s)	|Compressed (reads/)|
|--|--|--|--|--|--|
|fqtools|Y |	Y| 	R+W| 	701 375 |	444 |648 


considerations in [fqtools paper](https://academic.oup.com/bioinformatics/article/32/12/1883/1744334)

 - The ability to process the full range of valid FASTQ files;
 - The ability to detect the full range of FASTQ errors;
 - The ability to read and write compressed data; and
 - The processing speed.



### Example of how to use a FASTQ utils
#### online validators
#### local validators
An example of validating FASTQ files with _fastq-utils_.

__Step 1: Installing fastq-utils__
```shell
conda install -c bioconda fastq_utils
```

__Step 2: Get example test file__ 

To test the validator, we use Illumina iSeq 100 paired end sequencing; SARS-CoV-2/186197/human/2020/Malaysia_EPI_ISL_417919  files from [ENA](https://www.ebi.ac.uk/ena/data/view/SRR11542244).

Users can also test with their own paired end files.
```shell
# Get example paired-end data
wget -c ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR115/044/SRR11542244/SRR11542244_1.fastq.gz

wget -c ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR115/044/SRR11542244/SRR11542244_2.fastq.gz
```

__Step 3: Validate paired end files__ 
```shell
fastq_info SRR11542244_1.fastq.gz SRR11542244_2.fastq.gz
```
Optional Arguments:
    `-s`: "used when the reads are sorted in the same way in two paired fastq files"
    `-r`: Skip check for duplicated read names. The validation uses less memory and runs faster.

Example output
```shell
fastq_utils 0.23.0
DEFAULT_HASHSIZE=39000001
Scanning and indexing all reads from SRR11542244_1.fastq.gz
700000Scanning complete.

Reads processed: 733611
Memory used in indexing: ~47 MB
File SRR11542244_1.fastq.gz processed
Next file SRR11542244_2.fastq.gz
700000
------------------------------------
Number of reads: 733611
Quality encoding range: 35 70
Quality encoding: 33
Read length: 35 101 96
OK
```
TODO: removed 2 reads from SRR_2 still valid? how to check paired end?


### Considerations

> From Tony's doc
- memory requirements: "astQValidator checks for unique sequence names, it may use a large amount of memory - this can be disabled by specifying the --disableSeqI"
- ENA and EGA uses _samtools_ but with additional custom logic for checking the correct sets of files are received depending on the technology
- paired read files are now validated seperately in the recipes
- 10x sequencing we require BAM/CRAM rather than FASTQ because of the potential for missing barcodes
- long reads produced by nanopore [link](https://www.nature.com/articles/nbt.2181)

__Define which senario we want to cover in this recipe__ 

## Authors
|Name|Institute|ORCID|Contributions|
|--|--|--|--|
|Fuqi Xu|[EMBL-EBI](https://www.ebi.ac.uk/)|[0000-0002-5923-3859](https://orcid.org/0000-0002-5923-3859)|Writing - Original Draft|
|Eva Martin | [Barcelona Supercomputing Center (BSC)](https://www.bsc.es/) |[0000-0001-8324-2897](https://orcid.org/0000-0001-8324-2897)|Writing |

## License

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
