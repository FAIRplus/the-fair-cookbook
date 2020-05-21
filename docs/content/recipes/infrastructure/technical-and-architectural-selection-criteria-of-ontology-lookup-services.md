# Recipe 1.2 Technical & architectural selection criteria of ontology lookup services

**identifier:** [UC1 R1.2](UC3R1.2)

**version:** [v0.1](v0.1)
___

**_Difficulty level:_** :triangular_flag_on_post: :triangular_flag_on_post:	:white_circle:	:white_circle:	:white_circle:

**_Reading time:_** 20 minutes

**_Intended Audience:_** 

> :heavy_check_mark: Terminology Manager

> :heavy_check_mark: Ontologist

> :heavy_check_mark: System Administrator

> :heavy_check_mark: Data Scientist

**_Recipe Type_**: Technical Guidance

**_Executable code_**: No

___

[TOC]

___

## Main Objective

This recipe provides guidance to make a  decision about feasibility of local deployment of offered open source ontology services software. By the expression ‘ontology lookup service’ we refer **to any type of application, standalone or Web-based, that enables the use of existing ontologies to support knowledge formalization and sharing, by fostering ontology-based descriptions of knowledge**. Tools useful to build, edit or maintain ontologies are not considered ontology lookup services and thus are out of the scope of this recipe.

The recipe will:

- define the most common selection criteria to be considered
- provide general selection recommendations
- provide recommendations for applying those selection criteria
- give an overview about the most common open source ontology service software

## Software selection criteria

This section presents the minimal criteria to take in account when analyzing alternatives for ontology-based services development and deployment. Additional criteria, including a more detailed analysis of technical features can be found on the resources mentioned in section “Additional resources”.

### Functionality

Functionality of a software determines the range of capabilities and functions it can perform. 
Please note that specific functional selection criteria are beyond the scope of this recipe. Because functionality plays a very important role in the overall selection process it was added to show how it relates to the technical & architecture selection process.  
Functional selection criteria is covered by Recipe 1.1 (<to be replaced with recipe 1.1 URL>)

### Interfaces

Interfaces allow read or write data from outside the ontology lookup service either by a human being or application.

For an ontology lookup service the most important interface features are:

- Supported import and export ontology formats, e.g. OWL for uploading and downloading of ontologies.
- Flexible query interface, e.g. to answer very specific ontology questions or to extend functional gaps of the ontology service. Currently the most prominent query interface is SPARQL endpoint.
- Application Programming Interface (API) technology, if you want to integrate other applications with the ontology lookup service it is essential that you can use widely used and supported technical standards. Currently the most prominent API technology is REST API. 

Please note that this recipe does not focus on specific interface functionality. It looks at interfaces only from an architectural and technical view. 

## Software Architecture

The software architecture shows the used hardware and software components and their relationship.

Regarding ontology lookup service selection the most important architectural aspects are:

- *Overall architecture complexity*
It gives you an idea whether the complexity is appropriate for solving your requirements.
If you are trying to solve simple requirements with a very complex solution you might be on the wrong way. 
- *Used tools and programming languages*
It gives you an idea what knowledge you will need for supporting the system or extending the functionality. You also get an overview of the impact to the overall complexity of the IT tools and programming languages used in your organization.
- *Modularity*
It gives you an idea whether you could replace some of the components by software/hardware preferred as standard in your company. It can give you also a hint, whether you can scale the application by adding more hardware/software resources.

## Deployment model

The deployment model shows where and how the software can be installed and who owns the service.

Regarding ontology lookup service selection the most important deployment aspects are:

- *On premise versus cloud deployment*
Depending on your organisation policies and best practices it might be the case that you want to install and maintain the software on your own infrastructure (on premise) or you prefer to buy it as a service on the cloud. 
- *Manual versus docker versus virtual image installation*
With a manual installation you have full control over the installation but you need typically more time. 
A virtual image installation bundles software together with the operating system, so it is easier to install, but typically you would need additional infrastructure and knowledge in your organisation to maintain all virtual images. 
A docker based installation is also easy to install and typically saves more hardware resources than a virtual image installation, because you share the operating system amongst multiple docker applications. Similar to virtual image installation you would need additional infrastructure and knowledge in your organisation to run and maintain all docker images.

## Hardware and software requirements

The hardware requirements have mainly an impact on the costs. The software requirements have an impact on knowledge and costs (e.g. licences for operating systems).

The specific requirements of your organisation for data processing and storage will also influence the costs.

### License model

The license model defines the consumer rights and the usage costs.

So it is essential that the licence model:

- matches with your intended use 
- produces costs that  are acceptable for your organisation from a price/performance point of view.

### Database Technology

The database is a central component that will store the ontologies. From an ontology perspective state of the art is to use a graph database.

Two types of graph databases are currently available:

- Label-Property
A labeled-property graph model is represented by a set of nodes, relationships, properties, and labels. 
- Triple store
A triple store database allows you to store OWL formats natively and use the “query from remote” flexibility of a SPARQL endpoint. Also Shape Constraint Language (SHACL) W3C standard could help to add quality checks.

For storing metadata representable in flat taxonomies often Relational Database Management Systems (RDBMS) are used which represent data in tabular format.

The database system is considered as a core component of data quality supporting atomic consistent transactions for replacing ontologies or subsets of them.

A Database system is a complex piece of software where you need knowledge for managing it. In order to reduce overall complexity you will typically define per used database technology type. Therefore it might be an important selection criteria whether you can use your own standard.

The database system will typically also have a major impact on performance and scalability, because the bulk of ontology query processing will take place within the database system.

An ontology lookup service is defined to be **database agnostic**, if its database component: 

- provides Interfaces that use standard protocols for communication
- provides an configurable access to the database 
- Allows that any database product that supports the used standards (e.g. SPARQL) can be used 

A database agnostic ontology lookup service software will give you therefore the maximum freedom to use your defined database type standard.

### Ontology language

Following ontology languages are widely used in the pharma research arena to model ontologies:

- Web Ontology Language (OWL) 
OWL is defined by W3C and has become the de facto standard for ontology modelling. Therefore OWL support is considered as a must for the ontology lookup service. 
- OBO
The OBO file format is a biology-oriented language for building ontologies, based on the principles of OWL. A standard common mapping has been created for lossless roundtrip transformations among both languages. 

If you have ontologies in different languages you will need to transform them to OWL.

### Programming language

Programming languages are used to implement the data processing logic and user interface logic of the ontology lookup service.

The used programming languages will impact:

- Required programming language knowledge you need for customization or support
- Customization effort, e.g. The Python/Ruby programming languages are considered much more compact than Java.

### Support

Important support aspects for the ontology lookup service are: 

- Ongoing development of the tool 
- Frequency of issues and how fast they are solved
- Which organization you can get support from, and what is the associated cost?

## General selection considerations

Before looking into a concrete ontology service, some general thoughts are recommended. Two type of portal tools are available:

- Open data portal tool
Open data portals provide web-based interfaces designed to make it easier to find and access re-usable information. Some of them support also importing and exporting ontologies including a SPARQL endpoint and provide ontology lookup service core functionality.
An Open Portal Tool is the underlying software that is used to implement the ontology portal functionalities.
- Ontology portal tool
A formal definition of Ontology Portal does not exist. In the context of this document an Ontology Portal is defined as an Open Data Portal that is specialized to ontologies as data and typically provides out of the box more fine granulare ontology based functions.
An Ontology Portal Tool is the underlying software that is used to implement the ontology portal functionalities.

If you have only minimum functional requirements in sharing ontologies it might be also an option for you to use an open data portal tool. In this case you could extend the functionality by developing additional web pages using the SPARQL endpoint. Having data and metadata in one database, such a solution would allow to add functionality that needs to combine ontologies with data (e.g. by annotation).

If you need fine granular ontology lookup service functionality an ontology portal tool is recommended.

An additional option would be to combine an Open data platform tool with an Ontology portal tool in parallel. If both tools use a triplestore database this should be possible in principle. The challenge will be that you would need additional customisation.

## Choosing an ontology service software

As each organization may have its own preferences and requirements there is no common standard way to select the best suitable ontology service software. This section demonstrates a general selection process based on aforementioned selection criteria and gives guidance on a set of questions that must be answered in order to filter out tools that do not fit to your use case at an early stage. Therefore simplifying the ontology software selection process.

## Overall Selection Process

A three step selection approach is proposed: 

- High Level Gap Analysis
First it should be checked on a high level whether the tool does match with your high level requirements. 
- Low Level Gap Analysis
Only if the tool matches on a high level more effort should be invested in a more fine granular analysis to find out whether the tool is still a candidate for you. 
- From Candidates Selection 
Once you have identified the tool candidates you would rank them by assigning fulfillment numbers to the weighted criteria reflecting the importance for your organization.  Finally you will calculate the total fulfillment number out of them and choose the tool with the highest number. 

Following figure shows the overall process:

```mermaid
graph TB
No[Tool does not fit]
Candidate[Tool is a candidate]

subgraph High Level Criteria Selection
HlCheck[Does the tool match the high level criteria?]
end
HlCheck -->|yes| LlCheck
HlCheck -->|no| No 

subgraph Low Level Criteria Selection
LlCheck[Does the tool match the low level criteria?]
end
LlCheck -->|yes| Candidate
LlCheck -->|no| No
Candidate -->  Calc

subgraph From Candidates Selection
Calc[Define per criteria fullfillment number] --> Sum[Sum weightened fullfillment numbers]
Sum -->  Highest[Has candidate highest fullfillment number]
end
Highest -->|yes| Yes[Best Tool for you]
Highest -->|no| NotBest[Not Best Tool for you]
style Candidate fill:lightgreen
style Yes fill:green
style No fill:red
style NotBest fill:#FF9999
```

Figure 1: Overall Selection Process

### High Level Gap Analysis

As guidance for the High Level Gap Analysis an analysis order based on selection criteria is proposed. The most important selection criteria contain one major question that has to be answered positively either by the offerings of the tool or by some additional tool customization.

```mermaid
graph TB
subgraph Functionality
FuncGap[Do you need more functions than offered?] 
FuncCust[Can I add the functions by customization?] 
end
FuncNo[Tool does not fit]
style FuncNo fill:red
FuncGap-->|no| FuncOk
FuncGap-->|yes| FuncCust
FuncCust-->|yes| FuncOk
FuncCust-->|no| FuncNo
FuncOk[Ok] --> IfGap
style FuncOk fill:lightgreen

subgraph Interfaces
IfGap[Do you need more interfaces than offered?] 
IfCust[Can I add my interfaces by customization?] 
end
IfNo[Tool does not fit]
style IfNo fill:red
IfGap -->|yes| IfCust
IfGap-->|no| IfOk
IfCust -->|yes| IfOk
IfCust -->|no| IfNo
IfOk[Ok] --> Arch 
style IfOk fill:lightgreen

subgraph Architecture
Arch[Is the architecture too complex for solving your requirements?] 
end
ArchNo[Tool does not fit]
style ArchNo fill:red
Arch -->|yes| ArchOk
Arch -->|no| ArchNo
ArchOk[Ok] --> CostGap
style ArchOk fill:lightgreen

subgraph Costs
CostGap[Are the licence costs for the tool acceptable?] 
end
CostNo[Tool does not fit]
style CostNo fill:red
CostGap-->|yes| CostOk
CostGap-->|no| CostNo
CostOk[Ok] --> PerfGap
style CostOk fill:lightgreen

subgraph Performance
PerfGap[Does any existing installation cover your volume and processing profile?] 
end
PerfNo[Tool does not fit]
style PerfNo fill:red
PerfGap-->|yes| SupGap
PerfGap-->|no| PerfNo

subgraph Support
SupGap[Does the tool support match with your quality and long term support requirements?] 
end
SupNo[Tool does not fit]
style SupNo fill:red
Candidate[Tool is a candidate]
style Candidate fill:lightgreen
SupGap-->|yes| Candidate
SupGap-->|no| SupNo

```

Figure 2: High Level Gap Analysis

### Low Level Gap Analysis 

For a single low level selection criteria no common recommendation for the “tool does not fit” decision can be given, because the decision highly depends on the preferences set in your specific context. Instead a set of questions will be presented per selection criteria. You have then to pick out those questions that are absolutely mandatory in our context. If such an absolutely mandatory question can not be solved by the tool or by tool customization the “Tool does not fit” will fire.

Please note that for ontology functionality no questions will be presented, because functionality is out of the scope of this recipe.

```mermaid
graph TB;
No[Tool does not fit]
style No fill:red
Candidate[Tool is a candidate]
style Candidate fill:lightgreen
Start --> SCL
 
subgraph Selection Criteria Loop
SCL>For each: Selection Criteria]
style SCL fill:darkgrey
SCLF[Last Selection Criteria finished]
end
 
SCL --> SCLF
SCLF --> Candidate 
SCL --> SCQL 
 
subgraph Low Level Selection Criteria Gap Analysis
SCQL>For each: Selection Criteria Question]
style SCQL fill:darkgrey
SCQM[Is a yes to the question yes mandatory for you?]
end
SCQL --> SCQM
SCQM -->|yes| SCQY
 
 
subgraph Single Mandatory Question Analysis 
SCQY[Is the answer to the question yes?]
SCQC[Can customization provide a yes answer with costs below your limits?]
end
SCQY -->|no| SCQC
SCQC -->|no| No
```

Figure 3: Low Level Gap Analysis

Following figures are showing typical questions you will have to answer for the low level analysis. Please adapt or extend questions to your specific needs.

```mermaid
graph TB;

subgraph Functional Questions
FQ["Functional questions not covered by this recipe!"]
end
```

Figure 4: Typical Low Level Functional Questions

```mermaid
graph TB;
subgraph Interface Questions
Int1[Is the upload of Ontologies supported?]
Int2[Are all required upload ontology formats supported?]
Int3[Is the downlaod of Ontologies supported?]
Int4[Are all required download ontology formats supported?]
Int5[Is RestAPI interface supported?]
Int6[Is SPARQL endpoint supported?]
IntL[Is federation supported for SPARQL endpoint?]
end

Int1 --> Int2 --> Int3 --> Int4 --> Int5 --> Int6 -->  IntL
```
Figure 5: Typical Low Level Interface Questions
```mermaid
graph TB;
 
subgraph Architecture Questions
Arch1[Does the system support a distributed ontology administration model?]
Arch2[Do the supported Databases match with our standards and knowledge?]
Arch3[Can the Databases replaced by our standards and knowledge?]
Arch4[Does the customization language match with our standards and knowledge?]
Arch5[Do the supported Index server match with our standards and knowledge?]
Arch6[Does the supported Operating System match with our standards and knowledge?] 
Arch7[Does the supported web server match with our organisation standards and knowledge?]
Arch8[Does the system support on premise installation?]
Arch9[Does the system support cloud installation?]
Arch10[Is the system deployment supported by virtual image?]
ArchL[Is the system deployment support by docker images?]
end
Arch1 --> Arch2 --> Arch3 --> Arch4 --> Arch5
Arch5 --> Arch6 --> Arch7 --> Arch8 --> Arch9 --> Arch10 --> ArchL
```
Figure 6: Typical Low Level Architecture Questions
```mermaid
graph TB;
 
subgraph "Costs Questions (Initial and Ongoing)"
Cost1[Are the software licence costs acceptable?] 
Cost2[Are the database licence costs acceptable?]
Cost3[Are the hardware costs acceptable?]
Cost4[Are the training costs acceptable?]
Cost5[Are the support costs acceptable?]
CostL[Are the customization costs acceptable?]
end
Cost1 --> Cost2 --> Cost3 --> Cost4 --> Cost5 --> CostL
```

Figure 7: Typical Low Level Costs Questions

```mermaid
graph TB;
 
subgraph Performance Questions 
Perf1[Does the system provide a scalable architecture?] 
Perf2[Is the volume of existing installations equal or beyond my volume?]
Perf3[Is the number of users of existing installations similar or beyond my number of users?]
Perf4[Does the system collect performance indicators?]
PerfL[Does the system offer automatic performance measurements?]
end
Perf1 --> Perf2 --> Perf3 --> Perf4 --> PerfL
```

Figure 8: Typical Low Level Performance Questions

```mermaid
graph TB;
 
subgraph "Delivery Questions"
Del1[Is on premise supported?] 
Del2[Is cloud supported?] 
Del3[Is manual installation supported?] 
Del4[How much effort is needed for manual installation?] 
Del5[Is virtual image based installation supported?] 
DelL[Is Docker based installation supported?] 
end
Del1 --> Del2 --> Del3 --> Del4  --> Del5 --> DelL
```

Figure 9: Typical Low Level Delivery Questions

```mermaid
graph TB;
 
subgraph "Support (per component)"
Sup1[Was the system continuously improved?] 
Sup2[Do you have confidence in the future development of the system?] 
Sup3[Do you have a fallback if further support for the product is frozen?] 
Sup4[Do you have confidence that bugs are fixed in a reasonable time frame?]
Sup5[Is commercial support available?]
SupL[Is the support quality sufficient for you?]
end

Sup1 --> Sup2 --> Sup3 --> Sup4  --> Sup5 --> SupL
```

Figure 10: Typical Low Level Support Questions

## Available common open source software

### Ontology Lookup Service (Ontology Portal Tool)

#### Overview

It is a repository for biomedical ontologies that aims to provide a single point of access to the latest ontology versions. It allows browsing the ontologies through the website as well as programmatically via the OLS API. It is part of the ELIXIR interoperability service.

#### Details

1. Functionality: Ontology Portal Tool
2. Interface: REST-style API supported, SPARQL endpoint under development.
3. Architecture: OLS has been developed with the Spring Data and Spring Boot framework.
    1. Tomcat is used as a web server.
    2. MongoDB is used for storing configuration yaml files.
    3. Neo4J node-property graph database is used for storing and accessing the ontologies. OWL format is converted to a node-property representation.
4. Deployment model: It is available both as an on-premises and cloud-based solution. Docker based deployment is supported.
5. Requirements
    1. Hardware requirements. It requires a standard workstation, 1GB main memory, and about 100MB hard disk.
    2. Software requirements. It is implemented as a Java Web Application to be deployed to the Tomcat 7.5 Java Application Container. It requires Java 8, Maven 3+ as dependency manager and build environment, MongoDB 2.7.8+ as database; and solr 5.2.1+ as indexing and search engine.
    3. License model. Apache Software Licence (v. 2.0).
6. Databases: It supports the Neo4J graph store, which allows querying using Cypher query language. Reasoning supports two profiles: OWL2 and EL. Default is EL. The reasoners supported are HermiT and ELK.
7. Ontology Language: Custom translation of OBO and OWL 2 languages to the Neo4J graph model.
8. Programming Language: Java.

### Virtual Appliance (Ontology Portal Tool)

#### Overview

The National Center for Biomedical Ontology (NCBO).

#### Details

1. Functionality: Ontology Portal Tool
2. Interface: REST-style API supported, SPARQL endpoint 
3. Architecture: Virtual Appliance defines the framework for the Web Service. The system internally uses the following components
    1. A set of additional ruby based modules that implement the user interface and additional functionality can be found [here](https://github.com/ncbo).
    2. 4Store triple store database is used to store and access ontologies. 
    3. Solr is used to create indexes out of description text metadata.  
    4. MySQL is used to store additional metadata.
    5. MGrep is used for annotating text to ontologies.
4. Deployment model: It is available both as an on-premises and cloud-based solution. It is available as virtual VMWare Virtual Appliance or Amazon AWS AMI. 
5. Requirements:
    1. Hardware requirements. 
        1. Minimum: 2 CPU (2 GHz), 4GB RAM, 20GB hard disk space.
        2. Recommended for heavier usage: 3 CPU (3 GHz), 8GB RAM (or more depending on the size/number of ontologies), 20GB hard disk space (or more depending on number/size of ontologies)
    2. Software requirements. All software is already contained in the virtual image
        1. Operating system: CentOS (Linux)
        2. License model. Apache Software Licence (v. 2.0).
6. Databases: It supports the 4Store triple store and MySQL
7. Ontology Language: OBO, OWL, UMLS
8. Programming Language: Ruby, Java.

### Apache Marmotta (Open Data Platform Tool)

#### Overview

It is an Open Data Platform for Linked Data, which provides an open implementation of a Linked Data Platform that can be used, extended and deployed easily by organizations who want to publish Linked Data or build custom applications on Linked Data. It provides (a) read-write Linked Data server for the Java EE stack, (b) custom triple store built on top of RDBMS, with transactions, versioning and rule-based reasoning support, (c) pluggable RDF triple stores based on Eclipse RDF4J,  (d) LDP, SPARQL and LDPath querying, (e) transparent Linked Data Caching, and (f) Integrated basic security mechanisms.

#### Details

1. Functionality: Open (Linked) Data Platform.
2. Interface: REST-style API, SPARQL endpoint supported.
3. Architecture, the architecture comprises the following tiers:
    1. User Interface Layer. It mostly consists of admin and development interfaces and is not intended for end users.
    2. Web-service Layer. It offers REST web-services to access most of the server functionality.
    3. Service Layer. It offers CDI services to develop custom Java applications.
    4. Model Layer. It offers persistence and data access functionality.
    5. Persistence Layer. It is outside the Apache Marmotta Platform, which can use a number of Open Source database systems.
4. Deployment Model: It is available both as an on-premises and cloud-based solution. Docker based deployment is supported.
5. Requirements:
    1. Hardware requirements. It requires a standard workstation, 1GB main memory, and about 100MB hard disk.
    2. Software requirements. It is implemented as a Java Web Application that can, in principle, be deployed to any Java Application Container. It has been tested under Jetty 6.x and Tomcat 7.x. It requires Java JDK 6 or higher, Java Application Server (Tomcat 7.x or Jetty 6.x), and a database (PostgreSQL, MySQL). If not explicitly configured, an embedded H2 database will be used.
    3. License model. Apache Software Licence (v. 2.0).
6. Databases: It supports the following triple store backends: (a) KiWi Triple Store, (b) Sesame Native, and (c) BigData triple store. The default backend is the KiWi triple store, which stores all data in a relational database and it is the only option that supports reasoning and versioning.
7. Ontology Language: OWL serialized as RDF/RDFS triples. 
8. Programming Language: Java.

### European Data Portal (Open Data Platform Tool)

#### Overview

European data portal  (EDP) is an initiative by the Publications Office of the European Union and by the European Commission that aims to increase the impact of open data by making it easy to find and re-use by everyone.
It uses only open source software with extensions that are all available to the public for own use. As a core component CKAN open data portal software with DCAT-AF RDF extension is used. It allows sharing various data formats e.g. tabular data, RDF data (e.g. ontologies) combining relational and semantic technologies. The Triple Store database Virtuoso is used for storing ontologies. For metadata in relational format Postgres database is used as part of CKAN.

#### Details

1. Functionality: Open Data Portal 
2. Interface: REST-style API, SPARQL endpoint supported.
3. Architecture:
    1. CKAN manages and provides metadata content (datasets) in a central repository. 
    2. DRUPAL provides the Portal’s Home Page with editorial content (e.g. Portal’s objectives, articles, news, events, tweets, etc.) and links to an Adapt Framework based training platform. 
    3. The CKAN metadata is replicated into a Virtuoso triple store database via a CKAN synchronisation extension, in order to ensure that both repositories have the same set of metadata. 
    4. The SPARQL Manager component allows the user to enter and run SPARQL queries on the Virtuoso linked data repository. 
    5. The portal uses the SOLR search engine in order to separately search for editorial content in DRUPAL and for datasets in the CKAN repository. 
    6. The Harvester is a separate component that is able to harvest data from multiple data sources with different formats and APIs. 
4. Deployment model: It is available both as an on-premises and cloud-based solution.
5. Requirements:
    1. The setup of the EDP consists of 20 virtual servers per computer room and environment (PROD, TEST)
6. Databases: Postgres RDBMS for CKAN catalogue, Virtuoso for RDF data
7. Ontology Language: RDF, RDFS, OWL 2
8. Programming Language: Python(CKAN), PHP(Drupal)

### Authors

| Name               | Affiliation            | ORCID             | CRediT Role          |
|--------------------|------------------------|------------------:|--------------:|
|Kurt Dauth          | Boehringer Ingelheim   | |Original Author|
|Emiliano Reynares   | Boehringer Ingelheim   |0000-0002-5109-3716 | Author|
|Petros Papadopoulos | Heriot-Watt University |0000-0002-8110-7576 | Author|
|Karsten Quast       | Boehringer Ingelheim   |0000-0003-3922-5701 | Reviewer|
### Licence

[Please click here for licence](https://creativecommons.org/licenses/by/4.0/)
