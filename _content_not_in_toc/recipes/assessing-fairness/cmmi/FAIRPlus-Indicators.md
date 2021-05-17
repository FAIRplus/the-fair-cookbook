# IMI FAIRPlus Indicators

> version : v0.01

FAIRplus indicators are designed for measuring data sets compliance to Data Usage Areas. One indicator might support more than one Data Usage Area. Indicators are grouped according to the ISA framework.

![ISA](./img/isa-structure.png)

Image Reference : [Khan](https://www.researchgate.net/publication/333163209_Design_and_Development_of_a_Phenotypic_Data_Model_PDM)

## Index


| ID              | Indicators                                                   |
| --------------- | ------------------------------------------------------------ |
| [F+S01](#F+S01) | Study level documentation is available in a human readable format. |
| [F+S02](#F+S02) | Data is reported by following community specific minimum information guidelines |
| [F+S03](#F+S03) | Metadata documents and provides references about all data biological data types and formats in data is expressed. |
| [F+S04](#F+S04) | Relationships between different data sets in a study is well defined. |
| [F+S05](#F+S05)                | A versioning policy is applied to uniquely identify a particular form of a dataset from an earlier form or other forms of itself. |
| [F+S06](#F+S06)                | Share not only derived and publication related data but data generated in early phases of research data workflow such as primary data and analyzed data. |
| [F+S07](#F+S07) | Negative results are shared. |
| [F+S08](#F+S08) | The study is described with metadata including context, samples and data acquisition, methods for analyzing and processing data, quality control, and restriction for reuse. |
| [F+S08a](#F+S08a) | Metadata includes information about the study design, protocols and data collection methods. |
| [F+S08b](#F+S08b) | Metadata includes explicit references to research resources such as samples, cell lines |
| [F+S08c](#F+S08c) | Metadata contains information about data processing methods, data analysis and quality assurance metrics. |
| [F+S08d](#F+S08d) | Metadata includes information about data ownership, license and reuse constraints for sensitive data. |
| [F+A01](#F+A01)  |Data is organized and documented in a human understandable way |
| [F+A02](#F+A02)  | Data is encoded in a community specific exchange standard.   |
| [F+A03](#F+A03) | A machine and human readable formal description of the structure of data is available including types, properties. |
| [F+A04](#F+A04) | Data is structured by following a life sciences domain model, core classes and their semantic relations refers to a common data model. |
| [F+A05](#F+A05) | Data is described with terminology standards. |
| [F+A06](#F+A06) | Core data classes (important data elements) follows a common master and reference data entity. |


### Study Level

#### <a name="F+S01"> F+S01 </a> : Study level documentation is available in a human readable format.

|                 |                                                              |
| --------------- | ------------------------------------------------------------ |
| Description     | Study-level documentation provides high-level information on the research context and design, the data collection methods used, any data preparations and manipulations and summaries of findings based on the data. Examples and a suggested list of coverage can be found at [UK Data Services](https://www.ukdataservice.ac.uk/manage-data/document/study-level.aspx). <br><br>This indicator does not require any machine interpretable content, or semantic annotation of information with common vocabularies. It measures, availability of information to help data users to make informed use of the data. Publicly accessible web pages, pdf documents are acceptable formats. |
| Related DU Area | [Repurposing](Data_Usage_Areas.md#Repurposing)                                                  |



#### <a name="F+S02"> F+S02 </a> : **Data is reported by following community specific minimum information guidelines**

|                 |                                                              |
| --------------- | ------------------------------------------------------------ |
| Description     | A reporting standard ensures recording the information (metadata) required to unambiguously communicate experimental designs, treatments and analyses, to con-textualize the data generated. Such standards are also known as data content or minimum information standards ([Chervitz, et all.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4152841/)). See examples: reporting standards for[ health care](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4152841/table/T8/?report=objectonly), for [life sciences](https://www.biorxiv.org/content/biorxiv/early/2017/07/24/167619/T4/graphic-10.large.jpg) data, collection of [FAIRsharing ](https://fairsharing.org/standards/?q=minimum+information&selected_facets=type_exact:reporting%20guideline) |
| Related DU Area | [Reproducibility](Data_Usage_Areas.md#Reproducibility) + [Repurposing](Data_Usage_Areas.md#Repurposing)                                |



#### <a name="F+S03"> F+S03 </a> :  **Metadata documents and provides references about all data biological data types and formats in data is expressed.**

|                 |                                                              |
| --------------- | ------------------------------------------------------------ |
| Description     | Biological and biomedical research has been considered an especially challenging research field in this regard, as data types are extremely heterogeneous and not all have defined data standards ([Griffin, et. all](https://www.biorxiv.org/content/10.1101/167619v1.full)). Metadata should capture all data types and format names in a study, if possible provide a reference or URL for format specification, if not possible have a description.<br/><br/>[Example ](https://www.biorxiv.org/highwire/markup/341342/expansion?width=1000&height=500&iframe=true&postprocessors=highwire_tables%2Chighwire_reclass%2Chighwire_figures%2Chighwire_math%2Chighwire_inline_linked_media%2Chighwire_embed)list of common standard data formats for omics data. |
| Related DU Area | [Interpretability](Data_Usage_Areas.md#Interpretability)                                             |



#### <a name="F+S04"> F+S04</a> : **Relationships between different data sets in a study is well defined.**

|                 |                                                              |
| --------------- | ------------------------------------------------------------ |
| Description     | In a study there are multiple data sets which are used as input and produced as an output. When a data is FAIRified, it is important to understand which data files are generated from the analysis of which other data sets, or sample data. For example the EMBL-EBI [SDRF ](https://www.ebi.ac.uk/arrayexpress/help/creating_a_sdrf.html)(Sample and Data Relationship Format) describes the sample characteristics and the relationship between samples, arrays, data files. Some communities such as proteomics have adopted these file formats to their needs, see [SDRF for Proteomics](https://github.com/bigbio/proteomics-metadata-standard) . Furthermore, [ISA](https://isa-tools.org/format/specification.html) allows multiomics support and is used by [EMBL-EBI Metabolights](https://www.ebi.ac.uk/metabolights/index) <br><br/>The relationships can be also expressed as naming a convention. A good example is the [TCGA ](https://docs.gdc.cancer.gov/Encyclopedia/pages/TCGA_Barcode/)data set, where the barcode contains semantic information about the relation of data with other data (such as participant, sample, analyte, plate, sample). If there is a naming convention used, instead of a defined format standard, this convention should be clearly documented together with [code tables](https://gdc.cancer.gov/resources-tcga-users/tcga-code-tables). |
| Related DU Area | [Interpretability](Data_Usage_Areas.md#Interpretability)  + [Repurposing](Data_Usage_Areas.md#Repurposing)                               |



#### <a name="F+S05"> F+S05 </a> : **A versioning policy is applied to uniquely identify a particular form of a dataset from an earlier form or other forms of itself.**

|                 |                                                              |
| --------------- | ------------------------------------------------------------ |
| Description     | Versioning is tracking the changes made in data by saving new copies of data files with indicators of the changes made. A new version is created when there is a change in the structure, contents, or condition of the resource. In the case of research data, a new version of a dataset may be created when an existing dataset is reprocessed, corrected or appended with additional data. Versioned data are required to cite and identify the exact dataset used as a research input in order to support research reproducibility and trustworthiness ([ANDS](https://www.ands.org.au/working-with-data/data-management/data-versioning)). <br><br/>Best practices of versioning should include a numbering system, information about the status of the file, and what changes are made (see YALE Research Data Management for the Health Sciences: [File Versioning ](https://guides.library.yale.edu/rdm_healthsci/versioning#:~:text=Versioning) involves tracking the changes,access older copies of files.)) . PIDs can be assigned for versions, however there is no convention for that (see [ANDS](https://www.ands.org.au/working-with-data/data-management/data-versioning) : DOIs for versioned data). Some simple versioning solutions can be adopted (see [Stanford libraries](https://library.stanford.edu/research/data-management-services/data-best-practices/data-versioning), Uni. [Virginia Library](https://data.library.virginia.edu/data-management/plan/files/)). |
| Related DU Area |  [Reproducibility](Data_Usage_Areas.md#Reproducibility) + [Repurposing](Data_Usage_Areas.md#Repurposing)                                |



#### <a name="F+S06"> F+S06 </a> : **Share not only derived and publication related data but data generated in early phases of research data workflow such as primary data and analyzed data.**

|                 |                                                              |
| --------------- | ------------------------------------------------------------ |
| Description     | Life science experiments comprise different samples; based on experiment and sample, several measurements are performed. After quantification there is a step of data processing and analysis which results in life science research ([Colmsee](https://www.researchgate.net/publication/51724887_A_case_study_for_efficient_management_of_high_throughput_primary_lab_data/figures) et.all). In most cases, data is shared with publications as supplementary files, or in data repositories which are referenced by articles. However raw data and primary data resides in private storages ([Arend](https://www.researchgate.net/publication/263355191_EDAL_-_a_framework_to_store_share_and_publish_research_data/figures), et. all). There are great benefits of sharing primary data, including to make meaningful comparisons between results, to answer ‘what if’ questions and to carry out pilot studies without repeating experiments ([Koslow](https://www.nature.com/articles/nn0900_863) ). <br><br>This indicator measures availability of any primary data beyond the derived data or aggregated analyzed data. |
| Related DU Area | [Repurposing](Data_Usage_Areas.md#Repurposing)                                                  |



#### <a name="F+S07"> F+S07 </a> : **Negative results are shared.**

|                 |                                                              |
| --------------- | ------------------------------------------------------------ |
| Description     | Negative results are the outcomes which do not support study hypotheses. Researchers are rewarded more for publishing novel findings, and not for publishing negative results. However, sharing negative results could reduce efforts and avoid repeating work that may be difficult to replicate ([ATCC](https://www.nature.com/articles/d42473-019-00004-y#ref-CR15)).Negative result also can be reported in publications (e.g. [Negative Results Journal](https://www.negative-results.org/)). <br/><br>This indicator measures the availability of negative results sets in the shared data content. |
| Related DU Area | [Repurposing](Data_Usage_Areas.md#Repurposing)                                                  |



#### <a name="F+S08"> F+S08 </a> : **The study is described with metadata including context, samples and data acquisition, methods for analyzing and processing data, quality control, and restriction for reuse.**

|             |                                                              |
| ----------- | ------------------------------------------------------------ |
| Description | This indicator can be evaluated in two phases: 1) providing a structured metadata with domain conventions; 2) providing machine readable metadata by using any common vocabularies. <br/><br>This indicator is divided into a set of indicators from F+S08a to F+S08d. |

#### <a name="F+S08a"> F+S08a </a> : **Metadata includes information about the study design, protocols and data collection methods.**

|                 |                                                              |
| --------------- | ------------------------------------------------------------ |
| Description     | Example metadata: study / experiment design, trial protocol, data acquisition methods, experiment methods, data processing methods .<br/>See [multi omics metadata](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3903324/table/T1/) check list, [clinical trial metadata](https://www.ncbi.nlm.nih.gov/books/NBK286004/box/box_4-1/?report=objectonly) |
| Related DU Area |  [Reproducibility](Data_Usage_Areas.md#Reproducibility) + [Repurposing](Data_Usage_Areas.md#Repurposing)                                |



#### <a name="F+S08b"> F+S08b</a> : **Metadata includes explicit references to research resources such as samples, cell lines**

|                 |                                                              |
| --------------- | ------------------------------------------------------------ |
| Description     | Provide information about key research materials such as antibodies, cell lines, and organisms. Preferable with identifiers, see [RRID ](https://www.rrids.org/)portal. |
| Related DU Area |  [Reproducibility](Data_Usage_Areas.md#Reproducibility) + [Repurposing](Data_Usage_Areas.md#Repurposing)                                |



#### <a name="F+S08c"> F+S08c</a> : **Metadata contains information about data processing methods, data analysis and quality assurance metrics.**

|                 |                                                              |
| --------------- | ------------------------------------------------------------ |
| Description     | See specific examples for quality requirements for [In Vitro research](https://link.springer.com/chapter/10.1007/164_2019_284), such as chemical probes, cell line authentication, antibody validation. |
| Related DU Area |  [Reproducibility](Data_Usage_Areas.md#Reproducibility) + [Repurposing](Data_Usage_Areas.md#Repurposing)                                |



#### <a name="F+S08d"> F+S08d </a> :**Metadata includes information about data ownership, license and reuse constraints for sensitive data.**

|                 |                                                              |
| --------------- | ------------------------------------------------------------ |
| Description     | Considering the sensitive nature of life science data, beside data reuse license, consent, and if exist any other constraints should be documented. |
| Related DU Area | [Repurposing](Data_Usage_Areas.md#Repurposing)                                                  |

<hr></hr>

### Assays / Data Set Level:

#### <a name="F+A01"> F+A01 </a> : **Data is organized and documented in a human understandable way**

|                 |                                                              |
| --------------- | ------------------------------------------------------------ |
| Description     | Data-level, or object-level, documentation provides information at the level of variables in a database or individual objects such as images. Data-level information can be embedded in data files, such as variable, value and code labels in an SPSS file or headers in a document. Examples for quantitative, qualitative and secondary source documentation can be found at [UK Data Services](https://www.ukdataservice.ac.uk/manage-data/document/study-level.aspx).<br/><br/>This indicator does not require any machine readable content, or semantic annotation of information with common vocabularies. It measures how easily data can be explored and understood by humans who are familiar with the domain. |
| Related DU Area | [Interpretability](Data_Usage_Areas.md#Interpretability)                                              |

#### <a name="F+A02"> F+A02 </a> : **Data is encoded in a community specific exchange standard.**

|                 |                                                              |
| --------------- | ------------------------------------------------------------ |
| Description     | A data exchange standard defined the encoding format of data. A data exchange standard delineates what data types can be encoded and the particular way they should be encoded (e.g., tab-delimited columns, XML, binary, etc. They facilitate the exchange of information between researchers and organizations, and between software programs or information storage systems. ). They provide syntax standards but do not specify what the document should contain in order to be considered complete ([Chervitz, et all.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4152841/)).<br/></br> See examples for [omic data](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4152841/table/T4/), for microarray-based [transcriptomics ](https://www.researchgate.net/publication/257204855_A_sea_of_standards_for_omics_data_Sink_or_swim/figures), for [clinical data](https://en.wikipedia.org/wiki/Clinical_Data_Interchange_Standards_Consortium#Individual_standards). |
| Related DU Area | [Integration](Data_Usage_Areas.md#Integration)                                                  |

#### <a name="F+A03"> F+A03 </a> : **A machine and human readable formal description of the structure of data is available including types, properties.**

|                 |                                                              |
| --------------- | ------------------------------------------------------------ |
| Description     | A schema describes the structure of the data. Special schemes have meanings associated with databases, such as community agreed profiles. A schema consists of a key dimension and its properties, expected types, constraints, cardinalities and associated controlled vocabularies (preferably refers to existing ontologies). Schemas and profiles can be registered and reused, for examples [FAIRsharing Standards](https://fairsharing.org/standards/) and specific examples such as [Schema.org](https://schema.org/docs/schemas.html), [Bioschemas](https://bioschemas.org/profiles/), or [HL7 resources](https://www.hl7.org/fhir/resourcelist.html) in the context of health data records. |
| Related DU Area | [Integration](Data_Usage_Areas.md#Integration)                                                  |



####  <a name="F+A04"> F+A04 </a> : **Data is structured by following a life sciences domain model, core classes and their semantic relations refers to a common data model.**

|                 |                                                              |
| --------------- | ------------------------------------------------------------ |
| Description     | Meaningful exchange of information is a fundamental challenge in life sciences research. A domain model A domain is an abstract, implementation-independent representation of the grammar, or semantics, of a domain ([Freimuth, et. all)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3486731/) . Domain models define core classes and the semantic relationships between them, as well as providing unambiguous definitions for concepts required to describe life sciences research. Examples of life sciences common data models are [OMOP](https://www.ohdsi.org/data-standardization/the-common-data-model/), [BRIDG](https://bridgmodel.nci.nih.gov/high-level-concept), [Lifesciences DAM](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3486731/), [functional genomics](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1262694/figure/F1/) data modelling. |
| Related DU Area | [Interpretability](Data_Usage_Areas.md#Interpretability)  \+ [Integration](Data_Usage_Areas.md#Integration)                              |

####  <a name="F+A05">F+A05 </a> : Data is described with terminology standards.

|                 |                                                              |
| --------------- | ------------------------------------------------------------ |
| Description     | Terminology standards is typically defined by the use cases and provides control vocabularies to support and competency questions it is designed to answer. In life sciences domain ontologies are common ways to encode terminology standards ([Chervitz, et all.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4152841/)). Terminology standards add an interpretive layer to the data by defining the concepts or terms in a domain, and in some cases the relationships between them ([Tenenbaum et. all](https://doi.org/10.1136/amiajnl-2013-002066)). See an example list for [terminology standards](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4152841/table/T5/). For a complete listing see the [OBO ](http://www.obofoundry.org)Foundry. |
| Related DU Area | [Interpretability](Data_Usage_Areas.md#Interpretability) \+ [Integration](Data_Usage_Areas.md#Integration)                              |

####  <a name="F+A06">F+A06  </a> : **Core data classes (important data elements) follows a common master and reference data entity.**

|                 |                                                              |
| --------------- | ------------------------------------------------------------ |
| Description     | Master data is defined as core business objects used in different applications across an organization along with their associated metadata, definitions and taxonomies. Reference data is used to characterize or classify other data such as codes and description tables. Master and Reference data lowers cost and complexity through use of standards, common data models, and integration patterns. Sharing master data within a community or in organization reduces variability caused by multiple studies producing the same type of data, but in isolation, then inconsistencies in data structure and data values between the systems occurs (DAMA). <br>In the life science domain, master data entities examples can be a study, a subject, a file, a chemical compound, or an observation. Common data models provide core classes which can be useful for creating master data elements (see[ LS DAM ](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3486731/)Experiment, Molecular Biology, Molecular Databases core classes). However master data should be described, are assigned an unique identifier, and registered on a searchable source. An example to reference data from the health domain can be the [value set](https://simplifier.net/guide/ProfilingAcademy/Terminology) of the HL7.<br><br>Precondition of measuring this indicator is the existence of a master and reference data in a related research community, an organization, or a repository. |
| Related DU Area | [Integration](Data_Usage_Areas.md#Integration)                                                  |


---

## Authors

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Oya Deniz Beyan | fit.fraunhofer.de | [0000-0000-0000-0000](https://orcid.org/orcid.org/0000-0000-0000-0000) | Writing - Original Draft |
|  |  | | Writing - Review & Editing, Funding acquisition | 

---

## License

This page is released under the Creative Commons 4.0 BY license.

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png" height="20"/></a>

