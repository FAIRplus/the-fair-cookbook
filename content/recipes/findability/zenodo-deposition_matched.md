(fcb-find-zenodo (URL_TO_INSERT_RECORD_2040 https://fairsharing.org/FAIRsharing.wy4egf) )=
# Depositing to generic repositories - Zenodo use case


````{panels_fairplus}
:identifier_text: FCB009
:identifier_link: 'https://w3id.org/faircookbook/FCB009'
:difficulty_level: 2
:recipe_type: hands_on
:reading_time_minutes: 15
:intended_audience: principal_investigator, data_manager, data_scientist, funder
:maturity_level: 1
:maturity_indicator: 5, 6, 7, 8
:has_executable_code: nope
:recipe_name: Depositing to generic repositories - Zenodo use case
```` 

## Main Objectives

The main purpose of this recipe is:

> To show how to take advantage of CERN Zenodo (URL_TO_INSERT_RECORD_2044 https://fairsharing.org/FAIRsharing.wy4egf)  repository (URL_TO_INSERT_TERM_2042 https://fairsharing.org/search?recordType=repository)  to document the existence of datasets, thus increasing its findability. This is of particular relevant for IMI project (URL_TO_INSERT_TERM_2043 https://fairsharing.org/search?recordType=project) s since Zenodo (URL_TO_INSERT_RECORD_2045 https://fairsharing.org/FAIRsharing.wy4egf)  is aimed to support the European Commission (EC) nascent Open Data policy (URL_TO_INSERT_TERM_2041 https://fairsharing.org/search?fairsharingRegistry=Policy)  and is commissioned by the EC.


```{tabbed} FAIRification Objectives, Inputs and Outputs
| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [deposition](http://edamontology.org/operation_3431)  | [text](http://edamontology.org/data_3671)  | [DOI](http://edamontology.org/data_1188)  |
||file||

```
```{tabbed} Table of Data Standards
| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| [Datacite](https://fairsharing.org/fairsharing.me4qwe)  | none  |   |
| [JSON](https://fairsharing.org/bsg-s001212/)|||
| [JSON-LD](https://fairsharing.org/bsg-s001214/)|||
```


---

## Graphical Overview


````{dropdown} 
:open:
```{figure} /images/zenodo.png
---
width: 500px
name: 
alt: The process of depositing to CERN Zenodo (URL_TO_INSERT_RECORD_2046 https://fairsharing.org/FAIRsharing.wy4egf) 
---
The Zenodo (URL_TO_INSERT_RECORD_2047 https://fairsharing.org/FAIRsharing.wy4egf)  homepage.
```
````
---


## Introduction to Zenodo repository

### What is Zenodo?

Zenodo (URL_TO_INSERT_RECORD_2052 https://fairsharing.org/FAIRsharing.wy4egf)  is a repository (URL_TO_INSERT_TERM_2049 https://fairsharing.org/search?recordType=repository)  developed (URL_TO_INSERT_RECORD_2054 https://fairsharing.org/FAIRsharing.31385c)  by [CERN](https://home.cern/) under the [OpenAire](https://www.openaire.eu/) program, the focus of which is on **open data**. It was commissioned by the EC to support their nascent Open Data policy (URL_TO_INSERT_TERM_2048 https://fairsharing.org/search?fairsharingRegistry=Policy)  by providing a catch-all repository (URL_TO_INSERT_TERM_2050 https://fairsharing.org/search?recordType=repository)  for EC funded research (URL_TO_INSERT_RECORD_2053 https://fairsharing.org/FAIRsharing.52b22c) . This of particular relevance for all project (URL_TO_INSERT_TERM_2051 https://fairsharing.org/search?recordType=project) s funded under the `Innovative Medicine Initiative (IMI)`.

### Why use Zenodo?

To cite `Zenodo (URL_TO_INSERT_RECORD_2056 https://fairsharing.org/FAIRsharing.wy4egf) 's documentation`, here are a few reasons why using the repository (URL_TO_INSERT_TERM_2055 https://fairsharing.org/search?recordType=repository)  services provides a `low entry barrier` to making data findable:
* Safe — your research (URL_TO_INSERT_RECORD_2057 https://fairsharing.org/FAIRsharing.52b22c)  is stored safely for the future in CERN’s Data Centre for as long as CERN exists.
* Trusted — built and operated by CERN and OpenAIRE to ensure that everyone can join in Open Science.
* Citeab (URL_TO_INSERT_RECORD_2060 https://fairsharing.org/FAIRsharing.d404th) le — every upload is assigned a Digital Object Identifier (URL_TO_INSERT_TERM_2058 https://fairsharing.org/search?recordType=identifier_schema)  (URL_TO_INSERT_RECORD_2059 https://fairsharing.org/FAIRsharing.hFLKCn)  (DOI), to make them citable and trackable.
* No waiting time — Uploads are made available online as soon as you hit publish, and your DOI (URL_TO_INSERT_RECORD_2061 https://fairsharing.org/FAIRsharing.hFLKCn)  is registered within seconds.
* Open or closed — Share e.g. anonymized clinical trial data with only medical professionals via our restricted access mode.
* Versioning — Easily update your dataset with our versioning feature.
* GitHub (URL_TO_INSERT_RECORD_2064 https://fairsharing.org/FAIRsharing.c55d5e)  integration — Easily preserve your GitHub (URL_TO_INSERT_RECORD_2065 https://fairsharing.org/FAIRsharing.c55d5e)  repository (URL_TO_INSERT_TERM_2062 https://fairsharing.org/search?recordType=repository)  in Zenodo (URL_TO_INSERT_RECORD_2063 https://fairsharing.org/FAIRsharing.wy4egf) .
* Usage statisics — All uploads display standard (URL_TO_INSERT_TERM_2066 https://fairsharing.org/search?fairsharingRegistry=Standard) s compliant usage statistics.


## 1. How to use Zenodo Deposition Web Interface?

This section guides users through the key steps to perform to organize a deposition to Zenodo (URL_TO_INSERT_RECORD_2068 https://fairsharing.org/FAIRsharing.wy4egf)  using the user interface web component provided by the repository (URL_TO_INSERT_TERM_2067 https://fairsharing.org/search?recordType=repository) .

---

### Zenodo Compatible Data Collection - Login-in

* Login via ORCID (URL_TO_INSERT_RECORD_2070 https://fairsharing.org/FAIRsharing.nx58jg)  or Github (URL_TO_INSERT_RECORD_2069 https://fairsharing.org/FAIRsharing.c55d5e)  credentials

```{admonition} Tip
:class: tip

[Zenodo](https://zenodo.org/) has integrated authentication mechanism key partners such as [github](https://github.com)  and [Orcid](https://orcid.org). For [IMI](https://www.imi.europa.eu/) and for [FAIRplus](https://fairplus-project.eu), this means that consortium members can easyly login if they already have credentials on these 2 services. 
```

---

### Zenodo Compatible Data Collection - Data upload

<!-- <div> <img src="/images/TYpr8jM.png" alt="drawing" style="width:650px;" border="1px solid black" align="top" />
</div> -->

````{dropdown} 
:open:
```{figure} /images/TYpr8jM.png
---
height: 600px
name: Uploading files to Zenodo (URL_TO_INSERT_RECORD_2071 https://fairsharing.org/FAIRsharing.wy4egf) 
alt: Uploading files to Zenodo (URL_TO_INSERT_RECORD_2072 https://fairsharing.org/FAIRsharing.wy4egf) 
---
Uploading files to Zenodo (URL_TO_INSERT_RECORD_2074 https://fairsharing.org/FAIRsharing.wy4egf)  Repository (URL_TO_INSERT_TERM_2073 https://fairsharing.org/search?recordType=repository) .
```
````

Files can be dragged and dropped (URL_TO_INSERT_RECORD_2075 https://fairsharing.org/FAIRsharing.31385c) , with the following limitations:
* 5GB max each, 
* 50 GB total / dataset


After adding the set of files associated with the submission, the upload should be initiated by pressing the `start upload` green button.
Failing to do so will result in a failure to proceed with the submission and an error will be thrown, reminding users to do so.

<!-- <img src="/images/LwMorlw.png" alt="drawing" style="width:650px;" border="1px solid black" align="top" /> -->

````{dropdown} 
:open:
```{figure} /images/LwMorlw.png
---
height: 600px
name: Starting the file upload to Zenodo (URL_TO_INSERT_RECORD_2076 https://fairsharing.org/FAIRsharing.wy4egf) 
alt: Starting the file upload  to Zenodo (URL_TO_INSERT_RECORD_2077 https://fairsharing.org/FAIRsharing.wy4egf) 
---
Starting the file upload to Zenodo (URL_TO_INSERT_RECORD_2079 https://fairsharing.org/FAIRsharing.wy4egf)  Repository (URL_TO_INSERT_TERM_2078 https://fairsharing.org/search?recordType=repository) .
```
````

The next key step is to select the `upload type`. In this instance, the `Dataset` is selected. This matters as it provide strong typing which is relied on by `search (URL_TO_INSERT_RECORD_2080 https://fairsharing.org/FAIRsharing.52b22c)  engine` and therefore impacts `findability`.


<!-- <img src="/images/OYyz4dT.png" alt="drawing" style="width:500px;" border="1px solid black" align="top" /> -->

````{dropdown} 
:open:
```{figure} /images/OYyz4dT.png
---
height: 150px
name: Selecting the upload type to Zenodo (URL_TO_INSERT_RECORD_2081 https://fairsharing.org/FAIRsharing.wy4egf) 
alt: Selecting the upload type to Zenodo (URL_TO_INSERT_RECORD_2082 https://fairsharing.org/FAIRsharing.wy4egf) 
---
Selecting the upload type to Zenodo (URL_TO_INSERT_RECORD_2084 https://fairsharing.org/FAIRsharing.wy4egf)  Repository (URL_TO_INSERT_TERM_2083 https://fairsharing.org/search?recordType=repository) .
```
````


---

### Zenodo Compatible Data Collection - Providing Metadata

* Basic metadata such as. `title`, `description`, at minima should be provided.
* Authors should be identified, ideally using their `orcid`, so linking can be performed. This affects authors citation and impact evaluation. For IMI FAIR (URL_TO_INSERT_RECORD_2086 https://fairsharing.org/FAIRsharing.WWI10U) plus participants, since all have now such an identifier (URL_TO_INSERT_TERM_2085 https://fairsharing.org/search?recordType=identifier_schema) , the link should be made systematically.

<!-- <img src="/images/WmlqBjL.png" alt="drawing" style="width:700px;" border="1px solid black" align="top" /> -->

````{dropdown} 
:open:
```{figure} /images/WmlqBjL.png
---
height: 600px
name: Basic metadata to report 
alt:  Basic metadata to report 
---
Basic metadata to report .
```
````

* **Reserve a Digital Object Identifier (URL_TO_INSERT_TERM_2088 https://fairsharing.org/search?recordType=identifier_schema)  (URL_TO_INSERT_RECORD_2089 https://fairsharing.org/FAIRsharing.hFLKCn) **: This is a service provided natively by the Zenodo (URL_TO_INSERT_RECORD_2090 https://fairsharing.org/FAIRsharing.wy4egf)  service, by virtue of its integration with Datacite services. This is quite an important point as it means the Zenodo (URL_TO_INSERT_RECORD_2091 https://fairsharing.org/FAIRsharing.wy4egf)  submission can be cited. However, remember to carefully review all the data entered in the form as once a doi has been minted, the associated informat (URL_TO_INSERT_TERM_2087 https://fairsharing.org/search?recordType=model_and_format) ion **can not be changed without creating a new version of the arch (URL_TO_INSERT_RECORD_2092 https://fairsharing.org/FAIRsharing.52b22c) ive and therefore minting a new doi**
 


* 'Keywords' can be added to tag the submission. These are free text and no controlled terminology (URL_TO_INSERT_TERM_2093 https://fairsharing.org/search?recordType=terminology_artefact)  can be used in the interface at the moment.

<!-- <img src="/images/9Bp91gX.png" alt="drawing" style="width:700px;" border="1px solid black" align="top" /> -->

````{dropdown} 
:open:
```{figure} /images/9Bp91gX.png
---
height: 600px
name: Setting keywords associated with the Zenodo (URL_TO_INSERT_RECORD_2094 https://fairsharing.org/FAIRsharing.wy4egf)  deposition
alt:  Setting keywords associated with the Zenodo (URL_TO_INSERT_RECORD_2095 https://fairsharing.org/FAIRsharing.wy4egf)  deposition
---
Setting keywords associated with the Zenodo (URL_TO_INSERT_RECORD_2096 https://fairsharing.org/FAIRsharing.wy4egf)  deposition .
```
````


---

###  Zenodo Compatible Data Collection - Access and License information

* Zenodo (URL_TO_INSERT_RECORD_2098 https://fairsharing.org/FAIRsharing.wy4egf)  provides facilities to set `Access Conditions` and `License`, `Data Controler Contact Informat (URL_TO_INSERT_TERM_2097 https://fairsharing.org/search?recordType=model_and_format) ion`, as well as `Embargo Duration` if applicable.
* As indicated above, it is possible to `set an Embargo Period`, if the option `embargoed access` is selected under the `Access right` section.

<!-- <img src="/images/fSxOjXe.png" alt="drawing" style="width:750px;" border="1px solid black" align="top" /> -->

````{dropdown} 
:open:
```{figure} /images/fSxOjXe.png
---
height: 400px
name: Choosing a License is essential 
alt:  Choosing a License is essential 
---
Choosing a License is essential.
```
````



  * Zenodo (URL_TO_INSERT_RECORD_2101 https://fairsharing.org/FAIRsharing.wy4egf)  places no limit when it comes to duration of the embargo period. So submitters should check EC and IMI guideline (URL_TO_INSERT_TERM_2100 https://fairsharing.org/search?recordType=reporting_guideline) s or local institution (URL_TO_INSERT_TERM_2099 https://fairsharing.org/search?recordType=institution) al requirements for guidance.


* Setting Access Conditions/License, Data Controler Contact Informat (URL_TO_INSERT_TERM_2102 https://fairsharing.org/search?recordType=model_and_format) ion, Embargo Duration if applicable

<!-- <img src="/images/ty9rpXF.png" alt="drawing" style="width:750px;" border="1px solid black" align="top" /> -->

````{dropdown} 
:open:
```{figure} /images/ty9rpXF.png
---
height: 350px
name: Setting access conditions
alt:  Setting access conditions
---
Setting access conditions.
```
````

* Start typing to display more licenses available from Zenodo (URL_TO_INSERT_RECORD_2103 https://fairsharing.org/FAIRsharing.wy4egf) 

<!-- <img src="/images/249GhMg.png" alt="drawing" style="width:550px;" border="1px solid black" align="top"/> -->

````{dropdown} 
:open:
```{figure} /images/249GhMg.png
---
height: 150px
name: Autocompletion prompts available licenses
alt:  Autocompletion prompts available licenses
---
Autocompletion prompts available licenses.
```
````



---
### Zenodo Compatible Data Collection - Funding Information

Since the Zenodo (URL_TO_INSERT_RECORD_2106 https://fairsharing.org/FAIRsharing.wy4egf)  mission is to collect EC funded data, the repository (URL_TO_INSERT_TERM_2104 https://fairsharing.org/search?recordType=repository)  provides the means to lookup `Grant Informat (URL_TO_INSERT_TERM_2105 https://fairsharing.org/search?recordType=model_and_format) ion`:

<!-- <img src="/images/STjyFbT.png" alt="drawing" style="width:700px;" border="1px solid black" align="top" /> -->

````{dropdown} 
:open:
```{figure} /images/STjyFbT.png
---
height: 200px
name: Linking Funding to Zenodo (URL_TO_INSERT_RECORD_2107 https://fairsharing.org/FAIRsharing.wy4egf)  Submission
alt:  Linking Funding to Zenodo (URL_TO_INSERT_RECORD_2108 https://fairsharing.org/FAIRsharing.wy4egf)  Submission
---
Linking Funding to Zenodo (URL_TO_INSERT_RECORD_2109 https://fairsharing.org/FAIRsharing.wy4egf)  Submission.
```
````


  * Zenodo (URL_TO_INSERT_RECORD_2111 https://fairsharing.org/FAIRsharing.wy4egf) : openAIRE connected repository (URL_TO_INSERT_TERM_2110 https://fairsharing.org/search?recordType=repository) 

  * Connected to funding agencies

---
### Zenodo Compatible Data Collection - Miscellaneous Information

* Miscellaneous Informat (URL_TO_INSERT_TERM_2112 https://fairsharing.org/search?recordType=model_and_format) ion:

<!-- <img src="/images/uhGZN5t.png" alt="drawing" style="width:700px;" border="1px solid black" align="top" /> -->

````{dropdown} 
:open:
```{figure} /images/uhGZN5t.png
---
height: 500px
name: Miscellaneous Informat (URL_TO_INSERT_TERM_2113 https://fairsharing.org/search?recordType=model_and_format) ion about the Zenodo (URL_TO_INSERT_RECORD_2114 https://fairsharing.org/FAIRsharing.wy4egf)  Submission
alt:  Miscellaneous Informat (URL_TO_INSERT_TERM_2115 https://fairsharing.org/search?recordType=model_and_format) ion about the Zenodo (URL_TO_INSERT_RECORD_2116 https://fairsharing.org/FAIRsharing.wy4egf)  Submission
---
Miscellaneous Informat (URL_TO_INSERT_TERM_2117 https://fairsharing.org/search?recordType=model_and_format) ion about the Zenodo (URL_TO_INSERT_RECORD_2118 https://fairsharing.org/FAIRsharing.wy4egf)  Submission.
```
````


  * Contributors

  * References:

  * Journal (URL_TO_INSERT_TERM_2119 https://fairsharing.org/search?recordType=journal) , Conference, Book, and so on.



## 2. Programmatic Deposition to Zenodo via the REST-API

### Create a zenodo account and obtain an API token

* First, it is necessary to obtain an api key:

    `ACCESS_TOKEN` = "<enter-your_writeonly_token_for_testing or your_deposit_token if you want to get a DOI (URL_TO_INSERT_RECORD_2120 https://fairsharing.org/FAIRsharing.hFLKCn)   >"

* Then, the following code invoking the Zenodo (URL_TO_INSERT_RECORD_2121 https://fairsharing.org/FAIRsharing.wy4egf)  REST endpoint will allow deposition:

    ```python
    import requests
    import json

    zenodo (URL_TO_INSERT_RECORD_2122 https://fairsharing.org/FAIRsharing.wy4egf) _baseurl = "https://zenodo.org/api/"
    headers = {"Content-Type": "application/json"}

    AC (URL_TO_INSERT_RECORD_2123 https://fairsharing.org/FAIRsharing.md3e78) CESS_TOKEN = "<YOUR_TOKEN_GOES_HERE>"
    # testing the connection
    r = requests.get("https://zenodo.org/api/deposit/depositions", params={"access_token": AC (URL_TO_INSERT_RECORD_2124 https://fairsharing.org/FAIRsharing.md3e78) CESS_TOKEN})

    # creating an empty submission to get an zenodo (URL_TO_INSERT_RECORD_2125 https://fairsharing.org/FAIRsharing.wy4egf)  record id:
    r = requests.post('https://zenodo.org/api/deposit/depositions', params={'access_token': AC (URL_TO_INSERT_RECORD_2126 https://fairsharing.org/FAIRsharing.md3e78) CESS_TOKEN}, json={},
                      headers=headers)
    r.status_code

    # obtain the zenodo (URL_TO_INSERT_RECORD_2127 https://fairsharing.org/FAIRsharing.wy4egf)  metadata payload as json containing the id
    r.json()
    ```

### Create the payload for the programmatic deposition

*  For example, it can be obtained by parsing the content of a metadata template or from a dedicated acquisition form specifically made by a `data manager`

    ```python
    # getting the record id
    deposition_id = r.json()['id']

    # uploading the data

    data = {'filename': 'rose-aroma-naturegenetics2018-treatment-group-mean-sem-report-datapackage.json'}
    files = {'file': open('../data/processed/rose-data/rose-aroma-naturegenetics2018-treatment-group-mean-sem-report-datapackage.json', 'rb')}
    r = requests.post('https://zenodo.org/api/deposit/depositions/%s/files' % deposition_id,
                       params={'access_token': AC (URL_TO_INSERT_RECORD_2128 https://fairsharing.org/FAIRsharing.md3e78) CESS_TOKEN}, data=data,
                       files=files)
    r.status_code
    ```


* Forming the augmented data payload for a dataset corresponding to the JSON (URL_TO_INSERT_RECORD_2129 https://fairsharing.org/FAIRsharing.5bbab9)  data package (URL_TO_INSERT_RECORD_2130 https://fairsharing.org/FAIRsharing.3b861d)  for the matrix

    ```python

    metadata = {
         "metadata": {
             "title": "Frictionless Tabular data package (URL_TO_INSERT_RECORD_2131 https://fairsharing.org/FAIRsharing.082881)  (URL_TO_INSERT_RECORD_2132 https://fairsharing.org/FAIRsharing.3b861d)  for GC-MS data from Rose Genome article published\
              in Nature genetics, June, 2018",
             "upload_type": "dataset",
             "description": "This dataset, in the form of a Frictionless Tabular Data Package (URL_TO_INSERT_RECORD_2133 https://fairsharing.org/FAIRsharing.082881)  (URL_TO_INSERT_RECORD_2134 https://fairsharing.org/FAIRsharing.3b861d)  \
             (https://frictionlessdata.io/specs/tabular-data-package/), \
              holds the measurements of 61 known metabolites (all annotated with resolvable CHEBI identifier (URL_TO_INSERT_TERM_2135 https://fairsharing.org/search?recordType=identifier_schema) s and InChi), \
              measured by gas chromatography mass-spectrometry (GC-MS) in 6 different Rose cultivars (all annotated with \
              resolvable NCBITaxId) and 3 organism parts (all annotated with resolvable Plant Ontology (URL_TO_INSERT_TERM_2136 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_2138 https://fairsharing.org/FAIRsharing.3ngg40)  identifier (URL_TO_INSERT_TERM_2137 https://fairsharing.org/search?recordType=identifier_schema) s).\
              The data was extracted from a supplementary material table, available from \
              https://static-content.springer.com/esm/art%3A10.1038%2Fs41588-018-0110-3/MediaObjects/41588_2018_110_MOESM3_ESM.zip \
              and published alongside the Nature Genetics manuscript identified by the following doi: \
              https://doi.org/10.1038/s41588-018-0110-3, published in June 2018. \
              This dataset is used to demonstrate how to make data Findable, Accessible, Discoverable and Interoperable" \
              "(FAIR (URL_TO_INSERT_RECORD_2141 https://fairsharing.org/FAIRsharing.WWI10U) ) and how Tabular Data Package (URL_TO_INSERT_RECORD_2139 https://fairsharing.org/FAIRsharing.082881)  (URL_TO_INSERT_RECORD_2140 https://fairsharing.org/FAIRsharing.3b861d)  representations can be easily mobilized for re-analysis and data science. \
              It is associated to the following project (URL_TO_INSERT_TERM_2142 https://fairsharing.org/search?recordType=project)  available from github (URL_TO_INSERT_RECORD_2143 https://fairsharing.org/FAIRsharing.c55d5e)  at: \
              'https://github.com (URL_TO_INSERT_RECORD_2145 https://fairsharing.org/FAIRsharing.c55d5e) /proccaserra/rose2018ng-notebook' with all necessary informat (URL_TO_INSERT_TERM_2144 https://fairsharing.org/search?recordType=model_and_format) ion and Jupyter notebooks.",
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
                 "FAIR (URL_TO_INSERT_RECORD_2146 https://fairsharing.org/FAIRsharing.WWI10U)  data",
                 "Design of Experiment",
                 "Rose scent",
                 "targeted metabolite profiling",
                 "gas chromatography mass spectrometry",
                 "Tabular Data Package (URL_TO_INSERT_RECORD_2147 https://fairsharing.org/FAIRsharing.082881)  (URL_TO_INSERT_RECORD_2148 https://fairsharing.org/FAIRsharing.3b861d) ",
                 "STATO (URL_TO_INSERT_RECORD_2150 https://fairsharing.org/FAIRsharing.na5xp)  ontology (URL_TO_INSERT_TERM_2149 https://fairsharing.org/search?recordType=terminology_artefact) ",
                 "ISA format (URL_TO_INSERT_TERM_2151 https://fairsharing.org/search?recordType=model_and_format) ",
                 "interoperability"],
             "language": "eng",
             "license": {
                    "id": "CC-BY-4.0"
                        },
             "publication_date": "2019-03-13",
             "references": ["https://doi.org/10.1038/s41588-018-0110-3"],
             "related_identifier (URL_TO_INSERT_TERM_2152 https://fairsharing.org/search?recordType=identifier_schema) s": [
              {
                "relation": "cites",
                "identifier (URL_TO_INSERT_TERM_2153 https://fairsharing.org/search?recordType=identifier_schema) ": "10.1038/s41588-018-0110-3"
              },
              {
                "relation": "cites",
                "identifier (URL_TO_INSERT_TERM_2154 https://fairsharing.org/search?recordType=identifier_schema) ": "10.5281/zenodo (URL_TO_INSERT_RECORD_2155 https://fairsharing.org/FAIRsharing.wy4egf) .2598799"
              },
              {
                "relation": "isNewVersionOf",
                "identifier (URL_TO_INSERT_TERM_2156 https://fairsharing.org/search?recordType=identifier_schema) ": "10.5281/zenodo (URL_TO_INSERT_RECORD_2157 https://fairsharing.org/FAIRsharing.wy4egf) .2557893"
              }
            ],
             "grants": [{"links":{"self":"https://zenodo.org/api/grants/10.13039/501100000780::654241"},"acronym": "PhenoMenAl",
            "program": "H2020",
            "funder (URL_TO_INSERT_TERM_2158 https://fairsharing.org/search?recordType=funder) ": {
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
                      params={"access_token": AC (URL_TO_INSERT_RECORD_2159 https://fairsharing.org/FAIRsharing.md3e78) CESS_TOKEN}, data=json.dumps(metadata),
                     headers=headers)

    r.status_code
    ```

### Finalize request and post

* Finally, combine metadata and data payload in order to send a properlly formed request and obtain a DOI (URL_TO_INSERT_RECORD_2160 https://fairsharing.org/FAIRsharing.hFLKCn) .

```python
data_2 = {'filename': 'rose-aroma-naturegenetics2018-treatment-group-mean-sem-report-table-example.csv'}
files_2 = {'file': open('../data/processed/rose-data/rose-aroma-naturegenetics2018-treatment-group-mean-sem-report-table-example.csv', 'rb')}
r = requests.post('https://zenodo.org/api/deposit/depositions/%s/files' % deposition_id,
                   params={'access_token': ACCESS_TOKEN}, data=data_2,
                   files=files_2)
r.status_code
```
---

## Conclusions

> Relying on CERN Zenodo (URL_TO_INSERT_RECORD_2162 https://fairsharing.org/FAIRsharing.wy4egf)  repository (URL_TO_INSERT_TERM_2161 https://fairsharing.org/search?recordType=repository)  using any of the submission mechanisms (either web component or API) is one the simplest yet highly effective ways to deliver **dataset findability** for assets generated by publicly funded resources. 
> The integration with ORCID<!-- TODO add a link to corresponding document --> makes it very easy to obtain an account on CERN's service. 
> The integration with Datacite<!-- TODO add a link to corresponding document --> means that submitters can reserve and obtain Digital Object Identifiers (DOI) very simply. These can then be cited and used as references to the datasets.
> The integration with Crossref<!-- TODO add a link to corresponding document --> means that funding information case be easily looked up, thus reducing data entry burden in most conditions but especially for EU funded projects such as IMI.
> Licensing informat (URL_TO_INSERT_TERM_2163 https://fairsharing.org/search?recordType=model_and_format) ion can also be easily supplied.
> Data access and embargo dates can be reserved.
> Findability via search (URL_TO_INSERT_RECORD_2167 https://fairsharing.org/FAIRsharing.52b22c)  engines is enhanced as Zenodo (URL_TO_INSERT_RECORD_2166 https://fairsharing.org/FAIRsharing.wy4egf)  supports content negotiation, serving [schema.org](https://schema.org) based JSON (URL_TO_INSERT_RECORD_2164 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2165 https://fairsharing.org/FAIRsharing.8f9bbb)  documents.
> Users should however be reminded of the following limitations of the service:
    > - Absence of constraints on the nature of the datafiles being uploaded.
    > - No domain specific awareness and domain specific metadata.
    > - Absence of connection with specialized repositories (URL_TO_INSERT_TERM_2168 https://fairsharing.org/search?recordType=repository) .
    > - Size limitation for a given datasets.
    
    

### What to read next?
* [How to build a data catalogue?](fcb-infra-build-catalog)
* How to deploy the FAIRPORT data catalogue?<!-- TODO add a link to corresponding document -->
* [What is search engine optimization?](fcb-find-seo)
 
````{rdmkit_panel}
````

## References
````{dropdown} **References**
````

## Authors

````{authors_fairplus}
Philippe: Writing - Writing, Conceptualization
Susanna: Writing - Review & Editing, Funding acquisition
````

## License

````{license_fairplus}
CC-BY-4.0
````
