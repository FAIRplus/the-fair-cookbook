(fcb-interop-onto-op)=
# Ontology-related tools and services


````{panels_fairplus}
:identifier_text: FCB022
:identifier_link: https://w3id.org/faircookbook/FCB022
:difficulty_level: 5
:recipe_type: survey_review
:reading_time_minutes: 15
:intended_audience: data_curator, data_manager, data_scientist, ontologist, software_engineer, terminology_manager 
:maturity_level: 0
:maturity_indicator: 0
:has_executable_code: nope
:recipe_name: Introducing ontology-related tools and services
```` 


## Main Objectives

This recipe aims to provide `an overview of tools available` to perform a number of key operations using ontologies (URL_TO_INSERT_TERM_3944 https://fairsharing.org/search?recordType=terminology_artefact)  and relevant to FAIR (URL_TO_INSERT_RECORD-ABBREV_3945 https://fairsharing.org/FAIRsharing.WWI10U)  processes: from `ontology (URL_TO_INSERT_TERM_3941 https://fairsharing.org/search?recordType=terminology_artefact)  management` to using `ontology (URL_TO_INSERT_TERM_3942 https://fairsharing.org/search?recordType=terminology_artefact)  for annotation` or `performing ontology (URL_TO_INSERT_TERM_3943 https://fairsharing.org/search?recordType=terminology_artefact)  mapping`.

It aims to serve as a starting point to identify tools for FAIRification tasks where ontologies (URL_TO_INSERT_TERM_3946 https://fairsharing.org/search?recordType=terminology_artefact)  and semantic frameworks are needed. 

```{admonition} disclaimer
It is not intended to provide a comprehensive list covering all possible tools.
```

>The lists of tools are generated either automatically by querying the [bio.tools](https://bio.tools/) repository (URL_TO_INSERT_TERM_3947 https://fairsharing.org/search?recordType=repository) , or through manual curation. In this last instance, the list produced reflects what is being used in the industry and is influenced by the FAIRplus project (URL_TO_INSERT_TERM_3948 https://fairsharing.org/search?recordType=project)  partners that have been surveyed for the purpose of this work.

```{warning} 
The content in these tables was generated in March 2021.
For an updated contents, please check the [FAIR tooling repository](https://github.com/FAIRplus/WP3_FAIR_tooling).
```


## Requirements

* recipe dependency:
   * {ref}`fcb-selecting-ontologies (URL_TO_INSERT_TERM_3949 https://fairsharing.org/search?recordType=terminology_artefact) `
* knowledge requirement:
   * be familiar with ontologies (URL_TO_INSERT_TERM_3950 https://fairsharing.org/search?recordType=terminology_artefact)  and semantic annotation.

---

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [ontology and terminology](http://edamontology.org/topic_0089)  | 
| [text annotation](http://edamontology.org/operation_3778)  |

---
## Overview

The figure below shows different ontology (URL_TO_INSERT_TERM_3951 https://fairsharing.org/search?recordType=terminology_artefact) -related operations and their relationships, together with related tools and recipes.


````{dropdown} 
:open: 
```{figure} ontology-operations-mermaid.png
---
width: 700px
name: Overview of key aspects in ontology (URL_TO_INSERT_TERM_3952 https://fairsharing.org/search?recordType=terminology_artefact)  associated processes
alt: Overview of key aspects in ontology (URL_TO_INSERT_TERM_3953 https://fairsharing.org/search?recordType=terminology_artefact)  associated processes
---
Overview of key aspects in ontology (URL_TO_INSERT_TERM_3954 https://fairsharing.org/search?recordType=terminology_artefact)  associated processes
```
````

The table below is an overview of ontology (URL_TO_INSERT_TERM_3955 https://fairsharing.org/search?recordType=terminology_artefact)  strategies tools identified. Details of each tools are provided below.

|         Topic        |       Curated tools      |   Related tools in Bio.tools (URL_TO_INSERT_RECORD-NAME_3956 https://fairsharing.org/FAIRsharing.63520c)    |
|:--------------------:|:------------------------:|:------------------------------:|
| Ontology (URL_TO_INSERT_TERM_3957 https://fairsharing.org/search?recordType=terminology_artefact)  annotation  | ZOOMA                    | bioBERT                        |
|                      | NCBI BioPortal (URL_TO_INSERT_RECORD-NAME_3958 https://fairsharing.org/FAIRsharing.4m97ah)  Annotator | PPR-SSM                        |
|                      | BioBert                  | HPO2GO                         |
|                      | Termite                  | Vapur                          |
|                      | PoolParty Semantic Suite | matscholar                     |
|                      | OntoMaton                | CollaboNet                     |
|                      | Prodigy                  | Calchas                        |
|                      | OntoText                 | QTL TableMiner++(QTM)          |
|                      |                          | thbp                           |
| Ontology (URL_TO_INSERT_TERM_3959 https://fairsharing.org/search?recordType=terminology_artefact)  mapping     | OxO (URL_TO_INSERT_RECORD-ABBREV_3960 https://fairsharing.org/FAIRsharing.0c6fea)                       | meshr                          |
|                      |                          | locdb                          |
| Ontology (URL_TO_INSERT_TERM_3961 https://fairsharing.org/search?recordType=terminology_artefact)  management  | AberOWL                  | ngly1                          |
|                      | BioPortal (URL_TO_INSERT_RECORD-NAME_3962 https://fairsharing.org/FAIRsharing.4m97ah)                 | Doc2Hpo                        |
|                      | Centree Ontology (URL_TO_INSERT_TERM_3963 https://fairsharing.org/search?recordType=terminology_artefact)  Manager | PlanGexQ                       |
|                      | OLS (URL_TO_INSERT_RECORD-ABBREV_3964 https://fairsharing.org/FAIRsharing.Mkl9RR)                       | GOcats                         |
|                      | Ontobee (URL_TO_INSERT_RECORD-NAME_3965 https://fairsharing.org/FAIRsharing.q8fx1b)                   | RDFScape                       |
|                      | PoolParty                | OntoBrowser                    |
|                      |                          | QuickGO                        |
|                      |                          | Circular Gene Ontology (URL_TO_INSERT_TERM_3966 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD-NAME_3967 https://fairsharing.org/FAIRsharing.6xq0ee)  (CirGO) |
| Ontology (URL_TO_INSERT_TERM_3968 https://fairsharing.org/search?recordType=terminology_artefact)  engineering | eNanoMapper Slimmer      |                                |
|                      | OWLAPI                   |                                |
|                      | Protégé                  |                                |
|                      | ROBOT                    |                                |
|                      | TopBraid Composer        |                                |
|                      | VocBench                 |                                |

---
## Operations

### Ontology annotation

Ontoloy Annotation is the process of linking free text or data items to 'tokens' (defined terms from a lexicon) which provide semantic value. For example,  "type 2 diabetes" can be annotated with corresponding [term](http://purl.obolibrary.org/obo/MONDO_0005148) in the MONDO (URL_TO_INSERT_RECORD-ABBREV_3970 https://fairsharing.org/FAIRsharing.b2979t)  disease ontology (URL_TO_INSERT_TERM_3969 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD-NAME_3971 https://fairsharing.org/FAIRsharing.8b6wfq) . 

__Curated tools__

|Tool|Description|License|Topics|Resource Type|How to use|
|---|--|--|--|--|--|
|[ZOOMA](https://www.ebi.ac.uk/spot/zooma/)|A tool for mapping free text annotations to ontology (URL_TO_INSERT_TERM_3974 https://fairsharing.org/search?recordType=terminology_artefact)  term based on a curated repository (URL_TO_INSERT_TERM_3972 https://fairsharing.org/search?recordType=repository)  of annotation knowledge.|[EMBL-EBI Terms of Use](https://www.ebi.ac.uk/about/terms-of-use/)|Ontology and terminology (URL_TO_INSERT_TERM_3973 https://fairsharing.org/search?recordType=terminology_artefact) ,<br>Systems biology,<br>Data identity and mapping|Web application,<br> API|[ZOOMA-Getting started](https://www.ebi.ac.uk/spot/zooma/docs/search)|
|[NCBI BioPortal Annotator](https://bioportal.bioontology.org/annotatorplus)|Get annotations for biomedical text with classes from the ontologies (URL_TO_INSERT_TERM_3976 https://fairsharing.org/search?recordType=terminology_artefact) .|[BioPor (URL_TO_INSERT_RECORD-NAME_3977 https://fairsharing.org/FAIRsharing.4m97ah) tal Terms of Use](https://www.bioontology.org/terms/)|Ontology and terminology (URL_TO_INSERT_TERM_3975 https://fairsharing.org/search?recordType=terminology_artefact) ,<br>Systems biology,<br>Data identity and mapping|Web application,<br> API|[BioPort (URL_TO_INSERT_RECORD-NAME_3978 https://fairsharing.org/FAIRsharing.4m97ah) al help](https://bioportal.bioontology.org/help?pop=true#Annotator_Tab)|
|[BioBert](https://github.com/dmis-lab/biobert)|A biomedical language representation model (URL_TO_INSERT_TERM_3979 https://fairsharing.org/search?recordType=model_and_format)  designed for biomedical text mining tasks such as biomedical named entity recognition, relation extraction, question answering.|[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)|text mining,<br> named-entity recognition,<br> natural language processing|Python|
|[Termite](https://www.scibite.com/platform/termite/)|Semantic enrichment to unlock the value of unstructured text and simplify the identification of new potential biomarker leads from scientific text.|Commercial license|Ontology (URL_TO_INSERT_TERM_3981 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_3980 https://fairsharing.org/search?recordType=terminology_artefact) |
|[PoolParty Semantic Suite](https://semantic-web.com/poolparty-semantic-suite/)|Automate the handling of heterogeneous metadata systems and the creation of enterprise knowledge graphs.design knowledge graphs at your own pace and with speed. Create your own ontologies (URL_TO_INSERT_TERM_3982 https://fairsharing.org/search?recordType=terminology_artefact)  and custom schemes by reusing already existing ontologies (URL_TO_INSERT_TERM_3983 https://fairsharing.org/search?recordType=terminology_artefact)  such as FOAF, FIBO, schema.org (URL_TO_INSERT_RECORD-NAME_3984 https://fairsharing.org/FAIRsharing.hzdzq8)  and CHEBI, among others. Apply them to your existing taxonomies with ease.|Commercial license|Content enrichment,<br>Data integration|
|[OntoMaton](https://github.com/ISA-tools/OntoMaton)| A tool facilitating ontology (URL_TO_INSERT_TERM_3985 https://fairsharing.org/search?recordType=terminology_artefact)  search and tagging functionalities within Google Spreadsheets.|[CPAL license](https://opensource.org/licenses/CPAL-1.0)||Google Add-ons|
|[Prodigy](https://prodi.gy/)|A modern annotation tool for creating training and evaluation data for machine learning model (URL_TO_INSERT_TERM_3986 https://fairsharing.org/search?recordType=model_and_format) s. You can also use Prodigy to help you inspect and clean your data, do error analysis and develop rule-based systems to use in combination with your statistical model (URL_TO_INSERT_TERM_3987 https://fairsharing.org/search?recordType=model_and_format) s.|Commercial license|Data annotation|Python, Web application,API|
|[OntoText](https://www.ontotext.com/products/ontotext-platform/)|Connect and publish complex enterprise knowledge with standard (URL_TO_INSERT_TERM_3988 https://fairsharing.org/search?fairsharingRegistry=Standard) -compliant semantic graph database (URL_TO_INSERT_TERM_3989 https://fairsharing.org/search?fairsharingRegistry=Database) ; Customize and apply analytics to link documents to graphs, extract new facts, classify and recommend content.|Commercial license|

__Related tools in [Bio.Tools](https://bio.tools)__

| Tool| Description| License | Topics | Resource Type |
|-------|--------|---------|----|--------|
| [bioBERT](https://bio.tools/BioBERT) | A pre-trained weights of BioBERT, a language representation model (URL_TO_INSERT_TERM_3990 https://fairsharing.org/search?recordType=model_and_format)  for biomedical domain, especially designed for biomedical text mining tasks such as biomedical named entity recognition, relation extraction, question answering, etc.|  N/A | Medicine, Ontology (URL_TO_INSERT_TERM_3992 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_3991 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing  |Python|
|[PPR-SSM](https://bio.tools/PPR-SSM)| Personalized PageRank and semantic similarity measures for linking entities found in documents to concepts from domain-specific ontologies (URL_TO_INSERT_TERM_3995 https://fairsharing.org/search?recordType=terminology_artefact) . |N/A| Imaging, Natural language processing, Data mining, Genotype and phenotype, Ontology (URL_TO_INSERT_TERM_3994 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_3993 https://fairsharing.org/search?recordType=terminology_artefact)         |Java, Python|
|[HPO2GO](https://bio.tools/HPO2GO)| Prediction of human phenotype ontology (URL_TO_INSERT_TERM_3997 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD-NAME_4005 https://fairsharing.org/FAIRsharing.kbtt7f)  term associations using cross ontology (URL_TO_INSERT_TERM_3998 https://fairsharing.org/search?recordType=terminology_artefact)  annotation co-occurrences.Mapping between Human Phenotype Ontology (URL_TO_INSERT_TERM_3999 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD-NAME_4006 https://fairsharing.org/FAIRsharing.kbtt7f)  (HPO) and Gene Ontology (URL_TO_INSERT_TERM_4000 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD-NAME_4002 https://fairsharing.org/FAIRsharing.6xq0ee)  (GO (URL_TO_INSERT_RECORD-ABBREV_4003 https://fairsharing.org/FAIRsharing.6xq0ee) ) terms for the prediction of gene/protein - function - phenotype - disease associations.|[GPL-3.0](https://spdx.org/licenses/GPL-3.0)| Pathology, Protein (URL_TO_INSERT_RECORD-ABBREV_4004 https://fairsharing.org/FAIRsharing.rtndct)  interactions, Genotype and phenotype, Ontology (URL_TO_INSERT_TERM_4001 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_3996 https://fairsharing.org/search?recordType=terminology_artefact) , Gene expression| Command-line tool |
| [Vapur](https://bio.tools/vapur)| A Search Engine to Find Related Protein (URL_TO_INSERT_RECORD-ABBREV_4009 https://fairsharing.org/FAIRsharing.rtndct) .Vapur is an online entity-oriented search engine for the COVID-19 anthology. Vapur is empowered with a semantic inverted index that is created through named entity recognition and relation extraction on CORD-19 abstracts. |N/A| Pathology, Ontology (URL_TO_INSERT_TERM_4008 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_4007 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing, Enzymes |Python|
| [matscholar](https://bio.tools/matscholar)| A Python library for materials-focused natural language processing (NLP). Named Entity Recognition and Normalization Applied to Large-Scale Informat (URL_TO_INSERT_TERM_4010 https://fairsharing.org/search?recordType=model_and_format) ion Extraction from the Materials Science Literature.|[MIT](https://spdx.org/licenses/MIT)| Chemistry (URL_TO_INSERT_RECORD-NAME_4013 https://fairsharing.org/3524) , Ontology (URL_TO_INSERT_TERM_4012 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_4011 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing | Command-line tool |
|[CollaboNet](https://bio.tools/collabonet)| Collaboration of deep neural networks for biomedical named entity recognition.|[MIT](https://spdx.org/licenses/MIT)| Ontology (URL_TO_INSERT_TERM_4015 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_4014 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing, Machine learning | Command-line tool |
| [Calchas](https://bio.tools/calchas)| A web based framework that takes advantage of domain specific ontologies (URL_TO_INSERT_TERM_4021 https://fairsharing.org/search?recordType=terminology_artefact) , and Natural Language Processing, aiming to empower exploration of biomedical resources via semantic-based querying and search. The NLP engine analyzes the input free-text query and translates it into targeted queries with terms from the underlying ontology (URL_TO_INSERT_TERM_4019 https://fairsharing.org/search?recordType=terminology_artefact) . | N/A | Medical informat (URL_TO_INSERT_TERM_4016 https://fairsharing.org/search?recordType=model_and_format) ics, Ontology (URL_TO_INSERT_TERM_4020 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_4018 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing, Bioinformat (URL_TO_INSERT_TERM_4017 https://fairsharing.org/search?recordType=model_and_format) ics| Web application   |
|[QTL TableMiner++(QTM)](https://bio.tools/QTM) | It is a command-line tool to retrieve and semantically annotate results obtained from QTL mapping experiments. It takes full-text articles from the Europe PMC (URL_TO_INSERT_RECORD-ABBREV_4026 https://fairsharing.org/FAIRsharing.wpt5mp)  (URL_TO_INSERT_RECORD-ABBREV_4028 https://fairsharing.org/FAIRsharing.cmw6mm)  repository (URL_TO_INSERT_TERM_4023 https://fairsharing.org/search?recordType=repository)  as input and outputs the extracted QTLs into a relational database (URL_TO_INSERT_TERM_4022 https://fairsharing.org/search?fairsharingRegistry=Database)  (SQLite) and text file (CSV (URL_TO_INSERT_RECORD-ABBREV_4027 https://fairsharing.org/FAIRsharing.1943d4) ).|[Apache-2.0](https://spdx.org/licenses/Apache-2.0)| Ontology (URL_TO_INSERT_TERM_4025 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_4024 https://fairsharing.org/search?recordType=terminology_artefact) | Command-line tool |
| [thbp](https://bio.tools/thbp)| Mapping anatomical related entities to human body parts based on wikipedia in discharge summaries.|N/A| Anatomy, Ontology (URL_TO_INSERT_TERM_4030 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_4029 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing||

### Ontology mapping

The process of determining correspondences between equivalent concepts in alternative ontologies (URL_TO_INSERT_TERM_4031 https://fairsharing.org/search?recordType=terminology_artefact) , and other vocabularies. This may include mapping to convey different levels of granularity.

__Curated tools__

|Tool|Description|License|Topics|Resource Type|How to use|
|---|--|--|--|--|--|
|[OxO](https://www.ebi.ac.uk/spot/oxo/index)|A service for finding mappings (or cross-references) between terms from ontologies (URL_TO_INSERT_TERM_4033 https://fairsharing.org/search?recordType=terminology_artefact) , vocabularies and coding standard (URL_TO_INSERT_TERM_4032 https://fairsharing.org/search?fairsharingRegistry=Standard) s. |[EMBL-EBI Terms of Use](https://www.ebi.ac.uk/about/terms-of-use/)|Ontology alignment| GUI and API| |

__Related tools in [Bio.Tools](https://bio.tools)__

| Tool| Description| License | Topics     | Type|
|-------|--|---------|----|---|
|[meshr](https://bio.tools/meshr)| A set of annotation maps describing the entire MeSH assembled using data from MeSH. |[Apache-2.0](https://spdx.org/licenses/Apache-2.0)| Medical informat (URL_TO_INSERT_TERM_4034 https://fairsharing.org/search?recordType=model_and_format) ics, Data quality management  | Command-line tool, Library |
| [locdb](https://bio.tools/locdb) | Manually curated database (URL_TO_INSERT_TERM_4035 https://fairsharing.org/search?fairsharingRegistry=Database)  with experimental annotations for the subcellular localizations of proteins in Homo sapiens (HS, human) and Arabidopsis thaliana (AT, thale cress). | N/A | Ontology (URL_TO_INSERT_TERM_4038 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_4037 https://fairsharing.org/search?recordType=terminology_artefact) , Data submission, annotation and curation, Proteins | Database (URL_TO_INSERT_TERM_4036 https://fairsharing.org/search?fairsharingRegistry=Database)  portal|


### Ontology management

The process of managing ontologies (URL_TO_INSERT_TERM_4040 https://fairsharing.org/search?recordType=terminology_artefact)  and other vocabularies in semantic web-linked data environments.This includes policies (URL_TO_INSERT_TERM_4039 https://fairsharing.org/search?fairsharingRegistry=Policy)  for update and maintenance of constituent and new terms.

__Curated tools__

|Tool|Description|License|Topics|Resource Type|How to use|
|---|--|--|--|--|--|
|[OLS](https://www.ebi.ac.uk/ols/index)|a repository (URL_TO_INSERT_TERM_4041 https://fairsharing.org/search?recordType=repository)  for biomedical ontologies (URL_TO_INSERT_TERM_4044 https://fairsharing.org/search?recordType=terminology_artefact)  that aims to provide a single point of access to the latest ontology (URL_TO_INSERT_TERM_4043 https://fairsharing.org/search?recordType=terminology_artefact)  versions.|[EMBL-EBI Terms of Use](https://www.ebi.ac.uk/about/terms-of-use/)|Ontology and terminology (URL_TO_INSERT_TERM_4042 https://fairsharing.org/search?recordType=terminology_artefact) |Web Application, API|
|[BioPortal](https://bioportal.bioontology.org/)|A repository (URL_TO_INSERT_TERM_4045 https://fairsharing.org/search?recordType=repository)  of biomedical ontologies (URL_TO_INSERT_TERM_4047 https://fairsharing.org/search?recordType=terminology_artefact) .|[BioPor (URL_TO_INSERT_RECORD-NAME_4048 https://fairsharing.org/FAIRsharing.4m97ah) tal Terms of Use](https://www.bioontology.org/terms/)|Ontology and terminology (URL_TO_INSERT_TERM_4046 https://fairsharing.org/search?recordType=terminology_artefact) |Web Application, API|
|[PoolParty](https://www.poolparty.biz/) |Knowledge Engineering & Knowledge Graph Management. Taxonomy, ontology (URL_TO_INSERT_TERM_4050 https://fairsharing.org/search?recordType=terminology_artefact)  and linked dataset management. |Commercial license|Ontology (URL_TO_INSERT_TERM_4051 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_4049 https://fairsharing.org/search?recordType=terminology_artefact) |
|[Centree Ontology Manager](https://www.scibite.com/platform/centree/)|A centralised, enterprise-ready resource for ontology (URL_TO_INSERT_TERM_4052 https://fairsharing.org/search?recordType=terminology_artefact)  management and transforms the experience of maintaining and releasing ontologies (URL_TO_INSERT_TERM_4053 https://fairsharing.org/search?recordType=terminology_artefact)  for research-led businesses.|Commercial license||Web application, API|
|[Ontobee](http://www.ontobee.org/)|A linked data server designed for ontologies (URL_TO_INSERT_TERM_4055 https://fairsharing.org/search?recordType=terminology_artefact) . Ontobee (URL_TO_INSERT_RECORD-NAME_4056 https://fairsharing.org/FAIRsharing.q8fx1b)  is aimed to facilitate ontology (URL_TO_INSERT_TERM_4054 https://fairsharing.org/search?recordType=terminology_artefact)  data sharing, visualization, query, integration, and analysis.|[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)||Web application|
|[AberOWL](http://www.aber-owl.net/)|A framework for ontology (URL_TO_INSERT_TERM_4059 https://fairsharing.org/search?recordType=terminology_artefact) -based access to biological data. It consists of a repository (URL_TO_INSERT_TERM_4057 https://fairsharing.org/search?recordType=repository)  of bio-ontologies (URL_TO_INSERT_TERM_4061 https://fairsharing.org/search?recordType=terminology_artefact) , a set of webservices which provide access to OWL (URL_TO_INSERT_RECORD-ABBREV_4063 https://fairsharing.org/FAIRsharing.atygwy) (-EL) reasoning over the ontologies (URL_TO_INSERT_TERM_4062 https://fairsharing.org/search?recordType=terminology_artefact) , and several frontends which utilise the ontology (URL_TO_INSERT_TERM_4060 https://fairsharing.org/search?recordType=terminology_artefact)  repository (URL_TO_INSERT_TERM_4058 https://fairsharing.org/search?recordType=repository)  and reasoning services.|||Web application, API|


__Related tools in [Bio.Tools](https://bio.tools)__

| Tool| Description  | License | Topics | Type|
|---|--|--|--|--|
|[ngly1](https://bio.tools/ngly1)| A repository (URL_TO_INSERT_TERM_4064 https://fairsharing.org/search?recordType=repository)  for the NGLY1 Deficiency Knowledge Graph, the reasoning context to support hypothesis discovery for NGLY1 Deficiency-CDDG (DOID (URL_TO_INSERT_RECORD-ABBREV_4067 https://fairsharing.org/FAIRsharing.8b6wfq) :0060728) research. The user can navigate the knowledge in the graph in the Neo4j Browser website. | N/A  | Molecular interactions, pathways and networks, Ontology (URL_TO_INSERT_TERM_4066 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_4065 https://fairsharing.org/search?recordType=terminology_artefact) , Machine learning       | Command-line tool |
| [Doc2Hpo](https://bio.tools/doc2hpo) | Web application for efficient and accurate Human Phenotype Ontology (URL_TO_INSERT_TERM_4069 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD-NAME_4071 https://fairsharing.org/FAIRsharing.kbtt7f)  (HPO) concept curation. |[Unlicense](https://spdx.org/licenses/Unlicense) | Genotype and phenotype, Ontology (URL_TO_INSERT_TERM_4070 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_4068 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing| Web application |
| [PlanGexQ](https://bio.tools/PlanGexQ)| A user-friendly interactive tool for the curation and annotation of planarian morphologies and gene expression patterns in a centralized database (URL_TO_INSERT_TERM_4072 https://fairsharing.org/search?fairsharingRegistry=Database) .|N/A | Mathematics, Genotype and phenotype, Model (URL_TO_INSERT_TERM_4073 https://fairsharing.org/search?recordType=model_and_format)  organisms, Ontology (URL_TO_INSERT_TERM_4075 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_4074 https://fairsharing.org/search?recordType=terminology_artefact) , Gene expression |  |
|[GOcats](https://bio.tools/gocats)|Advances in gene ontology (URL_TO_INSERT_TERM_4077 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD-NAME_4079 https://fairsharing.org/FAIRsharing.6xq0ee)  utilization improve statistical power of annotation enrichment.|N/A| Mapping, Ontology (URL_TO_INSERT_TERM_4078 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_4076 https://fairsharing.org/search?recordType=terminology_artefact) , Microarray experiment     | Command-line tool                      |
| [RDFScape](https://bio.tools/rdfscape) | This is a project (URL_TO_INSERT_TERM_4080 https://fairsharing.org/search?recordType=project)  that brings Semantic Web features to the popular Systems Biology software Cytoscape. It allows to query, visualize and reason on ontologies (URL_TO_INSERT_TERM_4083 https://fairsharing.org/search?recordType=terminology_artefact)  represented in OWL (URL_TO_INSERT_RECORD-ABBREV_4084 https://fairsharing.org/FAIRsharing.atygwy)  or RDF (URL_TO_INSERT_RECORD-ABBREV_4085 https://fairsharing.org/FAIRsharing.p77ph9)  within Cytoscape.  |         | Systems biology, Ontology (URL_TO_INSERT_TERM_4082 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_4081 https://fairsharing.org/search?recordType=terminology_artefact) , Biology    | Desktop application                    |
| [OntoBrowser](https://bio.tools/ontobrowser)| The tool was developed to manage ontologies (URL_TO_INSERT_TERM_4091 https://fairsharing.org/search?recordType=terminology_artefact)  (and controlled terminologies (URL_TO_INSERT_TERM_4088 https://fairsharing.org/search?recordType=terminology_artefact)  e.g. CDISC (URL_TO_INSERT_RECORD-NAME_4094 https://fairsharing.org/3525)  SEND (URL_TO_INSERT_RECORD-ABBREV_4093 https://fairsharing.org/FAIRsharing.7z842d) ). The primary goal of the tool is to provide an online collaborative solution for expert curators to map (URL_TO_INSERT_RECORD-NAME_4092 https://fairsharing.org/FAIRsharing.53edcc)  code list terms (sourced from multiple systems/database (URL_TO_INSERT_TERM_4086 https://fairsharing.org/search?fairsharingRegistry=Database) s) to preferred ontology (URL_TO_INSERT_TERM_4089 https://fairsharing.org/search?recordType=terminology_artefact)  terms.|[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)| Ontology (URL_TO_INSERT_TERM_4090 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_4087 https://fairsharing.org/search?recordType=terminology_artefact) , Data identity and mapping      | Web API, Web application               |
|[QuickGO](https://bio.tools/quickgo)| A fast browser for Gene Ontology (URL_TO_INSERT_TERM_4096 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD-NAME_4098 https://fairsharing.org/FAIRsharing.6xq0ee)  terms and annotations.    |         | Ontology (URL_TO_INSERT_TERM_4097 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_4095 https://fairsharing.org/search?recordType=terminology_artefact)       | Web application                        |
|[Circular Gene Ontology (CirGO)](https://bio.tools/cirgo)| Visualises non-redundant two-level hierarchically structured ontology (URL_TO_INSERT_TERM_4100 https://fairsharing.org/search?recordType=terminology_artefact)  terms from gene expression data in a 2D space.   |[GPL3.0](https://spdx.org/licenses/GPL-3.0) | Ontology (URL_TO_INSERT_TERM_4101 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_4099 https://fairsharing.org/search?recordType=terminology_artefact) , Data visualisation, Gene expression| Command-line tool, Desktop application |

### Ontology engineering

Ontology (URL_TO_INSERT_TERM_4102 https://fairsharing.org/search?recordType=terminology_artefact)  engineering is the process of developing and maintaining ontologies (URL_TO_INSERT_TERM_4104 https://fairsharing.org/search?recordType=terminology_artefact)  during the ontology (URL_TO_INSERT_TERM_4103 https://fairsharing.org/search?recordType=terminology_artefact)  life cycle.

__Curated tools__

|Tool|Description|License|Topics|Resource Type|
|---|--|--|--|--|
|[Protégé](https://protege.stanford.edu/) |A free, open source ontology (URL_TO_INSERT_TERM_4105 https://fairsharing.org/search?recordType=terminology_artefact)  editor and a knowledge management system.|[2-Clause BSD](https://opensource.org/licenses/BSD-2-Clause)||Web application, Desktop application|
|[ROBOT](http://robot.obolibrary.org/)|An open source library and command-line tool for automating ontology (URL_TO_INSERT_TERM_4107 https://fairsharing.org/search?recordType=terminology_artefact)  development tasks. ROBOT provides ontology (URL_TO_INSERT_TERM_4108 https://fairsharing.org/search?recordType=terminology_artefact)  processing commands for a variety of tasks, including commands for converting format (URL_TO_INSERT_TERM_4106 https://fairsharing.org/search?recordType=model_and_format) s, running a reasoner, creating import modules, running reports, and various other tasks.|[BSD 3-Clause License](https://raw.githubusercontent.com/ontodev/robot/master/LICENSE.txt)||Command-line tool|
|[OWLAPI](http://owlcs.github.io/owlapi/)|A Java API and reference implmentation for creating, manipulating and serialising OWL (URL_TO_INSERT_RECORD-ABBREV_4110 https://fairsharing.org/FAIRsharing.atygwy)  Ontologies (URL_TO_INSERT_TERM_4109 https://fairsharing.org/search?recordType=terminology_artefact) .|LGPL and Apache||API|
|[eNanoMapper Slimmer](https://github.com/enanomapper/slimmer)|A slim tool to slim ontologies (URL_TO_INSERT_TERM_4114 https://fairsharing.org/search?recordType=terminology_artefact)  as part of ontology (URL_TO_INSERT_TERM_4111 https://fairsharing.org/search?recordType=terminology_artefact)  integration. It allows users to provide configuration files that specify which parts of an ontology (URL_TO_INSERT_TERM_4112 https://fairsharing.org/search?recordType=terminology_artefact)  should be kept and/or removed, allowing to just select parts of the ontology (URL_TO_INSERT_TERM_4113 https://fairsharing.org/search?recordType=terminology_artefact)  you like.|[MIT license](https://opensource.org/licenses/MIT)||Java|
|[TopBraid Composer](https://www.topquadrant.com/products/topbraid-composer/)|TopBraid Composer Maestro Edition is used to develop ontology (URL_TO_INSERT_TERM_4116 https://fairsharing.org/search?recordType=terminology_artefact)  model (URL_TO_INSERT_TERM_4115 https://fairsharing.org/search?recordType=model_and_format) s, configure data source integration, and create semantic services and user interfaces.|[Commercial license](https://www.topquadrant.com/legal/)||
|[VocBench](http://vocbench.uniroma2.it/)|a web-based, multilingual, collaborative development platform for managing OWL (URL_TO_INSERT_RECORD-ABBREV_4118 https://fairsharing.org/FAIRsharing.atygwy)  ontologies (URL_TO_INSERT_TERM_4117 https://fairsharing.org/search?recordType=terminology_artefact) , SKOS (URL_TO_INSERT_RECORD-ABBREV_4120 https://fairsharing.org/FAIRsharing.48e326) (/XL) thesauri, Ontolex-lemon lexicons and generic RDF (URL_TO_INSERT_RECORD-ABBREV_4119 https://fairsharing.org/FAIRsharing.p77ph9)  datasets.|[License](https://bitbucket.org/art-uniroma2/vocbench3/src/master/LICENSE)||Desktop application|


## Implementation examples

To show how these tools can be used in real life examples, please check the related recipes.
- {ref}`fcb-selecting-ontologies (URL_TO_INSERT_TERM_4121 https://fairsharing.org/search?recordType=terminology_artefact) `
- {ref}`fcb-interop-ontorobot`
<!-- - [Which vocabulary to use?](https://fairplus.github.io/the-fair-cookbook/content/recipes/interoperability/selecting-ontologies.html)
- [Building an application ontology with Robot](https://fairplus.github.io/the-fair-cookbook/content/recipes/interoperability/ontology-robot-recipe.html) -->


## References
````{dropdown} **References**

````


## Authors

````{authors_fairplus}
Fuqi: Writing - Original Draft, Software
Eva: Writing - Original Draft, Software
Sukhi: Data curation, Software
Philippe: Writing - Review & Editing 
````



## License

````{license_fairplus}
CC-BY-4.0
````




