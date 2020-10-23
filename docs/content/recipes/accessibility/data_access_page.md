---
dummy: dummy
---

# [Data access pages]

**identifier:** [RX.X_FIXME](RX.X_FIXME)

**version:** [0.1](0.1)

___

**_Difficulty level:_** moderate :triangular_flag_on_post: :triangular_flag_on_post: :white_circle:  :white_circle: :white_circle: _FIXME

**_Reading time:_** _FIXME minutes 

**_Intended Audience:_** 

> :heavy_check_mark: set_value_FIXME, e.g. Data Scientist

> :heavy_check_mark: set_value_FIXME, e.g. Data Scientist


**_Recipe Type_**: set_value_FIXME, e.g. Hands on

**_Executable code_**: [No]


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

> Provide guidance to resources about structured data access pages

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
   * development access to project website or datastore front end
* recipe dependency:
   * read recipe on data licensing first
* knowledge requirement:
   * Do your datasets contain controlled access data?
   * Is there a process by which external users can gain access to your restricted data, eg via a designated data access committee? 

---

## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Accessibility | minimal | repeatable |



----

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [validation](http://edamontology.org/operation_2428)  | [Structure Data File (SDF)](https://fairsharing.org/FAIRsharing.ew26v7)  | [report](http://edamontology.org/data_2048)  |


## Table of Data Standards

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| N/A  | [EDAM](https://fairsharing.org/FAIRsharing.2mk2zb)  | [Bioschemas](https://fairsharing.org/FAIRsharing.q72e3w)  |


___

## Main Content

Brain dump:

 Check the accessibility status of datasets
·         Is it available?
o    Is it full public access?
·         Provide link to download
o     Is there controlled access?
·         Else not available, is there an accessibility  date?
If there is controlled access:
·         Which parts of the data are under control?
·         What type of control is it and link to getting access


### Accessibility status

Different datasets and resources require different accessibility options depending on the data types they contain. Non-human data is generally not subject to any access controls for ethical reasons, although there may be funding or consortium-related conditions that need to be taken into considerations.

This recipe describes different options for data access requirements and discusses considerations for data providers to make their data maximally accessible while respecting data access restrictions. 

Please note that data access conditions differ from data usage licenses. Data can be fully open access but subject to reuse restrictions depending on the license under which it is released. For mroe information on data usage licenses, please see <TO DO - link required>.

#### Workflow

<div class="mermaid">
graph TD
    A(Does your dataset or resource contain data that requires access controls?)
	A -->|Yes| B(You will need to implement a data access policy for all your data)
	A -->|Partial|D(You will need to implement at least a partial a data access policy)
	A -->|No| C(Great, no further steps required!)
    B --> E{Define & implement a data access policy}
	D --> E
</div>

#### Fully open data

If all the data in a resource or dataset is open access, no restrictions need to be placed on third party access of the data. Data downloads should be made easily accessible through a public project website in whatever format is most appropriate for the data in question.

Please note that open access data should still have a clear data usage license to define any limitations on how the data can be reused.


#### Partial controlled access

Some resources or datasets contain a mix of publicly accessible and access-restricted data, for example if there is a mix of human and animal genomic data. In such a case, it is up to the data or resource owner to decide how to handle access control. Making any non-restricted data openly available is obviously the most desirable option from a FAIR perspective but this comes with a trade-off in terms of implementation costs for a split-level access model. Making all data in a dataset subject to the strictest data access requirements of the most confidential subset has a lower cost in terms of implementation but also sets a greater access and reusability barrier. 

#### Full controlled access

If all data in a dataset or resource is subject to access restrictions, this simplifies the implementation considerations compared to partial controlled access. The entire dataset or resource needs to be subject to access control measures.

#### Setting up a DAC

Any dataset or resource that is subject to access restrictions needs a Data Access Committee (DAC) to evaluate access requests on a case-by-case basis. As a general rule, the parameters for a DAC will have been defined in a project's funding agreement or data management plan. Please refer to the relevant documentation for your project to determine requirements for a DAC.


### Controlled access options

Allowing access to restricted data to third parties is generally done via a Data Access Agreement (DAA). The scope of a DAA in terms of users and data needs to be agreed between an applicant and a DAC. 

#### Per-dataset DAA

Access given for one dataset at a time


#### Resource-wide DAA

Access given to the entire resource

#### Single-user DAA

Access given to a single named user

#### User group DAA

Access given to a group of users, eg all members of a research group. also institutional access.


### Clarifying data access requirements

Every resource with access-restricted data should clearly state what kind of data is subject to access restrictions and why, and under what conditions a user can gain access to the restricted data.

Restrictions can be displayed on a dataset by dataset basis alongside publicly available high-level metadata such as number of samples, data types and species, or a resource can have a single static page displaying this information.

#### Machine-readable data access requirements

- curato
- Bioschemas


### Examples of controlled access notifications

#### EGA

<!-- https://www.ebi.ac.uk/ega/datasets/EGAD00000000001 -->

#### need second example of access controlled resource - pref entirely access controlled
 





___

## Conclusion:

> Summerize Key Learnings of the recipe.
> 
> Suggest further reading using the following:
>
> #### What should I read next?
> * [A related recipe which nice complements the current one ](TODO)

___
## Authors:

| Name | Affiliation  | orcid | CrediT role  | specific contribution |
| :------------- | :------------- | :------------- |:------------- |:------------- |
| Philippe Rocca-Serra |  University of Oxford, Data Readiness Group| [0000-0001-9853-5668](https://orcid.org/orcid.org/0000-0001-9853-5668) | Writing - Original Draft | original format |
| Danielle Welter |  University of Luxembourg | | Writing - Original draft | | 
| Peter Woollard |  GSK |  | Writing - Original draft |  |
___


## License:

This page is released under the Creative Commons 4.0 BY license.

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
