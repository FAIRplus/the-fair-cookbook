# Deploying a data catalogue


**identifier:**

**version:** [v0.1](v0.1)


___

**_Difficulty level:_** :triangular_flag_on_post: :triangular_flag_on_post: :triangular_flag_on_post:  :white_circle: :white_circle:

**_Reading time:_** 20 minutes (when the recipe is completed)

**_Intended Audience:_** 

> :heavy_check_mark: Data Managers

> :heavy_check_mark: Software Engineer

> :heavy_check_mark: System Administrator


**_Recipe Type_**: Service deployment

**_Executable code_**: No

___

## Main Objectives

This recipe is a step-by-step guide on how to deploy the IMI Data Catalogue in Docker. 

## Introduction

## Requirements

The following need to be installed on the machine the deployment is run on:
- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)




## Ingredients
- [IMI data catalogue code](https://github.com/FAIRplus/imi-data-catalogue) 

Check out the code to your local machine by running the following command in a terminal:

```shell
$ git clone git@github.com:FAIRplus/imi-data-catalogue.git
```


## Step-by-step guide:

Unless otherwise specified, all the following commands should be run in a terminal from the base directory of the data catalogue code.

### 1. Building

`(local)` and `(web container)` indicate context of execution.

1. First, generate the certificates that will be used to enable HTTPS in reverse proxy. To do so, execute:

    ```shell=
    $ docker/nginx/generate_keys.sh
    ``` 
    
    This relies on OpenSSL. If you don't plan to use HTTPS or just want to see demo running, you can skip this (warning - it would cause the HTTPS connection to be unsafe!).

1. Then, copy `datacatalog/settings.py.template` to `datacatalog/settings.py`. Edit the `settings.py` file to add a random string of characters in `SECRET_KEY` and then run:

	```shell=
	(local) $ docker-compose up --build
	```
	
	That will create a container with datacatalog web application, and a container for solr (the data will be persisted between runs).

1. In a new terminal, to create Solr cores:

	```shell=
	(local) $ docker-compose exec solr solr create_core -c datacatalog
	(local) $ docker-compose exec solr solr create_core -c datacatalog_test
	```

1. Then, still in the second terminal, put Solr data into the cores:  

	```shell=
	(local) $ docker-compose exec web /bin/bash
	(web container) $ python manage.py init_index 
	(web container) $ python manage.py import_entities Json dataset 
	```
	(PRESS CTRL+D or type: "exit" to kill the container)
	
1. The web application should now be available with loaded data via  http://0.0.0.0:5000/ or https://localhost 



### 2. Maintenance of docker-compose
Docker container keeps the application in the state that it has been when it was built. 
Therefore, if you change any files in the project, in order to see changes in application the container has to be rebuilt:

```shell=
$ docker-compose up --build
```

If you wanted to delete Solr data, you need to run (that will remove any persisted data - you must redo `solr create_core`):

```shell=
$ docker-compose down --volumes
```

### 3. Modifying the datasets

The datasets are all defined in the file `tests/data/records.json`. This file can me modified to add, delete and modify datasets. After saving the file, rebuild and restart docker-compose.

First, to stop all the containers:

```shell=
$ CTLR+D
```
Then rebuild and restart the containers:
```shell=
$ docker-compose up --build
```

Finally, reindex the datasets using:
```shell=
(local) $ docker-compose exec web /bin/bash
(web container) $ python manage.py import_entities Json dataset 
```
(PRESS CTRL+D or type: "exit" to to kill the container)


## Single Docker deployment
In some cases, you might not want Solr and Nginx to run (for example if there are multiple instances of Data Catalog runnning).
Then, simply use:

```shell=
(local) $ docker build . -t "data-catalog"
(local) $ docker run --name data-catalog --entrypoint "gunicorn" -p 5000:5000 -t data-catalog -t 600 -w 2 datacatalog:app --bind 0.0.0.0:5000
```

## Manual deployment

If you would prefer not to use Docker and compile and run the data catalogue manually instead, please follow the instructions in the [README file](https://github.com/FAIRplus/imi-data-catalogue/)
    
## Summary

This recipe provides a step-by-step guide to deploying the IMI data catalogue to a local system. 


 



## Authors:

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Danielle Welter |  LCSB, University of Luxembourg| [0000-0003-1058-2668](https://orcid.org/orcid.org/0000-0003-1058-2668) | Writing - Original Draft |
| Valentin Grouès | LCSB, University of Luxembourg |||
| Wei Gu | LCSB, University of Luxembourg |||
| Philippe Rocca-Serra ||||


___


## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
