
# Identifier mapping with BridgeDB



## Table of Contents
1. [Main Objectives](#Main%20FAIRification%20Objectives)
2. [Graphical Overview of the FAIRification Recipe Objectives](#Graphical%20Overview%20of%20the%20FAIRification%20Recipe%20Objectives)
3. Requirements
4. [FAIRification Objectives, Inputs and Outputs](#FAIRification%20Objectives,%20Inputs%20and%20Outputs)
5. [Capability & Maturity Table](#Capability%20&%20Maturity%20Table)
6. [Table of Data Standards](#Table%20of%20Data%20Standards)
7. [Main Content goes here...](#Main%20Content)
    * [... writing executable code](#Executable%20Code%20in%20Notebook)
    * [... creating workflow figures](#How%20to%20create%20workflow%20figures)
8. [License](#License)

---

## Main Objectives

The main purpose of this recipe is:

> Providing practical examples on how two of BridgeDB's interfaces (R package and Webservices) can be used to map identifiers 


___


## Graphical Overview of the FAIRification Recipe Objectives

Note: use this section to provide a decision tree for the overall process described in the recipe
For more information about the syntax used to generate the diagram, please refer to the [following documentation](https://mermaid-js.github.io/mermaid/#/flowchart)


<div class="mermaid">

    flowchart TB 

        subgraph TSV
        A[Local identifier]-->B[Affy]
        end

        subgraph BridgeDb
        C[Affy]-->Ensembl
        end

        subgraph Script
        D[Local identifier] --> F[Affy] --> E[Ensembl]
        end

        TSV --> Script
        BridgeDb --> Script
</div>

___


## Requirements

* technical requirements:
    * R
    * Webservices
    * Python
* recipe dependency:
    * "How to generate globally unique, resolvable and persistent identifiers"
    * "How to interlink data from different sources?"

---

## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Interoperability | minimal | repeatable |
| Reusability | minimal| reusable|


## Table of Data Standards
<!--

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| [FASTQ](https://fairsharing.org/FAIRsharing.r2ts5t)  | [LOINC](https://fairsharing.org/FAIRsharing.2mk2zb)  | [SRA XML](https://fairsharing.org/FAIRsharing.q72e3w)  |
| [DICOM](https://fairsharing.org/FAIRsharing.b7z8by)  | [Human Phenotype Ontology](https://fairsharing.org/FAIRsharing.kbtt7f)  | [OMOP](https://fairsharing.org/FAIRsharing.qk984b)  |
-->
___

## Identifier mapping with Bridgedb

[Identifier mapping](https://github.com/FAIRplus/the-fair-cookbook/blob/id-map-services/docs/content/recipes/interoperability/identifier-mapping.md) often is an essential step for data reusability and interoperability. 

#### Use cases:

1. Connect data with known identifiers to different known identifiers
3. Connect data with local identifiers that were mapped to a known identifier to a different known identifier

BridgeDB is an open source tool that can help us perform identifier mapping using three different interfaces:
* Java API
* R package
* Webservices

In this recipe we will cover how the R package and webservices can be used to accomplish the stated objectives.

## Webservices in Python
One of the biggest benefits of using BridgeDb's webservices is that these can be accessed using any programming language. Python has become one of the leading programming languages in data science and predictive modelling. Despite the lack of a BridgeDb Python library we show here how to use the Webservices to perform the mappings suggested under "Use cases" 

### Mapping known identifier to other known identifier
In this case we have a list of elements with an identifier that is part of [BridgeDbs data sources]((https://github.com/bridgedb/BridgeDb/blob/2dba5780260421de311cb3064df79e16a396b887/org.bridgedb.bio/resources/org/bridgedb/bio/datasources.tsv)). In our example we will use a list of Affymetrix Zen Mays gene identifiers stored in a TSV file. The objective is to map these to other available gene identifiers.

For this tutorial Python v3.8.5 and [pandas](https://pandas.pydata.org/) v1.1.3  were used.

We start by defining strings containing the url to the webservices and the specific method from the Webservices that we want to use. In our case a batch cross reference. When we do our query we will specify the organism and the source dataset. We can also optionally specify a target data source if we only want to map one of them (e.g. Ensembl)  

```python
url = "https://webservice.bridgedb.org/"
batch_request = url+"{org}/xrefsBatch/{source}{}"
```
We start by loading our data into a pandas dataframe. We then call the requests library using our query

```python
query = batch_request.format('?dataSource=En', org='Zea Mays', source='X')
response = requests.post(query, data=data.to_csv(index=False, header=False))
```

The webserivce's response is now stored in the `response` variable. We can now simply pass this variable to the `to_df` method provided in the `bridgedb_script.py` module. This method will extract the response in text form and turn it into a pandas Dataframe with conveniently named columns and structured data.

In our case the output of `to_df` is:
| original                 | source   | mapping        | target   |
|:-------------------------|:---------|:---------------|:---------|
| AFFX-Zm-ef1a-5_a_at      | Affy     | Zm00001d037873 | En       |
| AFFX-Zm-ef1a-5_a_at      | Affy     | Zm00001d037877 | En       |
| AFFX-Zm-ef1a-5_a_at      | Affy     | Zm00001d037875 | En       |
| AFFX-Zm_Ubiquitin_M_f_at | Affy     | Zm00001d053838 | En       |
| AFFX-Zm_Ubiquitin_5_f_at | Affy     | Zm00001d053838 | En       |

The output table will contain:
* The original identifier
* The data source that the identifier is part of
* The mapped identifier
* The data source for the mapped identifier

If we were to not specify the target data source we would get all the potential mappings for the given identifiers. In our case (top 10 rows):
| original            | source   | mapping    | target   |
|:--------------------|:---------|:-----------|:---------|
| AFFX-Zm-ef1a-5_a_at | Affy     | A0A1D6M1H3 | S        |
| AFFX-Zm-ef1a-5_a_at | Affy     | A0A1D6M1H2 | S        |
| AFFX-Zm-ef1a-5_a_at | Affy     | A0A1D6M1J4 | S        |
| AFFX-Zm-ef1a-5_a_at | Affy     | GO         | T        |
| AFFX-Zm-ef1a-5_a_at | Affy     | A0A1D6M1J3 | S        |
| AFFX-Zm-ef1a-5_a_at | Affy     | Q9M7E4     | S        |
| AFFX-Zm-ef1a-5_a_at | Affy     | A0A1D6M1H0 | S        |
| AFFX-Zm-ef1a-5_a_at | Affy     | A0A1D6M1J2 | S        |
| AFFX-Zm-ef1a-5_a_at | Affy     | B6SKA7     | S        |
| AFFX-Zm-ef1a-5_a_at | Affy     | A0A1D6M1J1 | S        |

### Mapping local identifier to known identifier
[NEED HELP HERE]
This is a step that should be done manually. In this case an important decision should be made, which identifiers to map to. To decide this you should look for the data source that contains the closest definition of the concepts to the one you used for your local identifiers.

### Mapping local identifier to a different known identifier
___

## Conclusion:

> Summarize Key Learnings of the recipe.
> 
> Suggest further reading using the following:
> #### What should I read next?
> * [HackMD & MarkDown Tips and Tricks](TODO)
> * [A related recipe which nice complements the current one ](TODO)

___
## Authors:

| Name | Affiliation  | orcid | CrediT role  | specific contribution |
| :------------- | :------------- | :------------- |:------------- |:------------- |
| Lucas Giovanni Uberti-Bona Marin |  Maastricht University| | Writing - Original Draft | Original format |
| Chris Evelo |  Maastricht University | | Writing - Review & Editing, Funding acquisition | | 
| Egon Willighagen |  Maastricht University | | Writing - Review & Editing, Funding acquisition | | 
| Alasdair Gray | Heriot-Watt Unviersity / ELIXIR-UK | [0000-0002-5711-4872](https://orcid.org/0000-0002-5711-4872) | Writing - Review & Editing | minor improvements (see git) |

___


## License:

This page is released under the Creative Commons 4.0 BY license.

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>

