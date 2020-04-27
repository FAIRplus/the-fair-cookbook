# Building a Dataset Catalogue

## Main Objectives

The main purpose of this recipe is:

> To detail the key elements for the creation of a `data catalogue` to enable data `findability` in an organisation.
> We will cover the following points:
1. metadata model selection
2. annotation with controled vocabularies
3. ETL
4. data loading
5. data indexing
6. facet oriented searching
7. minting of stable, persistent and resolvable identifiers

___

# Table of Contents
1. [Main FAIRification Objectives](#Main%20FAIRification%20Objectives)
2. [Graphical Overview of the FAIRification Recipe Objectives](#Graphical%20Overview%20of%20the%20FAIRification%20Recipe%20Objectives)
3. [FAIRification Objectives, Inputs and Outputs](#FAIRification%20Objectives,%20Inputs%20and%20Outputs)
4. [Capability & Maturity Table](#Capability%20&%20Maturity%20Table)
5. [Table of Data Standards](#Table%20of%20Data%20Standards)
6. [Executable Code in Notebook](#Executable%20Code%20in%20Notebook)
7. [How to create workflow figures](#How%20to%20create%20workflow%20figures)
8. [License](#License)

---



## Graphical Overview of the FAIRification Recipe Objectives

TODO

___

## Capability & Maturity Table 

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Findability | minimal | repeatable |
| Interoperability | minimal | repeatable |

----

## User Story
For **`role.Data Scientists`**, it is essential to be able to *`action.identify`* and *`action.discover`* datasets of potential relevance in the context of *`action.data integration`* and *`action.meta-analytical work`*.

For **`role.Database Managers`**, a lightweight solution is needed to support a shallow indexing supported fast ingest without intense curation, but good potential for data discovery. Works should rely on approved data standards.

For **`role.lab scientists`**, the key is to have a minimal burden when having to *`action.deposit`* a dataset to an institutional archive or simply *`action.register`* to dataset to the `data catalogue`. 


----
## Main body of the recipe

### What is a Data Catalogue?

A `Data Catalogue` is a resource meant to allow fast identification of `Data set`. In keeping with the familiar notion of catalogue, (be it that of an exhibition or that of brand products), the notion of `data catalogue` needs to be understood as the compendium of `short descriptive metadata elements` about an actual set of data. The `Data Index or Data Catalogue` **does not** store the datasets themselves but provides information about where the datasets can be obtained from. Therefore, `Data Catalogues` are often used to index the content of '`Data Repositories` and ` Data Archives`, which provide hosting solutions for the actual datasets, which are often organized (but not always)' around specific `data types` or `data production modalities` (e.g. NMR Imaging, Confocal microscopy imaging, Nucleic Acid sequence archives and so on.)
 

### What are the standards supporting establishing a data catalogue?

`Data Catalogues` have been identified as critical infrastructure and therefore a number of model exist to support their implementation.
1. DATS:
The [Data Article Tag Suite model]() has been developed during the NIH-BD2K projects and underpins the [datamed catalogue](https://datamed.org/), the aim of which was to produce a prototype of a [`Pubmed for Datasets`](https://pubmed.ncbi.nlm.nih.gov/29346583/).

3. DCAT:
In the world of semantic web technologies, The [W3C DCAT specifications]() (v1 and the newly released version 2) provide a vocabulary to express `data catalogue metadata` in **RDF**.
3. Schema.org:
The vocabulary developed by the consortium of search engines has defined a metadata profile for [`Dataset`](https://schema.org/DataSet), [`Data Catalogue`](https://schema.org/DataCatalog)


### How are Data Catalogue populated?

A number data Indexes/Data Catalogue are populated by harvest Dataset metadata from primary Data Repositories or harvesting JSON-LD files served by these same pages for rapid, shallow indexing. The former method is often richer but requires more 

### What are examples of Data Catalogues?

* Commercial solutions:
    *  (Collibra](https://www.collibra.com/download/data-catalog-study-dresner-advisory-services-ppc?_bk=catalogue%20data&_bt=389929247489&_bm=e&_bn=g)

    * [DataMed](https://datamed.org/)
    * [OMICS-DI](https://www.omicsdi.org/)
----



## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| []()  | []()  | []()  |
| []()  | []()  | []()  |
| []()  | []()  | []()  |

## Table of Data Standards

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| [JSON]()  | []()  | []()  |
| [RDF]()  | [DCAT v1]()  | [DATS]()  |
| [RDF]()  | [DCAT v2]()  | [DATS]()  |
| [JSON-LD]()  | [Schema.org]()  | []()  |


___


## Executable Code in Notebook

TO BE AUGMENTED.

```python
import dats
import json
import pandas as pd 
...
```



## References:



## Authors:

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Philippe Rocca-Serra |  University of Oxford, Data Readiness Group| [0000-0001-9853-5668](https://orcid.org/orcid.org/0000-0001-9853-5668) | Writing - Original Draft |


___


## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
