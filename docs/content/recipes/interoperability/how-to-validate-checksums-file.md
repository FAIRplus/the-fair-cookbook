
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
This recipe describes how to validate a list of checksums against the corresponding files,
focusing exclusively on the output of the Linux tool `md5sum`.


___


## Graphical Overview

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcblN0YXJ0KFNUQVJUKSAtLT4gQVxuQXtSZXF1aXJlbWVudHMgZnVsZmlsbGVkP30gLS0-fFllc3wgQltBcHBseSB0aGlzIHJlY2lwZV1cbkEgLS0-fE5vfCBTdG9wKFNUT1ApXG5CIC0tPiBDKFRyYW5zZmVyIHRoZSBjaGVja3N1bSBmaWxlIGZyb20gc291cmNlIHRvIHRhcmdldCBzeXN0ZW0pXG5DIC0tPiBDMihDb21wYXJlIHRoZSBjaGVja3N1bXMgZnJvbSBjaGVja3N1bSBmaWxlIHdpdGggY2hlY2tzdW1zIGNhbGN1bGF0ZWQgb24gdGhlIHRhcmdldCBzeXN0ZW0pXG5DMiAtLT4gRHtDaGVja3N1bXMgaWRlbnRpY2FsP31cbkQgLS0-fFllc3wgRShJZGVudGl0eSBjb25maXJtZWQpXG5EIC0tPnxOb3wgRihJZGVudGl0eSBjb3VsZCBub3QgYmUgY29uZmlybWVkKSIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcblN0YXJ0KFNUQVJUKSAtLT4gQVxuQXtSZXF1aXJlbWVudHMgZnVsZmlsbGVkP30gLS0-fFllc3wgQltBcHBseSB0aGlzIHJlY2lwZV1cbkEgLS0-fE5vfCBTdG9wKFNUT1ApXG5CIC0tPiBDKFRyYW5zZmVyIHRoZSBjaGVja3N1bSBmaWxlIGZyb20gc291cmNlIHRvIHRhcmdldCBzeXN0ZW0pXG5DIC0tPiBDMihDb21wYXJlIHRoZSBjaGVja3N1bXMgZnJvbSBjaGVja3N1bSBmaWxlIHdpdGggY2hlY2tzdW1zIGNhbGN1bGF0ZWQgb24gdGhlIHRhcmdldCBzeXN0ZW0pXG5DMiAtLT4gRHtDaGVja3N1bXMgaWRlbnRpY2FsP31cbkQgLS0-fFllc3wgRShJZGVudGl0eSBjb25maXJtZWQpXG5EIC0tPnxOb3wgRihJZGVudGl0eSBjb3VsZCBub3QgYmUgY29uZmlybWVkKSIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

<div class="mermaid">
graph TD
Start(START) --> A
A{Requirements fulfilled?} -->|Yes| B[Apply this recipe]
A -->|No| Stop(STOP)
B --> C(Transfer the checksum file from source to target system)
C --> C2(Compare the checksums from checksum file with checksums calculated on the target system)
C2 --> D{Checksums identical?}
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
  - for the more complex example (compare many files): the source and target files are both placed in a directory called `path_to_directory` within your home directory; we assume that this directory contains many image files with arbitrary names, but the common file extension ´.jpg´.
  - the list of checksums is available and was generated according to the recipe [./how-to-create-checksums-file.md]


Checking the requirements (tests):


  - Start up a console. Type `md5sum --version` and hit return. You should see as output: ````
md5sum (GNU coreutils) 8.30
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Ulrich Drepper, Scott Miller, and David Madore.```.
  - Execute on the console `ls ~/file_to_compare.txt`. The output should be something like `/home/USERNAME/file_to_compare.txt`, where `USERNAME` is your username on the computer system. The output should NOT be something like `ls: cannot access '/home/USERNAME/file_to_compare.txt2': No such file or directory`.
  - Execute on the console `ls -1 ~/path_to_directory/*.jpg`. You should see a list of all image files. The output should NOT be something like `ls: cannot access '/home/USERNAME/path_to_directory/*.jpg': No such file or directory`.
  - Execute on the console `ls -1 ~/checksums.md5`. You should see `/home/USERNAME/checksums.md5`, and NOT something like `ls: cannot access '/home/USERNAME/checksums.md5': No such file or directory`.
  - Execute `wc  ~/checksums.md5` and `ls -1 ~/path_to_directory/*.jpg | wc`. The first number of each output should match. This indicates that the number of checksums in the checksum file (which is the output of the first command) is equivalent to the number of jpg files in the `path_to_directory` directory.)


___

## Recipe instructions

### Validating the checksums directly

On the shell execute:

`md5sum -c ~/checksums.md5`

The output should be something like:

```
/home/USERNAME/path_to_directory/picture1.jpg: OK
/home/USERNAME/path_to_directory/picture2.jpg: OK
/home/USERNAME/path_to_directory/picture3.jpg: OK
...
```

This step will take as long as it needs to calculate the checksums of all files on the target system. As a benchmark you can expect 0.01 seconds per MB of data.


### Limitations of this recipe

This recipe in its current form has the following limitations:

  - the above assumes that everything is placed in your home folder. If this is not the case, replace `~`, the home directory indicator, by the corresponding path, or execute specifically all `md5sum` commands only with relative pathes (by navigating in the corresponding directory, first).
  - the above assumes that you don't have a problem with calculating the checksums sequentially. Depending on your system's resources (especially available CPU time), this calculation of checksums might take a while, however. A common benchmark on a typical laptop is: 0.01 seconds per MB of data.
  - you should mind the general limitations of checksums, which are however not covered in this recipe.
  - there is a known clash between the output format of the GNU / Linux tool `md5sum` and the macOS / BSD tool `md5`. Their standard output formats are incompatible; combining a macOS-based system with a Linux-based system, either one as source or target, is therefore not straightforward. (hint: the Linux tool has the `--tag` flag which generates macOS-compatible output.) 


### Extendability of this recipe

- The tool above could be used to calculate checksums in parallel if typical scheduling systems and multiple worker nodes are available sharing the same file system (equivalently, this would be possible in a cloud architecture). However, additional steps would be needed to align the generated checksums to each other (questions: how would they be stored; how would they be brought together in one file to enable effective transport of the file containing the checksum entries).
- The procedure above could be combined with a file length indicator (usually the amount of octets = bytes); the file length is usually retrieved much faster than the checksum, and might already indicate the inequality of two files (albeit similar file length does not guarantee content-identity, of course).


## Possible improvements from the current state of this recipe

- `md5` is the most common hashing algorithm, but is also known to have vulnerabilities for checksum hacking (see <https://en.wikipedia.org/wiki/MD5#Security>), and has obviously also higher collision frequencies than functions which generate longer hashes, e.g. `sha512`.
- `md5` and checksum concepts are neither part of EDAM ontology nor of FAIRsharing.org. It would greatly benefit the community if these terminologies were introduced.


## Further reading

- Wikipedia article on checksums: <https://en.wikipedia.org/wiki/Checksum>
- Wikipedia article on the tool `md5sum`: <https://en.wikipedia.org/wiki/Md5sum>
- Overview of checksum comparison with respect to file transmission: https://en.wikipedia.org/wiki/File:CPT-Hashing-File-Transmission.svg

## Capability & Maturity Table

TODO

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Interoperability | minimal | repeatable |

----

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |

COMMENT: the concepts in this recipe did not map to any terms from the EDAM ontology.

---

## Table of Data Standards

| Data Formats  |
| :------------- |

COMMENT: the concepts in this recipe did not map to any terms from the FAIRsharing.org database.


---

## Authors:

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Robert T. Giessmann |  Bayer AG | [0000-0002-0254-1500](https://http://orcid.org/0000-0002-0254-1500) | Writing - Original Draft |

---


## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
