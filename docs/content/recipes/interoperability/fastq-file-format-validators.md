>:bulb: __W.I.P__

# FASTQ file validation

### FASTQ file specification 
>TODO: Point to Eva's FASTQ specification recipe

|Format|Specification|Source|Link|Note|
|--|--|--|--|--|
|FATSQ|FASTQ Sequence and Sequence Quality Format |Sanger FASTQ file format for sequences with quality scores, and the Solexa/Illumina FASTQ variants.|[Link](https://fairsharing.org/FAIRsharing.r2ts5t)|Registered in FAIRsharing|
|FASTQ|FASTA Sequence Format| For NCBI BLAST|[link](https://fairsharing.org/bsg-s000228/)| Registered in FAIRsharing|
|fastq.gz| 
|FASTQ|ENA FASTQ specification|ENA| [link](https://ena-docs.readthedocs.io/en/latest/submit/fileprep/reads.html#fastq-format)|
|FASTQ|Illumina FASTQ specification|Illumina|[link](https://support.illumina.com/bulletins/2016/04/fastq-files-explained.html)

> TODO: summarize the common specification and highlight the differences

```mermaid
graph TB  

```
### Use cases
- :heavy_plus_sign: As a data owner, I want to validate my FASTQ file to make sure it is submittable to public archives.
- :heavy_plus_sign: As a data consumer, I want to validate the FASTQ file before running analysis to avoid wasting time on corrupted files.
- :heavy_plus_sign: As a data consumer, I want to check if the FASTQ file I got from unknown source is valid before depositing the file

### Challenges in FASTQ validation
- different variants
- large size

### Common errors.

### Where to find the FASTQ validators
- bio.tools
- Archives, e.g SRA, ENA, ArrayExpress
- ? _forums, publications?_

### Avaiable fastq validators
|Valiators| Users|
|---|---|
|FASTQ utils| Used by ENA|
|samtools htsjdk library| Used by ENA+EGA| 
| LibStatGen: FASTQ| [GH](https://github.com/statgen/fastQValidator) [documentaion](https://genome.sph.umich.edu/wiki/FastQValidator)
| Fqtools | [paper](https://academic.oup.com/bioinformatics/article/32/12/1883/1744334)

### What does it validate
"The two files of a paired reads run have the same size and number of sequences.
    That each sequence in a fastq file has a corresponding quality line with the same number of characters.
    That a fastq file is correctly formatted, basically that it consists of groups of 4 lines.
    That it ends with a new line, that it isn't truncated.
"


### Example of how to use a FASTQ utils
#### online validators
#### local validators

### Considerations

> From Tony's doc
- memory requirements: "astQValidator checks for unique sequence names, it may use a large amount of memory - this can be disabled by specifying the --disableSeqI"
- ENA and EGA uses _samtools_ but with additional custom logic for checking the correct sets of files are received depending on the technology
- paired read files are now validated seperately in the recipes
- 10x sequencing we require BAM/CRAM rather than FASTQ because of the potential for missing barcodes

__Define which senario we want to cover in this recipe__ 

### How to choose
- Validation purpose: for personal use, for data submission, etc.
- Special requirement: paired ends, _.gz_ files 
- speed

```
considerations in [fqtools paper](https://academic.oup.com/bioinformatics/article/32/12/1883/1744334)

 - The ability to process the full range of valid FASTQ files;

 - The ability to detect the full range of FASTQ errors;

 - The ability to read and write compressed data; and

 - The processing speed.
```

## Authors
|Name|Institute|ORCID|Contributions|
|--|--|--|--|
|Fuqi Xu|[EMBL-EBI](https://www.ebi.ac.uk/)|[0000-0002-5923-3859](https://orcid.org/0000-0002-5923-3859)|Writing - Original Draft|
|Eva Martin | [Barcelona Supercomputing Center (BSC)](https://www.bsc.es/) |[0000-0001-8324-2897](https://orcid.org/0000-0001-8324-2897)|Writing |

## License

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
