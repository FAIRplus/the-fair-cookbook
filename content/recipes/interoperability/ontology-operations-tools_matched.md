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

This recipe aims to provide `an overview of tools available` to perform a number of key operations using ontologies (URL_TO_INSERT_TERM_4991 https://fairsharing.org/search?recordType=terminology_artefact)  and relevant to FAIR (URL_TO_INSERT_RECORD_4993 https://fairsharing.org/FAIRsharing.WWI10U)  processes: from `ontology (URL_TO_INSERT_TERM_4988 https://fairsharing.org/search?recordType=terminology_artefact)  management` to using `ontology (URL_TO_INSERT_TERM_4989 https://fairsharing.org/search?recordType=terminology_artefact)  for annotation` or `performing ontology (URL_TO_INSERT_TERM_4990 https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD_4992 https://fairsharing.org/FAIRsharing.53edcc) ping`.

It aims to serve as a starting point to identify tools for FAIR (URL_TO_INSERT_RECORD_4995 https://fairsharing.org/FAIRsharing.WWI10U) ification tasks where ontologies (URL_TO_INSERT_TERM_4994 https://fairsharing.org/search?recordType=terminology_artefact)  and semantic frameworks are needed. 

```{admonition} disclaimer
It is not intended to provide a comprehensive list covering all possible tools.
```

>The lists of tools are generated either automatically by querying the [bio.tools](https://bio.tools/) repository (URL_TO_INSERT_TERM_4996 https://fairsharing.org/search?recordType=repository) , or through manual curation. In this last instance, the list produced reflects what is being used in the industry and is influenced by the FAIR (URL_TO_INSERT_RECORD_4998 https://fairsharing.org/FAIRsharing.WWI10U) plus project (URL_TO_INSERT_TERM_4997 https://fairsharing.org/search?recordType=project)  partners that have been surveyed for the purpose of this work.

```{warning} 
The content in these tables was generated in March 2021.
For an updated contents, please check the [FAIR tooling repository](https://github.com/FAIRplus/WP3_FAIR_tooling).
```


## Requirements

* recipe dependency:
   * {ref}`fcb-selecting-ontologies (URL_TO_INSERT_TERM_4999 https://fairsharing.org/search?recordType=terminology_artefact) `
* knowledge requirement:
   * be fam (URL_TO_INSERT_RECORD_5001 https://fairsharing.org/FAIRsharing.d0886a) iliar with ontologies (URL_TO_INSERT_TERM_5000 https://fairsharing.org/search?recordType=terminology_artefact)  and semantic annotation.

---

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [ontology and terminology](http://edamontology.org/topic_0089)  | 
| [text annotation](http://edamontology.org/operation_3778)  |

---
## Overview

The figure below shows different ontology (URL_TO_INSERT_TERM_5002 https://fairsharing.org/search?recordType=terminology_artefact) -related operations and their relationships, together with related tools and recipes.


````{dropdown} 
:open: 
```{figure} ontology-operations-mermaid.png
---
width: 700px
name: Overview of key aspects in ontology (URL_TO_INSERT_TERM_5003 https://fairsharing.org/search?recordType=terminology_artefact)  associated processes
alt: Overview of key aspects in ontology (URL_TO_INSERT_TERM_5004 https://fairsharing.org/search?recordType=terminology_artefact)  associated processes
---
Overview of key aspects in ontology (URL_TO_INSERT_TERM_5005 https://fairsharing.org/search?recordType=terminology_artefact)  associated processes
```
````

The table below is an overview of ontology (URL_TO_INSERT_TERM_5006 https://fairsharing.org/search?recordType=terminology_artefact)  strategies tools identified. Details of each tools are provided below.

|         Topic        |       Curated tools      |   Related tools in Bio.tools (URL_TO_INSERT_RECORD_5007 https://fairsharing.org/FAIRsharing.63520c)    |
|:--------------------:|:------------------------:|:------------------------------:|
| Ontology (URL_TO_INSERT_TERM_5008 https://fairsharing.org/search?recordType=terminology_artefact)  annotation  | ZOOMA                    | bioBERT                        |
|                      | NCBI BioPortal (URL_TO_INSERT_RECORD_5009 https://fairsharing.org/FAIRsharing.4m97ah)  Annotator | PP (URL_TO_INSERT_RECORD_5010 https://fairsharing.org/FAIRsharing.tghhc4) R-SSM                        |
|                      | BioBert                  | HP (URL_TO_INSERT_RECORD_5011 https://fairsharing.org/FAIRsharing.kbtt7f) O2GO                         |
|                      | Termite                  | Vapur                          |
|                      | PoolParty Semantic Suite | matscholar                     |
|                      | OntoMaton                | CollaboNet                     |
|                      | Prodigy                  | Calchas                        |
|                      | OntoText                 | QTL TableMiner++(QTM)          |
|                      |                          | thbp                           |
| Ontology (URL_TO_INSERT_TERM_5012 https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD_5013 https://fairsharing.org/FAIRsharing.53edcc) ping     | OxO (URL_TO_INSERT_RECORD_5014 https://fairsharing.org/FAIRsharing.0c6fea)                       | meshr                          |
|                      |                          | locdb                          |
| Ontology (URL_TO_INSERT_TERM_5015 https://fairsharing.org/search?recordType=terminology_artefact)  management  | AberOWL                  | ngly1                          |
|                      | BioPortal (URL_TO_INSERT_RECORD_5016 https://fairsharing.org/FAIRsharing.4m97ah)                 | Doc2Hpo                        |
|                      | Centree Ontology (URL_TO_INSERT_TERM_5017 https://fairsharing.org/search?recordType=terminology_artefact)  Manager | PlanGexQ                       |
|                      | OLS (URL_TO_INSERT_RECORD_5018 https://fairsharing.org/FAIRsharing.Mkl9RR)                       | GO (URL_TO_INSERT_RECORD_5019 https://fairsharing.org/FAIRsharing.6xq0ee) cats                         |
|                      | Ontobee (URL_TO_INSERT_RECORD_5022 https://fairsharing.org/FAIRsharing.q8fx1b)                   | RDF (URL_TO_INSERT_RECORD_5021 https://fairsharing.org/FAIRsharing.p77ph9) S (URL_TO_INSERT_RECORD_5020 https://fairsharing.org/FAIRsharing.v9n3gk) cape                       |
|                      | PoolParty                | OntoBrowser                    |
|                      |                          | QuickGO                        |
|                      |                          | Circular Gene Ontology (URL_TO_INSERT_TERM_5023 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_5024 https://fairsharing.org/FAIRsharing.6xq0ee)  (CirGO) |
| Ontology (URL_TO_INSERT_TERM_5025 https://fairsharing.org/search?recordType=terminology_artefact)  engineering | eNanoMap (URL_TO_INSERT_RECORD_5026 https://fairsharing.org/FAIRsharing.53edcc) per Slimmer      |                                |
|                      | OWL (URL_TO_INSERT_RECORD_5027 https://fairsharing.org/FAIRsharing.atygwy) API                   |                                |
|                      | Protégé                  |                                |
|                      | RO (URL_TO_INSERT_RECORD_5028 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_5029 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_5030 https://fairsharing.org/FAIRsharing.cp0ybc) BOT                    |                                |
|                      | TopBraid Composer        |                                |
|                      | VocBench                 |                                |

---
## Operations

### Ontology annotation

Ontoloy Annotation is the process of linking free text or data items to 'tokens' (defined terms from a lexicon) which provide semantic value. For example,  "type 2 diabetes" can be annotated with corresponding [term](http://purl.obolibrary.org/obo/MONDO_0005148) in the MONDO (URL_TO_INSERT_RECORD_5032 https://fairsharing.org/FAIRsharing.b2979t)  disease ontology (URL_TO_INSERT_TERM_5031 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_5033 https://fairsharing.org/FAIRsharing.8b6wfq) . 

__Curated tools__

|Tool|Description|License|Topics|Resource Type|How to use|
|---|--|--|--|--|--|
|[ZOOMA](https://www.ebi.ac.uk/spot/zooma/)|A tool for map (URL_TO_INSERT_RECORD_5037 https://fairsharing.org/FAIRsharing.53edcc) ping free text annotations to ontology (URL_TO_INSERT_TERM_5036 https://fairsharing.org/search?recordType=terminology_artefact)  term based on a curated repository (URL_TO_INSERT_TERM_5034 https://fairsharing.org/search?recordType=repository)  of annotation knowledge.|[EMBL-EBI Terms of Use](https://www.ebi.ac.uk/about/terms-of-use/)|Ontology and terminology (URL_TO_INSERT_TERM_5035 https://fairsharing.org/search?recordType=terminology_artefact) ,<br>Systems biology,<br>Data identity and map (URL_TO_INSERT_RECORD_5038 https://fairsharing.org/FAIRsharing.53edcc) ping|Web application,<br> API|[ZOOMA-Getting started](https://www.ebi.ac.uk/spot/zooma/docs/search)|
|[NCBI BioPortal Annotator](https://bioportal.bioontology.org/annotatorplus)|Get annotations for biomedical text with classes from the ontologies (URL_TO_INSERT_TERM_5040 https://fairsharing.org/search?recordType=terminology_artefact) .|[BioPortal (URL_TO_INSERT_RECORD_5041 https://fairsharing.org/FAIRsharing.4m97ah)  Terms of Use](https://www.bioontology.org/terms/)|Ontology and terminology (URL_TO_INSERT_TERM_5039 https://fairsharing.org/search?recordType=terminology_artefact) ,<br>Systems biology,<br>Data identity and map (URL_TO_INSERT_RECORD_5043 https://fairsharing.org/FAIRsharing.53edcc) ping|Web application,<br> API|[BioPortal (URL_TO_INSERT_RECORD_5042 https://fairsharing.org/FAIRsharing.4m97ah)  help](https://bioportal.bioontology.org/help?pop=true#Annotator_Tab)|
|[BioBert](https://github.com/dmis-lab/biobert)|A biomedical language representation model (URL_TO_INSERT_TERM_5044 https://fairsharing.org/search?recordType=model_and_format)  designed for biomedical text mining tasks such as biomedical named entity recognition, relation extraction, question answering.|[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)|text mining,<br> named-entity recognition,<br> natural language processing|Python|
|[Termite](https://www.scibite.com/platform/termite/)|Semantic enrichment to unlock the value of unstructured text and simplify the identification of new potential biomarker leads from scientific text.|Commercial license|Ontology (URL_TO_INSERT_TERM_5046 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5045 https://fairsharing.org/search?recordType=terminology_artefact) |
|[PoolParty Semantic Suite](https://semantic-web.com/poolparty-semantic-suite/)|Automate the handling of heterogeneous metadata systems and the creation of enterprise knowledge graphs.design knowledge graphs at your own pace and with speed. Create your own ontologies (URL_TO_INSERT_TERM_5047 https://fairsharing.org/search?recordType=terminology_artefact)  and custom schemes by reusing already existing ontologies (URL_TO_INSERT_TERM_5048 https://fairsharing.org/search?recordType=terminology_artefact)  such as FO (URL_TO_INSERT_RECORD_5050 https://fairsharing.org/FAIRsharing.ca63ce) AF, FIBO, schema.org (URL_TO_INSERT_RECORD_5049 https://fairsharing.org/FAIRsharing.hzdzq8)  and CHEBI, among others. Apply them to your existing taxonomies with ease.|Commercial license|Content enrichment,<br>Data integration|
|[OntoMaton](https://github.com/ISA-tools/OntoMaton)| A tool facilitating ontology (URL_TO_INSERT_TERM_5051 https://fairsharing.org/search?recordType=terminology_artefact)  search (URL_TO_INSERT_RECORD_5052 https://fairsharing.org/FAIRsharing.52b22c)  and tagging functionalities within Google Spreadsheets.|[CPAL license](https://opensource.org/licenses/CPAL-1.0)||Google Add-ons|
|[Prodigy](https://prodi.gy/)|A modern annotation tool for creating training and evaluation data for machine learning model (URL_TO_INSERT_TERM_5053 https://fairsharing.org/search?recordType=model_and_format) s. You can also use Prodigy to help you inspect and clean your data, do error analysis and develop rule-based systems to use in combination with your statistical model (URL_TO_INSERT_TERM_5054 https://fairsharing.org/search?recordType=model_and_format) s.|Commercial license|Data annotation|Python, Web application,API|
|[OntoText](https://www.ontotext.com/products/ontotext-platform/)|Connect and publish complex enterprise knowledge with standard (URL_TO_INSERT_TERM_5055 https://fairsharing.org/search?fairsharingRegistry=Standard) -compliant semantic graph database (URL_TO_INSERT_TERM_5056 https://fairsharing.org/search?fairsharingRegistry=Database) ; Customize and apply analytics to link documents to graphs, extract new facts, classify and recommend content.|Commercial license|

__Related tools in [Bio.Tools](https://bio.tools)__

| Tool| Description| License | Topics | Resource Type |
|-------|--------|---------|----|--------|
| [bioBERT](https://bio.tools/BioBERT) | A pre-trained weights of BioBERT, a language representation model (URL_TO_INSERT_TERM_5057 https://fairsharing.org/search?recordType=model_and_format)  for biomedical domain, especially designed for biomedical text mining tasks such as biomedical named entity recognition, relation extraction, question answering, etc.|  N/A | Medicine, Ontology (URL_TO_INSERT_TERM_5059 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5058 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing  |Python|
|[PPR-SSM](https://bio.tools/PPR-SSM)| Personalized PageRank and semantic similarity measures for linking entities found in documents to concepts from domain-specific ontologies (URL_TO_INSERT_TERM_5062 https://fairsharing.org/search?recordType=terminology_artefact) . |N/A| Imaging, Natural language processing, Data mining, Genotype and phenotype, Ontology (URL_TO_INSERT_TERM_5061 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5060 https://fairsharing.org/search?recordType=terminology_artefact)         |Java, Python|
|[HPO2GO](https://bio.tools/HPO2GO)| Prediction of human phenotype ontology (URL_TO_INSERT_TERM_5064 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_5072 https://fairsharing.org/FAIRsharing.kbtt7f)  term associations using cross ontology (URL_TO_INSERT_TERM_5065 https://fairsharing.org/search?recordType=terminology_artefact)  annotation co-occurrences.Map (URL_TO_INSERT_RECORD_5071 https://fairsharing.org/FAIRsharing.53edcc) ping between Human Phenotype Ontology (URL_TO_INSERT_TERM_5066 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_5073 https://fairsharing.org/FAIRsharing.kbtt7f)  (HPO) and Gene Ontology (URL_TO_INSERT_TERM_5067 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_5070 https://fairsharing.org/FAIRsharing.6xq0ee)  (GO) terms for the prediction of gene/protein - function - phenotype - disease associations.|[GPL-3.0](https://spdx.org/licenses/GPL-3.0)| Pathology, Protein (URL_TO_INSERT_RECORD_5069 https://fairsharing.org/FAIRsharing.rtndct)  interactions, Genotype and phenotype, Ontology (URL_TO_INSERT_TERM_5068 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5063 https://fairsharing.org/search?recordType=terminology_artefact) , Gene expression| Command-line tool |
| [Vapur](https://bio.tools/vapur)| A Search (URL_TO_INSERT_RECORD_5081 https://fairsharing.org/FAIRsharing.52b22c)  Engine to Find Related Protein (URL_TO_INSERT_RECORD_5076 https://fairsharing.org/FAIRsharing.rtndct) .Vapur is an online entity-oriented search (URL_TO_INSERT_RECORD_5082 https://fairsharing.org/FAIRsharing.52b22c)  engine for the CO (URL_TO_INSERT_RECORD_5077 https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD_5079 https://fairsharing.org/FAIRsharing.thskvr) VID-19 anthology. Vapur is empowered with a semantic inverted index that is created through named entity recognition and relation extraction on CO (URL_TO_INSERT_RECORD_5078 https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD_5080 https://fairsharing.org/FAIRsharing.thskvr) RD-19 abstracts. |N/A| Pathology, Ontology (URL_TO_INSERT_TERM_5075 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5074 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing, Enzymes |Python|
| [matscholar](https://bio.tools/matscholar)| A Python library for materials-focused natural language processing (NLP). Named Entity Recognition and Normalization Applied to Large-Scale Informat (URL_TO_INSERT_TERM_5083 https://fairsharing.org/search?recordType=model_and_format) ion Extraction from the Materials Science Literature.|[MIT](https://spdx.org/licenses/MIT)| Chemistry (URL_TO_INSERT_RECORD_5086 https://fairsharing.org/3524) , Ontology (URL_TO_INSERT_TERM_5085 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5084 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing | Command-line tool |
|[CollaboNet](https://bio.tools/collabonet)| Collaboration of deep neural networks for biomedical named entity recognition.|[MIT](https://spdx.org/licenses/MIT)| Ontology (URL_TO_INSERT_TERM_5088 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5087 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing, Machine learning | Command-line tool |
| [Calchas](https://bio.tools/calchas)| A web based framework that takes advantage of domain specific ontologies (URL_TO_INSERT_TERM_5094 https://fairsharing.org/search?recordType=terminology_artefact) , and Natural Language Processing, aiming to empower exploration of biomedical resources via semantic-based querying and search (URL_TO_INSERT_RECORD_5095 https://fairsharing.org/FAIRsharing.52b22c) . The NLP engine analyzes the input free-text query and translates it into targeted queries with terms from the underlying ontology (URL_TO_INSERT_TERM_5092 https://fairsharing.org/search?recordType=terminology_artefact) . | N/A | Medical informat (URL_TO_INSERT_TERM_5089 https://fairsharing.org/search?recordType=model_and_format) ics, Ontology (URL_TO_INSERT_TERM_5093 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5091 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing, Bioinformat (URL_TO_INSERT_TERM_5090 https://fairsharing.org/search?recordType=model_and_format) ics| Web application   |
|[QTL TableMiner++(QTM)](https://bio.tools/QTM) | It is a command-line tool to retrieve and semantically annotate results obtained from QTL map (URL_TO_INSERT_RECORD_5101 https://fairsharing.org/FAIRsharing.53edcc) ping experiments. It takes full-text articles from the Europe PMC (URL_TO_INSERT_RECORD_5100 https://fairsharing.org/FAIRsharing.cmw6mm)  (URL_TO_INSERT_RECORD_5102 https://fairsharing.org/FAIRsharing.wpt5mp)  repository (URL_TO_INSERT_TERM_5097 https://fairsharing.org/search?recordType=repository)  as input and outputs the extracted QTLs into a relational database (URL_TO_INSERT_TERM_5096 https://fairsharing.org/search?fairsharingRegistry=Database)  (SQLite) and text file (CSV).|[Apache-2.0](https://spdx.org/licenses/Apache-2.0)| Ontology (URL_TO_INSERT_TERM_5099 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5098 https://fairsharing.org/search?recordType=terminology_artefact) | Command-line tool |
| [thbp](https://bio.tools/thbp)| Map (URL_TO_INSERT_RECORD_5105 https://fairsharing.org/FAIRsharing.53edcc) ping anatomical related entities to human body parts based on wikiped (URL_TO_INSERT_RECORD_5106 https://fairsharing.org/FAIRsharing.31385c) ia in discharge summaries.|N/A| Anatomy, Ontology (URL_TO_INSERT_TERM_5104 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5103 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing||

### Ontology mapping

The process of determining correspondences between equivalent concepts in alternative ontologies (URL_TO_INSERT_TERM_5107 https://fairsharing.org/search?recordType=terminology_artefact) , and other vocabularies. This may include map (URL_TO_INSERT_RECORD_5108 https://fairsharing.org/FAIRsharing.53edcc) ping to convey different levels of granularity.

__Curated tools__

|Tool|Description|License|Topics|Resource Type|How to use|
|---|--|--|--|--|--|
|[OxO](https://www.ebi.ac.uk/spot/oxo/index)|A service for finding map (URL_TO_INSERT_RECORD_5111 https://fairsharing.org/FAIRsharing.53edcc) pings (or cross-references) between terms from ontologies (URL_TO_INSERT_TERM_5110 https://fairsharing.org/search?recordType=terminology_artefact) , vocabularies and coding standard (URL_TO_INSERT_TERM_5109 https://fairsharing.org/search?fairsharingRegistry=Standard) s. |[EMBL-EBI Terms of Use](https://www.ebi.ac.uk/about/terms-of-use/)|Ontology alignment| GUI and API| |

__Related tools in [Bio.Tools](https://bio.tools)__

| Tool| Description| License | Topics     | Type|
|-------|--|---------|----|---|
|[meshr](https://bio.tools/meshr)| A set of annotation map (URL_TO_INSERT_RECORD_5113 https://fairsharing.org/FAIRsharing.53edcc) s describing the entire MeSH assembled using data from MeSH. |[Apache-2.0](https://spdx.org/licenses/Apache-2.0)| Medical informat (URL_TO_INSERT_TERM_5112 https://fairsharing.org/search?recordType=model_and_format) ics, Data quality management  | Command-line tool, Library |
| [locdb](https://bio.tools/locdb) | Manually curated database (URL_TO_INSERT_TERM_5114 https://fairsharing.org/search?fairsharingRegistry=Database)  with experimental annotations for the subcellular localizations of proteins in Homo sapiens (HS, human) and Arabidopsis thaliana (AT, thale cress). | N/A | Ontology (URL_TO_INSERT_TERM_5117 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5116 https://fairsharing.org/search?recordType=terminology_artefact) , Data submission, annotation and curation, Protein (URL_TO_INSERT_RECORD_5118 https://fairsharing.org/FAIRsharing.rtndct) s | Database (URL_TO_INSERT_TERM_5115 https://fairsharing.org/search?fairsharingRegistry=Database)  portal|


### Ontology management

The process of managing ontologies (URL_TO_INSERT_TERM_5120 https://fairsharing.org/search?recordType=terminology_artefact)  and other vocabularies in semantic web-linked data environments.This includes policies (URL_TO_INSERT_TERM_5119 https://fairsharing.org/search?fairsharingRegistry=Policy)  for update and maintenance of constituent and new terms.

__Curated tools__

|Tool|Description|License|Topics|Resource Type|How to use|
|---|--|--|--|--|--|
|[OLS](https://www.ebi.ac.uk/ols/index)|a repository (URL_TO_INSERT_TERM_5121 https://fairsharing.org/search?recordType=repository)  for biomedical ontologies (URL_TO_INSERT_TERM_5124 https://fairsharing.org/search?recordType=terminology_artefact)  that aims to provide a single point of access to the latest ontology (URL_TO_INSERT_TERM_5123 https://fairsharing.org/search?recordType=terminology_artefact)  versions.|[EMBL-EBI Terms of Use](https://www.ebi.ac.uk/about/terms-of-use/)|Ontology and terminology (URL_TO_INSERT_TERM_5122 https://fairsharing.org/search?recordType=terminology_artefact) |Web Application, API|
|[BioPortal](https://bioportal.bioontology.org/)|A repository (URL_TO_INSERT_TERM_5125 https://fairsharing.org/search?recordType=repository)  of biomedical ontologies (URL_TO_INSERT_TERM_5127 https://fairsharing.org/search?recordType=terminology_artefact) .|[BioPortal (URL_TO_INSERT_RECORD_5128 https://fairsharing.org/FAIRsharing.4m97ah)  Terms of Use](https://www.bioontology.org/terms/)|Ontology and terminology (URL_TO_INSERT_TERM_5126 https://fairsharing.org/search?recordType=terminology_artefact) |Web Application, API|
|[PoolParty](https://www.poolparty.biz/) |Knowledge Engineering & Knowledge Graph Management. Taxonomy, ontology (URL_TO_INSERT_TERM_5130 https://fairsharing.org/search?recordType=terminology_artefact)  and linked dataset management. |Commercial license|Ontology (URL_TO_INSERT_TERM_5131 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5129 https://fairsharing.org/search?recordType=terminology_artefact) |
|[Centree Ontology Manager](https://www.scibite.com/platform/centree/)|A centralised, enterprise-ready resource for ontology (URL_TO_INSERT_TERM_5132 https://fairsharing.org/search?recordType=terminology_artefact)  management and transforms the experience of maintaining and releasing ontologies (URL_TO_INSERT_TERM_5133 https://fairsharing.org/search?recordType=terminology_artefact)  for research (URL_TO_INSERT_RECORD_5134 https://fairsharing.org/FAIRsharing.52b22c) -led businesses.|Commercial license||Web application, API|
|[Ontobee](http://www.ontobee.org/)|A linked data server designed for ontologies (URL_TO_INSERT_TERM_5136 https://fairsharing.org/search?recordType=terminology_artefact) . Ontobee (URL_TO_INSERT_RECORD_5137 https://fairsharing.org/FAIRsharing.q8fx1b)  is aimed to facilitate ontology (URL_TO_INSERT_TERM_5135 https://fairsharing.org/search?recordType=terminology_artefact)  data sharing, visualization, query, integration, and analysis.|[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)||Web application|
|[AberOWL](http://www.aber-owl.net/)|A framework for ontology (URL_TO_INSERT_TERM_5140 https://fairsharing.org/search?recordType=terminology_artefact) -based access to biological data. It consists of a repository (URL_TO_INSERT_TERM_5138 https://fairsharing.org/search?recordType=repository)  of bio-ontologies (URL_TO_INSERT_TERM_5142 https://fairsharing.org/search?recordType=terminology_artefact) , a set of webservices which provide access to OWL (URL_TO_INSERT_RECORD_5144 https://fairsharing.org/FAIRsharing.atygwy) (-EL) reasoning over the ontologies (URL_TO_INSERT_TERM_5143 https://fairsharing.org/search?recordType=terminology_artefact) , and several frontends which utilise the ontology (URL_TO_INSERT_TERM_5141 https://fairsharing.org/search?recordType=terminology_artefact)  repository (URL_TO_INSERT_TERM_5139 https://fairsharing.org/search?recordType=repository)  and reasoning services.|||Web application, API|


__Related tools in [Bio.Tools](https://bio.tools)__

| Tool| Description  | License | Topics | Type|
|---|--|--|--|--|
|[ngly1](https://bio.tools/ngly1)| A repository (URL_TO_INSERT_TERM_5145 https://fairsharing.org/search?recordType=repository)  for the NGLY1 Deficiency Knowledge Graph, the reasoning context to support hypothesis discovery for NGLY1 Deficiency-CDDG (DOID (URL_TO_INSERT_RECORD_5148 https://fairsharing.org/FAIRsharing.8b6wfq) :0060728) research (URL_TO_INSERT_RECORD_5149 https://fairsharing.org/FAIRsharing.52b22c) . The user can navigate the knowledge in the graph in the Neo4j Browser website. | N/A  | Molecular interactions, pathways and networks, Ontology (URL_TO_INSERT_TERM_5147 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5146 https://fairsharing.org/search?recordType=terminology_artefact) , Machine learning       | Command-line tool |
| [Doc2Hpo](https://bio.tools/doc2hpo) | Web application for efficient and accurate Human Phenotype Ontology (URL_TO_INSERT_TERM_5151 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_5153 https://fairsharing.org/FAIRsharing.kbtt7f)  (HPO) concept curation. |[Unlicense](https://spdx.org/licenses/Unlicense) | Genotype and phenotype, Ontology (URL_TO_INSERT_TERM_5152 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5150 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing| Web application |
| [PlanGexQ](https://bio.tools/PlanGexQ)| A user-friendly interactive tool for the curation and annotation of planarian morphologies and gene expression patterns in a centralized database (URL_TO_INSERT_TERM_5154 https://fairsharing.org/search?fairsharingRegistry=Database) .|N/A | Mathematics, Genotype and phenotype, Model (URL_TO_INSERT_TERM_5155 https://fairsharing.org/search?recordType=model_and_format)  organisms, Ontology (URL_TO_INSERT_TERM_5157 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5156 https://fairsharing.org/search?recordType=terminology_artefact) , Gene expression |  |
|[GOcats](https://bio.tools/gocats)|Advances in gene ontology (URL_TO_INSERT_TERM_5159 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_5161 https://fairsharing.org/FAIRsharing.6xq0ee)  utilization improve statistical power of annotation enrichment.|N/A| Map (URL_TO_INSERT_RECORD_5162 https://fairsharing.org/FAIRsharing.53edcc) ping, Ontology (URL_TO_INSERT_TERM_5160 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5158 https://fairsharing.org/search?recordType=terminology_artefact) , Microarray experiment     | Command-line tool                      |
| [RDFScape](https://bio.tools/rdfscape) | This is a project (URL_TO_INSERT_TERM_5163 https://fairsharing.org/search?recordType=project)  that brings Semantic Web features to the popular Systems Biology software Cytoscape. It allows to query, visualize and reason on ontologies (URL_TO_INSERT_TERM_5166 https://fairsharing.org/search?recordType=terminology_artefact)  represented in OWL (URL_TO_INSERT_RECORD_5167 https://fairsharing.org/FAIRsharing.atygwy)  or RDF (URL_TO_INSERT_RECORD_5168 https://fairsharing.org/FAIRsharing.p77ph9)  within Cytoscape.  |         | Systems biology, Ontology (URL_TO_INSERT_TERM_5165 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5164 https://fairsharing.org/search?recordType=terminology_artefact) , Biology    | Desktop application                    |
| [OntoBrowser](https://bio.tools/ontobrowser)| The tool was developed (URL_TO_INSERT_RECORD_5178 https://fairsharing.org/FAIRsharing.31385c)  to manage ontologies (URL_TO_INSERT_TERM_5174 https://fairsharing.org/search?recordType=terminology_artefact)  (and controlled terminologies (URL_TO_INSERT_TERM_5171 https://fairsharing.org/search?recordType=terminology_artefact)  e.g. CDI (URL_TO_INSERT_RECORD_5175 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_5180 https://fairsharing.org/3525)  SEND (URL_TO_INSERT_RECORD_5179 https://fairsharing.org/FAIRsharing.7z842d) ). The primary goal of the tool is to provide an online collaborative solution for expert curators to map (URL_TO_INSERT_RECORD_5176 https://fairsharing.org/FAIRsharing.53edcc)  code list terms (sourced from multiple systems/database (URL_TO_INSERT_TERM_5169 https://fairsharing.org/search?fairsharingRegistry=Database) s) to preferred ontology (URL_TO_INSERT_TERM_5172 https://fairsharing.org/search?recordType=terminology_artefact)  terms.|[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)| Ontology (URL_TO_INSERT_TERM_5173 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5170 https://fairsharing.org/search?recordType=terminology_artefact) , Data identity and map (URL_TO_INSERT_RECORD_5177 https://fairsharing.org/FAIRsharing.53edcc) ping      | Web API, Web application               |
|[QuickGO](https://bio.tools/quickgo)| A fast browser for Gene Ontology (URL_TO_INSERT_TERM_5182 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_5184 https://fairsharing.org/FAIRsharing.6xq0ee)  terms and annotations.    |         | Ontology (URL_TO_INSERT_TERM_5183 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5181 https://fairsharing.org/search?recordType=terminology_artefact)       | Web application                        |
|[Circular Gene Ontology (CirGO)](https://bio.tools/cirgo)| Visualises non-redundant two-level hierarch (URL_TO_INSERT_RECORD_5188 https://fairsharing.org/FAIRsharing.52b22c) ically structured ontology (URL_TO_INSERT_TERM_5186 https://fairsharing.org/search?recordType=terminology_artefact)  terms from gene expression data in a 2D space.   |[GPL3.0](https://spdx.org/licenses/GPL-3.0) | Ontology (URL_TO_INSERT_TERM_5187 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5185 https://fairsharing.org/search?recordType=terminology_artefact) , Data visualisation, Gene expression| Command-line tool, Desktop application |

### Ontology engineering

Ontology (URL_TO_INSERT_TERM_5189 https://fairsharing.org/search?recordType=terminology_artefact)  engineering is the process of developing and maintaining ontologies (URL_TO_INSERT_TERM_5191 https://fairsharing.org/search?recordType=terminology_artefact)  during the ontology (URL_TO_INSERT_TERM_5190 https://fairsharing.org/search?recordType=terminology_artefact)  life cycle.

__Curated tools__

|Tool|Description|License|Topics|Resource Type|
|---|--|--|--|--|
|[Protégé](https://protege.stanford.edu/) |A free, open source ontology (URL_TO_INSERT_TERM_5192 https://fairsharing.org/search?recordType=terminology_artefact)  editor and a knowledge management system.|[2-Clause BSD](https://opensource.org/licenses/BSD-2-Clause)||Web application, Desktop application|
|[ROBOT](http://robot.obolibrary.org/)|An open source library and command-line tool for automating ontology (URL_TO_INSERT_TERM_5194 https://fairsharing.org/search?recordType=terminology_artefact)  development tasks. RO (URL_TO_INSERT_RECORD_5196 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_5197 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_5198 https://fairsharing.org/FAIRsharing.cp0ybc) BOT provides ontology (URL_TO_INSERT_TERM_5195 https://fairsharing.org/search?recordType=terminology_artefact)  processing commands for a variety of tasks, including commands for converting format (URL_TO_INSERT_TERM_5193 https://fairsharing.org/search?recordType=model_and_format) s, running a reasoner, creating import modules, running reports, and various other tasks.|[BSD 3-Clause License](https://raw.githubusercontent.com/ontodev/robot/master/LICENSE.txt)||Command-line tool|
|[OWLAPI](http://owlcs.github.io/owlapi/)|A Java API and reference implmentation for creating, manipulating and serialising OWL (URL_TO_INSERT_RECORD_5200 https://fairsharing.org/FAIRsharing.atygwy)  Ontologies (URL_TO_INSERT_TERM_5199 https://fairsharing.org/search?recordType=terminology_artefact) .|LGPL and Apache||API|
|[eNanoMapper Slimmer](https://github.com/enanomapper/slimmer)|A slim tool to slim ontologies (URL_TO_INSERT_TERM_5204 https://fairsharing.org/search?recordType=terminology_artefact)  as part of ontology (URL_TO_INSERT_TERM_5201 https://fairsharing.org/search?recordType=terminology_artefact)  integration. It allows users to provide configuration files that specify which parts of an ontology (URL_TO_INSERT_TERM_5202 https://fairsharing.org/search?recordType=terminology_artefact)  should be kept and/or removed, allowing to just select parts of the ontology (URL_TO_INSERT_TERM_5203 https://fairsharing.org/search?recordType=terminology_artefact)  you like.|[MIT license](https://opensource.org/licenses/MIT)||Java|
|[TopBraid Composer](https://www.topquadrant.com/products/topbraid-composer/)|TopBraid Composer Maestro Edition is used to develop ontology (URL_TO_INSERT_TERM_5206 https://fairsharing.org/search?recordType=terminology_artefact)  model (URL_TO_INSERT_TERM_5205 https://fairsharing.org/search?recordType=model_and_format) s, configure data source integration, and create semantic services and user interfaces.|[Commercial license](https://www.topquadrant.com/legal/)||
|[VocBench](http://vocbench.uniroma2.it/)|a web-based, multilingual, collaborative development platform for managing OWL (URL_TO_INSERT_RECORD_5208 https://fairsharing.org/FAIRsharing.atygwy)  ontologies (URL_TO_INSERT_TERM_5207 https://fairsharing.org/search?recordType=terminology_artefact) , SKOS (URL_TO_INSERT_RECORD_5210 https://fairsharing.org/FAIRsharing.48e326) (/XL) thesauri, Ontolex-lemon lexicons and generic RDF (URL_TO_INSERT_RECORD_5209 https://fairsharing.org/FAIRsharing.p77ph9)  datasets.|[License](https://bitbucket.org/art-uniroma2/vocbench3/src/master/LICENSE)||Desktop application|


## Implementation examples

To show how these tools can be used in real life examples, please check the related recipes.
- {ref}`fcb-selecting-ontologies (URL_TO_INSERT_TERM_5211 https://fairsharing.org/search?recordType=terminology_artefact) `
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




