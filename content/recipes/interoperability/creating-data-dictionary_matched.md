(fcb-interop-datadictionary)=
# Creating data/variable dictionary


````{panels_fairplus}
:identifier_text: FCB025
:identifier_link: https://w3id.org/faircookbook/FCB025
:difficulty_level: 3
:recipe_type: technical_guidance
:reading_time_minutes: 15
:intended_audience: principal_investigator, data_manager, data_scientist 
:maturity_level: 2
:maturity_indicator: 20, 21
:has_executable_code: nope
:recipe_name: Creating a data/variable dictionary
```` 

<!-- # Table of Contents
1. [Main FAIRification Objectives](#Main%20FAIRification%20Objectives)
2. [User Stories](#User%20Stories)
3. [FAIRification Objectives, Inputs and Outputs](#FAIRification%20Objectives,%20Inputs%20and%20Outputs)
4. [An Example of Data Dictionary](#An%20Example%20of%20Data%20Dictionary)
5. [Factors to be considered when building a data dictionary](#Factors%20to%20be%20considered%20when%20building%20a%20data%20dictionary) -->

## Main FAIRification Objectives

A `data dictionary` is a file (or collection (URL_TO_INSERT_TERM_5670 https://fairsharing.org/search?recordType=collection)  of files) which unambiguously declares, defines and annotates all the variables collected in a project (URL_TO_INSERT_TERM_5669 https://fairsharing.org/search?recordType=project)  and associated to a dataset.

Building a `FAIR (URL_TO_INSERT_RECORD_5671 https://fairsharing.org/FAIRsharing.WWI10U)  data dictionary` means delivering a machine-actionable list of variables, thus greatly helping in assessing the **interoperability potential** of a dataset.

Presenting a `FAIR (URL_TO_INSERT_RECORD_5673 https://fairsharing.org/FAIRsharing.WWI10U)  data dictionary template` is also meant to be useful to deal with current [IMI](https://www.imi.europa.eu/) project (URL_TO_INSERT_TERM_5672 https://fairsharing.org/search?recordType=project) s as well as guide future ones.

The main purpose of this recipe is:

> - Provide a guide on what factors should be considered when building a `data dictionary` for data collection (URL_TO_INSERT_TERM_5674 https://fairsharing.org/search?recordType=collection) , data processing and analysis. 
> - Give an example of a data dictionary.
> - Provide an example of machine-actionable data dictionary template.
---

## User Stories

A well defined data dictionary is essential for data curation and analysis. It should contain all informat (URL_TO_INSERT_TERM_5676 https://fairsharing.org/search?recordType=model_and_format) ion needed for data collection (URL_TO_INSERT_TERM_5675 https://fairsharing.org/search?recordType=collection)  and subsequent processing of data.

---

## Graphical overview


````{dropdown} 
:open:
```{figure} creating-data-dictionary.md-figure1.mmd.png
---
width: 1000px
name: creating-data-dictionary-figure1
alt: Data Dictionary
---
Data Dictionary.
```
````

---

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks | Input | Output  |
| :------------- | :------------- | :------------- |
| [text annotation](http://edamontology.org (URL_TO_INSERT_RECORD_5677 https://fairsharing.org/FAIRsharing.a6r7zs) /operation_3778) | list of variables | machine-actionable list of annotated variables |

## Table of Data Standards


| Data Format (URL_TO_INSERT_TERM_5679 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_5680 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_5678 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
| [CDI (URL_TO_INSERT_RECORD_5681 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_5690 https://fairsharing.org/3525)  (URL_TO_INSERT_RECORD_5691 https://fairsharing.org/3525)  SDTM (URL_TO_INSERT_RECORD_5682 https://fairsharing.org/FAIRsharing.s51qk5) ](https://fairsharing.org (URL_TO_INSERT_RECORD_5683 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_5686 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_5692 https://fairsharing.org/3538) /FAIRsharing.s51qk5)  | [schema.org (URL_TO_INSERT_RECORD_5689 https://fairsharing.org/FAIRsharing.hzdzq8) ](https://fairsharing.org (URL_TO_INSERT_RECORD_5684 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_5687 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_5693 https://fairsharing.org/3538) /FAIRsharing.hzdzq8)  |  [OMOP](https://fairsharing.org (URL_TO_INSERT_RECORD_5685 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_5688 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_5694 https://fairsharing.org/3538) /FAIRsharing.qk984b) |
| [CDI (URL_TO_INSERT_RECORD_5695 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_5701 https://fairsharing.org/3525)  (URL_TO_INSERT_RECORD_5702 https://fairsharing.org/3525)  CDASH (URL_TO_INSERT_RECORD_5696 https://fairsharing.org/FAIRsharing.r87bgr) ](https://fairsharing.org (URL_TO_INSERT_RECORD_5697 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_5699 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_5703 https://fairsharing.org/3538) /FAIRsharing.r87bgr)  | [bioschema](https://fairsharing.org (URL_TO_INSERT_RECORD_5698 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_5700 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_5704 https://fairsharing.org/3538) /FAIRsharing.20sbr9)  ||
||[EFO (URL_TO_INSERT_RECORD_5707 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_5708 https://fairsharing.org/FAIRsharing.ca63ce) ](https://fairsharing.org (URL_TO_INSERT_RECORD_5705 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_5706 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_5709 https://fairsharing.org/3538) /FAIRsharing.1gr4tz)||
||[UO (URL_TO_INSERT_RECORD_5710 https://fairsharing.org/FAIRsharing.mjnypw) ](https://fairsharing.org (URL_TO_INSERT_RECORD_5711 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_5712 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_5713 https://fairsharing.org/3538) /FAIRsharing.mjnypw)||
||[EDAM (URL_TO_INSERT_RECORD_5714 https://fairsharing.org/FAIRsharing.a6r7zs) ](https://fairsharing.org (URL_TO_INSERT_RECORD_5715 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_5716 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_5717 https://fairsharing.org/3538) /FAIRsharing.a6r7zs)||




## An Example of Data Dictionary

| File Name            | Variable Name      | Variable Label            | Variable Ontology (URL_TO_INSERT_TERM_5719 https://fairsharing.org/search?recordType=terminology_artefact)  ID or RDF (URL_TO_INSERT_RECORD_5720 https://fairsharing.org/FAIRsharing.p77ph9) type                       | Variable ID Source                        | Variable Statistical Type | Variable Data Type | Variable Size | Max Allowed Value | Min Allowed Value |  Regex      | Allowed Value Shorthands | Allowed Value Descriptions      | Computed Value          | Unique (alone) | Unique (Combined with) | Required | Collection (URL_TO_INSERT_TERM_5718 https://fairsharing.org/search?recordType=collection)  Form Name | Comments                                    |
|----------------------|--------------------|---------------------------|-------------------------------------------------------|--------------------------------------------|---------------------------|--------------------|---------------|-------------------|-------------------| ------------|--------------------------|---------------------------------|-------------------------|----------------|------------------------|----------|----------------------|---------------------------------------------|
| 1\_Subjects.txt      | SUBJECT\_ID        | Subject number            | https://schema.org (URL_TO_INSERT_RECORD_5721 https://fairsharing.org/FAIRsharing.hzdzq8) /identifier | https://schema.org (URL_TO_INSERT_RECORD_5722 https://fairsharing.org/FAIRsharing.hzdzq8)     | categorical variable      | integer            |               |                   |                   |             |                          |                                 |                         | Y              |                        | Y        | FO (URL_TO_INSERT_RECORD_5723 https://fairsharing.org/FAIRsharing.ca63ce) RM 1               |                                             |
| 1\_Subjects.txt      | SP (URL_TO_INSERT_RECORD_5729 https://fairsharing.org/FAIRsharing.s63y3p) E (URL_TO_INSERT_RECORD_5724 https://fairsharing.org/FAIRsharing.b403jy) CIES            | Species name              | https://schema.org (URL_TO_INSERT_RECORD_5726 https://fairsharing.org/FAIRsharing.hzdzq8) /name      | https://schema.org (URL_TO_INSERT_RECORD_5727 https://fairsharing.org/FAIRsharing.hzdzq8)       | categorical variable      | string (URL_TO_INSERT_RECORD_5725 https://fairsharing.org/FAIRsharing.9b7wvk)              |               |                   |                   |            |                          |                                 |                         |                |                        |          | FO (URL_TO_INSERT_RECORD_5728 https://fairsharing.org/FAIRsharing.ca63ce) RM 1               |                                             |
| 1\_Subjects.txt      | STRAIN             | Strain                    | TO (URL_TO_INSERT_RECORD_5730 https://fairsharing.org/FAIRsharing.w69t6r) DO substitute broken link https://bioschemas.org (URL_TO_INSERT_RECORD_5732 https://fairsharing.org/3517) /profiles/Taxon/0.6-RELEASE (URL_TO_INSERT_RECORD_5731 https://fairsharing.org/FAIRsharing.9d574b) /identifier | https://schemas.org/  | categorical variable | string (URL_TO_INSERT_RECORD_5733 https://fairsharing.org/FAIRsharing.9b7wvk)             |               |                   |                   |            |                          | http://purl.obolibrary.org/obo/NCBITaxon_40674 |          |                |                        |          | FO (URL_TO_INSERT_RECORD_5734 https://fairsharing.org/FAIRsharing.ca63ce) RM 1               |                                             |
| 1\_Subjects.txt      | AGE                | Age at study initiation   | https://bioschemas.org (URL_TO_INSERT_RECORD_5735 https://fairsharing.org/3517) /types/BioSample/0.1-RELEASE-2019_06_19 | https://bioschemas.org (URL_TO_INSERT_RECORD_5736 https://fairsharing.org/3517) /   | continuous variable | integer |             |                   |                   |             |                          |                                 |                         |                |                        | Y        | FO (URL_TO_INSERT_RECORD_5737 https://fairsharing.org/FAIRsharing.ca63ce) RM 1               |                                             |
| 1\_Subjects.txt      | AGE\_UNIT          | Age unit                  | http://purl.obolibrary.org/obo/UO_0000003 | http://purl.obolibrary.org/obo/uo   | categorial variable | string (URL_TO_INSERT_RECORD_5738 https://fairsharing.org/FAIRsharing.9b7wvk)  |             |                   |                   |             |                          |                                 |                         |                |                        | Y        | FO (URL_TO_INSERT_RECORD_5739 https://fairsharing.org/FAIRsharing.ca63ce) RM 1               |                                             |
| 1\_Subjects.txt      | SEX                | Sex                       | https://schema.org (URL_TO_INSERT_RECORD_5740 https://fairsharing.org/FAIRsharing.hzdzq8) /gender              | https://schema.org (URL_TO_INSERT_RECORD_5741 https://fairsharing.org/FAIRsharing.hzdzq8)     | categorical variable      | enum               |               |                   |                   |             | M;F                      | M=male;F=female                 |                         |                |                        |          | FO (URL_TO_INSERT_RECORD_5742 https://fairsharing.org/FAIRsharing.ca63ce) RM 1               |                                             |
| 1\_Subjects.txt      | SO (URL_TO_INSERT_RECORD_5744 https://fairsharing.org/FAIRsharing.6bc7h9) ME (URL_TO_INSERT_RECORD_5743 https://fairsharing.org/3502) DATE           | Date of acquiring subject | https://schema.org (URL_TO_INSERT_RECORD_5745 https://fairsharing.org/FAIRsharing.hzdzq8) /dateCreated       | https://schema.org (URL_TO_INSERT_RECORD_5746 https://fairsharing.org/FAIRsharing.hzdzq8)      | ordinal variable          | date               |               |                   |                   | YYYY-MM-DD |                          |                                 |                         |                |                        |          | FO (URL_TO_INSERT_RECORD_5747 https://fairsharing.org/FAIRsharing.ca63ce) RM 1               |                                             |
| 1\_Subjects.txt      | HEMO (URL_TO_INSERT_RECORD_5748 https://fairsharing.org/FAIRsharing.a5e1jd) GLOBI (URL_TO_INSERT_RECORD_5749 https://fairsharing.org/FAIRsharing.284e1z) N         | Hematology: Hemoglobin    | http://www.ebi.ac.uk/efo (URL_TO_INSERT_RECORD_5750 https://fairsharing.org/FAIRsharing.1gr4tz) /EFO_0004509   | http://www.ebi.ac.uk/efo (URL_TO_INSERT_RECORD_5751 https://fairsharing.org/FAIRsharing.1gr4tz)   | continuous variable       | float              | 2,1           | 15.0              | 4.0               |             |                          |                                 |                         |                |                        |          | FO (URL_TO_INSERT_RECORD_5752 https://fairsharing.org/FAIRsharing.ca63ce) RM 1               | Field size denotes "places, decimal places" |
| 1\_Subjects.txt      | HEMO (URL_TO_INSERT_RECORD_5753 https://fairsharing.org/FAIRsharing.a5e1jd) GLOBI (URL_TO_INSERT_RECORD_5754 https://fairsharing.org/FAIRsharing.284e1z) N\_UNIT   | Hemoglobin unit           | http://purl.obolibrary.org/obo/UO_0000003 | http://www.ebi.ac.uk/efo (URL_TO_INSERT_RECORD_5755 https://fairsharing.org/FAIRsharing.1gr4tz)   | categorical variable       | string (URL_TO_INSERT_RECORD_5756 https://fairsharing.org/FAIRsharing.9b7wvk)               |            |               |               |             |                          |                                 |                         |                |                        |          | FO (URL_TO_INSERT_RECORD_5757 https://fairsharing.org/FAIRsharing.ca63ce) RM 1               | Field size denotes "places, decimal places" |
| 1\_Subjects.txt      | HEIGHT             | Body size                 | https://schema.org (URL_TO_INSERT_RECORD_5758 https://fairsharing.org/FAIRsharing.hzdzq8) /height               | https://schema.org (URL_TO_INSERT_RECORD_5759 https://fairsharing.org/FAIRsharing.hzdzq8)      | continuous variable       | float              |               | 2,5               | 0,5               |             |                          |                                 |                         |                |                        |          |                      |                                             |
| 1\_Subjects.txt      | HEIGHT\_UNIT       | Body size unit            | http://purl.obolibrary.org/obo/UO_0000003   | https://schema.org (URL_TO_INSERT_RECORD_5761 https://fairsharing.org/FAIRsharing.hzdzq8)      | categorical variable       | string (URL_TO_INSERT_RECORD_5760 https://fairsharing.org/FAIRsharing.9b7wvk)               |               |               |              |             |                          |                                 |                         |                |                        |          |                      |                                             |
| 1\_Subjects.txt      | WEIGHT             | Body weight               | https://schema.org (URL_TO_INSERT_RECORD_5762 https://fairsharing.org/FAIRsharing.hzdzq8) /weight            | https://schema.org (URL_TO_INSERT_RECORD_5763 https://fairsharing.org/FAIRsharing.hzdzq8)      | continuous variable       | float              |               | 300               | 25                |             |                          |                                 |                         |                |                        |          |                      |                                             |
| 1\_Subjects.txt      | WEIGHT\_UNIT       | Body weight unit          | http://purl.obolibrary.org/obo/UO_0000003  | https://schema.org (URL_TO_INSERT_RECORD_5765 https://fairsharing.org/FAIRsharing.hzdzq8)      | categorical variable       | string (URL_TO_INSERT_RECORD_5764 https://fairsharing.org/FAIRsharing.9b7wvk)               |               |                |                |             |                          |                                 |                         |                |                        |          |                      |                                             |
| 1\_Subjects.txt      | BMI                | Body mass index           | http://www.ebi.ac.uk/efo (URL_TO_INSERT_RECORD_5766 https://fairsharing.org/FAIRsharing.1gr4tz) /EFO_0004340     | http://www.ebi.ac.uk/efo (URL_TO_INSERT_RECORD_5767 https://fairsharing.org/FAIRsharing.1gr4tz)   | continuous variable       | float              |               | 100               | 10                |             |                          |                                 | WEIGHT/(HEIGHT\*HEIGHT) |                |                        |          |                      |                                             |
| 1\_Subjects.txt      | LAB                | Laboratory                | https://schema.org (URL_TO_INSERT_RECORD_5768 https://fairsharing.org/FAIRsharing.hzdzq8) /identifier      | https://schema.org (URL_TO_INSERT_RECORD_5769 https://fairsharing.org/FAIRsharing.hzdzq8)      | categorical variable      | integer            |               |                   |                   |             | 1;2;3                    | 1=LabA;2=UniversityB;3=CompanyC |                         |                |                        |          | FO (URL_TO_INSERT_RECORD_5770 https://fairsharing.org/FAIRsharing.ca63ce) RM 1               |                                             |
| 2\_Samples.txt       | SAM (URL_TO_INSERT_RECORD_5773 https://fairsharing.org/FAIRsharing.k97xzh) P (URL_TO_INSERT_RECORD_5771 https://fairsharing.org/FAIRsharing.kg1x4z)  (URL_TO_INSERT_RECORD_5772 https://fairsharing.org/FAIRsharing.dkKf7I) LE\_ID         | Sample ID                 | https://schema.org (URL_TO_INSERT_RECORD_5775 https://fairsharing.org/FAIRsharing.hzdzq8) /identifier       | https://schema.org (URL_TO_INSERT_RECORD_5776 https://fairsharing.org/FAIRsharing.hzdzq8)      | categorical variable      | string (URL_TO_INSERT_RECORD_5774 https://fairsharing.org/FAIRsharing.9b7wvk)              |               |                   |                   |             |                          |                                 |                         | Y              |                        | Y        | FO (URL_TO_INSERT_RECORD_5777 https://fairsharing.org/FAIRsharing.ca63ce) RM 2               |                                             |
| 2\_Samples.txt       | SAM (URL_TO_INSERT_RECORD_5783 https://fairsharing.org/FAIRsharing.k97xzh) P (URL_TO_INSERT_RECORD_5779 https://fairsharing.org/FAIRsharing.kg1x4z)  (URL_TO_INSERT_RECORD_5780 https://fairsharing.org/FAIRsharing.dkKf7I) LE\_SITE       | Sample collection (URL_TO_INSERT_TERM_5778 https://fairsharing.org/search?recordType=collection)  site    | https://bioschemas.org (URL_TO_INSERT_RECORD_5781 https://fairsharing.org/3517) /types/BioSample/0.1-RELEASE-2019_06_19  | https://bioschemas.org (URL_TO_INSERT_RECORD_5782 https://fairsharing.org/3517) /   | categorical variable | string (URL_TO_INSERT_RECORD_5784 https://fairsharing.org/FAIRsharing.9b7wvk)  |        |                   |                   |             |                          |                                 |                         |                |                        | Y        | FO (URL_TO_INSERT_RECORD_5785 https://fairsharing.org/FAIRsharing.ca63ce) RM 2               |                                             |
| 2\_Samples.txt       | ANALYTE\_TYPE (URL_TO_INSERT_RECORD_5786 https://fairsharing.org/FAIRsharing.b403jy)       | Type of analysis          | http://edamontology.org (URL_TO_INSERT_RECORD_5787 https://fairsharing.org/FAIRsharing.a6r7zs) /operation_2945         | http://edamontology.org (URL_TO_INSERT_RECORD_5788 https://fairsharing.org/FAIRsharing.a6r7zs)    | categorical variable      | string (URL_TO_INSERT_RECORD_5790 https://fairsharing.org/FAIRsharing.9b7wvk)              |               |                   |                   |             |                          | http://edamontology.org (URL_TO_INSERT_RECORD_5789 https://fairsharing.org/FAIRsharing.a6r7zs) /operation_2945 |                  |                |                        | Y        | FO (URL_TO_INSERT_RECORD_5791 https://fairsharing.org/FAIRsharing.ca63ce) RM 2               |                                             |
| 2\_Samples.txt       | GENO (URL_TO_INSERT_RECORD_5792 https://fairsharing.org/FAIRsharing.kpbna7) TYPING\_CENTER | GENO (URL_TO_INSERT_RECORD_5793 https://fairsharing.org/FAIRsharing.kpbna7) TYPING\_CENTER        | https://schema.org (URL_TO_INSERT_RECORD_5795 https://fairsharing.org/FAIRsharing.hzdzq8) /identifier    | https://schema.org (URL_TO_INSERT_RECORD_5796 https://fairsharing.org/FAIRsharing.hzdzq8)      | categorical variable      | string (URL_TO_INSERT_RECORD_5794 https://fairsharing.org/FAIRsharing.9b7wvk)              |               |                   |                   |             |                          |                                 |                         |                |                        |          | FO (URL_TO_INSERT_RECORD_5797 https://fairsharing.org/FAIRsharing.ca63ce) RM 2               |                                             |
| 2\_Samples.txt       | SEQUENCING\_CENTER | SEQUENCING\_CENTER        | https://schema.org (URL_TO_INSERT_RECORD_5799 https://fairsharing.org/FAIRsharing.hzdzq8) /identifier    | https://schema.org (URL_TO_INSERT_RECORD_5800 https://fairsharing.org/FAIRsharing.hzdzq8)      | categorical variable      | string (URL_TO_INSERT_RECORD_5798 https://fairsharing.org/FAIRsharing.9b7wvk)              |               |                   |                   |             |                          |                                 |                         |                |                        |          | FO (URL_TO_INSERT_RECORD_5801 https://fairsharing.org/FAIRsharing.ca63ce) RM 2               |                                             |
| 3\_SampleMap (URL_TO_INSERT_RECORD_5804 https://fairsharing.org/FAIRsharing.53edcc) ping.txt | SUBJECT\_ID        | Subject number            | https://schema.org (URL_TO_INSERT_RECORD_5806 https://fairsharing.org/FAIRsharing.hzdzq8) /identifier                   | https://schema.org (URL_TO_INSERT_RECORD_5807 https://fairsharing.org/FAIRsharing.hzdzq8)      | ordinal variable          | integer            |               |                   |                   |            |                          |                                 |                         |                | SAM (URL_TO_INSERT_RECORD_5805 https://fairsharing.org/FAIRsharing.k97xzh) P (URL_TO_INSERT_RECORD_5802 https://fairsharing.org/FAIRsharing.kg1x4z)  (URL_TO_INSERT_RECORD_5803 https://fairsharing.org/FAIRsharing.dkKf7I) LE\_ID             | Y        | FO (URL_TO_INSERT_RECORD_5808 https://fairsharing.org/FAIRsharing.ca63ce) RM 3               |                                             |
| 3\_SampleMap (URL_TO_INSERT_RECORD_5811 https://fairsharing.org/FAIRsharing.53edcc) ping.txt | SAM (URL_TO_INSERT_RECORD_5812 https://fairsharing.org/FAIRsharing.k97xzh) P (URL_TO_INSERT_RECORD_5809 https://fairsharing.org/FAIRsharing.kg1x4z)  (URL_TO_INSERT_RECORD_5810 https://fairsharing.org/FAIRsharing.dkKf7I) LE\_ID         | Sample ID                 | https://schema.org (URL_TO_INSERT_RECORD_5814 https://fairsharing.org/FAIRsharing.hzdzq8) /identifier         | https://schema.org (URL_TO_INSERT_RECORD_5815 https://fairsharing.org/FAIRsharing.hzdzq8)      | categorical variable      | string (URL_TO_INSERT_RECORD_5813 https://fairsharing.org/FAIRsharing.9b7wvk)              |               |                   |                   |             |                          |                                 |                         |                | SUBJECT\_ID            | Y        | FO (URL_TO_INSERT_RECORD_5816 https://fairsharing.org/FAIRsharing.ca63ce) RM 3               |                                             |                                          |
 
---

## Elements that should be included when building a data dictionary

* **File Name:** The file that contains the annotated variable(s).
* **Variable Name:** Name of the variable (field).
* **Variable Label:** A self explanatory annotation of the variable.
* **Ontology (URL_TO_INSERT_TERM_5818 https://fairsharing.org/search?recordType=terminology_artefact)  or RDF (URL_TO_INSERT_RECORD_5821 https://fairsharing.org/FAIRsharing.p77ph9)  type ID:** A unique identifier (URL_TO_INSERT_TERM_5820 https://fairsharing.org/search?recordType=identifier_schema)  that captures the type of the variable. Semantic types such as schema.org (URL_TO_INSERT_RECORD_5822 https://fairsharing.org/FAIRsharing.hzdzq8)  or ontology (URL_TO_INSERT_TERM_5819 https://fairsharing.org/search?recordType=terminology_artefact)  terms enhance the findability of the data in repositories (URL_TO_INSERT_TERM_5817 https://fairsharing.org/search?recordType=repository) . 
* **ID Source:** The source of the identifier (URL_TO_INSERT_TERM_5823 https://fairsharing.org/search?recordType=identifier_schema)  for the variable. 
* **Variable Data Type:** The type of the variable. It is recommended to use the same type definition as it will be implemented in the data capturing system (e.g. an `xsd:datatype` such as `{date, integer, float, date, string (URL_TO_INSERT_RECORD_5824 https://fairsharing.org/FAIRsharing.9b7wvk) }`).
* **Variable Type:** To unambiguously specify if the data associated with the variable being defined should be treated as a `continuous variable`, ` discrete/polychotomous variable` or an `ordinal variable`.
* **Field Size:** The size (length) of the variable value, e.g. 8 digits, 5,3 (for floating numbers)...
* **Max Allowed Value:** Upper limit of the allowed value.
* **Min Allowed Value:** Lower limit of the allowed value.
* **Regex:** a regular expression allowing input validation in the case the value should follow a certain pattern (e.g. "\d{5}" for a 5-digit `Post Code`).
* **Allowed Values:** Customised list of allowed values (e.g. "M" and "F" for Gender).
* **Allowed Value Description:** Annotation of the list of allowed values (e.g.: M=male;F=female).
* **Computed Value:** If a field is computed based on values from other fields, annotate the calculation rule (e.g BMI=	WEIGHT/(HEIGHT*HEIGHT) ).
* **Unique (alone):** If the value of in a field should be unique (e.g. Subject ID).
* **Unique (combined with):** If the combination of several fields should be unique (e.g. Sample ID and Visit Number).
* **Required:** If the field should NOT allow empty value.
* **Collection (URL_TO_INSERT_TERM_5825 https://fairsharing.org/search?recordType=collection)  Form Name:** Optional, if the field is collected in certain forms (e.g. in Case Report Forms from a clinical trial).
* **Comments:** Optional, for futher informat (URL_TO_INSERT_TERM_5826 https://fairsharing.org/search?recordType=model_and_format) ion.


### What fields to include in a data dictionary?

The right fields to include in a data dictionary are strongly dependent on the needs of the project (URL_TO_INSERT_TERM_5827 https://fairsharing.org/search?recordType=project)  and its context. 
- As a starting point, review existing community standard (URL_TO_INSERT_TERM_5828 https://fairsharing.org/search?fairsharingRegistry=Standard) s or minimum informat (URL_TO_INSERT_TERM_5829 https://fairsharing.org/search?recordType=model_and_format) ion checklists for your subject area to identify recommended fields (see for example recipes on [minimal metadata profiles for transcriptomics metadata](transcriptomics-metadata.md) and [guidance on creating minimal metadata profiles](creating-minimal-metadata-profiles.md)). We recommend consulting three key resources:
    - [FAIRsharing](https://fairsharing.org (URL_TO_INSERT_RECORD_5830 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_5832 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_5834 https://fairsharing.org/3538) ) and in particular the [Minimal Checklists](https://fairsharing.org (URL_TO_INSERT_RECORD_5831 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_5833 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_5835 https://fairsharing.org/3538) /standards/?q=&selected_facets=type_exact:reporting%20guideline&selected_facets=has_publication:false) section 
    - In the context of clinical trial data, get fam (URL_TO_INSERT_RECORD_5837 https://fairsharing.org/FAIRsharing.d0886a) iliar with [CDI (URL_TO_INSERT_RECORD_5836 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_5838 https://fairsharing.org/3525)  (URL_TO_INSERT_RECORD_5839 https://fairsharing.org/3525)  Therapeutic Area](https://www.cdisc.org (URL_TO_INSERT_RECORD_5840 https://fairsharing.org/3525) /standards/therapeutic-areas) annotation profiles
    - the [OHD (URL_TO_INSERT_RECORD_5842 https://fairsharing.org/FAIRsharing.bg7bb6) SI OMOP (URL_TO_INSERT_RECORD_5841 https://fairsharing.org/FAIRsharing.mct09a)  guidelines](https://www.ohdsi.org/resources/tutorials/) to bootstrap efforts and ensure interoperability.

- Make sure you capture all relevant variables for your planned analyses, in particular if you plan any non-standard (URL_TO_INSERT_TERM_5843 https://fairsharing.org/search?fairsharingRegistry=Standard)  or novel analyses. Also, ensure that variables are captured in the correct format (URL_TO_INSERT_TERM_5845 https://fairsharing.org/search?recordType=model_and_format)  (standard (URL_TO_INSERT_TERM_5844 https://fairsharing.org/search?fairsharingRegistry=Standard) ised if appropriate) **in order to minimise the need for transformat (URL_TO_INSERT_TERM_5846 https://fairsharing.org/search?recordType=model_and_format) ions later**.
- Capture variables in the **most atomic form possible** as it is easier to aggregate separate fields into a new, combined value than to extract values from a larger field.
- **Reduce free text use to a minimum** for value-sets associated with qualitative or ordinal variables by providing list of controlled values from standard (URL_TO_INSERT_TERM_5847 https://fairsharing.org/search?fairsharingRegistry=Standard) ised vocabularies (e.g. using NCI Thesaurus (URL_TO_INSERT_RECORD_5849 https://fairsharing.org/FAIRsharing.4cvwxa)  or CDI (URL_TO_INSERT_RECORD_5850 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_5852 https://fairsharing.org/3525)  (URL_TO_INSERT_RECORD_5853 https://fairsharing.org/3525)  vocabulary) suited for the context you operated in (e.g. LOINC (URL_TO_INSERT_RECORD_5851 https://fairsharing.org/FAIRsharing.2mk2zb) , SNOME (URL_TO_INSERT_RECORD_5848 https://fairsharing.org/3502) D-CT in clinical context).
- **Provide unambiguous textual definitions**, ideally through anchoring in semantic markup, for each of the variables so third party users can understand what the variable represents, instead of second-guessed obscure variable shorthands.
- **Provide units**, and where possible, acceptable ranges for continuous variables.
- **Provide regular expressions for input validation** where needed (e.g. expecting an identifier (URL_TO_INSERT_TERM_5854 https://fairsharing.org/search?recordType=identifier_schema)  or a particular reporting pattern)
- **Provide formula** if `derived variables` are computed from `primary variables`


### A note on using standards such as CDISC

Comprehensive standard (URL_TO_INSERT_TERM_5855 https://fairsharing.org/search?fairsharingRegistry=Standard) s such as CDI (URL_TO_INSERT_RECORD_5858 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_5861 https://fairsharing.org/3525)  (URL_TO_INSERT_RECORD_5863 https://fairsharing.org/3525)  offer a complete tabulation model (URL_TO_INSERT_TERM_5857 https://fairsharing.org/search?recordType=model_and_format)  for data capture, consolidation and analysis. CDI (URL_TO_INSERT_RECORD_5859 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_5862 https://fairsharing.org/3525)  (URL_TO_INSERT_RECORD_5864 https://fairsharing.org/3525)  should not be used in a cherrypicking fashion to map (URL_TO_INSERT_RECORD_5860 https://fairsharing.org/FAIRsharing.53edcc)  variables but rather full compliance with the standard (URL_TO_INSERT_TERM_5856 https://fairsharing.org/search?fairsharingRegistry=Standard)  should be ensured, both structurally and in terms of what data is collected.

CDI (URL_TO_INSERT_RECORD_5868 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_5874 https://fairsharing.org/3525)  (URL_TO_INSERT_RECORD_5877 https://fairsharing.org/3525) -compliant datasets group variables slightly differently to the format (URL_TO_INSERT_TERM_5866 https://fairsharing.org/search?recordType=model_and_format)  suggested here. Records are grouped (URL_TO_INSERT_RECORD_5873 https://fairsharing.org/FAIRsharing.31385c)  by `Domain` such as vital signs (VS) and demographics (DM). Records represent one single measurement, so rather than capturing both height and weight in one record, like in the data dictionary here, these would be separate records in the VS domain, with test name (VSTESTC (URL_TO_INSERT_RECORD_5871 https://fairsharing.org/FAIRsharing.RYXNBS) D) height or weight, respectively. CDI (URL_TO_INSERT_RECORD_5869 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_5875 https://fairsharing.org/3525)  (URL_TO_INSERT_RECORD_5878 https://fairsharing.org/3525)  also has a specific way of cross-referencing records, which is not cleanly map (URL_TO_INSERT_RECORD_5872 https://fairsharing.org/FAIRsharing.53edcc) pable to do simpler approach suggested in this sample data dictionary. For further informat (URL_TO_INSERT_TERM_5867 https://fairsharing.org/search?recordType=model_and_format) ion on the CDI (URL_TO_INSERT_RECORD_5870 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_5876 https://fairsharing.org/3525)  (URL_TO_INSERT_RECORD_5879 https://fairsharing.org/3525)  model (URL_TO_INSERT_TERM_5865 https://fairsharing.org/search?recordType=model_and_format) , please visit https://www.cdisc.org (URL_TO_INSERT_RECORD_5880 https://fairsharing.org/3525) /.  

### Indicate how missing values are dealt with:

Data collection (URL_TO_INSERT_TERM_5881 https://fairsharing.org/search?recordType=collection)  is never plain sailing. Patients drop out from studies, animals die, cell cultures or laboratory tests  fail. This results in holes in the datasets. However, without a clear plan to record missing data point unambiguously, empty cells in a record can be the cause of analysis pains.
It is therefore important and good practice to detail in a `data dictionary` what is a legimitate form to indicate a `missing value`, which should be interpreted as `null`.

Depending on the persistence system, how this needs to be specified varies. We provide an example on how to do so in the context of a Frictionless Tabular package. The specifications provide more informat (URL_TO_INSERT_TERM_5882 https://fairsharing.org/search?recordType=model_and_format) ion about how to specify how missing values should look like:

- https://specs.frictionlessdata.io/table-schema/#missing-values

```
"missingValues": [""]
"missingValues": ["-"]
"missingValues": ["NaN", "-"]
```

#### Remember to provide descriptive metadata for the data dictionary itself

- filename (with extension)
- checksum (preferably a SHA2 checksum)
- authors orcid (https://orcid.org (URL_TO_INSERT_RECORD_5883 https://fairsharing.org/FAIRsharing.nx58jg) /0000-0000-0000-00001)
- license url (e.g.)
- version number (semantic version as in `1.0.1`)

#### Remember to provide the data dictionary in an open syntax


## Data Dictionary Mapping in FAIRplus

While the most desirable approach is of course to design a fully FAIR (URL_TO_INSERT_RECORD_5885 https://fairsharing.org/FAIRsharing.WWI10U)  data dictionary at the start of a project (URL_TO_INSERT_TERM_5884 https://fairsharing.org/search?recordType=project) , it is possible to retroactively FAIR (URL_TO_INSERT_RECORD_5886 https://fairsharing.org/FAIRsharing.WWI10U) ify a data dictionary.
The [FAIR (URL_TO_INSERT_RECORD_5888 https://fairsharing.org/FAIRsharing.WWI10U) plus project](https://fairplus-project.eu/) is in the process of working with the [Innovative Medicine Initiative](https://www.imi.europa.eu/) [APPROACH](https://www.approachproject.eu/) and [ABIRISK](http://www.abirisk.eu/) project (URL_TO_INSERT_TERM_5887 https://fairsharing.org/search?recordType=project) s to assist with the FAIR (URL_TO_INSERT_RECORD_5889 https://fairsharing.org/FAIRsharing.WWI10U) ification of their data dictionaries with a view to improving both the findability and interoperability of their datasets.


## Conclusion

This recipe covered an essential output of any research (URL_TO_INSERT_RECORD_5890 https://fairsharing.org/FAIRsharing.52b22c)  program, **namely the documentation of all variables recorded about study subjects and key metadata descriptors used in subsequence analysis in the form of a `data dictionary`**.
The creation and provision of such a `data dictionary` should be a central component of any `data management plan` and should be one of the key deliverable of any IMI project (URL_TO_INSERT_TERM_5891 https://fairsharing.org/search?recordType=project) .
Why? Simply because if affords several key data management processes to take place
- First, it forces `data owners` to carefully structure core (URL_TO_INSERT_RECORD_5893 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_5894 https://fairsharing.org/FAIRsharing.xMmOCL)  metadata and annotation requirements, by spelling out the nature, purpose and constraints on the data collection (URL_TO_INSERT_TERM_5892 https://fairsharing.org/search?recordType=collection) .
- Second, it provides `data owners` the means to communicate about their scientific outputs, without necessarily disclosing the actual data collected over the course of the project (URL_TO_INSERT_TERM_5895 https://fairsharing.org/search?recordType=project) s. It simply brings clarity and removes ambiguity about collected metadata and data. This clarity helps gauge `reusability potential` as well as `interoperability potential` of datasets.
- Thirdl (URL_TO_INSERT_RECORD_5898 https://fairsharing.org/FAIRsharing.vm4688) y, the availability of the `data dictionary` proves extremely useful for any curatorial works, from gearing for an `ETL process`, to planning for map (URL_TO_INSERT_RECORD_5897 https://fairsharing.org/FAIRsharing.53edcc) ping across ontological frameworks. This is especially facilitated if the `data dictionaries` have clearly identified the semantic resources relied upon in a project (URL_TO_INSERT_TERM_5896 https://fairsharing.org/search?recordType=project) .
- Finally, in the context of the [Innovative Medicine Initiative](https://www.imi.europa.eu/), delivering `Data Dictionaries` contributes to making research (URL_TO_INSERT_RECORD_5900 https://fairsharing.org/FAIRsharing.52b22c)  output more FAIR (URL_TO_INSERT_RECORD_5899 https://fairsharing.org/FAIRsharing.WWI10U) .

### What to read next?

- {ref}`fcb-selecting-ontologies (URL_TO_INSERT_TERM_5901 https://fairsharing.org/search?recordType=terminology_artefact) `
- {ref}`fcb-interop-etl`
- Key issues to be aware of when planning [Extract-Transform-Load processes]( TO (URL_TO_INSERT_RECORD_5902 https://fairsharing.org/FAIRsharing.w69t6r) DO add link)

````{rdmkit_panel}
````

> 
<!--
 >- {ref}`fcb-interop-ontomapping` (*in preparation*)
  -->



## Authors

````{authors_fairplus}
Danielle: Writing - Original Draft
Wei: Writing - Original Draft
Philippe: Writing - Original Draft
````



## License

````{license_fairplus}
CC-BY-4.0
````
