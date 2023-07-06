(fcb-c4c-clinical-trials)=
# Creating a metadata profile for clinical trial protocols




````{panels_fairplus}
:identifier_text: FCB084
:identifier_link: 'https://w3id.org/faircookbook/FCB084'
:difficulty_level: 3
:recipe_type: applied_example
:reading_time_minutes: 20
:intended_audience: principal_investigator, data_manager, data_scientist, terminology_manager, ontologist
:maturity_level: 3  
:maturity_indicator: 19, 22
:has_executable_code: nope
:recipe_name: Creating a metadata profile for clinical trial protocols
```` 


## Main Objectives

The purpose of this recipe is to describe the process to define and standardize study and protocol-level (meta)data commonly collected in paediatric clinical trials, with the aim of making trial data more Findable through a common Interoperable metadata profile. The recipe details how to:

> * Collect & refine a list of representative variables
* Represent protocol-level additional (meta)data in a complementary data model
* Define extraction processes for populating variables of interest

---


## Graphical Overview

````{dropdown}
:open:
```{figure} c4c-clinical-trials.md-figure0.mmd.png
---
name: c4c-clinical-trials-figure0
height: 1000 px
alt: Recipe Steps
---
Recipe Steps
```
````


---


## Requirements

* Technical requirements:
   *none*
   
* Knowledge requirement:
   * A basic understanding of clinical trial design and the types of data that are collected in clinical trials. 
   * Understanding of what a [metadata profile](creating-minimal-metadata-profiles) is.
   

---

<!--## FAIRification Objectives, Inputs and Outputs


| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [text annotation](http://edamontology.org/operation_3778)  | local data dictionary  | [annotated text](http://edamontology.org/data_3779)  |-->


## Table of Data Standards


| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| | [OMOP](https://athena.ohdsi.org/search-terms/start) | | 
| | [Clinical Trials Ontology](https://www.ebi.ac.uk/ols/ontologies/cto) | | 
| | [NCI Thesaurus](https://ncithesaurus.nci.nih.gov/ncitbrowser/pages/multiple_search.jsf?nav_type=terminologies) | | 



---

## Introduction


This recipe was created in collaboration with [conect4children (c4c)](https://conect4children.org/), a large collaborative European network that aims to facilitate the development of new drugs and other therapies for the entire paediatric population. This work was carried out as part of the WP5 data harmonization and standardization tasks within c4c.

The creation of a clinical trial protocol metadata profile allows historic clinical trial data to be discovered, and increases the potential for data to be shared and reused. This may ultimately decrease the number of patients needed for new clinical trials, and potentially reduce the cost and effort of conducting those trials. For paediatric trials, the disease being studied is often rare and the number of patients enrolled is small, making the data scarce and valuable.  

Enabling FAIR data collection from the planning stages of a trial will improve the FAIRness of trial data and the potential for interoperable data sharing and (metadata-level) data querying from different studies. 


## Reviewing existing clinical trials registries


The first step in the process defined and then refined a list of variables to be collected. The (advanced) search features of the following repositories and registries were recorded and then mapped to create a list of common metadata items across all of the resources:

- [ClinicalTrials.gov](https://clinicaltrials.gov/)
- [EU Clinical Trials Register](https://www.clinicaltrialsregister.eu/)
- [Clinical Research Metadata Repository](https://ecrin.org/clinical-research-metadata-repository)
- [Vivli](https://vivli.org/)
- [The YODA Project](https://yoda.yale.edu/)
- [Pediatric Trials Network (PTN)](https://pediatrictrials.org/)
- [BioLINCC](https://biolincc.nhlbi.nih.gov/studies/)
- [ClinicalStudyDataRequest (CSDR)](https://www.clinicalstudydatarequest.com/)
- [Health Data Research Innovation Gateway](https://www.healthdatagateway.org/)
- [NIDDK Central Repository](https://repository.niddk.nih.gov/search/study/)
- [Project Data Sphere](https://data.projectdatasphere.org/projectdatasphere/html/access)
- [Immunology Database and Analysis Portal (ImmPort)]()
- [ITN TrialShare](https://www.immport.org/shared/)
- [National Sleep Research Resource (NSRR)](https://sleepdata.org/)
- [National Institute on Drug Abuse NIDA](https://datashare.nida.nih.gov/data)
- [RDCA-DAP](https://portal.rdca.c-path.org/)
- [European Genome-phenome Archive (EGA)](https://ega-archive.org/)

The first step created a list of metadata items from the Advanced Search screen on ClinicalTrials.gov. Metadata items from each subsequent repository were compared against this list and mapped across if there was a match. For example, ‘Age Group’ and ‘Age Range’ or ‘Trial Phase’ and ‘Study Phase’. New metadata items that couldn’t be mapped against existing entries were added to the bottom of the list. This gave a good visual of which metadata items occurred most frequently across all of the repositories. The results of the mapping exercise were captured in a [Google Sheet](https://docs.google.com/spreadsheets/d/1JGaSJKHHOXtkEtV_NrkSdktlTw5g69W03NjL8deUoMw/edit?usp=sharing). We started with ClinicalTrials.gov because it is the most comprehensive and used repository.



## Refining the initial metadata list
The list of metadata items was reviewed by c4c partners, and those not considered cross cutting or common enough for paediatric clinical trials were removed from the list. The original list consisted of 36 items and this was reduced to 27. The following were identified for inclusion:

| Considered cross cutting or common enough to be included in the metadata schema | Not considered cross cutting or common enough to be included in the Metadata Schema|
| :------------- | :------------- |
| Study IDs | Rare Disease (tick box yes/no) |
| Title | Intervention Model |
| Acronym | NCT Number |
| Condition or Disease | Consent |
| Therapeutic Area | Criterion |
| Indication | Site Name |
| Study Type | Formulation |
| Phase | Route of Administration |
| Funder Type |  |
| Study Start |  |
| Sample Size |  |
| Study Description |  |
| Status: Recruitment |  |
| Study Documents |  |
| Study Results |  |
| Country |  |
| Age |  |
| Age Group |  |
| Sex |  |
| Ethnicity |  |
| Race |  |
| Additional Inclusion Criteria |  |
| Additional Exclusion Criteria |  |
| Outcome Measures |  |
| Intervention/Treatment |  |
| IMP with Orphan Designation in the Indication |  |
| Biospecimens Retained |  |
| Product Class |  |

## Testing the metadata profile with a representative clinical trial protocol

Each of the above variables were populated (where possible) with information from a clinical trial protocol. They were also mapped to the following ontologies/vocabularies:

- [OMOP vocabularies](https://athena.ohdsi.org/search-terms/start)
- [Clinical Trials Ontology](https://www.ebi.ac.uk/ols/ontologies/cto)
- [NCI Thesaurus](https://ncit.nci.nih.gov/ncitbrowser/) 


Example:

| Term | Protocol | OMOP | Clinical Trials Ontology | NCI Thesaurus |
| :------------- | :------------- | :------------- |:------------- | :------------- | 
| Age Group | Child up to 15 years inclusive | 4305451 Infant 37016983 Toddler 4285883 Child 4305318 Adolescent |  NCIT:C49643 Infant & toddler NCIT:C16423 Child NCIT:C89342 Toddler NCIT:C49683 Children 2-11 years NCIT:C85405 School age child NCIT:C27954 Adolescent | C27956 Infant C89342 Toddler C16423 Child C27954 Adolescent |


## The metadata profile in action

The metadata profile created using the steps described above was used to create a metadata schema in MS Excel.

| Variable/record_id | Form Name | Section Header | Field Type | Field Label |
| :------------- | :------------- | :------------- |:------------- | :------------- |
| record_id | C4C Study Metadata Collection |  | autofill | Record ID |
| study_id | C4C Study Metadata Collection | Study Information | short text | Study ID |
| study_id\_1 | C4C Study Metadata Collection | Study Information | short text | Add Another Study ID |
| study_id\_text | C4C Study Metadata Collection | Study Information | text box | Add Additional Study IDs |
| study_title | C4C Study Metadata Collection | Study Information | text box | Study Title |
| study_acronym | C4C Study Metadata Collection | Study Information | short text | Study Acronym |
| disease | C4C Study Metadata Collection | Study Information | ontology field | Condition or Disease |
| therapeutic_area | C4C Study Metadata Collection | Study Information | ontology field | Therapeutic Area |
| indication | C4C Study Metadata Collection | Study Information | ontology field | Indication |
| study_type | C4C Study Metadata Collection | Study Information | dropdown | Study Type |
| country | C4C Study Metadata Collection | Study Information | multiple choice | Country |
| phase | C4C Study Metadata Collection | Study Information | dropdown | Phase of Trial |
| funder_type | C4C Study Metadata Collection | Study Information | dropdown | Funder Type |
| study_start | C4C Study Metadata Collection | Study Information | date field | Study Start |
| sample_size | C4C Study Metadata Collection | Study Information | short text | Estimated Sample Size |
| study_description | C4C Study Metadata Collection | Study Information | text box | Study Description |
| status_recruitment | C4C Study Metadata Collection | Study Information | dropdown | Status: Recruitment |
| study_documents | C4C Study Metadata Collection | Study Information | multiple choice | Study Documents Available |
| study_results | C4C Study Metadata Collection | Study Information | dropdown | Study Results |
| age | C4C Study Metadata Collection | Inclusion/Exclusion Criteria | short text | Age Range |
| age_group | C4C Study Metadata Collection | Inclusion/Exclusion Criteria | multiple choice | Age Grou(p) |
| sex | C4C Study Metadata Collection | Inclusion/Exclusion Criteria | dropdown | Sex |
| race | C4C Study Metadata Collection | Inclusion/Exclusion Criteria | multiple choice | Race |
| ethnicity | C4C Study Metadata Collection | Inclusion/Exclusion Criteria | multiple choice | Ethnicity |
| inclusion_criteria | C4C Study Metadata Collection | Inclusion/Exclusion Criteria | text box | Additional Inclusion Criteria |
| exclusion_criteria | C4C Study Metadata Collection | Inclusion/Exclusion Criteria | text box | Additional Exclusion Criteria |
| outcome_measures | C4C Study Metadata Collection | Inclusion/Exclusion Criteria | text box | Outcome Measures |
| intervention_treatment | C4C Study Metadata Collection | Treatment Information | ontology field | Intervention/Treatment |
| orphan_designation | C4C Study Metadata Collection | Treatment Information | dropdown | IMP with orphan designation in the indication |
| biospecimens_retained | C4C Study Metadata Collection | Treatment Information | dropdown | Biospecimens Retained |
| biospecimens_text | C4C Study Metadata Collection | Treatment Information | text box | Type of Specimens Retained |
| product_class | C4C Study Metadata Collection | Treatment Information | ontology field | Product Class |


This schema was used to create a survey in [REDCap](https://www.project-redcap.org/) to allow for more stringent review and testing. The creation of the survey resulted in changes to the schema which may not have been apparent without this additional step. For example, Race was removed from the survey as it was difficult to standardize responses due to geographic variance and text boxes were added for additional inclusion/exclusion criteria. The revised metadata schema is shown below.


| Variable/record_id | Form Name | Section Header | Field Type | Field Label |
| :------------- | :------------- | :------------- |:------------- | :------------- |
| record_id | C4C Study Metadata Collection |  | autofill | Record ID |
|  | C4C Study Metadata Collection | Study Information | begin new section |  |
| study_id\_ct.gov | C4C Study Metadata Collection | Study Information | short text | ClinicalTrials.gov ID |
| study_id\_eudract | C4C Study Metadata Collection | Study Information | short text | EudraCT/CTIS ID |
| study_id\_brand | C4C Study Metadata Collection | Study Information | short text | Study Brand Name ID (if applicable) |
| study_id\_text | C4C Study Metadata Collection | Study Information | text box | Add Additional Study IDs |
| study_title | C4C Study Metadata Collection | Study Information | text box | Study Title |
| study_acronym | C4C Study Metadata Collection | Study Information | short text | Study Acronym |
| disease | C4C Study Metadata Collection | Study Information | ontology field | Condition or Disease |
| therapeutic_area | C4C Study Metadata Collection | Study Information | ontology field | Therapeutic Area |
| indication | C4C Study Metadata Collection | Study Information | text box | Indication |
| study_type | C4C Study Metadata Collection | Study Information | dropdown | Study Type |
| study_type\_other | C4C Study Metadata Collection | Study Information | short text | Add Other Study Types |
| phase | C4C Study Metadata Collection | Study Information | dropdown | Phase of Trial |
| phase_other | C4C Study Metadata Collection | Study Information | short text | Add Additional Trial Phases |
| funder_type | C4C Study Metadata Collection | Study Information | dropdown | Funder Type |
| funder_type\_other | C4C Study Metadata Collection | Study Information | short text | Provide Information about 'Other' Funder Types |
| study_start | C4C Study Metadata Collection | Study Information | date field | Study Start Date |
| sample_size | C4C Study Metadata Collection | Study Information | short text | Estimated Sample Size |
| study_description | C4C Study Metadata Collection | Study Information | text box | Study Description |
| status_recruitment | C4C Study Metadata Collection | Study Information | dropdown | Status: Recruitment |
| study_documents | C4C Study Metadata Collection | Study Information | multiple choice | Study Documents Available |
| study_documents\_other | C4C Study Metadata Collection | Study Information | short text | Add Additional Types of Study Documents |
| study_results | C4C Study Metadata Collection | Study Information | dropdown | Study Results |
| study_continents | C4C Study Metadata Collection | Study Information | multiple choice | Please Select Study Site Locations |
| european_sites | C4C Study Metadata Collection | Study Information | multiple choice | Please Select European Study Site Locations |
| n_american\_sites | C4C Study Metadata Collection | Study Information | multiple choice | Please Select North American Study Site Locations |
|  | C4C Study Metadata Collection | Inclusion/Exclusion Criteria | begin new section |  |
| age | C4C Study Metadata Collection | Inclusion/Exclusion Criteria | short text | Age Range |
| age_group | C4C Study Metadata Collection | Inclusion/Exclusion Criteria | multiple choice | Age Group(s) |
| sex | C4C Study Metadata Collection | Inclusion/Exclusion Criteria | dropdown | Sex |
| ethnicity | C4C Study Metadata Collection | Inclusion/Exclusion Criteria | multiple choice | Ethnicity |
| inclusion_criteria | C4C Study Metadata Collection | Inclusion/Exclusion Criteria | text box | Additional Inclusion Criteria |
| exclusion_criteria | C4C Study Metadata Collection | Inclusion/Exclusion Criteria | text box | Additional Exclusion Criteria |
| outcome_measures | C4C Study Metadata Collection | Inclusion/Exclusion Criteria | text box | Outcome Measures |
|  | C4C Study Metadata Collection | Treatment Information | begin new section |  |
| intervention_treatment | C4C Study Metadata Collection | Treatment Information | ontology field | Intervention/Treatment |
| orphan_designation | C4C Study Metadata Collection | Treatment Information | dropdown | IMP with orphan designation in the indication |
| biospecimens_retained | C4C Study Metadata Collection | Treatment Information | dropdown | Biospecimens Retained |
| biospecimens_text | C4C Study Metadata Collection | Treatment Information | text box | Type of Biospecimens Retained |
| product_class | C4C Study Metadata Collection | Treatment Information | ontology field | Product Class |

The REDCap survey will be sent to studies within the c4c consortium for additional testing. A representative of the study will be asked to complete the survey with metadata from their study and provide feedback. This feedback will be used to further refine the list of metadata items collected. The final metadata schema will be used to create a [FAIR Data Point](https://www.fairdatapoint.org/) for c4c studies.  In the future this will allow researchers to find sources of paediatric data from clinical trials. 


---

## Conclusion

Paediatric data is often rare and scarce which contributes to the slow development of knowledge and treatments. Any activity that can improve the Findability (and potential Reusability) of the data is therefore valuable.  Other researchers could benefit from this recipe by applying it to other sources or types of (meta)data to improve Findability. 

The REDCap survey will be sent to c4c partners to allow for further testing of the (meta)data schema. The test results will be used to develop a FAIR data point for c4c studies. 


### What to read next?
* [Ontology mappings](../interoperability/selecting-ontologies.md)
* [Data dictionary](../interoperability/creating-data-dictionary.md)


````{rdmkit_panel}
````

<!--## References

````{dropdown} **References**
```{footbibliography}
```
````

-->

## Authors


````{authors_fairplus}
Avril: Writing - Original Draft
Becca: Writing - Original Draft
Anando: Writing - Original Draft
Ronald: Writing - Original Draft
Danielle:  Writing - Review & Editing
Philippe: Writing - Review & Editing
````


## License
````{license_fairplus}
CC-BY-4.0
````

