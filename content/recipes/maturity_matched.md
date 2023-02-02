(fcb-maturity)=
# Changing culture with the Dataset Maturity Model

<!--
````{panels_fairplus}
:identifier (URL_TO_INSERT_TERM_7757 https://fairsharing.org/search?recordType=identifier_schema) _text: FCB081
:identifier (URL_TO_INSERT_TERM_7758 https://fairsharing.org/search?recordType=identifier_schema) _link: 'https://w3id.org (URL_TO_INSERT_RECORD_7759 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB081'
:difficulty_level: 3
:recipe_type: guidance
:reading_time_minutes: 30
:intended_audience: principal_investigator, data_manager, data_scientist  
:maturity_level: 0
:maturity_indicator: 0
:has_executable_code: nope
:recipe_name: Changing culture with the Dataset Maturity Model (URL_TO_INSERT_TERM_7760 https://fairsharing.org/search?recordType=model_and_format) 
```` 
-->

## Abstract

The present content introduces the FAIR (URL_TO_INSERT_RECORD_7762 https://fairsharing.org/FAIRsharing.WWI10U) plus "Dataset Maturity Model (URL_TO_INSERT_TERM_7761 https://fairsharing.org/search?recordType=model_and_format) ", shows how to use it in the context of a 
FAIR (URL_TO_INSERT_RECORD_7763 https://fairsharing.org/FAIRsharing.WWI10U) ification process to decide how far to go on a FAIR (URL_TO_INSERT_RECORD_7764 https://fairsharing.org/FAIRsharing.WWI10U)  journey.
We also show how each FAIR (URL_TO_INSERT_RECORD_7766 https://fairsharing.org/FAIRsharing.WWI10U)  Cookbook recipes has been anchored to the model (URL_TO_INSERT_TERM_7765 https://fairsharing.org/search?recordType=model_and_format) .
Recipes can therefore be assembled to build a coherent path which should guarantee that datasets handle (URL_TO_INSERT_RECORD_7767 https://fairsharing.org/FAIRsharing.0b7e54) d according 
to the recommendations can meet data management expectations in terms of FAIR (URL_TO_INSERT_RECORD_7768 https://fairsharing.org/FAIRsharing.WWI10U) ness.
Therefore, the FAIR (URL_TO_INSERT_RECORD_7769 https://fairsharing.org/FAIRsharing.WWI10U) plus DSM provides a handy tool for data managers to advise on changing the culture of data management 
but also manage expectations (and costs) when devising a FAIR (URL_TO_INSERT_RECORD_7770 https://fairsharing.org/FAIRsharing.WWI10U) ification program for specific domains and digital objects
living in that space.

## Background

Maturity model (URL_TO_INSERT_TERM_7771 https://fairsharing.org/search?recordType=model_and_format) s are not new. There are in fact training programs specifically designed for this such as the
**Capability Maturity Model (URL_TO_INSERT_TERM_7772 https://fairsharing.org/search?recordType=model_and_format)  Integration (CMMI)** {footcite}`cmmi`.
These model (URL_TO_INSERT_TERM_7773 https://fairsharing.org/search?recordType=model_and_format) s originate from engineering and manufacturing fields, in particular the military and aerospace industries, 
as means to rate the reliability and degree of development of a particular technology, skill or process,
in other words, a capability. 
Notions such as **Technical Readiness Levels**  or TRLs define a scale of 9 levels to rate
a process from basic idea to production grade technology. 

With the digitization of society (URL_TO_INSERT_TERM_7774 https://fairsharing.org/search?recordType=society)  and the pervasiveness of digital technology, the life sciences, as other fields, are 
wrestling with the challenges of data management as defined in  the *Fourth paradigm: Data-intensive Scientific Discovery*
{footcite}`hey2009`. 
Organizations need to decide how to allocate resources to increase the impact of digital artefacts as they are created. 
Large amounts of literature exist detailing the key ideas for handling data. A resource such as the *DAMA book* covers in 
great depths the fundamental operations and challenges associated with data management activities {footcite}`DAMA-DMBOOK`.

More recently, The FAIR (URL_TO_INSERT_RECORD_7776 https://fairsharing.org/FAIRsharing.WWI10U)  principles (URL_TO_INSERT_RECORD_7775 https://fairsharing.org/FAIRsharing.WWI10U)  articulated key requirements and properties data should have {footcite}`pmid26978244`.
Following this important work, a number of initiatives have worked at producing domain specific maturity indicators. 
Among these initiatives, the Research (URL_TO_INSERT_RECORD_7777 https://fairsharing.org/FAIRsharing.52b22c)  Data Alliance Maturity Indicators seem to have gain notoriety
{footcite}`RDAindicators`.

Building on these efforts, the FAIR (URL_TO_INSERT_RECORD_7779 https://fairsharing.org/FAIRsharing.WWI10U) plus project (URL_TO_INSERT_TERM_7778 https://fairsharing.org/search?recordType=project)  has developed (URL_TO_INSERT_RECORD_7780 https://fairsharing.org/FAIRsharing.31385c)  a more targeted approach by focusing on the notion of 
dataset. 

## Presentation of the FAIRplus Dataset Maturity Model (DSM)

The FAIR (URL_TO_INSERT_RECORD_7782 https://fairsharing.org/FAIRsharing.WWI10U) plus Dataset Maturity Model (URL_TO_INSERT_TERM_7781 https://fairsharing.org/search?recordType=model_and_format)  proposes a framework to incorporate key concepts defined by the Capability and
Maturity Model (URL_TO_INSERT_TERM_7783 https://fairsharing.org/search?recordType=model_and_format) s and apply them to define maturity levels which can used to describe a dataset.

For a comprehensive overview of the FAIR (URL_TO_INSERT_RECORD_7785 https://fairsharing.org/FAIRsharing.WWI10U) plus Dataset Maturity Model (URL_TO_INSERT_TERM_7784 https://fairsharing.org/search?recordType=model_and_format) , refer to the [dedicated site](https://fairplus.github.io/Data-Maturity/),
a screenshot of which is presented below.

````{dropdown} **FAIR DSM**
:open:

```{figure} ../../images/maturity_img_1.png
---
width: 700px
name: FAIR (URL_TO_INSERT_RECORD_7787 https://fairsharing.org/FAIRsharing.WWI10U)  Dataset Maturity Model (URL_TO_INSERT_TERM_7786 https://fairsharing.org/search?recordType=model_and_format) 
alt:  FAIR (URL_TO_INSERT_RECORD_7789 https://fairsharing.org/FAIRsharing.WWI10U)  Dataset Maturity Model (URL_TO_INSERT_TERM_7788 https://fairsharing.org/search?recordType=model_and_format) 
---
 FAIR (URL_TO_INSERT_RECORD_7791 https://fairsharing.org/FAIRsharing.WWI10U)  Dataset Maturity Model (URL_TO_INSERT_TERM_7790 https://fairsharing.org/search?recordType=model_and_format) 
```
````


## Integrating the FAIRplus Dataset Maturity Model in the FAIRplus Cookbook

Each recipe in the FAIR (URL_TO_INSERT_RECORD_7792 https://fairsharing.org/FAIRsharing.WWI10U) plus Cookbook now incorporates one or more FAIR (URL_TO_INSERT_RECORD_7793 https://fairsharing.org/FAIRsharing.WWI10U) plus DSM indicators.

These can be found in the **Recipe Card**. 

They are there to provide our readership with a pointer to the level of data set maturity they can expect to meet if
they apply and implement the recipe.

The FAIR (URL_TO_INSERT_RECORD_7794 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators are also used to browse the recipes through the lense of maturity improvements level, which is
of interest. 

Finally, the FAIR (URL_TO_INSERT_RECORD_7797 https://fairsharing.org/FAIRsharing.WWI10U)  Cookbook produced specific content available as jupyter notebooks which use the fam (URL_TO_INSERT_RECORD_7796 https://fairsharing.org/FAIRsharing.d0886a) iliar Investigation Study Assay model (URL_TO_INSERT_TERM_7795 https://fairsharing.org/search?recordType=model_and_format)  {footcite}`pmid20679334` 
and Research (URL_TO_INSERT_RECORD_7798 https://fairsharing.org/FAIRsharing.52b22c)  Objects {footcite}`sefton_peter_2022_5841615` to showcase how users can move through maturity levels and decide for themselves how far they need to go along the scale.


````{dropdown} **FAIR DSM**
:open:

```{figure} ../../images/maturity_img.png
---
width: 450px
name: FAIR (URL_TO_INSERT_RECORD_7799 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators in the FAIR (URL_TO_INSERT_RECORD_7800 https://fairsharing.org/FAIRsharing.WWI10U)  Cookbook Recipe card
alt:  FAIR (URL_TO_INSERT_RECORD_7801 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators in the FAIR (URL_TO_INSERT_RECORD_7802 https://fairsharing.org/FAIRsharing.WWI10U)  Cookbook Recipe card
---
 FAIR (URL_TO_INSERT_RECORD_7803 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators in the FAIR (URL_TO_INSERT_RECORD_7804 https://fairsharing.org/FAIRsharing.WWI10U)  Cookbook Recipe card
```
````




## Assessing FAIRplus intervention


The FAIR (URL_TO_INSERT_RECORD_7805 https://fairsharing.org/FAIRsharing.WWI10U) plus DSM has subsequently been used to assess the effectiveness of interventions on datasets presented 
to FAIR (URL_TO_INSERT_RECORD_7806 https://fairsharing.org/FAIRsharing.WWI10U) plus experts.

Each of the 20 project (URL_TO_INSERT_TERM_7808 https://fairsharing.org/search?recordType=project) s, which have interacted with FAIR (URL_TO_INSERT_RECORD_7809 https://fairsharing.org/FAIRsharing.WWI10U) plus, have been subjected to a standard (URL_TO_INSERT_TERM_7807 https://fairsharing.org/search?fairsharingRegistry=Standard)  protocol looking at
FAIR (URL_TO_INSERT_RECORD_7810 https://fairsharing.org/FAIRsharing.WWI10U)  maturity before and after intervention, when performing retrospective processing of the data. 
In few instances, the effect of prospective interventions could also be measured. 

FAIR (URL_TO_INSERT_RECORD_7811 https://fairsharing.org/FAIRsharing.WWI10U) plus DSM developed (URL_TO_INSERT_RECORD_7812 https://fairsharing.org/FAIRsharing.31385c)  a dedicated manual assessment template.

### Training the assessor

As with any tool, fam (URL_TO_INSERT_RECORD_7813 https://fairsharing.org/FAIRsharing.d0886a) iliarization and training are necessary to ensure that the personnel carrying out the evaluations 
can use the framework in a consistent fashion. 


### Performing the assessment

The FAIR (URL_TO_INSERT_RECORD_7814 https://fairsharing.org/FAIRsharing.WWI10U) plus DSM group therefore recruited FAIR (URL_TO_INSERT_RECORD_7815 https://fairsharing.org/FAIRsharing.WWI10U)  experts and over the
course of a dedicated workshop presented the DSM model (URL_TO_INSERT_TERM_7816 https://fairsharing.org/search?recordType=model_and_format) , proposed exercises and then asked participants to rate several
datasets independently.

The next step consisted in evaluating the inter-rater agreement when using the framework.

A debriefing of the rating was carried out and was the ideal opportunity to clarify any misunderstandings about the
indicator definitions and therefore reconcile rating discrepancies between the participant.
Difference in interpretations
were identified leading in a refinement of the definitions and improvement of the documentation of the
FAIR (URL_TO_INSERT_RECORD_7818 https://fairsharing.org/FAIRsharing.WWI10U) plus dataset maturity model (URL_TO_INSERT_TERM_7817 https://fairsharing.org/search?recordType=model_and_format) .
It also resulted in streamlining both the training program and the evaluation program.

The following figure shows the effect of a FAIR (URL_TO_INSERT_RECORD_7819 https://fairsharing.org/FAIRsharing.WWI10U) ification process on an IMI eTOX dataset.

````{dropdown} **FAIR DSM image 1**
:open:

```{figure} ../../images/DSMeval-img1.png
---
width: 800px
name: FAIR (URL_TO_INSERT_RECORD_7820 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Content
alt:   FAIR (URL_TO_INSERT_RECORD_7821 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Content
---
FAIR (URL_TO_INSERT_RECORD_7822 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Content
```
````

---

````{dropdown} **FAIR DSM image 2**
:open:

```{figure} ../../images/DSMeval-img2.png
---
width: 800px
name: FAIR (URL_TO_INSERT_RECORD_7824 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Format (URL_TO_INSERT_TERM_7823 https://fairsharing.org/search?recordType=model_and_format) 
alt:   FAIR (URL_TO_INSERT_RECORD_7826 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Format (URL_TO_INSERT_TERM_7825 https://fairsharing.org/search?recordType=model_and_format) 
---
FAIR (URL_TO_INSERT_RECORD_7828 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Format (URL_TO_INSERT_TERM_7827 https://fairsharing.org/search?recordType=model_and_format) 
```
````


---


````{dropdown} **FAIR DSM image 3**
:open:

```{figure} ../../images/DSMeval-img3.png
---
width: 800px
name: FAIR (URL_TO_INSERT_RECORD_7829 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Access
alt:  FAIR (URL_TO_INSERT_RECORD_7830 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Access
---
FAIR (URL_TO_INSERT_RECORD_7831 https://fairsharing.org/FAIRsharing.WWI10U)  DSM indicators before and after intervention-Access
```
````



## Conclusions: It is about changing the data management culture!

The FAIR (URL_TO_INSERT_RECORD_7833 https://fairsharing.org/FAIRsharing.WWI10U) plus Dataset Maturity Model (URL_TO_INSERT_TERM_7832 https://fairsharing.org/search?recordType=model_and_format)  (DSM) developed (URL_TO_INSERT_RECORD_7834 https://fairsharing.org/FAIRsharing.31385c)  by the consortium is proving a valuable tool for Data Managers, 
Decision Makers and Data Scientist to identify the weak points in their FAIR (URL_TO_INSERT_RECORD_7835 https://fairsharing.org/FAIRsharing.WWI10U) ification strategies or more simply to define
the level of maturity they are capable of delivery within the constraints of the project (URL_TO_INSERT_TERM_7836 https://fairsharing.org/search?recordType=project)  or research (URL_TO_INSERT_RECORD_7837 https://fairsharing.org/FAIRsharing.52b22c)  program.
The FAIR (URL_TO_INSERT_RECORD_7839 https://fairsharing.org/FAIRsharing.WWI10U) plus DSM, following a minimal fam (URL_TO_INSERT_RECORD_7838 https://fairsharing.org/FAIRsharing.d0886a) iliarization and training period, provides the means to effective quantity and 
articulate on FAIR (URL_TO_INSERT_RECORD_7840 https://fairsharing.org/FAIRsharing.WWI10U) ification strategies and choke points. Therefore, by enabling a clearer way for communicating and talking
about FAIR (URL_TO_INSERT_RECORD_7841 https://fairsharing.org/FAIRsharing.WWI10U) ification process, the FAIR (URL_TO_INSERT_RECORD_7842 https://fairsharing.org/FAIRsharing.WWI10U) plus DSM constitutes an excellent tool to plan and enable changes in the way datasets
can be managed


### What to read next?

 
Moving through maturity levels with ISA by running the following notebooks in the indicated order:

- [improving dataset maturity: the MIAPPE use case](https://w3id.org (URL_TO_INSERT_RECORD_7843 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB062) 
- [create-a-simple-isa-descriptor](https://w3id.org (URL_TO_INSERT_RECORD_7844 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB063)
- [isa-api-programmatic-rebuild-of-BII-S-3](https://w3id.org (URL_TO_INSERT_RECORD_7845 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB064)
- [isa-json-conversion-to-rdf-linked-data](https://w3id.org (URL_TO_INSERT_RECORD_7846 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB064)
- [isa-as-ro](https://w3id.org (URL_TO_INSERT_RECORD_7847 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB066)


````{panels}
:column: col-md-4
:card: border-2
:header: bg-primary pa_dark
```{image} ../../images/logos/pistoia_logo.png
:height: 40px
:align: center
:name: FAIR (URL_TO_INSERT_RECORD_7848 https://fairsharing.org/FAIRsharing.WWI10U) toolkit_logo
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

