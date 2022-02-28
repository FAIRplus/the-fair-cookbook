(fcb-infra-build-catalog)=
# Building a catalogue of datasets

````{panels_fairplus}
:identifier_text: FCB047
:identifier_link: 'https://w3id.org/faircookbook/FCB047'
:difficulty_level: 4
:recipe_type: hands_on
:reading_time_minutes: 60
:intended_audience: data_manager, data_scientist, software_developer, system_administrator  
:has_executable_code: yeah
:recipe_name: Building a catalogue of datasets 
```` 

## Main Objectives

The main purpose of this recipe is:

>  To detail the key elements for the creation of a `data catalogue` to enable data `findability` in an organisation.

We will cover the following points:

1. metadata model selection
2. annotation with controled vocabularies
3. ETL
4. data loading
5. data indexing
6. facet oriented searching
7. minting of stable, persistent and resolvable identifiers

---


## Graphical Overview


```{figure} data-catalog.md-figure1.mmd.png
---
name: data-catalog-figure1
alt: Building and populating a data catalogue
---
Building and populating a data catalogue
```

---

## Capability & Maturity Table 

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Findability | minimal | repeatable |
| Interoperability | minimal | repeatable |

---

## User Story
For **`role.Data Scientists`**, it is essential to be able to *`action.identify`* and *`action.discover`* datasets of potential relevance in the context of *`action.data integration`* and *`action.meta-analytical work`*.

For **`role.Database Managers`**, a lightweight solution is needed to support a shallow indexing supported fast ingest without intense curation, but good potential for data discovery. Works should rely on approved data standards.

For **`role.lab scientists`**, the key is to have a minimal burden when having to *`action.deposit`* a dataset to an institutional archive or simply *`action.register`* to dataset to the `data catalogue`. 


---
## Main body of the recipe

### What is a Data Catalogue?

A `Data Catalogue` is a resource meant to allow fast identification of `Data set`. In keeping with the familiar notion of catalogue, (be it that of an exhibition or that of brand products), the notion of `data catalogue` needs to be understood as the compendium of `short descriptive metadata elements` about an actual set of data. The `Data Index or Data Catalogue` **does not** store the datasets themselves but provides information about where the datasets can be obtained from. Therefore, `Data Catalogues` are often used to index the content of '`Data Repositories` and ` Data Archives`, which provide hosting solutions for the actual datasets, which are often organized (but not always)' around specific `data types` or `data production modalities` (e.g. NMR Imaging, Confocal microscopy imaging, Nucleic Acid sequence archives and so on.)
 

### What are the standards supporting establishing a data catalogue?

`Data Catalogues` have been identified as critical infrastructure and therefore a number of model exist to support their implementation.
1. DATS:
The Data Article Tag Suite model<!-- TODO add a link to corresponding document --> has been developed during the NIH-BD2K projects and underpins the [datamed catalogue](https://datamed.org/), the aim of which was to produce a prototype of a [`Pubmed for Datasets`](https://pubmed.ncbi.nlm.nih.gov/29346583/).

3. DCAT:
In the world of semantic web technologies, The W3C DCAT specifications<!-- TODO add a link to corresponding document --> (v1 and the newly released version 2) provide a vocabulary to express `data catalogue metadata` in **RDF**.
3. Schema.org:
The vocabulary developed by the consortium of search engines has defined a metadata profile for [`Dataset`](https://schema.org/Dataset), [`Data Catalogue`](https://schema.org/DataCatalog)


### How are Data Catalogue populated?

A number data Indexes/Data Catalogue are populated by harvest Dataset metadata from primary Data Repositories or harvesting JSON-LD files served by these same pages for rapid, shallow indexing. The former method is often richer but requires more 

### What are examples of Data Catalogues?

* Commercial solutions:

    *  [Collibra](https://www.collibra.com/data-catalog)

* Open source solutions:

    * [NIH DataMed](https://datamed.org/)
    * [EMBL-EBI OMICS-DI](https://www.omicsdi.org/)
    * [Bayer AG Colid](https://bayer-group.github.io/COLID-Documentation/)


---


## Table of Data Standards

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| JSON<!-- TODO add a link to corresponding document -->  | <!-- TODO add a link to corresponding document -->  | <!-- TODO add a link to corresponding document -->  |
| RDF<!-- TODO add a link to corresponding document -->  | DCAT v1<!-- TODO add a link to corresponding document -->  | DATS<!-- TODO add a link to corresponding document -->  |
| RDF<!-- TODO add a link to corresponding document -->  | DCAT v2<!-- TODO add a link to corresponding document -->  | DATS<!-- TODO add a link to corresponding document -->  |
| JSON-LD<!-- TODO add a link to corresponding document -->  | Schema.org<!-- TODO add a link to corresponding document -->  | <!-- TODO add a link to corresponding document -->  |


---

    
## Conclusion

This recipe introduced the general concept of data catalogue and why they constitute a key capability to deliver data discoverability.

### What should I read next?
We encourage the readers to either delve deeper into the specific of data catalogues by consulting the following recipes

* {ref}`fcb-infra-imi-cat-deploy`
<!-- * TODO Deploying the FAIRPORT data catalogue {ref}` TODO fcb-infra-fairport-deploy` --> 
<!-- * TODO Deploying the GA4GH Beacon endpoint {ref}` TODO fcb-infra-beacon-deploy`     -->


For the readership interested in finding out about additional capabilities needed to enhance other aspects of FAIR such interoperability and reusability, see the following:

* {ref}`fcb-find-seo`
* {ref}`fcb-interop-metadataprofile`


---

## Authors

<!-- TODO seems unlikely that all authors did review, but noone the original draft. Clarify -->
````{authors_fairplus}
Philippe: Writing - Review & Editing
Susanna: Writing - Review & Editing, Funding acquisition
````


---

## License

````{license_fairplus}
CC-BY-4.0
````
