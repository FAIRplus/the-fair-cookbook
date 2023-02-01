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

The present content introduces the FAIR (URL_TO_INSERT_RECORD_10455 https://fairsharing.org/FAIRsharing.WWI10U) plus "Dataset Maturity Model (URL_TO_INSERT_TERM_10454 https://fairsharing.org/search?recordType=model_and_format) ", shows how to use it in the context of a 
FAIR (URL_TO_INSERT_RECORD_10456 https://fairsharing.org/FAIRsharing.WWI10U) ification process to decide how far to go on a FAIR (URL_TO_INSERT_RECORD_10457 https://fairsharing.org/FAIRsharing.WWI10U)  journey.
We also show how each FAIR (URL_TO_INSERT_RECORD_10460 https://fairsharing.org/FAIRsharing.WWI10U)  Cookbook (URL_TO_INSERT_RECORD_10459 https://fairsharing.org/FAIRsharing.cbz72b)  recipes has been anchored to the model (URL_TO_INSERT_TERM_10458 https://fairsharing.org/search?recordType=model_and_format) .
Recipes can therefore be assembled to build a coherent path which should guarantee that datasets handle (URL_TO_INSERT_RECORD_10461 https://fairsharing.org/FAIRsharing.0b7e54) d according 
to the recommendations can meet data management expectations in terms of FAIR (URL_TO_INSERT_RECORD_10462 https://fairsharing.org/FAIRsharing.WWI10U) ness.
Therefore, the FAIR (URL_TO_INSERT_RECORD_10463 https://fairsharing.org/FAIRsharing.WWI10U) plus DSM provides a handy tool for data managers to advise on changing the culture of data management 
but also manage expectations (and costs) when devising a FAIR (URL_TO_INSERT_RECORD_10464 https://fairsharing.org/FAIRsharing.WWI10U) ification program for specific domains and digital objects
living in that space.

## Background

Maturity model (URL_TO_INSERT_TERM_10465 https://fairsharing.org/search?recordType=model_and_format) s are not new. There are in fact training programs specifically designed for this such as the
**Capability Maturity Model (URL_TO_INSERT_TERM_10466 https://fairsharing.org/search?recordType=model_and_format)  Integration (CMMI)** {footcite}`cmmi`.
These model (URL_TO_INSERT_TERM_10467 https://fairsharing.org/search?recordType=model_and_format) s originate from engineering and manufacturing fields, in particular the military and aerospace industries, 
as means to rate the reliability and degree of development of a particular technology, skill or process,
in other words, a capability. 
Notions such as **Technical Readiness Levels**  or TRLs define a scale of 9 levels to rate
a process from basic idea to production grade technology. 

With the digitization of society (URL_TO_INSERT_TERM_10468 https://fairsharing.org/search?recordType=society)  and the pervasiveness of digital technology, the life sciences, as other fields, are 
wrestling with the challenges of data management as defined in  the *Fourth paradigm: Data-intensive Scientific Discovery*
{footcite}`hey2009`. 
Organizations need to decide how to allocate resources to increase the impact of digital artefacts as they are created. 
Large amounts of literature exist detailing the key ideas for handling data. A resource such as the *DAMA (URL_TO_INSERT_RECORD_10470 https://fairsharing.org/FAIRsharing.pdwqcr)  book (URL_TO_INSERT_RECORD_10469 https://fairsharing.org/FAIRsharing.cbz72b) * covers in 
great depths the fundamental operations and challenges associated with data management activities {footcite}`DAMA (URL_TO_INSERT_RECORD_10473 https://fairsharing.org/FAIRsharing.pdwqcr) -DMB (URL_TO_INSERT_RECORD_10474 https://fairsharing.org/FAIRsharing.a1rp4c) O (URL_TO_INSERT_RECORD_10472 https://fairsharing.org/FAIRsharing.cbz72b) OK (URL_TO_INSERT_RECORD_10471 https://fairsharing.org/FAIRsharing.cbz72b) `.

More recently, The FAIR (URL_TO_INSERT_RECORD_10476 https://fairsharing.org/FAIRsharing.WWI10U)  principles (URL_TO_INSERT_RECORD_10475 https://fairsharing.org/FAIRsharing.WWI10U)  articulated key requirements and properties data should have {footcite}`pmid26978244`.
Following this important work, a number of initiatives have worked at producing domain specific maturity indicators. 
Among these initiatives, the Research (URL_TO_INSERT_RECORD_10477 https://fairsharing.org/FAIRsharing.52b22c)  Data Alliance Maturity Indicators seem to have gain notoriety
{footcite}`RDA (URL_TO_INSERT_RECORD_10478 https://fairsharing.org/FAIRsharing.2g5kcb) indicators`.

Building on these efforts, the FAIR (URL_TO_INSERT_RECORD_10480 https://fairsharing.org/FAIRsharing.WWI10U) plus project (URL_TO_INSERT_TERM_10479 https://fairsharing.org/search?recordType=project)  has developed (URL_TO_INSERT_RECORD_10481 https://fairsharing.org/FAIRsharing.31385c)  a more targeted approach by focusing on the notion of 
dataset. 

## Presentation of the FAIRplus Dataset Maturity Model (DSM)

The FAIR (URL_TO_INSERT_RECORD_10483 https://fairsharing.org/FAIRsharing.WWI10U) plus Dataset Maturity Model (URL_TO_INSERT_TERM_10482 https://fairsharing.org/search?recordType=model_and_format)  proposes a framework to incorporate key concepts defined by the Capability and
Maturity Model (URL_TO_INSERT_TERM_10484 https://fairsharing.org/search?recordType=model_and_format) s and apply them to define maturity levels which can used to describe a dataset.

For a comprehensive overview of the FAIR (URL_TO_INSERT_RECORD_10486 https://fairsharing.org/FAIRsharing.WWI10U) plus Dataset Maturity Model (URL_TO_INSERT_TERM_10485 https://fairsharing.org/search?recordType=model_and_format) , refer to the [dedicated site](https://fairplus.github.io/Data-Maturity/),
a screenshot of which is presented below.

````{dropdown} **FAIR DSM**
:open:

```{figure} ../../images/maturity_img_1.png
---
width: 700px
name: FAIR (URL_TO_INSERT_RECORD_10488 https://fairsharing.org/FAIRsharing.WWI10U)  Dataset Maturity Model (URL_TO_INSERT_TERM_10487 https://fairsharing.org/search?recordType=model_and_format) 
alt:  FAIR (URL_TO_INSERT_RECORD_10490 https://fairsharing.org/FAIRsharing.WWI10U)  Dataset Maturity Model (URL_TO_INSERT_TERM_10489 https://fairsharing.org/search?recordType=model_and_format) 
---
 FAIR (URL_TO_INSERT_RECORD_10492 https://fairsharing.org/FAIRsharing.WWI10U)  Dataset Maturity Model (URL_TO_INSERT_TERM_10491 https://fairsharing.org/search?recordType=model_and_format) 
```
````


## Integrating the FAIRplus Dataset Maturity Model in the FAIRplus Cookbook

Each recipe in the FAIR (URL_TO_INSERT_RECORD_10494 https://fairsharing.org/FAIRsharing.WWI10U) plus Cookbook (URL_TO_INSERT_RECORD_10493 https://fairsharing.org/FAIRsharing.cbz72b)  now incorporates one or more FAIR (URL_TO_INSERT_RECORD_10495 https://fairsharing.org/FAIRsharing.WWI10U) plus DSM indicators.

These can be found in the **Recipe Card**. 

They are there to provide our readership with a pointer to the level of data set maturity they can expect to meet if
they apply and implement the recipe.

The FAIR (URL_TO_INSERT_RECORD_10496 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators are also used to browse the recipes through the lense of maturity improvements level, which is
of interest. 

Finally, the FAIR (URL_TO_INSERT_RECORD_10501 https://fairsharing.org/FAIRsharing.WWI10U)  Cookbook (URL_TO_INSERT_RECORD_10498 https://fairsharing.org/FAIRsharing.cbz72b)  produced specific content available as jupyter notebook (URL_TO_INSERT_RECORD_10499 https://fairsharing.org/FAIRsharing.cbz72b) s which use the fam (URL_TO_INSERT_RECORD_10500 https://fairsharing.org/FAIRsharing.d0886a) iliar Investigation Study Assay model (URL_TO_INSERT_TERM_10497 https://fairsharing.org/search?recordType=model_and_format)  {footcite}`pmid20679334` 
and Research (URL_TO_INSERT_RECORD_10502 https://fairsharing.org/FAIRsharing.52b22c)  Objects {footcite}`sefton_peter_2022_5841615` to showcase how users can move through maturity levels and decide for themselves how far they need to go along the scale.


````{dropdown} **FAIR DSM**
:open:

```{figure} ../../images/maturity_img.png
---
width: 450px
name: FAIR (URL_TO_INSERT_RECORD_10504 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators in the FAIR (URL_TO_INSERT_RECORD_10505 https://fairsharing.org/FAIRsharing.WWI10U)  Cookbook (URL_TO_INSERT_RECORD_10503 https://fairsharing.org/FAIRsharing.cbz72b)  Recipe card
alt:  FAIR (URL_TO_INSERT_RECORD_10507 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators in the FAIR (URL_TO_INSERT_RECORD_10508 https://fairsharing.org/FAIRsharing.WWI10U)  Cookbook (URL_TO_INSERT_RECORD_10506 https://fairsharing.org/FAIRsharing.cbz72b)  Recipe card
---
 FAIR (URL_TO_INSERT_RECORD_10510 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators in the FAIR (URL_TO_INSERT_RECORD_10511 https://fairsharing.org/FAIRsharing.WWI10U)  Cookbook (URL_TO_INSERT_RECORD_10509 https://fairsharing.org/FAIRsharing.cbz72b)  Recipe card
```
````




## Assessing FAIRplus intervention


The FAIR (URL_TO_INSERT_RECORD_10512 https://fairsharing.org/FAIRsharing.WWI10U) plus DSM has subsequently been used to assess the effectiveness of interventions on datasets presented 
to FAIR (URL_TO_INSERT_RECORD_10513 https://fairsharing.org/FAIRsharing.WWI10U) plus experts.

Each of the 20 project (URL_TO_INSERT_TERM_10515 https://fairsharing.org/search?recordType=project) s, which have interacted with FAIR (URL_TO_INSERT_RECORD_10516 https://fairsharing.org/FAIRsharing.WWI10U) plus, have been subjected to a standard (URL_TO_INSERT_TERM_10514 https://fairsharing.org/search?fairsharingRegistry=Standard)  protocol looking at
FAIR (URL_TO_INSERT_RECORD_10517 https://fairsharing.org/FAIRsharing.WWI10U)  maturity before and after intervention, when performing retrospective processing of the data. 
In few instances, the effect of prospective interventions could also be measured. 

FAIR (URL_TO_INSERT_RECORD_10518 https://fairsharing.org/FAIRsharing.WWI10U) plus DSM developed (URL_TO_INSERT_RECORD_10519 https://fairsharing.org/FAIRsharing.31385c)  a dedicated manual assessment template.

### Training the assessor

As with any tool, fam (URL_TO_INSERT_RECORD_10520 https://fairsharing.org/FAIRsharing.d0886a) iliarization and training are necessary to ensure that the personnel carrying out the evaluations 
can use the framework in a consistent fashion. 


### Performing the assessment

The FAIR (URL_TO_INSERT_RECORD_10521 https://fairsharing.org/FAIRsharing.WWI10U) plus DSM group therefore recruited FAIR (URL_TO_INSERT_RECORD_10522 https://fairsharing.org/FAIRsharing.WWI10U)  experts and over the
course of a dedicated workshop presented the DSM model (URL_TO_INSERT_TERM_10523 https://fairsharing.org/search?recordType=model_and_format) , proposed exercises and then asked participants to rate several
datasets independently.

The next step consisted in evaluating the inter-rater agreement when using the framework.

A debriefing of the rating was carried out and was the ideal opportunity to clarify any misunderstandings about the
indicator definitions and therefore reconcile rating discrepancies between the participant.
Difference in interpretations
were identified leading in a refinement of the definitions and improvement of the documentation of the
FAIR (URL_TO_INSERT_RECORD_10525 https://fairsharing.org/FAIRsharing.WWI10U) plus dataset maturity model (URL_TO_INSERT_TERM_10524 https://fairsharing.org/search?recordType=model_and_format) .
It also resulted in streamlining both the training program and the evaluation program.

The following figure shows the effect of a FAIR (URL_TO_INSERT_RECORD_10527 https://fairsharing.org/FAIRsharing.WWI10U) ification process on an IMI eTO (URL_TO_INSERT_RECORD_10526 https://fairsharing.org/FAIRsharing.w69t6r) X dataset.

````{dropdown} **FAIR DSM image 1**
:open:

```{figure} ../../images/DSMeval-img1.png
---
width: 800px
name: FAIR (URL_TO_INSERT_RECORD_10528 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Content
alt:   FAIR (URL_TO_INSERT_RECORD_10529 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Content
---
FAIR (URL_TO_INSERT_RECORD_10530 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Content
```
````

---

````{dropdown} **FAIR DSM image 2**
:open:

```{figure} ../../images/DSMeval-img2.png
---
width: 800px
name: FAIR (URL_TO_INSERT_RECORD_10532 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Format (URL_TO_INSERT_TERM_10531 https://fairsharing.org/search?recordType=model_and_format) 
alt:   FAIR (URL_TO_INSERT_RECORD_10534 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Format (URL_TO_INSERT_TERM_10533 https://fairsharing.org/search?recordType=model_and_format) 
---
FAIR (URL_TO_INSERT_RECORD_10536 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Format (URL_TO_INSERT_TERM_10535 https://fairsharing.org/search?recordType=model_and_format) 
```
````


---


````{dropdown} **FAIR DSM image 3**
:open:

```{figure} ../../images/DSMeval-img3.png
---
width: 800px
name: FAIR (URL_TO_INSERT_RECORD_10537 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Access
alt:  FAIR (URL_TO_INSERT_RECORD_10538 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Access
---
FAIR (URL_TO_INSERT_RECORD_10539 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Access
```
````



## Conclusions: It is about changing the data management culture!

The FAIR (URL_TO_INSERT_RECORD_10541 https://fairsharing.org/FAIRsharing.WWI10U) plus Dataset Maturity Model (URL_TO_INSERT_TERM_10540 https://fairsharing.org/search?recordType=model_and_format)  (DSM) developed (URL_TO_INSERT_RECORD_10542 https://fairsharing.org/FAIRsharing.31385c)  by the consortium is proving a valuable tool for Data Managers, 
Decision Makers and Data Scientist to identify the weak points in their FAIR (URL_TO_INSERT_RECORD_10543 https://fairsharing.org/FAIRsharing.WWI10U) ification strategies or more simply to define
the level of maturity they are capable of delivery within the constraints of the project (URL_TO_INSERT_TERM_10544 https://fairsharing.org/search?recordType=project)  or research (URL_TO_INSERT_RECORD_10545 https://fairsharing.org/FAIRsharing.52b22c)  program.
The FAIR (URL_TO_INSERT_RECORD_10547 https://fairsharing.org/FAIRsharing.WWI10U) plus DSM, following a minimal fam (URL_TO_INSERT_RECORD_10546 https://fairsharing.org/FAIRsharing.d0886a) iliarization and training period, provides the means to effective quantity and 
articulate on FAIR (URL_TO_INSERT_RECORD_10548 https://fairsharing.org/FAIRsharing.WWI10U) ification strategies and choke points. Therefore, by enabling a clearer way for communicating and talking
about FAIR (URL_TO_INSERT_RECORD_10549 https://fairsharing.org/FAIRsharing.WWI10U) ification process, the FAIR (URL_TO_INSERT_RECORD_10550 https://fairsharing.org/FAIRsharing.WWI10U) plus DSM constitutes an excellent tool to plan and enable changes in the way datasets
can be managed


### What to read next?

 
Moving through maturity levels with ISA by running the following notebook (URL_TO_INSERT_RECORD_10551 https://fairsharing.org/FAIRsharing.cbz72b) s in the indicated order:

- [improving dataset maturity: the MIAPP (URL_TO_INSERT_RECORD_10555 https://fairsharing.org/FAIRsharing.tghhc4) E (URL_TO_INSERT_RECORD_10553 https://fairsharing.org/FAIRsharing.b403jy)  (URL_TO_INSERT_RECORD_10554 https://fairsharing.org/FAIRsharing.nd9ce9)  use case](https://w3id.org (URL_TO_INSERT_RECORD_10552 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB062) 
- [create-a-simple-isa-descriptor](https://w3id.org (URL_TO_INSERT_RECORD_10556 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB063)
- [isa-api-programmatic-rebuild-of-BII-S-3](https://w3id.org (URL_TO_INSERT_RECORD_10557 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB064)
- [isa-json-conversion-to-rdf-linked-data](https://w3id.org (URL_TO_INSERT_RECORD_10558 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB064)
- [isa-as-ro](https://w3id.org (URL_TO_INSERT_RECORD_10559 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB066)


````{panels}
:column: col-md-4
:card: border-2
:header: bg-primary pa_dark
```{image} ../../images/logos/pistoia_logo.png
:height: 40px
:align: center
:name: FAIR (URL_TO_INSERT_RECORD_10560 https://fairsharing.org/FAIRsharing.WWI10U) toolkit_logo
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

