# How to build application ontology with ROBOT
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

> Building an **application ontology** from source ontologies using ROBOT via a sustainable dynamic pipeline to allow seamless integration of source ontology updates. An **application ontology** is a semantic artefact which is developed to answer the needs of a specific application or focus. Thus it may borrow terms from a number of reference ontologies, which can be extremely large but whose broad coverage may not be required by the application ontology. Yet, it is critical to keep the application ontology synchronized with the reference ontologies that imports are made from.  We aim to document how a certain level of automation can be achieved.

:bulb: Ontology population process is out of the scope of the recipe.

## Graphical Overview of the FAIRification Recipe Objectives

<!-- TO DO: REVIEW-->

<div class="mermaid">
graph TD
  I1(fa:fa-university ontology source 1) -->|extract| M1(fa:fa-cube ontology module 1)
  I2(fa:fa-university ontology source 2) -->|extract| M2(fa:fa-cube ontology module 2)
  I3(fa:fa-university ontology source 3) -->|extract| M3(fa:fa-cube ontology module 3)
  M1 --> |merge| R1(fa:fa-cubes core)
  M2 --> |merge| R1(fa:fa-cubes core)
  M3 --> |merge| R1(fa:fa-cubes core)
  R1(fa:fa-cubes core) --> |materialize| R2(fa:fa-cubes reasoned & reduced core)

  R2(fa:fa-cubes reasoned & reduced core) -->|report| R3(fa:fa-tasks report)
  R2(fa:fa-cubes reasoned & reduced core) --> |edit| R4(fa:fa-cubes reasoned & reduced core)
  R3 -->|edit| R4
  R4 -->|annotate| R5(fa:fa-cubes fa:fa-tags fa:fa-cc annotated,reasoned,reduced core)
  R5 -->|convert| R6(fa:fa-star-o obo version)
  R5 -->|convert| R7(fa:fa-star owl version)
  R5 -->|export| R8(fa:fa-list xlsx view)
</div>

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgSTEoZmE6ZmEtdW5pdmVyc2l0eSBvbnRvbG9neSBzb3VyY2UgMSkgLS0-fGV4dHJhY3R8IE0xKGZhOmZhLWN1YmUgb250b2xvZ3kgbW9kdWxlIDEpXG4gIEkyKGZhOmZhLXVuaXZlcnNpdHkgb250b2xvZ3kgc291cmNlIDIpIC0tPnxleHRyYWN0fCBNMihmYTpmYS1jdWJlIG9udG9sb2d5IG1vZHVsZSAyKVxuICBJMyhmYTpmYS11bml2ZXJzaXR5IG9udG9sb2d5IHNvdXJjZSAzKSAtLT58ZXh0cmFjdHwgTTMoZmE6ZmEtY3ViZSBvbnRvbG9neSBtb2R1bGUgMylcbiAgTTEgLS0-IHxtZXJnZXwgUjEoZmE6ZmEtY3ViZXMgY29yZSlcbiAgTTIgLS0-IHxtZXJnZXwgUjEoZmE6ZmEtY3ViZXMgY29yZSlcbiAgTTMgLS0-IHxtZXJnZXwgUjEoZmE6ZmEtY3ViZXMgY29yZSlcbiAgUjEoZmE6ZmEtY3ViZXMgY29yZSkgLS0-IHxtYXRlcmlhbGl6ZXwgUjIoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpXG5cbiAgUjIoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpIC0tPnxyZXBvcnR8IFIzKGZhOmZhLXRhc2tzIHJlcG9ydClcbiAgUjIoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpIC0tPiB8ZWRpdHwgUjQoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpXG4gIFIzIC0tPnxlZGl0fCBSNFxuICBSNCAtLT58YW5ub3RhdGV8IFI1KGZhOmZhLWN1YmVzIGZhOmZhLXRhZ3MgZmE6ZmEtY2MgYW5ub3RhdGVkLHJlYXNvbmVkLHJlZHVjZWQgY29yZSlcbiAgUjUgLS0-fGNvbnZlcnR8IFI2KGZhOmZhLXN0YXItbyBvYm8gdmVyc2lvbilcbiAgUjUgLS0-fGNvbnZlcnR8IFI3KGZhOmZhLXN0YXIgb3dsIHZlcnNpb24pXG4gIFI1IC0tPnxleHBvcnR8IFI4KGZhOmZhLWxpc3QgeGxzeCB2aWV3KVxuXG5cdFx0IiwibWVybWFpZCI6eyJ0aGVtZSI6Im5ldXRyYWwifX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiAgSTEoZmE6ZmEtdW5pdmVyc2l0eSBvbnRvbG9neSBzb3VyY2UgMSkgLS0-fGV4dHJhY3R8IE0xKGZhOmZhLWN1YmUgb250b2xvZ3kgbW9kdWxlIDEpXG4gIEkyKGZhOmZhLXVuaXZlcnNpdHkgb250b2xvZ3kgc291cmNlIDIpIC0tPnxleHRyYWN0fCBNMihmYTpmYS1jdWJlIG9udG9sb2d5IG1vZHVsZSAyKVxuICBJMyhmYTpmYS11bml2ZXJzaXR5IG9udG9sb2d5IHNvdXJjZSAzKSAtLT58ZXh0cmFjdHwgTTMoZmE6ZmEtY3ViZSBvbnRvbG9neSBtb2R1bGUgMylcbiAgTTEgLS0-IHxtZXJnZXwgUjEoZmE6ZmEtY3ViZXMgY29yZSlcbiAgTTIgLS0-IHxtZXJnZXwgUjEoZmE6ZmEtY3ViZXMgY29yZSlcbiAgTTMgLS0-IHxtZXJnZXwgUjEoZmE6ZmEtY3ViZXMgY29yZSlcbiAgUjEoZmE6ZmEtY3ViZXMgY29yZSkgLS0-IHxtYXRlcmlhbGl6ZXwgUjIoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpXG5cbiAgUjIoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpIC0tPnxyZXBvcnR8IFIzKGZhOmZhLXRhc2tzIHJlcG9ydClcbiAgUjIoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpIC0tPiB8ZWRpdHwgUjQoZmE6ZmEtY3ViZXMgcmVhc29uZWQgJiByZWR1Y2VkIGNvcmUpXG4gIFIzIC0tPnxlZGl0fCBSNFxuICBSNCAtLT58YW5ub3RhdGV8IFI1KGZhOmZhLWN1YmVzIGZhOmZhLXRhZ3MgZmE6ZmEtY2MgYW5ub3RhdGVkLHJlYXNvbmVkLHJlZHVjZWQgY29yZSlcbiAgUjUgLS0-fGNvbnZlcnR8IFI2KGZhOmZhLXN0YXItbyBvYm8gdmVyc2lvbilcbiAgUjUgLS0-fGNvbnZlcnR8IFI3KGZhOmZhLXN0YXIgb3dsIHZlcnNpb24pXG4gIFI1IC0tPnxleHBvcnR8IFI4KGZhOmZhLWxpc3QgeGxzeCB2aWV3KVxuXG5cdFx0IiwibWVybWFpZCI6eyJ0aGVtZSI6Im5ldXRyYWwifX0)

>[name=Fuqi][color=green]
>I didnt find the `robot export` command. Is it in historical versions.

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

### Step 0: Preliminary considerations

#### What is an application ontology?
An application ontology is a semantic artefact which is developed to answer the needs of a specific use case or scenario. It reuses agreed knowledge specified in reference ontologies, which can be extremely large but whose broad coverage may not be required by the application ontology.

#### What is a use a case?

#### Roles involved
> Reference project roles by Oya: [FAIR+ Grive here](https://docs.google.com/spreadsheets/d/1cmCj0GmOw4DFX8f6p-_EkJdPT2UUeAdd4wmeI8F9aVI/edit#gid=1559358961)

> TBD. Briefly depict each one.
* _Domain Expert_ --> "Subject Matter Expert" according to the Oya's spreadsheet?
* _Use case/Scenario Owner_ --> Any Oya's spreadsheet role match this one? 
* _Ontology Developer_ --> It could be the "IT Specialist" according to the Oya's spreadsheet, but such a role does not reflect ontology modelling skills required.

### Step 1: Define the goal of the application ontology

The development of an application ontology is driven by specific use cases and target datasets. The first step in application ontology development is to determine the subject and the aim of the application ontology. 

In this recipe, we demonstrate the workflow of building an application ontology for patient metadata and patient sequencing data investigations. Competency questions of this ontology are provided [here](https://github.com/FAIRplus/the-fair-cookbook/blob/ontology_robot_recipe/docs/content/recipes/ontology-robot/competency_questions.md). _Table 1_ is a snapshot of the example dataset. The complete patient metadata example dataset is [here](https://github.com/FAIRplus/the-fair-cookbook/blob/ontology_robot_recipe/docs/content/recipes/ontology-robot/ExternalStudiesKQ.xlsx).

_Table 1: Patient metadata example_

| Study                | source_id | sample_description  | tissue | source_tissue | cell                  | cellline | disease                       | gender | species      |
|----------------------|-----------|---------------------|--------|---------------|-----------------------|----------|-------------------------------|--------|--------------|
| GSE52463Nance2014    | EX08_001  | Lung - Normal       | Lung   |               |                       |          | Normal                        | male   | Homo sapiens |
| GSE52463Nance2014    | EX08_015  | Lung - IPF          | Lung   |               |                       |          | Idiopathic Pulmonary Fibrosis | male   | Homo sapiens |
| GSE116987Marcher2019 | EX101_1   | HSC CCl4-treated w0 |        |               | Hepatic Stellate Cell |          | NA                            |        | Mus musculus |


### Step 2: Select terms from reference ontologies

#### Step 2.1 Select source ontologies

To build an application ontology that supports communication between different data resources, it is recommended to reuse existing terms from existing reference ontologies instead of creating new terms.

>:book: _Reference ontology:_ a semantic artifact with a canonical and comprehensive representation of the entities in a specific domain.
>
>_Source ontology:_ An ontology to be integrated into the application ontology, usually a reference ontology. 

When selecting reference ontologies as source ontologies, the reusability and sustainability of the source ontology need to be considered. Many ontologies in [the OBO foundry](http://www.obofoundry.org/) use the [CC-BY](https://creativecommons.org/licenses/by/2.0/) licence, allowing sharing and adaptation. Such ontologies can be directly used as source ontology. Reference ontologies with similar umbrella structures can be conveniently combined in the application ontology. The format and maintenance of the reference ontology shall also be considered.

Specific use cases and requirements from the target dataset also affect the choice of source ontologies. For use cases focusing on extracting data from heterogeneous datasets with complicated data types and data relationships, reference ontologies with rich term relationships are preferred. The interpretation of each term also depends on the context and requirements of the target dataset. For example, _"hypertension"_ can be either interpreted as a _phenotype_ and mapped to phenotype ontologies, or a _disease_ mapped to disease ontologies.


The example dataset includes metadata related to disease, species, cell lines, tissues and biological sex. _Table 2_ lists some reference ontologies available in corresponding domains. In this recipe, we selected _MONDO_ for disease domain, _UBRERON_ for anatomy, _NCBItaxon_ for species taxonomy and _PATO_ for biological sex. 

_Table 2: Available reference ontologies in selected domains_ 

|Domain|Reference Ontologies|
|----|----|
|Disease| [Mondo Disease Ontology, MONDO](http://www.obofoundry.org/ontology/mondo.html)<br> [Disease Ontology, DIOD](https://disease-ontology.org/)<br> |
|Species|[NCBI organismal classification, NCBItaxon](http://www.obofoundry.org/ontology/ncbitaxon.html)|
|Cell line|[Cell Ontology, CL](http://www.obofoundry.org/ontology/cl.html)<br> [Cell Line Ontology, CLO](http://www.obofoundry.org/ontology/clo.html)|
|Tissue|[NCI Thesaurus OBO Edition, NCIT](http://www.obofoundry.org/ontology/ncit.html)<br> [Ontology for MIRNA Target, OMIT](http://www.obofoundry.org/ontology/omit.html)<br> [Uberon multi-species anatomy ontology, UBERON](http://www.obofoundry.org/ontology/uberon.html)|
|Biological Sex|[Phenotype And Trait Ontology, PATO](http://www.obofoundry.org/ontology/pato.html)|


#### Step 2.2 Select seed ontology terms
> :book: _Seed ontology terms_: A set of entities extracted from reference ontologies for the application ontology.
> 
**Aim**

To identify the seeds needed to perform the knowledge extraction from external sources, i.e., the set of entities to extract in order to be integrated on the application ontology.

**Main roles and tasks**

_Domain Expert_ and _Use Case/Scenario Owner_ identify the right seeds for a given application ontology.

**Supporting roles and tasks**

_Ontology Developer_ provides the helper tools to ease and to scale the identification of the seeds.

**Overview**

Besides the fact that is always possible to manually identify the set of seeds needed for the performing of the concept extraction, to have a helper tool allows to run the task at scale. Following, an automatable approach based on using widely known life sciences annotators  - Zooma and NCBO Annotator - are depicted.

ZOOMA is a web service for discovering optimal ontology mappings, developed by the Samples, Phenotypes and Ontologies Team at the European Bioinformatics Institute (EMBL-EBI). It can be used to automatically annotate plain text about biological entities with ontology classes. Zooma allows to limit the sources used to perform the annotations. These sources are either curated datasources, or ontologies from the Ontology Lookup Service (OLS). ZOOMA contains a linked data repository of annotation knowledge and highly annotated data that has been feeded with manually curated annotation derived from publicly available databases. Because the source data has been curated by hand, it is a rich source of knowledge that is optimised for this task of semantic markup of keywords, in contrast with text-mining approaches.

The NCBO Annotator is an ontology-based web service that annotates public datasets with biomedical ontology concepts based on their textual metadata. It can be used to automatically tag data  with ontology concepts. These concepts come from the Unified Medical Language System (UMLS) Metathesaurus and the National Center for Biomedical Ontology (NCBO) BioPortal ontologies.

Both the Zooma and NCBO Annotator service provides a web interface and a REST API to identify the seed terms by annotation of free text. Two scripts able to automate the annotation of a set of free text terms are shown following.

#### Seed term extraction with ZOOMA

The following sample script uses the Zooma web service to get a list of seed terms - i.e., the URIs of ontology classes -. The service also states the level of confidence of every seed proposed.
```python3
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
Running the before presented script to get the seeds for the terms `male`, `female`, and `unknown` generates the following results:
```python3
['http://purl.obolibrary.org/obo/PATO_0000384 # male-Confidence:HIGH',
 'http://purl.obolibrary.org/obo/PATO_0000383 # female-Confidence:HIGH',
 'http://www.orpha.net/ORDO/Orphanet_288 # unknown-Confidence:MEDIUM',
 'http://www.ebi.ac.uk/efo/EFO_0003850 # unknown-Confidence:MEDIUM',
 'http://www.ebi.ac.uk/efo/EFO_0003952 # unknown-Confidence:MEDIUM',
 'http://www.ebi.ac.uk/efo/EFO_0009471 # unknown-Confidence:MEDIUM',
 'http://www.ebi.ac.uk/efo/EFO_0000203 # unknown-Confidence:MEDIUM',
 'http://www.ebi.ac.uk/efo/EFO_0003863 # unknown-Confidence:MEDIUM',
 'http://www.ebi.ac.uk/efo/EFO_0000616 # unknown-Confidence:MEDIUM',
 'http://purl.obolibrary.org/obo/HP_0000952 # unknown-Confidence:MEDIUM',
 'http://www.ebi.ac.uk/efo/EFO_0003853 # unknown-Confidence:MEDIUM',
 'http://www.ebi.ac.uk/efo/EFO_1001331 # unknown-Confidence:MEDIUM',
 'http://www.ebi.ac.uk/efo/EFO_0003769 # unknown-Confidence:MEDIUM',
 'http://purl.obolibrary.org/obo/HP_0000132 # unknown-Confidence:MEDIUM',
 'http://www.ebi.ac.uk/efo/EFO_0000408 # unknown-Confidence:MEDIUM',
 'http://www.ebi.ac.uk/efo/EFO_0008549 # unknown-Confidence:MEDIUM',
 'http://www.ebi.ac.uk/efo/EFO_0001642 # unknown-Confidence:MEDIUM']
[]
```
#### Seed term extraction with NCBO Annotator

The following sample script uses the NCBO Annotator web service to get a list of seed terms - i.e., the URIs of ontology classes -.
```python3
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
        r = requests.get('http://data.bioontology.org/annotator', params=ploads)
        
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
Running the before presented script to get the seeds for the terms `male`, `female`, and `unknown` generates the following results:
```python3
['http://purl.obolibrary.org/obo/UBERON_0003101 # male',
 'http://purl.obolibrary.org/obo/UBERON_0003100 # female']
['unknown']
```

#### Step2.2.3 Seed term extraction with SPARQL 

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


### Step 3: Extract ontology modules from source ontologies

Module extractions from ontologies can be run manually and in an ad hoc fashion. We would however recommend to collect all steps together into a script or Make file to avoid missing steps. ROBOT steps can in theory be chained together into single large commands. Practical experience however teaches that this can have unexpected consequences as well as making debugging difficult in the event of an issue. It is therefore advisable to split extractions and merges out into individual steps with intermediate artefacts which can be deleted at the end of the process chain.

#### Step 3.1 Get source ontology files

We recommend starting each (re)build of the application ontology with the latest versions of the source ontologies unless there is a good reason not to update to the latest version. Ideally, this should be done automatically, for example through a shell script that CURLs all ontologies from their source URIs, e.g.

```shell script
curl -L http://purl.obolibrary.org/obo/uberon.owl > uberon.owl
```
#### Step 3.2 Choose ontology extraction algorithms

ROBOT supports two types of ontology module extraction, Syntactic Locality Module Extractor (SLME) and Minimum Information to Reference an External Ontology Term (MIREOT). SLME extractions can be further subdivided into TOP (top module), BOT (bottom module) and STAR (fixpoint-nested module). For full details of what these different options entail, see http://robot.obolibrary.org/extract.html. We recommend the use of BOT for comprehensive modules that preserve the links between ontology classes and the use of MIREOT if relationships apart from parent-child ones are less important. 


#### Step 3.3 Extract modules using seed terms

Using `robot` tool provided by the `OBO foundry`, the creation of a module can be done with one command:

```bash
robot extract --method <some_selection> \
    --input <some_input.owl> \ 
    --term-file <list_of_classes_of_interest_in_ontology.txt> \
    --intermediates <choose_from_option> \
    --output ./ontology_modules/extracted_module.owl
```
The `robot` extract command takes several arguments:

* *method*: `robot` uses 4 different algorithms to generate a module.  TOP, BOT, STAR (all from the SLME method), and MIREOT. The first two will create a module  below or above the seed classes (the classes of interest in the target ontology) respectively. The STAR method creates a module by pulling all the properties and axioms of the seed classes but nothing else. MIREOT uses a different methods and offers some more options, in particular when it comes to how many levels up or down (parent and children) are needed.     
* *input*: this argument is to specify the target ontology you want to extract a module from. It can be the original artefact or a filtered version of it.
* *imports*: this argument allows to specific whether or not to include imported ontologies. Note that the default is to do so using the value `include`. Choose `exclude` otherwise.
* *term-file*: the text file holding the list of classes of interested identified by their iri (e.g. http://purl.obolibrary.org/obo/UBERON_0001235 # adrenal cortex)
* *intermediates*: specific to the `MIREOT` method, it allows to let the algorithm know how much or how little to extract. It has 3 levels (`all`,`minimal`, `none`).
* *output*: the path to the owl file holding the results of the module extraction
* *copy-ontology-annotations*: a boolean value true/false to pull or not any class annotation from the parent ontology. default is `false`
* *sources*: optional, a pointer to a file mapping 
* *annotate-with-source*: a boolean value true/false. default is `false`


The above query, saved under `select_anatomy_subset.sparql` can be used to generate a dynamic seed list, then do a BOT extraction: 

```shell script
robot query --input uberon.owl --query select_anatomy_subset.sparql uberon_seed_list.txt

robot extract --method BOT --input uberon.owl --term-file uberon_seed_list.txt -o uberon_subset.owl
```

#### Step 3.4 Assess extracted modules

The extracted ontology module should include all seed terms and represent the term relationships correctly. It should also preserve the correct hierarchical structure of the source ontology and have consistent granularity.


### Step 4: Build the upper level umbrella ontology

**Aim**

To build the umbrella ontology, aimed to model the main entity of the use case and its relationships with the ontology classes extracted on the previous Step.

**Main roles and tasks**

_Domain Expert_ and _Use Case/Scenario Owner_ identify the main entity of the use case and its relationships with extracted modules. Both, the main entity and the relationships with the ontology classes previously extracted can be locally specified - i.e., be defined in the scope of the application ontology - or can also be extracted from external knolwedge sources.

**Supporting roles and tasks**

_Ontology Developer_ generates the artifacts to build the _umbrella_ ontology by means of the ROBOT tool.

**Overview**

ROBOT provides a template-driven ontology term generation system. A ROBOT template is a tab-separated values (TSV) or comma-separated values (CSV) file that depicts a set of patterns to build ontology entities - i.e., classes, properties, and individuals -. These templates can be used for modular ontology development.
After the _Domain Expert_ and the _Use Case/Scenario Owner_ specify the main entity of the use case and its relationships with remaining ontology entities, the _Ontology Developer_ generates the ROBOT templates depicting the set of patterns aimed to build the _umbrella_ ontology.

A ROBOT command using a template to build an ontology is shown below:
```bash
robot template --template template.csv \
    --prefix "r4: https://fairplus-project.eu/ontologies/R4/" \
    --ontology-iri "https://fairplus-project.eu/ontologies/R4/" \
    --output ./templates/umbrella.owl
```

And a template sample is presented following:


| ID | Label | Entity Type | Equivalent Axioms | Characteristic | Domain | Range | 
| -------- | -------- | -------- | -------- |-------- | -------- | -------- |
| ID     | LABEL     | TYPE     | EC % | CHARACTERISTIC | DOMAIN | RANGE |
|ex:cl_2 | Class_2 | class |-|-|-|-|
|ex:cl_3 | Class_3 | class |ex:cl_2|-|-|-|
|ex:op_1	|Prop_1| object property|-|Class_2|Class_3|
|ex:dp_1	|Prop_2| data property|-|functional|Class_2|xsd:string|

>:bulb: **_Tip:_** The generated ontology can be visualized by using the Protege tool or a local deployment of OLS (Recipe 1.3). The OLS local deployment option is recommended by this recipe, given that Protege crash when loading medium or large size ontologies.
    
### Step 5: Merge ontology modules and _umbrella_ ontology
**Aim**

To built a first draft of the application ontology by merging the ontology modules previuosly extracted and the _umbrella_ ontology locally built.

**Main roles and tasks**

_Ontology Developer_ merge (a) the ontology modules extracted from domain ontologies, and (b) the _umbrella_ ontology built on the previous step, by running the corresponding ROBOT command.

**Supporting roles and tasks**

Not needed.

**Overview**
The "merge" ROBOT command allows to combines two or more separate input ontology modules into a single ontology. Following, the ROBOT command merging the _umbrella_ ontology and the modules is shown:
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

```
robot materialize \
--reasoner ELK  \
--input merged_owl  \
reduce \
--output materialized.owl 
```

The ontology materialization uses OWL reasoners. ROBOT provides [several ontology reasoners](http://robot.obolibrary.org/reason). 

It's also possible to identify issues in the ontology with some quality control SPARQL queries. 

```
robot report --input edit.owl --output report.tsv
```


#### Step 6.2: Annotate

Ontology annotation adds metadata to the owl file. It's recommended to provide ontology IRIs, version IRIs, ontology title, descriptions and license to support future usage and management. 

The annotation can be added either line-by-line or provided in a turtile(.ttl) file. 
```
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
```
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

#### Step 6.3*: Convert

Besides OWL format, the Open Biomedical Ontology (OBO) format is also widely used in life science related ontologies. It's possible to convert an `.owl` file to `.obo` file using:

```
#CONVERT:
robot convert \
--input  annotated.owl\
--format obo \
--output results/annotated.obo
```

### Step 7: Assess coverage of the ontology scope

**Aim**

To assess coverage of the ontology scope by verifying if it is able to answer the competency questions formulated on Step 1.

**Main roles and tasks**

The _Ontology Developer_ implements the competency questions as a set of SPARQL queries and runs them against the developed ontology. It checks if the answers/results are aligned with the scope of the ontology.

**Supporting roles and tasks**

The _Use Case/Scenario Owner_ collaborate with the _Ontology Developer_ on the assessment of the competency questions answers/results. 

**Overview**

An ontology development workflow typically include query operations aimed to verify and validate the ontology. ROBOT provides the `query` command to perform SPARQL queries  against an ontology.
The query command run SPARQL `ASK`, `SELECT`, and `CONSTRUCT` queries by using the `--query` option with two arguments: a query file and an output file. Instead of specifying one or more pairs (query file, output file), it is also specify a single `--output-dir` and use the `--queries` option to provide one or more queries of any type. Each output file will be written to the output directory with the same base name as the query file that produced it. An pattern example of this commmand is shown following.

```bash
robot query --input <input_ontology_file> \
    --queries <query_file> \
    --output-dir <path_to_rsults> results/
```

### References
- R.C. Jackson, J.P. Balhoff, E. Douglass, N.L. Harris, C.J. Mungall, and J.A. Overton. [_ROBOT: A tool for automating ontology workflows_](https://link.springer.com/epdf/10.1186/s12859-019-3002-3?author_access_token=bB8BLjFWrdh42vR6DjT-nG_BpE1tBhCbnbw3BuzI2RPCZ2BK7EeexaCNYfT-cCz8Q_mrZomT2_svoQf12CW661Sagzw6JGF9DhJq3Q3fTPdMGFMtais7MRgx8-kDhp6uC9g2qcVh5FumTsveV22XVQ%3D%3D). BMC Bioinformatics, vol. 20, July 2019
- Arp, Robert, Barry Smith, and Andrew D. Spear. _Building ontologies with basic formal ontology_. Mit Press, 2015.

## Supplementary material:
- [Example Dataset](https://github.com/FAIRplus/the-fair-cookbook/blob/ontology_robot_recipe/docs/content/recipes/ontology-robot/ExternalStudiesKQ.xlsx)
- [Competency questions](https://github.com/FAIRplus/the-fair-cookbook/blob/ontology_robot_recipe/docs/content/recipes/ontology-robot/competency_questions.md)
- [Scripts and intermediate artifacts](https://github.com/FAIRplus/the-fair-cookbook/tree/ontology_robot_recipe/docs/content/recipes/ontology-robot)

## Authors:

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Danielle Welter |  LCSB, University of Luxembourg| [0000-0003-1058-2668](https://orcid.org/0000-0003-1058-2668) | Writing - Original Draft, Code |
|Philippe Rocca-Serra| UOXF|[0000-0001-9853-5668](https://orcid.org/orcid.org/0000-0001-9853-5668)| Writing - Review, Code|
|Fuqi Xu|EMBL-EBI|[0000-0002-5923-3859](https://orcid.org/orcid.org/0000-XXXX-XXXX-XXXX)|Writing - Draft, Review|
|Emiliano Reynares| Boehringer Ingelheim|[0000-0002-5109-3716](https://orcid.org/0000-0002-5109-3716)|Writing - Review,  Code |
|Karsten Quast|BI|[TODO-XXXX-XXXX-XXXX](https://orcid.org/orcid.org/0000-XXXX-XXXX-XXXX)| Writing|


___


## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
