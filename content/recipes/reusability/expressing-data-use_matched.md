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

The aim is also to document equivalent representations and how bridges (URL_TO_INSERT_RECORD_9769 https://fairsharing.org/FAIRsharing.ac95d5)  can be built between the distinct but equivalent implementations.

Finally, the content aims to highlight key use-cases which require coverage, how to code such informat (URL_TO_INSERT_TERM_9770 https://fairsharing.org/search?recordType=model_and_format) ion, documenting 
implementation patterns in the context of **data cataloguing efforts**, for instance by expressing **Data Access Policies (URL_TO_INSERT_TERM_9771 https://fairsharing.org/search?fairsharingRegistry=Policy) **.


## Graphical Overview


````{dropdown}
:open:
```{figure} data-usage-mermaid.png
---
width: 850px
name: expressing-data-use-figure1
alt: Dealing with Policies (URL_TO_INSERT_TERM_9772 https://fairsharing.org/search?fairsharingRegistry=Policy)  and Data Use
---
Data Use
```
````



---

## Tools

### Standards

 Data Format (URL_TO_INSERT_TERM_9774 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_9775 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_9773 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
| JSON-LD<!-- TODO add a link to corresponding document --> | <!-- TODO add a link to corresponding document -->  |   |
| [ISO-8601](https://www.iso.org/iso-8601-date-and-time-format.html)  | [DC (URL_TO_INSERT_RECORD_9778 https://fairsharing.org/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD_9779 https://fairsharing.org/3547) AT (URL_TO_INSERT_RECORD_9776 https://fairsharing.org/FAIRsharing.h4j3qm)  v2](https://www.w3.org/TR/vocab-dcat (URL_TO_INSERT_RECORD_9777 https://fairsharing.org/FAIRsharing.h4j3qm) -2/)  |   |
| [ISO-3066](https://www.iso.org/iso-3166-country-codes.html)  | [ODRL](https://www.w3.org/TR/odrl-vocab/)  |   |
| EGA XML<!-- TODO add a link to corresponding document -->   | [DUO](http://www.obofoundry.org/ontology/duo.html)  |   |
| [Data Article Tag Suite (DATS)](https://datatagsuite.github.io/schema/)  | [MONDO](http://www.obofoundry.org (URL_TO_INSERT_RECORD_9780 https://fairsharing.org/FAIRsharing.847069) /ontology/mondo.html)  |   |




### Implementation

DUO (URL_TO_INSERT_RECORD_9781 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_9782 https://fairsharing.org/FAIRsharing.mjnypw) S:
https://duos.broadinstitute.org/

---

## Introduction

The preservation of patient privacy and the compliance with patient consent are essential considerations when managing
sensitive informat (URL_TO_INSERT_TERM_9783 https://fairsharing.org/search?recordType=model_and_format) ion such as clinical and patient data.
Consent forms, as signed by patients, define the acceptable usage of data derived from a patient for research (URL_TO_INSERT_RECORD_9784 https://fairsharing.org/FAIRsharing.52b22c)  applications.
All major research (URL_TO_INSERT_RECORD_9785 https://fairsharing.org/FAIRsharing.52b22c)  organizations, at national and international levels, enforce strict rules for the management of such data.
Sensitive data cannot be accessed without undergoing a vetting process involving a **data access request** to a **data access committee**,
which will decide, whether or not, to grant requesters access to the data.

This is a time-consuming process in the absence of machine-readable version of data access/ data management policies (URL_TO_INSERT_TERM_9786 https://fairsharing.org/search?fairsharingRegistry=Policy) .
In turns, it can prove detrimental to research (URL_TO_INSERT_RECORD_9787 https://fairsharing.org/FAIRsharing.52b22c) .
Therefore, efforts to enable the provision of concise, efficient and **machine processable** summary of key permissions and prohibitions have been made. 
Several resources are now available for the coding and exchange of **machine-actionable**, **legally binding** and
**explicit** informat (URL_TO_INSERT_TERM_9788 https://fairsharing.org/search?recordType=model_and_format) ion related to allowed and consented data usage.

The following sections detail how the international sequence data arch (URL_TO_INSERT_RECORD_9790 https://fairsharing.org/FAIRsharing.52b22c) ives (US NCBI dbGAP, SRA (URL_TO_INSERT_RECORD_9791 https://fairsharing.org/FAIRsharing.g7t2hv)  and EU EMBL_EBI EGA (URL_TO_INSERT_RECORD_9789 https://fairsharing.org/FAIRsharing.mya1ff) )
are encoding **Data Use Informat (URL_TO_INSERT_TERM_9792 https://fairsharing.org/search?recordType=model_and_format) ion**  but also how ODR (URL_TO_INSERT_RECORD_9793 https://fairsharing.org/FAIRsharing.1sfhp3) L, a W3C specification, 
can be used to represent equivalent informat (URL_TO_INSERT_TERM_9794 https://fairsharing.org/search?recordType=model_and_format) ion in a format (URL_TO_INSERT_TERM_9795 https://fairsharing.org/search?recordType=model_and_format)  compatible with the data cataloguing efforts relying on W3C DC (URL_TO_INSERT_RECORD_9797 https://fairsharing.org/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD_9798 https://fairsharing.org/3547) AT (URL_TO_INSERT_RECORD_9796 https://fairsharing.org/FAIRsharing.h4j3qm)  specifications.




### SRA & EGA XML schema for Policy, Dataset and Controller

Next Generation Sequencing (NGS) techniques allow routine production of full genome data from patients.
This data is highly sensitive and data repositories (URL_TO_INSERT_TERM_9799 https://fairsharing.org/search?recordType=repository)  specialized in storing such informat (URL_TO_INSERT_TERM_9800 https://fairsharing.org/search?recordType=model_and_format) ion have developed (URL_TO_INSERT_RECORD_9801 https://fairsharing.org/FAIRsharing.31385c)  procedures 
and representation model (URL_TO_INSERT_TERM_9802 https://fairsharing.org/search?recordType=model_and_format) s for defining the conditions of use.

We summarize here the key objects used by the European Genome Arch (URL_TO_INSERT_RECORD_9806 https://fairsharing.org/FAIRsharing.52b22c) ive, in compliance with INSD (URL_TO_INSERT_RECORD_9804 https://fairsharing.org/FAIRsharing.mKDii0) C (URL_TO_INSERT_RECORD_9805 https://fairsharing.org/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD_9807 https://fairsharing.org/3547)  and GA4GH guideline (URL_TO_INSERT_TERM_9803 https://fairsharing.org/search?recordType=reporting_guideline) s.

https://ega-archive.org (URL_TO_INSERT_RECORD_9808 https://fairsharing.org/FAIRsharing.mya1ff) /data-use-conditions

````{dropdown}
:open:
```{figure} duo-ols-view-1.png
---
width: 700px
name: expressing-data-use-figure2
alt: Data Use Ontology (URL_TO_INSERT_TERM_9809 https://fairsharing.org/search?recordType=terminology_artefact)  Overview Part 1
---
Data Use Ontology (URL_TO_INSERT_TERM_9810 https://fairsharing.org/search?recordType=terminology_artefact)  Overview Part 1
```
````

````{dropdown}
:open:
```{figure} duo-ols-view-2.png
---
width: 700px
name: expressing-data-use-figure3
alt: Data Use Ontology (URL_TO_INSERT_TERM_9811 https://fairsharing.org/search?recordType=terminology_artefact)  Overview Part 2
---
Data Use Ontology (URL_TO_INSERT_TERM_9812 https://fairsharing.org/search?recordType=terminology_artefact)  Overview Part 2
```
````

<!-- 
````{panels}
:column: col-8
:card: border-2
DUO (URL_TO_INSERT_RECORD_9813 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_9815 https://fairsharing.org/FAIRsharing.mjnypw)  in OLS (URL_TO_INSERT_RECORD_9814 https://fairsharing.org/FAIRsharing.Mkl9RR) 
^^^
```{figure} duo-ols-view-1.png
width: 400px
```
---
DUO (URL_TO_INSERT_RECORD_9816 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_9818 https://fairsharing.org/FAIRsharing.mjnypw)  in OLS (URL_TO_INSERT_RECORD_9817 https://fairsharing.org/FAIRsharing.Mkl9RR) 
^^^
```{figure} duo-ols-view-2.png
width: 400px
```

```` -->


The information presented below has been sourced from the ENA GitHub repo.



1. The **Data Access Committee** and Contact information

```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<DAC (URL_TO_INSERT_RECORD_9819 https://fairsharing.org/FAIRsharing.md3e78) _SET>
    <DAC (URL_TO_INSERT_RECORD_9822 https://fairsharing.org/FAIRsharing.md3e78)  alias="DAC (URL_TO_INSERT_RECORD_9823 https://fairsharing.org/FAIRsharing.md3e78) -2011-08-11T11:45:28Z-1873" accession="EGA (URL_TO_INSERT_RECORD_9820 https://fairsharing.org/FAIRsharing.mya1ff) C (URL_TO_INSERT_RECORD_9824 https://fairsharing.org/FAIRsharing.md3e78) 00000000001" center_name="EBI" broker_name="EGA (URL_TO_INSERT_RECORD_9821 https://fairsharing.org/FAIRsharing.mya1ff) ">
        <IDENTIFIER (URL_TO_INSERT_TERM_9825 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9826 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9827 https://fairsharing.org/FAIRsharing.vajn3f) >
            <PRIMA (URL_TO_INSERT_RECORD_9831 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9828 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_9830 https://fairsharing.org/FAIRsharing.mya1ff) C (URL_TO_INSERT_RECORD_9833 https://fairsharing.org/FAIRsharing.md3e78) 00000000001</PRIMA (URL_TO_INSERT_RECORD_9832 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9829 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
            <SUBMITTER_ID namespace="EBI">DAC (URL_TO_INSERT_RECORD_9834 https://fairsharing.org/FAIRsharing.md3e78) -2011-08-11T11:45:28Z-1873</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_9835 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9836 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9837 https://fairsharing.org/FAIRsharing.vajn3f) >
        <TITLE>EGA (URL_TO_INSERT_RECORD_9838 https://fairsharing.org/FAIRsharing.mya1ff)  DAC (URL_TO_INSERT_RECORD_9839 https://fairsharing.org/FAIRsharing.md3e78)  TITLE</TITLE>
        <CO (URL_TO_INSERT_RECORD_9840 https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD_9841 https://fairsharing.org/FAIRsharing.thskvr) NTAC (URL_TO_INSERT_RECORD_9842 https://fairsharing.org/FAIRsharing.md3e78) TS>
            <CO (URL_TO_INSERT_RECORD_9843 https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD_9844 https://fairsharing.org/FAIRsharing.thskvr) NTAC (URL_TO_INSERT_RECORD_9845 https://fairsharing.org/FAIRsharing.md3e78) T name="Joe Bloggs" email="joe@noname.com" organisation="EBI"/>
        </CO (URL_TO_INSERT_RECORD_9846 https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD_9847 https://fairsharing.org/FAIRsharing.thskvr) NTAC (URL_TO_INSERT_RECORD_9848 https://fairsharing.org/FAIRsharing.md3e78) TS>
    </DAC (URL_TO_INSERT_RECORD_9849 https://fairsharing.org/FAIRsharing.md3e78) >
</DAC (URL_TO_INSERT_RECORD_9850 https://fairsharing.org/FAIRsharing.md3e78) _SET>
```


https://github.com/enasequence/schema/blob/USI/src/test/resources/uk/ac/ebi/ena/sra/xml/ega_dac/ega_dac.xml

2. The **Data Access Policy** object


https://github.com/enasequence/schema/blob/USI/src/test/resources/uk/ac/ebi/ena/sra/xml/ega_policy/ega_policy.xml

```{note}
in the following example, the text of the policy (URL_TO_INSERT_TERM_9851 https://fairsharing.org/search?fairsharingRegistry=Policy)  is present in the XML (URL_TO_INSERT_RECORD_9852 https://fairsharing.org/FAIRsharing.b5cc91)  representation
```


```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<PO (URL_TO_INSERT_RECORD_9854 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9853 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
    <PO (URL_TO_INSERT_RECORD_9857 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9855 https://fairsharing.org/search?fairsharingRegistry=Policy)  center_name="EBI" alias="Policy (URL_TO_INSERT_TERM_9856 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868" accession="EGA (URL_TO_INSERT_RECORD_9858 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001" broker_name="EBI">
        <IDENTIFIER (URL_TO_INSERT_TERM_9859 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9860 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9861 https://fairsharing.org/FAIRsharing.vajn3f) >
            <PRIMA (URL_TO_INSERT_RECORD_9865 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9862 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_9864 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001</PRIMA (URL_TO_INSERT_RECORD_9866 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9863 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
            <SUBMITTER_ID namespace="SC">Policy (URL_TO_INSERT_TERM_9867 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_9868 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9869 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9870 https://fairsharing.org/FAIRsharing.vajn3f) >
        <TITLE/>
        <DAC (URL_TO_INSERT_RECORD_9872 https://fairsharing.org/FAIRsharing.md3e78) _REF accession="EGA (URL_TO_INSERT_RECORD_9871 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001" refname="DAC (URL_TO_INSERT_RECORD_9873 https://fairsharing.org/FAIRsharing.md3e78) _-2011-08-26T12:23:49Z-1868" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_9874 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9875 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9876 https://fairsharing.org/FAIRsharing.vajn3f) >
                <PRIMA (URL_TO_INSERT_RECORD_9880 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9877 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_9879 https://fairsharing.org/FAIRsharing.mya1ff) C (URL_TO_INSERT_RECORD_9882 https://fairsharing.org/FAIRsharing.md3e78) 00001000001</PRIMA (URL_TO_INSERT_RECORD_9881 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9878 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
                <SUBMITTER_ID namespace="EBI">DAC (URL_TO_INSERT_RECORD_9883 https://fairsharing.org/FAIRsharing.md3e78) _-2011-08-26T12:23:49Z-1868</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_9884 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9885 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9886 https://fairsharing.org/FAIRsharing.vajn3f) >
        </DAC (URL_TO_INSERT_RECORD_9887 https://fairsharing.org/FAIRsharing.md3e78) _REF>
        <PO (URL_TO_INSERT_RECORD_9889 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9888 https://fairsharing.org/search?fairsharingRegistry=Policy) _TEXT>https://www.sanger.ac.uk/datasharing/</POLICY_TEXT>
    </PO (URL_TO_INSERT_RECORD_9891 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9890 https://fairsharing.org/search?fairsharingRegistry=Policy) >
</PO (URL_TO_INSERT_RECORD_9893 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9892 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
```


```{note}
In the following example, the file address (url) to the policy (URL_TO_INSERT_TERM_9894 https://fairsharing.org/search?fairsharingRegistry=Policy)  is included in the XML (URL_TO_INSERT_RECORD_9895 https://fairsharing.org/FAIRsharing.b5cc91)  representation.
Ideally, the url provided should be a globally unique persistent identifier (URL_TO_INSERT_TERM_9896 https://fairsharing.org/search?recordType=identifier_schema)  so one can be sure to obtain at least the metadata about the document.
```

```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<PO (URL_TO_INSERT_RECORD_9898 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9897 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
    <PO (URL_TO_INSERT_RECORD_9901 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9899 https://fairsharing.org/search?fairsharingRegistry=Policy)  center_name="EBI" alias="Policy (URL_TO_INSERT_TERM_9900 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868" accession="EGA (URL_TO_INSERT_RECORD_9902 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001" broker_name="EBI">
        <IDENTIFIER (URL_TO_INSERT_TERM_9903 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9904 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9905 https://fairsharing.org/FAIRsharing.vajn3f) >
            <PRIMA (URL_TO_INSERT_RECORD_9909 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9906 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_9908 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001</PRIMA (URL_TO_INSERT_RECORD_9910 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9907 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
            <SUBMITTER_ID namespace="SC">Policy (URL_TO_INSERT_TERM_9911 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_9912 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9913 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9914 https://fairsharing.org/FAIRsharing.vajn3f) >
        <TITLE/>
        <DAC (URL_TO_INSERT_RECORD_9916 https://fairsharing.org/FAIRsharing.md3e78) _REF accession="EGA (URL_TO_INSERT_RECORD_9915 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001" refname="DAC (URL_TO_INSERT_RECORD_9917 https://fairsharing.org/FAIRsharing.md3e78) _-2011-08-26T12:23:49Z-1868" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_9918 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9919 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9920 https://fairsharing.org/FAIRsharing.vajn3f) >
                <PRIMA (URL_TO_INSERT_RECORD_9924 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9921 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_9923 https://fairsharing.org/FAIRsharing.mya1ff) C (URL_TO_INSERT_RECORD_9926 https://fairsharing.org/FAIRsharing.md3e78) 00001000001</PRIMA (URL_TO_INSERT_RECORD_9925 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9922 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
                <SUBMITTER_ID namespace="EBI">DAC (URL_TO_INSERT_RECORD_9927 https://fairsharing.org/FAIRsharing.md3e78) _-2011-08-26T12:23:49Z-1868</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_9928 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9929 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9930 https://fairsharing.org/FAIRsharing.vajn3f) >
        </DAC (URL_TO_INSERT_RECORD_9931 https://fairsharing.org/FAIRsharing.md3e78) _REF>
        <PO (URL_TO_INSERT_RECORD_9933 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9932 https://fairsharing.org/search?fairsharingRegistry=Policy) _FILE>https://www.sanger.ac.uk/datasharing/</POLICY_FILE>
    </PO (URL_TO_INSERT_RECORD_9935 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9934 https://fairsharing.org/search?fairsharingRegistry=Policy) >
</PO (URL_TO_INSERT_RECORD_9937 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9936 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
```


3. Expressing Data Use with EGA XML and **Data Use Ontology** codes.

```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<PO (URL_TO_INSERT_RECORD_9939 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9938 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
    <PO (URL_TO_INSERT_RECORD_9942 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9940 https://fairsharing.org/search?fairsharingRegistry=Policy)  center_name="EBI" alias="Policy (URL_TO_INSERT_TERM_9941 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868" accession="EGA (URL_TO_INSERT_RECORD_9943 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001" broker_name="EBI">
        <IDENTIFIER (URL_TO_INSERT_TERM_9944 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9945 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9946 https://fairsharing.org/FAIRsharing.vajn3f) >
            <PRIMA (URL_TO_INSERT_RECORD_9950 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9947 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_9949 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001</PRIMA (URL_TO_INSERT_RECORD_9951 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9948 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
            <SUBMITTER_ID namespace="SC">Policy (URL_TO_INSERT_TERM_9952 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_9953 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9954 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9955 https://fairsharing.org/FAIRsharing.vajn3f) >
        <TITLE/>
        <DAC (URL_TO_INSERT_RECORD_9957 https://fairsharing.org/FAIRsharing.md3e78) _REF accession="EGA (URL_TO_INSERT_RECORD_9956 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001" refname="DAC (URL_TO_INSERT_RECORD_9958 https://fairsharing.org/FAIRsharing.md3e78) _-2011-08-26T12:23:49Z-1868" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_9959 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9960 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9961 https://fairsharing.org/FAIRsharing.vajn3f) >
                <PRIMA (URL_TO_INSERT_RECORD_9965 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9962 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_9964 https://fairsharing.org/FAIRsharing.mya1ff) C (URL_TO_INSERT_RECORD_9967 https://fairsharing.org/FAIRsharing.md3e78) 00001000001</PRIMA (URL_TO_INSERT_RECORD_9966 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9963 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
                <SUBMITTER_ID namespace="EBI">DAC (URL_TO_INSERT_RECORD_9968 https://fairsharing.org/FAIRsharing.md3e78) _-2011-08-26T12:23:49Z-1868</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_9969 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9970 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9971 https://fairsharing.org/FAIRsharing.vajn3f) >
        </DAC (URL_TO_INSERT_RECORD_9972 https://fairsharing.org/FAIRsharing.md3e78) _REF>
        <PO (URL_TO_INSERT_RECORD_9974 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9973 https://fairsharing.org/search?fairsharingRegistry=Policy) _FILE>https://www.sanger.ac.uk/datasharing/</POLICY_FILE>
        <DATA_USES>
                   	<!-- no restriction -->
   			<DATA_USE>http://purl.obolibrary.org/obo/DUO_0000004</DATA_USE>

			<DATA_USES>
			   <DATA_USE ontology (URL_TO_INSERT_TERM_9975 https://fairsharing.org/search?recordType=terminology_artefact) ="DUO (URL_TO_INSERT_RECORD_9976 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_9977 https://fairsharing.org/FAIRsharing.mjnypw) " code="0000004" version="17-07-2016"/>
			</DATA_USES>

        </DATA_USES>
    </PO (URL_TO_INSERT_RECORD_9979 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9978 https://fairsharing.org/search?fairsharingRegistry=Policy) >
</PO (URL_TO_INSERT_RECORD_9981 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9980 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
```



https://ega-archive.org/dacs

Indicating disease specific restriction on research with DUO and ontologies covering the Disease and Pathology domain.


```XML
<?xml version = '1.0' encoding = 'UTF-8'?>
<PO (URL_TO_INSERT_RECORD_9983 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9982 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
    <PO (URL_TO_INSERT_RECORD_9986 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_9984 https://fairsharing.org/search?fairsharingRegistry=Policy)  center_name="EBI" alias="Policy (URL_TO_INSERT_TERM_9985 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868" accession="EGA (URL_TO_INSERT_RECORD_9987 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001" broker_name="EBI">
        <IDENTIFIER (URL_TO_INSERT_TERM_9988 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9989 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9990 https://fairsharing.org/FAIRsharing.vajn3f) >
            <PRIMA (URL_TO_INSERT_RECORD_9994 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9991 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_9993 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001</PRIMA (URL_TO_INSERT_RECORD_9995 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_9992 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
            <SUBMITTER_ID namespace="SC">Policy (URL_TO_INSERT_TERM_9996 https://fairsharing.org/search?fairsharingRegistry=Policy) -2011-08-26T12:23:53Z-1868</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_9997 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_9998 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_9999 https://fairsharing.org/FAIRsharing.vajn3f) >
        <TITLE/>
        <DAC (URL_TO_INSERT_RECORD_10001 https://fairsharing.org/FAIRsharing.md3e78) _REF accession="EGA (URL_TO_INSERT_RECORD_10000 https://fairsharing.org/FAIRsharing.mya1ff) P00001000001" refname="DAC (URL_TO_INSERT_RECORD_10002 https://fairsharing.org/FAIRsharing.md3e78) _-2011-08-26T12:23:49Z-1868" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_10003 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_10004 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_10005 https://fairsharing.org/FAIRsharing.vajn3f) >
                <PRIMA (URL_TO_INSERT_RECORD_10009 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_10006 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_10008 https://fairsharing.org/FAIRsharing.mya1ff) C (URL_TO_INSERT_RECORD_10011 https://fairsharing.org/FAIRsharing.md3e78) 00001000001</PRIMA (URL_TO_INSERT_RECORD_10010 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_10007 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
                <SUBMITTER_ID namespace="EBI">DAC (URL_TO_INSERT_RECORD_10012 https://fairsharing.org/FAIRsharing.md3e78) _-2011-08-26T12:23:49Z-1868</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_10013 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_10014 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_10015 https://fairsharing.org/FAIRsharing.vajn3f) >
        </DAC (URL_TO_INSERT_RECORD_10016 https://fairsharing.org/FAIRsharing.md3e78) _REF>
        <PO (URL_TO_INSERT_RECORD_10018 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_10017 https://fairsharing.org/search?fairsharingRegistry=Policy) _FILE>https://www.sanger.ac.uk/datasharing/</POLICY_FILE>
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
    </PO (URL_TO_INSERT_RECORD_10020 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_10019 https://fairsharing.org/search?fairsharingRegistry=Policy) >
</PO (URL_TO_INSERT_RECORD_10022 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_10021 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
```


```{note}
When using the consent code DUO (URL_TO_INSERT_RECORD_10026 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_10028 https://fairsharing.org/FAIRsharing.mjnypw) _0000007 where data is restricted for use on a specific disease area, it is necessary to explicitly indicate which disease area is allowed. This can be done by associating codes/identifier (URL_TO_INSERT_TERM_10024 https://fairsharing.org/search?recordType=identifier_schema) s from well established disease terminologies (URL_TO_INSERT_TERM_10023 https://fairsharing.org/search?recordType=terminology_artefact)  such as MONDO (URL_TO_INSERT_RECORD_10029 https://fairsharing.org/FAIRsharing.b2979t) , DOI (URL_TO_INSERT_RECORD_10027 https://fairsharing.org/FAIRsharing.hFLKCn) D (URL_TO_INSERT_RECORD_10030 https://fairsharing.org/FAIRsharing.8b6wfq) , SNOME (URL_TO_INSERT_RECORD_10025 https://fairsharing.org/3502) D-CT.
For instance, if data reuse is restricted to research (URL_TO_INSERT_RECORD_10034 https://fairsharing.org/FAIRsharing.52b22c)  into `juvenile idiopathic arthritis`, the code should be displayed as DUO (URL_TO_INSERT_RECORD_10031 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_10032 https://fairsharing.org/FAIRsharing.mjnypw) _0000007; MONDO (URL_TO_INSERT_RECORD_10033 https://fairsharing.org/FAIRsharing.b2979t) :0011429
```



```XML
<PO (URL_TO_INSERT_RECORD_10036 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_10035 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
  <PO (URL_TO_INSERT_RECORD_10039 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_10037 https://fairsharing.org/search?fairsharingRegistry=Policy)  alias="ena-PO (URL_TO_INSERT_RECORD_10040 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_10038 https://fairsharing.org/search?fairsharingRegistry=Policy) -BABRAHAM-23-03-2017-09:47:38:853-62" center_name="BABRAHAM" accession="EGA (URL_TO_INSERT_RECORD_10041 https://fairsharing.org/FAIRsharing.mya1ff) P00001000615" broker_name="EGA (URL_TO_INSERT_RECORD_10042 https://fairsharing.org/FAIRsharing.mya1ff) ">  
    <IDENTIFIER (URL_TO_INSERT_TERM_10043 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_10044 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_10045 https://fairsharing.org/FAIRsharing.vajn3f) > 
      <PRIMA (URL_TO_INSERT_RECORD_10049 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_10046 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_10048 https://fairsharing.org/FAIRsharing.mya1ff) P00001000615</PRIMA (URL_TO_INSERT_RECORD_10050 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_10047 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
      <SUBMITTER_ID namespace="BABRAHAM">ena-PO (URL_TO_INSERT_RECORD_10052 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_10051 https://fairsharing.org/search?fairsharingRegistry=Policy) -BABRAHAM-23-03-2017-09:47:38:853-62</SUBMITTER_ID>
    </IDENTIFIER (URL_TO_INSERT_TERM_10053 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_10054 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_10055 https://fairsharing.org/FAIRsharing.vajn3f) >
    <TITLE>Data Access Agreement for PC (URL_TO_INSERT_RECORD_10056 https://fairsharing.org/FAIRsharing.5y3gdd) HiC, RNA-Seq, ChIP-Seq</TITLE>
    <DAC (URL_TO_INSERT_RECORD_10058 https://fairsharing.org/FAIRsharing.md3e78) _REF accession="EGA (URL_TO_INSERT_RECORD_10057 https://fairsharing.org/FAIRsharing.mya1ff) C (URL_TO_INSERT_RECORD_10059 https://fairsharing.org/FAIRsharing.md3e78) 00001000523">
      <IDENTIFIER (URL_TO_INSERT_TERM_10060 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_10061 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_10062 https://fairsharing.org/FAIRsharing.vajn3f) >
        <PRIMA (URL_TO_INSERT_RECORD_10066 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_10063 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_10065 https://fairsharing.org/FAIRsharing.mya1ff) C (URL_TO_INSERT_RECORD_10068 https://fairsharing.org/FAIRsharing.md3e78) 00001000523</PRIMA (URL_TO_INSERT_RECORD_10067 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_10064 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
      </IDENTIFIER (URL_TO_INSERT_TERM_10069 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_10070 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_10071 https://fairsharing.org/FAIRsharing.vajn3f) >
    </DAC (URL_TO_INSERT_RECORD_10072 https://fairsharing.org/FAIRsharing.md3e78) _REF>
    <PO (URL_TO_INSERT_RECORD_10074 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_10073 https://fairsharing.org/search?fairsharingRegistry=Policy) _FILE>ftp://ftp.ebi.ac.uk/pub/contrib/pchic/EGA_Data_Access_Request_DIL.docx</POLICY_FILE>
    <DATA_USES>
      <DATA_USE ontology (URL_TO_INSERT_TERM_10075 https://fairsharing.org/search?recordType=terminology_artefact) ="DUO (URL_TO_INSERT_RECORD_10076 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_10077 https://fairsharing.org/FAIRsharing.mjnypw) " code="0000007" version="17-07-2016">
      	<!-- disease specific research -->
        <MODIF (URL_TO_INSERT_RECORD_10078 https://fairsharing.org/FAIRsharing.esxaaq) IER>
           <DB>EFO (URL_TO_INSERT_RECORD_10079 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_10080 https://fairsharing.org/FAIRsharing.ca63ce) </DB>
           <ID>0001645</ID>
        </MODIF (URL_TO_INSERT_RECORD_10081 https://fairsharing.org/FAIRsharing.esxaaq) IER> 
        <MODIF (URL_TO_INSERT_RECORD_10082 https://fairsharing.org/FAIRsharing.esxaaq) IER>
           <DB>EFO (URL_TO_INSERT_RECORD_10083 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_10084 https://fairsharing.org/FAIRsharing.ca63ce) </DB>
           <ID>0001655</ID>
        </MODIF (URL_TO_INSERT_RECORD_10085 https://fairsharing.org/FAIRsharing.esxaaq) IER>
       </DATA_USE>
       <DATA_USE ontology (URL_TO_INSERT_TERM_10086 https://fairsharing.org/search?recordType=terminology_artefact) ="DUO (URL_TO_INSERT_RECORD_10087 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_10088 https://fairsharing.org/FAIRsharing.mjnypw) " code="0000014" version="17-07-2016"/>
       </DATA_USES>
   </PO (URL_TO_INSERT_RECORD_10090 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_10089 https://fairsharing.org/search?fairsharingRegistry=Policy) >
</PO (URL_TO_INSERT_RECORD_10092 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_10091 https://fairsharing.org/search?fairsharingRegistry=Policy) _SET>
```




https://github.com/enasequence/schema/blob/USI/src/test/resources/uk/ac/ebi/ena/sra/xml/ega_dataset/ega_dataset.xml


```XML
<DATASETS>
    <DATASET alias="EGA (URL_TO_INSERT_RECORD_10093 https://fairsharing.org/FAIRsharing.mya1ff) S000000001-sc-20110919" center_name="SC" broker_name="EGA (URL_TO_INSERT_RECORD_10094 https://fairsharing.org/FAIRsharing.mya1ff) " accession="EGA (URL_TO_INSERT_RECORD_10095 https://fairsharing.org/FAIRsharing.mya1ff) D00001000039">
        <IDENTIFIER (URL_TO_INSERT_TERM_10096 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_10097 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_10098 https://fairsharing.org/FAIRsharing.vajn3f) >
            <PRIMA (URL_TO_INSERT_RECORD_10102 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_10099 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_10101 https://fairsharing.org/FAIRsharing.mya1ff) D00001000039</PRIMA (URL_TO_INSERT_RECORD_10103 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_10100 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
            <SUBMITTER_ID namespace="SC">EGA (URL_TO_INSERT_RECORD_10104 https://fairsharing.org/FAIRsharing.mya1ff) S000000001-sc-20110919</SUBMITTER_ID>
        </IDENTIFIER (URL_TO_INSERT_TERM_10105 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_10106 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_10107 https://fairsharing.org/FAIRsharing.vajn3f) >
        <TITLE>Platelet collagen defect</TITLE>
        <RUN_REF accession="EGA (URL_TO_INSERT_RECORD_10108 https://fairsharing.org/FAIRsharing.mya1ff) R0000000001" refname="RUN_1" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_10109 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_10110 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_10111 https://fairsharing.org/FAIRsharing.vajn3f) >
                <PRIMA (URL_TO_INSERT_RECORD_10115 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_10112 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_10114 https://fairsharing.org/FAIRsharing.mya1ff) R0000000001</PRIMA (URL_TO_INSERT_RECORD_10116 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_10113 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
                <SUBMITTER_ID namespace="EBI">RUN_1</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_10117 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_10118 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_10119 https://fairsharing.org/FAIRsharing.vajn3f) >
        </RUN_REF>
        <PO (URL_TO_INSERT_RECORD_10122 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_10120 https://fairsharing.org/search?fairsharingRegistry=Policy) _REF accession="EGA (URL_TO_INSERT_RECORD_10123 https://fairsharing.org/FAIRsharing.mya1ff) P00000001" refname="Policy (URL_TO_INSERT_TERM_10121 https://fairsharing.org/search?fairsharingRegistry=Policy) _-2011-08-17T15:05:39Z-1888" refcenter="EBI">
            <IDENTIFIER (URL_TO_INSERT_TERM_10124 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_10125 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_10126 https://fairsharing.org/FAIRsharing.vajn3f) >
                <PRIMA (URL_TO_INSERT_RECORD_10130 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_10127 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>EGA (URL_TO_INSERT_RECORD_10129 https://fairsharing.org/FAIRsharing.mya1ff) P00001000024</PRIMA (URL_TO_INSERT_RECORD_10131 https://fairsharing.org/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD_10128 https://fairsharing.org/FAIRsharing.SnTbUa) Y_ID>
                <SUBMITTER_ID namespace="EBI">Policy (URL_TO_INSERT_TERM_10132 https://fairsharing.org/search?fairsharingRegistry=Policy) _-2011-08-17T15:05:39Z-1888</SUBMITTER_ID>
            </IDENTIFIER (URL_TO_INSERT_TERM_10133 https://fairsharing.org/search?recordType=identifier_schema) S (URL_TO_INSERT_RECORD_10134 https://fairsharing.org/FAIRsharing.cbc5c8)  (URL_TO_INSERT_RECORD_10135 https://fairsharing.org/FAIRsharing.vajn3f) >
        </PO (URL_TO_INSERT_RECORD_10137 https://fairsharing.org/FAIRsharing.3ngg40) LICY (URL_TO_INSERT_TERM_10136 https://fairsharing.org/search?fairsharingRegistry=Policy) _REF>
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
In 2015, the dedicated working group produced the following JSO (URL_TO_INSERT_RECORD_10139 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_10138 https://fairsharing.org/FAIRsharing.5bbab9)  schema implementation guidance
https://www.w3.org/community/odrl/json/2.1/#section-Schema

We base our representations on this specification {footcite}`ODR (URL_TO_INSERT_RECORD_10142 https://fairsharing.org/FAIRsharing.1sfhp3) LJSO (URL_TO_INSERT_RECORD_10141 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_10140 https://fairsharing.org/FAIRsharing.5bbab9) `. 

We are aware of a possible misalignment between the specifications of the Working Group (from 2015) and the latest
specifications as to whether to use the keys "name" or "leftOperand" (https://www.w3.org/TR/odrl-model/#constraint-rule, 2018).
In the following representations, we use the key "name" to validate against the 2015 JSO (URL_TO_INSERT_RECORD_10144 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_10143 https://fairsharing.org/FAIRsharing.5bbab9) -schema
 https://www.w3.org/community/odrl/json/2.1/#section-Schema / https://github.com (URL_TO_INSERT_RECORD_10145 https://fairsharing.org/FAIRsharing.c55d5e) /iptc/rightsml-dev/blob/master/licensed/ODRL21.json

```

#### The different types of Policies

The ODRL model defines several subclasses for the **Policy** entity, namely  **Agreement**, **Set**, **Offer**.

##### Describing an agreement with ODRL

```json
{
    "policy (URL_TO_INSERT_TERM_10146 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Agreement",
    "policy (URL_TO_INSERT_TERM_10147 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "http://example.com/policy:5531",
    "inheritallowed": true,
    "permissions": [{
        "target": "http://example.com/report:2321",
        "action": "http://www.w3.org/ns/odrl/2/print",
        "assigner": "http://example.com/pub:88",
        "assignee": "http://example.com/billie:888"
    }]
}
{
    "policy (URL_TO_INSERT_TERM_10148 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Agreement",
    "policy (URL_TO_INSERT_TERM_10149 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "http://example.com/policy:9999",
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
    "policy (URL_TO_INSERT_TERM_10150 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_10151 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "https://fairplus.github.io/examples/policy_122334",
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
The main limitation of the representation is that it provides no informat (URL_TO_INSERT_TERM_10152 https://fairsharing.org/search?recordType=model_and_format) ion about which diseases are vetted for research (URL_TO_INSERT_RECORD_10153 https://fairsharing.org/FAIRsharing.52b22c) .
```

The following representation is more sophisticated and includes 3 types of restrictions:

- restriction on specific disease (juvenile arthritis, to reuse the exemplar representation in EGA/SRA XML presented in section 1)
- restriction on the geographical location where the research can be conducted
- an obligation to delete the data obtained through the access agreement past a specified duration, 3 years in our example

Let's proceed stepwise.


* Representing Research Restriction on Specific Disease Area using DUO and MONDO ontologies


```json
{
    "policy (URL_TO_INSERT_TERM_10154 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_10155 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "https://fairplus.github.io/examples/policy_122334",
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
While DUO (URL_TO_INSERT_RECORD_10157 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_10158 https://fairsharing.org/FAIRsharing.mjnypw)  is unique in its coverage of data uses, various disease ontologies (URL_TO_INSERT_TERM_10156 https://fairsharing.org/search?recordType=terminology_artefact)  exist and may be used to specify the
specific focus research (URL_TO_INSERT_RECORD_10159 https://fairsharing.org/FAIRsharing.52b22c)  should have.
For instance, SNOME (URL_TO_INSERT_RECORD_10161 https://fairsharing.org/3502) D-CT, Disease Ontology (URL_TO_INSERT_TERM_10160 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_10162 https://fairsharing.org/FAIRsharing.8b6wfq)  could also be used.
It is worth noting that extensive cross referencing exists between resources such as DOI (URL_TO_INSERT_RECORD_10163 https://fairsharing.org/FAIRsharing.hFLKCn) D (URL_TO_INSERT_RECORD_10165 https://fairsharing.org/FAIRsharing.8b6wfq) , MONDO (URL_TO_INSERT_RECORD_10164 https://fairsharing.org/FAIRsharing.b2979t)  and
SNOME (URL_TO_INSERT_RECORD_10166 https://fairsharing.org/3502) D-CT but this is something to consider when implementing brokering systems.
```



* Representing Research Restriction based on Geographical Regions

The section shows how to use ODRL to document geographical restrictions, either by listing countries where research is 
allowed or by listing those countries excluded from doing so.

In the following example, research is only allowed in a specific country, **Italy** in this case, which is 
encoded using the **ISO-3166 code**.


```json
{
    "policy (URL_TO_INSERT_TERM_10167 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_10168 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "https://fairplus.github.io/examples/policy_122334",
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
    "policy (URL_TO_INSERT_TERM_10169 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_10170 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "https://fairplus.github.io/examples/policy_122334",
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

This ODR (URL_TO_INSERT_RECORD_10172 https://fairsharing.org/FAIRsharing.1sfhp3) L representation is **not vetted, nor endorsed by GA4GH or EGA (URL_TO_INSERT_RECORD_10171 https://fairsharing.org/FAIRsharing.mya1ff) **.
This example is currently meant to present an example of how to use ODR (URL_TO_INSERT_RECORD_10175 https://fairsharing.org/FAIRsharing.1sfhp3) L to represent some of the informat (URL_TO_INSERT_TERM_10173 https://fairsharing.org/search?recordType=model_and_format) ion represented in EGA (URL_TO_INSERT_RECORD_10174 https://fairsharing.org/FAIRsharing.mya1ff) .

```

```json
{
    "policy (URL_TO_INSERT_TERM_10176 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_10177 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "https://ega-archive.org (URL_TO_INSERT_RECORD_10178 https://fairsharing.org/FAIRsharing.mya1ff) /datasets/EGAP0000000XYZ",
    "permissions": [
        {
            "target": "https://ega-archive.org (URL_TO_INSERT_RECORD_10179 https://fairsharing.org/FAIRsharing.mya1ff) /datasets/EGAD0000000YYY",
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
            "assigner": "https://ega-archive.org (URL_TO_INSERT_RECORD_10180 https://fairsharing.org/FAIRsharing.mya1ff) /",
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
                "target": "https://ega-archive.org (URL_TO_INSERT_RECORD_10181 https://fairsharing.org/FAIRsharing.mya1ff) /datasets/EGAD0000000YYY",
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
    "policy (URL_TO_INSERT_TERM_10182 https://fairsharing.org/search?fairsharingRegistry=Policy) type": "http://www.w3.org/ns/odrl/2/Policy",
    "policy (URL_TO_INSERT_TERM_10183 https://fairsharing.org/search?fairsharingRegistry=Policy) id": "http://example.com/policy:0099",
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

<#daa-policy (URL_TO_INSERT_TERM_10184 https://fairsharing.org/search?fairsharingRegistry=Policy) -1>
 a odrl:Policy (URL_TO_INSERT_TERM_10185 https://fairsharing.org/search?fairsharingRegistry=Policy)  .

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
  odrl:hasPolicy (URL_TO_INSERT_TERM_10186 https://fairsharing.org/search?fairsharingRegistry=Policy)  <#daa-policy (URL_TO_INSERT_TERM_10187 https://fairsharing.org/search?fairsharingRegistry=Policy) -1>;
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

