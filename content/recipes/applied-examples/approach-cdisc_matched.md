(fcb-approach-cdisc (URL_TO_INSERT_RECORD_15 https://fairsharing.org/3525) )=
# Mapping of clinical trial data to CDISC-SDTM: a practical example based on APPROACH and ABIRISK




````{panels_fairplus}
:identifier_text: FCB078
:identifier_link: 'https://w3id.org/faircookbook/FCB078'
:difficulty_level: 3
:recipe_type: applied_example
:reading_time_minutes: 20
:intended_audience: principal_investigator, data_manager, data_scientist, terminology_manager, ontologist
:maturity_level: 3  
:maturity_indicator: 19, 22
:has_executable_code: nope
:recipe_name: Mapping datasets to CDISC-SDTM standard
```` 


## Main Objectives

This recipe provides a general guide for map (URL_TO_INSERT_RECORD_18 https://fairsharing.org/FAIRsharing.53edcc) ping a clinical trial dataset to [CDISC Study Data Tabulated Model](https://doi.org/10.25504/FAIRsharing.s51qk5) (CDISC (URL_TO_INSERT_RECORD_19 https://fairsharing.org/3525) -SDTM) using practical examples from two Innovative Medicine Initiative project (URL_TO_INSERT_TERM_16 https://fairsharing.org/search?recordType=project) s, APPROACH and ABIRIS (URL_TO_INSERT_RECORD_17 https://fairsharing.org/FAIRsharing.e20b79) K.

The recipe will cover the following elements:

> * Provide a general overview of the challenges of map (URL_TO_INSERT_RECORD_23 https://fairsharing.org/FAIRsharing.53edcc) ping a non-conforming data dictionary to CDI (URL_TO_INSERT_RECORD_21 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_24 https://fairsharing.org/3525)  STDM standard (URL_TO_INSERT_TERM_20 https://fairsharing.org/search?fairsharingRegistry=Standard)  and CDI (URL_TO_INSERT_RECORD_22 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_25 https://fairsharing.org/3525)  Vocabulary.
>
> * Illustrate the map (URL_TO_INSERT_RECORD_27 https://fairsharing.org/FAIRsharing.53edcc) ping process using the above project (URL_TO_INSERT_TERM_26 https://fairsharing.org/search?recordType=project) s.
>
> * Describe the Extract-Transform-Load (ETL) processes necessary to convert the data to CDI (URL_TO_INSERT_RECORD_28 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_31 https://fairsharing.org/3525) -SDTM based on the map (URL_TO_INSERT_RECORD_29 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_30 https://fairsharing.org/FAIRsharing.31385c)  data dictionary.

---


## Graphical Overview

````{dropdown}
:open:
```{figure} approach-cdisc.md-figure0.mmd.png
---
name: approach-cdisc (URL_TO_INSERT_RECORD_32 https://fairsharing.org/3525) -figure0
height: 1000 px
alt: Recipe Steps
---
Recipe Steps
```
````


---


## Requirements

* Technical requirements:
   * Knowledge of relational database (URL_TO_INSERT_TERM_33 https://fairsharing.org/search?fairsharingRegistry=Database) s is an advantage
   * Fluency in a scripting language such as bash, Python or R
* Knowledge requirement:
   * A thorough understanding of CDI (URL_TO_INSERT_RECORD_35 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_37 https://fairsharing.org/3525)  standard (URL_TO_INSERT_TERM_34 https://fairsharing.org/search?fairsharingRegistry=Standard) s, in particular CDI (URL_TO_INSERT_RECORD_36 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_38 https://fairsharing.org/3525) -SDTM, is essential
   * understanding of what a  [data dictionary](../interoperability/creating-data-dictionary.md) is.
   

---

<!--## FAIRification Objectives, Inputs and Outputs


| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [text annotation](http://edamontology.org/operation_3778)  | local data dictionary  | [annotated text](http://edamontology.org/data_3779)  |-->


## Table of Data Standards


| Data Format (URL_TO_INSERT_TERM_40 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_41 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_39 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
| [CDISC-SDTM](https://www.cdisc.org/standards/foundational/sdtm)  |  [CDISC (URL_TO_INSERT_RECORD_42 https://fairsharing.org/3525)  terminology](https://www.cdisc.org/standards/terminology/controlled-terminology) | |
| [CDISC-SDTM v2](https://www.cdisc.org/standards/foundational/sdtm/sdtm-v2-0)| | |
| [CDISC-SDTMIG 3.4](https://www.cdisc.org/standards/foundational/sdtmig/sdtmig-v3-4)| | |
---

## General challenges of mapping to CDISC-SDTM

[CDISC-SDTM](https://www.cdisc.org/standards/foundational/sdtm) is a standard (URL_TO_INSERT_TERM_43 https://fairsharing.org/search?fairsharingRegistry=Standard)  model (URL_TO_INSERT_TERM_44 https://fairsharing.org/search?recordType=model_and_format)  and framework for organising, 
annotating and format (URL_TO_INSERT_TERM_45 https://fairsharing.org/search?recordType=model_and_format) ting data from clinical trials {footcite}`sdtm`. Regulator (URL_TO_INSERT_RECORD_46 https://fairsharing.org/FAIRsharing.ey49c6) y agencies, such as the
[US FDA](https://www.fda.gov/media/122970/download), require clinical trial results to be submitted in this format (URL_TO_INSERT_TERM_47 https://fairsharing.org/search?recordType=model_and_format) . 
While SDTM is a very complex framework with a high learning curve, its ubiquity in the field of clinical trials makes 
it a useful interoperability tool for comparing and combining datasets. 
The SDTM Implementation Guide ([SDTMIG](https://www.cdisc.org/standards/foundational/sdtmig)) provides expanded guidance
on implementing SDTM for specific use cases or "domains" {footcite}`sdtm_v2`. A general introduction to the SDTMIG is available 
[on the CDISC website](https://www.cdisc.org/standards/foundational/sdtmig/primer) {footcite}`sdtmig_v3_4`.

```{warning}
Given the complexity of CDISC standards, any project team intending conversion of their datasets to SDTM at any point 
in the project life cycle should aim to align with the standard **as early on in the process as possible**. 

Data dictionaries and data collection instruments should, where possible, be aligned to the relevant CDISC standards to
facilitate data conversions later on. In particular, CDISC standards provide procedures and guidelines for encoding 
project-specific data that might not fit into the existing domains.
```

```{note}
Commercial solutions are available to address all of these use cases but these are outside the scope of this recipe. 

We will focus on outlining how to perform the mapping process manually, without bespoke tooling.
```


## Step-by-step process

### Initial review of the data dictionary & identification of relevant domains

Before any map (URL_TO_INSERT_RECORD_49 https://fairsharing.org/FAIRsharing.53edcc) ping can take place, it is essential to gain a good understanding of the project (URL_TO_INSERT_TERM_48 https://fairsharing.org/search?recordType=project) 's data dictionary, i.e. 
its list of variables, their types, definitions and domains. 

A good data dictionary will already split properties into domains, for example: by data collection (URL_TO_INSERT_TERM_50 https://fairsharing.org/search?recordType=collection)  instrument or other data source. 

Guidance for creating a data dictionary is available [elsewhere in this Cookbook](../interoperability/creating-data-dictionary.md).

This step may also include reviewing actual data to refine contexts.
 
Once a good understanding of the data dictionary has been gained, the main domains from the SDTMIG that apply to this
data need to be identified. Common domains that will occur in most clinical trial datasets include Demographics (DM), 
Medical History (MH), Laboratory Test Results (LB), Adverse Events (AE) and Vital Signs (VS).

* The ABIRIS (URL_TO_INSERT_RECORD_51 https://fairsharing.org/FAIRsharing.e20b79) K data dictionary already used a similar setup to CDI (URL_TO_INSERT_RECORD_52 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_53 https://fairsharing.org/3525) -SDTM, which made this step relatively straight-forward. 
* The APPROACH data dictionary on the other hand used categories that, while providing a clear structure to the data, 
did not align directly with SDTMIG domains. This made the identification of appropriate domains more difficult and the
initial list had to be revised several times during the variable map (URL_TO_INSERT_RECORD_54 https://fairsharing.org/FAIRsharing.53edcc) ping process, when variables were identified that 
didn't fit within the primary domain matched to a data dictionary category.  


### Assignment of properties to domains and mapping to SDTMIG variables

Map (URL_TO_INSERT_RECORD_55 https://fairsharing.org/FAIRsharing.53edcc) ping of data dictionary properties to SDTMIG variables falls into several categories:

* Direct match - a property from the data dictionary directly matches a variable in the SDTMIG.
* Combination - two or more properties from the data dictionary need be combined into a single SDTM variable. As an example, sample collection (URL_TO_INSERT_TERM_56 https://fairsharing.org/search?recordType=collection)  times in the APPROACH dataset were recorded as separate variables for year, month, day, hour and minute. In SDTM, these were combined into LB.LBDTC.
* Splitting - a property from the dataset needs to be split into component parts. This is commonly the case if values and units were captured together in the same field.
* Derivation - some values might be derived from another value, for example using a logical decision tree "if A=x, then value=y" or transformed, e.g. converting a laboratory result reported in non-standard (URL_TO_INSERT_TERM_57 https://fairsharing.org/search?fairsharingRegistry=Standard)  units into standard (URL_TO_INSERT_TERM_58 https://fairsharing.org/search?fairsharingRegistry=Standard)  units.
* Fixed value - an implicit field in the original dataset may correspond to a fixed value for an SDTMIG variable. In the APPROACH dataset, the demographics property "Age" has the unit "years" implied in the property description as the inclusion criteria for the trial specify adult subjects only. DM.AGEU is a required value so in this particular conversion, "YEARS" is set a fixed value.
* One-to-many/many-to-one - In some cases, a single property might map (URL_TO_INSERT_RECORD_59 https://fairsharing.org/FAIRsharing.53edcc)  to multiple SDTMIG variables, depending on the corresponding value in the dataset. Equally, multiple properties may map (URL_TO_INSERT_RECORD_60 https://fairsharing.org/FAIRsharing.53edcc)  to the same SDTMIG variable. 
* Unmap (URL_TO_INSERT_RECORD_62 https://fairsharing.org/FAIRsharing.53edcc) pable properties - some project (URL_TO_INSERT_TERM_61 https://fairsharing.org/search?recordType=project) -specific properties may not have an equivalent SDTMIG variable at all. If the property and its values are important for the interpretation of the dataset overall, this scenario may require the creation of a custom domain. Equally however, some properties may simply be out of scope of SDTM. The APPROACH data dictionary contains a number of such properties, including checks whether a given CRF (URL_TO_INSERT_RECORD_63 https://fairsharing.org/FAIRsharing.1ece03) , examination or questionnaire was completed or sample collected, and properties to identify the coder or analyst. 
* Auto-generated - some SDTM variables such as "STUDYID" or sequence ID ("-SEQ") will likely not be encoded directly in the dataset and need to be autogenerated or autocompleted during the data transformat (URL_TO_INSERT_TERM_64 https://fairsharing.org/search?recordType=model_and_format) ion process.


### Putting together an ETL template

For most of the scenarios listed above, with the exception of direct one-to-one matches, ETL scripts will need to be implemented in order to convert the data into an SDTM-compliant format (URL_TO_INSERT_TERM_65 https://fairsharing.org/search?recordType=model_and_format) . As the implementation of scripts was outside the scope of our map (URL_TO_INSERT_RECORD_66 https://fairsharing.org/FAIRsharing.53edcc) ping work, we instead implemented a template that could be used as a basis to generate the scripts. A copy of our template can be downloaded from [this URL](https://webdav-r3lab.uni.lu/public/datacatalog_documents//dataset/df780ac2-c79d-11ec-9b1d-acde48001122/APPROACH_CDISC-SDTM_mappings.xlsx).

A recipe on ETL processes is available [elswhere in this resource](../interoperability/ETL-tools.md)


### Issues, pitfalls and caveats

One major issue that we encountered with both our map (URL_TO_INSERT_RECORD_68 https://fairsharing.org/FAIRsharing.53edcc) ping project (URL_TO_INSERT_TERM_67 https://fairsharing.org/search?recordType=project) s was trial/study data coverage gaps from the respective
study data dictionaries. 
The SDTM includes an entire area called the "Trial Design Model (URL_TO_INSERT_TERM_69 https://fairsharing.org/search?recordType=model_and_format) ", which provides a structured way of representing all 
activities of a clinical trial, such as planned visits, treatment arms and inclusion and exclusion criteria. 
While this informat (URL_TO_INSERT_TERM_70 https://fairsharing.org/search?recordType=model_and_format) ion is a key component of a completely SDTM-compliant dataset, it was not part of the data dictionary
and was therefore not part of the map (URL_TO_INSERT_RECORD_71 https://fairsharing.org/FAIRsharing.53edcc) ping strategy. 
As a result, any ETL process covering the data alone would not have generated a fully SDTM-compliant dataset.
Another area of the SDTMIG we did not include in our map (URL_TO_INSERT_RECORD_72 https://fairsharing.org/FAIRsharing.53edcc) pings was the representation of relationships in the data,
such as those between different records for a given subject (RELREC domain).
These relationships need to be factored into any ETL procedures but require additional documents, distinct from the
Data Dictionary *stricto-sensu* and these relations cannot only be established working from a data dictionary,
which only lists variables. 
In order to build those links, actual subject, specimen and visit informat (URL_TO_INSERT_TERM_73 https://fairsharing.org/search?recordType=model_and_format) ion is needed. This informat (URL_TO_INSERT_TERM_74 https://fairsharing.org/search?recordType=model_and_format) ion is specified 
in the SDTM syntax itself, which is outside the scope of this specific document.


---

## Conclusion

* We presented an overview of our approach to map (URL_TO_INSERT_RECORD_77 https://fairsharing.org/FAIRsharing.53edcc) ping project (URL_TO_INSERT_TERM_75 https://fairsharing.org/search?recordType=project) -specific data dictionaries to the CDI (URL_TO_INSERT_RECORD_76 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_78 https://fairsharing.org/3525) -SDTMIG with a view to transforming the corresponding datasets to be SDTM-compliant.
* The CDI (URL_TO_INSERT_RECORD_82 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_83 https://fairsharing.org/3525) -SDTM standard (URL_TO_INSERT_TERM_79 https://fairsharing.org/search?fairsharingRegistry=Standard)  supports the interoperability between datasets due to its high level of standard (URL_TO_INSERT_TERM_80 https://fairsharing.org/search?fairsharingRegistry=Standard) isation, detailed model (URL_TO_INSERT_TERM_81 https://fairsharing.org/search?recordType=model_and_format) ling and widespread use.
* The high level of detailed knowledge of the standard (URL_TO_INSERT_TERM_84 https://fairsharing.org/search?fairsharingRegistry=Standard)  required to successfully convert a dataset to SDTM presents a significant hurdl (URL_TO_INSERT_RECORD_85 https://fairsharing.org/FAIRsharing.vm4688) e 

### What to read next?
* [Ontology mappings](../interoperability/selecting-ontologies.md)
* [Data dictionary](../interoperability/creating-data-dictionary.md)
* [ETL processes](../interoperability/ETL-tools.md)

````{rdmkit_panel}
````

## References

````{dropdown} **References**
```{footbibliography}
```
````



## Authors


````{authors_fairplus}
Danielle: Writing - Original Draft
Philippe:  Writing - Review & Editing
````


## License
````{license_fairplus}
CC-BY-4.0
````

