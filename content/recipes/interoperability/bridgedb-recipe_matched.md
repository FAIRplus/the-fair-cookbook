(fcb-bridgedb(URL_TO_INSERT_RECORD https://bridgedb.github.io)-recipe)=
# Identifier mapping with BridgeDb


<!--
TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO : the recipe does not reference its figures
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

> Provide practical examples on how to **map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map) identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s for Genes, Protein(URL_TO_INSERT_RECORD http://www.ncbi.nlm.nih.gov/protein)s, Metabolites and Pathways** between resources using a purpose built tool, namely [BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io)](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/bridgedb).
> Hands on guidance is provided for 2 interfaces (R package and a Python Webservices) provided by [BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io)](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/bridgedb).


---


## Graphical Overview

This recipe will cover the highlighted topics

````{dropdown} 
:open:
```{figure} identifier-mapping.md-figure1.mmd.png
---
width: 1000px
name: bridgedb(URL_TO_INSERT_RECORD https://bridgedb.github.io)-recipe-figure0
alt: Overview of key aspects in Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) Map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping
---
Overview of key aspects in Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) Map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping
```
````

---


## Requirements

This recipe has the following requirements:

* Recipe dependency:
    <!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO (recipe not existent yet ) * {ref}`fcb-identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s` -->
    * {ref}`fcb-identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)-map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping`

* Skill dependency:
    * Programming knowledge
    * R
    * Python

* Technical dependency
    * R or Python environment
    * BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io) R package installed
---

## Tools

The table below lists the software that is used to execute the examples in this recipe.

| Software                                            | Description                                                                                                                                                                               | version | Biotools record                                          |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------------------------------------------- 
| [BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io) webservices](https://bridgedb.github.io(URL_TO_INSERT_RECORD https://bridgedb.github.io)/) | BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io) is a framework to map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map) identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s between various database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)s. It includes a Java library that provides an API to work with identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)-identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)s and resources. | 0.0.9   | [https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/bridgedb](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/bridgedb) |
| Python                                              | An interpreted, high-level and general-purpose programming language.                                                                                                                       | 3.8.5   |                                                          |
| [pandas](https://pandas.pydata.org/)                | pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.                                     | 1.1.3   |                                                          |
| R                                                   | R is a programming language and free software environment for statistical computing and graphics supported by the R Foundation for Statistical Computing.                                 | v4.0.3  | https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/r                                      |
| [tidyverse](https://www.tidyverse.org/)                                           | tidyverse is an opinionated collection (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=collection) of R packages designed for data science.  | 1.3.0||
|[BridgeDbR](https://doi.org/doi:10.18129/B9.bioc.BridgeDbR)|An R package for BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io)| 2.0.0||

---

## Identifier mapping with BridgeDb

{ref}`Interlinking data from different sources <fcb-identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)-map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping>` is an essential step for data reusability and interoperability. This step requires dedicated tools. With the present recipe, we show how to use [BridgeDb](https://bridgedb.github.io(URL_TO_INSERT_RECORD https://bridgedb.github.io)/) to carry out this process.

[BridgeDb](https://bridgedb.github.io(URL_TO_INSERT_RECORD https://bridgedb.github.io)/) is an open source tool dedicated to performing identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping {footcite}`van_iersel_bridgedb(URL_TO_INSERT_RECORD https://bridgedb.github.io)_2010`. BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io) offers three different interfaces:
* Java API
* R package
* REST Web-services


> 📖 In the context of this recipe, we disting(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html)uish between two types of identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s:
>* *Local identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s* which refer to identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s that are minted within an organization or database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database) and thus internally defined (i.e. local to said organization). 
>* *Global identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s* which refer to identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s that are globally unique and uniquely point to an entity, as available from BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io)'s [data sources file](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/bridgedb/datasources)

We will focus here on two distinct cases, depending on the nature of the incoming data. Namely, whether our data is already using global identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s or only relies on local identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s. 

In this recipe, we will cover how BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io)'s R package and webservices can be used to map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map) between resource identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s.

### Mapping a global identifier to other global identifiers
In this case, the input data is a list of elements with an identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) that is part of [BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io)'s data sources](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/bridgedb/datasources). In our example, we will use a list of Homo Sapien Hugo Gene Nomenclature Convention ([HGNC](http://www.genenames.org(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/))) gene identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s stored in a TSV(URL_TO_INSERT_RECORD http://www.iana.org/assignments/media-types/text/tab-separated-values) file. The objective is to map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map) these to other available gene identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s.

#### BridgeDb via Webservices using Python
> ❗ For this tutorial Python v3.8.5, [pandas](https://pandas.pydata.org/) v1.1.3, and BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io) Webservices v0.9.0 were used.

One of the biggest benefits of using BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io) webservices is that these can be accessed using most programming languages. Python has become one of the leading programming languages in data science and predictive model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ling. Despite the lack of a dedicated BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io) Python library, we show here how to use the BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io) Webservices to perform exemplary map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)pings.

We start by defining string(URL_TO_INSERT_RECORD https://string-db.org/)s containing the URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630) of the webservices and the specific method from the Webservices we want to use. In our case, a `batch cross reference`. When doing the query, we need to specify **the organism** and **the source dataset**. We can also *optionally* specify a *target data source* if we only want to map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map) to a specific data source, e.g. Ensembl(URL_TO_INSERT_RECORD http://www.ensembl.org/)(URL_TO_INSERT_RECORD http://www.ensembl.org/).

```python
url = "https://webservice.bridgedb.org/"
batch_request = url+"{org}/xrefsBatch/{source}{}"
```

If the aim is to map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map) only to a specific target data source, then one can check whether the map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping is supported by invoking the following webservice call:  

```python
mapping_available = "{org}/isMappingSupported/{source}/{target}"
query = url+mapping_available.format(org='Homo sapiens', source='H', target='En')
requests.get(query).text
```

This will return `True` if the map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping between the given source and target is supported for the given organism or `False` otherwise.

We then load our data into a pandas dataframe and call the requests library using our query.

```python
query = batch_request.format('?dataSource=En', org='Homo sapiens', source='H')
response = requests.post(query, data=data.to_csv(index=False, header=False))
```

The webservice response is now stored in the `response` variable. We can then simply pass this variable to the `to_df` method provided in the `bridgedb(URL_TO_INSERT_RECORD https://bridgedb.github.io)_script.py` module (see [Code](#Code)). This method will extract the response in text form and turn it into a pandas Dataframe with conveniently named columns and structured data.

The output table will contain the:
* Original identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)
* Data source that the identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) is part of
* Map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ped(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)
* Data source for the map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ped(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)

In our case the output of `to_df` is:

| original   | source   | map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping         | target   |
|:-----------|:---------|:----------------|:---------|
| A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | ENSG00000121410 | En       |
| A1CF       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | ENSG00000148584 | En       |
| A2MP(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/mp_ontology)1      | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | ENSG00000256069 | En       |

If we were to not specify the target data source (by passing an empty string(URL_TO_INSERT_RECORD https://string-db.org/) as the parameter), we would get all the potential map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)pings for the given identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s. In our case (top 10 rows):

| original   | source   | map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping      | target   |
|:-----------|:---------|:-------------|:---------|
| A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | uc002qsd.5   | Uc       |
| A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | 8039748      | X        |
| A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | GO(URL_TO_INSERT_RECORD http://www.geneontology.org):0072562   | T        |
| A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | uc061drj.1   | Uc       |
| A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | ILMN_2055271 | Il       |
| A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | Hs.529161    | U        |
| A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | GO(URL_TO_INSERT_RECORD http://www.geneontology.org):0070062   | T        |
| A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | GO(URL_TO_INSERT_RECORD http://www.geneontology.org):0002576   | T        |
| A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | uc061drt.1   | Uc       |
| A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | 51020_at     | X        |

As one can see, using the BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io) webservice via Python is extremely simple and can be easily integrated in an annotation pipeline.


#### BridgeDb via the dedicated R package

```{note} 
For this tutorial R v4.0.3, [tidyverse](https://www.tidyverse.org/) v1.3.0, and [BridgeDbR](https://www.bioconductor.org/packages/release/bioc/html/BridgeDbR.html) v2.0.0 were used.
```

After having loaded the required R libraries, we read the data and create a new column to include the source of the identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema).

```r
data_df <- read_tsv(filepath, col_names=c('identifier'))
data_df$source = 'H'
``` 

We then load the data for the organism we are map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping from.

```r
 location <- getDatabase('Homo sapiens')
 mapper <- loadDatabase(location)
```

And use the library's     dedicated function to map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map) the identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s:

```r
mapping = maps(mapper, data_df, target='En')
```
This will return:
| identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) | source | target | map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping         |
|:---------- |:------ |:------ |:--------------- |
| A1BG       | H      | En     | ENSG00000121410 |
| A1CF       | H      | En     | ENSG00000148584 |
| A2MP(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/mp_ontology)1      | H      | En     | ENSG00000256069 |

As seen earlier when using Python language, we can obtain all possible map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)pings simply by not specifying the target. This will result in (top 10) 
| identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) | source | target | map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping      |
|:---------- |:------ |:------ |:------------ |
| A1BG       | H      | Uc     | uc002qsd.5   |
| A1BG       | H      | X      | 8039748      |
| A1BG       | H      | T      | GO(URL_TO_INSERT_RECORD http://www.geneontology.org):0072562   |
| A1BG       | H      | Uc     | uc061drj.1   |
| A1BG       | H      | Il     | ILMN_2055271 |
| A1BG       | H      | U      | Hs.529161    |
| A1BG       | H      | T      | GO(URL_TO_INSERT_RECORD http://www.geneontology.org):0070062   |
| A1BG       | H      | T      | GO(URL_TO_INSERT_RECORD http://www.geneontology.org):0002576   |
| A1BG       | H      | Uc     | uc061drt.1   |
| A1BG       | H      | X      | 51020_at     |

```{warning} 
An error message indicating "Error in download.file" may be thrown. This may be caused by the `timeout` variable being set to too small a value. To remediate the issue, try increasing the timeout variable value by calling `options(timeout=300)`.
```

<!--
This will maybe link to the identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping recipe in the future, where there will be a specific section detailing identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) equivalence files taking into account scientific lenses, as discussed with Egon. 

--------------------------------


### Mapping a local identifier to global identifier
[NEE(URL_TO_INSERT_RECORD https://earthexplorer.usgs.gov/)D HELP HERE]
This is a step that should be done manually. In this case an important decision should be made, which identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s to map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map) to. To decide this you should look for the data source that contains the closest definition of the concepts to the one you used for your local identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s.

-->

### Mapping local identifier to a different global identifier

```{note} 
 In this section, we assume that we already have an equivalence file containing the mapping of a local identifier to one of the global identifiers. In our case, this will be contained in a TSV where we map our local gene identifier to [HGNC](http://www.genenames.org). One may consult the list of other potential data formats in the {ref}`fcb-identifier-mapping` recipe. The mapping should be **one-to-one** for this recipe. 
```

The TSV(URL_TO_INSERT_RECORD http://www.iana.org/assignments/media-types/text/tab-separated-values) map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping file looks as follows:
| local   | source   |
|:--------|:---------|
| aa11    | A1BG     |
| bb34    | A1CF     |
| eg93    | A2MP(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/mp_ontology)1    |

You may notice the `source` identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s correspond with those used in the previous example.


This is how the map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping will work

````{dropdown} 
:open:
```{figure} bridgedb-recipe.md-figure1.mmd.png
---
name: bridgedb(URL_TO_INSERT_RECORD https://bridgedb.github.io)-recipe-figure1
alt: Overview of BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io) tools
---
Overview of BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io) tools
```
````

#### Webservices in Python

As before, we will define variables including the `web-service's URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)` and the `method` that we will use, in this instance: `xRefsBatch`.
We then pass the source column to the `post request` as follows

```python
source_data = case2.source.to_csv(index=False, header=False)
query = batch_request.format('', org=org, source=source)
response2 = requests.post(query, data = source_data)
```
You may notice here that we did not pass a target source, this could be done as specified before. Then, we use `to_df` again and as expected obtain the same dataframe as before.
To see the equivalences with our local identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s, we can simply join the dataframes, as follows:

```python
local_mapping = mappings.join(case2.set_index('source'), on='original')
```
which will return the following table (first 10 rows)
| original   | source   | map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping      | target   | local   |
|:-----------|:---------|:-------------|:---------|:--------|
| A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | uc002qsd.5   | Uc       | aa11    |
| A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | 8039748      | X        | aa11    |
| A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | GO(URL_TO_INSERT_RECORD http://www.geneontology.org):0072562   | T        | aa11    |
| A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | uc061drj.1   | Uc       | aa11    |
| A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | ILMN_2055271 | Il       | aa11    |
| A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | Hs.529161    | U        | aa11    |
| A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | GO(URL_TO_INSERT_RECORD http://www.geneontology.org):0070062   | T        | aa11    |
| A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | GO(URL_TO_INSERT_RECORD http://www.geneontology.org):0002576   | T        | aa11    |
| A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | uc061drt.1   | Uc       | aa11    |
| A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | 51020_at     | X        | aa11    |

In case we did specify the `target` argument to be `Ensembl(URL_TO_INSERT_RECORD http://www.ensembl.org/)(URL_TO_INSERT_RECORD http://www.ensembl.org/) (En)`, we would instead get

| original   | source   | map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping         | target   | local   |
|:-----------|:---------|:----------------|:---------|:--------|
| A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | ENSG00000121410 | En       | aa11    |
| A1CF       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | ENSG00000148584 | En       | bb34    |
| A2MP(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/mp_ontology)1      | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)     | ENSG00000256069 | En       | eg93    |

Here, we see a `one-to-one` relation between the identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s in HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/) and En while the relation between HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/) and UCSC Genome Browser (Uc) or Gene Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD http://www.geneontology.org) (T) is `one-to-many`. Depending on the identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s and resources, the relation could also be `many-to-many` as shown below.


````{dropdown} 
:open:
```{figure} bridgedb-recipe.md-figure2.mmd.png
---
name: bridgedb(URL_TO_INSERT_RECORD https://bridgedb.github.io)-recipe-figure2
alt: An example of a map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping via BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io).
---
An example of a map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping via BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io). You may notice that despite the 1-to-1 relation between `local` and `original` we get a N-to-N relation between `local` and `map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping` due to the N-to-N relation between `original` and `map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping`.
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
Then, after computing the map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping, we can join it with the local identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)

```r
right_join(data_df, mapping)
```
Assuming we did not specify the target data source we obtain the following table (first 10 rows):
| local | identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) | source | target | map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping      |
|:----- |:--------   |:------ |:------ |:------------ |
| aa11  | A1BG       | H      | Uc     | uc002qsd.5   |
| aa11  | A1BG       | H      | X      | 8039748      |
| aa11  | A1BG       | H      | T      | GO(URL_TO_INSERT_RECORD http://www.geneontology.org):0072562   |
| aa11  | A1BG       | H      | Uc     | uc061drj.1   |
| aa11  | A1BG       | H      | Il     | ILMN_2055271 |
| aa11  | A1BG       | H      | U      | Hs.529161    |
| aa11  | A1BG       | H      | T      | GO(URL_TO_INSERT_RECORD http://www.geneontology.org):0070062   |
| aa11  | A1BG       | H      | T      | GO(URL_TO_INSERT_RECORD http://www.geneontology.org):0002576   |
| aa11  | A1BG       | H      | Uc     | uc061drt.1   |
| aa11  | A1BG       | H      | X      | 51020_at     |

In case we did specify the target data source we would get:

| local | identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) | source | target | map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping         |
|:----- |:---------- |:------ |:------ |:--------------- |
| aa11  | A1BG       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)   | En     | ENSG00000121410 |
| bb34  | A1CF       | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)   | En     | ENSG00000148584 |
| eg93  | A2MP(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/mp_ontology)1      | HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/)   | En     | ENSG00000256069 |

---
## Provenance

BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io) provides provenance informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion through:
* A call to `/properties/` method of the Webservice
* `getProperties()` in BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io)R (passing the map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)per as a parameter)

This returns the following informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion for each of the data sources for a given organism:
* Data source name
* Build date
* Series
* Data type
* Data source version
* Schema version

Improvements on provenance are under way (see [here](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/bridgedb/BridgeDb/issues/164)).

---

## Code 
You can find ready-made methods to map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map) using R and Python for the given use cases [here](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/FAIRplus/the-fair-cookbook/tree/9ad9481be32812b2565f9f9f1897642ae26eddff/content/recipes/interoperability/bridgedb/data). These assume the data has the structure described in this recipe.

---

## Conclusion

We showed how to use BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io)'s webservices and R package to map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map) identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s from different data sources using a minimal dataset. 
BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io) provides handy functionality to make 'omics' data more interoperable and reusable.
As with all annotation services, it is important to bear in mind the version of the service being used as well as the data on which the service invokation has been performed.
These are aspects of informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion provenance which we plan to provide in the future.
 
### What to read next?

* {ref}`fcb-find-identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s`
* {ref}`fcb-identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)-map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping`

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
