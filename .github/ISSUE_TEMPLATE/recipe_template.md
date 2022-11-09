(fcb-recipeshorthand-template)=
# Recipe Template



```{admonition} Important
:class: tip
This section is highly standardized and is relied upon by another component developed by FAIRplus to enhance search and presentation. It is therefore important to comply with the layout. 
The authors should therefore edit the all but the `recipe metadata`. 
For the `Intended Audience` section, the allowed values should be picked from the following list:

    - Funder
    - Procurement Officer
    - Principal Investigator
    - Data Curator
    - Data Manager
    - Data Scientist
        - Chemoinformatician
        - Bioinformatician
    - Software Engineer
    - System Administrator
    - Terminology Manager
    - Ontologist


For the `Recipe Type` section, the allowed values should be picked from the following list:

    - Background information (introductory material)
    - Survey / Review (state of the art material)
    - Guidance (documentation aimed at both technical and non-technical audience)
    - Technical Guidance (documentation aimed at a technical audience, without executable code examples)
    - Hands-on (documentation aimed at a technical audience, with executable code examples available as jupyter notebooks)



```

---

````{panels_fairplus}
:identifier_text: FCBxxx
:identifier_link: 'https://w3id.org/faircookbook/FCBxxx'
:difficulty_level: <select a level, from 1 to 5 >
:recipe_type: hands-on, background_information, guidance, technical_guidance, survey
:reading_time_minutes: e.g. 15
:intended_audience: chemoinformatician, data_curator, data_manager, data_scientist  
:maturity_level: <select a level, from 1 to 5 >
:maturity_indicator: <select a level, from 1 to 55, refering to the FAIRplus DSM guidance.
:has_executable_code: yeah
:recipe_name: a name that should match the recipe name used in the table of content
```` 



---

## Main Objectives

The main purpose of this recipe is:

> Provid a summary statement about the purpose of the recipe.

---


## Graphical Overview

Note: use this section to provide a decision tree for the overall process described in the recipe
For more information about the syntax used to generate the diagram, please refer to the [following documentation](https://mermaid-js.github.io/mermaid/#/flowchart)


````{panels} 
:container: container-lg pb-3
:column: col-lg-12 p-2
:card: rounded

<div class="mermaid">
graph TD;
    A(Data Acquisition):::box -->B(Raw Data):::box
    B --> C{FAIR by Design}
    C:::box-->|Yes| D(Standard Compliant Data):::box
    C:::box -->|No| E(Vendor locked Data):::box
    classDef box font-family:avenir,font-size:14px,fill:#2a9fc9,stroke:#222,color:#fff,stroke-width:1px
    linkStyle 0,1,2,3 stroke:#2a9fc9,stroke-width:1px,color:#2a9fc9,font-family:avenir;
</div>

````


````{panels} 
:container: container-lg pb-3
:column: col-lg-12 p-2
:card: rounded

<div class="mermaid" align="left">
classDiagram
  SharedData <-- DataOwner: owns
  SharedData <-- DataConsumer: consumes
  SharedData <-- DataProvider: provides
  class SharedData
  class DataOwner
  class DataProvider
  class DataConsumer
  
</div>
````


---


## Requirements

* technical requirements:
   * bash knowledge
   * ...
* recipe dependency:
   * read Recipe 1 first!
* knowledge requirement:
   * be sure to know what OBO is, or read it here: ...link to knowledge...

---


## FAIRification Objectives, Inputs and Outputs


```{tabbed} FAIRification Objectives, Inputs and Outputs
| [validation](http://edamontology.org/operation_2428)  | [Structure Data File (SDF)](https://fairsharing.org/FAIRsharing.ew26v7)  | [report](http://edamontology.org/data_2048)  |
| [calculation](http://edamontology.org/operation_3438)  | [Structure Data File (SDF)](https://fairsharing.org/FAIRsharing.ew26v7) | [InChi](https://fairsharing.org/FAIRsharing.ddk9t9) |
| [calculation](http://edamontology.org/operation_3438)  | [Structure Data File (SDF)](https://fairsharing.org/FAIRsharing.ew26v7)  | [SMILES](https://fairsharing.org/FAIRsharing.qv4b3c)  |
| [text annotation](http://edamontology.org/operation_3778)  | [Human Phenotype Ontology](https://fairsharing.org/FAIRsharing.kbtt7f)  | [annotated text](http://edamontology.org/data_3779)  |
```
```{tabbed} Tools
* Skill dependency:
   * Bash experience (for example)
* Technical requirements:
   * Python (for example)
```


## Table of Data Standards

Authors should list all the data standards, format specification, syntax and controlled terminologies used in the FAIRification process applied to the IMI project data.
Ideally, authors should mark up the information using either EDAM Ontology URI or FAIRsharing identifiers (which are DOIs)

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| [FASTQ](https://fairsharing.org/FAIRsharing.r2ts5t)  | [LOINC](https://fairsharing.org/FAIRsharing.2mk2zb)  | [SRA XML](https://fairsharing.org/FAIRsharing.q72e3w)  |
| [DICOM](https://fairsharing.org/FAIRsharing.b7z8by)  | [Human Phenotype Ontology](https://fairsharing.org/FAIRsharing.kbtt7f)  | [OMOP](https://fairsharing.org/FAIRsharing.qk984b)  |

---

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

If you want to include figures, please use the following 



```{figure} ./my_figure.svg
---
width: 700px
name: the figure title
alt: something to display if the link to the figure is broken
---
the proper caption for the figure.
```


one may use the following **[mermaid](https://mermaid-js.github.io/mermaid/#/)** syntax:

````{panels} 
:container: container-lg pb-3
:column: col-lg-12 p-2
:card: rounded

```
graph LR;
    A[Data Acquisition] -->B(Raw Data)
    B --> C{FAIR by Design}
    C -->|Yes| D[Standard Compliant Data]
    C -->|No| E[Vendor locked Data]
```
````
which is then rendered like this:

````{panels} 
:container: container-lg pb-3
:column: col-lg-12 p-2
:card: rounded

<div class="mermaid">
graph LR;
    A[Data Acquisition] -->B(Raw Data)
    B --> C{FAIR by Design}
    C -->|Yes| D[Standard Compliant Data]
    C -->|No| E[Vendor locked Data]
</div>
````

Authors of graphical representations using the mermaid syntax can also style their graphs, as shown below

````{panels} 
:container: container-lg pb-3
:column: col-lg-12 p-2
:card: rounded

<div class="mermaid">
graph TD;
    A[input data]-->B[conversion to open format]
    A[input data]-->C[automatic annotation]
    B[conversion to open format]-->D((output data))
    C[automatic annotation]-->D((output data))  
    style A fill:#FF5733,stroke:#333,stroke-width:2px
    style D fill:#0A749B,stroke:#333,stroke-width:2px
</div>
````


---

## Conclusion

Summerize Key Learnings of the recipe.

Suggest further reading using the following:

### What to read next?
* [Tips and Tricks](./tips-tricks.md)
* [how-to-create-recipe-with-hackmd](./how-to-create-recipe-with-hackmd.md)
* using a reference tag affored by MyST markdown and sphinx with JupyterBook 0.7+. {ref}`fcb-intro-fair-principles`

````{rdmkit_panel}
````

---

## Authors

````{authors_fairplus}
YourName: YourContribution
````


---

## License

````{license_fairplus}
CC-BY-4.0
````
