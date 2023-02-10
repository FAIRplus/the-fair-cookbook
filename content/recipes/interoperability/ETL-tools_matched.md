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

This recipe identifies tools for `data extraction`, `transformat (URL_TO_INSERT_TERM_2791 https://fairsharing.org/search?recordType=model_and_format) ion`, and `loading` (ETL). 
ETL is the process of collecting data from one source to persist it in another designated system in which the data is represented differently {footcite}`etl_wiki`.
A common use case in data science is to build a scalable and portable ETL system to extract data from various sources, transform said-data into a cohesive dataset, and load the data to an internal or public database (URL_TO_INSERT_TERM_2792 https://fairsharing.org/search?fairsharingRegistry=Database)  to support data exploration.

This recipe aims to serve as a start point for designing ETL workflows, rather than provide a comprehensive list covering all available tools.

>The lists of tools are generated either by manual curation, which reflects what is being used in the industry, or automatally discovered from the bio.tools (URL_TO_INSERT_RECORD-NAME_2794 https://fairsharing.org/FAIRsharing.63520c)  repository (URL_TO_INSERT_TERM_2793 https://fairsharing.org/search?recordType=repository) .

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
For ETL tools for RDF data model, please check the dedicated recipe<!-- {ref}`fcb-interop-etl2rdf-tools` -->.

|                          |                               |                 |
|--------------------------|-------------------------------|-----------------|
| Data query and retrieval | Data transformat (URL_TO_INSERT_TERM_2795 https://fairsharing.org/search?recordType=model_and_format) ion           | Data deposition |
| TAMR                     | SDTM                          | REDCap          |
| Bert                     | TriFacta                      | TransMART       |
| Termite                  | OMOP                          | Stardog         |
| Oracle clinical          | Collibra                      | Postgresql      |
| GeoBoost2                | Apache Hadoop                 | Chemotion       |
| MartView                 | Talend                        |                 |
| CLOBNET                  | Informat (URL_TO_INSERT_TERM_2796 https://fairsharing.org/search?recordType=model_and_format) ica                   |                 |
| PDBUSQLExtractor         | OpenRefine-metadata-extension |                 |
| repo                     | DISQOVER                      |                 |
| SNPator                  | Query Tabular                 |                 |
| PyGMQL                   | ms-data-cor (URL_TO_INSERT_RECORD-NAME_2797 https://fairsharing.org/FAIRsharing.xMmOCL)  (URL_TO_INSERT_RECORD-ABBREV_2798 https://fairsharing.org/FAIRsharing.m283c) e-api              |                 |
| PlantPIs                 |                               |                 |
| BAGET                    |                               |                 |
| NCBI Resources           |                               |                 |
| CPAD                     |                               |                 |

```{warning} 
The tools list above aims to provide a basic overview of what is available on the market. It is *not* a formal recommendation. If you think key tools are missing or the list needs an update, please contact us via the [github issue tracker](https://github.com/FAIRplus/the-fair-cookbook/issues).
```


## Requirements

* Knowledge requirement:

   * General familiarity with data cleaning, data loading tasks.
   
---

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [data retrieval](http://edamontology.org/operation_2422)  | 
| [validation](http://edamontology.org/operation_2428)||
| [data deposition](http://edamontology.org/operation_3431)||
| [data submission, annotation and curation](http://edamontology.org/topic_0219)| |


---

## Operations

<!-- <h3 id=Data-query-and-retrieval>Data query and retrieval</h3> -->

`Data query and retrieval` is the process of extracting structured or unstructured data from different sources. The process of identifying and obtaining data from data management systems.

__Manually curated list of tools__

|Tool|Description|License|Topics|Resource type|
|---|--|--|--|--|
|[TAMR](https://www.tamr.com/)|A cloud-native data mastering solution (cloud MDM (URL_TO_INSERT_RECORD-ABBREV_2800 https://fairsharing.org/FAIRsharing.wnk2eq) ) accelerate analytics through machine learning (ML), available on Google Cloud, Azure and AWS.|Commercial license|informat (URL_TO_INSERT_TERM_2799 https://fairsharing.org/search?recordType=model_and_format) ion integration, data unification|
|[Bert](https://github.com/google-research/bert)|Bidirectional Encoder Representations from Transformers (BERT) is a Transformer-based machine learning technique for natural language processing (NLP) pre-training developed by Google, aiming to extractcontext-sensitive features from an input text.  |Apache License 2.0|relationship extraction|Data model (URL_TO_INSERT_TERM_2801 https://fairsharing.org/search?recordType=model_and_format) |
|[Termite](https://www.scibite.com/platform/termite/)|TERMite (TERM identification, tagging & extraction) is a fast named entity recognition (NER) and extraction engine for semantic analytics.|Commercial license|informat (URL_TO_INSERT_TERM_2802 https://fairsharing.org/search?recordType=model_and_format) ion extraction|
|[Oracle clinical](https://www.oracle.com/uk/industries/life-sciences/clinical-research/)|a single application and infrastructure for electronic data capture and clinical data management, while leveraging the renowned Oracle database (URL_TO_INSERT_TERM_2803 https://fairsharing.org/search?fairsharingRegistry=Database) . Oracle Clinical enables management of all clinical trial data in a single system, improving accuracy, visibility, and data integrity.|Commercial license|Clinical data|

__Automatically created list of tools by querying [Bio.Tools](https://bio.tools).__

|Tool|Description|License|Topics|Resource type|
|---|--|--|--|--|
|[GeoBoost2](https://bio.tools/geoboost2)|A natural languageprocessing pipeline for GenBank (URL_TO_INSERT_RECORD-ABBREV_2804 https://fairsharing.org/FAIRsharing.9kahy4)  metadata enrichment for virus phylogeography.|Apache-2.0 License|Biotechnology, Natural language processing, Workflows, Public health and epidemiology, Infectiousdisease|Web application|
|[MartView](https://bio.tools/martview)|Tool for data retrieval and data mining that integrates data from Ensembl (URL_TO_INSERT_RECORD-NAME_2807 https://fairsharing.org/FAIRsharing.fx0mw7) . Through the web interface it allows you to apply a series of filters to create custom datasets which can be converted to several useful output format (URL_TO_INSERT_TERM_2806 https://fairsharing.org/search?recordType=model_and_format) s.| N/A |Pathology, Data integration and warehousing, Database (URL_TO_INSERT_TERM_2805 https://fairsharing.org/search?fairsharingRegistry=Database)  management, Molecular interactions, pathways and networks, Gene transcripts|Web Application|
|[CLOBNET](https://bio.tools/CLOBNET)|Cloud-based machine learning system (CLOBNET) that is an open-source, lean infrastructure for electronic health record (EHR) data integration and is capable of extract, transform, and load (ETL) processing|BSD-2-Clause|Machine learning, Medicines research and development|Web application (for internal use)|
|[PDBUSQLExtractor](https://bio.tools/PDBUSQLExtractor)|Scalable Extraction of Big Macromolecular Data in Azure Data Lake Environment.|GPL-3.0|Nucleic acid structure analysis|C# library|
|[repo](https://bio.tools/repo)|A data manager meant to avoid manual storage/retrieval of data to/from the file system. It builds one (or more) centralized repository (URL_TO_INSERT_TERM_2809 https://fairsharing.org/search?recordType=repository)  where R objects are stored with rich annotations, including corresponding code chunks, and easily searched and retrieved.|GPL-3.0|Data submission, annotation and curation, Data management, Database (URL_TO_INSERT_TERM_2808 https://fairsharing.org/search?fairsharingRegistry=Database)  management|R library|
|[SNPator](https://bio.tools/snpator)|Originally designed to help CeGen users to handle (URL_TO_INSERT_RECORD-NAME_2815 https://fairsharing.org/FAIRsharing.0b7e54) , retrieve, transform and analyze the genetic data generated by the genotyping facilities of the institution (URL_TO_INSERT_TERM_2810 https://fairsharing.org/search?recordType=institution) . However, it is also open to external users who may want to upload their own genotyped data in order to take advantage its data processing features. Users will be able to perform a set of operations which may range from very simple format (URL_TO_INSERT_TERM_2811 https://fairsharing.org/search?recordType=model_and_format)  transformat (URL_TO_INSERT_TERM_2812 https://fairsharing.org/search?recordType=model_and_format) ions to some complex biostatistical calculations.|N/A|Bioinformat (URL_TO_INSERT_TERM_2813 https://fairsharing.org/search?recordType=model_and_format) ics, Data quality management, Genetic variation, GWAS (URL_TO_INSERT_RECORD-ABBREV_2814 https://fairsharing.org/FAIRsharing.ubYn8D)  study|Web Application|
|[PyGMQL](https://bio.tools/PyGMQL)|Scalable data extraction and analysis for heterogeneous genomic datasets. Based on GMQL.|Apache-2.0|Imaging, Workflows, Database (URL_TO_INSERT_TERM_2816 https://fairsharing.org/search?fairsharingRegistry=Database)  management|Python Library|

__Data portals with extraction functionalities discovered from [Bio.Tools](https://bio.tools).__

|Tool|Description|License|Topics|Resource type|
|---|--|--|--|--|
|[PlantPIs](https://bio.tools/plantpis)|Web querying system for a database (URL_TO_INSERT_TERM_2817 https://fairsharing.org/search?fairsharingRegistry=Database)  collecting plant protease inhibitors data.|Plant biology, Gene and protein families (URL_TO_INSERT_RECORD-NAME_2819 https://fairsharing.org/FAIRsharing.y3scf6) |Database (URL_TO_INSERT_TERM_2818 https://fairsharing.org/search?fairsharingRegistry=Database)  Portal|
|[BAGET](https://bio.tools/baget)|Web service designed to facilitate extraction of specific gene and protein sequences from completely determined prokaryotic genomes. Query results can be exported as a rich text format (URL_TO_INSERT_TERM_2821 https://fairsharing.org/search?recordType=model_and_format)  (URL_TO_INSERT_RECORD-NAME_2822 https://fairsharing.org/FAIRsharing.364323)  file for printing, archival or further analysis.|N/A|DNA, Sequencing, Model (URL_TO_INSERT_TERM_2820 https://fairsharing.org/search?recordType=model_and_format)  organisms, Sequence analysis|Web application|
|[NCBI Resources](https://bio.tools/ncbi_resources)|Analysis and retrieval resources for the data in GenBank (URL_TO_INSERT_RECORD-ABBREV_2825 https://fairsharing.org/FAIRsharing.9kahy4)  and other biological data made available through the NCBI web site.|Open Access|Data mining, Data integration and warehousing, Database (URL_TO_INSERT_TERM_2823 https://fairsharing.org/search?fairsharingRegistry=Database)  management, Molecular interactions, pathways and networks, Rare diseases|Web Application, Database (URL_TO_INSERT_TERM_2824 https://fairsharing.org/search?fairsharingRegistry=Database)  portal|
|[CPAD](https://bio.tools/cpad)|Curated Protein (URL_TO_INSERT_RECORD-ABBREV_2829 https://fairsharing.org/FAIRsharing.rtndct)  Aggregation Database (URL_TO_INSERT_TERM_2826 https://fairsharing.org/search?fairsharingRegistry=Database)  (CPAD) is an integrated database (URL_TO_INSERT_TERM_2827 https://fairsharing.org/search?fairsharingRegistry=Database)  which contains informat (URL_TO_INSERT_TERM_2828 https://fairsharing.org/search?recordType=model_and_format) ion related to amyloidogenic proteins, Aggregation prone regions, aggregation kinetics and structure of proteins relevant to aggregation.|N/A|Proteomics, Data submission, annotation and curation, Proteins, Small molecules, Literature and language|Data Portal|
|[GenomicsDB](https://bio.tools/GenomicsDB)|Advancing clinical cohort selection with genomics analysis on a distributed platform. Highly performant data storage in C++ for importing, querying and transforming variant data with Java/Spark. Used in gatk4.|MIT License|Exome sequencing, Systems medicine (URL_TO_INSERT_RECORD-NAME_2830 https://fairsharing.org/3536) , Personalised medicine, Complementary medicine, Biobank|Command-line|
|[Epiviz File Server](https://bio.tools/epivizFileServer)|A library to query and transform genomic data from indexed files|MIT License|Oncology,Workflows, DNA|Python Library|

<!-- <h3 id=Data-transformation>Data transformation</h3> -->

### Data transformation

`Data transformat (URL_TO_INSERT_TERM_2832 https://fairsharing.org/search?recordType=model_and_format) ion` is the process of converting the data format (URL_TO_INSERT_TERM_2833 https://fairsharing.org/search?recordType=model_and_format) , structure, and value for a specific goal, which may include meeting a specific data standard (URL_TO_INSERT_TERM_2831 https://fairsharing.org/search?fairsharingRegistry=Standard) s.

Below are listed common operations in data transformat (URL_TO_INSERT_TERM_2834 https://fairsharing.org/search?recordType=model_and_format) ion:

- Data annotation
    The process of labeling data or metadata.
- Data validation
    The process of ensuring data has met data standard (URL_TO_INSERT_TERM_2835 https://fairsharing.org/search?fairsharingRegistry=Standard) s both in terms of data content and data format (URL_TO_INSERT_TERM_2836 https://fairsharing.org/search?recordType=model_and_format) .
- Data aggregation
    The process of gathering data and presenting it, usually, in a summarized format (URL_TO_INSERT_TERM_2837 https://fairsharing.org/search?recordType=model_and_format) .



**Manually curated list of tools**

|Tool|Description|License|Topics|Resource type|
|---|--|--|--|--|
|[SDTM](https://www.cdisc.org/standards/foundational/sdtm)|SDTM provides a standard (URL_TO_INSERT_TERM_2838 https://fairsharing.org/search?fairsharingRegistry=Standard)  for organizing and format (URL_TO_INSERT_TERM_2842 https://fairsharing.org/search?recordType=model_and_format) ting data to streamline processes in collection (URL_TO_INSERT_TERM_2841 https://fairsharing.org/search?recordType=collection)  management analysis and reporting.|N/A|data aggregation, data warehousing, Standard (URL_TO_INSERT_TERM_2839 https://fairsharing.org/search?fairsharingRegistry=Standard)  for Exchange of Non-clinical Data|Data standard (URL_TO_INSERT_TERM_2840 https://fairsharing.org/search?fairsharingRegistry=Standard) 
|[TriFacta](https://www.trifacta.com)|A data preparation tool for data quality improvement, data transformat (URL_TO_INSERT_TERM_2843 https://fairsharing.org/search?recordType=model_and_format) ion, and building data pipelines.|Commercial license|
|[OMOP](https://www.ohdsi.org/data-standardization/the-common-data-model/)|The OMOP Common Data Model (URL_TO_INSERT_TERM_2845 https://fairsharing.org/search?recordType=model_and_format)  allows for the systematic analysis of disparate observational database (URL_TO_INSERT_TERM_2844 https://fairsharing.org/search?fairsharingRegistry=Database) s.|N/A|Data transformat (URL_TO_INSERT_TERM_2847 https://fairsharing.org/search?recordType=model_and_format) ion|Data model (URL_TO_INSERT_TERM_2846 https://fairsharing.org/search?recordType=model_and_format) |
|[Collibra](https://www.collibra.com/)|an enterprise-oriented data governance platform that provides tools for data management and stewardship.|Commercial license|Data catalogue,data governance, data linkage|
|[Apache Hadoop](https://hadoop.apache.org/)|A framework that allows for the distributed processing of large data sets across clusters of computers using simple programming model (URL_TO_INSERT_TERM_2848 https://fairsharing.org/search?recordType=model_and_format) s. It is designed to scale up from single servers to thousands of machines|[Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)|Distributed computing|
|[Talend](https://www.talend.com/products/integrate-data/)|A unified approach that combines rapid data integration, transformat (URL_TO_INSERT_TERM_2849 https://fairsharing.org/search?recordType=model_and_format) ion, and mapping with automated quality checks to ensure trustworthy data in every step.|Commercial license|Data integration|
|[Informatica](https://www.informatica.com/)|Connect & fetch data from different heterogeneous source and processing of data.|Commercial license|Data integration|

__Automatically created list of tools by querying [Bio.Tools](https://bio.tools).__

|Tool|Description|License|Topics|Resource type|
|---|--|--|--|--|
|[OpenRefine-metadata-extension](https://github.com/FAIRDataTeam/OpenRefine-metadata-extension)| Enables a post-hoc FAIRification workflow: load an existing dataset, perform data wrangling tasks, add FAIR (URL_TO_INSERT_RECORD-ABBREV_2850 https://fairsharing.org/FAIRsharing.WWI10U)  attributes to the data, generate a linked data version of the data and, finally, push the result to an online FAIR (URL_TO_INSERT_RECORD-ABBREV_2851 https://fairsharing.org/FAIRsharing.WWI10U)  data infrastructure to make it accessible and discoverable.|MIT License|Data submission, Annotation and curation, Data identity and mapping|Extension|
|[DISQOVER](https://bio.tools/discover)|Data integration platform for public, licensed and internal data. The Data Ingestion Engine enables transforming data into Linked Data which can be searched, navigated and analysed via the user interface and the API.|N/A|Biomedical science, Omics, Biology, Chemistry (URL_TO_INSERT_RECORD-NAME_2852 https://fairsharing.org/3524) , Medicine|--|
|[PGA](https://bio.tools/pga)|Construction of customized protein database (URL_TO_INSERT_TERM_2853 https://fairsharing.org/search?fairsharingRegistry=Database) s based on RNA-Seq data with/without genome guided, database (URL_TO_INSERT_TERM_2854 https://fairsharing.org/search?fairsharingRegistry=Database)  searching, post-processing and report generation.|GPL-2.0|Proteomics, Proteomics experiment, Data submission, annotation and curation, Data integration and warehousing, Database (URL_TO_INSERT_TERM_2855 https://fairsharing.org/search?fairsharingRegistry=Database)  management, Data governance, RNA-seq| R library|
|[Query Tabular](https://bio.tools/Query_Tabular)|Galaxy-based tool which manipulates tabular files. Query Tabular automatically creates a SQLite database (URL_TO_INSERT_TERM_2856 https://fairsharing.org/search?fairsharingRegistry=Database)  directly from a tabular file within a Galaxy workflow. The SQLite database (URL_TO_INSERT_TERM_2857 https://fairsharing.org/search?fairsharingRegistry=Database)  can be saved to the Galaxy history, and further process to generate tabular outputs containing desired informat (URL_TO_INSERT_TERM_2858 https://fairsharing.org/search?recordType=model_and_format) ion and format (URL_TO_INSERT_TERM_2859 https://fairsharing.org/search?recordType=model_and_format) ting.|CC-BY-4.0|Bioinformat (URL_TO_INSERT_TERM_2860 https://fairsharing.org/search?recordType=model_and_format) ics,Workflows|Galaxy-based|
|[ms-data-core-api](https://bio.tools/ms-data-core-api)|The primary purpose of ms-data-cor (URL_TO_INSERT_RECORD-NAME_2863 https://fairsharing.org/FAIRsharing.xMmOCL)  (URL_TO_INSERT_RECORD-ABBREV_2864 https://fairsharing.org/FAIRsharing.m283c) e-api library is to provide commonly used classes and Object Model (URL_TO_INSERT_TERM_2862 https://fairsharing.org/search?recordType=model_and_format)  for Proteomics Experiments. You may also find it useful for your own computational proteomics project (URL_TO_INSERT_TERM_2861 https://fairsharing.org/search?recordType=project) s.|Apache-2.0|Proteomics, Proteomics experiment, Software engineering|Java Library|

<!-- <h3 id=Data-deposition>Data deposition</h3> -->

### Data Deposition

`Data deposition` is the process of loading data to hosting (end) destinations, such as public data archives and data warehouses.

__Manually curated list of tools__

|Tool|Description|License|Topics|Resource type|
|---|--|--|--|--|
|[REDCap](https://www.project-redcap.org/)|REDCap is a secure web application for building and managing online surveys and database (URL_TO_INSERT_TERM_2865 https://fairsharing.org/search?fairsharingRegistry=Database) s. While REDCap can be used to collect virtually any type of data in any environment|[REDCap License Terms](https://projectredcap.org/partners/termsofuse/)|Cloud migration|Web application|
|[TransMART](https://github.com/transmart)|An open-source data warehouse designed to store large amounts of clinical data from clinical trials, as well as data from basic research|[GPL-3.0 License](https://github.com/transmart/transmartApp/blob/master/LICENSE.TXT)|Data storage, clinical data|
|[Stardog](https://www.stardog.com/)|Triple Store Database (URL_TO_INSERT_TERM_2866 https://fairsharing.org/search?fairsharingRegistry=Database) , Provide an enterprise knowledge graph as FAIR (URL_TO_INSERT_RECORD-ABBREV_2867 https://fairsharing.org/FAIRsharing.WWI10U) + data catalogue|Commercial license|Data integration,data catalog|
|[Postgresql](https://www.postgresql.org/)|A free and open-source relational database (URL_TO_INSERT_TERM_2868 https://fairsharing.org/search?fairsharingRegistry=Database)  management system (RDBMS) emphasizing extensibility and SQL compliance.|[The PostgreSQL Licence](https://www.postgresql.org/about/licence/)|Relational database (URL_TO_INSERT_TERM_2869 https://fairsharing.org/search?fairsharingRegistry=Database) |

__Automatically created list of tools by querying [Bio.Tools](https://bio.tools).__

|Tool|Description|License|Topics|Resource type|
|---|--|--|--|--|
|[Chemotion](https://bio.tools/chemotion)|Repository for chemistry (URL_TO_INSERT_RECORD-NAME_2873 https://fairsharing.org/3524)  research data that provides solutions for current challenges to store research data in a feasible manner, allowing the conservation of domain specific informat (URL_TO_INSERT_TERM_2871 https://fairsharing.org/search?recordType=model_and_format) ion in a machine readable format (URL_TO_INSERT_TERM_2872 https://fairsharing.org/search?recordType=model_and_format) . |CC-BY-4.0|Data submission, annotation and curation, Workflows, Chemistry (URL_TO_INSERT_RECORD-NAME_2874 https://fairsharing.org/3524) |Data repository (URL_TO_INSERT_TERM_2870 https://fairsharing.org/search?recordType=repository) |

### Example use case: 

To show how some of these tools may be used, the following related recipes provide further guidance with real life examples.


1. {ref}`fcb-interop-fastqval`
   
<!--
2. OMOP ETL [link]( TODO link to recipe) (*in prepartion*)
3. RDF ETL [link]( TODO link to recipe)  (*in prepartion*)
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



