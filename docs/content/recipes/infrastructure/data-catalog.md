# Building a Dataset Catalogue

<!-- **identifier:**

**version:** [v0.1](v0.1)

___

**_Difficulty level:_** :triangular_flag_on_post: :triangular_flag_on_post: :triangular_flag_on_post:  :triangular_flag_on_post: :white_circle:

**_Reading time:_** 60 minutes (when the recipe is completed)

**_Intended Audience:_** 

> :heavy_check_mark: Data Managers

> :heavy_check_mark: Software Engineer

> :heavy_check_mark: System Administrator

> :heavy_check_mark: Data Scientists


**_Recipe Type_**: Survey / Review

**_Executable code_**: Yes -->

___

<div class="row">

  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-qrcode fa-2x" style="color:#7e0038;"></i>
        <h4><b>Recipe metadata</b></h4>
        <p> identifier: <a href="">RX.X</a> </p>
        <p> version: <a href="">v0.1</a> </p>
      </div>
    </div>
  </div>
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-fire fa-2x" style="color:#7e0038;"></i>
        <h4><b>Difficulty level</b></h4>
        <i class="fa fa-fire fa-lg" style="color:#7e0038;"></i>
        <i class="fa fa-fire fa-lg" style="color:#7e0038;"></i>
        <i class="fa fa-fire fa-lg" style="color:#7e0038;"></i>
        <i class="fa fa-fire fa-lg" style="color:l#7e0038;"></i>
        <i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
  <!--       <p><span data-v-013baba1="" title="" class=""><svg data-v-013baba1="" viewBox="0 0 16 16" width="1em" height="1em" focusable="false" role="img" alt="icon" xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi-bar-chart-fill b-icon bi medium-level"><g data-v-013baba1=""><rect width="4" height="5" x="1" y="10" rx="1"></rect><rect width="4" height="9" x="6" y="6" rx="1"></rect><rect width="4" height="14" x="11" y="1" rx="1"></rect></g></svg> Medium </span></p> -->
      </div>
    </div>
  </div>  
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-clock-o fa-2x" style="color:#7e0038;"></i>
        <h4><b>Reading Time</b></h4>
        <p><i class="fa fa-clock-o fa-lg" style="color:#7e0038;"></i> 60 minutes (upon recipe completion)</p>
        <h4><b>Recipe Type</b></h4>
        <p><i class="fa fa-laptop fa-lg" style="color:#7e0038;"></i> Hands-on</p>
        <h4><b>Executable Code</b></h4>
        <p><i class="fa fa-play-circle fa-lg" style="color:#7e0038;"></i> Yes</p>
      </div>
    </div>
  </div>
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-group fa-2x" style="color:#7e0038;"></i>
        <h4><b>Intended Audience</b></h4>
<!--         <p> <i class="fa fa-tags fa-lg" style="color:#7e0038;"></i> Terminology Managers </p> -->
        <p> <i class="fa fa-database fa-lg" style="color:#7e0038;"></i> Data Managers </p>
        <p> <i class="fa fa-wrench fa-lg" style="color:#7e0038;"></i> Data Scientists </p>
        <p> <i class="fa fa-cogs fa-lg" style="color:#7e0038;"></i> Software Developers </p>
        <p> <i class="fa fa-terminal fa-lg" style="color:#7e0038;"></i> System Administrators</p>
      </div>
    </div>
  </div>
</div>

___

## Main Objectives

The main purpose of this recipe is:

>  To detail the key elements for the creation of a `data catalogue` to enable data `findability` in an organisation.

We will cover the following points:

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
<style>
    .mermaidClass > rect{
        fill:#FF0000;
        stroke:#FFFF00;
        stroke-width:4px;
    }
</style>

 <div class="mermaid">
  graph TD

  subgraph b
  AA(Populate Data Catalogue):::box
  AA --> |identify<br>data<br>sources| E(Data Source #1):::box
  AA --> |identify<br>data<br>sources| F(Data Source #n):::box
  
  E -->|ETL-1|B1(instance file):::box
  F -->|ETL-2|B2(instance file):::box

  B1 -->|data persistence| DL(document oriented database)
  B2 -->|data persistence| DL:::box

  DL[Build Search Function] --> |build search index|SE(Search Engine):::box
  SE -->|ontology tree search| SSS(Query Expansion):::box
  SE -->|synonym space search| SSS(Query Expansion)
  end

  subgraph a
  A(Building Data Catalogue):::box
  style a fill:#e8eaeb,font-family:avenir
  style b fill:#e8eaeb
  A-->|define curation policies| A3(Curation<br> Policies):::box
  A3-->|select data model| B(DATS):::box
  B-->|select controled<br> vocabularies| CV1(key facet #1:<br> CV1):::box
  B-->|select controled<br> vocabularies| CV2(key facet #2:<br> CV2):::box
  B-->|select controled<br> vocabularies| CV3(key facet #n:<br> CVn):::box

  linkStyle 0,1,2,3,4,5,6,7,8,9,10,11,12,13 stroke:#2a9fc9,stroke-width:1px,color:#2a9fc9,font-family:avenir;
  classDef box font-family:avenir,font-size:14px,fill:#2a9fc9,stroke:#222,color:#fff,stroke-width:1px
  end
</div>

<!-- 
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiBcbiAgc3ViZ3JhcGggdHdvXG4gIEFBKFBvcHVsYXRlIERhdGEgQ2F0YWxvZ3VlKTo6OmJveFxuICBBQSAtLT4gfGlkZW50aWZ5PGJyPmRhdGE8YnI-c291cmNlc3wgRShEYXRhIFNvdXJjZSAjMSk6Ojpib3hcbiAgQUEgLS0-IHxpZGVudGlmeTxicj5kYXRhPGJyPnNvdXJjZXN8IEYoRGF0YSBTb3VyY2UgI24pOjo6Ym94XG4gIFxuICBFIC0tPnxFVEwtMXxCMShpbnN0YW5jZSBmaWxlKTo6OmJveFxuICBGIC0tPnxFVEwtMnxCMihpbnN0YW5jZSBmaWxlKTo6OmJveFxuXG4gIEIxIC0tPnxkYXRhIHBlcnNpc3RlbmNlfCBETChkb2N1bWVudCBvcmllbnRlZCBkYXRhYmFzZSlcbiAgQjIgLS0-fGRhdGEgcGVyc2lzdGVuY2V8IERMOjo6Ym94XG5cbiAgRExbQnVpbGQgU2VhcmNoIEZ1bmN0aW9uXSAtLT4gfGJ1aWxkIHNlYXJjaCBpbmRleHxTRShTZWFyY2ggRW5naW5lKTo6OmJveFxuICBTRSAtLT58b250b2xvZ3kgdHJlZSBzZWFyY2h8IFNTUyhRdWVyeSBFeHBhbnNpb24pOjo6Ym94XG4gIFNFIC0tPnxzeW5vbnltIHNwYWNlIHNlYXJjaHwgU1NTKFF1ZXJ5IEV4cGFuc2lvbilcbiAgZW5kXG5cbiAgc3ViZ3JhcGggb25lXG4gIEEoQnVpbGRpbmcgRGF0YSBDYXRhbG9ndWUpIFxuICBzdHlsZSBBIGZpbGw6IzJhOWZjOSxzdHJva2U6IzIyMixjb2xvcjojZmZmLHN0cm9rZS13aWR0aDoxcHhcbiAgY2xhc3NEZWYgYm94IGZpbGw6IzJhOWZjOSxjb2xvcjojZmZmO1xuICBBIC0tPiB8ZGVmaW5lIGN1cmF0aW9uIHBvbGljaWVzfCBBMyhDdXJhdGlvbjxicj4gUG9saWNpZXMpOjo6Ym94XG4gIFxuICBCOjo6Ym94IC0tPnxzZWxlY3QgY29udHJvbGxlZDxicj4gdm9jYWJ1bGFyaWVzfCBDVjEoa2V5LWZhY2V0IzE6PGJyPiBDVjEpOjo6Ym94XG4gIEIgLS0-fHNlbGVjdCBjb250cm9sbGVkPGJyPiB2b2NhYnVsYXJpZXN8IENWMihrZXktZmFjZXQjMjo8YnI-IENWMik6Ojpib3hcbiAgQiAtLT58c2VsZWN0IGNvbnRyb2xsZWQ8YnI-IHZvY2FidWxhcmllc3wgQ1YzKGtleS1mYWNldCNuOjxicj4gQ1ZuKTo6OmJveFxuXG4gIEEzIC0tPnxzZWxlY3QgZGF0YSBtb2RlbHwgQihEQVRTKVxuICBlbmRcblx0XHQiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiBcbiAgc3ViZ3JhcGggdHdvXG4gIEFBKFBvcHVsYXRlIERhdGEgQ2F0YWxvZ3VlKTo6OmJveFxuICBBQSAtLT4gfGlkZW50aWZ5PGJyPmRhdGE8YnI-c291cmNlc3wgRShEYXRhIFNvdXJjZSAjMSk6Ojpib3hcbiAgQUEgLS0-IHxpZGVudGlmeTxicj5kYXRhPGJyPnNvdXJjZXN8IEYoRGF0YSBTb3VyY2UgI24pOjo6Ym94XG4gIFxuICBFIC0tPnxFVEwtMXxCMShpbnN0YW5jZSBmaWxlKTo6OmJveFxuICBGIC0tPnxFVEwtMnxCMihpbnN0YW5jZSBmaWxlKTo6OmJveFxuXG4gIEIxIC0tPnxkYXRhIHBlcnNpc3RlbmNlfCBETChkb2N1bWVudCBvcmllbnRlZCBkYXRhYmFzZSlcbiAgQjIgLS0-fGRhdGEgcGVyc2lzdGVuY2V8IERMOjo6Ym94XG5cbiAgRExbQnVpbGQgU2VhcmNoIEZ1bmN0aW9uXSAtLT4gfGJ1aWxkIHNlYXJjaCBpbmRleHxTRShTZWFyY2ggRW5naW5lKTo6OmJveFxuICBTRSAtLT58b250b2xvZ3kgdHJlZSBzZWFyY2h8IFNTUyhRdWVyeSBFeHBhbnNpb24pOjo6Ym94XG4gIFNFIC0tPnxzeW5vbnltIHNwYWNlIHNlYXJjaHwgU1NTKFF1ZXJ5IEV4cGFuc2lvbilcbiAgZW5kXG5cbiAgc3ViZ3JhcGggb25lXG4gIEEoQnVpbGRpbmcgRGF0YSBDYXRhbG9ndWUpIFxuICBzdHlsZSBBIGZpbGw6IzJhOWZjOSxzdHJva2U6IzIyMixjb2xvcjojZmZmLHN0cm9rZS13aWR0aDoxcHhcbiAgY2xhc3NEZWYgYm94IGZpbGw6IzJhOWZjOSxjb2xvcjojZmZmO1xuICBBIC0tPiB8ZGVmaW5lIGN1cmF0aW9uIHBvbGljaWVzfCBBMyhDdXJhdGlvbjxicj4gUG9saWNpZXMpOjo6Ym94XG4gIFxuICBCOjo6Ym94IC0tPnxzZWxlY3QgY29udHJvbGxlZDxicj4gdm9jYWJ1bGFyaWVzfCBDVjEoa2V5LWZhY2V0IzE6PGJyPiBDVjEpOjo6Ym94XG4gIEIgLS0-fHNlbGVjdCBjb250cm9sbGVkPGJyPiB2b2NhYnVsYXJpZXN8IENWMihrZXktZmFjZXQjMjo8YnI-IENWMik6Ojpib3hcbiAgQiAtLT58c2VsZWN0IGNvbnRyb2xsZWQ8YnI-IHZvY2FidWxhcmllc3wgQ1YzKGtleS1mYWNldCNuOjxicj4gQ1ZuKTo6OmJveFxuXG4gIEEzIC0tPnxzZWxlY3QgZGF0YSBtb2RlbHwgQihEQVRTKVxuICBlbmRcblx0XHQiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)  
-->


---

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
