(fcb-dats-model)=
# Introduction to the DATS model


<br/>
<br/>

````{panels_fairplus}
:identifier_text: FCB000
:identifier_link: 'https://w3id.org/faircookbook/FCB000'
:difficulty_level: 2
:recipe_type: background_information
:reading_time_minutes: 15
:intended_audience: data_manager, data_curator, software_developer
:maturity_level: 2  
:maturity_indicator: 15
:has_executable_code: nope
:recipe_name: Data Tag Suite (DATS)
```` 


## Main Objectives

The main purpose of this recipe is:

>* Provide a general introduction to the Data Tag Suite model for representing project, study and dataset metadata
>* Compare the model to other relevant data catalogue models
>* Highlight challenges in implementing the model in a data catalogue

---


## Graphical Overview

<!--DATS diagram goes here-->


---


## Table of Data Standards


<!--TO DO - review & hyperlinks -->

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| JSON-LD |  | DATS |

---

## Model overview

Data Tag Suits (DATS) is a data description model designed and produced to describe datasets being ingested in DataMed, a prototype for data discovery developed as part of the bioCADDIE project. DATS was co-developed by the Oxford e-Research Centre and the NIH Data Common Big Data to Knowledge (BD2K) initiative, where it was used to uniformly represent metadata across a number of projects, including the Genotype-Tissue Expression project (GTEx) and Trans-Omics for Precision Medicine (TOPMed).

DATS is semantically compatible with the Data Catalog Vocabulary (DCAT), a Resource Description Framework (RDF) vocabulary designed to facilitate interoperability among data catalogues published on the web, as well as schema.org (SDO), which is a community-driven effort with a similar interoperability goal to DCAT but a more general-purpose scope.

The original DATS model centered around concept of a "Dataset", an entity that covers technical aspects such as licensing, data types and distributions. The Dataset is produced by or is the input or output of a “Study”, which contains elements that are specific to life, environmental and biomedical science domains, and which models experimental processes, cohorts and protocol information. To meet the requirements of project-generated datasets, the DATS model was extended to include the third core concept of “Project”, covering general information such as title, publications, funding and contributors.


### Core objects

The DATS model centres around three core objects, "Project", "Study" and "Dataset", each of which contains a set of sub-objects, which in turn can be nested down to the lowest unitary object (which contains no further objects), which is the “Annotation”. Project, Study and Dataset relate to each other in a triangular fashion as shown in figure 1.

At first glance, the three core objects make the DATS model reminiscent of the ISA (Investigation, Study, Assay) model for describing experimental processes. There are however several key differences between the two. For one, ISA has a waterfall structure whereby any instance of the model has to contain a Study object between an Investigation and an Assay. In DATS on the other hand, it is possible for a Dataset to be directly dependent on a Project, without any Study information. This is relevant for datasets such as knowledge graphs or synthetic datasets, for which no study metadata may be available. Additionally, DATS focuses on the technical details, availability and use restrictions of datasets whereas the purpose of the ISA model is to describe experimental procedures in great detail. While the DATS Study covers some of this information, it is much less comprehensive or central to the captured data than for ISA.

#### Project

The Project object was not part of the original version of DATS. It was added in the second version as a means of linking different studies and datasets under one common parent as well as capture information such as project contacts or consortium information, publications not linked to one specific study, funding sources, project websites and start/end dates.

#### Study

The Study object

#### Dataset

The Dataset object was the central concept of the initial DATS model but became an equal 


### Sub-objects





### Ontology annotations



### Encoding in JSON-LD




## Implementing DATS in a data catalogue

We implemented DATS v2.0 in the IMI Data Catalog. The DATS model's flexibility presents both a benefit and a challenge in that some concepts could be encoded in a number of ways. Experimental materials for example can be encoded at both the Study level, in `Study.input` or at the Dataset level, in `Dataset.isAbout`. In order to encode metadata consistently and simplify indexing and display processes for the IMI Data Catalog, we therefore made a number of assumptions about how to encode certain metadata entities in the model.

### Assumptions

* Study and Dataset objects can't exist without a Project. This rule was necessary to provide a root for our indexing service.

* The Study object encodes information about the input materials to the experiment, such as study subjects in the case of clinical trials or biological molecules in the case of chemical assays. At this level, we collect cohort descriptions, sample sizes, sample sources, types of samples and diseases.
 
* The Dataset object encodes information about the dataset, including technical information such as version number, creation and update dates, data standards and file types. The dataset also lists the experiment types that generated the data, the number and types of samples that contributed to the dataset and any diseases in the samples. These properties can be distinct from the ones at Study level as not all samples collected in a Study may be used to generate a given dataset, eg blood samples might be used for sequencing experiments, generating a sequencing dataset, while other tissue samples are used in imaging assays, generating an imaging dataset. The number of samples collected can be different from the cohort sample size (ie number of subject), either because multiple samples were collected from each subject or because some samples were excluded from the dataset for quality reasons.

---

## Conclusion

> Summerize Key Learnings of the recipe.


### What should I read next?
* Data Catalog recipe?


## References:

````{dropdown} **References**
```{footbibliography}
```
````



## Authors

````{authors_fairplus}
Danielle: Writing - original draft
Philippe: Writing - review & editing
````


## License
````{license_fairplus}
CC-BY-4.0
````

