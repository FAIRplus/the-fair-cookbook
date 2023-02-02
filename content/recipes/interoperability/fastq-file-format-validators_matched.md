(fcb-interop-fastqval)=
# File format validation, FASTQ example


````{panels_fairplus}
:identifier_text: FCB030
:identifier_link: 'https://w3id.org/faircookbook/FCB030'
:difficulty_level: 2
:recipe_type: hands_on
:reading_time_minutes: 15
:intended_audience: principal_investigator, data_manager, data_scientist 
:maturity_level: 0
:maturity_indicator: 0
:has_executable_code: yeah
:recipe_name: Validating file format - FASTQ example
```` 

## Main Objectives

The main purpose of this recipe is to:

> - provide a FAST (URL_TO_INSERT_RECORD_6000 https://fairsharing.org/FAIRsharing.p5df9c) Q file validation solution
> - propose a general file validation workflow. 

## Graphical Overview


````{dropdown} 
:open:
```{figure} fastq-validation.png
---
width: 350px
name: Validating FAST (URL_TO_INSERT_RECORD_6003 https://fairsharing.org/FAIRsharing.p5df9c) Q open standard (URL_TO_INSERT_TERM_6001 https://fairsharing.org/search?fairsharingRegistry=Standard)  file format (URL_TO_INSERT_TERM_6002 https://fairsharing.org/search?recordType=model_and_format) 
alt: Validating FAST (URL_TO_INSERT_RECORD_6006 https://fairsharing.org/FAIRsharing.p5df9c) Q open standard (URL_TO_INSERT_TERM_6004 https://fairsharing.org/search?fairsharingRegistry=Standard)  file format (URL_TO_INSERT_TERM_6005 https://fairsharing.org/search?recordType=model_and_format) 
---
Validating FAST (URL_TO_INSERT_RECORD_6009 https://fairsharing.org/FAIRsharing.p5df9c) Q open standard (URL_TO_INSERT_TERM_6007 https://fairsharing.org/search?fairsharingRegistry=Standard)  file format (URL_TO_INSERT_TERM_6008 https://fairsharing.org/search?recordType=model_and_format) .
```
````

<!-- [![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVEQ7XG4gICAgQVtEYXRhIEFjcXVpc2l0aW9uXSAtLT5CKFJhdyBEYXRhKVxuICAgIEIgLS0-IEN7SXMgc3RhbmRhcmQgZm9ybWF0P31cbiAgICBDIC0tPnxZZXN8IER7RmlsZSBmb3JtYXQgdmFsaWQ_fVxuICAgIEMgLS0-fE5vfCBFW0NvbnZlcnQgdG8gc3RhbmRhcmQgZmlsZSBmb3JtYXRdXG4gICAgRCAtLT4gfFllc3xGWy0gRGF0YSBkZXBvc2l0aW9uIDxicj4gLSBEYXRhIHNoYXJpbmcgPGJyPiAgLSBEb3duc3RyZWFtIGFuYWx5c2lzIF1cbiAgICBEIC0tPiB8Tm98R1tSZXZpc2UgZmlsZV1cbiAgICBFIC0tPiAgRFxuICAgIEcgLS0-IHxyZXZpc2V8RCIsIm1lcm1haWQiOnsidGhlbWUiOiJuZXV0cmFsIn19)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVEQ7XG4gICAgQVtEYXRhIEFjcXVpc2l0aW9uXSAtLT5CKFJhdyBEYXRhKVxuICAgIEIgLS0-IEN7SXMgc3RhbmRhcmQgZm9ybWF0P31cbiAgICBDIC0tPnxZZXN8IER7RmlsZSBmb3JtYXQgdmFsaWQ_fVxuICAgIEMgLS0-fE5vfCBFW0NvbnZlcnQgdG8gc3RhbmRhcmQgZmlsZSBmb3JtYXRdXG4gICAgRCAtLT4gfFllc3xGWy0gRGF0YSBkZXBvc2l0aW9uIDxicj4gLSBEYXRhIHNoYXJpbmcgPGJyPiAgLSBEb3duc3RyZWFtIGFuYWx5c2lzIF1cbiAgICBEIC0tPiB8Tm98R1tSZXZpc2UgZmlsZV1cbiAgICBFIC0tPiAgRFxuICAgIEcgLS0-IHxyZXZpc2V8RCIsIm1lcm1haWQiOnsidGhlbWUiOiJuZXV0cmFsIn19) -->

## User Stories

The table below lists common file validation use cases. This recipe provides solutions with FAST (URL_TO_INSERT_RECORD_6010 https://fairsharing.org/FAIRsharing.p5df9c) Q files {footcite}`Cock2010` as an example.

|As a ..| I want to .. |So that I can ..|
|---|--|--|
|Data owner| Validate my sequencing files before depositing to public arch (URL_TO_INSERT_RECORD_6011 https://fairsharing.org/FAIRsharing.52b22c) ives| Reduce the risk of submitting invalid files or submission rejection|
|Data consumer| Validate files before running analysis|Avoid wasting time and resource processing corrupted files|
|Data consumer| Integrate file format (URL_TO_INSERT_TERM_6012 https://fairsharing.org/search?recordType=model_and_format)  validation into my data process pipeline| Build a more reproducible and error-proof pipeline| 
|Data librarian| Check files downloaded from unknown sources before deposition| Ensure the file is usable in the future.|


---

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [Format (URL_TO_INSERT_TERM_6013 https://fairsharing.org/search?recordType=model_and_format)  validation](http://edamontology.org (URL_TO_INSERT_RECORD_6015 https://fairsharing.org/FAIRsharing.a6r7zs) /operation_0336)  | [FAST (URL_TO_INSERT_RECORD_6014 https://fairsharing.org/FAIRsharing.p5df9c) Q file](http://edamontology.org (URL_TO_INSERT_RECORD_6016 https://fairsharing.org/FAIRsharing.a6r7zs) /format_2182)  | Validation results  |


## Table of Data Standards

| Data Format (URL_TO_INSERT_TERM_6018 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_6019 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_6017 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
| [FASTQ](http://edamontology.org (URL_TO_INSERT_RECORD_6020 https://fairsharing.org/FAIRsharing.a6r7zs) /format_2182)  | |
| [Compressed Format](https://www.ebi.ac.uk/ols/ontologies/edam/terms?iri=http%3A%2F%2Fedamontology.org (URL_TO_INSERT_RECORD_6021 https://fairsharing.org/FAIRsharing.a6r7zs) %2Fformat_4006)| |
---

[FASTQ](http://edamontology.org (URL_TO_INSERT_RECORD_6030 https://fairsharing.org/FAIRsharing.a6r7zs) /format_2182) is the _de facto_ sequencing file format (URL_TO_INSERT_TERM_6022 https://fairsharing.org/search?recordType=model_and_format)  and one of the most common file format (URL_TO_INSERT_TERM_6023 https://fairsharing.org/search?recordType=model_and_format) s in bioinformat (URL_TO_INSERT_TERM_6024 https://fairsharing.org/search?recordType=model_and_format) ics analysis {footcite}`ENA (URL_TO_INSERT_RECORD_6027 https://fairsharing.org/FAIRsharing.dj8nt8) fastq`, {footcite}`NCBIformat (URL_TO_INSERT_TERM_6025 https://fairsharing.org/search?recordType=model_and_format) s`. Research (URL_TO_INSERT_RECORD_6031 https://fairsharing.org/FAIRsharing.52b22c) ers receive FAST (URL_TO_INSERT_RECORD_6028 https://fairsharing.org/FAIRsharing.p5df9c) Q files from various sources. These files are used intensively in automated bioinformat (URL_TO_INSERT_TERM_6026 https://fairsharing.org/search?recordType=model_and_format) ics analysis pipelines. Therefore, it is important to validate FAST (URL_TO_INSERT_RECORD_6029 https://fairsharing.org/FAIRsharing.p5df9c) Q files to improve the data reusability and build error-proof data analysis processes.

FAST (URL_TO_INSERT_RECORD_6033 https://fairsharing.org/FAIRsharing.p5df9c) Q validators detect truncated reads, base calls and quality score (URL_TO_INSERT_RECORD_6032 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_6036 https://fairsharing.org/FAIRsharing.xMmOCL)  mismatches, invalid encoding, etc. For paired-end reads, they also check if the forward reads match with the reverse reads. Most validators can process different FAST (URL_TO_INSERT_RECORD_6034 https://fairsharing.org/FAIRsharing.p5df9c) Q variants automatically and handle (URL_TO_INSERT_RECORD_6037 https://fairsharing.org/FAIRsharing.0b7e54)  compressed FAST (URL_TO_INSERT_RECORD_6035 https://fairsharing.org/FAIRsharing.p5df9c) Q files. 

[FASTQ-utils](https://github.com (URL_TO_INSERT_RECORD_6041 https://fairsharing.org/FAIRsharing.c55d5e) /nunofonseca/fastq_utils) is an open-source software to validate and process FAST (URL_TO_INSERT_RECORD_6040 https://fairsharing.org/FAIRsharing.p5df9c) Q files. It has been applied in the [European Nucleotide Archive (URL_TO_INSERT_RECORD_6038 https://fairsharing.org/FAIRsharing.dj8nt8) (ENA)](https://www.ebi.ac.uk/ena (URL_TO_INSERT_RECORD_6039 https://fairsharing.org/FAIRsharing.dj8nt8) ), and several research (URL_TO_INSERT_RECORD_6042 https://fairsharing.org/FAIRsharing.52b22c)  initiatives. 

This recipe provides an example of validating FAST (URL_TO_INSERT_RECORD_6043 https://fairsharing.org/FAIRsharing.p5df9c) Q files with _FAST (URL_TO_INSERT_RECORD_6044 https://fairsharing.org/FAIRsharing.p5df9c) Q-utils_ on MacOS and Linux machines.

```{warning}
⚠️ Quality control is out of the scope of file format validation.
```


<!-- ![](/images/jOYK2ZM.jpg) -->


````{dropdown} 
:open:
```{figure} /images/jOYK2ZM.jpg
---
width: 800px
name: FAST (URL_TO_INSERT_RECORD_6045 https://fairsharing.org/FAIRsharing.p5df9c) Qutils library
alt: FAST (URL_TO_INSERT_RECORD_6046 https://fairsharing.org/FAIRsharing.p5df9c) Qutils library
---
the FAST (URL_TO_INSERT_RECORD_6047 https://fairsharing.org/FAIRsharing.p5df9c) Qutils library.
```
````

### Requirements

The users are expected to be comfortable with Unix-based OS and basic Bash programming syntax and commands.

|Software|Description|Version|
|--|--|--|
|[conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)|Package manager for installing validators |4.8.3
|[FASTQ-utils](https://github.com (URL_TO_INSERT_RECORD_6049 https://fairsharing.org/FAIRsharing.c55d5e) /nunofonseca/fastq_utils)| FAST (URL_TO_INSERT_RECORD_6048 https://fairsharing.org/FAIRsharing.p5df9c) Q validator|0.23.0
|[wget](https://www.gnu.org/software/wget/)|File downloader|1.19.4|

### Step 1: Install fastq-utils

The command below installs _fastq-utils_ via Conda. It is also possible to install _fastq-utils_ from [the source code](https://github.com (URL_TO_INSERT_RECORD_6050 https://fairsharing.org/FAIRsharing.c55d5e) /nunofonseca/fastq_utils) {footcite}`nuno_fonseca_2020_3936692`.

```shell
conda install -c bioconda fastq_utils
```


### Step 2: Get example file for testing*

```{admonition} Note
:class: tip
*  Users can skip this step and test with their own files._ 
```


In this step, we download example FAST (URL_TO_INSERT_RECORD_6052 https://fairsharing.org/FAIRsharing.p5df9c) Q files from ENA (URL_TO_INSERT_RECORD_6051 https://fairsharing.org/FAIRsharing.dj8nt8)  for testing. The first example file is a single read file, the other ones are paired-end read files.

__Example 1: Get single read FAST (URL_TO_INSERT_RECORD_6053 https://fairsharing.org/FAIRsharing.p5df9c) Q file__

The command below downloads an _Ion Torrent S5_ fastq file from ENA (URL_TO_INSERT_RECORD_6054 https://fairsharing.org/FAIRsharing.dj8nt8) . [This file](https://www.ebi.ac.uk/ena (URL_TO_INSERT_RECORD_6055 https://fairsharing.org/FAIRsharing.dj8nt8) /browser/view/SRR12132977) is the whole genome sequencing file of SARS (URL_TO_INSERT_RECORD_6056 https://fairsharing.org/FAIRsharing.vajn3f) -CoV-2. The complete file is 192Mb. 

```shell
wget -c ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR121/077/SRR12132977/SRR12132977.fastq.gz
```
Users can inspect the _fastq.gz_ file using `gzip -cd SRR12132977.fastq.gz | head -8`. Below is the header of this FAST (URL_TO_INSERT_RECORD_6057 https://fairsharing.org/FAIRsharing.p5df9c) Q file.
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
__Example 2: Get paired-read FAST (URL_TO_INSERT_RECORD_6058 https://fairsharing.org/FAIRsharing.p5df9c) Q files__

The command below downloads Illumina iSeq 100 paired end sequencing files from ENA (URL_TO_INSERT_RECORD_6059 https://fairsharing.org/FAIRsharing.dj8nt8) . [These files](https://www.ebi.ac.uk/ena (URL_TO_INSERT_RECORD_6060 https://fairsharing.org/FAIRsharing.dj8nt8) /data/view/SRR11542244) are raw sequence reads of a SARS (URL_TO_INSERT_RECORD_6061 https://fairsharing.org/FAIRsharing.vajn3f) -CoV-2 sample. Each file is 26 Mb.

```shell
wget -c \
ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR115/044/SRR11542244/SRR11542244_1.fastq.gz \
ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR115/044/SRR11542244/SRR11542244_2.fastq.gz
```
Below is the headers of the two files. The read pairs info is listed in the read IDs.
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
Below are the validation results. _fastq-utils_ returns the number of reads, read length details, and encoding info. Field `Quality encoding` indicates the fastq file variant. FAST (URL_TO_INSERT_RECORD_6062 https://fairsharing.org/FAIRsharing.p5df9c) Q-utils returns `OK` for a valid fastq file. Otherwise, it will return the validation details in the Error message.

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
fastq_info SRR11542244_1.fastq.gz SRR11542244_2.fastq.gz
```
Here are the validation results.
```
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
_fastq_util_ also provides additional arguments to tune the validation:

`-s`: to validate if reads in two files have the same ordering.

`-r`: to skip duplicated read names validation. It uses less memory and runs faster.

`-e`: to allow empty files pass the validation

`-q`: not to fail if the encoding can't be decided.

#### Error messages for invalid files
FAST (URL_TO_INSERT_RECORD_6063 https://fairsharing.org/FAIRsharing.p5df9c) Q-utils returns an error message with the location of invalid lines and type of errors if the files are invalid. Below are examples of error messages.

- Invalid file example 1, duplicated reads
    > ERRO (URL_TO_INSERT_RECORD_6065 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_6066 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_6067 https://fairsharing.org/FAIRsharing.cp0ybc) R (URL_TO_INSERT_RECORD_6064 https://fairsharing.org/FAIRsharing.1jKfji) : Error in file SRR11542244_2.fastq: line 16: duplicated sequence SRR11542244.5 5/

- Invalid file example 2, wrong base call encoding
    > ERRO (URL_TO_INSERT_RECORD_6069 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_6070 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_6072 https://fairsharing.org/FAIRsharing.cp0ybc) R (URL_TO_INSERT_RECORD_6068 https://fairsharing.org/FAIRsharing.1jKfji) : Error in file SRR11542244_2.fastq: line 5: invalid character 'e' (hex. code:'65'), expected AC (URL_TO_INSERT_RECORD_6071 https://fairsharing.org/FAIRsharing.md3e78) GTacgt0123nN.

### FASTA-utils feature summary

The table lists technical considerations when selecting the validator, including basic validation function, performance, interface, etc. It also provides a detailed summary of _fastq-utils_ features.  


|Aspects|Validation content |Description|FAST (URL_TO_INSERT_RECORD_6073 https://fairsharing.org/FAIRsharing.p5df9c) Q-utils|
|--|--|--|--|
|Basic validation|4-line format (URL_TO_INSERT_TERM_6074 https://fairsharing.org/search?recordType=model_and_format) |Check if the FAST (URL_TO_INSERT_RECORD_6075 https://fairsharing.org/FAIRsharing.p5df9c) Q file is a 4-line file|☑️|
| |Character encoding| Check if the base calls and quality score (URL_TO_INSERT_RECORD_6076 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_6077 https://fairsharing.org/FAIRsharing.xMmOCL)  encoding are correct.  |☑️| 
||Read length| Check if the length of the base calls are the same as that of the quality score (URL_TO_INSERT_RECORD_6078 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_6079 https://fairsharing.org/FAIRsharing.xMmOCL) s|☑️|
||File truncation|Check if the file is truncated or not|☑️|
|Paired-end reads validation| Deinterleaved paired reads| Validate when the forward and reverse reads are in two files.|☑️|
| |Interleaved _"8-line"_ files|Validate when the forward and reverse reads are listed together as an 8-line file|☑️|
|Compressed file validation| gzip| Validate compressed fastq files, with extension `fastq.gz`|☑️|
|FAST (URL_TO_INSERT_RECORD_6081 https://fairsharing.org/FAIRsharing.p5df9c) Q variants* validation| fastq-illumina|Validate the _fastq-illumina_ format (URL_TO_INSERT_TERM_6080 https://fairsharing.org/search?recordType=model_and_format) |☑️|
| |fastq-sanger|Validate the _fastq-sanger_ format (URL_TO_INSERT_TERM_6082 https://fairsharing.org/search?recordType=model_and_format) |☑️||
| |fastq-solexa|Validate the _fastq-solexa_ format (URL_TO_INSERT_TERM_6083 https://fairsharing.org/search?recordType=model_and_format) |☑️|
|Performance| Memory||`N/A`|
| |Speed| |`N/A`|
|Arch (URL_TO_INSERT_RECORD_6086 https://fairsharing.org/FAIRsharing.52b22c) ieve compatiablity|ENA (URL_TO_INSERT_RECORD_6084 https://fairsharing.org/FAIRsharing.dj8nt8) |File validated can be submitted to the ENA (URL_TO_INSERT_RECORD_6085 https://fairsharing.org/FAIRsharing.dj8nt8)  arch (URL_TO_INSERT_RECORD_6087 https://fairsharing.org/FAIRsharing.52b22c) ive.|☑️|
||ArrayExpress (URL_TO_INSERT_RECORD_6088 https://fairsharing.org/FAIRsharing.6k0kwd)  (URL_TO_INSERT_RECORD_6089 https://fairsharing.org/FAIRsharing.6k0kwd) |File validated can be submitted to Array Express.|☑️|
||SRA (URL_TO_INSERT_RECORD_6091 https://fairsharing.org/FAIRsharing.g7t2hv) |File validated can be submitted to the SRA (URL_TO_INSERT_RECORD_6092 https://fairsharing.org/FAIRsharing.g7t2hv)  arch (URL_TO_INSERT_RECORD_6090 https://fairsharing.org/FAIRsharing.52b22c) ive.|☑️|
|Interface|Command line interface|Can be used in shell and intergerated in pipe commands|☑️|
|License|Licensed||☑️[GPL-3](https://www.gnu.org/licenses/gpl-3.0.en.html)|
| |Commercial use|Can be used for commercial purpose|☑️|
|Code|Open source|Source code available on public platforms|☑️|

_*See details in the [FAST (URL_TO_INSERT_RECORD_6093 https://fairsharing.org/FAIRsharing.p5df9c) Q specification recipe]( TO (URL_TO_INSERT_RECORD_6094 https://fairsharing.org/FAIRsharing.w69t6r) DO include link)._
 
## Conclusion

In this recipe, we have shown how to validate fastq files, and proposed indicators to evaluate a FAST (URL_TO_INSERT_RECORD_6096 https://fairsharing.org/FAIRsharing.p5df9c) Q validator. We also identified common file validation related use cases and provided a general file validation workflow. This recipe can be expanded to other file format (URL_TO_INSERT_TERM_6095 https://fairsharing.org/search?recordType=model_and_format) s and other use cases.


### What to read next?

- 🐙[From proprietary format (URL_TO_INSERT_TERM_6098 https://fairsharing.org/search?recordType=model_and_format)  to open standard (URL_TO_INSERT_TERM_6097 https://fairsharing.org/search?fairsharingRegistry=Standard)  format (URL_TO_INSERT_TERM_6099 https://fairsharing.org/search?recordType=model_and_format) : an exemplar](https://github.com (URL_TO_INSERT_RECORD_6100 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/the-fair-cookbook/blob/mzml-format/docs/content/recipes/interoperability/from-proprietary-to-open-standard-mzml-exemplar.md) 
- 🐙[FAST (URL_TO_INSERT_RECORD_6101 https://fairsharing.org/FAIRsharing.p5df9c) Q file specification recipe](TO (URL_TO_INSERT_RECORD_6102 https://fairsharing.org/FAIRsharing.w69t6r) DO include link to recipe https://www.TBD.org )
- 🐙[FAST (URL_TO_INSERT_RECORD_6103 https://fairsharing.org/FAIRsharing.p5df9c) Q file validator in Biopython](TO (URL_TO_INSERT_RECORD_6104 https://fairsharing.org/FAIRsharing.w69t6r) DO include link to recipe https://www.TBD.org)

````{rdmkit_panel}
````



## References
````{dropdown} **References**
```{footbibliography}
```
````
<!-- - Cock, Peter J. A., Christopher J. Fields, Naohisa Goto, Michael L. Heuer, and Peter M. Rice. ‘The Sanger FASTQ File Format for Sequences with Quality Scores, and the Solexa/Illumina FASTQ Variants’. Nucleic Acids Research 38, no. 6 (1 April 2010): 1767-71. https://doi.org/10.1093/nar/gkp1137.
- ENA. ‘Accepted Read Data Formats — ENA Training Modules 1 Documentation’. Accessed 6 July 2020. https://ena-docs.readthedocs.io/en/latest/submit/fileprep/reads.html#fastq-format.
- NCBI. ‘File Format Guide’. Accessed 14 July 2020. https://www.ncbi.nlm.nih.gov/sra/docs/submitformats/#fastq-files.
- Nuno Fonseca, and Jonathan Manning. Nunofonseca/Fastq_utils 0.24.0. Zenodo, 2020. https://doi.org/10.5281/zenodo.3936692. -->


## Authors

````{authors_fairplus}
Fuqi: Writing - Original Draft
Eva: Writing - Review & Editing
Peter: Writing - Review & Editing
````


## License

````{license_fairplus}
CC-BY-4.0
````
