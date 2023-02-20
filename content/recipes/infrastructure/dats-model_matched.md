(fcb-dats-model)=
# Introducing the DATS model


<br/>
<br/>

````{panels_fairplus}
:identifier_text: FCB082
:identifier_link: 'https://w3id.org/faircookbook/FCB082'
:difficulty_level: 2
:recipe_type: background_information
:reading_time_minutes: 15
:intended_audience: data_manager, data_curator, software_developer
:maturity_level: 2  
:maturity_indicator: 15
:has_executable_code: nope
:recipe_name: Introducing the DATS model
```` 


## Main Objectives

The main purpose of this recipe is:

>* Provide a general introduction to the Data Tag Suite (URL_TO_INSERT_RECORD-NAME_795 https://fairsharing.org/FAIRsharing.e20vsd)  model for representing project, study and dataset metadata
>* Highlight challenges in implementing the model in a data catalogue

---


## Graphical Overview

````{dropdown} **Data Model**
:open:
```{figure} DataModelDiagram.png
---
width: 800px
name: data-model-diagram
alt: Data Model Diagram
---
Data Model Diagram
```
````

---


## Table of Data Standards


| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| [JSON-LD](https://json-ld.org/) | [OBO Foundry (URL_TO_INSERT_RECORD-NAME_796 https://fairsharing.org/FAIRsharing.847069) ](https://obofoundry.org/) | [DATS](https://datatagsuite.github.io/docs/html/dats.html) |
| |  | [DCAT](https://www.w3.org/TR/vocab-dcat-2/) |
| |  | [SDO](https://schema.org/) |

---

## Model overview

Data Tag Suits (DATS (URL_TO_INSERT_RECORD-ABBREV_797 https://fairsharing.org/FAIRsharing.e20vsd) ) {footcite}`pmid28585923` is a data description model designed and produced to describe datasets being ingested in DataMed (URL_TO_INSERT_RECORD-NAME_800 https://fairsharing.org/FAIRsharing.v5q4zc) , a prototype for data discovery developed as part of the bioCADDIE (URL_TO_INSERT_RECORD-NAME_799 https://fairsharing.org/3506)  project {footcite}`pmid28546571`. DATS (URL_TO_INSERT_RECORD-ABBREV_798 https://fairsharing.org/FAIRsharing.e20vsd)  was co-developed by the Oxford e-Research Centre and the NIH Data Common Big Data to Knowledge (BD2K) initiative, where it was used to uniformly represent metadata across a number of projects, including the Genotype-Tissue Expression project (GTEx) and Trans-Omics for Precision Medicine (TOPMed).

DATS (URL_TO_INSERT_RECORD-ABBREV_806 https://fairsharing.org/FAIRsharing.e20vsd)  is semantically compatible with the Data Catalog Vocabulary (URL_TO_INSERT_RECORD-NAME_801 https://fairsharing.org/FAIRsharing.h4j3qm)  (DCAT (URL_TO_INSERT_RECORD-ABBREV_802 https://fairsharing.org/FAIRsharing.h4j3qm) ), a Resource Description Framework (URL_TO_INSERT_RECORD-NAME_804 https://fairsharing.org/FAIRsharing.p77ph9)  (RDF (URL_TO_INSERT_RECORD-ABBREV_805 https://fairsharing.org/FAIRsharing.p77ph9) ) vocabulary designed to facilitate interoperability among data catalogues published on the web, as well as schema.org (URL_TO_INSERT_RECORD-NAME_808 https://fairsharing.org/FAIRsharing.hzdzq8)  (SDO (URL_TO_INSERT_RECORD-ABBREV_807 https://fairsharing.org/FAIRsharing.7s74s8) ), which is a community-driven effort with a similar interoperability goal to DCAT (URL_TO_INSERT_RECORD-ABBREV_803 https://fairsharing.org/FAIRsharing.h4j3qm)  but a more general-purpose scope.

The original DATS (URL_TO_INSERT_RECORD-ABBREV_811 https://fairsharing.org/FAIRsharing.e20vsd)  model centered around concept of a "Dataset", an entity that covers technical aspects such as licensing, data types and distributions. The Dataset is produced by or is the input or output of a “Study”, which contains elements that are specific to life, environmental and biomedical science domains, and which models experimental processes, cohorts and protocol information. To meet the requirements of project-generated datasets, the DATS (URL_TO_INSERT_RECORD-ABBREV_812 https://fairsharing.org/FAIRsharing.e20vsd)  model was extended to include the third core (URL_TO_INSERT_RECORD-NAME_809 https://fairsharing.org/FAIRsharing.xMmOCL)  (URL_TO_INSERT_RECORD-ABBREV_810 https://fairsharing.org/FAIRsharing.m283c)  concept of “Project”, covering general information such as title, publications, funding and contributors.


### Core objects

The DATS (URL_TO_INSERT_RECORD-ABBREV_815 https://fairsharing.org/FAIRsharing.e20vsd)  model centres around three core (URL_TO_INSERT_RECORD-NAME_813 https://fairsharing.org/FAIRsharing.xMmOCL)  (URL_TO_INSERT_RECORD-ABBREV_814 https://fairsharing.org/FAIRsharing.m283c)  objects, "Project", "Study" and "Dataset", each of which contains a set of sub-objects, which in turn can be nested down to the lowest unitary object (which contains no further objects), which is the “Annotation”. Project, Study and Dataset relate to each other in a triangular fashion as shown in figure 1.

At first glance, the three core (URL_TO_INSERT_RECORD-NAME_816 https://fairsharing.org/FAIRsharing.xMmOCL)  (URL_TO_INSERT_RECORD-ABBREV_817 https://fairsharing.org/FAIRsharing.m283c)  objects make the DATS (URL_TO_INSERT_RECORD-ABBREV_818 https://fairsharing.org/FAIRsharing.e20vsd)  model reminiscent of the ISA (Investigation, Study, Assay) model for describing experimental processes. There are however several key differences between the two. For one, ISA has a waterfall structure whereby any instance of the model has to contain a Study object between an Investigation and an Assay. In DATS (URL_TO_INSERT_RECORD-ABBREV_819 https://fairsharing.org/FAIRsharing.e20vsd)  on the other hand, it is possible for a Dataset to be directly dependent on a Project, without any Study information. This is relevant for datasets such as knowledge graphs or synthetic datasets, for which no study metadata may be available. Additionally, DATS (URL_TO_INSERT_RECORD-ABBREV_820 https://fairsharing.org/FAIRsharing.e20vsd)  focuses on the technical details, availability and use restrictions of datasets whereas the purpose of the ISA model is to describe experimental procedures in great detail. While the DATS (URL_TO_INSERT_RECORD-ABBREV_821 https://fairsharing.org/FAIRsharing.e20vsd)  Study covers some of this information, it is much less comprehensive or central to the captured data than for ISA.

#### Project

The Project object was not part of the original version of DATS (URL_TO_INSERT_RECORD-ABBREV_822 https://fairsharing.org/FAIRsharing.e20vsd) . It was added in the second version as a means of linking different studies and datasets under one common parent as well as capturing information such as project contacts or consortium information, publications not linked to one specific study, funding sources, project websites and start/end dates.

#### Study

The Study object, although part of the original DATS (URL_TO_INSERT_RECORD-ABBREV_823 https://fairsharing.org/FAIRsharing.e20vsd)  model, had a less central role in the first iteration than it has in this latest one. Capturing the context in which the Dataset was either generated or used, the Study provides information about the type of study undertaken (e.g. clinical trials or chemical toxicity screens), cohorts (or "studyGroups), input materials, selection criteria and the steps involved in the study. 

#### Dataset

The Dataset object was the central concept of the initial DATS (URL_TO_INSERT_RECORD-ABBREV_825 https://fairsharing.org/FAIRsharing.e20vsd)  model but became an equal part in the `Project-Study-Dataset` triangle in version 2. The object captures technical information about the dataset, such as file types, data standards, versions and licensing as well as links to the actual data if available. It also models information related to the creation of the dataset such as input materials, diseases, biological entities and other similar objects, as well as the types of experiments from which the dataset was derived and any associated dimensions (URL_TO_INSERT_RECORD-NAME_824 https://fairsharing.org/FAIRsharing.9af33c)  or components.

### Sub-objects

Each of the three top-level objects references a range of sub-objects, which in turn contain further sub-objects, down to the lowest unitary object (which contains no further objects), which is the “Annotation”. An “Annotation” consists of just two key-value pairs, the “value” and, optionally, the “valueIRI”, designed to capture the Internationalized Resource Identifier (IRI) of an ontology term contextualising the free text “value”. Due to this nested object structure, DATS (URL_TO_INSERT_RECORD-ABBREV_826 https://fairsharing.org/FAIRsharing.e20vsd)  can be quite opaque to parse for the human reader but allows for easier programmatic processing of the objects. A full overview of the DATS (URL_TO_INSERT_RECORD-ABBREV_827 https://fairsharing.org/FAIRsharing.e20vsd)  schema can be found on the [DataTagSuite Github repository](https://github.com/datatagsuite/schema).

### Ontology annotations

The provision for ontology annotations is at the core (URL_TO_INSERT_RECORD-NAME_829 https://fairsharing.org/FAIRsharing.xMmOCL)  (URL_TO_INSERT_RECORD-ABBREV_830 https://fairsharing.org/FAIRsharing.m283c)  of the DATS (URL_TO_INSERT_RECORD-ABBREV_831 https://fairsharing.org/FAIRsharing.e20vsd)  model, with the smallest object available in the model being the `Annotation` schema, which simply consists of two key-value pairs: `value`, which can contain a text string (URL_TO_INSERT_RECORD-NAME_832 https://fairsharing.org/FAIRsharing.9b7wvk)  or number (to allow for coded values), and `valueIRI`, which contains a URI (URL_TO_INSERT_RECORD-ABBREV_828 https://fairsharing.org/FAIRsharing.d261e1) -formatted string (URL_TO_INSERT_RECORD-NAME_833 https://fairsharing.org/FAIRsharing.9b7wvk)  representing a concept or ontology term associated with the value. It should be noted that the Annotation object has no required properties, so the valueIRI in particular can be empty. 

The model also provides an extension mechanism through a schema object called `CategoryValuesPair`. This allows the addition of extra properties to the entities in cases where there are no specific properties to deal with the desired property. In order to capture the semantics of the category, CategoryValuesPairs capture both a `category` as a free-text string (URL_TO_INSERT_RECORD-NAME_835 https://fairsharing.org/FAIRsharing.9b7wvk)  and a `categoryIRI` for the URI (URL_TO_INSERT_RECORD-ABBREV_834 https://fairsharing.org/FAIRsharing.d261e1)  of an associated ontology context. The `values` are of type `Annotation` and can therefore also have ontology annotations.

DATS (URL_TO_INSERT_RECORD-ABBREV_836 https://fairsharing.org/FAIRsharing.e20vsd)  does not prescribe the use of specific ontologies in relation to various properties, although it would be advisable to include this type of restriction in a given implementation of the model in order to simply the interoperability between different objects of the same type.

### Encoding in JSON-LD

DATS (URL_TO_INSERT_RECORD-ABBREV_845 https://fairsharing.org/FAIRsharing.e20vsd)  objects are encoded in JSON (URL_TO_INSERT_RECORD-ABBREV_839 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD-ABBREV_847 https://fairsharing.org/FAIRsharing.8f9bbb) , a method for encoding linked data in the open standard file and data interchange format JSON (URL_TO_INSERT_RECORD-ABBREV_840 https://fairsharing.org/FAIRsharing.5bbab9) . JSON (URL_TO_INSERT_RECORD-ABBREV_841 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD-ABBREV_848 https://fairsharing.org/FAIRsharing.8f9bbb)  is designed around the concept of a "context" to provide additional mappings from JSON (URL_TO_INSERT_RECORD-ABBREV_842 https://fairsharing.org/FAIRsharing.5bbab9)  to an RDF (URL_TO_INSERT_RECORD-ABBREV_843 https://fairsharing.org/FAIRsharing.p77ph9)  model. DATS (URL_TO_INSERT_RECORD-ABBREV_846 https://fairsharing.org/FAIRsharing.e20vsd)  provides three sets of context mappings, to DCAT (URL_TO_INSERT_RECORD-ABBREV_837 https://fairsharing.org/FAIRsharing.h4j3qm) , schema.org (URL_TO_INSERT_RECORD-NAME_850 https://fairsharing.org/FAIRsharing.hzdzq8)  (SDO (URL_TO_INSERT_RECORD-ABBREV_849 https://fairsharing.org/FAIRsharing.7s74s8) ) and the OBO Foundry (URL_TO_INSERT_RECORD-NAME_844 https://fairsharing.org/FAIRsharing.847069)  Ontologies. None of the three sets of contexts individually cover all properties in the model but they can be used in combination to maximise the semantic linking of the model, likely to increase interoperability, for instance with DCAT (URL_TO_INSERT_RECORD-ABBREV_838 https://fairsharing.org/FAIRsharing.h4j3qm)  based catalogues.



## Implementing DATS in a data catalogue

We implemented DATS (URL_TO_INSERT_RECORD-ABBREV_851 https://fairsharing.org/FAIRsharing.e20vsd)  v2.0 in the [IMI Translational Data Catalog](https://datacatalog.elixir-luxembourg.org/). The DATS (URL_TO_INSERT_RECORD-ABBREV_852 https://fairsharing.org/FAIRsharing.e20vsd)  model's flexibility presents both a benefit and a challenge in that some concepts could be encoded in a number of ways. Experimental materials for example can be encoded at both the Study level, in `Study.input` or at the Dataset level, in `Dataset.isAbout`. In order to encode metadata consistently and simplify indexing and display processes for the IMI Data Catalog (URL_TO_INSERT_RECORD-ABBREV_853 https://fairsharing.org/FAIRsharing.de533c) , we therefore made a number of assumptions about how to encode certain metadata entities in the model.

### Assumptions

* Study and Dataset objects can't exist without a Project. This rule was necessary to provide a root for our indexing service.

* The Study object encodes information about the input materials to the experiment, such as study subjects in the case of clinical trials or biological molecules in the case of chemical assays. At this level, we collect cohort descriptions, sample sizes, sample sources, types of samples and diseases.
 
* The Dataset object encodes information about the dataset, including technical information such as version number, creation and update dates, data standards and file types. The dataset also lists the experiment types that generated the data, the number and types of samples that contributed to the dataset and any diseases in the samples. These properties can be distinct from the ones at Study level as not all samples collected in a Study may be used to generate a given dataset, e.g. blood samples might be used for sequencing experiments, generating a sequencing dataset, while other tissue samples are used in imaging assays, generating an imaging dataset. The number of samples collected can be different from the cohort sample size (i.e. number of subject), either because multiple samples were collected from each subject or because some samples were excluded from the dataset for quality reasons.

* In the implementation of the model, preference as given to specific ontologies in certain contexts, eg MONDO (URL_TO_INSERT_RECORD-ABBREV_854 https://fairsharing.org/FAIRsharing.b2979t)  for diseases, UBERON (URL_TO_INSERT_RECORD-ABBREV_856 https://fairsharing.org/FAIRsharing.4c0b6b)  for anatomical components, NCIt (URL_TO_INSERT_RECORD-ABBREV_855 https://fairsharing.org/FAIRsharing.4cvwxa) , EFO (URL_TO_INSERT_RECORD-ABBREV_859 https://fairsharing.org/FAIRsharing.1gr4tz)  and OBI (URL_TO_INSERT_RECORD-ABBREV_858 https://fairsharing.org/FAIRsharing.284e1z)  for experiment types, UO (URL_TO_INSERT_RECORD-ABBREV_857 https://fairsharing.org/FAIRsharing.mjnypw)  for units etc.

---

## Conclusion

> * DATS (URL_TO_INSERT_RECORD-ABBREV_860 https://fairsharing.org/FAIRsharing.e20vsd)  is a flexible data model aimed at biomedical datasets.
> * DATS (URL_TO_INSERT_RECORD-ABBREV_862 https://fairsharing.org/FAIRsharing.e20vsd)  utilises the power of JSON (URL_TO_INSERT_RECORD-ABBREV_861 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD-ABBREV_863 https://fairsharing.org/FAIRsharing.8f9bbb)  to encode semantics at all levels of the model.
> * DATS (URL_TO_INSERT_RECORD-ABBREV_864 https://fairsharing.org/FAIRsharing.e20vsd) ' flexibility does mean that consistent implementation of the model in a specific context requires assumptions to be made.


### What should I read next?
> * [Building a catalogue of datasets](./data-catalog.md) 
> * [Deploying the IMI data catalog](./data-catalog-deployment.md) 
> * [Introduction to terminologies and ontologies](../interoperability/introduction-terminologies-ontologies.md)

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

