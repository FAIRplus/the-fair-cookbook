(fcb-interop-onto-op)=
# Ontology-related tools and services


````{panels_fairplus}
:identifier_text: FCB022
:identifier_link: https://w3id.org/faircookbook/FCB022
:difficulty_level: 5
:recipe_type: survey_review
:reading_time_minutes: 15
:intended_audience: data_curator, data_manager, data_scientist, ontologist, software_engineer, terminology_manager  
:has_executable_code: nope
:recipe_name: Ontology-related tools and services
```` 


## Main Objectives

This recipe aims to provide `an overview of tools available` to perform a number of key operations using ontologies and relevant to FAIR processes: from `ontology management` to using `ontology for annotation` or `performing ontology mapping`.

It aims to serve as a starting point to identify tools for FAIRification tasks where ontologies and semantic frameworks are needed. 

```{admonition} disclaimer
It is not intended to provide a comprehensive list covering all possible tools.
```

>The lists of tools are generated either automatically by querying the [bio.tools](https://bio.tools/) repository, or through manual curation. In this last instance, the list produced reflects what is being used in the industry and is influenced by the FAIRplus project partners that have been surveyed for the purpose of this work.

```{warning} 
The content in these tables was generated in March 2021.
For an updated contents, please check the [FAIR tooling repository](https://github.com/FAIRplus/WP3_FAIR_tooling).
```


## Requirements

* recipe dependency:
   * {ref}`fcb-selecting-ontologies`
* knowledge requirement:
   * be familiar with ontologies and semantic annotation.

---
## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Interoperability | minimal | automatable |
---

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [ontology and terminology](http://edamontology.org/topic_0089)  | 
| [text annotation](http://edamontology.org/operation_3778)  |

---
## Overview

The figure below shows different ontology-related operations and their relationships, together with related tools and recipes.
 
```{figure} ontology-operations-mermaid.png
---
width: 700px
name: Overview of key aspects in ontology associated processes
alt: Overview of key aspects in ontology associated processes
---
Overview of key aspects in ontology associated processes
```
The table below is an overview of ontology strategies tools identified. Details of each tools are provided below.

|         Topic        |       Curated tools      |   Related tools in Bio.tools   |
|:--------------------:|:------------------------:|:------------------------------:|
| Ontology annotation  | ZOOMA                    | bioBERT                        |
|                      | NCBI BioPortal Annotator | PPR-SSM                        |
|                      | BioBert                  | HPO2GO                         |
|                      | Termite                  | Vapur                          |
|                      | PoolParty Semantic Suite | matscholar                     |
|                      | OntoMaton                | CollaboNet                     |
|                      | Prodigy                  | Calchas                        |
|                      | OntoText                 | QTL TableMiner++(QTM)          |
|                      |                          | thbp                           |
| Ontology mapping     | OxO                      | meshr                          |
|                      |                          | locdb                          |
| Ontology management  | AberOWL                  | ngly1                          |
|                      | BioPortal                | Doc2Hpo                        |
|                      | Centree Ontology Manager | PlanGexQ                       |
|                      | OLS                      | GOcats                         |
|                      | Ontobee                  | RDFScape                       |
|                      | PoolParty                | OntoBrowser                    |
|                      |                          | QuickGO                        |
|                      |                          | Circular Gene Ontology (CirGO) |
| Ontology engineering | eNanoMapper Slimmer      |                                |
|                      | OWLAPI                   |                                |
|                      | Protégé                  |                                |
|                      | ROBOT                    |                                |
|                      | TopBraid Composer        |                                |
|                      | VocBench                 |                                |

---
## Operations

### Ontology annotation

Ontoloy Annotation is the process of linking free text or data items to 'tokens' (defined terms from a lexicon) which provide semantic value. For example,  "type 2 diabetes" can be annotated with corresponding [term](http://purl.obolibrary.org/obo/MONDO_0005148) in the MONDO disease ontology. 

__Curated tools__

|Tool|Description|License|Topics|Resource Type|How to use|
|---|--|--|--|--|--|
|[ZOOMA](https://www.ebi.ac.uk/spot/zooma/)|A tool for mapping free text annotations to ontology term based on a curated repository of annotation knowledge.|[EMBL-EBI Terms of Use](https://www.ebi.ac.uk/about/terms-of-use/)|Ontology and terminology,<br>Systems biology,<br>Data identity and mapping|Web application,<br> API|[ZOOMA-Getting started](https://www.ebi.ac.uk/spot/zooma/docs/search)|
|[NCBI BioPortal Annotator](https://bioportal.bioontology.org/annotatorplus)|Get annotations for biomedical text with classes from the ontologies.|[BioPortal Terms of Use](https://www.bioontology.org/terms/)|Ontology and terminology,<br>Systems biology,<br>Data identity and mapping|Web application,<br> API|[BioPortal help](https://bioportal.bioontology.org/help?pop=true#Annotator_Tab)|
|[BioBert](https://github.com/dmis-lab/biobert)|A biomedical language representation model designed for biomedical text mining tasks such as biomedical named entity recognition, relation extraction, question answering.|[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)|text mining,<br> named-entity recognition,<br> natural language processing|Python|
|[Termite](https://www.scibite.com/platform/termite/)|Semantic enrichment to unlock the value of unstructured text and simplify the identification of new potential biomarker leads from scientific text.|Commercial license|Ontology and terminology|
|[PoolParty Semantic Suite](https://semantic-web.com/poolparty-semantic-suite/)|Automate the handling of heterogeneous metadata systems and the creation of enterprise knowledge graphs.design knowledge graphs at your own pace and with speed. Create your own ontologies and custom schemes by reusing already existing ontologies such as FOAF, FIBO, schema.org and CHEBI, among others. Apply them to your existing taxonomies with ease.|Commercial license|Content enrichment,<br>Data integration|
|[OntoMaton](https://github.com/ISA-tools/OntoMaton)| A tool facilitating ontology search and tagging functionalities within Google Spreadsheets.|[CPAL license](https://opensource.org/licenses/CPAL-1.0)||Google Add-ons|
|[Prodigy](https://prodi.gy/)|A modern annotation tool for creating training and evaluation data for machine learning models. You can also use Prodigy to help you inspect and clean your data, do error analysis and develop rule-based systems to use in combination with your statistical models.|Commercial license|Data annotation|Python, Web application,API|
|[OntoText](https://www.ontotext.com/products/ontotext-platform/)|Connect and publish complex enterprise knowledge with standard-compliant semantic graph database; Customize and apply analytics to link documents to graphs, extract new facts, classify and recommend content.|Commercial license|

__Related tools in [Bio.Tools](https://bio.tools)__

| Tool| Description| License | Topics | Resource Type |
|-------|--------|---------|----|--------|
| [bioBERT](https://bio.tools/BioBERT) | A pre-trained weights of BioBERT, a language representation model for biomedical domain, especially designed for biomedical text mining tasks such as biomedical named entity recognition, relation extraction, question answering, etc.|  N/A | Medicine, Ontology and terminology, Natural language processing  |Python|
|[PPR-SSM](https://bio.tools/PPR-SSM)| Personalized PageRank and semantic similarity measures for linking entities found in documents to concepts from domain-specific ontologies. |N/A| Imaging, Natural language processing, Data mining, Genotype and phenotype, Ontology and terminology        |Java, Python|
|[HPO2GO](https://bio.tools/HPO2GO)| Prediction of human phenotype ontology term associations using cross ontology annotation co-occurrences.Mapping between Human Phenotype Ontology (HPO) and Gene Ontology (GO) terms for the prediction of gene/protein - function - phenotype - disease associations.|[GPL-3.0](https://spdx.org/licenses/GPL-3.0)| Pathology, Protein interactions, Genotype and phenotype, Ontology and terminology, Gene expression| Command-line tool |
| [Vapur](https://bio.tools/vapur)| A Search Engine to Find Related Protein.Vapur is an online entity-oriented search engine for the COVID-19 anthology. Vapur is empowered with a semantic inverted index that is created through named entity recognition and relation extraction on CORD-19 abstracts. |N/A| Pathology, Ontology and terminology, Natural language processing, Enzymes |Python|
| [matscholar](https://bio.tools/matscholar)| A Python library for materials-focused natural language processing (NLP). Named Entity Recognition and Normalization Applied to Large-Scale Information Extraction from the Materials Science Literature.|[MIT](https://spdx.org/licenses/MIT)| Chemistry, Ontology and terminology, Natural language processing | Command-line tool |
|[CollaboNet](https://bio.tools/collabonet)| Collaboration of deep neural networks for biomedical named entity recognition.|[MIT](https://spdx.org/licenses/MIT)| Ontology and terminology, Natural language processing, Machine learning | Command-line tool |
| [Calchas](https://bio.tools/calchas)| A web based framework that takes advantage of domain specific ontologies, and Natural Language Processing, aiming to empower exploration of biomedical resources via semantic-based querying and search. The NLP engine analyzes the input free-text query and translates it into targeted queries with terms from the underlying ontology. | N/A | Medical informatics, Ontology and terminology, Natural language processing, Bioinformatics| Web application   |
|[QTL TableMiner++(QTM)](https://bio.tools/QTM) | It is a command-line tool to retrieve and semantically annotate results obtained from QTL mapping experiments. It takes full-text articles from the Europe PMC repository as input and outputs the extracted QTLs into a relational database (SQLite) and text file (CSV).|[Apache-2.0](https://spdx.org/licenses/Apache-2.0)| Ontology and terminology| Command-line tool |
| [thbp](https://bio.tools/thbp)| Mapping anatomical related entities to human body parts based on wikipedia in discharge summaries.|N/A| Anatomy, Ontology and terminology, Natural language processing||

### Ontology mapping

The process of determining correspondences between equivalent concepts in alternative ontologies, and other vocabularies. This may include mapping to convey different levels of granularity.

__Curated tools__

|Tool|Description|License|Topics|Resource Type|How to use|
|---|--|--|--|--|--|
|[OxO](https://www.ebi.ac.uk/spot/oxo/index)|A service for finding mappings (or cross-references) between terms from ontologies, vocabularies and coding standards. |[EMBL-EBI Terms of Use](https://www.ebi.ac.uk/about/terms-of-use/)|Ontology alignment| GUI and API| |

__Related tools in [Bio.Tools](https://bio.tools)__

| Tool| Description| License | Topics     | Type|
|-------|--|---------|----|---|
|[meshr](https://bio.tools/meshr)| A set of annotation maps describing the entire MeSH assembled using data from MeSH. |[Apache-2.0](https://spdx.org/licenses/Apache-2.0)| Medical informatics, Data quality management  | Command-line tool, Library |
| [locdb](https://bio.tools/locdb) | Manually curated database with experimental annotations for the subcellular localizations of proteins in Homo sapiens (HS, human) and Arabidopsis thaliana (AT, thale cress). | N/A | Ontology and terminology, Data submission, annotation and curation, Proteins | Database portal|


### Ontology management

The process of managing ontologies and other vocabularies in semantic web-linked data environments.This includes policies for update and maintenance of constituent and new terms.

__Curated tools__

|Tool|Description|License|Topics|Resource Type|How to use|
|---|--|--|--|--|--|
|[OLS](https://www.ebi.ac.uk/ols/index)|a repository for biomedical ontologies that aims to provide a single point of access to the latest ontology versions.|[EMBL-EBI Terms of Use](https://www.ebi.ac.uk/about/terms-of-use/)|Ontology and terminology|Web Application, API|
|[BioPortal](https://bioportal.bioontology.org/)|A repository of biomedical ontologies.|[BioPortal Terms of Use](https://www.bioontology.org/terms/)|Ontology and terminology|Web Application, API|
|[PoolParty](https://www.poolparty.biz/) |Knowledge Engineering & Knowledge Graph Management. Taxonomy, ontology and linked dataset management. |Commercial license|Ontology and terminology|
|[Centree Ontology Manager](https://www.scibite.com/platform/centree/)|A centralised, enterprise-ready resource for ontology management and transforms the experience of maintaining and releasing ontologies for research-led businesses.|Commercial license||Web application, API|
|[Ontobee](http://www.ontobee.org/)|A linked data server designed for ontologies. Ontobee is aimed to facilitate ontology data sharing, visualization, query, integration, and analysis.|[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)||Web application|
|[AberOWL](http://www.aber-owl.net/)|A framework for ontology-based access to biological data. It consists of a repository of bio-ontologies, a set of webservices which provide access to OWL(-EL) reasoning over the ontologies, and several frontends which utilise the ontology repository and reasoning services.|||Web application, API|


__Related tools in [Bio.Tools](https://bio.tools)__

| Tool| Description  | License | Topics | Type|
|---|--|--|--|--|
|[ngly1](https://bio.tools/ngly1)| A repository for the NGLY1 Deficiency Knowledge Graph, the reasoning context to support hypothesis discovery for NGLY1 Deficiency-CDDG (DOID:0060728) research. The user can navigate the knowledge in the graph in the Neo4j Browser website. | N/A  | Molecular interactions, pathways and networks, Ontology and terminology, Machine learning       | Command-line tool |
| [Doc2Hpo](https://bio.tools/doc2hpo) | Web application for efficient and accurate Human Phenotype Ontology (HPO) concept curation. |[Unlicense](https://spdx.org/licenses/Unlicense) | Genotype and phenotype, Ontology and terminology, Natural language processing| Web application |
| [PlanGexQ](https://bio.tools/PlanGexQ)| A user-friendly interactive tool for the curation and annotation of planarian morphologies and gene expression patterns in a centralized database.|N/A | Mathematics, Genotype and phenotype, Model organisms, Ontology and terminology, Gene expression |  |
|[GOcats](https://bio.tools/gocats)|Advances in gene ontology utilization improve statistical power of annotation enrichment.|N/A| Mapping, Ontology and terminology, Microarray experiment     | Command-line tool                      |
| [RDFScape](https://bio.tools/rdfscape) | This is a project that brings Semantic Web features to the popular Systems Biology software Cytoscape. It allows to query, visualize and reason on ontologies represented in OWL or RDF within Cytoscape.  |         | Systems biology, Ontology and terminology, Biology    | Desktop application                    |
| [OntoBrowser](https://bio.tools/ontobrowser)| The tool was developed to manage ontologies (and controlled terminologies e.g. CDISC SEND). The primary goal of the tool is to provide an online collaborative solution for expert curators to map code list terms (sourced from multiple systems/databases) to preferred ontology terms.|[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)| Ontology and terminology, Data identity and mapping      | Web API, Web application               |
|[QuickGO](https://bio.tools/quickgo)| A fast browser for Gene Ontology terms and annotations.    |         | Ontology and terminology      | Web application                        |
|[Circular Gene Ontology (CirGO)](https://bio.tools/cirgo)| Visualises non-redundant two-level hierarchically structured ontology terms from gene expression data in a 2D space.   |[GPL3.0](https://spdx.org/licenses/GPL-3.0) | Ontology and terminology, Data visualisation, Gene expression| Command-line tool, Desktop application |

### Ontology engineering

Ontology engineering is the process of developing and maintaining ontologies during the ontology life cycle.

__Curated tools__

|Tool|Description|License|Topics|Resource Type|
|---|--|--|--|--|
|[Protégé](https://protege.stanford.edu/) |A free, open source ontology editor and a knowledge management system.|[2-Clause BSD](https://opensource.org/licenses/BSD-2-Clause)||Web application, Desktop application|
|[ROBOT](http://robot.obolibrary.org/)|An open source library and command-line tool for automating ontology development tasks. ROBOT provides ontology processing commands for a variety of tasks, including commands for converting formats, running a reasoner, creating import modules, running reports, and various other tasks.|[BSD 3-Clause License](https://raw.githubusercontent.com/ontodev/robot/master/LICENSE.txt)||Command-line tool|
|[OWLAPI](http://owlcs.github.io/owlapi/)|A Java API and reference implmentation for creating, manipulating and serialising OWL Ontologies.|LGPL and Apache||API|
|[eNanoMapper Slimmer](https://github.com/enanomapper/slimmer)|A slim tool to slim ontologies as part of ontology integration. It allows users to provide configuration files that specify which parts of an ontology should be kept and/or removed, allowing to just select parts of the ontology you like.|[MIT license](https://opensource.org/licenses/MIT)||Java|
|[TopBraid Composer](https://www.topquadrant.com/products/topbraid-composer/)|TopBraid Composer Maestro Edition is used to develop ontology models, configure data source integration, and create semantic services and user interfaces.|[Commercial license](https://www.topquadrant.com/legal/)||
|[VocBench](http://vocbench.uniroma2.it/)|a web-based, multilingual, collaborative development platform for managing OWL ontologies, SKOS(/XL) thesauri, Ontolex-lemon lexicons and generic RDF datasets.|[License](https://bitbucket.org/art-uniroma2/vocbench3/src/master/LICENSE)||Desktop application|


## Implementation examples

To show how these tools can be used in real life examples, please check the related recipes.
- {ref}`fcb-selecting-ontologies`
- {ref}`fcb-interop-ontorobot`
<!-- - [Which vocabulary to use?](https://fairplus.github.io/the-fair-cookbook/content/recipes/interoperability/selecting-ontologies.html)
- [Building an application ontology with Robot](https://fairplus.github.io/the-fair-cookbook/content/recipes/interoperability/ontology-robot-recipe.html) -->

---

## Authors

````{authors_fairplus}
Fuqi: Writing - Original Draft, Software
Eva: Writing - Original Draft, Software
Sukhi: Data curation, Software
Philippe: Writing - Review & Editing 
````


---

## License

````{license_fairplus}
CC-BY-4.0
````




