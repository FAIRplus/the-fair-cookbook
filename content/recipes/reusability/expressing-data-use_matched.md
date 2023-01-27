(fcb-reusability-data_use)=
# Declaring data permitted uses


````{panels_fairplus}
```` 

## Main Objectives

The purpose of this content is to provide guidance on how to describe **permitted use of data** and identify the **resources** that exist to do so.

The aim is also to document equivalent representations and how bridges(URL_TO_INSERT_RECORD https://bridges.monash.edu/) can be built between the distinct but equivalent implementations.

Finally, the content aims to highlight key use-cases which require coverage, how to code such informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion, documenting 
implementation patterns in the context of **data cataloguing efforts**, for instance by expressing **Data Access Policies (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Policy)**.


## Graphical Overview


````{dropdown}
```{figure} data-usage-mermaid.png
---
width: 850px
name: expressing-data-use-figure1
alt: Dealing with Policies (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Policy) and Data Use
---
Data Use
```
````



---

## Tools

### Standards

 Data Format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s  | Terminologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) | Model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s  |
| :------------- | :------------- | :------------- |
| JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259)-LD(URL_TO_INSERT_RECORD https://json-ld.org/spec/latest/json-ld/)<!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO add a link to corresponding document --> | <!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO add a link to corresponding document -->  |   |
| [ISO-8601](https://www.iso.org/iso-8601-date-and-time-format.html)  | [DC(URL_TO_INSERT_RECORD http://dublincore.org/documents/dces/)(URL_TO_INSERT_RECORD https://doi.org/10.25504/FAIRsharing.3nx7t)AT(URL_TO_INSERT_RECORD https://www.w3.org/TR/vocab-dcat/)(URL_TO_INSERT_RECORD http://cat.aii.caas.cn/) v2](https://www.w3.org/TR/vocab-dcat(URL_TO_INSERT_RECORD https://www.w3.org/TR/vocab-dcat/)-2/)  |   |
| [ISO-3066](https://www.iso.org/iso-3166-country-codes.html)  | [ODRL](https://www.w3.org/TR/odrl-vocab/)  |   |
| EGA(URL_TO_INSERT_RECORD https://ega-archive.org/) XML(URL_TO_INSERT_RECORD https://www.w3.org/TR/xml/)<!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO add a link to corresponding document -->   | [DUO](http://www.obofoundry.org(URL_TO_INSERT_RECORD http://www.obofoundry.org/)/ontology/duo.html)  |   |
| [Data Article Tag Suite (DATS)](https://datatagsuite.github.io/schema/)  | [MONDO](http://www.obofoundry.org(URL_TO_INSERT_RECORD http://www.obofoundry.org/)/ontology/mondo.html)  |   |




### Implementation

DUO(URL_TO_INSERT_RECORD https://raw.githubusercontent.com/EBISPOT/DUO/master/duo.owl)(URL_TO_INSERT_RECORD https://github.com/bio-ontology-research-group/unit-ontology)S:
https://duos.broadinstitute.org/

---

## Introduction

The preservation of patient privacy and the compliance with patient consent are essential considerations when managing
sensitive informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion such as clinical and patient data.
Consent forms, as signed by patients, define the acceptable usage of data derived from a patient for research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) applications.
All major research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) organizations, at national and international levels, enforce strict rules for the management of such data.
Sensitive data cannot be accessed without undergoing a vetting process involving a **data access request** to a **data access committee**,
which will decide, whether or not, to grant requesters access to the data.

This is a time-consuming process in the absence of machine-readable version of data access/ data management policies (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Policy).
In turns, it can prove detrimental to research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/).
Therefore, efforts to enable the provision of concise, efficient and **machine processable** summary of key permissions and prohibitions have been made. 
Several resources are now available for the coding and exchange of **machine-actionable**, **legally binding** and
**explicit** informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion related to allowed and consented data usage.

The following sections detail how the international sequence data arch(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ives (US NCBI dbGAP, SRA(URL_TO_INSERT_RECORD http://www.ncbi.nlm.nih.gov/sra) and EU EMB(URL_TO_INSERT_RECORD http://www.Metabase.net)L_EBI EGA(URL_TO_INSERT_RECORD https://ega-archive.org/))
are encoding **Data Use Informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion**  but also how ODR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)L, a W3C specification, 
can be used to represent equivalent informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion in a format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) compatible with the data cataloguing efforts relying on W3C DC(URL_TO_INSERT_RECORD http://dublincore.org/documents/dces/)(URL_TO_INSERT_RECORD https://doi.org/10.25504/FAIRsharing.3nx7t)AT(URL_TO_INSERT_RECORD https://www.w3.org/TR/vocab-dcat/)(URL_TO_INSERT_RECORD http://cat.aii.caas.cn/) specifications.




### SRA & EGA XML schema for Policy, Dataset and Controller

Next Generation Sequencing (NGS) techniques allow routine production of full genome data from patients.
This data is highly sensitive and data repositories (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository) specialized in storing such informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion have developed(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) procedures 
and representation model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s for defining the conditions of use.

We summarize here the key objects used by the European Genome Arch(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ive, in compliance with INSD(URL_TO_INSERT_RECORD https://nsd.no/en/)C(URL_TO_INSERT_RECORD http://dublincore.org/documents/dces/)(URL_TO_INSERT_RECORD https://doi.org/10.25504/FAIRsharing.3nx7t) and GA4GH(URL_TO_INSERT_RECORD https://github.com/ga4gh/schemas) guideline (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=reporting_guideline)s.

https://ega-archive.org(URL_TO_INSERT_RECORD https://ega-archive.org/)/data-use-conditions

````{dropdown}
```{figure} duo-ols-view-1.png
---
width: 700px
name: expressing-data-use-figure2
alt: Data Use Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) Overview Part 1
---
Data Use Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) Overview Part 1
```
````

````{dropdown}
```{figure} duo-ols-view-2.png
---
width: 700px
name: expressing-data-use-figure3
alt: Data Use Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) Overview Part 2
---
Data Use Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) Overview Part 2
```
````

<!-- 
````{panels}
```{figure} duo-ols-view-1.png
width: 400px
```
```{figure} duo-ols-view-2.png
width: 400px
```

```` -->


The informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion presented below has been sourced from the ENA(URL_TO_INSERT_RECORD http://www.ebi.ac.uk/ena) GitHub(URL_TO_INSERT_RECORD https://github.com/)(URL_TO_INSERT_RECORD https://github.com/) repo.



1. The **Data Access Committee** and Contact informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion

```XML
```


https://github.com(URL_TO_INSERT_RECORD https://github.com/)/enasequence/schema/blob/USI/src/test/resources/uk/ac/ebi/ena/sra/xml/ega_dac/ega_dac.xml

2. The **Data Access Policy (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Policy)** object


https://github.com(URL_TO_INSERT_RECORD https://github.com/)/enasequence/schema/blob/USI/src/test/resources/uk/ac/ebi/ena/sra/xml/ega_policy/ega_policy.xml

```{note}
```


```XML
```


```{note}
```

```XML
```


3. Expressing Data Use with EGA(URL_TO_INSERT_RECORD https://ega-archive.org/) XML(URL_TO_INSERT_RECORD https://www.w3.org/TR/xml/) and **Data Use Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)** codes.

```XML


```



https://ega-archive.org(URL_TO_INSERT_RECORD https://ega-archive.org/)/dacs

Indicating disease specific restriction on research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) with DUO(URL_TO_INSERT_RECORD https://raw.githubusercontent.com/EBISPOT/DUO/master/duo.owl)(URL_TO_INSERT_RECORD https://github.com/bio-ontology-research-group/unit-ontology) and ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) covering the Disease and Pathology domain.


```XML
```


```{note}
```



```XML
```




https://github.com(URL_TO_INSERT_RECORD https://github.com/)/enasequence/schema/blob/USI/src/test/resources/uk/ac/ebi/ena/sra/xml/ega_dataset/ega_dataset.xml


```XML
```




Browsing Data Access Committees available from EGA(URL_TO_INSERT_RECORD https://ega-archive.org/):

````{dropdown}
```{figure} dac-ega.png
---
width: 700px
name: 
alt: List of Data Access Policy (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Policy) from EGA(URL_TO_INSERT_RECORD https://ega-archive.org/)
---
List of Data Access Policy (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Policy) from EGA(URL_TO_INSERT_RECORD https://ega-archive.org/)
```
````


### ODRL, Open Digital Rights Language

ODR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)L stands for Open Digital Rights Language and is a set of W3C Recommendations defining a **policy (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Policy) expression language**. 

ODR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)L is made up of several components:

- [The ODR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)L Model](https://www.w3.org/TR/odrl-model/) {footcite}`ODR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)Lmodel (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)`

````{dropdown}
```{figure} https://www.w3.org/TR/odrl-model/00Model.png
---
width: 700px
name: 
alt: Open Digital Rights Language model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)
---
ODR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)L overview
```
````


- [The ODR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)L Vocabulary](https://www.w3.org/TR/odrl-vocab/) {footcite}`ODR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)Lvocab`

The **ODR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)L Vocabulary and Expression** provides the terms to express policies (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Policy) in RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) language.

The ODR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)L Vocabulary and Expression complements the ODR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)L informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format), which allows expressing similar informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion in JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) language.



```{warning}



```

#### The different types of Policies

The ODR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)L model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) defines several subclasses for the **Policy (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Policy)** entity, namely  **Agreement**, **Set**, **Offer**.

##### Describing an agreement with ODRL

```json
```


### Encoding Research Restriction on disease and geographical area using ODRL and DUO

In this section, we document how to rely on a basic ODR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)L-based pattern using a DUO(URL_TO_INSERT_RECORD https://raw.githubusercontent.com/EBISPOT/DUO/master/duo.owl)(URL_TO_INSERT_RECORD https://github.com/bio-ontology-research-group/unit-ontology) term {footcite}`DUO(URL_TO_INSERT_RECORD https://raw.githubusercontent.com/EBISPOT/DUO/master/duo.owl)(URL_TO_INSERT_RECORD https://github.com/bio-ontology-research-group/unit-ontology)` to represent a
situation where SecondaryUse of the data is allowed on the condition that work is restricted to **disease specific research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)**.


```json
```

```{note}
```

The following representation is more sophisticated and includes 3 types of restrictions:

- restriction on specific disease (juvenile arthritis, to reuse the exemplar representation in EGA(URL_TO_INSERT_RECORD https://ega-archive.org/)/SRA(URL_TO_INSERT_RECORD http://www.ncbi.nlm.nih.gov/sra) XML(URL_TO_INSERT_RECORD https://www.w3.org/TR/xml/) presented in section 1)
- restriction on the geographical location where the research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) can be conducted
- an obligation to delete the data obtained through the access agreement past a specified duration, 3 years in our example

Let's proceed stepwise.


* Representing Research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) Restriction on Specific Disease Area using DUO(URL_TO_INSERT_RECORD https://raw.githubusercontent.com/EBISPOT/DUO/master/duo.owl)(URL_TO_INSERT_RECORD https://github.com/bio-ontology-research-group/unit-ontology) and MO(URL_TO_INSERT_RECORD http://mged.sourceforge.net/ontologies/MGEDontology.php)NDO(URL_TO_INSERT_RECORD https://github.com/monarch-initiative/monarch-disease-ontology) ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)


```json
```

```{note}




```


```{note}
```



* Representing Research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) Restriction based on Geographical Regions

The section shows how to use ODR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)L to document geographical restrictions, either by listing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) countries where research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) is 
allowed or by listing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) those countries excluded from doing so.

In the following example, research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) is only allowed in a specific country, **Italy** in this case, which is 
encoded using the **ISO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)-3166 code**.


```json
```

* Representing Obligations regarding Data Management

The following example shows how to explicitly state in a Policy (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Policy) element that the data must be deleted after a defined
period of time (3 years in this example).
Duration and time related value should be represented using **ISO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)-8601 standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)**.

```json
```


## Possible specifications of EGA related information using ODRL

```{warning} 


```

```json
```

### Indicating Prohibitions and Interdictions

The ODR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)L model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) {footcite}`ODR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)Lmodel (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)` provides the **prohibitions** relation, which uses similar patterns to those seen while covering **permissions**.
The ODR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)L vocabulary is then used to identify the **actions** which are restricted under the **prohibition** header. 
Complex prohibitions can be expressed using **constraints** and **refinement** elements.


```json
```



## Implementation in Data Catalogues built with DCAT or DATS


### Referring to an ODRL Policy from a DCAT DataSet

```bash



```

For more details, please see the following publication by [de Vos et al, 2019](https://www.specialprivacy.eu/images/documents/RuleMLRR_2019_.pdf)

### DATS and ODRL JSON

An evolution of the DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) {footcite}`pmid28585923`, {footcite}`pmid32031623` schema is used by University of Luxembourg 
to build a data catalogue for IMI project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project)s and datasets.
The proposed patterns could be used and tested to representation DAC(URL_TO_INSERT_RECORD https://ac.tdwg.org/introduction/)/DAA informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion as well as the allowed uses of 
datasets generated by the consortia funded by IMI.
More complex use cases can be considered to assess to ability of the representations to be associated to specific 
datasets, for instance datasets associated with a particular data acquisition technique the access of which may require 
specific policies (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Policy) and conditions to be made machine-readable.

The approach is therefore to reference the  JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) representations compliant with the ODR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)L JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) schema 2.1 specification,
as presented in earlier sections in conjunction with DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) documents.



### Validating ODRL RDF documents

Code exists that allows developers to validate ODR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)L documents **expressed in legitimate RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) serializations**.

http://odrlapi.appspot.com/


````{dropdown}
```{figure} ./odrl-validation-app.png
---
width: 800px
alt: ODR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)L Validation and Evaluation Sandbox
name: ODR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)L Validation and Evaluation Sandbox
---
ODR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)L Validation and Evaluation Sandbox
```
````


The web-application is powered by a REST-API the swagger document of which is available from the following address:
http://odrlapi.appspot.com/apidoc/index.html

<!-- ## TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO discuss relation to RightML

https://iptc.org/std/RightsML/2.0/RightsML_2.0-specification.html -->

## Consuming Data Use related annotations

It is all good and well to describe patterns in various format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s but are there any tools or services capable exploiting these annotations?
Well, when it comes to genomics data, there is the Broad Institute's 
[Data Use Oversight System (DUOS)](https://duos.broadinstitute.org/#/home) is one such tool.

````{dropdown}
```{figure} ./broads-duos.png
---
width: 800px
alt: Broad's Institute  Data Use Oversight System
name: Broad's Institute  Data Use Oversight System
---
Broad's Institute  Data Use Oversight System landing page
```
````

DUO(URL_TO_INSERT_RECORD https://raw.githubusercontent.com/EBISPOT/DUO/master/duo.owl)(URL_TO_INSERT_RECORD https://github.com/bio-ontology-research-group/unit-ontology)S requires official clearance from a **Data Access Committee** representative or an **Authorized Submission Representative** 
to enable registration of a dataset into the DUO(URL_TO_INSERT_RECORD https://raw.githubusercontent.com/EBISPOT/DUO/master/duo.owl)(URL_TO_INSERT_RECORD https://github.com/bio-ontology-research-group/unit-ontology)S.
Once this authorization is available, the dataset has to be annotated following the patterns defined by GA4GH(URL_TO_INSERT_RECORD https://github.com/ga4gh/schemas) with
Data Use Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) {footcite}`pmid26796797` and 'SRA(URL_TO_INSERT_RECORD http://www.ncbi.nlm.nih.gov/sra) XML(URL_TO_INSERT_RECORD https://www.w3.org/TR/xml/)' format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format).

The European Genome Arch(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ive allows programmatic filtering based on this informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion via the REST-API of the service.

## Conclusion

Making sure that machine-readable informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion about the conditions of use of datasets and data is available is key to 
enable privacy preserving and policy (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Policy) compliant use of informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion across organizations.
This content provides an overview of the model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s available to do so and how it has been applied to life science data, 
showing the main features of the model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s and how to define use based on the major properties such as the type of research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)
allowed, how to indicate disease domain or geographical restrictions as well as temporal restrictions associated to the
dataset and defined by the data owners/data controllers.



### What to read next?

* {ref}`rr-licensing-software`
* {ref}`rr-licensing-data`

````{rdmkit_panel}
````



## References
````{dropdown} **References**
```{footbibliography}
```
````


## Authors

````{authors_fairplus}
````


## License

````{license_fairplus}
````

