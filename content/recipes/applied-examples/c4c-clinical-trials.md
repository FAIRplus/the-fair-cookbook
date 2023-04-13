(fcb-c4c-clinical-trials)=
# Creating a metadata profile for clinical trial protocols




````{panels_fairplus}
:identifier_text: FCB0xx
:identifier_link: 'https://w3id.org/faircookbook/FCB0xx'
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


The purpose of this recipe is to describe the process to define and standardize study and protocol-level (meta)data commonly collected in paediatric clinical trials, with the aim of making trial data more Findable. The recipe details how to:

> * Define & refine a list of variables to be collected
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
   * A good understanding of clinical trials design
   * Understanding of what a [metadata profile](../interoperability/creating-minimal-metadata-profiles) is.
   

---

<!--## FAIRification Objectives, Inputs and Outputs


| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [text annotation](http://edamontology.org/operation_3778)  | local data dictionary  | [annotated text](http://edamontology.org/data_3779)  |-->


## Table of Data Standards


| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |

---

## Introduction


This recipe was created in collaboration with conect4children (c4c), a large collaborative European network that aims to facilitate the development of new drugs and other therapies for the entire paediatric population. This work was carried out as part of the data harmonization and standardization tasks within c4c.

The creation of a clinical trial protocol metadata profile allows historic clinical trial data to be discovered, and increases the potential for data to be shared and reused. This may ultimately decrease the number of patients needed for new clinical trials, and potentially reduce the cost and effort of conducting those trials. Enabling FAIR data collection from the planning stages of a trial will improve the FAIRness of trial data and the potential for interoperable data sharing and (metadata-level) data querying from different studies. For paediatric trials, the disease being studied is often rare and the number of patients enrolled is small, making the data scarce and valuable.  

## Reviewing existing clinical trials registries


The first step in the process defined and then refined a list of variables to be collected. The (advanced) search features of the following repositories were recorded and then mapped to create a list of common metadata items across all of the resources:
ClinicalTrials.gov
EU Clinical Trials Register
Clinical Research Metadata Repository
Vivli
The YODA Project
NICHD DASH
Biologic Specimen and Data Repository Information Coordinating Center (BioLINCC)
ClinicalStudyDataRequest.com
Health Data Research Innovation Gateway
NIDDK Central Repository
Project Data Sphere
ImmPort
TrialShare
National Sleep Research Resource
NIH Data Share Website
RDCA-DAP
European Genome-Phenome Archive
NIH Genomic Data Commons

The first step created a list of metadata items from the Advanced Search screen on ClinicalTrials.gov. Metadata items from each subsequent repository were compared against this list and mapped across if there was a match. For example, ‘Age Group’ and ‘Age Range’ or ‘Trial Phase’ and ‘Study Phase’. New metadata items that couldn’t be mapped against existing entries were added to the bottom of the list. This gave a good visual of which metadata items occurred most frequently across all of the repositories. The results of the mapping exercise were captured in a Google Sheet. We started with clinicaltrials.gov because it is the most comprehensive and used repository.

## Refining the initial metadata list
The list of metadata items was reviewed by clinical partners, and those not considered cross cutting or common enough for paediatric clinical trials were removed from the list. The following were identified for inclusion:
Condition or Disease
Study Type
Study Results
Status: Recruitment
Age
Age Group
Sex (seemed to be interchangeable with Gender)
Intervention/Treatment
Title/Acronym
Outcome Measure
Study IDs
Country
Phase
Funder Type
Study Documents
Study Start
IMP with Orphan Designation in the Indication
Biospecimens Retained
Sample Size
Therapeutic Area
Product Class
Race
Ethnicity
Study Description
Additional Inclusion Criteria
Additional Exclusion Criteria
Indication
Testing the metadata profile with a representative clinical trial protocol
Don’t need to talk about the specific clinical trial but briefly talk about mapping to ontologies/vocabularies etc.

Each of the above variables were populated (where possible) with information from a clinical trial protocol. They were also mapped to the following ontologies/vocabularies:
https://athena.ohdsi.org/search-terms/start
https://www.ebi.ac.uk/ols/ontologies/cto
https://ncit.nci.nih.gov/ncitbrowser/ 

Example:

Term
Protocol
OMOP
Clinical Trials Ontology
NCI Thesaurus
Age Group
Child up to 15 years inclusive
4305451 Infant
37016983 Toddler
4285883 Child
4305318 Adolescent
NCIT:C49643 Infant & toddler
NCIT:C16423 Child
NCIT:C89342 Toddler
NCIT:C49683 Children 2-11 years
NCIT:C85405 School age child
NCIT:C27954 Adolescent
C27956 Infant
C89342 Toddler
C16423 Child
C27954 Adolescent


The metadata profile in action
What’s going to happen next?

The metadata profile created using the steps described above was used to create a metadata schema in MS Excel.


Variable/record_id
Form Name
Section Header
Field Type
Field Label
record_id
C4C Study Metadata Collection


autofill
Record ID
study_id
C4C Study Metadata Collection
Study Information
short text
Study ID
study_id_1
C4C Study Metadata Collection
Study Information
short text
Add Another Study ID
study_id_text
C4C Study Metadata Collection
Study Information
text box
Add Additional Study IDs
study_title
C4C Study Metadata Collection
Study Information
text box
Study Title
study_acronym
C4C Study Metadata Collection
Study Information
short text
Study Acronym
disease
C4C Study Metadata Collection
Study Information
ontology field
Condition or Disease
therapeutic_area
C4C Study Metadata Collection
Study Information
ontology field
Therapeutic Area
indication
C4C Study Metadata Collection
Study Information
ontology field
Indication
study_type
C4C Study Metadata Collection
Study Information
dropdown
Study Type
country
C4C Study Metadata Collection
Study Information
multiple choice
Country
phase
C4C Study Metadata Collection
Study Information
dropdown
Phase of Trial
funder_type
C4C Study Metadata Collection
Study Information
dropdown
Funder Type
study_start
C4C Study Metadata Collection
Study Information
date field
Study Start
sample_size
C4C Study Metadata Collection
Study Information
short text
Estimated Sample Size
study_description
C4C Study Metadata Collection
Study Information
text box
Study Description
status_recruitment
C4C Study Metadata Collection
Study Information
dropdown
Status: Recruitment
study_documents
C4C Study Metadata Collection
Study Information
multiple choice
Study Documents Available
study_results
C4C Study Metadata Collection
Study Information
dropdown
Study Results
age
C4C Study Metadata Collection
Inclusion/Exclusion Criteria
short text
Age Range
age_group
C4C Study Metadata Collection
Inclusion/Exclusion Criteria
multiple choice
Age Grou(p)
sex
C4C Study Metadata Collection
Inclusion/Exclusion Criteria
dropdown
Sex
race
C4C Study Metadata Collection
Inclusion/Exclusion Criteria
multiple choice
Race
ethnicity
C4C Study Metadata Collection
Inclusion/Exclusion Criteria
multiple choice
Ethnicity
inclusion_criteria
C4C Study Metadata Collection
Inclusion/Exclusion Criteria
text box
Additional Inclusion Criteria
exclusion_criteria
C4C Study Metadata Collection
Inclusion/Exclusion Criteria
text box
Additional Exclusion Criteria
outcome_measures
C4C Study Metadata Collection
Inclusion/Exclusion Criteria
text box
Outcome Measures
intervention_treatment
C4C Study Metadata Collection
Treatment Information
ontology field
Intervention/Treatment
orphan_designation
C4C Study Metadata Collection
Treatment Information
dropdown
IMP with orphan designation in the indication
biospecimens_retained
C4C Study Metadata Collection
Treatment Information
dropdown
Biospecimens Retained
biospecimens_text
C4C Study Metadata Collection
Treatment Information
text box
Type of Biospeciments Retained
product_class
C4C Study Metadata Collection
Treatment Information
ontology field
Product Class



This was used to create a survey in REDCap to allow for more stringent review and testing. The creation of the survey resulted in changes to the schema which may not have been apparent without this additional step. The REDCap survey will be sent to studies within the c4c consortium for additional testing. The studies will be asked to complete the survey with metadata from their study and provide feedback. This feedback will be used to further refine the list of metadata items collected. The final metadata schema will be used to create a FAIR Data Point for c4c studies.   


and then tested using metadata from c4c Proof of Viability (PoV) studies. A FAIR data point will be created for c4c studies after testing has taken place.



---

## Conclusion

* stuff things

### What to read next?
* [Ontology mappings](../interoperability/selecting-ontologies.md)
* [Data dictionary](../interoperability/creating-data-dictionary.md)


````{rdmkit_panel}
````

## References

````{dropdown} **References**
```{footbibliography}
```
````



## Authors


````{authors_fairplus}
Danielle: Writing - Original Draft
Philippe:  Writing - Review & Editing
````


## License
````{license_fairplus}
CC-BY-4.0
````

