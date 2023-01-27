(fcb-dats-model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format))=
# Introducing the DATS model


<br/>
<br/>

````{panels_fairplus}
:identifier_text: FCB082
:identifier_link: 'https://w3id.org/faircookbook/FCB082'
:difficulty_level: 2
:recipe_type: background_information
:reading_time_minutes: 15
:intended_audience: data_manager, data_curator, software_developer
:maturity_level: 2  
:maturity_indicator: 15
:has_executable_code: nope
:recipe_name: Introducing the DATS model
```` 


## Main Objectives

The main purpose of this recipe is:

>* Provide a general introduction to the Data Tag Suite(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) for representing project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project), study and dataset metadata
>* Highlight challenges in implementing the model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) in a data catalogue

---


## Graphical Overview

````{dropdown} **Data Model**
:open:
```{figure} DataModelDiagram.png
---
width: 800px
name: data-model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)-diagram
alt: Data Model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) Diagram
---
Data Model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) Diagram
```
````

---


## Table of Data Standards


| Data Format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s  | Terminologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) | Model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s  |
| :------------- | :------------- | :------------- |
| [JSON-LD](https://json-ld.org/) | [OBO(URL_TO_INSERT_RECORD http://www.obofoundry.org/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059) Foundry(URL_TO_INSERT_RECORD http://www.obofoundry.org/)](https://obofoundry.org/) | [DATS](https://datatagsuite.github.io/docs/html/dats.html) |
| |  | [DCAT](https://www.w3.org/TR/vocab-dcat(URL_TO_INSERT_RECORD https://www.w3.org/TR/vocab-dcat/)-2/) |
| |  | [SDO](https://schema.org(URL_TO_INSERT_RECORD http://schema.org/)/) |

---

## Model overview

Data Tag Suits (DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications)) {footcite}`pmid28585923` is a data description model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) designed and produced to describe datasets being ingested in DataMed(URL_TO_INSERT_RECORD https://datamed.org)(URL_TO_INSERT_RECORD https://datamed.org), a prototype for data discovery developed(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) as part of the bioCADDI(URL_TO_INSERT_RECORD https://code.google.com/p/ddi-ontology/)E(URL_TO_INSERT_RECORD http://biocaddie.org/)(URL_TO_INSERT_RECORD http://biocaddie.org/) project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project) {footcite}`pmid28546571`. DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) was co-developed(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) by the Oxford e-Research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) Centre and the NIH(URL_TO_INSERT_RECORD http://sweetgum.nybg.org/science/ih/) Data Common Big Data to Knowledge (BD2K) initiative, where it was used to uniformly represent metadata across a number of project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project)s, including the Genotype-Tissue Expression project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project) (GTEx) and Trans-Omics for Precision Medicine (TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)P(URL_TO_INSERT_RECORD http://top-thesaurus.org/)(URL_TO_INSERT_RECORD https://cos.io/top)M(URL_TO_INSERT_RECORD https://doi.org/10.1016/j.future.2010.07.005)ed).

DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) is semantically compatible with the Data Catalog Vocabulary(URL_TO_INSERT_RECORD https://www.w3.org/TR/vocab-dcat/) (DC(URL_TO_INSERT_RECORD http://dublincore.org/documents/dces/)(URL_TO_INSERT_RECORD https://doi.org/10.25504/FAIRsharing.3nx7t)AT(URL_TO_INSERT_RECORD https://www.w3.org/TR/vocab-dcat/)(URL_TO_INSERT_RECORD http://cat.aii.caas.cn/)), a Resource Description Framework(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) (RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/)) vocabulary designed to facilitate interoperability among data catalogues published on the web, as well as schema.org(URL_TO_INSERT_RECORD http://schema.org/) (SDO(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/1651)), which is a community-driven effort with a similar interoperability goal to DC(URL_TO_INSERT_RECORD http://dublincore.org/documents/dces/)(URL_TO_INSERT_RECORD https://doi.org/10.25504/FAIRsharing.3nx7t)AT(URL_TO_INSERT_RECORD https://www.w3.org/TR/vocab-dcat/)(URL_TO_INSERT_RECORD http://cat.aii.caas.cn/) but a more general-purpose scope.

The original DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) centered around concept of a "Dataset", an entity that covers technical aspects such as licensing, data types and distributions. The Dataset is produced by or is the input or output of a “Study”, which contains elements that are specific to life, environmental and biomedical science domains, and which model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s experimental processes, cohorts and protocol informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion. To meet the requirements of project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project)-generated datasets, the DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) was extended to include the third core(URL_TO_INSERT_RECORD http://purl.uniprot.org/core/)(URL_TO_INSERT_RECORD https://core.ac.uk) concept of “Project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project)”, covering general informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion such as title, publications, funding and contributors.


### Core objects

The DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) centres around three core(URL_TO_INSERT_RECORD http://purl.uniprot.org/core/)(URL_TO_INSERT_RECORD https://core.ac.uk) objects, "Project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project)", "Study" and "Dataset", each of which contains a set of sub-objects, which in turn can be nested down to the lowest unitary object (which contains no further objects), which is the “Annotation”. Project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project), Study and Dataset relate to each other in a triangular fashion as shown in figure 1.

At first glance, the three core(URL_TO_INSERT_RECORD http://purl.uniprot.org/core/)(URL_TO_INSERT_RECORD https://core.ac.uk) objects make the DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) reminiscent of the ISA (Investigation, Study, Assay) model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) for describing experimental processes. There are however several key differences between the two. For one, ISA has a waterfall structure whereby any instance of the model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) has to contain a Study object between an Investigation and an Assay. In DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) on the other hand, it is possible for a Dataset to be directly dependent on a Project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project), without any Study informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion. This is relevant for datasets such as knowledge graphs or synthetic datasets, for which no study metadata may be available. Additionally, DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) focuses on the technical details, availability and use restrictions of datasets whereas the purpose of the ISA model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) is to describe experimental procedures in great detail. While the DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) Study covers some of this informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion, it is much less comprehensive or central to the captured data than for ISA.

#### Project

The Project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project) object was not part of the original version of DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications). It was added in the second version as a means of linking different studies and datasets under one common parent as well as capturing informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion such as project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project) contacts or consortium informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion, publications not linked to one specific study, funding sources, project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project) websites and start/end dates.

#### Study

The Study object, although part of the original DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format), had a less central role in the first iteration than it has in this latest one. Capturing the context in which the Dataset was either generated or used, the Study provides informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion about the type of study undertaken (e.g. clinical trials or chemical toxicity screens), cohorts (or "studyGroups), input materials, selection criteria and the steps involved in the study. 

#### Dataset

The Dataset object was the central concept of the initial DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) but became an equal part in the `Project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project)-Study-Dataset` triangle in version 2. The object captures technical informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion about the dataset, such as file types, data standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s, versions and licensing as well as links to the actual data if available. It also model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion related to the creation of the dataset such as input materials, diseases, biological entities and other similar objects, as well as the types of experiments from which the dataset was derived and any associated dimensions(URL_TO_INSERT_RECORD https://www.dimensions.ai/) or components.

### Sub-objects

Each of the three top-level objects references a range of sub-objects, which in turn contain further sub-objects, down to the lowest unitary object (which contains no further objects), which is the “Annotation”. An “Annotation” consists of just two key-value pairs, the “value” and, optionally, the “valueIRI”, designed to capture the Internationalized Resource Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) (IRI) of an ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) term contextualising the free text “value”. Due to this nested object structure, DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) can be quite opaque to parse for the human reader but allows for easier programmatic processing of the objects. A full overview of the DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) schema can be found on the [DataTagSuite Github(URL_TO_INSERT_RECORD https://github.com/) repository (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository)](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/datatagsuite/schema).

### Ontology annotations

The provision for ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) annotations is at the core(URL_TO_INSERT_RECORD http://purl.uniprot.org/core/)(URL_TO_INSERT_RECORD https://core.ac.uk) of the DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format), with the smallest object available in the model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) being the `Annotation` schema, which simply consists of two key-value pairs: `value`, which can contain a text string(URL_TO_INSERT_RECORD https://string-db.org/) or number (to allow for coded values), and `valueIRI`, which contains a URI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)-format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ted string(URL_TO_INSERT_RECORD https://string-db.org/) representing a concept or ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) term associated with the value. It should be noted that the Annotation object has no required properties, so the valueIRI in particular can be empty. 

The model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) also provides an extension mechanism through a schema object called `CategoryValuesPair`. This allows the addition of extra properties to the entities in cases where there are no specific properties to deal with the desired property. In order to capture the semantics of the category, CategoryValuesPairs capture both a `category` as a free-text string(URL_TO_INSERT_RECORD https://string-db.org/) and a `categoryIRI` for the URI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986) of an associated ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) context. The `values` are of type `Annotation` and can therefore also have ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) annotations.

DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) does not prescribe the use of specific ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) in relation to various properties, although it would be advisable to include this type of restriction in a given implementation of the model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) in order to simply the interoperability between different objects of the same type.

### Encoding in JSON-LD

DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) objects are encoded in JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259)-LD(URL_TO_INSERT_RECORD https://json-ld.org/spec/latest/json-ld/), a method for encoding linked data in the open standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) file and data interchange format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259). JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259)-LD(URL_TO_INSERT_RECORD https://json-ld.org/spec/latest/json-ld/) is designed around the concept of a "context" to provide additional map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)pings from JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) to an RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format). DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) provides three sets of context map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)pings, to DC(URL_TO_INSERT_RECORD http://dublincore.org/documents/dces/)(URL_TO_INSERT_RECORD https://doi.org/10.25504/FAIRsharing.3nx7t)AT(URL_TO_INSERT_RECORD https://www.w3.org/TR/vocab-dcat/)(URL_TO_INSERT_RECORD http://cat.aii.caas.cn/), schema.org(URL_TO_INSERT_RECORD http://schema.org/) (SDO(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/1651)) and the OBO(URL_TO_INSERT_RECORD http://www.obofoundry.org/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059) Foundry(URL_TO_INSERT_RECORD http://www.obofoundry.org/) Ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact). None of the three sets of contexts individually cover all properties in the model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) but they can be used in combination to maximise the semantic linking of the model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format), likely to increase interoperability, for instance with DC(URL_TO_INSERT_RECORD http://dublincore.org/documents/dces/)(URL_TO_INSERT_RECORD https://doi.org/10.25504/FAIRsharing.3nx7t)AT(URL_TO_INSERT_RECORD https://www.w3.org/TR/vocab-dcat/)(URL_TO_INSERT_RECORD http://cat.aii.caas.cn/) based catalogues.



## Implementing DATS in a data catalogue

We implemented DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) v2.0 in the [IMI Translational Data Catalog(URL_TO_INSERT_RECORD https://datacatalog.elixir-luxembourg.org/)](https://datacatalog.elixir-luxembourg.org(URL_TO_INSERT_RECORD https://datacatalog.elixir-luxembourg.org/)/). The DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)'s flexibility presents both a benefit and a challenge in that some concepts could be encoded in a number of ways. Experimental materials for example can be encoded at both the Study level, in `Study.input` or at the Dataset level, in `Dataset.isAbout`. In order to encode metadata consistently and simplify indexing and display processes for the IMI Data Catalog(URL_TO_INSERT_RECORD https://datacatalog.elixir-luxembourg.org/), we therefore made a number of assumptions about how to encode certain metadata entities in the model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format).

### Assumptions

* Study and Dataset objects can't exist without a Project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project). This rule was necessary to provide a root for our indexing service.

* The Study object encodes informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion about the input materials to the experiment, such as study subjects in the case of clinical trials or biological molecules in the case of chemical assays. At this level, we collect cohort descriptions, sample sizes, sample sources, types of samples and diseases.
 
* The Dataset object encodes informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion about the dataset, including technical informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion such as version number, creation and update dates, data standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s and file types. The dataset also lists the experiment types that generated the data, the number and types of samples that contributed to the dataset and any diseases in the samples. These properties can be distinct from the ones at Study level as not all samples collected in a Study may be used to generate a given dataset, e.g. blood samples might be used for sequencing experiments, generating a sequencing dataset, while other tissue samples are used in imaging assays, generating an imaging dataset. The number of samples collected can be different from the cohort sample size (i.e. number of subject), either because multiple samples were collected from each subject or because some samples were excluded from the dataset for quality reasons.

* In the implementation of the model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format), preference as given to specific ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) in certain contexts, eg MO(URL_TO_INSERT_RECORD http://mged.sourceforge.net/ontologies/MGEDontology.php)NDO(URL_TO_INSERT_RECORD https://github.com/monarch-initiative/monarch-disease-ontology) for diseases, UBERO(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD https://open.med.harvard.edu/wiki/display/eaglei/Ontology)(URL_TO_INSERT_RECORD https://w3id.org/ro/)N(URL_TO_INSERT_RECORD http://uberon.org/) for anatomical components, NCIt(URL_TO_INSERT_RECORD https://ncit.nci.nih.gov), EFO(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO) and OBI(URL_TO_INSERT_RECORD http://obi-ontology.org/) for experiment types, UO(URL_TO_INSERT_RECORD https://github.com/bio-ontology-research-group/unit-ontology) for units etc.

---

## Conclusion

> * DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) is a flexible data model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) aimed at biomedical datasets.
> * DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications) utilises the power of JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259)-LD(URL_TO_INSERT_RECORD https://json-ld.org/spec/latest/json-ld/) to encode semantics at all levels of the model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format).
> * DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications)' flexibility does mean that consistent implementation of the model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) in a specific context requires assumptions to be made.


### What should I read next?
> * [Building a catalogue of datasets](./data-catalog.md) 
> * [Deploying the IMI data catalog](./data-catalog-deployment.md) 
> * [Introduction to terminologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)](../interoperability/introduction-terminologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)-ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact).md)

## References:

````{dropdown} **References**
```{footbibliography}
```
````

## Authors

````{authors_fairplus}
Danielle: Writing - original draft
Philippe: Writing - review & editing
````


## License
````{license_fairplus}
CC-BY-4.0
````

