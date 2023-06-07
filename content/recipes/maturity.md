(fcb-maturity)=
# Changing culture with the Dataset Maturity Model

<!--
````{panels_fairplus}
:identifier_text: FCB081
:identifier_link: 'https://w3id.org/faircookbook/FCB081'
:difficulty_level: 3
:recipe_type: guidance
:reading_time_minutes: 30
:intended_audience: principal_investigator, data_manager, data_scientist  
:maturity_level: 0
:maturity_indicator: 0
:has_executable_code: nope
:recipe_name: Changing culture with the Dataset Maturity Model
```` 
-->

## Abstract

The present content introduces the FAIRplus "Dataset Maturity Model", shows how to use it in the context of a 
FAIRification process to decide how far to go on a FAIR journey.
We also show how each FAIR Cookbook recipes has been anchored to the model.
Recipes can therefore be assembled to build a coherent path which should guarantee that datasets handled according 
to the recommendations can meet data management expectations in terms of FAIRness.
Therefore, the FAIRplus DSM provides a handy tool for data managers to advise on changing the culture of data management 
but also manage expectations (and costs) when devising a FAIRification program for specific domains and digital objects
living in that space.

## Background

Maturity models are not new. There are in fact training programs specifically designed for this such as the
**Capability Maturity Model Integration (CMMI)** {footcite}`cmmi`.
These models originate from engineering and manufacturing fields, in particular the military and aerospace industries, 
as means to rate the reliability and degree of development of a particular technology, skill or process,
in other words, a capability. 
Notions such as **Technical Readiness Levels**  or TRLs define a scale of 9 levels to rate
a process from basic idea to production grade technology. 

With the digitization of society and the pervasiveness of digital technology, the life sciences, as other fields, are 
wrestling with the challenges of data management as defined in  the *Fourth paradigm: Data-intensive Scientific Discovery*
{footcite}`hey2009`. 
Organizations need to decide how to allocate resources to increase the impact of digital artefacts as they are created. 
Large amounts of literature exist detailing the key ideas for handling data. A resource such as the *DAMA book* covers in 
great depths the fundamental operations and challenges associated with data management activities {footcite}`DAMA-DMBOOK`.

More recently, The FAIR principles articulated key requirements and properties data should have {footcite}`pmid26978244`.
Following this important work, a number of initiatives have worked at producing domain specific maturity indicators. 
Among these initiatives, the Research Data Alliance Maturity Indicators seem to have gain notoriety
{footcite}`RDAindicators`.

Building on these efforts, the FAIRplus project has developed a more targeted approach by focusing on the notion of 
dataset. 

## Presentation of the FAIRplus Dataset Maturity Model (DSM)

The FAIRplus Dataset Maturity Model proposes a framework to incorporate key concepts defined by the Capability and
Maturity Models and apply them to define maturity levels which can used to describe a dataset.

For a comprehensive overview of the FAIRplus Dataset Maturity Model, refer to the [dedicated site](https://fairplus.github.io/Data-Maturity/),
a screenshot of which is presented below.

````{dropdown} **FAIR DSM**
:open:

```{figure} ../../images/maturity_img_1.png
---
width: 700px
name: FAIR Dataset Maturity Model
alt:  FAIR Dataset Maturity Model
---
 FAIR Dataset Maturity Model
```
````


## Integrating the FAIRplus Dataset Maturity Model in the FAIRplus Cookbook

Each recipe in the FAIRplus Cookbook now incorporates one or more FAIRplus DSM indicators.

These can be found in the **Recipe Card**. 

They are there to provide our readership with a pointer to the level of data set maturity they can expect to meet if
they apply and implement the recipe.

The FAIR DSM indicators are also used to browse the recipes through the lense of maturity improvements level, which is
of interest. 

Finally, the FAIR Cookbook produced specific content available as jupyter notebooks which use the familiar Investigation Study Assay model {footcite}`pmid20679334` 
and Research Objects {footcite}`sefton_peter_2022_5841615` to showcase how users can move through maturity levels and decide for themselves how far they need to go along the scale.


````{dropdown} **FAIR DSM**
:open:

```{figure} ../../images/maturity_img.png
---
width: 450px
name: FAIR DSM indicators in the FAIR Cookbook Recipe card
alt:  FAIR DSM indicators in the FAIR Cookbook Recipe card
---
 FAIR DSM indicators in the FAIR Cookbook Recipe card
```
````




## Assessing FAIRplus intervention


The FAIRplus DSM has subsequently been used to assess the effectiveness of interventions on datasets presented 
to FAIRplus experts.

Each of the 20 projects, which have interacted with FAIRplus, have been subjected to a standard protocol looking at
FAIR maturity before and after intervention, when performing retrospective processing of the data. 
In few instances, the effect of prospective interventions could also be measured. 

FAIRplus DSM developed a dedicated manual assessment template.

### Training the assessor

As with any tool, familiarization and training are necessary to ensure that the personnel carrying out the evaluations 
can use the framework in a consistent fashion. 


### Performing the assessment

The FAIRplus DSM group therefore recruited FAIR experts and over the
course of a dedicated workshop presented the DSM model, proposed exercises and then asked participants to rate several
datasets independently.

The next step consisted in evaluating the inter-rater agreement when using the framework.

A debriefing of the rating was carried out and was the ideal opportunity to clarify any misunderstandings about the
indicator definitions and therefore reconcile rating discrepancies between the participant.
Difference in interpretations
were identified leading in a refinement of the definitions and improvement of the documentation of the
FAIRplus dataset maturity model.
It also resulted in streamlining both the training program and the evaluation program.

The following figure shows the effect of a FAIRification process on an IMI eTOX dataset.

````{dropdown} **FAIR DSM image 1**
:open:

```{figure} ../../images/DSMeval-img1.png
---
width: 800px
name: FAIR DSM indicators before and after intervention-Content
alt:   FAIR DSM indicators before and after intervention-Content
---
FAIR DSM indicators before and after intervention-Content
```
````

---

````{dropdown} **FAIR DSM image 2**
:open:

```{figure} ../../images/DSMeval-img2.png
---
width: 800px
name: FAIR DSM indicators before and after intervention-Format
alt:   FAIR DSM indicators before and after intervention-Format
---
FAIR DSM indicators before and after intervention-Format
```
````


---


````{dropdown} **FAIR DSM image 3**
:open:

```{figure} ../../images/DSMeval-img3.png
---
width: 800px
name: FAIR DSM indicators before and after intervention-Access
alt:  FAIR DSM indicators before and after intervention-Access
---
FAIR DSM indicators before and after intervention-Access
```
````



## Conclusions: It is about changing the data management culture!

The FAIRplus Dataset Maturity Model (DSM) developed by the consortium is proving a valuable tool for Data Managers, 
Decision Makers and Data Scientist to identify the weak points in their FAIRification strategies or more simply to define
the level of maturity they are capable of delivery within the constraints of the project or research program.
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

