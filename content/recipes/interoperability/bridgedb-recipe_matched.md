(fcb-bridgedb (URL_TO_INSERT_RECORD_4208 https://fairsharing.org/FAIRsharing.5ry74y) -recipe)=
# Identifier mapping with BridgeDb


<!--
TODO : the recipe does not reference its figures
-->

````{panels_fairplus}
:identifier_text: FCB017
:identifier_link: 'https://w3id.org/faircookbook/FCB017'
:difficulty_level: 3
:recipe_type: hands_on
:reading_time_minutes: 30
:intended_audience: principal_investigator, data_manager, data_scientist 
:maturity_level: 4
:maturity_indicator: 49
:has_executable_code: nope
:recipe_name: Mapping identifiers with BridgeDb
```` 


## Main Objectives

The main purpose of this recipe is to:

> Provide practical examples on how to **map (URL_TO_INSERT_RECORD_4211 https://fairsharing.org/FAIRsharing.53edcc)  identifier (URL_TO_INSERT_TERM_4209 https://fairsharing.org/search?recordType=identifier_schema) s for Genes, Protein (URL_TO_INSERT_RECORD_4210 https://fairsharing.org/FAIRsharing.rtndct) s, Metabolites and Pathways** between resources using a purpose built tool, namely [BridgeDb](https://bio.tools (URL_TO_INSERT_RECORD_4212 https://fairsharing.org/FAIRsharing.63520c) /bridgedb).
> Hands on guidance is provided for 2 interfaces (R package and a Python Webservices) provided by [BridgeDb](https://bio.tools (URL_TO_INSERT_RECORD_4213 https://fairsharing.org/FAIRsharing.63520c) /bridgedb).


---


## Graphical Overview

This recipe will cover the highlighted topics

````{dropdown} 
:open:
```{figure} identifier-mapping.md-figure1.mmd.png
---
width: 1000px
name: bridgedb (URL_TO_INSERT_RECORD_4214 https://fairsharing.org/FAIRsharing.5ry74y) -recipe-figure0
alt: Overview of key aspects in Identifier (URL_TO_INSERT_TERM_4215 https://fairsharing.org/search?recordType=identifier_schema)  Map (URL_TO_INSERT_RECORD_4216 https://fairsharing.org/FAIRsharing.53edcc) ping
---
Overview of key aspects in Identifier (URL_TO_INSERT_TERM_4217 https://fairsharing.org/search?recordType=identifier_schema)  Map (URL_TO_INSERT_RECORD_4218 https://fairsharing.org/FAIRsharing.53edcc) ping
```
````

---


## Requirements

This recipe has the following requirements:

* Recipe dependency:
    <!-- TODO (recipe not existent yet ) * {ref}`fcb-identifiers` -->
    * {ref}`fcb-identifier (URL_TO_INSERT_TERM_4219 https://fairsharing.org/search?recordType=identifier_schema) -map (URL_TO_INSERT_RECORD_4220 https://fairsharing.org/FAIRsharing.53edcc) ping`

* Skill dependency:
    * Programming knowledge
    * R
    * Python

* Technical dependency
    * R or Python environment
    * BridgeDb (URL_TO_INSERT_RECORD_4221 https://fairsharing.org/FAIRsharing.5ry74y)  R package installed
---

## Tools

The table below lists the software that is used to execute the examples in this recipe.

| Software                                            | Description                                                                                                                                                                               | version | Biotools record                                          |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------------------------------------------- 
| [BridgeDb webservices](https://bridgedb.github.io (URL_TO_INSERT_RECORD_4228 https://fairsharing.org/FAIRsharing.5ry74y) /) | BridgeDb (URL_TO_INSERT_RECORD_4227 https://fairsharing.org/FAIRsharing.5ry74y)  is a framework to map (URL_TO_INSERT_RECORD_4229 https://fairsharing.org/FAIRsharing.53edcc)  identifier (URL_TO_INSERT_TERM_4224 https://fairsharing.org/search?recordType=identifier_schema) s between various database (URL_TO_INSERT_TERM_4222 https://fairsharing.org/search?fairsharingRegistry=Database) s. It includes a Java library that provides an API to work with identifier (URL_TO_INSERT_TERM_4225 https://fairsharing.org/search?recordType=identifier_schema) -identifier (URL_TO_INSERT_TERM_4226 https://fairsharing.org/search?recordType=identifier_schema)  map (URL_TO_INSERT_RECORD_4230 https://fairsharing.org/FAIRsharing.53edcc) ping database (URL_TO_INSERT_TERM_4223 https://fairsharing.org/search?fairsharingRegistry=Database) s and resources. | 0.0.9   | [https://bio.tools (URL_TO_INSERT_RECORD_4231 https://fairsharing.org/FAIRsharing.63520c) /bridgedb](https://bio.tools (URL_TO_INSERT_RECORD_4232 https://fairsharing.org/FAIRsharing.63520c) /bridgedb) |
| Python                                              | An interpreted, high-level and general-purpose programming language.                                                                                                                       | 3.8.5   |                                                          |
| [pandas](https://pandas.pydata.org/)                | pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.                                     | 1.1.3   |                                                          |
| R                                                   | R is a programming language and free software environment for statistical computing and graphics supported by the R Foundation for Statistical Computing.                                 | v4.0.3  | https://bio.tools (URL_TO_INSERT_RECORD_4233 https://fairsharing.org/FAIRsharing.63520c) /r                                      |
| [tidyverse](https://www.tidyverse.org/)                                           | tidyverse is an opinionated collection (URL_TO_INSERT_TERM_4234 https://fairsharing.org/search?recordType=collection)  of R packages designed for data science.  | 1.3.0||
|[BridgeDbR](https://doi.org/doi:10.18129/B9.bioc.BridgeDbR)|An R package for BridgeDb (URL_TO_INSERT_RECORD_4235 https://fairsharing.org/FAIRsharing.5ry74y) | 2.0.0||

---

## Identifier mapping with BridgeDb

{ref}`Interlinking data from different sources <fcb-identifier (URL_TO_INSERT_TERM_4236 https://fairsharing.org/search?recordType=identifier_schema) -map (URL_TO_INSERT_RECORD_4238 https://fairsharing.org/FAIRsharing.53edcc) ping>` is an essential step for data reusability and interoperability. This step requires dedicated tools. With the present recipe, we show how to use [BridgeDb](https://bridgedb.github.io (URL_TO_INSERT_RECORD_4237 https://fairsharing.org/FAIRsharing.5ry74y) /) to carry out this process.

[BridgeDb](https://bridgedb.github.io (URL_TO_INSERT_RECORD_4242 https://fairsharing.org/FAIRsharing.5ry74y) /) is an open source tool dedicated to performing identifier (URL_TO_INSERT_TERM_4239 https://fairsharing.org/search?recordType=identifier_schema)  map (URL_TO_INSERT_RECORD_4243 https://fairsharing.org/FAIRsharing.53edcc) ping {footcite}`van_iersel_bridgedb (URL_TO_INSERT_RECORD_4240 https://fairsharing.org/FAIRsharing.5ry74y) _2010`. BridgeDb (URL_TO_INSERT_RECORD_4241 https://fairsharing.org/FAIRsharing.5ry74y)  offers three different interfaces:
* Java API
* R package
* REST Web-services


> 📖 In the context of this recipe, we distinguish between two types of identifier (URL_TO_INSERT_TERM_4244 https://fairsharing.org/search?recordType=identifier_schema) s:
>* *Local identifier (URL_TO_INSERT_TERM_4246 https://fairsharing.org/search?recordType=identifier_schema) s* which refer to identifier (URL_TO_INSERT_TERM_4247 https://fairsharing.org/search?recordType=identifier_schema) s that are minted within an organization or database (URL_TO_INSERT_TERM_4245 https://fairsharing.org/search?fairsharingRegistry=Database)  and thus internally defined (i.e. local to said organization). 
>* *Global identifier (URL_TO_INSERT_TERM_4248 https://fairsharing.org/search?recordType=identifier_schema) s* which refer to identifier (URL_TO_INSERT_TERM_4249 https://fairsharing.org/search?recordType=identifier_schema) s that are globally unique and uniquely point to an entity, as available from BridgeDb (URL_TO_INSERT_RECORD_4250 https://fairsharing.org/FAIRsharing.5ry74y) 's [data sources file](https://github.com (URL_TO_INSERT_RECORD_4251 https://fairsharing.org/FAIRsharing.c55d5e) /bridgedb/datasources)

We will focus here on two distinct cases, depending on the nature of the incoming data. Namely, whether our data is already using global identifier (URL_TO_INSERT_TERM_4252 https://fairsharing.org/search?recordType=identifier_schema) s or only relies on local identifier (URL_TO_INSERT_TERM_4253 https://fairsharing.org/search?recordType=identifier_schema) s. 

In this recipe, we will cover how BridgeDb (URL_TO_INSERT_RECORD_4255 https://fairsharing.org/FAIRsharing.5ry74y) 's R package and webservices can be used to map (URL_TO_INSERT_RECORD_4256 https://fairsharing.org/FAIRsharing.53edcc)  between resource identifier (URL_TO_INSERT_TERM_4254 https://fairsharing.org/search?recordType=identifier_schema) s.

### Mapping a global identifier to other global identifiers
In this case, the input data is a list of elements with an identifier (URL_TO_INSERT_TERM_4257 https://fairsharing.org/search?recordType=identifier_schema)  that is part of [BridgeDb's data sources](https://github.com (URL_TO_INSERT_RECORD_4263 https://fairsharing.org/FAIRsharing.c55d5e) /bridgedb/datasources). In our example, we will use a list of Homo Sapien Hugo Gene Nomenclature Convention ([HGNC](http://www.genenames.org (URL_TO_INSERT_RECORD_4261 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4264 https://fairsharing.org/FAIRsharing.29we0s) )) gene identifier (URL_TO_INSERT_TERM_4258 https://fairsharing.org/search?recordType=identifier_schema) s stored in a TSV (URL_TO_INSERT_RECORD_4260 https://fairsharing.org/FAIRsharing.a978c9)  file. The objective is to map (URL_TO_INSERT_RECORD_4262 https://fairsharing.org/FAIRsharing.53edcc)  these to other available gene identifier (URL_TO_INSERT_TERM_4259 https://fairsharing.org/search?recordType=identifier_schema) s.

#### BridgeDb via Webservices using Python
> ❗ For this tutorial Python v3.8.5, [pandas](https://pandas.pydata.org/) v1.1.3, and BridgeDb (URL_TO_INSERT_RECORD_4265 https://fairsharing.org/FAIRsharing.5ry74y)  Webservices v0.9.0 were used.

One of the biggest benefits of using BridgeDb (URL_TO_INSERT_RECORD_4267 https://fairsharing.org/FAIRsharing.5ry74y)  webservices is that these can be accessed using most programming languages. Python has become one of the leading programming languages in data science and predictive model (URL_TO_INSERT_TERM_4266 https://fairsharing.org/search?recordType=model_and_format) ling. Despite the lack of a dedicated BridgeDb (URL_TO_INSERT_RECORD_4268 https://fairsharing.org/FAIRsharing.5ry74y)  Python library, we show here how to use the BridgeDb (URL_TO_INSERT_RECORD_4269 https://fairsharing.org/FAIRsharing.5ry74y)  Webservices to perform exemplary map (URL_TO_INSERT_RECORD_4270 https://fairsharing.org/FAIRsharing.53edcc) pings.

We start by defining string (URL_TO_INSERT_RECORD_4274 https://fairsharing.org/FAIRsharing.9b7wvk) s containing the URL (URL_TO_INSERT_RECORD_4272 https://fairsharing.org/FAIRsharing.9d38e2)  of the webservices and the specific method from the Webservices we want to use. In our case, a `batch cross reference`. When doing the query, we need to specify **the organism** and **the source dataset**. We can also *optionally* specify a *target data source* if we only want to map (URL_TO_INSERT_RECORD_4273 https://fairsharing.org/FAIRsharing.53edcc)  to a specific data source, e.g. Ensembl (URL_TO_INSERT_RECORD_4271 https://fairsharing.org/FAIRsharing.fx0mw7) .

```python
url = "https://webservice.bridgedb.org/"
batch_request = url+"{org}/xrefsBatch/{source}{}"
```

If the aim is to map (URL_TO_INSERT_RECORD_4275 https://fairsharing.org/FAIRsharing.53edcc)  only to a specific target data source, then one can check whether the map (URL_TO_INSERT_RECORD_4276 https://fairsharing.org/FAIRsharing.53edcc) ping is supported by invoking the following webservice call:  

```python
mapping_available = "{org}/isMappingSupported/{source}/{target}"
query = url+mapping_available.format(org='Homo sapiens', source='H', target='En')
requests.get(query).text
```

This will return `True` if the map (URL_TO_INSERT_RECORD_4277 https://fairsharing.org/FAIRsharing.53edcc) ping between the given source and target is supported for the given organism or `False` otherwise.

We then load our data into a pandas dataframe and call the requests library using our query.

```python
query = batch_request.format('?dataSource=En', org='Homo sapiens', source='H')
response = requests.post(query, data=data.to_csv(index=False, header=False))
```

The webservice response is now stored in the `response` variable. We can then simply pass this variable to the `to_df` method provided in the `bridgedb (URL_TO_INSERT_RECORD_4278 https://fairsharing.org/FAIRsharing.5ry74y) _script.py` module (see [Code](#Code)). This method will extract the response in text form and turn it into a pandas Dataframe with conveniently named columns and structured data.

The output table will contain the:
* Original identifier (URL_TO_INSERT_TERM_4279 https://fairsharing.org/search?recordType=identifier_schema) 
* Data source that the identifier (URL_TO_INSERT_TERM_4280 https://fairsharing.org/search?recordType=identifier_schema)  is part of
* Map (URL_TO_INSERT_RECORD_4282 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_4283 https://fairsharing.org/FAIRsharing.31385c)  identifier (URL_TO_INSERT_TERM_4281 https://fairsharing.org/search?recordType=identifier_schema) 
* Data source for the map (URL_TO_INSERT_RECORD_4285 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_4286 https://fairsharing.org/FAIRsharing.31385c)  identifier (URL_TO_INSERT_TERM_4284 https://fairsharing.org/search?recordType=identifier_schema) 

In our case the output of `to_df` is:

| original   | source   | map (URL_TO_INSERT_RECORD_4287 https://fairsharing.org/FAIRsharing.53edcc) ping         | target   |
|:-----------|:---------|:----------------|:---------|
| A1BG       | HGNC (URL_TO_INSERT_RECORD_4288 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4289 https://fairsharing.org/FAIRsharing.29we0s)      | ENSG00000121410 | En       |
| A1CF       | HGNC (URL_TO_INSERT_RECORD_4290 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4291 https://fairsharing.org/FAIRsharing.29we0s)      | ENSG00000148584 | En       |
| A2MP1      | HGNC (URL_TO_INSERT_RECORD_4292 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4293 https://fairsharing.org/FAIRsharing.29we0s)      | ENSG00000256069 | En       |

If we were to not specify the target data source (by passing an empty string (URL_TO_INSERT_RECORD_4296 https://fairsharing.org/FAIRsharing.9b7wvk)  as the parameter), we would get all the potential map (URL_TO_INSERT_RECORD_4295 https://fairsharing.org/FAIRsharing.53edcc) pings for the given identifier (URL_TO_INSERT_TERM_4294 https://fairsharing.org/search?recordType=identifier_schema) s. In our case (top 10 rows):

| original   | source   | map (URL_TO_INSERT_RECORD_4297 https://fairsharing.org/FAIRsharing.53edcc) ping      | target   |
|:-----------|:---------|:-------------|:---------|
| A1BG       | HGNC (URL_TO_INSERT_RECORD_4298 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4299 https://fairsharing.org/FAIRsharing.29we0s)      | uc002qsd.5   | Uc       |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_4300 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4301 https://fairsharing.org/FAIRsharing.29we0s)      | 8039748      | X        |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_4303 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4304 https://fairsharing.org/FAIRsharing.29we0s)      | GO (URL_TO_INSERT_RECORD_4302 https://fairsharing.org/FAIRsharing.6xq0ee) :0072562   | T        |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_4305 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4306 https://fairsharing.org/FAIRsharing.29we0s)      | uc061drj.1   | Uc       |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_4307 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4308 https://fairsharing.org/FAIRsharing.29we0s)      | ILMN_2055271 | Il       |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_4309 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4310 https://fairsharing.org/FAIRsharing.29we0s)      | Hs.529161    | U        |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_4312 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4313 https://fairsharing.org/FAIRsharing.29we0s)      | GO (URL_TO_INSERT_RECORD_4311 https://fairsharing.org/FAIRsharing.6xq0ee) :0070062   | T        |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_4315 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4316 https://fairsharing.org/FAIRsharing.29we0s)      | GO (URL_TO_INSERT_RECORD_4314 https://fairsharing.org/FAIRsharing.6xq0ee) :0002576   | T        |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_4317 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4318 https://fairsharing.org/FAIRsharing.29we0s)      | uc061drt.1   | Uc       |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_4319 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4320 https://fairsharing.org/FAIRsharing.29we0s)      | 51020_at     | X        |

As one can see, using the BridgeDb (URL_TO_INSERT_RECORD_4321 https://fairsharing.org/FAIRsharing.5ry74y)  webservice via Python is extremely simple and can be easily integrated in an annotation pipeline.


#### BridgeDb via the dedicated R package

```{note} 
For this tutorial R v4.0.3, [tidyverse](https://www.tidyverse.org/) v1.3.0, and [BridgeDbR](https://www.bioconductor.org/packages/release/bioc/html/BridgeDbR.html) v2.0.0 were used.
```

After having loaded the required R libraries, we read the data and create a new column to include the source of the identifier (URL_TO_INSERT_TERM_4322 https://fairsharing.org/search?recordType=identifier_schema) .

```r
data_df <- read_tsv(filepath, col_names=c('identifier'))
data_df$source = 'H'
``` 

We then load the data for the organism we are map (URL_TO_INSERT_RECORD_4323 https://fairsharing.org/FAIRsharing.53edcc) ping from.

```r
 location <- getDatabase('Homo sapiens')
 mapper <- loadDatabase(location)
```

And use the library's     dedicated function to map (URL_TO_INSERT_RECORD_4325 https://fairsharing.org/FAIRsharing.53edcc)  the identifier (URL_TO_INSERT_TERM_4324 https://fairsharing.org/search?recordType=identifier_schema) s:

```r
mapping = maps(mapper, data_df, target='En')
```
This will return:
| identifier (URL_TO_INSERT_TERM_4326 https://fairsharing.org/search?recordType=identifier_schema)  | source | target | map (URL_TO_INSERT_RECORD_4327 https://fairsharing.org/FAIRsharing.53edcc) ping         |
|:---------- |:------ |:------ |:--------------- |
| A1BG       | H      | En     | ENSG00000121410 |
| A1CF       | H      | En     | ENSG00000148584 |
| A2MP1      | H      | En     | ENSG00000256069 |

As seen earlier when using Python language, we can obtain all possible map (URL_TO_INSERT_RECORD_4328 https://fairsharing.org/FAIRsharing.53edcc) pings simply by not specifying the target. This will result in (top 10) 
| identifier (URL_TO_INSERT_TERM_4329 https://fairsharing.org/search?recordType=identifier_schema)  | source | target | map (URL_TO_INSERT_RECORD_4330 https://fairsharing.org/FAIRsharing.53edcc) ping      |
|:---------- |:------ |:------ |:------------ |
| A1BG       | H      | Uc     | uc002qsd.5   |
| A1BG       | H      | X      | 8039748      |
| A1BG       | H      | T      | GO (URL_TO_INSERT_RECORD_4331 https://fairsharing.org/FAIRsharing.6xq0ee) :0072562   |
| A1BG       | H      | Uc     | uc061drj.1   |
| A1BG       | H      | Il     | ILMN_2055271 |
| A1BG       | H      | U      | Hs.529161    |
| A1BG       | H      | T      | GO (URL_TO_INSERT_RECORD_4332 https://fairsharing.org/FAIRsharing.6xq0ee) :0070062   |
| A1BG       | H      | T      | GO (URL_TO_INSERT_RECORD_4333 https://fairsharing.org/FAIRsharing.6xq0ee) :0002576   |
| A1BG       | H      | Uc     | uc061drt.1   |
| A1BG       | H      | X      | 51020_at     |

```{warning} 
An error message indicating "Error in download.file" may be thrown. This may be caused by the `timeout` variable being set to too small a value. To remediate the issue, try increasing the timeout variable value by calling `options(timeout=300)`.
```

<!--
This will maybe link to the identifier mapping recipe in the future, where there will be a specific section detailing identifier equivalence files taking into account scientific lenses, as discussed with Egon. 

--------------------------------


### Mapping a local identifier to global identifier
[NEED HELP HERE]
This is a step that should be done manually. In this case an important decision should be made, which identifiers to map to. To decide this you should look for the data source that contains the closest definition of the concepts to the one you used for your local identifiers.

-->

### Mapping local identifier to a different global identifier

```{note} 
 In this section, we assume that we already have an equivalence file containing the mapping of a local identifier to one of the global identifiers. In our case, this will be contained in a TSV where we map our local gene identifier to [HGNC](http://www.genenames.org). One may consult the list of other potential data formats in the {ref}`fcb-identifier-mapping` recipe. The mapping should be **one-to-one** for this recipe. 
```

The TSV (URL_TO_INSERT_RECORD_4334 https://fairsharing.org/FAIRsharing.a978c9)  map (URL_TO_INSERT_RECORD_4335 https://fairsharing.org/FAIRsharing.53edcc) ping file looks as follows:
| local   | source   |
|:--------|:---------|
| aa11    | A1BG     |
| bb34    | A1CF     |
| eg93    | A2MP1    |

You may notice the `source` identifier (URL_TO_INSERT_TERM_4336 https://fairsharing.org/search?recordType=identifier_schema) s correspond with those used in the previous example.


This is how the map (URL_TO_INSERT_RECORD_4337 https://fairsharing.org/FAIRsharing.53edcc) ping will work

````{dropdown} 
:open:
```{figure} bridgedb-recipe.md-figure1.mmd.png
---
name: bridgedb (URL_TO_INSERT_RECORD_4338 https://fairsharing.org/FAIRsharing.5ry74y) -recipe-figure1
alt: Overview of BridgeDb (URL_TO_INSERT_RECORD_4339 https://fairsharing.org/FAIRsharing.5ry74y)  tools
---
Overview of BridgeDb (URL_TO_INSERT_RECORD_4340 https://fairsharing.org/FAIRsharing.5ry74y)  tools
```
````

#### Webservices in Python

As before, we will define variables including the `web-service's URL (URL_TO_INSERT_RECORD_4341 https://fairsharing.org/FAIRsharing.9d38e2) ` and the `method` that we will use, in this instance: `xRefsBatch`.
We then pass the source column to the `post request` as follows

```python
source_data = case2.source.to_csv(index=False, header=False)
query = batch_request.format('', org=org, source=source)
response2 = requests.post(query, data = source_data)
```
You may notice here that we did not pass a target source, this could be done as specified before. Then, we use `to_df` again and as expected obtain the same dataframe as before.
To see the equivalences with our local identifier (URL_TO_INSERT_TERM_4342 https://fairsharing.org/search?recordType=identifier_schema) s, we can simply join the dataframes, as follows:

```python
local_mapping = mappings.join(case2.set_index('source'), on='original')
```
which will return the following table (first 10 rows)
| original   | source   | map (URL_TO_INSERT_RECORD_4343 https://fairsharing.org/FAIRsharing.53edcc) ping      | target   | local   |
|:-----------|:---------|:-------------|:---------|:--------|
| A1BG       | HGNC (URL_TO_INSERT_RECORD_4344 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4345 https://fairsharing.org/FAIRsharing.29we0s)      | uc002qsd.5   | Uc       | aa11    |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_4346 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4347 https://fairsharing.org/FAIRsharing.29we0s)      | 8039748      | X        | aa11    |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_4349 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4350 https://fairsharing.org/FAIRsharing.29we0s)      | GO (URL_TO_INSERT_RECORD_4348 https://fairsharing.org/FAIRsharing.6xq0ee) :0072562   | T        | aa11    |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_4351 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4352 https://fairsharing.org/FAIRsharing.29we0s)      | uc061drj.1   | Uc       | aa11    |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_4353 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4354 https://fairsharing.org/FAIRsharing.29we0s)      | ILMN_2055271 | Il       | aa11    |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_4355 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4356 https://fairsharing.org/FAIRsharing.29we0s)      | Hs.529161    | U        | aa11    |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_4358 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4359 https://fairsharing.org/FAIRsharing.29we0s)      | GO (URL_TO_INSERT_RECORD_4357 https://fairsharing.org/FAIRsharing.6xq0ee) :0070062   | T        | aa11    |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_4361 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4362 https://fairsharing.org/FAIRsharing.29we0s)      | GO (URL_TO_INSERT_RECORD_4360 https://fairsharing.org/FAIRsharing.6xq0ee) :0002576   | T        | aa11    |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_4363 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4364 https://fairsharing.org/FAIRsharing.29we0s)      | uc061drt.1   | Uc       | aa11    |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_4365 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4366 https://fairsharing.org/FAIRsharing.29we0s)      | 51020_at     | X        | aa11    |

In case we did specify the `target` argument to be `Ensembl (URL_TO_INSERT_RECORD_4367 https://fairsharing.org/FAIRsharing.fx0mw7)  (En)`, we would instead get

| original   | source   | map (URL_TO_INSERT_RECORD_4368 https://fairsharing.org/FAIRsharing.53edcc) ping         | target   | local   |
|:-----------|:---------|:----------------|:---------|:--------|
| A1BG       | HGNC (URL_TO_INSERT_RECORD_4369 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4370 https://fairsharing.org/FAIRsharing.29we0s)      | ENSG00000121410 | En       | aa11    |
| A1CF       | HGNC (URL_TO_INSERT_RECORD_4371 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4372 https://fairsharing.org/FAIRsharing.29we0s)      | ENSG00000148584 | En       | bb34    |
| A2MP1      | HGNC (URL_TO_INSERT_RECORD_4373 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4374 https://fairsharing.org/FAIRsharing.29we0s)      | ENSG00000256069 | En       | eg93    |

Here, we see a `one-to-one` relation between the identifier (URL_TO_INSERT_TERM_4376 https://fairsharing.org/search?recordType=identifier_schema) s in HGNC (URL_TO_INSERT_RECORD_4379 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4381 https://fairsharing.org/FAIRsharing.29we0s)  and En while the relation between HGNC (URL_TO_INSERT_RECORD_4380 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4382 https://fairsharing.org/FAIRsharing.29we0s)  and UCSC Genome Browser (Uc) or Gene Ontology (URL_TO_INSERT_TERM_4375 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_4378 https://fairsharing.org/FAIRsharing.6xq0ee)  (T) is `one-to-many`. Depending on the identifier (URL_TO_INSERT_TERM_4377 https://fairsharing.org/search?recordType=identifier_schema) s and resources, the relation could also be `many-to-many` as shown below.


````{dropdown} 
:open:
```{figure} bridgedb-recipe.md-figure2.mmd.png
---
name: bridgedb (URL_TO_INSERT_RECORD_4383 https://fairsharing.org/FAIRsharing.5ry74y) -recipe-figure2
alt: An example of a map (URL_TO_INSERT_RECORD_4385 https://fairsharing.org/FAIRsharing.53edcc) ping via BridgeDb (URL_TO_INSERT_RECORD_4384 https://fairsharing.org/FAIRsharing.5ry74y) .
---
An example of a map (URL_TO_INSERT_RECORD_4387 https://fairsharing.org/FAIRsharing.53edcc) ping via BridgeDb (URL_TO_INSERT_RECORD_4386 https://fairsharing.org/FAIRsharing.5ry74y) . You may notice that despite the 1-to-1 relation between `local` and `original` we get a N-to-N relation between `local` and `map (URL_TO_INSERT_RECORD_4388 https://fairsharing.org/FAIRsharing.53edcc) ping` due to the N-to-N relation between `original` and `map (URL_TO_INSERT_RECORD_4389 https://fairsharing.org/FAIRsharing.53edcc) ping`.
```
````

```{note} 
This many-to-many relationship stems from different *scientific lenses* in the data sources. You can read more about these in {footcite}`batchelor_scientific_nodate`. The core idea is that depending on the domain/application of the data we can consider different entities as unique. While certain proteins could be considered "equal" from a biological perspective they may require differentiation when using a chemical len. This is what then leads to many-to-many relationships.
```

#### R Package

Here, we will follow the same steps as in the previous case. The only difference is that we need to specify the columns/fields to use when loading the data:

```r
data_df <- read_tsv(filepath, col_names=c('local', 'identifier'))
``` 
Then, after computing the map (URL_TO_INSERT_RECORD_4391 https://fairsharing.org/FAIRsharing.53edcc) ping, we can join it with the local identifier (URL_TO_INSERT_TERM_4390 https://fairsharing.org/search?recordType=identifier_schema) 

```r
right_join(data_df, mapping)
```
Assuming we did not specify the target data source we obtain the following table (first 10 rows):
| local | identifier (URL_TO_INSERT_TERM_4392 https://fairsharing.org/search?recordType=identifier_schema)  | source | target | map (URL_TO_INSERT_RECORD_4393 https://fairsharing.org/FAIRsharing.53edcc) ping      |
|:----- |:--------   |:------ |:------ |:------------ |
| aa11  | A1BG       | H      | Uc     | uc002qsd.5   |
| aa11  | A1BG       | H      | X      | 8039748      |
| aa11  | A1BG       | H      | T      | GO (URL_TO_INSERT_RECORD_4394 https://fairsharing.org/FAIRsharing.6xq0ee) :0072562   |
| aa11  | A1BG       | H      | Uc     | uc061drj.1   |
| aa11  | A1BG       | H      | Il     | ILMN_2055271 |
| aa11  | A1BG       | H      | U      | Hs.529161    |
| aa11  | A1BG       | H      | T      | GO (URL_TO_INSERT_RECORD_4395 https://fairsharing.org/FAIRsharing.6xq0ee) :0070062   |
| aa11  | A1BG       | H      | T      | GO (URL_TO_INSERT_RECORD_4396 https://fairsharing.org/FAIRsharing.6xq0ee) :0002576   |
| aa11  | A1BG       | H      | Uc     | uc061drt.1   |
| aa11  | A1BG       | H      | X      | 51020_at     |

In case we did specify the target data source we would get:

| local | identifier (URL_TO_INSERT_TERM_4397 https://fairsharing.org/search?recordType=identifier_schema)  | source | target | map (URL_TO_INSERT_RECORD_4398 https://fairsharing.org/FAIRsharing.53edcc) ping         |
|:----- |:---------- |:------ |:------ |:--------------- |
| aa11  | A1BG       | HGNC (URL_TO_INSERT_RECORD_4399 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4400 https://fairsharing.org/FAIRsharing.29we0s)    | En     | ENSG00000121410 |
| bb34  | A1CF       | HGNC (URL_TO_INSERT_RECORD_4401 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4402 https://fairsharing.org/FAIRsharing.29we0s)    | En     | ENSG00000148584 |
| eg93  | A2MP1      | HGNC (URL_TO_INSERT_RECORD_4403 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_4404 https://fairsharing.org/FAIRsharing.29we0s)    | En     | ENSG00000256069 |

---
## Provenance

BridgeDb (URL_TO_INSERT_RECORD_4406 https://fairsharing.org/FAIRsharing.5ry74y)  provides provenance informat (URL_TO_INSERT_TERM_4405 https://fairsharing.org/search?recordType=model_and_format) ion through:
* A call to `/properties/` method of the Webservice
* `getProperties()` in BridgeDb (URL_TO_INSERT_RECORD_4407 https://fairsharing.org/FAIRsharing.5ry74y) R (passing the map (URL_TO_INSERT_RECORD_4408 https://fairsharing.org/FAIRsharing.53edcc) per as a parameter)

This returns the following informat (URL_TO_INSERT_TERM_4409 https://fairsharing.org/search?recordType=model_and_format) ion for each of the data sources for a given organism:
* Data source name
* Build date
* Series
* Data type
* Data source version
* Schema version

Improvements on provenance are under way (see [here](https://github.com (URL_TO_INSERT_RECORD_4410 https://fairsharing.org/FAIRsharing.c55d5e) /bridgedb/BridgeDb/issues/164)).

---

## Code 
You can find ready-made methods to map (URL_TO_INSERT_RECORD_4411 https://fairsharing.org/FAIRsharing.53edcc)  using R and Python for the given use cases [here](https://github.com (URL_TO_INSERT_RECORD_4412 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/the-fair-cookbook/tree/9ad9481be32812b2565f9f9f1897642ae26eddff/content/recipes/interoperability/bridgedb/data). These assume the data has the structure described in this recipe.

---

## Conclusion

We showed how to use BridgeDb (URL_TO_INSERT_RECORD_4414 https://fairsharing.org/FAIRsharing.5ry74y) 's webservices and R package to map (URL_TO_INSERT_RECORD_4415 https://fairsharing.org/FAIRsharing.53edcc)  identifier (URL_TO_INSERT_TERM_4413 https://fairsharing.org/search?recordType=identifier_schema) s from different data sources using a minimal dataset. 
BridgeDb (URL_TO_INSERT_RECORD_4416 https://fairsharing.org/FAIRsharing.5ry74y)  provides handy functionality to make 'omics' data more interoperable and reusable.
As with all annotation services, it is important to bear in mind the version of the service being used as well as the data on which the service invokation has been performed.
These are aspects of informat (URL_TO_INSERT_TERM_4417 https://fairsharing.org/search?recordType=model_and_format) ion provenance which we plan to provide in the future.
 
### What to read next?

* {ref}`fcb-find-identifier (URL_TO_INSERT_TERM_4418 https://fairsharing.org/search?recordType=identifier_schema) s`
* {ref}`fcb-identifier (URL_TO_INSERT_TERM_4419 https://fairsharing.org/search?recordType=identifier_schema) -map (URL_TO_INSERT_RECORD_4420 https://fairsharing.org/FAIRsharing.53edcc) ping`

````{rdmkit_panel}
````

---


## References

````{dropdown} **references**
```{footbibliography}
```
````

## Authors

````{authors_fairplus}
Lucas: Writing - Original Draft
Philippe: Writing - Review & Editing
Alasdair: Writing - Review & Editing
````


## License

````{license_fairplus}
CC-BY-4.0
````
