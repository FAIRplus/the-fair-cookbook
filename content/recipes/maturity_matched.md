(fcb-maturity)=
# Changing culture with the Dataset Maturity Model

<!--
````{panels_fairplus}
:identifier (URL_TO_INSERT_TERM_5564 https://fairsharing.org/search?recordType=identifier_schema) _text: FCB081
:identifier (URL_TO_INSERT_TERM_5565 https://fairsharing.org/search?recordType=identifier_schema) _link: 'https://w3id.org (URL_TO_INSERT_RECORD-HOMEPAGE_5566 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB081'
:difficulty_level: 3
:recipe_type: guidance
:reading_time_minutes: 30
:intended_audience: principal_investigator, data_manager, data_scientist  
:maturity_level: 0
:maturity_indicator: 0
:has_executable_code: nope
:recipe_name: Changing culture with the Dataset Maturity Model (URL_TO_INSERT_TERM_5567 https://fairsharing.org/search?recordType=model_and_format) 
```` 
-->

## Abstract

The present content introduces the FAIRplus "Dataset Maturity Model (URL_TO_INSERT_TERM_5568 https://fairsharing.org/search?recordType=model_and_format) ", shows how to use it in the context of a 
FAIRification process to decide how far to go on a FAIR (URL_TO_INSERT_RECORD-ABBREV_5569 https://fairsharing.org/FAIRsharing.WWI10U)  journey.
We also show how each FAIR (URL_TO_INSERT_RECORD-ABBREV_5571 https://fairsharing.org/FAIRsharing.WWI10U)  Cookbook recipes has been anchored to the model (URL_TO_INSERT_TERM_5570 https://fairsharing.org/search?recordType=model_and_format) .
Recipes can therefore be assembled to build a coherent path which should guarantee that datasets handled according 
to the recommendations can meet data management expectations in terms of FAIRness.
Therefore, the FAIRplus DSM provides a handy tool for data managers to advise on changing the culture of data management 
but also manage expectations (and costs) when devising a FAIRification program for specific domains and digital objects
living in that space.

## Background

Maturity model (URL_TO_INSERT_TERM_5572 https://fairsharing.org/search?recordType=model_and_format) s are not new. There are in fact training programs specifically designed for this such as the
**Capability Maturity Model (URL_TO_INSERT_TERM_5573 https://fairsharing.org/search?recordType=model_and_format)  Integration (CMMI)** {footcite}`cmmi`.
These model (URL_TO_INSERT_TERM_5574 https://fairsharing.org/search?recordType=model_and_format) s originate from engineering and manufacturing fields, in particular the military and aerospace industries, 
as means to rate the reliability and degree of development of a particular technology, skill or process,
in other words, a capability. 
Notions such as **Technical Readiness Levels**  or TRLs define a scale of 9 levels to rate
a process from basic idea to production grade technology. 

With the digitization of society (URL_TO_INSERT_TERM_5575 https://fairsharing.org/search?recordType=society)  and the pervasiveness of digital technology, the life sciences, as other fields, are 
wrestling with the challenges of data management as defined in  the *Fourth paradigm: Data-intensive Scientific Discovery*
{footcite}`hey2009`. 
Organizations need to decide how to allocate resources to increase the impact of digital artefacts as they are created. 
Large amounts of literature exist detailing the key ideas for handling data. A resource such as the *DAMA book* covers in 
great depths the fundamental operations and challenges associated with data management activities {footcite}`DAMA-DMBOOK`.

More recently, The FAIR (URL_TO_INSERT_RECORD-ABBREV_5577 https://fairsharing.org/FAIRsharing.WWI10U)  principles (URL_TO_INSERT_RECORD-NAME_5576 https://fairsharing.org/FAIRsharing.WWI10U)  articulated key requirements and properties data should have {footcite}`pmid26978244`.
Following this important work, a number of initiatives have worked at producing domain specific maturity indicators. 
Among these initiatives, the Research Data Alliance Maturity Indicators seem to have gain notoriety
{footcite}`RDAindicators`.

Building on these efforts, the FAIRplus project (URL_TO_INSERT_TERM_5578 https://fairsharing.org/search?recordType=project)  has developed a more targeted approach by focusing on the notion of 
dataset. 

## Presentation of the FAIRplus Dataset Maturity Model (DSM)

The FAIRplus Dataset Maturity Model (URL_TO_INSERT_TERM_5579 https://fairsharing.org/search?recordType=model_and_format)  proposes a framework to incorporate key concepts defined by the Capability and
Maturity Model (URL_TO_INSERT_TERM_5580 https://fairsharing.org/search?recordType=model_and_format) s and apply them to define maturity levels which can used to describe a dataset.

For a comprehensive overview of the FAIRplus Dataset Maturity Model (URL_TO_INSERT_TERM_5581 https://fairsharing.org/search?recordType=model_and_format) , refer to the [dedicated site](https://fairplus.github.io/Data-Maturity/),
a screenshot of which is presented below.

````{dropdown} **FAIR DSM**
:open:

```{figure} ../../images/maturity_img_1.png
---
width: 700px
name: FAIR (URL_TO_INSERT_RECORD-ABBREV_5583 https://fairsharing.org/FAIRsharing.WWI10U)  Dataset Maturity Model (URL_TO_INSERT_TERM_5582 https://fairsharing.org/search?recordType=model_and_format) 
alt:  FAIR (URL_TO_INSERT_RECORD-ABBREV_5585 https://fairsharing.org/FAIRsharing.WWI10U)  Dataset Maturity Model (URL_TO_INSERT_TERM_5584 https://fairsharing.org/search?recordType=model_and_format) 
---
 FAIR (URL_TO_INSERT_RECORD-ABBREV_5587 https://fairsharing.org/FAIRsharing.WWI10U)  Dataset Maturity Model (URL_TO_INSERT_TERM_5586 https://fairsharing.org/search?recordType=model_and_format) 
```
````


## Integrating the FAIRplus Dataset Maturity Model in the FAIRplus Cookbook

Each recipe in the FAIRplus Cookbook now incorporates one or more FAIRplus DSM indicators.

These can be found in the **Recipe Card**. 

They are there to provide our readership with a pointer to the level of data set maturity they can expect to meet if
they apply and implement the recipe.

The FAIR (URL_TO_INSERT_RECORD-ABBREV_5588 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators are also used to browse the recipes through the lense of maturity improvements level, which is
of interest. 

Finally, the FAIR (URL_TO_INSERT_RECORD-ABBREV_5590 https://fairsharing.org/FAIRsharing.WWI10U)  Cookbook produced specific content available as jupyter notebooks which use the familiar Investigation Study Assay model (URL_TO_INSERT_TERM_5589 https://fairsharing.org/search?recordType=model_and_format)  {footcite}`pmid20679334` 
and Research Objects {footcite}`sefton_peter_2022_5841615` to showcase how users can move through maturity levels and decide for themselves how far they need to go along the scale.


````{dropdown} **FAIR DSM**
:open:

```{figure} ../../images/maturity_img.png
---
width: 450px
name: FAIR (URL_TO_INSERT_RECORD-ABBREV_5591 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators in the FAIR (URL_TO_INSERT_RECORD-ABBREV_5592 https://fairsharing.org/FAIRsharing.WWI10U)  Cookbook Recipe card
alt:  FAIR (URL_TO_INSERT_RECORD-ABBREV_5593 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators in the FAIR (URL_TO_INSERT_RECORD-ABBREV_5594 https://fairsharing.org/FAIRsharing.WWI10U)  Cookbook Recipe card
---
 FAIR (URL_TO_INSERT_RECORD-ABBREV_5595 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators in the FAIR (URL_TO_INSERT_RECORD-ABBREV_5596 https://fairsharing.org/FAIRsharing.WWI10U)  Cookbook Recipe card
```
````




## Assessing FAIRplus intervention


The FAIRplus DSM has subsequently been used to assess the effectiveness of interventions on datasets presented 
to FAIRplus experts.

Each of the 20 project (URL_TO_INSERT_TERM_5598 https://fairsharing.org/search?recordType=project) s, which have interacted with FAIRplus, have been subjected to a standard (URL_TO_INSERT_TERM_5597 https://fairsharing.org/search?fairsharingRegistry=Standard)  protocol looking at
FAIR (URL_TO_INSERT_RECORD-ABBREV_5599 https://fairsharing.org/FAIRsharing.WWI10U)  maturity before and after intervention, when performing retrospective processing of the data. 
In few instances, the effect of prospective interventions could also be measured. 

FAIRplus DSM developed a dedicated manual assessment template.

### Training the assessor

As with any tool, familiarization and training are necessary to ensure that the personnel carrying out the evaluations 
can use the framework in a consistent fashion. 


### Performing the assessment

The FAIRplus DSM group therefore recruited FAIR (URL_TO_INSERT_RECORD-ABBREV_5600 https://fairsharing.org/FAIRsharing.WWI10U)  experts and over the
course of a dedicated workshop presented the DSM model (URL_TO_INSERT_TERM_5601 https://fairsharing.org/search?recordType=model_and_format) , proposed exercises and then asked participants to rate several
datasets independently.

The next step consisted in evaluating the inter-rater agreement when using the framework.

A debriefing of the rating was carried out and was the ideal opportunity to clarify any misunderstandings about the
indicator definitions and therefore reconcile rating discrepancies between the participant.
Difference in interpretations
were identified leading in a refinement of the definitions and improvement of the documentation of the
FAIRplus dataset maturity model (URL_TO_INSERT_TERM_5602 https://fairsharing.org/search?recordType=model_and_format) .
It also resulted in streamlining both the training program and the evaluation program.

The following figure shows the effect of a FAIRification process on an IMI eTOX dataset.

````{dropdown} **FAIR DSM image 1**
:open:

```{figure} ../../images/DSMeval-img1.png
---
width: 800px
name: FAIR (URL_TO_INSERT_RECORD-ABBREV_5603 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Content
alt:   FAIR (URL_TO_INSERT_RECORD-ABBREV_5604 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Content
---
FAIR (URL_TO_INSERT_RECORD-ABBREV_5605 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Content
```
````

---

````{dropdown} **FAIR DSM image 2**
:open:

```{figure} ../../images/DSMeval-img2.png
---
width: 800px
name: FAIR (URL_TO_INSERT_RECORD-ABBREV_5607 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Format (URL_TO_INSERT_TERM_5606 https://fairsharing.org/search?recordType=model_and_format) 
alt:   FAIR (URL_TO_INSERT_RECORD-ABBREV_5609 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Format (URL_TO_INSERT_TERM_5608 https://fairsharing.org/search?recordType=model_and_format) 
---
FAIR (URL_TO_INSERT_RECORD-ABBREV_5611 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Format (URL_TO_INSERT_TERM_5610 https://fairsharing.org/search?recordType=model_and_format) 
```
````


---


````{dropdown} **FAIR DSM image 3**
:open:

```{figure} ../../images/DSMeval-img3.png
---
width: 800px
name: FAIR (URL_TO_INSERT_RECORD-ABBREV_5612 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Access
alt:  FAIR (URL_TO_INSERT_RECORD-ABBREV_5613 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Access
---
FAIR (URL_TO_INSERT_RECORD-ABBREV_5614 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Access
```
````



## Conclusions: It is about changing the data management culture!

The FAIRplus Dataset Maturity Model (URL_TO_INSERT_TERM_5615 https://fairsharing.org/search?recordType=model_and_format)  (DSM) developed by the consortium is proving a valuable tool for Data Managers, 
Decision Makers and Data Scientist to identify the weak points in their FAIRification strategies or more simply to define
the level of maturity they are capable of delivery within the constraints of the project (URL_TO_INSERT_TERM_5616 https://fairsharing.org/search?recordType=project)  or research program.
The FAIRplus DSM, following a minimal familiarization and training period, provides the means to effective quantity and 
articulate on FAIRification strategies and choke points. Therefore, by enabling a clearer way for communicating and talking
about FAIRification process, the FAIRplus DSM constitutes an excellent tool to plan and enable changes in the way datasets
can be managed


### What to read next?

 
Moving through maturity levels with ISA by running the following notebooks in the indicated order:

- [improving dataset maturity: the MIAPPE use case](https://w3id.org/faircookbook/FCB062) 
- [create-a-simple-isa-descriptor](https://w3id.org/faircookbook/FCB063)
- [isa-api-programmatic-rebuild-of-BII-S-3](https://w3id.org/faircookbook/FCB064)
- [isa-json-conversion-to-rdf-linked-data](https://w3id.org/faircookbook/FCB064)
- [isa-as-ro](https://w3id.org/faircookbook/FCB066)


````{panels}
:column: col-md-4
:card: border-2
:header: bg-primary pa_dark
```{image} ../../images/logos/pistoia_logo.png
:height: 40px
:align: center
:name: FAIRtoolkit_logo
```
^^^
[The Pistoia Alliance FAIRtoolkit Data Capability Maturity Model](https://fairtoolkit.pistoiaalliance.org/methods/data-capability-maturity-model/)
````
````{rdmkit_panel}
````


## Reference

````{dropdown} **References**
```{footbibliography}
```
````




## Authors
````{authors_fairplus}
Ibrahim: Writing & Editing
Philippe: Writing & Editing - Initial Draft
````




## Licence
````{license_fairplus}
CC-BY-4.0
````

