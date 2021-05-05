# Resources for dealing with consent information

## Main Objectives

The main objective is to raise awareness to the existence of several vocabularies devised to support capturing and tracking of patient consent information while complying with with some specific or local (EU) legal requirements.

## Introduction

Ethical issues surrounding the use of clinical information and patient data have been brought to the fore by a number of publications [ref] and as the digital transformation of medical information accelerates, information scientists, technologists and legal representatives are working at developing methods and tools which can enable Science to be done while preserving the privacy of patients and respecting their wishes as to what use of their data is allowed.

The focus of this present content og the FAIR Cookbook is to highlight existing efforts which focused on developing terminologies capable of allowing software agents and machines to consume statements reflecting key information found in `consent forms` signed by patients when enrolled in studies.

The information artefacts built by information technologists working in the field fall into two main categories:

1. efforts meant to allow structuring of consent forms in machine readable formats

2. efforts meant to code the nature of the consent given, its scope as well as its evolution. 

```{note}
this last point is particularly important as it is central to accommodating the reality of changing opinions and sensibilities with respect to research topics. Patients who may have given consent at one point in time retain the right to withdraw their consent or alter it to a more restrictive position. Scientists, tools and software agents need to be able to act on these changes, ensuring that the will of patients is respected.
Failure to do so could seriously erode the confidence of the public in the use of their data for the purpose of medical research and industrial production but also result in costly legal proceedings and court cases, all of which are detrimental to all stakeholders.
```

## A survey of the existing

This section introduces several semantic artifacts of relevance to the topic.

### Informed Consent Ontology

Consent forms in paper form are routinely used in medical practice when patients undergo medical treatment. Those forms are written in natural language but often contain standard legal clauses.

[ICO, the Informed Consent Ontology](https://github.com/ICO-ontology/ICO) is being used to model consent information as help in Electronic Health Records (EHR)

```{figure} https://i.imgur.com/pR8PUA1.png
---
width: 800px
name: Informed Consent Ontology in the OBOFoundry
alt: Informed Consent Ontology in the OBOFoundry
---
Informed Consent Ontology in the OBOFoundry
```


<!-- ![](https://i.imgur.com/pR8PUA1.png) -->

ICO is an OWL ontology based on the BFO ontology, which is also known as [ISO/IEC 21838-2]() standard.

```bash=

add RDF statement using ICO

```


```{figure} https://i.imgur.com/BJ1VONG.jpg
---
width: 800px
name: Informed Consent Ontology overview
alt: Informed Consent Ontology overview
---
Informed Consent Ontology overview
```
(source: http://www.jneilotte.com/2018/07/the-informed-consent-ontology-ico/)

<!-- ![](https://i.imgur.com/BJ1VONG.jpg) -->






### GConset: a GDPR-based Consent Vocabulary

This resource is of importance as it is based of the GDRP regulation, which came into force in the European Union in 2018. 
Heavy sanctions and penalties are enforced for organization and businesses breaching the regulation.
The GDRP regulation has had a significant impact on the information technology industry, which until then was pretty much unregulated, leading to abuse in use of individual data, such as tracking of browsing history and navigation habits.



http://openscience.adaptcentre.ie/ontologies/GConsent/docs/ontology



```{figure} https://i.imgur.com/2m5NmzN.png
---
width: 800px
name: GConsent Ontology specifications
alt: GConsent Ontology specifications
---
GConsent Ontology specifications
```
<!-- ![](https://i.imgur.com/2m5NmzN.png) -->


GConsent is an OWL2 ontology for representing consent for GDPR compliance developed by the ADAPT Centre (Trinity College Dublin)


```{figure} https://i.imgur.com/OVjfSMe.png
---
width: 800px
name: GConsent Ontology overview
alt: GConsent Ontology overview
---
GConsent Ontology overview
```
<!-- ![](https://i.imgur.com/OVjfSMe.png) -->

GConsent Ontology has a very specific scope which focuses on:
- defining an instance of consent
- the data subject the consent is about
- the status of the consent

GConsent Ontology uses concepts from the well know Provenance Ontology Model (PROV-O), which will be detailed below.



### Tracking changes with PROV-O, the Provenance Ontology:

The W3C PROV-O specification is a vocabulary to `represent and interchange provenance information generated in different systems and under different contexts` to quote the [original documentation](https://www.w3.org/TR/prov-o/).
The vocabulary supports the expression of `provenance`, by relying on a very simple model whereby an `Entity` can be brought about by an `Activity` which may be associated to an `Agent`.

The following example shows how the `PROV ontology` can be used to form RDF statement to track how a `document` has been generated and how `attribution` to a `Person` can be made.


```code
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix :     <http://example.org#> .

:consent_document
   a odrl:Policy;
   prov:wasGeneratedBy  :publicationActivity;
   prov:wasAttributedTo :pavel;
.

:pavel
   a foaf:Person, prov:Agent;
   foaf:givenName       "Pavel";
   foaf:mbox            <mailto:pavel@example.org>;
   prov:actedOnBehalfOf :pharma_inc;
.

:pharma_inc a foaf:Organization, prov:Agent ;
    foaf:name "Pharma INC";
.

```




```warning
Using those resources, it is important to understand the following:

GConsent Vocabulary makes are clear distinction between the `consent` and the `consent document`. In fact, GConsent clearly states that modeling `consent document` is out of scope. For this, it recommends using W3C ODRL to express such documents, possibly in the form of a `odrl:Policy`.

```


### Bringing it all together:

```bash
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix gc:     <https://w3id.org/GConsent#> .


:consent_1
     a gc:GivenConsent;
     gc:isProvidedBy :pavel;
     gc:hasStatus :status_1;
     gc:forPurpose :ad_hoc_purpose_1;
     gc:atTime "2020-04-21"^xsd:date;
     gc:hasExpiry "2024-04-21"^xsd:date;
.
:status_1
    a gc:ConsentStatusExplicitlyGiven;
.    
:ad_hoc_purpose_1 
    a gc:Purpose;
.
    
```

___

### Conclusion

This quick state of the art covered the semantic resources available to express consent information with RDF statements.

#### What to read next?
> {ref}`fcb-reusability-data_use`
> {ref}`fcb-reusability-provenance`
> {ref}`rr-licensing-data`


___

## References



___

## Authors

| Name             | Affiliation                        | orcid                                                        | CrediT role              | 
|:---------------- |:---------------------------------- |:------------------------------------------------------------ |:------------------------ |
| Philippe Rocca-Serra | Data Readiness Group, University of Oxford, UK | [0000-0001-9853-5668](https://orcid.org/0000-0001-9853-5668) | Writing, Original Draft |
||||Review|


___

## License

This page is released under the Creative Commons 4.0 BY license.

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>