>:bulb: __W.I.P__

# FASTQ file validation

### FASTQ file specification 
|Format|Specification|Source|Link|Note|
|--|--|--|--|--|
|FATSQ|FASTQ Sequence and Sequence Quality Format |Sanger FASTQ file format for sequences with quality scores, and the Solexa/Illumina FASTQ variants.|[Link](https://fairsharing.org/FAIRsharing.r2ts5t)|Registered in FAIRsharing|
|FASTQ|FASTA Sequence Format| For NCBI BLAST|[link](https://fairsharing.org/bsg-s000228/)| Registered in FAIRsharing|
|fastq.gz| 
|FASTQ|ENA FASTQ sepecification|ENA| [link](https://ena-docs.readthedocs.io/en/latest/submit/fileprep/reads.html#fastq-format)|
### When to validate a file
- Downloading file from "not trusted" source
- Before carrying out time consuming tasks
- Before submitting data to public archives

### Where to find the FASTQ validators

### Avaiable fastq validators
|Valiators| Users|
|---|---|
|FASTQ utils| Used by ENA|
|samtools htsjdk library| Used by ENA+EGA| 

### Example of how to use a FASTQ utils

### Considerations
> From Tony's doc

- ENA and EGA uses _samtools_ but with additional custom logic for checking the correct sets of files are received depending on the technology
- paired read files are now validated seperately in the recipes
- 10x sequencing we require BAM/CRAM rather than FASTQ because of the potential for missing barcodes

__Define which senario we want to cover in this recipe__ 

### How to choose
- Validation purpose: for personal use, for data submission, etc.
- Special requirement: paired ends, _.gz_ files 
- speed
- 

