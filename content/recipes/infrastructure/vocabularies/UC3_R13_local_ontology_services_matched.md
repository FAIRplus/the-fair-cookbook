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

This recipe is a step-by-step guide on how to deploy the EBI Ontology (URL_TO_INSERT_TERM_4138 https://fairsharing.org/search?recordType=terminology_artefact)  Lookup Service (URL_TO_INSERT_RECORD_4139 https://fairsharing.org/FAIRsharing.Mkl9RR)  (OLS (URL_TO_INSERT_RECORD_4140 https://fairsharing.org/FAIRsharing.Mkl9RR) ) {footcite}`pmid20460452`, {footcite}`ols_jupp` on local machines. 
This demonstrates the workflow for deploying open source ontology (URL_TO_INSERT_TERM_4141 https://fairsharing.org/search?recordType=terminology_artefact)  service software in-house {footcite}`ols-install-guide`. 

## Introduction
With an increasing need for ontology (URL_TO_INSERT_TERM_4143 https://fairsharing.org/search?recordType=terminology_artefact)  infrastructure to improve the interoperability of informat (URL_TO_INSERT_TERM_4142 https://fairsharing.org/search?recordType=model_and_format) ion-based R&D activities,
many pharmaceutical companies seek ontology (URL_TO_INSERT_TERM_4144 https://fairsharing.org/search?recordType=terminology_artefact)  management solutions and ontology (URL_TO_INSERT_TERM_4145 https://fairsharing.org/search?recordType=terminology_artefact)  services. 
Compared with developing local ontology (URL_TO_INSERT_TERM_4146 https://fairsharing.org/search?recordType=terminology_artefact)  services from scratch, reusing and redeveloping open-source ontology (URL_TO_INSERT_TERM_4147 https://fairsharing.org/search?recordType=terminology_artefact)  services
save the time and cost. [Recipe FCB003](https://w3id.org (URL_TO_INSERT_RECORD_4149 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB003) identifies public open-source ontology (URL_TO_INSERT_TERM_4148 https://fairsharing.org/search?recordType=terminology_artefact)  services. 
In this recipe, we use the [Ontology (URL_TO_INSERT_TERM_4150 https://fairsharing.org/search?recordType=terminology_artefact)  Lookup Service (URL_TO_INSERT_RECORD_4151 https://fairsharing.org/FAIRsharing.Mkl9RR) ](https://www.ebi.ac.uk/ols/index (URL_TO_INSERT_RECORD_4152 https://fairsharing.org/FAIRsharing.Mkl9RR) ) to demonstrate the workflow of 
deploying public ontology (URL_TO_INSERT_TERM_4153 https://fairsharing.org/search?recordType=terminology_artefact)  services in-house.

Ontology (URL_TO_INSERT_TERM_4154 https://fairsharing.org/search?recordType=terminology_artefact)  Lookup Service (URL_TO_INSERT_RECORD_4156 https://fairsharing.org/FAIRsharing.Mkl9RR)  is an open-source ontology (URL_TO_INSERT_TERM_4155 https://fairsharing.org/search?recordType=terminology_artefact)  management service developed (URL_TO_INSERT_RECORD_4157 https://fairsharing.org/FAIRsharing.31385c)  by [EMBL-EBI](https://www.ebi.ac.uk/).

It is a repository (URL_TO_INSERT_TERM_4158 https://fairsharing.org/search?recordType=repository)  for biomedical ontologies (URL_TO_INSERT_TERM_4159 https://fairsharing.org/search?recordType=terminology_artefact) , and serves as a single point of access to query, browse and navigate
different ontologies (URL_TO_INSERT_TERM_4160 https://fairsharing.org/search?recordType=terminology_artefact) . 

OLS (URL_TO_INSERT_RECORD_4162 https://fairsharing.org/FAIRsharing.Mkl9RR)  supports the [Open Biological and Biomedical Ontology (URL_TO_INSERT_TERM_4161 https://fairsharing.org/search?recordType=terminology_artefact)  (OBO (URL_TO_INSERT_RECORD_4163 https://fairsharing.org/FAIRsharing.847069) ) Foundry](http://www.obofoundry.org (URL_TO_INSERT_RECORD_4164 https://fairsharing.org/FAIRsharing.847069) /)
guideline (URL_TO_INSERT_TERM_4166 https://fairsharing.org/search?recordType=reporting_guideline) s and connects with other ontology (URL_TO_INSERT_TERM_4165 https://fairsharing.org/search?recordType=terminology_artefact)  services. 

It provides both web interface and API to search (URL_TO_INSERT_RECORD_4167 https://fairsharing.org/FAIRsharing.52b22c)  and browser 
ontologies (URL_TO_INSERT_TERM_4168 https://fairsharing.org/search?recordType=terminology_artefact) . 
[Recipe FCB003](https://w3id.org (URL_TO_INSERT_RECORD_4170 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB003) provides a detailed description of OLS (URL_TO_INSERT_RECORD_4169 https://fairsharing.org/FAIRsharing.Mkl9RR) .

A local OLS (URL_TO_INSERT_RECORD_4173 https://fairsharing.org/FAIRsharing.Mkl9RR)  allows users to protect and control their ontology (URL_TO_INSERT_TERM_4171 https://fairsharing.org/search?recordType=terminology_artefact) -related data, and make stable and fast access to ontology (URL_TO_INSERT_TERM_4172 https://fairsharing.org/search?recordType=terminology_artefact) 
services possible. 

It can serve as the hub of internal ontology (URL_TO_INSERT_TERM_4174 https://fairsharing.org/search?recordType=terminology_artefact)  eco-system, linking internal vocabulary, 
terminology (URL_TO_INSERT_TERM_4175 https://fairsharing.org/search?recordType=terminology_artefact)  management and data annotation activities together to improve the interoperability.

## Requirements
This recipe is intended for bioinformat (URL_TO_INSERT_TERM_4176 https://fairsharing.org/search?recordType=model_and_format) icians or developers who want to explore public ontologies (URL_TO_INSERT_TERM_4178 https://fairsharing.org/search?recordType=terminology_artefact)  and ontology (URL_TO_INSERT_TERM_4177 https://fairsharing.org/search?recordType=terminology_artefact)  services. 
The users are expected to be fam (URL_TO_INSERT_RECORD_4179 https://fairsharing.org/FAIRsharing.d0886a) iliar with Unix-based OS and basic Bash programming syntax and commands. 
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
alt: Deploying EMBL-EBI OLS (URL_TO_INSERT_RECORD_4180 https://fairsharing.org/FAIRsharing.Mkl9RR) 
---
Deploying EMBL-EBI Ontology (URL_TO_INSERT_TERM_4181 https://fairsharing.org/search?recordType=terminology_artefact)  Lookup Service (URL_TO_INSERT_RECORD_4182 https://fairsharing.org/FAIRsharing.Mkl9RR) 
```
````
 
## Ingredients
- [OLS (URL_TO_INSERT_RECORD_4183 https://fairsharing.org/FAIRsharing.Mkl9RR)  Docker image](https://github.com (URL_TO_INSERT_RECORD_4184 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/OLS-docker) 
- [Ontology (URL_TO_INSERT_TERM_4185 https://fairsharing.org/search?recordType=terminology_artefact)  metadata in OBO foundry (URL_TO_INSERT_RECORD_4186 https://fairsharing.org/FAIRsharing.847069) ](https://github.com (URL_TO_INSERT_RECORD_4187 https://fairsharing.org/FAIRsharing.c55d5e) /OBOFoundry/purl.obolibrary.org/tree/master/config)

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

Ontologies (URL_TO_INSERT_TERM_4188 https://fairsharing.org/search?recordType=terminology_artefact)  in both [OBO](https://fairsharing.org (URL_TO_INSERT_RECORD_4189 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_4190 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_4191 https://fairsharing.org/3538) /10.25504/FAIRsharing.aa0eat) and
[OWL](https://fairsharing.org (URL_TO_INSERT_RECORD_4195 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_4196 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_4197 https://fairsharing.org/3538) /10.25504/FAIRsharing.atygwy) format (URL_TO_INSERT_TERM_4192 https://fairsharing.org/search?recordType=model_and_format) s can be loaded to OLS (URL_TO_INSERT_RECORD_4194 https://fairsharing.org/FAIRsharing.Mkl9RR)  by adding ontology (URL_TO_INSERT_TERM_4193 https://fairsharing.org/search?recordType=terminology_artefact) 
metadata to the configuration file, **ols-config.yaml**. 

Three fields, **id**,**url** and **ontology (URL_TO_INSERT_TERM_4198 https://fairsharing.org/search?recordType=terminology_artefact) _purl** are mandatory ontology (URL_TO_INSERT_TERM_4199 https://fairsharing.org/search?recordType=terminology_artefact)  metadata attributes.

Other fields are also recommended, especially for self-defined ontologies (URL_TO_INSERT_TERM_4200 https://fairsharing.org/search?recordType=terminology_artefact) . 

Below is an example configuration of the Experimental Factor Ontology (URL_TO_INSERT_TERM_4201 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_4202 https://fairsharing.org/FAIRsharing.1gr4tz)  (EFO (URL_TO_INSERT_RECORD_4203 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_4204 https://fairsharing.org/FAIRsharing.ca63ce) ) provided
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

The location of the target ontology (URL_TO_INSERT_TERM_4205 https://fairsharing.org/search?recordType=terminology_artefact)  shall be specified in the **ontology (URL_TO_INSERT_TERM_4206 https://fairsharing.org/search?recordType=terminology_artefact) _purl** field in the **`ols-config.yaml** file.

Ontologies (URL_TO_INSERT_TERM_4207 https://fairsharing.org/search?recordType=terminology_artefact)  from both local files and online resources can be imported. 

To add local ontologies (URL_TO_INSERT_TERM_4209 https://fairsharing.org/search?recordType=terminology_artefact) , the ontology (URL_TO_INSERT_TERM_4208 https://fairsharing.org/search?recordType=terminology_artefact)  files need to be first copied to the **OLS (URL_TO_INSERT_RECORD_4210 https://fairsharing.org/FAIRsharing.Mkl9RR) -docker** directory. 

By default, the ontology (URL_TO_INSERT_TERM_4211 https://fairsharing.org/search?recordType=terminology_artefact)  file location is specified as **/opt/ols/example.owl**. 

For example, **ontology (URL_TO_INSERT_TERM_4212 https://fairsharing.org/search?recordType=terminology_artefact) _purl:file:///opt/ols/example.owl**.

To add ontologies (URL_TO_INSERT_TERM_4214 https://fairsharing.org/search?recordType=terminology_artefact)  from online resources, ontology (URL_TO_INSERT_TERM_4213 https://fairsharing.org/search?recordType=terminology_artefact)  URL (URL_TO_INSERT_RECORD_4215 https://fairsharing.org/FAIRsharing.9d38e2) s are required.

Most reference ontologies (URL_TO_INSERT_TERM_4216 https://fairsharing.org/search?recordType=terminology_artefact)  use the OBO foundry (URL_TO_INSERT_RECORD_4218 https://fairsharing.org/FAIRsharing.847069)  Permanent URL (URL_TO_INSERT_RECORD_4219 https://fairsharing.org/FAIRsharing.9d38e2) s (PURL (URL_TO_INSERT_RECORD_4217 https://fairsharing.org/FAIRsharing.3e603c)  (URL_TO_INSERT_RECORD_4220 https://fairsharing.org/FAIRsharing.9d38e2) s). 

The PURL (URL_TO_INSERT_RECORD_4221 https://fairsharing.org/FAIRsharing.3e603c)  (URL_TO_INSERT_RECORD_4223 https://fairsharing.org/FAIRsharing.9d38e2) s can be found [here](http://www.obofoundry.org (URL_TO_INSERT_RECORD_4222 https://fairsharing.org/FAIRsharing.847069) /). 

For example, the location of Data Usage Ontology (URL_TO_INSERT_TERM_4224 https://fairsharing.org/search?recordType=terminology_artefact)  (DUO (URL_TO_INSERT_RECORD_4225 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_4226 https://fairsharing.org/FAIRsharing.mjnypw) ) can be specified by adding:

```
ontology_purl: http://purl.obolibrary.org/obo/duo.owl
```

to the configuration file. 

Ontology (URL_TO_INSERT_TERM_4227 https://fairsharing.org/search?recordType=terminology_artefact)  metadata for the configuration file can be written by users. 

For common public ontologies (URL_TO_INSERT_TERM_4229 https://fairsharing.org/search?recordType=terminology_artefact) , the ontology (URL_TO_INSERT_TERM_4228 https://fairsharing.org/search?recordType=terminology_artefact)  metadata can also be downloaded from either the 
[EBI OLS](https://www.ebi.ac.uk/ols/index (URL_TO_INSERT_RECORD_4230 https://fairsharing.org/FAIRsharing.Mkl9RR) ) or the [OBO Foundry (URL_TO_INSERT_RECORD_4231 https://fairsharing.org/FAIRsharing.847069) ](https://obofoundry.org/) {footcite}`pmid17989687obofoundry2007`,
{footcite}`pmid34697637obofoundry2021` .

#### 2.1 Get ontology metadata from the EBI OLS

For ontologies (URL_TO_INSERT_TERM_4232 https://fairsharing.org/search?recordType=terminology_artefact)  included in the EBI OLS (URL_TO_INSERT_RECORD_4233 https://fairsharing.org/FAIRsharing.Mkl9RR) , the metadata can be downloaded directly using the EBI OLS (URL_TO_INSERT_RECORD_4234 https://fairsharing.org/FAIRsharing.Mkl9RR)  endpoint,
**https://www.ebi.ac.uk/ols/api/ols-config\?ids\=<ontologies-short-names-list>**, by providing the ontology (URL_TO_INSERT_TERM_4235 https://fairsharing.org/search?recordType=terminology_artefact)  short names.

Metadata of multiple ontologies (URL_TO_INSERT_TERM_4236 https://fairsharing.org/search?recordType=terminology_artefact)  can be downloaded at the same time.

[Here](https://www.ebi.ac.uk/ols/ontologies) is a list of all the ontologies (URL_TO_INSERT_TERM_4237 https://fairsharing.org/search?recordType=terminology_artefact)  available at OLS (URL_TO_INSERT_RECORD_4238 https://fairsharing.org/FAIRsharing.Mkl9RR) , along with their
respective "short name" and other informat (URL_TO_INSERT_TERM_4239 https://fairsharing.org/search?recordType=model_and_format) ion. 

For example, the following command downloads the ontology (URL_TO_INSERT_TERM_4240 https://fairsharing.org/search?recordType=terminology_artefact)  metadata of EFO (URL_TO_INSERT_RECORD_4245 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_4247 https://fairsharing.org/FAIRsharing.ca63ce)  and Adverse Event Reporting Ontology (URL_TO_INSERT_TERM_4241 https://fairsharing.org/search?recordType=terminology_artefact)  (AERO (URL_TO_INSERT_RECORD_4242 https://fairsharing.org/FAIRsharing.nwgynk)  (URL_TO_INSERT_RECORD_4243 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_4244 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_4246 https://fairsharing.org/FAIRsharing.cp0ybc) ) 
and saves it as **ols-config.yaml**:

```{warning}
- The command overwrites the original **ols-config.yml** file and **removes** pre-loaded ontologies.

- On Windows systems, make sure to wrap the url with quotes, e.g.***"<URL>"***.
```



```shell
wget -O ols-config.yaml https://www.ebi.ac.uk/ols/api/ols-config\?ids\=aero,efo
```
To avoid losing pre-loaded ontologies (URL_TO_INSERT_TERM_4248 https://fairsharing.org/search?recordType=terminology_artefact) , the metadata of EFO (URL_TO_INSERT_RECORD_4252 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_4254 https://fairsharing.org/FAIRsharing.ca63ce)  and AERO (URL_TO_INSERT_RECORD_4249 https://fairsharing.org/FAIRsharing.nwgynk)  (URL_TO_INSERT_RECORD_4250 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_4251 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_4253 https://fairsharing.org/FAIRsharing.cp0ybc)  can also be appended to the already existing **ols-config.yml** using:

```shell
wget -O - https://www.ebi.ac.uk/ols/api/ols-config\?ids\=efo,aero >> ols-config.yaml
```

```{warning}
>:warning: The file needs to be manually edited by removing the header of the new metadata and adding proper indentation.
```

For ontologies (URL_TO_INSERT_TERM_4256 https://fairsharing.org/search?recordType=terminology_artefact)  that are in the OBO foundry (URL_TO_INSERT_RECORD_4257 https://fairsharing.org/FAIRsharing.847069) , the metadata can also be downloaded from the [OBO Foundry (URL_TO_INSERT_RECORD_4258 https://fairsharing.org/FAIRsharing.847069)  GitHub (URL_TO_INSERT_RECORD_4259 https://fairsharing.org/FAIRsharing.c55d5e)  repository (URL_TO_INSERT_TERM_4255 https://fairsharing.org/search?recordType=repository) ](https://github.com (URL_TO_INSERT_RECORD_4260 https://fairsharing.org/FAIRsharing.c55d5e) /OBOFoundry/purl.obolibrary.org/tree/master/config).

Additional format (URL_TO_INSERT_TERM_4261 https://fairsharing.org/search?recordType=model_and_format) ting is required for metadata downloaded from the OBO foundry (URL_TO_INSERT_RECORD_4262 https://fairsharing.org/FAIRsharing.847069) .

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

The local OLS (URL_TO_INSERT_RECORD_4263 https://fairsharing.org/FAIRsharing.Mkl9RR)  service can be accessed at http://localhost:8080/index 

### 4. Manage ontologies
OLS (URL_TO_INSERT_RECORD_4265 https://fairsharing.org/FAIRsharing.Mkl9RR)  allows the addition, update, and removal of ontologies (URL_TO_INSERT_TERM_4264 https://fairsharing.org/search?recordType=terminology_artefact) .

Such ontology (URL_TO_INSERT_TERM_4266 https://fairsharing.org/search?recordType=terminology_artefact)  management is achieved through editing the configuration file, **ols-config.yaml**. 

The ontology (URL_TO_INSERT_TERM_4267 https://fairsharing.org/search?recordType=terminology_artefact)  changes can be loaded by rebuilding the image and restarting the service.

#### 4.1 Modify OLS configuration

To add or remove ontologies (URL_TO_INSERT_TERM_4268 https://fairsharing.org/search?recordType=terminology_artefact) , modify corresponding sections in the configuration file.

Loaded ontologies (URL_TO_INSERT_TERM_4269 https://fairsharing.org/search?recordType=terminology_artefact)  will be updated to the latest version automatically by rebuilding the Docker image. 

#### 4.2 Rebuild OLS image and restart OLS 
Before rebuilding the Docker image, the existing container needs to be stopped (URL_TO_INSERT_RECORD_4270 https://fairsharing.org/FAIRsharing.31385c)  and removed. 

The OLS (URL_TO_INSERT_RECORD_4271 https://fairsharing.org/FAIRsharing.Mkl9RR)  container can be stopped (URL_TO_INSERT_RECORD_4272 https://fairsharing.org/FAIRsharing.31385c)  and removed by providing the container name. 

According to the parameters presented on the previous Docker creation command block, 
the name of the OLS (URL_TO_INSERT_RECORD_4273 https://fairsharing.org/FAIRsharing.Mkl9RR)  Docker container is "OLS (URL_TO_INSERT_RECORD_4274 https://fairsharing.org/FAIRsharing.Mkl9RR) ": 

```{warning}
By rebuilding the OLS image, all loaded ontologies will be automatically updated to the latest version.
```

```shell
## Stop OLS container
docker stop OLS

## Remove OLS container
docker rm OLS
```

The Docker container can also be stopped (URL_TO_INSERT_RECORD_4275 https://fairsharing.org/FAIRsharing.31385c)  and removed using the Docker image ID.

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

Loading multiple ontologies (URL_TO_INSERT_TERM_4276 https://fairsharing.org/search?recordType=terminology_artefact)  from disk:
    
If more than one ontology (URL_TO_INSERT_TERM_4277 https://fairsharing.org/search?recordType=terminology_artefact)  are going to be loaded into OLS (URL_TO_INSERT_RECORD_4278 https://fairsharing.org/FAIRsharing.Mkl9RR)  from disk, the **Dockerfile** needs modifying before 
building the Docker container again:

* At Line 3 of the configuration file, replace **ENV OLS (URL_TO_INSERT_RECORD_4281 https://fairsharing.org/FAIRsharing.Mkl9RR) _HOM (URL_TO_INSERT_RECORD_4283 https://fairsharing.org/FAIRsharing.efv7gw) E (URL_TO_INSERT_RECORD_4279 https://fairsharing.org/3502)  /opt/ols** with **ENV OLS (URL_TO_INSERT_RECORD_4282 https://fairsharing.org/FAIRsharing.Mkl9RR) _HOM (URL_TO_INSERT_RECORD_4284 https://fairsharing.org/FAIRsharing.efv7gw) E (URL_TO_INSERT_RECORD_4280 https://fairsharing.org/3502)  /opt/ols/**

* At Line 3 of the configuration file, replace

    ```bash
    && java -Dols.obofoundry.ontology (URL_TO_INSERT_TERM_4285 https://fairsharing.org/search?recordType=terminology_artefact) .config=foo.yaml -Dols.ontology.config=file://${OLS_HOME}/ols-config.yaml -jar ${OLS (URL_TO_INSERT_RECORD_4287 https://fairsharing.org/FAIRsharing.Mkl9RR) _HOM (URL_TO_INSERT_RECORD_4288 https://fairsharing.org/FAIRsharing.efv7gw) E (URL_TO_INSERT_RECORD_4286 https://fairsharing.org/3502) }/ols-config-importer.jar
    ```
    
    with:

    ```bash
    && java -Dols.obofoundry.ontology (URL_TO_INSERT_TERM_4289 https://fairsharing.org/search?recordType=terminology_artefact) .config=foo.yaml -Dols.ontology.config=file://${OLS_HOME}ols-config.yaml -jar ${OLS (URL_TO_INSERT_RECORD_4291 https://fairsharing.org/FAIRsharing.Mkl9RR) _HOM (URL_TO_INSERT_RECORD_4292 https://fairsharing.org/FAIRsharing.efv7gw) E (URL_TO_INSERT_RECORD_4290 https://fairsharing.org/3502) }ols-config-importer.jar
    ```
    
## Conclusion
The local OLS (URL_TO_INSERT_RECORD_4294 https://fairsharing.org/FAIRsharing.Mkl9RR)  provides API endpoints for retrieving, submitting, updating, and querying ontology (URL_TO_INSERT_TERM_4293 https://fairsharing.org/search?recordType=terminology_artefact)  data, as well as a 
user interface for search (URL_TO_INSERT_RECORD_4297 https://fairsharing.org/FAIRsharing.52b22c) ing and browsing ontologies (URL_TO_INSERT_TERM_4296 https://fairsharing.org/search?recordType=terminology_artefact)  and ontology (URL_TO_INSERT_TERM_4295 https://fairsharing.org/search?recordType=terminology_artefact)  terms.

For example, all ontologies (URL_TO_INSERT_TERM_4298 https://fairsharing.org/search?recordType=terminology_artefact)  loaded can be queried through endpoint **http://localhost:8080/api/ontologies**.

A detailed description of OLS (URL_TO_INSERT_RECORD_4299 https://fairsharing.org/FAIRsharing.Mkl9RR)  functions can be found in the built-in documentation page.

To customize the local OLS (URL_TO_INSERT_RECORD_4300 https://fairsharing.org/FAIRsharing.Mkl9RR)  user interface, for example, adding corporate logos, please check the OLS (URL_TO_INSERT_RECORD_4301 https://fairsharing.org/FAIRsharing.Mkl9RR)  source code
[here](https://github.com (URL_TO_INSERT_RECORD_4302 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/OLS). 

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
