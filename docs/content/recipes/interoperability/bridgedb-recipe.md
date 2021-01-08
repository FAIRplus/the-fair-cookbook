
# Identifier mapping with BridgeDB


___

<div class="row">

  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-qrcode fa-2x" style="color:#7e0038"></i>
        <h4><b>Recipe metadata</b></h4>
        <p> identifier: <a href="">RX.X</a> </p>
        <p> version: <a href="">v1.0</a> </p>
      </div>
    </div>
  </div>
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-fire fa-2x" style="color:#7e0038"></i>
        <h4><b>Difficulty level</b></h4>
        <i class="fa fa-fire fa-lg" style="color:#7e0038"></i>
        <i class="fa fa-fire fa-lg" style="color:#7e0038"></i>
        <i class="fa fa-fire fa-lg" style="color:#7e0038"></i>
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
        <p><i class="fa fa-clock-o fa-lg" style="color:#7e0038;"></i> 30 minutes</p>
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
<!--         <p> <i class="fa fa-money fa-lg" style="color:#7e0038;"></i> Funders</p> -->
      </div>
    </div>
  </div>
</div>

___

<!-- ## Table of Contents
[toc]

--- -->

## Main Objectives

The main purpose of this recipe is to:

> Provide practical examples on how to map **identifiers for molecular entities** (`such as Genes, Proteins, Metabolights and Pathways`) between resources using a purpose built tool, namely [BridgeDB](https://bio.tools/bridgedb).
> Hands on guidance is provided for 2 interfaces (R package and a Python Webservices) provided by [BridgeDB](https://bio.tools/bridgedb).


___


## Graphical Overview of the FAIRification Recipe Objectives

This recipe will cover the highlighted topics
```mermaid
    graph TB
      I[Identifier]
      I --> IM[Identifier Mapping]
      M[Mapping Process] --> OM[Ontology Mapping]
      OM --> OxO[OxO Service]

      M --> IM

      IM -- performs --> IMS

      IM -- performs--> IE([Identifier Equivalence Assessment])
      IE -- uses service--> SL{{Scientific Lenses}}

      IMS([Identifier Mapping Services])
      IMS -- uses service --> BDb[BridgeDb]
      IMS -- uses service --> UniChem{{UniChem}}
      IMS -- uses service --> Sameas{{Sameas}}
      IMS -- uses service --> Identifiers{{Identifiers.org}}

      BDb -- performs --> MGG[Mapping global identifiers to other global identifiers]
      BDb -- performs --> MLG[Mapping local identifiers to other global identifiers]

      MGG -- implemented in --> P1([Python])
      MGG -- implemented in --> R1([R])
      MLG -- implemented in --> P2([Python])
      MLG -- implemented in --> R2([R])

        style OM stroke-dasharray: 5 5
        style M stroke-dasharray: 5 5

       classDef select fill:#f9f;
       class BDb select;
       class MLG select;
       class MGG select;
       class P1 select;
       class P2 select;
       class R1 select;
       class R2 select;
      %% style IM fill:#f9f
      %% style I fill:#f9f
      %% style OxO fill:#f9f
```

___


## Requirements

* recipe dependency:
    * [How to generate globally unique, resolvable and persistent identifiers]()
    * [How to interlink data from different sources?]()

* skill dependency:
    * programming knowledge
    * R
    * Python

* technical dependency
    * R or Python environment
    * BridgeDB R package installed
---

## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Interoperability | minimal | repeatable |
| Reusability | minimal| reusable|

---

## Tools


|Software|Description|version|Biotools record|
|--|--|--|--|
|[BrideDb](https://bridgedb.github.io/)|BridgeDb is a framework to map identifiers between various databases. It includes a Java library that provides an API to work with identifier-identifier mapping databases and resources.| 0.0.9|[https://bio.tools/bridgedb](https://bio.tools/bridgedb)
|Python|an interpreted, high-level and general-purpose programming language|3.8.5| |
|[Pandas](https://pandas.pydata.org/)|pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,built on top of the Python programming language.|1.1.3| |
|R|R is a programming language and free software environment for statistical computing and graphics supported by the R Foundation for Statistical Computing.|v4.0.3|https://bio.tools/r|
|tidyverse|The tidyverse is an opinionated collection of R packages designed for data science.  | 1.3.0||
|BridgeDbR|an R package for BridgDb| 2.0.0||



<!--## Table of Data Standards


| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| [FASTQ](https://fairsharing.org/FAIRsharing.r2ts5t)  | [LOINC](https://fairsharing.org/FAIRsharing.2mk2zb)  | [SRA XML](https://fairsharing.org/FAIRsharing.q72e3w)  |
| [DICOM](https://fairsharing.org/FAIRsharing.b7z8by)  | [Human Phenotype Ontology](https://fairsharing.org/FAIRsharing.kbtt7f)  | [OMOP](https://fairsharing.org/FAIRsharing.qk984b)  |
-->
___

## Identifier mapping with BridgeDb

[Identifier mapping](https://github.com/FAIRplus/the-fair-cookbook/blob/id-map-services/docs/content/recipes/interoperability/identifier-mapping.md) is an essential step for data reusability and interoperability. This step requires dedicated tools. With the present recipe, we show how to use BridgeDb to carry out  this process.

BridgeDB is an open source tool dedicated to performing identifier mapping. BridgeDB offers three different interfaces:
* Java API
* R package
* REST Web-services


> :book: In the context of this recipe, we distinguish between two types of identifiers:
>* *Local identifiers*, which refer to identifiers that are minted within an organization or database and thus internally defined (i.e. local to said organization) 
>* *Global identifiers*, which refer to identifiers which globally unique and uniquely point to an entity, as available from BridgeDb's [data sources file](https://github.com/bridgedb/BridgeDb/blob/2dba5780260421de311cb3064df79e16a396b887/org.bridgedb.bio/resources/org/bridgedb/bio/datasources.tsv)

We will focus here on two distinct cases, depending on the nature of the incoming data. Namely, whether our data is already using global identifiers or only relies on local identifiers. 


#### Cases:

1. Connect data with global identifiers to different global identifiers
3. Connect data with local identifiers that were mapped to a global identifier to a different global identifier
 
<!-- [NEED HELP HERE]
:warning:[Question: does it mean the `local identifier` must already be mapped to a 'global identifier'] --> 

In this recipe, we will cover how the R package and webservices can be used to accomplish the stated objectives.

### Mapping global identifier to other global identifier
In this case, the input data is a list of elements with an identifier that is part of [BridgeDbs data sources](https://github.com/bridgedb/BridgeDb/blob/2dba5780260421de311cb3064df79e16a396b887/org.bridgedb.bio/resources/org/bridgedb/bio/datasources.tsv). In our example, we will use a list of Homo Sapiens, Hugo Gene Nomenclature Convention (HGNC) gene identifiers stored in a TSV file. The objective is to map these to other available gene identifiers.

#### BridgeDb via Webservices using Python
> :exclamation: For this tutorial Python v3.8.5, [pandas](https://pandas.pydata.org/) v1.1.3 and BridgeDb Webservices v0.9.0 were used.

One of the biggest benefits of using BridgeDb webservices is that these can be accessed using most programming language. Python has become one of the leading programming languages in data science and predictive modelling. Despite the lack of a dedicated BridgeDb Python library, we show here how to use the BridgeDb Webservices to perform the mappings suggested under [Cases](#Cases) 

- We start by defining strings containing the url of the webservices and the specific method from the Webservices we want to use. In our case, a `batch cross reference`. When doing the query, we need to specify **the organism** and **the source dataset**. We can also *optionally* specify a *target data source* if we only want to map one of them (e.g. Ensembl)  

```python=3.8.5
url = "https://webservice.bridgedb.org/"
batch_request = url+"{org}/xrefsBatch/{source}{}"
```

> If the aim is to only map to a specific target data source, then one can check whether the mapping is supported by invoking the following  webservices:  

```python=3.8.5
mapping_available = "{org}/isMappingSupported/{source}/{target}"
query = url+mapping_available.format(org='Homo sapiens', source='H', target='En')
requests.get(query).text
```
> This will return `True` if the mapping between the given source and target is supported for the given organism or `False` otherwise.

- We then load our data into a pandas dataframe and call the requests library using our query.

```python=3.8.5
query = batch_request.format('?dataSource=En', org='Homo sapiens', source='H')
response = requests.post(query, data=data.to_csv(index=False, header=False))
```

> The webservice response is now stored in the `response` variable. We can then simply pass this variable to the `to_df` method provided in the `bridgedb_script.py` module (see [Code](#Code)). This method will extract the response in text form and turn it into a pandas Dataframe with conveniently named columns and structured data.

The output table will contain:
* The original identifier
* The data source that the identifier is part of
* The mapped identifier
* The data source for the mapped identifier

>In our case the output of `to_df` is:

| original   | source   | mapping         | target   |
|:-----------|:---------|:----------------|:---------|
| A1BG       | HGNC     | ENSG00000121410 | En       |
| A1CF       | HGNC     | ENSG00000148584 | En       |
| A2MP1      | HGNC     | ENSG00000256069 | En       |



> If we were to not specify the target data source (by passing an empty string as the parameter), we would get all the potential mappings for the given identifiers. In our case (top 10 rows):

| original   | source   | mapping      | target   |
|:-----------|:---------|:-------------|:---------|
| A1BG       | HGNC     | uc002qsd.5   | Uc       |
| A1BG       | HGNC     | 8039748      | X        |
| A1BG       | HGNC     | GO:0072562   | T        |
| A1BG       | HGNC     | uc061drj.1   | Uc       |
| A1BG       | HGNC     | ILMN_2055271 | Il       |
| A1BG       | HGNC     | Hs.529161    | U        |
| A1BG       | HGNC     | GO:0070062   | T        |
| A1BG       | HGNC     | GO:0002576   | T        |
| A1BG       | HGNC     | uc061drt.1   | Uc       |
| A1BG       | HGNC     | 51020_at     | X        |

As one can see, using BridgeDb service via Python is extremely  simple and can be easily integrated in an annotation pipeline.


#### BridgeDb via the dedicated R package
> :exclamation: For this tutorial R v4.0.3, [tidyverse](https://www.tidyverse.org/) v1.3.0 and [BridgeDbR](https://www.bioconductor.org/packages/release/bioc/html/BridgeDbR.html) v2.0.0 were used.

After having loaded the required R libraries, we read the data and create a new column to include the source of the identifier.

```r
data_df <- read_tsv(filepath, col_names=c('identifier'))
data_df$source = 'H'
``` 

We then load the data for the organism we are mapping from.

```r
 location <- getDatabase('Homo sapiens')
 mapper <- loadDatabase(location)
```

And use the library's     dedicated function to map the identifiers:

```r
mapping = maps(mapper, data_df, target='En')
```
This will return:
| identifier | source | target | mapping         |
|:---------- |:------ |:------ |:--------------- |
| A1BG       | H      | En     | ENSG00000121410 |
| A1CF       | H      | En     | ENSG00000148584 |
| A2MP1      | H      | En     | ENSG00000256069 |

As seen earlier when using Python language, we can obtain all possible mappings simply by not specifying the target. This will result in (top 10) 
| identifier | source | target | mapping      |
|:---------- |:------ |:------ |:------------ |
| A1BG       | H      | Uc     | uc002qsd.5   |
| A1BG       | H      | X      | 8039748      |
| A1BG       | H      | T      | GO:0072562   |
| A1BG       | H      | Uc     | uc061drj.1   |
| A1BG       | H      | Il     | ILMN_2055271 |
| A1BG       | H      | U      | Hs.529161    |
| A1BG       | H      | T      | GO:0070062   |
| A1BG       | H      | T      | GO:0002576   |
| A1BG       | H      | Uc     | uc061drt.1   |
| A1BG       | H      | X      | 51020_at     |

> :warning: An error message indicating "Error in download.file" may be thrown. If the case, it may be caused by `timeout` variable being set to too small a value. To remediate the issue, try increasing the timeout variable value by calling `options(timeout=300)`


<!--
This will maybe link to the identifier mapping recipe in the future, where there will be a specific section detailing identifier equivalence files taking into account scientific lenses, as discussed with Egon. 

--------------------------------


### Mapping local identifier to global identifier
[NEED HELP HERE]
This is a step that should be done manually. In this case an important decision should be made, which identifiers to map to. To decide this you should look for the data source that contains the closest definition of the concepts to the one you used for your local identifiers.

-->

### Mapping local identifier to a different global identifier

> :bulb: In this section, we assume that we already have an equivalence file containing the mapping of a local identifier to one of the global identifiers. In our case, this will be contained in a TSV where we map our local gene identifier to HGNC [specific what it is]. One may consult the list of other potential data formats in the [Identifier Mapping recipe](). The mapping should be **one-to-one** for this recipe. 

The TSV mapping file looks as follows:
| local   | source   |
|:--------|:---------|
| aa11    | A1BG     |
| bb34    | A1CF     |
| eg93    | A2MP1    |

You may notice the `source` identifiers correspond with those used in the previous example.


This is how the mapping will work
```mermaid
    graph TB 
      subgraph Script

          subgraph BridgeDb
              B[Affy]-->E[Gene Ontology]
              B[Affy]-->F[NCBI gene]
              B[Affy] --> H[UniProt]
          subgraph Pre-made mapping
            A[Local identifier.source]-->B[Ensembl]
          end
          end
        end
```

#### Webservices in Python

As before, we will define variables including the `web-service's URL` and the `method` that we will use, in this instance: `xRefsBatch`.

We then pass the source column to the `post request` as follows

```python=3.8.5
source_data = case2.source.to_csv(index=False, header=False)
query = batch_request.format('', org=org, source=source)
response2 = requests.post(query, data = source_data)
```
You may notice here that we did not pass a target source, this could be done as specified before. Then, we use `to_df` again and as expected obtain the same dataframe as before.
To see the equivalences with our local identifiers, we can simply join the dataframes, as follows:

```python=3.8.5
local_mapping = mappings.join(case2.set_index('source'), on='original')
```
which will return the following table (first 10 rows)
| original   | source   | mapping      | target   | local   |
|:-----------|:---------|:-------------|:---------|:--------|
| A1BG       | HGNC     | uc002qsd.5   | Uc       | aa11    |
| A1BG       | HGNC     | 8039748      | X        | aa11    |
| A1BG       | HGNC     | GO:0072562   | T        | aa11    |
| A1BG       | HGNC     | uc061drj.1   | Uc       | aa11    |
| A1BG       | HGNC     | ILMN_2055271 | Il       | aa11    |
| A1BG       | HGNC     | Hs.529161    | U        | aa11    |
| A1BG       | HGNC     | GO:0070062   | T        | aa11    |
| A1BG       | HGNC     | GO:0002576   | T        | aa11    |
| A1BG       | HGNC     | uc061drt.1   | Uc       | aa11    |
| A1BG       | HGNC     | 51020_at     | X        | aa11    |

In case we did specify the `target` argument to be `Ensembl (En)`, we would instead get

| original   | source   | mapping         | target   | local   |
|:-----------|:---------|:----------------|:---------|:--------|
| A1BG       | HGNC     | ENSG00000121410 | En       | aa11    |
| A1CF       | HGNC     | ENSG00000148584 | En       | bb34    |
| A2MP1      | HGNC     | ENSG00000256069 | En       | eg93    |

Here, we see a `one-to-one` relation between the identifiers in HGNC and En while the relation between HGNC and UCSC Genome Browser (Uc) or Gene Ontology (T) is `one-to-many`. Depending on the identifiers and resources, the relation could also be `many-to-many` as shown below.

<!--
You may notice that despite the 1-to-1 relation between `local` and `original` we get a N-to-N relation between `local` and `mapping` due to the N-to-N relation between `original` and `mapping`. This can be easily understood with the diagram below-->
```mermaid
    graph LR 
      classDef sources stroke-width:4px;

      class En sources;
      class X sources;
      class Local sources;

      classDef BDb fill: #d5fca6, fontSize: 40px, stroke-width:6px, stroke: #000
      class BridgeDb BDb;

      1234 <==>  AF1
      5555 <==> AF3
      6789 <==> AF2

      subgraph Local
        1234
        5555
        6789
      end


      subgraph BridgeDb
        AF1 --> ZM1
        AF1 --> ZM2
        AF1 --> ZM3
        AF2 --> ZM4
        AF3 --> ZM4
        subgraph Affy
          AF1[AFFX-Zm-ef1a-5_a_at]
          AF2[AFFX-Zm_Ubiquitin_M_f_at]
          AF3[AFFX-Zm_Ubiquitin_5_f_at]
        end
        subgraph Ensembl
          ZM1[Zm00001d037873]
          ZM2[Zm00001d037877]
          ZM3[Zm00001d037875]
          ZM4[Zm00001d053838]
        end
      end

```

> :book: This many-to-many relationship stems from different *scientific lenses* in the data sources. You can read more about these in (Brenninkmeijer et al., n.d.). The core idea is that depending on the domain/application of the data we can consider different entities as unique. While certain proteins could be considered "equal" from a biological perspective they may require differentiation when using a chemical lense. This is what then leads to many-to-many relationships.

#### R Package

Here, we will follow the same steps as in the previous case. The only difference is that we need to specify the columns/fields to use when loading the data:

```r
data_df <- read_tsv(filepath, col_names=c('local', 'identifier'))
``` 
Then, after computing the mapping, we can join it with the local identifier

```r
right_join(data_df, mapping)
```
Assuming we did not specify the target data source we obtain the following table (first 10 rows):
| local | identifier | source | target | mapping      |
|:----- |:--------   |:------ |:------ |:------------ |
| aa11  | A1BG       | H      | Uc     | uc002qsd.5   |
| aa11  | A1BG       | H      | X      | 8039748      |
| aa11  | A1BG       | H      | T      | GO:0072562   |
| aa11  | A1BG       | H      | Uc     | uc061drj.1   |
| aa11  | A1BG       | H      | Il     | ILMN_2055271 |
| aa11  | A1BG       | H      | U      | Hs.529161    |
| aa11  | A1BG       | H      | T      | GO:0070062   |
| aa11  | A1BG       | H      | T      | GO:0002576   |
| aa11  | A1BG       | H      | Uc     | uc061drt.1   |
| aa11  | A1BG       | H      | X      | 51020_at     |

In case we did specify the target data source we would get:

| local | identifier | source | target | mapping         |
|:----- |:---------- |:------ |:------ |:--------------- |
| aa11  | A1BG       | HGNC   | En     | ENSG00000121410 |
| bb34  | A1CF       | HGNC   | En     | ENSG00000148584 |
| eg93  | A2MP1      | HGNC   | En     | ENSG00000256069 |


___
## Code 
You can find ready-made methods to map using R and Python for the given use cases [here](https://github.com/mavrokefalidis/bridgedb-recipe-code). These assume the data has the structure described in this recipe.

---

## Conclusion

> We showed how to use BridgeDb webservices and R package to map identifiers from different data sources using a minimal dataset. 
> BridgeDb provides handy functionality to make 'omics' type of data more interoperable and reusable.
> As with all annotation services, it is important to bear in mind the version of the service being used as well as the data on which the service invokation has been performed.
> These are aspects of information provenance which 
> 
> #### What should I read next?
> * [Identifiers](#TODO)
> * [Identifier mapping](#TODO)
> * [Provenance information]()

## References
---
1. Brenninkmeijer, C., Evelo, C., Goble, C., Gray, A. J. G., Groth, P., Pettifer, S., Stevens, R., Williams, A. J., & Willighagen, L. (n.d.). Scientiﬁc Lenses over Linked Data: An approach to support task speciﬁc views of the data. A vision. 4.
2. Leemans C, Willighagen E, Slenter D, Bohler A, Eijssen L (2020). BridgeDbR: Code for using BridgeDb identifier mapping framework from within R. R package version 2.0.0, https://github.com/bridgedb/BridgeDbR. 
3. Standardised access to Gene, Gene-Variant, Protein, Metabolite and Interaction Identifier Mapping Services. (n.d.). bridgedb.github.io. Retrieved January 4, 2021, from https://bridgedb.github.io/

___
## Authors

| Name | Affiliation  | orcid | Credit role  | specific contribution |
| :------------- | :------------- | :------------- |:------------- |:------------- |
| Lucas Giovanni Uberti-Bona Marin |  Maastricht University| [0000-0001-6518-9535](https://orcid.org/0000-0001-6518-9535)| Writing - Original Draft | Original format |

___


## License

This page is released under the Creative Commons 4.0 BY license.

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>

