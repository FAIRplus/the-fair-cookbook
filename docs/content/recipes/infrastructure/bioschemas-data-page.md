# Findability: Data Page Markup with Bioschemas 

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

## Main Objectives

The main purpose of this recipe is:

> To markup a webpage representing a data record with Bioschemas compliant markup.

___


## Graphical Overview of the FAIRification Recipe Objectives



[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiBBW0hUTUwgcGFnZV0gLS0-IEJ7d2hhdCB0eXBlIG9mIHJlc291cmNlP31cbiBCIC0tPiBDW0NoZW1pY2FsIFN1YnN0YW5jZV1cbiBCIC0tPiBEW0dlbmVdXG4gQiAtLT4gRVtNb2xlY3VsYXIgRW50aXR5XVxuIEIgLS0-IEZbUHJvdGVpbl1cbiBCIC0tPiBHW1NhbXBsZV1cbiBCIC0tPiBIW1RheG9uXVxuIEMgLS0-IElcbiBEIC0tPiBJXG4gRSAtLT4gSVxuIEYgLS0-IElcbiBHIC0tPiBJXG4gSCAtLT4gSVtmYTpmYS1zZWFyY2ggZmE6ZmEtY29nIGZhOmZhLWZpZ2h0ZXItamV0IFNjaGVtYS5vcmcgYXVnbWVudGVkIEhUTUwgcGFnZV0iLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiBBW0hUTUwgcGFnZV0gLS0-IEJ7d2hhdCB0eXBlIG9mIHJlc291cmNlP31cbiBCIC0tPiBDW0NoZW1pY2FsIFN1YnN0YW5jZV1cbiBCIC0tPiBEW0dlbmVdXG4gQiAtLT4gRVtNb2xlY3VsYXIgRW50aXR5XVxuIEIgLS0-IEZbUHJvdGVpbl1cbiBCIC0tPiBHW1NhbXBsZV1cbiBCIC0tPiBIW1RheG9uXVxuIEMgLS0-IElcbiBEIC0tPiBJXG4gRSAtLT4gSVxuIEYgLS0-IElcbiBHIC0tPiBJXG4gSCAtLT4gSVtmYTpmYS1zZWFyY2ggZmE6ZmEtY29nIGZhOmZhLWZpZ2h0ZXItamV0IFNjaGVtYS5vcmcgYXVnbWVudGVkIEhUTUwgcGFnZV0iLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)

```
graph TD
 A[HTML page] --> B{what type of resource?}
 B --> C[Chemical Substance]
 B --> D[Gene]
 B --> E[Molecular Entity]
 B --> F[Protein]
 B --> G[Sample]
 B --> H[Taxon]
 C --> I
 D --> I
 E --> I
 F --> I
 G --> I
 H --> I[fa:fa-search fa:fa-cog fa:fa-fighter-jet Schema.org augmented HTML page]
```



___

## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Findability | minimal | repeatable |
| Interoperability | minimal |  |

----

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [validation](http://edamontology.org/operation_2428)  | [Structure Data File (SDF)](https://fairsharing.org/FAIRsharing.ew26v7)  | [report](http://edamontology.org/data_2048)  |
| [calculation](http://edamontology.org/operation_3438)  | [Structure Data File (SDF)](https://fairsharing.org/FAIRsharing.ew26v7) | [InChi](https://fairsharing.org/FAIRsharing.ddk9t9) |
| [calculation](http://edamontology.org/operation_3438)  | [Structure Data File (SDF)](https://fairsharing.org/FAIRsharing.ew26v7)  | [SMILES](https://fairsharing.org/FAIRsharing.qv4b3c)  |
| [text annotation](http://edamontology.org/operation_3778)  | [Human Phenotype Ontology](https://fairsharing.org/FAIRsharing.kbtt7f)  | [annotated text](http://edamontology.org/data_3779)  |


## Table of Data Standards

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| [FASTQ](https://fairsharing.org/FAIRsharing.r2ts5t)  | [LOINC](https://fairsharing.org/FAIRsharing.2mk2zb)  | [SRA XML](https://fairsharing.org/FAIRsharing.q72e3w)  |
| [DICOM](https://fairsharing.org/FAIRsharing.b7z8by)  | [Human Phenotype Ontology](https://fairsharing.org/FAIRsharing.kbtt7f)  | [OMOP](https://fairsharing.org/FAIRsharing.qk984b)  |

___


## Executable Code in Notebook


```python
import isatools
import json
import pandas as pd 
import holoview
```

___

## How to create workflow figures

one may use the following **[mermaid](https://mermaid-js.github.io/mermaid/#/)** syntax:

```
graph LR;
    A[Data Acquisition] -->B(Raw Data)
    B --> C{FAIR by Design}
    C -->|Yes| D[Standard Compliant Data]
    C -->|No| E[Vendor locked Data]
```

<div class="mermaid">
graph LR;
    A["input data"]-->B["conversion to open format"];
    A["input data"]-->C["automatic annotation"];
    B["conversion to open format"]-->D(("output data"));
    C["automatic annotation"]-->D(("output data"));  

    style A fill:#FF5733,stroke:#333,stroke-width:2px
    style D fill:#0A749B,stroke:#333,stroke-width:2px
</div>

___



## Authors:

| Name          | Affiliation                                                  | orcid                                                        | CrediT role              |
| :------------ | :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------- |
| Alasdair Gray | Bioschemas Community Lead / Heriot-Watt Unviersity / ELIXIR-UK | [0000-0002-5711-4872](https://orcid.org/0000-0002-5711-4872) | Writing - Original Draft |

___


## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
