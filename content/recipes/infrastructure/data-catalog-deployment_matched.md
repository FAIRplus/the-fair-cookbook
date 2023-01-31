(fcb-infra-imi-cat-deploy)=
# Deploying the IMI data catalogue



````{panels_fairplus}
:identifier_text: FCB048
:identifier_link: 'https://w3id.org/faircookbook/FCB048'
:difficulty_level: 3
:recipe_type: hands_on
:reading_time_minutes: 20
:intended_audience: software_developer, data_manager, system_administrator  
:maturity_level: 0
:maturity_indicator: 0
:has_executable_code: yeah
:recipe_name: Deploying a data catalogue - The IMI data catalogue example
```` 


## Main Objectives

This recipe is a step-by-step guide on how to deploy the IMI Data Catalog (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.de533c) ue in Docker. 

## Introduction

For a more general introduction to data catalogues, their elements and data model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) s, 
see the [data catalogue recipe](https://www.TODO.uldatacatalog.ul). 
This recipe is intended as a set of step-by-step instructions to deploy via Docker the IMI Data Catalog (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.de533c) ue
developed (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.31385c)  at the Luxembourg Centre for Systems Biomedicine. The overall purpose of the data catalogue is to host 
dataset-level metadata for a wide range of IMI project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project) s. Datasets are FAIR (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.WWI10U) ified and search (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.52b22c) able by a range facets. 
The catalogue is not intended to hold the actual data, although it provides links to where the data is hosted, 
together with informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion on any access restrictions.

## Requirements

The following need to be installed on the machine the deployment is run on:
- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)


## Ingredients
- [IMI data catalogue code](https://github.com (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.c55d5e) /FAIRplus/imi-data-catalogue) 

Check out the code to your local machine by running the following command in a terminal:

```shell
$ git clone git@github.com:FAIRplus/imi-data-catalogue.git
```

Thanks to **docker-compose**, it is possible to easily manage all the components (solr and web server) required to run
the application.


## Step-by-step guide

Unless otherwise specified, all the following commands should be run in a terminal *from the base directory of the data catalogue code*.

### Building

**(local)** and **(web container)** indicate context of execution.

* First, generate the certificates that will be used to enable HTTPS (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.cd2f9e)  in reverse proxy. To do so, execute:

```bash
$ cd docker/nginx/
$ ./generate_keys.sh
``` 
 
````{warning}       
⚡ _Please note that if you run this command outside the `nginx` directory, the certificate and key will be generated in the wrong location._         
This command relies on OpenSSL. If you don't plan to use HTTPS or just want to see demo running, you can skip this.

```{warning}
⚡ However, be aware that skipping this would cause the HTTPS (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.cd2f9e)  connection to be unsafe!
```

````

* Return to the root directory (`$cd ../..`), then copy **datacatalog/settings.py.template** to **datacatalog/settings.py**. 

```bash
$ cd ../..
$ cp datacatalog/settings.py.template datacatalog/settings.py
```

* Edit the **settings.py** file to add a random string (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9b7wvk)  of characters in **SECRET_KEY** attribute. For maximum security,
in **Python**, use the following to generate this key:

```python
import os
os.urandom(24)
```
    
* Build and start the docker containers by running:

```bash
(local) $ docker-compose up --build
```
	
    That will create:
    * a container with `datacatalog web application`

    * a container for `Solr`
 
```{note} 
> ⚡ the data will be persistant between runs.
```


* In a new terminal, to create `Solr` core (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.xMmOCL) s, do:

```bash
(local) $ docker-compose exec solr solr create_core -c datacatalog
(local) $ docker-compose exec solr solr create_core -c datacatalog_test
```

* Then, still in the second terminal, put Solr data into the core (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.xMmOCL) s:  

```bash
(local) $ docker-compose exec web /bin/bash
```

```bash
(web container) $ python manage.py init_index 
(web container) $ python manage.py import_entities Json dataset 
```

```{admonition} Tip
:class: tip
> ⚡ to kill the container, press "`CTRL+D`" or type: "`exit`" from the terminal
```
	
* The web application should now be available with loaded data via  http://localhost and https://localhost with ssl connection 
 
```{warning}
⚡ - Most browsers display a warning or block self-signed certificates. 
```

### Maintenance of docker-compose
Docker container keeps the application in the state it was when  built. Therefore, **if you change any files in 
the project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project) , the container has to be rebuilt in order to see changes in application** :

```shell
$ docker-compose up --build
```

If you wanted to delete Solr data, you'd need to run:

```shell
$ docker-compose down --volumes
```

This will remove any persisted data - you must redo **solr create_core (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.xMmOCL) ** (see step 4 in the previous section) to 
recreate the Solr core (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.xMmOCL) s.

### Modifying the datasets

The datasets are all defined in the file **tests/data/records.json**. This file can be modified to add, 
delete and modify datasets. **After saving the file, rebuild and restart docker-compose**.

First, to stop all the containers:

```shell
$ CTRL+D
```

Then rebuild and restart the containers:

```shell
$ docker-compose up --build
```

Finally, reindex the datasets using:

```shell
(local) $ docker-compose exec web /bin/bash
```

```shell
(web container) $ python manage.py import_entities Json dataset 
```


```{admonition} Tip
:class: tip
> ⚡ to kill the container, press "`CTRL+D`" or type: "`exit`" from the terminal
```

---

## Single Docker deployment
In some cases, you might not want Solr and Nginx to run (for example, if there are **multiple instances** of
**Data Catalog** running).
Then, simply use:

```shell
(local) $ docker build . -t "data-catalog"
(local) $ docker run --name data-catalog --entrypoint "gunicorn" -p 5000:5000 -t data-catalog -t 600 -w 2 datacatalog:app --bind 0.0.0.0:5000
```

## Manual deployment

If you'd rather not to use Docker and compile and run the data catalogue manually instead, please follow the
instructions in the [README file](https://github.com (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.c55d5e) /FAIRplus/imi-data-catalogue/blob/master/README.md)

---
    
## Conclusion

This recipe provides a step-by-step guide to deploying the **IMI data catalogue** developed (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.31385c)  at [University of Luxembourg](https://wwwen.uni.lu/lcsb),
as part of [IMI FAIRplus](https://fairplus-project.eu/) to a local system.

### What to read next?

* {ref}`fcb-infra-build-catalog`
* How to deploy the FAIR (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.WWI10U) PO (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.3ngg40)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.x9s8e) RT data catalogue?<!-- TO (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.w69t6r) DO add a link to corresponding document --> (*in preparation*)
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
Danielle: Writing - Original Draft
Valentin: Writing - Original Draft
Wei: Writing - Review & Editing
Venkata: Writing - Review & Editing
Philippe: Writing - Review & Editing
````

## License

````{license_fairplus}
CC-BY-4.0
````
