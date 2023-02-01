(fcb-bridgedb (URL_TO_INSERT_RECORD_5692 https://fairsharing.org/FAIRsharing.5ry74y) -recipe)=
# Identifier mapping with BridgeDb


<!--
TO (URL_TO_INSERT_RECORD_5693 https://fairsharing.org/FAIRsharing.w69t6r) DO : the recipe does not reference its figures
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

> Provide practical examples on how to **map (URL_TO_INSERT_RECORD_5698 https://fairsharing.org/FAIRsharing.53edcc)  identifier (URL_TO_INSERT_TERM_5694 https://fairsharing.org/search?recordType=identifier_schema) s for Genes, Protein (URL_TO_INSERT_RECORD_5695 https://fairsharing.org/FAIRsharing.rtndct) s, Metabolites and Pathways** between resources using a purpose built tool, namely [BridgeDb (URL_TO_INSERT_RECORD_5696 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5697 https://fairsharing.org/FAIRsharing.5ry74y) ](https://bio.tools (URL_TO_INSERT_RECORD_5699 https://fairsharing.org/FAIRsharing.63520c) /bridgedb).
> Hands on guidance is provided for 2 interfaces (R package and a Python Webservices) provided by [BridgeDb (URL_TO_INSERT_RECORD_5700 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5701 https://fairsharing.org/FAIRsharing.5ry74y) ](https://bio.tools (URL_TO_INSERT_RECORD_5702 https://fairsharing.org/FAIRsharing.63520c) /bridgedb).


---


## Graphical Overview

This recipe will cover the highlighted topics

````{dropdown} 
:open:
```{figure} identifier-mapping.md-figure1.mmd.png
---
width: 1000px
name: bridgedb (URL_TO_INSERT_RECORD_5703 https://fairsharing.org/FAIRsharing.5ry74y) -recipe-figure0
alt: Overview of key aspects in Identifier (URL_TO_INSERT_TERM_5704 https://fairsharing.org/search?recordType=identifier_schema)  Map (URL_TO_INSERT_RECORD_5705 https://fairsharing.org/FAIRsharing.53edcc) ping
---
Overview of key aspects in Identifier (URL_TO_INSERT_TERM_5706 https://fairsharing.org/search?recordType=identifier_schema)  Map (URL_TO_INSERT_RECORD_5707 https://fairsharing.org/FAIRsharing.53edcc) ping
```
````

---


## Requirements

This recipe has the following requirements:

* Recipe dependency:
    <!-- TO (URL_TO_INSERT_RECORD_5709 https://fairsharing.org/FAIRsharing.w69t6r) DO (recipe not existent yet ) * {ref}`fcb-identifier (URL_TO_INSERT_TERM_5708 https://fairsharing.org/search?recordType=identifier_schema) s` -->
    * {ref}`fcb-identifier (URL_TO_INSERT_TERM_5710 https://fairsharing.org/search?recordType=identifier_schema) -map (URL_TO_INSERT_RECORD_5711 https://fairsharing.org/FAIRsharing.53edcc) ping`

* Skill dependency:
    * Programming knowledge
    * R
    * Python

* Technical dependency
    * R or Python environment
    * BridgeDb (URL_TO_INSERT_RECORD_5712 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5713 https://fairsharing.org/FAIRsharing.5ry74y)  R package installed
---

## Tools

The table below lists the software that is used to execute the examples in this recipe.

| Software                                            | Description                                                                                                                                                                               | version | Biotools record                                          |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------------------------------------------- 
| [BridgeDb (URL_TO_INSERT_RECORD_5719 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5721 https://fairsharing.org/FAIRsharing.5ry74y)  webservices](https://bridgedb.github.io (URL_TO_INSERT_RECORD_5723 https://fairsharing.org/FAIRsharing.5ry74y) /) | BridgeDb (URL_TO_INSERT_RECORD_5720 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5722 https://fairsharing.org/FAIRsharing.5ry74y)  is a framework to map (URL_TO_INSERT_RECORD_5724 https://fairsharing.org/FAIRsharing.53edcc)  identifier (URL_TO_INSERT_TERM_5716 https://fairsharing.org/search?recordType=identifier_schema) s between various database (URL_TO_INSERT_TERM_5714 https://fairsharing.org/search?fairsharingRegistry=Database) s. It includes a Java library that provides an API to work with identifier (URL_TO_INSERT_TERM_5717 https://fairsharing.org/search?recordType=identifier_schema) -identifier (URL_TO_INSERT_TERM_5718 https://fairsharing.org/search?recordType=identifier_schema)  map (URL_TO_INSERT_RECORD_5725 https://fairsharing.org/FAIRsharing.53edcc) ping database (URL_TO_INSERT_TERM_5715 https://fairsharing.org/search?fairsharingRegistry=Database) s and resources. | 0.0.9   | [https://bio.tools (URL_TO_INSERT_RECORD_5726 https://fairsharing.org/FAIRsharing.63520c) /bridgedb](https://bio.tools (URL_TO_INSERT_RECORD_5727 https://fairsharing.org/FAIRsharing.63520c) /bridgedb) |
| Python                                              | An interpreted, high-level and general-purpose programming language.                                                                                                                       | 3.8.5   |                                                          |
| [pandas](https://pandas.pydata.org/)                | pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.                                     | 1.1.3   |                                                          |
| R                                                   | R is a programming language and free software environment for statistical computing and graphics supported by the R Foundation for Statistical Computing.                                 | v4.0.3  | https://bio.tools (URL_TO_INSERT_RECORD_5728 https://fairsharing.org/FAIRsharing.63520c) /r                                      |
| [tidyverse](https://www.tidyverse.org/)                                           | tidyverse is an opinionated collection (URL_TO_INSERT_TERM_5729 https://fairsharing.org/search?recordType=collection)  of R packages designed for data science.  | 1.3.0||
|[BridgeDbR](https://doi.org/doi:10.18129/B9.bioc.BridgeDbR)|An R package for BridgeDb (URL_TO_INSERT_RECORD_5730 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5731 https://fairsharing.org/FAIRsharing.5ry74y) | 2.0.0||

---

## Identifier mapping with BridgeDb

{ref}`Interlinking data from different sources <fcb-identifier (URL_TO_INSERT_TERM_5732 https://fairsharing.org/search?recordType=identifier_schema) -map (URL_TO_INSERT_RECORD_5734 https://fairsharing.org/FAIRsharing.53edcc) ping>` is an essential step for data reusability and interoperability. This step requires dedicated tools. With the present recipe, we show how to use [BridgeDb](https://bridgedb.github.io (URL_TO_INSERT_RECORD_5733 https://fairsharing.org/FAIRsharing.5ry74y) /) to carry out this process.

[BridgeDb](https://bridgedb.github.io (URL_TO_INSERT_RECORD_5739 https://fairsharing.org/FAIRsharing.5ry74y) /) is an open source tool dedicated to performing identifier (URL_TO_INSERT_TERM_5735 https://fairsharing.org/search?recordType=identifier_schema)  map (URL_TO_INSERT_RECORD_5740 https://fairsharing.org/FAIRsharing.53edcc) ping {footcite}`van_iersel_bridgedb (URL_TO_INSERT_RECORD_5736 https://fairsharing.org/FAIRsharing.5ry74y) _2010`. BridgeDb (URL_TO_INSERT_RECORD_5737 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5738 https://fairsharing.org/FAIRsharing.5ry74y)  offers three different interfaces:
* Java API
* R package
* REST Web-services


> 📖 In the context of this recipe, we disting (URL_TO_INSERT_RECORD_5742 https://fairsharing.org/FAIRsharing.q7bkqr) uish between two types of identifier (URL_TO_INSERT_TERM_5741 https://fairsharing.org/search?recordType=identifier_schema) s:
>* *Local identifier (URL_TO_INSERT_TERM_5744 https://fairsharing.org/search?recordType=identifier_schema) s* which refer to identifier (URL_TO_INSERT_TERM_5745 https://fairsharing.org/search?recordType=identifier_schema) s that are minted within an organization or database (URL_TO_INSERT_TERM_5743 https://fairsharing.org/search?fairsharingRegistry=Database)  and thus internally defined (i.e. local to said organization). 
>* *Global identifier (URL_TO_INSERT_TERM_5746 https://fairsharing.org/search?recordType=identifier_schema) s* which refer to identifier (URL_TO_INSERT_TERM_5747 https://fairsharing.org/search?recordType=identifier_schema) s that are globally unique and uniquely point to an entity, as available from BridgeDb (URL_TO_INSERT_RECORD_5748 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5749 https://fairsharing.org/FAIRsharing.5ry74y) 's [data sources file](https://github.com (URL_TO_INSERT_RECORD_5750 https://fairsharing.org/FAIRsharing.c55d5e) /bridgedb/datasources)

We will focus here on two distinct cases, depending on the nature of the incoming data. Namely, whether our data is already using global identifier (URL_TO_INSERT_TERM_5751 https://fairsharing.org/search?recordType=identifier_schema) s or only relies on local identifier (URL_TO_INSERT_TERM_5752 https://fairsharing.org/search?recordType=identifier_schema) s. 

In this recipe, we will cover how BridgeDb (URL_TO_INSERT_RECORD_5754 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5755 https://fairsharing.org/FAIRsharing.5ry74y) 's R package and webservices can be used to map (URL_TO_INSERT_RECORD_5756 https://fairsharing.org/FAIRsharing.53edcc)  between resource identifier (URL_TO_INSERT_TERM_5753 https://fairsharing.org/search?recordType=identifier_schema) s.

### Mapping a global identifier to other global identifiers
In this case, the input data is a list of elements with an identifier (URL_TO_INSERT_TERM_5757 https://fairsharing.org/search?recordType=identifier_schema)  that is part of [BridgeDb (URL_TO_INSERT_RECORD_5761 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5762 https://fairsharing.org/FAIRsharing.5ry74y) 's data sources](https://github.com (URL_TO_INSERT_RECORD_5765 https://fairsharing.org/FAIRsharing.c55d5e) /bridgedb/datasources). In our example, we will use a list of Homo Sapien Hugo Gene Nomenclature Convention ([HGNC](http://www.genenames.org (URL_TO_INSERT_RECORD_5763 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5766 https://fairsharing.org/FAIRsharing.29we0s) )) gene identifier (URL_TO_INSERT_TERM_5758 https://fairsharing.org/search?recordType=identifier_schema) s stored in a TSV (URL_TO_INSERT_RECORD_5760 https://fairsharing.org/FAIRsharing.a978c9)  file. The objective is to map (URL_TO_INSERT_RECORD_5764 https://fairsharing.org/FAIRsharing.53edcc)  these to other available gene identifier (URL_TO_INSERT_TERM_5759 https://fairsharing.org/search?recordType=identifier_schema) s.

#### BridgeDb via Webservices using Python
> ❗ For this tutorial Python v3.8.5, [pandas](https://pandas.pydata.org/) v1.1.3, and BridgeDb (URL_TO_INSERT_RECORD_5767 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5768 https://fairsharing.org/FAIRsharing.5ry74y)  Webservices v0.9.0 were used.

One of the biggest benefits of using BridgeDb (URL_TO_INSERT_RECORD_5770 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5773 https://fairsharing.org/FAIRsharing.5ry74y)  webservices is that these can be accessed using most programming languages. Python has become one of the leading programming languages in data science and predictive model (URL_TO_INSERT_TERM_5769 https://fairsharing.org/search?recordType=model_and_format) ling. Despite the lack of a dedicated BridgeDb (URL_TO_INSERT_RECORD_5771 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5774 https://fairsharing.org/FAIRsharing.5ry74y)  Python library, we show here how to use the BridgeDb (URL_TO_INSERT_RECORD_5772 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5775 https://fairsharing.org/FAIRsharing.5ry74y)  Webservices to perform exemplary map (URL_TO_INSERT_RECORD_5776 https://fairsharing.org/FAIRsharing.53edcc) pings.

We start by defining string (URL_TO_INSERT_RECORD_5781 https://fairsharing.org/FAIRsharing.9b7wvk) s containing the URL (URL_TO_INSERT_RECORD_5779 https://fairsharing.org/FAIRsharing.9d38e2)  of the webservices and the specific method from the Webservices we want to use. In our case, a `batch cross reference`. When doing the query, we need to specify **the organism** and **the source dataset**. We can also *optionally* specify a *target data source* if we only want to map (URL_TO_INSERT_RECORD_5780 https://fairsharing.org/FAIRsharing.53edcc)  to a specific data source, e.g. Ensembl (URL_TO_INSERT_RECORD_5777 https://fairsharing.org/FAIRsharing.fx0mw7)  (URL_TO_INSERT_RECORD_5778 https://fairsharing.org/FAIRsharing.fx0mw7) .

```python
url = "https://webservice.bridgedb.org/"
batch_request = url+"{org}/xrefsBatch/{source}{}"
```

If the aim is to map (URL_TO_INSERT_RECORD_5782 https://fairsharing.org/FAIRsharing.53edcc)  only to a specific target data source, then one can check whether the map (URL_TO_INSERT_RECORD_5783 https://fairsharing.org/FAIRsharing.53edcc) ping is supported by invoking the following webservice call:  

```python
mapping_available = "{org}/isMappingSupported/{source}/{target}"
query = url+mapping_available.format(org='Homo sapiens', source='H', target='En')
requests.get(query).text
```

This will return `True` if the map (URL_TO_INSERT_RECORD_5784 https://fairsharing.org/FAIRsharing.53edcc) ping between the given source and target is supported for the given organism or `False` otherwise.

We then load our data into a pandas dataframe and call the requests library using our query.

```python
query = batch_request.format('?dataSource=En', org='Homo sapiens', source='H')
response = requests.post(query, data=data.to_csv(index=False, header=False))
```

The webservice response is now stored in the `response` variable. We can then simply pass this variable to the `to_df` method provided in the `bridgedb (URL_TO_INSERT_RECORD_5785 https://fairsharing.org/FAIRsharing.5ry74y) _script.py` module (see [Code](#Code)). This method will extract the response in text form and turn it into a pandas Dataframe with conveniently named columns and structured data.

The output table will contain the:
* Original identifier (URL_TO_INSERT_TERM_5786 https://fairsharing.org/search?recordType=identifier_schema) 
* Data source that the identifier (URL_TO_INSERT_TERM_5787 https://fairsharing.org/search?recordType=identifier_schema)  is part of
* Map (URL_TO_INSERT_RECORD_5789 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_5790 https://fairsharing.org/FAIRsharing.31385c)  identifier (URL_TO_INSERT_TERM_5788 https://fairsharing.org/search?recordType=identifier_schema) 
* Data source for the map (URL_TO_INSERT_RECORD_5792 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_5793 https://fairsharing.org/FAIRsharing.31385c)  identifier (URL_TO_INSERT_TERM_5791 https://fairsharing.org/search?recordType=identifier_schema) 

In our case the output of `to_df` is:

| original   | source   | map (URL_TO_INSERT_RECORD_5794 https://fairsharing.org/FAIRsharing.53edcc) ping         | target   |
|:-----------|:---------|:----------------|:---------|
| A1BG       | HGNC (URL_TO_INSERT_RECORD_5795 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5796 https://fairsharing.org/FAIRsharing.29we0s)      | ENSG00000121410 | En       |
| A1CF       | HGNC (URL_TO_INSERT_RECORD_5797 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5798 https://fairsharing.org/FAIRsharing.29we0s)      | ENSG00000148584 | En       |
| A2MP (URL_TO_INSERT_RECORD_5799 https://fairsharing.org/FAIRsharing.kg1x4z) 1      | HGNC (URL_TO_INSERT_RECORD_5800 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5801 https://fairsharing.org/FAIRsharing.29we0s)      | ENSG00000256069 | En       |

If we were to not specify the target data source (by passing an empty string (URL_TO_INSERT_RECORD_5804 https://fairsharing.org/FAIRsharing.9b7wvk)  as the parameter), we would get all the potential map (URL_TO_INSERT_RECORD_5803 https://fairsharing.org/FAIRsharing.53edcc) pings for the given identifier (URL_TO_INSERT_TERM_5802 https://fairsharing.org/search?recordType=identifier_schema) s. In our case (top 10 rows):

| original   | source   | map (URL_TO_INSERT_RECORD_5805 https://fairsharing.org/FAIRsharing.53edcc) ping      | target   |
|:-----------|:---------|:-------------|:---------|
| A1BG       | HGNC (URL_TO_INSERT_RECORD_5806 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5807 https://fairsharing.org/FAIRsharing.29we0s)      | uc002qsd.5   | Uc       |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_5808 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5809 https://fairsharing.org/FAIRsharing.29we0s)      | 8039748      | X        |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_5811 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5812 https://fairsharing.org/FAIRsharing.29we0s)      | GO (URL_TO_INSERT_RECORD_5810 https://fairsharing.org/FAIRsharing.6xq0ee) :0072562   | T        |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_5813 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5814 https://fairsharing.org/FAIRsharing.29we0s)      | uc061drj.1   | Uc       |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_5815 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5816 https://fairsharing.org/FAIRsharing.29we0s)      | ILMN_2055271 | Il       |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_5817 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5818 https://fairsharing.org/FAIRsharing.29we0s)      | Hs.529161    | U        |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_5820 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5821 https://fairsharing.org/FAIRsharing.29we0s)      | GO (URL_TO_INSERT_RECORD_5819 https://fairsharing.org/FAIRsharing.6xq0ee) :0070062   | T        |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_5823 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5824 https://fairsharing.org/FAIRsharing.29we0s)      | GO (URL_TO_INSERT_RECORD_5822 https://fairsharing.org/FAIRsharing.6xq0ee) :0002576   | T        |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_5825 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5826 https://fairsharing.org/FAIRsharing.29we0s)      | uc061drt.1   | Uc       |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_5827 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5828 https://fairsharing.org/FAIRsharing.29we0s)      | 51020_at     | X        |

As one can see, using the BridgeDb (URL_TO_INSERT_RECORD_5829 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5830 https://fairsharing.org/FAIRsharing.5ry74y)  webservice via Python is extremely simple and can be easily integrated in an annotation pipeline.


#### BridgeDb via the dedicated R package

```{note} 
For this tutorial R v4.0.3, [tidyverse](https://www.tidyverse.org/) v1.3.0, and [BridgeDbR](https://www.bioconductor.org/packages/release/bioc/html/BridgeDbR.html) v2.0.0 were used.
```

After having loaded the required R libraries, we read the data and create a new column to include the source of the identifier (URL_TO_INSERT_TERM_5831 https://fairsharing.org/search?recordType=identifier_schema) .

```r
data_df <- read_tsv(filepath, col_names=c('identifier'))
data_df$source = 'H'
``` 

We then load the data for the organism we are map (URL_TO_INSERT_RECORD_5832 https://fairsharing.org/FAIRsharing.53edcc) ping from.

```r
 location <- getDatabase('Homo sapiens')
 mapper <- loadDatabase(location)
```

And use the library's     dedicated function to map (URL_TO_INSERT_RECORD_5834 https://fairsharing.org/FAIRsharing.53edcc)  the identifier (URL_TO_INSERT_TERM_5833 https://fairsharing.org/search?recordType=identifier_schema) s:

```r
mapping = maps(mapper, data_df, target='En')
```
This will return:
| identifier (URL_TO_INSERT_TERM_5835 https://fairsharing.org/search?recordType=identifier_schema)  | source | target | map (URL_TO_INSERT_RECORD_5836 https://fairsharing.org/FAIRsharing.53edcc) ping         |
|:---------- |:------ |:------ |:--------------- |
| A1BG       | H      | En     | ENSG00000121410 |
| A1CF       | H      | En     | ENSG00000148584 |
| A2MP (URL_TO_INSERT_RECORD_5837 https://fairsharing.org/FAIRsharing.kg1x4z) 1      | H      | En     | ENSG00000256069 |

As seen earlier when using Python language, we can obtain all possible map (URL_TO_INSERT_RECORD_5838 https://fairsharing.org/FAIRsharing.53edcc) pings simply by not specifying the target. This will result in (top 10) 
| identifier (URL_TO_INSERT_TERM_5839 https://fairsharing.org/search?recordType=identifier_schema)  | source | target | map (URL_TO_INSERT_RECORD_5840 https://fairsharing.org/FAIRsharing.53edcc) ping      |
|:---------- |:------ |:------ |:------------ |
| A1BG       | H      | Uc     | uc002qsd.5   |
| A1BG       | H      | X      | 8039748      |
| A1BG       | H      | T      | GO (URL_TO_INSERT_RECORD_5841 https://fairsharing.org/FAIRsharing.6xq0ee) :0072562   |
| A1BG       | H      | Uc     | uc061drj.1   |
| A1BG       | H      | Il     | ILMN_2055271 |
| A1BG       | H      | U      | Hs.529161    |
| A1BG       | H      | T      | GO (URL_TO_INSERT_RECORD_5842 https://fairsharing.org/FAIRsharing.6xq0ee) :0070062   |
| A1BG       | H      | T      | GO (URL_TO_INSERT_RECORD_5843 https://fairsharing.org/FAIRsharing.6xq0ee) :0002576   |
| A1BG       | H      | Uc     | uc061drt.1   |
| A1BG       | H      | X      | 51020_at     |

```{warning} 
An error message indicating "Error in download.file" may be thrown. This may be caused by the `timeout` variable being set to too small a value. To remediate the issue, try increasing the timeout variable value by calling `options(timeout=300)`.
```

<!--
This will maybe link to the identifier (URL_TO_INSERT_TERM_5844 https://fairsharing.org/search?recordType=identifier_schema)  map (URL_TO_INSERT_RECORD_5846 https://fairsharing.org/FAIRsharing.53edcc) ping recipe in the future, where there will be a specific section detailing identifier (URL_TO_INSERT_TERM_5845 https://fairsharing.org/search?recordType=identifier_schema)  equivalence files taking into account scientific lenses, as discussed with Egon. 

--------------------------------


### Mapping a local identifier to global identifier
[NEE (URL_TO_INSERT_RECORD_5847 https://fairsharing.org/FAIRsharing.0b711a) D HELP HERE]
This is a step that should be done manually. In this case an important decision should be made, which identifier (URL_TO_INSERT_TERM_5848 https://fairsharing.org/search?recordType=identifier_schema) s to map (URL_TO_INSERT_RECORD_5850 https://fairsharing.org/FAIRsharing.53edcc)  to. To decide this you should look for the data source that contains the closest definition of the concepts to the one you used for your local identifier (URL_TO_INSERT_TERM_5849 https://fairsharing.org/search?recordType=identifier_schema) s.

-->

### Mapping local identifier to a different global identifier

```{note} 
 In this section, we assume that we already have an equivalence file containing the mapping of a local identifier to one of the global identifiers. In our case, this will be contained in a TSV where we map our local gene identifier to [HGNC](http://www.genenames.org). One may consult the list of other potential data formats in the {ref}`fcb-identifier-mapping` recipe. The mapping should be **one-to-one** for this recipe. 
```

The TSV (URL_TO_INSERT_RECORD_5851 https://fairsharing.org/FAIRsharing.a978c9)  map (URL_TO_INSERT_RECORD_5852 https://fairsharing.org/FAIRsharing.53edcc) ping file looks as follows:
| local   | source   |
|:--------|:---------|
| aa11    | A1BG     |
| bb34    | A1CF     |
| eg93    | A2MP (URL_TO_INSERT_RECORD_5853 https://fairsharing.org/FAIRsharing.kg1x4z) 1    |

You may notice the `source` identifier (URL_TO_INSERT_TERM_5854 https://fairsharing.org/search?recordType=identifier_schema) s correspond with those used in the previous example.


This is how the map (URL_TO_INSERT_RECORD_5855 https://fairsharing.org/FAIRsharing.53edcc) ping will work

````{dropdown} 
:open:
```{figure} bridgedb-recipe.md-figure1.mmd.png
---
name: bridgedb (URL_TO_INSERT_RECORD_5856 https://fairsharing.org/FAIRsharing.5ry74y) -recipe-figure1
alt: Overview of BridgeDb (URL_TO_INSERT_RECORD_5857 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5858 https://fairsharing.org/FAIRsharing.5ry74y)  tools
---
Overview of BridgeDb (URL_TO_INSERT_RECORD_5859 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5860 https://fairsharing.org/FAIRsharing.5ry74y)  tools
```
````

#### Webservices in Python

As before, we will define variables including the `web-service's URL (URL_TO_INSERT_RECORD_5861 https://fairsharing.org/FAIRsharing.9d38e2) ` and the `method` that we will use, in this instance: `xRefsBatch`.
We then pass the source column to the `post request` as follows

```python
source_data = case2.source.to_csv(index=False, header=False)
query = batch_request.format('', org=org, source=source)
response2 = requests.post(query, data = source_data)
```
You may notice here that we did not pass a target source, this could be done as specified before. Then, we use `to_df` again and as expected obtain the same dataframe as before.
To see the equivalences with our local identifier (URL_TO_INSERT_TERM_5862 https://fairsharing.org/search?recordType=identifier_schema) s, we can simply join the dataframes, as follows:

```python
local_mapping = mappings.join(case2.set_index('source'), on='original')
```
which will return the following table (first 10 rows)
| original   | source   | map (URL_TO_INSERT_RECORD_5863 https://fairsharing.org/FAIRsharing.53edcc) ping      | target   | local   |
|:-----------|:---------|:-------------|:---------|:--------|
| A1BG       | HGNC (URL_TO_INSERT_RECORD_5864 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5865 https://fairsharing.org/FAIRsharing.29we0s)      | uc002qsd.5   | Uc       | aa11    |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_5866 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5867 https://fairsharing.org/FAIRsharing.29we0s)      | 8039748      | X        | aa11    |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_5869 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5870 https://fairsharing.org/FAIRsharing.29we0s)      | GO (URL_TO_INSERT_RECORD_5868 https://fairsharing.org/FAIRsharing.6xq0ee) :0072562   | T        | aa11    |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_5871 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5872 https://fairsharing.org/FAIRsharing.29we0s)      | uc061drj.1   | Uc       | aa11    |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_5873 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5874 https://fairsharing.org/FAIRsharing.29we0s)      | ILMN_2055271 | Il       | aa11    |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_5875 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5876 https://fairsharing.org/FAIRsharing.29we0s)      | Hs.529161    | U        | aa11    |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_5878 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5879 https://fairsharing.org/FAIRsharing.29we0s)      | GO (URL_TO_INSERT_RECORD_5877 https://fairsharing.org/FAIRsharing.6xq0ee) :0070062   | T        | aa11    |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_5881 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5882 https://fairsharing.org/FAIRsharing.29we0s)      | GO (URL_TO_INSERT_RECORD_5880 https://fairsharing.org/FAIRsharing.6xq0ee) :0002576   | T        | aa11    |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_5883 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5884 https://fairsharing.org/FAIRsharing.29we0s)      | uc061drt.1   | Uc       | aa11    |
| A1BG       | HGNC (URL_TO_INSERT_RECORD_5885 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5886 https://fairsharing.org/FAIRsharing.29we0s)      | 51020_at     | X        | aa11    |

In case we did specify the `target` argument to be `Ensembl (URL_TO_INSERT_RECORD_5887 https://fairsharing.org/FAIRsharing.fx0mw7)  (URL_TO_INSERT_RECORD_5888 https://fairsharing.org/FAIRsharing.fx0mw7)  (En)`, we would instead get

| original   | source   | map (URL_TO_INSERT_RECORD_5889 https://fairsharing.org/FAIRsharing.53edcc) ping         | target   | local   |
|:-----------|:---------|:----------------|:---------|:--------|
| A1BG       | HGNC (URL_TO_INSERT_RECORD_5890 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5891 https://fairsharing.org/FAIRsharing.29we0s)      | ENSG00000121410 | En       | aa11    |
| A1CF       | HGNC (URL_TO_INSERT_RECORD_5892 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5893 https://fairsharing.org/FAIRsharing.29we0s)      | ENSG00000148584 | En       | bb34    |
| A2MP (URL_TO_INSERT_RECORD_5894 https://fairsharing.org/FAIRsharing.kg1x4z) 1      | HGNC (URL_TO_INSERT_RECORD_5895 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5896 https://fairsharing.org/FAIRsharing.29we0s)      | ENSG00000256069 | En       | eg93    |

Here, we see a `one-to-one` relation between the identifier (URL_TO_INSERT_TERM_5898 https://fairsharing.org/search?recordType=identifier_schema) s in HGNC (URL_TO_INSERT_RECORD_5901 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5903 https://fairsharing.org/FAIRsharing.29we0s)  and En while the relation between HGNC (URL_TO_INSERT_RECORD_5902 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5904 https://fairsharing.org/FAIRsharing.29we0s)  and UCSC Genome Browser (Uc) or Gene Ontology (URL_TO_INSERT_TERM_5897 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_5900 https://fairsharing.org/FAIRsharing.6xq0ee)  (T) is `one-to-many`. Depending on the identifier (URL_TO_INSERT_TERM_5899 https://fairsharing.org/search?recordType=identifier_schema) s and resources, the relation could also be `many-to-many` as shown below.


````{dropdown} 
:open:
```{figure} bridgedb-recipe.md-figure2.mmd.png
---
name: bridgedb (URL_TO_INSERT_RECORD_5905 https://fairsharing.org/FAIRsharing.5ry74y) -recipe-figure2
alt: An example of a map (URL_TO_INSERT_RECORD_5908 https://fairsharing.org/FAIRsharing.53edcc) ping via BridgeDb (URL_TO_INSERT_RECORD_5906 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5907 https://fairsharing.org/FAIRsharing.5ry74y) .
---
An example of a map (URL_TO_INSERT_RECORD_5911 https://fairsharing.org/FAIRsharing.53edcc) ping via BridgeDb (URL_TO_INSERT_RECORD_5909 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5910 https://fairsharing.org/FAIRsharing.5ry74y) . You may notice that despite the 1-to-1 relation between `local` and `original` we get a N-to-N relation between `local` and `map (URL_TO_INSERT_RECORD_5912 https://fairsharing.org/FAIRsharing.53edcc) ping` due to the N-to-N relation between `original` and `map (URL_TO_INSERT_RECORD_5913 https://fairsharing.org/FAIRsharing.53edcc) ping`.
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
Then, after computing the map (URL_TO_INSERT_RECORD_5915 https://fairsharing.org/FAIRsharing.53edcc) ping, we can join it with the local identifier (URL_TO_INSERT_TERM_5914 https://fairsharing.org/search?recordType=identifier_schema) 

```r
right_join(data_df, mapping)
```
Assuming we did not specify the target data source we obtain the following table (first 10 rows):
| local | identifier (URL_TO_INSERT_TERM_5916 https://fairsharing.org/search?recordType=identifier_schema)  | source | target | map (URL_TO_INSERT_RECORD_5917 https://fairsharing.org/FAIRsharing.53edcc) ping      |
|:----- |:--------   |:------ |:------ |:------------ |
| aa11  | A1BG       | H      | Uc     | uc002qsd.5   |
| aa11  | A1BG       | H      | X      | 8039748      |
| aa11  | A1BG       | H      | T      | GO (URL_TO_INSERT_RECORD_5918 https://fairsharing.org/FAIRsharing.6xq0ee) :0072562   |
| aa11  | A1BG       | H      | Uc     | uc061drj.1   |
| aa11  | A1BG       | H      | Il     | ILMN_2055271 |
| aa11  | A1BG       | H      | U      | Hs.529161    |
| aa11  | A1BG       | H      | T      | GO (URL_TO_INSERT_RECORD_5919 https://fairsharing.org/FAIRsharing.6xq0ee) :0070062   |
| aa11  | A1BG       | H      | T      | GO (URL_TO_INSERT_RECORD_5920 https://fairsharing.org/FAIRsharing.6xq0ee) :0002576   |
| aa11  | A1BG       | H      | Uc     | uc061drt.1   |
| aa11  | A1BG       | H      | X      | 51020_at     |

In case we did specify the target data source we would get:

| local | identifier (URL_TO_INSERT_TERM_5921 https://fairsharing.org/search?recordType=identifier_schema)  | source | target | map (URL_TO_INSERT_RECORD_5922 https://fairsharing.org/FAIRsharing.53edcc) ping         |
|:----- |:---------- |:------ |:------ |:--------------- |
| aa11  | A1BG       | HGNC (URL_TO_INSERT_RECORD_5923 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5924 https://fairsharing.org/FAIRsharing.29we0s)    | En     | ENSG00000121410 |
| bb34  | A1CF       | HGNC (URL_TO_INSERT_RECORD_5925 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5926 https://fairsharing.org/FAIRsharing.29we0s)    | En     | ENSG00000148584 |
| eg93  | A2MP (URL_TO_INSERT_RECORD_5927 https://fairsharing.org/FAIRsharing.kg1x4z) 1      | HGNC (URL_TO_INSERT_RECORD_5928 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5929 https://fairsharing.org/FAIRsharing.29we0s)    | En     | ENSG00000256069 |

---
## Provenance

BridgeDb (URL_TO_INSERT_RECORD_5931 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5932 https://fairsharing.org/FAIRsharing.5ry74y)  provides provenance informat (URL_TO_INSERT_TERM_5930 https://fairsharing.org/search?recordType=model_and_format) ion through:
* A call to `/properties/` method of the Webservice
* `getProperties()` in BridgeDb (URL_TO_INSERT_RECORD_5933 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5934 https://fairsharing.org/FAIRsharing.5ry74y) R (passing the map (URL_TO_INSERT_RECORD_5935 https://fairsharing.org/FAIRsharing.53edcc) per as a parameter)

This returns the following informat (URL_TO_INSERT_TERM_5936 https://fairsharing.org/search?recordType=model_and_format) ion for each of the data sources for a given organism:
* Data source name
* Build date
* Series
* Data type
* Data source version
* Schema version

Improvements on provenance are under way (see [here](https://github.com (URL_TO_INSERT_RECORD_5937 https://fairsharing.org/FAIRsharing.c55d5e) /bridgedb/BridgeDb/issues/164)).

---

## Code 
You can find ready-made methods to map (URL_TO_INSERT_RECORD_5938 https://fairsharing.org/FAIRsharing.53edcc)  using R and Python for the given use cases [here](https://github.com (URL_TO_INSERT_RECORD_5939 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/the-fair-cookbook/tree/9ad9481be32812b2565f9f9f1897642ae26eddff/content/recipes/interoperability/bridgedb/data). These assume the data has the structure described in this recipe.

---

## Conclusion

We showed how to use BridgeDb (URL_TO_INSERT_RECORD_5941 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5942 https://fairsharing.org/FAIRsharing.5ry74y) 's webservices and R package to map (URL_TO_INSERT_RECORD_5943 https://fairsharing.org/FAIRsharing.53edcc)  identifier (URL_TO_INSERT_TERM_5940 https://fairsharing.org/search?recordType=identifier_schema) s from different data sources using a minimal dataset. 
BridgeDb (URL_TO_INSERT_RECORD_5944 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_5945 https://fairsharing.org/FAIRsharing.5ry74y)  provides handy functionality to make 'omics' data more interoperable and reusable.
As with all annotation services, it is important to bear in mind the version of the service being used as well as the data on which the service invokation has been performed.
These are aspects of informat (URL_TO_INSERT_TERM_5946 https://fairsharing.org/search?recordType=model_and_format) ion provenance which we plan to provide in the future.
 
### What to read next?

* {ref}`fcb-find-identifier (URL_TO_INSERT_TERM_5947 https://fairsharing.org/search?recordType=identifier_schema) s`
* {ref}`fcb-identifier (URL_TO_INSERT_TERM_5948 https://fairsharing.org/search?recordType=identifier_schema) -map (URL_TO_INSERT_RECORD_5949 https://fairsharing.org/FAIRsharing.53edcc) ping`

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
