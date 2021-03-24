# Tools for ontology strategies

## Main objectives
This recipe identifies tools for different operations regarding ontology strategies, such as ontology annotation, ontology mapping, ontology management, etc. It aims to serve as a start point for implementing ontology-related FAIRifications, instead of provide a comprehensive list covering all available tools.

>The lists of tools  are generated either by manual curation, which reflects what is being used in the industry, or automatally discovered from the [bio.tools](https://bio.tools/) repository. 
>
>:bulb: _Contents in this table are generated in March 2021. 
>For updated contents, please check the [FAIR tooling repository]()._ You can provide feedback or report issues in the `comments` section.


## Overview

The figure below shows different ontology-related operations and their relationships, together with related tools and recipes.

```mermaid
graph TB
    subgraph Ontology strategies<br>
    
        subgraph Metadata enrichment
            A[Ontology recommendation]
            B[Ontology annotation]
            C[Ontology mapping]
        end
        
        subgraph Ontology life cycle
            D[Ontology engineering]
            E[Ontology management]
        end
        
        A-->B
        B-->C
        
        E-.-A
        E-.-C
        
        
    end
    
    classDef className fill:#f9f,stroke:#333,stroke-width:2px

```
The table below is an overview of ontology strategies tools identified. Details of each tools are provided below.

<table>
  <tr>
   <td>Topic
   </td>
   <td><a href="https://hackmd.io/d_8tCiFYQkSl6tT7NP-1_Q#Ontology-annotation">Ontology annotation</a>
   </td>
   <td><a href="https://hackmd.io/d_8tCiFYQkSl6tT7NP-1_Q#Ontology-mapping">Ontology mapping</a>
   </td>
   <td><a href="https://hackmd.io/d_8tCiFYQkSl6tT7NP-1_Q#Ontology-management">Ontology management</a>
   </td>
   <td><a href="https://hackmd.io/d_8tCiFYQkSl6tT7NP-1_Q#Ontology-engineering">Ontology engineering</a>
   </td>
  </tr>
  <tr>
   <td rowspan="8" >Manual selected tools
   </td>
   <td><a href="https://github.com/dmis-lab/biobert">BioBert</a>
   </td>
   <td><a href="https://www.ebi.ac.uk/spot/oxo/index">OxO</a>
   </td>
   <td><a href="http://www.aber-owl.net/">AberOWL</a>
   </td>
   <td><a href="https://github.com/enanomapper/slimmer">eNanoMapper Slimmer</a>
   </td>
  </tr>
  <tr>
   <td><a href="https://bioportal.bioontology.org/annotatorplus">NCBI BioPortal Annotator</a>
   </td>
   <td>
   </td>
   <td><a href="https://bioportal.bioontology.org/">BioPortal</a>
   </td>
   <td><a href="http://owlcs.github.io/owlapi/">OWLAPI</a>
   </td>
  </tr>
  <tr>
   <td><a href="https://github.com/ISA-tools/OntoMaton">OntoMaton</a>
   </td>
   <td>
   </td>
   <td><a href="https://www.scibite.com/platform/centree/">Centree Ontology Manager</a>
   </td>
   <td><a href="https://protege.stanford.edu/">Protégé</a>
   </td>
  </tr>
  <tr>
   <td><a href="https://www.ontotext.com/products/ontotext-platform/">OntoText</a>
   </td>
   <td>
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/index">OLS</a>
   </td>
   <td><a href="http://robot.obolibrary.org/">ROBOT</a>
   </td>
  </tr>
  <tr>
   <td><a href="https://semantic-web.com/poolparty-semantic-suite/">PoolParty Semantic Suite</a>
   </td>
   <td>
   </td>
   <td><a href="http://www.ontobee.org/">Ontobee</a>
   </td>
   <td><a href="https://www.topquadrant.com/products/topbraid-composer/">TopBraid Composer</a>
   </td>
  </tr>
  <tr>
   <td><a href="https://prodi.gy/">Prodigy</a>
   </td>
   <td>
   </td>
   <td><a href="https://www.poolparty.biz/">PoolParty</a>
   </td>
   <td><a href="http://vocbench.uniroma2.it/">VocBench</a>
   </td>
  </tr>
  <tr>
   <td><a href="https://www.scibite.com/platform/termite/">Termite</a>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://www.ebi.ac.uk/spot/zooma/">ZOOMA</a>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td rowspan="11" >Tools found in Bio.toools
   </td>
   <td><a href="https://bio.tools/biobert">biobert</a>
   </td>
   <td><a href="https://bio.tools/meshr">meshr</a>
   </td>
   <td><a href="https://bio.tools/ngly1">ngly1</a>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/ppr-ssm">ppr-ssm</a>
   </td>
   <td><a href="https://bio.tools/locdb">locdb</a>
   </td>
   <td><a href="https://bio.tools/doc2hpo">doc2hpo</a>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/hpo2go">hpo2go</a>
   </td>
   <td><a href="https://bio.tools/zooma">zooma</a>
   </td>
   <td><a href="https://bio.tools/amigo%202">amigo 2</a>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/vapur">vapur</a>
   </td>
   <td>
   </td>
   <td><a href="https://bio.tools/plangexq">plangexq</a>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/belief">belief</a>
   </td>
   <td>
   </td>
   <td><a href="https://bio.tools/gocats">gocats</a>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/matscholar">matscholar</a>
   </td>
   <td>
   </td>
   <td><a href="https://bio.tools/rdfscape">rdfscape</a>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/collabonet">collabonet</a>
   </td>
   <td>
   </td>
   <td><a href="https://bio.tools/ontobrowser">ontobrowser</a>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/calchas">calchas</a>
   </td>
   <td>
   </td>
   <td><a href="https://bio.tools/quickgo">quickgo</a>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/qtl%20tableminer%EF%BF%BD(qtm)">qtl tableminer(qtm)</a>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/thbp">thbp</a>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
</table>

## Operations

<h3 id="Ontology-annotationr">Ontology annotation</h3>

The process of linking free text or data items to 'tokens'(defined terms from a lexicon) which provide semantic value. For example, free text "type 2 diabetes" can be be annotated with [terms](http://purl.obolibrary.org/obo/MONDO_0005148) in the MONDO disease ontology. 

__Manually curated tools__ 
|Tool|Description|License|Topics|Resource Type|
|---|--|--|--|--|
|[ZOOMA](https://www.ebi.ac.uk/spot/zooma/)|A tool for mapping free text annotations to ontology term based on a curated repository of annotation knowledge|[EMBL-EBI Terms of Use](https://www.ebi.ac.uk/about/terms-of-use/)|Ontology and terminology,<br>Systems biology,<br>Data identity and mapping|Web application,<br> API|
|[NCBI BioPortal Annotator](https://bioportal.bioontology.org/annotatorplus)|Get annotations for biomedical text with classes from the ontologies.|[NioPortal Terms of Use](https://www.ebi.ac.uk/about/terms-of-use/)|Ontology and terminology,<br>Systems biology,<br>Data identity and mapping|Web application,<br> API|
|[BioBert](https://github.com/dmis-lab/biobert)|A biomedical language representation model designed for biomedical text mining tasks such as biomedical named entity recognition, relation extraction, question answering.|[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)|text mining,<br> named-entity recognition,<br> natural language processing|Python|
|[Termite](https://www.scibite.com/platform/termite/)|Semantic enrichment to unlock the value of unstructured text and simplify the identification of new potential biomarker leads from scientific text.|Commercial license|Ontology and terminology|
|[PoolParty Semantic Suite](https://semantic-web.com/poolparty-semantic-suite/)|Automate the handling of heterogeneous metadata systems and the creation of enterprise knowledge graphs.design knowledge graphs at your own pace and with speed. Create your own ontologies and custom schemes by reusing already existing ontologies such as FOAF, FIBO, schema.org and CHEBI, among others. Apply them to your existing taxonomies with ease.|Commercial license|Content enrichment,<br>Data integration|
|[OntoMaton](https://github.com/ISA-tools/OntoMaton)| A tool facilitating ontology search and tagging functionalities within Google Spreadsheets.|[CPAL license](https://opensource.org/licenses/CPAL-1.0)||Google Add-ons|
|[Prodigy](https://prodi.gy/)|A modern annotation tool for creating training and evaluation data for machine learning models. You can also use Prodigy to help you inspect and clean your data, do error analysis and develop rule-based systems to use in combination with your statistical models.|Commercial license|Data annotation|Python, Web application,API|
|[OntoText](https://www.ontotext.com/products/ontotext-platform/)|Connect and publish complex enterprise knowledge with standard-compliant semantic graph database;Customize and apply analytics to link documents to graphs, extract new facts, classify and recommend content...|Commercial license|

__Tools discovered from [Bio.Tools](https://bio.tools).__

<table>
  <tr>
   <td>Tool
   </td>
   <td>Description
   </td>
   <td>License
   </td>
   <td>Topics
   </td>
   <td>Resource Type
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/biobert">biobert</a>
   </td>
   <td>A pre-trained biomedical language representation model for biomedical text mining | BioBERT: a pre-trained biomedical language representation model | This repository provides pre-trained weights of BioBERT, a language representation model for biomedical domain, especially designed for biomedical text mining tasks such as biomedical named entity recognition, relation extraction, question answering, etc. Please refer to our paper BioBERT: a pre-trained biomedical language representation model for biomedical text mining for more details | This repository provides fine-tuning codes of BioBERT, a language representation model for biomedical domain, especially designed for biomedical text mining tasks such as biomedical named entity recognition, relation extraction, question answering, etc. Please refer to our paper BioBERT: a pre-trained biomedical language representation model for biomedical text mining for more details. This project is done by DMIS-Lab
   </td>
   <td>
   </td>
   <td>Medicine, Ontology and terminology, Natural language processing
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/ppr-ssm">ppr-ssm</a>
   </td>
   <td>personalized PageRank and semantic similarity measures for entity linking.
<p>
BACKGROUND:Biomedical literature concerns a wide range of concepts, requiring controlled vocabularies to maintain a consistent terminology across different research groups. However, as new concepts are introduced, biomedical literature is prone to ambiguity, specifically in fields that are advancing more rapidly, for example, drug design and development. Entity linking is a text mining task that aims at linking entities mentioned in the literature to concepts in a knowledge base. For example, entity linking can help finding all documents that mention the same concept and improve relation extraction methods. Existing approaches focus on the local similarity of each entity and the global coherence of all entities in a document, but do not take into account the semantics of the domain. RESULTS:We propose a method, PPR-SSM, to link entities found in documents to concepts from domain-specific ontologies
   </td>
   <td>
   </td>
   <td>Imaging, Natural language processing, Data mining, Genotype and phenotype, Ontology and terminology
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/hpo2go">hpo2go</a>
   </td>
   <td>Prediction of human phenotype ontology term associations using cross ontology annotation co-occurrences.
<p>
Mapping between HPO and GO terms.
<p>
If you find HPO2GO useful, please consider citing this publication:.
<p>
Mapping between Human Phenotype Ontology (HPO) and Gene Ontology (GO) terms for the prediction of gene/protein - function - phenotype - disease associations.
<p>
In this study, a novel approach is proposed for the identification of relationships between biomedical entities by automatically mapping phenotypic abnormality defining HPO terms with biomolecular function defining GO terms, where each association indicates the occurrence of the abnormality due to the loss of the biomolecular function expressed by the corresponding GO term
   </td>
   <td>
   </td>
   <td>Pathology, Protein interactions, Genotype and phenotype, Ontology and terminology, Gene expression
   </td>
   <td>Command-line tool
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/vapur">vapur</a>
   </td>
   <td>A Search Engine to Find Related Protein.
<p>
Vapur is an online entity-oriented search engine for the COVID-19 anthology. Vapur is empowered with a semantic inverted index that is created through named entity recognition and relation extraction on CORD-19 abstracts.
<p>
In order to run scripts from scratch, please follow these:.
<p>
Enter a chemical or protein/gene and let Vapur find related bio-molecules in 150,000 COVID-19 publications!.
   </td>
   <td>
   </td>
   <td>Pathology, Ontology and terminology, Natural language processing, Enzymes
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/belief">belief</a>
   </td>
   <td>BELIEF (Biological Expression Language Information Extraction WorkFlow) is a semi-automated workflow for BEL network creation. It embeds an information extraction workflow with state-of-the-art named entity recognition (NER) and relation extraction (RE) methods.
   </td>
   <td>
   </td>
   <td>Natural language processing, Machine learning, Workflows, Genotype and phenotype, Ontology and terminology
   </td>
   <td>Web application
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/matscholar">matscholar</a>
   </td>
   <td>Named Entity Recognition and Normalization Applied to Large-Scale Information Extraction from the Materials Science Literature | Public API for the Materials Scholar database | matscholar (Materials Scholar) is a Python library for materials-focused natural language processing (NLP). It is maintained by a team of researchers at UC Berkeley and Lawrence Berkeley National Laboratory as part of a project funded by the Toyota Research Institute
   </td>
   <td>
   </td>
   <td>Chemistry, Ontology and terminology, Natural language processing
   </td>
   <td>Command-line tool
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/collabonet">collabonet</a>
   </td>
   <td>Collaboration of deep neural networks for biomedical named entity recognition.
   </td>
   <td>
   </td>
   <td>Ontology and terminology, Natural language processing, Machine learning
   </td>
   <td>Command-line tool
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/calchas">calchas</a>
   </td>
   <td>A web based framework that takes advantage of domain specific ontologies, and Natural Language Processing, aiming to empower exploration of biomedical resources via semantic-based querying and search. The NLP engine analyzes the input free-text query and translates it into targeted queries with terms from the underlying ontology. Each query is passed to the semantically-annotated tools repository, and based on similarity matches, it ranks the available resources.
   </td>
   <td>
   </td>
   <td>Medical informatics, Ontology and terminology, Natural language processing, Bioinformatics
   </td>
   <td>Web application
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/qtl%20tableminer%EF%BF%BD(qtm)">qtl tableminer(qtm)</a>
   </td>
   <td>It is a command-line tool to retrieve and semantically annotate results obtained from QTL mapping experiments. It takes full-text articles from the Europe PMC repository as input and outputs the extracted QTLs into a relational database (SQLite) and text file (CSV).
   </td>
   <td>
   </td>
   <td>Ontology and terminology
   </td>
   <td>Command-line tool
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/thbp">thbp</a>
   </td>
   <td>Mapping anatomical related entities to human body parts based on wikipedia in discharge summaries | *: Background Consisting of dictated free-text documents such as discharge summaries, medical narratives are widely used in medical natural language processing. Relationships between anatomical entities and human body parts are crucial for building medical text mining applications. To achieve this, we establish a mapping system consisting of a Wikipedia-based scoring algorithm and a named entity normalization method (NEN). The mapping system makes full use of information available on Wikipedia, which is a comprehensive Internet medical knowledge base
   </td>
   <td>
   </td>
   <td>Anatomy, Ontology and terminology, Natural language processing
   </td>
   <td>
   </td>
  </tr>
</table>

<h3 id="Ontology mapping">Ontology mapping</h3>

The process of determining correspondences between equivalent concepts in alternative ontologies, and other vocabularies. This may include mapping to convey different levels of granularity.

__Manually curated tools__ 
|Tool|Description|License|Topics|Resource Type|
|---|--|--|--|--|
|[OxO](https://www.ebi.ac.uk/spot/oxo/index)|a service for finding mappings (or cross-references) between terms from ontologies, vocabularies and coding standards. OxO imports mappings from a variety of sources including the Ontology Lookup Service and a subset of mappings provided by the UMLS. We're still developing the service so please get in touch if you have any feedback.|[EMBL-EBI Terms of Use](https://www.ebi.ac.uk/about/terms-of-use/)|GUI and API|

__Tools discovered from [Bio.Tools](https://bio.tools).__
<table>
  <tr>
   <td>Tool
   </td>
   <td>Description
   </td>
   <td>License
   </td>
   <td>Topics
   </td>
   <td>Type
   </td>
  </tr>
  <tr>
  
   <td><p style="text-align: right">
<a href="https://bio.tools/meshr">meshr</a></p>

   </td>
   <td>A set of annotation maps describing the entire MeSH assembled using data from MeSH.
   </td>
   <td>
   </td>
   <td>Medical informatics, Data quality management
   </td>
   <td>Command-line tool, Library
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<a href="https://bio.tools/locdb">locdb</a></p>

   </td>
   <td>Manually curated database with experimental annotations for the subcellular localizations of proteins in Homo sapiens (HS, human) and Arabidopsis thaliana (AT, thale cress). Each database entry contains the experimentally derived localization in Gene Ontology (GO) terminology, the experimental annotation of localization, localization predictions by state-of-the-art methods and, where available, the type of experimental information.
   </td>
   <td>
   </td>
   <td>Ontology and terminology, Data submission, annotation and curation, Proteins
   </td>
   <td>Database portal
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
<a href="https://bio.tools/zooma">zooma</a></p>

   </td>
   <td>ZOOMA 2 is a search engine for automatic curation and a repository of annotation knowledge. It facilitates automated data annotation against a variety of ontologies by exploring context and previous annotation efforts as well as lexical matching
   </td>
   <td>
   </td>
   <td>Systems biology, Ontology and terminology, Data identity and mapping
   </td>
   <td>Web application
   </td>
  </tr>
  <tr>
   
</table>


<h3 id="Ontology management">Ontology management</h3>
The process of managing ontologies and other vocabularies in semantic web-linked data environments.This includes policies for update and maintenance of constituent and new terms.

__Manually curated tools__ 
|Tool|Description|License|Topics|Resource Type|
|---|--|--|--|--|
|[OLS](https://www.ebi.ac.uk/ols/index)|a repository for biomedical ontologies that aims to provide a single point of access to the latest ontology versions.|[EMBL-EBI Terms of Use](https://www.ebi.ac.uk/about/terms-of-use/)||Web Application, API|
|[BioPortal](https://bioportal.bioontology.org/)|A repository of biomedical ontologies|[BioPortal Terms of Use](https://www.bioontology.org/terms/)||Web Application, API|
|[PoolParty](https://www.poolparty.biz/) |Knowledge Engineering & Knowledge Graph Management. Taxonomy, ontology and linked dataset management |Commercial license|Ontology and terminology|
|[Centree Ontology Manager](https://www.scibite.com/platform/centree/)|a centralised, enterprise-ready resource for ontology management and transforms the experience of maintaining and releasing ontologies for research-led businesses.|Commercial license||Web application, API|
|[Ontobee](http://www.ontobee.org/)|A linked data server designed for ontologies. Ontobee is aimed to facilitate ontology data sharing, visualization, query, integration, and analysis.|[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)||Web application|
|[AberOWL](http://www.aber-owl.net/)|A framework for ontology-based access to biological data. It consists of a repository of bio-ontologies, a set of webservices which provide access to OWL(-EL) reasoning over the ontologies, and several frontends which utilise the ontology repository and reasoning services.|||Web application, API|


__Tools discovered from [Bio.Tools](https://bio.tools).__
<table>
  <tr>
   <td>Tool
   </td>
   <td>Description
   </td>
   <td>License
   </td>
   <td>Topics
   </td>
   <td>Type
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/ngly1">ngly1</a>
   </td>
   <td>Structured Reviews for Data and Knowledge Driven Research | The NGLY1 Deficiency Knowledge Graph | This is the repository for the NGLY1 Deficiency Knowledge Graph, the reasoning context to support hypothesis discovery for NGLY1 Deficiency-CDDG (DOID:0060728) research. The user can navigate the knowledge in the graph in the Neo4j Browser website. This knowledge graph is a structured review around the research question what is the mechanism underpinning the NGLY1-AQP1 regulation association and explaining the reduced transcriptomic expression of multiple Aquaporins in NGLY1 deficient cells?. The graph v3.2 is the first deployed in the Wikibase application for community contribution and curation
   </td>
   <td>
   </td>
   <td>Molecular interactions, pathways and networks, Ontology and terminology, Machine learning
   </td>
   <td>Command-line tool
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/doc2hpo">doc2hpo</a>
   </td>
   <td>Web application for efficient and accurate Human Phenotype Ontology (HPO) concept curation.
   </td>
   <td>
   </td>
   <td>Genotype and phenotype, Ontology and terminology, Natural language processing
   </td>
   <td>Web application
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/amigo 2">amigo 2</a>
   </td>
   <td>The GO Consortium GO browser and search engine.
   </td>
   <td>
   </td>
   <td>Ontology and terminology
   </td>
   <td>Web application
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/plangexq">plangexq</a>
   </td>
   <td>PlanGexQ is a user-friendly interactive tool for the curation and annotation of planarian morphologies and gene expression patterns in a centralized database. PlanGexQ allows any user to define reference morphologies using mathematical graphs and a drag-and-drop interface. Gene expression pattern images can be uploaded to the program and then registered into the reference morphologies. Annotations with terms from the planarian anatomy ontology are autommatically created by analyzing the gene expression patterns and their textual descriptions. PlanGexQ represents a complete methodology for centralizing with formal and annotated descriptions the morphologies and gene expression patterns of planarian worms.
   </td>
   <td>
   </td>
   <td>Mathematics, Genotype and phenotype, Model organisms, Ontology and terminology, Gene expression
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/gocats">gocats</a>
   </td>
   <td>Advances in gene ontology utilization improve statistical power of annotation enrichment | Welcome to GOcats�â�� documentation! �â�� GOcats 1.1.5 documentation
   </td>
   <td>
   </td>
   <td>Mapping, Ontology and terminology, Microarray experiment
   </td>
   <td>Command-line tool
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/rdfscape">rdfscape</a>
   </td>
   <td>This is a project that brings Semantic Web features to the popular Systems Biology software Cytoscape. It allows to query, visualize and reason on ontologies represented in OWL or RDF within Cytoscape.
   </td>
   <td>
   </td>
   <td>Systems biology, Ontology and terminology, Biology
   </td>
   <td>Desktop application
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/ontobrowser">ontobrowser</a>
   </td>
   <td>The tool was developed to manage ontologies (and controlled terminologies e.g. CDISC SEND). The primary goal of the tool is to provide an online collaborative solution for expert curators to map code list terms (sourced from multiple systems/databases) to preferred ontology terms. Other key features include visualisation of ontologies in hierarchical/graph format, advanced search capabilities, peer review/approval workflow and web service access to data.
   </td>
   <td>
   </td>
   <td>Ontology and terminology, Data identity and mapping
   </td>
   <td>Web API, Web application
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/quickgo">quickgo</a>
   </td>
   <td>A fast browser for Gene Ontology terms and annotations.
   </td>
   <td>
   </td>
   <td>Ontology and terminology
   </td>
   <td>Web application
   </td>
  </tr>
  <tr>
   <td><a href="https://bio.tools/circular gene ontology (cirgo)">circular gene ontology (cirgo)</a>
   </td>
   <td>Visualises non-redundant two-level hierarchically structured ontology terms from gene expression data in a 2D space.
   </td>
   <td>
   </td>
   <td>Ontology and terminology, Data visualisation, Gene expression
   </td>
   <td>Command-line tool, Desktop application
   </td>
  </tr>
</table>
<h3 id="Ontology engineering">Ontology engineering</h3>

The process of developing and maintaining ontologies during the ontology life cycle.

__Manually curated tools__ 
|Tool|Description|License|Topics|Resource Type|
|---|--|--|--|--|
|[Protégé](https://protege.stanford.edu/)|A free, open source ontology editor and a knowledge management system|[2-Clause BSD](https://opensource.org/licenses/BSD-2-Clause)||Web application, Desktop application|
|[ROBOT](http://robot.obolibrary.org/)|An open source library and command-line tool for automating ontology development tasks. ROBOT provides ontology processing commands for a variety of tasks, including commands for converting formats, running a reasoner, creating import modules, running reports, and various other tasks.|[BSD 3-Clause License](https://raw.githubusercontent.com/ontodev/robot/master/LICENSE.txt)||Command-line tool|
|[OWLAPI](http://owlcs.github.io/owlapi/)|A Java API and reference implmentation for creating, manipulating and serialising OWL Ontologies|LGPL and Apache||API|
|[eNanoMapper Slimmer](https://github.com/enanomapper/slimmer)|A slim tool to slim ontologies as part of ontology integration. It allows users to provide configuration files that specify which parts of an ontology should be kept and/or removed, allowing to just select parts of the ontology you like.|[MIT license](https://opensource.org/licenses/MIT)||Java|
|[TopBraid Composer](https://www.topquadrant.com/products/topbraid-composer/)|TopBraid Composer Maestro Edition is used to develop ontology models, configure data source integration, and create semantic services and user interfaces.|[Commercial license](https://www.topquadrant.com/legal/)||
|[VocBench](http://vocbench.uniroma2.it/)|a web-based, multilingual, collaborative development platform for managing OWL ontologies, SKOS(/XL) thesauri, Ontolex-lemon lexicons and generic RDF datasets.|[License](https://bitbucket.org/art-uniroma2/vocbench3/src/master/LICENSE)||Desktop application|


## Implementation examples
To show how these tools can be used in real life examples, please check the related recipes.
- [Which vocabulary to use?](https://fairplus.github.io/the-fair-cookbook/content/recipes/interoperability/selecting-ontologies.html)
- [Building an application ontology with Robot](https://fairplus.github.io/the-fair-cookbook/content/recipes/interoperability/ontology-robot-recipe.html)

## Authors
|Name|Affiliation|ORCID|Credit role|
|---|--|--|--|
|Fuqi Xu|EMBL-EBI|0000-0002-5923-3859|Original draft|
|Eva|||Original draft
|Sukhi||Tool curation|
|Nick||Reviewing|
|Peter|||Reviewing |
|Philippe||


