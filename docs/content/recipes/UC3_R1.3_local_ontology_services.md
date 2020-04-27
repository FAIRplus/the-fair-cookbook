# Recipe 1.3: How to deploy the service internally: an example with the EBI Ontology Lookup Service

[TOC]

## Main Objectives

This recipe is a step-by-step guide on how to deploy the EBI Ontology Lookup Service(OLS) on local machines. This demonstrates the workflow for deploying open source ontology service softwares in-house. 

## Ingredients
- [OLS Docker image](https://github.com/EBISPOT/OLS-docker) 
- [OLS Documentation: Build a local version of OLS(without Docker)](https://www.ebi.ac.uk/ols/docs/installation-guide)
- [Ontology metadata in OBO foundry](https://github.com/OBOFoundry/purl.obolibrary.org/tree/master/config)

### Introduction
With an increasing need for ontology infrastructure to improve the interoperability of information-based R&D activities, many pharmaceutical companies seek ontology management solutions and ontology services. Compared with developing local ontology services from scratch, reusing and redeveloping open-source ontology services save the time and cost. __Recipe 3.1__ identifies public open-source ontology services. In this recipe, we use the [Ontology Lookup Service](https://www.ebi.ac.uk/ols/index) to demonstrate the workflow of deploying public ontology services in-house.

Ontology Lookup Service is an open-source ontology management service developed by [EMBL-EBI](https://www.ebi.ac.uk/). It is a repository for biomedical ontologies, and serves as a single point of access to query, browser and navigates different ontologies. OLS supports the [Open Biological and Biomedical Ontology (OBO) Foundry](http://www.obofoundry.org/) guidelines and connects with other ontology services. It provides both web interface and API to search and browser ontologies. __Recipe 3.1__ provides a detailed description of OLS.

A local OLS allows users to protect and control their ontology-related data, and make stable and fast access to ontology services possible. It can serve as the hub of internal ontology eco-system, linking internal vocabulary and terminology management, data annotation activities together to improve the interoperability.

### Requirements
This recipe is intended for bioinformaticians or developers who wants to explore public ontologies and ontology services. The users are expected to be familiar with Unix-based OS and basic Bash programming syntax and commands. The users should also be comfortable with YAML or other data-serialization languages. 

Knowledge about [Docker](https://www.docker.com/) allows users to further customize their local service.

## Graphic view

graph TD
    A[Install dependencies] --> B[Import ontologies]
    B--> C[Set up local OLS] 
    C--> D[Start local OLS service]
    D --> E[Add new ontologies from OLS]
    E --> D

    subgraph Get ontology resources
    G(From the online sources)
    F(From local files)
    end

    G -.-> B
    F -.-> B

style G fill:yellow
style F fill:yellow

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBW0luc3RhbGwgZGVwZW5kZW5jaWVzXSAtLT4gQltJbXBvcnQgb250b2xvZ2llc11cbiAgICBCLS0-IENbU2V0IHVwIGxvY2FsIE9MU10gXG4gICAgQy0tPiBEW1N0YXJ0IGxvY2FsIE9MUyBzZXJ2aWNlXVxuICAgIEQgLS0-IEVbQWRkIG5ldyBvbnRvbG9naWVzIGZyb20gT0xTXVxuICAgIEUgLS0-IERcblxuICAgIHN1YmdyYXBoIEdldCBvbnRvbG9neSByZXNvdXJjZXNcbiAgICBHKEZyb20gdGhlIG9ubGluZSBzb3VyY2VzKVxuICAgIEYoRnJvbSBsb2NhbCBmaWxlcylcbiAgICBlbmRcblxuICAgIEcgLS4tPiBCXG4gICAgRiAtLi0-IEJcblxuc3R5bGUgRyBmaWxsOnllbGxvd1xuc3R5bGUgRiBmaWxsOnllbGxvd1xuXG5cbiAgICAiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBW0luc3RhbGwgZGVwZW5kZW5jaWVzXSAtLT4gQltJbXBvcnQgb250b2xvZ2llc11cbiAgICBCLS0-IENbU2V0IHVwIGxvY2FsIE9MU10gXG4gICAgQy0tPiBEW1N0YXJ0IGxvY2FsIE9MUyBzZXJ2aWNlXVxuICAgIEQgLS0-IEVbQWRkIG5ldyBvbnRvbG9naWVzIGZyb20gT0xTXVxuICAgIEUgLS0-IERcblxuICAgIHN1YmdyYXBoIEdldCBvbnRvbG9neSByZXNvdXJjZXNcbiAgICBHKEZyb20gdGhlIG9ubGluZSBzb3VyY2VzKVxuICAgIEYoRnJvbSBsb2NhbCBmaWxlcylcbiAgICBlbmRcblxuICAgIEcgLS4tPiBCXG4gICAgRiAtLi0-IEJcblxuc3R5bGUgRyBmaWxsOnllbGxvd1xuc3R5bGUgRiBmaWxsOnllbGxvd1xuXG5cbiAgICAiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)


## Step by step guide:

### 1. Installing dependencies

__Unix-based environment:__
|Software|Description|Version|Installation|
|--|--|--|--|
|Git|Get the versioned source file|2.17.1 |[Official guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)|
|Docker|Deliver software in containers|18.09.01 |[Official guide](https://docs.docker.com/install/)|

__Windows-based enviroment (Windows 10,64bits):__
|Software|Description|Version|Installation|
|--|--|--|--|
|Git|Get the versioned source file|2.26.2.windows.1|[Official guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)|
|Docker Desktop|Deliver software in containers|2.2.0.5 (Engine v.19.03.8)|[Official guide](https://docs.docker.com/install/)|
|PowerShell|Excute commands| 5.1.17763(Desktop Edition)|[Official Guide](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7)|

### 2. Loading ontologies into OLS 

Ontologies in both [OBO](https://fairsharing.org/10.25504/FAIRsharing.aa0eat) and [OWL](https://fairsharing.org/10.25504/FAIRsharing.atygwy) formats can be loaded to OLS by adding ontology metadata to the configuration file, `ols-config.yaml`. Three fields, `id`,`url` and `ontology_purl` are mandatory ontology metadata attributes. Other fields are also recommended, especially for self-defined ontologies. Below is an example configuration of the Experimental Factor Ontology (EFO) provided by [OLS](https://www.ebi.ac.uk/ols/docs/installation-guide). 

```yaml
## EFO
# * are required fields
    id: efo // short unique id for the ontology *
    preferredPrefix: EFO // preferred display name for the ontology
    title: Experimental Factor Ontology // Short title of the ontology
    uri: http://www.ebi.ac.uk/efo // The ontology URI * description: "The Experimental Factor Ontology (EFO) provides a…​" // Full ontology description
    ontology_purl: http://www.ebi.ac.uk/efo/efo.owl // URL to get the ontology from *
    homepage: http://www.ebi.ac.uk/efo // homepage of the ontology
    mailing_list: efo-users@lists.sourceforge.net // assocaited mailing list
    definition_property: // predicates that are used for term definitions
     — http://www.ebi.ac.uk/efo/definition
    synonym_property: // prediates used for synonyms
     — http://www.ebi.ac.uk/efo/alternative_term
    hierarchical_property: // predicates that are hierarchical (like part of) will be included in default tree view
     — http://purl.obolibrary.org/obo/BFO_0000050
     — http://purl.obolibrary.org/obo/RO_0002202
    hidden_property: // any predicates that should be ignored when indexing
     — http://www.ebi.ac.uk/efo/has_flag
    base_uri: // base URIs for local terms
     — http://www.ebi.ac.uk/efo/EFO_
    reasoner: OWL2 // can be one of OWL2, EL, NONE - deafult is EL
    oboSlims: false // contains OBO style slim annotations
```

The location of the target ontology shall be specified in the `ontology_purl` field in the `ols-config.yaml` file. Ontologies from both local files and online resources can be imported. 

To add local ontologies, the ontology files need to be first copied to the `OLS-docker` directory. By default, the ontology file location is specificed a as`/opt/ols/example.owl`. For example,  `ontology_purl:file:///opt/ols/example.owl`:




To add ontologies from online resources, Ontology URLs are required. Most reference ontologies use the OBO foundry Permanent URLs (PURLs). The PURLs can be found [here](http://www.obofoundry.org/). For example, the location of Data Usage Ontology (DUO) can be specified by adding `ontology_purl: http://purl.obolibrary.org/obo/duo.owl` to the configuration file. 

Ontology metadata for the configuration file can be written by users. For common public ontologies, the ontology metadata can also be downloaded from either the EBI OLS or the OBO Foundry.

#### 2.1 Getting ontology metadata from the EBI OLS

For ontologies included in the EBI OLS, the metadata can be downloaded directly using the the EBI OLS endpoint, `https://www.ebi.ac.uk/ols/api/ols-config\?ids\=<ontologies-short-names-list>`, by providing the ontology short names. Metadata of multiple ontologies can be downloaded at the same time.  [Here](https://www.ebi.ac.uk/ols/ontologies) is a list of all the ontologies available at OLS, along with their respective "short name" and other information. 

For example, the following command downloads the ontologies metadata of *EFO* and *Adverse Event Reporting Ontology(AERO)* and saves it as `ols-config.yaml`:

>:warning: The command overwrites the original `ols-config.yml` file and removes pre-loaded ontologies.

```shell
wget -O ols-config.yaml https://www.ebi.ac.uk/ols/api/ols-config\?ids\=aero,efo
```
To avoid losing pre-loaded ontologies, the metadata of EFO and AERO can also be append to the already existing `ols-config.yml` using:
```shell
wget -O - https://www.ebi.ac.uk/ols/api/ols-config\?ids\=efo,aero >> ols-config.yaml
```
>:warning: The file needs to be manually edited by removing the header of the new metadata and adding proper indentation.


For ontologies that are in the OBO foundry, the metadata can also be downloaded from the [OBO Foundry GitHub repository](https://github.com/OBOFoundry/purl.obolibrary.org/tree/master/config). Additional formatting is required for metadata downloaded from the OBO foundry.

### 3. Set up OLS in the local environment 

```sh
## Download OLS docker image
git clone https://github.com/EBISPOT/OLS-docker
cd OLS-docker

##  Start docker
sudo snap services
sudo snap start docker

## Build OLS docker image
sudo docker build -t ols .

## Run OLS docker image at port 8080
sudo docker run -d -p 8080:8080 --name=OLS -t ols
```

The local OLS service can be accessed at http://localhost:8080/index 

### 4. Adding new ontologies to OLS

To add new ontologies to OLS, the new ontology metadata should be added to file `ols-config.yml`. It is essential to rebuild the OLS docker image to load new ontologies.

Before rebuilding the docker image, the existing container needs to be stoped and removed. The OLS container can be removed by providing the container name. By default, the name of the OLS docker container is "OLS": 
```shell
## Stop OLS container
docker stop OLS

## Remove OLS container
docker rm OLS
``` 
The docker container can also be stopped with the Docker image ID.

To rebuild the docker image, the commands are the same as those in Step 3.

```shell
## Build OLS docker image
sudo docker build -t ols .

## Run OLS docker image at port 8080
sudo docker run -d -p 8080:8080 --name=OLS -t ols
```
## Troubleshooting
- Loading multiple ontologies from disk
    
    If more than one ontologies are going to be loaded into OLS from disk, the `Dockerfile` need modified before building the docker container:

    In line 3, replace `ENV OLS_HOME /opt/ols` with `ENV OLS_HOME /opt/ols/`
    
    In line 14, replace 
    > && java -Dols.obofoundry.ontology.config=foo.yaml -Dols.ontology.config=file://${OLS_HOME}/ols-config.yaml -jar ${OLS_HOME}/ols-config-importer.jar \
    
    with 
    >&& java -Dols.obofoundry.ontology.config=foo.yaml -Dols.ontology.config=file://${OLS_HOME}ols-config.yaml -jar ${OLS_HOME}ols-config-importer.jar \
    
    

## Summary
The local OLS provides API endpoints for retrieving, submitting, updating, and querying ontology data, as well as a user interface for searching and browsing ontology and ontology terms. Detailed description of OLS functions can be found in the built-in documenation page. 


## Authors
|Name|Institute|ORCID|Contributions|
|--|--|--|--|
|Fuqi Xu|[EMBL-EBI](https://www.ebi.ac.uk/)|[0000-0002-5923-3859](https://orcid.org/0000-0002-5923-3859)|Writing - Original Draft|
|Eva Martin | [Barcelona Supercomputing Center (BSC)](https://www.bsc.es/) |[0000-0001-8324-2897](https://orcid.org/0000-0001-8324-2897)|Writing - Original Draft |
Emiliano Reynares|[Boehringer Ingelheim](https://www.boehringer-ingelheim.com/)|[0000-0002-5109-3716](https://orcid.org/0000-0002-5109-3716)|Reviewing|

## License

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>

## Reference
* [Côté, Richard G., et al. "The Ontology Lookup Service, a lightweight cross-platform tool for controlled vocabulary queries." BMC bioinformatics 7.1 (2006): 97.](https://link.springer.com/article/10.1186/1471-2105-7-97)