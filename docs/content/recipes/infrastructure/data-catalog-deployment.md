# Deploying a data catalogue


<!-- **identifier:** UC9.1

**version:** [v0.1](v0.1)


___

**_Difficulty level:_** :triangular_flag_on_post: :triangular_flag_on_post: :triangular_flag_on_post:  :white_circle: :white_circle:

**_Reading time:_** 20 minutes (when the recipe is completed)

**_Intended Audience:_** 

> :heavy_check_mark: Software Engineer

> :heavy_check_mark: System Administrator

> :heavy_check_mark: Data Manager

**_Recipe Type_**: Service deployment

**_Executable code_**: No -->

___


<div class="row">

  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-qrcode fa-2x" style="color:#7e0038;"></i>
        <h4><b>Recipe metadata</b></h4>
        <p> identifier: <a href="">UC9.1</a> </p>
        <p> version: <a href="">v0.1</a> </p>
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
        <p><i class="fa fa-play-circle fa-lg" style="color:#fc7a4a;"></i> No</p>
      </div>
    </div>
  </div>
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-group fa-2x" style="color:#7e0038;"></i>
        <h4><b>Intended Audience</b></h4>
<!--         <p> <i class="fa fa-tags fa-lg" style="color:#7e0038;"></i> Terminology Managers </p> -->
        <p> <i class="fa fa-cogs fa-lg" style="color:#7e0038;"></i> Software Developers </p>
        <p> <i class="fa fa-database fa-lg" style="color:#7e0038;"></i> Data Managers </p>
        <p> <i class="fa fa-terminal fa-lg" style="color:#7e0038;"></i> System Administrators</p>
      </div>
    </div>
  </div>
</div>


___

## Main Objectives

This recipe is a step-by-step guide on how to deploy the IMI Data Catalogue in Docker. 

## Introduction

For a more general introduction to data catalogues, their elements and data models, see the [data catalogue recipe](link). This recipe is intended as a set of step-by-step instructions to deploy via Docker the IMI Data Catalogue developed at the Luxembourg Centre for Systems Biomedicine. The overall purpose of the data catalogue is to host dataset-level metadata for a wide range of IMI projects. Datasets are FAIRified and searchable by a range facets. The catalogue is not intended to hold the actual data, although it provides links to where the data is hosted, together with information on any access restrictions.

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

Thanks to `docker-compose`, it is possible to easily manage all the components (solr and web server) required to run the application.


## Step-by-step guide:

Unless otherwise specified, all the following commands should be run in a terminal *from the base directory of the data catalogue code*.

### 1. Building

`(local)` and `(web container)` indicate context of execution.

1. First, generate the certificates that will be used to enable HTTPS in reverse proxy. To do so, execute:

    ```bash
    $ cd docker/nginx/
$ ./generate_keys.sh
    ``` 
        
    >:warning: _Please note that if you run this command outside the `nginx` directory, the certificate and key will be generated in the wrong location._ 
        
    This command relies on OpenSSL. If you don't plan to use HTTPS or just want to see demo running, you can skip this.

    >:warning: - it would cause the HTTPS connection to be unsafe!

2. Return to the root directory (`$cd ../..`), then copy `datacatalog/settings.py.template` to `datacatalog/settings.py`. 

    ```bash
    $ cd ../..
$ cp datacatalog/settings.py.template datacatalog/settings.py
    ```

3. Edit the `settings.py` file to add a random string of characters in `SECRET_KEY` attribute. For maximum security, in `Python`, use the following to generate this key:

    ```python
    import os
    os.urandom(24)
    ```
    
4.  Build and start the docker containers by running:

    ```bash
    (local) $ docker-compose up --build
    ```
	
    That will create:
    * a container with `datacatalog web application`

    * a container for `Solr`
    
    > :thumbsup:  the data will be persistant between runs.

5. In a new terminal, to create `Solr` cores, do:

    ```bash
    (local) $ docker-compose exec solr solr create_core -c datacatalog
(local) $ docker-compose exec solr solr create_core -c datacatalog_test
    ```

6. Then, still in the second terminal, put Solr data into the cores:  

    ```bash
    (local) $ docker-compose exec web /bin/bash
(web container) $ python manage.py init_index 
(web container) $ python manage.py import_entities Json dataset 
    ```

    > :bell: to kill the container, press `CTRL+D` or type: `exit` from the terminal
	
7. The web application should now be available with loaded data via  http://localhost and https://localhost with ssl connection 

    > :warning: most browsers display a warning or block self-signed certificates. 


### 2. Maintenance of docker-compose
Docker container keeps the application in the state it was when  built. Therefore, **if you change any files in the project, the container has to be rebuilt in order to see changes in application** :

```shell=
$ docker-compose up --build
```

If you wanted to delete Solr data, you'd need to run:

```shell=
$ docker-compose down --volumes
```

This will remove any persisted data - you must redo `solr create_core` (see step 4 in the previous section) to recreate the Solr cores.

### 3. Modifying the datasets

The datasets are all defined in the file `tests/data/records.json`. This file can me modified to add, delete and modify datasets. **After saving the file, rebuild and restart docker-compose**.

First, to stop all the containers:

```shell=
$ CTRL+D
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

> :bell: to kill the container, press "`CTRL+D`" or type: "`exit`" from the terminal

---

## Single Docker deployment
In some cases, you might not want Solr and Nginx to run (for example, if there are **multiple instances** of `Data Catalog` running).
Then, simply use:

```shell=
(local) $ docker build . -t "data-catalog"
(local) $ docker run --name data-catalog --entrypoint "gunicorn" -p 5000:5000 -t data-catalog -t 600 -w 2 datacatalog:app --bind 0.0.0.0:5000
```

## Manual deployment

If you would prefer not to use Docker and compile and run the data catalogue manually instead, please follow the instructions in the [README file](https://github.com/FAIRplus/imi-data-catalogue/blob/master/README.md)

---
    
## Conclusion:

This recipe provides a step-by-step guide to deploying the `IMI data catalogue` developed at [University of Luxembourg](https://wwwen.uni.lu/lcsb), as parrt of [IMI FAIRplus](https://fairplus-project.eu/) to a local system.

> #### What should I read next?
> * [How to build a data catalogue?]()
> * [How to deploy the FAIRPORT data catalogue?]()
> * [What is search engine optimization?]()
> * [How to create a minimal information metadata profile?]()

 
---


## Authors:

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Danielle Welter |  LCSB, University of Luxembourg| [0000-0003-1058-2668](https://orcid.org/0000-0003-1058-2668) | Writing - Original Draft |
| Valentin Grouès | LCSB, University of Luxembourg |[0000-0001-6501-0806 ](https://orcid.org/0000-0001-6501-0806 )|Writing - Original Draft|
| Wei Gu | LCSB, University of Luxembourg |[0000-0003-3951-6680](https://orcid.org/0000-0003-3951-6680)|Writing - Review|
| Venkata Satagopam | LCSB, University of Luxembourg |[0000-0002-6532-5880](https://orcid.org/0000-0002-6532-5880)|Writing - Review|
| Philippe Rocca-Serra |  University of Oxford, Data Readiness Group| [0000-0001-9853-5668](https://orcid.org/0000-0001-9853-5668) | Writing - Review |


___


## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
