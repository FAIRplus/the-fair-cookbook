(fcb-reusability-data_use)=
# Declaring data permitted uses


````{panels_fairplus}
:identifier_text: FCB035
:identifier_link: 'https://w3id.org/faircookbook/FCB035'
:difficulty_level: 4
:recipe_type: background_information
:reading_time_minutes: 15
:intended_audience: principal_investigator, data_manager, data_scientist, ontologist  
:maturity_level: 4
:maturity_indicator: 59
:has_executable_code: nope
:recipe_name: Declaring data permitted uses
```` 

## Main Objectives

The purpose of this content is to provide guidance on how to describe **permitted use of data** and identify the **resources** that exist to do so.

The aim is also to document equivalent representations and how bridges (URL_TO_INSERT_RECORD_9364 https://fairsharing.org/FAIRsharing.ac95d5)  can be built between the distinct but equivalent implementations.

Finally, the content aims to highlight key use-cases which require coverage, how to code such informat (URL_TO_INSERT_TERM_9365 https://fairsharing.org/search?recordType=model_and_format) ion, documenting 
implementation patterns in the context of **data cataloguing efforts**, for instance by expressing **Data Access Policies (URL_TO_INSERT_TERM_9366 https://fairsharing.org/search?fairsharingRegistry=Policy) **.


## Graphical Overview


````{dropdown}
:open:
```{figure} data-usage-mermaid.png
---
width: 850px
name: expressing-data-use-figure1
alt: Dealing with Policies (URL_TO_INSERT_TERM_9367 https://fairsharing.org/search?fairsharingRegistry=Policy)  and Data Use
---
Data Use
```
````



---

## Tools

### Standards

 Data Format (URL_TO_INSERT_TERM_9369 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_9370 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_9368 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
| JSON-LD<!-- TODO add a link to corresponding document --> | <!-- TODO add a link to corresponding document -->  |   |
| [ISO-8601](https://www.iso.org/iso-8601-date-and-time-format.html)  | [DC (URL_TO_INSERT_RECORD_9373 https://fairsharing.org/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD_9374 https://fairsharing.org/3547) AT (URL_TO_INSERT_RECORD_9371 https://fairsharing.org/FAIRsharing.h4j3qm)  v2](https://www.w3.org/TR/vocab-dcat (URL_TO_INSERT_RECORD_9372 https://fairsharing.org/FAIRsharing.h4j3qm) -2/)  |   |
| [ISO-3066](https://www.iso.org/iso-3166-country-codes.html)  | [ODRL](https://www.w3.org/TR/odrl-vocab/)  |   |
| EGA XML<!-- TODO add a link to corresponding document -->   | [DUO](http://www.obofoundry.org/ontology/duo.html)  |   |
| [Data Article Tag Suite (DATS)](https://datatagsuite.github.io/schema/)  | [MONDO](http://www.obofoundry.org (URL_TO_INSERT_RECORD_9375 https://fairsharing.org/FAIRsharing.847069) /ontology/mondo.html)  |   |




### Implementation

DUO (URL_TO_INSERT_RECORD_9376 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_9377 https://fairsharing.org/FAIRsharing.mjnypw) S:
https://duos.broadinstitute.org/

---

## Introduction

The preservation of patient privacy and the compliance with patient consent are essential considerations when managing
sensitive informat (URL_TO_INSERT_TERM_9378 https://fairsharing.org/search?recordType=model_and_format) ion such as clinical and patient data.
Consent forms, as signed by patients, define the acceptable usage of data derived from a patient for research (URL_TO_INSERT_RECORD_9379 https://fairsharing.org/FAIRsharing.52b22c)  applications.
All major research (URL_TO_INSERT_RECORD_9380 https://fairsharing.org/FAIRsharing.52b22c)  organizations, at national and international levels, enforce strict rules for the management of such data.
Sensitive data cannot be accessed without undergoing a vetting process involving a **data access request** to a **data access committee**,
which will decide, whether or not, to grant requesters access to the data.

This is a time-consuming process in the absence of machine-readable version of data access/ data management policies (URL_TO_INSERT_TERM_9381 https://fairsharing.org/search?fairsharingRegistry=Policy) .
In turns, it can prove detrimental to research (URL_TO_INSERT_RECORD_9382 https://fairsharing.org/FAIRsharing.52b22c) .
Therefore, efforts to enable the provision of concise, efficient and **machine processable** summary of key permissions and prohibitions have been made. 
Several resources are now available for the coding and exchange of **machine-actionable**, **legally binding** and
**explicit** informat (URL_TO_INSERT_TERM_9383 https://fairsharing.org/search?recordType=model_and_format) ion related to allowed and consented data usage.

The following sections detail how the international sequence data arch (URL_TO_INSERT_RECORD_9385 https://fairsharing.org/FAIRsharing.52b22c) ives (US NCBI dbGAP, SRA (URL_TO_INSERT_RECORD_9386 https://fairsharing.org/FAIRsharing.g7t2hv)  and EU EMBL_EBI EGA (URL_TO_INSERT_RECORD_9384 https://fairsharing.org/FAIRsharing.mya1ff) )
are encoding **Data Use Informat (URL_TO_INSERT_TERM_9387 https://fairsharing.org/search?recordType=model_and_format) ion**  but also how ODR (URL_TO_INSERT_RECORD_9388 https://fairsharing.org/FAIRsharing.1sfhp3) L, a W3C specification, 
can be used to represent equivalent informat (URL_TO_INSERT_TERM_9389 https://fairsharing.org/search?recordType=model_and_format) ion in a format (URL_TO_INSERT_TERM_9390 https://fairsharing.org/search?recordType=model_and_format)  compatible with the data cataloguing efforts relying on W3C DC (URL_TO_INSERT_RECORD_9392 https://fairsharing.org/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD_9393 https://fairsharing.org/3547) AT (URL_TO_INSERT_RECORD_9391 https://fairsharing.org/FAIRsharing.h4j3qm)  specifications.




### SRA & EGA XML schema for Policy, Dataset and Controller

Next Generation Sequencing (NGS) techniques allow routine production of full genome data from patients.
This data is highly sensitive and data repositories (URL_TO_INSERT_TERM_9394 https://fairsharing.org/search?recordType=repository)  specialized in storing such informat (URL_TO_INSERT_TERM_9395 https://fairsharing.org/search?recordType=model_and_format) ion have developed (URL_TO_INSERT_RECORD_9396 https://fairsharing.org/FAIRsharing.31385c)  procedures 
and representation model (URL_TO_INSERT_TERM_9397 https://fairsharing.org/search?recordType=model_and_format) s for defining the conditions of use.

We summarize here the key objects used by the European Genome Arch (URL_TO_INSERT_RECORD_9401 https://fairsharing.org/FAIRsharing.52b22c) ive, in compliance with INSD (URL_TO_INSERT_RECORD_9399 https://fairsharing.org/FAIRsharing.mKDii0) C (URL_TO_INSERT_RECORD_9400 https://fairsharing.org/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD_9402 https://fairsharing.org/3547)  and GA4GH guideline (URL_TO_INSERT_TERM_9398 https://fairsharing.org/search?recordType=reporting_guideline) s.

https://ega-archive.org (URL_TO_INSERT_RECORD_9403 https://fairsharing.org/FAIRsharing.mya1ff) /data-use-conditions

````{dropdown}
:open:
```{figure} duo-ols-view-1.png
---
width: 700px
name: expressing-data-use-figure2
alt: Data Use Ontology (URL_TO_INSERT_TERM_9404 https://fairsharing.org/search?recordType=terminology_artefact)  Overview Part 1
---
Data Use Ontology (URL_TO_INSERT_TERM_9405 https://fairsharing.org/search?recordType=terminology_artefact)  Overview Part 1
```
````

````{dropdown}
:open:
```{figure} duo-ols-view-2.png
---
width: 700px
name: expressing-data-use-figure3
alt: Data Use Ontology (URL_TO_INSERT_TERM_9406 https://fairsharing.org/search?recordType=terminology_artefact)  Overview Part 2
---
Data Use Ontology (URL_TO_INSERT_TERM_9407 https://fairsharing.org/search?recordType=terminology_artefact)  Overview Part 2
```
````

<!-- 
````{panels}
:column: col-8
:card: border-2
DUO (URL_TO_INSERT_RECORD_9408 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_9410 https://fairsharing.org/FAIRsharing.mjnypw)  in OLS (URL_TO_INSERT_RECORD_9409 https://fairsharing.org/FAIRsharing.Mkl9RR) 
^^^
```{figure} duo-ols-view-1.png
width: 400px
```
---
DUO (URL_TO_INSERT_RECORD_9411 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_9413 https://fairsharing.org/FAIRsharing.mjnypw)  in OLS (URL_TO_INSERT_RECORD_9412 https://fairsharing.org/FAIRsharing.Mkl9RR) 
^^^
```{figure} duo-ols-view-2.png
width: 400px
```

```` -->


The information presented below has been sourced from the ENA GitHub repo.



1. The **Data Access Committee** and Contact information

```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<DAC (URL_TO_INSERT_RECORD_9414 https://fairsharing.org/FAIRsharing.md3e78) _SET>
    <DAC (URL_TO_INSERT_RECORD_9417 https://fairsharing.org/FAIRsharing.md3e78)  alias="DAC (URL_TO_INSERT_RECORD_9418 https://fairsharing.org/FAIRsharing.md3e78) -2011-08-11T11:45:28Z-1873" accession="EGA (URL_TO_INSERT_RECORD_9415 https://fairsharing.org/FAIRsharing.mya1ff) C (URL_TO_INSERT_RECORD_9419 https://fairsharing.org/FAIRsharing.md3e78) 00000000001" center_name="EBI" broker_name="EGA (URL_TO_INSERT_RECORD_9416 https://fairsharing.org/FAIRsharing.mya1ff) ">
        <IDENTIFIER (URL_TO_INSERT_TERM_9420 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9421 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9422 https://fairsharing.org/FAIRsharing.vajn3f) >
            <PRIMA (URL_TO_INSERT_RECORD_9426 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9423 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_9425 https://fairsharing.org/FAIRsharing.mya1ff) C (URL_TO_INSERT_RECORD_9428 https://fairsharing.org/FAIRsharing.md3e78) 00000000001</PRIMA (URL_TO_INSERT_RECORD_9427 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9424 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
            <SUBMITTER_ID namespace="EBI">DAC (URL_TO_INSERT_RECORD_9429 https://fairsharing.org/FAIRsharing.md3e78) -2011-08-11T11:45:28Z-1873</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_9430 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9431 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9432 https://fairsharing.org/FAIRsharing.vajn3f) >
        <TITLE>EGA (URL_TO_INSERT_RECORD_9433 https://fairsharing.org/FAIRsharing.mya1ff)  DAC (URL_TO_INSERT_RECORD_9434 https://fairsharing.org/FAIRsharing.md3e78)  TITLE</TITLE>
        <CO (URL_TO_INSERT_RECORD_9435 https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD_9436 https://fairsharing.org/FAIRsharing.thskvr) NTAC (URL_TO_INSERT_RECORD_9437 https://fairsharing.org/FAIRsharing.md3e78) TS>
            <CO (URL_TO_INSERT_RECORD_9438 https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD_9439 https://fairsharing.org/FAIRsharing.thskvr) NTAC (URL_TO_INSERT_RECORD_9440 https://fairsharing.org/FAIRsharing.md3e78) T name="Joe Bloggs" email="joe@noname.com" organisation="EBI"/>
        </CO (URL_TO_INSERT_RECORD_9441 https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD_9442 https://fairsharing.org/FAIRsharing.thskvr) NTAC (URL_TO_INSERT_RECORD_9443 https://fairsharing.org/FAIRsharing.md3e78) TS>
    </DAC (URL_TO_INSERT_RECORD_9444 https://fairsharing.org/FAIRsharing.md3e78) >
</DAC (URL_TO_INSERT_RECORD_9445 https://fairsharing.org/FAIRsharing.md3e78) _SET>
```


https://github.com/enasequence/schema/blob/USI/src/test/resources/uk/ac/ebi/ena/sra/xml/ega_dac/ega_dac.xml

2. The **Data Access Policy** object


https://github.com/enasequence/schema/blob/USI/src/test/resources/uk/ac/ebi/ena/sra/xml/ega_policy/ega_policy.xml

```{note}
in the following example, the text of the policy (URL_TO_INSERT_TERM_9446 https://fairsharing.org/search?fairsharingRegistry=Policy)  is present in the XML (URL_TO_INSERT_RECORD_9447 https://fairsharing.org/FAIRsharing.b5cc91)  representation
```


```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<PO (URL_TO_INSERT_RECORD_9449 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9448 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
    <PO (URL_TO_INSERT_RECORD_9452 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9450 https://fairsharing.org/search?fairsharingRegistry=Policy)  center_name="EBI" alias="Policy (URL_TO_INSERT_TERM_9451 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868" accession="EGA (URL_TO_INSERT_RECORD_9453 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001" broker_name="EBI">
        <IDENTIFIER (URL_TO_INSERT_TERM_9454 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9455 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9456 https://fairsharing.org/FAIRsharing.vajn3f) >
            <PRIMA (URL_TO_INSERT_RECORD_9460 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9457 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_9459 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001</PRIMA (URL_TO_INSERT_RECORD_9461 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9458 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
            <SUBMITTER_ID namespace="SC">Policy (URL_TO_INSERT_TERM_9462 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_9463 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9464 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9465 https://fairsharing.org/FAIRsharing.vajn3f) >
        <TITLE/>
        <DAC (URL_TO_INSERT_RECORD_9467 https://fairsharing.org/FAIRsharing.md3e78) _REF accession="EGA (URL_TO_INSERT_RECORD_9466 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001" refname="DAC (URL_TO_INSERT_RECORD_9468 https://fairsharing.org/FAIRsharing.md3e78) _-2011-08-26T12:23:49Z-1868" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_9469 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9470 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9471 https://fairsharing.org/FAIRsharing.vajn3f) >
                <PRIMA (URL_TO_INSERT_RECORD_9475 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9472 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_9474 https://fairsharing.org/FAIRsharing.mya1ff) C (URL_TO_INSERT_RECORD_9477 https://fairsharing.org/FAIRsharing.md3e78) 00001000001</PRIMA (URL_TO_INSERT_RECORD_9476 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9473 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
                <SUBMITTER_ID namespace="EBI">DAC (URL_TO_INSERT_RECORD_9478 https://fairsharing.org/FAIRsharing.md3e78) _-2011-08-26T12:23:49Z-1868</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_9479 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9480 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9481 https://fairsharing.org/FAIRsharing.vajn3f) >
        </DAC (URL_TO_INSERT_RECORD_9482 https://fairsharing.org/FAIRsharing.md3e78) _REF>
        <PO (URL_TO_INSERT_RECORD_9484 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9483 https://fairsharing.org/search?fairsharingRegistry=Policy) _TEXT>https://www.sanger.ac.uk/datasharing/</POLICY_TEXT>
    </PO (URL_TO_INSERT_RECORD_9486 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9485 https://fairsharing.org/search?fairsharingRegistry=Policy) >
</PO (URL_TO_INSERT_RECORD_9488 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9487 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
```


```{note}
In the following example, the file address (url) to the policy (URL_TO_INSERT_TERM_9489 https://fairsharing.org/search?fairsharingRegistry=Policy)  is included in the XML (URL_TO_INSERT_RECORD_9490 https://fairsharing.org/FAIRsharing.b5cc91)  representation.
Ideally, the url provided should be a globally unique persistent identifier (URL_TO_INSERT_TERM_9491 https://fairsharing.org/search?recordType=identifier_schema)  so one can be sure to obtain at least the metadata about the document.
```

```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<PO (URL_TO_INSERT_RECORD_9493 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9492 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
    <PO (URL_TO_INSERT_RECORD_9496 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9494 https://fairsharing.org/search?fairsharingRegistry=Policy)  center_name="EBI" alias="Policy (URL_TO_INSERT_TERM_9495 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868" accession="EGA (URL_TO_INSERT_RECORD_9497 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001" broker_name="EBI">
        <IDENTIFIER (URL_TO_INSERT_TERM_9498 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9499 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9500 https://fairsharing.org/FAIRsharing.vajn3f) >
            <PRIMA (URL_TO_INSERT_RECORD_9504 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9501 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_9503 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001</PRIMA (URL_TO_INSERT_RECORD_9505 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9502 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
            <SUBMITTER_ID namespace="SC">Policy (URL_TO_INSERT_TERM_9506 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_9507 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9508 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9509 https://fairsharing.org/FAIRsharing.vajn3f) >
        <TITLE/>
        <DAC (URL_TO_INSERT_RECORD_9511 https://fairsharing.org/FAIRsharing.md3e78) _REF accession="EGA (URL_TO_INSERT_RECORD_9510 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001" refname="DAC (URL_TO_INSERT_RECORD_9512 https://fairsharing.org/FAIRsharing.md3e78) _-2011-08-26T12:23:49Z-1868" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_9513 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9514 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9515 https://fairsharing.org/FAIRsharing.vajn3f) >
                <PRIMA (URL_TO_INSERT_RECORD_9519 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9516 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_9518 https://fairsharing.org/FAIRsharing.mya1ff) C (URL_TO_INSERT_RECORD_9521 https://fairsharing.org/FAIRsharing.md3e78) 00001000001</PRIMA (URL_TO_INSERT_RECORD_9520 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9517 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
                <SUBMITTER_ID namespace="EBI">DAC (URL_TO_INSERT_RECORD_9522 https://fairsharing.org/FAIRsharing.md3e78) _-2011-08-26T12:23:49Z-1868</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_9523 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9524 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9525 https://fairsharing.org/FAIRsharing.vajn3f) >
        </DAC (URL_TO_INSERT_RECORD_9526 https://fairsharing.org/FAIRsharing.md3e78) _REF>
        <PO (URL_TO_INSERT_RECORD_9528 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9527 https://fairsharing.org/search?fairsharingRegistry=Policy) _FILE>https://www.sanger.ac.uk/datasharing/</POLICY_FILE>
    </PO (URL_TO_INSERT_RECORD_9530 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9529 https://fairsharing.org/search?fairsharingRegistry=Policy) >
</PO (URL_TO_INSERT_RECORD_9532 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9531 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
```


3. Expressing Data Use with EGA XML and **Data Use Ontology** codes.

```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<PO (URL_TO_INSERT_RECORD_9534 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9533 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
    <PO (URL_TO_INSERT_RECORD_9537 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9535 https://fairsharing.org/search?fairsharingRegistry=Policy)  center_name="EBI" alias="Policy (URL_TO_INSERT_TERM_9536 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868" accession="EGA (URL_TO_INSERT_RECORD_9538 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001" broker_name="EBI">
        <IDENTIFIER (URL_TO_INSERT_TERM_9539 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9540 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9541 https://fairsharing.org/FAIRsharing.vajn3f) >
            <PRIMA (URL_TO_INSERT_RECORD_9545 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9542 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_9544 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001</PRIMA (URL_TO_INSERT_RECORD_9546 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9543 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
            <SUBMITTER_ID namespace="SC">Policy (URL_TO_INSERT_TERM_9547 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_9548 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9549 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9550 https://fairsharing.org/FAIRsharing.vajn3f) >
        <TITLE/>
        <DAC (URL_TO_INSERT_RECORD_9552 https://fairsharing.org/FAIRsharing.md3e78) _REF accession="EGA (URL_TO_INSERT_RECORD_9551 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001" refname="DAC (URL_TO_INSERT_RECORD_9553 https://fairsharing.org/FAIRsharing.md3e78) _-2011-08-26T12:23:49Z-1868" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_9554 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9555 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9556 https://fairsharing.org/FAIRsharing.vajn3f) >
                <PRIMA (URL_TO_INSERT_RECORD_9560 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9557 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_9559 https://fairsharing.org/FAIRsharing.mya1ff) C (URL_TO_INSERT_RECORD_9562 https://fairsharing.org/FAIRsharing.md3e78) 00001000001</PRIMA (URL_TO_INSERT_RECORD_9561 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9558 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
                <SUBMITTER_ID namespace="EBI">DAC (URL_TO_INSERT_RECORD_9563 https://fairsharing.org/FAIRsharing.md3e78) _-2011-08-26T12:23:49Z-1868</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_9564 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9565 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9566 https://fairsharing.org/FAIRsharing.vajn3f) >
        </DAC (URL_TO_INSERT_RECORD_9567 https://fairsharing.org/FAIRsharing.md3e78) _REF>
        <PO (URL_TO_INSERT_RECORD_9569 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9568 https://fairsharing.org/search?fairsharingRegistry=Policy) _FILE>https://www.sanger.ac.uk/datasharing/</POLICY_FILE>
        <DATA_USES>
                   	<!-- no restriction -->
   			<DATA_USE>http://purl.obolibrary.org/obo/DUO_0000004</DATA_USE>

			<DATA_USES>
			   <DATA_USE ontology (URL_TO_INSERT_TERM_9570 https://fairsharing.org/search?recordType=terminology_artefact) ="DUO (URL_TO_INSERT_RECORD_9571 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_9572 https://fairsharing.org/FAIRsharing.mjnypw) " code="0000004" version="17-07-2016"/>
			</DATA_USES>

        </DATA_USES>
    </PO (URL_TO_INSERT_RECORD_9574 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9573 https://fairsharing.org/search?fairsharingRegistry=Policy) >
</PO (URL_TO_INSERT_RECORD_9576 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9575 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
```



https://ega-archive.org/dacs

Indicating disease specific restriction on research with DUO and ontologies covering the Disease and Pathology domain.


```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<PO (URL_TO_INSERT_RECORD_9578 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9577 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
    <PO (URL_TO_INSERT_RECORD_9581 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9579 https://fairsharing.org/search?fairsharingRegistry=Policy)  center_name="EBI" alias="Policy (URL_TO_INSERT_TERM_9580 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868" accession="EGA (URL_TO_INSERT_RECORD_9582 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001" broker_name="EBI">
        <IDENTIFIER (URL_TO_INSERT_TERM_9583 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9584 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9585 https://fairsharing.org/FAIRsharing.vajn3f) >
            <PRIMA (URL_TO_INSERT_RECORD_9589 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9586 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_9588 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001</PRIMA (URL_TO_INSERT_RECORD_9590 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9587 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
            <SUBMITTER_ID namespace="SC">Policy (URL_TO_INSERT_TERM_9591 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_9592 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9593 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9594 https://fairsharing.org/FAIRsharing.vajn3f) >
        <TITLE/>
        <DAC (URL_TO_INSERT_RECORD_9596 https://fairsharing.org/FAIRsharing.md3e78) _REF accession="EGA (URL_TO_INSERT_RECORD_9595 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001" refname="DAC (URL_TO_INSERT_RECORD_9597 https://fairsharing.org/FAIRsharing.md3e78) _-2011-08-26T12:23:49Z-1868" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_9598 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9599 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9600 https://fairsharing.org/FAIRsharing.vajn3f) >
                <PRIMA (URL_TO_INSERT_RECORD_9604 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9601 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_9603 https://fairsharing.org/FAIRsharing.mya1ff) C (URL_TO_INSERT_RECORD_9606 https://fairsharing.org/FAIRsharing.md3e78) 00001000001</PRIMA (URL_TO_INSERT_RECORD_9605 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9602 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
                <SUBMITTER_ID namespace="EBI">DAC (URL_TO_INSERT_RECORD_9607 https://fairsharing.org/FAIRsharing.md3e78) _-2011-08-26T12:23:49Z-1868</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_9608 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9609 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9610 https://fairsharing.org/FAIRsharing.vajn3f) >
        </DAC (URL_TO_INSERT_RECORD_9611 https://fairsharing.org/FAIRsharing.md3e78) _REF>
        <PO (URL_TO_INSERT_RECORD_9613 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9612 https://fairsharing.org/search?fairsharingRegistry=Policy) _FILE>https://www.sanger.ac.uk/datasharing/</POLICY_FILE>
        <DATA_USES>
           	<!-- ethics approval required -->
   			<DATA_USE>http://purl.obolibrary.org/obo/DUO_0000021</DATA_USE>
   			<!-- geographical restriction -->
   			<DATA_USE>http://purl.obolibrary.org/obo/DUO_0000022</DATA_USE>
   			<!-- not-for-profit-organization-use-only -->
   			<DATA_USE>http://purl.obolibrary.org/obo/DUO_0000045</DATA_USE>
   			<!-- disease specific research -->
   			<DATA_USE>http://purl.obolibrary.org/obo/DUO_0000007</DATA_USE>
        </DATA_USES>
    </PO (URL_TO_INSERT_RECORD_9615 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9614 https://fairsharing.org/search?fairsharingRegistry=Policy) >
</PO (URL_TO_INSERT_RECORD_9617 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9616 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
```


```{note}
When using the consent code DUO (URL_TO_INSERT_RECORD_9621 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_9623 https://fairsharing.org/FAIRsharing.mjnypw) _0000007 where data is restricted for use on a specific disease area, it is necessary to explicitly indicate which disease area is allowed. This can be done by associating codes/identifier (URL_TO_INSERT_TERM_9619 https://fairsharing.org/search?recordType=identifier_schema) s from well established disease terminologies (URL_TO_INSERT_TERM_9618 https://fairsharing.org/search?recordType=terminology_artefact)  such as MONDO (URL_TO_INSERT_RECORD_9624 https://fairsharing.org/FAIRsharing.b2979t) , DOI (URL_TO_INSERT_RECORD_9622 https://fairsharing.org/FAIRsharing.hFLKCn) D (URL_TO_INSERT_RECORD_9625 https://fairsharing.org/FAIRsharing.8b6wfq) , SNOME (URL_TO_INSERT_RECORD_9620 https://fairsharing.org/3502) D-CT.
For instance, if data reuse is restricted to research (URL_TO_INSERT_RECORD_9629 https://fairsharing.org/FAIRsharing.52b22c)  into `juvenile idiopathic arthritis`, the code should be displayed as DUO (URL_TO_INSERT_RECORD_9626 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_9627 https://fairsharing.org/FAIRsharing.mjnypw) _0000007; MONDO (URL_TO_INSERT_RECORD_9628 https://fairsharing.org/FAIRsharing.b2979t) :0011429
```



```XML
<PO (URL_TO_INSERT_RECORD_9631 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9630 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
  <PO (URL_TO_INSERT_RECORD_9634 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9632 https://fairsharing.org/search?fairsharingRegistry=Policy)  alias="ena-PO (URL_TO_INSERT_RECORD_9635 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9633 https://fairsharing.org/search?fairsharingRegistry=Policy) -BABRAHAM-23-03-2017-09:47:38:853-62" center_name="BABRAHAM" accession="EGA (URL_TO_INSERT_RECORD_9636 https://fairsharing.org/FAIRsharing.mya1ff) P00001000615" broker_name="EGA (URL_TO_INSERT_RECORD_9637 https://fairsharing.org/FAIRsharing.mya1ff) ">  
    <IDENTIFIER (URL_TO_INSERT_TERM_9638 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9639 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9640 https://fairsharing.org/FAIRsharing.vajn3f) > 
      <PRIMA (URL_TO_INSERT_RECORD_9644 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9641 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_9643 https://fairsharing.org/FAIRsharing.mya1ff) P00001000615</PRIMA (URL_TO_INSERT_RECORD_9645 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9642 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
      <SUBMITTER_ID namespace="BABRAHAM">ena-PO (URL_TO_INSERT_RECORD_9647 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9646 https://fairsharing.org/search?fairsharingRegistry=Policy) -BABRAHAM-23-03-2017-09:47:38:853-62</SUBMITTER_ID>
    </IDENTIFIER (URL_TO_INSERT_TERM_9648 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9649 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9650 https://fairsharing.org/FAIRsharing.vajn3f) >
    <TITLE>Data Access Agreement for PC (URL_TO_INSERT_RECORD_9651 https://fairsharing.org/FAIRsharing.5y3gdd) HiC, RNA-Seq, ChIP-Seq</TITLE>
    <DAC (URL_TO_INSERT_RECORD_9653 https://fairsharing.org/FAIRsharing.md3e78) _REF accession="EGA (URL_TO_INSERT_RECORD_9652 https://fairsharing.org/FAIRsharing.mya1ff) C (URL_TO_INSERT_RECORD_9654 https://fairsharing.org/FAIRsharing.md3e78) 00001000523">
      <IDENTIFIER (URL_TO_INSERT_TERM_9655 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9656 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9657 https://fairsharing.org/FAIRsharing.vajn3f) >
        <PRIMA (URL_TO_INSERT_RECORD_9661 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9658 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_9660 https://fairsharing.org/FAIRsharing.mya1ff) C (URL_TO_INSERT_RECORD_9663 https://fairsharing.org/FAIRsharing.md3e78) 00001000523</PRIMA (URL_TO_INSERT_RECORD_9662 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9659 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
      </IDENTIFIER (URL_TO_INSERT_TERM_9664 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9665 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9666 https://fairsharing.org/FAIRsharing.vajn3f) >
    </DAC (URL_TO_INSERT_RECORD_9667 https://fairsharing.org/FAIRsharing.md3e78) _REF>
    <PO (URL_TO_INSERT_RECORD_9669 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9668 https://fairsharing.org/search?fairsharingRegistry=Policy) _FILE>ftp://ftp.ebi.ac.uk/pub/contrib/pchic/EGA_Data_Access_Request_DIL.docx</POLICY_FILE>
    <DATA_USES>
      <DATA_USE ontology (URL_TO_INSERT_TERM_9670 https://fairsharing.org/search?recordType=terminology_artefact) ="DUO (URL_TO_INSERT_RECORD_9671 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_9672 https://fairsharing.org/FAIRsharing.mjnypw) " code="0000007" version="17-07-2016">
      	<!-- disease specific research -->
        <MODIF (URL_TO_INSERT_RECORD_9673 https://fairsharing.org/FAIRsharing.esxaaq) IER>
           <DB>EFO (URL_TO_INSERT_RECORD_9674 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_9675 https://fairsharing.org/FAIRsharing.ca63ce) </DB>
           <ID>0001645</ID>
        </MODIF (URL_TO_INSERT_RECORD_9676 https://fairsharing.org/FAIRsharing.esxaaq) IER> 
        <MODIF (URL_TO_INSERT_RECORD_9677 https://fairsharing.org/FAIRsharing.esxaaq) IER>
           <DB>EFO (URL_TO_INSERT_RECORD_9678 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_9679 https://fairsharing.org/FAIRsharing.ca63ce) </DB>
           <ID>0001655</ID>
        </MODIF (URL_TO_INSERT_RECORD_9680 https://fairsharing.org/FAIRsharing.esxaaq) IER>
       </DATA_USE>
       <DATA_USE ontology (URL_TO_INSERT_TERM_9681 https://fairsharing.org/search?recordType=terminology_artefact) ="DUO (URL_TO_INSERT_RECORD_9682 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_9683 https://fairsharing.org/FAIRsharing.mjnypw) " code="0000014" version="17-07-2016"/>
       </DATA_USES>
   </PO (URL_TO_INSERT_RECORD_9685 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9684 https://fairsharing.org/search?fairsharingRegistry=Policy) >
</PO (URL_TO_INSERT_RECORD_9687 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9686 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
```




https://github.com/enasequence/schema/blob/USI/src/test/resources/uk/ac/ebi/ena/sra/xml/ega_dataset/ega_dataset.xml


```XML
<DATASETS>
    <DATASET alias="EGA (URL_TO_INSERT_RECORD_9688 https://fairsharing.org/FAIRsharing.mya1ff) S000000001-sc-20110919" center_name="SC" broker_name="EGA (URL_TO_INSERT_RECORD_9689 https://fairsharing.org/FAIRsharing.mya1ff) " accession="EGA (URL_TO_INSERT_RECORD_9690 https://fairsharing.org/FAIRsharing.mya1ff) D00001000039">
        <IDENTIFIER (URL_TO_INSERT_TERM_9691 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9692 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9693 https://fairsharing.org/FAIRsharing.vajn3f) >
            <PRIMA (URL_TO_INSERT_RECORD_9697 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9694 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_9696 https://fairsharing.org/FAIRsharing.mya1ff) D00001000039</PRIMA (URL_TO_INSERT_RECORD_9698 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9695 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
            <SUBMITTER_ID namespace="SC">EGA (URL_TO_INSERT_RECORD_9699 https://fairsharing.org/FAIRsharing.mya1ff) S000000001-sc-20110919</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_9700 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9701 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9702 https://fairsharing.org/FAIRsharing.vajn3f) >
        <TITLE>Platelet collagen defect</TITLE>
        <RUN_REF accession="EGA (URL_TO_INSERT_RECORD_9703 https://fairsharing.org/FAIRsharing.mya1ff) R0000000001" refname="RUN_1" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_9704 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9705 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9706 https://fairsharing.org/FAIRsharing.vajn3f) >
                <PRIMA (URL_TO_INSERT_RECORD_9710 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9707 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_9709 https://fairsharing.org/FAIRsharing.mya1ff) R0000000001</PRIMA (URL_TO_INSERT_RECORD_9711 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9708 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
                <SUBMITTER_ID namespace="EBI">RUN_1</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_9712 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9713 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9714 https://fairsharing.org/FAIRsharing.vajn3f) >
        </RUN_REF>
        <PO (URL_TO_INSERT_RECORD_9717 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9715 https://fairsharing.org/search?fairsharingRegistry=Policy) _REF accession="EGA (URL_TO_INSERT_RECORD_9718 https://fairsharing.org/FAIRsharing.mya1ff) P00000001" refname="Policy (URL_TO_INSERT_TERM_9716 https://fairsharing.org/search?fairsharingRegistry=Policy) _-2011-08-17T15:05:39Z-1888" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_9719 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9720 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9721 https://fairsharing.org/FAIRsharing.vajn3f) >
                <PRIMA (URL_TO_INSERT_RECORD_9725 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9722 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_9724 https://fairsharing.org/FAIRsharing.mya1ff) P00001000024</PRIMA (URL_TO_INSERT_RECORD_9726 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9723 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
                <SUBMITTER_ID namespace="EBI">Policy (URL_TO_INSERT_TERM_9727 https://fairsharing.org/search?fairsharingRegistry=Policy) _-2011-08-17T15:05:39Z-1888</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_9728 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9729 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9730 https://fairsharing.org/FAIRsharing.vajn3f) >
        </PO (URL_TO_INSERT_RECORD_9732 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9731 https://fairsharing.org/search?fairsharingRegistry=Policy) _REF>
    </DATASET>
</DATASETS>
```




Browsing Data Access Committees available from EGA:

````{dropdown}
:open:
```{figure} dac-ega.png
---
width: 700px
name: 
alt: List of Data Access Policy from EGA
---
List of Data Access Policy from EGA
```
````


### ODRL, Open Digital Rights Language

ODRL stands for Open Digital Rights Language and is a set of W3C Recommendations defining a **policy expression language**. 

ODRL is made up of several components:

- [The ODRL Model](https://www.w3.org/TR/odrl-model/) {footcite}`ODRLmodel`

````{dropdown}
:open:
```{figure} https://www.w3.org/TR/odrl-model/00Model.png
---
width: 700px
name: 
alt: Open Digital Rights Language model
---
ODRL overview
```
````


- [The ODRL Vocabulary](https://www.w3.org/TR/odrl-vocab/) {footcite}`ODRLvocab`

The **ODRL Vocabulary and Expression** provides the terms to express policies in RDF language.

The ODRL Vocabulary and Expression complements the ODRL information model, which allows expressing similar information in JSON language.



```{warning}
In 2015, the dedicated working group produced the following JSO (URL_TO_INSERT_RECORD_9734 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_9733 https://fairsharing.org/FAIRsharing.5bbab9)  schema implementation guidance
https://www.w3.org/community/odrl/json/2.1/#section-Schema

We base our representations on this specification {footcite}`ODR (URL_TO_INSERT_RECORD_9737 https://fairsharing.org/FAIRsharing.1sfhp3) LJSO (URL_TO_INSERT_RECORD_9736 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_9735 https://fairsharing.org/FAIRsharing.5bbab9) `. 

We are aware of a possible misalignment between the specifications of the Working Group (from 2015) and the latest
specifications as to whether to use the keys "name" or "leftOperand" (https://www.w3.org/TR/odrl-model/#constraint-rule, 2018).
In the following representations, we use the key "name" to validate against the 2015 JSO (URL_TO_INSERT_RECORD_9739 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_9738 https://fairsharing.org/FAIRsharing.5bbab9) -schema
 https://www.w3.org/community/odrl/json/2.1/#section-Schema / https://github.com (URL_TO_INSERT_RECORD_9740 https://fairsharing.org/FAIRsharing.c55d5e) /iptc/rightsml-dev/blob/master/licensed/ODRL21.json

```

#### The different types of Policies

The ODRL model defines several subclasses for the **Policy** entity, namely  **Agreement**, **Set**, **Offer**.

##### Describing an agreement with ODRL

```json
{
    "policy (URL_TO_INSERT_TERM_9741 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Agreement",
    "policy (URL_TO_INSERT_TERM_9742 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "http://example.com/policy:5531",
    "inheritallowed": true,
    "permissions": [{
        "target": "http://example.com/report:2321",
        "action": "http://www.w3.org/ns/odrl/2/print",
        "assigner": "http://example.com/pub:88",
        "assignee": "http://example.com/billie:888"
    }]
}
{
    "policy (URL_TO_INSERT_TERM_9743 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Agreement",
    "policy (URL_TO_INSERT_TERM_9744 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "http://example.com/policy:9999",
    "inheritfrom": "http://example.com/policy:5531",
    "permissions": [{
        "target": "http://example.com/report:2333",
        "action": "http://www.w3.org/ns/odrl/2/display",
        "assigner": "http://example.com/pub:88",
        "assignee": "http://example.com/class:IT01",
        "assignee_scope": "http://www.w3.org/ns/odrl/2/group"
    }]
}
```


### Encoding Research Restriction on disease and geographical area using ODRL and DUO

In this section, we document how to rely on a basic ODRL-based pattern using a DUO term {footcite}`DUO` to represent a
situation where SecondaryUse of the data is allowed on the condition that work is restricted to **disease specific research**.


```json
{
    "policy (URL_TO_INSERT_TERM_9745 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_9746 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "https://fairplus.github.io/examples/policy_122334",
    "permissions": [
        {
        "target": "https://fairplus.github.io/examples/dataset_00001",
        "action": "http://www.w3.org/ns/odrl/2/secondaryUse",
        "assigner": "https://fairplus.github.io/examples/examples/efpia_organization_00002",
        "constraints":[{
              "name": "http://www.w3.org/ns/odrl/2/purpose",
              "operator": "http://www.w3.org/ns/odrl/2/eq",
              "rightoperand": "http://purl.obolibrary.org/obo/DUO_0000007"
            }
            ]
        }
    ]
}
```

```{note}
:class: tip
The main limitation of the representation is that it provides no informat (URL_TO_INSERT_TERM_9747 https://fairsharing.org/search?recordType=model_and_format) ion about which diseases are vetted for research (URL_TO_INSERT_RECORD_9748 https://fairsharing.org/FAIRsharing.52b22c) .
```

The following representation is more sophisticated and includes 3 types of restrictions:

- restriction on specific disease (juvenile arthritis, to reuse the exemplar representation in EGA/SRA XML presented in section 1)
- restriction on the geographical location where the research can be conducted
- an obligation to delete the data obtained through the access agreement past a specified duration, 3 years in our example

Let's proceed stepwise.


* Representing Research Restriction on Specific Disease Area using DUO and MONDO ontologies


```json
{
    "policy (URL_TO_INSERT_TERM_9749 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_9750 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "https://fairplus.github.io/examples/policy_122334",
    "permissions": [
        {
            "target": "https://fairplus.github.io/examples/dataset_00001",
            "action": [{
                "rdf:value": { "@id": "odrl:secondaryUse" },
                "refinement": {
                        "xone": { 
                        "@list": [ 
                            { "@id": "http://purl.obolibrary.org/obo/MONDO_0011429" },
                            { "@id": "http://purl.obolibrary.org/obo/EFO_0001645" },
                            { "@id": "http://purl.obolibrary.org/obo/EFO_0001655" }  
                        ]
                    }
                }
            }],
            "assigner": "https://fairplus.github.io/examples/examples/efpia_organization_00002",
            "constraints":[{
                "name": "http://www.w3.org/ns/odrl/2/purpose",
                "operator": "http://www.w3.org/ns/odrl/2/eq",
                "rightoperand": "http://purl.obolibrary.org/obo/DUO_0000007"
                }
            ]
        }
    ]
}
```

```{note}

When using refinements, note the difference in representation to indicate the nature of the action.
here it uses:

while the ordinary is simpler: 
"action": "http://www.w3.org/ns/odrl/2/secondaryUse",

vs

"action": [{
           		"rdf:value": { "@id": "odrl:secondaryUse" },
```


```{note}
While DUO (URL_TO_INSERT_RECORD_9752 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_9753 https://fairsharing.org/FAIRsharing.mjnypw)  is unique in its coverage of data uses, various disease ontologies (URL_TO_INSERT_TERM_9751 https://fairsharing.org/search?recordType=terminology_artefact)  exist and may be used to specify the
specific focus research (URL_TO_INSERT_RECORD_9754 https://fairsharing.org/FAIRsharing.52b22c)  should have.
For instance, SNOME (URL_TO_INSERT_RECORD_9756 https://fairsharing.org/3502) D-CT, Disease Ontology (URL_TO_INSERT_TERM_9755 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_9757 https://fairsharing.org/FAIRsharing.8b6wfq)  could also be used.
It is worth noting that extensive cross referencing exists between resources such as DOI (URL_TO_INSERT_RECORD_9758 https://fairsharing.org/FAIRsharing.hFLKCn) D (URL_TO_INSERT_RECORD_9760 https://fairsharing.org/FAIRsharing.8b6wfq) , MONDO (URL_TO_INSERT_RECORD_9759 https://fairsharing.org/FAIRsharing.b2979t)  and
SNOME (URL_TO_INSERT_RECORD_9761 https://fairsharing.org/3502) D-CT but this is something to consider when implementing brokering systems.
```



* Representing Research Restriction based on Geographical Regions

The section shows how to use ODRL to document geographical restrictions, either by listing countries where research is 
allowed or by listing those countries excluded from doing so.

In the following example, research is only allowed in a specific country, **Italy** in this case, which is 
encoded using the **ISO-3166 code**.


```json
{
    "policy (URL_TO_INSERT_TERM_9762 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_9763 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "https://fairplus.github.io/examples/policy_122334",
    "permissions": [
        {
            "target": "https://fairplus.github.io/examples/dataset_00001",
            "action": [{
           	    "rdf:value": { "@id": "odrl:secondaryUse" },
                    "refinement": {
                        "xone": { 
                        "@list": [ 
                        { "@id": "http://purl.obolibrary.org/obo/MONDO_0011429" },
                        { "@id": "http://purl.obolibrary.org/obo/EFO_0001645" },
                        { "@id": "http://purl.obolibrary.org/obo/EFO_0001655" }  
                        ]
                    }
                }
            }],
            "assigner": "https://fairplus.github.io/examples/examples/efpia_organization_00002",
            "constraints":[{
                "name": "http://www.w3.org/ns/odrl/2/purpose",
                "operator": "http://www.w3.org/ns/odrl/2/eq",
                "rightoperand": "http://purl.obolibrary.org/obo/DUO_0000007"
                },
                {
                "name": "http://www.w3.org/ns/odrl/2/spatial",
                "operator": "http://www.w3.org/ns/odrl/2/eq",
                "rightoperand": "http://www.itu.int/tML/tML-ISO-3166:it"
            }
            ]
        }
    ]
}
```

* Representing Obligations regarding Data Management

The following example shows how to explicitly state in a Policy element that the data must be deleted after a defined
period of time (3 years in this example).
Duration and time related value should be represented using **ISO-8601 standard**.

```json
{
    "policy (URL_TO_INSERT_TERM_9764 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_9765 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "https://fairplus.github.io/examples/policy_122334",
    "permissions": [
        {
            "target": "https://fairplus.github.io/examples/dataset_00001",
            "action": "http://www.w3.org/ns/odrl/2/secondaryUse",
            "action": [{
                "rdf:value": { "@id": "odrl:secondaryUse" },
                "refinement": {
                    "xone": { 
                    "@list": [ 
                            { "@id": "http://purl.obolibrary.org/obo/MONDO_0011429" },
                            { "@id": "http://purl.obolibrary.org/obo/EFO_0001645" },
                            { "@id": "http://purl.obolibrary.org/obo/EFO_0001655" }  
                        ]
                  }
                }
            }],
            "assigner": "https://fairplus.github.io/examples/examples/efpia_organization_00002",
            "constraints":[{
                    "name": "http://www.w3.org/ns/odrl/2/purpose",
                    "operator": "http://www.w3.org/ns/odrl/2/eq",
                    "rightoperand": "http://purl.obolibrary.org/obo/DUO_0000007"
                },
                {
                "name": "http://www.w3.org/ns/odrl/2/spatial",
                "operator": "http://www.w3.org/ns/odrl/2/eq",
                "rightoperand": "http://www.itu.int/tML/tML-ISO-3166:it"
            }
            ],
            "duties": [{
                "action": "http://www.w3.org/ns/odrl/2/delete",
                "target": "https://fairplus.github.io/examples/dataset_00001",
                "constraints": [{
                    "name": "http://www.w3.org/ns/odrl/2/dateTime",
                    "operator": "http://www.w3.org/ns/odrl/2/eq",
                    "rightoperand": "P36M"
                }]
        }]
        }
    ]
}
```


## Possible specifications of EGA related information using ODRL

```{warning} 

This ODR (URL_TO_INSERT_RECORD_9767 https://fairsharing.org/FAIRsharing.1sfhp3) L representation is **not vetted, nor endorsed by GA4GH or EGA (URL_TO_INSERT_RECORD_9766 https://fairsharing.org/FAIRsharing.mya1ff) **.
This example is currently meant to present an example of how to use ODR (URL_TO_INSERT_RECORD_9770 https://fairsharing.org/FAIRsharing.1sfhp3) L to represent some of the informat (URL_TO_INSERT_TERM_9768 https://fairsharing.org/search?recordType=model_and_format) ion represented in EGA (URL_TO_INSERT_RECORD_9769 https://fairsharing.org/FAIRsharing.mya1ff) .

```

```json
{
    "policy (URL_TO_INSERT_TERM_9771 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_9772 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "https://ega-archive.org (URL_TO_INSERT_RECORD_9773 https://fairsharing.org/FAIRsharing.mya1ff) /datasets/EGAP0000000XYZ",
    "permissions": [
        {
            "target": "https://ega-archive.org (URL_TO_INSERT_RECORD_9774 https://fairsharing.org/FAIRsharing.mya1ff) /datasets/EGAD0000000YYY",
            "action": [{
                "rdf:value": { "@id": "odrl:secondaryUse" },
                "refinement": {
                    "xone": { 
                    "@list": [ 
                            { "@id": "http://purl.obolibrary.org/obo/MONDO_0011429" },
                            { "@id": "http://purl.obolibrary.org/obo/EFO_0001645" },
                            { "@id": "http://purl.obolibrary.org/obo/EFO_0001655" }  
                        ]
                  }
                }
            }],
            "assigner": "https://ega-archive.org (URL_TO_INSERT_RECORD_9775 https://fairsharing.org/FAIRsharing.mya1ff) /",
            "constraints":[{
                    "name": "http://www.w3.org/ns/odrl/2/purpose",
                    "operator": "http://www.w3.org/ns/odrl/2/eq",
                    "rightoperand": "http://purl.obolibrary.org/obo/DUO_0000007"
                },
                {
                "name": "http://www.w3.org/ns/odrl/2/spatial",
                "operator": "http://www.w3.org/ns/odrl/2/eq",
                "rightoperand": "http://www.itu.int/tML/tML-ISO-3166:it"
            }
            ],
            "duties": [{
                "action": "http://www.w3.org/ns/odrl/2/delete",
                "target": "https://ega-archive.org (URL_TO_INSERT_RECORD_9776 https://fairsharing.org/FAIRsharing.mya1ff) /datasets/EGAD0000000YYY",
                "constraints": [{
                    "name": "http://www.w3.org/ns/odrl/2/dateTime",
                    "operator": "http://www.w3.org/ns/odrl/2/eq",
                    "rightoperand": "P36M"
                }]
        }]
        }
    ]
}
```

### Indicating Prohibitions and Interdictions

The ODRL model {footcite}`ODRLmodel` provides the **prohibitions** relation, which uses similar patterns to those seen while covering **permissions**.
The ODRL vocabulary is then used to identify the **actions** which are restricted under the **prohibition** header. 
Complex prohibitions can be expressed using **constraints** and **refinement** elements.


```json
{
    "policy (URL_TO_INSERT_TERM_9777 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_9778 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "http://example.com/policy:0099",
    "permissions": [{
        "target": "http://example.com/asset:9898",
        "action": "http://www.w3.org/ns/odrl/2/reproduce"
    }],
    "prohibitions": [{
        "target": "http://example.com/asset:9898",
        "action": "http://www.w3.org/ns/odrl/2/modify"
    }]
}
```



## Implementation in Data Catalogues built with DCAT or DATS


### Referring to an ODRL Policy from a DCAT DataSet

```bash
@prefix dcat:<https://www.w3.org/ns/dcat> .
@prefix odrl:<https://www.w3.org/ns/odrl/2/core> .
@prefix dct: <http://purl.org/dc/elements/1.1/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<#daa-policy (URL_TO_INSERT_TERM_9779 https://fairsharing.org/search?fairsharingRegistry=Policy) -1>
 a odrl:Policy (URL_TO_INSERT_TERM_9780 https://fairsharing.org/search?fairsharingRegistry=Policy)  .

<#dataset-001>
  a dcat:Dataset ;
  dct:title "Human Patient Genomic Dataset"@en ;
  dcat:keyword "genotype"@en, "phenotyping"@en, "IMI"@en ;
  dct:creator "imi-consortium-XYZ" ;
  dct:issued "2021-12-05"^^xsd:date ;
  dct:modified "2021-12-15"^^xsd:date ;
  dcat:contactPoint <http://example.org/imi-project-xyz/contact1> ;
  dct:publisher "imi-consortium-XYZ";
  dct:language <http://id.loc.gov/vocabulary/iso639-1/en>  ;
  dcat:distribution _:dataset-001-csv ;
  odrl:hasPolicy (URL_TO_INSERT_TERM_9781 https://fairsharing.org/search?fairsharingRegistry=Policy)  <#daa-policy (URL_TO_INSERT_TERM_9782 https://fairsharing.org/search?fairsharingRegistry=Policy) -1>;
  .

```

For more details, please see the following publication by [de Vos et al, 2019](https://www.specialprivacy.eu/images/documents/RuleMLRR_2019_.pdf)

### DATS and ODRL JSON

An evolution of the DATS {footcite}`pmid28585923`, {footcite}`pmid32031623` schema is used by University of Luxembourg 
to build a data catalogue for IMI projects and datasets.
The proposed patterns could be used and tested to representation DAC/DAA information as well as the allowed uses of 
datasets generated by the consortia funded by IMI.
More complex use cases can be considered to assess to ability of the representations to be associated to specific 
datasets, for instance datasets associated with a particular data acquisition technique the access of which may require 
specific policies and conditions to be made machine-readable.

The approach is therefore to reference the  JSON representations compliant with the ODRL JSON schema 2.1 specification,
as presented in earlier sections in conjunction with DATS JSON documents.



### Validating ODRL RDF documents

Code exists that allows developers to validate ODRL documents **expressed in legitimate RDF serializations**.

http://odrlapi.appspot.com/


````{dropdown}
:open:
```{figure} ./odrl-validation-app.png
---
width: 800px
alt: ODRL Validation and Evaluation Sandbox
name: ODRL Validation and Evaluation Sandbox
---
ODRL Validation and Evaluation Sandbox
```
````


The web-application is powered by a REST-API the swagger document of which is available from the following address:
http://odrlapi.appspot.com/apidoc/index.html

<!-- ## TODO discuss relation to RightML

https://iptc.org/std/RightsML/2.0/RightsML_2.0-specification.html -->

## Consuming Data Use related annotations

It is all good and well to describe patterns in various formats but are there any tools or services capable exploiting these annotations?
Well, when it comes to genomics data, there is the Broad Institute's 
[Data Use Oversight System (DUOS)](https://duos.broadinstitute.org/#/home) is one such tool.

````{dropdown}
:open:
```{figure} ./broads-duos.png
---
width: 800px
alt: Broad's Institute  Data Use Oversight System
name: Broad's Institute  Data Use Oversight System
---
Broad's Institute  Data Use Oversight System landing page
```
````

DUOS requires official clearance from a **Data Access Committee** representative or an **Authorized Submission Representative** 
to enable registration of a dataset into the DUOS.
Once this authorization is available, the dataset has to be annotated following the patterns defined by GA4GH with
Data Use Ontology {footcite}`pmid26796797` and 'SRA XML' format.

The European Genome Archive allows programmatic filtering based on this information via the REST-API of the service.

## Conclusion

Making sure that machine-readable information about the conditions of use of datasets and data is available is key to 
enable privacy preserving and policy compliant use of information across organizations.
This content provides an overview of the models available to do so and how it has been applied to life science data, 
showing the main features of the models and how to define use based on the major properties such as the type of research
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
Tom: Conceptualization, Writing, Review & Editing
Philippe: Conceptualization,Writing - Original Draft, Review & Editing 
Melanie: Review & Editing 
Fuqi: Review & Editing 
Wei: Review & Editing 
````


## License

````{license_fairplus}
CC-BY-4.0
````

