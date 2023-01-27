(fcb-infra-build-catalog)=
# Building a catalogue of datasets

````{panels_fairplus}
:identifier_text: FCB047
:identifier_link: 'https://w3id.org/faircookbook/FCB047'
:difficulty_level: 4
:recipe_type: hands_on
:reading_time_minutes: 60
:intended_audience: data_manager, data_scientist, software_developer, system_administrator  
:maturity_level: 2
:maturity_indicator: 24
:has_executable_code: nope
:recipe_name: Building a catalogue of datasets 
```` 

## Main Objectives

The main purpose of this recipe is:

>  To detail the key elements for the creation of a **data catalogue** to enable data **findability** in an organisation.

We will cover the following points:

1. metadata model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)  selection
2. annotation with controlled vocabularies
3. ETL
4. data loading
5. data indexing
6. facet oriented search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ing
7. minting of stable, persistent and resolvable identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s

```{tabbed} Table of Data Standards
| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| JSON<!-- TODO add a link to corresponding document -->  | <!-- TODO add a link to corresponding document -->  | <!-- TODO add a link to corresponding document -->  |
| RDF<!-- TODO add a link to corresponding document -->  | DCAT v1<!-- TODO add a link to corresponding document -->  | DATS<!-- TODO add a link to corresponding document -->  |
| RDF<!-- TODO add a link to corresponding document -->  | DCAT v2<!-- TODO add a link to corresponding document -->  | DATS<!-- TODO add a link to corresponding document -->  |
| JSON-LD<!-- TODO add a link to corresponding document -->  | Schema.org<!-- TODO add a link to corresponding document -->  | <!-- TODO add a link to corresponding document -->  |
``` 

---


## Graphical Overview


```{figure} ../../../images/data-catalog-md-figure1.png
---
name: data-catalog-figure1
alt: Building and populating a data catalogue
---
Building and populating a data catalogue
```

---

## User Story
For **role.Data Scientists**, it is essential to be able to *action.identify* and *action.discover* datasets of potential
relevance in the context of *action.data integration* and *action.meta-analytical work*.

For **role.Database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)  Managers**, a lightweight solution is needed to support a shallow indexing supported fast ingest 
without intense curation, but good potential for data discovery. Works should rely on approved data standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) s.

For **role.lab scientists**, the key is to have a minimal burden when having to *action.deposit* a dataset to an 
institution (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=institution) al arch(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ive or simply *action.register* to dataset to the **data catalogue**. 


---
## Main body of the recipe

### What is a Data Catalogue?

A **Data Catalogue** is a resource meant to allow fast identification of **Data set**. In keeping with the fam(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#fam)iliar notion 
of catalogue, (be it that of an exhibition or that of brand products), the notion of **data catalogue** needs to be
understood as the compendium of **short descriptive metadata elements** about an actual set of data. The 
**Data Index or Data Catalogue** ***does not*** store the datasets themselves but provides informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion
about where the datasets can be obtained from. Therefore, **Data Catalogues** are often used to index the content of
'**Data Repositories (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository) ** and ** Data Arch(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ives**, which provide hosting(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) solutions for the actual datasets, which are often
organized (but not always)' around specific **data types** or **data production modalities** 
(e.g. NMR Imaging, Confocal microscopy imaging, Nucleic Acid sequence arch(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ives and so on.)
 

### What are the standards supporting establishing a data catalogue?

**Data Catalogues** have been identified as critical infrastructure and therefore a number of model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)  exist to support their implementation.
1. DATS(URL_TO_INSERT_RECORD https://github.com/biocaddie/WG3-MetadataSpecifications):
The Data Article Tag Suite model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) <!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO add a link to corresponding document --> has been developed(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) during the 
NIH(URL_TO_INSERT_RECORD http://sweetgum.nybg.org/science/ih/)-BD2K project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project) s and underpins the [datamed(URL_TO_INSERT_RECORD https://datamed.org) catalogue](https://datamed.org(URL_TO_INSERT_RECORD https://datamed.org)/), the aim of which was to produce a 
prototype of a [**Pubmed(URL_TO_INSERT_RECORD http://www.ncbi.nlm.nih.gov/pubmed/) for Datasets**](https://pubmed.ncbi.nlm.nih.gov/29346583/).

2. DC(URL_TO_INSERT_RECORD http://dublincore.org/documents/dces/)(URL_TO_INSERT_RECORD https://doi.org/10.25504/FAIRsharing.3nx7t)AT(URL_TO_INSERT_RECORD https://www.w3.org/TR/vocab-dcat/)(URL_TO_INSERT_RECORD http://cat.aii.caas.cn/):
In the world of semantic web technologies, The W3C DC(URL_TO_INSERT_RECORD http://dublincore.org/documents/dces/)(URL_TO_INSERT_RECORD https://doi.org/10.25504/FAIRsharing.3nx7t)AT(URL_TO_INSERT_RECORD https://www.w3.org/TR/vocab-dcat/)(URL_TO_INSERT_RECORD http://cat.aii.caas.cn/) specifications<!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO add a link to corresponding document -->
(v1 and the newly released version 2) provide a vocabulary to express **data catalogue metadata** in **RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/)**.
3. Schema.org(URL_TO_INSERT_RECORD http://schema.org/)(URL_TO_INSERT_RECORD http://schema.org/):
The vocabulary developed(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) by the consortium of search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) engines has defined a metadata profile for [**Dataset**](https://schema.org(URL_TO_INSERT_RECORD http://schema.org/)/Dataset),
[**Data Catalogue**](https://schema.org(URL_TO_INSERT_RECORD http://schema.org/)/DataCatalog)


### How are Data Catalogue populated?

A number data Indexes/Data Catalogue are populated by harvest Dataset metadata from primary Data Repositories (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository)  or harvesting(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259)-LD(URL_TO_INSERT_RECORD https://json-ld.org/spec/latest/json-ld/) files served by these same pages for rapid, shallow indexing. The former method is often richer but requires more 

### What are examples of Data Catalogues?

* Commercial solutions:

    *  [Collibra](https://www.collibra.com/data-catalog)

* Open source solutions:

    * [NIH(URL_TO_INSERT_RECORD http://sweetgum.nybg.org/science/ih/) DataMed(URL_TO_INSERT_RECORD https://datamed.org)(URL_TO_INSERT_RECORD https://datamed.org)](https://datamed.org(URL_TO_INSERT_RECORD https://datamed.org)/)
    * [EMB(URL_TO_INSERT_RECORD http://www.Metabase.net)L-EBI OMICS-DI](https://www.omicsdi.org/)
    * [Bayer AG Colid](https://bayer-group.github.io/COLID-Documentation/)


---

    
## Conclusion

This recipe introduced the general concept of data catalogue and why they constitute a key capability to deliver data discoverability.

### What to read next?

We encourage the readers to either delve deeper into the specific of data catalogues by consulting the following recipes

* {ref}`fcb-infra-imi-cat-deploy`
<!-- * TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO Deploying the FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)PO(URL_TO_INSERT_RECORD http://plantontology.org/)(URL_TO_INSERT_RECORD https://bioportal.bioontology.org/ontologies/RPO)RT data catalogue {ref}` TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO fcb-infra-fairport-deploy` --> 
<!-- * TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO Deploying the GA4GH(URL_TO_INSERT_RECORD https://github.com/ga4gh/schemas) Beacon(URL_TO_INSERT_RECORD http://docs.genomebeacons.org) endpoint {ref}` TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO fcb-infra-beacon(URL_TO_INSERT_RECORD http://docs.genomebeacons.org)(URL_TO_INSERT_RECORD http://docs.genomebeacons.org)-deploy`     -->

For the readership interested in finding out about additional capabilities needed to enhance other aspects of FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) such
interoperability and reusability, see the following:

* {ref}`fcb-find-seo`
* {ref}`fcb-interop-metadataprofile`

````{rdmkit_panel}
````


## References
````{dropdown} **References**
````

## Authors

<!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO seems unlikely that all authors did review, but no-one the original draft. Clarify -->
````{authors_fairplus}
Philippe: Writing - Review & Editing
Susanna: Writing - Review & Editing, Funding acquisition
````


## License

````{license_fairplus}
CC-BY-4.0
````
