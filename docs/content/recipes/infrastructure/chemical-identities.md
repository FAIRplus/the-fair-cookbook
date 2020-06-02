# Chemical Identity - Generating InChi Keys and SMILES strings:

**identifier:** [RX.X](RX.X)

**version:** [v0.1](v0.1)
___

**_Difficulty level:_**  :triangular_flag_on_post: :white_circle: :white_circle: :white_circle: :white_circle:

**_Reading time:_** 15 minutes

**_Intended Audience:_** 

> :heavy_check_mark: *Data Scientist*

> :heavy_check_mark: *Chemoinformatician*

> :heavy_check_mark: *Metabolome Analyst*

> :heavy_check_mark: *Data Curator*


**_Recipe Type_**: Hands-on practical

**_Executable code_**: Yes

___

[TOC]

___

## Standards:

* SDFile (FairSharing doi:[10.25504/fairsharing.ew26v7](https://doi.org/10.25504/fairsharing.ew26v7))
* SMILES (FairSharing doi:[10.25504/fairsharing.qv4b3c](https://doi.org/10.25504/fairsharing.qv4b3c))
* InChI (FairSharing doi:[10.25504/fairsharing.ddk9t9](https://doi.org/10.25504/fairsharing.ddk9t9))

## Databases:

Not applicable.

## Identifiers:

* InChI

## Tools:

* Programming Language: Groovy
* Dependencies: CDK 2.3
# FAIRPlus SDF tools

### Requirements

To run the below scripts, you need a [Groovy](https://groovy.apache.org/download.html) installation.
The Groovy scripts use version 2.3 of the [Chemistry Development Kit](https://cdk.github.io/)
(see also doi:[10.1186/s13321-017-0220-4](https://doi.org/10.1186/s13321-017-0220-4)).
This library and its use in Groovy is further explain in
the book [Groovy Cheminformatics with the Chemistry Development Kit](https://egonw.github.io/cdkbook/).


[Click here on how to use:](https://github.com/FAIRplus/fairplus-sdf)

### Record validation

When generating InChIs, the InChI library may return two success states reflecting issues with
the compound record in the SD file: WARNING and ERROR. This first script reports such issues:

```bash
groovy badRecords.groovy -f foo.sdf
```

* Input: SD file
* Output: Reports validation issues


### Calculate InChls

Similarly, InChIKeys can be generated:

```bash
groovy inchikeys.groovy -f foo.sdf
```

* Input: SD file
* Output: list of InChIs

When the success state is ERROR, nothing is outputted.

### Calculate SMILES strings

The last script calculates a SMILES for each entry in the SD file:

```bash
groovy smiles.groovy -f foo.sdf
```

* Input: SD file
* Output: list of SMILES strings



## Authors:

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Egon Willighagen|  [Maastricht University,Department of Bioinformatics NUTRIM School of Nutrition and Translational Research in Metabolism Faculty of Health, Medicine and Life Sciences](https://www.maastrichtuniversity.nl/egon.willighagen)| [0000-0001-7542-0286](http://orcid.org/0000-0001-7542-0286) | Writing - Original Draft |
|  |   | | Reviewer | 

___


## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>


