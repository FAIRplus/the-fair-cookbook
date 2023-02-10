(fcb-dats-model (URL_TO_INSERT_TERM_1699 https://fairsharing.org/search?recordType=model_and_format) )=
# Introducing the DATS model


<br/>
<br/>

````{panels_fairplus}
:identifier_text: FCB082
:identifier_link: 'https://w3id.org/faircookbook/FCB082'
:difficulty_level: 2
:recipe_type: background_information
:reading_time_minutes: 15
:intended_audience: data_manager, data_curator, software_developer
:maturity_level: 2  
:maturity_indicator: 15
:has_executable_code: nope
:recipe_name: Introducing the DATS model
```` 


## Main Objectives

The main purpose of this recipe is:

>* Provide a general introduction to the Data Tag Suite (URL_TO_INSERT_RECORD-NAME_1702 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_1701 https://fairsharing.org/search?recordType=model_and_format)  for representing project (URL_TO_INSERT_TERM_1700 https://fairsharing.org/search?recordType=project) , study and dataset metadata
>* Highlight challenges in implementing the model (URL_TO_INSERT_TERM_1703 https://fairsharing.org/search?recordType=model_and_format)  in a data catalogue

---


## Graphical Overview

````{dropdown} **Data Model**
:open:
```{figure} DataModelDiagram.png
---
width: 800px
name: data-model (URL_TO_INSERT_TERM_1704 https://fairsharing.org/search?recordType=model_and_format) -diagram
alt: Data Model (URL_TO_INSERT_TERM_1705 https://fairsharing.org/search?recordType=model_and_format)  Diagram
---
Data Model (URL_TO_INSERT_TERM_1706 https://fairsharing.org/search?recordType=model_and_format)  Diagram
```
````

---


## Table of Data Standards


| Data Format (URL_TO_INSERT_TERM_1708 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_1709 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_1707 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
| [JSON-LD](https://json-ld.org/) | [OBO Foundry (URL_TO_INSERT_RECORD-NAME_1710 https://fairsharing.org/FAIRsharing.847069) ](https://obofoundry.org/) | [DATS](https://datatagsuite.github.io/docs/html/dats.html) |
| |  | [DCAT](https://www.w3.org/TR/vocab-dcat-2/) |
| |  | [SDO](https://schema.org/) |

---

## Model overview

Data Tag Suits (DATS (URL_TO_INSERT_RECORD-ABBREV_1715 https://fairsharing.org/FAIRsharing.e20vsd) ) {footcite}`pmid28585923` is a data description model (URL_TO_INSERT_TERM_1714 https://fairsharing.org/search?recordType=model_and_format)  designed and produced to describe datasets being ingested in DataMed (URL_TO_INSERT_RECORD-NAME_1718 https://fairsharing.org/FAIRsharing.v5q4zc) , a prototype for data discovery developed as part of the bioCADDIE (URL_TO_INSERT_RECORD-NAME_1717 https://fairsharing.org/3506)  project (URL_TO_INSERT_TERM_1711 https://fairsharing.org/search?recordType=project)  {footcite}`pmid28546571`. DATS (URL_TO_INSERT_RECORD-ABBREV_1716 https://fairsharing.org/FAIRsharing.e20vsd)  was co-developed by the Oxford e-Research Centre and the NIH Data Common Big Data to Knowledge (BD2K) initiative, where it was used to uniformly represent metadata across a number of project (URL_TO_INSERT_TERM_1712 https://fairsharing.org/search?recordType=project) s, including the Genotype-Tissue Expression project (URL_TO_INSERT_TERM_1713 https://fairsharing.org/search?recordType=project)  (GTEx) and Trans-Omics for Precision Medicine (TOPMed).

DATS (URL_TO_INSERT_RECORD-ABBREV_1724 https://fairsharing.org/FAIRsharing.e20vsd)  is semantically compatible with the Data Catalog Vocabulary (URL_TO_INSERT_RECORD-NAME_1719 https://fairsharing.org/FAIRsharing.h4j3qm)  (DCAT (URL_TO_INSERT_RECORD-ABBREV_1720 https://fairsharing.org/FAIRsharing.h4j3qm) ), a Resource Description Framework (URL_TO_INSERT_RECORD-NAME_1722 https://fairsharing.org/FAIRsharing.p77ph9)  (RDF (URL_TO_INSERT_RECORD-ABBREV_1723 https://fairsharing.org/FAIRsharing.p77ph9) ) vocabulary designed to facilitate interoperability among data catalogues published on the web, as well as schema.org (URL_TO_INSERT_RECORD-NAME_1726 https://fairsharing.org/FAIRsharing.hzdzq8)  (SDO (URL_TO_INSERT_RECORD-ABBREV_1725 https://fairsharing.org/FAIRsharing.7s74s8) ), which is a community-driven effort with a similar interoperability goal to DCAT (URL_TO_INSERT_RECORD-ABBREV_1721 https://fairsharing.org/FAIRsharing.h4j3qm)  but a more general-purpose scope.

The original DATS (URL_TO_INSERT_RECORD-ABBREV_1736 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_1729 https://fairsharing.org/search?recordType=model_and_format)  centered around concept of a "Dataset", an entity that covers technical aspects such as licensing, data types and distributions. The Dataset is produced by or is the input or output of a “Study”, which contains elements that are specific to life, environmental and biomedical science domains, and which model (URL_TO_INSERT_TERM_1730 https://fairsharing.org/search?recordType=model_and_format) s experimental processes, cohorts and protocol informat (URL_TO_INSERT_TERM_1732 https://fairsharing.org/search?recordType=model_and_format) ion. To meet the requirements of project (URL_TO_INSERT_TERM_1727 https://fairsharing.org/search?recordType=project) -generated datasets, the DATS (URL_TO_INSERT_RECORD-ABBREV_1737 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_1731 https://fairsharing.org/search?recordType=model_and_format)  was extended to include the third core (URL_TO_INSERT_RECORD-NAME_1734 https://fairsharing.org/FAIRsharing.xMmOCL)  (URL_TO_INSERT_RECORD-ABBREV_1735 https://fairsharing.org/FAIRsharing.m283c)  concept of “Project (URL_TO_INSERT_TERM_1728 https://fairsharing.org/search?recordType=project) ”, covering general informat (URL_TO_INSERT_TERM_1733 https://fairsharing.org/search?recordType=model_and_format) ion such as title, publications, funding and contributors.


### Core objects

The DATS (URL_TO_INSERT_RECORD-ABBREV_1743 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_1740 https://fairsharing.org/search?recordType=model_and_format)  centres around three core (URL_TO_INSERT_RECORD-NAME_1741 https://fairsharing.org/FAIRsharing.xMmOCL)  (URL_TO_INSERT_RECORD-ABBREV_1742 https://fairsharing.org/FAIRsharing.m283c)  objects, "Project (URL_TO_INSERT_TERM_1738 https://fairsharing.org/search?recordType=project) ", "Study" and "Dataset", each of which contains a set of sub-objects, which in turn can be nested down to the lowest unitary object (which contains no further objects), which is the “Annotation”. Project (URL_TO_INSERT_TERM_1739 https://fairsharing.org/search?recordType=project) , Study and Dataset relate to each other in a triangular fashion as shown in figure 1.

At first glance, the three core (URL_TO_INSERT_RECORD-NAME_1751 https://fairsharing.org/FAIRsharing.xMmOCL)  (URL_TO_INSERT_RECORD-ABBREV_1752 https://fairsharing.org/FAIRsharing.m283c)  objects make the DATS (URL_TO_INSERT_RECORD-ABBREV_1753 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_1745 https://fairsharing.org/search?recordType=model_and_format)  reminiscent of the ISA (Investigation, Study, Assay) model (URL_TO_INSERT_TERM_1746 https://fairsharing.org/search?recordType=model_and_format)  for describing experimental processes. There are however several key differences between the two. For one, ISA has a waterfall structure whereby any instance of the model (URL_TO_INSERT_TERM_1747 https://fairsharing.org/search?recordType=model_and_format)  has to contain a Study object between an Investigation and an Assay. In DATS (URL_TO_INSERT_RECORD-ABBREV_1754 https://fairsharing.org/FAIRsharing.e20vsd)  on the other hand, it is possible for a Dataset to be directly dependent on a Project (URL_TO_INSERT_TERM_1744 https://fairsharing.org/search?recordType=project) , without any Study informat (URL_TO_INSERT_TERM_1749 https://fairsharing.org/search?recordType=model_and_format) ion. This is relevant for datasets such as knowledge graphs or synthetic datasets, for which no study metadata may be available. Additionally, DATS (URL_TO_INSERT_RECORD-ABBREV_1755 https://fairsharing.org/FAIRsharing.e20vsd)  focuses on the technical details, availability and use restrictions of datasets whereas the purpose of the ISA model (URL_TO_INSERT_TERM_1748 https://fairsharing.org/search?recordType=model_and_format)  is to describe experimental procedures in great detail. While the DATS (URL_TO_INSERT_RECORD-ABBREV_1756 https://fairsharing.org/FAIRsharing.e20vsd)  Study covers some of this informat (URL_TO_INSERT_TERM_1750 https://fairsharing.org/search?recordType=model_and_format) ion, it is much less comprehensive or central to the captured data than for ISA.

#### Project

The Project (URL_TO_INSERT_TERM_1757 https://fairsharing.org/search?recordType=project)  object was not part of the original version of DATS (URL_TO_INSERT_RECORD-ABBREV_1762 https://fairsharing.org/FAIRsharing.e20vsd) . It was added in the second version as a means of linking different studies and datasets under one common parent as well as capturing informat (URL_TO_INSERT_TERM_1760 https://fairsharing.org/search?recordType=model_and_format) ion such as project (URL_TO_INSERT_TERM_1758 https://fairsharing.org/search?recordType=project)  contacts or consortium informat (URL_TO_INSERT_TERM_1761 https://fairsharing.org/search?recordType=model_and_format) ion, publications not linked to one specific study, funding sources, project (URL_TO_INSERT_TERM_1759 https://fairsharing.org/search?recordType=project)  websites and start/end dates.

#### Study

The Study object, although part of the original DATS (URL_TO_INSERT_RECORD-ABBREV_1765 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_1763 https://fairsharing.org/search?recordType=model_and_format) , had a less central role in the first iteration than it has in this latest one. Capturing the context in which the Dataset was either generated or used, the Study provides informat (URL_TO_INSERT_TERM_1764 https://fairsharing.org/search?recordType=model_and_format) ion about the type of study undertaken (e.g. clinical trials or chemical toxicity screens), cohorts (or "studyGroups), input materials, selection criteria and the steps involved in the study. 

#### Dataset

The Dataset object was the central concept of the initial DATS (URL_TO_INSERT_RECORD-ABBREV_1773 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_1768 https://fairsharing.org/search?recordType=model_and_format)  but became an equal part in the `Project (URL_TO_INSERT_TERM_1767 https://fairsharing.org/search?recordType=project) -Study-Dataset` triangle in version 2. The object captures technical informat (URL_TO_INSERT_TERM_1770 https://fairsharing.org/search?recordType=model_and_format) ion about the dataset, such as file types, data standard (URL_TO_INSERT_TERM_1766 https://fairsharing.org/search?fairsharingRegistry=Standard) s, versions and licensing as well as links to the actual data if available. It also model (URL_TO_INSERT_TERM_1769 https://fairsharing.org/search?recordType=model_and_format) s informat (URL_TO_INSERT_TERM_1771 https://fairsharing.org/search?recordType=model_and_format) ion related to the creation of the dataset such as input materials, diseases, biological entities and other similar objects, as well as the types of experiments from which the dataset was derived and any associated dimensions (URL_TO_INSERT_RECORD-NAME_1772 https://fairsharing.org/FAIRsharing.9af33c)  or components.

### Sub-objects

Each of the three top-level objects references a range of sub-objects, which in turn contain further sub-objects, down to the lowest unitary object (which contains no further objects), which is the “Annotation”. An “Annotation” consists of just two key-value pairs, the “value” and, optionally, the “valueIRI”, designed to capture the Internationalized Resource Identifier (URL_TO_INSERT_TERM_1775 https://fairsharing.org/search?recordType=identifier_schema)  (IRI) of an ontology (URL_TO_INSERT_TERM_1774 https://fairsharing.org/search?recordType=terminology_artefact)  term contextualising the free text “value”. Due to this nested object structure, DATS (URL_TO_INSERT_RECORD-ABBREV_1776 https://fairsharing.org/FAIRsharing.e20vsd)  can be quite opaque to parse for the human reader but allows for easier programmatic processing of the objects. A full overview of the DATS (URL_TO_INSERT_RECORD-ABBREV_1777 https://fairsharing.org/FAIRsharing.e20vsd)  schema can be found on the [DataTagSuite Github repository](https://github.com/datatagsuite/schema).

### Ontology annotations

The provision for ontology (URL_TO_INSERT_TERM_1781 https://fairsharing.org/search?recordType=terminology_artefact)  annotations is at the core (URL_TO_INSERT_RECORD-NAME_1784 https://fairsharing.org/FAIRsharing.xMmOCL)  (URL_TO_INSERT_RECORD-ABBREV_1785 https://fairsharing.org/FAIRsharing.m283c)  of the DATS (URL_TO_INSERT_RECORD-ABBREV_1786 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_1778 https://fairsharing.org/search?recordType=model_and_format) , with the smallest object available in the model (URL_TO_INSERT_TERM_1779 https://fairsharing.org/search?recordType=model_and_format)  being the `Annotation` schema, which simply consists of two key-value pairs: `value`, which can contain a text string (URL_TO_INSERT_RECORD-NAME_1787 https://fairsharing.org/FAIRsharing.9b7wvk)  or number (to allow for coded values), and `valueIRI`, which contains a URI (URL_TO_INSERT_RECORD-ABBREV_1783 https://fairsharing.org/FAIRsharing.d261e1) -format (URL_TO_INSERT_TERM_1780 https://fairsharing.org/search?recordType=model_and_format) ted string (URL_TO_INSERT_RECORD-NAME_1788 https://fairsharing.org/FAIRsharing.9b7wvk)  representing a concept or ontology (URL_TO_INSERT_TERM_1782 https://fairsharing.org/search?recordType=terminology_artefact)  term associated with the value. It should be noted that the Annotation object has no required properties, so the valueIRI in particular can be empty. 

The model (URL_TO_INSERT_TERM_1789 https://fairsharing.org/search?recordType=model_and_format)  also provides an extension mechanism through a schema object called `CategoryValuesPair`. This allows the addition of extra properties to the entities in cases where there are no specific properties to deal with the desired property. In order to capture the semantics of the category, CategoryValuesPairs capture both a `category` as a free-text string (URL_TO_INSERT_RECORD-NAME_1793 https://fairsharing.org/FAIRsharing.9b7wvk)  and a `categoryIRI` for the URI (URL_TO_INSERT_RECORD-ABBREV_1792 https://fairsharing.org/FAIRsharing.d261e1)  of an associated ontology (URL_TO_INSERT_TERM_1790 https://fairsharing.org/search?recordType=terminology_artefact)  context. The `values` are of type `Annotation` and can therefore also have ontology (URL_TO_INSERT_TERM_1791 https://fairsharing.org/search?recordType=terminology_artefact)  annotations.

DATS (URL_TO_INSERT_RECORD-ABBREV_1796 https://fairsharing.org/FAIRsharing.e20vsd)  does not prescribe the use of specific ontologies (URL_TO_INSERT_TERM_1795 https://fairsharing.org/search?recordType=terminology_artefact)  in relation to various properties, although it would be advisable to include this type of restriction in a given implementation of the model (URL_TO_INSERT_TERM_1794 https://fairsharing.org/search?recordType=model_and_format)  in order to simply the interoperability between different objects of the same type.

### Encoding in JSON-LD

DATS (URL_TO_INSERT_RECORD-ABBREV_1811 https://fairsharing.org/FAIRsharing.e20vsd)  objects are encoded in JSON (URL_TO_INSERT_RECORD-ABBREV_1805 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD-ABBREV_1813 https://fairsharing.org/FAIRsharing.8f9bbb) , a method for encoding linked data in the open standard (URL_TO_INSERT_TERM_1797 https://fairsharing.org/search?fairsharingRegistry=Standard)  file and data interchange format (URL_TO_INSERT_TERM_1801 https://fairsharing.org/search?recordType=model_and_format)  JSON (URL_TO_INSERT_RECORD-ABBREV_1806 https://fairsharing.org/FAIRsharing.5bbab9) . JSON (URL_TO_INSERT_RECORD-ABBREV_1807 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD-ABBREV_1814 https://fairsharing.org/FAIRsharing.8f9bbb)  is designed around the concept of a "context" to provide additional mappings from JSON (URL_TO_INSERT_RECORD-ABBREV_1808 https://fairsharing.org/FAIRsharing.5bbab9)  to an RDF (URL_TO_INSERT_RECORD-ABBREV_1809 https://fairsharing.org/FAIRsharing.p77ph9)  model (URL_TO_INSERT_TERM_1798 https://fairsharing.org/search?recordType=model_and_format) . DATS (URL_TO_INSERT_RECORD-ABBREV_1812 https://fairsharing.org/FAIRsharing.e20vsd)  provides three sets of context mappings, to DCAT (URL_TO_INSERT_RECORD-ABBREV_1803 https://fairsharing.org/FAIRsharing.h4j3qm) , schema.org (URL_TO_INSERT_RECORD-NAME_1816 https://fairsharing.org/FAIRsharing.hzdzq8)  (SDO (URL_TO_INSERT_RECORD-ABBREV_1815 https://fairsharing.org/FAIRsharing.7s74s8) ) and the OBO Foundry (URL_TO_INSERT_RECORD-NAME_1810 https://fairsharing.org/FAIRsharing.847069)  Ontologies (URL_TO_INSERT_TERM_1802 https://fairsharing.org/search?recordType=terminology_artefact) . None of the three sets of contexts individually cover all properties in the model (URL_TO_INSERT_TERM_1799 https://fairsharing.org/search?recordType=model_and_format)  but they can be used in combination to maximise the semantic linking of the model (URL_TO_INSERT_TERM_1800 https://fairsharing.org/search?recordType=model_and_format) , likely to increase interoperability, for instance with DCAT (URL_TO_INSERT_RECORD-ABBREV_1804 https://fairsharing.org/FAIRsharing.h4j3qm)  based catalogues.



## Implementing DATS in a data catalogue

We implemented DATS (URL_TO_INSERT_RECORD-ABBREV_1819 https://fairsharing.org/FAIRsharing.e20vsd)  v2.0 in the [IMI Translational Data Catalog](https://datacatalog.elixir-luxembourg.org/). The DATS (URL_TO_INSERT_RECORD-ABBREV_1820 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_1817 https://fairsharing.org/search?recordType=model_and_format) 's flexibility presents both a benefit and a challenge in that some concepts could be encoded in a number of ways. Experimental materials for example can be encoded at both the Study level, in `Study.input` or at the Dataset level, in `Dataset.isAbout`. In order to encode metadata consistently and simplify indexing and display processes for the IMI Data Catalog (URL_TO_INSERT_RECORD-ABBREV_1821 https://fairsharing.org/FAIRsharing.de533c) , we therefore made a number of assumptions about how to encode certain metadata entities in the model (URL_TO_INSERT_TERM_1818 https://fairsharing.org/search?recordType=model_and_format) .

### Assumptions

* Study and Dataset objects can't exist without a Project (URL_TO_INSERT_TERM_1822 https://fairsharing.org/search?recordType=project) . This rule was necessary to provide a root for our indexing service.

* The Study object encodes informat (URL_TO_INSERT_TERM_1823 https://fairsharing.org/search?recordType=model_and_format) ion about the input materials to the experiment, such as study subjects in the case of clinical trials or biological molecules in the case of chemical assays. At this level, we collect cohort descriptions, sample sizes, sample sources, types of samples and diseases.
 
* The Dataset object encodes informat (URL_TO_INSERT_TERM_1825 https://fairsharing.org/search?recordType=model_and_format) ion about the dataset, including technical informat (URL_TO_INSERT_TERM_1826 https://fairsharing.org/search?recordType=model_and_format) ion such as version number, creation and update dates, data standard (URL_TO_INSERT_TERM_1824 https://fairsharing.org/search?fairsharingRegistry=Standard) s and file types. The dataset also lists the experiment types that generated the data, the number and types of samples that contributed to the dataset and any diseases in the samples. These properties can be distinct from the ones at Study level as not all samples collected in a Study may be used to generate a given dataset, e.g. blood samples might be used for sequencing experiments, generating a sequencing dataset, while other tissue samples are used in imaging assays, generating an imaging dataset. The number of samples collected can be different from the cohort sample size (i.e. number of subject), either because multiple samples were collected from each subject or because some samples were excluded from the dataset for quality reasons.

* In the implementation of the model (URL_TO_INSERT_TERM_1827 https://fairsharing.org/search?recordType=model_and_format) , preference as given to specific ontologies (URL_TO_INSERT_TERM_1828 https://fairsharing.org/search?recordType=terminology_artefact)  in certain contexts, eg MONDO (URL_TO_INSERT_RECORD-ABBREV_1829 https://fairsharing.org/FAIRsharing.b2979t)  for diseases, UBERON (URL_TO_INSERT_RECORD-ABBREV_1831 https://fairsharing.org/FAIRsharing.4c0b6b)  for anatomical components, NCIt (URL_TO_INSERT_RECORD-ABBREV_1830 https://fairsharing.org/FAIRsharing.4cvwxa) , EFO (URL_TO_INSERT_RECORD-ABBREV_1834 https://fairsharing.org/FAIRsharing.1gr4tz)  and OBI (URL_TO_INSERT_RECORD-ABBREV_1833 https://fairsharing.org/FAIRsharing.284e1z)  for experiment types, UO (URL_TO_INSERT_RECORD-ABBREV_1832 https://fairsharing.org/FAIRsharing.mjnypw)  for units etc.

---

## Conclusion

> * DATS (URL_TO_INSERT_RECORD-ABBREV_1836 https://fairsharing.org/FAIRsharing.e20vsd)  is a flexible data model (URL_TO_INSERT_TERM_1835 https://fairsharing.org/search?recordType=model_and_format)  aimed at biomedical datasets.
> * DATS (URL_TO_INSERT_RECORD-ABBREV_1839 https://fairsharing.org/FAIRsharing.e20vsd)  utilises the power of JSON (URL_TO_INSERT_RECORD-ABBREV_1838 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD-ABBREV_1840 https://fairsharing.org/FAIRsharing.8f9bbb)  to encode semantics at all levels of the model (URL_TO_INSERT_TERM_1837 https://fairsharing.org/search?recordType=model_and_format) .
> * DATS (URL_TO_INSERT_RECORD-ABBREV_1842 https://fairsharing.org/FAIRsharing.e20vsd) ' flexibility does mean that consistent implementation of the model (URL_TO_INSERT_TERM_1841 https://fairsharing.org/search?recordType=model_and_format)  in a specific context requires assumptions to be made.


### What should I read next?
> * [Building a catalogue of datasets](./data-catalog.md) 
> * [Deploying the IMI data catalog](./data-catalog-deployment.md) 
> * [Introduction to terminologies and ontologies](../interoperability/introduction-terminologies-ontologies.md)

## References:

````{dropdown} **References**
```{footbibliography}
```
````

## Authors

````{authors_fairplus}
Danielle: Writing - original draft
Philippe: Writing - review & editing
````


## License
````{license_fairplus}
CC-BY-4.0
````

