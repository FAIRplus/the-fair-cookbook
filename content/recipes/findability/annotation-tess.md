# Annotating training materials in ELIXIR TeSS with interoperable keywords/registry entries

---

````{panels_fairplus}
:identifier_text: FCB___
:identifier_link: https://w3id.org/faircookbook/FCB___
:difficulty_level: 1
:recipe_type: technical_guidance
:reading_time_minutes: 20
:intended_audience: trainer, data_curator, data_manager
:maturity_level: 3  
:maturity_indicator: 33
:has_executable_code: nope
:recipe_name: Annotating training materials in ELIXIR TeSS
```` 


## Main Objectives

[TeSS (Training eSupport System)](https://tess.elixir-europe.org/) is a platform developed to provide a one-stop shop for trainers and trainees to discover online information and content, including training materials, events, and interactive tutorials.
TeSS provides trainers with a platform for exchanging information and workshop materials, and to trainees a useful collection of content that was delivered across the ELIXIR nodes and beyond. 
As the catalogue grows in size, it becomes increasingly challenging to locate and categorise the relevant materials. While it is possible to annotate TeSS entries with keywords, these are not from a controlled vocabulary. 
As a partial solution to this, TeSS implements integrations towards services providing persistent identifiers, which can be used for annotating TeSS pages in a more FAIR-oriented fashion, and, consequently, to implement smarter queries that can lead users to relevant training materials and events. 
This recipe is particularly relevant to training coordinators and providers, and to TeSS curators and annotators.

---

## Requirements

* knowledge requirement:
   * Please familiarise yourself with the [ELIXIR Training Lesson about TeSS](https://elixir-europe-training.github.io/ELIXIR-TrP-TeSS/chapters/00_Preface/#introduction).
 
This recipe requires working with the following resources:  
* TeSS: [Registry of training materials and events](https://tess.elixir-europe.org/). 
* FAIRsharing: [A registry of (meta)data standards, databases, and policies](https://fairsharing.org/)
* bio.tools: [A registry of software tools for bioinformatics and the life sciences](https://bio.tools/)
* EDAM: [The ontology of data analysis and data management](https://edamontology.org/)  
** EDAM can be browsed via BioPortal: [A repository of biomedical ontologies](https://bioportal.bioontology.org/ontologies/EDAM)

```{note} 
The recipe can be completed using only TeSS, as the implemented integration allows browsing via API the registries and ontology on the TeSS portal. It is, however, recommended also looking at the entries on the various portals to get a more precise view and, possibly, find other relevant elements that can be used for annotation.
```
---

## Table of Data Standards

| Resources                                                  |
|:-----------------------------------------------------------| 
| [FAIRsharing](https://doi.org/10.25504/FAIRsharing.2abjs5) |
| [EDAM](https://doi.org/10.25504/FAIRsharing.a6r7zs)        |
| [bio.tools](https://doi.org/10.25504/FAIRsharing.63520c)   |

---

## Main Content
We provide here detailed information on how to perform annotation on TeSS. All the annotation work is done on TeSS, although it is sometimes useful to visit the registry providing the identifier or the ontology portal for better clarity. All the annotations are performed by editing the form collecting information for TeSS entries. This applies to both training materials and events. Annotations using the three resources mentioned here can be done independently and without following any particular order.
```{note} 
You need to be the resource creator of the page or have annotator privileges on TeSS to add these annotations on a previously generated pages
```  

### Annotating TeSS with FAIRsharing identifiers
Each FAIRsharing entry is assigned a human-readable, unique identifier. 

These allow to trace resources and integrate FAIRsharing data with other resources. To annotate a TeSS entry with FAIRsharing identifiers, follow these steps:

1. Please select event or material you wish to annotate on TeSS or create a new one.
1. Click the EDIT button on the top right. 
1. In this edit mode, scroll down to the "Suggested policies, standards and databases to associate with this resource" section and expand it.
1. Type the name of the standard/repository/policy to be associated with the TeSS entry. You have the option to choose one of the sub-registries from FAIRsharing.
1. Click on the "+" symbol to add the identifier to the page.
1. Scroll to the bottom and click the orange "update" button to publish your updates.
1. The annotation will appear on the materials page in the "External resources" section

This annotations can be used for filtered queries on TeSS using the syntax:

`https://tess.elixir-europe.org/` + "__TeSS SUBREGISTRY__" + `standard_database_or_policy=` + "__FAIRSHARING NAME__"

where "__TeSS SUBREGISTRY__" is one of the subregistries of TeSS (e.g. "materials") and "__FAIRSHARING NAME__" is the name (not the DOI) associated with the FAIRsharing entry.  
In the case of training materials for the European Nucleotide Archive, for example, the query sting would be:

[https://tess.elixir-europe.org/__materials__?standard_database_or_policy=__European+Nucleotide+Archive__](https://tess.elixir-europe.org/materials?standard_database_or_policy=European+Nucleotide+Archive)


### Annotating TeSS with bio.tools identifiers

Each bio.tools entry is assigned a human-readable, unique identifier.

These identifiers provide a reference to a "Tool Cards" of essential information. These allow to trace resources and integrate bio.tools data with other resources. To annotate a TeSS entry with bio.tools identifiers, follow these steps:

1. Please select event or material you wish to annotate on TeSS or create a new one.
1. Click the EDIT button on the top right. 
1. In this edit mode, scroll down to the "Suggested tools to associate with this resource" section and expand it.
1. Type the name of the tool to be associated with the TeSS entry.
1. Click on the "+" symbol to add the identifier to the page.
1. Scroll to the bottom and click the orange "update" button to publish your updates.
1. The annotation will appear on the materials page in the "External resources" section

These annotations can be used for filtered queries on TeSS using the syntax:   

`https://tess.elixir-europe.org/` + "__TeSS SUBREGISTRY__" + `?tools=` + "__BIOTOOLS_NAME__"

where "__TeSS SUBREGISTRY__" is one of the subregistries of TeSS (e.g. "materials") and "__BIOTOOLS_NAME__" is the name (not the tool ID) associated with the bio.tools entry.   
In the case of training materials for the Data Stewardship Wizard, for example, the query string would be: 

[https://tess.elixir-europe.org/__materials__?tools=__Data+Stewardship+Wizard__](https://tess.elixir-europe.org/materials?tools=Data+Stewardship+Wizard)

### Annotating TeSS with EDAM ontology

#### Annotating with EDAM main terms

TeSS pages can be annotated using two subregistries of EDAM: "Scientific topics" and "Operations". These would need to be added separately. To annotate a TeSS entry using a main terms of EDAM, use the following procedure:

1. Please select event or material you wish to annotate on TeSS or create a new one.
1. Click the EDIT button on the top right. 
1. In this edit mode, scroll down to the "Scientific topics" or to the "Operations" section.
1. Type the name of the main EDAM term to be associated with the TeSS entry. As you are typing, suggestions will be provided. If no relevant suggestions appear, follow the block of instructions below.
1. Click on the suggestion to add the annotation to the page. 
1. Scroll to the bottom and click the orange "update" button to publish your updates.
1. The annotation will appear on the materials page in the "Scientific Topics" and "Operations" sections. Note that the terms are not clickable.


#### Browse through synonyms on EDAM to find the right class

In the current integration ([Version: 1.4.1](https://github.com/ElixirTeSS/TeSS/releases/tag/v1.4.1)), TeSS only displays the main EDAM terms. Synonyms cannot be accessed. Instructions on how to browse this additional information are provided below:

1.Open the [NCBO BioPortal](https://bioportal.bioontology.org/)
1.Under "Find an ontology", start typing "EDAM" and click on "EDAM - The data analysis and management ontology"
1. Open the "Classes" tab and type your desired term. This will search also through synonyms and provide a better suggestion than the native TeSS implementation. 
1. Use the "preferred name" as the main EDAM term when following the block of instructions above.  

```{note} 
EDAM supports a wide range on synonyms with various degrees of semantic proximity to the main term.
```

EDAM-annotated entries can be retrieved using filtered queries on TeSS with the syntax: 

* for EDAM’s Topics  
`https://tess.elixir-europe.org/` + "__TeSS SUBREGISTRY__" + `?scientific_topic=` + "__EDAM_NAME__"

* for EDAM’s Operations  
`https://tess.elixir-europe.org/` + "__TeSS SUBREGISTRY__" + `?operations=` + "__EDAM_NAME__"

where "__TeSS SUBREGISTRY__" is one of the subregistries of TeSS (e.g. “materials”) and "__EDAM_NAME__" is the name (not the ID) associated with the EDAM class.   
In the case of training events with “data management” as a topic, for example, the query string would be: 
[https://tess.elixir-europe.org/__events__?scientific_topics=__Data+management__](https://tess.elixir-europe.org/events?scientific_topics=Data+management)

---

## Conclusion

In this recipe, we provide detailed instructions on how to make use of the existing integrations on TeSS to manually annotate “Training Materials” entries. These annotations, provided by ELIXIR registries such as FAIRsharing and bio.tools, and by the EDAM Ontology, greatly improve the findability of the entry in a FAIR-oriented way through the usage of the dedicated identifiers. These annotations will furthermore facilitate the integration of fine-tuned TeSS queries based on these identifiers into external resources.

## Further reading
* [How TeSS supports FAIR](https://elixirtess.github.io/docs/overview/fair/)
* Bianchini, F., Botzki, A., Helena, R., & Pérez Sitjà, X. (2024, December 20). __RDM training annotation: strategies for improved curation in TeSS.__ Zenodo. [https://doi.org/10.5281/zenodo.14534996](https://doi.org/10.5281/zenodo.14534996). 
* Pérez Sitjà, X., Lawson-Tovey, S., Bianchini, F., & Jetten, M. (2026). __D2.3 End report on FAIR training resources.__ Zenodo. [https://doi.org/10.5281/zenodo.18481270](https://doi.org/10.5281/zenodo.18481270) 

## Authors
```{authors_fairplus}
Federico: writing, conceptualization, original draft
DianaPilvar: review, editing
GilPoiares-Oliveira: review, editing
DanielWibberg: review
JeanneWilbrandt: review
HelenaSchnitzer: review
Vassilios: review
```

## License
````{license_fairplus}
CC-BY-4.0
````