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

The aim is also to document equivalent representations and how bridges (URL_TO_INSERT_RECORD_8219 https://fairsharing.org/FAIRsharing.ac95d5)  can be built between the distinct but equivalent implementations.

Finally, the content aims to highlight key use-cases which require coverage, how to code such informat (URL_TO_INSERT_TERM_8220 https://fairsharing.org/search?recordType=model_and_format) ion, documenting 
implementation patterns in the context of **data cataloguing efforts**, for instance by expressing **Data Access Policies (URL_TO_INSERT_TERM_8221 https://fairsharing.org/search?fairsharingRegistry=Policy) **.


## Graphical Overview


````{dropdown}
:open:
```{figure} data-usage-mermaid.png
---
width: 850px
name: expressing-data-use-figure1
alt: Dealing with Policies (URL_TO_INSERT_TERM_8222 https://fairsharing.org/search?fairsharingRegistry=Policy)  and Data Use
---
Data Use
```
````



---

## Tools

### Standards

 Data Format (URL_TO_INSERT_TERM_8224 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_8225 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_8223 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
| JSON-LD<!-- TODO add a link to corresponding document --> | <!-- TODO add a link to corresponding document -->  |   |
| [ISO-8601](https://www.iso.org/iso-8601-date-and-time-format.html)  | [DCAT (URL_TO_INSERT_RECORD_8226 https://fairsharing.org/FAIRsharing.h4j3qm)  v2](https://www.w3.org/TR/vocab-dcat (URL_TO_INSERT_RECORD_8227 https://fairsharing.org/FAIRsharing.h4j3qm) -2/)  |   |
| [ISO-3066](https://www.iso.org/iso-3166-country-codes.html)  | [ODRL](https://www.w3.org/TR/odrl-vocab/)  |   |
| EGA XML<!-- TODO add a link to corresponding document -->   | [DUO](http://www.obofoundry.org/ontology/duo.html)  |   |
| [Data Article Tag Suite (DATS)](https://datatagsuite.github.io/schema/)  | [MONDO](http://www.obofoundry.org (URL_TO_INSERT_RECORD_8228 https://fairsharing.org/FAIRsharing.847069) /ontology/mondo.html)  |   |




### Implementation

DUOS:
https://duos.broadinstitute.org/

---

## Introduction

The preservation of patient privacy and the compliance with patient consent are essential considerations when managing
sensitive informat (URL_TO_INSERT_TERM_8229 https://fairsharing.org/search?recordType=model_and_format) ion such as clinical and patient data.
Consent forms, as signed by patients, define the acceptable usage of data derived from a patient for research (URL_TO_INSERT_RECORD_8230 https://fairsharing.org/FAIRsharing.52b22c)  applications.
All major research (URL_TO_INSERT_RECORD_8231 https://fairsharing.org/FAIRsharing.52b22c)  organizations, at national and international levels, enforce strict rules for the management of such data.
Sensitive data cannot be accessed without undergoing a vetting process involving a **data access request** to a **data access committee**,
which will decide, whether or not, to grant requesters access to the data.

This is a time-consuming process in the absence of machine-readable version of data access/ data management policies (URL_TO_INSERT_TERM_8232 https://fairsharing.org/search?fairsharingRegistry=Policy) .
In turns, it can prove detrimental to research (URL_TO_INSERT_RECORD_8233 https://fairsharing.org/FAIRsharing.52b22c) .
Therefore, efforts to enable the provision of concise, efficient and **machine processable** summary of key permissions and prohibitions have been made. 
Several resources are now available for the coding and exchange of **machine-actionable**, **legally binding** and
**explicit** informat (URL_TO_INSERT_TERM_8234 https://fairsharing.org/search?recordType=model_and_format) ion related to allowed and consented data usage.

The following sections detail how the international sequence data arch (URL_TO_INSERT_RECORD_8236 https://fairsharing.org/FAIRsharing.52b22c) ives (US NCBI dbGAP, SRA (URL_TO_INSERT_RECORD_8237 https://fairsharing.org/FAIRsharing.g7t2hv)  and EU EMBL_EBI EGA (URL_TO_INSERT_RECORD_8235 https://fairsharing.org/FAIRsharing.mya1ff) )
are encoding **Data Use Informat (URL_TO_INSERT_TERM_8238 https://fairsharing.org/search?recordType=model_and_format) ion**  but also how ODRL, a W3C specification, 
can be used to represent equivalent informat (URL_TO_INSERT_TERM_8239 https://fairsharing.org/search?recordType=model_and_format) ion in a format (URL_TO_INSERT_TERM_8240 https://fairsharing.org/search?recordType=model_and_format)  compatible with the data cataloguing efforts relying on W3C DC (URL_TO_INSERT_RECORD_8242 https://fairsharing.org/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD_8243 https://fairsharing.org/3547) AT (URL_TO_INSERT_RECORD_8241 https://fairsharing.org/FAIRsharing.h4j3qm)  specifications.




### SRA & EGA XML schema for Policy, Dataset and Controller

Next Generation Sequencing (NGS) techniques allow routine production of full genome data from patients.
This data is highly sensitive and data repositories (URL_TO_INSERT_TERM_8244 https://fairsharing.org/search?recordType=repository)  specialized in storing such informat (URL_TO_INSERT_TERM_8245 https://fairsharing.org/search?recordType=model_and_format) ion have developed (URL_TO_INSERT_RECORD_8246 https://fairsharing.org/FAIRsharing.31385c)  procedures 
and representation model (URL_TO_INSERT_TERM_8247 https://fairsharing.org/search?recordType=model_and_format) s for defining the conditions of use.

We summarize here the key objects used by the European Genome Arch (URL_TO_INSERT_RECORD_8249 https://fairsharing.org/FAIRsharing.52b22c) ive, in compliance with INSDC and GA4GH guideline (URL_TO_INSERT_TERM_8248 https://fairsharing.org/search?recordType=reporting_guideline) s.

https://ega-archive.org (URL_TO_INSERT_RECORD_8250 https://fairsharing.org/FAIRsharing.mya1ff) /data-use-conditions

````{dropdown}
:open:
```{figure} duo-ols-view-1.png
---
width: 700px
name: expressing-data-use-figure2
alt: Data Use Ontology (URL_TO_INSERT_TERM_8251 https://fairsharing.org/search?recordType=terminology_artefact)  Overview Part 1
---
Data Use Ontology (URL_TO_INSERT_TERM_8252 https://fairsharing.org/search?recordType=terminology_artefact)  Overview Part 1
```
````

````{dropdown}
:open:
```{figure} duo-ols-view-2.png
---
width: 700px
name: expressing-data-use-figure3
alt: Data Use Ontology (URL_TO_INSERT_TERM_8253 https://fairsharing.org/search?recordType=terminology_artefact)  Overview Part 2
---
Data Use Ontology (URL_TO_INSERT_TERM_8254 https://fairsharing.org/search?recordType=terminology_artefact)  Overview Part 2
```
````

<!-- 
````{panels}
:column: col-8
:card: border-2
DUO in OLS (URL_TO_INSERT_RECORD_8255 https://fairsharing.org/FAIRsharing.Mkl9RR) 
^^^
```{figure} duo-ols-view-1.png
width: 400px
```
---
DUO in OLS (URL_TO_INSERT_RECORD_8256 https://fairsharing.org/FAIRsharing.Mkl9RR) 
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
    <DAC alias="DAC-2011-08-11T11:45:28Z-1873" accession="EGAC00000000001" center_name="EBI" broker_name="EGA">
        <IDENTIFIER (URL_TO_INSERT_TERM_8257 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8258 https://fairsharing.org/FAIRsharing.cbc5c8) >
            <PRIMARY_ID>EGAC00000000001</PRIMARY_ID>
            <SUBMITTER_ID namespace="EBI">DAC-2011-08-11T11:45:28Z-1873</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_8259 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8260 https://fairsharing.org/FAIRsharing.cbc5c8) >
        <TITLE>EGA DAC TITLE</TITLE>
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
in the following example, the text of the policy (URL_TO_INSERT_TERM_8261 https://fairsharing.org/search?fairsharingRegistry=Policy)  is present in the XML (URL_TO_INSERT_RECORD_8262 https://fairsharing.org/FAIRsharing.b5cc91)  representation
```


```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<POLICY (URL_TO_INSERT_TERM_8263 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
    <POLICY (URL_TO_INSERT_TERM_8264 https://fairsharing.org/search?fairsharingRegistry=Policy)  center_name="EBI" alias="Policy (URL_TO_INSERT_TERM_8265 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868" accession="EGAP00001000001" broker_name="EBI">
        <IDENTIFIER (URL_TO_INSERT_TERM_8266 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8267 https://fairsharing.org/FAIRsharing.cbc5c8) >
            <PRIMARY_ID>EGAP00001000001</PRIMARY_ID>
            <SUBMITTER_ID namespace="SC">Policy (URL_TO_INSERT_TERM_8268 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_8269 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8270 https://fairsharing.org/FAIRsharing.cbc5c8) >
        <TITLE/>
        <DAC_REF accession="EGAP00001000001" refname="DAC_-2011-08-26T12:23:49Z-1868" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_8271 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8272 https://fairsharing.org/FAIRsharing.cbc5c8) >
                <PRIMARY_ID>EGAC00001000001</PRIMARY_ID>
                <SUBMITTER_ID namespace="EBI">DAC_-2011-08-26T12:23:49Z-1868</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_8273 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8274 https://fairsharing.org/FAIRsharing.cbc5c8) >
        </DAC_REF>
        <POLICY (URL_TO_INSERT_TERM_8275 https://fairsharing.org/search?fairsharingRegistry=Policy) _TEXT>https://www.sanger.ac.uk/datasharing/</POLICY_TEXT>
    </POLICY (URL_TO_INSERT_TERM_8276 https://fairsharing.org/search?fairsharingRegistry=Policy) >
</POLICY (URL_TO_INSERT_TERM_8277 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
```


```{note}
In the following example, the file address (url) to the policy (URL_TO_INSERT_TERM_8278 https://fairsharing.org/search?fairsharingRegistry=Policy)  is included in the XML (URL_TO_INSERT_RECORD_8279 https://fairsharing.org/FAIRsharing.b5cc91)  representation.
Ideally, the url provided should be a globally unique persistent identifier (URL_TO_INSERT_TERM_8280 https://fairsharing.org/search?recordType=identifier_schema)  so one can be sure to obtain at least the metadata about the document.
```

```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<POLICY (URL_TO_INSERT_TERM_8281 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
    <POLICY (URL_TO_INSERT_TERM_8282 https://fairsharing.org/search?fairsharingRegistry=Policy)  center_name="EBI" alias="Policy (URL_TO_INSERT_TERM_8283 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868" accession="EGAP00001000001" broker_name="EBI">
        <IDENTIFIER (URL_TO_INSERT_TERM_8284 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8285 https://fairsharing.org/FAIRsharing.cbc5c8) >
            <PRIMARY_ID>EGAP00001000001</PRIMARY_ID>
            <SUBMITTER_ID namespace="SC">Policy (URL_TO_INSERT_TERM_8286 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_8287 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8288 https://fairsharing.org/FAIRsharing.cbc5c8) >
        <TITLE/>
        <DAC_REF accession="EGAP00001000001" refname="DAC_-2011-08-26T12:23:49Z-1868" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_8289 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8290 https://fairsharing.org/FAIRsharing.cbc5c8) >
                <PRIMARY_ID>EGAC00001000001</PRIMARY_ID>
                <SUBMITTER_ID namespace="EBI">DAC_-2011-08-26T12:23:49Z-1868</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_8291 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8292 https://fairsharing.org/FAIRsharing.cbc5c8) >
        </DAC_REF>
        <POLICY (URL_TO_INSERT_TERM_8293 https://fairsharing.org/search?fairsharingRegistry=Policy) _FILE>https://www.sanger.ac.uk/datasharing/</POLICY_FILE>
    </POLICY (URL_TO_INSERT_TERM_8294 https://fairsharing.org/search?fairsharingRegistry=Policy) >
</POLICY (URL_TO_INSERT_TERM_8295 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
```


3. Expressing Data Use with EGA XML and **Data Use Ontology** codes.

```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<POLICY (URL_TO_INSERT_TERM_8296 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
    <POLICY (URL_TO_INSERT_TERM_8297 https://fairsharing.org/search?fairsharingRegistry=Policy)  center_name="EBI" alias="Policy (URL_TO_INSERT_TERM_8298 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868" accession="EGAP00001000001" broker_name="EBI">
        <IDENTIFIER (URL_TO_INSERT_TERM_8299 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8300 https://fairsharing.org/FAIRsharing.cbc5c8) >
            <PRIMARY_ID>EGAP00001000001</PRIMARY_ID>
            <SUBMITTER_ID namespace="SC">Policy (URL_TO_INSERT_TERM_8301 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_8302 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8303 https://fairsharing.org/FAIRsharing.cbc5c8) >
        <TITLE/>
        <DAC_REF accession="EGAP00001000001" refname="DAC_-2011-08-26T12:23:49Z-1868" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_8304 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8305 https://fairsharing.org/FAIRsharing.cbc5c8) >
                <PRIMARY_ID>EGAC00001000001</PRIMARY_ID>
                <SUBMITTER_ID namespace="EBI">DAC_-2011-08-26T12:23:49Z-1868</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_8306 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8307 https://fairsharing.org/FAIRsharing.cbc5c8) >
        </DAC_REF>
        <POLICY (URL_TO_INSERT_TERM_8308 https://fairsharing.org/search?fairsharingRegistry=Policy) _FILE>https://www.sanger.ac.uk/datasharing/</POLICY_FILE>
        <DATA_USES>
                   	<!-- no restriction -->
   			<DATA_USE>http://purl.obolibrary.org/obo/DUO_0000004</DATA_USE>

			<DATA_USES>
			   <DATA_USE ontology (URL_TO_INSERT_TERM_8309 https://fairsharing.org/search?recordType=terminology_artefact) ="DUO" code="0000004" version="17-07-2016"/>
			</DATA_USES>

        </DATA_USES>
    </POLICY (URL_TO_INSERT_TERM_8310 https://fairsharing.org/search?fairsharingRegistry=Policy) >
</POLICY (URL_TO_INSERT_TERM_8311 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
```



https://ega-archive.org/dacs

Indicating disease specific restriction on research with DUO and ontologies covering the Disease and Pathology domain.


```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<POLICY (URL_TO_INSERT_TERM_8312 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
    <POLICY (URL_TO_INSERT_TERM_8313 https://fairsharing.org/search?fairsharingRegistry=Policy)  center_name="EBI" alias="Policy (URL_TO_INSERT_TERM_8314 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868" accession="EGAP00001000001" broker_name="EBI">
        <IDENTIFIER (URL_TO_INSERT_TERM_8315 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8316 https://fairsharing.org/FAIRsharing.cbc5c8) >
            <PRIMARY_ID>EGAP00001000001</PRIMARY_ID>
            <SUBMITTER_ID namespace="SC">Policy (URL_TO_INSERT_TERM_8317 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_8318 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8319 https://fairsharing.org/FAIRsharing.cbc5c8) >
        <TITLE/>
        <DAC_REF accession="EGAP00001000001" refname="DAC_-2011-08-26T12:23:49Z-1868" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_8320 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8321 https://fairsharing.org/FAIRsharing.cbc5c8) >
                <PRIMARY_ID>EGAC00001000001</PRIMARY_ID>
                <SUBMITTER_ID namespace="EBI">DAC_-2011-08-26T12:23:49Z-1868</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_8322 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8323 https://fairsharing.org/FAIRsharing.cbc5c8) >
        </DAC_REF>
        <POLICY (URL_TO_INSERT_TERM_8324 https://fairsharing.org/search?fairsharingRegistry=Policy) _FILE>https://www.sanger.ac.uk/datasharing/</POLICY_FILE>
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
    </POLICY (URL_TO_INSERT_TERM_8325 https://fairsharing.org/search?fairsharingRegistry=Policy) >
</POLICY (URL_TO_INSERT_TERM_8326 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
```


```{note}
When using the consent code DUO (URL_TO_INSERT_RECORD_8329 https://fairsharing.org/FAIRsharing.5dnjs2) _0000007 where data is restricted for use on a specific disease area, it is necessary to explicitly indicate which disease area is allowed. This can be done by associating codes/identifier (URL_TO_INSERT_TERM_8328 https://fairsharing.org/search?recordType=identifier_schema) s from well established disease terminologies (URL_TO_INSERT_TERM_8327 https://fairsharing.org/search?recordType=terminology_artefact)  such as MONDO (URL_TO_INSERT_RECORD_8331 https://fairsharing.org/FAIRsharing.b2979t) , DOI (URL_TO_INSERT_RECORD_8330 https://fairsharing.org/FAIRsharing.hFLKCn) D (URL_TO_INSERT_RECORD_8332 https://fairsharing.org/FAIRsharing.8b6wfq) , SNOMED-CT.
For instance, if data reuse is restricted to research (URL_TO_INSERT_RECORD_8335 https://fairsharing.org/FAIRsharing.52b22c)  into `juvenile idiopathic arthritis`, the code should be displayed as DUO (URL_TO_INSERT_RECORD_8333 https://fairsharing.org/FAIRsharing.5dnjs2) _0000007; MONDO (URL_TO_INSERT_RECORD_8334 https://fairsharing.org/FAIRsharing.b2979t) :0011429
```



```XML
<POLICY (URL_TO_INSERT_TERM_8336 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
  <POLICY (URL_TO_INSERT_TERM_8337 https://fairsharing.org/search?fairsharingRegistry=Policy)  alias="ena-POLICY (URL_TO_INSERT_TERM_8338 https://fairsharing.org/search?fairsharingRegistry=Policy) -BABRAHAM-23-03-2017-09:47:38:853-62" center_name="BABRAHAM" accession="EGAP00001000615" broker_name="EGA">  
    <IDENTIFIER (URL_TO_INSERT_TERM_8339 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8340 https://fairsharing.org/FAIRsharing.cbc5c8) > 
      <PRIMARY_ID>EGAP00001000615</PRIMARY_ID>
      <SUBMITTER_ID namespace="BABRAHAM">ena-POLICY (URL_TO_INSERT_TERM_8341 https://fairsharing.org/search?fairsharingRegistry=Policy) -BABRAHAM-23-03-2017-09:47:38:853-62</SUBMITTER_ID>
    </IDENTIFIER (URL_TO_INSERT_TERM_8342 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8343 https://fairsharing.org/FAIRsharing.cbc5c8) >
    <TITLE>Data Access Agreement for PC (URL_TO_INSERT_RECORD_8344 https://fairsharing.org/FAIRsharing.5y3gdd) HiC, RNA-Seq, ChIP-Seq</TITLE>
    <DAC_REF accession="EGAC00001000523">
      <IDENTIFIER (URL_TO_INSERT_TERM_8345 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8346 https://fairsharing.org/FAIRsharing.cbc5c8) >
        <PRIMARY_ID>EGAC00001000523</PRIMARY_ID>
      </IDENTIFIER (URL_TO_INSERT_TERM_8347 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8348 https://fairsharing.org/FAIRsharing.cbc5c8) >
    </DAC_REF>
    <POLICY (URL_TO_INSERT_TERM_8349 https://fairsharing.org/search?fairsharingRegistry=Policy) _FILE>ftp://ftp.ebi.ac.uk/pub/contrib/pchic/EGA_Data_Access_Request_DIL.docx</POLICY_FILE>
    <DATA_USES>
      <DATA_USE ontology (URL_TO_INSERT_TERM_8350 https://fairsharing.org/search?recordType=terminology_artefact) ="DUO" code="0000007" version="17-07-2016">
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
       <DATA_USE ontology (URL_TO_INSERT_TERM_8351 https://fairsharing.org/search?recordType=terminology_artefact) ="DUO" code="0000014" version="17-07-2016"/>
       </DATA_USES>
   </POLICY (URL_TO_INSERT_TERM_8352 https://fairsharing.org/search?fairsharingRegistry=Policy) >
</POLICY (URL_TO_INSERT_TERM_8353 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
```




https://github.com/enasequence/schema/blob/USI/src/test/resources/uk/ac/ebi/ena/sra/xml/ega_dataset/ega_dataset.xml


```XML
<DATASETS>
    <DATASET alias="EGAS000000001-sc-20110919" center_name="SC" broker_name="EGA" accession="EGAD00001000039">
        <IDENTIFIER (URL_TO_INSERT_TERM_8354 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8355 https://fairsharing.org/FAIRsharing.cbc5c8) >
            <PRIMARY_ID>EGAD00001000039</PRIMARY_ID>
            <SUBMITTER_ID namespace="SC">EGAS000000001-sc-20110919</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_8356 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8357 https://fairsharing.org/FAIRsharing.cbc5c8) >
        <TITLE>Platelet collagen defect</TITLE>
        <RUN_REF accession="EGAR0000000001" refname="RUN_1" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_8358 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8359 https://fairsharing.org/FAIRsharing.cbc5c8) >
                <PRIMARY_ID>EGAR0000000001</PRIMARY_ID>
                <SUBMITTER_ID namespace="EBI">RUN_1</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_8360 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8361 https://fairsharing.org/FAIRsharing.cbc5c8) >
        </RUN_REF>
        <POLICY (URL_TO_INSERT_TERM_8362 https://fairsharing.org/search?fairsharingRegistry=Policy) _REF accession="EGAP00000001" refname="Policy (URL_TO_INSERT_TERM_8363 https://fairsharing.org/search?fairsharingRegistry=Policy) _-2011-08-17T15:05:39Z-1888" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_8364 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8365 https://fairsharing.org/FAIRsharing.cbc5c8) >
                <PRIMARY_ID>EGAP00001000024</PRIMARY_ID>
                <SUBMITTER_ID namespace="EBI">Policy (URL_TO_INSERT_TERM_8366 https://fairsharing.org/search?fairsharingRegistry=Policy) _-2011-08-17T15:05:39Z-1888</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_8367 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_8368 https://fairsharing.org/FAIRsharing.cbc5c8) >
        </POLICY (URL_TO_INSERT_TERM_8369 https://fairsharing.org/search?fairsharingRegistry=Policy) _REF>
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
In 2015, the dedicated working group produced the following JSON (URL_TO_INSERT_RECORD_8370 https://fairsharing.org/FAIRsharing.5bbab9)  schema implementation guidance
https://www.w3.org/community/odrl/json/2.1/#section-Schema

We base our representations on this specification {footcite}`ODRLJSON (URL_TO_INSERT_RECORD_8371 https://fairsharing.org/FAIRsharing.5bbab9) `. 

We are aware of a possible misalignment between the specifications of the Working Group (from 2015) and the latest
specifications as to whether to use the keys "name" or "leftOperand" (https://www.w3.org/TR/odrl-model/#constraint-rule, 2018).
In the following representations, we use the key "name" to validate against the 2015 JSON (URL_TO_INSERT_RECORD_8372 https://fairsharing.org/FAIRsharing.5bbab9) -schema
 https://www.w3.org/community/odrl/json/2.1/#section-Schema / https://github.com (URL_TO_INSERT_RECORD_8373 https://fairsharing.org/FAIRsharing.c55d5e) /iptc/rightsml-dev/blob/master/licensed/ODRL21.json

```

#### The different types of Policies

The ODRL model defines several subclasses for the **Policy** entity, namely  **Agreement**, **Set**, **Offer**.

##### Describing an agreement with ODRL

```json
{
    "policy (URL_TO_INSERT_TERM_8374 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Agreement",
    "policy (URL_TO_INSERT_TERM_8375 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "http://example.com/policy:5531",
    "inheritallowed": true,
    "permissions": [{
        "target": "http://example.com/report:2321",
        "action": "http://www.w3.org/ns/odrl/2/print",
        "assigner": "http://example.com/pub:88",
        "assignee": "http://example.com/billie:888"
    }]
}
{
    "policy (URL_TO_INSERT_TERM_8376 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Agreement",
    "policy (URL_TO_INSERT_TERM_8377 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "http://example.com/policy:9999",
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
    "policy (URL_TO_INSERT_TERM_8378 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_8379 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "https://fairplus.github.io/examples/policy_122334",
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
The main limitation of the representation is that it provides no informat (URL_TO_INSERT_TERM_8380 https://fairsharing.org/search?recordType=model_and_format) ion about which diseases are vetted for research (URL_TO_INSERT_RECORD_8381 https://fairsharing.org/FAIRsharing.52b22c) .
```

The following representation is more sophisticated and includes 3 types of restrictions:

- restriction on specific disease (juvenile arthritis, to reuse the exemplar representation in EGA/SRA XML presented in section 1)
- restriction on the geographical location where the research can be conducted
- an obligation to delete the data obtained through the access agreement past a specified duration, 3 years in our example

Let's proceed stepwise.


* Representing Research Restriction on Specific Disease Area using DUO and MONDO ontologies


```json
{
    "policy (URL_TO_INSERT_TERM_8382 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_8383 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "https://fairplus.github.io/examples/policy_122334",
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
While DUO (URL_TO_INSERT_RECORD_8385 https://fairsharing.org/FAIRsharing.5dnjs2)  is unique in its coverage of data uses, various disease ontologies (URL_TO_INSERT_TERM_8384 https://fairsharing.org/search?recordType=terminology_artefact)  exist and may be used to specify the
specific focus research (URL_TO_INSERT_RECORD_8386 https://fairsharing.org/FAIRsharing.52b22c)  should have.
For instance, SNOMED-CT, Disease Ontology (URL_TO_INSERT_TERM_8387 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_8388 https://fairsharing.org/FAIRsharing.8b6wfq)  could also be used.
It is worth noting that extensive cross referencing exists between resources such as DOI (URL_TO_INSERT_RECORD_8389 https://fairsharing.org/FAIRsharing.hFLKCn) D (URL_TO_INSERT_RECORD_8391 https://fairsharing.org/FAIRsharing.8b6wfq) , MONDO (URL_TO_INSERT_RECORD_8390 https://fairsharing.org/FAIRsharing.b2979t)  and
SNOMED-CT but this is something to consider when implementing brokering systems.
```



* Representing Research Restriction based on Geographical Regions

The section shows how to use ODRL to document geographical restrictions, either by listing countries where research is 
allowed or by listing those countries excluded from doing so.

In the following example, research is only allowed in a specific country, **Italy** in this case, which is 
encoded using the **ISO-3166 code**.


```json
{
    "policy (URL_TO_INSERT_TERM_8392 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_8393 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "https://fairplus.github.io/examples/policy_122334",
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
    "policy (URL_TO_INSERT_TERM_8394 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_8395 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "https://fairplus.github.io/examples/policy_122334",
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

This ODRL representation is **not vetted, nor endorsed by GA4GH or EGA (URL_TO_INSERT_RECORD_8396 https://fairsharing.org/FAIRsharing.mya1ff) **.
This example is currently meant to present an example of how to use ODRL to represent some of the informat (URL_TO_INSERT_TERM_8397 https://fairsharing.org/search?recordType=model_and_format) ion represented in EGA (URL_TO_INSERT_RECORD_8398 https://fairsharing.org/FAIRsharing.mya1ff) .

```

```json
{
    "policy (URL_TO_INSERT_TERM_8399 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_8400 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "https://ega-archive.org (URL_TO_INSERT_RECORD_8401 https://fairsharing.org/FAIRsharing.mya1ff) /datasets/EGAP0000000XYZ",
    "permissions": [
        {
            "target": "https://ega-archive.org (URL_TO_INSERT_RECORD_8402 https://fairsharing.org/FAIRsharing.mya1ff) /datasets/EGAD0000000YYY",
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
            "assigner": "https://ega-archive.org (URL_TO_INSERT_RECORD_8403 https://fairsharing.org/FAIRsharing.mya1ff) /",
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
                "target": "https://ega-archive.org (URL_TO_INSERT_RECORD_8404 https://fairsharing.org/FAIRsharing.mya1ff) /datasets/EGAD0000000YYY",
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
    "policy (URL_TO_INSERT_TERM_8405 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_8406 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "http://example.com/policy:0099",
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

<#daa-policy (URL_TO_INSERT_TERM_8407 https://fairsharing.org/search?fairsharingRegistry=Policy) -1>
 a odrl:Policy (URL_TO_INSERT_TERM_8408 https://fairsharing.org/search?fairsharingRegistry=Policy)  .

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
  odrl:hasPolicy (URL_TO_INSERT_TERM_8409 https://fairsharing.org/search?fairsharingRegistry=Policy)  <#daa-policy (URL_TO_INSERT_TERM_8410 https://fairsharing.org/search?fairsharingRegistry=Policy) -1>;
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

