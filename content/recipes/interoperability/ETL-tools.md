(fcb-interop-etl)=

# Extraction, transformation, and loading process

````{panels_fairplus}
:identifier_text: FCB031
:identifier_link: 'https://w3id.org/faircookbook/FCB031'
:difficulty_level: 5
:recipe_type: survey_review
:reading_time_minutes: 15
:intended_audience: data_curator, data_manager, data_scientist  
:has_executable_code: nope
:recipe_name: Extraction, transformation, and loading process
```` 


## Main Objectives

This recipe identifies tools for `data extraction`, `transformation`, and `loading` (ETL). 
ETL is the process of collecting data from one source to persist it in another designated system in which the data is represented differently [1].
A common use case in data science is to build a scalable and portable ETL system to extract data from various sources, transform said-data into a cohesive dataset, and load the data to an internal or public database to support data exploration.

This recipe aims to serve as a start point for designing ETL workflows, rather than provide a comprehensive list covering all available tools.

>The lists of tools are generated either by manual curation, which reflects what is being used in the industry, or automatally discovered from the bio.tools repository.

```{warning} 
The content in these tables was generated in March 2021.
For an updated contents, please check the [FAIR tooling repository](https://github.com/FAIRplus/WP3_FAIR_tooling).
To provide feedback on this content or report issues, please do so via the [FAIR Cookbook github issue tracker](https://github.com/FAIRplus/the-fair-cookbook/issues)
```

## Graphical Overview

The figure below shows different ETL-related operations and their relationships, together with related tools and recipes.

 
```{figure} ETL-tools-mermaid.png
---
width: 800px
name: Overview of key aspects in ETL process
alt: Overview of key aspects in ETL process
---
Overview of key aspects in ETL process
```


The table below is an overview of ETL tools identified.
Details of each tools are also provided in this doc.
For ETL tools for RDF data model, please check the dedicated recipe<!-- {ref}`fcb-interop-etl2rdf-tools` -->.


<table>
  <tr>
   <td><strong><a href=#Data-query-and-retrieval>Data query and retrieval</a></strong>
   </td>
   <td><strong><a href=#Data-transformation>Data transformation</a></strong>
   </td>
   <td><strong><a href=#Data-deposition>Data deposition</a></strong>
   </td>
  </tr>
  <tr>
   <td><a href="https://www.tamr.com/">TAMR</a>
   </td>
   <td><a href="https://www.cdisc.org/standards/foundational/sdtm">SDTM</a>
   </td>
   <td><a href="https://www.project-redcap.org/">REDCap</a>
   </td>
  </tr>
  <tr>
   <td><a href="https://github.com/google-research/bert">Bert</a>
   </td>
   <td><a href="https://www.trifacta.com">TriFacta</a>
   </td>
   <td><a href="https://github.com/transmart">TransMART</a>
   </td>
  </tr>
  <tr>
   <td><a href="https://www.scibite.com/platform/termite/">Termite</a>
   </td>
   <td><a href="https://www.ohdsi.org/data-standardization/the-common-data-model/">OMOP</a>
   </td>
   <td><a href="https://www.stardog.com/">Stardog</a>
   </td>
  </tr>
  <tr>
   <td><a href="https://www.oracle.com/uk/industries/life-sciences/clinical-research/">Oracle clinical</a>
   </td>
   <td><a href="https://www.collibra.com/">Collibra</a>
   </td>
   <td><a href="https://www.postgresql.org/">Postgresql</a>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/geoboost2">GeoBoost2</a>
   </td>
   <td><a href="https://hadoop.apache.org/">Apache Hadoop</a>
   </td>
   <td><a href="https://bio.tools/chemotion">Chemotion</a>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/martview">MartView</a>
   </td>
   <td><a href="https://www.talend.com/products/integrate-data/">Talend</a>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/CLOBNET">CLOBNET</a>
   </td>
   <td><a href="https://www.informatica.com/">Informatica</a>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/PDBUSQLExtractor">PDBUSQLExtractor</a>
   </td>
   <td><a href="https://github.com/FAIRDataTeam/OpenRefine-metadata-extension">OpenRefine-metadata-extension</a>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/repo">repo</a>
   </td>
   <td><a href="https://bio.tools/discover">DISQOVER</a>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/snpator">SNPator</a>
   </td>
   <td><a href="https://bio.tools/Query_Tabular">Query Tabular</a>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/PyGMQL">PyGMQL</a>
   </td>
   <td><a href="https://bio.tools/ms-data-core-api">ms-data-core-api</a>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/plantpis">PlantPIs</a>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/baget">BAGET</a>
   </td>
   <td><a href=""></a>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/ncbi_resources">NCBI Resources</a>
   </td>
   <td><a href=""></a>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/cpad">CPAD</a>
   </td>
   <td><a href=""></a>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/GenomicsDB">GenomicsDB</a>
   </td>
   <td><a href=""></a>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/epivizFileServer">Epiviz File Server</a></a>
   </td>
   <td><a href=""></a>
   </td>
   <td>
   </td>
  </tr>
  
</table>

```{warning} 
The tools list below aims to provide an basic overview of what is there on the market. It is *not* a formal recommendation. If you think key tools are missing or the list needs an update, please contact us via the [github issue tracker](https://github.com/FAIRplus/the-fair-cookbook/issues).
```


## Requirements

* Knowledge requirement:

   * General familiarity with data cleaning, data loading tasks.

---

## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Interoperability | minimal | automated |


----

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [data retrieval](http://edamontology.org/operation_2422)  | 
| [validation](http://edamontology.org/operation_2428)||
| [data deposition](http://edamontology.org/operation_3431)||
| [data submission, annotation and curation](http://edamontology.org/topic_0219)| |


___

## Operations

<!-- <h3 id=Data-query-and-retrieval>Data query and retrieval</h3> -->

`Data query and retrieval` is the process of extracting structured or unstructured data from different sources. The process of identifying and obtaining data from data management systems.

__Manually curated list of tools__

|Tool|Description|License|Topics|Resource type|
|---|--|--|--|--|
|[TAMR](https://www.tamr.com/)|A cloud-native data mastering solution (cloud MDM) accelerate analytics through machine learning (ML), available on Google Cloud, Azure and AWS.|Commercial license|information integration, data unification|
|[Bert](https://github.com/google-research/bert)|Bidirectional Encoder Representations from Transformers (BERT) is a Transformer-based machine learning technique for natural language processing (NLP) pre-training developed by Google, aiming to extractcontext-sensitive features from an input text.  |Apache License 2.0|relationship extraction|Data model|
|[Termite](https://www.scibite.com/platform/termite/)|TERMite (TERM identification, tagging & extraction) is a fast named entity recognition (NER) and extraction engine for semantic analytics.|Commercial license|information extraction|
|[Oracle clinical](https://www.oracle.com/uk/industries/life-sciences/clinical-research/)|a single application and infrastructure for electronic data capture and clinical data management, while leveraging the renowned Oracle database. Oracle Clinical enables management of all clinical trial data in a single system, improving accuracy, visibility, and data integrity.|Commercial license|Clinical data|

__Automatically created list of tools by querying [Bio.Tools](https://bio.tools).__

|Tool|Description|License|Topics|Resource type|
|---|--|--|--|--|
|[GeoBoost2](https://bio.tools/geoboost2)|A natural languageprocessing pipeline for GenBank metadata enrichment for virus phylogeography.|Apache-2.0 License|Biotechnology, Natural language processing, Workflows, Public health and epidemiology, Infectiousdisease|Web application|
|[MartView](https://bio.tools/martview)|Tool for data retrieval and data mining that integrates data from Ensembl. Through the web interface it allows you to apply a series of filters to create custom datasets which can be converted to several useful output formats.| N/A |Pathology, Data integration and warehousing, Database management, Molecular interactions, pathways and networks, Gene transcripts|Web Application|
|[CLOBNET](https://bio.tools/CLOBNET)|Cloud-based machine learning system (CLOBNET) that is an open-source, lean infrastructure for electronic health record (EHR) data integration and is capable of extract, transform, and load (ETL) processing|BSD-2-Clause|Machine learning, Medicines research and development|Web application (for internal use)|
|[PDBUSQLExtractor](https://bio.tools/PDBUSQLExtractor)|Scalable Extraction of Big Macromolecular Data in Azure Data Lake Environment.|GPL-3.0|Nucleic acid structure analysis|C# library|
|[repo](https://bio.tools/repo)|A data manager meant to avoid manual storage/retrieval of data to/from the file system. It builds one (or more) centralized repository where R objects are stored with rich annotations, including corresponding code chunks, and easily searched and retrieved.|GPL-3.0|Data submission, annotation and curation, Data management, Database management|R library|
|[SNPator](https://bio.tools/snpator)|Originally designed to help CeGen users to handle, retrieve, transform and analyze the genetic data generated by the genotyping facilities of the institution. However, it is also open to external users who may want to upload their own genotyped data in order to take advantage its data processing features. Users will be able to perform a set of operations which may range from very simple format transformations to some complex biostatistical calculations.|N/A|Bioinformatics, Data quality management, Genetic variation, GWAS study|Web Application|
|[PyGMQL](https://bio.tools/PyGMQL)|Scalable data extraction and analysis for heterogeneous genomic datasets. Based on GMQL.|Apache-2.0|Imaging, Workflows, Database management|Python Library|

__Data portals with extraction functionalities discovered from [Bio.Tools](https://bio.tools).__

|Tool|Description|License|Topics|Resource type|
|---|--|--|--|--|
|[PlantPIs](https://bio.tools/plantpis)|Web querying system for a database collecting plant protease inhibitors data.|Plant biology, Gene and protein families|Database Portal|
|[BAGET](https://bio.tools/baget)|Web service designed to facilitate extraction of specific gene and protein sequences from completely determined prokaryotic genomes. Query results can be exported as a rich text format file for printing, archival or further analysis.|N/A|DNA, Sequencing, Model organisms, Sequence analysis|Web application|
|[NCBI Resources](https://bio.tools/ncbi_resources)|Analysis and retrieval resources for the data in GenBank and other biological data made available through the NCBI web site.|Open Access|Data mining, Data integration and warehousing, Database management, Molecular interactions, pathways and networks, Rare diseases|Web Application, Database portal|
|[CPAD](https://bio.tools/cpad)|Curated Protein Aggregation Database (CPAD) is an integrated database which contains information related to amyloidogenic proteins, Aggregation prone regions, aggregation kinetics and structure of proteins relevant to aggregation.|N/A|Proteomics, Data submission, annotation and curation, Proteins, Small molecules, Literature and language|Data Portal|
|[GenomicsDB](https://bio.tools/GenomicsDB)|Advancing clinical cohort selection with genomics analysis on a distributed platform. Highly performant data storage in C++ for importing, querying and transforming variant data with Java/Spark. Used in gatk4.|MIT License|Exome sequencing, Systems medicine, Personalised medicine, Complementary medicine, Biobank|Command-line|
|[Epiviz File Server](https://bio.tools/epivizFileServer)|A library to query and transform genomic data from indexed files|MIT License|Oncology,Workflows, DNA|Python Library|

<!-- <h3 id=Data-transformation>Data transformation</h3> -->

### Data transformation

`Data transformation` is the process of converting the data format, structure, and value for a specific goal, which may include meeting a specific data standards.

Below are listed common operations in data transformation:

- Data annotation
    The process of labeling data or metadata.
- Data validation
    The process of ensuring data has met data standards both in terms of data content and data format.
- Data aggregation
    The process of gathering data and presenting it, usually, in a summarized format.



**Manually curated list of tools**

|Tool|Description|License|Topics|Resource type|
|---|--|--|--|--|
|[SDTM](https://www.cdisc.org/standards/foundational/sdtm)|SDTM provides a standard for organizing and formatting data to streamline processes in collection management analysis and reporting.|N/A|data aggregation, data warehousing, Standard for Exchange of Non-clinical Data|Data standard
|[TriFacta](https://www.trifacta.com)|A data preparation tool for data quality improvement, data transformation, and building data pipelines.|Commercial license|
|[OMOP](https://www.ohdsi.org/data-standardization/the-common-data-model/)|The OMOP Common Data Model allows for the systematic analysis of disparate observational databases.|N/A|Data transformation|Data model|
|[Collibra](https://www.collibra.com/)|an enterprise-oriented data governance platform that provides tools for data management and stewardship.|Commercial license|Data catalogue,data governance, data linkage|
|[Apache Hadoop](https://hadoop.apache.org/)|A framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models. It is designed to scale up from single servers to thousands of machines|[Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)|Distributed computing|
|[Talend](https://www.talend.com/products/integrate-data/)|A unified approach that combines rapid data integration, transformation, and mapping with automated quality checks to ensure trustworthy data in every step.|Commercial license|Data integration|
|[Informatica](https://www.informatica.com/)|Connect & fetch data from different heterogeneous source and processing of data.|Commercial license|Data integration|

__Automatically created list of tools by querying [Bio.Tools](https://bio.tools).__

|Tool|Description|License|Topics|Resource type|
|---|--|--|--|--|
|[OpenRefine-metadata-extension](https://github.com/FAIRDataTeam/OpenRefine-metadata-extension)| Enables a post-hoc FAIRification workflow: load an existing dataset, perform data wrangling tasks, add FAIR attributes to the data, generate a linked data version of the data and, finally, push the result to an online FAIR data infrastructure to make it accessible and discoverable.|MIT License|Data submission, Annotation and curation, Data identity and mapping|Extension|
|[DISQOVER](https://bio.tools/discover)|Data integration platform for public, licensed and internal data. The Data Ingestion Engine enables transforming data into Linked Data which can be searched, navigated and analysed via the user interface and the API.|N/A|Biomedical science, Omics, Biology, Chemistry, Medicine|--|
|[PGA](https://bio.tools/pga)|Construction of customized protein databases based on RNA-Seq data with/without genome guided, database searching, post-processing and report generation.|GPL-2.0|Proteomics, Proteomics experiment, Data submission, annotation and curation, Data integration and warehousing, Database management, Data governance, RNA-seq| R library|
|[Query Tabular](https://bio.tools/Query_Tabular)|Galaxy-based tool which manipulates tabular files. Query Tabular automatically creates a SQLite database directly from a tabular file within a Galaxy workflow. The SQLite database can be saved to the Galaxy history, and further process to generate tabular outputs containing desired information and formatting.|CC-BY-4.0|Bioinformatics,Workflows|Galaxy-based|
|[ms-data-core-api](https://bio.tools/ms-data-core-api)|The primary purpose of ms-data-core-api library is to provide commonly used classes and Object Model for Proteomics Experiments. You may also find it useful for your own computational proteomics projects.|Apache-2.0|Proteomics, Proteomics experiment, Software engineering|Java Library|

<!-- <h3 id=Data-deposition>Data deposition</h3> -->

### Data Deposition

`Data deposition` is the process of loading data to hosting (end) destinations, such as public data archives and data warehouses.

__Manually curated list of tools__

|Tool|Description|License|Topics|Resource type|
|---|--|--|--|--|
|[REDCap](https://www.project-redcap.org/)|REDCap is a secure web application for building and managing online surveys and databases. While REDCap can be used to collect virtually any type of data in any environment|[REDCap License Terms](https://projectredcap.org/partners/termsofuse/)|Cloud migration|Web application|
|[TransMART](https://github.com/transmart)|An open-source data warehouse designed to store large amounts of clinical data from clinical trials, as well as data from basic research|[GPL-3.0 License](https://github.com/transmart/transmartApp/blob/master/LICENSE.TXT)|Data storage, clinical data|
|[Stardog](https://www.stardog.com/)|Triple Store Database, Provide an enterprise knowledge graph as FAIR+ data catalogue|Commercial license|Data integration,data catalog|
|[Postgresql](https://www.postgresql.org/)|A free and open-source relational database management system (RDBMS) emphasizing extensibility and SQL compliance.|[The PostgreSQL Licence](https://www.postgresql.org/about/licence/)|Relational database|

__Automatically created list of tools by querying [Bio.Tools](https://bio.tools).__

|Tool|Description|License|Topics|Resource type|
|---|--|--|--|--|
|[Chemotion](https://bio.tools/chemotion)|Repository for chemistry research data that provides solutions for current challenges to store research data in a feasible manner, allowing the conservation of domain specific information in a machine readable format. |CC-BY-4.0|Data submission, annotation and curation, Workflows, Chemistry|Data repository|

### Example use case: 

To show how some of these tools may be used, the following related recipes provide further guidance with real life examples.


1. {ref}`fcb-interop-fastqval`
2. OMOP ETL [link]() (*in prepartion*)
3. RDF ETL [link]()  (*in prepartion*)

___


## References

1. https://en.wikipedia.org/wiki/Extract,_transform,_load

___


## Authors

| Name                                                                                                                                                                            | Orcid                                                                                                         | Affiliation              | Type                                                                              |                                                              Elixir Node                                                              | Credit Role
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|--------------------------|-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------:|:----------------:|
| <div class="firstCol"><a target="_blank" href='https://github.com/fuqix'><img class='avatar-style' src='https://avatars.githubusercontent.com/fuqix'></img><div class="d-block">Fuqi Xu</div></a>   </div>      | <a target="_blank" href='https://orcid.org/0000-0002-5923-3859'><i class='fab fa-orcid fa-2x text--orange'></i></a> | EMBL-EBI      | <i class="fas fa-graduation-cap fa-1x text--orange" alt="Academic"></i> | | Writing - Original Draft
| <div class="firstCol"><a target="_blank" href='https://github.com/evaMart'><img class='avatar-style' src='https://avatars.githubusercontent.com/EvaMart'></img><div class="d-block">Eva Marin del Pico</div></a></div>   | <a target="_blank" href='https://orcid.org/0000-0001-8324-2897'><i class='fab fa-orcid fa-2x text--orange'></i></a> | Barcelona Supercomputing Centre | <i class="fas fa-graduation-cap fa-1x text--orange" alt="Academic"></i> | <img class='elixir-style' src='/the-fair-cookbook/_static/images/logo/Elixir/ELIXIR-ES.svg' ></img> | Writing - Original Draft
| <div class="firstCol"><img class='avatar-style' src='https://avatars.githubusercontent.com/no-github'></img><div class="d-block">Sukhi Singh</div>        </div> |  <a target="_blank" href='https://orcid.org/0000-0001-8324-2897'><i class='fab fa-orcid fa-2x text--orange'></i></a>  | The Hyve      | <i class="fas fa-project-diagram fa-1x" style="color:#300861;" alt="SME"></i>    | | Tool curation
| <div class="firstCol"><a target="_blank" href='https://github.com/proccaserra'><img class='avatar-style' src='https://avatars.githubusercontent.com/proccaserra'></img><div class="d-block">Philippe Rocca-Serra</div></a>  </div>         | <a target="_blank" href='https://orcid.org/0000-0001-9853-5668'><i class='fab fa-orcid fa-2x text--orange'></i></a> | University of Oxford     | <i class="fas fa-graduation-cap fa-1x text--orange" alt="Academic"></i> | <img class='elixir-style' src='/the-fair-cookbook/_static/images/logo/Elixir/ELIXIR-UK.svg' ></img> | Writing – Review & Editing |


___

## License

This page is released under the Creative Commons 4.0 BY license.

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>



