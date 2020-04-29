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
```
graph TD
  A[Building Data Catalogue] 

  A --> |define curation policies| A3[Curation<br> Policies]
  
  B -->|select controlled<br> vocabularies| CV1[key-facet#1:<br> CV1]
  B -->|select controlled<br> vocabularies| CV2[key-facet#2:<br> CV2]
  B -->|select controlled<br> vocabularies| CV3[key-facet#n:<br> CVn]

  A3 -->|select data model| B(DATS)

  AA[Populate Data Catalogue]
  AA --> |identify<br>data<br>sources| E[Data Source #1]
  AA --> |identify<br>data<br>sources| F[Data Source #n]
  
  E -->|ETL-1|B1[instance file]
  F -->|ETL-2|B2[instance file]

  B1 -->|data persistence| DL[document oriented database]
  B2 -->|data persistence| DL

  DL[Build Search Function] --> |build search index|SE[Search Engine]
  SE -->|ontology tree search| SSS[Query Expansion]
  SE -->|synonym space search| SSS[Query Expansion]

		
```
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgQVtCdWlsZGluZyBEYXRhIENhdGFsb2d1ZV0gXG5cbiAgQSAtLT4gfGRlZmluZSBjdXJhdGlvbiBwb2xpY2llc3wgQTNbQ3VyYXRpb248YnI-IFBvbGljaWVzXVxuICBcbiAgQiAtLT58c2VsZWN0IGNvbnRyb2xsZWQ8YnI-IHZvY2FidWxhcmllc3wgQ1YxW2tleS1mYWNldCMxOjxicj4gQ1YxXVxuICBCIC0tPnxzZWxlY3QgY29udHJvbGxlZDxicj4gdm9jYWJ1bGFyaWVzfCBDVjJba2V5LWZhY2V0IzI6PGJyPiBDVjJdXG4gIEIgLS0-fHNlbGVjdCBjb250cm9sbGVkPGJyPiB2b2NhYnVsYXJpZXN8IENWM1trZXktZmFjZXQjbjo8YnI-IENWbl1cblxuICBBMyAtLT58c2VsZWN0IGRhdGEgbW9kZWx8IEIoREFUUylcblxuICBBQVtQb3B1bGF0ZSBEYXRhIENhdGFsb2d1ZV1cbiAgQUEgLS0-IHxpZGVudGlmeTxicj5kYXRhPGJyPnNvdXJjZXN8IEVbRGF0YSBTb3VyY2UgIzFdXG4gIEFBIC0tPiB8aWRlbnRpZnk8YnI-ZGF0YTxicj5zb3VyY2VzfCBGW0RhdGEgU291cmNlICNuXVxuICBcbiAgRSAtLT58RVRMLTF8QjFbaW5zdGFuY2UgZmlsZV1cbiAgRiAtLT58RVRMLTJ8QjJbaW5zdGFuY2UgZmlsZV1cblxuICBCMSAtLT58ZGF0YSBwZXJzaXN0ZW5jZXwgRExbZG9jdW1lbnQgb3JpZW50ZWQgZGF0YWJhc2VdXG4gIEIyIC0tPnxkYXRhIHBlcnNpc3RlbmNlfCBETFxuXG4gIERMW0J1aWxkIFNlYXJjaCBGdW5jdGlvbl0gLS0-IHxidWlsZCBzZWFyY2ggaW5kZXh8U0VbU2VhcmNoIEVuZ2luZV1cbiAgU0UgLS0-fG9udG9sb2d5IHRyZWUgc2VhcmNofCBTU1NbUXVlcnkgRXhwYW5zaW9uXVxuICBTRSAtLT58c3lub255bSBzcGFjZSBzZWFyY2h8IFNTU1tRdWVyeSBFeHBhbnNpb25dXG5cblx0XHQiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiAgQVtCdWlsZGluZyBEYXRhIENhdGFsb2d1ZV0gXG5cbiAgQSAtLT4gfGRlZmluZSBjdXJhdGlvbiBwb2xpY2llc3wgQTNbQ3VyYXRpb248YnI-IFBvbGljaWVzXVxuICBcbiAgQiAtLT58c2VsZWN0IGNvbnRyb2xsZWQ8YnI-IHZvY2FidWxhcmllc3wgQ1YxW2tleS1mYWNldCMxOjxicj4gQ1YxXVxuICBCIC0tPnxzZWxlY3QgY29udHJvbGxlZDxicj4gdm9jYWJ1bGFyaWVzfCBDVjJba2V5LWZhY2V0IzI6PGJyPiBDVjJdXG4gIEIgLS0-fHNlbGVjdCBjb250cm9sbGVkPGJyPiB2b2NhYnVsYXJpZXN8IENWM1trZXktZmFjZXQjbjo8YnI-IENWbl1cblxuICBBMyAtLT58c2VsZWN0IGRhdGEgbW9kZWx8IEIoREFUUylcblxuICBBQVtQb3B1bGF0ZSBEYXRhIENhdGFsb2d1ZV1cbiAgQUEgLS0-IHxpZGVudGlmeTxicj5kYXRhPGJyPnNvdXJjZXN8IEVbRGF0YSBTb3VyY2UgIzFdXG4gIEFBIC0tPiB8aWRlbnRpZnk8YnI-ZGF0YTxicj5zb3VyY2VzfCBGW0RhdGEgU291cmNlICNuXVxuICBcbiAgRSAtLT58RVRMLTF8QjFbaW5zdGFuY2UgZmlsZV1cbiAgRiAtLT58RVRMLTJ8QjJbaW5zdGFuY2UgZmlsZV1cblxuICBCMSAtLT58ZGF0YSBwZXJzaXN0ZW5jZXwgRExbZG9jdW1lbnQgb3JpZW50ZWQgZGF0YWJhc2VdXG4gIEIyIC0tPnxkYXRhIHBlcnNpc3RlbmNlfCBETFxuXG4gIERMW0J1aWxkIFNlYXJjaCBGdW5jdGlvbl0gLS0-IHxidWlsZCBzZWFyY2ggaW5kZXh8U0VbU2VhcmNoIEVuZ2luZV1cbiAgU0UgLS0-fG9udG9sb2d5IHRyZWUgc2VhcmNofCBTU1NbUXVlcnkgRXhwYW5zaW9uXVxuICBTRSAtLT58c3lub255bSBzcGFjZSBzZWFyY2h8IFNTU1tRdWVyeSBFeHBhbnNpb25dXG5cblx0XHQiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)
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
