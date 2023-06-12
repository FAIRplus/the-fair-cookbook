(fcb-infra-localols)=

# Deploying the EBI OLS


````{panels_fairplus}
:identifier_text: FCB005
:identifier_link: 'https://w3id.org/faircookbook/FCB005'
:difficulty_level: 3
:recipe_type: hands_on
:reading_time_minutes: 20
:intended_audience: data_manager, data_scientist, terminology_manager, system_administrator
:maturity_level: 0
:maturity_indicator: 0
:has_executable_code: nope
:recipe_name: Deploying EBI Ontology Lookup Service 
````

## Main Objectives

This recipe is a step-by-step guide on how to deploy the EBI Ontology Lookup Service (OLS) {footcite}`pmid20460452`, {footcite}`ols_jupp` on local machines. 
This demonstrates the workflow for deploying open source ontology service software in-house {footcite}`ols-install-guide`. 

## Introduction
With an increasing need for ontology infrastructure to improve the interoperability of information-based R&D activities,
many pharmaceutical companies seek ontology management solutions and ontology services. 
Compared with developing local ontology services from scratch, reusing and redeveloping open-source ontology services
save the time and cost. [Recipe FCB003](https://w3id.org/faircookbook/FCB003) identifies public open-source ontology services. 
In this recipe, we use the [Ontology Lookup Service](https://www.ebi.ac.uk/ols/index) to demonstrate the workflow of 
deploying public ontology services in-house.

Ontology Lookup Service is an open-source ontology management service developed by [EMBL-EBI](https://www.ebi.ac.uk/).

It is a repository for biomedical ontologies, and serves as a single point of access to query, browse and navigate
different ontologies. 

OLS supports the [Open Biological and Biomedical Ontology (OBO) Foundry](http://www.obofoundry.org/)
guidelines and connects with other ontology services. 

It provides both web interface and API to search and browser 
ontologies. 
[Recipe FCB003](https://w3id.org/faircookbook/FCB003) provides a detailed description of OLS.

A local OLS allows users to protect and control their ontology-related data, and make stable and fast access to ontology
services possible. 

It can serve as the hub of internal ontology eco-system, linking internal vocabulary, 
terminology management and data annotation activities together to improve the interoperability.

## Requirements
This recipe is intended for bioinformaticians or developers who want to explore public ontologies and ontology services. 
The users are expected to be familiar with Unix-based OS and basic Bash programming syntax and commands. 
The users should also be comfortable with YAML or other data-serialization languages. 
Knowledge about [Docker](https://www.docker.com/) allows users to further customize their local service.

This recipe can also be applied by organizational users. 

```{warning}
* Make sure to comply with good cyber security practices and talk to local IT departments and support staff about
specific policies regarding tool deployment the use of containerized applications, proxy settings, and firewalls.
```

## Graphical overview

````{dropdown}
:open:
```{figure} ols-deploy.svg
---
name: ols-deploy
alt: Deploying EMBL-EBI OLS
---
Deploying EMBL-EBI Ontology Lookup Service
```
````
 
## Ingredients
- [OLS Docker image](https://github.com/EBISPOT/OLS-docker) 
- [Ontology metadata in OBO foundry](https://github.com/OBOFoundry/purl.obolibrary.org/tree/master/config)

## Step-by-step guide

### 1. Install dependencies


```{tabbed} Unix-based environment (macOS, Linux)
|Software|Description|Version|Installation|
|--|--|--|--|
|Git|Get the versioned source file|2.17.1 |[Official guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)|
|Docker|Deliver software in containers|18.09.01 |[Official guide](https://docs.docker.com/install/)|
```

```{tabbed} Windows-based environment (Windows 10 64bits)
|Software|Description|Version|Installation|
|--|--|--|--|
|Git|Get the versioned source file|2.26.2.windows.1|[Official guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)|
|Docker Desktop|Deliver software in containers|2.2.0.5 (Engine v.19.03.8)|[Official guide](https://docs.docker.com/install/)|
|PowerShell|Execute commands| 5.1.17763(Desktop Edition)|[Official Guide](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7)|

```



```{note}
This recipe was developed on a Unix-based environment and tested on Linux and macOS machines.

Minor modifications are required to run it on Windows machines.
```

### 2. Load ontologies into OLS 

Ontologies in both [OBO](https://fairsharing.org/10.25504/FAIRsharing.aa0eat) and
[OWL](https://fairsharing.org/10.25504/FAIRsharing.atygwy) formats can be loaded to OLS by adding ontology
metadata to the configuration file, **ols-config.yaml**. 

Three fields, **id**,**url** and **ontology_purl** are mandatory ontology metadata attributes.

Other fields are also recommended, especially for self-defined ontologies. 

Below is an example configuration of the Experimental Factor Ontology (EFO) provided
by [OLS](https://www.ebi.ac.uk/ols/docs/installation-guide). 

```bash
## EFO
# * are required fields
id: efo // short unique id for the ontology *
preferredPrefix: EFO // preferred display name for the ontology
title: Experimental Factor Ontology // Short title of the ontology
uri: http://www.ebi.ac.uk/efo // The ontology URI * description: "The Experimental Factor Ontology (EFO) provides a…" // Full ontology description
ontology_purl: http://www.ebi.ac.uk/efo/efo.owl // URL to get the ontology from *
homepage: http://www.ebi.ac.uk/efo // homepage of the ontology
mailing_list: efo-users@lists.sourceforge.net // assocaited mailing list
definition_property: // predicates that are used for term definitions
 - http://www.ebi.ac.uk/efo/definition
synonym_property: // prediates used for synonyms
 - http://www.ebi.ac.uk/efo/alternative_term
hierarchical_property: // predicates that are hierarchical (like part of) will be included in default tree view
 - http://purl.obolibrary.org/obo/BFO_0000050
 - http://purl.obolibrary.org/obo/RO_0002202
hidden_property: // any predicates that should be ignored when indexing
 - http://www.ebi.ac.uk/efo/has_flag
base_uri: // base URIs for local terms
 - http://www.ebi.ac.uk/efo/EFO_
reasoner: OWL2 // can be one of OWL2, EL, NONE - deafult is EL
oboSlims: false // contains OBO style slim annotations
```

The location of the target ontology shall be specified in the **ontology_purl** field in the **`ols-config.yaml** file.

Ontologies from both local files and online resources can be imported. 

To add local ontologies, the ontology files need to be first copied to the **OLS-docker** directory. 

By default, the ontology file location is specified as **/opt/ols/example.owl**. 

For example, **ontology_purl:file:///opt/ols/example.owl**.

To add ontologies from online resources, ontology URLs are required.

Most reference ontologies use the OBO foundry Permanent URLs (PURLs). 

The PURLs can be found [here](http://www.obofoundry.org/). 

For example, the location of Data Usage Ontology (DUO) can be specified by adding:

```
ontology_purl: http://purl.obolibrary.org/obo/duo.owl
```

to the configuration file. 

Ontology metadata for the configuration file can be written by users. 

For common public ontologies, the ontology metadata can also be downloaded from either the 
[EBI OLS](https://www.ebi.ac.uk/ols/index) or the [OBO Foundry](https://obofoundry.org/) {footcite}`pmid17989687obofoundry2007`,
{footcite}`pmid34697637obofoundry2021` .

#### 2.1 Get ontology metadata from the EBI OLS

For ontologies included in the EBI OLS, the metadata can be downloaded directly using the EBI OLS endpoint,
**https://www.ebi.ac.uk/ols/api/ols-config\?ids\=<ontologies-short-names-list>**, by providing the ontology short names.

Metadata of multiple ontologies can be downloaded at the same time.

[Here](https://www.ebi.ac.uk/ols/ontologies) is a list of all the ontologies available at OLS, along with their
respective "short name" and other information. 

For example, the following command downloads the ontology metadata of EFO and Adverse Event Reporting Ontology (AERO) 
and saves it as **ols-config.yaml**:

```{warning}
- The command overwrites the original **ols-config.yml** file and **removes** pre-loaded ontologies.

- On Windows systems, make sure to wrap the url with quotes, e.g.***"<URL>"***.
```



```shell
wget -O ols-config.yaml https://www.ebi.ac.uk/ols/api/ols-config\?ids\=aero,efo
```
To avoid losing pre-loaded ontologies, the metadata of EFO and AERO can also be appended to the already existing **ols-config.yml** using:

```shell
wget -O - https://www.ebi.ac.uk/ols/api/ols-config\?ids\=efo,aero >> ols-config.yaml
```

```{warning}
>:warning: The file needs to be manually edited by removing the header of the new metadata and adding proper indentation.
```

For ontologies that are in the OBO foundry, the metadata can also be downloaded from the [OBO Foundry GitHub repository](https://github.com/OBOFoundry/purl.obolibrary.org/tree/master/config).

Additional formatting is required for metadata downloaded from the OBO foundry.

### 3. Set up OLS in the local environment 

**First be sure the Docker daemon is up running. On Windows and MacOS set-ups, this requires starting the Docker Desktop app.**


```shell
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

### 4. Manage ontologies
OLS allows the addition, update, and removal of ontologies.

Such ontology management is achieved through editing the configuration file, **ols-config.yaml**. 

The ontology changes can be loaded by rebuilding the image and restarting the service.

#### 4.1 Modify OLS configuration

To add or remove ontologies, modify corresponding sections in the configuration file.

Loaded ontologies will be updated to the latest version automatically by rebuilding the Docker image. 

#### 4.2 Rebuild OLS image and restart OLS 
Before rebuilding the Docker image, the existing container needs to be stopped and removed. 

The OLS container can be stopped and removed by providing the container name. 

According to the parameters presented on the previous Docker creation command block, 
the name of the OLS Docker container is "OLS": 

```{warning}
By rebuilding the OLS image, all loaded ontologies will be automatically updated to the latest version.
```

```shell
## Stop OLS container
docker stop OLS

## Remove OLS container
docker rm OLS
```

The Docker container can also be stopped and removed using the Docker image ID.

The previous Docker image shall also be removed before rebuilding the image.

```shell
## Remove previous docker image
sudo docker rmi ols
```

To rebuild the Docker image, repeat the commands in Step 3.

```shell
## Build OLS docker image
sudo docker build -t ols .

## Run OLS docker image at port 8080
sudo docker run -d -p 8080:8080 --name=OLS -t ols
```

### Troubleshooting

Loading multiple ontologies from disk:
    
If more than one ontology are going to be loaded into OLS from disk, the **Dockerfile** needs modifying before 
building the Docker container again:

* At Line 3 of the configuration file, replace **ENV OLS_HOME /opt/ols** with **ENV OLS_HOME /opt/ols/**

* At Line 3 of the configuration file, replace

    ```bash
    && java -Dols.obofoundry.ontology.config=foo.yaml -Dols.ontology.config=file://${OLS_HOME}/ols-config.yaml -jar ${OLS_HOME}/ols-config-importer.jar
    ```
    
    with:

    ```bash
    && java -Dols.obofoundry.ontology.config=foo.yaml -Dols.ontology.config=file://${OLS_HOME}ols-config.yaml -jar ${OLS_HOME}ols-config-importer.jar
    ```
    
## Conclusion
The local OLS provides API endpoints for retrieving, submitting, updating, and querying ontology data, as well as a 
user interface for searching and browsing ontologies and ontology terms.

For example, all ontologies loaded can be queried through endpoint **http://localhost:8080/api/ontologies**.

A detailed description of OLS functions can be found in the built-in documentation page.

To customize the local OLS user interface, for example, adding corporate logos, please check the OLS source code
[here](https://github.com/EBISPOT/OLS). 

---

<!--
## Reference
* [Documentation < Ontology Lookup Service < EMBL-EBI. Accessed 20 April 2020.](https://www.ebi.ac.uk/ols/docs/installation-guide)
* [Jupp S. et al. (2015) A new Ontology Lookup Service at EMBL-EBI. In: Malone, J. et al. (eds.) Proceedings of SWAT4LS International Conference 2015](https://conferences.ncl.ac.uk/media/sites/conferencewebsites/ukon2016/UKON_2016_paper_9.pdf)
* [Côté, Richard G., et al. "The Ontology Lookup Service, a lightweight cross-platform tool for controlled vocabulary queries." BMC bioinformatics 7.1 (2006): 97.](https://link.springer.com/article/10.1186/1471-2105-7-97)
-->


## References
````{dropdown} **References**
```{footbibliography}
```
````

## Authors

````{authors_fairplus}
Fuqi: Writing - Original Draft
Eva: Writing - Original Draft
Emiliano: Writing - Review & Editing
Philippe: Writing - Review & Editing
````


## License

````{license_fairplus}
CC-BY-4.0
````
