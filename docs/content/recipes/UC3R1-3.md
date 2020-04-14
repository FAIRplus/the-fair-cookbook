# Recipe 1.3: How to deploy the service internally, an examplar

#AI: feedback to Squad1. more ontology services

- [Main Objectives](#main-objectives)
- [Ingredients](#ingredients)
  * [Introduction](#introduction)
- [Graphic view](#graphic-view)
- [Step by step guide:](#step-by-step-guide-)
  * [1. Installing dependencies](#1-installing-dependencies)
    + [Add memory requirements](#add-memory-requirements)
  * [2. Loading ontologies into OLS](#2-loading-ontologies-into-ols)
    + [2.1 Downloading configuration files from EBI OLS.](#21-downloading-configuration-files-from-ebi-ols)
    + [2.2 Loading ontologies from OBO Foundry](#22-loading-ontologies-from-obo-foundry)
  * [3. Set up OLS in the local environment](#3-set-up-ols-in-the-local-environment)
    + [Troubleshooting](#troubleshooting)
- [Summary](#summary)
- [Authors](#authors)
- [License](#license)
- [Reference](#reference)

## Main Objectives

How to deploy public ontology services in local machines, take the EBI Ontology Lookup Service (OLS) as an example.

## Ingredients
- [OLS Docker image](https://github.com/EBISPOT/OLS-docker) 
- [OLS Documentation: Build a local version of OLS(without Docker)](https://www.ebi.ac.uk/ols/docs/installation-guide)
- [Ontology metadata in OBO foundry](https://github.com/OBOFoundry/purl.obolibrary.org/tree/master/config)

### Introduction

> :bulb: **Hint:** This recipe is intended for bioinformaticians or developers who wants to explore public ontologies and ontology services. The users are expected to be familiar with Bash and other command line tools. 
> 
> Knowledge about building and running docker images allows users further customize the local OLS machine.
> 

#TODO: is knowing yaml also mandatory?

> [name=Emiliano][color=red] This hint allows to infer that the recipe uses some Unix-based OS. Maybe that assumption should be explicit stated among a ingredients/dependencies/requirements section.
> On the other side, would be needed to provide instructions on how to deploy the service on a Windows environment?

#TODO test it on Windows
 
[Ontology lookup service (OLS)](https://www.ebi.ac.uk/ols/index) is a repository for biomedical ontologies. It serves as a single point of access to query, browser and navigates different ontologies. OLS supports the [Open Biological and Biomedical Ontology (OBO) Foundry](http://www.obofoundry.org/) guidelines and connects with other ontology services. It provides both web interface and API to search and browser ontologies. 

TODO: add ontology metadata intro.
what is ontology metadata. why do we need to use it (load). Where to find it (local, download from EBI/OBO)

## Graphic view

#TODO use mermaid code instead of this link

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVEJcbiAgICBBW0luc3RhbGwgZGVwZW5kZW5jaWVzXSAtLT4gQltMb2FkIG9udG9sb2d5IG1ldGFkYXRhXVxuICAgIEIgLS0-IENbU2V0IHVwIGxvY2FsIE9MU11cbiAgICBcbiAgICBzdWJncmFwaCBkb3dubG9hZCBvbnRvbG9neSBtZXRhZGF0YVxuICAgICAgICBEKEZyb20gdGhlIEVCSSBPTFMpIFxuICAgICAgICBFKEZyb20gdGhlIE9CTyBmb3VuZHJ5KVxuICAgICAgICBGKHNlbGYtZGVmaW5lZCBvbnRvbG9neSBtZXRhZGF0YSkgXG4gICAgICAgIGVuZFxuICAgIEcob250b2xneSBtZXRhZGF0YSBvbiBhIGRpc2spXG4gICAgRCAtLT4gR1xuICAgIEUgLS0-IEdcblxuRy0tPiBCXG5DLS0-IE1bT0xTIGluc3RhbGxlZCBhbmQgc3RhcnRlZF1cblxuIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVEJcbiAgICBBW0luc3RhbGwgZGVwZW5kZW5jaWVzXSAtLT4gQltMb2FkIG9udG9sb2d5IG1ldGFkYXRhXVxuICAgIEIgLS0-IENbU2V0IHVwIGxvY2FsIE9MU11cbiAgICBcbiAgICBzdWJncmFwaCBkb3dubG9hZCBvbnRvbG9neSBtZXRhZGF0YVxuICAgICAgICBEKEZyb20gdGhlIEVCSSBPTFMpIFxuICAgICAgICBFKEZyb20gdGhlIE9CTyBmb3VuZHJ5KVxuICAgICAgICBGKHNlbGYtZGVmaW5lZCBvbnRvbG9neSBtZXRhZGF0YSkgXG4gICAgICAgIGVuZFxuICAgIEcob250b2xneSBtZXRhZGF0YSBvbiBhIGRpc2spXG4gICAgRCAtLT4gR1xuICAgIEUgLS0-IEdcblxuRy0tPiBCXG5DLS0-IE1bT0xTIGluc3RhbGxlZCBhbmQgc3RhcnRlZF1cblxuIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)

#TODO make a better graph

## Step by step guide:

### 1. Installing dependencies

#### Add memory requirements

|Software|Description|Installation|
|--|--|--|
|Git| Get the versioned source file|[Official guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)|
|Docker|Deliver software in containers |[Official guide](https://docs.docker.com/install/)|
> This recipe has been tested using Git v2.17.1 and Docker v18.09.01.

### 2. Loading ontologies into OLS 

#TODO rephrase

Ontologies in both [OBO](https://fairsharing.org/10.25504/FAIRsharing.aa0eat) and [OWL](https://fairsharing.org/10.25504/FAIRsharing.atygwy) formats can be loaded to OLS by adding ontology metadata to the configuration files `ols-config.yaml`, if the metadata follows the [ols specification](https://www.ebi.ac.uk/ols/docs/installation-guide), or `obo-config.yaml`, if metadata follows the [OBO Foundry specification](http://obofoundry.github.io/faq/how-do-i-edit-metadata.html). In either case, there are three mandatory fields: 

|Attribute|Description|
|--|--|
|id|Short unique id for the ontology|
|uri|The ontology URL|
|ontology_purl|URL to get the ontology from| 

Ontologies can be loaded either from disk or providing the PURL. 

To add an ontology from a PURL, it must be specified in configuration file as follows: `ontology_purl: <PURL>`. 

OLS provides an [example configuration file](https://www.ebi.ac.uk/ols/docs/installation-guide) to load EFO ontology.  For example: 

```
## EFO

  - id: efo
    preferredPrefix: EFO
    title: Experimental Factor Ontology
    uri: http://www.ebi.ac.uk/efo/efo.owl
    description: "The Experimental Factor Ontology (EFO) provides a systematic description of many experimental variables available in EBI databases, and for projects such as the GWAS catalog"
    homepage: https://www.ebi.ac.uk/efo/
    ontology_purl: http://www.ebi.ac.uk/efo/efo.owl
```

To add a local ontology to the service, first copy the ontology file inside the docker directory and then specify it in the configuration file as follows `ontology_purl: file:///opt/ols/<filename>.owl`. 

For example, to load the GO ontology from disk, the ontology file `go.owl` is placed inside the OLS directory and the following metadata is added to the configuration file `ols-config.yaml`:
```
ontologies:

## GO
  - id: go
    preferredPrefix: GO
    title: Gene Ontology
    uri: file:///opt/ols/go.owl
    description: "The logical structure describing the full complexity of the biology, comprised of the ‘classes’ for the many different kinds of biological functions, the pathways carrying out different biological programs, and the cellular locations where these occur; and equally important, the different types of specific relationships that indicate how each of these classes is related to other classes"
    homepage: http://geneontology.org/
    ontology_purl: file:///opt/ols/go.owl
```


Ontology metadata can be downloaded from either the OBO foundry, or the EBI OLS. Users can also provide their own ontology metadata. 



#### 2.1 Downloading configuration files from EBI OLS.

#TODO add how to find ontology ID as Emiliano suggested.

#TODO distinct "append" and "create new file" 

#TODO check indentation of the downloaded file

For ontologies included in the EBI OLS, the metadata can be downloaded directly using the OLS API using the ontology ID. 

```sh
    # EBI OLS endpoint for ontology metadata
    # https://www.ebi.ac.uk/ols/api/ols-config\?ids\=<ontologies-ids-list>

    # e.g. Download ontology metadata of EFO and AERO from the EBI OLS.
    wget -O ols-config.yaml https://www.ebi.ac.uk/ols/api/ols-config\?ids\=aero,efo
```
> [name=Emiliano][color=red] Ontology ID (aka "Short name") can be found in https://www.ebi.ac.uk/ols/ontologies.
> The ```wget -O ...``` command shown overwrites the ```ols-config.yaml``` file. An alternative to *add* new entries to a existing file is to run:
> 
> ```wget -O - https://www.ebi.ac.uk/ols/api/ols-config\?ids\=IDS_TO_ADD >> ols-config.yaml```
> 
> However, is it needed to fix the indentation of the resulting ```ols-config.yaml``` file. I.e., to indent the added entries and delete the ```---``` and ```ontologies:``` added lines.


#### 2.2 Loading ontologies from OBO Foundry
> @EvaMart **TODO**

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
sudo docker run -d -p 8080:8080 -t ols
```

The local OLS service can be accessed at http://localhost:8080/index 

> @EvaMart **TODO** 
> 
> ###TODO (advanced feature, maybe a hint box) suggestions about how to modify the docker file.
>
> #TODO as Emiliano suggested.
> 
>[name=Emiliano][color=red] Could be useful to depict the steps to follow to add new ontologies by re-building the OLS docker image.

#### Troubleshooting
1. **java.lang.OutOfMemoryError: Java heap space**. When the building process runs out of memory with the previous message, the maximum heap size used by the Java Virtual Machine has to be increased. Prior to building the image, inside the Dockerfile, change the parameter `“JAVA_OPTS” `from:
`ENV JAVA_OPTS "-Xmx1g"` to: `ENV JAVA_OPTS "-Xmx2g -Xms2g"`

###TODO: check if allocating more memory improves the speed. 

2. **GC overhead limit exceeded.** When this error happends while building, the maximum heap size used by the Java Virtual Machine has to be increased. Prior to building the image, inside the Dockerfile, change the parameter `“JAVA_OPTS” `from:
`ENV JAVA_OPTS "-Xmx1g"` to: `ENV JAVA_OPTS "-Xmx2g -Xms2g"` 

##TODO a hint box pointing to OLS docker helpdesk

>[name=Emiliano][color=red] I didn't have any of these issues.

>[name=Eva][color=orange] The first, I did in my laptop. The second, only with very big ontologies. Do you think we should not include issues that do not seem frequent?

> [name=Emiliano][color=red] If you have already identified a way to tackle these kind of issues, it's OK. But in a first draft I'd focus on the _happy_ deployment path. Maybe later would be possible to spend some time depicting _apparently non-frequent_ issues and suggested solutions. 

## Summary
The local OLS provides :
- API endpoints for retrieving, submitting, updating, and querying ontology data.
- A user interface for searching and browsing ontology and ontology terms.

For detailed description of OLS functions, please check the OLS documentation page either on your local machine or on [the EBI OLS page](https://www.ebi.ac.uk/ols/docs/index). 

#TODO a summary of the recipe instead of OLS

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