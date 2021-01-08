# How to create a FAIR Data/Variable Dictionary


**identifier:** [TBA](TBA)
**version:** [v0.1](v0.1)

___


**_Difficulty level:_** : TBD

**_Reading time:_** 15 minutes

**_Intended Audience:_** Data Scientist, Data Manager

**_Recipe Type_**: TBA 

**_Executable code_**: No

___

<div class="row">

  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-qrcode fa-2x" style="color:#7e0038;"></i>
        <h4><b>Recipe metadata</b></h4>
        <p> identifier: <a href="">TBA</a> </p>
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
        <i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
        <i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
        <i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
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
        <p><i class="fa fa-clock-o fa-lg" style="color:#7e0038;"></i> 15 minutes</p>
        <h4><b>Recipe Type</b></h4>
        <p><i class="fa fa-globe fa-lg" style="color:#7e0038;"></i> Guidance</p>
        <h4><b>Executable Code</b></h4>
        <p><i class="fa fa-play-circle" style="color:#fc7a4a;"></i> No</p>
      </div>
    </div>
  </div>
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-group fa-2x" style="color:#7e0038;"></i>
        <h4><b>Intended Audience</b></h4>
        <p> <i class="fa fa-database fa-lg" style="color:#7e0038;"></i> Data Managers </p>
        <p> <i class="fa fa-wrench fa-lg" style="color:#7e0038;"></i> Data Scientists </p>
<!--         <p> <i class="fa fa-terminal fa-lg" style="color:#7e0038;"></i> System Administrators</p>  -->       
      </div>
    </div>
  </div>
</div>

___


# Table of Contents
1. [Main FAIRification Objectives](#Main%20FAIRification%20Objectives)
2. [User Stories](#User%20Stories)
3. [Capability & Maturity Table](#Capability%20&%20Maturity%20Table)
4. [FAIRification Objectives, Inputs and Outputs](#FAIRification%20Objectives,%20Inputs%20and%20Outputs)
5. [An Example of Data Dictionary](#An%20Example%20of%20Data%20Dictionary)
6. [Factors to be considered when building a data dictionary](#Factors%20to%20be%20considered%20when%20building%20a%20data%20dictionary)

---

## Main FAIRification Objectives

Scope: Based on prior experience with other IMI projects, it is essentail to have a comprehensive data dictionary that annotates all the variables collected in a dataset. Building a FAIR data dictionary template will be useful to deal with current IMI projects as well as guide future ones.

The main purpose of this recipe is:

> Provide a guide on what factors should be considered when building a data dictionary for data collection, data processing and analysis. 
> Give an example of a data dictionary template.
___

## User Stories

When working on data from previous IMI projects, it became apparent that a well defined data dictionary is essential for data curation and analysis. It should contain all information needed for data collection and subsequent processing of data.

## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Interoperability | minimal | repeatable |

----

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks | Input | Output  |
| :------------- | :------------- | :------------- |
| [text annotation](http://edamontology.org/operation_3778) | list of Variables | annotation of the Variables |

## An Example of Data Dictionary

| File Name            | Field Name         | Field Label               | Field Ontology Source | Filed Ontology ID                                   | Field Type | Field Size | Max Allowed Value | Min Allowed Value | Unit   | Regex      | Allowed Values | Allowed Value Description       | Computed Value          | Unique (alone) | Unique (Combined with) | Required | Collection Form Name | Comments                                    |
| -------------------- | ------------------ | ------------------------- | --------------------- | --------------------------------------------------- | ---------- | ---------- | ----------------- | ----------------- | ------ | ---------- | -------------- | ------------------------------- | ----------------------- | -------------- | ---------------------- | -------- | ---------------------- | ------------------------------------------- |
| 1\_Subjects.txt      | SUBJECT\_ID        | Subject number            |                       |                                                     | integer    |            |                   |                   |        |            |                |                                 |                         | Y              |                        | Y        | FORM 1                 |                                             |
| 1\_Subjects.txt      | SPECIES            | Species name              |                       |                                                     | string     |            |                   |                   |        |            |                |                                 |                         |                |                        |          | FORM 1                 |                                             |
| 1\_Subjects.txt      | STRAIN             | Strain                    |                       |                                                     | string     |            |                   |                   |        |            |                |                                 |                         |                |                        |          | FORM 1                 |                                             |
| 1\_Subjects.txt      | AGE                | Age at study initiation   |                       |                                                     | integer    |            |                   |                   | month  |            |                |                                 |                         |                |                        | Y        | FORM 1                 |                                             |
| 1\_Subjects.txt      | SEX                | Sex                       | LOINC                 | http://purl.bioontology.org/ontology/LNC/MTHU002975 | enum       |            |                   |                   |        |            | M;F            | M=male;F=female                 |                         |                |                        |          | FORM 1                 |                                             |
| 1\_Subjects.txt      | SOMEDATE           | Date of acquiring subject |                       |                                                     | date       |            |                   |                   |        | YYYY-MM-DD |                |                                 |                         |                |                        |          | FORM 1                 |                                             |
| 1\_Subjects.txt      | HEMOGLOBIN         | Hematology: Hemoglobin    |                       |                                                     | float      | 2,1        | 15.0              | 4.0               | mmol/l |            |                |                                 |                         |                |                        |          | FORM 1                 | Field size denotes "places, decimal places" |
| 1\_Subjects.txt      | HEIGHT             | Body size                 |                       |                                                     | float      |            | 2,5               | 0,5               | m      |            |                |                                 |                         |                |                        |          |                        |                                             |
| 1\_Subjects.txt      | WEIGHT             | Body weight               |                       |                                                     | float      |            | 300               | 25                | kg     |            |                |                                 |                         |                |                        |          |                        |                                             |
| 1\_Subjects.txt      | BMI                | Body mass index           |                       |                                                     | float      |            | 100               | 10                |        |            |                |                                 | WEIGHT/(HEIGHT\*HEIGHT) |                |                        |          |                        |                                             |
| 1\_Subjects.txt      | LAB                | Laboratory                |                       |                                                     | integer    |            |                   |                   |        |            | 1;2;3          | 1=LabA;2=UniversityB;3=CompanyC |                         |                |                        |          | FORM 1                 |                                             |
| 2\_Samples.txt       | SAMPLE\_ID         | Sample ID                 |                       |                                                     | string     |            |                   |                   |        |            |                |                                 |                         | Y              |                        | Y        | FORM 2                 |                                             |
| 2\_Samples.txt       | SAMPLE\_SITE       | Sample collection site    |                       |                                                     | string     |            |                   |                   |        |            |                |                                 |                         |                |                        | Y        | FORM 2                 |                                             |
| 2\_Samples.txt       | ANALYTE\_TYPE      | Type of analysis          |                       |                                                     | string     |            |                   |                   |        |            |                |                                 |                         |                |                        | Y        | FORM 2                 |                                             |
| 2\_Samples.txt       | GENOTYPING\_CENTER | GENOTYPING\_CENTER        |                       |                                                     | string     |            |                   |                   |        |            |                |                                 |                         |                |                        |          | FORM 2                 |                                             |
| 2\_Samples.txt       | SEQUENCING\_CENTER | SEQUENCING\_CENTER        |                       |                                                     | string     |            |                   |                   |        |            |                |                                 |                         |                |                        |          | FORM 2                 |                                             |
| 3\_SampleMapping.txt | SUBJECT\_ID        | Subject number            |                       |                                                     | integer    |            |                   |                   |        |            |                |                                 |                         |                | SAMPLE\_ID             | Y        | FORM 3                 |                                             |
| 3\_SampleMapping.txt | SAMPLE\_ID         | Sample ID                 |                       |                                                     | string     |            |                   |                   |        |            |                |                                 |                         |                | SUBJECT\_ID            | Y        | FORM 3                 |                                             |

___

## Elements that should be included when building a data dictionary

* **File Name:** The file that contains the the annotated variable(s).
* **Field Name:** Name of the variable (field).
* **Field Label:** A self explanatory annotation of the variable.
* **Field Ontology Source:** If the variable has been mapped to an ontology term, the source of that ontology.
* **Field Ontology ID:** The ontology term ID.
* **Field Type:** The type of the variable. It is recommended to use the same type definition as it will be implemented in the data capturing system.
* **Field Size:** The size (length) of the variable value, e.g. 8 digits, 5,3 (for floating numbers)...
* **Max Allowed Value:** Upper limit of the allowed value.
* **Min Allowed Value:** Lower limit of the allowed value.
* **Unit:** Unit of the value.
* **Regex:** If the value should follow a certain pattern (e.g. "\d{5}" for a 5-digits Post Code).
* **Allowed Values:** Customised list of allowed values (e.g. "M" and "F" for Gender).
* **Allowed Value Description:** Annotation of the list of allowed values (e.g.: M=male;F=female).
* **Computed Value:** If a field is computed based on values from other fields, annotate the calculation rule (e.g BMI=	WEIGHT/(HEIGHT*HEIGHT) ).
* **Unique (alone):** If the value of in a field should be unique (e.g. Subject ID).
* **Unique (combined with):** If the combination of several fields should be unique (e.g. Sample ID and Visit Number).
* **Required:** If the field should NOT allow empty value.
* **Collection Form Name:** Optional, if the field is collected in certain forms (e.g. in Case Report Forms from a clinical trial).
* **Comments:** Optional, for futher information.


### What fields to include in a data dictionary?

The right fields to include in a data dictionary are strongly dependent on the needs of the project. As a starting point, review existing community standards or minimum information checklists for your subject area to identify recommended fields (see for example recipes on [minimal metadata profiles for transcriptomics metadata](transcriptomics-metadata.md) and [guidance on creating minimal metadata profiles](creating-minimal-metadata-profiles.md)). 

Make sure you capture all relevant variables for your planned analyses, in particular if you plan any non-standard or novel analyses. Also ensure that variables are captured in the correct format (standardised if appropriate) in order to minimise the need for transformations later. Capture variables in the most atomised fashion possible as it is easier to aggregate separate fields into a new combined value than to extract values from a larger field.

___



## Authors:

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Wei Gu |  LCSB, University of Luxembourg| [0000-0003-3951-6680](https://orcid.org/0000-0003-3951-6680) | Writing - Original Draft |
| Danielle Welter |  LCSB, University of Luxembourg| [0000-0003-1058-2668](https://orcid.org/0000-0003-1058-2668) | Writing - Original Draft |
| Philippe Rocca-Serra |  University of Oxford, Data Readiness Group| [0000-0001-9853-5668](https://orcid.org/orcid.org/0000-0001-9853-5668) | Writing - Original Draft |

___


## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
