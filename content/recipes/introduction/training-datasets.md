(fcb-intro-training-datasets)=
# Biomedical datasets of relevance for training in FAIRification


````{panels_fairplus}
:identifier_text: FCB069
:identifier_link: 'https://w3id.org/faircookbook/FCB069'
:difficulty_level: 1
:recipe_type: guidance
:reading_time_minutes: 15
:intended_audience: principal_investigator, data_manager, terminology_manager, data_scientist  
:has_executable_code: nope
:maturity_level: 0
:maturity_indicator: 0
:recipe_name: Training for FAIRification with open or synthetic biomedical datasets
```` 


## Main Objectives

> This recipe aims to provide example clinical datasets to allow users to get familiar with the process of handling clinical datasets
and develop related computational tools while minimizing the challenges of accessing real-world human data.

The FAIR cookbook aims to provide hands-on, practical advice on how to deliver FAIR data through interactions with
Innovative Medicine Initiative(IMI) projects. These research projects, by nature, often involve patient-centric information. 
But dealing with real-world data and human-centric information, clinical data, in particular, is challenging. 
It most often mandates interacting with Data Access Committees (DACs), and undergoes a vetting process, 
which can be lengthy and convoluted. This can become a hindrance if the focus of the work is to deliver training on 
the computational methods available to deal with such data rather than data custody-related tasks,
however important these are. 

This recipe aims to provide a list of relevant resources belonging to the realm of clinical data so readers can, with minimal hassle :
- familiarize with clinical data types, such as Electronic Health Records(EHR).
- familiarize with the procedures to gain access to sensitive data.
- obtain datasets with which to work and hone computational skills.

The recipe will cover two types of datasets:
- `real datasets`, such as the Medical Information Mart for Intensive Care III(MIMIC-III) dataset {footcite}`pmid27219127`, which corresponds to actual medical notes data
for which data access requests must be made but which are made available to computational scientists
for research purposes.
- `synthetic datasets`, which are available without restrictions since produced by computational methods 
and are independent of any real patient. While handy, this type of data may come with a number of limitations prospective 
users need to be aware of.




### Electronic Health Records: The MIMIC-III Critical Care Database

````{dropdown}
:open:
- **Data Type**: Electronic Medical Notes
- **Nature of the data**: Real Patient Data
- **Description**: MIMIC-III (Medical Information Mart for Intensive Care III) is a large, freely-available database 
comprising de-identified health-related data associated with over forty thousand patients who stayed in critical care
units of the Beth Israel Deaconess Medical Center between 2001 and 2012. {footcite}`pmid27219127`. 
The database includes information such as demographics, vital sign measurements made at the bedside 
(circa 1 data point per hour), laboratory test results, procedures, medications, caregiver notes, imaging reports,
and mortality (both in and out of hospital).
- **Purpose**: MIMIC supports a diverse range of analytic studies spanning epidemiology, clinical decision-rule improvement,
and electronic tool development. It is notable for three factors: it is freely available to researchers worldwide. 
It encompasses a diverse and very large population of ICU patients. it contains high temporal resolution data including
lab results, electronic documentation, and bedside monitor trends and waveforms.
- **Availability**: 
    * https://mimic.physionet.org/about/mimic/
    * From Amazon Web Service Public Data: https://registry.opendata.aws/mimiciii/
- **Requesting access**:
    * https://mimic.mit.edu/docs/gettingstarted/
- **Format**: SQL database dump
- **License**: [PhysioNet Credentialed Health Data License 1.5.0](https://physionet.org/content/mimiciii/view-license/1.4/)
- **Examples of use**:
    * [Perform biomedical informatics without a database using MIMIC-III data and Amazon Athena](https://aws.amazon.com/blogs/big-data/perform-biomedical-informatics-without-a-database-using-mimic-iii-data-and-amazon-athena/)
    * [Building predictive disease models using Amazon SageMaker with Amazon HealthLake normalized data](https://aws.amazon.com/blogs/machine-learning/building-predictive-disease-models-using-amazon-sagemaker-with-amazon-healthlake-normalized-data/)

````

### Electronics Medical Notes: The EBM NLP
````{dropdown}
:open:
- **Data Type**: Electronic Medical Notes
- **Nature of the data**: Synthetic Data
- **Description**: A corpus containing 4,993 abstracts annotated with `(P)articipants`, `(I)nterventions`, and `(O)utcomes`.
Training labels are sourced from AMT workers and aggregated to reduce noise. 
Test labels are collected from medical professionals. {footcite}`lee_evans_CDMV5_test_data`
- **Purpose**: Corpus for training and testing Natural Language Processing algorithms
- **Availability**: https://github.com/bepnye/EBM-NLP
- **Format**: *ad-hoc*, UTF-8 text file with tab-delimited values
- **License**: [APACHE license, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)
````

### Electronics Medical Notes: SynPUF 1000 person dataset & OMOP-CDM v5 standard
`````{dropdown}
:open:
- **Data Type**: Electronic Medical Notes
- **Nature of the data**: Synthetic Data
- **Description**: This test data set, generated by  Lee Evans while working at LTS Computing LLC is an OMOP-CDM version 5
formatted collection of 1000 patient samples of CMS 2008-2010 Data Entrepreneurs’ Synthetic Public Use File (DE-SynPUF).
The information held in the dataset corresponds to synthetic patients & medicare claims or prescription data.
- **Purpose**:  
    * Public data to demo the OHDSI Ontologies
    * Benchmark performance
    * Developing & testing OHDSI tools
    * OHDSI tools training
- **Availability**: http://www.ltscomputingllc.com/downloads/
- **Format**: [OMOP CDM v5.2.2](https://github.com/OHDSI/CommonDataModel/releases/tag/v5.2.2) and CSV files compatible with the OMOP CDM V5.2.2 format.
- **License**: LTS Computing LLC license
````{dropdown} SynPUF 1000 person dataset in OMOP CDM v5.2.2 format:

This synthetic dataset corresponds to 1000 person composite dataset:

http://www.ltscomputingllc.com/wp-content/uploads/2018/08/synpuf1k_omop_cdm_5.2.2.zip

For more information about the OMOP Common Data Model, refer to the following:

CDM 5.2.2 DDL for the OHDSI supported DBMSs is available health-related

https://github.com/OHDSI/CommonDataModel/tree/v5.2.2
````

`````


### Synthean Electronic Health Records

`````{dropdown}
:open:
- **Data Type**: Electronic Health Records
- **Nature of the data**: Synthetic EHR
- **Description**: One of the main bottlenecks for data miners is the lack of dataset availability of electronic health records, due to
Health Insurance Portability and Accountability Act (HIPAA) concerns. Synthean, Synthetic Electronic Health Records generating software {footcite}`pmid29025144`
is one of the tools developed to generate synthetic datasets without restrictions to bypass these roadblocks.
- **Purpose**:
   * Generation of synthetic training dataset for data mining and algorithm development
- **Availability**: 
    - [Synthea Official website](https://synthetichealth.github.io/synthea/)
    - [SyntheticMass Data Downloads](https://synthea.mitre.org/downloads)
    - [Synthea Patient Generator](https://github.com/synthetichealth/synthea/)
- **Format**: HL7 FHIR, CCDA, CSV and others
- **License**: [CC0 - "Public Domain Dedication"](https://creativecommons.org/publicdomain/zero/1.0/)

````{dropdown} Exemplar datasets available for download  
:open:
```{figure} ../../../images/Synthea-synthdata.png
---
width: 900px
name: Exemplar Synthetic EHR datasets available for download in HL7 FHIR
alt: Exemplar Synthetic EHR datasets available for download in HL7 FHIR
---
Exemplar Synthetic EHR datasets available for download in HL7 FHIR
``` 
````
`````

### Clinical Trial Data in CDISC SDTM format:

````{dropdown}
:open:
- **Data Type**: Clinical Trial Data
- **Nature of the data**: Synthetic Data
- **Description**: This is a sample study dataset containing [CDISC SDTM](https://www.cdisc.org/standards/foundational/sdtm) formatted data files created originally by CDISC
for demo purposes. This dataset can be used by anyone who is interested in CDISC SDTM formatted dataset.

- **Purpose**:  
    * Benchmark performance
    * Developing & testing CDISC tools
    * CDISC SDTM tools training
- **Availability**: [CDISC-SDTM sample study](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/51B6NK)
- **Format**: CDISC SDTM
- **License**: [CC0 - "Public Domain Dedication"](https://creativecommons.org/publicdomain/zero/1.0/)
- **Examples of use**: [loading standard clinical datasets into PlatformTM live demo](https://platformtm.cloud/app/#/projects/15/main)
````

---
## Conclusions

This content provides you with a set of resources to kick start your exploration of unstructured text in clinical context.
Remember to understand the data stewardship requirements that go along with handling real clinical data but also the limitations associated with some synthetic datasets.

<!-- 
TODO : fill in the links to what-should-I-read-next recipes 

### What to read next?
* How to request data access and deal with data access committees? < TODO add a link to corresponding document >
* How to do NER on EHR with NLP?< TODO add a link to corresponding document >
* How to deal with unstructured text?< TODO add a link to corresponding document >
--->

<!-- {download}`bibliography-identifier-mapping.bib <./bibref/bibliography-identifier-mapping.bib>` -->

## References

````{dropdown} **Reference**
```{footbibliography}
```
````
<!-- Johnson, A., Pollard, T., Shen, L. et al. MIMIC-III, a freely accessible critical care database. Sci Data 3, 160035 (2016). https://doi.org/10.1038/sdata.2016.35

https://www.ohdsi.org/wp-content/uploads/2015/04/Lee_Evans_CDMV5_Test_Data_Presentation.pdf

 -->


## Authors
````{authors_fairplus}
Philippe: Writing - Original Draft
Susanna: Writing - Review & Editing
Yojana: Writing - Review & Editing
Fuqi: Reviewing
````


## License

````{license_fairplus}
CC-BY-4.0
````


