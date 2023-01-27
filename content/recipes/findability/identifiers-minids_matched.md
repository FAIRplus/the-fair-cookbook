(fcb-find-id-minid)=
# Minting identifiers with Minid


````{panels_fairplus}
```` 


## Main Objectives

The main purpose of this recipe is:

To create a **persistent**, **globally unique** and **resolvable identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)** using the ***Minid client*** accessing the Minid 2.0 release {footcite}`Madduri2019` {footcite}`minid-identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s`.

---


## Graphical Overview

<!--  <div><img src="./images/minid-mermaid.png" width="650px" style="padding:1px;border:thin solid black;"/></div>   -->



<!-- <div><img src="https://github.com(URL_TO_INSERT_RECORD https://github.com/)/nih-cfde/the-fair-cookbook/blob/master/content/recipes/08/2/images/minid-mermaid.png?raw=true" alt="drawing" style="border:1px solid black;" width="650"  align="top" /></div>
 -->

````{dropdown} 
```{figure} identifiers-minids-fig1.png
---
height: 550px
name: Minting Minid
alt: An overview of the identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) minting process
---
An overview of the identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) minting process.
```
````



---

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [service invokation](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/operation_3763)  | [file](http://purl.obolibrary.org/obo/STATO_0000002)  | [guid](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/data_0976)  |

---


## Installing the minid 2.0 client

This is a prerequisite to be able to call the minid API hosted on a server at the following url [http://minid.bd2k.org/minid](http://minid.bd2k.org/minid)

### installing with pip

```python
```

### building from source:

use the dev branch to obtain to source
[minid github(URL_TO_INSERT_RECORD https://github.com/) repository (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository)](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/fair-research/minid)

---

## Configuration


1. prerequisite: create a minig-config.cfg file
  
  As a convenience you need specify this informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion in a minid configuration file (`~/.minid/minid-config.cfg`)
  To do so from the command line, issue the following:

```bash
```


2. Create a GlobusID account
  
  Before using the API you first need to create a [globus account](https://www.globusid.org/create)
  <!-- <kbd>![](./images/globus/globus-account-create.png)<kbd/> -->

 <!--  <div><img src="./images/globus/globus-account-create.png" width="900px" style="padding:1px;border:thin solid black;"/></div>   -->
<!-- <div>
  <img src="https://github.com(URL_TO_INSERT_RECORD https://github.com/)/nih-cfde/the-fair-cookbook/blob/dev/content/recipes/08/2/images/globus/globus-account-create.png?raw=true" alt="drawing" style="border:1px solid black;" width="650"  align="top" />
</div> 
 -->
  <!-- ![](/images/B5UbkpF.png) -->

````{dropdown} 
```{figure} ../../../images/globus-account-create.png
---
height: 500px
name: Creating a Globus account
alt: Creating a Globus account
---
Creating a Globus account.
```
````






  and validate your email address, as part of the registration process. A unique code will be sent to your email address. You must present this code along with your email address when accessing the API.


3. Accessing minid service from the command line
  
  With the completion of the previous steps, you are now ready to use the minid service. The first thing to do is to invoke to `minid login` command

  
  ```bash
  $ minid login
  ```

  This will open the GlobusID login page. Simply enter your credentials obtained from 2.

<!-- ![](./images/globus/globus-account-login.png) -->
<!-- ![](/images/2OZFcJa.png) -->
<!-- <div>
<img src="./images/globus/globus-account-login.png" width="900px" style="padding:1px;border:thin solid black;"/>
</div>  -->
<!-- <div>
  <img src="https://github.com(URL_TO_INSERT_RECORD https://github.com/)/nih-cfde/the-fair-cookbook/blob/dev/content/recipes/08/2/images/globus/globus-account-login.png?raw=true" alt="drawing" style="border:1px solid black;" width="750"  align="top" />
</div>  -->

````{dropdown} 
```{figure} ../../../images/globus-account-login.png
---
height: 250px
name: Globus account login
alt: Globus account login
---
Globus account login.
```
````
  
  followed by:

<!-- ![](./images/globus/globus-account-allow.png) -->
<!-- ![](/images/avzyAFZ.png) -->
<!-- <div>
<img src="./images/globus/globus-account-allow.png" width="900px" style="padding:1px;border:thin solid black;"/>
</div>  -->
<!-- <div>
<img src="https://github.com(URL_TO_INSERT_RECORD https://github.com/)/nih-cfde/the-fair-cookbook/blob/dev/content/recipes/08/2/images/globus/globus-account-allow.png?raw=true" width="900px" style="padding:1px;border:thin solid black;"/>
</div> -->

````{dropdown} 
```{figure} ../../../images/globus-account-allow.png
---
height: 550px
name: Globus account allow
alt: Globus account allow
---
Globus account allow.
```
````
  
  If all goes well, the following browser screen will be shown:

<!-- ![](./images/globus/globus-account-login-success.png) -->
<!-- ![](/images/THYPg4E.png) -->
<!-- <div>
<img src="./images/globus/globus-account-login-success.png" width="650px" style="padding:1px;border:thin solid black;"/>
</div>  -->
<!-- <div>
<img src="https://github.com(URL_TO_INSERT_RECORD https://github.com/)/nih-cfde/the-fair-cookbook/blob/dev/content/recipes/08/2/images/globus/globus-account-login-success.png?raw=true" width="900px" style="padding:1px;border:thin solid black;"/>
</div>
 -->


````{dropdown} 
```{figure} ../../../images/globus-account-login-success.png
---
height: 200px
name: Globus account login success
alt: Globus account login success
---
Globus account login success.
```
````
  
  While the terminal will show the following:

  ```bash
  You have been logged in.
  ```

  This means you are now ready to use the minid service from the command line.

-----

## Usage


The CL(URL_TO_INSERT_RECORD https://github.com/obophenotype/cell-ontology)I supports the following simple operations (Note: the `--test` flag creates names in a test namespace that is removed periodically; remove that flag to create production minids.):

* Check a known minid identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)

```bash
```

if everything is setup correctly, the command will return:

```bash
```

* Create a new identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) (the `--location` option, if provided, must be at the end).

```bash
```

* Update metadata about an identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema):

```bash
```

*  View all minid options:

```bash
```

Landing pages are accessible via the minid website: [http://minid.bd2k.org/minid/landingpage/\<identifier\>](http://minid.bd2k.org/minid/landingpage/\<identifier\>).

---

### file manifest format


Minids can only be assigned to a single file. In order to assign a minid to a collection (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=collection) of files, we recommend using a `BDBag <https://github.com(URL_TO_INSERT_RECORD https://github.com/)/ini-bdds/bdbag>`_ or the minid file manifest format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format).

The minid file manifest format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) is a JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259)-based format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) that enumerates a list of files as JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) objects that have the following attributes:


* length: The length of the file in bytes.

* filename: The filename (or path) relative to the manifest file.

* One or more (only one of each) of the following `algorithm:checksum` key-value pairs:

  * md5:\<md5 hex value\>

  * sha256:\<sha256 hex value\>

  * sha512:\<sha512 hex value\>

* url: the URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630) to the file.

The manifest may be used to create a minid for a collection (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=collection) of files or alternatively as input to the minid batch-register command.

Below is a sample file manifest configuration file:

```bash
```

## Conclusions

Using the `Minid` service, resources can now generate stable, resolvable identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s for their digitial documents. The `Minid` service thus provides a key component to enable `interoperability` and `reusability` by ensuring digital assets can be looked up using a standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) protocol (HTTP request). The service also supports data integrity checks thanks to the native support of checksumming functions, with sha256 being recommended.


## References
````{dropdown} **References**
```{footbibliography}
```
````


<!-- 1. Madduri R, Chard K, D’Arcy M, Jung SC, Rodriguez A, Sulakhe D, et al. (2019) Reproducible big data science: A case study in continuous FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)ness. PLoS ONE(URL_TO_INSERT_RECORD https://www.strobe-nut.ugent.be/content/strobe-nut-ontology) 14(4): e0213013. https://doi.org/10.1371/journal.pone.0213013

2. https://minid.readthedocs.io/en/develop/identifiers.html#minids-vs-handles -->


## Authors

````{authors_fairplus}
````

## License

````{license_fairplus}
````
