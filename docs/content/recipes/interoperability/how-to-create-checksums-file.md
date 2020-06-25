
# Table of Contents
0. [Abstract](#Abstract)
1. [Graphical Overview](#Graphical%20Overview)
2. [Requirements](#Requirements)
3. [Recipe instructions](#Recipe%20instructions)
4. [Possible improvements from the state of this recipe](#Possible%20improvements%20from%20the%20state%20of%20this%20recipe)
5. [Further reading](#Further%20reading)
6. [Capability & Maturity Table](#Capability%20&%20Maturity%20Table)
7. [FAIRification Objectives, Inputs and Outputs](#FAIRification Objectives, Inputs and Outputs)
5. [Table of Data Standards](#Table%20of%20Data%20Standards)
6. [Authors](#Authors)
8. [License](#License)

---

## Abstract

When copying a file ("source file") to a target location, it may become necessary
to confirm that the actual content, i.e. the bits that make up the information, arrived correctly in the target system.
Confirming the identity of two different files may be achieved by calculating
a so-called "checksum" of the file
in the source system, calculating the checksum in the target system, and comparing
the outputs. The checksum is a proxy of the content of the file, but is much shorter.
Because the algorithm is previously agreed on and shared between the source and target system,
the comparison of the checksum indicates whether the files are identical (within some limitations).


___


## Graphical Overview

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbkF7UmVxdWlyZW1lbnRzIGZ1bGZpbGxlZD99IC0tPnxZZXN8IEJbQXBwbHkgdGhpcyByZWNpcGVdXG5BIC0tPnxOb3wgRChTVE9QKVxuQiAtLT4gQyhGQVNUUSBmaWxlIHZhbGlkYXRpb24gb3V0cHV0KVxuIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbkF7UmVxdWlyZW1lbnRzIGZ1bGZpbGxlZD99IC0tPnxZZXN8IEJbQXBwbHkgdGhpcyByZWNpcGVdXG5BIC0tPnxOb3wgRChTVE9QKVxuQiAtLT4gQyhGQVNUUSBmaWxlIHZhbGlkYXRpb24gb3V0cHV0KVxuIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)

<div class="mermaid">
graph TD
S(START) --> A
A{Requirements fulfilled?} -->|Yes| B[Apply this recipe]
A -->|No| D(STOP)
B --> C(Calculate the checksums in source and target system)
C --> D{Checksums identical?}
D -->|Yes| E(Identity confirmed)
D -->|No| F(Identity could not be confirmed)
</div>

---

## Requirements:

This recipe assumes the following:

  - both source and target systems have the Linux operating system, preferentially Debian (no root access needed)
  - you have basic knowledge of how to use a terminal (called "shell", this can be bash or similar)
  - the tool `md5sum` is installed
  - the source and target files are both placed in your home directory; we assume they are called `file_to_compare.txt` (replace this filename as necessary in the recipe instructions; you can download a demo file from here: ##TODO


Checking the requirements (tests):

  - Start up a console. Type `md5sum -v` and hit return. You should see `TODO` as output.

___

## Recipe instructions

### Generating the checksums

On the shell execute:

`md5sum file_to_compare.txt`

The output should be:

```

```


### Limitations of this recipe

This recipe in its current form has the following limitations:

  - with the tool above, the nucleotide alphabet is checked by default only on whether it conforms to a "SingleLetterAlphabet", but this allows even insensible characters such as `ä` as nucleotide letters.
  - the error messages are not indicating at which position exactly an error occured, i.e. which letter of the quality score is incorrect (the error message is e.g. `ValueError: Invalid character in quality string` where it might be preferable to get an error message like `ValueError: Invalid character "ö" in quality string of read 12 at position 5.`)
  - the read names are not further checked and might not fulfill specific requirements of the subsequent tool, for which this check was supposed to be designed.


### Extendability of this recipe

- The tool above can also be used to check selectively for other variants of the PHRED score encoding, i.e. `fastq-illumina` or `fastq-solexa`. See <https://biopython.org/wiki/SeqIO> for a list of supported file formats.
- This recipe can also be applied to check general sequences without quality scores, e.g. files in FASTA format.


## Possible improvements from the state of this recipe

- It would be preferable to introduce a further, harder check for the specification of the nucleotide sequence, e.g. only allowing the the "IUPAC DNA alphabet" (see <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC322779>), including degenerate bases (e.g. `B` representing the bases (`A` OR `G` OR `T`), lowercase and uppercase mixtures (e.g. `acGTgTGaa`), and gaps (symbolized by `.`).
- It might be possible to extend the tool above into the desired direction of more consistent checks, considering the content of <https://biopython.org/wiki/SeqIO_dev>.
- It would be preferable to be able to exchange the concrete FASTQ specification that was used to derive the validation result with other tools and/or make them visible.
- It would be preferable to document the result of the file format validation in a machine-readable and consistent way.


## Further reading

- The documentation of BioPython, and specifically Bio.SeqIO: <https://biopython.org/docs/1.77/api/Bio.SeqIO.QualityIO.html>


## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Interoperability | minimal | repeatable |

----

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [Format Validation](http://edamontology.org/operation_0336)  | [FASTQ file](https://fairsharing.org/FAIRsharing.r2ts5t)  | [report](http://edamontology.org/data_2048)  |

---

## Table of Data Standards

| Data Formats  |
| :------------- |
| [FASTQ](https://fairsharing.org/FAIRsharing.r2ts5t)  |

---


## Authors:

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Robert T. Giessmann |  Bayer AG | [0000-0002-0254-1500](https://http://orcid.org/0000-0002-0254-1500) | Writing - Original Draft |

---


## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
