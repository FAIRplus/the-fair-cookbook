(fcb-interop-phenopacket)=
# How to standardizing and exchanging patient and sample phenotypic data


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
 identifier: <a href="">RX.X</a> 
 version: <a href="">v0.1</a>

---
<i class="fa fa-fire fa-2x" style="color:#7e0038;"></i>
^^^
<h4><b>Difficulty level</b></h4>
<i class="fa fa-fire fa-lg" style="color:#7e0038;"></i>
<i class="fa fa-fire fa-lg" style="color:#7e0038;"></i>
<i class="fa fa-fire fa-lg" style="color:l#7e0038;"></i>
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
<i class="fa fa-play-circle fa-lg" style="color:#7e0038;"></i> No

---
<i class="fa fa-users fa-2x" style="color:#7e0038;"></i>
^^^
<h4><b>Intended Audience</b></h4>
<!-- <p> <i class="fa fa-user-md fa-lg" style="color:#7e0038;"></i> Principal Investigator </p> -->
<p> <i class="fa fa-database fa-lg" style="color:#7e0038;"></i> Data Manager </p>
<p> <i class="fa fa-wrench fa-lg" style="color:#7e0038;"></i> Data Scientist </p>
````

___



<!-- # Table of Contents
1. [An introduction of the phenopacket schema](#An%20introduction%20of%20the%20phenopacket%20schema)
2. [An example of phenotypic data represented in phenopacket](#An%20example%20of%20phenotypic%20data%20represented%20in%20phenopacket)
3. [Existing tools and ETLs for know formats](#Existing%20tools%20and%20ETLs%20for%20know%20formats)
4. [A demo case of adopting phenopacket at BioSamples](#A%20demo%20case%20of%20adopting%20phenopacket%20at%20BioSamples) -->

## Main FAIRification Objectives

Scope: Submitting and exchange different type of molecular data (e.g. OMICS) data requires the submission of the phenotypic data of the associated patients and samples. 
The phenopackets schema is a community accpeted open standard (approved by the GA4GH Steering Committee) for sharing disease and phenotype information to improve the understand, diagnose, and treat both rare and common diseases. 

Prepare the phenotypic data using the phenopackets schema will greatly help in improving the **interoperability** of a dataset. It is also becoming mandatory for the submission to public data repositories.

The main purpose of this recipe is:

> - Provide a basic introduction of the phenopacket specification.
> - Give an example of how to transform phenotypic data using the phenopackets schema.
> - Provide links to existing tools and ETLs from established formats.
> - A demo case of adopting phenopacket at BioSamples
___

## User Stories

Submit your genomics sequencing data to the European Genome-Phenome Archive (EGA).

---

## Graphical overview


```{figure} phenopacket-overview.png
---
width: 450px
name: Phenopacket Overview
alt: Phenopacket Overview
---
Phenopacket Overview
```


```mermaid
graph LR
  A(project):::box -->|data collection| B(Data Management Plan):::box

  B -->|refers to| C(Data Dictionary):::box
  B -->|identifies| F(fa:fa-car Metadata Models):::box5
  B -->|lists| E(Data Collection <br> Formulaires):::box5

  C --> |declares| D(variable):::box

  D --> |defined by| G(variable data type <br> e.g. string,integer,float):::box
  D --> |defined by| H(variable statistical type <br> one of continuous,categorical or ordinal variable):::box
  D --> |defined by| I(variable semantic type <br> e.g. associated a class from an ontology <br>or controlled vocabulary):::box
  D --> |defined by| J(variable values range for continuous variables):::box
  D --> |defined by| K(variable values sets for categorical variables):::box
  D --> |defined by| L(allowed values to indicate missing values <br> e.g. `NaN`,`None`,``):::box
  D --> |defined by| LL(regular expression for input validation):::box
  D --> |defined by| LLL(computation formula if specifying a derived variable):::box
  D --> |defined by| L4(variable domain grouping, e.g. clinical chemistry variable):::box
  D --> |used in| E
  L4 --> |refers to| E
  C --> |states| M(license):::box1
  C --> |states| N(terms of use):::box1
  C --> |authored_by| O(authors):::box1
  C --> |documented in open format| P(format):::box1

linkStyle 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17 stroke:#2a9fc9,stroke-width:1px,color:#2a9fc9,font-family:avenir;
classDef box font-family:avenir,font-size:14px,fill:#2a9fc9,stroke:#222,color:#fff,stroke-width:1px
classDef box1 font-family:avenir,font-size:14px,fill:purple,stroke:#222,color:#fff,stroke-width:1px
classDef box5 font-family:avenir,font-size:14px,fill:#FF3371,stroke:#222,color:#fff,stroke-width:1px
```

---

## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Interoperability | minimal | repeatable |

----

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks | Input | Output  |
| :------------- | :------------- | :------------- |
| [text annotation](http://edamontology.org/operation_3778) | list of Variables | Machine-acionable list of annotated Variables |

## An introduction of the phenopacket schema

TO BE MODIFIED: "The Phenopacket Schema represents an open standard for sharing disease and phenotype information to improve our ability to understand, diagnose, and treat both rare and common diseases..."

## An example of phenotypic data represented in phenopacket

Example here.


## Existing tools and ETLs for know formats

The link

## A demo case of adopting phenopacket at BioSamples

BioSamples 


---
## Conclusion

This recipe covered an essential part of standardizing and exchangign patient and sample phenotype using the phenopacket schema...

## What to read next:

> - [Phenopacket Documentation](https://phenopackets-schema.readthedocs.io/en/latest/)
> - [The Human Phenotype Ontology (HPO)](https://hpo.jax.org/app/)

___
## Authors

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Danielle Welter |  LCSB, University of Luxembourg| [0000-0003-1058-2668](https://orcid.org/0000-0003-1058-2668) | Writing - Original Draft |
| Philippe Rocca-Serra |  University of Oxford, Data Readiness Group| [0000-0001-9853-5668](https://orcid.org/orcid.org/0000-0001-9853-5668) | Writing - Original Draft |
| Wei Gu |  LCSB, University of Luxembourg| [0000-0003-3951-6680](https://orcid.org/0000-0003-3951-6680) | Writing - Original Draft |
| Mélanie Courtot | EMBL-EBI| [0000-0002-9551-6370](https://orcid.org/orcid.org/0000-0002-9551-6370) | Writing - Original Draft |
___


## License

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
