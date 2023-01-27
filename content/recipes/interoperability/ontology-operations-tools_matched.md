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

This recipe aims to provide `an overview of tools available` to perform a number of key operations using ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and relevant to FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) processes: from `ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) management` to using `ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) for annotation` or `performing ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping`.

It aims to serve as a starting point to identify tools for FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)ification tasks where ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and semantic frameworks are needed. 

```{admonition} disclaimer
It is not intended to provide a comprehensive list covering all possible tools.
```

>The lists of tools are generated either automatically by querying the [bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/) repository (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository), or through manual curation. In this last instance, the list produced reflects what is being used in the industry and is influenced by the FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)plus project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project) partners that have been surveyed for the purpose of this work.

```{warning} 
The content in these tables was generated in March 2021.
For an updated contents, please check the [FAIR tooling repository](https://github.com/FAIRplus/WP3_FAIR_tooling).
```


## Requirements

* recipe dependency:
   * {ref}`fcb-selecting-ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)`
* knowledge requirement:
   * be fam(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#fam)iliar with ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and semantic annotation.

---

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and terminology](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/topic_0089)  | 
| [text annotation](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/operation_3778)  |

---
## Overview

The figure below shows different ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)-related operations and their relationships, together with related tools and recipes.


````{dropdown} 
:open: 
```{figure} ontology-operations-mermaid.png
---
width: 700px
name: Overview of key aspects in ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) associated processes
alt: Overview of key aspects in ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) associated processes
---
Overview of key aspects in ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) associated processes
```
````

The table below is an overview of ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) strategies tools identified. Details of each tools are provided below.

|         Topic        |       Curated tools      |   Related tools in Bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)   |
|:--------------------:|:------------------------:|:------------------------------:|
| Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) annotation  | ZOOMA(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/gxd/ma_ontology/)(URL_TO_INSERT_RECORD http://omabrowser.org/oma/about/)                    | bioBERT                        |
|                      | NCBI BioPortal(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/) Annotator | PP(URL_TO_INSERT_RECORD https://bitbucket.org/PlantExpAssay/ontology)R-SSM                        |
|                      | BioBert                  | HP(URL_TO_INSERT_RECORD https://hpo.jax.org/)O(URL_TO_INSERT_RECORD http://plantontology.org/)2(URL_TO_INSERT_RECORD http://dx.doi.org/10.15454/1.4702114192525708E12)GO(URL_TO_INSERT_RECORD http://www.geneontology.org)                         |
|                      | Termite                  | Vapur                          |
|                      | PoolParty Semantic Suite | matscholar                     |
|                      | OntoMaton                | CollaboNet                     |
|                      | Prodigy                  | Calchas                        |
|                      | OntoText                 | QTL TableMiner++(QTM)          |
|                      |                          | thbp                           |
| Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping     | OxO(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/spot/oxo/)                      | meshr                          |
|                      |                          | locdb                          |
| Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) management  | AberOWL(URL_TO_INSERT_RECORD http://www.w3.org/TR/owl-overview/)                  | ngly1                          |
|                      | BioPortal(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)                | Doc2Hpo                        |
|                      | Centree Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) Manager | PlanGexQ                       |
|                      | OLS(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/ols/index)                      | GO(URL_TO_INSERT_RECORD http://www.geneontology.org)cats                         |
|                      | Ontobee(URL_TO_INSERT_RECORD http://www.ontobee.org/)(URL_TO_INSERT_RECORD http://www.ontobee.org/)                  | RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/)S(URL_TO_INSERT_RECORD https://www.w3.org/TR/rdf-schema/)cape                       |
|                      | PoolParty                | OntoBrowser                    |
|                      |                          | QuickGO(URL_TO_INSERT_RECORD http://www.geneontology.org)                        |
|                      |                          | Circular Gene Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD http://www.geneontology.org) (CirGO(URL_TO_INSERT_RECORD http://www.geneontology.org)) |
| Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) engineering | eNanoMap(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)per Slimmer      |                                |
|                      | OWL(URL_TO_INSERT_RECORD http://www.w3.org/TR/owl-overview/)API                   |                                |
|                      | Protégé                  |                                |
|                      | RO(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD https://w3id.org/ro/)BO(URL_TO_INSERT_RECORD http://www.obofoundry.org/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059)T                    |                                |
|                      | TopBraid Composer        |                                |
|                      | VocBench                 |                                |

---
## Operations

### Ontology annotation

Ontoloy Annotation is the process of linking free text or data items to 'tokens' (defined terms from a lexicon) which provide semantic value. For example,  "type 2 diabetes" can be annotated with corresponding [term](http://purl.obolibrary.org/obo/MONDO_0005148) in the MO(URL_TO_INSERT_RECORD http://mged.sourceforge.net/ontologies/MGEDontology.php)NDO(URL_TO_INSERT_RECORD https://github.com/monarch-initiative/monarch-disease-ontology) disease ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD http://www.disease-ontology.org). 

__Curated tools__

|Tool|Description|License|Topics|Resource Type|How to use|
|---|--|--|--|--|--|
|[ZOOMA](https://www.ebi.ac.uk/spot/zooma/)|A tool for map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping free text annotations to ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) term based on a curated repository (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository) of annotation knowledge.|[EMB(URL_TO_INSERT_RECORD http://www.Metabase.net)L-EBI Terms of Use](https://www.ebi.ac.uk/about/terms-of-use/)|Ontology and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact),<br>Systems biology,<br>Data identity and map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping|Web application,<br> API|[ZOOMA(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/gxd/ma_ontology/)(URL_TO_INSERT_RECORD http://omabrowser.org/oma/about/)-Getting started](https://www.ebi.ac.uk/spot/zooma/docs/search)|
|[NCBI BioPortal(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/) Annotator](https://bioportal.bioontology.org(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)/annotatorplus)|Get annotations for biomedical text with classes from the ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact).|[BioPortal(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/) Terms of Use](https://www.bioontology.org/terms/)|Ontology and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact),<br>Systems biology,<br>Data identity and map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping|Web application,<br> API|[BioPortal(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/) help](https://bioportal.bioontology.org(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)/help?pop=true#Annotator_Tab)|
|[BioBert](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/dmis-lab/biobert)|A biomedical language representation model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) designed for biomedical text mining tasks such as biomedical named entity recognition, relation extraction, question answering.|[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)|text mining,<br> named-entity recognition,<br> natural language processing|Python|
|[Termite](https://www.scibite.com/platform/termite/)|Semantic enrichment to unlock the value of unstructured text and simplify the identification of new potential biomarker leads from scientific text.|Commercial license|Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)|
|[PoolParty Semantic Suite](https://semantic-web.com/poolparty-semantic-suite/)|Automate the handling of heterogeneous metadata systems and the creation of enterprise knowledge graphs.design knowledge graphs at your own pace and with speed. Create your own ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and custom schemes by reusing already existing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) such as FO(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO)AF, FIBO(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059), schema.org(URL_TO_INSERT_RECORD http://schema.org/) and CHEBI, among others. Apply them to your existing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) taxonomies with ease.|Commercial license|Content enrichment,<br>Data integration|
|[OntoMaton](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/ISA-tools/OntoMaton)| A tool facilitating ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) and tagging functionalities within Google Spreadsheets.|[CP(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/complexportal/)AL license](https://opensource.org/licenses/CPAL-1.0)||Google Add-ons|
|[Prodigy](https://prodi.gy/)|A modern annotation tool for creating training and evaluation data for machine learning model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s. You can also use Prodigy to help you inspect and clean your data, do error analysis and develop rule-based systems to use in combination with your statistical model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s.|Commercial license|Data annotation|Python, Web application,API|
|[OntoText](https://www.ontotext.com/products/ontotext-platform/)|Connect and publish complex enterprise knowledge with standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)-compliant semantic graph database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database); Customize and apply analytics to link documents to graphs, extract new facts, classify and recommend content.|Commercial license|

__Related tools in [Bio.Tools(URL_TO_INSERT_RECORD https://bio.tools/)](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/))__

| Tool| Description| License | Topics | Resource Type |
|-------|--------|---------|----|--------|
| [bioBERT](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/BioBERT) | A pre-trained weights of BioBERT, a language representation model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) for biomedical domain, especially designed for biomedical text mining tasks such as biomedical named entity recognition, relation extraction, question answering, etc.|  N/A | Medicine, Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), Natural language processing  |Python|
|[PPR-SSM](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/PPR-SSM)| Personalized PageRank and semantic similarity measures for linking entities found in documents to concepts from domain-specific ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact). |N/A| Imaging, Natural language processing, Data mining, Genotype and phenotype, Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)        |Java, Python|
|[HPO2GO](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/HPO2GO)| Prediction of human phenotype ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD https://hpo.jax.org/) term associations using cross ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) annotation co-occurrences.Map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping between Human Phenotype Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD https://hpo.jax.org/) (HP(URL_TO_INSERT_RECORD https://hpo.jax.org/)O(URL_TO_INSERT_RECORD http://plantontology.org/)) and Gene Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD http://www.geneontology.org) (GO(URL_TO_INSERT_RECORD http://www.geneontology.org)) terms for the prediction of gene/protein - function - phenotype - disease associations.|[GPL-3.0](https://spdx.org/licenses/GPL-3.0)| Pathology, Protein(URL_TO_INSERT_RECORD http://www.ncbi.nlm.nih.gov/protein) interactions, Genotype and phenotype, Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), Gene expression| Command-line tool |
| [Vapur](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/vapur)| A Search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) Engine to Find Related Protein(URL_TO_INSERT_RECORD http://www.ncbi.nlm.nih.gov/protein).Vapur is an online entity-oriented search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) engine for the CO(URL_TO_INSERT_RECORD http://www.cropontology.org/)(URL_TO_INSERT_RECORD https://codeocean.com)VID-19 anthology. Vapur is empowered with a semantic inverted index that is created through named entity recognition and relation extraction on CO(URL_TO_INSERT_RECORD http://www.cropontology.org/)(URL_TO_INSERT_RECORD https://codeocean.com)RD-19 abstracts. |N/A| Pathology, Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), Natural language processing, Enzymes |Python|
| [matscholar](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/matscholar)| A Python library for materials-focused natural language processing (NLP). Named Entity Recognition and Normalization Applied to Large-Scale Informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion Extraction from the Materials Science Literature.|[MIT](https://spdx.org/licenses/MIT)| Chemistry(URL_TO_INSERT_RECORD https://www.go-fair.org/implementation-networks/overview/chemistryin/)(URL_TO_INSERT_RECORD https://www.go-fair.org/implementation-networks/overview/chemistryin/), Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), Natural language processing | Command-line tool |
|[CollaboNet](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/collabonet)| Collaboration of deep neural networks for biomedical named entity recognition.|[MIT](https://spdx.org/licenses/MIT)| Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), Natural language processing, Machine learning | Command-line tool |
| [Calchas](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/calchas)| A web based framework that takes advantage of domain specific ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), and Natural Language Processing, aiming to empower exploration of biomedical resources via semantic-based querying and search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/). The NLP engine analyzes the input free-text query and translates it into targeted queries with terms from the underlying ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact). | N/A | Medical informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ics, Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), Natural language processing, Bioinformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ics| Web application   |
|[QTL TableMiner++(QTM)](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/QTM) | It is a command-line tool to retrieve and semantically annotate results obtained from QTL map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping experiments. It takes full-text articles from the Europe PMC(URL_TO_INSERT_RECORD https://europepmc.org)(URL_TO_INSERT_RECORD http://www.ncbi.nlm.nih.gov/pmc/) repository (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository) as input and outputs the extracted QTLs into a relational database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database) (SQLite) and text file (CSV).|[Apache-2.0](https://spdx.org/licenses/Apache-2.0)| Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)| Command-line tool |
| [thbp](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/thbp)| Map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping anatomical related entities to human body parts based on wikiped(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped)ia in discharge summaries.|N/A| Anatomy, Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), Natural language processing||

### Ontology mapping

The process of determining correspondences between equivalent concepts in alternative ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), and other vocabularies. This may include map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping to convey different levels of granularity.

__Curated tools__

|Tool|Description|License|Topics|Resource Type|How to use|
|---|--|--|--|--|--|
|[OxO](https://www.ebi.ac.uk/spot/oxo(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/spot/oxo/)/index)|A service for finding map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)pings (or cross-references) between terms from ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), vocabularies and coding standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s. |[EMB(URL_TO_INSERT_RECORD http://www.Metabase.net)L-EBI Terms of Use](https://www.ebi.ac.uk/about/terms-of-use/)|Ontology alignment| GUI and API| |

__Related tools in [Bio.Tools(URL_TO_INSERT_RECORD https://bio.tools/)](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/))__

| Tool| Description| License | Topics     | Type|
|-------|--|---------|----|---|
|[meshr](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/meshr)| A set of annotation map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)s describing the entire MeSH assembled using data from MeSH. |[Apache-2.0](https://spdx.org/licenses/Apache-2.0)| Medical informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ics, Data quality management  | Command-line tool, Library |
| [locdb](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/locdb) | Manually curated database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database) with experimental annotations for the subcellular localizations of proteins in Homo sapiens (HS, human) and Arabidopsis thaliana (AT, thale cress). | N/A | Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), Data submission, annotation and curation, Protein(URL_TO_INSERT_RECORD http://www.ncbi.nlm.nih.gov/protein)s | Database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database) portal|


### Ontology management

The process of managing ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and other vocabularies in semantic web-linked data environments.This includes policies (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Policy) for update and maintenance of constituent and new terms.

__Curated tools__

|Tool|Description|License|Topics|Resource Type|How to use|
|---|--|--|--|--|--|
|[OLS](https://www.ebi.ac.uk/ols/index(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/ols/index))|a repository (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository) for biomedical ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) that aims to provide a single point of access to the latest ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) versions.|[EMB(URL_TO_INSERT_RECORD http://www.Metabase.net)L-EBI Terms of Use](https://www.ebi.ac.uk/about/terms-of-use/)|Ontology and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)|Web Application, API|
|[BioPortal](https://bioportal.bioontology.org(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)/)|A repository (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository) of biomedical ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact).|[BioPortal(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/) Terms of Use](https://www.bioontology.org/terms/)|Ontology and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)|Web Application, API|
|[PoolParty](https://www.poolparty.biz/) |Knowledge Engineering & Knowledge Graph Management. Taxonomy, ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and linked dataset management. |Commercial license|Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)|
|[Centree Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) Manager](https://www.scibite.com/platform/centree/)|A centralised, enterprise-ready resource for ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) management and transforms the experience of maintaining and releasing ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) for research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)-led businesses.|Commercial license||Web application, API|
|[Ontobee](http://www.ontobee.org(URL_TO_INSERT_RECORD http://www.ontobee.org/)/)|A linked data server designed for ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact). Ontobee(URL_TO_INSERT_RECORD http://www.ontobee.org/)(URL_TO_INSERT_RECORD http://www.ontobee.org/) is aimed to facilitate ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) data sharing, visualization, query, integration, and analysis.|[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)||Web application|
|[AberOWL](http://www.aber-owl.net/)|A framework for ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)-based access to biological data. It consists of a repository (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository) of bio-ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), a set of webservices which provide access to OWL(URL_TO_INSERT_RECORD http://www.w3.org/TR/owl-overview/)(-EL) reasoning over the ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), and several frontends which utilise the ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) repository (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository) and reasoning services.|||Web application, API|


__Related tools in [Bio.Tools(URL_TO_INSERT_RECORD https://bio.tools/)](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/))__

| Tool| Description  | License | Topics | Type|
|---|--|--|--|--|
|[ngly1](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/ngly1)| A repository (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository) for the NGLY1 Deficiency Knowledge Graph, the reasoning context to support hypothesis discovery for NGLY1 Deficiency-CDD(URL_TO_INSERT_RECORD https://www.ncbi.nlm.nih.gov/Structure/cdd/cdd.shtml)(URL_TO_INSERT_RECORD https://www.publicsafety.gc.ca/cnt/rsrcs/cndn-dsstr-dtbs/index-en.aspx)G (DOI(URL_TO_INSERT_RECORD https://www.doi.org)D(URL_TO_INSERT_RECORD http://www.disease-ontology.org):0060728) research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/). The user can navigate the knowledge in the graph in the Neo4j Browser website. | N/A  | Molecular interactions, pathways and networks, Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), Machine learning       | Command-line tool |
| [Doc2Hpo](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/doc2hpo) | Web application for efficient and accurate Human Phenotype Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD https://hpo.jax.org/) (HP(URL_TO_INSERT_RECORD https://hpo.jax.org/)O(URL_TO_INSERT_RECORD http://plantontology.org/)) concept curation. |[Unlicense](https://spdx.org/licenses/Unlicense) | Genotype and phenotype, Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), Natural language processing| Web application |
| [PlanGexQ](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/PlanGexQ)| A user-friendly interactive tool for the curation and annotation of planarian morphologies and gene expression patterns in a centralized database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database).|N/A | Mathematics, Genotype and phenotype, Model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) organisms, Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), Gene expression |  |
|[GOcats](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/gocats)|Advances in gene ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD http://www.geneontology.org) utilization improve statistical power of annotation enrichment.|N/A| Map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping, Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), Microarray experiment     | Command-line tool                      |
| [RDFScape](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/rdfscape) | This is a project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project) that brings Semantic Web features to the popular Systems Biology software Cytoscape. It allows to query, visualize and reason on ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) represented in OWL(URL_TO_INSERT_RECORD http://www.w3.org/TR/owl-overview/) or RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) within Cytoscape.  |         | Systems biology, Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), Biology    | Desktop application                    |
| [OntoBrowser](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/ontobrowser)| The tool was developed(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) to manage ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) (and controlled terminologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) e.g. CDI(URL_TO_INSERT_RECORD https://www.seadatanet.org/Metadata/CDI-Common-Data-Index)SC(URL_TO_INSERT_RECORD https://www.cdisc.org/)(URL_TO_INSERT_RECORD https://www.cdisc.org/) SEND(URL_TO_INSERT_RECORD https://www.cdisc.org/standards/foundational/send)). The primary goal of the tool is to provide an online collaborative solution for expert curators to map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map) code list terms (sourced from multiple systems/database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)s) to preferred ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) terms.|[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)| Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), Data identity and map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping      | Web API, Web application               |
|[QuickGO](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/quickgo)| A fast browser for Gene Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD http://www.geneontology.org) terms and annotations.    |         | Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)      | Web application                        |
|[Circular Gene Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD http://www.geneontology.org) (CirGO)](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/cirgo)| Visualises non-redundant two-level hierarch(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ically structured ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) terms from gene expression data in a 2D space.   |[GPL3.0](https://spdx.org/licenses/GPL-3.0) | Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), Data visualisation, Gene expression| Command-line tool, Desktop application |

### Ontology engineering

Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) engineering is the process of developing and maintaining ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) during the ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) life cycle.

__Curated tools__

|Tool|Description|License|Topics|Resource Type|
|---|--|--|--|--|
|[Protégé](https://protege.stanford.edu/) |A free, open source ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) editor and a knowledge management system.|[2-Clause BSD](https://opensource.org/licenses/BSD-2-Clause)||Web application, Desktop application|
|[ROBOT](http://robot.obolibrary.org/)|An open source library and command-line tool for automating ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) development tasks. RO(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD https://w3id.org/ro/)BO(URL_TO_INSERT_RECORD http://www.obofoundry.org/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059)T provides ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) processing commands for a variety of tasks, including commands for converting format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s, running a reasoner, creating import modules, running reports, and various other tasks.|[BSD 3-Clause License](https://raw.githubusercontent.com/ontodev/robot/master/LICENSE.txt)||Command-line tool|
|[OWLAPI](http://owlcs.github.io/owlapi/)|A Java API and reference implmentation for creating, manipulating and serialising OWL(URL_TO_INSERT_RECORD http://www.w3.org/TR/owl-overview/) Ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact).|LGPL and Apache||API|
|[eNanoMap(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)per Slimmer](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/enanomapper/slimmer)|A slim tool to slim ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) as part of ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) integration. It allows users to provide configuration files that specify which parts of an ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) should be kept and/or removed, allowing to just select parts of the ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) you like.|[MIT license](https://opensource.org/licenses/MIT)||Java|
|[TopBraid Composer](https://www.topquadrant.com/products/topbraid-composer/)|TopBraid Composer Maestro Edition is used to develop ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s, configure data source integration, and create semantic services and user interfaces.|[Commercial license](https://www.topquadrant.com/legal/)||
|[VocBench](http://vocbench.uniroma2.it/)|a web-based, multilingual, collaborative development platform for managing OWL(URL_TO_INSERT_RECORD http://www.w3.org/TR/owl-overview/) ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), SKOS(URL_TO_INSERT_RECORD http://www.w3.org/TR/skos-reference)(/XL) thesauri, Ontolex-lemon lexicons and generic RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) datasets.|[License](https://bitbucket.org(URL_TO_INSERT_RECORD https://bitbucket.org/)/art-uniroma2/vocbench3/src/master/LICENSE)||Desktop application|


## Implementation examples

To show how these tools can be used in real life examples, please check the related recipes.
- {ref}`fcb-selecting-ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)`
- {ref}`fcb-interop-ontorobot`
<!-- - [Which vocabulary to use?](https://fairplus.github.io/the-fair-cookbook/content/recipes/interoperability/selecting-ontologies.html)
- [Building an application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) with Robot](https://fairplus.github.io/the-fair-cookbook/content/recipes/interoperability/ontology-robot-recipe.html) -->


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




