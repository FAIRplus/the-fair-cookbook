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

This recipe aims to provide `an overview of tools available` to perform a number of key operations using ontologies (URL_TO_INSERT_TERM_5869 https://fairsharing.org/search?recordType=terminology_artefact)  and relevant to FAIR (URL_TO_INSERT_RECORD_5871 https://fairsharing.org/FAIRsharing.WWI10U)  processes: from `ontology (URL_TO_INSERT_TERM_5866 https://fairsharing.org/search?recordType=terminology_artefact)  management` to using `ontology (URL_TO_INSERT_TERM_5867 https://fairsharing.org/search?recordType=terminology_artefact)  for annotation` or `performing ontology (URL_TO_INSERT_TERM_5868 https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD_5870 https://fairsharing.org/FAIRsharing.53edcc) ping`.

It aims to serve as a starting point to identify tools for FAIR (URL_TO_INSERT_RECORD_5873 https://fairsharing.org/FAIRsharing.WWI10U) ification tasks where ontologies (URL_TO_INSERT_TERM_5872 https://fairsharing.org/search?recordType=terminology_artefact)  and semantic frameworks are needed. 

```{admonition} disclaimer
It is not intended to provide a comprehensive list covering all possible tools.
```

>The lists of tools are generated either automatically by querying the [bio.tools (URL_TO_INSERT_RECORD_5877 https://fairsharing.org/FAIRsharing.63520c) ](https://bio.tools (URL_TO_INSERT_RECORD_5878 https://fairsharing.org/FAIRsharing.63520c) /) repository (URL_TO_INSERT_TERM_5874 https://fairsharing.org/search?recordType=repository) , or through manual curation. In this last instance, the list produced reflects what is being used in the industry and is influenced by the FAIR (URL_TO_INSERT_RECORD_5876 https://fairsharing.org/FAIRsharing.WWI10U) plus project (URL_TO_INSERT_TERM_5875 https://fairsharing.org/search?recordType=project)  partners that have been surveyed for the purpose of this work.

```{warning} 
The content in these tables was generated in March 2021.
For an updated contents, please check the [FAIR tooling repository](https://github.com/FAIRplus/WP3_FAIR_tooling).
```


## Requirements

* recipe dependency:
   * {ref}`fcb-selecting-ontologies (URL_TO_INSERT_TERM_5879 https://fairsharing.org/search?recordType=terminology_artefact) `
* knowledge requirement:
   * be fam (URL_TO_INSERT_RECORD_5881 https://fairsharing.org/FAIRsharing.d0886a) iliar with ontologies (URL_TO_INSERT_TERM_5880 https://fairsharing.org/search?recordType=terminology_artefact)  and semantic annotation.

---

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [ontology (URL_TO_INSERT_TERM_5882 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology](http://edamontology.org (URL_TO_INSERT_RECORD_5883 https://fairsharing.org/FAIRsharing.a6r7zs) /topic_0089)  | 
| [text annotation](http://edamontology.org (URL_TO_INSERT_RECORD_5884 https://fairsharing.org/FAIRsharing.a6r7zs) /operation_3778)  |

---
## Overview

The figure below shows different ontology (URL_TO_INSERT_TERM_5885 https://fairsharing.org/search?recordType=terminology_artefact) -related operations and their relationships, together with related tools and recipes.


````{dropdown} 
:open: 
```{figure} ontology-operations-mermaid.png
---
width: 700px
name: Overview of key aspects in ontology (URL_TO_INSERT_TERM_5886 https://fairsharing.org/search?recordType=terminology_artefact)  associated processes
alt: Overview of key aspects in ontology (URL_TO_INSERT_TERM_5887 https://fairsharing.org/search?recordType=terminology_artefact)  associated processes
---
Overview of key aspects in ontology (URL_TO_INSERT_TERM_5888 https://fairsharing.org/search?recordType=terminology_artefact)  associated processes
```
````

The table below is an overview of ontology (URL_TO_INSERT_TERM_5889 https://fairsharing.org/search?recordType=terminology_artefact)  strategies tools identified. Details of each tools are provided below.

|         Topic        |       Curated tools      |   Related tools in Bio.tools (URL_TO_INSERT_RECORD_5890 https://fairsharing.org/FAIRsharing.63520c)    |
|:--------------------:|:------------------------:|:------------------------------:|
| Ontology (URL_TO_INSERT_TERM_5891 https://fairsharing.org/search?recordType=terminology_artefact)  annotation  | ZOOMA                    | bioBERT                        |
|                      | NCBI BioPortal (URL_TO_INSERT_RECORD_5892 https://fairsharing.org/FAIRsharing.4m97ah)  Annotator | PP (URL_TO_INSERT_RECORD_5893 https://fairsharing.org/FAIRsharing.tghhc4) R-SSM                        |
|                      | BioBert                  | HP (URL_TO_INSERT_RECORD_5894 https://fairsharing.org/FAIRsharing.kbtt7f) O2GO                         |
|                      | Termite                  | Vapur                          |
|                      | PoolParty Semantic Suite | matscholar                     |
|                      | OntoMaton                | CollaboNet                     |
|                      | Prodigy                  | Calchas                        |
|                      | OntoText                 | QTL TableMiner++(QTM)          |
|                      |                          | thbp                           |
| Ontology (URL_TO_INSERT_TERM_5895 https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD_5896 https://fairsharing.org/FAIRsharing.53edcc) ping     | OxO (URL_TO_INSERT_RECORD_5897 https://fairsharing.org/FAIRsharing.0c6fea)                       | meshr                          |
|                      |                          | locdb                          |
| Ontology (URL_TO_INSERT_TERM_5898 https://fairsharing.org/search?recordType=terminology_artefact)  management  | AberOWL                  | ngly1                          |
|                      | BioPortal (URL_TO_INSERT_RECORD_5899 https://fairsharing.org/FAIRsharing.4m97ah)                 | Doc2Hpo                        |
|                      | Centree Ontology (URL_TO_INSERT_TERM_5900 https://fairsharing.org/search?recordType=terminology_artefact)  Manager | PlanGexQ                       |
|                      | OLS (URL_TO_INSERT_RECORD_5901 https://fairsharing.org/FAIRsharing.Mkl9RR)                       | GO (URL_TO_INSERT_RECORD_5902 https://fairsharing.org/FAIRsharing.6xq0ee) cats                         |
|                      | Ontobee (URL_TO_INSERT_RECORD_5905 https://fairsharing.org/FAIRsharing.q8fx1b)                   | RDF (URL_TO_INSERT_RECORD_5904 https://fairsharing.org/FAIRsharing.p77ph9) S (URL_TO_INSERT_RECORD_5903 https://fairsharing.org/FAIRsharing.v9n3gk) cape                       |
|                      | PoolParty                | OntoBrowser                    |
|                      |                          | QuickGO                        |
|                      |                          | Circular Gene Ontology (URL_TO_INSERT_TERM_5906 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_5907 https://fairsharing.org/FAIRsharing.6xq0ee)  (CirGO) |
| Ontology (URL_TO_INSERT_TERM_5908 https://fairsharing.org/search?recordType=terminology_artefact)  engineering | eNanoMap (URL_TO_INSERT_RECORD_5909 https://fairsharing.org/FAIRsharing.53edcc) per Slimmer      |                                |
|                      | OWL (URL_TO_INSERT_RECORD_5910 https://fairsharing.org/FAIRsharing.atygwy) API                   |                                |
|                      | Protégé                  |                                |
|                      | RO (URL_TO_INSERT_RECORD_5911 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_5912 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_5913 https://fairsharing.org/FAIRsharing.cp0ybc) BOT                    |                                |
|                      | TopBraid Composer        |                                |
|                      | VocBench                 |                                |

---
## Operations

### Ontology annotation

Ontoloy Annotation is the process of linking free text or data items to 'tokens' (defined terms from a lexicon) which provide semantic value. For example,  "type 2 diabetes" can be annotated with corresponding [term](http://purl.obolibrary.org/obo/MONDO_0005148) in the MONDO (URL_TO_INSERT_RECORD_5915 https://fairsharing.org/FAIRsharing.b2979t)  disease ontology (URL_TO_INSERT_TERM_5914 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_5916 https://fairsharing.org/FAIRsharing.8b6wfq) . 

__Curated tools__

|Tool|Description|License|Topics|Resource Type|How to use|
|---|--|--|--|--|--|
|[ZOOMA](https://www.ebi.ac.uk/spot/zooma/)|A tool for map (URL_TO_INSERT_RECORD_5920 https://fairsharing.org/FAIRsharing.53edcc) ping free text annotations to ontology (URL_TO_INSERT_TERM_5919 https://fairsharing.org/search?recordType=terminology_artefact)  term based on a curated repository (URL_TO_INSERT_TERM_5917 https://fairsharing.org/search?recordType=repository)  of annotation knowledge.|[EMBL-EBI Terms of Use](https://www.ebi.ac.uk/about/terms-of-use/)|Ontology and terminology (URL_TO_INSERT_TERM_5918 https://fairsharing.org/search?recordType=terminology_artefact) ,<br>Systems biology,<br>Data identity and map (URL_TO_INSERT_RECORD_5921 https://fairsharing.org/FAIRsharing.53edcc) ping|Web application,<br> API|[ZOOMA-Getting started](https://www.ebi.ac.uk/spot/zooma/docs/search)|
|[NCBI BioPortal (URL_TO_INSERT_RECORD_5924 https://fairsharing.org/FAIRsharing.4m97ah)  Annotator](https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_5927 https://fairsharing.org/FAIRsharing.4m97ah) /annotatorplus)|Get annotations for biomedical text with classes from the ontologies (URL_TO_INSERT_TERM_5923 https://fairsharing.org/search?recordType=terminology_artefact) .|[BioPortal (URL_TO_INSERT_RECORD_5925 https://fairsharing.org/FAIRsharing.4m97ah)  Terms of Use](https://www.bioontology.org/terms/)|Ontology and terminology (URL_TO_INSERT_TERM_5922 https://fairsharing.org/search?recordType=terminology_artefact) ,<br>Systems biology,<br>Data identity and map (URL_TO_INSERT_RECORD_5929 https://fairsharing.org/FAIRsharing.53edcc) ping|Web application,<br> API|[BioPortal (URL_TO_INSERT_RECORD_5926 https://fairsharing.org/FAIRsharing.4m97ah)  help](https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_5928 https://fairsharing.org/FAIRsharing.4m97ah) /help?pop=true#Annotator_Tab)|
|[BioBert](https://github.com (URL_TO_INSERT_RECORD_5931 https://fairsharing.org/FAIRsharing.c55d5e) /dmis-lab/biobert)|A biomedical language representation model (URL_TO_INSERT_TERM_5930 https://fairsharing.org/search?recordType=model_and_format)  designed for biomedical text mining tasks such as biomedical named entity recognition, relation extraction, question answering.|[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)|text mining,<br> named-entity recognition,<br> natural language processing|Python|
|[Termite](https://www.scibite.com/platform/termite/)|Semantic enrichment to unlock the value of unstructured text and simplify the identification of new potential biomarker leads from scientific text.|Commercial license|Ontology (URL_TO_INSERT_TERM_5933 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5932 https://fairsharing.org/search?recordType=terminology_artefact) |
|[PoolParty Semantic Suite](https://semantic-web.com/poolparty-semantic-suite/)|Automate the handling of heterogeneous metadata systems and the creation of enterprise knowledge graphs.design knowledge graphs at your own pace and with speed. Create your own ontologies (URL_TO_INSERT_TERM_5934 https://fairsharing.org/search?recordType=terminology_artefact)  and custom schemes by reusing already existing ontologies (URL_TO_INSERT_TERM_5935 https://fairsharing.org/search?recordType=terminology_artefact)  such as FO (URL_TO_INSERT_RECORD_5937 https://fairsharing.org/FAIRsharing.ca63ce) AF, FIBO, schema.org (URL_TO_INSERT_RECORD_5936 https://fairsharing.org/FAIRsharing.hzdzq8)  and CHEBI, among others. Apply them to your existing taxonomies with ease.|Commercial license|Content enrichment,<br>Data integration|
|[OntoMaton](https://github.com (URL_TO_INSERT_RECORD_5939 https://fairsharing.org/FAIRsharing.c55d5e) /ISA-tools/OntoMaton)| A tool facilitating ontology (URL_TO_INSERT_TERM_5938 https://fairsharing.org/search?recordType=terminology_artefact)  search (URL_TO_INSERT_RECORD_5940 https://fairsharing.org/FAIRsharing.52b22c)  and tagging functionalities within Google Spreadsheets.|[CPAL license](https://opensource.org/licenses/CPAL-1.0)||Google Add-ons|
|[Prodigy](https://prodi.gy/)|A modern annotation tool for creating training and evaluation data for machine learning model (URL_TO_INSERT_TERM_5941 https://fairsharing.org/search?recordType=model_and_format) s. You can also use Prodigy to help you inspect and clean your data, do error analysis and develop rule-based systems to use in combination with your statistical model (URL_TO_INSERT_TERM_5942 https://fairsharing.org/search?recordType=model_and_format) s.|Commercial license|Data annotation|Python, Web application,API|
|[OntoText](https://www.ontotext.com/products/ontotext-platform/)|Connect and publish complex enterprise knowledge with standard (URL_TO_INSERT_TERM_5943 https://fairsharing.org/search?fairsharingRegistry=Standard) -compliant semantic graph database (URL_TO_INSERT_TERM_5944 https://fairsharing.org/search?fairsharingRegistry=Database) ; Customize and apply analytics to link documents to graphs, extract new facts, classify and recommend content.|Commercial license|

__Related tools in [Bio.Tools (URL_TO_INSERT_RECORD_5945 https://fairsharing.org/FAIRsharing.63520c) ](https://bio.tools (URL_TO_INSERT_RECORD_5946 https://fairsharing.org/FAIRsharing.63520c) )__

| Tool| Description| License | Topics | Resource Type |
|-------|--------|---------|----|--------|
| [bioBERT](https://bio.tools (URL_TO_INSERT_RECORD_5950 https://fairsharing.org/FAIRsharing.63520c) /BioBERT) | A pre-trained weights of BioBERT, a language representation model (URL_TO_INSERT_TERM_5947 https://fairsharing.org/search?recordType=model_and_format)  for biomedical domain, especially designed for biomedical text mining tasks such as biomedical named entity recognition, relation extraction, question answering, etc.|  N/A | Medicine, Ontology (URL_TO_INSERT_TERM_5949 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5948 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing  |Python|
|[PPR-SSM](https://bio.tools (URL_TO_INSERT_RECORD_5954 https://fairsharing.org/FAIRsharing.63520c) /PPR-SSM)| Personalized PageRank and semantic similarity measures for linking entities found in documents to concepts from domain-specific ontologies (URL_TO_INSERT_TERM_5953 https://fairsharing.org/search?recordType=terminology_artefact) . |N/A| Imaging, Natural language processing, Data mining, Genotype and phenotype, Ontology (URL_TO_INSERT_TERM_5952 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5951 https://fairsharing.org/search?recordType=terminology_artefact)         |Java, Python|
|[HPO2GO](https://bio.tools (URL_TO_INSERT_RECORD_5966 https://fairsharing.org/FAIRsharing.63520c) /HPO2GO)| Prediction of human phenotype ontology (URL_TO_INSERT_TERM_5956 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_5964 https://fairsharing.org/FAIRsharing.kbtt7f)  term associations using cross ontology (URL_TO_INSERT_TERM_5957 https://fairsharing.org/search?recordType=terminology_artefact)  annotation co-occurrences.Map (URL_TO_INSERT_RECORD_5963 https://fairsharing.org/FAIRsharing.53edcc) ping between Human Phenotype Ontology (URL_TO_INSERT_TERM_5958 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_5965 https://fairsharing.org/FAIRsharing.kbtt7f)  (HPO) and Gene Ontology (URL_TO_INSERT_TERM_5959 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_5962 https://fairsharing.org/FAIRsharing.6xq0ee)  (GO) terms for the prediction of gene/protein - function - phenotype - disease associations.|[GPL-3.0](https://spdx.org/licenses/GPL-3.0)| Pathology, Protein (URL_TO_INSERT_RECORD_5961 https://fairsharing.org/FAIRsharing.rtndct)  interactions, Genotype and phenotype, Ontology (URL_TO_INSERT_TERM_5960 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5955 https://fairsharing.org/search?recordType=terminology_artefact) , Gene expression| Command-line tool |
| [Vapur](https://bio.tools (URL_TO_INSERT_RECORD_5976 https://fairsharing.org/FAIRsharing.63520c) /vapur)| A Search (URL_TO_INSERT_RECORD_5974 https://fairsharing.org/FAIRsharing.52b22c)  Engine to Find Related Protein (URL_TO_INSERT_RECORD_5969 https://fairsharing.org/FAIRsharing.rtndct) .Vapur is an online entity-oriented search (URL_TO_INSERT_RECORD_5975 https://fairsharing.org/FAIRsharing.52b22c)  engine for the CO (URL_TO_INSERT_RECORD_5970 https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD_5972 https://fairsharing.org/FAIRsharing.thskvr) VID-19 anthology. Vapur is empowered with a semantic inverted index that is created through named entity recognition and relation extraction on CO (URL_TO_INSERT_RECORD_5971 https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD_5973 https://fairsharing.org/FAIRsharing.thskvr) RD-19 abstracts. |N/A| Pathology, Ontology (URL_TO_INSERT_TERM_5968 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5967 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing, Enzymes |Python|
| [matscholar](https://bio.tools (URL_TO_INSERT_RECORD_5981 https://fairsharing.org/FAIRsharing.63520c) /matscholar)| A Python library for materials-focused natural language processing (NLP). Named Entity Recognition and Normalization Applied to Large-Scale Informat (URL_TO_INSERT_TERM_5977 https://fairsharing.org/search?recordType=model_and_format) ion Extraction from the Materials Science Literature.|[MIT](https://spdx.org/licenses/MIT)| Chemistry (URL_TO_INSERT_RECORD_5980 https://fairsharing.org/3524) , Ontology (URL_TO_INSERT_TERM_5979 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5978 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing | Command-line tool |
|[CollaboNet](https://bio.tools (URL_TO_INSERT_RECORD_5984 https://fairsharing.org/FAIRsharing.63520c) /collabonet)| Collaboration of deep neural networks for biomedical named entity recognition.|[MIT](https://spdx.org/licenses/MIT)| Ontology (URL_TO_INSERT_TERM_5983 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5982 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing, Machine learning | Command-line tool |
| [Calchas](https://bio.tools (URL_TO_INSERT_RECORD_5992 https://fairsharing.org/FAIRsharing.63520c) /calchas)| A web based framework that takes advantage of domain specific ontologies (URL_TO_INSERT_TERM_5990 https://fairsharing.org/search?recordType=terminology_artefact) , and Natural Language Processing, aiming to empower exploration of biomedical resources via semantic-based querying and search (URL_TO_INSERT_RECORD_5991 https://fairsharing.org/FAIRsharing.52b22c) . The NLP engine analyzes the input free-text query and translates it into targeted queries with terms from the underlying ontology (URL_TO_INSERT_TERM_5988 https://fairsharing.org/search?recordType=terminology_artefact) . | N/A | Medical informat (URL_TO_INSERT_TERM_5985 https://fairsharing.org/search?recordType=model_and_format) ics, Ontology (URL_TO_INSERT_TERM_5989 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5987 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing, Bioinformat (URL_TO_INSERT_TERM_5986 https://fairsharing.org/search?recordType=model_and_format) ics| Web application   |
|[QTL TableMiner++(QTM)](https://bio.tools (URL_TO_INSERT_RECORD_5999 https://fairsharing.org/FAIRsharing.63520c) /QTM) | It is a command-line tool to retrieve and semantically annotate results obtained from QTL map (URL_TO_INSERT_RECORD_5998 https://fairsharing.org/FAIRsharing.53edcc) ping experiments. It takes full-text articles from the Europe PMC (URL_TO_INSERT_RECORD_5997 https://fairsharing.org/FAIRsharing.cmw6mm)  (URL_TO_INSERT_RECORD_6000 https://fairsharing.org/FAIRsharing.wpt5mp)  repository (URL_TO_INSERT_TERM_5994 https://fairsharing.org/search?recordType=repository)  as input and outputs the extracted QTLs into a relational database (URL_TO_INSERT_TERM_5993 https://fairsharing.org/search?fairsharingRegistry=Database)  (SQLite) and text file (CSV).|[Apache-2.0](https://spdx.org/licenses/Apache-2.0)| Ontology (URL_TO_INSERT_TERM_5996 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_5995 https://fairsharing.org/search?recordType=terminology_artefact) | Command-line tool |
| [thbp](https://bio.tools (URL_TO_INSERT_RECORD_6005 https://fairsharing.org/FAIRsharing.63520c) /thbp)| Map (URL_TO_INSERT_RECORD_6003 https://fairsharing.org/FAIRsharing.53edcc) ping anatomical related entities to human body parts based on wikiped (URL_TO_INSERT_RECORD_6004 https://fairsharing.org/FAIRsharing.31385c) ia in discharge summaries.|N/A| Anatomy, Ontology (URL_TO_INSERT_TERM_6002 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_6001 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing||

### Ontology mapping

The process of determining correspondences between equivalent concepts in alternative ontologies (URL_TO_INSERT_TERM_6006 https://fairsharing.org/search?recordType=terminology_artefact) , and other vocabularies. This may include map (URL_TO_INSERT_RECORD_6007 https://fairsharing.org/FAIRsharing.53edcc) ping to convey different levels of granularity.

__Curated tools__

|Tool|Description|License|Topics|Resource Type|How to use|
|---|--|--|--|--|--|
|[OxO](https://www.ebi.ac.uk/spot/oxo (URL_TO_INSERT_RECORD_6011 https://fairsharing.org/FAIRsharing.0c6fea) /index)|A service for finding map (URL_TO_INSERT_RECORD_6010 https://fairsharing.org/FAIRsharing.53edcc) pings (or cross-references) between terms from ontologies (URL_TO_INSERT_TERM_6009 https://fairsharing.org/search?recordType=terminology_artefact) , vocabularies and coding standard (URL_TO_INSERT_TERM_6008 https://fairsharing.org/search?fairsharingRegistry=Standard) s. |[EMBL-EBI Terms of Use](https://www.ebi.ac.uk/about/terms-of-use/)|Ontology alignment| GUI and API| |

__Related tools in [Bio.Tools (URL_TO_INSERT_RECORD_6012 https://fairsharing.org/FAIRsharing.63520c) ](https://bio.tools (URL_TO_INSERT_RECORD_6013 https://fairsharing.org/FAIRsharing.63520c) )__

| Tool| Description| License | Topics     | Type|
|-------|--|---------|----|---|
|[meshr](https://bio.tools (URL_TO_INSERT_RECORD_6016 https://fairsharing.org/FAIRsharing.63520c) /meshr)| A set of annotation map (URL_TO_INSERT_RECORD_6015 https://fairsharing.org/FAIRsharing.53edcc) s describing the entire MeSH assembled using data from MeSH. |[Apache-2.0](https://spdx.org/licenses/Apache-2.0)| Medical informat (URL_TO_INSERT_TERM_6014 https://fairsharing.org/search?recordType=model_and_format) ics, Data quality management  | Command-line tool, Library |
| [locdb](https://bio.tools (URL_TO_INSERT_RECORD_6022 https://fairsharing.org/FAIRsharing.63520c) /locdb) | Manually curated database (URL_TO_INSERT_TERM_6017 https://fairsharing.org/search?fairsharingRegistry=Database)  with experimental annotations for the subcellular localizations of proteins in Homo sapiens (HS, human) and Arabidopsis thaliana (AT, thale cress). | N/A | Ontology (URL_TO_INSERT_TERM_6020 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_6019 https://fairsharing.org/search?recordType=terminology_artefact) , Data submission, annotation and curation, Protein (URL_TO_INSERT_RECORD_6021 https://fairsharing.org/FAIRsharing.rtndct) s | Database (URL_TO_INSERT_TERM_6018 https://fairsharing.org/search?fairsharingRegistry=Database)  portal|


### Ontology management

The process of managing ontologies (URL_TO_INSERT_TERM_6024 https://fairsharing.org/search?recordType=terminology_artefact)  and other vocabularies in semantic web-linked data environments.This includes policies (URL_TO_INSERT_TERM_6023 https://fairsharing.org/search?fairsharingRegistry=Policy)  for update and maintenance of constituent and new terms.

__Curated tools__

|Tool|Description|License|Topics|Resource Type|How to use|
|---|--|--|--|--|--|
|[OLS](https://www.ebi.ac.uk/ols/index (URL_TO_INSERT_RECORD_6029 https://fairsharing.org/FAIRsharing.Mkl9RR) )|a repository (URL_TO_INSERT_TERM_6025 https://fairsharing.org/search?recordType=repository)  for biomedical ontologies (URL_TO_INSERT_TERM_6028 https://fairsharing.org/search?recordType=terminology_artefact)  that aims to provide a single point of access to the latest ontology (URL_TO_INSERT_TERM_6027 https://fairsharing.org/search?recordType=terminology_artefact)  versions.|[EMBL-EBI Terms of Use](https://www.ebi.ac.uk/about/terms-of-use/)|Ontology and terminology (URL_TO_INSERT_TERM_6026 https://fairsharing.org/search?recordType=terminology_artefact) |Web Application, API|
|[BioPortal](https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_6034 https://fairsharing.org/FAIRsharing.4m97ah) /)|A repository (URL_TO_INSERT_TERM_6030 https://fairsharing.org/search?recordType=repository)  of biomedical ontologies (URL_TO_INSERT_TERM_6032 https://fairsharing.org/search?recordType=terminology_artefact) .|[BioPortal (URL_TO_INSERT_RECORD_6033 https://fairsharing.org/FAIRsharing.4m97ah)  Terms of Use](https://www.bioontology.org/terms/)|Ontology and terminology (URL_TO_INSERT_TERM_6031 https://fairsharing.org/search?recordType=terminology_artefact) |Web Application, API|
|[PoolParty](https://www.poolparty.biz/) |Knowledge Engineering & Knowledge Graph Management. Taxonomy, ontology (URL_TO_INSERT_TERM_6036 https://fairsharing.org/search?recordType=terminology_artefact)  and linked dataset management. |Commercial license|Ontology (URL_TO_INSERT_TERM_6037 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_6035 https://fairsharing.org/search?recordType=terminology_artefact) |
|[Centree Ontology (URL_TO_INSERT_TERM_6038 https://fairsharing.org/search?recordType=terminology_artefact)  Manager](https://www.scibite.com/platform/centree/)|A centralised, enterprise-ready resource for ontology (URL_TO_INSERT_TERM_6039 https://fairsharing.org/search?recordType=terminology_artefact)  management and transforms the experience of maintaining and releasing ontologies (URL_TO_INSERT_TERM_6040 https://fairsharing.org/search?recordType=terminology_artefact)  for research (URL_TO_INSERT_RECORD_6041 https://fairsharing.org/FAIRsharing.52b22c) -led businesses.|Commercial license||Web application, API|
|[Ontobee](http://www.ontobee.org (URL_TO_INSERT_RECORD_6045 https://fairsharing.org/FAIRsharing.q8fx1b) /)|A linked data server designed for ontologies (URL_TO_INSERT_TERM_6043 https://fairsharing.org/search?recordType=terminology_artefact) . Ontobee (URL_TO_INSERT_RECORD_6044 https://fairsharing.org/FAIRsharing.q8fx1b)  is aimed to facilitate ontology (URL_TO_INSERT_TERM_6042 https://fairsharing.org/search?recordType=terminology_artefact)  data sharing, visualization, query, integration, and analysis.|[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)||Web application|
|[AberOWL](http://www.aber-owl.net/)|A framework for ontology (URL_TO_INSERT_TERM_6048 https://fairsharing.org/search?recordType=terminology_artefact) -based access to biological data. It consists of a repository (URL_TO_INSERT_TERM_6046 https://fairsharing.org/search?recordType=repository)  of bio-ontologies (URL_TO_INSERT_TERM_6050 https://fairsharing.org/search?recordType=terminology_artefact) , a set of webservices which provide access to OWL (URL_TO_INSERT_RECORD_6052 https://fairsharing.org/FAIRsharing.atygwy) (-EL) reasoning over the ontologies (URL_TO_INSERT_TERM_6051 https://fairsharing.org/search?recordType=terminology_artefact) , and several frontends which utilise the ontology (URL_TO_INSERT_TERM_6049 https://fairsharing.org/search?recordType=terminology_artefact)  repository (URL_TO_INSERT_TERM_6047 https://fairsharing.org/search?recordType=repository)  and reasoning services.|||Web application, API|


__Related tools in [Bio.Tools (URL_TO_INSERT_RECORD_6053 https://fairsharing.org/FAIRsharing.63520c) ](https://bio.tools (URL_TO_INSERT_RECORD_6054 https://fairsharing.org/FAIRsharing.63520c) )__

| Tool| Description  | License | Topics | Type|
|---|--|--|--|--|
|[ngly1](https://bio.tools (URL_TO_INSERT_RECORD_6060 https://fairsharing.org/FAIRsharing.63520c) /ngly1)| A repository (URL_TO_INSERT_TERM_6055 https://fairsharing.org/search?recordType=repository)  for the NGLY1 Deficiency Knowledge Graph, the reasoning context to support hypothesis discovery for NGLY1 Deficiency-CDDG (DOID (URL_TO_INSERT_RECORD_6058 https://fairsharing.org/FAIRsharing.8b6wfq) :0060728) research (URL_TO_INSERT_RECORD_6059 https://fairsharing.org/FAIRsharing.52b22c) . The user can navigate the knowledge in the graph in the Neo4j Browser website. | N/A  | Molecular interactions, pathways and networks, Ontology (URL_TO_INSERT_TERM_6057 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_6056 https://fairsharing.org/search?recordType=terminology_artefact) , Machine learning       | Command-line tool |
| [Doc2Hpo](https://bio.tools (URL_TO_INSERT_RECORD_6065 https://fairsharing.org/FAIRsharing.63520c) /doc2hpo) | Web application for efficient and accurate Human Phenotype Ontology (URL_TO_INSERT_TERM_6062 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_6064 https://fairsharing.org/FAIRsharing.kbtt7f)  (HPO) concept curation. |[Unlicense](https://spdx.org/licenses/Unlicense) | Genotype and phenotype, Ontology (URL_TO_INSERT_TERM_6063 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_6061 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing| Web application |
| [PlanGexQ](https://bio.tools (URL_TO_INSERT_RECORD_6070 https://fairsharing.org/FAIRsharing.63520c) /PlanGexQ)| A user-friendly interactive tool for the curation and annotation of planarian morphologies and gene expression patterns in a centralized database (URL_TO_INSERT_TERM_6066 https://fairsharing.org/search?fairsharingRegistry=Database) .|N/A | Mathematics, Genotype and phenotype, Model (URL_TO_INSERT_TERM_6067 https://fairsharing.org/search?recordType=model_and_format)  organisms, Ontology (URL_TO_INSERT_TERM_6069 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_6068 https://fairsharing.org/search?recordType=terminology_artefact) , Gene expression |  |
|[GOcats](https://bio.tools (URL_TO_INSERT_RECORD_6076 https://fairsharing.org/FAIRsharing.63520c) /gocats)|Advances in gene ontology (URL_TO_INSERT_TERM_6072 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_6074 https://fairsharing.org/FAIRsharing.6xq0ee)  utilization improve statistical power of annotation enrichment.|N/A| Map (URL_TO_INSERT_RECORD_6075 https://fairsharing.org/FAIRsharing.53edcc) ping, Ontology (URL_TO_INSERT_TERM_6073 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_6071 https://fairsharing.org/search?recordType=terminology_artefact) , Microarray experiment     | Command-line tool                      |
| [RDFScape](https://bio.tools (URL_TO_INSERT_RECORD_6083 https://fairsharing.org/FAIRsharing.63520c) /rdfscape) | This is a project (URL_TO_INSERT_TERM_6077 https://fairsharing.org/search?recordType=project)  that brings Semantic Web features to the popular Systems Biology software Cytoscape. It allows to query, visualize and reason on ontologies (URL_TO_INSERT_TERM_6080 https://fairsharing.org/search?recordType=terminology_artefact)  represented in OWL (URL_TO_INSERT_RECORD_6081 https://fairsharing.org/FAIRsharing.atygwy)  or RDF (URL_TO_INSERT_RECORD_6082 https://fairsharing.org/FAIRsharing.p77ph9)  within Cytoscape.  |         | Systems biology, Ontology (URL_TO_INSERT_TERM_6079 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_6078 https://fairsharing.org/search?recordType=terminology_artefact) , Biology    | Desktop application                    |
| [OntoBrowser](https://bio.tools (URL_TO_INSERT_RECORD_6094 https://fairsharing.org/FAIRsharing.63520c) /ontobrowser)| The tool was developed (URL_TO_INSERT_RECORD_6093 https://fairsharing.org/FAIRsharing.31385c)  to manage ontologies (URL_TO_INSERT_TERM_6089 https://fairsharing.org/search?recordType=terminology_artefact)  (and controlled terminologies (URL_TO_INSERT_TERM_6086 https://fairsharing.org/search?recordType=terminology_artefact)  e.g. CDI (URL_TO_INSERT_RECORD_6090 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_6096 https://fairsharing.org/3525)  SEND (URL_TO_INSERT_RECORD_6095 https://fairsharing.org/FAIRsharing.7z842d) ). The primary goal of the tool is to provide an online collaborative solution for expert curators to map (URL_TO_INSERT_RECORD_6091 https://fairsharing.org/FAIRsharing.53edcc)  code list terms (sourced from multiple systems/database (URL_TO_INSERT_TERM_6084 https://fairsharing.org/search?fairsharingRegistry=Database) s) to preferred ontology (URL_TO_INSERT_TERM_6087 https://fairsharing.org/search?recordType=terminology_artefact)  terms.|[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)| Ontology (URL_TO_INSERT_TERM_6088 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_6085 https://fairsharing.org/search?recordType=terminology_artefact) , Data identity and map (URL_TO_INSERT_RECORD_6092 https://fairsharing.org/FAIRsharing.53edcc) ping      | Web API, Web application               |
|[QuickGO](https://bio.tools (URL_TO_INSERT_RECORD_6101 https://fairsharing.org/FAIRsharing.63520c) /quickgo)| A fast browser for Gene Ontology (URL_TO_INSERT_TERM_6098 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_6100 https://fairsharing.org/FAIRsharing.6xq0ee)  terms and annotations.    |         | Ontology (URL_TO_INSERT_TERM_6099 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_6097 https://fairsharing.org/search?recordType=terminology_artefact)       | Web application                        |
|[Circular Gene Ontology (URL_TO_INSERT_TERM_6103 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_6106 https://fairsharing.org/FAIRsharing.6xq0ee)  (CirGO)](https://bio.tools (URL_TO_INSERT_RECORD_6108 https://fairsharing.org/FAIRsharing.63520c) /cirgo)| Visualises non-redundant two-level hierarch (URL_TO_INSERT_RECORD_6107 https://fairsharing.org/FAIRsharing.52b22c) ically structured ontology (URL_TO_INSERT_TERM_6104 https://fairsharing.org/search?recordType=terminology_artefact)  terms from gene expression data in a 2D space.   |[GPL3.0](https://spdx.org/licenses/GPL-3.0) | Ontology (URL_TO_INSERT_TERM_6105 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_6102 https://fairsharing.org/search?recordType=terminology_artefact) , Data visualisation, Gene expression| Command-line tool, Desktop application |

### Ontology engineering

Ontology (URL_TO_INSERT_TERM_6109 https://fairsharing.org/search?recordType=terminology_artefact)  engineering is the process of developing and maintaining ontologies (URL_TO_INSERT_TERM_6111 https://fairsharing.org/search?recordType=terminology_artefact)  during the ontology (URL_TO_INSERT_TERM_6110 https://fairsharing.org/search?recordType=terminology_artefact)  life cycle.

__Curated tools__

|Tool|Description|License|Topics|Resource Type|
|---|--|--|--|--|
|[Protégé](https://protege.stanford.edu/) |A free, open source ontology (URL_TO_INSERT_TERM_6112 https://fairsharing.org/search?recordType=terminology_artefact)  editor and a knowledge management system.|[2-Clause BSD](https://opensource.org/licenses/BSD-2-Clause)||Web application, Desktop application|
|[ROBOT](http://robot.obolibrary.org/)|An open source library and command-line tool for automating ontology (URL_TO_INSERT_TERM_6114 https://fairsharing.org/search?recordType=terminology_artefact)  development tasks. RO (URL_TO_INSERT_RECORD_6116 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_6117 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_6118 https://fairsharing.org/FAIRsharing.cp0ybc) BOT provides ontology (URL_TO_INSERT_TERM_6115 https://fairsharing.org/search?recordType=terminology_artefact)  processing commands for a variety of tasks, including commands for converting format (URL_TO_INSERT_TERM_6113 https://fairsharing.org/search?recordType=model_and_format) s, running a reasoner, creating import modules, running reports, and various other tasks.|[BSD 3-Clause License](https://raw.githubusercontent.com/ontodev/robot/master/LICENSE.txt)||Command-line tool|
|[OWLAPI](http://owlcs.github.io/owlapi/)|A Java API and reference implmentation for creating, manipulating and serialising OWL (URL_TO_INSERT_RECORD_6120 https://fairsharing.org/FAIRsharing.atygwy)  Ontologies (URL_TO_INSERT_TERM_6119 https://fairsharing.org/search?recordType=terminology_artefact) .|LGPL and Apache||API|
|[eNanoMap (URL_TO_INSERT_RECORD_6125 https://fairsharing.org/FAIRsharing.53edcc) per Slimmer](https://github.com (URL_TO_INSERT_RECORD_6126 https://fairsharing.org/FAIRsharing.c55d5e) /enanomapper/slimmer)|A slim tool to slim ontologies (URL_TO_INSERT_TERM_6124 https://fairsharing.org/search?recordType=terminology_artefact)  as part of ontology (URL_TO_INSERT_TERM_6121 https://fairsharing.org/search?recordType=terminology_artefact)  integration. It allows users to provide configuration files that specify which parts of an ontology (URL_TO_INSERT_TERM_6122 https://fairsharing.org/search?recordType=terminology_artefact)  should be kept and/or removed, allowing to just select parts of the ontology (URL_TO_INSERT_TERM_6123 https://fairsharing.org/search?recordType=terminology_artefact)  you like.|[MIT license](https://opensource.org/licenses/MIT)||Java|
|[TopBraid Composer](https://www.topquadrant.com/products/topbraid-composer/)|TopBraid Composer Maestro Edition is used to develop ontology (URL_TO_INSERT_TERM_6128 https://fairsharing.org/search?recordType=terminology_artefact)  model (URL_TO_INSERT_TERM_6127 https://fairsharing.org/search?recordType=model_and_format) s, configure data source integration, and create semantic services and user interfaces.|[Commercial license](https://www.topquadrant.com/legal/)||
|[VocBench](http://vocbench.uniroma2.it/)|a web-based, multilingual, collaborative development platform for managing OWL (URL_TO_INSERT_RECORD_6130 https://fairsharing.org/FAIRsharing.atygwy)  ontologies (URL_TO_INSERT_TERM_6129 https://fairsharing.org/search?recordType=terminology_artefact) , SKOS (URL_TO_INSERT_RECORD_6133 https://fairsharing.org/FAIRsharing.48e326) (/XL) thesauri, Ontolex-lemon lexicons and generic RDF (URL_TO_INSERT_RECORD_6131 https://fairsharing.org/FAIRsharing.p77ph9)  datasets.|[License](https://bitbucket.org (URL_TO_INSERT_RECORD_6132 https://fairsharing.org/FAIRsharing.fc3431) /art-uniroma2/vocbench3/src/master/LICENSE)||Desktop application|


## Implementation examples

To show how these tools can be used in real life examples, please check the related recipes.
- {ref}`fcb-selecting-ontologies (URL_TO_INSERT_TERM_6134 https://fairsharing.org/search?recordType=terminology_artefact) `
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




