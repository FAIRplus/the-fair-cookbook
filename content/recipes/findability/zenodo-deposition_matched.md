(fcb-find-zenodo (URL_TO_INSERT_RECORD_2853 https://fairsharing.org/FAIRsharing.wy4egf) )=
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

> To show how to take advantage of CERN Zenodo (URL_TO_INSERT_RECORD_2857 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2859 https://fairsharing.org/FAIRsharing.wy4egf)  repository (URL_TO_INSERT_TERM_2855 https://fairsharing.org/search?recordType=repository)  to document the existence of datasets, thus increasing its findability. This is of particular relevant for IMI project (URL_TO_INSERT_TERM_2856 https://fairsharing.org/search?recordType=project) s since Zenodo (URL_TO_INSERT_RECORD_2858 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2860 https://fairsharing.org/FAIRsharing.wy4egf)  is aimed to support the European Commission (EC) nascent Open Data policy (URL_TO_INSERT_TERM_2854 https://fairsharing.org/search?fairsharingRegistry=Policy)  and is commissioned by the EC.


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
alt: The process of depositing to CERN Zenodo (URL_TO_INSERT_RECORD_2861 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2862 https://fairsharing.org/FAIRsharing.wy4egf) 
---
The Zenodo (URL_TO_INSERT_RECORD_2863 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2864 https://fairsharing.org/FAIRsharing.wy4egf)  homepage.
```
````
---


## Introduction to Zenodo repository

### What is Zenodo?

Zenodo (URL_TO_INSERT_RECORD_2869 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2870 https://fairsharing.org/FAIRsharing.wy4egf)  is a repository (URL_TO_INSERT_TERM_2866 https://fairsharing.org/search?recordType=repository)  developed (URL_TO_INSERT_RECORD_2872 https://fairsharing.org/FAIRsharing.31385c)  by [CERN](https://home.cern/) under the [OpenAire](https://www.openaire.eu/) program, the focus of which is on **open data**. It was commissioned by the EC to support their nascent Open Data policy (URL_TO_INSERT_TERM_2865 https://fairsharing.org/search?fairsharingRegistry=Policy)  by providing a catch-all repository (URL_TO_INSERT_TERM_2867 https://fairsharing.org/search?recordType=repository)  for EC funded research (URL_TO_INSERT_RECORD_2871 https://fairsharing.org/FAIRsharing.52b22c) . This of particular relevance for all project (URL_TO_INSERT_TERM_2868 https://fairsharing.org/search?recordType=project) s funded under the `Innovative Medicine Initiative (IMI)`.

### Why use Zenodo?

To cite `Zenodo (URL_TO_INSERT_RECORD_2874 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2875 https://fairsharing.org/FAIRsharing.wy4egf) 's documentation`, here are a few reasons why using the repository (URL_TO_INSERT_TERM_2873 https://fairsharing.org/search?recordType=repository)  services provides a `low entry barrier` to making data findable:
* Safe — your research (URL_TO_INSERT_RECORD_2876 https://fairsharing.org/FAIRsharing.52b22c)  is stored safely for the future in CERN’s Data Centre for as long as CERN exists.
* Trusted — built and operated by CERN and OpenAIRE to ensure that everyone can join in Open Science.
* Citeab (URL_TO_INSERT_RECORD_2880 https://fairsharing.org/FAIRsharing.d404th) le — every upload is assigned a Digital Object Identifier (URL_TO_INSERT_TERM_2877 https://fairsharing.org/search?recordType=identifier_schema)  (URL_TO_INSERT_RECORD_2878 https://fairsharing.org/FAIRsharing.hFLKCn)  (DOI (URL_TO_INSERT_RECORD_2879 https://fairsharing.org/FAIRsharing.hFLKCn) ), to make them citable and trackable.
* No waiting time — Uploads are made available online as soon as you hit publish, and your DOI (URL_TO_INSERT_RECORD_2881 https://fairsharing.org/FAIRsharing.hFLKCn)  is registered within seconds.
* Open or closed — Share e.g. anonymized clinical trial data with only medical professionals via our restricted access mode.
* Versioning — Easily update your dataset with our versioning feature.
* GitHub (URL_TO_INSERT_RECORD_2885 https://fairsharing.org/FAIRsharing.c55d5e)  (URL_TO_INSERT_RECORD_2887 https://fairsharing.org/FAIRsharing.c55d5e)  integration — Easily preserve your GitHub (URL_TO_INSERT_RECORD_2886 https://fairsharing.org/FAIRsharing.c55d5e)  (URL_TO_INSERT_RECORD_2888 https://fairsharing.org/FAIRsharing.c55d5e)  repository (URL_TO_INSERT_TERM_2882 https://fairsharing.org/search?recordType=repository)  in Zenodo (URL_TO_INSERT_RECORD_2883 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2884 https://fairsharing.org/FAIRsharing.wy4egf) .
* Usage statisics — All uploads display standard (URL_TO_INSERT_TERM_2889 https://fairsharing.org/search?fairsharingRegistry=Standard) s compliant usage statistics.


## 1. How to use Zenodo Deposition Web Interface?

This section guides users through the key steps to perform to organize a deposition to Zenodo (URL_TO_INSERT_RECORD_2891 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2892 https://fairsharing.org/FAIRsharing.wy4egf)  using the user interface web component provided by the repository (URL_TO_INSERT_TERM_2890 https://fairsharing.org/search?recordType=repository) .

---

### Zenodo Compatible Data Collection - Login-in

* Login via ORCID (URL_TO_INSERT_RECORD_2894 https://fairsharing.org/FAIRsharing.nx58jg)  or Github (URL_TO_INSERT_RECORD_2893 https://fairsharing.org/FAIRsharing.c55d5e)  credentials

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
name: Uploading files to Zenodo (URL_TO_INSERT_RECORD_2895 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2896 https://fairsharing.org/FAIRsharing.wy4egf) 
alt: Uploading files to Zenodo (URL_TO_INSERT_RECORD_2897 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2898 https://fairsharing.org/FAIRsharing.wy4egf) 
---
Uploading files to Zenodo (URL_TO_INSERT_RECORD_2900 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2901 https://fairsharing.org/FAIRsharing.wy4egf)  Repository (URL_TO_INSERT_TERM_2899 https://fairsharing.org/search?recordType=repository) .
```
````

Files can be dragged and dropped (URL_TO_INSERT_RECORD_2902 https://fairsharing.org/FAIRsharing.31385c) , with the following limitations:
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
name: Starting the file upload to Zenodo (URL_TO_INSERT_RECORD_2903 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2904 https://fairsharing.org/FAIRsharing.wy4egf) 
alt: Starting the file upload  to Zenodo (URL_TO_INSERT_RECORD_2905 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2906 https://fairsharing.org/FAIRsharing.wy4egf) 
---
Starting the file upload to Zenodo (URL_TO_INSERT_RECORD_2908 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2909 https://fairsharing.org/FAIRsharing.wy4egf)  Repository (URL_TO_INSERT_TERM_2907 https://fairsharing.org/search?recordType=repository) .
```
````

The next key step is to select the `upload type`. In this instance, the `Dataset` is selected. This matters as it provide strong typing which is relied on by `search (URL_TO_INSERT_RECORD_2910 https://fairsharing.org/FAIRsharing.52b22c)  engine` and therefore impacts `findability`.


<!-- <img src="/images/OYyz4dT.png" alt="drawing" style="width:500px;" border="1px solid black" align="top" /> -->

````{dropdown} 
:open:
```{figure} /images/OYyz4dT.png
---
height: 150px
name: Selecting the upload type to Zenodo (URL_TO_INSERT_RECORD_2911 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2912 https://fairsharing.org/FAIRsharing.wy4egf) 
alt: Selecting the upload type to Zenodo (URL_TO_INSERT_RECORD_2913 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2914 https://fairsharing.org/FAIRsharing.wy4egf) 
---
Selecting the upload type to Zenodo (URL_TO_INSERT_RECORD_2916 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2917 https://fairsharing.org/FAIRsharing.wy4egf)  Repository (URL_TO_INSERT_TERM_2915 https://fairsharing.org/search?recordType=repository) .
```
````


---

### Zenodo Compatible Data Collection - Providing Metadata

* Basic metadata such as. `title`, `description`, at minima should be provided.
* Authors should be identified, ideally using their `orcid`, so linking can be performed. This affects authors citation and impact evaluation. For IMI FAIR (URL_TO_INSERT_RECORD_2919 https://fairsharing.org/FAIRsharing.WWI10U) plus participants, since all have now such an identifier (URL_TO_INSERT_TERM_2918 https://fairsharing.org/search?recordType=identifier_schema) , the link should be made systematically.

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

* **Reserve a Digital Object Identifier (URL_TO_INSERT_TERM_2921 https://fairsharing.org/search?recordType=identifier_schema)  (URL_TO_INSERT_RECORD_2922 https://fairsharing.org/FAIRsharing.hFLKCn) **: This is a service provided natively by the Zenodo (URL_TO_INSERT_RECORD_2923 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2925 https://fairsharing.org/FAIRsharing.wy4egf)  service, by virtue of its integration with Datacite services. This is quite an important point as it means the Zenodo (URL_TO_INSERT_RECORD_2924 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2926 https://fairsharing.org/FAIRsharing.wy4egf)  submission can be cited. However, remember to carefully review all the data entered in the form as once a doi has been minted, the associated informat (URL_TO_INSERT_TERM_2920 https://fairsharing.org/search?recordType=model_and_format) ion **can not be changed without creating a new version of the arch (URL_TO_INSERT_RECORD_2927 https://fairsharing.org/FAIRsharing.52b22c) ive and therefore minting a new doi**
 


* 'Keywords' can be added to tag the submission. These are free text and no controlled terminology (URL_TO_INSERT_TERM_2928 https://fairsharing.org/search?recordType=terminology_artefact)  can be used in the interface at the moment.

<!-- <img src="/images/9Bp91gX.png" alt="drawing" style="width:700px;" border="1px solid black" align="top" /> -->

````{dropdown} 
:open:
```{figure} /images/9Bp91gX.png
---
height: 600px
name: Setting keywords associated with the Zenodo (URL_TO_INSERT_RECORD_2929 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2930 https://fairsharing.org/FAIRsharing.wy4egf)  deposition
alt:  Setting keywords associated with the Zenodo (URL_TO_INSERT_RECORD_2931 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2932 https://fairsharing.org/FAIRsharing.wy4egf)  deposition
---
Setting keywords associated with the Zenodo (URL_TO_INSERT_RECORD_2933 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2934 https://fairsharing.org/FAIRsharing.wy4egf)  deposition .
```
````


---

###  Zenodo Compatible Data Collection - Access and License information

* Zenodo (URL_TO_INSERT_RECORD_2936 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2937 https://fairsharing.org/FAIRsharing.wy4egf)  provides facilities to set `Access Conditions` and `License`, `Data Controler Contact Informat (URL_TO_INSERT_TERM_2935 https://fairsharing.org/search?recordType=model_and_format) ion`, as well as `Embargo Duration` if applicable.
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



  * Zenodo (URL_TO_INSERT_RECORD_2940 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2941 https://fairsharing.org/FAIRsharing.wy4egf)  places no limit when it comes to duration of the embargo period. So submitters should check EC and IMI guideline (URL_TO_INSERT_TERM_2939 https://fairsharing.org/search?recordType=reporting_guideline) s or local institution (URL_TO_INSERT_TERM_2938 https://fairsharing.org/search?recordType=institution) al requirements for guidance.


* Setting Access Conditions/License, Data Controler Contact Informat (URL_TO_INSERT_TERM_2942 https://fairsharing.org/search?recordType=model_and_format) ion, Embargo Duration if applicable

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

* Start typing to display more licenses available from Zenodo (URL_TO_INSERT_RECORD_2943 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2944 https://fairsharing.org/FAIRsharing.wy4egf) 

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

Since the Zenodo (URL_TO_INSERT_RECORD_2947 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2948 https://fairsharing.org/FAIRsharing.wy4egf)  mission is to collect EC funded data, the repository (URL_TO_INSERT_TERM_2945 https://fairsharing.org/search?recordType=repository)  provides the means to lookup `Grant Informat (URL_TO_INSERT_TERM_2946 https://fairsharing.org/search?recordType=model_and_format) ion`:

<!-- <img src="/images/STjyFbT.png" alt="drawing" style="width:700px;" border="1px solid black" align="top" /> -->

````{dropdown} 
:open:
```{figure} /images/STjyFbT.png
---
height: 200px
name: Linking Funding to Zenodo (URL_TO_INSERT_RECORD_2949 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2950 https://fairsharing.org/FAIRsharing.wy4egf)  Submission
alt:  Linking Funding to Zenodo (URL_TO_INSERT_RECORD_2951 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2952 https://fairsharing.org/FAIRsharing.wy4egf)  Submission
---
Linking Funding to Zenodo (URL_TO_INSERT_RECORD_2953 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2954 https://fairsharing.org/FAIRsharing.wy4egf)  Submission.
```
````


  * Zenodo (URL_TO_INSERT_RECORD_2956 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2957 https://fairsharing.org/FAIRsharing.wy4egf) : openAIRE connected repository (URL_TO_INSERT_TERM_2955 https://fairsharing.org/search?recordType=repository) 

  * Connected to funding agencies

---
### Zenodo Compatible Data Collection - Miscellaneous Information

* Miscellaneous Informat (URL_TO_INSERT_TERM_2958 https://fairsharing.org/search?recordType=model_and_format) ion:

<!-- <img src="/images/uhGZN5t.png" alt="drawing" style="width:700px;" border="1px solid black" align="top" /> -->

````{dropdown} 
:open:
```{figure} /images/uhGZN5t.png
---
height: 500px
name: Miscellaneous Informat (URL_TO_INSERT_TERM_2959 https://fairsharing.org/search?recordType=model_and_format) ion about the Zenodo (URL_TO_INSERT_RECORD_2960 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2961 https://fairsharing.org/FAIRsharing.wy4egf)  Submission
alt:  Miscellaneous Informat (URL_TO_INSERT_TERM_2962 https://fairsharing.org/search?recordType=model_and_format) ion about the Zenodo (URL_TO_INSERT_RECORD_2963 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2964 https://fairsharing.org/FAIRsharing.wy4egf)  Submission
---
Miscellaneous Informat (URL_TO_INSERT_TERM_2965 https://fairsharing.org/search?recordType=model_and_format) ion about the Zenodo (URL_TO_INSERT_RECORD_2966 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2967 https://fairsharing.org/FAIRsharing.wy4egf)  Submission.
```
````


  * Contributors

  * References:

  * Journal (URL_TO_INSERT_TERM_2968 https://fairsharing.org/search?recordType=journal) , Conference, Book, and so on.



## 2. Programmatic Deposition to Zenodo via the REST-API

### Create a zenodo account and obtain an API token

* First, it is necessary to obtain an api key:

    `AC (URL_TO_INSERT_RECORD_2972 https://fairsharing.org/FAIRsharing.md3e78) CESS_TO (URL_TO_INSERT_RECORD_2971 https://fairsharing.org/FAIRsharing.w69t6r) K (URL_TO_INSERT_RECORD_2970 https://fairsharing.org/FAIRsharing.cyv30a) EN` = "<enter-your_writeonly_token_for_testing or your_deposit_token if you want to get a DOI (URL_TO_INSERT_RECORD_2969 https://fairsharing.org/FAIRsharing.hFLKCn)   >"

* Then, the following code invoking the Zenodo (URL_TO_INSERT_RECORD_2973 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_2974 https://fairsharing.org/FAIRsharing.wy4egf)  REST endpoint will allow deposition:

    ```python
    import requests
    import json

    zenodo (URL_TO_INSERT_RECORD_2975 https://fairsharing.org/FAIRsharing.wy4egf) _baseurl = "https://zenodo.org/api/"
    headers = {"Content-Type": "application/json"}

    AC (URL_TO_INSERT_RECORD_2981 https://fairsharing.org/FAIRsharing.md3e78) CESS_TO (URL_TO_INSERT_RECORD_2979 https://fairsharing.org/FAIRsharing.w69t6r) K (URL_TO_INSERT_RECORD_2976 https://fairsharing.org/FAIRsharing.cyv30a) EN = "<YOUR_TO (URL_TO_INSERT_RECORD_2980 https://fairsharing.org/FAIRsharing.w69t6r) K (URL_TO_INSERT_RECORD_2977 https://fairsharing.org/FAIRsharing.cyv30a) EN_GO (URL_TO_INSERT_RECORD_2978 https://fairsharing.org/FAIRsharing.6xq0ee) ES_HERE>"
    # testing the connection
    r = requests.get("https://zenodo.org/api/deposit/depositions", params={"access_token": AC (URL_TO_INSERT_RECORD_2984 https://fairsharing.org/FAIRsharing.md3e78) CESS_TO (URL_TO_INSERT_RECORD_2983 https://fairsharing.org/FAIRsharing.w69t6r) K (URL_TO_INSERT_RECORD_2982 https://fairsharing.org/FAIRsharing.cyv30a) EN})

    # creating an empty submission to get an zenodo (URL_TO_INSERT_RECORD_2985 https://fairsharing.org/FAIRsharing.wy4egf)  record id:
    r = requests.post('https://zenodo.org/api/deposit/depositions', params={'access_token': AC (URL_TO_INSERT_RECORD_2988 https://fairsharing.org/FAIRsharing.md3e78) CESS_TO (URL_TO_INSERT_RECORD_2987 https://fairsharing.org/FAIRsharing.w69t6r) K (URL_TO_INSERT_RECORD_2986 https://fairsharing.org/FAIRsharing.cyv30a) EN}, json={},
                      headers=headers)
    r.status_code

    # obtain the zenodo (URL_TO_INSERT_RECORD_2989 https://fairsharing.org/FAIRsharing.wy4egf)  metadata payload as json containing the id
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
                       params={'access_token': AC (URL_TO_INSERT_RECORD_2992 https://fairsharing.org/FAIRsharing.md3e78) CESS_TO (URL_TO_INSERT_RECORD_2991 https://fairsharing.org/FAIRsharing.w69t6r) K (URL_TO_INSERT_RECORD_2990 https://fairsharing.org/FAIRsharing.cyv30a) EN}, data=data,
                       files=files)
    r.status_code
    ```


* Forming the augmented data payload for a dataset corresponding to the JSO (URL_TO_INSERT_RECORD_2994 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_2993 https://fairsharing.org/FAIRsharing.5bbab9)  data package (URL_TO_INSERT_RECORD_2995 https://fairsharing.org/FAIRsharing.3b861d)  for the matrix

    ```python

    metadata = {
         "metadata": {
             "title": "Frictionless Tabular data package (URL_TO_INSERT_RECORD_2996 https://fairsharing.org/FAIRsharing.082881)  (URL_TO_INSERT_RECORD_2997 https://fairsharing.org/FAIRsharing.3b861d)  for GC-MS data from Rose Genome article published\
              in Nature genetics, June, 2018",
             "upload_type": "dataset",
             "description": "This dataset, in the form of a Frictionless Tabular Data Package (URL_TO_INSERT_RECORD_2998 https://fairsharing.org/FAIRsharing.082881)  (URL_TO_INSERT_RECORD_2999 https://fairsharing.org/FAIRsharing.3b861d)  (URL_TO_INSERT_RECORD_3000 https://fairsharing.org/FAIRsharing.3b861d)  \
             (https://frictionlessdata.io/specs/tabular-data-package (URL_TO_INSERT_RECORD_3001 https://fairsharing.org/FAIRsharing.082881) /), \
              holds the measurements of 61 known metabolites (all annotated with resolvable CHEBI identifier (URL_TO_INSERT_TERM_3002 https://fairsharing.org/search?recordType=identifier_schema) s and InChi), \
              measured by gas chromatography mass-spectrometry (GC-MS) in 6 different Rose cultivars (all annotated with \
              resolvable NCBITaxId) and 3 organism parts (all annotated with resolvable Plant Ontology (URL_TO_INSERT_TERM_3003 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_3005 https://fairsharing.org/FAIRsharing.3ngg40)  identifier (URL_TO_INSERT_TERM_3004 https://fairsharing.org/search?recordType=identifier_schema) s).\
              The data was extracted from a supplementary material table, available from \
              https://static-content.springer.com/esm/art%3A10.1038%2Fs41588-018-0110-3/MediaObjects/41588_2018_110_MOESM3_ESM.zip \
              and published alongside the Nature Genetics manuscript identified by the following doi: \
              https://doi.org/10.1038/s41588-018-0110-3, published in June 2018. \
              This dataset is used to demonstrate how to make data Findable, Accessible, Discoverable and Interoperable" \
              "(FAIR (URL_TO_INSERT_RECORD_3009 https://fairsharing.org/FAIRsharing.WWI10U) ) and how Tabular Data Package (URL_TO_INSERT_RECORD_3006 https://fairsharing.org/FAIRsharing.082881)  (URL_TO_INSERT_RECORD_3007 https://fairsharing.org/FAIRsharing.3b861d)  (URL_TO_INSERT_RECORD_3008 https://fairsharing.org/FAIRsharing.3b861d)  representations can be easily mobilized for re-analysis and data science. \
              It is associated to the following project (URL_TO_INSERT_TERM_3010 https://fairsharing.org/search?recordType=project)  available from github (URL_TO_INSERT_RECORD_3011 https://fairsharing.org/FAIRsharing.c55d5e)  at: \
              'https://github.com (URL_TO_INSERT_RECORD_3013 https://fairsharing.org/FAIRsharing.c55d5e) /proccaserra/rose2018ng-notebook' with all necessary informat (URL_TO_INSERT_TERM_3012 https://fairsharing.org/search?recordType=model_and_format) ion and Jupyter notebooks.",
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
                 "FAIR (URL_TO_INSERT_RECORD_3014 https://fairsharing.org/FAIRsharing.WWI10U)  data",
                 "Design of Experiment",
                 "Rose scent",
                 "targeted metabolite profiling",
                 "gas chromatography mass spectrometry",
                 "Tabular Data Package (URL_TO_INSERT_RECORD_3015 https://fairsharing.org/FAIRsharing.082881)  (URL_TO_INSERT_RECORD_3016 https://fairsharing.org/FAIRsharing.3b861d)  (URL_TO_INSERT_RECORD_3017 https://fairsharing.org/FAIRsharing.3b861d) ",
                 "STATO (URL_TO_INSERT_RECORD_3019 https://fairsharing.org/FAIRsharing.w69t6r)  (URL_TO_INSERT_RECORD_3020 https://fairsharing.org/FAIRsharing.na5xp)  ontology (URL_TO_INSERT_TERM_3018 https://fairsharing.org/search?recordType=terminology_artefact) ",
                 "ISA format (URL_TO_INSERT_TERM_3021 https://fairsharing.org/search?recordType=model_and_format) ",
                 "interoperability"],
             "language": "eng",
             "license": {
                    "id": "CC-BY-4.0"
                        },
             "publication_date": "2019-03-13",
             "references": ["https://doi.org/10.1038/s41588-018-0110-3"],
             "related_identifier (URL_TO_INSERT_TERM_3022 https://fairsharing.org/search?recordType=identifier_schema) s": [
              {
                "relation": "cites",
                "identifier (URL_TO_INSERT_TERM_3023 https://fairsharing.org/search?recordType=identifier_schema) ": "10.1038/s41588-018-0110-3"
              },
              {
                "relation": "cites",
                "identifier (URL_TO_INSERT_TERM_3024 https://fairsharing.org/search?recordType=identifier_schema) ": "10.5281/zenodo (URL_TO_INSERT_RECORD_3025 https://fairsharing.org/FAIRsharing.wy4egf) .2598799"
              },
              {
                "relation": "isNewVersionOf",
                "identifier (URL_TO_INSERT_TERM_3026 https://fairsharing.org/search?recordType=identifier_schema) ": "10.5281/zenodo (URL_TO_INSERT_RECORD_3027 https://fairsharing.org/FAIRsharing.wy4egf) .2557893"
              }
            ],
             "grants": [{"links":{"self":"https://zenodo.org/api/grants/10.13039/501100000780::654241"},"acronym": "PhenoMenAl",
            "program": "H2020",
            "funder (URL_TO_INSERT_TERM_3028 https://fairsharing.org/search?recordType=funder) ": {
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
                      params={"access_token": AC (URL_TO_INSERT_RECORD_3031 https://fairsharing.org/FAIRsharing.md3e78) CESS_TO (URL_TO_INSERT_RECORD_3030 https://fairsharing.org/FAIRsharing.w69t6r) K (URL_TO_INSERT_RECORD_3029 https://fairsharing.org/FAIRsharing.cyv30a) EN}, data=json.dumps(metadata),
                     headers=headers)

    r.status_code
    ```

### Finalize request and post

* Finally, combine metadata and data payload in order to send a properlly formed request and obtain a DOI (URL_TO_INSERT_RECORD_3032 https://fairsharing.org/FAIRsharing.hFLKCn) .

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

> Relying on CERN Zenodo (URL_TO_INSERT_RECORD_3034 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_3035 https://fairsharing.org/FAIRsharing.wy4egf)  repository (URL_TO_INSERT_TERM_3033 https://fairsharing.org/search?recordType=repository)  using any of the submission mechanisms (either web component or API) is one the simplest yet highly effective ways to deliver **dataset findability** for assets generated by publicly funded resources. 
> The integration with ORCID<!-- TODO add a link to corresponding document --> makes it very easy to obtain an account on CERN's service. 
> The integration with Datacite<!-- TODO add a link to corresponding document --> means that submitters can reserve and obtain Digital Object Identifiers (DOI) very simply. These can then be cited and used as references to the datasets.
> The integration with Crossref<!-- TODO add a link to corresponding document --> means that funding information case be easily looked up, thus reducing data entry burden in most conditions but especially for EU funded projects such as IMI.
> Licensing informat (URL_TO_INSERT_TERM_3036 https://fairsharing.org/search?recordType=model_and_format) ion can also be easily supplied.
> Data access and embargo dates can be reserved.
> Findability via search (URL_TO_INSERT_RECORD_3042 https://fairsharing.org/FAIRsharing.52b22c)  engines is enhanced as Zenodo (URL_TO_INSERT_RECORD_3040 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_3041 https://fairsharing.org/FAIRsharing.wy4egf)  supports content negotiation, serving [schema.org (URL_TO_INSERT_RECORD_3043 https://fairsharing.org/FAIRsharing.hzdzq8) ](https://schema.org (URL_TO_INSERT_RECORD_3044 https://fairsharing.org/FAIRsharing.hzdzq8) ) based JSO (URL_TO_INSERT_RECORD_3038 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_3037 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_3039 https://fairsharing.org/FAIRsharing.8f9bbb)  documents.
> Users should however be reminded of the following limitations of the service:
    > - Absence of constraints on the nature of the datafiles being uploaded.
    > - No domain specific awareness and domain specific metadata.
    > - Absence of connection with specialized repositories (URL_TO_INSERT_TERM_3045 https://fairsharing.org/search?recordType=repository) .
    > - Size limitation for a given datasets.
    
    

### What to read next?
* [How to build a data catalogue?](fcb-infra-build-catalog)
* How to deploy the FAIRPORT data catalogue?<!-- TODO add a link to corresponding document -->
* [What is search (URL_TO_INSERT_RECORD_3046 https://fairsharing.org/FAIRsharing.52b22c)  engine optimization?](fcb-find-seo)
 
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
