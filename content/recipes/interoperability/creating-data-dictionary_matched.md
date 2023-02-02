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

A `data dictionary` is a file (or collection (URL_TO_INSERT_TERM_5368 https://fairsharing.org/search?recordType=collection)  of files) which unambiguously declares, defines and annotates all the variables collected in a project (URL_TO_INSERT_TERM_5367 https://fairsharing.org/search?recordType=project)  and associated to a dataset.

Building a `FAIR (URL_TO_INSERT_RECORD_5369 https://fairsharing.org/FAIRsharing.WWI10U)  data dictionary` means delivering a machine-actionable list of variables, thus greatly helping in assessing the **interoperability potential** of a dataset.

Presenting a `FAIR (URL_TO_INSERT_RECORD_5371 https://fairsharing.org/FAIRsharing.WWI10U)  data dictionary template` is also meant to be useful to deal with current [IMI](https://www.imi.europa.eu/) project (URL_TO_INSERT_TERM_5370 https://fairsharing.org/search?recordType=project) s as well as guide future ones.

The main purpose of this recipe is:

> - Provide a guide on what factors should be considered when building a `data dictionary` for data collection (URL_TO_INSERT_TERM_5372 https://fairsharing.org/search?recordType=collection) , data processing and analysis. 
> - Give an example of a data dictionary.
> - Provide an example of machine-actionable data dictionary template.
---

## User Stories

A well defined data dictionary is essential for data curation and analysis. It should contain all informat (URL_TO_INSERT_TERM_5374 https://fairsharing.org/search?recordType=model_and_format) ion needed for data collection (URL_TO_INSERT_TERM_5373 https://fairsharing.org/search?recordType=collection)  and subsequent processing of data.

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
| [text annotation](http://edamontology.org (URL_TO_INSERT_RECORD_5375 https://fairsharing.org/FAIRsharing.a6r7zs) /operation_3778) | list of variables | machine-actionable list of annotated variables |

## Table of Data Standards


| Data Format (URL_TO_INSERT_TERM_5377 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_5378 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_5376 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
| [CDI (URL_TO_INSERT_RECORD_5379 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_5388 https://fairsharing.org/3525)  SDTM (URL_TO_INSERT_RECORD_5380 https://fairsharing.org/FAIRsharing.s51qk5) ](https://fairsharing.org (URL_TO_INSERT_RECORD_5381 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_5384 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_5389 https://fairsharing.org/3538) /FAIRsharing.s51qk5)  | [schema.org (URL_TO_INSERT_RECORD_5387 https://fairsharing.org/FAIRsharing.hzdzq8) ](https://fairsharing.org (URL_TO_INSERT_RECORD_5382 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_5385 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_5390 https://fairsharing.org/3538) /FAIRsharing.hzdzq8)  |  [OMOP](https://fairsharing.org (URL_TO_INSERT_RECORD_5383 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_5386 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_5391 https://fairsharing.org/3538) /FAIRsharing.qk984b) |
| [CDI (URL_TO_INSERT_RECORD_5392 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_5398 https://fairsharing.org/3525)  CDASH (URL_TO_INSERT_RECORD_5393 https://fairsharing.org/FAIRsharing.r87bgr) ](https://fairsharing.org (URL_TO_INSERT_RECORD_5394 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_5396 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_5399 https://fairsharing.org/3538) /FAIRsharing.r87bgr)  | [bioschema](https://fairsharing.org (URL_TO_INSERT_RECORD_5395 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_5397 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_5400 https://fairsharing.org/3538) /FAIRsharing.20sbr9)  ||
||[EFO (URL_TO_INSERT_RECORD_5403 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_5404 https://fairsharing.org/FAIRsharing.ca63ce) ](https://fairsharing.org (URL_TO_INSERT_RECORD_5401 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_5402 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_5405 https://fairsharing.org/3538) /FAIRsharing.1gr4tz)||
||[UO (URL_TO_INSERT_RECORD_5406 https://fairsharing.org/FAIRsharing.mjnypw) ](https://fairsharing.org (URL_TO_INSERT_RECORD_5407 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_5408 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_5409 https://fairsharing.org/3538) /FAIRsharing.mjnypw)||
||[EDAM (URL_TO_INSERT_RECORD_5410 https://fairsharing.org/FAIRsharing.a6r7zs) ](https://fairsharing.org (URL_TO_INSERT_RECORD_5411 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_5412 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_5413 https://fairsharing.org/3538) /FAIRsharing.a6r7zs)||




## An Example of Data Dictionary

| File Name            | Variable Name      | Variable Label            | Variable Ontology (URL_TO_INSERT_TERM_5415 https://fairsharing.org/search?recordType=terminology_artefact)  ID or RDF (URL_TO_INSERT_RECORD_5416 https://fairsharing.org/FAIRsharing.p77ph9) type                       | Variable ID Source                        | Variable Statistical Type | Variable Data Type | Variable Size | Max Allowed Value | Min Allowed Value |  Regex      | Allowed Value Shorthands | Allowed Value Descriptions      | Computed Value          | Unique (alone) | Unique (Combined with) | Required | Collection (URL_TO_INSERT_TERM_5414 https://fairsharing.org/search?recordType=collection)  Form Name | Comments                                    |
|----------------------|--------------------|---------------------------|-------------------------------------------------------|--------------------------------------------|---------------------------|--------------------|---------------|-------------------|-------------------| ------------|--------------------------|---------------------------------|-------------------------|----------------|------------------------|----------|----------------------|---------------------------------------------|
| 1\_Subjects.txt      | SUBJECT\_ID        | Subject number            | https://schema.org (URL_TO_INSERT_RECORD_5417 https://fairsharing.org/FAIRsharing.hzdzq8) /identifier | https://schema.org (URL_TO_INSERT_RECORD_5418 https://fairsharing.org/FAIRsharing.hzdzq8)     | categorical variable      | integer            |               |                   |                   |             |                          |                                 |                         | Y              |                        | Y        | FO (URL_TO_INSERT_RECORD_5419 https://fairsharing.org/FAIRsharing.ca63ce) RM 1               |                                             |
| 1\_Subjects.txt      | SP (URL_TO_INSERT_RECORD_5425 https://fairsharing.org/FAIRsharing.s63y3p) E (URL_TO_INSERT_RECORD_5420 https://fairsharing.org/FAIRsharing.b403jy) CIES            | Species name              | https://schema.org (URL_TO_INSERT_RECORD_5422 https://fairsharing.org/FAIRsharing.hzdzq8) /name      | https://schema.org (URL_TO_INSERT_RECORD_5423 https://fairsharing.org/FAIRsharing.hzdzq8)       | categorical variable      | string (URL_TO_INSERT_RECORD_5421 https://fairsharing.org/FAIRsharing.9b7wvk)              |               |                   |                   |            |                          |                                 |                         |                |                        |          | FO (URL_TO_INSERT_RECORD_5424 https://fairsharing.org/FAIRsharing.ca63ce) RM 1               |                                             |
| 1\_Subjects.txt      | STRAIN             | Strain                    | TO (URL_TO_INSERT_RECORD_5426 https://fairsharing.org/FAIRsharing.w69t6r) DO substitute broken link https://bioschemas.org (URL_TO_INSERT_RECORD_5428 https://fairsharing.org/3517) /profiles/Taxon/0.6-RELEASE (URL_TO_INSERT_RECORD_5427 https://fairsharing.org/FAIRsharing.9d574b) /identifier | https://schemas.org/  | categorical variable | string (URL_TO_INSERT_RECORD_5429 https://fairsharing.org/FAIRsharing.9b7wvk)             |               |                   |                   |            |                          | http://purl.obolibrary.org/obo/NCBITaxon_40674 |          |                |                        |          | FO (URL_TO_INSERT_RECORD_5430 https://fairsharing.org/FAIRsharing.ca63ce) RM 1               |                                             |
| 1\_Subjects.txt      | AGE                | Age at study initiation   | https://bioschemas.org (URL_TO_INSERT_RECORD_5431 https://fairsharing.org/3517) /types/BioSample/0.1-RELEASE-2019_06_19 | https://bioschemas.org (URL_TO_INSERT_RECORD_5432 https://fairsharing.org/3517) /   | continuous variable | integer |             |                   |                   |             |                          |                                 |                         |                |                        | Y        | FO (URL_TO_INSERT_RECORD_5433 https://fairsharing.org/FAIRsharing.ca63ce) RM 1               |                                             |
| 1\_Subjects.txt      | AGE\_UNIT          | Age unit                  | http://purl.obolibrary.org/obo/UO_0000003 | http://purl.obolibrary.org/obo/uo   | categorial variable | string (URL_TO_INSERT_RECORD_5434 https://fairsharing.org/FAIRsharing.9b7wvk)  |             |                   |                   |             |                          |                                 |                         |                |                        | Y        | FO (URL_TO_INSERT_RECORD_5435 https://fairsharing.org/FAIRsharing.ca63ce) RM 1               |                                             |
| 1\_Subjects.txt      | SEX                | Sex                       | https://schema.org (URL_TO_INSERT_RECORD_5436 https://fairsharing.org/FAIRsharing.hzdzq8) /gender              | https://schema.org (URL_TO_INSERT_RECORD_5437 https://fairsharing.org/FAIRsharing.hzdzq8)     | categorical variable      | enum               |               |                   |                   |             | M;F                      | M=male;F=female                 |                         |                |                        |          | FO (URL_TO_INSERT_RECORD_5438 https://fairsharing.org/FAIRsharing.ca63ce) RM 1               |                                             |
| 1\_Subjects.txt      | SO (URL_TO_INSERT_RECORD_5440 https://fairsharing.org/FAIRsharing.6bc7h9) ME (URL_TO_INSERT_RECORD_5439 https://fairsharing.org/3502) DATE           | Date of acquiring subject | https://schema.org (URL_TO_INSERT_RECORD_5441 https://fairsharing.org/FAIRsharing.hzdzq8) /dateCreated       | https://schema.org (URL_TO_INSERT_RECORD_5442 https://fairsharing.org/FAIRsharing.hzdzq8)      | ordinal variable          | date               |               |                   |                   | YYYY-MM-DD |                          |                                 |                         |                |                        |          | FO (URL_TO_INSERT_RECORD_5443 https://fairsharing.org/FAIRsharing.ca63ce) RM 1               |                                             |
| 1\_Subjects.txt      | HEMO (URL_TO_INSERT_RECORD_5444 https://fairsharing.org/FAIRsharing.a5e1jd) GLOBI (URL_TO_INSERT_RECORD_5445 https://fairsharing.org/FAIRsharing.284e1z) N         | Hematology: Hemoglobin    | http://www.ebi.ac.uk/efo (URL_TO_INSERT_RECORD_5446 https://fairsharing.org/FAIRsharing.1gr4tz) /EFO_0004509   | http://www.ebi.ac.uk/efo (URL_TO_INSERT_RECORD_5447 https://fairsharing.org/FAIRsharing.1gr4tz)   | continuous variable       | float              | 2,1           | 15.0              | 4.0               |             |                          |                                 |                         |                |                        |          | FO (URL_TO_INSERT_RECORD_5448 https://fairsharing.org/FAIRsharing.ca63ce) RM 1               | Field size denotes "places, decimal places" |
| 1\_Subjects.txt      | HEMO (URL_TO_INSERT_RECORD_5449 https://fairsharing.org/FAIRsharing.a5e1jd) GLOBI (URL_TO_INSERT_RECORD_5450 https://fairsharing.org/FAIRsharing.284e1z) N\_UNIT   | Hemoglobin unit           | http://purl.obolibrary.org/obo/UO_0000003 | http://www.ebi.ac.uk/efo (URL_TO_INSERT_RECORD_5451 https://fairsharing.org/FAIRsharing.1gr4tz)   | categorical variable       | string (URL_TO_INSERT_RECORD_5452 https://fairsharing.org/FAIRsharing.9b7wvk)               |            |               |               |             |                          |                                 |                         |                |                        |          | FO (URL_TO_INSERT_RECORD_5453 https://fairsharing.org/FAIRsharing.ca63ce) RM 1               | Field size denotes "places, decimal places" |
| 1\_Subjects.txt      | HEIGHT             | Body size                 | https://schema.org (URL_TO_INSERT_RECORD_5454 https://fairsharing.org/FAIRsharing.hzdzq8) /height               | https://schema.org (URL_TO_INSERT_RECORD_5455 https://fairsharing.org/FAIRsharing.hzdzq8)      | continuous variable       | float              |               | 2,5               | 0,5               |             |                          |                                 |                         |                |                        |          |                      |                                             |
| 1\_Subjects.txt      | HEIGHT\_UNIT       | Body size unit            | http://purl.obolibrary.org/obo/UO_0000003   | https://schema.org (URL_TO_INSERT_RECORD_5457 https://fairsharing.org/FAIRsharing.hzdzq8)      | categorical variable       | string (URL_TO_INSERT_RECORD_5456 https://fairsharing.org/FAIRsharing.9b7wvk)               |               |               |              |             |                          |                                 |                         |                |                        |          |                      |                                             |
| 1\_Subjects.txt      | WEIGHT             | Body weight               | https://schema.org (URL_TO_INSERT_RECORD_5458 https://fairsharing.org/FAIRsharing.hzdzq8) /weight            | https://schema.org (URL_TO_INSERT_RECORD_5459 https://fairsharing.org/FAIRsharing.hzdzq8)      | continuous variable       | float              |               | 300               | 25                |             |                          |                                 |                         |                |                        |          |                      |                                             |
| 1\_Subjects.txt      | WEIGHT\_UNIT       | Body weight unit          | http://purl.obolibrary.org/obo/UO_0000003  | https://schema.org (URL_TO_INSERT_RECORD_5461 https://fairsharing.org/FAIRsharing.hzdzq8)      | categorical variable       | string (URL_TO_INSERT_RECORD_5460 https://fairsharing.org/FAIRsharing.9b7wvk)               |               |                |                |             |                          |                                 |                         |                |                        |          |                      |                                             |
| 1\_Subjects.txt      | BMI                | Body mass index           | http://www.ebi.ac.uk/efo (URL_TO_INSERT_RECORD_5462 https://fairsharing.org/FAIRsharing.1gr4tz) /EFO_0004340     | http://www.ebi.ac.uk/efo (URL_TO_INSERT_RECORD_5463 https://fairsharing.org/FAIRsharing.1gr4tz)   | continuous variable       | float              |               | 100               | 10                |             |                          |                                 | WEIGHT/(HEIGHT\*HEIGHT) |                |                        |          |                      |                                             |
| 1\_Subjects.txt      | LAB                | Laboratory                | https://schema.org (URL_TO_INSERT_RECORD_5464 https://fairsharing.org/FAIRsharing.hzdzq8) /identifier      | https://schema.org (URL_TO_INSERT_RECORD_5465 https://fairsharing.org/FAIRsharing.hzdzq8)      | categorical variable      | integer            |               |                   |                   |             | 1;2;3                    | 1=LabA;2=UniversityB;3=CompanyC |                         |                |                        |          | FO (URL_TO_INSERT_RECORD_5466 https://fairsharing.org/FAIRsharing.ca63ce) RM 1               |                                             |
| 2\_Samples.txt       | SAM (URL_TO_INSERT_RECORD_5469 https://fairsharing.org/FAIRsharing.k97xzh) P (URL_TO_INSERT_RECORD_5467 https://fairsharing.org/FAIRsharing.kg1x4z)  (URL_TO_INSERT_RECORD_5468 https://fairsharing.org/FAIRsharing.dkKf7I) LE\_ID         | Sample ID                 | https://schema.org (URL_TO_INSERT_RECORD_5471 https://fairsharing.org/FAIRsharing.hzdzq8) /identifier       | https://schema.org (URL_TO_INSERT_RECORD_5472 https://fairsharing.org/FAIRsharing.hzdzq8)      | categorical variable      | string (URL_TO_INSERT_RECORD_5470 https://fairsharing.org/FAIRsharing.9b7wvk)              |               |                   |                   |             |                          |                                 |                         | Y              |                        | Y        | FO (URL_TO_INSERT_RECORD_5473 https://fairsharing.org/FAIRsharing.ca63ce) RM 2               |                                             |
| 2\_Samples.txt       | SAM (URL_TO_INSERT_RECORD_5479 https://fairsharing.org/FAIRsharing.k97xzh) P (URL_TO_INSERT_RECORD_5475 https://fairsharing.org/FAIRsharing.kg1x4z)  (URL_TO_INSERT_RECORD_5476 https://fairsharing.org/FAIRsharing.dkKf7I) LE\_SITE       | Sample collection (URL_TO_INSERT_TERM_5474 https://fairsharing.org/search?recordType=collection)  site    | https://bioschemas.org (URL_TO_INSERT_RECORD_5477 https://fairsharing.org/3517) /types/BioSample/0.1-RELEASE-2019_06_19  | https://bioschemas.org (URL_TO_INSERT_RECORD_5478 https://fairsharing.org/3517) /   | categorical variable | string (URL_TO_INSERT_RECORD_5480 https://fairsharing.org/FAIRsharing.9b7wvk)  |        |                   |                   |             |                          |                                 |                         |                |                        | Y        | FO (URL_TO_INSERT_RECORD_5481 https://fairsharing.org/FAIRsharing.ca63ce) RM 2               |                                             |
| 2\_Samples.txt       | ANALYTE\_TYPE (URL_TO_INSERT_RECORD_5482 https://fairsharing.org/FAIRsharing.b403jy)       | Type of analysis          | http://edamontology.org (URL_TO_INSERT_RECORD_5483 https://fairsharing.org/FAIRsharing.a6r7zs) /operation_2945         | http://edamontology.org (URL_TO_INSERT_RECORD_5484 https://fairsharing.org/FAIRsharing.a6r7zs)    | categorical variable      | string (URL_TO_INSERT_RECORD_5486 https://fairsharing.org/FAIRsharing.9b7wvk)              |               |                   |                   |             |                          | http://edamontology.org (URL_TO_INSERT_RECORD_5485 https://fairsharing.org/FAIRsharing.a6r7zs) /operation_2945 |                  |                |                        | Y        | FO (URL_TO_INSERT_RECORD_5487 https://fairsharing.org/FAIRsharing.ca63ce) RM 2               |                                             |
| 2\_Samples.txt       | GENO (URL_TO_INSERT_RECORD_5488 https://fairsharing.org/FAIRsharing.kpbna7) TYPING\_CENTER | GENO (URL_TO_INSERT_RECORD_5489 https://fairsharing.org/FAIRsharing.kpbna7) TYPING\_CENTER        | https://schema.org (URL_TO_INSERT_RECORD_5491 https://fairsharing.org/FAIRsharing.hzdzq8) /identifier    | https://schema.org (URL_TO_INSERT_RECORD_5492 https://fairsharing.org/FAIRsharing.hzdzq8)      | categorical variable      | string (URL_TO_INSERT_RECORD_5490 https://fairsharing.org/FAIRsharing.9b7wvk)              |               |                   |                   |             |                          |                                 |                         |                |                        |          | FO (URL_TO_INSERT_RECORD_5493 https://fairsharing.org/FAIRsharing.ca63ce) RM 2               |                                             |
| 2\_Samples.txt       | SEQUENCING\_CENTER | SEQUENCING\_CENTER        | https://schema.org (URL_TO_INSERT_RECORD_5495 https://fairsharing.org/FAIRsharing.hzdzq8) /identifier    | https://schema.org (URL_TO_INSERT_RECORD_5496 https://fairsharing.org/FAIRsharing.hzdzq8)      | categorical variable      | string (URL_TO_INSERT_RECORD_5494 https://fairsharing.org/FAIRsharing.9b7wvk)              |               |                   |                   |             |                          |                                 |                         |                |                        |          | FO (URL_TO_INSERT_RECORD_5497 https://fairsharing.org/FAIRsharing.ca63ce) RM 2               |                                             |
| 3\_SampleMap (URL_TO_INSERT_RECORD_5500 https://fairsharing.org/FAIRsharing.53edcc) ping.txt | SUBJECT\_ID        | Subject number            | https://schema.org (URL_TO_INSERT_RECORD_5502 https://fairsharing.org/FAIRsharing.hzdzq8) /identifier                   | https://schema.org (URL_TO_INSERT_RECORD_5503 https://fairsharing.org/FAIRsharing.hzdzq8)      | ordinal variable          | integer            |               |                   |                   |            |                          |                                 |                         |                | SAM (URL_TO_INSERT_RECORD_5501 https://fairsharing.org/FAIRsharing.k97xzh) P (URL_TO_INSERT_RECORD_5498 https://fairsharing.org/FAIRsharing.kg1x4z)  (URL_TO_INSERT_RECORD_5499 https://fairsharing.org/FAIRsharing.dkKf7I) LE\_ID             | Y        | FO (URL_TO_INSERT_RECORD_5504 https://fairsharing.org/FAIRsharing.ca63ce) RM 3               |                                             |
| 3\_SampleMap (URL_TO_INSERT_RECORD_5507 https://fairsharing.org/FAIRsharing.53edcc) ping.txt | SAM (URL_TO_INSERT_RECORD_5508 https://fairsharing.org/FAIRsharing.k97xzh) P (URL_TO_INSERT_RECORD_5505 https://fairsharing.org/FAIRsharing.kg1x4z)  (URL_TO_INSERT_RECORD_5506 https://fairsharing.org/FAIRsharing.dkKf7I) LE\_ID         | Sample ID                 | https://schema.org (URL_TO_INSERT_RECORD_5510 https://fairsharing.org/FAIRsharing.hzdzq8) /identifier         | https://schema.org (URL_TO_INSERT_RECORD_5511 https://fairsharing.org/FAIRsharing.hzdzq8)      | categorical variable      | string (URL_TO_INSERT_RECORD_5509 https://fairsharing.org/FAIRsharing.9b7wvk)              |               |                   |                   |             |                          |                                 |                         |                | SUBJECT\_ID            | Y        | FO (URL_TO_INSERT_RECORD_5512 https://fairsharing.org/FAIRsharing.ca63ce) RM 3               |                                             |                                          |
 
---

## Elements that should be included when building a data dictionary

* **File Name:** The file that contains the annotated variable(s).
* **Variable Name:** Name of the variable (field).
* **Variable Label:** A self explanatory annotation of the variable.
* **Ontology (URL_TO_INSERT_TERM_5514 https://fairsharing.org/search?recordType=terminology_artefact)  or RDF (URL_TO_INSERT_RECORD_5517 https://fairsharing.org/FAIRsharing.p77ph9)  type ID:** A unique identifier (URL_TO_INSERT_TERM_5516 https://fairsharing.org/search?recordType=identifier_schema)  that captures the type of the variable. Semantic types such as schema.org (URL_TO_INSERT_RECORD_5518 https://fairsharing.org/FAIRsharing.hzdzq8)  or ontology (URL_TO_INSERT_TERM_5515 https://fairsharing.org/search?recordType=terminology_artefact)  terms enhance the findability of the data in repositories (URL_TO_INSERT_TERM_5513 https://fairsharing.org/search?recordType=repository) . 
* **ID Source:** The source of the identifier (URL_TO_INSERT_TERM_5519 https://fairsharing.org/search?recordType=identifier_schema)  for the variable. 
* **Variable Data Type:** The type of the variable. It is recommended to use the same type definition as it will be implemented in the data capturing system (e.g. an `xsd:datatype` such as `{date, integer, float, date, string (URL_TO_INSERT_RECORD_5520 https://fairsharing.org/FAIRsharing.9b7wvk) }`).
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
* **Collection (URL_TO_INSERT_TERM_5521 https://fairsharing.org/search?recordType=collection)  Form Name:** Optional, if the field is collected in certain forms (e.g. in Case Report Forms from a clinical trial).
* **Comments:** Optional, for futher informat (URL_TO_INSERT_TERM_5522 https://fairsharing.org/search?recordType=model_and_format) ion.


### What fields to include in a data dictionary?

The right fields to include in a data dictionary are strongly dependent on the needs of the project (URL_TO_INSERT_TERM_5523 https://fairsharing.org/search?recordType=project)  and its context. 
- As a starting point, review existing community standard (URL_TO_INSERT_TERM_5524 https://fairsharing.org/search?fairsharingRegistry=Standard) s or minimum informat (URL_TO_INSERT_TERM_5525 https://fairsharing.org/search?recordType=model_and_format) ion checklists for your subject area to identify recommended fields (see for example recipes on [minimal metadata profiles for transcriptomics metadata](transcriptomics-metadata.md) and [guidance on creating minimal metadata profiles](creating-minimal-metadata-profiles.md)). We recommend consulting three key resources:
    - [FAIRsharing](https://fairsharing.org (URL_TO_INSERT_RECORD_5526 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_5528 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_5530 https://fairsharing.org/3538) ) and in particular the [Minimal Checklists](https://fairsharing.org (URL_TO_INSERT_RECORD_5527 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_5529 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_5531 https://fairsharing.org/3538) /standards/?q=&selected_facets=type_exact:reporting%20guideline&selected_facets=has_publication:false) section 
    - In the context of clinical trial data, get fam (URL_TO_INSERT_RECORD_5533 https://fairsharing.org/FAIRsharing.d0886a) iliar with [CDI (URL_TO_INSERT_RECORD_5532 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_5534 https://fairsharing.org/3525)  Therapeutic Area](https://www.cdisc.org (URL_TO_INSERT_RECORD_5535 https://fairsharing.org/3525) /standards/therapeutic-areas) annotation profiles
    - the [OHD (URL_TO_INSERT_RECORD_5537 https://fairsharing.org/FAIRsharing.bg7bb6) SI OMOP (URL_TO_INSERT_RECORD_5536 https://fairsharing.org/FAIRsharing.mct09a)  guidelines](https://www.ohdsi.org/resources/tutorials/) to bootstrap efforts and ensure interoperability.

- Make sure you capture all relevant variables for your planned analyses, in particular if you plan any non-standard (URL_TO_INSERT_TERM_5538 https://fairsharing.org/search?fairsharingRegistry=Standard)  or novel analyses. Also, ensure that variables are captured in the correct format (URL_TO_INSERT_TERM_5540 https://fairsharing.org/search?recordType=model_and_format)  (standard (URL_TO_INSERT_TERM_5539 https://fairsharing.org/search?fairsharingRegistry=Standard) ised if appropriate) **in order to minimise the need for transformat (URL_TO_INSERT_TERM_5541 https://fairsharing.org/search?recordType=model_and_format) ions later**.
- Capture variables in the **most atomic form possible** as it is easier to aggregate separate fields into a new, combined value than to extract values from a larger field.
- **Reduce free text use to a minimum** for value-sets associated with qualitative or ordinal variables by providing list of controlled values from standard (URL_TO_INSERT_TERM_5542 https://fairsharing.org/search?fairsharingRegistry=Standard) ised vocabularies (e.g. using NCI Thesaurus (URL_TO_INSERT_RECORD_5544 https://fairsharing.org/FAIRsharing.4cvwxa)  or CDI (URL_TO_INSERT_RECORD_5545 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_5547 https://fairsharing.org/3525)  vocabulary) suited for the context you operated in (e.g. LOINC (URL_TO_INSERT_RECORD_5546 https://fairsharing.org/FAIRsharing.2mk2zb) , SNOME (URL_TO_INSERT_RECORD_5543 https://fairsharing.org/3502) D-CT in clinical context).
- **Provide unambiguous textual definitions**, ideally through anchoring in semantic markup, for each of the variables so third party users can understand what the variable represents, instead of second-guessed obscure variable shorthands.
- **Provide units**, and where possible, acceptable ranges for continuous variables.
- **Provide regular expressions for input validation** where needed (e.g. expecting an identifier (URL_TO_INSERT_TERM_5548 https://fairsharing.org/search?recordType=identifier_schema)  or a particular reporting pattern)
- **Provide formula** if `derived variables` are computed from `primary variables`


### A note on using standards such as CDISC

Comprehensive standard (URL_TO_INSERT_TERM_5549 https://fairsharing.org/search?fairsharingRegistry=Standard) s such as CDI (URL_TO_INSERT_RECORD_5552 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_5555 https://fairsharing.org/3525)  offer a complete tabulation model (URL_TO_INSERT_TERM_5551 https://fairsharing.org/search?recordType=model_and_format)  for data capture, consolidation and analysis. CDI (URL_TO_INSERT_RECORD_5553 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_5556 https://fairsharing.org/3525)  should not be used in a cherrypicking fashion to map (URL_TO_INSERT_RECORD_5554 https://fairsharing.org/FAIRsharing.53edcc)  variables but rather full compliance with the standard (URL_TO_INSERT_TERM_5550 https://fairsharing.org/search?fairsharingRegistry=Standard)  should be ensured, both structurally and in terms of what data is collected.

CDI (URL_TO_INSERT_RECORD_5560 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_5566 https://fairsharing.org/3525) -compliant datasets group variables slightly differently to the format (URL_TO_INSERT_TERM_5558 https://fairsharing.org/search?recordType=model_and_format)  suggested here. Records are grouped (URL_TO_INSERT_RECORD_5565 https://fairsharing.org/FAIRsharing.31385c)  by `Domain` such as vital signs (VS) and demographics (DM). Records represent one single measurement, so rather than capturing both height and weight in one record, like in the data dictionary here, these would be separate records in the VS domain, with test name (VSTESTC (URL_TO_INSERT_RECORD_5563 https://fairsharing.org/FAIRsharing.RYXNBS) D) height or weight, respectively. CDI (URL_TO_INSERT_RECORD_5561 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_5567 https://fairsharing.org/3525)  also has a specific way of cross-referencing records, which is not cleanly map (URL_TO_INSERT_RECORD_5564 https://fairsharing.org/FAIRsharing.53edcc) pable to do simpler approach suggested in this sample data dictionary. For further informat (URL_TO_INSERT_TERM_5559 https://fairsharing.org/search?recordType=model_and_format) ion on the CDI (URL_TO_INSERT_RECORD_5562 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_5568 https://fairsharing.org/3525)  model (URL_TO_INSERT_TERM_5557 https://fairsharing.org/search?recordType=model_and_format) , please visit https://www.cdisc.org (URL_TO_INSERT_RECORD_5569 https://fairsharing.org/3525) /.  

### Indicate how missing values are dealt with:

Data collection (URL_TO_INSERT_TERM_5570 https://fairsharing.org/search?recordType=collection)  is never plain sailing. Patients drop out from studies, animals die, cell cultures or laboratory tests  fail. This results in holes in the datasets. However, without a clear plan to record missing data point unambiguously, empty cells in a record can be the cause of analysis pains.
It is therefore important and good practice to detail in a `data dictionary` what is a legimitate form to indicate a `missing value`, which should be interpreted as `null`.

Depending on the persistence system, how this needs to be specified varies. We provide an example on how to do so in the context of a Frictionless Tabular package. The specifications provide more informat (URL_TO_INSERT_TERM_5571 https://fairsharing.org/search?recordType=model_and_format) ion about how to specify how missing values should look like:

- https://specs.frictionlessdata.io/table-schema/#missing-values

```
"missingValues": [""]
"missingValues": ["-"]
"missingValues": ["NaN", "-"]
```

#### Remember to provide descriptive metadata for the data dictionary itself

- filename (with extension)
- checksum (preferably a SHA2 checksum)
- authors orcid (https://orcid.org (URL_TO_INSERT_RECORD_5572 https://fairsharing.org/FAIRsharing.nx58jg) /0000-0000-0000-00001)
- license url (e.g.)
- version number (semantic version as in `1.0.1`)

#### Remember to provide the data dictionary in an open syntax


## Data Dictionary Mapping in FAIRplus

While the most desirable approach is of course to design a fully FAIR (URL_TO_INSERT_RECORD_5574 https://fairsharing.org/FAIRsharing.WWI10U)  data dictionary at the start of a project (URL_TO_INSERT_TERM_5573 https://fairsharing.org/search?recordType=project) , it is possible to retroactively FAIR (URL_TO_INSERT_RECORD_5575 https://fairsharing.org/FAIRsharing.WWI10U) ify a data dictionary.
The [FAIR (URL_TO_INSERT_RECORD_5577 https://fairsharing.org/FAIRsharing.WWI10U) plus project](https://fairplus-project.eu/) is in the process of working with the [Innovative Medicine Initiative](https://www.imi.europa.eu/) [APPROACH](https://www.approachproject.eu/) and [ABIRISK](http://www.abirisk.eu/) project (URL_TO_INSERT_TERM_5576 https://fairsharing.org/search?recordType=project) s to assist with the FAIR (URL_TO_INSERT_RECORD_5578 https://fairsharing.org/FAIRsharing.WWI10U) ification of their data dictionaries with a view to improving both the findability and interoperability of their datasets.


## Conclusion

This recipe covered an essential output of any research (URL_TO_INSERT_RECORD_5579 https://fairsharing.org/FAIRsharing.52b22c)  program, **namely the documentation of all variables recorded about study subjects and key metadata descriptors used in subsequence analysis in the form of a `data dictionary`**.
The creation and provision of such a `data dictionary` should be a central component of any `data management plan` and should be one of the key deliverable of any IMI project (URL_TO_INSERT_TERM_5580 https://fairsharing.org/search?recordType=project) .
Why? Simply because if affords several key data management processes to take place
- First, it forces `data owners` to carefully structure core (URL_TO_INSERT_RECORD_5582 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_5583 https://fairsharing.org/FAIRsharing.xMmOCL)  metadata and annotation requirements, by spelling out the nature, purpose and constraints on the data collection (URL_TO_INSERT_TERM_5581 https://fairsharing.org/search?recordType=collection) .
- Second, it provides `data owners` the means to communicate about their scientific outputs, without necessarily disclosing the actual data collected over the course of the project (URL_TO_INSERT_TERM_5584 https://fairsharing.org/search?recordType=project) s. It simply brings clarity and removes ambiguity about collected metadata and data. This clarity helps gauge `reusability potential` as well as `interoperability potential` of datasets.
- Thirdl (URL_TO_INSERT_RECORD_5587 https://fairsharing.org/FAIRsharing.vm4688) y, the availability of the `data dictionary` proves extremely useful for any curatorial works, from gearing for an `ETL process`, to planning for map (URL_TO_INSERT_RECORD_5586 https://fairsharing.org/FAIRsharing.53edcc) ping across ontological frameworks. This is especially facilitated if the `data dictionaries` have clearly identified the semantic resources relied upon in a project (URL_TO_INSERT_TERM_5585 https://fairsharing.org/search?recordType=project) .
- Finally, in the context of the [Innovative Medicine Initiative](https://www.imi.europa.eu/), delivering `Data Dictionaries` contributes to making research (URL_TO_INSERT_RECORD_5589 https://fairsharing.org/FAIRsharing.52b22c)  output more FAIR (URL_TO_INSERT_RECORD_5588 https://fairsharing.org/FAIRsharing.WWI10U) .

### What to read next?

- {ref}`fcb-selecting-ontologies (URL_TO_INSERT_TERM_5590 https://fairsharing.org/search?recordType=terminology_artefact) `
- {ref}`fcb-interop-etl`
- Key issues to be aware of when planning [Extract-Transform-Load processes]( TO (URL_TO_INSERT_RECORD_5591 https://fairsharing.org/FAIRsharing.w69t6r) DO add link)

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
