# Recipe 1.3: How to deploy a terminology service  - an example with the EBI Ontology Lookup Service

<!-- **identifier:** [UC3 R1.3](UC3R1.3)

**version:** [v0.1](v0.1)

___

**_Difficulty level:_** :triangular_flag_on_post: :triangular_flag_on_post:	:triangular_flag_on_post:	:white_circle:	:white_circle:

**_Reading time:_** 20 minutes

**_Intended Audience:_** 

> :heavy_check_mark: Terminology Manager

> :heavy_check_mark: Ontologist

> :heavy_check_mark: System Administrator

> :heavy_check_mark: Data Scientist

**_Recipe Type_**: Service deployment

**_Executable code_**: Yes -->


___


<div class="row">

  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-qrcode fa-2x" style="color:#7e0038;"></i>
        <h4><b>Recipe metadata</b></h4>
        <p> identifier: <a href="">UC3 R1.3</a> </p>
        <p> version: <a href="">v1.0</a> </p>
      </div>
    </div>
  </div>
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-fire fa-2x" style="color:#7e0038;"></i>
        <h4><b>Difficulty level</b></h4>
        <i class="fa fa-fire fa-lg" style="color:#7e0038;"></i>
        <i class="fa fa-fire fa-lg" style="color:#7e0038;"></i>
        <i class="fa fa-fire fa-lg" style="color:#7e0038;"></i>
        <i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
        <i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
  <!--       <p><span data-v-013baba1="" title="" class=""><svg data-v-013baba1="" viewBox="0 0 16 16" width="1em" height="1em" focusable="false" role="img" alt="icon" xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi-bar-chart-fill b-icon bi medium-level"><g data-v-013baba1=""><rect width="4" height="5" x="1" y="10" rx="1"></rect><rect width="4" height="9" x="6" y="6" rx="1"></rect><rect width="4" height="14" x="11" y="1" rx="1"></rect></g></svg> Medium </span></p> -->
      </div>
    </div>
  </div>  
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-clock-o fa-2x" style="color:#7e0038;"></i>
        <h4><b>Reading Time</b></h4>
        <p><i class="fa fa-clock-o fa-lg" style="color:#7e0038;"></i> 20 minutes</p>
        <h4><b>Recipe Type</b></h4>
        <p><i class="fa fa-laptop fa-lg" style="color:#7e0038;"></i> Hands-on</p>
        <h4><b>Executable Code</b></h4>
        <p><i class="fa fa-play-circle fa-lg" style="color:#7e0038;"></i> Yes</p>
      </div>
    </div>
  </div>
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-group fa-2x" style="color:#7e0038;"></i>
        <h4><b>Intended Audience</b></h4>
        <p> <i class="fa fa-tags fa-lg" style="color:#7e0038;"></i> Terminology Managers </p>
        <p> <i class="fa fa-database fa-lg" style="color:#7e0038;"></i> Data Managers </p>
        <p> <i class="fa fa-wrench fa-lg" style="color:#7e0038;"></i> Data Scientists </p>
        <p> <i class="fa fa-terminal fa-lg" style="color:#7e0038;"></i> System Administrators</p>
      </div>
    </div>
  </div>
</div>

___

[TOC]

## Main Objectives

This recipe is a step-by-step guide on how to deploy the EBI Ontology Lookup Service(OLS) on local machines. This demonstrates the workflow for deploying open source ontology service softwares in-house. 

## Introduction
With an increasing need for ontology infrastructure to improve the interoperability of information-based R&D activities, many pharmaceutical companies seek ontology management solutions and ontology services. Compared with developing local ontology services from scratch, reusing and redeveloping open-source ontology services save the time and cost. __Recipe 3.1__ identifies public open-source ontology services. In this recipe, we use the [Ontology Lookup Service](https://www.ebi.ac.uk/ols/index) to demonstrate the workflow of deploying public ontology services in-house.

Ontology Lookup Service is an open-source ontology management service developed by [EMBL-EBI](https://www.ebi.ac.uk/). It is a repository for biomedical ontologies, and serves as a single point of access to query, browse and navigate different ontologies. OLS supports the [Open Biological and Biomedical Ontology (OBO) Foundry](http://www.obofoundry.org/) guidelines and connects with other ontology services. It provides both web interface and API to search and browser ontologies. __Recipe 3.1__ provides a detailed description of OLS.

A local OLS allows users to protect and control their ontology-related data, and make stable and fast access to ontology services possible. It can serve as the hub of internal ontology eco-system, linking internal vocabulary, terminology management and data annotation activities together to improve the interoperability.

## Requirements
This recipe is intended for bioinformaticians or developers who wants to explore public ontologies and ontology services. The users are expected to be familiar with Unix-based OS and basic Bash programming syntax and commands. The users should also be comfortable with YAML or other data-serialization languages. Knowledge about [Docker](https://www.docker.com/) allows users to further customize their local service.

This recipe can also be applied by organizational users. Please check with your IT support staff about specific policies regarding the use of containerized applications, proxy settings, and firewalls.

## Graphical overview

<div class="mermaid">
graph LR
    A[Install dependencies] --> B[Import ontologies]
    B--> C[Set up and start local OLS] 
    C--> D[Manage ontologies]
    D --> C
    

    subgraph Get ontology resources
    B1([From the online sources])
    B2([From local files])
    end

    subgraph Ontology management
    E([Add new ontologies])
    F([Update existing ontologies])
    G([Delete ontologies])
    end

    B1-.-> B
    B2 -.->B
   
    E -.-> D
    F -.-> D
    G -.-> D
    
    style E fill:#FFFF99
    style F fill:#FFFF99
    style G fill:#FFFF99
    style B1 fill:#FFFF99
    style B2 fill:#FFFF99

</div>
 
## Ingredients
- [OLS Docker image](https://github.com/EBISPOT/OLS-docker) 
- [Ontology metadata in OBO foundry](https://github.com/OBOFoundry/purl.obolibrary.org/tree/master/config)

## Step-by-step guide:

### 1. Install dependencies

- Unix-based environment (macOS, Linux):

|Software|Description|Version|Installation|
|--|--|--|--|
|Git|Get the versioned source file|2.17.1 |[Official guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)|
|Docker|Deliver software in containers|18.09.01 |[Official guide](https://docs.docker.com/install/)|

- Windows-based enviroment (Windows 10 64bits):

|Software|Description|Version|Installation|
|--|--|--|--|
|Git|Get the versioned source file|2.26.2.windows.1|[Official guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)|
|Docker Desktop|Deliver software in containers|2.2.0.5 (Engine v.19.03.8)|[Official guide](https://docs.docker.com/install/)|
|PowerShell|Execute commands| 5.1.17763(Desktop Edition)|[Official Guide](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7)|

> :bulb: This recipe was developed on a Unix-based environment and tested on Linux, macOS and Windows machines. Minor modifications are required  to run it on Windows machines.

### 2. Load ontologies into OLS 

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

To add local ontologies, the ontology files need to be first copied to the `OLS-docker` directory. By default, the ontology file location is specified as`/opt/ols/example.owl`. For example,  `ontology_purl:file:///opt/ols/example.owl`.

To add ontologies from online resources, ontology URLs are required. Most reference ontologies use the OBO foundry Permanent URLs (PURLs). The PURLs can be found [here](http://www.obofoundry.org/). For example, the location of Data Usage Ontology (DUO) can be specified by adding `ontology_purl: http://purl.obolibrary.org/obo/duo.owl` to the configuration file. 

Ontology metadata for the configuration file can be written by users. For common public ontologies, the ontology metadata can also be downloaded from either the EBI OLS or the OBO Foundry.

#### 2.1 Get ontology metadata from the EBI OLS

For ontologies included in the EBI OLS, the metadata can be downloaded directly using the EBI OLS endpoint, `https://www.ebi.ac.uk/ols/api/ols-config\?ids\=<ontologies-short-names-list>`, by providing the ontology short names. Metadata of multiple ontologies can be downloaded at the same time.  [Here](https://www.ebi.ac.uk/ols/ontologies) is a list of all the ontologies available at OLS, along with their respective "short name" and other information. 

For example, the following command downloads the ontologies metadata of EFO and Adverse Event Reporting Ontology (AERO) and saves it as `ols-config.yaml`:

>:warning: The command overwrites the original `ols-config.yml` file and removes pre-loaded ontologies.

>On Windows systems, add quotations around the URL. e.g.`"<URL>"`.

```shell
wget -O ols-config.yaml https://www.ebi.ac.uk/ols/api/ols-config\?ids\=aero,efo
```
To avoid losing pre-loaded ontologies, the metadata of EFO and AERO can also be appended to the already existing `ols-config.yml` using:
```shell
wget -O - https://www.ebi.ac.uk/ols/api/ols-config\?ids\=efo,aero >> ols-config.yaml
```
>:warning: The file needs to be manually edited by removing the header of the new metadata and adding proper indentation.


For ontologies that are in the OBO foundry, the metadata can also be downloaded from the [OBO Foundry GitHub repository](https://github.com/OBOFoundry/purl.obolibrary.org/tree/master/config). Additional formatting is required for metadata downloaded from the OBO foundry.

### 3. Set up OLS in the local environment 
>For Windows machines, run the Docker Desktop app to start the Docker daemon.

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

### 4. Manage ontologies
OLS allows the addition, update, and removal of ontologies. Such ontology management is achieved through editing the configuration file, `ols-config.yaml`. The ontology changes can be loaded by rebuilding the image and restarting the service.

#### 4.1 Modify OLS configuration

To add or remove ontologies, modify corresponding sections in the configuration file. Loaded ontologies will be updated to the latest version automatically by rebuilding the Docker image. 

#### 4.2 Rebuild OLS image and restart OLS 
Before rebuilding the Docker image, the existing container needs to be stopped and removed. The OLS container can be stopped and removed by providing the container name. According to the parameters presented on the previous Docker creation command block, the name of the OLS Docker container is "OLS": 

>:bulb: By rebuilding the OLS image, all loaded ontologies will be automatically updated to the latest version.

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
- Loading multiple ontologies from disk
    
If more than one ontologies are going to be loaded into OLS from disk, the `Dockerfile` needs modifications before building the Docker container:

In Line 3, replace `ENV OLS_HOME /opt/ols` with `ENV OLS_HOME /opt/ols/`
    
In Line 14, replace

```bash
&& java -Dols.obofoundry.ontology.config=foo.yaml -Dols.ontology.config=file://${OLS_HOME}/ols-config.yaml -jar ${OLS_HOME}/ols-config-importer.jar
```
    
    with:

```bash
&& java -Dols.obofoundry.ontology.config=foo.yaml -Dols.ontology.config=file://${OLS_HOME}ols-config.yaml -jar ${OLS_HOME}ols-config-importer.jar
```
    
## Summary
The local OLS provides API endpoints for retrieving, submitting, updating, and querying ontology data, as well as a user interface for searching and browsing ontologies and ontology terms. For example, all ontologies loaded can be queried through endpoint ` http://localhost:8080/api/ontologies`. A detailed description of OLS functions can be found in the built-in documentation page.



To customize the local OLS user interface, for example, adding corporate logos, please check the OLS source code [here](https://github.com/EBISPOT/OLS). 

## Reference
* [Documentation < Ontology Lookup Service < EMBL-EBI. Accessed 20 April 2020.](https://www.ebi.ac.uk/ols/docs/installation-guide)
* [Jupp S. et al. (2015) A new Ontology Lookup Service at EMBL-EBI. In: Malone, J. et al. (eds.) Proceedings of SWAT4LS International Conference 2015](https://conferences.ncl.ac.uk/media/sites/conferencewebsites/ukon2016/UKON_2016_paper_9.pdf)
* [Côté, Richard G., et al. "The Ontology Lookup Service, a lightweight cross-platform tool for controlled vocabulary queries." BMC bioinformatics 7.1 (2006): 97.](https://link.springer.com/article/10.1186/1471-2105-7-97)

## Authors

| Name | Affiliation  | ORCID | CRediT role  |
|--|--|--|--|
|Fuqi Xu|[EMBL-EBI](https://www.ebi.ac.uk/)|[0000-0002-5923-3859](https://orcid.org/0000-0002-5923-3859)|Writing - Original Draft|
|Eva Martin | [Barcelona Supercomputing Center (BSC)](https://www.bsc.es/) |[0000-0001-8324-2897](https://orcid.org/0000-0001-8324-2897)|Writing - Original Draft |
Emiliano Reynares|[Boehringer Ingelheim](https://www.boehringer-ingelheim.com/)|[0000-0002-5109-3716](https://orcid.org/0000-0002-5109-3716)|Reviewing|
| Philippe Rocca-Serra |  [University of Oxford, Data Readiness Group](https://datareadiness.eng.ox.ac.uk/)| [0000-0001-9853-5668](https://orcid.org/orcid.org/0000-0001-9853-5668) | Reviewing |

## License

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
