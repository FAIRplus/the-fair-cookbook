# Table of Contents
1. [Main FAIRification Objectives](#Main%20FAIRification%20Objectives)
2. [Graphical Overview of the FAIRification Recipe Objectives](#Graphical%20Overview%20of%20the%20FAIRification%20Recipe%20Objectives)
3. [FAIRification Objectives, Inputs and Outputs](#FAIRification%20Objectives,%20Inputs%20and%20Outputs)
4. [Capability & Maturity Table](#Capability%20&%20Maturity%20Table)
5. [Table of Data Standards](#Table%20of%20Data%20Standards)
6. [Executable Code in Notebook](#Executable%20Code%20in%20Notebook)
7. [How to create workflow figures](#How%20to%20create%20workflow%20figures)
8. [License](#License)

---

## Main Objectives

The main purpose of this recipe is:

> Building an **application ontology** from source ontologies using ROBOT via a sustainable dynamic pipeline to allow seamless integration of source ontology updates. An **application ontology** is a semantic artefact which is developed to answer the needs of a specific application or focus. Thus it may borrow terms from a number of reference ontologies, which can be extremely large but whose broad coverage may not be required by the application ontology. Yet, it is critical to keep the application ontology synchronized with the reference ontologies imports are made from.  We aim to document how a certain level of automation can be achieved

## Graphical Overview of the FAIRification Recipe Objectives

<!-- TO DO: REVIEW-->

<div class="mermaid">
graph TD
  I1(fa:fa-university ontology source 1):::box -->|extract| M1(fa:fa-cube ontology module 1):::box
  I2(fa:fa-university ontology source 2):::box -->|extract| M2(fa:fa-cube ontology module 2):::box
  I3(fa:fa-university ontology source 3):::box -->|extract| M3(fa:fa-cube ontology module 3):::box
  M1 --> |merge| R1(fa:fa-cubes core):::box
  M2 --> |merge| R1(fa:fa-cubes core)
  M3 --> |merge| R1(fa:fa-cubes core)
  R1(fa:fa-cubes core) --> |materialize| R2(fa:fa-cubes reasoned & reduced core):::box

  R2(fa:fa-cubes reasoned & reduced core) -->|report| R3(fa:fa-tasks report):::box
  R2(fa:fa-cubes reasoned & reduced core) --> |edit| R4(fa:fa-cubes reasoned & reduced core):::box
  R3 -->|edit| R4
  R4 -->|annotate| R5(fa:fa-cubes fa:fa-tags fa:fa-cc annotated,reasoned,reduced core):::box
  R5 -->|convert| R6(fa:fa-star-o obo version):::box
  R5 -->|convert| R7(fa:fa-star owl version):::box
  R5 -->|export| R8(fa:fa-list xlsx view):::box

  linkStyle 0,1,2,3,4,5,6,7,8,9,10,11,12,13 stroke:#2a9fc9,stroke-width:1px,color:#2a9fc9,font-family:avenir;
  classDef box font-family:avenir,font-size:14px,fill:#2a9fc9,stroke:#222,color:#fff,stroke-width:1px
</div>

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgSTEoZmE6ZmEtdW5pdmVyc2l0eSBvbnRvbG9neSBzb3VyY2UgMSk6Ojpib3ggLS0-fGV4dHJhY3R8IE0xKGZhOmZhLWN1YmUgb250b2xvZ3kgbW9kdWxlIDEpOjo6Ym94XG4gIEkyKGZhOmZhLXVuaXZlcnNpdHkgb250b2xvZ3kgc291cmNlIDIpOjo6Ym94IC0tPnxleHRyYWN0fCBNMihmYTpmYS1jdWJlIG9udG9sb2d5IG1vZHVsZSAyKTo6OmJveFxuICBJMyhmYTpmYS11bml2ZXJzaXR5IG9udG9sb2d5IHNvdXJjZSAzKTo6OmJveCAtLT58ZXh0cmFjdHwgTTMoZmE6ZmEtY3ViZSBvbnRvbG9neSBtb2R1bGUgMyk6Ojpib3hcbiAgTTEgLS0-IHxtZXJnZXwgUjEoZmE6ZmEtY3ViZXMgY29yZSk6Ojpib3hcbiAgTTIgLS0-IHxtZXJnZXwgUjEoZmE6ZmEtY3ViZXMgY29yZSlcbiAgTTMgLS0-IHxtZXJnZXwgUjEoZmE6ZmEtY3ViZXMgY29yZSlcbiAgUjEoZmE6ZmEtY3ViZXMgY29yZSkgLS0-IHxtYXRlcmlhbGl6ZXwgUjIoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpOjo6Ym94XG5cbiAgUjIoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpIC0tPnxyZXBvcnR8IFIzKGZhOmZhLXRhc2tzIHJlcG9ydCk6Ojpib3hcbiAgUjIoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpIC0tPiB8ZWRpdHwgUjQoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpOjo6Ym94XG4gIFIzIC0tPnxlZGl0fCBSNFxuICBSNCAtLT58YW5ub3RhdGV8IFI1KGZhOmZhLWN1YmVzIGZhOmZhLXRhZ3MgZmE6ZmEtY2MgYW5ub3RhdGVkLHJlYXNvbmVkLHJlZHVjZWQgY29yZSk6Ojpib3hcbiAgUjUgLS0-fGNvbnZlcnR8IFI2KGZhOmZhLXN0YXItbyBvYm8gdmVyc2lvbik6Ojpib3hcbiAgUjUgLS0-fGNvbnZlcnR8IFI3KGZhOmZhLXN0YXIgb3dsIHZlcnNpb24pOjo6Ym94XG4gIFI1IC0tPnxleHBvcnR8IFI4KGZhOmZhLWxpc3QgeGxzeCB2aWV3KTo6OmJveFxuXG4gIGxpbmtTdHlsZSAwLDEsMiwzLDQsNSw2LDcsOCw5LDEwLDExLDEyLDEzIHN0cm9rZTojMmE5ZmM5LHN0cm9rZS13aWR0aDoxcHgsY29sb3I6IzJhOWZjOSxmb250LWZhbWlseTphdmVuaXI7XG4gIGNsYXNzRGVmIGJveCBmb250LWZhbWlseTphdmVuaXIsZm9udC1zaXplOjE0cHgsZmlsbDojMmE5ZmM5LHN0cm9rZTojMjIyLGNvbG9yOiNmZmYsc3Ryb2tlLXdpZHRoOjFweFxuXHRcdCIsIm1lcm1haWQiOnsidGhlbWUiOiJuZXV0cmFsIn0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiAgSTEoZmE6ZmEtdW5pdmVyc2l0eSBvbnRvbG9neSBzb3VyY2UgMSk6Ojpib3ggLS0-fGV4dHJhY3R8IE0xKGZhOmZhLWN1YmUgb250b2xvZ3kgbW9kdWxlIDEpOjo6Ym94XG4gIEkyKGZhOmZhLXVuaXZlcnNpdHkgb250b2xvZ3kgc291cmNlIDIpOjo6Ym94IC0tPnxleHRyYWN0fCBNMihmYTpmYS1jdWJlIG9udG9sb2d5IG1vZHVsZSAyKTo6OmJveFxuICBJMyhmYTpmYS11bml2ZXJzaXR5IG9udG9sb2d5IHNvdXJjZSAzKTo6OmJveCAtLT58ZXh0cmFjdHwgTTMoZmE6ZmEtY3ViZSBvbnRvbG9neSBtb2R1bGUgMyk6Ojpib3hcbiAgTTEgLS0-IHxtZXJnZXwgUjEoZmE6ZmEtY3ViZXMgY29yZSk6Ojpib3hcbiAgTTIgLS0-IHxtZXJnZXwgUjEoZmE6ZmEtY3ViZXMgY29yZSlcbiAgTTMgLS0-IHxtZXJnZXwgUjEoZmE6ZmEtY3ViZXMgY29yZSlcbiAgUjEoZmE6ZmEtY3ViZXMgY29yZSkgLS0-IHxtYXRlcmlhbGl6ZXwgUjIoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpOjo6Ym94XG5cbiAgUjIoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpIC0tPnxyZXBvcnR8IFIzKGZhOmZhLXRhc2tzIHJlcG9ydCk6Ojpib3hcbiAgUjIoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpIC0tPiB8ZWRpdHwgUjQoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpOjo6Ym94XG4gIFIzIC0tPnxlZGl0fCBSNFxuICBSNCAtLT58YW5ub3RhdGV8IFI1KGZhOmZhLWN1YmVzIGZhOmZhLXRhZ3MgZmE6ZmEtY2MgYW5ub3RhdGVkLHJlYXNvbmVkLHJlZHVjZWQgY29yZSk6Ojpib3hcbiAgUjUgLS0-fGNvbnZlcnR8IFI2KGZhOmZhLXN0YXItbyBvYm8gdmVyc2lvbik6Ojpib3hcbiAgUjUgLS0-fGNvbnZlcnR8IFI3KGZhOmZhLXN0YXIgb3dsIHZlcnNpb24pOjo6Ym94XG4gIFI1IC0tPnxleHBvcnR8IFI4KGZhOmZhLWxpc3QgeGxzeCB2aWV3KTo6OmJveFxuXG4gIGxpbmtTdHlsZSAwLDEsMiwzLDQsNSw2LDcsOCw5LDEwLDExLDEyLDEzIHN0cm9rZTojMmE5ZmM5LHN0cm9rZS13aWR0aDoxcHgsY29sb3I6IzJhOWZjOSxmb250LWZhbWlseTphdmVuaXI7XG4gIGNsYXNzRGVmIGJveCBmb250LWZhbWlseTphdmVuaXIsZm9udC1zaXplOjE0cHgsZmlsbDojMmE5ZmM5LHN0cm9rZTojMjIyLGNvbG9yOiNmZmYsc3Ryb2tlLXdpZHRoOjFweFxuXHRcdCIsIm1lcm1haWQiOnsidGhlbWUiOiJuZXV0cmFsIn0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

<!--
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgSTEoZmE6ZmEtdW5pdmVyc2l0eSBvbnRvbG9neSBzb3VyY2UgMSkgLS0-fGV4dHJhY3R8IE0xKGZhOmZhLWN1YmUgb250b2xvZ3kgbW9kdWxlIDEpXG4gIEkyKGZhOmZhLXVuaXZlcnNpdHkgb250b2xvZ3kgc291cmNlIDIpIC0tPnxleHRyYWN0fCBNMihmYTpmYS1jdWJlIG9udG9sb2d5IG1vZHVsZSAyKVxuICBJMyhmYTpmYS11bml2ZXJzaXR5IG9udG9sb2d5IHNvdXJjZSAzKSAtLT58ZXh0cmFjdHwgTTMoZmE6ZmEtY3ViZSBvbnRvbG9neSBtb2R1bGUgMylcbiAgTTEgLS0-IHxtZXJnZXwgUjEoZmE6ZmEtY3ViZXMgY29yZSlcbiAgTTIgLS0-IHxtZXJnZXwgUjEoZmE6ZmEtY3ViZXMgY29yZSlcbiAgTTMgLS0-IHxtZXJnZXwgUjEoZmE6ZmEtY3ViZXMgY29yZSlcbiAgUjEoZmE6ZmEtY3ViZXMgY29yZSkgLS0-IHxtYXRlcmlhbGl6ZXwgUjIoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpXG5cbiAgUjIoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpIC0tPnxyZXBvcnR8IFIzKGZhOmZhLXRhc2tzIHJlcG9ydClcbiAgUjIoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpIC0tPiB8ZWRpdHwgUjQoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpXG4gIFIzIC0tPnxlZGl0fCBSNFxuICBSNCAtLT58YW5ub3RhdGV8IFI1KGZhOmZhLWN1YmVzIGZhOmZhLXRhZ3MgZmE6ZmEtY2MgYW5ub3RhdGVkLHJlYXNvbmVkLHJlZHVjZWQgY29yZSlcbiAgUjUgLS0-fGNvbnZlcnR8IFI2KGZhOmZhLXN0YXItbyBvYm8gdmVyc2lvbilcbiAgUjUgLS0-fGNvbnZlcnR8IFI3KGZhOmZhLXN0YXIgb3dsIHZlcnNpb24pXG4gIFI1IC0tPnxleHBvcnR8IFI4KGZhOmZhLWxpc3QgeGxzeCB2aWV3KVxuXG5cdFx0IiwibWVybWFpZCI6eyJ0aGVtZSI6Im5ldXRyYWwifX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiAgSTEoZmE6ZmEtdW5pdmVyc2l0eSBvbnRvbG9neSBzb3VyY2UgMSkgLS0-fGV4dHJhY3R8IE0xKGZhOmZhLWN1YmUgb250b2xvZ3kgbW9kdWxlIDEpXG4gIEkyKGZhOmZhLXVuaXZlcnNpdHkgb250b2xvZ3kgc291cmNlIDIpIC0tPnxleHRyYWN0fCBNMihmYTpmYS1jdWJlIG9udG9sb2d5IG1vZHVsZSAyKVxuICBJMyhmYTpmYS11bml2ZXJzaXR5IG9udG9sb2d5IHNvdXJjZSAzKSAtLT58ZXh0cmFjdHwgTTMoZmE6ZmEtY3ViZSBvbnRvbG9neSBtb2R1bGUgMylcbiAgTTEgLS0-IHxtZXJnZXwgUjEoZmE6ZmEtY3ViZXMgY29yZSlcbiAgTTIgLS0-IHxtZXJnZXwgUjEoZmE6ZmEtY3ViZXMgY29yZSlcbiAgTTMgLS0-IHxtZXJnZXwgUjEoZmE6ZmEtY3ViZXMgY29yZSlcbiAgUjEoZmE6ZmEtY3ViZXMgY29yZSkgLS0-IHxtYXRlcmlhbGl6ZXwgUjIoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpXG5cbiAgUjIoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpIC0tPnxyZXBvcnR8IFIzKGZhOmZhLXRhc2tzIHJlcG9ydClcbiAgUjIoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpIC0tPiB8ZWRpdHwgUjQoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpXG4gIFIzIC0tPnxlZGl0fCBSNFxuICBSNCAtLT58YW5ub3RhdGV8IFI1KGZhOmZhLWN1YmVzIGZhOmZhLXRhZ3MgZmE6ZmEtY2MgYW5ub3RhdGVkLHJlYXNvbmVkLHJlZHVjZWQgY29yZSlcbiAgUjUgLS0-fGNvbnZlcnR8IFI2KGZhOmZhLXN0YXItbyBvYm8gdmVyc2lvbilcbiAgUjUgLS0-fGNvbnZlcnR8IFI3KGZhOmZhLXN0YXIgb3dsIHZlcnNpb24pXG4gIFI1IC0tPnxleHBvcnR8IFI4KGZhOmZhLWxpc3QgeGxzeCB2aWV3KVxuXG5cdFx0IiwibWVybWFpZCI6eyJ0aGVtZSI6Im5ldXRyYWwifX0)
-->
## Capability & Maturity Table

<!-- TO DO -->

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Interoperability | minimal | repeatable |

----

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [ontology building](http://edamontology.org/operation_XXXX)  | [tsv,OWL]|OWL|


## Table of Data Standards

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| [OWL](https://fairsharing.org/FAIRsharing.atygwy)  |   |   |
| [OBO](https://fairsharing.org/FAIRsharing.aa0eat)  |   |   |

___


### Competency questions

General Questions

- How to identify relevant public domain ontologies suiting our needs? (Might be out of scope for ROBOT)
- How to establish an ontology covering all terms that are included in the actual data to be represented?
- How to merge the internal ontology with publicly available ontologies?
- How to remove terms from the resulting ontology that are not needed?
- How to guarantee consistency of the final ontology?
- How to identify differences in comparison to a previous version of the resulting ontology?

Questions without specifying compounds or genes

- Identify all data generated from tissues taken from patients suffering from a specific disease.
- Identify all data generated from a specific tissues obtained from mouse models that are related to a specific disease.
- Identify all data generated from lung tissue taken from patients suffering from a lung disease that is not related to oncology.
- Identify all data generated from primary cells whose origin is the lung.
- Identify all data generated from celllines whose origin is the lung.

Questions including single genes or gene sets

- What is the expression of PPARg / growths factors in lung tissue from IPF patients?
- What is the expression of PPARg / growths factors in primary cells obtained from lung tissue from healthy subjects?
- What is the expression of PPARg / growths factors in all available tissues obtained from healthy subjects? 

Questions including compound or treatment information

- Identify all data generated from primary cells treated with a kinase inhibitor.
- Identify all data from patients treated with a specific medication.
- Identify all data generated from cells / cell lines that have been treated with compounds targeting a member of a specific pathway.
- What is the expression of PPARg in lung tissue upon treatment with a specific compound in patients suffering from a specific diseas
___

## Ingredients

| Tool Name  |  Tool Location  | Tool function |
| :------------- | :------------- | :------------ |
| ROBOT | [http://robot.obolibrary.org/](http://robot.obolibrary.org/) | ontology management cli |
| Ontology development kit | [https://github.com/INCATools/ontology-development-kit](https://github.com/INCATools/ontology-development-kit) (comes with ROBOT included)| ontology management environment |
| Protégé/other ontology editor | [https://protege.stanford.edu/](https://protege.stanford.edu/) | ontology editor |
| SPARQL | [https://www.w3.org/TR/sparql11-query/](https://www.w3.org/TR/sparql11-query/) | ontology query language |
| ELK |[https://www.cs.ox.ac.uk/isg/tools/ELK/](https://www.cs.ox.ac.uk/isg/tools/ELK/)|ontology reasoner|
|Hermit|[http://www.hermit-reasoner.com/](http://www.hermit-reasoner.com/)|ontology reasoner|


## Step by step process
### Step 1: Define the scope of the application ontology

The development of application ontology is driven by the target data and use cases. The first step in building an application ontology is to identify the scope of the ontology, including which domain it covers, which use case it targets, which data set it could be applied and which terms it includes.

In this recipe, we use example patient metadata to demonstrate how to build an application ontology for modelling patient metadata variables to support patient sequencing data investigation. The target domain of this ontology includes disease, taxonomy, tissue, cell line, and biological sex. Table 1 is a snapshot of the example dataset. The complete patient metadata example dataset is [here](https://github.com/FAIRplus/the-fair-cookbook/blob/ontology_robot_recipe/docs/content/recipes/ontology-robot/ExternalStudiesKQ.xlsx).

>Table 1: Example patient metadata. 
>
>| Study                | source_id | sample_description  | tissue | source_tissue | cell                  | cellline | disease                       | gender | species      |
>|----------------------|-----------|---------------------|--------|---------------|-----------------------|----------|-------------------------------|--------|--------------|
>| GSE52463Nance2014    | EX08_001  | Lung - Normal       | Lung   |               |                       |          | Normal                        | male   | Homo sapiens |
>| GSE52463Nance2014    | EX08_015  | Lung - IPF          | Lung   |               |                       |          | Idiopathic Pulmonary Fibrosis | male   | Homo sapiens |
>| GSE116987Marcher2019 | EX101_1   | HSC CCl4-treated w0 |        |               | Hepatic Stellate Cell |          | NA                            |        | Mus musculus |


### Step 2: Select appropriate source ontologies & branches

#### Step 2.1 Select source ontologies

Reusing ontology terms from source ontologies captures the most accurate and complete term definition and term relationships, avoids redundancy across ontologies, and makes the application ontology more maintainable and evolvable. It's recommended to reuse existing ontology terms, instead of creating new ontology terms.

Source ontology selection considers source ontology properties, application ontology use cases, and the target dataset. For source ontology properties, the first thing to check is the licence. For example, many ontologies in [the OBO foundary](http://www.obofoundry.org/) use [CC-BY](https://creativecommons.org/licenses/by/2.0/) licence, allowing sharing and adaptation, even commercially. Such ontologies can be used directly. Also, source ontologies with similar umbrella structure can be conviniently combined together in the application ontology. Maintainance, format and update frequency of the source ontology shall also be consideded. In terms of application ontology use cases, 

>The scope of ontology (hyper-tension in HP and DOID), the coverage of corrent dataset. whether the ontology 

>For specific use cases, for example, if use case is able finding data using multiple-domain keywords, they better ontology 
includes both the property of the source ontology and how it matches the target dataset.  To select proper source ontology, several factors need to be considered. Firstly, the ontology license need to be checked. Most ontologies in the OBO foundry uses [CC-BY] license allowing sharing and adaptation even commercially. Secondly, since application ontologies covers multiple domains, to make it easier to combine branches in different ontologies, it is recommended to choose source ontologies with similar umbrella ontology terms. Thirdly, for specific domains, e.g. disease domain, the source ontology should cover terms in the data set as much as possible to ensure the consistency between term relationships and link all data together. Also, the format and style of the source ontology, the update frequency/maintainance of the source term ontology. Depending on the use case, the best source ontology varies.

>The example dataset covers disease, species, cell line, tissue and biological sex. Ther are many reference ontologies covering the domain. Table 2 lists some source ontology available in selected domains. 
> Table 2: Available source ontologies in selected domains 
>
>|Domain|Example source Ontologies|
>|----|----|
>|Disease| [Mondo Disease Ontology, MONDO](http://www.obofoundry.org/ontology/mondo.html)<br> [Disease Ontology, DIOD](https://disease-ontology.org/)<br> |
>|Species|[NCBI organismal classification, NCBItaxon](http://www.obofoundry.org/ontology/ncbitaxon.html)|
>|Cell line|[Cell Ontology, CL](http://www.obofoundry.org/ontology/cl.html)<br> [Cell Line Ontology, CLO](http://www.obofoundry.org/ontology/clo.html)|
>|Tissue|[NCI Thesaurus OBO Edition, NCIT](http://www.obofoundry.org/ontology/ncit.html)<br> [Ontology for MIRNA Target, OMIT](http://www.obofoundry.org/ontology/omit.html)<br> [Uberon multi-species anatomy ontology, UBERON](http://www.obofoundry.org/ontology/uberon.html)|
>|[Biological Sex]|[Phenotype And Trait Ontology, PATO](http://www.obofoundry.org/ontology/pato.html)|

>In this recipe we choose MONDO, CL, UBRERON to demonstrate the ontology branch extraction selection. The best source ontology selection depending on the dataset and the use cases. 

#### Step 2.2 Select seed ontology terms

- why do i need to select a subset of the source ontology. what is ontology seed and ontology brach

- What is seed terms. 
- How to select: ontology term search + manual selection
    - Tools: ZOOMA（maybe pros and cons using zooma) , BioPortal Annotator, OLS, others.
    - SPARQL?
    - An example with ZOOMA?
- Rules in seed terms selection
    - include the domain title, e.g. "tissue", "disease", etc.
    - stick to one reference ontology if possible
    - if term doesnt exist, solutions: new term request > use terms other reference ontology > create your own term
    - Coverage. Should cover all terms.

### Step 2: Build the upper level "umbrella" ontology 

tools: protege/other ontology editor
considerations: ontology base URI/namespace


### Step 3: Extract ontology modules from source ontologies

#### Preliminary considerations

Module extractions from ontologies can be run manually and in an ad hoc fashion. We would however recommend to collect all steps together into a script or Make file to avoid missing steps. ROBOT steps can in theory be chained together into single large commands. Practical experience however teaches that this can have unexpected consequences as well as making debugging difficult in the event of an issue. It is therefore advisable to split extractions and merges out into individual steps with intermediate artefacts which can be deleted at the end of the process chain.

We recommend starting each (re)build of the application ontology with the latest versions of the source ontologies unless there is a good reason not to update to the latest version. Ideally, this should be done automatically, for example through a shell script that CURLs all ontologies from their source URIs, e.g.

```shell script
curl -L http://purl.obolibrary.org/obo/uberon.owl > uberon.owl
```

#### Extraction types 

ROBOT supports two types of ontology module extraction, Syntactic Locality Module Extractor (SLME) and Minimum Information to Reference an External Ontology Term (MIREOT). SLME extractions can be further subdivided into TOP (top module), BOT (bottom module) and STAR (fixpoint-nested module). For full details of what these different options entail, see http://robot.obolibrary.org/extract.html. We recommend the use of BOT for comprehensive modules that preserve the links between ontology classes and the use of MIREOT if relationships apart from parent-child ones are less important. 

:pencil:__WIP__ We used MIREOT to extract species in NCBITaxon, cell types in CL, and sex in PATO. For disease term, we used BOT to extract terms in MONDO. (as one of MONDO's features is the term hierarchy.) It's also possible to important the complete ontology if ???.


#### Module extraction - using manual text lists

Using `robot` tool provided by the `OBO foundry`, the creation of a module can be done with one command:

```
robot extract --method <some_selection> --input <some_input.owl>\ 
              --term-file <list_of_classes_of_interest_in_ontology.txt \
              --intermediates <choose_from_option>
              --output results/extracted_module.owl
```
`robot` extract command takes several arguments:

* *method*: `robot` uses 4 different algorithms to generate a module.  TOP, BOT, STAR (all from the SLME method), and MIREOT. The first two will create a module  below or above the seed classes (the classes of interest in the target ontology) respectively. The STAR method creates a module by pulling all the properties and axioms of the seed classes but nothing else. MIREOT uses a different methods and offers some more options, in particular when it comes to how many levels up or down (parent and children) are needed.     
* *input*: this argument is to specify the target ontology you want to extract a module from. It can be the original artefact or a filtered version of it.
* *imports*: this argument allows to specific whether or not to include imported ontologies. Note that the default is to do so using the value `include`. Choose `exclude` otherwise.
* *term-file*: the text file holding the list of classes of interested identified by their iri (e.g. http://purl.obolibrary.org/obo/UBERON_0001235 # adrenal cortex)
* *intermediates*: specific to the `MIREOT` method, it allows to let the algorithm know how much or how little to extract. It has 3 levels (`all`,`minimal`, `none`).
* *output*: the path to the owl file holding the results of the module extraction
* *copy-ontology-annotations*: a boolean value true/false to pull or not any class annotation from the parent ontology. default is `false`
* *sources*: optional, a pointer to a file mapping 
* *annotate-with-source*: a boolean value true/false. default is `false`



#### Module extraction - using SPARQL

Instead of manually maintaining a list of seed terms to generate a module, a term list can be generated on the fly using a SPARQL query. Here, we generate a subset of UBERON terms which have a crossreference to either FMA or MA terms.

```sql
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

The above query, saved under `select_anatomy_subset.sparql` can be used to generate a dynamic seed list, then do a BOT extraction: 

```shell script
uberon_seed_list.txt: $(UBERON_WHOLE)
	$(ROBOT) query --input $(UBERON_WHOLE) --query select_anatomy_subset.sparql uberon_seed_list.txt


uberon_subset.owl: uberon_seed_list.txt
	$(ROBOT) extract --method BOT --input $(UBERON_WHOLE) --term-file $< -o $@

```

#### Evaluation and validation of extracted branches

? For example by comparing different outcomes of MIREOT, BOT
? how to manually check it is a good branch

### Step 3/4 ? : How to creat your own term [is this section necessary?]
Always consider reusing existing terms first.
If have to create a term, use portege. 
How to give it a proper identifier.
    EFO identifier generator tool?


### Step 4: Merge extracted modules under the umbrella

```
#MERGING:
java -jar robot.jar merge \
--input ./ontology-module/iao_mireot_robot-module.owl \
--input ./ontology-module/obi_mireot_robot-module.owl \
--input ./ontology-module/duo-mireot-robot-module.owl \
--input ./ontology-module/chmo_mireot_module.owl \
--input ./ontology-module/uo-mireot-robot-module.owl \
--input ./ontology-module/psims-mireot-robot-module.owl \
--input ./ontology-module/chebi_mireot_no-inter-new-upper-module.owl \
--output ./results/msio-test-merge.owl
```


### Step 5: Post-merge modifications

#### Step 5.0 Add term relationships

- why do we need term relationships.
- where to get term relationships: borrow existing relationships in reference ontologies(e.g. MONDO, DIOD) or EFO; manually linking by domain expert
- How to import relationship
    WEBOLOUS. ROBOT spreadsheet to OWL.
- how to make sure the relationship is consistent.
- Example

#### Step 5.1: reasoninng and removing extraneous classes
Q: how to choose a proper reasoner?

```
#MATERIALIZE:
java -jar robot.jar materialize \
--reasoner ELK  \
--input ./results/msio-test-merge.owl  \
reduce \
--output ./materialize/msio-test-materialize.owl 
```


#### Step 5.2: Annotate

At minimum, this step is necessary to specify version

```
#ANNOTATE
robot annotate --input edit.owl \
  --ontology-iri "https://github.com/ontodev/robot/examples/annotated.owl" \
  --version-iri "https://github.com/ontodev/robot/examples/annotated-1.owl" \
  --annotation rdfs:comment "Comment" \
  --annotation rdfs:label "Label" \
  --annotation-file annotations.ttl \
  --output results/annotated.owl

```

#### Step 5.3: Convert

Ontologies may be distributed in a variety of format. The following command shows how to convert an `owl` file to `obo`:
```
#CONVERT:
robot convert \
--input /Documents/git/stato/dev/ontology/stato.owl \
--format obo \
--output results/stato.obo
```

#### Step 5.4: Export

An experimental feature to provide a list of an ontology classes in a tabular view:
```
java -jar robot.jar export \
--input /Documents/git/stato/dev/ontology/stato.owl  \
--header "IRI|ID|LABEL|definition" SubClass Of" \
--include "classes properties" \
--format xlsx \
--export /Documents/git/stato/export-result/stato-view.xlsx
```

### Step 6: evolving ontology
How to update and maintaing. e.g. 



## Executable Code in Notebook


```python
import isatools
import json
import pandas as pd 
import holoview
```





## Authors:

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Danielle Welter |  LCSB, University of Luxembourg| [0000-0003-1058-2668](https://orcid.org/0000-0003-1058-2668) | Writing - Original Draft, Code |
|Philippe Rocca-Serra| UOXF|[0000-0001-9853-5668](https://orcid.org/orcid.org/0000-0001-9853-5668)| Writing - Review, Code|
|Fuqi Xu|EMBL-EBI|[TODO-XXXX-XXXX-XXXX](https://orcid.org/orcid.org/0000-XXXX-XXXX-XXXX)|Writing - Review|
|Emiliano Reynares| Boehringer Ingelheim|[0000-0002-5109-3716](https://orcid.org/0000-0002-5109-3716)|Writing - Review,  Code |
|Karsten Quast|BI|[TODO-XXXX-XXXX-XXXX](https://orcid.org/orcid.org/0000-XXXX-XXXX-XXXX)| Writing|


___


## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
