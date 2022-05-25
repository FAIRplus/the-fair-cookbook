---
dummy: dummy
---

# [Introduction to the DATS model]

**identifier:** [RX.X_FIXME](RX.X_FIXME)

**version:** [0.1](0.1)

___

**_Difficulty level:_** moderate :triangular_flag_on_post: :triangular_flag_on_post: :white_circle:  :white_circle: :white_circle: _FIXME

**_Reading time:_** _FIXME minutes 

**_Intended Audience:_** 

> :heavy_check_mark: set_value_FIXME, e.g. Data Scientist

> :heavy_check_mark: set_value_FIXME, e.g. Data Scientist


**_Recipe Type_**: set_value_FIXME, e.g. Hands on

**_Executable code_**: set_value_FIXME, [Yes,No]


[TOC]
## Table of Contents
1. [Main FAIRification Objectives](#Main%20FAIRification%20Objectives)
2. [Graphical Overview of the FAIRification Recipe Objectives](#Graphical%20Overview%20of%20the%20FAIRification%20Recipe%20Objectives)
3. Requirements
4. [FAIRification Objectives, Inputs and Outputs](#FAIRification%20Objectives,%20Inputs%20and%20Outputs)
5. [Capability & Maturity Table](#Capability%20&%20Maturity%20Table)
6. [Table of Data Standards](#Table%20of%20Data%20Standards)
7. [Main Content goes here...](#Main%20Content)
    * [... writing executable code](#Executable%20Code%20in%20Notebook)
    * [... creating workflow figures](#How%20to%20create%20workflow%20figures)
8. [License](#License)

---

## Main Objectives

The main purpose of this recipe is:

> Provid a summary statement about the purpose of the recipe.

___


## Graphical Overview of the FAIRification Recipe Objectives

Note: use this section to provide a decision tree for the overall process described in the recipe
For more information about the syntax used to generate the diagram, please refer to the [following documentation](https://mermaid-js.github.io/mermaid/#/flowchart)

<!--
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFI7XG4gICAgQShEYXRhIEFjcXVpc2l0aW9uKTo6OmJveCAtLT5CKFJhdyBEYXRhKTo6OmJveFxuICAgIEIgLS0-IEN7RkFJUiBieSBEZXNpZ259XG4gICAgQzo6OmJveC0tPnxZZXN8IEQoU3RhbmRhcmQgQ29tcGxpYW50IERhdGEpOjo6Ym94XG4gICAgQzo6OmJveCAtLT58Tm98IEUoVmVuZG9yIGxvY2tlZCBEYXRhKTo6OmJveFxuICAgIGNsYXNzRGVmIGJveCBmb250LWZhbWlseTphdmVuaXIsZm9udC1zaXplOjE0cHgsZmlsbDojMmE5ZmM5LHN0cm9rZTojMjIyLGNvbG9yOiNmZmYsc3Ryb2tlLXdpZHRoOjFweFxuICAgIGxpbmtTdHlsZSAwLDEsMiwzIHN0cm9rZTojMmE5ZmM5LHN0cm9rZS13aWR0aDoxcHgsY29sb3I6IzJhOWZjOSxmb250LWZhbWlseTphdmVuaXI7IiwibWVybWFpZCI6eyJ0aGVtZSI6bnVsbH0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggTFI7XG4gICAgQShEYXRhIEFjcXVpc2l0aW9uKTo6OmJveCAtLT5CKFJhdyBEYXRhKTo6OmJveFxuICAgIEIgLS0-IEN7RkFJUiBieSBEZXNpZ259XG4gICAgQzo6OmJveC0tPnxZZXN8IEQoU3RhbmRhcmQgQ29tcGxpYW50IERhdGEpOjo6Ym94XG4gICAgQzo6OmJveCAtLT58Tm98IEUoVmVuZG9yIGxvY2tlZCBEYXRhKTo6OmJveFxuICAgIGNsYXNzRGVmIGJveCBmb250LWZhbWlseTphdmVuaXIsZm9udC1zaXplOjE0cHgsZmlsbDojMmE5ZmM5LHN0cm9rZTojMjIyLGNvbG9yOiNmZmYsc3Ryb2tlLXdpZHRoOjFweFxuICAgIGxpbmtTdHlsZSAwLDEsMiwzIHN0cm9rZTojMmE5ZmM5LHN0cm9rZS13aWR0aDoxcHgsY29sb3I6IzJhOWZjOSxmb250LWZhbWlseTphdmVuaXI7IiwibWVybWFpZCI6eyJ0aGVtZSI6bnVsbH0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)
-->


<div class="mermaid">
graph LR;
    A(Data Acquisition):::box -->B(Raw Data):::box
    B --> C{FAIR by Design}
    C:::box-->|Yes| D(Standard Compliant Data):::box
    C:::box -->|No| E(Vendor locked Data):::box
    classDef box font-family:avenir,font-size:14px,fill:#2a9fc9,stroke:#222,color:#fff,stroke-width:1px
    linkStyle 0,1,2,3 stroke:#2a9fc9,stroke-width:1px,color:#2a9fc9,font-family:avenir;
</div>

___


## Requirements

* technical requirements:
   * bash knowledge
   * ...
* recipe dependency:
   * read Recipe 1 first!
* knowledge requirement:
   * be sure to know what OBO is, or read it here: ...link to knowledge...

---

## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Interoperability | minimal | repeatable |

Help to fill this table out can be found ...(not yet)...

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

## Main Content

This is the place for your actual content. You can also ...

### ... write executable code


```python
import isatools
import json
import pandas as pd 
import holoview
```


### ... create workflow figures

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

## Conclusion:

> Summerize Key Learnings of the recipe.
> 
> Suggest further reading using the following:
> #### What should I read next?
> * [HackMD & MarkDown Tips and Tricks](TODO)
> * [A related recipe which nice complements the current one ](TODO)

___
## Authors:

| Name | Affiliation  | orcid | CrediT role  | specific contribution |
| :------------- | :------------- | :------------- |:------------- |:------------- |
| Philippe Rocca-Serra |  University of Oxford, Data Readiness Group| [0000-0001-9853-5668](https://orcid.org/orcid.org/0000-0001-9853-5668) | Writing - Original Draft | original format |
| Danielle Welter |  University of Luxembourg | | Writing - Original draft | | 
___


## License:

This page is released under the Creative Commons 4.0 BY license.

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
