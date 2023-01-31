(fcb-interop-etl)=

# Extraction, transformation, and loading process


````{panels_fairplus}
:identifier_text: FCB031
:identifier_link: 'https://w3id.org/faircookbook/FCB031'
:difficulty_level: 5
:recipe_type: survey_review
:reading_time_minutes: 15
:intended_audience: data_curator, data_manager, data_scientist  
:maturity_level: 0
:maturity_indicator: 0
:has_executable_code: nope
:recipe_name: Surveying extraction, transformation, load (ETL) tools
```` 


## Main Objectives

This recipe identifies tools for `data extraction`, `transformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion`, and `loading` (ETL). 
ETL is the process of collecting data from one source to persist it in another designated system in which the data is represented differently {footcite}`etl_wiki`.
A common use case in data science is to build a scalable and portable ETL system to extract data from various sources, transform said-data into a cohesive dataset, and load the data to an internal or public database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)  to support data exploration.

This recipe aims to serve as a start point for designing ETL workflows, rather than provide a comprehensive list covering all available tools.

>The lists of tools are generated either by manual curation, which reflects what is being used in the industry, or automatally discovered from the bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c)  repository (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository) .

```{warning} 
The content in these tables was generated in March 2021.
For updated content, please check the [FAIR tooling repository](https://github.com/FAIRplus/WP3_FAIR_tooling).
To provide feedback on this content or report issues, please do so via the [FAIR Cookbook github issue tracker](https://github.com/FAIRplus/the-fair-cookbook/issues)
```

## Graphical Overview

The figure below shows different ETL-related operations and their relationships, together with related tools and recipes.


````{dropdown} 
:open:
```{figure} ETL-tools-mermaid.png
---
width: 800px
name: Overview of key aspects in ETL process
alt: Overview of key aspects in ETL process
---
Overview of key aspects in ETL process
```
````


The table below is an overview of ETL tools identified.
Details of each tools are also provided in this doc.
For ETL tools for RDF (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.p77ph9)  data model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) , please check the dedicated recipe<!-- {ref}`fcb-interop-etl2rdf-tools` -->.

|                          |                               |                 |
|--------------------------|-------------------------------|-----------------|
| Data query and retrieval | Data transformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion           | Data deposition |
| TAMR                     | SDTM                          | REDC (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.4e7190)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/3547) ap          |
| Bert                     | TriFacta                      | TransMA (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.pdwqcr) R (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.SnTbUa) T       |
| Termite                  | OMO (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.qs4x5m) P (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.mct09a)                           | Stardog         |
| Oracle clinical          | Collibra                      | Postgresql      |
| GeoBoost2                | Apache Hadoop                 | Chemotion       |
| MartView                 | Talend                        |                 |
| CL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.j9y503) O (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.4dvtcz) BNET                  | Informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ica                   |                 |
| PDB (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9y4cqw) USQLExtractor         | OpenRefine-metadata-extension |                 |
| repo                     | DISQOVER                      |                 |
| SNPator                  | Query Tabular                 |                 |
| PyGMQL                   | ms-data-core (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.xMmOCL) -api              |                 |
| PlantPIs                 |                               |                 |
| BAGET                    |                               |                 |
| NCBI Resources           |                               |                 |
| CP (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.wP3t2L) AD                     |                               |                 |

```{warning} 
The tools list above aims to provide a basic overview of what is available on the market. It is *not* a formal recommendation. If you think key tools are missing or the list needs an update, please contact us via the [github issue tracker](https://github.com/FAIRplus/the-fair-cookbook/issues).
```


## Requirements

* Knowledge requirement:

   * General fam (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d0886a) iliarity with data cleaning, data loading tasks.
   
---

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [data retrieval](http://edamontology.org (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.a6r7zs) /operation_2422)  | 
| [validation](http://edamontology.org (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.a6r7zs) /operation_2428)||
| [data deposition](http://edamontology.org (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.a6r7zs) /operation_3431)||
| [data submission, annotation and curation](http://edamontology.org (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.a6r7zs) /topic_0219)| |


---

## Operations

<!-- <h3 id=Data-query-and-retrieval>Data query and retrieval</h3> -->

`Data query and retrieval` is the process of extracting structured or unstructured data from different sources. The process of identifying and obtaining data from data management systems.

__Manually curated list of tools__

|Tool|Description|License|Topics|Resource type|
|---|--|--|--|--|
|[TAMR](https://www.tamr.com/)|A cloud-native data mastering solution (cloud MDM (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.wnk2eq) ) accelerate analytics through machine learning (ML), available on Google Cloud, Azure and AWS.|Commercial license|informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion integration, data unification|
|[Bert](https://github.com (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.c55d5e) /google-research/bert)|Bidirectional Encoder Representations from Transformers (BERT) is a Transformer-based machine learning technique for natural language processing (NLP) pre-training developed (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.31385c)  by Google, aiming to extractcontext-sensitive features from an input text.  |Apache License 2.0|relationship extraction|Data model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) |
|[Termite](https://www.scibite.com/platform/termite/)|TERMite (TERM identification, tagging & extraction) is a fast named entity recognition (NER) and extraction engine for semantic analytics.|Commercial license|informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion extraction|
|[Oracle clinical](https://www.oracle.com/uk/industries/life-sciences/clinical-research/)|a single application and infrastructure for electronic data capture and clinical data management, while leveraging the renowned Oracle database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database) . Oracle Clinical enables management of all clinical trial data in a single system, improving accuracy, visibility, and data integrity.|Commercial license|Clinical data|

__Automatically created list of tools by querying [Bio.Tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) ](https://bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) ).__

|Tool|Description|License|Topics|Resource type|
|---|--|--|--|--|
|[GeoBoost2](https://bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) /geoboost2)|A natural languageprocessing pipeline for GenBank (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9kahy4)  metadata enrichment for virus phylogeography.|Apache-2.0 License|Biotechnology, Natural language processing, Workflows, Public health and epidemiology, Infectiousdisease|Web application|
|[MartView](https://bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) /martview)|Tool for data retrieval and data mining that integrates data from Ensembl (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.fx0mw7)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.fx0mw7) . Through the web interface it allows you to apply a series of filters to create custom datasets which can be converted to several useful output format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) s.| N/A |Pathology, Data integration and warehousing, Database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)  management, Molecular interactions, pathways and networks, Gene transcripts|Web Application|
|[CLOBNET](https://bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) /CLOBNET)|Cloud-based machine learning system (CL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.j9y503) O (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.4dvtcz) BNET) that is an open-source, lean infrastructure for electronic health record (EHR) data integration and is capable of extract, transform, and load (ETL) processing|BSD-2-Clause|Machine learning, Medicines research (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.52b22c)  and development|Web application (for internal use)|
|[PDBUSQLExtractor](https://bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) /PDBUSQLExtractor)|Scalable Extraction of Big Macromolecular Data in Azure Data Lake Environment.|GPL-3.0|Nucleic acid structure analysis|C# library|
|[repo](https://bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) /repo)|A data manager meant to avoid manual storage/retrieval of data to/from the file system. It builds one (or more) centralized repository (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository)  where R objects are stored with rich annotations, including corresponding code chunks, and easily search (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.52b22c) ed and retrieved.|GPL-3.0|Data submission, annotation and curation, Data management, Database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)  management|R library|
|[SNPator](https://bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) /snpator)|Originally designed to help CeGen users to handle (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.0b7e54) , retrieve, transform and analyze the genetic data generated by the genotyping facilities of the institution (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=institution) . However, it is also open to external users who may want to upload their own genotyped (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.31385c)  data in order to take advantage its data processing features. Users will be able to perform a set of operations which may range from very simple format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)  transformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ions to some complex biostatistical calculations.|N/A|Bioinformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ics, Data quality management, Genetic variation, GWAS (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.ubYn8D)  study|Web Application|
|[PyGMQL](https://bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) /PyGMQL)|Scalable data extraction and analysis for heterogeneous genomic datasets. Based on GMQL.|Apache-2.0|Imaging, Workflows, Database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)  management|Python Library|

__Data portals with extraction functionalities discovered from [Bio.Tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) ](https://bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) ).__

|Tool|Description|License|Topics|Resource type|
|---|--|--|--|--|
|[PlantPIs](https://bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) /plantpis)|Web querying system for a database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)  collecting plant protease inhibitors data.|Plant biology, Gene and protein fam (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d0886a) ilies (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.y3scf6) |Database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)  Portal|
|[BAGET](https://bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) /baget)|Web service designed to facilitate extraction of specific gene and protein sequences from completely determined prokaryotic genomes. Query results can be exported as a rich text format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.364323)  file for printing, arch (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.52b22c) ival or further analysis.|N/A|DNA, Sequencing, Model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)  organisms, Sequence analysis|Web application|
|[NCBI Resources](https://bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) /ncbi_resources)|Analysis and retrieval resources for the data in GenBank (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9kahy4)  and other biological data made available through the NCBI web site.|Open Access|Data mining, Data integration and warehousing, Database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)  management, Molecular interactions, pathways and networks, Rare diseases|Web Application, Database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)  portal|
|[CPAD](https://bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) /cpad)|Curated Protein (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.rtndct)  Aggregation Database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)  (CP (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.wP3t2L) AD) is an integrated database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)  which contains informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion related to amyloidog (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.exc0vp)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.408108) enic proteins, Aggregation prone regions, aggregation kinetics and structure of proteins relevant to aggregation.|N/A|Proteomics, Data submission, annotation and curation, Protein (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.rtndct) s, Small molecules, Literature and language|Data Portal|
|[GenomicsDB](https://bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) /GenomicsDB)|Advancing clinical cohort selection with genomics analysis on a distributed platform. Highly performant data storage in C++ for importing, querying and transforming variant data with Java/Spark. Used in gatk4.|MIT License|Exome sequencing, Systems medicine (URL_TO_INSERT_RECORD http://127.0.0.1:8080/3536) , Personalised medicine, Complementary medicine, Biobank|Command-line|
|[Epiviz File Server](https://bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) /epivizFileServer)|A library to query and transform genomic data from indexed files|MIT License|Oncology,Workflows, DNA|Python Library|

<!-- <h3 id=Data-transformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion>Data transformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion</h3> -->

### Data transformation

`Data transformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion` is the process of converting the data format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) , structure, and value for a specific goal, which may include meeting a specific data standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) s.

Below are listed common operations in data transformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion:

- Data annotation
    The process of labeling data or metadata.
- Data validation
    The process of ensuring data has met data standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) s both in terms of data content and data format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) .
- Data aggregation
    The process of gathering data and presenting it, usually, in a summarized format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) .



**Manually curated list of tools**

|Tool|Description|License|Topics|Resource type|
|---|--|--|--|--|
|[SDTM](https://www.cdisc.org (URL_TO_INSERT_RECORD http://127.0.0.1:8080/3525) /standards/foundational/sdtm (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.s51qk5) )|SDTM provides a standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)  for organizing and format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ting data to streamline processes in collection (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=collection)  management analysis and reporting.|N/A|data aggregation, data warehousing, Standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)  for Exchange of Non-clinical Data|Data standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) 
|[TriFacta](https://www.trifacta.com)|A data preparation tool for data quality improvement, data transformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion, and building data pipelines.|Commercial license|
|[OMOP](https://www.ohdsi.org/data-standardization/the-common-data-model (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.qk984b) /)|The OMO (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.qs4x5m) P (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.mct09a)  Common Data Model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)  allows for the systematic analysis of disparate observational database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database) s.|N/A|Data transformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion|Data model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) |
|[Collibra](https://www.collibra.com/)|an enterprise-oriented data governance platform that provides tools for data management and stewardship.|Commercial license|Data catalogue,data governance, data linkage|
|[Apache Hadoop](https://hadoop.apache.org/)|A framework that allows for the distributed processing of large data sets across clusters of computers using simple programming model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) s. It is designed to scale up from single servers to thousands of machines|[Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)|Distributed computing|
|[Talend](https://www.talend.com/products/integrate-data/)|A unified approach that combines rapid data integration, transformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion, and map (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.53edcc) ping with automated quality checks to ensure trustworthy data in every step.|Commercial license|Data integration|
|[Informatica](https://www.informatica.com/)|Connect & fetch data from different heterogeneous source and processing of data.|Commercial license|Data integration|

__Automatically created list of tools by querying [Bio.Tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) ](https://bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) ).__

|Tool|Description|License|Topics|Resource type|
|---|--|--|--|--|
|[OpenRefine-metadata-extension](https://github.com (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.c55d5e) /FAIRDataTeam/OpenRefine-metadata-extension)| Enables a post-hoc FAIR (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.WWI10U) ification workflow: load an existing (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.q7bkqr)  dataset, perform data wrangling tasks, add FAIR (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.WWI10U)  attributes to the data, generate a linked data version of the data and, finally, push the result to an online FAIR (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.WWI10U)  data infrastructure to make it accessible and discoverable.|MIT License|Data submission, Annotation and curation, Data identity and map (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.53edcc) ping|Extension|
|[DISQOVER](https://bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) /discover)|Data integration platform for public, licensed and internal data. The Data Ingestion Engine enables transforming data into Linked Data which can be search (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.52b22c) ed, navigated and analysed via the user interface and the API.|N/A|Biomedical science, Omics, Biology, Chemistry (URL_TO_INSERT_RECORD http://127.0.0.1:8080/3524)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/3524) , Medicine|--|
|[PGA](https://bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) /pga)|Construction of customized protein database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database) s based on RNA-Seq data with/without genome guided, database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)  search (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.52b22c) ing, post-processing and report generation.|GPL-2.0|Proteomics, Proteomics experiment, Data submission, annotation and curation, Data integration and warehousing, Database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)  management, Data governance, RNA-seq| R library|
|[Query Tabular](https://bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) /Query_Tabular)|Galaxy-based tool which manipulates tabular files. Query Tabular automatically creates a SQLite database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)  directly from a tabular file within a Galaxy workflow. The SQLite database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)  can be saved to the Galaxy history, and further process to generate tabular outputs containing desired informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion and format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ting.|CC-BY-4.0|Bioinformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ics,Workflows|Galaxy-based|
|[ms-data-core-api](https://bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) /ms-data-core-api)|The primary purpose of ms-data-core (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.xMmOCL) -api library is to provide commonly used classes and Object Model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)  for Proteomics Experiments. You may also find it useful for your own computational proteomics project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project) s.|Apache-2.0|Proteomics, Proteomics experiment, Software engineering|Java Library|

<!-- <h3 id=Data-deposition>Data deposition</h3> -->

### Data Deposition

`Data deposition` is the process of loading data to hosting (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.q7bkqr)  (end) destinations, such as public data arch (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.52b22c) ives and data warehouses.

__Manually curated list of tools__

|Tool|Description|License|Topics|Resource type|
|---|--|--|--|--|
|[REDCap](https://www.project-redcap.org/)|REDCap is a secure web application for building and managing online surveys and database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database) s. While REDC (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.4e7190)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/3547) ap can be used to collect virtually any type of data in any environment|[REDC (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.4e7190)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/3547) ap License Terms](https://projectredcap.org/partners/termsofuse/)|Cloud migration|Web application|
|[TransMART](https://github.com (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.c55d5e) /transmart)|An open-source data warehouse designed to store large amounts of clinical data from clinical trials, as well as data from basic research (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.52b22c) |[GPL-3.0 License](https://github.com (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.c55d5e) /transmart/transmartApp/blob/master/LICENSE.TXT)|Data storage, clinical data|
|[Stardog](https://www.stardog.com/)|Triple Store Database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database) , Provide an enterprise knowledge graph as FAIR (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.WWI10U) + data catalogue|Commercial license|Data integration,data catalog|
|[Postgresql](https://www.postgresql.org/)|A free and open-source relational database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)  management system (RDBMS) emphasizing extensibility and SQL compliance.|[The PostgreSQL Licence](https://www.postgresql.org/about/licence/)|Relational database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database) |

__Automatically created list of tools by querying [Bio.Tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) ](https://bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) ).__

|Tool|Description|License|Topics|Resource type|
|---|--|--|--|--|
|[Chemotion](https://bio.tools (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.63520c) /chemotion)|Repository for chemistry (URL_TO_INSERT_RECORD http://127.0.0.1:8080/3524)  research (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.52b22c)  data that provides solutions for current challenges to store research (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.52b22c)  data in a feasible manner, allowing the conservation of domain specific informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion in a machine readable format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) . |CC-BY-4.0|Data submission, annotation and curation, Workflows, Chemistry (URL_TO_INSERT_RECORD http://127.0.0.1:8080/3524)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/3524) |Data repository (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository) |

### Example use case: 

To show how some of these tools may be used, the following related recipes provide further guidance with real life examples.


1. {ref}`fcb-interop-fastqval`
   
<!--
2. OMO (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.qs4x5m) P (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.mct09a)  ETL [link]( TO (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.w69t6r) DO link to recipe) (*in prepartion*)
3. RDF (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.p77ph9)  ETL [link]( TO (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.w69t6r) DO link to recipe)  (*in prepartion*)
-->


## References
````{dropdown} **References**
```{footbibliography}
```
````

## Authors

````{authors_fairplus}
Fuqi: Writing - Original Draft
Eva: Writing - Original Draft
Sukhi: Tool curation
Philippe: Writing - Review & Editing
````


## License

````{license_fairplus}
CC-BY-4.0
````



