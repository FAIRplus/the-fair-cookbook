(fcb-help-recipe-template)=
# Recipe Template

+++
<br/>

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

----

````{panels}
:container: container-lg pb-3
:column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-1
:card: rounded

<i class="fa fa-qrcode fa-2x" style="color:#7e0038;"></i>
^^^
<h4><b>Recipe metadata</b></h4>
 identifier: <a href="">RX.X</a> 
 version: <a href="">v1.0</a>

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
<i class="fa fa-laptop fa-lg" style="color:#7e0038;"></i> Background Information
<h4><b>Executable Code</b></h4>
<i class="fa fa-play-circle fa-lg" style="color:#7e0038;"></i> No

---
<i class="fa fa-users fa-2x" style="color:#7e0038;"></i>
^^^
<h4><b>Intended Audience</b></h4>
<p><i class="fa fa-user-md fa-lg" style="color:#7e0038;"></i> Principal Investigator</p>
<p><i class="fa fa-database fa-lg" style="color:#7e0038;"></i> Data Manager</p>
<p><i class="fa fa-wrench fa-lg" style="color:#7e0038;"></i> Data Scientist</p>
<p><i class="fa fa-money fa-lg" style="color:#7e0038;"></i> Funder</p>
````


---

## Main Objectives

The main purpose of this recipe is:

> Provid a summary statement about the purpose of the recipe.

___


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

This section is meant for authors to describe the specific `capability` which they aim to bring from one `maturity level` to the next.
This is therefore to document the methods used **to enable change** at the level of information process
The table is therefore structure to identify the capability, the **initial** maturity level it is estimated to be and the **final** maturity it has been brought to.


| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Interoperability | minimal | repeatable |

```{admonition} Important
:class: tip
this section is relied upon by another component developed by FAIRplus to enhance search and presentation. It is therefore important to comply with the layout. 
```

----

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [validation](http://edamontology.org/operation_2428)  | [Structure Data File (SDF)](https://fairsharing.org/FAIRsharing.ew26v7)  | [report](http://edamontology.org/data_2048)  |
| [calculation](http://edamontology.org/operation_3438)  | [Structure Data File (SDF)](https://fairsharing.org/FAIRsharing.ew26v7) | [InChi](https://fairsharing.org/FAIRsharing.ddk9t9) |
| [calculation](http://edamontology.org/operation_3438)  | [Structure Data File (SDF)](https://fairsharing.org/FAIRsharing.ew26v7)  | [SMILES](https://fairsharing.org/FAIRsharing.qv4b3c)  |
| [text annotation](http://edamontology.org/operation_3778)  | [Human Phenotype Ontology](https://fairsharing.org/FAIRsharing.kbtt7f)  | [annotated text](http://edamontology.org/data_3779)  |


## Table of Data Standards

Authors should list all the data standards, format specification, syntax and controlled terminologies used in the FAIRification process applied to the IMI project data.
Ideally, authors should mark up the information using either EDAM Ontology URI or FAIRsharing identifiers (which are DOIs)

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


___

## Conclusion

> Summerize Key Learnings of the recipe.
> 
> Suggest further reading using the following:
> ### What should I read next?
> * [Tips and Tricks](./tips-tricks.md)
> * [how-to-create-recipe-with-hackmd](./how-to-create-recipe-with-hackmd.md)
> * using a reference tag affored by MyST markdown and sphinx with JupyterBook 0.7+. {ref}`fcb-intro-fair-principles`

___

## Authors

| Name | Affiliation  | orcid | CrediT role  | specific contribution |
| :------------- | :------------- | :------------- |:------------- |:------------- |
| First Name Last Name |  Organization, Country| [0000-0000-0000-0000](https://orcid.org/orcid.org/0000-0000-0000-0000) | Writing - Original Draft | original format |

___



## License

This page is released under the Creative Commons 4.0 BY license.

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png" height="20"/></a>
