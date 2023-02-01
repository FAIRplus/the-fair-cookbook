(fcb-dats-model (URL_TO_INSERT_TERM_3435 https://fairsharing.org/search?recordType=model_and_format) )=
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

>* Provide a general introduction to the Data Tag Suite (URL_TO_INSERT_RECORD_3438 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_3437 https://fairsharing.org/search?recordType=model_and_format)  for representing project (URL_TO_INSERT_TERM_3436 https://fairsharing.org/search?recordType=project) , study and dataset metadata
>* Highlight challenges in implementing the model (URL_TO_INSERT_TERM_3439 https://fairsharing.org/search?recordType=model_and_format)  in a data catalogue

---


## Graphical Overview

````{dropdown} **Data Model**
:open:
```{figure} DataModelDiagram.png
---
width: 800px
name: data-model (URL_TO_INSERT_TERM_3440 https://fairsharing.org/search?recordType=model_and_format) -diagram
alt: Data Model (URL_TO_INSERT_TERM_3441 https://fairsharing.org/search?recordType=model_and_format)  Diagram
---
Data Model (URL_TO_INSERT_TERM_3442 https://fairsharing.org/search?recordType=model_and_format)  Diagram
```
````

---


## Table of Data Standards


| Data Format (URL_TO_INSERT_TERM_3444 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_3445 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_3443 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
| [JSON-LD](https://json-ld.org/) | [OBO (URL_TO_INSERT_RECORD_3447 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_3448 https://fairsharing.org/FAIRsharing.cbz72b)  Foundry (URL_TO_INSERT_RECORD_3446 https://fairsharing.org/FAIRsharing.847069) ](https://obofoundry.org/) | [DATS](https://datatagsuite.github.io/docs/html/dats.html) |
| |  | [DCAT](https://www.w3.org/TR/vocab-dcat (URL_TO_INSERT_RECORD_3449 https://fairsharing.org/FAIRsharing.h4j3qm) -2/) |
| |  | [SDO](https://schema.org (URL_TO_INSERT_RECORD_3450 https://fairsharing.org/FAIRsharing.hzdzq8) /) |

---

## Model overview

Data Tag Suits (DATS (URL_TO_INSERT_RECORD_3456 https://fairsharing.org/FAIRsharing.e20vsd) ) {footcite}`pmid28585923` is a data description model (URL_TO_INSERT_TERM_3454 https://fairsharing.org/search?recordType=model_and_format)  designed and produced to describe datasets being ingested in DataMed (URL_TO_INSERT_RECORD_3467 https://fairsharing.org/FAIRsharing.v5q4zc)  (URL_TO_INSERT_RECORD_3468 https://fairsharing.org/FAIRsharing.v5q4zc) , a prototype for data discovery developed (URL_TO_INSERT_RECORD_3464 https://fairsharing.org/FAIRsharing.31385c)  as part of the bioCADDI (URL_TO_INSERT_RECORD_3469 https://fairsharing.org/FAIRsharing.pf2qyq) E (URL_TO_INSERT_RECORD_3459 https://fairsharing.org/3506)  (URL_TO_INSERT_RECORD_3460 https://fairsharing.org/3506)  project (URL_TO_INSERT_TERM_3451 https://fairsharing.org/search?recordType=project)  {footcite}`pmid28546571`. DATS (URL_TO_INSERT_RECORD_3457 https://fairsharing.org/FAIRsharing.e20vsd)  was co-developed (URL_TO_INSERT_RECORD_3465 https://fairsharing.org/FAIRsharing.31385c)  by the Oxford e-Research (URL_TO_INSERT_RECORD_3463 https://fairsharing.org/FAIRsharing.52b22c)  Centre and the NIH (URL_TO_INSERT_RECORD_3462 https://fairsharing.org/FAIRsharing.41718d)  Data Common Big Data to Knowledge (BD2K) initiative, where it was used to uniformly represent metadata across a number of project (URL_TO_INSERT_TERM_3452 https://fairsharing.org/search?recordType=project) s, including the Genotype-Tissue Expression project (URL_TO_INSERT_TERM_3453 https://fairsharing.org/search?recordType=project)  (GTEx) and Trans-Omics for Precision Medicine (TO (URL_TO_INSERT_RECORD_3461 https://fairsharing.org/FAIRsharing.w69t6r) P (URL_TO_INSERT_RECORD_3458 https://fairsharing.org/707)  (URL_TO_INSERT_RECORD_3466 https://fairsharing.org/FAIRsharing.yvmb9y) M (URL_TO_INSERT_RECORD_3455 https://fairsharing.org/FAIRsharing.7c683b) ed).

DATS (URL_TO_INSERT_RECORD_3477 https://fairsharing.org/FAIRsharing.e20vsd)  is semantically compatible with the Data Catalog Vocabulary (URL_TO_INSERT_RECORD_3474 https://fairsharing.org/FAIRsharing.h4j3qm)  (DC (URL_TO_INSERT_RECORD_3478 https://fairsharing.org/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD_3480 https://fairsharing.org/3547) AT (URL_TO_INSERT_RECORD_3470 https://fairsharing.org/FAIRsharing.3a96ae)  (URL_TO_INSERT_RECORD_3475 https://fairsharing.org/FAIRsharing.h4j3qm) ), a Resource Description Framework (URL_TO_INSERT_RECORD_3472 https://fairsharing.org/FAIRsharing.p77ph9)  (RDF (URL_TO_INSERT_RECORD_3473 https://fairsharing.org/FAIRsharing.p77ph9) ) vocabulary designed to facilitate interoperability among data catalogues published on the web, as well as schema.org (URL_TO_INSERT_RECORD_3483 https://fairsharing.org/FAIRsharing.hzdzq8)  (SDO (URL_TO_INSERT_RECORD_3482 https://fairsharing.org/FAIRsharing.7s74s8) ), which is a community-driven effort with a similar interoperability goal to DC (URL_TO_INSERT_RECORD_3479 https://fairsharing.org/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD_3481 https://fairsharing.org/3547) AT (URL_TO_INSERT_RECORD_3471 https://fairsharing.org/FAIRsharing.3a96ae)  (URL_TO_INSERT_RECORD_3476 https://fairsharing.org/FAIRsharing.h4j3qm)  but a more general-purpose scope.

The original DATS (URL_TO_INSERT_RECORD_3492 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_3486 https://fairsharing.org/search?recordType=model_and_format)  centered around concept of a "Dataset", an entity that covers technical aspects such as licensing, data types and distributions. The Dataset is produced by or is the input or output of a “Study”, which contains elements that are specific to life, environmental and biomedical science domains, and which model (URL_TO_INSERT_TERM_3487 https://fairsharing.org/search?recordType=model_and_format) s experimental processes, cohorts and protocol informat (URL_TO_INSERT_TERM_3489 https://fairsharing.org/search?recordType=model_and_format) ion. To meet the requirements of project (URL_TO_INSERT_TERM_3484 https://fairsharing.org/search?recordType=project) -generated datasets, the DATS (URL_TO_INSERT_RECORD_3493 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_3488 https://fairsharing.org/search?recordType=model_and_format)  was extended to include the third core (URL_TO_INSERT_RECORD_3491 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_3494 https://fairsharing.org/FAIRsharing.xMmOCL)  concept of “Project (URL_TO_INSERT_TERM_3485 https://fairsharing.org/search?recordType=project) ”, covering general informat (URL_TO_INSERT_TERM_3490 https://fairsharing.org/search?recordType=model_and_format) ion such as title, publications, funding and contributors.


### Core objects

The DATS (URL_TO_INSERT_RECORD_3499 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_3497 https://fairsharing.org/search?recordType=model_and_format)  centres around three core (URL_TO_INSERT_RECORD_3498 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_3500 https://fairsharing.org/FAIRsharing.xMmOCL)  objects, "Project (URL_TO_INSERT_TERM_3495 https://fairsharing.org/search?recordType=project) ", "Study" and "Dataset", each of which contains a set of sub-objects, which in turn can be nested down to the lowest unitary object (which contains no further objects), which is the “Annotation”. Project (URL_TO_INSERT_TERM_3496 https://fairsharing.org/search?recordType=project) , Study and Dataset relate to each other in a triangular fashion as shown in figure 1.

At first glance, the three core (URL_TO_INSERT_RECORD_3508 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_3513 https://fairsharing.org/FAIRsharing.xMmOCL)  objects make the DATS (URL_TO_INSERT_RECORD_3509 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_3502 https://fairsharing.org/search?recordType=model_and_format)  reminiscent of the ISA (Investigation, Study, Assay) model (URL_TO_INSERT_TERM_3503 https://fairsharing.org/search?recordType=model_and_format)  for describing experimental processes. There are however several key differences between the two. For one, ISA has a waterfall structure whereby any instance of the model (URL_TO_INSERT_TERM_3504 https://fairsharing.org/search?recordType=model_and_format)  has to contain a Study object between an Investigation and an Assay. In DATS (URL_TO_INSERT_RECORD_3510 https://fairsharing.org/FAIRsharing.e20vsd)  on the other hand, it is possible for a Dataset to be directly dependent on a Project (URL_TO_INSERT_TERM_3501 https://fairsharing.org/search?recordType=project) , without any Study informat (URL_TO_INSERT_TERM_3506 https://fairsharing.org/search?recordType=model_and_format) ion. This is relevant for datasets such as knowledge graphs or synthetic datasets, for which no study metadata may be available. Additionally, DATS (URL_TO_INSERT_RECORD_3511 https://fairsharing.org/FAIRsharing.e20vsd)  focuses on the technical details, availability and use restrictions of datasets whereas the purpose of the ISA model (URL_TO_INSERT_TERM_3505 https://fairsharing.org/search?recordType=model_and_format)  is to describe experimental procedures in great detail. While the DATS (URL_TO_INSERT_RECORD_3512 https://fairsharing.org/FAIRsharing.e20vsd)  Study covers some of this informat (URL_TO_INSERT_TERM_3507 https://fairsharing.org/search?recordType=model_and_format) ion, it is much less comprehensive or central to the captured data than for ISA.

#### Project

The Project (URL_TO_INSERT_TERM_3514 https://fairsharing.org/search?recordType=project)  object was not part of the original version of DATS (URL_TO_INSERT_RECORD_3519 https://fairsharing.org/FAIRsharing.e20vsd) . It was added in the second version as a means of linking different studies and datasets under one common parent as well as capturing informat (URL_TO_INSERT_TERM_3517 https://fairsharing.org/search?recordType=model_and_format) ion such as project (URL_TO_INSERT_TERM_3515 https://fairsharing.org/search?recordType=project)  contacts or consortium informat (URL_TO_INSERT_TERM_3518 https://fairsharing.org/search?recordType=model_and_format) ion, publications not linked to one specific study, funding sources, project (URL_TO_INSERT_TERM_3516 https://fairsharing.org/search?recordType=project)  websites and start/end dates.

#### Study

The Study object, although part of the original DATS (URL_TO_INSERT_RECORD_3522 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_3520 https://fairsharing.org/search?recordType=model_and_format) , had a less central role in the first iteration than it has in this latest one. Capturing the context in which the Dataset was either generated or used, the Study provides informat (URL_TO_INSERT_TERM_3521 https://fairsharing.org/search?recordType=model_and_format) ion about the type of study undertaken (e.g. clinical trials or chemical toxicity screens), cohorts (or "studyGroups), input materials, selection criteria and the steps involved in the study. 

#### Dataset

The Dataset object was the central concept of the initial DATS (URL_TO_INSERT_RECORD_3529 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_3525 https://fairsharing.org/search?recordType=model_and_format)  but became an equal part in the `Project (URL_TO_INSERT_TERM_3524 https://fairsharing.org/search?recordType=project) -Study-Dataset` triangle in version 2. The object captures technical informat (URL_TO_INSERT_TERM_3527 https://fairsharing.org/search?recordType=model_and_format) ion about the dataset, such as file types, data standard (URL_TO_INSERT_TERM_3523 https://fairsharing.org/search?fairsharingRegistry=Standard) s, versions and licensing as well as links to the actual data if available. It also model (URL_TO_INSERT_TERM_3526 https://fairsharing.org/search?recordType=model_and_format) s informat (URL_TO_INSERT_TERM_3528 https://fairsharing.org/search?recordType=model_and_format) ion related to the creation of the dataset such as input materials, diseases, biological entities and other similar objects, as well as the types of experiments from which the dataset was derived and any associated dimensions (URL_TO_INSERT_RECORD_3530 https://fairsharing.org/FAIRsharing.9af33c)  or components.

### Sub-objects

Each of the three top-level objects references a range of sub-objects, which in turn contain further sub-objects, down to the lowest unitary object (which contains no further objects), which is the “Annotation”. An “Annotation” consists of just two key-value pairs, the “value” and, optionally, the “valueIRI”, designed to capture the Internationalized Resource Identifier (URL_TO_INSERT_TERM_3533 https://fairsharing.org/search?recordType=identifier_schema)  (IRI) of an ontology (URL_TO_INSERT_TERM_3532 https://fairsharing.org/search?recordType=terminology_artefact)  term contextualising the free text “value”. Due to this nested object structure, DATS (URL_TO_INSERT_RECORD_3534 https://fairsharing.org/FAIRsharing.e20vsd)  can be quite opaque to parse for the human reader but allows for easier programmatic processing of the objects. A full overview of the DATS (URL_TO_INSERT_RECORD_3535 https://fairsharing.org/FAIRsharing.e20vsd)  schema can be found on the [DataTagSuite Github (URL_TO_INSERT_RECORD_3536 https://fairsharing.org/FAIRsharing.c55d5e)  repository (URL_TO_INSERT_TERM_3531 https://fairsharing.org/search?recordType=repository) ](https://github.com (URL_TO_INSERT_RECORD_3537 https://fairsharing.org/FAIRsharing.c55d5e) /datatagsuite/schema).

### Ontology annotations

The provision for ontology (URL_TO_INSERT_TERM_3541 https://fairsharing.org/search?recordType=terminology_artefact)  annotations is at the core (URL_TO_INSERT_RECORD_3544 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_3546 https://fairsharing.org/FAIRsharing.xMmOCL)  of the DATS (URL_TO_INSERT_RECORD_3545 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_3538 https://fairsharing.org/search?recordType=model_and_format) , with the smallest object available in the model (URL_TO_INSERT_TERM_3539 https://fairsharing.org/search?recordType=model_and_format)  being the `Annotation` schema, which simply consists of two key-value pairs: `value`, which can contain a text string (URL_TO_INSERT_RECORD_3547 https://fairsharing.org/FAIRsharing.9b7wvk)  or number (to allow for coded values), and `valueIRI`, which contains a URI (URL_TO_INSERT_RECORD_3543 https://fairsharing.org/FAIRsharing.d261e1) -format (URL_TO_INSERT_TERM_3540 https://fairsharing.org/search?recordType=model_and_format) ted string (URL_TO_INSERT_RECORD_3548 https://fairsharing.org/FAIRsharing.9b7wvk)  representing a concept or ontology (URL_TO_INSERT_TERM_3542 https://fairsharing.org/search?recordType=terminology_artefact)  term associated with the value. It should be noted that the Annotation object has no required properties, so the valueIRI in particular can be empty. 

The model (URL_TO_INSERT_TERM_3549 https://fairsharing.org/search?recordType=model_and_format)  also provides an extension mechanism through a schema object called `CategoryValuesPair`. This allows the addition of extra properties to the entities in cases where there are no specific properties to deal with the desired property. In order to capture the semantics of the category, CategoryValuesPairs capture both a `category` as a free-text string (URL_TO_INSERT_RECORD_3553 https://fairsharing.org/FAIRsharing.9b7wvk)  and a `categoryIRI` for the URI (URL_TO_INSERT_RECORD_3552 https://fairsharing.org/FAIRsharing.d261e1)  of an associated ontology (URL_TO_INSERT_TERM_3550 https://fairsharing.org/search?recordType=terminology_artefact)  context. The `values` are of type `Annotation` and can therefore also have ontology (URL_TO_INSERT_TERM_3551 https://fairsharing.org/search?recordType=terminology_artefact)  annotations.

DATS (URL_TO_INSERT_RECORD_3556 https://fairsharing.org/FAIRsharing.e20vsd)  does not prescribe the use of specific ontologies (URL_TO_INSERT_TERM_3555 https://fairsharing.org/search?recordType=terminology_artefact)  in relation to various properties, although it would be advisable to include this type of restriction in a given implementation of the model (URL_TO_INSERT_TERM_3554 https://fairsharing.org/search?recordType=model_and_format)  in order to simply the interoperability between different objects of the same type.

### Encoding in JSON-LD

DATS (URL_TO_INSERT_RECORD_3570 https://fairsharing.org/FAIRsharing.e20vsd)  objects are encoded in JSO (URL_TO_INSERT_RECORD_3576 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_3572 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_3583 https://fairsharing.org/FAIRsharing.8f9bbb) , a method for encoding linked data in the open standard (URL_TO_INSERT_TERM_3557 https://fairsharing.org/search?fairsharingRegistry=Standard)  file and data interchange format (URL_TO_INSERT_TERM_3561 https://fairsharing.org/search?recordType=model_and_format)  JSO (URL_TO_INSERT_RECORD_3577 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_3573 https://fairsharing.org/FAIRsharing.5bbab9) . JSO (URL_TO_INSERT_RECORD_3578 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_3574 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_3584 https://fairsharing.org/FAIRsharing.8f9bbb)  is designed around the concept of a "context" to provide additional map (URL_TO_INSERT_RECORD_3581 https://fairsharing.org/FAIRsharing.53edcc) pings from JSO (URL_TO_INSERT_RECORD_3579 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_3575 https://fairsharing.org/FAIRsharing.5bbab9)  to an RDF (URL_TO_INSERT_RECORD_3565 https://fairsharing.org/FAIRsharing.p77ph9)  model (URL_TO_INSERT_TERM_3558 https://fairsharing.org/search?recordType=model_and_format) . DATS (URL_TO_INSERT_RECORD_3571 https://fairsharing.org/FAIRsharing.e20vsd)  provides three sets of context map (URL_TO_INSERT_RECORD_3582 https://fairsharing.org/FAIRsharing.53edcc) pings, to DC (URL_TO_INSERT_RECORD_3585 https://fairsharing.org/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD_3587 https://fairsharing.org/3547) AT (URL_TO_INSERT_RECORD_3563 https://fairsharing.org/FAIRsharing.3a96ae)  (URL_TO_INSERT_RECORD_3566 https://fairsharing.org/FAIRsharing.h4j3qm) , schema.org (URL_TO_INSERT_RECORD_3590 https://fairsharing.org/FAIRsharing.hzdzq8)  (SDO (URL_TO_INSERT_RECORD_3589 https://fairsharing.org/FAIRsharing.7s74s8) ) and the OBO (URL_TO_INSERT_RECORD_3569 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_3580 https://fairsharing.org/FAIRsharing.cbz72b)  Foundry (URL_TO_INSERT_RECORD_3568 https://fairsharing.org/FAIRsharing.847069)  Ontologies (URL_TO_INSERT_TERM_3562 https://fairsharing.org/search?recordType=terminology_artefact) . None of the three sets of contexts individually cover all properties in the model (URL_TO_INSERT_TERM_3559 https://fairsharing.org/search?recordType=model_and_format)  but they can be used in combination to maximise the semantic linking of the model (URL_TO_INSERT_TERM_3560 https://fairsharing.org/search?recordType=model_and_format) , likely to increase interoperability, for instance with DC (URL_TO_INSERT_RECORD_3586 https://fairsharing.org/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD_3588 https://fairsharing.org/3547) AT (URL_TO_INSERT_RECORD_3564 https://fairsharing.org/FAIRsharing.3a96ae)  (URL_TO_INSERT_RECORD_3567 https://fairsharing.org/FAIRsharing.h4j3qm)  based catalogues.



## Implementing DATS in a data catalogue

We implemented DATS (URL_TO_INSERT_RECORD_3593 https://fairsharing.org/FAIRsharing.e20vsd)  v2.0 in the [IMI Translational Data Catalog (URL_TO_INSERT_RECORD_3595 https://fairsharing.org/FAIRsharing.de533c) ](https://datacatalog.elixir-luxembourg.org (URL_TO_INSERT_RECORD_3597 https://fairsharing.org/FAIRsharing.de533c) /). The DATS (URL_TO_INSERT_RECORD_3594 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_3591 https://fairsharing.org/search?recordType=model_and_format) 's flexibility presents both a benefit and a challenge in that some concepts could be encoded in a number of ways. Experimental materials for example can be encoded at both the Study level, in `Study.input` or at the Dataset level, in `Dataset.isAbout`. In order to encode metadata consistently and simplify indexing and display processes for the IMI Data Catalog (URL_TO_INSERT_RECORD_3596 https://fairsharing.org/FAIRsharing.de533c) , we therefore made a number of assumptions about how to encode certain metadata entities in the model (URL_TO_INSERT_TERM_3592 https://fairsharing.org/search?recordType=model_and_format) .

### Assumptions

* Study and Dataset objects can't exist without a Project (URL_TO_INSERT_TERM_3598 https://fairsharing.org/search?recordType=project) . This rule was necessary to provide a root for our indexing service.

* The Study object encodes informat (URL_TO_INSERT_TERM_3599 https://fairsharing.org/search?recordType=model_and_format) ion about the input materials to the experiment, such as study subjects in the case of clinical trials or biological molecules in the case of chemical assays. At this level, we collect cohort descriptions, sample sizes, sample sources, types of samples and diseases.
 
* The Dataset object encodes informat (URL_TO_INSERT_TERM_3601 https://fairsharing.org/search?recordType=model_and_format) ion about the dataset, including technical informat (URL_TO_INSERT_TERM_3602 https://fairsharing.org/search?recordType=model_and_format) ion such as version number, creation and update dates, data standard (URL_TO_INSERT_TERM_3600 https://fairsharing.org/search?fairsharingRegistry=Standard) s and file types. The dataset also lists the experiment types that generated the data, the number and types of samples that contributed to the dataset and any diseases in the samples. These properties can be distinct from the ones at Study level as not all samples collected in a Study may be used to generate a given dataset, e.g. blood samples might be used for sequencing experiments, generating a sequencing dataset, while other tissue samples are used in imaging assays, generating an imaging dataset. The number of samples collected can be different from the cohort sample size (i.e. number of subject), either because multiple samples were collected from each subject or because some samples were excluded from the dataset for quality reasons.

* In the implementation of the model (URL_TO_INSERT_TERM_3603 https://fairsharing.org/search?recordType=model_and_format) , preference as given to specific ontologies (URL_TO_INSERT_TERM_3604 https://fairsharing.org/search?recordType=terminology_artefact)  in certain contexts, eg MO (URL_TO_INSERT_RECORD_3616 https://fairsharing.org/FAIRsharing.qs4x5m) NDO (URL_TO_INSERT_RECORD_3611 https://fairsharing.org/FAIRsharing.b2979t)  for diseases, UBERO (URL_TO_INSERT_RECORD_3605 https://fairsharing.org/FAIRsharing.nwgynk)  (URL_TO_INSERT_RECORD_3608 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_3612 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_3614 https://fairsharing.org/FAIRsharing.cp0ybc) N (URL_TO_INSERT_RECORD_3607 https://fairsharing.org/FAIRsharing.4c0b6b)  for anatomical components, NCIt (URL_TO_INSERT_RECORD_3606 https://fairsharing.org/FAIRsharing.4cvwxa) , EFO (URL_TO_INSERT_RECORD_3613 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_3615 https://fairsharing.org/FAIRsharing.ca63ce)  and OBI (URL_TO_INSERT_RECORD_3610 https://fairsharing.org/FAIRsharing.284e1z)  for experiment types, UO (URL_TO_INSERT_RECORD_3609 https://fairsharing.org/FAIRsharing.mjnypw)  for units etc.

---

## Conclusion

> * DATS (URL_TO_INSERT_RECORD_3618 https://fairsharing.org/FAIRsharing.e20vsd)  is a flexible data model (URL_TO_INSERT_TERM_3617 https://fairsharing.org/search?recordType=model_and_format)  aimed at biomedical datasets.
> * DATS (URL_TO_INSERT_RECORD_3620 https://fairsharing.org/FAIRsharing.e20vsd)  utilises the power of JSO (URL_TO_INSERT_RECORD_3622 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_3621 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_3623 https://fairsharing.org/FAIRsharing.8f9bbb)  to encode semantics at all levels of the model (URL_TO_INSERT_TERM_3619 https://fairsharing.org/search?recordType=model_and_format) .
> * DATS (URL_TO_INSERT_RECORD_3625 https://fairsharing.org/FAIRsharing.e20vsd) ' flexibility does mean that consistent implementation of the model (URL_TO_INSERT_TERM_3624 https://fairsharing.org/search?recordType=model_and_format)  in a specific context requires assumptions to be made.


### What should I read next?
> * [Building a catalogue of datasets](./data-catalog.md) 
> * [Deploying the IMI data catalog](./data-catalog-deployment.md) 
> * [Introduction to terminologies (URL_TO_INSERT_TERM_3626 https://fairsharing.org/search?recordType=terminology_artefact)  and ontologies (URL_TO_INSERT_TERM_3628 https://fairsharing.org/search?recordType=terminology_artefact) ](../interoperability/introduction-terminologies (URL_TO_INSERT_TERM_3627 https://fairsharing.org/search?recordType=terminology_artefact) -ontologies (URL_TO_INSERT_TERM_3629 https://fairsharing.org/search?recordType=terminology_artefact) .md)

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

