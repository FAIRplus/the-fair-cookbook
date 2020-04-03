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

> Building an application ontology from source ontologies using ROBOT via a sustainable dynamic pipeline to allow seamless integration of source ontology updates

___

## Ingredients

Tools
- Ontology development kit (https://github.com/INCATools/ontology-development-kit) (comes with ROBOT included)
or
- ROBOT (http://robot.obolibrary.org/)
- Protégé/other ontology editor



## Step by step process

### Step 1: Select appropriate source ontologies & branches

reference other recipe 

### Step 2: Build the upper level "umbrella" ontology 

tools: protege/other ontology editor
considerations: ontology base URI/namespace

### Step 3: Extract ontology modules from source ontologies

discuss different approaches for extraction (TOP/BOT/MIREOT) with guidance of which to use

pros & cons of different methods

#### Module extraction - using manual text lists

#### Module extraction - using SPARQL

### Step 4: Merge extracted modules under the umbrella



### Step 5: Post-merge modifications
eg removing extraneous classes



## Graphical Overview of the FAIRification Recipe Objectives

<!-- TO DO -->

<div class="mermaid">
graph LR;
    A[Data Acquisition] -->B(Raw Data)
    B --> C{FAIR by Design}
    C -->|Yes| D[Standard Compliant Data]
    C -->|No| E[Vendor locked Data]
</div>

___

## Capability & Maturity Table

<!-- TO DO -->

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Interoperability | minimal | repeatable |

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

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Danielle Welter |  LCSB, University of Luxembourg| [0000-0003-1058-2668](https://orcid.org/0000-0003-1058-2668) | Writing - Original Draft |

___


## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
