# Deploying a data catalogue


**identifier:**

**version:** [v0.1](v0.1)


___

**_Difficulty level:_** :triangular_flag_on_post: :triangular_flag_on_post: :triangular_flag_on_post:  :triangular_flag_on_post: :white_circle:

**_Reading time:_** 20 minutes (when the recipe is completed)

**_Intended Audience:_** 

> :heavy_check_mark: Data Managers

> :heavy_check_mark: Software Engineer

> :heavy_check_mark: System Administrator

> :heavy_check_mark: Data Scientists


**_Recipe Type_**: Service deployment

**_Executable code_**: Yes

___

## Main Objectives

This recipe is a step-by-step guide on how to deploy the IMI Data Catalogue in Docker. 

## Introduction

## Requirements

Docker
Git



## Ingredients
- [OLS Docker image](https://github.com/EBISPOT/OLS-docker) 


## Step-by-step guide:


### Building

`(local)` and `(web container)` indicate context of execution.

1. First, generate the certificates that will be used to enable HTTPS in reverse proxy. To do so, execute `deploy/nginx/generate_keys.sh` (relies on OpenSSL).
If you don't plan to use HTTPS or just want to see demo running, you can skip this (warning - it would cause the HTTPS connection to be unsafe!).

1. Then, copy `settings.py.template` to `settings.py`. Edit the `settings.py` file to add a random string of characters in `SECRET_KEY` and then run:

	```
	(local) $ docker-compose up --build
	```
	
	That will create a container with datacatalog web application, and a container for solr (the data will be persisted between runs).

1. Then, to create solr cores, execute in another console:

	```
	(local) $ docker-compose exec solr solr create_core -c datacatalog
	(local) $ docker-compose exec solr solr create_core -c datacatalog_test
	
	```

1. Then, to fill solr data:  

	```
	(local) $ docker-compose exec web /bin/bash
	(web container) $ python manage.py init_index 
	(web container) $ python manage.py import_entities Json dataset 
	
	(PRESS CTRL+D or type: "exit" to exit)
	```
1. The web application should now be available with loaded data via https://localhost  

### Maintenance of docker-compose
Docker container keeps the application in the state that it has been when it was built. 
Therefore, if you change any files in the project, in order to see changes in application the container has to be rebuilt:

```
docker-compose up --build
```

If you wanted to delete solr data, you need to run (that will remove any persisted data - you must redo `solr create_core`):

```
docker-compose down --volumes
```

### Modifying the datasets

The datasets are all defined in the file `tests/data/records.json`.
This file can me modified to add, delete and modify datasets.
After saving the file, rebuild and restart docker-compose with:

```
CTLR+D
```
to stop all the containers

```
docker-compose up --build
```
to rebuild and restart the containers

```
(local) $ docker-compose exec web /bin/bash
(web container) $ python manage.py import_entities Json dataset 

(PRESS CTRL+D or type: "exit" to exit)
```
To reindex the datasets

## Single Docker deployment
In some cases, you might not want Solr and Nginx to run (for example if there are multiple instances of Data Catalog runnning).
Then, simply use:

```
(local) $ docker build . -t "data-catalog"
(local) $ docker run --name data-catalog --entrypoint "gunicorn" -p 5000:5000 -t data-catalog -t 600 -w 2 datacatalog:app --bind 0.0.0.0:5000
```


### 1. Install dependencies

- Unix-based environment (macOS, Linux):

|Software|Description|Version|Installation|
|--|--|--|--|
|Git|Get the versioned source file|2.17.1 |[Official guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)|
|Docker|Deliver software in containers|18.09.01 |[Official guide](https://docs.docker.com/install/)|


### 2. Load ontologies into OLS 
### 3. Set up OLS in the local environment 
>For Windows machines, run the Docker Desktop app to start the Docker daemon.



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

    
## Summary




To customize the local OLS user interface, for example, adding corporate logos, please check the OLS source code [here](https://github.com/EBISPOT/OLS). 



## References:



## Authors:

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Danielle Welter |  LCSB, University of Luxembourg| [0000-0003-1058-2668](https://orcid.org/orcid.org/0000-0003-1058-2668) | Writing - Original Draft |
| Valentin Groues | LCSB, University of Luxembourg |||
| Wei Gu | LCSB, University of Luxembourg |||
| Philippe Rocca-Serra ||||


___


## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
