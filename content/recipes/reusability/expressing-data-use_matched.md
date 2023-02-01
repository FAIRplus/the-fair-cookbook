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

The aim is also to document equivalent representations and how bridges (URL_TO_INSERT_RECORD_10599 https://fairsharing.org/FAIRsharing.ac95d5)  can be built between the distinct but equivalent implementations.

Finally, the content aims to highlight key use-cases which require coverage, how to code such informat (URL_TO_INSERT_TERM_10600 https://fairsharing.org/search?recordType=model_and_format) ion, documenting 
implementation patterns in the context of **data cataloguing efforts**, for instance by expressing **Data Access Policies (URL_TO_INSERT_TERM_10601 https://fairsharing.org/search?fairsharingRegistry=Policy) **.


## Graphical Overview


````{dropdown}
:open:
```{figure} data-usage-mermaid.png
---
width: 850px
name: expressing-data-use-figure1
alt: Dealing with Policies (URL_TO_INSERT_TERM_10602 https://fairsharing.org/search?fairsharingRegistry=Policy)  and Data Use
---
Data Use
```
````



---

## Tools

### Standards

 Data Format (URL_TO_INSERT_TERM_10604 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_10605 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_10603 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
| JSO (URL_TO_INSERT_RECORD_10607 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_10606 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_10610 https://fairsharing.org/FAIRsharing.8f9bbb) <!-- TO (URL_TO_INSERT_RECORD_10608 https://fairsharing.org/FAIRsharing.w69t6r) DO add a link to corresponding document --> | <!-- TO (URL_TO_INSERT_RECORD_10609 https://fairsharing.org/FAIRsharing.w69t6r) DO add a link to corresponding document -->  |   |
| [ISO-8601](https://www.iso.org/iso-8601-date-and-time-format.html)  | [DC (URL_TO_INSERT_RECORD_10614 https://fairsharing.org/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD_10615 https://fairsharing.org/3547) AT (URL_TO_INSERT_RECORD_10611 https://fairsharing.org/FAIRsharing.3a96ae)  (URL_TO_INSERT_RECORD_10612 https://fairsharing.org/FAIRsharing.h4j3qm)  v2](https://www.w3.org/TR/vocab-dcat (URL_TO_INSERT_RECORD_10613 https://fairsharing.org/FAIRsharing.h4j3qm) -2/)  |   |
| [ISO-3066](https://www.iso.org/iso-3166-country-codes.html)  | [ODRL](https://www.w3.org/TR/odrl-vocab/)  |   |
| EGA (URL_TO_INSERT_RECORD_10618 https://fairsharing.org/FAIRsharing.mya1ff)  XML (URL_TO_INSERT_RECORD_10616 https://fairsharing.org/FAIRsharing.b5cc91) <!-- TO (URL_TO_INSERT_RECORD_10619 https://fairsharing.org/FAIRsharing.w69t6r) DO add a link to corresponding document -->   | [DUO](http://www.obofoundry.org (URL_TO_INSERT_RECORD_10617 https://fairsharing.org/FAIRsharing.847069) /ontology/duo.html)  |   |
| [Data Article Tag Suite (DATS)](https://datatagsuite.github.io/schema/)  | [MONDO](http://www.obofoundry.org (URL_TO_INSERT_RECORD_10620 https://fairsharing.org/FAIRsharing.847069) /ontology/mondo.html)  |   |




### Implementation

DUO (URL_TO_INSERT_RECORD_10621 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_10622 https://fairsharing.org/FAIRsharing.mjnypw) S:
https://duos.broadinstitute.org/

---

## Introduction

The preservation of patient privacy and the compliance with patient consent are essential considerations when managing
sensitive informat (URL_TO_INSERT_TERM_10623 https://fairsharing.org/search?recordType=model_and_format) ion such as clinical and patient data.
Consent forms, as signed by patients, define the acceptable usage of data derived from a patient for research (URL_TO_INSERT_RECORD_10624 https://fairsharing.org/FAIRsharing.52b22c)  applications.
All major research (URL_TO_INSERT_RECORD_10625 https://fairsharing.org/FAIRsharing.52b22c)  organizations, at national and international levels, enforce strict rules for the management of such data.
Sensitive data cannot be accessed without undergoing a vetting process involving a **data access request** to a **data access committee**,
which will decide, whether or not, to grant requesters access to the data.

This is a time-consuming process in the absence of machine-readable version of data access/ data management policies (URL_TO_INSERT_TERM_10626 https://fairsharing.org/search?fairsharingRegistry=Policy) .
In turns, it can prove detrimental to research (URL_TO_INSERT_RECORD_10627 https://fairsharing.org/FAIRsharing.52b22c) .
Therefore, efforts to enable the provision of concise, efficient and **machine processable** summary of key permissions and prohibitions have been made. 
Several resources are now available for the coding and exchange of **machine-actionable**, **legally binding** and
**explicit** informat (URL_TO_INSERT_TERM_10628 https://fairsharing.org/search?recordType=model_and_format) ion related to allowed and consented data usage.

The following sections detail how the international sequence data arch (URL_TO_INSERT_RECORD_10630 https://fairsharing.org/FAIRsharing.52b22c) ives (US NCBI dbGAP, SRA (URL_TO_INSERT_RECORD_10632 https://fairsharing.org/FAIRsharing.g7t2hv)  and EU EMB (URL_TO_INSERT_RECORD_10631 https://fairsharing.org/FAIRsharing.a1rp4c) L_EBI EGA (URL_TO_INSERT_RECORD_10629 https://fairsharing.org/FAIRsharing.mya1ff) )
are encoding **Data Use Informat (URL_TO_INSERT_TERM_10633 https://fairsharing.org/search?recordType=model_and_format) ion**  but also how ODR (URL_TO_INSERT_RECORD_10634 https://fairsharing.org/FAIRsharing.1sfhp3) L, a W3C specification, 
can be used to represent equivalent informat (URL_TO_INSERT_TERM_10635 https://fairsharing.org/search?recordType=model_and_format) ion in a format (URL_TO_INSERT_TERM_10636 https://fairsharing.org/search?recordType=model_and_format)  compatible with the data cataloguing efforts relying on W3C DC (URL_TO_INSERT_RECORD_10639 https://fairsharing.org/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD_10640 https://fairsharing.org/3547) AT (URL_TO_INSERT_RECORD_10637 https://fairsharing.org/FAIRsharing.3a96ae)  (URL_TO_INSERT_RECORD_10638 https://fairsharing.org/FAIRsharing.h4j3qm)  specifications.




### SRA & EGA XML schema for Policy, Dataset and Controller

Next Generation Sequencing (NGS) techniques allow routine production of full genome data from patients.
This data is highly sensitive and data repositories (URL_TO_INSERT_TERM_10641 https://fairsharing.org/search?recordType=repository)  specialized in storing such informat (URL_TO_INSERT_TERM_10642 https://fairsharing.org/search?recordType=model_and_format) ion have developed (URL_TO_INSERT_RECORD_10643 https://fairsharing.org/FAIRsharing.31385c)  procedures 
and representation model (URL_TO_INSERT_TERM_10644 https://fairsharing.org/search?recordType=model_and_format) s for defining the conditions of use.

We summarize here the key objects used by the European Genome Arch (URL_TO_INSERT_RECORD_10649 https://fairsharing.org/FAIRsharing.52b22c) ive, in compliance with INSD (URL_TO_INSERT_RECORD_10646 https://fairsharing.org/FAIRsharing.mKDii0) C (URL_TO_INSERT_RECORD_10648 https://fairsharing.org/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD_10650 https://fairsharing.org/3547)  and GA4GH (URL_TO_INSERT_RECORD_10647 https://fairsharing.org/FAIRsharing.2tpx4v)  guideline (URL_TO_INSERT_TERM_10645 https://fairsharing.org/search?recordType=reporting_guideline) s.

https://ega-archive.org (URL_TO_INSERT_RECORD_10651 https://fairsharing.org/FAIRsharing.mya1ff) /data-use-conditions

````{dropdown}
:open:
```{figure} duo-ols-view-1.png
---
width: 700px
name: expressing-data-use-figure2
alt: Data Use Ontology (URL_TO_INSERT_TERM_10652 https://fairsharing.org/search?recordType=terminology_artefact)  Overview Part 1
---
Data Use Ontology (URL_TO_INSERT_TERM_10653 https://fairsharing.org/search?recordType=terminology_artefact)  Overview Part 1
```
````

````{dropdown}
:open:
```{figure} duo-ols-view-2.png
---
width: 700px
name: expressing-data-use-figure3
alt: Data Use Ontology (URL_TO_INSERT_TERM_10654 https://fairsharing.org/search?recordType=terminology_artefact)  Overview Part 2
---
Data Use Ontology (URL_TO_INSERT_TERM_10655 https://fairsharing.org/search?recordType=terminology_artefact)  Overview Part 2
```
````

<!-- 
````{panels}
:column: col-8
:card: border-2
DUO in OLS
^^^
```{figure} duo-ols-view-1.png
width: 400px
```
---
DUO in OLS
^^^
```{figure} duo-ols-view-2.png
width: 400px
```

```` -->


The informat (URL_TO_INSERT_TERM_10656 https://fairsharing.org/search?recordType=model_and_format) ion presented below has been sourced from the ENA (URL_TO_INSERT_RECORD_10657 https://fairsharing.org/FAIRsharing.dj8nt8)  GitHub (URL_TO_INSERT_RECORD_10658 https://fairsharing.org/FAIRsharing.c55d5e)  (URL_TO_INSERT_RECORD_10659 https://fairsharing.org/FAIRsharing.c55d5e)  repo.



1. The **Data Access Committee** and Contact informat (URL_TO_INSERT_TERM_10660 https://fairsharing.org/search?recordType=model_and_format) ion

```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<DAC_SET>
    <DAC alias="DAC-2011-08-11T11:45:28Z-1873" accession="EGAC00000000001" center_name="EBI" broker_name="EGA">
        <IDENTIFIERS>
            <PRIMARY_ID>EGAC00000000001</PRIMARY_ID>
            <SUBMITTER_ID namespace="EBI">DAC-2011-08-11T11:45:28Z-1873</SUBMITTER_ID>
        </IDENTIFIERS>
        <TITLE>EGA DAC TITLE</TITLE>
        <CONTACTS>
            <CONTACT name="Joe Bloggs" email="joe@noname.com" organisation="EBI"/>
        </CONTACTS>
    </DAC>
</DAC_SET>
```


https://github.com (URL_TO_INSERT_RECORD_10661 https://fairsharing.org/FAIRsharing.c55d5e) /enasequence/schema/blob/USI/src/test/resources/uk/ac/ebi/ena/sra/xml/ega_dac/ega_dac.xml

2. The **Data Access Policy (URL_TO_INSERT_TERM_10662 https://fairsharing.org/search?fairsharingRegistry=Policy) ** object


https://github.com (URL_TO_INSERT_RECORD_10663 https://fairsharing.org/FAIRsharing.c55d5e) /enasequence/schema/blob/USI/src/test/resources/uk/ac/ebi/ena/sra/xml/ega_policy/ega_policy.xml

```{note}
in the following example, the text of the policy is present in the XML representation
```


```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<POLICY_SET>
    <POLICY center_name="EBI" alias="Policy-2011-08-26T12:23:53Z-1868" accession="EGAP00001000001" broker_name="EBI">
        <IDENTIFIERS>
            <PRIMARY_ID>EGAP00001000001</PRIMARY_ID>
            <SUBMITTER_ID namespace="SC">Policy-2011-08-26T12:23:53Z-1868</SUBMITTER_ID>
        </IDENTIFIERS>
        <TITLE/>
        <DAC_REF accession="EGAP00001000001" refname="DAC_-2011-08-26T12:23:49Z-1868" refcenter="EBI">
            <IDENTIFIERS>
                <PRIMARY_ID>EGAC00001000001</PRIMARY_ID>
                <SUBMITTER_ID namespace="EBI">DAC_-2011-08-26T12:23:49Z-1868</SUBMITTER_ID>
            </IDENTIFIERS>
        </DAC_REF>
        <POLICY_TEXT>https://www.sanger.ac.uk/datasharing/</POLICY_TEXT>
    </POLICY>
</POLICY_SET>
```


```{note}
In the following example, the file address (url) to the policy is included in the XML representation.
Ideally, the url provided should be a globally unique persistent identifier so one can be sure to obtain at least the metadata about the document.
```

```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<POLICY_SET>
    <POLICY center_name="EBI" alias="Policy-2011-08-26T12:23:53Z-1868" accession="EGAP00001000001" broker_name="EBI">
        <IDENTIFIERS>
            <PRIMARY_ID>EGAP00001000001</PRIMARY_ID>
            <SUBMITTER_ID namespace="SC">Policy-2011-08-26T12:23:53Z-1868</SUBMITTER_ID>
        </IDENTIFIERS>
        <TITLE/>
        <DAC_REF accession="EGAP00001000001" refname="DAC_-2011-08-26T12:23:49Z-1868" refcenter="EBI">
            <IDENTIFIERS>
                <PRIMARY_ID>EGAC00001000001</PRIMARY_ID>
                <SUBMITTER_ID namespace="EBI">DAC_-2011-08-26T12:23:49Z-1868</SUBMITTER_ID>
            </IDENTIFIERS>
        </DAC_REF>
        <POLICY_FILE>https://www.sanger.ac.uk/datasharing/</POLICY_FILE>
    </POLICY>
</POLICY_SET>
```


3. Expressing Data Use with EGA (URL_TO_INSERT_RECORD_10666 https://fairsharing.org/FAIRsharing.mya1ff)  XML (URL_TO_INSERT_RECORD_10665 https://fairsharing.org/FAIRsharing.b5cc91)  and **Data Use Ontology (URL_TO_INSERT_TERM_10664 https://fairsharing.org/search?recordType=terminology_artefact) ** codes.

```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<POLICY_SET>
    <POLICY center_name="EBI" alias="Policy-2011-08-26T12:23:53Z-1868" accession="EGAP00001000001" broker_name="EBI">
        <IDENTIFIERS>
            <PRIMARY_ID>EGAP00001000001</PRIMARY_ID>
            <SUBMITTER_ID namespace="SC">Policy-2011-08-26T12:23:53Z-1868</SUBMITTER_ID>
        </IDENTIFIERS>
        <TITLE/>
        <DAC_REF accession="EGAP00001000001" refname="DAC_-2011-08-26T12:23:49Z-1868" refcenter="EBI">
            <IDENTIFIERS>
                <PRIMARY_ID>EGAC00001000001</PRIMARY_ID>
                <SUBMITTER_ID namespace="EBI">DAC_-2011-08-26T12:23:49Z-1868</SUBMITTER_ID>
            </IDENTIFIERS>
        </DAC_REF>
        <POLICY_FILE>https://www.sanger.ac.uk/datasharing/</POLICY_FILE>
        <DATA_USES>
                   	<!-- no restriction -->
   			<DATA_USE>http://purl.obolibrary.org/obo/DUO_0000004</DATA_USE>

			<DATA_USES>
			   <DATA_USE ontology="DUO" code="0000004" version="17-07-2016"/>
			</DATA_USES>

        </DATA_USES>
    </POLICY>
</POLICY_SET>
```



https://ega-archive.org (URL_TO_INSERT_RECORD_10667 https://fairsharing.org/FAIRsharing.mya1ff) /dacs

Indicating disease specific restriction on research (URL_TO_INSERT_RECORD_10671 https://fairsharing.org/FAIRsharing.52b22c)  with DUO (URL_TO_INSERT_RECORD_10669 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_10670 https://fairsharing.org/FAIRsharing.mjnypw)  and ontologies (URL_TO_INSERT_TERM_10668 https://fairsharing.org/search?recordType=terminology_artefact)  covering the Disease and Pathology domain.


```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<POLICY_SET>
    <POLICY center_name="EBI" alias="Policy-2011-08-26T12:23:53Z-1868" accession="EGAP00001000001" broker_name="EBI">
        <IDENTIFIERS>
            <PRIMARY_ID>EGAP00001000001</PRIMARY_ID>
            <SUBMITTER_ID namespace="SC">Policy-2011-08-26T12:23:53Z-1868</SUBMITTER_ID>
        </IDENTIFIERS>
        <TITLE/>
        <DAC_REF accession="EGAP00001000001" refname="DAC_-2011-08-26T12:23:49Z-1868" refcenter="EBI">
            <IDENTIFIERS>
                <PRIMARY_ID>EGAC00001000001</PRIMARY_ID>
                <SUBMITTER_ID namespace="EBI">DAC_-2011-08-26T12:23:49Z-1868</SUBMITTER_ID>
            </IDENTIFIERS>
        </DAC_REF>
        <POLICY_FILE>https://www.sanger.ac.uk/datasharing/</POLICY_FILE>
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
    </POLICY>
</POLICY_SET>
```


```{note}
When using the consent code DUO_0000007 where data is restricted for use on a specific disease area, it is necessary to explicitly indicate which disease area is allowed. This can be done by associating codes/identifiers from well established disease terminologies such as MONDO, DOID, SNOMED-CT.
For instance, if data reuse is restricted to research into `juvenile idiopathic arthritis`, the code should be displayed as DUO_0000007; MONDO:0011429
```



```XML
<POLICY_SET>
  <POLICY alias="ena-POLICY-BABRAHAM-23-03-2017-09:47:38:853-62" center_name="BABRAHAM" accession="EGAP00001000615" broker_name="EGA">  
    <IDENTIFIERS> 
      <PRIMARY_ID>EGAP00001000615</PRIMARY_ID>
      <SUBMITTER_ID namespace="BABRAHAM">ena-POLICY-BABRAHAM-23-03-2017-09:47:38:853-62</SUBMITTER_ID>
    </IDENTIFIERS>
    <TITLE>Data Access Agreement for PCHiC, RNA-Seq, ChIP-Seq</TITLE>
    <DAC_REF accession="EGAC00001000523">
      <IDENTIFIERS>
        <PRIMARY_ID>EGAC00001000523</PRIMARY_ID>
      </IDENTIFIERS>
    </DAC_REF>
    <POLICY_FILE>ftp://ftp.ebi.ac.uk/pub/contrib/pchic/EGA_Data_Access_Request_DIL.docx</POLICY_FILE>
    <DATA_USES>
      <DATA_USE ontology="DUO" code="0000007" version="17-07-2016">
      	<!-- disease specific research -->
        <MODIFIER>
           <DB>EFO</DB>
           <ID>0001645</ID>
        </MODIFIER> 
        <MODIFIER>
           <DB>EFO</DB>
           <ID>0001655</ID>
        </MODIFIER>
       </DATA_USE>
       <DATA_USE ontology="DUO" code="0000014" version="17-07-2016"/>
       </DATA_USES>
   </POLICY>
</POLICY_SET>
```




https://github.com (URL_TO_INSERT_RECORD_10672 https://fairsharing.org/FAIRsharing.c55d5e) /enasequence/schema/blob/USI/src/test/resources/uk/ac/ebi/ena/sra/xml/ega_dataset/ega_dataset.xml


```XML
<DATASETS>
    <DATASET alias="EGAS000000001-sc-20110919" center_name="SC" broker_name="EGA" accession="EGAD00001000039">
        <IDENTIFIERS>
            <PRIMARY_ID>EGAD00001000039</PRIMARY_ID>
            <SUBMITTER_ID namespace="SC">EGAS000000001-sc-20110919</SUBMITTER_ID>
        </IDENTIFIERS>
        <TITLE>Platelet collagen defect</TITLE>
        <RUN_REF accession="EGAR0000000001" refname="RUN_1" refcenter="EBI">
            <IDENTIFIERS>
                <PRIMARY_ID>EGAR0000000001</PRIMARY_ID>
                <SUBMITTER_ID namespace="EBI">RUN_1</SUBMITTER_ID>
            </IDENTIFIERS>
        </RUN_REF>
        <POLICY_REF accession="EGAP00000001" refname="Policy_-2011-08-17T15:05:39Z-1888" refcenter="EBI">
            <IDENTIFIERS>
                <PRIMARY_ID>EGAP00001000024</PRIMARY_ID>
                <SUBMITTER_ID namespace="EBI">Policy_-2011-08-17T15:05:39Z-1888</SUBMITTER_ID>
            </IDENTIFIERS>
        </POLICY_REF>
    </DATASET>
</DATASETS>
```




Browsing Data Access Committees available from EGA (URL_TO_INSERT_RECORD_10673 https://fairsharing.org/FAIRsharing.mya1ff) :

````{dropdown}
:open:
```{figure} dac-ega.png
---
width: 700px
name: 
alt: List of Data Access Policy (URL_TO_INSERT_TERM_10674 https://fairsharing.org/search?fairsharingRegistry=Policy)  from EGA (URL_TO_INSERT_RECORD_10675 https://fairsharing.org/FAIRsharing.mya1ff) 
---
List of Data Access Policy (URL_TO_INSERT_TERM_10676 https://fairsharing.org/search?fairsharingRegistry=Policy)  from EGA (URL_TO_INSERT_RECORD_10677 https://fairsharing.org/FAIRsharing.mya1ff) 
```
````


### ODRL, Open Digital Rights Language

ODR (URL_TO_INSERT_RECORD_10679 https://fairsharing.org/FAIRsharing.1sfhp3) L stands for Open Digital Rights Language and is a set of W3C Recommendations defining a **policy (URL_TO_INSERT_TERM_10678 https://fairsharing.org/search?fairsharingRegistry=Policy)  expression language**. 

ODR (URL_TO_INSERT_RECORD_10680 https://fairsharing.org/FAIRsharing.1sfhp3) L is made up of several components:

- [The ODR (URL_TO_INSERT_RECORD_10682 https://fairsharing.org/FAIRsharing.1sfhp3) L Model](https://www.w3.org/TR/odrl-model/) {footcite}`ODR (URL_TO_INSERT_RECORD_10683 https://fairsharing.org/FAIRsharing.1sfhp3) Lmodel (URL_TO_INSERT_TERM_10681 https://fairsharing.org/search?recordType=model_and_format) `

````{dropdown}
:open:
```{figure} https://www.w3.org/TR/odrl-model/00Model.png
---
width: 700px
name: 
alt: Open Digital Rights Language model (URL_TO_INSERT_TERM_10684 https://fairsharing.org/search?recordType=model_and_format) 
---
ODR (URL_TO_INSERT_RECORD_10685 https://fairsharing.org/FAIRsharing.1sfhp3) L overview
```
````


- [The ODR (URL_TO_INSERT_RECORD_10686 https://fairsharing.org/FAIRsharing.1sfhp3) L Vocabulary](https://www.w3.org/TR/odrl-vocab/) {footcite}`ODR (URL_TO_INSERT_RECORD_10687 https://fairsharing.org/FAIRsharing.1sfhp3) Lvocab`

The **ODR (URL_TO_INSERT_RECORD_10690 https://fairsharing.org/FAIRsharing.1sfhp3) L Vocabulary and Expression** provides the terms to express policies (URL_TO_INSERT_TERM_10688 https://fairsharing.org/search?fairsharingRegistry=Policy)  in RDF (URL_TO_INSERT_RECORD_10689 https://fairsharing.org/FAIRsharing.p77ph9)  language.

The ODR (URL_TO_INSERT_RECORD_10696 https://fairsharing.org/FAIRsharing.1sfhp3) L Vocabulary and Expression complements the ODR (URL_TO_INSERT_RECORD_10697 https://fairsharing.org/FAIRsharing.1sfhp3) L informat (URL_TO_INSERT_TERM_10692 https://fairsharing.org/search?recordType=model_and_format) ion model (URL_TO_INSERT_TERM_10691 https://fairsharing.org/search?recordType=model_and_format) , which allows expressing similar informat (URL_TO_INSERT_TERM_10693 https://fairsharing.org/search?recordType=model_and_format) ion in JSO (URL_TO_INSERT_RECORD_10695 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_10694 https://fairsharing.org/FAIRsharing.5bbab9)  language.



```{warning}
In 2015, the dedicated working group produced the following JSON schema implementation guidance
https://www.w3.org/community/odrl/json/2.1/#section-Schema

We base our representations on this specification {footcite}`ODRLJSON`. 

We are aware of a possible misalignment between the specifications of the Working Group (from 2015) and the latest
specifications as to whether to use the keys "name" or "leftOperand" (https://www.w3.org/TR/odrl-model/#constraint-rule, 2018).
In the following representations, we use the key "name" to validate against the 2015 JSON-schema
 https://www.w3.org/community/odrl/json/2.1/#section-Schema / https://github.com/iptc/rightsml-dev/blob/master/licensed/ODRL21.json

```

#### The different types of Policies

The ODR (URL_TO_INSERT_RECORD_10700 https://fairsharing.org/FAIRsharing.1sfhp3) L model (URL_TO_INSERT_TERM_10699 https://fairsharing.org/search?recordType=model_and_format)  defines several subclasses for the **Policy (URL_TO_INSERT_TERM_10698 https://fairsharing.org/search?fairsharingRegistry=Policy) ** entity, namely  **Agreement**, **Set**, **Offer**.

##### Describing an agreement with ODRL

```json
{
    "policytype": "http://www.w3.org/ns/odrl/2/Agreement",
    "policyid": "http://example.com/policy:5531",
    "inheritallowed": true,
    "permissions": [{
        "target": "http://example.com/report:2321",
        "action": "http://www.w3.org/ns/odrl/2/print",
        "assigner": "http://example.com/pub:88",
        "assignee": "http://example.com/billie:888"
    }]
}
{
    "policytype": "http://www.w3.org/ns/odrl/2/Agreement",
    "policyid": "http://example.com/policy:9999",
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

In this section, we document how to rely on a basic ODR (URL_TO_INSERT_RECORD_10705 https://fairsharing.org/FAIRsharing.1sfhp3) L-based pattern using a DUO (URL_TO_INSERT_RECORD_10701 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_10703 https://fairsharing.org/FAIRsharing.mjnypw)  term {footcite}`DUO (URL_TO_INSERT_RECORD_10702 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_10704 https://fairsharing.org/FAIRsharing.mjnypw) ` to represent a
situation where SecondaryUse of the data is allowed on the condition that work is restricted to **disease specific research (URL_TO_INSERT_RECORD_10706 https://fairsharing.org/FAIRsharing.52b22c) **.


```json
{
    "policytype": "http://www.w3.org/ns/odrl/2/Policy",
    "policyid": "https://fairplus.github.io/examples/policy_122334",
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
The main limitation of the representation is that it provides no information about which diseases are vetted for research.
```

The following representation is more sophisticated and includes 3 types of restrictions:

- restriction on specific disease (juvenile arthritis, to reuse the exemplar representation in EGA (URL_TO_INSERT_RECORD_10708 https://fairsharing.org/FAIRsharing.mya1ff) /SRA (URL_TO_INSERT_RECORD_10709 https://fairsharing.org/FAIRsharing.g7t2hv)  XML (URL_TO_INSERT_RECORD_10707 https://fairsharing.org/FAIRsharing.b5cc91)  presented in section 1)
- restriction on the geographical location where the research (URL_TO_INSERT_RECORD_10710 https://fairsharing.org/FAIRsharing.52b22c)  can be conducted
- an obligation to delete the data obtained through the access agreement past a specified duration, 3 years in our example

Let's proceed stepwise.


* Representing Research (URL_TO_INSERT_RECORD_10715 https://fairsharing.org/FAIRsharing.52b22c)  Restriction on Specific Disease Area using DUO (URL_TO_INSERT_RECORD_10712 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_10713 https://fairsharing.org/FAIRsharing.mjnypw)  and MO (URL_TO_INSERT_RECORD_10716 https://fairsharing.org/FAIRsharing.qs4x5m) NDO (URL_TO_INSERT_RECORD_10714 https://fairsharing.org/FAIRsharing.b2979t)  ontologies (URL_TO_INSERT_TERM_10711 https://fairsharing.org/search?recordType=terminology_artefact) 


```json
{
    "policytype": "http://www.w3.org/ns/odrl/2/Policy",
    "policyid": "https://fairplus.github.io/examples/policy_122334",
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
While DUO is unique in its coverage of data uses, various disease ontologies exist and may be used to specify the
specific focus research should have.
For instance, SNOMED-CT, Disease Ontology could also be used.
It is worth noting that extensive cross referencing exists between resources such as DOID, MONDO and
SNOMED-CT but this is something to consider when implementing brokering systems.
```



* Representing Research (URL_TO_INSERT_RECORD_10717 https://fairsharing.org/FAIRsharing.52b22c)  Restriction based on Geographical Regions

The section shows how to use ODR (URL_TO_INSERT_RECORD_10718 https://fairsharing.org/FAIRsharing.1sfhp3) L to document geographical restrictions, either by listing (URL_TO_INSERT_RECORD_10719 https://fairsharing.org/FAIRsharing.q7bkqr)  countries where research (URL_TO_INSERT_RECORD_10720 https://fairsharing.org/FAIRsharing.52b22c)  is 
allowed or by listing (URL_TO_INSERT_RECORD_10721 https://fairsharing.org/FAIRsharing.q7bkqr)  those countries excluded from doing so.

In the following example, research (URL_TO_INSERT_RECORD_10722 https://fairsharing.org/FAIRsharing.52b22c)  is only allowed in a specific country, **Italy** in this case, which is 
encoded using the **ISO (URL_TO_INSERT_RECORD_10723 https://fairsharing.org/FAIRsharing.6bc7h9) -3166 code**.


```json
{
    "policytype": "http://www.w3.org/ns/odrl/2/Policy",
    "policyid": "https://fairplus.github.io/examples/policy_122334",
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

The following example shows how to explicitly state in a Policy (URL_TO_INSERT_TERM_10724 https://fairsharing.org/search?fairsharingRegistry=Policy)  element that the data must be deleted after a defined
period of time (3 years in this example).
Duration and time related value should be represented using **ISO (URL_TO_INSERT_RECORD_10726 https://fairsharing.org/FAIRsharing.6bc7h9) -8601 standard (URL_TO_INSERT_TERM_10725 https://fairsharing.org/search?fairsharingRegistry=Standard) **.

```json
{
    "policytype": "http://www.w3.org/ns/odrl/2/Policy",
    "policyid": "https://fairplus.github.io/examples/policy_122334",
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

This ODRL representation is **not vetted, nor endorsed by GA4GH or EGA**.
This example is currently meant to present an example of how to use ODRL to represent some of the information represented in EGA.

```

```json
{
    "policytype": "http://www.w3.org/ns/odrl/2/Policy",
    "policyid": "https://ega-archive.org/datasets/EGAP0000000XYZ",
    "permissions": [
        {
            "target": "https://ega-archive.org/datasets/EGAD0000000YYY",
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
            "assigner": "https://ega-archive.org/",
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
                "target": "https://ega-archive.org/datasets/EGAD0000000YYY",
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

The ODR (URL_TO_INSERT_RECORD_10729 https://fairsharing.org/FAIRsharing.1sfhp3) L model (URL_TO_INSERT_TERM_10727 https://fairsharing.org/search?recordType=model_and_format)  {footcite}`ODR (URL_TO_INSERT_RECORD_10730 https://fairsharing.org/FAIRsharing.1sfhp3) Lmodel (URL_TO_INSERT_TERM_10728 https://fairsharing.org/search?recordType=model_and_format) ` provides the **prohibitions** relation, which uses similar patterns to those seen while covering **permissions**.
The ODR (URL_TO_INSERT_RECORD_10731 https://fairsharing.org/FAIRsharing.1sfhp3) L vocabulary is then used to identify the **actions** which are restricted under the **prohibition** header. 
Complex prohibitions can be expressed using **constraints** and **refinement** elements.


```json
{
    "policytype": "http://www.w3.org/ns/odrl/2/Policy",
    "policyid": "http://example.com/policy:0099",
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

<#daa-policy-1>
 a odrl:Policy .

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
  odrl:hasPolicy <#daa-policy-1>;
  .

```

For more details, please see the following publication by [de Vos et al, 2019](https://www.specialprivacy.eu/images/documents/RuleMLRR_2019_.pdf)

### DATS and ODRL JSON

An evolution of the DATS (URL_TO_INSERT_RECORD_10732 https://fairsharing.org/FAIRsharing.e20vsd)  {footcite}`pmid28585923`, {footcite}`pmid32031623` schema is used by University of Luxembourg 
to build a data catalogue for IMI project (URL_TO_INSERT_TERM_10733 https://fairsharing.org/search?recordType=project) s and datasets.
The proposed patterns could be used and tested to representation DAC (URL_TO_INSERT_RECORD_10735 https://fairsharing.org/FAIRsharing.md3e78) /DAA informat (URL_TO_INSERT_TERM_10734 https://fairsharing.org/search?recordType=model_and_format) ion as well as the allowed uses of 
datasets generated by the consortia funded by IMI.
More complex use cases can be considered to assess to ability of the representations to be associated to specific 
datasets, for instance datasets associated with a particular data acquisition technique the access of which may require 
specific policies (URL_TO_INSERT_TERM_10736 https://fairsharing.org/search?fairsharingRegistry=Policy)  and conditions to be made machine-readable.

The approach is therefore to reference the  JSO (URL_TO_INSERT_RECORD_10739 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_10737 https://fairsharing.org/FAIRsharing.5bbab9)  representations compliant with the ODR (URL_TO_INSERT_RECORD_10741 https://fairsharing.org/FAIRsharing.1sfhp3) L JSO (URL_TO_INSERT_RECORD_10740 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_10738 https://fairsharing.org/FAIRsharing.5bbab9)  schema 2.1 specification,
as presented in earlier sections in conjunction with DATS (URL_TO_INSERT_RECORD_10742 https://fairsharing.org/FAIRsharing.e20vsd)  JSO (URL_TO_INSERT_RECORD_10744 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_10743 https://fairsharing.org/FAIRsharing.5bbab9)  documents.



### Validating ODRL RDF documents

Code exists that allows developers to validate ODR (URL_TO_INSERT_RECORD_10746 https://fairsharing.org/FAIRsharing.1sfhp3) L documents **expressed in legitimate RDF (URL_TO_INSERT_RECORD_10745 https://fairsharing.org/FAIRsharing.p77ph9)  serializations**.

http://odrlapi.appspot.com/


````{dropdown}
:open:
```{figure} ./odrl-validation-app.png
---
width: 800px
alt: ODR (URL_TO_INSERT_RECORD_10747 https://fairsharing.org/FAIRsharing.1sfhp3) L Validation and Evaluation Sandbox
name: ODR (URL_TO_INSERT_RECORD_10748 https://fairsharing.org/FAIRsharing.1sfhp3) L Validation and Evaluation Sandbox
---
ODR (URL_TO_INSERT_RECORD_10749 https://fairsharing.org/FAIRsharing.1sfhp3) L Validation and Evaluation Sandbox
```
````


The web-application is powered by a REST-API the swagger document of which is available from the following address:
http://odrlapi.appspot.com/apidoc/index.html

<!-- ## TO (URL_TO_INSERT_RECORD_10750 https://fairsharing.org/FAIRsharing.w69t6r) DO discuss relation to RightML

https://iptc.org/std/RightsML/2.0/RightsML_2.0-specification.html -->

## Consuming Data Use related annotations

It is all good and well to describe patterns in various format (URL_TO_INSERT_TERM_10751 https://fairsharing.org/search?recordType=model_and_format) s but are there any tools or services capable exploiting these annotations?
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

DUO (URL_TO_INSERT_RECORD_10752 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_10753 https://fairsharing.org/FAIRsharing.mjnypw) S requires official clearance from a **Data Access Committee** representative or an **Authorized Submission Representative** 
to enable registration of a dataset into the DUO (URL_TO_INSERT_RECORD_10754 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_10755 https://fairsharing.org/FAIRsharing.mjnypw) S.
Once this authorization is available, the dataset has to be annotated following the patterns defined by GA4GH (URL_TO_INSERT_RECORD_10756 https://fairsharing.org/FAIRsharing.2tpx4v)  with
Data Use Ontology (URL_TO_INSERT_TERM_10758 https://fairsharing.org/search?recordType=terminology_artefact)  {footcite}`pmid26796797` and 'SRA (URL_TO_INSERT_RECORD_10760 https://fairsharing.org/FAIRsharing.g7t2hv)  XML (URL_TO_INSERT_RECORD_10759 https://fairsharing.org/FAIRsharing.b5cc91) ' format (URL_TO_INSERT_TERM_10757 https://fairsharing.org/search?recordType=model_and_format) .

The European Genome Arch (URL_TO_INSERT_RECORD_10762 https://fairsharing.org/FAIRsharing.52b22c) ive allows programmatic filtering based on this informat (URL_TO_INSERT_TERM_10761 https://fairsharing.org/search?recordType=model_and_format) ion via the REST-API of the service.

## Conclusion

Making sure that machine-readable informat (URL_TO_INSERT_TERM_10763 https://fairsharing.org/search?recordType=model_and_format) ion about the conditions of use of datasets and data is available is key to 
enable privacy preserving and policy (URL_TO_INSERT_TERM_10764 https://fairsharing.org/search?fairsharingRegistry=Policy)  compliant use of informat (URL_TO_INSERT_TERM_10765 https://fairsharing.org/search?recordType=model_and_format) ion across organizations.
This content provides an overview of the model (URL_TO_INSERT_TERM_10766 https://fairsharing.org/search?recordType=model_and_format) s available to do so and how it has been applied to life science data, 
showing the main features of the model (URL_TO_INSERT_TERM_10767 https://fairsharing.org/search?recordType=model_and_format) s and how to define use based on the major properties such as the type of research (URL_TO_INSERT_RECORD_10768 https://fairsharing.org/FAIRsharing.52b22c) 
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

