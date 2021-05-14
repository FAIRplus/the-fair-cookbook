(fcb-reusability-data_use)=
# Patterns and practice for expressing allowed data usage

+++
<br/>

````{panels_fairplus}
:identifier_text: RX.X
:identifier_link: 'https://example.com'
:difficulty_level: 4
:recipe_type: hands_on
:reading_time_minutes: 15
:intended_audience: principal_investigator, data_manager, data_scientist, ontologist  
:has_executable_code: yeah
:recipe_name: Patterns and practice for expressing allowed data usage
```` 

## Main Objectives

The purpose of this content is to provide guidance on how to describe permitted use of data, identify the resources that exist to do so.
The aim is also to document equivalent representations and how bridges can be built between the distinct but equivalent implementations.

Finally, the content aims to highlight key use-cases which require coverage, how to code such information, suggest patterns and demonstrate implementation patterns for Policies which can be used in data cataloguing efforts.


## Graphical Overview



```{figure} data-usage-mermaid.png
---
width: 700px
name: 
alt: Dealing with Policies and Data Use
---
Data Use
```


---

## Capability and Maturity Table.

Capability Initial Maturity Level Final Maturity Level
Interoperability – minimal - repeatable

---

## tools

### vocabularies
DUO
ODRL
DCAT

### format

Short Read Archive XML
Data Article Tag Suite JSON


### implementation

DUOS:
https://duos.broadinstitute.org/#/home

---

## Introduction

The preservation of patient privacy and the compliance with patient consent are essential considerations when managing clinically sensitive information.
Consent forms as signed by patients define the acceptable usage of data derived from a patient for research applications.
All major research organizations, at national and international levels, enforce strict rules for the management of such data.
Sensitive data can not be accessed without undergoing a vetting process invovlving a data access request to a data access committee, which will decide whether or not to grant requesters access to the data.

This is a time consuming process in the absence of machine readable version of data access/ data management policies.
In turns, it can prove detrimental to research.
Therefore, efforts to enable the provision of concise, efficient and **machine processable** summary of key permissions and prohibitions have been made. 
Several resources are now available for the coding and exchange of `machine-actionable`, `legally binding` and `explicit` information related to allowed and consented data usage.

The following sections details how international sequence data archives (US NCBI' dbGAP, SRA and EU EMBL_EBI EGA) are encoding Data Use Information  but also how a W3C specification, ODRL, can be used to represent equivalent information in a format compatible with the data cataloguing efforts relying on W3C DCAT specification.




### SRA & EGA XML schema for Policy, Dataset and Controler

Next Generation Sequencing technique allow routine production of full genome data from patients. This data is highly sensitive and data repositories specialized in storing such information have developed procedures and representation models for defining the conditions of use.

We summerize here the key objects used by the European Genome Archive, in compliance with INSDC and GA4GH guidelines.

https://ega-archive.org/data-use-conditions

```{figure} duo-ols-view-1.png
---
width: 700px
name: 
alt: Data Use Ontology Overview Part 1
---
Data Use Ontology Overview Part 1
```

```{figure} duo-ols-view-2.png
---
width: 700px
name: 
alt: Data Use Ontology Overview Part 2
---
Data Use Ontology Overview Part 2
```

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


The information presented below has been sourced from:



1. The Data Access Committee and Contact information

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


https://github.com/enasequence/schema/blob/USI/src/test/resources/uk/ac/ebi/ena/sra/xml/ega_dac/ega_dac.xml

2. The Data Access Policy object


https://github.com/enasequence/schema/blob/USI/src/test/resources/uk/ac/ebi/ena/sra/xml/ega_policy/ega_policy.xml

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
in the following example, the file address (url) to the policy is included in the XML representation.
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


3. Expressing Data Use with EGA xml and Data Use Ontology codes.

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



https://ega-archive.org/dacs

Indicated disease specific restriction on research with DUO and Ontologies covering the Disease and Pathology domain


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


Point to Notice : For the consent code DUO_0000007 where data is restricted to use on a specific disease, please accompany it with an appropriate ontology from MONDO e.g., If the data is restricted to the use of research into juvenile idiopathic arthritis the code should be displayed as DUO_0000007; MONDO:0011429


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




https://github.com/enasequence/schema/blob/USI/src/test/resources/uk/ac/ebi/ena/sra/xml/ega_dataset/ega_dataset.xml


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




Browsing Data Access Committees available from EGA:


```{figure} dac-ega.png
---
width: 700px
name: 
alt: List of Data Access Policy from EGA
---
List of Data Access Policy from EGA
```



### ODRL

ODRL stands for Open Digital Rights Language, which is a set  W3C Recommendations defining a `policy expression language`. 

ODRL is made up of:

- [The ODRL Model](https://www.w3.org/TR/odrl-model/)


```{figure} https://www.w3.org/TR/odrl-model/00Model.png
---
width: 700px
name: 
alt: Open Digital Rights Language model
---
ODRL overview
```

- [The ODRL Vocabulary](https://www.w3.org/TR/odrl-vocab/)

The ODRL Vocabulary and Expression describes the terms used in ODRL policies and how to encode them.

The ODRL Vocabulary and Expression complements the ODRL information model.



```{warning}
In 2015, the dedicated working group produced the following JSON schema implementation guidance
https://www.w3.org/community/odrl/json/2.1/#section-Schema

We base our representations on this specification. 

We are aware of a possible misalignment between the specifications of the Working Group (from 2015) and the latest specifications as to whether to use the keys "name" or "leftOperand" (https://www.w3.org/TR/odrl-model/#constraint-rule, 2018).
In the following representations, we use the key "name" to validate against the 2015 JSON-schema https://www.w3.org/community/odrl/json/2.1/#section-Schema / https://github.com/iptc/rightsml-dev/blob/master/licensed/ODRL21.json

```

#### The different types of Policy

The ODRL model defines several subclasses for the `Policy` entity, namely  `Agreement`,`Set`,`Offer`

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


### Encoding research restriction on type of disease and geographical area

A basic ODRL based pattern using a DUO term to represent a situation where SecondaryUse of the data is allowed on the condition that work is restricted to `disease specific research`


```json
{
    "policytype": "http://www.w3.org/ns/odrl/2/Policy",
    "policyid": "ftp://ftp.ebi.ac.uk/pub/contrib/pchic/EGA_Data_Access_Request_DIL.docx",
    "permissions": [
        {
        "target": "EGAD00001000039",
        "action": "http://www.w3.org/ns/odrl/2/secondaryUse",
        "assigner": "https://ega-archive.org/",
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

The following representation is more sophisticated and includes 3 types for restrictions:

- restriction on specific disease (juvenile arthritis, to reuse to examplar representation in EGA/SRA XML presented in section 1)
- restriction on the geographical location where the research can be conducted
- an obligation to delete the data obtained through the agreement past a specified duration, 3 years in our example

Let's proceed stepwise.


* Representing Research Restriction on Specific Disease Area using DUO and MONDO ontologies


```json
{
    "policytype": "http://www.w3.org/ns/odrl/2/Policy",
    "policyid": "ftp://ftp.ebi.ac.uk/pub/contrib/pchic/EGA_Data_Access_Request_DIL.docx",
    "permissions": [
        {
            "target": "EGAD00001000039",
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
                }
            ]
        }
    ]
}
```

```{note}

when using refinements, note the difference in representation to indicate the nature of the action.
here is uses:

while the ordinary is simpler: 
"action": "http://www.w3.org/ns/odrl/2/secondaryUse",

vs

"action": [{
           		"rdf:value": { "@id": "odrl:secondaryUse" },
```


```{note}
While DUO is unique in its coverage of data uses, various disease ontologies exist and may be used to specify the specific focus research should have.
For instance, SNOMED-CT, Disease Ontology could also be used.
It is worth noting that extensive cross referencing exists between resources such as DOID, MONDO and SNOMED-CT but this is something to consider when implementing brokering systems.
```



* Representing Research Restriction based on Geographical Regions, geofencing

The section step shows how to use ODRL to document a geographical restrictions. This can be to list countries where research is allowed or to exclude countries from using a given dataset.

In the following example, research is only allowed in a specific country, Italy in our example, which is encoded using ISO-3166 code.


```json
{
    "policytype": "http://www.w3.org/ns/odrl/2/Policy",
    "policyid": "ftp://ftp.ebi.ac.uk/pub/contrib/pchic/EGA_Data_Access_Request_DIL.docx",
    "permissions": [
        {
            "target": "EGAD00001000039",
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
            ]
        }
    ]
}
```

* Representing Obligations regarding Data Management

The following example shows how explicitly state in a Policy element that the data must be deleted after a defined period of time, here 3 years.
Duration and time related value should be represented using ISO-8601 standard.


```json
{
    "policytype": "http://www.w3.org/ns/odrl/2/Policy",
    "policyid": "ftp://ftp.ebi.ac.uk/pub/contrib/pchic/EGA_Data_Access_Request_DIL.docx",
    "permissions": [
        {
            "target": "EGAD00001000039",
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
                "target": "EGAD00001000039",
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

The ODRL model provides the `prohibitions` relation, which uses similar patterns to those seen while covering  `permissions`. The ODRL vocabulary is then used to identify the `actions` which are restricted under the `prohibition` header. Complex prohibitions can be expressed using `constraints` and `refinement` elements.


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



## Implementing in Datacatalogues with DCAT or with DATS


### RDF representation of an ODRL Policy from a DCAT DataSet

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

An evolution of the DATS [2,3] schema is used by University of Luxembourg to build a data catalogue for IMI projects and datasets.
The proposed patterns could be used and tested to representation DAC/DAA information as well as the allowed uses of datasets generated by the consortia funded by IMI.
More complex use cases can be considered to assess to ability of the representations to be associated to specific datasets, for instance datasets associated with a particular data acquisition technique the access of which may require specific policies and conditions to be made machine readable.

The approach is therefore to reference the  JSON representations compliant with the ODRL JSON schema 2.1 specification, as presented in earlier sections in conjunction with DATS JSON documents.



### ODRL Validation:

Code exists that allows developers to validate ODRL documents **expressed in legitimate RDF serializations**.

http://odrlapi.appspot.com/



```{figure} ./odrl-validation-app.png
---
width: 800px
alt: ODRL Validation and Evaluation Sandbox
name: ODRL Validation and Evaluation Sandbox
---
ODRL Validation and Evaluation Sandbox
```



The webapplication is powered by a REST-API the swagger document of which is available from the following address: http://odrlapi.appspot.com/apidoc/index.html

<!-- ## TODO discuss relation to RightML

https://iptc.org/std/RightsML/2.0/RightsML_2.0-specification.html -->

## Consuming Data Use related annotations

It is all good and and well to describe patterns in various formats but are there any tools or services capable exploiting these annotations?
Well, when it comes to genomics data, the Broad Institute's  [Data Use Oversight System (DUOS)](https://duos.broadinstitute.org/#/home).


```{figure} ./broads-duos.png
---
width: 800px
alt: Broad's Institute  Data Use Oversight System
name: Broad's Institute  Data Use Oversight System
---
Broad's Institute  Data Use Oversight System landing page
```

DUOS requires official clearance from `Data Access Committee` representative or an `Authorized Submission Representative` to enable registration of a dataset into the DUOS.
Once this authorization is available, the dataset has to be annotated following the patterns defined by GA4GH with Data Use Ontology and 'SRA xml' format.

The European Genome Archive allows programmatic filtering based on the this information via the REST-API of the service.

## Conclusion

Making sure that machine readable information about the conditions of use of dataset and data is key to enable privacy preserving and policy compliant use of information across organizations.
This content provides an overview of the models available to do so and how it has been applied to life science data, showing the main features of the models and how to define used based on the major properties such as the type of research allowed, how to indicate disease domain or geographical restrictions as well as temporal restrictions associated to the dataset and defined by the data owners/data controlers.



### What to read next?

* {ref}`rr-licensing-software`
* {ref}`rr-licensing-data`



___


## References


[1]. Dyke et al, 2017. http://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1005772

[2]. Sansone et al, 2017: https://doi.org/10.1038/sdata.2017.59

[3]. Alter et al, 2020: https://doi.org/10.1093/gigascience/giz165

[4]. ODLR model: https://www.w3.org/TR/odrl-model

[5]. ODRL vocabulary: https://www.w3.org/TR/odrl-vocab/

[6]. DRL JSON schema: https://www.w3.org/community/odrl/json/2.1/#section-Schema

[7]. DUO: http://purl.obolibrary.org/obo/duo.owl

[8]. RIGHTML: https://iptc.org/std/RightsML/2.0/RightsML_2.0-specification.html


---

## Authors

| Name                                                                                                                                                                            | Orcid                                                                                                         | Affiliation              | Type                                                                              |                                                              Elixir Node                                                              | Credit Role
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|--------------------------|-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------:|:----------------:|
| <div class="firstCol"><a target="_blank" href='https://github.com/proccaserra'><img class='avatar-style' src='https://avatars.githubusercontent.com/proccaserra'></img><div class="d-block">Philippe Rocca-Serra</div></a>  </div>         | <a target="_blank" href='https://orcid.org/0000-0001-9853-5668'><i class='fab fa-orcid fa-2x text--orange'></i></a> | University of Oxford     | <i class="fas fa-graduation-cap fa-1x text--orange" alt="Academic"></i> | <img class='elixir-style' src='/the-fair-cookbook/_static/images/logo/Elixir/ELIXIR-UK.svg' ></img> | Writing - Original Draft, Conceptualization |
| <div class="firstCol"><img class='avatar-style' src='https://avatars.githubusercontent.com/no_github'></img><div class="d-block">Tom Plasterer</div></div>    |   | Astra-Zeneca  | <i class="fas fa-industry fa-1x text--purple-light" alt="EFPIA"></i>       |  |Writing - Original Draft, Conceptualization
| <div class="firstCol"><a target="_blank" href='https://github.com/mcourtot'><img class='avatar-style' src='https://avatars.githubusercontent.com/mcourtot'></img><div class="d-block">Melanie Courtot</div></a></div>    | <a target="_blank" href='https://orcid.org/0000-0002-9551-6370'><i class='fab fa-orcid fa-2x text--orange'></i></a> | EMBL-EBI      | <i class="fas fa-graduation-cap fa-1x text--orange" alt="Academic"></i> | | Writing – Review & Editing
| <div class="firstCol"><a target="_blank" href='https://github.com/fuqix'><img class='avatar-style' src='https://avatars.githubusercontent.com/fuqix'></img><div class="d-block">Fuqi Xu</div></a>   </div>      | <a target="_blank" href='https://orcid.org/0000-0002-5923-3859'><i class='fab fa-orcid fa-2x text--orange'></i></a> | EMBL-EBI      | <i class="fas fa-graduation-cap fa-1x text--orange" alt="Academic"></i> | | Writing – Review & Editing
| <div class="firstCol"><a target="_blank" href='https://github.com/weiguUL'><img class='avatar-style' src='https://avatars.githubusercontent.com/weiguUL'></img><div class="d-block">Wei Gu</div></a>  </div>    | <a target="_blank" href='https://orcid.org/0000-0003-3951-6680'><i class='fab fa-orcid fa-2x text--orange'></i></a> | University of Luxembourg        | <i class="fas fa-graduation-cap fa-1x text--orange" alt="Academic"></i> | <img class='elixir-style' src='/the-fair-cookbook/_static/images/logo/Elixir/ELIXIR-LU.svg' ></img> | Writing – Review & Editing

___

## License

This page is released under the Creative Commons 4.0 BY license.

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png" height="20"/></a>

