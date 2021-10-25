# How to discover Tools
:construction: :female-construction-worker:  **Work in progress** :construction: :female-construction-worker: 

<!--
>tooling workflow documentation: 
>https://docs.google.com/document/d/18IEEO14I_rmxV6ZFl4-wWrn43zzEFbn5IK45NigsKLw/edit
>F2F tooling slides: 
>https://docs.google.com/presentation/d/1NBfAhGgxhAkljac1A_99fJj8belyw3fC8A461snE62o/edit#slide=id.gcd87a8e32a_0_309
-->
[TOC]

## Main

Identifying tools and softwares for FAIRification operations makes it easier to implement FAIRification. Many tool registeries, such as the Elixir bio.tools platform, bioconda, and bioconductor, collects a wide range of biomedical tools. Most tools on those platforms are open source tools. Tools with commercial licenses are also widely used.

Identifying and selecting the proper tools rely on previous experiences, colleague recommendations. Bioinformaticians and biologists always end up spending a lot of times searching for and testing different tools. 

In the discrption of each tool, information on what kind of operations they support is given, but such operations are not directly linked to FAIR ification, and hence, it is hard to evaluate whether a tool is suitable for a FAIRification task, or can be assembled into this pipeline.

To identify what tools can be used for FAIRification and whether it possible to integrate them into a FAIRification pipeline, we developed this FAIRification tool discoverer, which searches through the big public tool repositories using selected FAIRification topics and operations, evaluates the relevance and FAIRness of each tool, and provide rich description for each tool.

The FAIR discoverer includes three parts: 1. FAIRification capability identification 2. tool discoverer 3. ranking and selection

## Step-by-step discovery

### Step 1: identify FAIRification capability
We identified a list of key fairification topics, which serves as the backlog. table 1 shows a exmaple list of topis and related pre-curated keywords
|topic|keywords|
|--|--|
|metadata curation|vocabulary, ontology annotation, 

### Step 2: run the discoverer.
#### 2.1 Download the program
>:warning: We have the program inside WP3_FAIR_tooling. Maybe we should put it in a repo for its own to simplify download, issues, etc
> The following works for the current location of the program (inside WP3_FAIR_tooling)
1. Go to [GitZip](http://kinolien.github.io/gitzip/)
2. Introduce the following URL in the search bar:
```
https://github.com/FAIRplus/WP3_FAIR_tooling/tree/main/tool_discovery/tool_discoverer
```
![](https://i.imgur.com/odlYLgR.png)

3. Click 'Download'.
#### 2.2 Prepare input files
##### [Required] Configuration file
The paths to the input files and other parameters are provided to the program through a configuration file,  a plain text .ini file were five parameters are specified. It has the following form:
```ini
[required]
terms_file = keywords/ontology_annotation_EDAM_curated.csv
[optional]
ranked_terms_file = keywords/ontology_annotation_EDAM_ranked.csv
default_unspecified_keyword_score = 0.75
output_directory = results
name = example
```
###### **Required parameters**

* `terms_file`: path of file that contains keywords and matching EDAM terms and IRIs. 
 
###### **Optional parameters**
* `ranked_terms_file`: path of file that contains the scores assigned to each keyword. If empty, all keywords will be assigned a weight = 1.

* `default_unspecified_keyword_weight`: the weight automatically assigned to keywords that are not included in the 'ranked_terms_file'. If empty, 0.7 will be assigned.

* `output_directory`: directory where results are stored. If empty, results will be saved in the working directory.

* `name`: name associated to the execution and is used to name the result files.

>:warning: The following tow files specifications can be moved to steps 2 and 3, where they are produced, and provide a mini example of each. 

##### [Required] `terms_file` file format
CSV file of three columns: `keyword`, `label` and `iri`. Each row corresponds to a keyword.
* `keyword`: term to be included in the search.
* `label`: EDAM label.
* `iri`: EDAM IRI.

##### [Optional]`ranked_terms_file` file format
CSV file of two columns: `keyword`, `weight`. Each row correspond to a keyword.
* `kyeword`: term to be included in the search.
* `weight`: weight assigned the keyword. In order for the maximum score to be 1, weights must be in the interval [0,1].


#### 2.3 Run *tool_discoverer*

```bash
python3 tool_discoverer.py <configuration_file> [-v] [-h]
```
* `configuration_file`: path of configuration file.
* `-v, --verbose`: print detail information about the program progress to prompt.
* `-h, --help`: show help message.

```




