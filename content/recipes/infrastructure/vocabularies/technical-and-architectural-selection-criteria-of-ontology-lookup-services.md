(fcb-select-onto-service-criteria)=
# Portals and lookup services



````{panels_fairplus}
:identifier_text: FCB003
:identifier_link: 'https://w3id.org/faircookbook/FCB003'
:difficulty_level: 2
:recipe_type: technical_guidance
:reading_time_minutes: 20
:intended_audience: data_manager, data_scientist, terminology_manager, system_administrator  
:maturity_level: 0
:maturity_indicator: 0
:has_executable_code: nope
:recipe_name: Introducing vocabulary portals and lookup services
```` 

## Main Objective

This recipe provides guidance on making a decision about the feasibility of a local deployment of existing open source
ontology service software. 

By the expression **"ontology lookup service"**, we refer **to any type of application, 
standalone or Web-based, that enables the use of existing ontologies to support knowledge formalization and sharing,
by fostering ontology-based descriptions of knowledge**.

Therefore, tools useful to build, edit or maintain ontologies 
are not considered as ontology lookup services and thus are out of the scope of this document.

The recipe will:

- define the most common selection criteria to be considered
- provide general selection recommendations
- provide recommendations for applying those selection criteria
- give an overview about the most common open source ontology service software

## Software selection criteria

This section presents the minimal criteria to take in account when analyzing alternatives for ontology-based services
development and deployment. Additional criteria, including a more detailed analysis of technical features can be found 
on the resources mentioned in section **Additional resources**.

### Functionality

Functionality of a software determines the range of capabilities and functions it can perform. 
Please note that specific functional selection criteria are beyond the scope of this recipe.
Because functionality plays a very important role in the overall selection process it was added to show how it relates
to the technical & architecture selection process.  
Functional selection criteria are covered by Recipe [FCB004](https://w3id.org/faircookbook/FCB004   ) 

### Interfaces

Interfaces allow read or write data from outside the ontology lookup service either by a human being or application.

For an ontology lookup service the most important interface features are:

- Supported import and export ontology formats, e.g. OWL for uploading and downloading of ontologies.
- Flexible query interface, e.g. to answer very specific ontology questions or to extend functional gaps of the ontology service.
Currently, the most prominent query interface is SPARQL endpoint.
- Application Programming Interface (API) technology, if you want to integrate other applications with the ontology 
lookup service it is essential that you can use widely used and supported technical standards. 
Currently, the most prominent API technology is REST API. 

Please note that this recipe does not focus on specific interface functionality. It looks at interfaces only from an
architectural and technical view. 

## Software Architecture

The software architecture shows the used hardware and software components and their relationship.

Regarding ontology lookup service selection the most important architectural aspects are:

- *Overall architecture complexity*
It gives you an idea whether the complexity is appropriate for solving your requirements.
If you are trying to solve simple requirements with a very complex solution you might be on the wrong way. 
- *Used tools and programming languages*
It gives you an idea what knowledge you will need for supporting the system or extending the functionality. 
You also get an overview of the impact to the overall complexity of the IT tools and programming languages used in your organization.
- *Modularity*
It gives you an idea whether you could replace few of the components by software/hardware preferred as standard in your company.
It can give you also a hint, whether you can scale the application by adding more hardware/software resources.

## Deployment model

The deployment model shows where and how the software can be installed and who owns the service.

Regarding ontology lookup service selection the most important deployment aspects are:

- **On premise versus cloud deployment**
Depending on your organisation policies and best practices, it might be the case that you want to install and maintain 
the software on your own infrastructure (***on premise***) or you prefer to buy it as a service on the cloud. 
- ** **Manual** versus **containerized** versus **virtual image** installation**
    - With a **manual installation**, you have full control over the installation, but you need typically more time. 
      - A **virtual image installation**` bundles software together with the operating system, so it is easier to install,
  but typically you would need additional infrastructure and knowledge in your organisation to maintain all virtual images.
    - A **docker based installation** is also easy to install and typically saves more hardware resources than a virtual
  image installation, because you share the operating system amongst multiple docker applications.
  Similar to virtual image installation you would need additional infrastructure and knowledge in your organisation to
  run and maintain all docker images.

## Hardware and software requirements

The hardware requirements have mainly an impact on the costs. The software requirements have an impact on knowledge 
and costs (e.g. licences for operating systems).

The specific requirements of your organisation for data processing and storage will also influence the costs.

### License model

The license model defines the consumer rights and the usage costs.

So it is essential that the licence model:

- matches with your intended use 
- produces costs that  are acceptable for your organisation from a price/performance point of view.

### Database Technology for storing knowledge representation resources

The **terminology database** is a central component of knowledge management stack as it will store the ontologies. 

The database system will typically also have a major impact on performance and scalability, because the bulk of ontology
query processing will take place within the database system.

An ontology lookup service is defined to be **database agnostic** if its database component:

- provides interfaces that use standard communication protocols.
- provides a configurable access to the database. 
- allows any database product supporting a specific standards(e.g. SQL, SPARQL) to be used

A database agnostic ontology lookup service software will give you therefore the maximum freedom to use your defined database type standard.

#### Relational databases:
- For storing metadata representable in flat taxonomies often Relational Database Management Systems (RDBMS) are used 
which represent data in tabular format.

#### Graph databases
From an ontology perspective, state of the art is to use a [**graph database**](https://en.wikipedia.org/wiki/Graph_database).
Two types of graph databases are currently available:

- **Labeled-Property**
A **labeled-property graph model** is represented by a set of nodes, relationships, properties, and labels. 
- **Triple store**
A **triple store database** allows to store documents in [RDF](https://www.w3.org/TR/rdf-concepts/#section-data-model) or
[OWL/RDF format](https://www.w3.org/TR/owl2-rdf-based-semantics/) natively and use the **query from remote** flexibility of
a [**SPARQL endpoint**](https://www.w3.org/TR/rdf-sparql-query/). 
Also, [**Shape Constraint Language (SHACL)**](https://www.w3.org/TR/shacl/) W3C standard could help to add quality checks.



### Ontology language

The following ontology languages are widely used in the pharma research arena to model ontologies:

- **Simple Knowledge Organization System (SKOS)**
SKOS is a W3C standard which provides a standard way to represent knowledge organization systems using the Resource Description Framework (RDF). 
Encoding this information in RDF allows it to be passed between computer applications in an interoperable way {footcite}`SkosReference2008`
- **Web Ontology Language (OWL)** 
OWL is defined by W3C and has become the de facto standard for ontology modelling. 
Therefore, OWL support is considered as a must for the ontology lookup service. 
- **OBO**
The OBO file format is a biology-oriented language for building ontologies, based on the principles of OWL.
A standard common mapping has been created for lossless round-trip transformations among both languages. 


Persisting semantics artefacts expressed in various languages and representation frameworks in the same management 
system isn't straightforward and conversions may be necessary. Even then, transformations may lead to information loss or 
difficulty in rendering information consistently.



### Programming language

Programming languages are used to implement the data processing logic and user interface logic of the ontology lookup service.

The used programming languages will impact:

- Required programming language knowledge you need for customization or support
- Customization effort

### Support

Important support aspects for a vocabulary service/ontology lookup service are: 

- Ongoing development of the tool 
- Frequency of issues and how fast they are solved
- Which organization you can get support from, and what is the associated cost?

## General selection considerations

Before looking into a concrete ontology service, some general thoughts are recommended. Two types of portal tools are available:

- **Open data portal tool**
**Open data portals** provide web-based interfaces designed to make it easier to find and access re-usable information. 
Some of them also support importing and exporting ontologies, including a SPARQL endpoint and provide ontology lookup 
service core functionality.
An **Open Portal Tool**` is the underlying software that is used to implement the ontology portal functionalities.
- **Ontology portal tool**
A formal definition of an **Ontology Portal** does not exist. In the context of this document, an **Ontology Portal** is
defined as an Open Data Portal that is specialized to ontologies as data and typically provides out of the box more fine
granular ontology based functions.
An Ontology Portal Tool is the underlying software that is used to implement the ontology portal functionalities.

If you have only minimum functional requirements in sharing ontologies it might be also an option for you to use an 
open data portal tool. In this case you could extend the functionality by developing additional web pages using the
SPARQL endpoint. Having data and metadata in one database, such a solution would allow adding functionality that needs 
to combine ontologies with data (e.g. by annotation).

If you need **fine granular ontology lookup service functionality**, an ontology portal tool is recommended.

An additional option would be to combine an Open data platform tool with an Ontology portal tool in parallel. 
If both tools use a triplestore database, this should be possible in principle. The challenge will be that you would
need additional customisation.

## Choosing an ontology service software

As each organization may have its own preferences and requirements, there is no standard way to select the best
suitable ontology service software. This section presents a general selection process based on the aforementioned
selection criteria and gives guidance on a set of questions that should be answered in order to filter out tools that
do not fit to use case at an early stage.

## Overall Selection Process

A three-step selection approach is proposed: 

- `High Level Gap Analysis`
First, it should be checked on a high level whether the tool does match the high level requirements. 
- `Low Level Gap Analysis`
Only if the tool matches on a high level, more efforts should be invested in a finer analysis to find out whether the
tool is still a suitable candidate. 
- `From Candidates Selection` 
Once the tool candidates have been identified, a ranking process can start by assigning fulfillment numbers to the
weighted criteria reflecting the importance for the requesting organization.  Finally, completing the ranking by 
summing up the total numbers from each atomic ranking criteria will allow to choose the tool, based on the highest scorer. 

Following figure shows the overall process:


````{dropdown}
:open:  
```{figure} onto-services-figure1.svg
---
name: onto-services-figure1
width: 450px
alt: Overall Process for Selecting Ontology Services 
---
Overall Process for Selecting Ontology Services 
```
````



### High Level Gap Analysis

As guidance for the **High Level Gap Analysis**, an analysis order based on selection criteria is proposed. 
The most important selection criteria contains one major question that has to be answered positively, 
either by the offerings of the tool or by some additional tool customization.

````{dropdown}
:open:
```{figure} onto-services-figure2.svg
---
name: onto-services-figure2
alt: Ontology Services High Level Gap Analysis
---
Ontology Services High Level Gap Analysis
```
````


<!-- Figure 2: High Level Gap Analysis -->

### Low Level Gap Analysis 

For a single **low level selection criteria**, no common recommendation for the “tool does not fit” decision can be
given, because the decision highly depends on the preferences set in your specific context.

Instead, a set of questions  will be presented per selection criteria. 
One has then to pick out those questions that are absolutely mandatory in a  local context.

If such an absolutely mandatory question can not be solved by the tool or by tool customization, the “Tool does not fit” will fire.

```{warning}
Please note that for **ontology functionality**, no questions will be presented, because functionality is out
of the scope of this recipe.
```

````{dropdown}
:open:
```{figure} onto-services-figure3.svg
---
name: onto-services-figure3
alt: Ontology Services  Low Level Gap Analysis
---
Ontology Services Low Level Gap Analysis
```
````



<!-- Figure 3: Low Level Gap Analysis -->

The following figures are showing typical questions one would have to answer for the low level analysis.

These questions may have to be adapted or extended depending on the local, specific needs.

````{dropdown} functional questions
:open:
```{figure} onto-services-figure4.svg
---
name: onto-services-figure4
alt: Typical Low Level Functional Questions
---
Typical Low Level Functional Questions
```
````

<!-- Figure 4: Typical Low Level Functional Questions -->


````{dropdown} user interface questions
:open:
```{figure} onto-services-figure5.svg
---
name: onto-services-figure5
alt: Typical Low Level Interface Questions
---
Typical Low Level Interface Questions
```
````

<!-- Figure 5: Typical Low Level Interface Questions -->



````{dropdown} Architecture questions
:open:
```{figure} onto-services-figure6.svg
---
name: onto-services-figure6
alt: Typical Low Level Architecture Questions
---
Typical Low Level Architecture Questions
```
````

<!-- Figure 6: Typical Low Level Architecture Questions -->


````{dropdown} Costs questions
:open:
```{figure} onto-services-figure7.svg
---
name: onto-services-figure7
alt:  Typical Low Level Costs Questions
---
 Typical Low Level Costs Questions
```
````

<!-- Figure 7: Typical Low Level Costs Questions -->


````{dropdown} Performance questions
:open:
```{figure} onto-services-figure8.svg
---
name: onto-services-figure8
alt:  Typical Low Level Performance Questions
---
 Typical Low Level Performance Questions
```
````

<!-- Figure 8: Typical Low Level Performance Questions -->


````{dropdown} Delivery questions
:open:
```{figure} onto-services-figure9.svg
---
name: onto-services-figure9
alt:  Typical Low Level Delivery Questions
---
 Typical Low Level Delivery Questions
```
````

<!-- Figure 9: Typical Low Level Delivery Questions -->


````{dropdown} Support questions
:open:
```{figure} onto-services-figure10.svg
---
name: onto-services-figure10
alt:  Typical Low Level Support Questions
---
 Typical Low Level Support Questions
```
````

<!-- Figure 10: Typical Low Level Support Questions -->

## Available  open source software

### EMBL-EBI Ontology Lookup Service

#### Overview

It is a repository for biomedical ontologies that aims to provide a single point of access to the latest ontology versions. It allows browsing the ontologies through the website as well as programmatically via the OLS API. It is part of the ELIXIR interoperability service.

#### Details

1. **Functionality**: `Ontology Portal Tool`
2. **Interface**: REST-style API supported, SPARQL endpoint under development.
3. **Architecture**: OLS has been developed with the Spring Data and Spring Boot framework.
    1. Tomcat is used as a web server.
    2. MongoDB is used for storing configuration yaml files.
    3. Neo4J node-property graph database is used for storing and accessing the ontologies. OWL format is converted to a node-property representation.
4. **Deployment model**: It is available both as an on-premises and cloud-based solution. Docker based deployment is supported.
5. **Requirements**:
    1. Hardware requirements. It requires a standard workstation, 1 GB main memory, and about 100 MB hard disk.
    2. Software requirements. It is implemented as a Java Web Application to be deployed to the Tomcat 7.5 Java Application Container. It requires Java 8, Maven 3+ as dependency manager and build environment, MongoDB 2.7.8+ as database; and solr 5.2.1+ as indexing and search engine.
    3. License model. Apache Software Licence (v. 2.0).
6. **Databases**: It supports the Neo4J graph store, which allows querying using Cypher query language. Reasoning supports two profiles: OWL2 and EL. Default is EL. The reasoners supported are HermiT and ELK.
7. **Ontology Language**: Custom translation of OBO and OWL 2 languages to the Neo4J graph model.
8. **Programming Language**: Java.

### NCBO Bioportal Virtual Appliance<!-- TODO add a link to corresponding document --> (Ontology Portal Tool)

#### Overview

The National Center for Biomedical Ontology (NCBO).

#### Details

1. **Functionality**: `Ontology Portal Tool`
2. **Interface**: REST-style API supported, SPARQL endpoint 
3. **Architecture**: Virtual Appliance defines the framework for the Web Service. The system internally uses the following components
    1. A set of additional ruby based modules that implement the user interface and additional functionality can be found [here](https://github.com/ncbo).
    2. 4Store triple store database is used to store and access ontologies. 
    3. Solr is used to create indexes out of description text metadata.  
    4. MySQL is used to store additional metadata.
    5. MGrep is used for annotating text to ontologies.
4. **Deployment model**: It is available both as an on-premises and cloud-based solution. It is available as virtual VMWare Virtual Appliance or Amazon AWS AMI. 
5. **Requirements**:
    1. Hardware requirements. 
        1. Minimum: 2 CPU (2 GHz), 4GB RAM, 20GB hard disk space.
        2. Recommended for heavier usage: 3 CPU (3 GHz), 8GB RAM (or more depending on the size/number of ontologies), 20GB hard disk space (or more depending on number/size of ontologies)
    2. Software requirements. All software is already contained in the virtual image
        1. Operating system: CentOS (Linux)
        2. License model. Apache Software Licence (v. 2.0).
6. **Databases**: It supports the 4Store triple store and MySQL
7. **Ontology Language**: OBO, OWL
8. **Programming Language**: Ruby, Java.

### [Apache Marmotta](https://marmotta.apache.org/) (Open Data Platform Tool)

#### Overview

It is an Open Data Platform for Linked Data, which provides an open implementation of 
a Linked Data Platform that can be used, extended and deployed easily by organizations who want to publish 
Linked Data or build custom applications on Linked Data {footcite}`apache_marmotta`. 
It provides:
> * a) read-write Linked Data server for the **Java EE stack** 
> * b) custom triple store built on top of RDBMS, with transactions, versioning and rule-based reasoning support
> * c) pluggable RDF triple stores based on [**Eclipse RDF4J**](https://projects.eclipse.org/projects/technology.rdf4j),
> * d) LDP, SPARQL and LD Path querying
> * e) transparent Linked Data Caching
> * f) Integrated basic security mechanisms.

```{warning}
This project is now retired and is no longer supported or developed.
```

#### Details

1. **Functionality**: `Open (Linked) Data Platform`.
2. **Interface**: REST-style API, SPARQL endpoint supported.
3. **Architecture**, the architecture comprises the following tiers:
    1. User Interface Layer. It mostly consists of admin and development interfaces and is not intended for end users.
    2. Web-service Layer. It offers REST web-services to access most of the server functionality.
    3. Service Layer. It offers CDI services to develop custom Java applications.
    4. Model Layer. It offers persistence and data access functionality.
    5. Persistence Layer. It is outside the Apache Marmotta Platform, which can use a number of Open Source database systems.
4. **Deployment Model**: It is available both as an on-premises and cloud-based solution. Docker based deployment is supported.
5. **Requirements**:
    1. Hardware requirements. It requires a standard workstation, 1 GB main memory, and about 100 MB hard disk.
    2. Software requirements. It is implemented as a Java Web Application that can, in principle, be deployed to any 
   Java Application Container. It has been tested under Jetty 6.x and Tomcat 7.x. It requires Java JDK 6 or higher,
   Java Application Server (Tomcat 7.x or Jetty 6.x), and a database (PostgreSQL, MySQL). If not explicitly configured, 
   an embedded H2 database will be used.
    3. License model. Apache Software Licence (v. 2.0).
6. **Databases**: It supports the following triple store backends: (a.) KiWi Triple Store, (b.) Sesame Native, and (c.) 
BigData triple store. The default backend is the KiWi triple store, which stores all data in a relational database, and
it is the only option that supports reasoning and versioning.
7. **Ontology Language**: OWL serialized as RDF/RDFS triples. 
8. **Programming Language**: Java.

### European Data Portal<!-- TODO add a link to corresponding document --> (Open Data Platform Tool)

#### Overview

[European data portal](https://www.europeandataportal.eu/en)  (EDP) is an initiative by 
the [Publications Office of the European Union](https://op.europa.eu/da/home) and by the [European Commission](https://ec.europa.eu/info/index_en) that aims to increase the impact of open data by making it easy to find and re-use by everyone.

It uses only open source software with extensions that are all available to the public for own use. 

As a core component,
[CKAN open data portal software](https://ckan.org/) with [DCAT-AP](https://op.europa.eu/da/web/eu-vocabularies/dcat-ap)
RDF extension is used. 

It allows sharing various data formats e.g. tabular data, RDF data (e.g. ontologies) combining
relational and semantic technologies.

The [Triple Store database Virtuoso](https://virtuoso.openlinksw.com/) is used 
for storing ontologies. 

For metadata in relational format, the [PostgreSQL](https://www.postgresql.org/) database is used as part of CKAN.

#### Details

1. **Functionality**: `Open Data Portal` 
2. **Interface**: REST-style API, SPARQL endpoint supported.
3. **Architecture**:
    1. CKAN manages and provides metadata content (datasets) in a central repository. 
    2. DRUPAL provides the Portal’s Home Page with editorial content (e.g. Portal’s objectives, articles, news, events, tweets, etc.) 
    and links to an *Adapt Framework* based training platform. 
    3. The CKAN metadata is replicated into a Virtuoso triple store database via a CKAN synchronisation extension, in order
    to ensure that both repositories have the same set of metadata. 
    4. The SPARQL Manager component allows the user to enter and run SPARQL queries on the Virtuoso linked data repository. 
    5. The portal uses the SOLR search engine in order to separately search for editorial content in DRUPAL and for 
    datasets in the CKAN repository. 
    6. The Harvester is a separate component that is able to harvest data from multiple data sources with different formats and APIs. 
4. **Deployment model**: It is available both as an on-premises and cloud-based solution.
5. **Requirements**:
    1. The setup of the EDP consists of 20 virtual servers per computer room and environment (PROD, TEST)
6. **Databases**: PostgreSQL RDBMS for CKAN catalogue, Virtuoso for RDF data
7. **Ontology Language**: RDF, RDFS, OWL 2
8. **Programming Language**: Python(CKAN), PHP(Drupal)

---
## Conclusions

Determining which infrastructure to rely on for service terminologies and ontologies is a complex issue. 

This FAIR Cookbook recipe gave an overview of non-functional criteria to take into consideration when appraising a software solution.

To complement this recipe, reading the following chapter is highly encouraged.

### What to read next?

* [Key functional requirements to consider when selecting an ontology service?](https://w3id.org/faircookbook/FCB004)
* [Deploying EMBL-EBI Ontology Lookup Service](https://w3id.org/faircookbook/FCB005)
* [Introduction to terminologies and ontologies](https://w3id.org/faircookbook/FCB019)
* [How to select an ontology?](https://w3id.org/faircookbook/FCB020)
* [How to build an application ontology?](https://w3id.org/faircookbook/FCB023)

````{rdmkit_panel}
````
## References
````{dropdown} **References**
```{footbibliography}
```
````


## Authors

````{authors_fairplus}
Kurt: Writing - Original Draft
Emiliano: Writing - Original Draft
Petros: Writing - Review & Editing
Karsten: Writing - Review & Editing
Philippe: Writing - Review & Editing
````



## License

````{license_fairplus}
CC-BY-4.0
````
