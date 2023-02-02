(fcb-fairify-examples-datamatrix)=
# Making omics data matrix FAIR



````{panels_fairplus}
:identifier_text: FCB037
:identifier_link: 'https://w3id.org/faircookbook/FCB037'
:difficulty_level: 4
:recipe_type: hands_on
:reading_time_minutes: 30
:intended_audience: data_manager, data_scientist 
:maturity_level: 2 
:maturity_indicator: 1, 2
:has_executable_code: yeah
:recipe_name: Making an omics data matrix FAIR
```` 


## Main Objectives

The main purpose of this recipe is:

> Making self describing tabular data using [the suite of Frictionless specifications](https://specs.frictionlessdata.io/) instead of dumping Excel files

- ensure that results presented in Excel files or PDF tables are made more open and unambiguous
- provide an RDF (URL_TO_INSERT_RECORD_455 https://fairsharing.org/FAIRsharing.p77ph9)  representation
- enable reproducibility of results
- evaluate efficiency of the method via a data integrate challenge
---


## Summary

Scientific data is often stored as unstructured data in proprietary file format (URL_TO_INSERT_TERM_456 https://fairsharing.org/search?recordType=model_and_format) s, with meaning of the files and data understandable by knowledgeable experts only. Often the meaning derives from the context, given in a scientific publication to which the data is attached as a "supporting informat (URL_TO_INSERT_TERM_457 https://fairsharing.org/search?recordType=model_and_format) ion". One of the aims of FAIR (URL_TO_INSERT_RECORD_459 https://fairsharing.org/FAIRsharing.WWI10U)  is to change this towards machine-understandable representation of informat (URL_TO_INSERT_TERM_458 https://fairsharing.org/search?recordType=model_and_format) ion. This recipe exemplifies this journey on a concrete example:  

- The first data source: article by [Raymond et al. Nat Genet. 50:772-777 (2018)](https://doi.org/10.1038/s41588-018-0110-3); is a targeted metabolite profiling study of strain-related chemical signatures of the rose fragrance; the biological material was selected to allow a comparison between parts of the plant, and across cultivars in the same tissue type.

- The starting point: the human-understandable data in the [supplementary file 41588_2018_110_MOESM3_ESM.zip](https://static-content.springer.com/esm/art%3A10.1038%2Fs41588-018-0110-3/MediaObjects/41588_2018_110_MOESM3_ESM.zip), containing the mean concentrations of 61 metabolites measured in three different parts of the rose flower, in six distinct genotypes.

- The second data source: article by [Magnard et al. Science.Jul 3;349(6243):81-3 (2015)](https://doi.org/10.1126/science.aab0696); this is early work of the same group of authors of the first data source.

- The approach: we performed a retrospective curation and re-annotation of the data matrices, disambiguating of the experimental design, using community, open interoperability standard (URL_TO_INSERT_TERM_460 https://fairsharing.org/search?fairsharingRegistry=Standard) s from [FAIRsharing](https://fairsharing.org); we focused on the clarity of the statistical results to ensure reusability and reproducibility of the analytical workflow by humans and machines. The FAIR (URL_TO_INSERT_RECORD_461 https://fairsharing.org/FAIRsharing.WWI10U) ification steps for the first data source are documented in the sections below; the same steps were applied to the second data source to assess inter-experiment agreement, as both studies used the same varieties of rose and plant parts. 

- The results: semantically-anchored data matrices served as Linked Data, deposited in public arch (URL_TO_INSERT_RECORD_464 https://fairsharing.org/FAIRsharing.52b22c) ives (Zenodo (URL_TO_INSERT_RECORD_463 https://fairsharing.org/FAIRsharing.wy4egf)  and MetaboLights (URL_TO_INSERT_RECORD_462 https://fairsharing.org/FAIRsharing.kkdpxe) ), and consumable by software agents for queries like “Retrieve study predictor variables and their levels” and “What is sample size used to compute the means?” to support study results review and assessment.


## Graphical Overview

````{dropdown}
:open:
```{figure} fair-data-matrix-recipe.md-figure1.mmd.png
---
width: 800px
name: fcb-fairify-examples-datamatrix-figure1
alt: Overview of the FAIR (URL_TO_INSERT_RECORD_465 https://fairsharing.org/FAIRsharing.WWI10U) ification process of a data matrix
---
Overview of the FAIR (URL_TO_INSERT_RECORD_466 https://fairsharing.org/FAIRsharing.WWI10U) ification process of a data matrix.
```
````

---

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [conversion](http://edamontology.org/operation_3434)  | Microsoft Excel file (.xlsx)<!-- TODO add a link to a specification of MS Excel file format -->  | [Frictionless JSON Data Package](https://frictionlessdata.io/specs/data-package/)  |
| [conversion](http://edamontology.org/operation_3434)  | Adobe PDF (.pdf)<!-- TODO add a link to a specification of Adobe PDF file format -->  | [Frictionless JSON Data Package](https://frictionlessdata.io/specs/data-package/)  |
| [format validation](http://edamontology.org/operation_0336)  | [Frictionless JSON (URL_TO_INSERT_RECORD_467 https://fairsharing.org/FAIRsharing.5bbab9)  Data Package (URL_TO_INSERT_RECORD_468 https://fairsharing.org/FAIRsharing.3b861d) ](https://frictionlessdata.io/specs/data-package/)   | [report](http://edamontology.org/data_2048)  |
| [conversion](http://edamontology.org/operation_3434)  | [Frictionless JSON (URL_TO_INSERT_RECORD_469 https://fairsharing.org/FAIRsharing.5bbab9)  Data Package (URL_TO_INSERT_RECORD_470 https://fairsharing.org/FAIRsharing.3b861d) ](https://frictionlessdata.io/specs/data-package/)  | [RDF/linked data](https://fairsharing.org/FAIRsharing.p77ph9)  |
| [text annotation](http://edamontology.org/operation_3778)  | [Human Phenotype Ontology (URL_TO_INSERT_RECORD_471 https://fairsharing.org/FAIRsharing.kbtt7f) ](https://fairsharing.org/FAIRsharing.kbtt7f)| [annotated text](http://edamontology.org/data_3779)|


## Table of Data Standards

| Data Format (URL_TO_INSERT_TERM_473 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_474 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_472 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
| [Frictionless JSON Data Package](https://frictionlessdata.io/specs/data-package/)  | [CHEBI](http://www.obofoundry.org/ontology/chebi.html)  ||
| [ISA-Tab](https://doi.org/10.25504/FAIRsharing.53gp75)  | [STATO](http://stato-ontology.org) ||
|  | [NCBITaxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi)||
|   | [Plant Ontology](http://www.obofoundry.org/ontology/po.html)||


---


## Table of Software and Tools

| Tool Name|
|:-----|
| [github](https://github.com/)|
| [zenodo API](https://developers.zenodo.org/)|
| [cookie cutter for data science](https://drivendata.github.io/cookiecutter-data-science/)|
| [python](https://www.python.org/)|
| [pandas](https://pandas.pydata.org/)|
| [camelot-py](https://camelot-py.readthedocs.io/en/master/)|
| [rdflib](https://rdflib.readthedocs.io/en/stable/)|
| [jupyter notebook](https://jupyter.org/)|
| [matplotlib](https://matplotlib.org/)|    
| [sparql](https://www.w3.org/TR/sparql11-query/)|

---




## Step by Step Process

### Step1: Address Data Findability and Accessibility

We made the initial spreadsheet table discoverable and citable by:

- uploading it to Zenodo (URL_TO_INSERT_RECORD_475 https://fairsharing.org/FAIRsharing.wy4egf) . 
- assigning an open license ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/))
- obtaining a persistent unique identifier (URL_TO_INSERT_TERM_476 https://fairsharing.org/search?recordType=identifier_schema)  in the form of a DOI (URL_TO_INSERT_RECORD_477 https://fairsharing.org/FAIRsharing.hFLKCn) : https://doi.org/10.5281/zenodo.2598799


     
### Step2: Address Interoperability

We transformed the data into a three-dimensional matrix (data cube), which represent: i) the metabolites (molecular entities), ii) the treatments (experimental conditions and corresponding biomaterials and bioassays), and iii) the quantitation type (measurements).

#### Step 2A: semantic anchoring
Metabolites (free text) names were augmented with unambiguous InChI (URL_TO_INSERT_RECORD_478 https://fairsharing.org/FAIRsharing.ddk9t9)  codes, assigned by accessing CHEBI (https://doi.org/10.25504/FAIRsharing.62qk8w) programmatically via its LibChebi library (https://github.com/libChEBI/libChEBIpy).  
We unpacked the informat (URL_TO_INSERT_TERM_479 https://fairsharing.org/search?recordType=model_and_format) ion held in the column header, identifying the main types of tabulated entities and their relationships, and replacing free text with ontology (URL_TO_INSERT_TERM_480 https://fairsharing.org/search?recordType=terminology_artefact)  terms.
For example, we disambiguated the taxonomic name of the cultivar from the anatomical part using terms and identifier (URL_TO_INSERT_TERM_482 https://fairsharing.org/search?recordType=identifier_schema) s from the NCBI Taxonomy (URL_TO_INSERT_RECORD_484 https://fairsharing.org/FAIRsharing.fj07xj)  (https://doi.org/10.25504/FAIRsharing.fj07xj) and Plant Ontology (URL_TO_INSERT_TERM_481 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_483 https://fairsharing.org/FAIRsharing.3ngg40)  (https://doi.org/10.25504/FAIRsharing.3ngg40) respectively.

#### Step 2B: disambiguation of the experimental design
We clarified the intent of the experimentalist, which is a comparison between two independent variables identified: the rose variety and the organism part, which are both categorical variables with six and three discrete factor levels, respectively. Since only eight factor combinations are reported, we concluded that this is a fractional factorial design (rather than a  factorial design, where eighteen theoretical factor combinations are possible)
We disambiguated among the attributes of the samples those that are study factors and their values, to explicitly enable queries on treatment groups and their sizes. 
We used the STATistics Ontology (URL_TO_INSERT_TERM_485 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_486 https://fairsharing.org/FAIRsharing.na5xp)  (STATO (URL_TO_INSERT_RECORD_487 https://fairsharing.org/FAIRsharing.na5xp) ; https://doi.org/10.25504/FAIRsharing.na5xp) to unambiguously express and semantically type these notions.

#### Step 2C: clarification of the measurement performed
We unpacked the type of measurement, and formally annotated them with the STATO (URL_TO_INSERT_RECORD_488 https://fairsharing.org/FAIRsharing.na5xp)  classes; we also clarified the size of the sample over which the calculation was performed. 
Two measurements were identified for each of the experimental conditions, and for each treatment, a single biological material was prepared and assayed three times on the same analytical platform. 
We marked-up all entities with persistent resolvable identifier (URL_TO_INSERT_TERM_489 https://fairsharing.org/search?recordType=identifier_schema) s to enhance dataset connectivity. Therefore, the computed sample mean can only be used to estimate the variability of the measurement technique, not the biological variability. 
    
### Step3: Preservation of the data matrices in an open syntax

We used the Frictionless Tabular Data Package (URL_TO_INSERT_RECORD_491 https://fairsharing.org/FAIRsharing.082881)  (URL_TO_INSERT_RECORD_493 https://fairsharing.org/FAIRsharing.3b861d)  (https://specs.frictionlessdata.io/data-package/) to describe the table headers in JSON (URL_TO_INSERT_RECORD_492 https://fairsharing.org/FAIRsharing.5bbab9)  format (URL_TO_INSERT_TERM_490 https://fairsharing.org/search?recordType=model_and_format) .
The transformat (URL_TO_INSERT_TERM_494 https://fairsharing.org/search?recordType=model_and_format) ion is documented in a jupyter notebook (https://github.com/proccaserra/rose2018ng-notebook/blob/master/notebooks/0-rose-metabolites-Python-data-handling.ipynb).
     
### Step4: Address Reusability

We performed a conversion to Linked Data, using terms from OBO (URL_TO_INSERT_RECORD_497 https://fairsharing.org/FAIRsharing.847069)  Foundry (URL_TO_INSERT_RECORD_496 https://fairsharing.org/FAIRsharing.847069)  Ontologies (URL_TO_INSERT_TERM_495 https://fairsharing.org/search?recordType=terminology_artefact)  (https://fairsharing.org/biodbcore-001083/) 
As a result, the metabolite measurements can be plotted using popular visualization libraries (Python plotnine or R ggplot2) from either a SP (URL_TO_INSERT_RECORD_501 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_500 https://fairsharing.org/FAIRsharing.87ccfd)  query over the RDF (URL_TO_INSERT_RECORD_498 https://fairsharing.org/FAIRsharing.p77ph9)  representation or from the data package (URL_TO_INSERT_RECORD_499 https://fairsharing.org/FAIRsharing.3b861d)  directly.

     
### Step5: address Findability and Accessibility

We made the FAIR (URL_TO_INSERT_RECORD_504 https://fairsharing.org/FAIRsharing.WWI10U) ified outputs discoverable and citable by uploading them to Zenodo (URL_TO_INSERT_RECORD_503 https://fairsharing.org/FAIRsharing.wy4egf) , assigning an open license (CC-BY 4.0), and obtaining persistent unique identifier (URL_TO_INSERT_TERM_502 https://fairsharing.org/search?recordType=identifier_schema) s:
- GC-MS data from the 'Rose Genome' available as Frictionless Tabular Data Package (URL_TO_INSERT_RECORD_505 https://fairsharing.org/FAIRsharing.082881)  (URL_TO_INSERT_RECORD_506 https://fairsharing.org/FAIRsharing.3b861d) : https://doi.org/10.5281/zenodo.2640873
- RDF (URL_TO_INSERT_RECORD_507 https://fairsharing.org/FAIRsharing.p77ph9)  Linked Data representation of GC-MS data from the 'Rose Genome' article: https://doi.org/10.5281/zenodo.2598812
- Comparison of GC-MS datasets available as Frictionless Tabular Data Package (URL_TO_INSERT_RECORD_508 https://fairsharing.org/FAIRsharing.082881)  (URL_TO_INSERT_RECORD_509 https://fairsharing.org/FAIRsharing.3b861d) : https://doi.org/10.5281/zenodo.2640919
- Rose scent FAIR (URL_TO_INSERT_RECORD_511 https://fairsharing.org/FAIRsharing.WWI10U) ification project (URL_TO_INSERT_TERM_510 https://fairsharing.org/search?recordType=project)  code release: https://doi.org/10.5281/zenodo.2641109


To further demonstrate the value of such study design driven data representation, we applied a similar FAIR (URL_TO_INSERT_RECORD_513 https://fairsharing.org/FAIRsharing.WWI10U) ification process on the second data source. The results of this comparison are also released via Zenodo (URL_TO_INSERT_RECORD_512 https://fairsharing.org/FAIRsharing.wy4egf)  (https://doi.org/10.5281/zenodo.2640919).
Lastly, we produced a study description file, in ISA-Tab (URL_TO_INSERT_RECORD_519 https://fairsharing.org/FAIRsharing.53gp75)  format (URL_TO_INSERT_TERM_516 https://fairsharing.org/search?recordType=model_and_format)  (https://doi.org/10.25504/FAIRsharing.53gp75), which references the Tabular Data Package (URL_TO_INSERT_RECORD_517 https://fairsharing.org/FAIRsharing.082881)  (URL_TO_INSERT_RECORD_520 https://fairsharing.org/FAIRsharing.3b861d) s representing the results held in data matrices. The ISA file is suitable for deposition to MetaboLights (URL_TO_INSERT_RECORD_518 https://fairsharing.org/FAIRsharing.kkdpxe) , a public repository (URL_TO_INSERT_TERM_514 https://fairsharing.org/search?recordType=repository)  for metabolomics data recommended by several journal (URL_TO_INSERT_TERM_515 https://fairsharing.org/search?recordType=journal) s (https://doi.org/10.25504/FAIRsharing.kkdpxe).



## Reference
````{dropdown} **Reference**
Rocca-Serra, P., Sansone, S. Experiment design driven FAIRification of omics data matrices, an exemplar. Sci Data 6, 271 (2019) [doi:10.1038/s41597-019-0286-0](https://doi.org/10.1038/s41597-019-0286-0)
````

## Authors

````{authors_fairplus}
Philippe: Writing - Original Draft
Susanna: Writing - Review & Editing, Funding acquisition
````


## License

````{license_fairplus}
CC-BY-4.0
````
