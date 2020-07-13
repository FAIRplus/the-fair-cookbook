>:bulb: __W.I.P__

# FASTQ file validation

[toc]

---

## Main Objectives

The main purpose of this recipe is:

> FASTQ file validation solutions. Available validators, how to select and how to use.

FASTQ file is the de facto sequencing file format, and it is the foundation of many downstream analysis. The downstream analysis is usually automated, time-consuming and error-prone. Hence it is important to validate FASTQ files before further analysis.

Also, intergrating FASTQ file variation to pipelines improves the reproducibility of the process and offers a better way to check the status.

"Its is a common practice to re-use data deposited in one of the large public repositories.  In some cases only highly processed quantitated data will be used, but often it is better to go back to lower level formats such as fastq files to run your analysis.  In these cases we rely on the repository providing accurate data from which we can work but there are a number of ways in which this can fail."

## Graphical Overview of the FAIRification Recipe Objectives

TODO
```mermaid
graph LR;
    A[Data Acquisition] -->B(Raw Data)
    B --> C{FAIR by Design}
    C -->|Yes| D[Standard Compliant Data]
    C -->|No| E[Vendor locked Data]
```

___
## User Stories

The table below listed use cases where the FASTQ files need to be validated. This recipe provides a solution to these users. and avoid going into too much detail.

|As a ..| I want to .. |So that I can ..|
|---|--|--|
|Data owner| validate my sequencing files before submission| avoid wasting time __submitting large corrupted files??__|
|Data consumer| validate the FASTQ files before running analysis|Avoid wasting time and resource on processing corrupted files|
|Data consumer| intergrate FASTQ validation into my data analysis pipeline| Build a more reproducible and error-proof pipeline| 
|Data manager| validate the FASTQ file I got from unknown source before depositing the file| Ensure the file is usable in the future.|


## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
|   |  |   |

----

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [Format validation](http://edamontology.org/operation_0336)  | [FASTQ file](http://edamontology.org/format_2182)  | Validation results  |


## Table of Data Standards

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| [FASTQ](http://edamontology.org/format_2182)  | |
___

Most validators detects FASTQ variants automaticlly. The Quality control of FASTQ file are not included in this recipe. 

FASTQ validators detect truncated reads, base calls and quality score mismatches, invalid encoding. For paired-end reads, they also checks if the forward reads have the same number of reads, and paired with the reverse reads. Most validators can detect different FASTQ variants and process compressed FASTQ files automatically.

[FASTQ-utils](https://github.com/nunofonseca/fastq_utils) is an open-source software to validate and process FASTQ files. It has been used in __popular archives___, European Nucleotide Archive, (ENA) and several research projects, __Human Cell Atlas__, for example.

Here is an example of validating FASTQ file with _FASTQ-utils_

### Step 1: Install fastq-utils
```shell
conda install -c bioconda fastq_utils
```
___fastq-utils_ can also be installed using the source code.__

### Step 2: Get example file for testing*
> *Users can skip this step and test with their own files.

__Here we provide two FASTQ examples in ENA for testing.__ The first example is _Ion Torrent S5_ sequencing FASTQ single read. The second example is _Illumina iSeq 100_ paired end sequencing files.

__Example 1: Get single read FASTQ file__

The command below downloads an _Ion Torrent S5_ fastq file from ENA. [This file](https://www.ebi.ac.uk/ena/browser/view/SRR12132977) is the Whole genome sequencing file of SARS-CoV-2. The complete file is 192Mb. 
```shell
wget -c ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR121/077/SRR12132977/SRR12132977.fastq.gz
```
Uses can inspect the _fastq.gz_ file using `gzip -cd SRR12132977.fastq.gz | head -8`. Below is the header of the FASTQ file.
```
@SRR12132977.1 1/1
AACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAACGAACAAACTAAAATGTCTGATAATGGACCCCAAAATCAGCGAAATGCACCCCGCATTACGTTTGGTGGACCCTCAG
+
C@CCD>DBC?B692;;;09?<BBBBC>BBBBBBBBB@?ABB@BC<BBB>@A?:999992;=>>@??==:=C;>=<:'555)8;;;;;AG:AAAAADD;CCBB>?@;;;0:<@A>CEE?CFCC
@SRR12132977.2 2/1
AACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAACGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAACTAATTACTGTCGTTGACAGGACACGAGTAACTCGTCTATCTTCTGCAGGCTGCTTACGGTTTCGTCCGTGTTGCAGCCGATCATCAGCAC
+
A>A@@=@@F@D@C<999,:<@ABBBB@B=>=BB@BBB?@@><;;7>??=BBB>BDD;D>????@@;@CDC@@@BBB>BBB@AAC>>9BBBB;;;@@?;><::;99<9<;A;>><@@A:=:>@@@>A@>:>===>:=<<>>;;;>=BCAA?>=A>>>:==>;998<=;===@@@<>>9>>>?;??==:=>>>>:>>;;;;;;;<;;
```
__Example 2: Get paired-read FASTQ files__

The command below downloads Illumina iSeq 100 paired end sequencing files from ENA. [These files](https://www.ebi.ac.uk/ena/data/view/SRR11542244) are raw sequence reads of a SARS-CoV-2 sample. Each file is 26 Mb.

```shell
wget -c \
ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR115/044/SRR11542244/SRR11542244_1.fastq.gz \
ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR115/044/SRR11542244/SRR11542244_2.fastq.gz
```
Below is the headers of the two files. The paired info are indicated in the read ID.
```
# Header of the forward read, SRR11542244_1.fastq.gz
@SRR11542244.1 1/1
GTGTGTGTATACATATATATATATATCACATTTTCTTTATCCATTTATCTGTTGTTGGACACTTAGGTTGATTCCATATCTTGGCTATTGTGAATAGTG
+
,,FFFFFFFFFFFFFFFFFFFFFFFF:FFF:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF:FFFFFFFFFFFF:FFFFFFFFFFFFFFFFFFFFFF
@SRR11542244.2 2/1
GTGATTCCTCAAAGATTTAGAACCAGAAATACCATGTGACCCAGCAATTCCATTACCAGGTCTAAACCCAAAGGAATATAAATCATTCTGTAATGAAGATA
+
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF


# Header of the reverse read, SRR11542244_2.fastq.gz
@SRR11542244.1 1/2
CTATTGGGTATTTAATCCAAAGAAAGGAAATCGGTATATCAAAGAGACATCTGCATGCCCATGTTTATTGTAGCACTATTCACAATAGCCAAGATATGGAA
+
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF:FFFFFFFFFFFFFFFFFFFF
@SRR11542244.2 2/2
GAACATATGTGTGCATGTATCTTCATTACAGAATGATTTATATTCCTTTGGGTTTAGACCTGGTAATGGAATTGCTGGGTCACATGGTATTTCTGGTTCTA
+
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
```


### Step 3: Perform validation

The command below validates the single read file in _Example 1_. 

```shell
fastq_info -r SRR12132977.fastq.gz
```
Here is an validation result. __Explain quality encoding__
```
Skipping check for duplicated read names
1900000
------------------------------------
Number of reads: 1919741
Quality encoding range: 34 77
Quality encoding: 33
Read length: 25 352 215
OK
```

The validation of paired end reads is similar to single read file validation.

```shell
fastq_info -s SRR11542244_1.fastq.gz SRR11542244_2.fastq.gz
```
Here is an example output.
```
DEFAULT_HASHSIZE=39000001
Scanning and indexing all reads from SRR11542244_1.fastq.gz
700000Scanning complete.

Reads processed: 733611
Memory used in indexing: ~47 MB
------------------------------------
Number of reads: 733611
Quality encoding range: 35 70
Quality encoding: 33
Read length: 35 101 96
OK
```
_fastq_util_ also provides additional argument to customize the validation:
`-s`: to validate two paired fastq files when the reads are sorted in the same way.
`-r`: to skip duplicated read names validation. This uses less memory and runs faster.
    `-r`: Skip check for duplicated read names. The validation uses less memory and runs faster.
    
 -h  : print this help message
 -s  : the reads in the two fastq files have the same ordering
 -e  : do not fail with empty files
 -q  : do not fail if quality encoding cannot be determined
 -r  : skip check for duplicated readnames


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
:bulb: :bulb: :bulb:
If the paired-end reads doens't match, it returns
```
```
__Example invalid files and outputs__

#### Overview of fastq utils

|Aspects|Validation content |Description|FASTQ-utils|
|--|--|--|--|
|Basic validation|4-line format|Check if the FASTQ file validates the format|:heavy_check_mark:|
| |Character encoding| Check if the base calls and quality score encoding are correct.  |:heavy_check_mark:| 
||Read length| check if the length of the base calls are the same as that of the quality scores|:heavy_check_mark:|
||File truncation|Check if the file is truncated or not|:heavy_check_mark:|
|Paired end reads| Deinterleaved paired reads| Forward and reverse reads are provided in two files.|:x:|
| |Interleaved _"8-line"_ files|Forward and reverse reads are provided together as an 8-line file|:x:|
|Compressed files| gzip| Compressed fastq files, with extension `fastq.gz`|:heavy_check_mark:|
|FASTQ variants| fastq-illumina|A fastq varaint, using PHRED score. </br> ASCII character offset = 66|:heavy_check_mark:|
| |fastq-sanger|A fastq varaint, using PHRED score.</br> ASCII character offset = 33|:heavy_check_mark:||
| |fastq- solexa|A fastq varaint, using Solexa quality score| |
|File by sequencing machines|Illumina|FASTQ files produced by Illumina sequencing machines|:heavy_check_mark:|
| |nanopore|FASTQ files produced by Illumina sequencing machines |:heavy_check_mark:|:x:|
| |454 |FASTQ files produced by Illumina sequencing machines|:heavy_check_mark:|:x:|
| |pacbio|FASTQ files produced by Illumina sequencing machines| :heavy_check_mark:|:x:|
|performance| memory||`N/A`|
| |speed| |`N/A`|
|Archieve compatiablity|ENA|File validated can be submitted to the ENA archive.|:heavy_check_mark:|
||ArrayExpress|File validated can be submitted to Array Express.|:heavy_check_mark:|
||SRA|File validated can be submitted to the SRA archive.|:heavy_check_mark:|
|Interface|Command line interface||:heavy_check_mark:|
|License|Free license|A license allowing use the data 'freely', e.g."CC-BY"|:heavy_check_mark:|
|Code|Open source|Source code available on public platforms|:heavy_check_mark:|
 
## Summary






## Authors
|Name|Institute|ORCID|Contributions|
|--|--|--|--|
|Fuqi Xu|[EMBL-EBI](https://www.ebi.ac.uk/)|[0000-0002-5923-3859](https://orcid.org/0000-0002-5923-3859)|Writing - Original Draft|
|Eva Martin | [Barcelona Supercomputing Center (BSC)](https://www.bsc.es/) |[0000-0001-8324-2897](https://orcid.org/0000-0001-8324-2897)|Writing |

## License

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>