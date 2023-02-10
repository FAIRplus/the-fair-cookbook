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

This recipe is a step-by-step guide on how to deploy the EBI Ontology (URL_TO_INSERT_TERM_2480 https://fairsharing.org/search?recordType=terminology_artefact)  Lookup Service (URL_TO_INSERT_RECORD-NAME_2481 https://fairsharing.org/FAIRsharing.Mkl9RR)  (OLS (URL_TO_INSERT_RECORD-ABBREV_2482 https://fairsharing.org/FAIRsharing.Mkl9RR) ) {footcite}`pmid20460452`, {footcite}`ols_jupp` on local machines. 
This demonstrates the workflow for deploying open source ontology (URL_TO_INSERT_TERM_2483 https://fairsharing.org/search?recordType=terminology_artefact)  service software in-house {footcite}`ols-install-guide`. 

## Introduction
With an increasing need for ontology (URL_TO_INSERT_TERM_2485 https://fairsharing.org/search?recordType=terminology_artefact)  infrastructure to improve the interoperability of informat (URL_TO_INSERT_TERM_2484 https://fairsharing.org/search?recordType=model_and_format) ion-based R&D activities,
many pharmaceutical companies seek ontology (URL_TO_INSERT_TERM_2486 https://fairsharing.org/search?recordType=terminology_artefact)  management solutions and ontology (URL_TO_INSERT_TERM_2487 https://fairsharing.org/search?recordType=terminology_artefact)  services. 
Compared with developing local ontology (URL_TO_INSERT_TERM_2488 https://fairsharing.org/search?recordType=terminology_artefact)  services from scratch, reusing and redeveloping open-source ontology (URL_TO_INSERT_TERM_2489 https://fairsharing.org/search?recordType=terminology_artefact)  services
save the time and cost. [Recipe FCB003](https://w3id.org/faircookbook/FCB003) identifies public open-source ontology (URL_TO_INSERT_TERM_2490 https://fairsharing.org/search?recordType=terminology_artefact)  services. 
In this recipe, we use the [Ontology Lookup Service](https://www.ebi.ac.uk/ols/index) to demonstrate the workflow of 
deploying public ontology (URL_TO_INSERT_TERM_2491 https://fairsharing.org/search?recordType=terminology_artefact)  services in-house.

Ontology (URL_TO_INSERT_TERM_2492 https://fairsharing.org/search?recordType=terminology_artefact)  Lookup Service (URL_TO_INSERT_RECORD-NAME_2494 https://fairsharing.org/FAIRsharing.Mkl9RR)  is an open-source ontology (URL_TO_INSERT_TERM_2493 https://fairsharing.org/search?recordType=terminology_artefact)  management service developed by [EMBL-EBI](https://www.ebi.ac.uk/).

It is a repository (URL_TO_INSERT_TERM_2495 https://fairsharing.org/search?recordType=repository)  for biomedical ontologies (URL_TO_INSERT_TERM_2496 https://fairsharing.org/search?recordType=terminology_artefact) , and serves as a single point of access to query, browse and navigate
different ontologies (URL_TO_INSERT_TERM_2497 https://fairsharing.org/search?recordType=terminology_artefact) . 

OLS (URL_TO_INSERT_RECORD-ABBREV_2498 https://fairsharing.org/FAIRsharing.Mkl9RR)  supports the [Open Biological and Biomedical Ontology (OBO) Foundry](http://www.obofoundry.org/)
guideline (URL_TO_INSERT_TERM_2500 https://fairsharing.org/search?recordType=reporting_guideline) s and connects with other ontology (URL_TO_INSERT_TERM_2499 https://fairsharing.org/search?recordType=terminology_artefact)  services. 

It provides both web interface and API to search and browser 
ontologies (URL_TO_INSERT_TERM_2501 https://fairsharing.org/search?recordType=terminology_artefact) . 
[Recipe FCB003](https://w3id.org/faircookbook/FCB003) provides a detailed description of OLS (URL_TO_INSERT_RECORD-ABBREV_2502 https://fairsharing.org/FAIRsharing.Mkl9RR) .

A local OLS (URL_TO_INSERT_RECORD-ABBREV_2505 https://fairsharing.org/FAIRsharing.Mkl9RR)  allows users to protect and control their ontology (URL_TO_INSERT_TERM_2503 https://fairsharing.org/search?recordType=terminology_artefact) -related data, and make stable and fast access to ontology (URL_TO_INSERT_TERM_2504 https://fairsharing.org/search?recordType=terminology_artefact) 
services possible. 

It can serve as the hub of internal ontology (URL_TO_INSERT_TERM_2506 https://fairsharing.org/search?recordType=terminology_artefact)  eco-system, linking internal vocabulary, 
terminology (URL_TO_INSERT_TERM_2507 https://fairsharing.org/search?recordType=terminology_artefact)  management and data annotation activities together to improve the interoperability.

## Requirements
This recipe is intended for bioinformat (URL_TO_INSERT_TERM_2508 https://fairsharing.org/search?recordType=model_and_format) icians or developers who want to explore public ontologies (URL_TO_INSERT_TERM_2510 https://fairsharing.org/search?recordType=terminology_artefact)  and ontology (URL_TO_INSERT_TERM_2509 https://fairsharing.org/search?recordType=terminology_artefact)  services. 
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
alt: Deploying EMBL-EBI OLS (URL_TO_INSERT_RECORD-ABBREV_2511 https://fairsharing.org/FAIRsharing.Mkl9RR) 
---
Deploying EMBL-EBI Ontology (URL_TO_INSERT_TERM_2512 https://fairsharing.org/search?recordType=terminology_artefact)  Lookup Service (URL_TO_INSERT_RECORD-NAME_2513 https://fairsharing.org/FAIRsharing.Mkl9RR) 
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

Ontologies (URL_TO_INSERT_TERM_2514 https://fairsharing.org/search?recordType=terminology_artefact)  in both [OBO](https://fairsharing.org/10.25504/FAIRsharing.aa0eat) and
[OWL](https://fairsharing.org/10.25504/FAIRsharing.atygwy) format (URL_TO_INSERT_TERM_2515 https://fairsharing.org/search?recordType=model_and_format) s can be loaded to OLS (URL_TO_INSERT_RECORD-ABBREV_2517 https://fairsharing.org/FAIRsharing.Mkl9RR)  by adding ontology (URL_TO_INSERT_TERM_2516 https://fairsharing.org/search?recordType=terminology_artefact) 
metadata to the configuration file, **ols-config.yaml**. 

Three fields, **id**,**url** and **ontology (URL_TO_INSERT_TERM_2518 https://fairsharing.org/search?recordType=terminology_artefact) _purl** are mandatory ontology (URL_TO_INSERT_TERM_2519 https://fairsharing.org/search?recordType=terminology_artefact)  metadata attributes.

Other fields are also recommended, especially for self-defined ontologies (URL_TO_INSERT_TERM_2520 https://fairsharing.org/search?recordType=terminology_artefact) . 

Below is an example configuration of the Experimental Factor Ontology (URL_TO_INSERT_TERM_2521 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD-NAME_2522 https://fairsharing.org/FAIRsharing.1gr4tz)  (EFO (URL_TO_INSERT_RECORD-ABBREV_2523 https://fairsharing.org/FAIRsharing.1gr4tz) ) provided
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

The location of the target ontology (URL_TO_INSERT_TERM_2524 https://fairsharing.org/search?recordType=terminology_artefact)  shall be specified in the **ontology (URL_TO_INSERT_TERM_2525 https://fairsharing.org/search?recordType=terminology_artefact) _purl** field in the **`ols-config.yaml** file.

Ontologies (URL_TO_INSERT_TERM_2526 https://fairsharing.org/search?recordType=terminology_artefact)  from both local files and online resources can be imported. 

To add local ontologies (URL_TO_INSERT_TERM_2528 https://fairsharing.org/search?recordType=terminology_artefact) , the ontology (URL_TO_INSERT_TERM_2527 https://fairsharing.org/search?recordType=terminology_artefact)  files need to be first copied to the **OLS (URL_TO_INSERT_RECORD-ABBREV_2529 https://fairsharing.org/FAIRsharing.Mkl9RR) -docker** directory. 

By default, the ontology (URL_TO_INSERT_TERM_2530 https://fairsharing.org/search?recordType=terminology_artefact)  file location is specified as **/opt/ols/example.owl**. 

For example, **ontology (URL_TO_INSERT_TERM_2531 https://fairsharing.org/search?recordType=terminology_artefact) _purl:file:///opt/ols/example.owl**.

To add ontologies (URL_TO_INSERT_TERM_2533 https://fairsharing.org/search?recordType=terminology_artefact)  from online resources, ontology (URL_TO_INSERT_TERM_2532 https://fairsharing.org/search?recordType=terminology_artefact)  URLs are required.

Most reference ontologies (URL_TO_INSERT_TERM_2534 https://fairsharing.org/search?recordType=terminology_artefact)  use the OBO foundry (URL_TO_INSERT_RECORD-NAME_2535 https://fairsharing.org/FAIRsharing.847069)  Permanent URLs (PURLs). 

The PURLs can be found [here](http://www.obofoundry.org/). 

For example, the location of Data Usage Ontology (URL_TO_INSERT_TERM_2536 https://fairsharing.org/search?recordType=terminology_artefact)  (DUO (URL_TO_INSERT_RECORD-ABBREV_2537 https://fairsharing.org/FAIRsharing.5dnjs2) ) can be specified by adding:

```
ontology_purl: http://purl.obolibrary.org/obo/duo.owl
```

to the configuration file. 

Ontology (URL_TO_INSERT_TERM_2538 https://fairsharing.org/search?recordType=terminology_artefact)  metadata for the configuration file can be written by users. 

For common public ontologies (URL_TO_INSERT_TERM_2540 https://fairsharing.org/search?recordType=terminology_artefact) , the ontology (URL_TO_INSERT_TERM_2539 https://fairsharing.org/search?recordType=terminology_artefact)  metadata can also be downloaded from either the 
[EBI OLS](https://www.ebi.ac.uk/ols/index) or the [OBO Foundry (URL_TO_INSERT_RECORD-NAME_2541 https://fairsharing.org/FAIRsharing.847069) ](https://obofoundry.org/) {footcite}`pmid17989687obofoundry2007`,
{footcite}`pmid34697637obofoundry2021` .

#### 2.1 Get ontology metadata from the EBI OLS

For ontologies (URL_TO_INSERT_TERM_2542 https://fairsharing.org/search?recordType=terminology_artefact)  included in the EBI OLS (URL_TO_INSERT_RECORD-ABBREV_2543 https://fairsharing.org/FAIRsharing.Mkl9RR) , the metadata can be downloaded directly using the EBI OLS (URL_TO_INSERT_RECORD-ABBREV_2544 https://fairsharing.org/FAIRsharing.Mkl9RR)  endpoint,
**https://www.ebi.ac.uk/ols/api/ols-config\?ids\=<ontologies-short-names-list>**, by providing the ontology (URL_TO_INSERT_TERM_2545 https://fairsharing.org/search?recordType=terminology_artefact)  short names.

Metadata of multiple ontologies (URL_TO_INSERT_TERM_2546 https://fairsharing.org/search?recordType=terminology_artefact)  can be downloaded at the same time.

[Here](https://www.ebi.ac.uk/ols/ontologies) is a list of all the ontologies (URL_TO_INSERT_TERM_2547 https://fairsharing.org/search?recordType=terminology_artefact)  available at OLS (URL_TO_INSERT_RECORD-ABBREV_2548 https://fairsharing.org/FAIRsharing.Mkl9RR) , along with their
respective "short name" and other informat (URL_TO_INSERT_TERM_2549 https://fairsharing.org/search?recordType=model_and_format) ion. 

For example, the following command downloads the ontology (URL_TO_INSERT_TERM_2550 https://fairsharing.org/search?recordType=terminology_artefact)  metadata of EFO (URL_TO_INSERT_RECORD-ABBREV_2552 https://fairsharing.org/FAIRsharing.1gr4tz)  and Adverse Event Reporting Ontology (URL_TO_INSERT_TERM_2551 https://fairsharing.org/search?recordType=terminology_artefact)  (AERO) 
and saves it as **ols-config.yaml**:

```{warning}
- The command overwrites the original **ols-config.yml** file and **removes** pre-loaded ontologies.

- On Windows systems, make sure to wrap the url with quotes, e.g.***"<URL>"***.
```



```shell
wget -O ols-config.yaml https://www.ebi.ac.uk/ols/api/ols-config\?ids\=aero,efo
```
To avoid losing pre-loaded ontologies (URL_TO_INSERT_TERM_2553 https://fairsharing.org/search?recordType=terminology_artefact) , the metadata of EFO (URL_TO_INSERT_RECORD-ABBREV_2554 https://fairsharing.org/FAIRsharing.1gr4tz)  and AERO can also be appended to the already existing **ols-config.yml** using:

```shell
wget -O - https://www.ebi.ac.uk/ols/api/ols-config\?ids\=efo,aero >> ols-config.yaml
```

```{warning}
>:warning: The file needs to be manually edited by removing the header of the new metadata and adding proper indentation.
```

For ontologies (URL_TO_INSERT_TERM_2555 https://fairsharing.org/search?recordType=terminology_artefact)  that are in the OBO foundry (URL_TO_INSERT_RECORD-NAME_2556 https://fairsharing.org/FAIRsharing.847069) , the metadata can also be downloaded from the [OBO Foundry GitHub repository](https://github.com/OBOFoundry/purl.obolibrary.org/tree/master/config).

Additional format (URL_TO_INSERT_TERM_2557 https://fairsharing.org/search?recordType=model_and_format) ting is required for metadata downloaded from the OBO foundry (URL_TO_INSERT_RECORD-NAME_2558 https://fairsharing.org/FAIRsharing.847069) .

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

The local OLS (URL_TO_INSERT_RECORD-ABBREV_2559 https://fairsharing.org/FAIRsharing.Mkl9RR)  service can be accessed at http://localhost:8080/index 

### 4. Manage ontologies
OLS (URL_TO_INSERT_RECORD-ABBREV_2561 https://fairsharing.org/FAIRsharing.Mkl9RR)  allows the addition, update, and removal of ontologies (URL_TO_INSERT_TERM_2560 https://fairsharing.org/search?recordType=terminology_artefact) .

Such ontology (URL_TO_INSERT_TERM_2562 https://fairsharing.org/search?recordType=terminology_artefact)  management is achieved through editing the configuration file, **ols-config.yaml**. 

The ontology (URL_TO_INSERT_TERM_2563 https://fairsharing.org/search?recordType=terminology_artefact)  changes can be loaded by rebuilding the image and restarting the service.

#### 4.1 Modify OLS configuration

To add or remove ontologies (URL_TO_INSERT_TERM_2564 https://fairsharing.org/search?recordType=terminology_artefact) , modify corresponding sections in the configuration file.

Loaded ontologies (URL_TO_INSERT_TERM_2565 https://fairsharing.org/search?recordType=terminology_artefact)  will be updated to the latest version automatically by rebuilding the Docker image. 

#### 4.2 Rebuild OLS image and restart OLS 
Before rebuilding the Docker image, the existing container needs to be stopped and removed. 

The OLS (URL_TO_INSERT_RECORD-ABBREV_2566 https://fairsharing.org/FAIRsharing.Mkl9RR)  container can be stopped and removed by providing the container name. 

According to the parameters presented on the previous Docker creation command block, 
the name of the OLS (URL_TO_INSERT_RECORD-ABBREV_2567 https://fairsharing.org/FAIRsharing.Mkl9RR)  Docker container is "OLS (URL_TO_INSERT_RECORD-ABBREV_2568 https://fairsharing.org/FAIRsharing.Mkl9RR) ": 

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

Loading multiple ontologies (URL_TO_INSERT_TERM_2569 https://fairsharing.org/search?recordType=terminology_artefact)  from disk:
    
If more than one ontology (URL_TO_INSERT_TERM_2570 https://fairsharing.org/search?recordType=terminology_artefact)  are going to be loaded into OLS (URL_TO_INSERT_RECORD-ABBREV_2571 https://fairsharing.org/FAIRsharing.Mkl9RR)  from disk, the **Dockerfile** needs modifying before 
building the Docker container again:

* At Line 3 of the configuration file, replace **ENV OLS_HOME /opt/ols** with **ENV OLS_HOME /opt/ols/**

* At Line 3 of the configuration file, replace

    ```bash
    && java -Dols.obofoundry.ontology (URL_TO_INSERT_TERM_2572 https://fairsharing.org/search?recordType=terminology_artefact) .config=foo.yaml -Dols.ontology.config=file://${OLS_HOME}/ols-config.yaml -jar ${OLS_HOME}/ols-config-importer.jar
    ```
    
    with:

    ```bash
    && java -Dols.obofoundry.ontology (URL_TO_INSERT_TERM_2573 https://fairsharing.org/search?recordType=terminology_artefact) .config=foo.yaml -Dols.ontology.config=file://${OLS_HOME}ols-config.yaml -jar ${OLS_HOME}ols-config-importer.jar
    ```
    
## Conclusion
The local OLS (URL_TO_INSERT_RECORD-ABBREV_2575 https://fairsharing.org/FAIRsharing.Mkl9RR)  provides API endpoints for retrieving, submitting, updating, and querying ontology (URL_TO_INSERT_TERM_2574 https://fairsharing.org/search?recordType=terminology_artefact)  data, as well as a 
user interface for searching and browsing ontologies (URL_TO_INSERT_TERM_2577 https://fairsharing.org/search?recordType=terminology_artefact)  and ontology (URL_TO_INSERT_TERM_2576 https://fairsharing.org/search?recordType=terminology_artefact)  terms.

For example, all ontologies (URL_TO_INSERT_TERM_2578 https://fairsharing.org/search?recordType=terminology_artefact)  loaded can be queried through endpoint **http://localhost:8080/api/ontologies**.

A detailed description of OLS (URL_TO_INSERT_RECORD-ABBREV_2579 https://fairsharing.org/FAIRsharing.Mkl9RR)  functions can be found in the built-in documentation page.

To customize the local OLS (URL_TO_INSERT_RECORD-ABBREV_2580 https://fairsharing.org/FAIRsharing.Mkl9RR)  user interface, for example, adding corporate logos, please check the OLS (URL_TO_INSERT_RECORD-ABBREV_2581 https://fairsharing.org/FAIRsharing.Mkl9RR)  source code
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
