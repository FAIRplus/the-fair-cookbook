(fcb-infra-chemid)=
# Chemical Identity - InChI and SMILES

+++
<br/>

----

````{panels}
:container: container-lg pb-3
:column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-1
:card: rounded

<i class="fa fa-qrcode fa-2x" style="color:#7e0038;"></i>
^^^
<h4><b>Recipe metadata</b></h4>
 identifier: <a href="">F1</a> 
 version: <a href="">v1.1</a>

---
<i class="fa fa-fire fa-2x" style="color:#7e0038;"></i>
^^^
<h4><b>Difficulty level</b></h4>
<i class="fa fa-fire fa-lg" style="color:#7e0038;"></i>
<i class="fa fa-fire fa-lg" style="color:#7e0038;"></i>
<i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
<i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
<i class="fa fa-fire fa-lg" style="color:lightgrey"></i>

---
<i class="fas fa-clock fa-2x" style="color:#7e0038;"></i>
^^^
<h4><b>Reading Time</b></h4>
<i class="fa fa-clock fa-lg" style="color:#7e0038;"></i> 15 minutes
<h4><b>Recipe Type</b></h4>
<i class="fa fa-laptop fa-lg" style="color:#7e0038;"></i> Hands-on
<h4><b>Executable Code</b></h4>
<i class="fa fa-play-circle fa-lg" style="color:#7e0038;"></i> Yes

---
<i class="fa fa-users fa-2x" style="color:#7e0038;"></i>
^^^
<h4><b>Intended Audience</b></h4>
<p><i class="fa fa-flask fa-lg" style="color:#7e0038;"></i> Chemoinformatician</p>
<p> <i class="fa fa-diamond fa-lg" style="color:#7e0038;"></i> Data Curator</p>
<p><i class="fa fa-database fa-lg" style="color:#7e0038;"></i> Data Manager</p>
<p><i class="fa fa-wrench fa-lg" style="color:#7e0038;"></i> Data Scientist</p>
<!-- <p><i class="fa fa-money fa-lg" style="color:#7e0038;"></i> Funder</p> -->
````

___

## Standards:

* SDF file (FairSharing doi:[10.25504/fairsharing.ew26v7](https://doi.org/10.25504/fairsharing.ew26v7))
* SMILES (FairSharing doi:[10.25504/fairsharing.qv4b3c](https://doi.org/10.25504/fairsharing.qv4b3c))
* InChI (FairSharing doi:[10.25504/fairsharing.ddk9t9](https://doi.org/10.25504/fairsharing.ddk9t9))

## Databases:

* PubChem (FairSharing doi:[10.25504/fairsharing.qt3w7z](https://doi.org/10.25504/fairsharing.qt3w7z))
* ChemSpider (FairSharing doi:[10.25504/fairsharing.96f3gm](https://doi.org/10.25504/fairsharing.96f3gm))
* Wikidata (FairSharing doi:[10.25504/fairsharing.6s749p](https://doi.org/10.25504/fairsharing.6s749p))

## Identifiers:

* International Chemical Identifier (InChI)

## Tools:

* Programming Language: Groovy
* Dependencies: CDK 2.3
* FAIRPlus SDF tools

### Requirements

To run the below scripts, you need a [Groovy](https://groovy.apache.org/download.html) installation.
The Groovy scripts use version 2.3 of the [Chemistry Development Kit](https://cdk.github.io/)
(see also doi:[10.1186/s13321-017-0220-4](https://doi.org/10.1186/s13321-017-0220-4)).
This library and its use in Groovy is further explain in
the book [Groovy Cheminformatics with the Chemistry Development Kit](https://egonw.github.io/cdkbook/).


Click here for more detailed use instructions and where to find the tools:
[https://github.com/FAIRplus/fairplus-sdf](https://github.com/FAIRplus/fairplus-sdf)

### Record validation

When generating InChIs, the InChI library may return two success states reflecting issues with
the compound record in the SDF file: WARNING and ERROR. This first script reports such issues:

```bash
groovy badRecords.groovy -f foo.sdf
```

* Input: SDF file
* Output: Reports validation issues


### Calculate InChls

Similarly, InChIKeys can be generated:

```bash
groovy inchikeys.groovy -f foo.sdf
```

* Input: SDF file
* Output: list of InChIs

When the success state is ERROR, nothing is outputted.

### Calculate SMILES strings

The last script calculates a SMILES for each entry in the SDF file:

```bash
groovy smiles.groovy -f foo.sdf
```

* Input: SD file
* Output: list of SMILES strings



## Authors:

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Egon Willighagen|  [Maastricht University, Department of Bioinformatics - BIGCaT, NUTRIM School of Nutrition and Translational Research in Metabolism Faculty of Health, Medicine and Life Sciences](https://www.maastrichtuniversity.nl/egon.willighagen)| [0000-0001-7542-0286](http://orcid.org/0000-0001-7542-0286) | Writing - Original Draft |
|  |   | | Reviewer | 

___

## License:

This page is released under the Creative Commons 4.0 BY license.

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png" height="20"/></a>


