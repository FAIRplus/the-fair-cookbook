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

This recipe aims to provide `an overview of tools available` to perform a number of key operations using ontologies (URL_TO_INSERT_TERM_7518 https://fairsharing.org/search?recordType=terminology_artefact)  and relevant to FAIR (URL_TO_INSERT_RECORD_7520 https://fairsharing.org/FAIRsharing.WWI10U)  processes: from `ontology (URL_TO_INSERT_TERM_7515 https://fairsharing.org/search?recordType=terminology_artefact)  management` to using `ontology (URL_TO_INSERT_TERM_7516 https://fairsharing.org/search?recordType=terminology_artefact)  for annotation` or `performing ontology (URL_TO_INSERT_TERM_7517 https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD_7519 https://fairsharing.org/FAIRsharing.53edcc) ping`.

It aims to serve as a starting point to identify tools for FAIR (URL_TO_INSERT_RECORD_7522 https://fairsharing.org/FAIRsharing.WWI10U) ification tasks where ontologies (URL_TO_INSERT_TERM_7521 https://fairsharing.org/search?recordType=terminology_artefact)  and semantic frameworks are needed. 

```{admonition} disclaimer
It is not intended to provide a comprehensive list covering all possible tools.
```

>The lists of tools are generated either automatically by querying the [bio.tools (URL_TO_INSERT_RECORD_7526 https://fairsharing.org/FAIRsharing.63520c) ](https://bio.tools (URL_TO_INSERT_RECORD_7527 https://fairsharing.org/FAIRsharing.63520c) /) repository (URL_TO_INSERT_TERM_7523 https://fairsharing.org/search?recordType=repository) , or through manual curation. In this last instance, the list produced reflects what is being used in the industry and is influenced by the FAIR (URL_TO_INSERT_RECORD_7525 https://fairsharing.org/FAIRsharing.WWI10U) plus project (URL_TO_INSERT_TERM_7524 https://fairsharing.org/search?recordType=project)  partners that have been surveyed for the purpose of this work.

```{warning} 
The content in these tables was generated in March 2021.
For an updated contents, please check the [FAIR tooling repository](https://github.com/FAIRplus/WP3_FAIR_tooling).
```


## Requirements

* recipe dependency:
   * {ref}`fcb-selecting-ontologies (URL_TO_INSERT_TERM_7528 https://fairsharing.org/search?recordType=terminology_artefact) `
* knowledge requirement:
   * be fam (URL_TO_INSERT_RECORD_7530 https://fairsharing.org/FAIRsharing.d0886a) iliar with ontologies (URL_TO_INSERT_TERM_7529 https://fairsharing.org/search?recordType=terminology_artefact)  and semantic annotation.

---

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [ontology (URL_TO_INSERT_TERM_7531 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology](http://edamontology.org (URL_TO_INSERT_RECORD_7532 https://fairsharing.org/FAIRsharing.a6r7zs) /topic_0089)  | 
| [text annotation](http://edamontology.org (URL_TO_INSERT_RECORD_7533 https://fairsharing.org/FAIRsharing.a6r7zs) /operation_3778)  |

---
## Overview

The figure below shows different ontology (URL_TO_INSERT_TERM_7534 https://fairsharing.org/search?recordType=terminology_artefact) -related operations and their relationships, together with related tools and recipes.


````{dropdown} 
:open: 
```{figure} ontology-operations-mermaid.png
---
width: 700px
name: Overview of key aspects in ontology (URL_TO_INSERT_TERM_7535 https://fairsharing.org/search?recordType=terminology_artefact)  associated processes
alt: Overview of key aspects in ontology (URL_TO_INSERT_TERM_7536 https://fairsharing.org/search?recordType=terminology_artefact)  associated processes
---
Overview of key aspects in ontology (URL_TO_INSERT_TERM_7537 https://fairsharing.org/search?recordType=terminology_artefact)  associated processes
```
````

The table below is an overview of ontology (URL_TO_INSERT_TERM_7538 https://fairsharing.org/search?recordType=terminology_artefact)  strategies tools identified. Details of each tools are provided below.

|         Topic        |       Curated tools      |   Related tools in Bio.tools (URL_TO_INSERT_RECORD_7539 https://fairsharing.org/FAIRsharing.63520c)    |
|:--------------------:|:------------------------:|:------------------------------:|
| Ontology (URL_TO_INSERT_TERM_7540 https://fairsharing.org/search?recordType=terminology_artefact)  annotation  | ZOOMA (URL_TO_INSERT_RECORD_7541 https://fairsharing.org/FAIRsharing.pdwqcr)  (URL_TO_INSERT_RECORD_7542 https://fairsharing.org/FAIRsharing.g3j5qj)                     | bioBERT                        |
|                      | NCBI BioPortal (URL_TO_INSERT_RECORD_7543 https://fairsharing.org/FAIRsharing.4m97ah)  (URL_TO_INSERT_RECORD_7544 https://fairsharing.org/FAIRsharing.4m97ah)  Annotator | PP (URL_TO_INSERT_RECORD_7545 https://fairsharing.org/FAIRsharing.tghhc4) R-SSM                        |
|                      | BioBert                  | HP (URL_TO_INSERT_RECORD_7549 https://fairsharing.org/FAIRsharing.kbtt7f) O (URL_TO_INSERT_RECORD_7546 https://fairsharing.org/FAIRsharing.3ngg40) 2 (URL_TO_INSERT_RECORD_7548 https://fairsharing.org/FAIRsharing.r1rjvx) GO (URL_TO_INSERT_RECORD_7547 https://fairsharing.org/FAIRsharing.6xq0ee)                          |
|                      | Termite                  | Vapur                          |
|                      | PoolParty Semantic Suite | matscholar                     |
|                      | OntoMaton                | CollaboNet                     |
|                      | Prodigy                  | Calchas                        |
|                      | OntoText                 | QTL TableMiner++(QTM)          |
|                      |                          | thbp                           |
| Ontology (URL_TO_INSERT_TERM_7550 https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD_7551 https://fairsharing.org/FAIRsharing.53edcc) ping     | OxO (URL_TO_INSERT_RECORD_7552 https://fairsharing.org/FAIRsharing.0c6fea)                       | meshr                          |
|                      |                          | locdb                          |
| Ontology (URL_TO_INSERT_TERM_7553 https://fairsharing.org/search?recordType=terminology_artefact)  management  | AberOWL (URL_TO_INSERT_RECORD_7554 https://fairsharing.org/FAIRsharing.atygwy)                   | ngly1                          |
|                      | BioPortal (URL_TO_INSERT_RECORD_7555 https://fairsharing.org/FAIRsharing.4m97ah)  (URL_TO_INSERT_RECORD_7556 https://fairsharing.org/FAIRsharing.4m97ah)                 | Doc2Hpo                        |
|                      | Centree Ontology (URL_TO_INSERT_TERM_7557 https://fairsharing.org/search?recordType=terminology_artefact)  Manager | PlanGexQ                       |
|                      | OLS (URL_TO_INSERT_RECORD_7558 https://fairsharing.org/FAIRsharing.Mkl9RR)                       | GO (URL_TO_INSERT_RECORD_7559 https://fairsharing.org/FAIRsharing.6xq0ee) cats                         |
|                      | Ontobee (URL_TO_INSERT_RECORD_7562 https://fairsharing.org/FAIRsharing.q8fx1b)  (URL_TO_INSERT_RECORD_7563 https://fairsharing.org/FAIRsharing.q8fx1b)                   | RDF (URL_TO_INSERT_RECORD_7561 https://fairsharing.org/FAIRsharing.p77ph9) S (URL_TO_INSERT_RECORD_7560 https://fairsharing.org/FAIRsharing.v9n3gk) cape                       |
|                      | PoolParty                | OntoBrowser                    |
|                      |                          | QuickGO (URL_TO_INSERT_RECORD_7564 https://fairsharing.org/FAIRsharing.6xq0ee)                         |
|                      |                          | Circular Gene Ontology (URL_TO_INSERT_TERM_7565 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_7566 https://fairsharing.org/FAIRsharing.6xq0ee)  (CirGO (URL_TO_INSERT_RECORD_7567 https://fairsharing.org/FAIRsharing.6xq0ee) ) |
| Ontology (URL_TO_INSERT_TERM_7568 https://fairsharing.org/search?recordType=terminology_artefact)  engineering | eNanoMap (URL_TO_INSERT_RECORD_7569 https://fairsharing.org/FAIRsharing.53edcc) per Slimmer      |                                |
|                      | OWL (URL_TO_INSERT_RECORD_7570 https://fairsharing.org/FAIRsharing.atygwy) API                   |                                |
|                      | Protégé                  |                                |
|                      | RO (URL_TO_INSERT_RECORD_7573 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_7574 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_7575 https://fairsharing.org/FAIRsharing.cp0ybc) BO (URL_TO_INSERT_RECORD_7571 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_7572 https://fairsharing.org/FAIRsharing.cbz72b) T                    |                                |
|                      | TopBraid Composer        |                                |
|                      | VocBench                 |                                |

---
## Operations

### Ontology annotation

Ontoloy Annotation is the process of linking free text or data items to 'tokens' (defined terms from a lexicon) which provide semantic value. For example,  "type 2 diabetes" can be annotated with corresponding [term](http://purl.obolibrary.org/obo/MONDO_0005148) in the MO (URL_TO_INSERT_RECORD_7579 https://fairsharing.org/FAIRsharing.qs4x5m) NDO (URL_TO_INSERT_RECORD_7577 https://fairsharing.org/FAIRsharing.b2979t)  disease ontology (URL_TO_INSERT_TERM_7576 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_7578 https://fairsharing.org/FAIRsharing.8b6wfq) . 

__Curated tools__

|Tool|Description|License|Topics|Resource Type|How to use|
|---|--|--|--|--|--|
|[ZOOMA](https://www.ebi.ac.uk/spot/zooma/)|A tool for map (URL_TO_INSERT_RECORD_7583 https://fairsharing.org/FAIRsharing.53edcc) ping free text annotations to ontology (URL_TO_INSERT_TERM_7582 https://fairsharing.org/search?recordType=terminology_artefact)  term based on a curated repository (URL_TO_INSERT_TERM_7580 https://fairsharing.org/search?recordType=repository)  of annotation knowledge.|[EMB (URL_TO_INSERT_RECORD_7587 https://fairsharing.org/FAIRsharing.a1rp4c) L-EBI Terms of Use](https://www.ebi.ac.uk/about/terms-of-use/)|Ontology and terminology (URL_TO_INSERT_TERM_7581 https://fairsharing.org/search?recordType=terminology_artefact) ,<br>Systems biology,<br>Data identity and map (URL_TO_INSERT_RECORD_7584 https://fairsharing.org/FAIRsharing.53edcc) ping|Web application,<br> API|[ZOOMA (URL_TO_INSERT_RECORD_7585 https://fairsharing.org/FAIRsharing.pdwqcr)  (URL_TO_INSERT_RECORD_7586 https://fairsharing.org/FAIRsharing.g3j5qj) -Getting started](https://www.ebi.ac.uk/spot/zooma/docs/search)|
|[NCBI BioPortal (URL_TO_INSERT_RECORD_7590 https://fairsharing.org/FAIRsharing.4m97ah)  (URL_TO_INSERT_RECORD_7593 https://fairsharing.org/FAIRsharing.4m97ah)  Annotator](https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_7596 https://fairsharing.org/FAIRsharing.4m97ah) /annotatorplus)|Get annotations for biomedical text with classes from the ontologies (URL_TO_INSERT_TERM_7589 https://fairsharing.org/search?recordType=terminology_artefact) .|[BioPortal (URL_TO_INSERT_RECORD_7591 https://fairsharing.org/FAIRsharing.4m97ah)  (URL_TO_INSERT_RECORD_7594 https://fairsharing.org/FAIRsharing.4m97ah)  Terms of Use](https://www.bioontology.org/terms/)|Ontology and terminology (URL_TO_INSERT_TERM_7588 https://fairsharing.org/search?recordType=terminology_artefact) ,<br>Systems biology,<br>Data identity and map (URL_TO_INSERT_RECORD_7598 https://fairsharing.org/FAIRsharing.53edcc) ping|Web application,<br> API|[BioPortal (URL_TO_INSERT_RECORD_7592 https://fairsharing.org/FAIRsharing.4m97ah)  (URL_TO_INSERT_RECORD_7595 https://fairsharing.org/FAIRsharing.4m97ah)  help](https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_7597 https://fairsharing.org/FAIRsharing.4m97ah) /help?pop=true#Annotator_Tab)|
|[BioBert](https://github.com (URL_TO_INSERT_RECORD_7600 https://fairsharing.org/FAIRsharing.c55d5e) /dmis-lab/biobert)|A biomedical language representation model (URL_TO_INSERT_TERM_7599 https://fairsharing.org/search?recordType=model_and_format)  designed for biomedical text mining tasks such as biomedical named entity recognition, relation extraction, question answering.|[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)|text mining,<br> named-entity recognition,<br> natural language processing|Python|
|[Termite](https://www.scibite.com/platform/termite/)|Semantic enrichment to unlock the value of unstructured text and simplify the identification of new potential biomarker leads from scientific text.|Commercial license|Ontology (URL_TO_INSERT_TERM_7602 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_7601 https://fairsharing.org/search?recordType=terminology_artefact) |
|[PoolParty Semantic Suite](https://semantic-web.com/poolparty-semantic-suite/)|Automate the handling of heterogeneous metadata systems and the creation of enterprise knowledge graphs.design knowledge graphs at your own pace and with speed. Create your own ontologies (URL_TO_INSERT_TERM_7603 https://fairsharing.org/search?recordType=terminology_artefact)  and custom schemes by reusing already existing (URL_TO_INSERT_RECORD_7606 https://fairsharing.org/FAIRsharing.q7bkqr)  ontologies (URL_TO_INSERT_TERM_7604 https://fairsharing.org/search?recordType=terminology_artefact)  such as FO (URL_TO_INSERT_RECORD_7609 https://fairsharing.org/FAIRsharing.ca63ce) AF, FIBO (URL_TO_INSERT_RECORD_7605 https://fairsharing.org/FAIRsharing.cbz72b) , schema.org (URL_TO_INSERT_RECORD_7608 https://fairsharing.org/FAIRsharing.hzdzq8)  and CHEBI, among others. Apply them to your existing (URL_TO_INSERT_RECORD_7607 https://fairsharing.org/FAIRsharing.q7bkqr)  taxonomies with ease.|Commercial license|Content enrichment,<br>Data integration|
|[OntoMaton](https://github.com (URL_TO_INSERT_RECORD_7612 https://fairsharing.org/FAIRsharing.c55d5e) /ISA-tools/OntoMaton)| A tool facilitating ontology (URL_TO_INSERT_TERM_7610 https://fairsharing.org/search?recordType=terminology_artefact)  search (URL_TO_INSERT_RECORD_7613 https://fairsharing.org/FAIRsharing.52b22c)  and tagging functionalities within Google Spreadsheets.|[CP (URL_TO_INSERT_RECORD_7611 https://fairsharing.org/FAIRsharing.wP3t2L) AL license](https://opensource.org/licenses/CPAL-1.0)||Google Add-ons|
|[Prodigy](https://prodi.gy/)|A modern annotation tool for creating training and evaluation data for machine learning model (URL_TO_INSERT_TERM_7614 https://fairsharing.org/search?recordType=model_and_format) s. You can also use Prodigy to help you inspect and clean your data, do error analysis and develop rule-based systems to use in combination with your statistical model (URL_TO_INSERT_TERM_7615 https://fairsharing.org/search?recordType=model_and_format) s.|Commercial license|Data annotation|Python, Web application,API|
|[OntoText](https://www.ontotext.com/products/ontotext-platform/)|Connect and publish complex enterprise knowledge with standard (URL_TO_INSERT_TERM_7616 https://fairsharing.org/search?fairsharingRegistry=Standard) -compliant semantic graph database (URL_TO_INSERT_TERM_7617 https://fairsharing.org/search?fairsharingRegistry=Database) ; Customize and apply analytics to link documents to graphs, extract new facts, classify and recommend content.|Commercial license|

__Related tools in [Bio.Tools (URL_TO_INSERT_RECORD_7618 https://fairsharing.org/FAIRsharing.63520c) ](https://bio.tools (URL_TO_INSERT_RECORD_7619 https://fairsharing.org/FAIRsharing.63520c) )__

| Tool| Description| License | Topics | Resource Type |
|-------|--------|---------|----|--------|
| [bioBERT](https://bio.tools (URL_TO_INSERT_RECORD_7623 https://fairsharing.org/FAIRsharing.63520c) /BioBERT) | A pre-trained weights of BioBERT, a language representation model (URL_TO_INSERT_TERM_7620 https://fairsharing.org/search?recordType=model_and_format)  for biomedical domain, especially designed for biomedical text mining tasks such as biomedical named entity recognition, relation extraction, question answering, etc.|  N/A | Medicine, Ontology (URL_TO_INSERT_TERM_7622 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_7621 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing  |Python|
|[PPR-SSM](https://bio.tools (URL_TO_INSERT_RECORD_7627 https://fairsharing.org/FAIRsharing.63520c) /PPR-SSM)| Personalized PageRank and semantic similarity measures for linking entities found in documents to concepts from domain-specific ontologies (URL_TO_INSERT_TERM_7626 https://fairsharing.org/search?recordType=terminology_artefact) . |N/A| Imaging, Natural language processing, Data mining, Genotype and phenotype, Ontology (URL_TO_INSERT_TERM_7625 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_7624 https://fairsharing.org/search?recordType=terminology_artefact)         |Java, Python|
|[HPO2GO](https://bio.tools (URL_TO_INSERT_RECORD_7642 https://fairsharing.org/FAIRsharing.63520c) /HPO2GO)| Prediction of human phenotype ontology (URL_TO_INSERT_TERM_7629 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_7639 https://fairsharing.org/FAIRsharing.kbtt7f)  term associations using cross ontology (URL_TO_INSERT_TERM_7630 https://fairsharing.org/search?recordType=terminology_artefact)  annotation co-occurrences.Map (URL_TO_INSERT_RECORD_7638 https://fairsharing.org/FAIRsharing.53edcc) ping between Human Phenotype Ontology (URL_TO_INSERT_TERM_7631 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_7640 https://fairsharing.org/FAIRsharing.kbtt7f)  (HP (URL_TO_INSERT_RECORD_7641 https://fairsharing.org/FAIRsharing.kbtt7f) O (URL_TO_INSERT_RECORD_7634 https://fairsharing.org/FAIRsharing.3ngg40) ) and Gene Ontology (URL_TO_INSERT_TERM_7632 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_7636 https://fairsharing.org/FAIRsharing.6xq0ee)  (GO (URL_TO_INSERT_RECORD_7637 https://fairsharing.org/FAIRsharing.6xq0ee) ) terms for the prediction of gene/protein - function - phenotype - disease associations.|[GPL-3.0](https://spdx.org/licenses/GPL-3.0)| Pathology, Protein (URL_TO_INSERT_RECORD_7635 https://fairsharing.org/FAIRsharing.rtndct)  interactions, Genotype and phenotype, Ontology (URL_TO_INSERT_TERM_7633 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_7628 https://fairsharing.org/search?recordType=terminology_artefact) , Gene expression| Command-line tool |
| [Vapur](https://bio.tools (URL_TO_INSERT_RECORD_7652 https://fairsharing.org/FAIRsharing.63520c) /vapur)| A Search (URL_TO_INSERT_RECORD_7650 https://fairsharing.org/FAIRsharing.52b22c)  Engine to Find Related Protein (URL_TO_INSERT_RECORD_7645 https://fairsharing.org/FAIRsharing.rtndct) .Vapur is an online entity-oriented search (URL_TO_INSERT_RECORD_7651 https://fairsharing.org/FAIRsharing.52b22c)  engine for the CO (URL_TO_INSERT_RECORD_7646 https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD_7648 https://fairsharing.org/FAIRsharing.thskvr) VID-19 anthology. Vapur is empowered with a semantic inverted index that is created through named entity recognition and relation extraction on CO (URL_TO_INSERT_RECORD_7647 https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD_7649 https://fairsharing.org/FAIRsharing.thskvr) RD-19 abstracts. |N/A| Pathology, Ontology (URL_TO_INSERT_TERM_7644 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_7643 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing, Enzymes |Python|
| [matscholar](https://bio.tools (URL_TO_INSERT_RECORD_7658 https://fairsharing.org/FAIRsharing.63520c) /matscholar)| A Python library for materials-focused natural language processing (NLP). Named Entity Recognition and Normalization Applied to Large-Scale Informat (URL_TO_INSERT_TERM_7653 https://fairsharing.org/search?recordType=model_and_format) ion Extraction from the Materials Science Literature.|[MIT](https://spdx.org/licenses/MIT)| Chemistry (URL_TO_INSERT_RECORD_7656 https://fairsharing.org/3524)  (URL_TO_INSERT_RECORD_7657 https://fairsharing.org/3524) , Ontology (URL_TO_INSERT_TERM_7655 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_7654 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing | Command-line tool |
|[CollaboNet](https://bio.tools (URL_TO_INSERT_RECORD_7661 https://fairsharing.org/FAIRsharing.63520c) /collabonet)| Collaboration of deep neural networks for biomedical named entity recognition.|[MIT](https://spdx.org/licenses/MIT)| Ontology (URL_TO_INSERT_TERM_7660 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_7659 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing, Machine learning | Command-line tool |
| [Calchas](https://bio.tools (URL_TO_INSERT_RECORD_7669 https://fairsharing.org/FAIRsharing.63520c) /calchas)| A web based framework that takes advantage of domain specific ontologies (URL_TO_INSERT_TERM_7667 https://fairsharing.org/search?recordType=terminology_artefact) , and Natural Language Processing, aiming to empower exploration of biomedical resources via semantic-based querying and search (URL_TO_INSERT_RECORD_7668 https://fairsharing.org/FAIRsharing.52b22c) . The NLP engine analyzes the input free-text query and translates it into targeted queries with terms from the underlying ontology (URL_TO_INSERT_TERM_7665 https://fairsharing.org/search?recordType=terminology_artefact) . | N/A | Medical informat (URL_TO_INSERT_TERM_7662 https://fairsharing.org/search?recordType=model_and_format) ics, Ontology (URL_TO_INSERT_TERM_7666 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_7664 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing, Bioinformat (URL_TO_INSERT_TERM_7663 https://fairsharing.org/search?recordType=model_and_format) ics| Web application   |
|[QTL TableMiner++(QTM)](https://bio.tools (URL_TO_INSERT_RECORD_7676 https://fairsharing.org/FAIRsharing.63520c) /QTM) | It is a command-line tool to retrieve and semantically annotate results obtained from QTL map (URL_TO_INSERT_RECORD_7675 https://fairsharing.org/FAIRsharing.53edcc) ping experiments. It takes full-text articles from the Europe PMC (URL_TO_INSERT_RECORD_7674 https://fairsharing.org/FAIRsharing.cmw6mm)  (URL_TO_INSERT_RECORD_7677 https://fairsharing.org/FAIRsharing.wpt5mp)  repository (URL_TO_INSERT_TERM_7671 https://fairsharing.org/search?recordType=repository)  as input and outputs the extracted QTLs into a relational database (URL_TO_INSERT_TERM_7670 https://fairsharing.org/search?fairsharingRegistry=Database)  (SQLite) and text file (CSV).|[Apache-2.0](https://spdx.org/licenses/Apache-2.0)| Ontology (URL_TO_INSERT_TERM_7673 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_7672 https://fairsharing.org/search?recordType=terminology_artefact) | Command-line tool |
| [thbp](https://bio.tools (URL_TO_INSERT_RECORD_7682 https://fairsharing.org/FAIRsharing.63520c) /thbp)| Map (URL_TO_INSERT_RECORD_7680 https://fairsharing.org/FAIRsharing.53edcc) ping anatomical related entities to human body parts based on wikiped (URL_TO_INSERT_RECORD_7681 https://fairsharing.org/FAIRsharing.31385c) ia in discharge summaries.|N/A| Anatomy, Ontology (URL_TO_INSERT_TERM_7679 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_7678 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing||

### Ontology mapping

The process of determining correspondences between equivalent concepts in alternative ontologies (URL_TO_INSERT_TERM_7683 https://fairsharing.org/search?recordType=terminology_artefact) , and other vocabularies. This may include map (URL_TO_INSERT_RECORD_7684 https://fairsharing.org/FAIRsharing.53edcc) ping to convey different levels of granularity.

__Curated tools__

|Tool|Description|License|Topics|Resource Type|How to use|
|---|--|--|--|--|--|
|[OxO](https://www.ebi.ac.uk/spot/oxo (URL_TO_INSERT_RECORD_7688 https://fairsharing.org/FAIRsharing.0c6fea) /index)|A service for finding map (URL_TO_INSERT_RECORD_7687 https://fairsharing.org/FAIRsharing.53edcc) pings (or cross-references) between terms from ontologies (URL_TO_INSERT_TERM_7686 https://fairsharing.org/search?recordType=terminology_artefact) , vocabularies and coding standard (URL_TO_INSERT_TERM_7685 https://fairsharing.org/search?fairsharingRegistry=Standard) s. |[EMB (URL_TO_INSERT_RECORD_7689 https://fairsharing.org/FAIRsharing.a1rp4c) L-EBI Terms of Use](https://www.ebi.ac.uk/about/terms-of-use/)|Ontology alignment| GUI and API| |

__Related tools in [Bio.Tools (URL_TO_INSERT_RECORD_7690 https://fairsharing.org/FAIRsharing.63520c) ](https://bio.tools (URL_TO_INSERT_RECORD_7691 https://fairsharing.org/FAIRsharing.63520c) )__

| Tool| Description| License | Topics     | Type|
|-------|--|---------|----|---|
|[meshr](https://bio.tools (URL_TO_INSERT_RECORD_7694 https://fairsharing.org/FAIRsharing.63520c) /meshr)| A set of annotation map (URL_TO_INSERT_RECORD_7693 https://fairsharing.org/FAIRsharing.53edcc) s describing the entire MeSH assembled using data from MeSH. |[Apache-2.0](https://spdx.org/licenses/Apache-2.0)| Medical informat (URL_TO_INSERT_TERM_7692 https://fairsharing.org/search?recordType=model_and_format) ics, Data quality management  | Command-line tool, Library |
| [locdb](https://bio.tools (URL_TO_INSERT_RECORD_7700 https://fairsharing.org/FAIRsharing.63520c) /locdb) | Manually curated database (URL_TO_INSERT_TERM_7695 https://fairsharing.org/search?fairsharingRegistry=Database)  with experimental annotations for the subcellular localizations of proteins in Homo sapiens (HS, human) and Arabidopsis thaliana (AT, thale cress). | N/A | Ontology (URL_TO_INSERT_TERM_7698 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_7697 https://fairsharing.org/search?recordType=terminology_artefact) , Data submission, annotation and curation, Protein (URL_TO_INSERT_RECORD_7699 https://fairsharing.org/FAIRsharing.rtndct) s | Database (URL_TO_INSERT_TERM_7696 https://fairsharing.org/search?fairsharingRegistry=Database)  portal|


### Ontology management

The process of managing ontologies (URL_TO_INSERT_TERM_7702 https://fairsharing.org/search?recordType=terminology_artefact)  and other vocabularies in semantic web-linked data environments.This includes policies (URL_TO_INSERT_TERM_7701 https://fairsharing.org/search?fairsharingRegistry=Policy)  for update and maintenance of constituent and new terms.

__Curated tools__

|Tool|Description|License|Topics|Resource Type|How to use|
|---|--|--|--|--|--|
|[OLS](https://www.ebi.ac.uk/ols/index (URL_TO_INSERT_RECORD_7707 https://fairsharing.org/FAIRsharing.Mkl9RR) )|a repository (URL_TO_INSERT_TERM_7703 https://fairsharing.org/search?recordType=repository)  for biomedical ontologies (URL_TO_INSERT_TERM_7706 https://fairsharing.org/search?recordType=terminology_artefact)  that aims to provide a single point of access to the latest ontology (URL_TO_INSERT_TERM_7705 https://fairsharing.org/search?recordType=terminology_artefact)  versions.|[EMB (URL_TO_INSERT_RECORD_7708 https://fairsharing.org/FAIRsharing.a1rp4c) L-EBI Terms of Use](https://www.ebi.ac.uk/about/terms-of-use/)|Ontology and terminology (URL_TO_INSERT_TERM_7704 https://fairsharing.org/search?recordType=terminology_artefact) |Web Application, API|
|[BioPortal](https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_7714 https://fairsharing.org/FAIRsharing.4m97ah) /)|A repository (URL_TO_INSERT_TERM_7709 https://fairsharing.org/search?recordType=repository)  of biomedical ontologies (URL_TO_INSERT_TERM_7711 https://fairsharing.org/search?recordType=terminology_artefact) .|[BioPortal (URL_TO_INSERT_RECORD_7712 https://fairsharing.org/FAIRsharing.4m97ah)  (URL_TO_INSERT_RECORD_7713 https://fairsharing.org/FAIRsharing.4m97ah)  Terms of Use](https://www.bioontology.org/terms/)|Ontology and terminology (URL_TO_INSERT_TERM_7710 https://fairsharing.org/search?recordType=terminology_artefact) |Web Application, API|
|[PoolParty](https://www.poolparty.biz/) |Knowledge Engineering & Knowledge Graph Management. Taxonomy, ontology (URL_TO_INSERT_TERM_7716 https://fairsharing.org/search?recordType=terminology_artefact)  and linked dataset management. |Commercial license|Ontology (URL_TO_INSERT_TERM_7717 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_7715 https://fairsharing.org/search?recordType=terminology_artefact) |
|[Centree Ontology (URL_TO_INSERT_TERM_7718 https://fairsharing.org/search?recordType=terminology_artefact)  Manager](https://www.scibite.com/platform/centree/)|A centralised, enterprise-ready resource for ontology (URL_TO_INSERT_TERM_7719 https://fairsharing.org/search?recordType=terminology_artefact)  management and transforms the experience of maintaining and releasing ontologies (URL_TO_INSERT_TERM_7720 https://fairsharing.org/search?recordType=terminology_artefact)  for research (URL_TO_INSERT_RECORD_7721 https://fairsharing.org/FAIRsharing.52b22c) -led businesses.|Commercial license||Web application, API|
|[Ontobee](http://www.ontobee.org (URL_TO_INSERT_RECORD_7726 https://fairsharing.org/FAIRsharing.q8fx1b) /)|A linked data server designed for ontologies (URL_TO_INSERT_TERM_7723 https://fairsharing.org/search?recordType=terminology_artefact) . Ontobee (URL_TO_INSERT_RECORD_7724 https://fairsharing.org/FAIRsharing.q8fx1b)  (URL_TO_INSERT_RECORD_7725 https://fairsharing.org/FAIRsharing.q8fx1b)  is aimed to facilitate ontology (URL_TO_INSERT_TERM_7722 https://fairsharing.org/search?recordType=terminology_artefact)  data sharing, visualization, query, integration, and analysis.|[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)||Web application|
|[AberOWL](http://www.aber-owl.net/)|A framework for ontology (URL_TO_INSERT_TERM_7729 https://fairsharing.org/search?recordType=terminology_artefact) -based access to biological data. It consists of a repository (URL_TO_INSERT_TERM_7727 https://fairsharing.org/search?recordType=repository)  of bio-ontologies (URL_TO_INSERT_TERM_7731 https://fairsharing.org/search?recordType=terminology_artefact) , a set of webservices which provide access to OWL (URL_TO_INSERT_RECORD_7733 https://fairsharing.org/FAIRsharing.atygwy) (-EL) reasoning over the ontologies (URL_TO_INSERT_TERM_7732 https://fairsharing.org/search?recordType=terminology_artefact) , and several frontends which utilise the ontology (URL_TO_INSERT_TERM_7730 https://fairsharing.org/search?recordType=terminology_artefact)  repository (URL_TO_INSERT_TERM_7728 https://fairsharing.org/search?recordType=repository)  and reasoning services.|||Web application, API|


__Related tools in [Bio.Tools (URL_TO_INSERT_RECORD_7734 https://fairsharing.org/FAIRsharing.63520c) ](https://bio.tools (URL_TO_INSERT_RECORD_7735 https://fairsharing.org/FAIRsharing.63520c) )__

| Tool| Description  | License | Topics | Type|
|---|--|--|--|--|
|[ngly1](https://bio.tools (URL_TO_INSERT_RECORD_7743 https://fairsharing.org/FAIRsharing.63520c) /ngly1)| A repository (URL_TO_INSERT_TERM_7736 https://fairsharing.org/search?recordType=repository)  for the NGLY1 Deficiency Knowledge Graph, the reasoning context to support hypothesis discovery for NGLY1 Deficiency-CDD (URL_TO_INSERT_RECORD_7740 https://fairsharing.org/FAIRsharing.b9st5p)  (URL_TO_INSERT_RECORD_7744 https://fairsharing.org/FAIRsharing.ea287c) G (DOI (URL_TO_INSERT_RECORD_7739 https://fairsharing.org/FAIRsharing.hFLKCn) D (URL_TO_INSERT_RECORD_7741 https://fairsharing.org/FAIRsharing.8b6wfq) :0060728) research (URL_TO_INSERT_RECORD_7742 https://fairsharing.org/FAIRsharing.52b22c) . The user can navigate the knowledge in the graph in the Neo4j Browser website. | N/A  | Molecular interactions, pathways and networks, Ontology (URL_TO_INSERT_TERM_7738 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_7737 https://fairsharing.org/search?recordType=terminology_artefact) , Machine learning       | Command-line tool |
| [Doc2Hpo](https://bio.tools (URL_TO_INSERT_RECORD_7751 https://fairsharing.org/FAIRsharing.63520c) /doc2hpo) | Web application for efficient and accurate Human Phenotype Ontology (URL_TO_INSERT_TERM_7746 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_7749 https://fairsharing.org/FAIRsharing.kbtt7f)  (HP (URL_TO_INSERT_RECORD_7750 https://fairsharing.org/FAIRsharing.kbtt7f) O (URL_TO_INSERT_RECORD_7748 https://fairsharing.org/FAIRsharing.3ngg40) ) concept curation. |[Unlicense](https://spdx.org/licenses/Unlicense) | Genotype and phenotype, Ontology (URL_TO_INSERT_TERM_7747 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_7745 https://fairsharing.org/search?recordType=terminology_artefact) , Natural language processing| Web application |
| [PlanGexQ](https://bio.tools (URL_TO_INSERT_RECORD_7756 https://fairsharing.org/FAIRsharing.63520c) /PlanGexQ)| A user-friendly interactive tool for the curation and annotation of planarian morphologies and gene expression patterns in a centralized database (URL_TO_INSERT_TERM_7752 https://fairsharing.org/search?fairsharingRegistry=Database) .|N/A | Mathematics, Genotype and phenotype, Model (URL_TO_INSERT_TERM_7753 https://fairsharing.org/search?recordType=model_and_format)  organisms, Ontology (URL_TO_INSERT_TERM_7755 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_7754 https://fairsharing.org/search?recordType=terminology_artefact) , Gene expression |  |
|[GOcats](https://bio.tools (URL_TO_INSERT_RECORD_7762 https://fairsharing.org/FAIRsharing.63520c) /gocats)|Advances in gene ontology (URL_TO_INSERT_TERM_7758 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_7760 https://fairsharing.org/FAIRsharing.6xq0ee)  utilization improve statistical power of annotation enrichment.|N/A| Map (URL_TO_INSERT_RECORD_7761 https://fairsharing.org/FAIRsharing.53edcc) ping, Ontology (URL_TO_INSERT_TERM_7759 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_7757 https://fairsharing.org/search?recordType=terminology_artefact) , Microarray experiment     | Command-line tool                      |
| [RDFScape](https://bio.tools (URL_TO_INSERT_RECORD_7769 https://fairsharing.org/FAIRsharing.63520c) /rdfscape) | This is a project (URL_TO_INSERT_TERM_7763 https://fairsharing.org/search?recordType=project)  that brings Semantic Web features to the popular Systems Biology software Cytoscape. It allows to query, visualize and reason on ontologies (URL_TO_INSERT_TERM_7766 https://fairsharing.org/search?recordType=terminology_artefact)  represented in OWL (URL_TO_INSERT_RECORD_7767 https://fairsharing.org/FAIRsharing.atygwy)  or RDF (URL_TO_INSERT_RECORD_7768 https://fairsharing.org/FAIRsharing.p77ph9)  within Cytoscape.  |         | Systems biology, Ontology (URL_TO_INSERT_TERM_7765 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_7764 https://fairsharing.org/search?recordType=terminology_artefact) , Biology    | Desktop application                    |
| [OntoBrowser](https://bio.tools (URL_TO_INSERT_RECORD_7780 https://fairsharing.org/FAIRsharing.63520c) /ontobrowser)| The tool was developed (URL_TO_INSERT_RECORD_7779 https://fairsharing.org/FAIRsharing.31385c)  to manage ontologies (URL_TO_INSERT_TERM_7775 https://fairsharing.org/search?recordType=terminology_artefact)  (and controlled terminologies (URL_TO_INSERT_TERM_7772 https://fairsharing.org/search?recordType=terminology_artefact)  e.g. CDI (URL_TO_INSERT_RECORD_7776 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_7782 https://fairsharing.org/3525)  (URL_TO_INSERT_RECORD_7783 https://fairsharing.org/3525)  SEND (URL_TO_INSERT_RECORD_7781 https://fairsharing.org/FAIRsharing.7z842d) ). The primary goal of the tool is to provide an online collaborative solution for expert curators to map (URL_TO_INSERT_RECORD_7777 https://fairsharing.org/FAIRsharing.53edcc)  code list terms (sourced from multiple systems/database (URL_TO_INSERT_TERM_7770 https://fairsharing.org/search?fairsharingRegistry=Database) s) to preferred ontology (URL_TO_INSERT_TERM_7773 https://fairsharing.org/search?recordType=terminology_artefact)  terms.|[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)| Ontology (URL_TO_INSERT_TERM_7774 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_7771 https://fairsharing.org/search?recordType=terminology_artefact) , Data identity and map (URL_TO_INSERT_RECORD_7778 https://fairsharing.org/FAIRsharing.53edcc) ping      | Web API, Web application               |
|[QuickGO](https://bio.tools (URL_TO_INSERT_RECORD_7788 https://fairsharing.org/FAIRsharing.63520c) /quickgo)| A fast browser for Gene Ontology (URL_TO_INSERT_TERM_7785 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_7787 https://fairsharing.org/FAIRsharing.6xq0ee)  terms and annotations.    |         | Ontology (URL_TO_INSERT_TERM_7786 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_7784 https://fairsharing.org/search?recordType=terminology_artefact)       | Web application                        |
|[Circular Gene Ontology (URL_TO_INSERT_TERM_7790 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_7793 https://fairsharing.org/FAIRsharing.6xq0ee)  (CirGO)](https://bio.tools (URL_TO_INSERT_RECORD_7795 https://fairsharing.org/FAIRsharing.63520c) /cirgo)| Visualises non-redundant two-level hierarch (URL_TO_INSERT_RECORD_7794 https://fairsharing.org/FAIRsharing.52b22c) ically structured ontology (URL_TO_INSERT_TERM_7791 https://fairsharing.org/search?recordType=terminology_artefact)  terms from gene expression data in a 2D space.   |[GPL3.0](https://spdx.org/licenses/GPL-3.0) | Ontology (URL_TO_INSERT_TERM_7792 https://fairsharing.org/search?recordType=terminology_artefact)  and terminology (URL_TO_INSERT_TERM_7789 https://fairsharing.org/search?recordType=terminology_artefact) , Data visualisation, Gene expression| Command-line tool, Desktop application |

### Ontology engineering

Ontology (URL_TO_INSERT_TERM_7796 https://fairsharing.org/search?recordType=terminology_artefact)  engineering is the process of developing and maintaining ontologies (URL_TO_INSERT_TERM_7798 https://fairsharing.org/search?recordType=terminology_artefact)  during the ontology (URL_TO_INSERT_TERM_7797 https://fairsharing.org/search?recordType=terminology_artefact)  life cycle.

__Curated tools__

|Tool|Description|License|Topics|Resource Type|
|---|--|--|--|--|
|[Protégé](https://protege.stanford.edu/) |A free, open source ontology (URL_TO_INSERT_TERM_7799 https://fairsharing.org/search?recordType=terminology_artefact)  editor and a knowledge management system.|[2-Clause BSD](https://opensource.org/licenses/BSD-2-Clause)||Web application, Desktop application|
|[ROBOT](http://robot.obolibrary.org/)|An open source library and command-line tool for automating ontology (URL_TO_INSERT_TERM_7801 https://fairsharing.org/search?recordType=terminology_artefact)  development tasks. RO (URL_TO_INSERT_RECORD_7805 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_7806 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_7807 https://fairsharing.org/FAIRsharing.cp0ybc) BO (URL_TO_INSERT_RECORD_7803 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_7804 https://fairsharing.org/FAIRsharing.cbz72b) T provides ontology (URL_TO_INSERT_TERM_7802 https://fairsharing.org/search?recordType=terminology_artefact)  processing commands for a variety of tasks, including commands for converting format (URL_TO_INSERT_TERM_7800 https://fairsharing.org/search?recordType=model_and_format) s, running a reasoner, creating import modules, running reports, and various other tasks.|[BSD 3-Clause License](https://raw.githubusercontent.com/ontodev/robot/master/LICENSE.txt)||Command-line tool|
|[OWLAPI](http://owlcs.github.io/owlapi/)|A Java API and reference implmentation for creating, manipulating and serialising OWL (URL_TO_INSERT_RECORD_7809 https://fairsharing.org/FAIRsharing.atygwy)  Ontologies (URL_TO_INSERT_TERM_7808 https://fairsharing.org/search?recordType=terminology_artefact) .|LGPL and Apache||API|
|[eNanoMap (URL_TO_INSERT_RECORD_7814 https://fairsharing.org/FAIRsharing.53edcc) per Slimmer](https://github.com (URL_TO_INSERT_RECORD_7815 https://fairsharing.org/FAIRsharing.c55d5e) /enanomapper/slimmer)|A slim tool to slim ontologies (URL_TO_INSERT_TERM_7813 https://fairsharing.org/search?recordType=terminology_artefact)  as part of ontology (URL_TO_INSERT_TERM_7810 https://fairsharing.org/search?recordType=terminology_artefact)  integration. It allows users to provide configuration files that specify which parts of an ontology (URL_TO_INSERT_TERM_7811 https://fairsharing.org/search?recordType=terminology_artefact)  should be kept and/or removed, allowing to just select parts of the ontology (URL_TO_INSERT_TERM_7812 https://fairsharing.org/search?recordType=terminology_artefact)  you like.|[MIT license](https://opensource.org/licenses/MIT)||Java|
|[TopBraid Composer](https://www.topquadrant.com/products/topbraid-composer/)|TopBraid Composer Maestro Edition is used to develop ontology (URL_TO_INSERT_TERM_7817 https://fairsharing.org/search?recordType=terminology_artefact)  model (URL_TO_INSERT_TERM_7816 https://fairsharing.org/search?recordType=model_and_format) s, configure data source integration, and create semantic services and user interfaces.|[Commercial license](https://www.topquadrant.com/legal/)||
|[VocBench](http://vocbench.uniroma2.it/)|a web-based, multilingual, collaborative development platform for managing OWL (URL_TO_INSERT_RECORD_7819 https://fairsharing.org/FAIRsharing.atygwy)  ontologies (URL_TO_INSERT_TERM_7818 https://fairsharing.org/search?recordType=terminology_artefact) , SKOS (URL_TO_INSERT_RECORD_7822 https://fairsharing.org/FAIRsharing.48e326) (/XL) thesauri, Ontolex-lemon lexicons and generic RDF (URL_TO_INSERT_RECORD_7820 https://fairsharing.org/FAIRsharing.p77ph9)  datasets.|[License](https://bitbucket.org (URL_TO_INSERT_RECORD_7821 https://fairsharing.org/FAIRsharing.fc3431) /art-uniroma2/vocbench3/src/master/LICENSE)||Desktop application|


## Implementation examples

To show how these tools can be used in real life examples, please check the related recipes.
- {ref}`fcb-selecting-ontologies (URL_TO_INSERT_TERM_7823 https://fairsharing.org/search?recordType=terminology_artefact) `
- {ref}`fcb-interop-ontorobot`
<!-- - [Which vocabulary to use?](https://fairplus.github.io/the-fair-cookbook/content/recipes/interoperability/selecting-ontologies.html)
- [Building an application ontology (URL_TO_INSERT_TERM_7824 https://fairsharing.org/search?recordType=terminology_artefact)  with Robot](https://fairplus.github.io/the-fair-cookbook/content/recipes/interoperability/ontology-robot-recipe.html) -->


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




