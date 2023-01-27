(fcb-infra-imi-cat-deploy)=
# Deploying the IMI data catalogue



````{panels_fairplus}
```` 


## Main Objectives

This recipe is a step-by-step guide on how to deploy the IMI Data Catalog(URL_TO_INSERT_RECORD https://datacatalog.elixir-luxembourg.org/)ue in Docker. 

## Introduction

For a more general introduction to data catalogues, their elements and data model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s, 
see the [data catalogue recipe](https://www.TODO.uldatacatalog.ul). 
This recipe is intended as a set of step-by-step instructions to deploy via Docker the IMI Data Catalog(URL_TO_INSERT_RECORD https://datacatalog.elixir-luxembourg.org/)ue
developed(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) at the Luxembourg Centre for Systems Biomedicine. The overall purpose of the data catalogue is to host 
dataset-level metadata for a wide range of IMI project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project)s. Datasets are FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)ified and search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)able by a range facets. 
The catalogue is not intended to hold the actual data, although it provides links to where the data is hosted, 
together with informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion on any access restrictions.

## Requirements

The following need to be installed on the machine the deployment is run on:
- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)


## Ingredients
- [IMI data catalogue code](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/FAIRplus/imi-data-catalogue) 

Check out the code to your local machine by running the following command in a terminal:

```shell
```

Thanks to **docker-compose**, it is possible to easily manage all the components (solr and web server) required to run
the application.


## Step-by-step guide

Unless otherwise specified, all the following commands should be run in a terminal *from the base directory of the data catalogue code*.

### Building

**(local)** and **(web container)** indicate context of execution.

* First, generate the certificates that will be used to enable HTTPS(URL_TO_INSERT_RECORD https://en.wikipedia.org/wiki/HTTPS) in reverse proxy. To do so, execute:

```bash
``` 
 
````{warning}       

```{warning}
⚡ However, be aware that skipping this would cause the HTTPS(URL_TO_INSERT_RECORD https://en.wikipedia.org/wiki/HTTPS) connection to be unsafe!
```

````

* Return to the root directory (`$cd ../..`), then copy **datacatalog/settings.py.template** to **datacatalog/settings.py**. 

```bash
```

* Edit the **settings.py** file to add a random string(URL_TO_INSERT_RECORD https://string-db.org/) of characters in **SECRET_KEY** attribute. For maximum security,
in **Python**, use the following to generate this key:

```python
```
    
* Build and start the docker containers by running:

```bash
```
	
    That will create:
    * a container with `datacatalog web application`

    * a container for `Solr`
 
```{note} 
```


* In a new terminal, to create `Solr` core(URL_TO_INSERT_RECORD http://purl.uniprot.org/core/)(URL_TO_INSERT_RECORD https://core.ac.uk)s, do:

```bash
```

* Then, still in the second terminal, put Solr data into the core(URL_TO_INSERT_RECORD http://purl.uniprot.org/core/)(URL_TO_INSERT_RECORD https://core.ac.uk)s:  

```bash
```

```bash
```

```{admonition} Tip
```
	
* The web application should now be available with loaded data via  http://localhost and https://localhost with ssl connection 
 
```{warning}
```

### Maintenance of docker-compose
Docker container keeps the application in the state it was when  built. Therefore, **if you change any files in 
the project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project), the container has to be rebuilt in order to see changes in application** :

```shell
```

If you wanted to delete Solr data, you'd need to run:

```shell
```

This will remove any persisted data - you must redo **solr create_core(URL_TO_INSERT_RECORD http://purl.uniprot.org/core/)(URL_TO_INSERT_RECORD https://core.ac.uk)** (see step 4 in the previous section) to 
recreate the Solr core(URL_TO_INSERT_RECORD http://purl.uniprot.org/core/)(URL_TO_INSERT_RECORD https://core.ac.uk)s.

### Modifying the datasets

The datasets are all defined in the file **tests/data/records.json**. This file can be modified to add, 
delete and modify datasets. **After saving the file, rebuild and restart docker-compose**.

First, to stop all the containers:

```shell
```

Then rebuild and restart the containers:

```shell
```

Finally, reindex the datasets using:

```shell
```

```shell
```


```{admonition} Tip
```

---

## Single Docker deployment
In some cases, you might not want Solr and Nginx to run (for example, if there are **multiple instances** of
**Data Catalog** running).
Then, simply use:

```shell
```

## Manual deployment

If you'd rather not to use Docker and compile and run the data catalogue manually instead, please follow the
instructions in the [README file](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/FAIRplus/imi-data-catalogue/blob/master/README.md)

---
    
## Conclusion

This recipe provides a step-by-step guide to deploying the **IMI data catalogue** developed(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) at [University of Luxembourg](https://wwwen.uni.lu/lcsb),
as part of [IMI FAIRplus](https://fairplus-project.eu/) to a local system.

### What to read next?

* {ref}`fcb-infra-build-catalog`
* How to deploy the FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)PO(URL_TO_INSERT_RECORD http://plantontology.org/)(URL_TO_INSERT_RECORD https://bioportal.bioontology.org/ontologies/RPO)RT data catalogue?<!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO add a link to corresponding document --> (*in preparation*)
* {ref}`fcb-find-seo`
* {ref}`fcb-interop-metadataprofile`
* {ref}`fcb-interop-txmetadata`

````{rdmkit_panel}
````
## References
````{dropdown} **References**
````

## Authors

````{authors_fairplus}
````

## License

````{license_fairplus}
````
