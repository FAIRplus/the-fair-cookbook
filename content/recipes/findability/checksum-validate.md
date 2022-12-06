(fcb-checksum-validate)=
# How to check file integrity by validating checksums


````{panels_fairplus}
:identifier_text: FCB053 
:identifier_link: 'https://w3id.org/faircookbook/FCB053'
:difficulty_level: 4
:recipe_type: hands_on
:reading_time_minutes: 15
:intended_audience: bioinformatician, data_scientist, data_engineer
:maturity_level: 0
:maturity_indicator: 0
:has_executable_code: nope
:recipe_name: Validating checksums to verify file integrity
```` 

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


---

## Graphical Overview

````{dropdown} 
:open:
```{figure} checksum-validate.md-figure1.mmd.png
---
width: 450px
name: checksum-validate-figure1
alt: Graphical overview of the steps taken by this recipe.
---
Graphical overview of the steps taken by this recipe.
```
````


---

## Requirements:

This recipe assumes the following:

  - both source and target systems have the Linux operating system, preferentially Debian (no root access needed)
  - you have basic knowledge of how to use a terminal (called "shell", this can be bash or similar)
  - the tool `md5sum` is installed
  - the source and target files are both placed in your home directory; we assume they are called `file_to_compare.txt` (replace this filename as necessary in the recipe instructions; you can download a demo file from here: {download}`./checksum-create.md-file_to_compare.txt` (remember to rename it to `file_to_compare.txt`)
  - for the more complex example (compare many files): the source and target files are both placed in a directory called `path_to_directory` within your home directory; we assume that this directory contains many image files with arbitrary names, but the common file extension ´.jpg´.
  - the list of checksums is available and was generated according to the recipe {ref}`fcb-checksum-create`


Checking the requirements (tests):


  - Start up a console. Type 
    ```
    md5sum --version
    ``` 
    and hit return.
      - You should see as output: 
        ```text
        md5sum (GNU coreutils) 8.30
        Copyright (C) 2018 Free Software Foundation, Inc.
        License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
        This is free software: you are free to change and redistribute it.
        There is NO WARRANTY, to the extent permitted by law.

        Written by Ulrich Drepper, Scott Miller, and David Madore.
        ```
  - Execute on the console: 
    ```
    ls ~/file_to_compare.txt
    ```
    - The output should be something like: 
      ```
      /home/USERNAME/file_to_compare.txt
      ```
      where `USERNAME` is your username on the computer system. The output should NOT be something like:
      ```
      ls: cannot access '/home/USERNAME/file_to_compare.txt2': No such file or directory
      ```
  - Execute on the console:
    ```
    ls -1 ~/path_to_directory/*.jpg
    ```
    - You should see a list of all image files. The output should NOT be something like:
      ```
      ls: cannot access '/home/USERNAME/path_to_directory/*.jpg': No such file or directory
      ```
  - Execute on the console:
    ```
    ls -1 ~/checksums.md5
    ```
    - You should see 
      ```
      /home/USERNAME/checksums.md5
      ```
      and NOT something like: 
      ```
      ls: cannot access '/home/USERNAME/checksums.md5': No such file or directory
      ```
  - Execute 
    ```
    wc  ~/checksums.md5
    ``` 
    and 
    ```
    ls -1 ~/path_to_directory/*.jpg | wc
    ```
      - The first number of each output should match. This indicates that the number of checksums in the checksum file (which is the output of the first command) is equivalent to the number of jpg files in the `path_to_directory` directory.


---

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

  - the above assumes that everything is placed in your home folder. (for a resolution see section "Extendability of this recipe" below.)
  - the above assumes that you don't have a problem with calculating the checksums sequentially. Depending on your system's resources (especially available CPU time), this calculation of checksums might take a while, however. A common benchmark on a typical laptop is: 0.01 seconds per MB of data.
  - you should mind the general limitations of checksums, which are however not covered in this recipe.
  - there is a known clash between the output format of the GNU / Linux tool `md5sum` and the macOS / BSD tool `md5`. Their standard output formats are incompatible; combining a macOS-based system with a Linux-based system, either one as source or target, is therefore not straightforward. (hint: the Linux tool has the `--tag` flag which generates macOS-compatible output.) 
  - Windows users may use the included PowerShell function "Get-FileHash"
  - the recipe assumes that the absolute paths of the files are the same on source as well as on target system. If necessary for the use case, the "relative mode" by executing e.g. `md5sum ./*` can be used to circumvent problems with absolute paths.
  - `md5` is the most common hashing algorithm, but is also known to have vulnerabilities for checksum hacking (see <https://en.wikipedia.org/wiki/MD5#Security>), and has obviously also higher collision frequencies than functions which generate longer hashes, e.g. `sha512`.


### Extendability of this recipe

- The tool above could be used to calculate checksums in parallel if typical scheduling systems and multiple worker nodes are available sharing the same file system (equivalently, this would be possible in a cloud architecture). However, additional steps would be needed to align the generated checksums to each other (questions: how would they be stored; how would they be brought together in one file to enable effective transport of the file containing the checksum entries).
- the recipe assumes that everything is placed in your home folder. If this is not the case, replace `~`, the home directory indicator, by the corresponding path, or execute specifically all `md5sum` commands only with relative pathes (by navigating in the corresponding directory, first). The command will be something like `md5sum ./YOUR_PATH_HERE/*.jpg`, then, and will output something like `c691b3d2fc2678839a9c141b6ee1524e  ./YOUR_PATH_HERE/picture1.jpg` then.
- The procedure above could be combined with a file length indicator (usually the amount of octets = bytes); the file length is usually retrieved much faster than the checksum, and might already indicate the inequality of two files (albeit similar file length does not guarantee content-identity, of course).


## Further reading

- Wikipedia article on checksums: <https://en.wikipedia.org/wiki/Checksum>
- Wikipedia article on the tool `md5sum`: <https://en.wikipedia.org/wiki/Md5sum>
- Overview of checksum comparison with respect to file transmission: https://en.wikipedia.org/wiki/File:CPT-Hashing-File-Transmission.svg

````{rdmkit_panel}
````

---

## Authors

````{authors_fairplus}
Robert: Writing - Original Draft
````


---

## License

````{license_fairplus}
CC-BY-4.0
````
