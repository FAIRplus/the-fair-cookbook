(fcb-help-recipe-template)=
# Mapping of clinical trial data to CDISC-SDTM: a practical example based on APPROACH and ABIRISK


<br/>
<br/>


````{panels_fairplus}
:identifier_text: FCB000
:identifier_link: 'https://w3id.org/faircookbook/FCB000'
:difficulty_level: 3
:recipe_type: applied_example
:reading_time_minutes: 20
:intended_audience: principal_investigator, data_manager, data_scientist, terminology_manager, ontologist
:maturity_level: 3  
:maturity_indicator: 19, 22
:has_executable_code: nope
:recipe_name: Mapping datasets to CDISC-SDTM
```` 


## Main Objectives

This recipe provides a general guide for mapping a clinical trial dataset to CDISC-SDTM using practical examples from two projects, APPROACH and ABIRISK.

The recipe will cover the following elements:

> * Provide a general overview of the challenges of mapping a on-conforming data dictionary to CDISC.

> * Illustrate the mapping process using the above projects.

> * Describe the ETL processes necessary to convert the data to CDISC-SDTM based on the mapped data dictionary.

---


## Graphical Overview

````{dropdown}
:open:
```{figure} approach-cdisc.md-figure0.mmd.png
---
name: approach-cdisc-figure0
alt: Recipe Steps
---
Recipe Steps
```
````


---


## Requirements

* Technical requirements:
   * Knowledge of relational databases is an advantage
   * Fluency in a scripting language such as bash, Python or R
* Knowledge requirement:
   * A thorough understanding of CDISC standards, in particular CDISC-SDTM, is essential
   

---

## FAIRification Objectives, Inputs and Outputs

```{admonition} Important
:class: tip
this section is relied upon by another component developed by FAIRplus to enhance search and presentation. It is therefore important to comply with the layout. 
```

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [validation](http://edamontology.org/operation_2428)  | [Structure Data File (SDF)](https://fairsharing.org/FAIRsharing.ew26v7)  | [report](http://edamontology.org/data_2048)  |
| [calculation](http://edamontology.org/operation_3438)  | [Structure Data File (SDF)](https://fairsharing.org/FAIRsharing.ew26v7) | [InChi](https://fairsharing.org/FAIRsharing.ddk9t9) |
| [calculation](http://edamontology.org/operation_3438)  | [Structure Data File (SDF)](https://fairsharing.org/FAIRsharing.ew26v7)  | [SMILES](https://fairsharing.org/FAIRsharing.qv4b3c)  |
| [text annotation](http://edamontology.org/operation_3778)  | [Human Phenotype Ontology](https://fairsharing.org/FAIRsharing.kbtt7f)  | [annotated text](http://edamontology.org/data_3779)  |


## Table of Data Standards


| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
|  NA |  CDISC terminology | CDISC-SDTM  |

---

## Step-by-step process

* initial review of data dictionary - how is it setup, how many properties, what vocabularies (if any) are used
* assigning of properties to CDISC domains and first pass mapping of each properties
* review of particularly complex properties against data (actual or synthetic) to refine domain and property allocations
* identification of problematic properties - eg value and unit encoded in the same field that need splitting, single property that maps to multiple CDISC properties based on value of another variable or vice-versa
* putting together an ETL template
* implement ETL scripts
* migrate data to CDISC 

* specific problems encountered with mapping APPROACH, eg assumptions based on missing elements that are required in CDISC





---

## Conclusion

> Summerize Key Learnings of the recipe.
> 

### What should I read next?
> * [Ontology mappings?](./tips-tricks.md)
> * [Data dictionary?](./tips-tricks.md)



## References:

````{dropdown} **References**
```{footbibliography}
```
````



## Authors


````{authors_fairplus}
Danielle: Writing - Original Draft
````


## License
````{license_fairplus}
CC-BY-4.0
````

