# Deposition to Zenodo Archive

<!-- **identifier:** [RX.X](RX.X)

**version:** [v1.0](v1.0)

___

**_Difficulty level:_** easy :triangular_flag_on_post: :triangular_flag_on_post: :white_circle:  :white_circle: :white_circle:

**_Reading time:_** 15 minutes 

**_Intended Audience:_** 

> :heavy_check_mark: Principal Investigators

> :heavy_check_mark: Data Managers

> :heavy_check_mark: Data Scientists

> :heavy_check_mark: Funders

**_Recipe Type_**: Hands on

**_Executable code_**: Yes -->

___


<div class="row">

  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-qrcode fa-2x" style="color:#7e0038;"></i>
        <h4><b>Recipe metadata</b></h4>
        <p> identifier: <a href="">RX.X</a> </p>
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
        <i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
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
        <p><i class="fa fa-clock-o fa-lg" style="color:#7e0038;"></i> 15 minutes</p>
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
        <p> <i class="fa fa-user-md fa-lg" style="color:#7e0038;"></i> Principal Investigators </p>
        <p> <i class="fa fa-database fa-lg" style="color:#7e0038;"></i> Data Managers </p>
        <p> <i class="fa fa-wrench fa-lg" style="color:#7e0038;"></i> Data Scientists </p>
        <p> <i class="fa fa-money fa-lg" style="color:#7e0038;"></i> Funders</p>
      </div>
    </div>
  </div>
</div>
 



___

# Table of Contents
1. [Main FAIRification Objectives](#Main%20FAIRification%20Objectives)
2. [Graphical Overview of the FAIRification Recipe Objectives](#Graphical%20Overview%20of%20the%20FAIRification%20Recipe%20Objectives)
3. [FAIRification Objectives, Inputs and Outputs](#FAIRification%20Objectives,%20Inputs%20and%20Outputs)
4. [Capability & Maturity Table](#Capability%20&%20Maturity%20Table)
5. [Table of Data Standards](#Table%20of%20Data%20Standards)
6. [Executable Code in Notebook](#Executable%20Code%20in%20Notebook)
7. [How to create workflow figures](#How%20to%20create%20workflow%20figures)
8. [License](#License)

---

## Main Objectives

The main purpose of this recipe is:

> To show how to take advantage of CERN Zenodo repository to document the existence of datasets, thus increasing its findeability. This is of particular relevant for IMI projects since Zenodo is aimed to support the European Commission (EC) nascent Open Data policy and is commissioned by the EC.

___
## Graphical Overview of the FAIRification Recipe Objectives

TODO:
___

## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Findability | minimal | repeatable |

----
## Introduction to Zenodo repository

### What is Zenodo?

Zenodo is a repository developed by [CERN](https://home.cern/), under the [OpenAire](https://www.openaire.eu/) program which focus is on **open data**. It was commissioned by the EC to support their nascent Open Data policy by providing a catch-all repository for EC funded research. This of particular relevance for all projects funded under the `Innovative Medicine Initiative (IMI)`.

### Why use Zenodo?

To cite `Zenodo's documentation`, here are a few reasons why using the repository services provides a `low entry barrier` to making data findable:
* Safe — your research is stored safely for the future in CERN’s Data Centre for as long as CERN exists.
* Trusted — built and operated by CERN and OpenAIRE to ensure that everyone can join in Open Science.
* Citeable — every upload is assigned a Digital Object Identifier (DOI), to make them citable and trackable.
* No waiting time — Uploads are made available online as soon as you hit publish, and your DOI is registered within seconds.
* Open or closed — Share e.g. anonymized clinical trial data with only medical professionals via our restricted access mode.
* Versioning — Easily update your dataset with our versioning feature.
* GitHub integration — Easily preserve your GitHub repository in Zenodo.
* Usage statisics — All uploads display standards compliant usage statistics


## 1. How to use Zenodo Deposition Web Interface?

This section guides users through the key steps to perform to organize a deposition to Zenodo using the user interface web component provided by the repository.

---

### Zenodo Compatible Data Collection - Login-in

* Login via ORCID or Github credentials

[Zenodo](https://zenodo.org/) has integrated authentication mechanism key partners such as [github](https://github.com)  and [Orcid](https://orcid.org). For [IMI](https://imi.org) and for [FAIRplus](https://fairplus-project.eu), this means that consortium members can easyly login if they already have credentials on these 2 services. 


---

### Zenodo Compatible Data Collection - Data upload

<div> <img src="https://i.imgur.com/TYpr8jM.png" alt="drawing" style="width:650px;" border="1px solid black" align="top" />
</div>

Files can be dragged and dropped, with the following limitations:
* 5GB max each, 
* 50 GB total / dataset


After adding the set of files associated with the submission, the upload should be initiated by the pressing the `start upload` green button.
Failing to do so will result in a failure to proceed with the submission and an error will be thrown, reminding users to do so.

<img src="https://i.imgur.com/LwMorlw.png" alt="drawing" style="width:650px;" border="1px solid black" align="top" />


:warning:

The next key step is to select the `upload type`. In this instance, the `Dataset` is selected. This matters as it provide strong typing which is relied on by `search engine` and therefore impacts `findability`.



<img src="https://i.imgur.com/OYyz4dT.png" alt="drawing" style="width:500px;" border="1px solid black" align="top" />

---

### Zenodo Compatible Data Collection - Providing Metadata

* Basic metadata such as. `title`, `description`, at minima should be provided.
* Authors should be identified, ideally using their `orcid`, so linking can be performed. This impacts authors citation and impact evaluation. For IMI FAIRplus participants, since all have now such an identifier, the link should be made systematically.

<img src="https://i.imgur.com/WmlqBjL.png" alt="drawing" style="width:700px;" border="1px solid black" align="top" />


* **Reserve a Digital Object Identifier**: This is a service provided natively by the Zenodo service owing the integration with Datacite services. This is quite an important point as it means the a Zenodo submission can be cited. However, remember to carefully review all the data entered in the form as once a doi has been minted, the associated information **can not be changed without creating a new version of the archive and therefore minting a new doi**
 


* 'Keywords' can be adding to tag the submission. These are free text and no controlled terminology can be used in the interface at the moment.

<img src="https://i.imgur.com/9Bp91gX.png" alt="drawing" style="width:700px;" border="1px solid black" align="top" />


---

###  Zenodo Compatible Data Collection - Access and License informatioon

* Zenodo provides facilities to set `Access Conditions` and `License`, `Data Controler Contact Information`, as well as `Embargo Duration` if applicable
* As indicated above, it is possible to `set an Embargo Period`, if the option `embargoed access` is selected under the `Access right` section.

<img src="https://i.imgur.com/fSxOjXe.png" alt="drawing" style="width:750px;" border="1px solid black" align="top" />


  * Zenodo places to no limit when it comes to duration of the embargo period. So submitters should check EC and IMI guidelines or local institutional requirements for guidance.


* Setting Access Conditions/License, Data Controler Contact Information, Embargo Duration if applicable

<img src="https://i.imgur.com/ty9rpXF.png" alt="drawing" style="width:750px;" border="1px solid black" align="top" />


* Start typing to display more licenses available from Zenodo

<img src="https://i.imgur.com/249GhMg.png" alt="drawing" style="width:550px;" border="1px solid black" align="top"/>

---
### Zenodo Compatible Data Collection - Funding Information

Since Zenodo mission is to collect EC funded data, the repository provides the means to lookup `Grant Information`:

<img src="https://i.imgur.com/STjyFbT.png" alt="drawing" style="width:700px;" border="1px solid black" align="top" />
  
  * Zenodo: openAIRE connected repository

  * Connected to funding agencies

---
### Zenodo Compatible Data Collection - Miscellaneous Information

* Miscellaneous Information:

<img src="https://i.imgur.com/uhGZN5t.png" alt="drawing" style="width:700px;" border="1px solid black" align="top" />

  * Contributors

  * References:

  * Journal, Conference, Book, and so on.



## 2. Programmatic Deposition to Zenodo via the REST-API: 

### Create a zenodo account and obtain an API token

* First, it is necessary to obtain an api key:

    `ACCESS_TOKEN` = "<enter-your_writeonly_token_for_testing or your_deposit_token if you want to get a DOI  >"

* Then, the following code invoking the Zenodo REST endpoint will allow deposition:

    ```python
    import requests
    import json

    zenodo_baseurl = "https://zenodo.org/api/"
    headers = {"Content-Type": "application/json"}

    ACCESS_TOKEN = "<YOUR_TOKEN_GOES_HERE>"
    # testing the connection
    r = requests.get("https://zenodo.org/api/deposit/depositions", params={"access_token": ACCESS_TOKEN})

    # creating an empty submission to get an zenodo record id:
    r = requests.post('https://zenodo.org/api/deposit/depositions', params={'access_token': ACCESS_TOKEN}, json={},
                      headers=headers)
    r.status_code

    # obtain the zenodo metadata payload as json containing the id
    r.json()
    ```

### Create the payload for the programmatic deposition.

*  For example, it can be obtained by parsing the content of a metadata template or from a dedicated acquisition form specifically made by a `data manager`

    ```python
    # getting the record id
    deposition_id = r.json()['id']

    # uploading the data

    data = {'filename': 'rose-aroma-naturegenetics2018-treatment-group-mean-sem-report-datapackage.json'}
    files = {'file': open('../data/processed/rose-data/rose-aroma-naturegenetics2018-treatment-group-mean-sem-report-datapackage.json', 'rb')}
    r = requests.post('https://zenodo.org/api/deposit/depositions/%s/files' % deposition_id,
                       params={'access_token': ACCESS_TOKEN}, data=data,
                       files=files)
    r.status_code
    ```


* Forming the augmented data payload for a dataset corresponding to the JSON data package for the matrix

    ```python

    metadata = {
         "metadata": {
             "title": "Frictionless Tabular data package for GC-MS data from Rose Genome article published\
              in Nature genetics, June, 2018",
             "upload_type": "dataset",
             "description": "This dataset, in the form of a Frictionless Tabular Data Package \
             (https://frictionlessdata.io/specs/tabular-data-package/), \
              holds the measurements of 61 known metabolites (all annotated with resolvable CHEBI identifiers and InChi), \
              measured by gas chromatography mass-spectrometry (GC-MS) in 6 different Rose cultivars (all annotated with \
              resolvable NCBITaxId) and 3 organism parts (all annotated with resolvable Plant Ontology identifiers).\
              The data was extracted from a supplementary material table, available from \
              https://static-content.springer.com/esm/art%3A10.1038%2Fs41588-018-0110-3/MediaObjects/41588_2018_110_MOESM3_ESM.zip \
              and published alongside the Nature Genetics manuscript identified by the following doi: \
              https://doi.org/10.1038/s41588-018-0110-3, published in June 2018. \
              This dataset is used to demonstrate how to make data Findeable, Accessible, Discoverable and Interoperable" \
              "(FAIR) and how Tabular Data Package representations can be easily mobilized for re-analysis and data science. \
              It is associated to the following project available from github at: \
              'https://github.com/proccaserra/rose2018ng-notebook' with all necessary information and Jupyter notebooks.",
             "creators": [
                          {
                            "affiliation": "University of Oxford",
                            "name": "Philippe Rocca-Serra",
                            "orcid": "0000-0001-9853-5668"
                          },
                          {
                            "affiliation": "University of Oxford",
                            "name": "Susanna Assunta Sansone",
                            "orcid": "0000-0001-5306-5690"
                          }
                        ],
             "access_right": "open",
             "keywords": [
                 "FAIR data",
                 "Design of Experiment",
                 "Rose scent",
                 "targeted metabolite profiling",
                 "gas chromatography mass spectrometry",
                 "Tabular Data Package",
                 "STATO ontology",
                 "ISA format",
                 "interoperability"],
             "language": "eng",
             "license": {
                    "id": "CC-BY-4.0"
                        },
             "publication_date": "2019-03-13",
             "references": ["https://doi.org/10.1038/s41588-018-0110-3"],
             "related_identifiers": [
              {
                "relation": "cites",
                "identifier": "10.1038/s41588-018-0110-3"
              },
              {
                "relation": "cites",
                "identifier": "10.5281/zenodo.2598799"
              },
              {
                "relation": "isNewVersionOf",
                "identifier": "10.5281/zenodo.2557893"
              }
            ],
             "grants": [{"links":{"self":"https://zenodo.org/api/grants/10.13039/501100000780::654241"},"acronym": "PhenoMenAl",
            "program": "H2020",
            "funder": {
              "doi": "10.13039/501100000780",
              "acronyms": [
                "EC"
              ],
              "name": "European Commission",
              "links": {
                "self": "https://zenodo.org/api/funders/10.13039/501100000780"
              }
            }
                         }]
            }
        }

    r = requests.put("https://zenodo.org/api/deposit/depositions/%s" % deposition_id,
                      params={"access_token": ACCESS_TOKEN}, data=json.dumps(metadata),
                     headers=headers)

    r.status_code
    ```

### Finalize request and post:

* Finally, combine metadata and data payload in order to send a properlly formed request and obtain a DOI.

```python
data_2 = {'filename': 'rose-aroma-naturegenetics2018-treatment-group-mean-sem-report-table-example.csv'}
files_2 = {'file': open('../data/processed/rose-data/rose-aroma-naturegenetics2018-treatment-group-mean-sem-report-table-example.csv', 'rb')}
r = requests.post('https://zenodo.org/api/deposit/depositions/%s/files' % deposition_id,
                   params={'access_token': ACCESS_TOKEN}, data=data_2,
                   files=files_2)
r.status_code
```
---

## Conclusions:

> Relying on CERN Zenodo repository using any of the submission mechanisms (either web component or API) is one the simplest yet highly effective ways to deliver **dataset findeability** for assets generated by publicly funded resources. 
> The integration with [ORCID]() makes it very easy to obtain an account on the CERN's service. 
> The integration with [Datacite]() means that submitters can reserve and obtain Digital Object Identifiers (DOI) very simply. These can then be cited and used as references to the datasets.
> The integration with [Crossref]() means that funding information case be easily looked up, thus reducing data entry burden in most conditions but especially for EU funded projects such as IMI.
> Licensing information can also be easily supplied
> Data access and embargo dates can be reserved.
> Findability via search engines is enhanced as Zenodo supports content negotiation, serving [schema.org](https://schema.org) based JSON-LD documents
> Users should however be reminded of the following limitations of the service:
    > - absence of contraints on the nature of the datafiles being uploaded
    > - no domain specific awareness and domain specific metadata
    > - absent of connection with specialized repositories
    > - size limitation for a given datasets.
    
    

> #### What should I read next?
> * [How to build a data catalogue?]()
> * [How to deploy the FAIRPORT data catalogue?]()
> * [What is search engine optimization?]()


## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [deposition](http://edamontology.org/operation_3431)  | [text](http://edamontology.org/data_3671)  | [DOI](http://edamontology.org/data_1188)  |
||file||



## Table of Data Standards

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| [Datacite](https://fairsharing.org/fairsharing.me4qwe)  | none  |   |
| [JSON](https://fairsharing.org/bsg-s001212/)|||
| [JSON-LD](https://fairsharing.org/bsg-s001214/)|||


___
## Authors:

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Philippe Rocca-Serra |  University of Oxford, Data Readiness Group| [0000-0001-9853-5668](https://orcid.org/orcid.org/0000-0001-9853-5668) | Writing - Original Draft |
| Susanna-Assunta Sansone |  University of Oxford, Data Readiness Group | | Writing - Review & Editing, Funding acquisition | 

___
## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
