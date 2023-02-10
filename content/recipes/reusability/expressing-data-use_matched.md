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

The aim is also to document equivalent representations and how bridges (URL_TO_INSERT_RECORD-NAME_5629 https://fairsharing.org/FAIRsharing.ac95d5)  can be built between the distinct but equivalent implementations.

Finally, the content aims to highlight key use-cases which require coverage, how to code such informat (URL_TO_INSERT_TERM_5630 https://fairsharing.org/search?recordType=model_and_format) ion, documenting 
implementation patterns in the context of **data cataloguing efforts**, for instance by expressing **Data Access Policies (URL_TO_INSERT_TERM_5631 https://fairsharing.org/search?fairsharingRegistry=Policy) **.


## Graphical Overview


````{dropdown}
:open:
```{figure} data-usage-mermaid.png
---
width: 850px
name: expressing-data-use-figure1
alt: Dealing with Policies (URL_TO_INSERT_TERM_5632 https://fairsharing.org/search?fairsharingRegistry=Policy)  and Data Use
---
Data Use
```
````



---

## Tools

### Standards

 Data Format (URL_TO_INSERT_TERM_5634 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_5635 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_5633 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
| JSON-LD<!-- TODO add a link to corresponding document --> | <!-- TODO add a link to corresponding document -->  |   |
| [ISO-8601](https://www.iso.org/iso-8601-date-and-time-format.html)  | [DCAT (URL_TO_INSERT_RECORD-ABBREV_5636 https://fairsharing.org/FAIRsharing.h4j3qm)  v2](https://www.w3.org/TR/vocab-dcat-2/)  |   |
| [ISO-3066](https://www.iso.org/iso-3166-country-codes.html)  | [ODRL](https://www.w3.org/TR/odrl-vocab/)  |   |
| EGA XML<!-- TODO add a link to corresponding document -->   | [DUO](http://www.obofoundry.org/ontology/duo.html)  |   |
| [Data Article Tag Suite (DATS)](https://datatagsuite.github.io/schema/)  | [MONDO](http://www.obofoundry.org/ontology/mondo.html)  |   |




### Implementation

DUOS:
https://duos.broadinstitute.org/

---

## Introduction

The preservation of patient privacy and the compliance with patient consent are essential considerations when managing
sensitive informat (URL_TO_INSERT_TERM_5637 https://fairsharing.org/search?recordType=model_and_format) ion such as clinical and patient data.
Consent forms, as signed by patients, define the acceptable usage of data derived from a patient for research applications.
All major research organizations, at national and international levels, enforce strict rules for the management of such data.
Sensitive data cannot be accessed without undergoing a vetting process involving a **data access request** to a **data access committee**,
which will decide, whether or not, to grant requesters access to the data.

This is a time-consuming process in the absence of machine-readable version of data access/ data management policies (URL_TO_INSERT_TERM_5638 https://fairsharing.org/search?fairsharingRegistry=Policy) .
In turns, it can prove detrimental to research.
Therefore, efforts to enable the provision of concise, efficient and **machine processable** summary of key permissions and prohibitions have been made. 
Several resources are now available for the coding and exchange of **machine-actionable**, **legally binding** and
**explicit** informat (URL_TO_INSERT_TERM_5639 https://fairsharing.org/search?recordType=model_and_format) ion related to allowed and consented data usage.

The following sections detail how the international sequence data archives (US NCBI dbGAP, SRA (URL_TO_INSERT_RECORD-ABBREV_5641 https://fairsharing.org/FAIRsharing.g7t2hv)  and EU EMBL_EBI EGA (URL_TO_INSERT_RECORD-ABBREV_5640 https://fairsharing.org/FAIRsharing.mya1ff) )
are encoding **Data Use Informat (URL_TO_INSERT_TERM_5642 https://fairsharing.org/search?recordType=model_and_format) ion**  but also how ODRL, a W3C specification, 
can be used to represent equivalent informat (URL_TO_INSERT_TERM_5643 https://fairsharing.org/search?recordType=model_and_format) ion in a format (URL_TO_INSERT_TERM_5644 https://fairsharing.org/search?recordType=model_and_format)  compatible with the data cataloguing efforts relying on W3C DCAT (URL_TO_INSERT_RECORD-ABBREV_5645 https://fairsharing.org/FAIRsharing.h4j3qm)  specifications.




### SRA & EGA XML schema for Policy, Dataset and Controller

Next Generation Sequencing (NGS) techniques allow routine production of full genome data from patients.
This data is highly sensitive and data repositories (URL_TO_INSERT_TERM_5646 https://fairsharing.org/search?recordType=repository)  specialized in storing such informat (URL_TO_INSERT_TERM_5647 https://fairsharing.org/search?recordType=model_and_format) ion have developed procedures 
and representation model (URL_TO_INSERT_TERM_5648 https://fairsharing.org/search?recordType=model_and_format) s for defining the conditions of use.

We summarize here the key objects used by the European Genome Archive, in compliance with INSDC and GA4GH guideline (URL_TO_INSERT_TERM_5649 https://fairsharing.org/search?recordType=reporting_guideline) s.

https://ega-archive.org (URL_TO_INSERT_RECORD-HOMEPAGE_5650 https://fairsharing.org/FAIRsharing.mya1ff) /data-use-conditions

````{dropdown}
:open:
```{figure} duo-ols-view-1.png
---
width: 700px
name: expressing-data-use-figure2
alt: Data Use Ontology (URL_TO_INSERT_TERM_5651 https://fairsharing.org/search?recordType=terminology_artefact)  Overview Part 1
---
Data Use Ontology (URL_TO_INSERT_TERM_5652 https://fairsharing.org/search?recordType=terminology_artefact)  Overview Part 1
```
````

````{dropdown}
:open:
```{figure} duo-ols-view-2.png
---
width: 700px
name: expressing-data-use-figure3
alt: Data Use Ontology (URL_TO_INSERT_TERM_5653 https://fairsharing.org/search?recordType=terminology_artefact)  Overview Part 2
---
Data Use Ontology (URL_TO_INSERT_TERM_5654 https://fairsharing.org/search?recordType=terminology_artefact)  Overview Part 2
```
````

<!-- 
````{panels}
:column: col-8
:card: border-2
DUO (URL_TO_INSERT_RECORD-ABBREV_5655 https://fairsharing.org/FAIRsharing.5dnjs2)  in OLS (URL_TO_INSERT_RECORD-ABBREV_5656 https://fairsharing.org/FAIRsharing.Mkl9RR) 
^^^
```{figure} duo-ols-view-1.png
width: 400px
```
---
DUO (URL_TO_INSERT_RECORD-ABBREV_5657 https://fairsharing.org/FAIRsharing.5dnjs2)  in OLS (URL_TO_INSERT_RECORD-ABBREV_5658 https://fairsharing.org/FAIRsharing.Mkl9RR) 
^^^
```{figure} duo-ols-view-2.png
width: 400px
```

```` -->


The information presented below has been sourced from the ENA GitHub repo.



1. The **Data Access Committee** and Contact information

```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<DAC_SET>
    <DAC alias="DAC-2011-08-11T11:45:28Z-1873" accession="EGAC00000000001" center_name="EBI" broker_name="E (URL_TO_INSERT_RECORD-ABBREV_5659 https://fairsharing.org/FAIRsharing.mya1ff) GA">
        <IDENTIFIER (URL_TO_INSERT_TERM_5660 https://fairsharing.org/search?recordType=identifier_schema) S>
            <PRIMARY_ID>EGAC00000000001</PRIMARY_ID>
            <SUBMITTER_ID namespace="EBI">DAC-2011-08-11T11:45:28Z-1873</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_5661 https://fairsharing.org/search?recordType=identifier_schema) S>
        <TITLE>EG (URL_TO_INSERT_RECORD-ABBREV_5662 https://fairsharing.org/FAIRsharing.mya1ff) A DAC TITLE</TITLE>
        <CONTACTS>
            <CONTACT name="Joe Bloggs" email="joe@noname.com" organisation="EBI"/>
        </CONTACTS>
    </DAC>
</DAC_SET>
```


https://github.com/enasequence/schema/blob/USI/src/test/resources/uk/ac/ebi/ena/sra/xml/ega_dac/ega_dac.xml

2. The **Data Access Policy** object


https://github.com/enasequence/schema/blob/USI/src/test/resources/uk/ac/ebi/ena/sra/xml/ega_policy/ega_policy.xml

```{note}
in the following example, the text of the policy (URL_TO_INSERT_TERM_5663 https://fairsharing.org/search?fairsharingRegistry=Policy)  is present in the XML (URL_TO_INSERT_RECORD-ABBREV_5664 https://fairsharing.org/FAIRsharing.b5cc91)  representation
```


```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<POLICY (URL_TO_INSERT_TERM_5665 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
    <POLICY (URL_TO_INSERT_TERM_5666 https://fairsharing.org/search?fairsharingRegistry=Policy)  center_name="EBI" alias="Policy (URL_TO_INSERT_TERM_5667 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868" accession="EGAP00001000001" broker_name="EBI">
        <IDENTIFIER (URL_TO_INSERT_TERM_5668 https://fairsharing.org/search?recordType=identifier_schema) S>
            <PRIMARY_ID>EGAP00001000001</PRIMARY_ID>
            <SUBMITTER_ID namespace="SC">Policy (URL_TO_INSERT_TERM_5669 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_5670 https://fairsharing.org/search?recordType=identifier_schema) S>
        <TITLE/>
        <DAC_REF accession="EGAP00001000001" refname="DAC_-2011-08-26T12:23:49Z-1868" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_5671 https://fairsharing.org/search?recordType=identifier_schema) S>
                <PRIMARY_ID>EGAC00001000001</PRIMARY_ID>
                <SUBMITTER_ID namespace="EBI">DAC_-2011-08-26T12:23:49Z-1868</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_5672 https://fairsharing.org/search?recordType=identifier_schema) S>
        </DAC_REF>
        <POLICY (URL_TO_INSERT_TERM_5673 https://fairsharing.org/search?fairsharingRegistry=Policy) _TEXT>https://www.sanger.ac.uk/datasharing/</POLICY_TEXT>
    </POLICY (URL_TO_INSERT_TERM_5674 https://fairsharing.org/search?fairsharingRegistry=Policy) >
</POLICY (URL_TO_INSERT_TERM_5675 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
```


```{note}
In the following example, the file address (url) to the policy (URL_TO_INSERT_TERM_5676 https://fairsharing.org/search?fairsharingRegistry=Policy)  is included in the XML (URL_TO_INSERT_RECORD-ABBREV_5677 https://fairsharing.org/FAIRsharing.b5cc91)  representation.
Ideally, the url provided should be a globally unique persistent identifier (URL_TO_INSERT_TERM_5678 https://fairsharing.org/search?recordType=identifier_schema)  so one can be sure to obtain at least the metadata about the document.
```

```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<POLICY (URL_TO_INSERT_TERM_5679 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
    <POLICY (URL_TO_INSERT_TERM_5680 https://fairsharing.org/search?fairsharingRegistry=Policy)  center_name="EBI" alias="Policy (URL_TO_INSERT_TERM_5681 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868" accession="EGAP00001000001" broker_name="EBI">
        <IDENTIFIER (URL_TO_INSERT_TERM_5682 https://fairsharing.org/search?recordType=identifier_schema) S>
            <PRIMARY_ID>EGAP00001000001</PRIMARY_ID>
            <SUBMITTER_ID namespace="SC">Policy (URL_TO_INSERT_TERM_5683 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_5684 https://fairsharing.org/search?recordType=identifier_schema) S>
        <TITLE/>
        <DAC_REF accession="EGAP00001000001" refname="DAC_-2011-08-26T12:23:49Z-1868" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_5685 https://fairsharing.org/search?recordType=identifier_schema) S>
                <PRIMARY_ID>EGAC00001000001</PRIMARY_ID>
                <SUBMITTER_ID namespace="EBI">DAC_-2011-08-26T12:23:49Z-1868</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_5686 https://fairsharing.org/search?recordType=identifier_schema) S>
        </DAC_REF>
        <POLICY (URL_TO_INSERT_TERM_5687 https://fairsharing.org/search?fairsharingRegistry=Policy) _FILE>https://www.sanger.ac.uk/datasharing/</POLICY_FILE>
    </POLICY (URL_TO_INSERT_TERM_5688 https://fairsharing.org/search?fairsharingRegistry=Policy) >
</POLICY (URL_TO_INSERT_TERM_5689 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
```


3. Expressing Data Use with EGA XML and **Data Use Ontology** codes.

```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<POLICY (URL_TO_INSERT_TERM_5690 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
    <POLICY (URL_TO_INSERT_TERM_5691 https://fairsharing.org/search?fairsharingRegistry=Policy)  center_name="EBI" alias="Policy (URL_TO_INSERT_TERM_5692 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868" accession="EGAP00001000001" broker_name="EBI">
        <IDENTIFIER (URL_TO_INSERT_TERM_5693 https://fairsharing.org/search?recordType=identifier_schema) S>
            <PRIMARY_ID>EGAP00001000001</PRIMARY_ID>
            <SUBMITTER_ID namespace="SC">Policy (URL_TO_INSERT_TERM_5694 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_5695 https://fairsharing.org/search?recordType=identifier_schema) S>
        <TITLE/>
        <DAC_REF accession="EGAP00001000001" refname="DAC_-2011-08-26T12:23:49Z-1868" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_5696 https://fairsharing.org/search?recordType=identifier_schema) S>
                <PRIMARY_ID>EGAC00001000001</PRIMARY_ID>
                <SUBMITTER_ID namespace="EBI">DAC_-2011-08-26T12:23:49Z-1868</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_5697 https://fairsharing.org/search?recordType=identifier_schema) S>
        </DAC_REF>
        <POLICY (URL_TO_INSERT_TERM_5698 https://fairsharing.org/search?fairsharingRegistry=Policy) _FILE>https://www.sanger.ac.uk/datasharing/</POLICY_FILE>
        <DATA_USES>
                   	<!-- no restriction -->
   			<DATA_USE>http://purl.obolibrary.org/obo/DUO_0000004</DATA_USE>

			<DATA_USES>
			   <DATA_USE ontology (URL_TO_INSERT_TERM_5699 https://fairsharing.org/search?recordType=terminology_artefact) ="D (URL_TO_INSERT_RECORD-ABBREV_5700 https://fairsharing.org/FAIRsharing.5dnjs2) UO" code="0000004" version="17-07-2016"/>
			</DATA_USES>

        </DATA_USES>
    </POLICY (URL_TO_INSERT_TERM_5701 https://fairsharing.org/search?fairsharingRegistry=Policy) >
</POLICY (URL_TO_INSERT_TERM_5702 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
```



https://ega-archive.org/dacs

Indicating disease specific restriction on research with DUO and ontologies covering the Disease and Pathology domain.


```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<POLICY (URL_TO_INSERT_TERM_5703 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
    <POLICY (URL_TO_INSERT_TERM_5704 https://fairsharing.org/search?fairsharingRegistry=Policy)  center_name="EBI" alias="Policy (URL_TO_INSERT_TERM_5705 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868" accession="EGAP00001000001" broker_name="EBI">
        <IDENTIFIER (URL_TO_INSERT_TERM_5706 https://fairsharing.org/search?recordType=identifier_schema) S>
            <PRIMARY_ID>EGAP00001000001</PRIMARY_ID>
            <SUBMITTER_ID namespace="SC">Policy (URL_TO_INSERT_TERM_5707 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_5708 https://fairsharing.org/search?recordType=identifier_schema) S>
        <TITLE/>
        <DAC_REF accession="EGAP00001000001" refname="DAC_-2011-08-26T12:23:49Z-1868" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_5709 https://fairsharing.org/search?recordType=identifier_schema) S>
                <PRIMARY_ID>EGAC00001000001</PRIMARY_ID>
                <SUBMITTER_ID namespace="EBI">DAC_-2011-08-26T12:23:49Z-1868</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_5710 https://fairsharing.org/search?recordType=identifier_schema) S>
        </DAC_REF>
        <POLICY (URL_TO_INSERT_TERM_5711 https://fairsharing.org/search?fairsharingRegistry=Policy) _FILE>https://www.sanger.ac.uk/datasharing/</POLICY_FILE>
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
    </POLICY (URL_TO_INSERT_TERM_5712 https://fairsharing.org/search?fairsharingRegistry=Policy) >
</POLICY (URL_TO_INSERT_TERM_5713 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
```


```{note}
When using the consent code DUO_0000007 where data is restricted for use on a specific disease area, it is necessary to explicitly indicate which disease area is allowed. This can be done by associating codes/identifier (URL_TO_INSERT_TERM_5715 https://fairsharing.org/search?recordType=identifier_schema) s from well established disease terminologies (URL_TO_INSERT_TERM_5714 https://fairsharing.org/search?recordType=terminology_artefact)  such as MONDO (URL_TO_INSERT_RECORD-ABBREV_5716 https://fairsharing.org/FAIRsharing.b2979t) , DOID (URL_TO_INSERT_RECORD-ABBREV_5717 https://fairsharing.org/FAIRsharing.8b6wfq) , SNOMED-CT.
For instance, if data reuse is restricted to research into `juvenile idiopathic arthritis`, the code should be displayed as DUO_0000007; MONDO (URL_TO_INSERT_RECORD-ABBREV_5718 https://fairsharing.org/FAIRsharing.b2979t) :0011429
```



```XML
<POLICY (URL_TO_INSERT_TERM_5719 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
  <POLICY (URL_TO_INSERT_TERM_5720 https://fairsharing.org/search?fairsharingRegistry=Policy)  alias="ena-POLICY (URL_TO_INSERT_TERM_5721 https://fairsharing.org/search?fairsharingRegistry=Policy) -BABRAHAM-23-03-2017-09:47:38:853-62" center_name="BABRAHAM" accession="EGAP00001000615" broker_name="E (URL_TO_INSERT_RECORD-ABBREV_5722 https://fairsharing.org/FAIRsharing.mya1ff) GA">  
    <IDENTIFIER (URL_TO_INSERT_TERM_5723 https://fairsharing.org/search?recordType=identifier_schema) S> 
      <PRIMARY_ID>EGAP00001000615</PRIMARY_ID>
      <SUBMITTER_ID namespace="BABRAHAM">ena-POLICY (URL_TO_INSERT_TERM_5724 https://fairsharing.org/search?fairsharingRegistry=Policy) -BABRAHAM-23-03-2017-09:47:38:853-62</SUBMITTER_ID>
    </IDENTIFIER (URL_TO_INSERT_TERM_5725 https://fairsharing.org/search?recordType=identifier_schema) S>
    <TITLE>Data Access Agreement for PCHiC, RNA-Seq, ChIP-Seq</TITLE>
    <DAC_REF accession="EGAC00001000523">
      <IDENTIFIER (URL_TO_INSERT_TERM_5726 https://fairsharing.org/search?recordType=identifier_schema) S>
        <PRIMARY_ID>EGAC00001000523</PRIMARY_ID>
      </IDENTIFIER (URL_TO_INSERT_TERM_5727 https://fairsharing.org/search?recordType=identifier_schema) S>
    </DAC_REF>
    <POLICY (URL_TO_INSERT_TERM_5728 https://fairsharing.org/search?fairsharingRegistry=Policy) _FILE>ftp://ftp.ebi.ac.uk/pub/contrib/pchic/EGA_Data_Access_Request_DIL.docx</POLICY_FILE>
    <DATA_USES>
      <DATA_USE ontology (URL_TO_INSERT_TERM_5729 https://fairsharing.org/search?recordType=terminology_artefact) ="D (URL_TO_INSERT_RECORD-ABBREV_5730 https://fairsharing.org/FAIRsharing.5dnjs2) UO" code="0000007" version="17-07-2016">
      	<!-- disease specific research -->
        <MODIFIER>
           <DB>EF (URL_TO_INSERT_RECORD-ABBREV_5731 https://fairsharing.org/FAIRsharing.1gr4tz) O</DB>
           <ID>0001645</ID>
        </MODIFIER> 
        <MODIFIER>
           <DB>EF (URL_TO_INSERT_RECORD-ABBREV_5732 https://fairsharing.org/FAIRsharing.1gr4tz) O</DB>
           <ID>0001655</ID>
        </MODIFIER>
       </DATA_USE>
       <DATA_USE ontology (URL_TO_INSERT_TERM_5733 https://fairsharing.org/search?recordType=terminology_artefact) ="D (URL_TO_INSERT_RECORD-ABBREV_5734 https://fairsharing.org/FAIRsharing.5dnjs2) UO" code="0000014" version="17-07-2016"/>
       </DATA_USES>
   </POLICY (URL_TO_INSERT_TERM_5735 https://fairsharing.org/search?fairsharingRegistry=Policy) >
</POLICY (URL_TO_INSERT_TERM_5736 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
```




https://github.com/enasequence/schema/blob/USI/src/test/resources/uk/ac/ebi/ena/sra/xml/ega_dataset/ega_dataset.xml


```XML
<DATASETS>
    <DATASET alias="EGAS000000001-sc-20110919" center_name="SC" broker_name="E (URL_TO_INSERT_RECORD-ABBREV_5737 https://fairsharing.org/FAIRsharing.mya1ff) GA" accession="EGAD00001000039">
        <IDENTIFIER (URL_TO_INSERT_TERM_5738 https://fairsharing.org/search?recordType=identifier_schema) S>
            <PRIMARY_ID>EGAD00001000039</PRIMARY_ID>
            <SUBMITTER_ID namespace="SC">EGAS000000001-sc-20110919</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_5739 https://fairsharing.org/search?recordType=identifier_schema) S>
        <TITLE>Platelet collagen defect</TITLE>
        <RUN_REF accession="EGAR0000000001" refname="RUN_1" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_5740 https://fairsharing.org/search?recordType=identifier_schema) S>
                <PRIMARY_ID>EGAR0000000001</PRIMARY_ID>
                <SUBMITTER_ID namespace="EBI">RUN_1</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_5741 https://fairsharing.org/search?recordType=identifier_schema) S>
        </RUN_REF>
        <POLICY (URL_TO_INSERT_TERM_5742 https://fairsharing.org/search?fairsharingRegistry=Policy) _REF accession="EGAP00000001" refname="Policy (URL_TO_INSERT_TERM_5743 https://fairsharing.org/search?fairsharingRegistry=Policy) _-2011-08-17T15:05:39Z-1888" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_5744 https://fairsharing.org/search?recordType=identifier_schema) S>
                <PRIMARY_ID>EGAP00001000024</PRIMARY_ID>
                <SUBMITTER_ID namespace="EBI">Policy (URL_TO_INSERT_TERM_5745 https://fairsharing.org/search?fairsharingRegistry=Policy) _-2011-08-17T15:05:39Z-1888</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_5746 https://fairsharing.org/search?recordType=identifier_schema) S>
        </POLICY (URL_TO_INSERT_TERM_5747 https://fairsharing.org/search?fairsharingRegistry=Policy) _REF>
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
In 2015, the dedicated working group produced the following JSON (URL_TO_INSERT_RECORD-ABBREV_5748 https://fairsharing.org/FAIRsharing.5bbab9)  schema implementation guidance
https://www.w3.org/community/odrl/json/2.1/#section-Schema

We base our representations on this specification {footcite}`ODRLJSON`. 

We are aware of a possible misalignment between the specifications of the Working Group (from 2015) and the latest
specifications as to whether to use the keys "name" or "leftOperand" (https://www.w3.org/TR/odrl-model/#constraint-rule, 2018).
In the following representations, we use the key "name" to validate against the 2015 JSON (URL_TO_INSERT_RECORD-ABBREV_5749 https://fairsharing.org/FAIRsharing.5bbab9) -schema
 https://www.w3.org/community/odrl/json/2.1/#section-Schema / https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_5750 https://fairsharing.org/FAIRsharing.c55d5e) /iptc/rightsml-dev/blob/master/licensed/ODRL21.json

```

#### The different types of Policies

The ODRL model defines several subclasses for the **Policy** entity, namely  **Agreement**, **Set**, **Offer**.

##### Describing an agreement with ODRL

```json
{
    "policy (URL_TO_INSERT_TERM_5751 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Agreement",
    "policy (URL_TO_INSERT_TERM_5752 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "http://example.com/policy:5531",
    "inheritallowed": true,
    "permissions": [{
        "target": "http://example.com/report:2321",
        "action": "http://www.w3.org/ns/odrl/2/print",
        "assigner": "http://example.com/pub:88",
        "assignee": "http://example.com/billie:888"
    }]
}
{
    "policy (URL_TO_INSERT_TERM_5753 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Agreement",
    "policy (URL_TO_INSERT_TERM_5754 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "http://example.com/policy:9999",
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
    "policy (URL_TO_INSERT_TERM_5755 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_5756 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "https://fairplus.github.io/examples/policy_122334",
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
The main limitation of the representation is that it provides no informat (URL_TO_INSERT_TERM_5757 https://fairsharing.org/search?recordType=model_and_format) ion about which diseases are vetted for research.
```

The following representation is more sophisticated and includes 3 types of restrictions:

- restriction on specific disease (juvenile arthritis, to reuse the exemplar representation in EGA/SRA XML presented in section 1)
- restriction on the geographical location where the research can be conducted
- an obligation to delete the data obtained through the access agreement past a specified duration, 3 years in our example

Let's proceed stepwise.


* Representing Research Restriction on Specific Disease Area using DUO and MONDO ontologies


```json
{
    "policy (URL_TO_INSERT_TERM_5758 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_5759 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "https://fairplus.github.io/examples/policy_122334",
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
While DUO (URL_TO_INSERT_RECORD-ABBREV_5761 https://fairsharing.org/FAIRsharing.5dnjs2)  is unique in its coverage of data uses, various disease ontologies (URL_TO_INSERT_TERM_5760 https://fairsharing.org/search?recordType=terminology_artefact)  exist and may be used to specify the
specific focus research should have.
For instance, SNOMED-CT, Disease Ontology (URL_TO_INSERT_TERM_5762 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD-NAME_5763 https://fairsharing.org/FAIRsharing.8b6wfq)  could also be used.
It is worth noting that extensive cross referencing exists between resources such as DOID (URL_TO_INSERT_RECORD-ABBREV_5765 https://fairsharing.org/FAIRsharing.8b6wfq) , MONDO (URL_TO_INSERT_RECORD-ABBREV_5764 https://fairsharing.org/FAIRsharing.b2979t)  and
SNOMED-CT but this is something to consider when implementing brokering systems.
```



* Representing Research Restriction based on Geographical Regions

The section shows how to use ODRL to document geographical restrictions, either by listing countries where research is 
allowed or by listing those countries excluded from doing so.

In the following example, research is only allowed in a specific country, **Italy** in this case, which is 
encoded using the **ISO-3166 code**.


```json
{
    "policy (URL_TO_INSERT_TERM_5766 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_5767 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "https://fairplus.github.io/examples/policy_122334",
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
    "policy (URL_TO_INSERT_TERM_5768 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_5769 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "https://fairplus.github.io/examples/policy_122334",
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

This ODRL representation is **not vetted, nor endorsed by GA4GH or EGA (URL_TO_INSERT_RECORD-ABBREV_5770 https://fairsharing.org/FAIRsharing.mya1ff) **.
This example is currently meant to present an example of how to use ODRL to represent some of the informat (URL_TO_INSERT_TERM_5771 https://fairsharing.org/search?recordType=model_and_format) ion represented in EGA (URL_TO_INSERT_RECORD-ABBREV_5772 https://fairsharing.org/FAIRsharing.mya1ff) .

```

```json
{
    "policy (URL_TO_INSERT_TERM_5773 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_5774 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "https://ega-archive.org (URL_TO_INSERT_RECORD-HOMEPAGE_5775 https://fairsharing.org/FAIRsharing.mya1ff) /datasets/EGAP0000000XYZ",
    "permissions": [
        {
            "target": "https://ega-archive.org (URL_TO_INSERT_RECORD-HOMEPAGE_5776 https://fairsharing.org/FAIRsharing.mya1ff) /datasets/EGAD0000000YYY",
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
            "assigner": "https://ega-archive.org (URL_TO_INSERT_RECORD-HOMEPAGE_5777 https://fairsharing.org/FAIRsharing.mya1ff) /",
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
                "target": "https://ega-archive.org (URL_TO_INSERT_RECORD-HOMEPAGE_5778 https://fairsharing.org/FAIRsharing.mya1ff) /datasets/EGAD0000000YYY",
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
    "policy (URL_TO_INSERT_TERM_5779 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_5780 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "http://example.com/policy:0099",
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

<#daa-policy (URL_TO_INSERT_TERM_5781 https://fairsharing.org/search?fairsharingRegistry=Policy) -1>
 a odrl:Policy (URL_TO_INSERT_TERM_5782 https://fairsharing.org/search?fairsharingRegistry=Policy)  .

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
  odrl:hasPolicy (URL_TO_INSERT_TERM_5783 https://fairsharing.org/search?fairsharingRegistry=Policy)  <#daa-policy (URL_TO_INSERT_TERM_5784 https://fairsharing.org/search?fairsharingRegistry=Policy) -1>;
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

