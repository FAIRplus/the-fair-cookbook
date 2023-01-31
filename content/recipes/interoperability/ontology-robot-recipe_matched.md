(fcb-interop-ontorobot)=
# Building an application ontology with ROBOT


````{panels_fairplus}
:identifier_text: FCB023
:identifier_link: 'https://w3id.org/faircookbook/FCB023'
:difficulty_level: 4
:recipe_type: hands_on
:reading_time_minutes: 60
:intended_audience: terminology_manager, data_manager, data_scientist, ontologist
:maturity_level: 3
:maturity_indicator: 33
:has_executable_code: yeah
:recipe_name: Building an application ontology with ROBOT
```` 

## Main Objectives

> The main purpose of this recipe is building an application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  from source ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  using `RO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cp0ybc) BO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b) T` {footcite}`pmid31357927` via a sustainable dynamic pipeline to allow seamless integration of source ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  updates {footcite}`Arp2015`. 

An application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  is a semantic artefact which is developed (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.31385c)  to answer the needs of a specific application or focus. 
Thus, it may borrow terms from a number of reference ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) , which can be extremely large but whose broad coverage may not be required by the application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) . Yet, it is critical to keep the `application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) ` synchronized with the `reference ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) ` that imports are made from.  We aim to document how a certain level of automation can be achieved.

[ROBOT](http://robot.obolibrary.org/) is an open source tool for ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  development. It supports ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  editing, ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  annotation, ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)  conversion, and other functions. It runs on the Java Virtual Machine (JVM) and can be used through command line tools on Windows, macOS and Linux.


## Graphical Overview


````{dropdown} 
:open:
```{figure} ontology-robot-recipe.md-figure1.mmd.png
---
name: ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) -robot-recipe-figure1
alt: Building an ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  with Robot tool
---
Building an ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  with Robot tool.
```
````

---

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  and terminology](http://edamontology.org (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.a6r7zs) /topic_0089)  | [tsv,OWL (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.atygwy) ]|OWL (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.atygwy) |


## Table of Data Standards


| Data Format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
| [OWL](https://fairsharing.org (URL_TO_INSERT_RECORD https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD https://fairsharing.org/3538) /FAIRsharing.atygwy)  |   |   |
| [OBO](https://fairsharing.org (URL_TO_INSERT_RECORD https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD https://fairsharing.org/3538) /FAIRsharing.aa0eat)  |   |    |



---


## Ingredients


| Tool Name  |  Tool Location  | Tool function |
| :------------- | :------------- | :------------ |
| RO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cp0ybc) BO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b) T | [http://robot.obolibrary.org/](http://robot.obolibrary.org/) | ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  management cli |
| Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  development kit | [https://github.com (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.c55d5e) /INCATools/ontology-development-kit](https://github.com (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.c55d5e) /INCATools/ontology-development-kit) (comes with RO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cp0ybc) BO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b) T included)| ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  management environment |
| Protégé/other ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  editor | [https://protege.stanford.edu/](https://protege.stanford.edu/) | ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  editor |
| SP (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.87ccfd)  | [https://www.w3.org/TR/sparql11-query/](https://www.w3.org/TR/sparql11-query/) | ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  query language |
| ELK |[https://www.cs.ox.ac.uk/isg/tools/ELK/](https://www.cs.ox.ac.uk/isg/tools/ELK/)|ontology reasoner|
|Hermit|[http://www.hermit-reasoner.com/](http://www.hermit-reasoner.com/)|ontology reasoner|


## Step-by-step process

### Preliminary requirements

The development of an `application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) ` requires joint contributions from `domain experts`, `use case owners` and `ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  developers`. The domain expert provides essential domain knowledge. The use case owners defines the `competency questions` of the application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) . And the ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  developers are `IT specialists` working on the construction of the application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) .

### Step 1: Define the goal of the application ontology

The development of an `application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) ` is driven by specific use cases and target datasets. The first step in application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  development is to determine the subject and the aim of the application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) . 

In this recipe, we demonstrate the workflow of building an application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  for patient metadata and patient sequencing data investigations. `Competency questions` of this ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  are provided below:

<!-- [here](https://github.com (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/the-fair-cookbook/blob/ontology_robot_recipe/docs/content/recipes/ontology-robot/competency_questions.md).  -->



| **Theme**                                             | **Competency Questions**                                                                                                              |
|:------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------|
| **General Questions**                                 |                                                                                                                                       |
|                                                       | ➕ How to identify relevant public domain ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  suiting our needs?             |
|                                                       | ➕ How to establish an ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  covering all terms that are included in the actual data to be represented?
|                                                       | ➕ How to remove terms from the resulting ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  that are not needed?                                               |
|                                                       | ➕ How to guarantee consistency of the final ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) ?                                                                |
|                                                       | ➕ How to identify differences in comparison to a previous version of the resulting ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) ?                         |
| **Questions without specifying compounds or genes for the {download}`example dataset <./ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) -robot-recipe/ExternalStudiesKQ.xlsx>`**   |                                                                                                                                       |
|                                                       | ➕ Identify all data generated from tissues (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.yXPvpU)  taken from patients suffering from a specific disease.                                     |
|                                                       | ➕ Identify all data generated from a specific tissues (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.yXPvpU)  obtained from mouse model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) s that are related to a specific disease.              |
|                                                       | ➕ Identify all data generated from lung tissue taken from patients suffering from a lung disease that is not related to oncology.     |
|                                                       | ➕ Identify all data generated from primary cells whose origin is the lung.                                                            |
|                                                       | ➕ Identify all data generated from cell lines whose origin is the lung.                                                                |
| **Questions including single genes or gene sets**     |                                                                                                                                       |
|                                                       | ➕ What is the expression of PP (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.tghhc4) ARg / growths factors in lung tissue from IPF patients?                                                 |
|                                                       | ➕ What is the expression of PP (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.tghhc4) ARg / growths factors in primary cells obtained from lung tissue from healthy subjects?                 |
|                                                       | ➕ What is the expression of PP (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.tghhc4) ARg / growths factors in all available tissues (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.yXPvpU)  obtained from healthy subjects?                          |
| **Questions including compound or treatment informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion** |                                                                                                                                       |
|                                                       | ➕ Identify all data generated from primary cells treated with a kinase inhibitor.                                                     |
|                                                       | ➕ Identify all data from patients treated with a specific medication.                                                                 |
|                                                       | ➕ Identify all data generated from cells / cell lines that have been treated with compounds targeting a member of a specific pathway.  |
|                                                       | ➕ What is the expression of PP (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.tghhc4) ARg in lung tissue upon treatment with a specific compound in patients suffering from a specific disease |



_Table 1_ is a snapshot of the example dataset. The complete patient metadata example dataset is {download}`here <./ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) -robot-recipe/ExternalStudiesKQ.xlsx>`.



| Study                | source_id | sample_description  | tissue | source_tissue | cell                  | cellline | disease                       | gender | species      |
|----------------------|-----------|---------------------|--------|---------------|-----------------------|----------|-------------------------------|--------|--------------|
| GSE52463Nance2014    | EX08_001  | Lung - Normal       | Lung   |               |                       |          | Normal                        | male   | Homo sapiens |
| GSE52463Nance2014    | EX08_015  | Lung - IPF          | Lung   |               |                       |          | Idiopathic Pulmonary Fibrosis | male   | Homo sapiens |
| GSE116987March (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.52b22c) er2019 | EX101_1   | HSC CCl4-treated w0 |        |               | Hepatic Stellate Cell |          | NA                            |        | Mus musculus |

_Table 1: Patient metadata example_


### Step 2: Select terms from reference ontologies

#### Step 2.1 Select source ontologies

To build an `application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) ` that supports communication between different data resources, it is recommended to reuse existing (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.q7bkqr)  terms from existing (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.q7bkqr)  reference ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  instead of creating new terms.

>⚡ _Reference ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) :_ a semantic artifact with a canonical and comprehensive representation of the entities in a specific domain.
>
>⚡ _Source ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) :_ An ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  to be integrated into the application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) , usually a reference ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) . 

When selecting reference ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  as source ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) , the reusability and sustainability of the source ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  need to be considered. Many ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  in [the OBO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b)  foundry (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069) ](http://www.obofoundry.org (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069) /) use the [CC-BY](https://creativecommons.org/licenses/by/2.0/) licence, allowing sharing and adaptation. Such ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  can be directly used as source ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) . Reference ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  with similar umbrella structures can be conveniently combined in the application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) . The format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)  and maintenance of the reference ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  shall also be considered.

Specific use cases and requirements from the target dataset also affect the choice of source ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) . For use cases focusing on extracting data from heterogeneous datasets with complicated data types and data relationships, reference ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  with rich term relationships are preferred. The interpretation of each term also depends on the context and requirements of the target dataset. For example, _"hypertension"_ can be either interpreted as a _phenotype_ and map (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.31385c)  to phenotype ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) , or a _disease_ map (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.31385c)  to disease ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) .


The example dataset includes metadata related to disease, species, cell lines, tissues (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.yXPvpU)  and biological sex. _Table 2_ lists some reference ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  available in corresponding domains. In this recipe, we selected _MO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.qs4x5m) NDO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.b2979t) _ for disease domain, _UBERO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.nwgynk)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cp0ybc) N (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.4c0b6b) _ for anatomy, _NCBItaxon_ for species taxonomy and _PATO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.ayjdsm)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.w69t6r)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.ezwdhz) _ for biological sex. 


|Domain|Reference Ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) |
|----|----|
|Disease| [Mondo Disease Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.8b6wfq) , MONDO](http://www.obofoundry.org (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069) /ontology/mondo.html)<br> [Disease Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.8b6wfq) , DOID](https://disease-ontology.org/)<br> |
|Species|[NCBI organismal classification, NCBItaxon](http://www.obofoundry.org (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069) /ontology/ncbitaxon.html)|
|Cell line|[Cell Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.j9y503) , CL](http://www.obofoundry.org (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069) /ontology/cl.html)<br> [Cell Line Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.4dvtcz) , CL (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.j9y503) O (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.4dvtcz) ](http://www.obofoundry.org (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069) /ontology/clo.html)|
|Tissue|[NCI Thesaurus (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.4cvwxa)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.aqnss4)  OBO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b)  Edition, NCIT](http://www.obofoundry.org (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069) /ontology/ncit.html)<br> [Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  for MIRNA Target, OMIT](http://www.obofoundry.org (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069) /ontology/omit.html)<br> [Uberon multi-species anatomy ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) , UBERO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.nwgynk)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cp0ybc) N (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.4c0b6b) ](http://www.obofoundry.org (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069) /ontology/uberon.html)|
|Biological Sex|[Phenotype And Trait Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) , PATO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.ayjdsm)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.w69t6r)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.ezwdhz) ](http://www.obofoundry.org (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069) /ontology/pato.html)|

_Table 2: Available reference ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  in selected domains_ 


#### Step 2.2 Select seed ontology terms

> ⚡ _Seed ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  terms_: A set of entities extracted from reference ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  for the application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) .
> 

This step identifies the seeds needed to perform the knowledge extraction from external sources, i.e., the set of entities to extract in order to be integrated on the application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) . Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  Developer can provide the tools to ease and to scale the identification of the seeds. Domain experts can identify the right seeds for a given application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) .

Besides, the fact that is always possible to manually identify the set of seeds needed for the performing of the concept extraction, to have a helper tool allows to run the task at scale. Following, an automatable approach based on using widely known life sciences annotators  - [Zooma](https://www.ebi.ac.uk/spot/zooma/) and [NCBO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.y2dt83)  Annotator](https://bioportal.bioontology.org (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.4m97ah) /annotator) - are depicted.


````{dropdown} 
:open:
```{figure} ontology-robot-recipe.md-figure2.mmd.png
---
name: ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) -robot-recipe-figure2
alt: Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  seed term selection approaches.
---
Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  seed term selection approaches.
```
````


[ZOOMA](https://www.ebi.ac.uk/spot/zooma/) is a web service for discovering optimal ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.53edcc) pings, developed (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.31385c)  by the Samples, Phenotypes and Ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  Team at the [European Bioinformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ics Institute (EMB (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.a1rp4c) L-EBI)](https://www.ebi.ac.uk)
. It can be used to automatically annotate plain text about biological entities with ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  classes. Zooma allows to limit the sources used to perform the annotations. These sources are either curated data sources, or ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  from the [Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  Lookup Service (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.Mkl9RR)  (OLS)](https://www.ebi.ac.uk/ols/index (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.Mkl9RR) ). Zooma contains a linked data repository (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository)  of annotation knowledge and highly annotated data that has been fed with manually curated annotation derived from publicly available database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database) s. Because the source data has been curated by hand, it is a rich source of knowledge that is optimised for this task of semantic markup of keywords, in contrast with text-mining approaches.

The [NCBO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.y2dt83)  Annotator](https://bioportal.bioontology.org (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.4m97ah) /annotator) is an ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) -based web service that annotates public datasets with biomedical ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  concepts based on their textual metadata. It can be used to automatically tag data  with ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  concepts. These concepts come from the Unified Medical Language System (UMLS) Metathesaurus (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.aqnss4)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.aqnss4)  and the National Center for Biomedical Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  (NCBO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.y2dt83) ) BioPortal (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.4m97ah)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.4m97ah)  ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) .

Both the `Zooma` and `NCBO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.y2dt83)  Annotator service` provides a `web interface` and a `REST API` to identify the seed terms by annotation of free text. Two scripts able to automate the annotation of a set of free text terms are shown following.

#### Seed term extraction with ZOOMA

The following sample script uses the `Zooma web service` to get a list of seed terms - i.e., the URI (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.d261e1) s of ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  classes -. The service also states the level of confidence of every seed proposed.
```python
#Python3
#zooma-annotator-script.py file

def get_annotations(propertyType, propertyValues, filters = ""):
    """
    Get Zooma annotations for the values of a given property of a given type.
    """
    
    import requests
    
    annotations = []
    no_annotations = []

    for value in propertyValues:
        ploads = {'propertyValue': value,
                  'propertyType': propertyType,
                  'filter': filters}
        r = requests.get('http://www.ebi.ac.uk/spot/zooma/v2/api/services/annotate',
                         params=ploads)
            
        import json
        data = json.loads(r.text)
        
        if len(data) == 0:
            no_annotations.append(value)
        
        for item in data:
            annotations.append((f"{item['semanticTags'][0]} "
                                f"# {value}"
                                f"-Confidence:{item['confidence']}"))

    return annotations, no_annotations

if __name__ == "__main__":
    propertyType = 'gender'
    propertyValues = ['male', 'female', 'unknown']

    annotations, no_annotations = get_annotations(propertyType, propertyValues)

    from pprint import pprint
    pprint(annotations)
    pprint(no_annotations)
```
Running the above script to get the seeds for the terms `male`, `female`, and `unknown` generates the following results:
```python
['https://purl.obolibrary.org/obo/PATO_0000384 # male-Confidence:HIGH',
 'https://purl.obolibrary.org/obo/PATO_0000383 # female-Confidence:HIGH',
 'https://www.orpha.net/ORDO/Orphanet_288 # unknown-Confidence:MEDIUM',
 'https://www.ebi.ac.uk/efo/EFO_0003850 # unknown-Confidence:MEDIUM',
 'https://www.ebi.ac.uk/efo/EFO_0003952 # unknown-Confidence:MEDIUM',
 'https://www.ebi.ac.uk/efo/EFO_0009471 # unknown-Confidence:MEDIUM',
 'https://www.ebi.ac.uk/efo/EFO_0000203 # unknown-Confidence:MEDIUM',
 'https://www.ebi.ac.uk/efo/EFO_0003863 # unknown-Confidence:MEDIUM',
 'https://www.ebi.ac.uk/efo/EFO_0000616 # unknown-Confidence:MEDIUM',
 'https://purl.obolibrary.org/obo/HP_0000952 # unknown-Confidence:MEDIUM',
 'https://www.ebi.ac.uk/efo/EFO_0003853 # unknown-Confidence:MEDIUM',
 'https://www.ebi.ac.uk/efo/EFO_1001331 # unknown-Confidence:MEDIUM',
 'https://www.ebi.ac.uk/efo/EFO_0003769 # unknown-Confidence:MEDIUM',
 'https://purl.obolibrary.org/obo/HP_0000132 # unknown-Confidence:MEDIUM',
 'https://www.ebi.ac.uk/efo/EFO_0000408 # unknown-Confidence:MEDIUM',
 'https://www.ebi.ac.uk/efo/EFO_0008549 # unknown-Confidence:MEDIUM',
 'https://www.ebi.ac.uk/efo/EFO_0001642 # unknown-Confidence:MEDIUM']
[]
```
#### Seed term extraction with NCBO Annotator

The following sample script uses the NCBO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.y2dt83)  Annotator web service to get a list of seed terms - i.e., the URI (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.d261e1) s of ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  classes -.
```python
#Python3
#ncbo-annotator-script.py file

def get_annotations(propertyValues, ontologies = ''):
    """
    Get NCBO Annotations for the values of a given property.
    """
        
    import requests
    
    annotations = []
    no_annotations = []
    
    for value in propertyValues:
        ploads = {'apikey': '8b5b7825-538d-40e0-9e9e-5ab9274a9aeb',
                  'text': value,
                  'ontologies': ontologies,
                  'longest_only': 'true',
                  'exclude_numbers': 'false',
                  'whole_word_only': 'true',
                  'exclude_synonyms': 'false'}
        r = requests.get('https://data.bioontology.org/annotator', params=ploads)
        
        import json
        data = json.loads(r.text)
        
        if len(data) == 0:
            no_annotations.append(value)
        
        for item in data:
            annotations.append(f"{item['annotatedClass']['@id']} # {value}")

    return annotations, no_annotations

if __name__ == "__main__":
    propertyType = 'gender'
    propertyValues = ['male', 'female', 'unknown']

    annotations, no_annotations = get_annotations(propertyType, propertyValues)

    from pprint import pprint
    pprint(annotations)
    pprint(no_annotations)
```
Running the above script to get the seeds for the terms `male`, `female`, and `unknown` generates the following results:

```python
['http://purl.obolibrary.org/obo/UBERON_0003101 # male',
 'http://purl.obolibrary.org/obo/UBERON_0003100 # female']
['unknown']
```

#### Step 2.2.3 Seed term extraction with SPARQL 

Instead of manually maintaining a list of seed terms to generate a module, a term list can be generated on the fly using a `SP (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.87ccfd)  query`. Here, we generate a subset of `UBERO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.nwgynk)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cp0ybc) N (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.4c0b6b) ` terms which have a cross-reference to either `FMA (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.x56jsy)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.pdwqcr)  (for human anatomy)` or `MA (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.pdwqcr)  (for mouse anatomy)` terms, since our example datasets includes human, mouse and rat data.

```bash
PREFIX scdo: <http://scdontology.h3abionet.org/ontology/>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT ?uri WHERE {

{
 {
  ?uri oboInOwl:hasDbXref ?xref .
 }
UNION
 {
  ?axiom a owl:Axiom;
  	owl:annotatedSource ?uri;
        oboInOwl:hasDbXref ?xref .
 }
}

?uri a owl:Class

FILTER isLiteral(?xref)
FILTER regex( ?xref, "^FMA|^MA:", "i") 

}
```


### Step 3: Extract ontology modules from source ontologies

Module extractions from ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  can be run manually and in an ad hoc fashion. We would however recommend collecting all steps together into a script or `Makefile` to avoid missing steps. `RO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cp0ybc) BO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b) T` steps can in theory be chained together into single large commands. Practical experience however teaches that this can have unexpected consequences as well as making debugging difficult in the event of an issue. It is therefore advisable to split extractions and merges out into individual steps with intermediate artefacts which can be deleted at the end of the process chain.

#### Step 3.1 Get source ontology files

We recommend starting each (re)build of the application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  with the latest versions of the source ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  unless there is a good reason not to update to the latest version. Ideally, this should be done automatically, for example through a shell script that CURL (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.9d38e2) s all ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  from their source URI (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.d261e1) s, e.g.

```shell
curl -L http://purl.obolibrary.org/obo/uberon.owl > uberon.owl
```

#### Step 3.2 Choose ontology extraction algorithms

`RO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cp0ybc) BO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b) T` supports two types of ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  module extraction, `Syntactic Locality Module Extractor` (SLME) and `Minimum Informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion to Reference an External Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  Term` (MIREO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.w7a76x)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.d1zzym) T). `SLME` extractions can be further subdivided into TO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.w69t6r) P (URL_TO_INSERT_RECORD https://fairsharing.org/707)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.yvmb9y)  (top module), `BO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b) T` (bottom module) and `STAR` (fixpoint-nested module). For full details of what these different options entail, see http://robot.obolibrary.org/extract.html. We recommend the use of BO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b) T for comprehensive modules that preserve the links between ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  classes and the use of `MIREO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.w7a76x)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.d1zzym) T` if relationships apart from parent-child ones are less important. 


#### Step 3.3 Extract modules using seed terms

Using `robot` tool provided by the `OBO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b)  foundry (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069) `, the creation of a module can be done with one command:

```bash
robot extract --method <some_selection> \
    --input <some_input.owl> \
    --term-file <list_of_classes_of_interest_in_ontology.txt> \
    --intermediates <choose_from_option> \
    --output ./ontology_modules/extracted_module.owl
```
The `robot` extract command takes several arguments:

* *method*: `RO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cp0ybc) BO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b) T` uses 4 different algorithms to generate a module.  `TO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.w69t6r) P (URL_TO_INSERT_RECORD https://fairsharing.org/707)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.yvmb9y) `, `BO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b) T`, `STAR` (all from the SLME method), and `MIREO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.w7a76x)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.d1zzym) T`. The first two will create a module  below or above the seed classes (the classes of interest in the target ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) ) respectively. The `STAR` method creates a module by pulling all the properties and axioms of the seed classes but nothing else. `MIREO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.w7a76x)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.d1zzym) T` uses a different methods and offers some more options, in particular when it comes to how many levels up or down (parent and children) are needed.     
* *input*: this argument is to specify the target ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  you want to extract a module from. It can be the original artefact or a filtered version of it.
* *imports*: this argument allows specifying whether or not to include imported ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) . Note that the default is to do so using the value `include`. Choose `exclude` otherwise.
* *term-file*: the text file holding the list of classes of interested identified by their iri (e.g. http://purl.obolibrary.org/obo/UBERON_0001235 # adrenal cortex).
* *intermediates*: specific to the `MIREO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.w7a76x)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.d1zzym) T` method, it allows to let the algorithm know how much or how little to extract. It has 3 levels (`all`,`minimal`, `none`).
* *output*: the path to the owl file holding the results of the module extraction.
* *copy-ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) -annotations*: a boolean value true/false to pull or not any class annotation from the parent ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) . default is `false`
* *sources*: optional, a pointer to a file map (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.53edcc) ping .
* *annotate-with-source*: a boolean value true/false. Default is `false`.


The above query, saved under `select_anatomy_subset.sparql` can be used to generate a dynamic seed list, then do a `BO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b) T` extraction: 

```shell
robot query --input uberon.owl --query select_anatomy_subset.sparql uberon_seed_list.txt

robot extract --method BOT --input uberon.owl --term-file uberon_seed_list.txt -o uberon_subset.owl
```

#### Step 3.4 Assess extracted modules

The extracted ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  module should include all seed terms and represent the term relationships correctly. It should also preserve the correct hierarch (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.52b22c) ical structure of the source ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  and have consistent granularity.


### Step 4: Build the upper level umbrella ontology

The umbrella ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  is the root structure of the ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) . Building the umbrella ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  aims to model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)  the main entity of the use case and its relationships with the ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  classes extracted on the previous step. The main identity of the ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  and relationships with extracted modules can be identified by domain experts, or specified by the use case owner.

`RO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cp0ybc) BO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b) T` provides a template-driven ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  term generation system. A `RO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cp0ybc) BO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b) T template` is a `tab-separated values (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.a978c9) ` (TSV (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.a978c9) ) or `comma-separated values (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.1943d4) ` (CSV (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.1943d4) ) file that depicts a set of patterns to build ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  entities - i.e., classes, properties, and individuals -. These templates can be used for modular ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  development.
After the _Domain Expert_ and the _Use Case/Scenario Owner_ specify the main entity of the use case and its relationships with remaining ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  entities, the _Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  Developer_ generates the `RO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cp0ybc) BO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b) T` templates depicting the set of patterns aimed to build the _umbrella_ ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) .

A `RO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cp0ybc) BO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b) T` command using a template to build an ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  is shown below:

```bash
robot template --template template.csv \
    --prefix "r4: https://fairplus-project.eu/ontologies/R4/" \
    --ontology-iri "https://fairplus-project.eu/ontologies/R4/" \
    --output ./templates/umbrella.owl
```

And a template sample is presented following:


| ID | Label | Entity Type | Equivalent Axioms | Characteristic | Domain | Range | 
| -------- | -------- | -------- | -------- |-------- | -------- | -------- |
| ID     | LABEL (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.dp0jvd)      | TYPE (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.b403jy)      | EC % | CHARAC (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.md3e78) TERIS (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.efb730) TIC | DOMA (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.pdwqcr)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.g3j5qj) IN | RANGE |
|ex:cl_2 | Class_2 | class |-|-|-|-|
|ex:cl_3 | Class_3 | class |ex:cl_2|-|-|-|
|ex:op_1	|Prop_1| object property|-|Class_2|Class_3| |
|ex:dp_1	|Prop_2| data property|-|functional|Class_2|xsd:string (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.9b7wvk) |


```{admonition} Tip
:class: tip

⚡ The generated ontology can be visualized by using the [Protégé tool](https://protege.stanford.edu/) or local deployment of OLS. 
The {ref}`fcb-infra-localols` option is recommended by this recipe, given that `Protégé` may crash when loading medium or large size ontologies.
```
    
### Step 5: Merge ontology modules and umbrella ontology

Merging the ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  modules previously extracted and the umbrella ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  locally built produces a first draft of the application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) . 

The `merge` RO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cp0ybc) BO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b) T command allows combining two or more separate input ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  modules into a single ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) . Following, the `RO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cp0ybc) BO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b) T` command merging the umbrella ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  and the modules is shown:

```bash
java -jar robot.jar merge \
    --input ./ontology_modules/iao_mireot_robot_module_1.owl \
    --input ./ontology_modules/obi_mireot_robot_module_2.owl \
    --input ./ontology_modules/duo_mireot_robot_module_3.owl \
    --input ./templates/umbrella.owl \
    --output ./results/r4_app_ontology.owl
```

### Step 6: Post-merge modifications

#### Step 6.1: Materialize and Reasoning

Commands below infer superclasses and superclasses and reduce duplicated axioms merged term:

```bash
robot materialize \
--reasoner ELK  \
--input merged_owl  \
reduce \
--output materialized.owl 
```

The ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  materialization uses `OWL (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.atygwy)  reasoners`. `RO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cp0ybc) BO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b) T` provides [several ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  reasoners](http://robot.obolibrary.org/reason). 

It is also possible to identify issues in the ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  with some `quality control SP (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.87ccfd)  queries`. 

```bash
robot report --input edit.owl --output report.tsv
```


#### Step 6.2: Annotate

Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  annotation adds metadata to the owl file. It is recommended to provide `ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  IRIs`, `version IRIs`, `ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  title`, `descriptions` and `license` to support future usage and management. 

The annotation can be added either line-by-line or provided in a turtle (.ttl) file. 
```bash
#ANNOTATE
robot annotate --input materialized.owl \
  --ontology-iri "https://github.com/ontodev/robot/examples/annotated.owl" \
  --version-iri "https://github.com/ontodev/robot/examples/annotated-1.owl" \
  --annotation rdfs:comment "Comment" \
  --annotation rdfs:label "Label" \
  --annotation-file annotations.ttl \
  --output results/annotated.owl

```

Below is an example annotation file.

```bash
@prefix rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl:     <http://www.w3.org/2002/07/owl#> .
@prefix example: <https://github.com/ontodev/robot/examples/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
example:annotated.owl
  rdf:type owl:Ontology ;
  rdfs:comment "Comment from annotations.ttl file." .
  dcterms:title "Example title"
  dcterms:license <http://creativecommons.org/publicdomain/zero/1.0/>
  owl:versionIRI <https://github.com/ontodev/robot/examples/annotated-1.owl>
```

#### Step 6.3: Convert

Besides `OWL (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.atygwy)  format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) `, the `Open Biomedical Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  (OBO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b) ) format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ` is also widely used in life science related ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) . It is possible to convert an `.owl` file to `.obo` file using:

```bash
#CONVERT:
robot convert \
--input  annotated.owl\
--format obo \
--output results/annotated.obo
```

### Step 7: Assess coverage of the ontology scope

The final step of the ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  construction is to assess coverage of the ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  scope by verifying if it is able to answer the competency questions predefined. The competency questions can be implemented as a set of `SP (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.87ccfd)  queries` and run against the developed (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.31385c)  ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  to check if the answers/results are aligned with the scope of the ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) . The `use case owner` and `ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  developer` can also collaborate on the assessment of the competency questions answers/results. 

`RO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cp0ybc) BO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b) T` provides the `query` command to perform `SP (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.87ccfd)  queries`  against an ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  to verify and validate the ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) .

The query command runs SP (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.87ccfd)  `ASK`, `SELECT`, and `CO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.thskvr) NS (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.rfec93) TR (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.18je7e) UCT` queries by using the `--query` option with two arguments: `a query file` and `an output file`. Instead of specifying one or more pairs (query file, output file), it is also possible to specify a single `--output-dir` and use the `--queries` option to provide one or more queries of any type. Each output file will be written to the output directory with the same base name as the query file that produced it. A pattern example of this command is shown as follows.

```bash
robot query --input <input_ontology_file> \
    --queries <query_file> \
    --output-dir <path_to_results> results/
```


## Conclusions

Creation an application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  and semantic model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)  to support knowledge discovery is an important process in the data management life cycle. 
This more advanced recipe has identified and described all the different steps that one needs to consider building such a resource.
While this is important, one should bear in mind the costs associated with maintaining those artefacts and keeping them up to date.
It is therefore also critical to understand the benefits of contributing to existing (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.q7bkqr)  open efforts.    

### What to read next?

* OBO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b)  Foundry (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.847069)  Semantic Engineering training and the [Robot tutorial](https://oboacademy.github.io/obook/tutorial/robot-tutorial-1/) 
* {ref}`fcb-interop-metadataprofile`  <!-- How to establish a minimal metadata profile? --> <!-- TO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.w69t6r) DO add a link to corresponding document -->
* {ref}`fcb-interop-ontorequest` <!-- How to submit/request terms to an ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  ?--> <!-- TO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.w69t6r) DO add a link to corresponding document -->

````{rdmkit_panel}
````



## References
````{dropdown} **References**
```{footbibliography}
```
````

<!-- ```{bibliography} ../../../_bibliography/bibliography-identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) -map (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.53edcc) ping.bib
:filter: docname in docnames
``` -->


<!-- - R.C. Jackson, J.P. Balhoff, E. Douglass, N.L. Harris, C.J. Mungall, and J.A. Overton. [_ROBOT: A tool for automating ontology workflows_](https://link.springer.com/epdf/10.1186/s12859-019-3002-3?author_access_token=bB8BLjFWrdh42vR6DjT-nG_BpE1tBhCbnbw3BuzI2RPCZ2BK7EeexaCNYfT-cCz8Q_mrZomT2_svoQf12CW661Sagzw6JGF9DhJq3Q3fTPdMGFMtais7MRgx8-kDhp6uC9g2qcVh5FumTsveV22XVQ%3D%3D). BMC Bioinformatics, vol. 20, July 2019
- Arp, Robert, Barry Smith, and Andrew D. Spear. _Building ontologies with basic formal ontology_. Mit Press, 2015. -->


## Supplementary material
````{dropdown} **Supplementary material**
- {download}`Example Dataset <./ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) -robot-recipe/ExternalStudiesKQ.xlsx>`
- [Competency questions](ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) -robot-recipe/competency-questions.md)
- [IPython Notebook (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.cbz72b)  for the MSIO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.dpkb5f)  Build Process](ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) -robot-recipe/MSIO (URL_TO_INSERT_RECORD https://fairsharing.org/FAIRsharing.dpkb5f) -robot-build-process.ipynb)
````


## Authors

````{authors_fairplus}
Danielle: Writing - Original Draft, Code
Karsten: Writing - Original Draft
Philippe: Writing - Review & Editing, Conceptualization
Fuqi: Writing - Original Draft, Writing - Review & Editing
Emiliano: Writing - Review & Editing
````


## License
````{license_fairplus}
CC-BY-4.0
````
