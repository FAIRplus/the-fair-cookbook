(fcb-interop-oxo)=
# Ontology mapping with Ontology Xref Service (OxO)

<br/>


````{panels_fairplus}
:identifier_text: FCB076
:identifier_link: 'https://w3id.org/faircookbook/FCB076'
:difficulty_level: 3
:recipe_type: hands_on
:reading_time_minutes: 30
:intended_audience: ontologist, terminology_manager, data_scientist, data_curator, data_manager 
:maturity_level: 1
:maturity_indicator: 1
:has_executable_code: nope
:recipe_name: Mapping Ontologies with OxO, EBI Ontology Xref Service
```` 

---

## Main Objectives

Different ontology (URL_TO_INSERT_TERM_5586 https://fairsharing.org/search?recordType=terminology_artefact)  terms can describe the same concept, which makes it difficult for data integration.
`Ontology (URL_TO_INSERT_TERM_5587 https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD_5589 https://fairsharing.org/FAIRsharing.53edcc) ping`, or ontology (URL_TO_INSERT_TERM_5588 https://fairsharing.org/search?recordType=terminology_artefact)  alignment, is the process of determining correspondences between equivalent
concepts in alternative ontologies (URL_TO_INSERT_TERM_5590 https://fairsharing.org/search?recordType=terminology_artefact)  and distinct vocabularies. 

OxO map (URL_TO_INSERT_RECORD_5593 https://fairsharing.org/FAIRsharing.53edcc) s terms in different ontologies (URL_TO_INSERT_TERM_5592 https://fairsharing.org/search?recordType=terminology_artefact) , vocabularies and coding standard (URL_TO_INSERT_TERM_5591 https://fairsharing.org/search?fairsharingRegistry=Standard) s using evidence collected mainly 
from the Ontology (URL_TO_INSERT_TERM_5594 https://fairsharing.org/search?recordType=terminology_artefact)  Lookup Service (URL_TO_INSERT_RECORD_5595 https://fairsharing.org/FAIRsharing.Mkl9RR)  (OLS), Unified Medical Language System (UMLS), but also from other sources. 

This recipe shows how to use the [EMBL-EBI Ontology (URL_TO_INSERT_TERM_5596 https://fairsharing.org/search?recordType=terminology_artefact)  Xref Service (OxO)](https://www.ebi.ac.uk/spot/oxo (URL_TO_INSERT_RECORD_5597 https://fairsharing.org/FAIRsharing.0c6fea) /) service
to map (URL_TO_INSERT_RECORD_5599 https://fairsharing.org/FAIRsharing.53edcc)  ontology (URL_TO_INSERT_TERM_5598 https://fairsharing.org/search?recordType=terminology_artefact)  terms between source and target vocabularies {footcite}`oxo` .

## Graphical Overview


````{dropdown} 
:open:
```{figure} ontology-align-oxo.mmd.svg
---
height: 550px
name: Aligning Ontologies (URL_TO_INSERT_TERM_5600 https://fairsharing.org/search?recordType=terminology_artefact) 
alt: An overview of the ontology (URL_TO_INSERT_TERM_5601 https://fairsharing.org/search?recordType=terminology_artefact)  alignment process
---
An overview of the ontology (URL_TO_INSERT_TERM_5602 https://fairsharing.org/search?recordType=terminology_artefact)  alignment process
```
````


## Requirements
* recipe dependency:
   * {ref}`fcb-introduction-terminologies (URL_TO_INSERT_TERM_5603 https://fairsharing.org/search?recordType=terminology_artefact) -ontologies (URL_TO_INSERT_TERM_5604 https://fairsharing.org/search?recordType=terminology_artefact) `
   * {ref}`fcb-selecting-ontologies (URL_TO_INSERT_TERM_5605 https://fairsharing.org/search?recordType=terminology_artefact) `
* knowledge requirements:
   * Fam (URL_TO_INSERT_RECORD_5606 https://fairsharing.org/FAIRsharing.d0886a) iliar with metadata curation
   * Fam (URL_TO_INSERT_RECORD_5608 https://fairsharing.org/FAIRsharing.d0886a) iliar with ontology (URL_TO_INSERT_TERM_5607 https://fairsharing.org/search?recordType=terminology_artefact)  and other vocabularies
* technical requirements:
    * Experience with API or Bash scripts allows users to try the automated solutions.



## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [ID mapping](http://edamontology.org (URL_TO_INSERT_RECORD_5611 https://fairsharing.org/FAIRsharing.a6r7zs) /operation_3282)  | [Ontology (URL_TO_INSERT_TERM_5609 https://fairsharing.org/search?recordType=terminology_artefact)  term](http://edamontology.org (URL_TO_INSERT_RECORD_5612 https://fairsharing.org/FAIRsharing.a6r7zs) /data_0966)  | [Ontology (URL_TO_INSERT_TERM_5610 https://fairsharing.org/search?recordType=terminology_artefact)  term](http://edamontology.org (URL_TO_INSERT_RECORD_5613 https://fairsharing.org/FAIRsharing.a6r7zs) /data_0966)  |
| [Annotation](http://edamontology.org (URL_TO_INSERT_RECORD_5616 https://fairsharing.org/FAIRsharing.a6r7zs) /operation_0226)  | [Ontology (URL_TO_INSERT_TERM_5614 https://fairsharing.org/search?recordType=terminology_artefact)  term](http://edamontology.org (URL_TO_INSERT_RECORD_5617 https://fairsharing.org/FAIRsharing.a6r7zs) /data_0966)  | [Ontology (URL_TO_INSERT_TERM_5615 https://fairsharing.org/search?recordType=terminology_artefact)  term](http://edamontology.org (URL_TO_INSERT_RECORD_5618 https://fairsharing.org/FAIRsharing.a6r7zs) /data_0966)  |

## Table of Data Standards

| Data Format (URL_TO_INSERT_TERM_5620 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_5621 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_5619 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
|  | [Mondo Disease ontology (URL_TO_INSERT_RECORD_5622 https://fairsharing.org/FAIRsharing.8b6wfq) ](https://www.ebi.ac.uk/ols/ontologies/mondo)  | |
| | [Human Disease ontology (URL_TO_INSERT_RECORD_5623 https://fairsharing.org/FAIRsharing.8b6wfq) ](https://www.ebi.ac.uk/ols/ontologies/doid)  |  |
|| [Medical Subject Headings (URL_TO_INSERT_RECORD_5624 https://fairsharing.org/FAIRsharing.qnkw45) ](https://meshb.nlm.nih.gov/search)


## Using EMBL-EBI OXO

Ontology (URL_TO_INSERT_TERM_5625 https://fairsharing.org/search?recordType=terminology_artefact)  cross Ontology (URL_TO_INSERT_TERM_5626 https://fairsharing.org/search?recordType=terminology_artefact)  or OxO (URL_TO_INSERT_RECORD_5627 https://fairsharing.org/FAIRsharing.0c6fea)  service is available from a web interface or a programmatic interface. The following sections show both.

### OXO Web Interface:

#### Step 1: Identify source vocabulary and target vocabulary

For pathology data annotation, vocabularies, such as [MeSH](https://meshb.nlm.nih.gov/search), [NCI thesaurus (URL_TO_INSERT_RECORD_5630 https://fairsharing.org/FAIRsharing.4cvwxa) ](https://www.ebi.ac.uk/ols/ontologies/ncit), [ICD-10](https://www.who.int (URL_TO_INSERT_RECORD_5637 https://fairsharing.org/3498) /standards/classifications/classification-of-diseases), [UMLS](https://www.nlm.nih.gov/research/umls/index.html), [Human Disease Ontology (URL_TO_INSERT_RECORD_5634 https://fairsharing.org/FAIRsharing.8b6wfq) (DOID)](https://www.ebi.ac.uk/ols/ontologies/doid), and [MONDO (URL_TO_INSERT_RECORD_5632 https://fairsharing.org/FAIRsharing.b2979t)  disease ontology (URL_TO_INSERT_RECORD_5635 https://fairsharing.org/FAIRsharing.8b6wfq) ](https://www.ebi.ac.uk/ols/ontologies/mondo), are widely used. In this example, we use **MeSH and DOI (URL_TO_INSERT_RECORD_5629 https://fairsharing.org/FAIRsharing.hFLKCn) D (URL_TO_INSERT_RECORD_5636 https://fairsharing.org/FAIRsharing.8b6wfq) ** as `source vocabularies` and **MONDO (URL_TO_INSERT_RECORD_5633 https://fairsharing.org/FAIRsharing.b2979t) ** as the `target vocabulary` to demonstrate the ontology (URL_TO_INSERT_TERM_5628 https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD_5631 https://fairsharing.org/FAIRsharing.53edcc) ping workflow. 

Obviously, a target vocabulary needs to be selected before map (URL_TO_INSERT_RECORD_5640 https://fairsharing.org/FAIRsharing.53edcc) ping. A variety of factors can influence the selection of a terminology (URL_TO_INSERT_TERM_5639 https://fairsharing.org/search?recordType=terminology_artefact)  resource for a specific purpose or curation context. For more informat (URL_TO_INSERT_TERM_5638 https://fairsharing.org/search?recordType=model_and_format) ion about this topic, more detailed guidance on how to select vocabularies can be found [here](https://fairplus.github.io/the-fair-cookbook/content/recipes/interoperability/selecting-ontologies.html). 


OxO allows users to explore the map (URL_TO_INSERT_RECORD_5643 https://fairsharing.org/FAIRsharing.53edcc) ping status between the target vocabulary and other vocabularies. Figure 1 shows how terms in MONDO (URL_TO_INSERT_RECORD_5646 https://fairsharing.org/FAIRsharing.b2979t)  are linked to terms in other ontologies (URL_TO_INSERT_TERM_5641 https://fairsharing.org/search?recordType=terminology_artefact) . MONDO (URL_TO_INSERT_RECORD_5647 https://fairsharing.org/FAIRsharing.b2979t)  has over 16,000 map (URL_TO_INSERT_RECORD_5644 https://fairsharing.org/FAIRsharing.53edcc) pings to terms in UMLS. It is also map (URL_TO_INSERT_RECORD_5645 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_5649 https://fairsharing.org/FAIRsharing.31385c)  to terms in DOI (URL_TO_INSERT_RECORD_5642 https://fairsharing.org/FAIRsharing.hFLKCn) D (URL_TO_INSERT_RECORD_5648 https://fairsharing.org/FAIRsharing.8b6wfq) , Ophanet, OMIM (URL_TO_INSERT_RECORD_5650 https://fairsharing.org/FAIRsharing.9qkaz9) , MeSH, etc.


````{dropdown} 
:open:
```{figure} ../../../images/bi5WoIf.png
---
width: 600px
name: OxO (URL_TO_INSERT_RECORD_5651 https://fairsharing.org/FAIRsharing.0c6fea)  summary result overview
alt: OxO (URL_TO_INSERT_RECORD_5652 https://fairsharing.org/FAIRsharing.0c6fea)  summary result overview
---
OxO summary result overview.
```
````

### Step 2: Provide the source vocabulary term ID

OxO takes ontology (URL_TO_INSERT_TERM_5653 https://fairsharing.org/search?recordType=terminology_artefact)  term IDs as inputs for ontology (URL_TO_INSERT_TERM_5654 https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD_5656 https://fairsharing.org/FAIRsharing.53edcc) ping, which assumes the (meta)data has been annotated. If the data is not annotated, please check the ontology (URL_TO_INSERT_TERM_5655 https://fairsharing.org/search?recordType=terminology_artefact)  annotation recipe first. 

In this example, we use terms for ***type 2 diabetes*** from 2 distinct sources. The corresponding term IDs are listed in the table below.

|Text|Corresponding term in MeSH| Corresponding term in DOI (URL_TO_INSERT_RECORD_5657 https://fairsharing.org/FAIRsharing.hFLKCn) D (URL_TO_INSERT_RECORD_5658 https://fairsharing.org/FAIRsharing.8b6wfq) |
|--|--|--|
|type 2 diabetes|[MeSH:D003924](https://www.ncbi.nlm.nih.gov/mesh/68003924)|[DOID:9352](https://www.ebi.ac.uk/ols/ontologies/doid/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FDOID_9352)

### Step 3: Perform mapping

Figure 2 shows how to map (URL_TO_INSERT_RECORD_5661 https://fairsharing.org/FAIRsharing.53edcc)  the MeSH and DOI (URL_TO_INSERT_RECORD_5660 https://fairsharing.org/FAIRsharing.hFLKCn) D (URL_TO_INSERT_RECORD_5664 https://fairsharing.org/FAIRsharing.8b6wfq)  terms to the MONDO (URL_TO_INSERT_RECORD_5662 https://fairsharing.org/FAIRsharing.b2979t)  disease ontology (URL_TO_INSERT_TERM_5659 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_5663 https://fairsharing.org/FAIRsharing.8b6wfq) . Users are expected to:
- specify the target ontology (URL_TO_INSERT_TERM_5665 https://fairsharing.org/search?recordType=terminology_artefact) 
- provide a list of source term IDs
- indicate the expected map (URL_TO_INSERT_RECORD_5666 https://fairsharing.org/FAIRsharing.53edcc) ping distance.

In this example, we set the `map (URL_TO_INSERT_RECORD_5667 https://fairsharing.org/FAIRsharing.53edcc) ping distance` to 1, which uses high confidence map (URL_TO_INSERT_RECORD_5668 https://fairsharing.org/FAIRsharing.53edcc) ping evidence only.
Having greater map (URL_TO_INSERT_RECORD_5669 https://fairsharing.org/FAIRsharing.53edcc) ping distance returns more map (URL_TO_INSERT_RECORD_5670 https://fairsharing.org/FAIRsharing.53edcc) pings but decreases the map (URL_TO_INSERT_RECORD_5671 https://fairsharing.org/FAIRsharing.53edcc) ping confidence. 


````{dropdown} 
:open:
```{figure} ../../../images/1EepmN9.png
---
width: 600px
name: OxO (URL_TO_INSERT_RECORD_5673 https://fairsharing.org/FAIRsharing.0c6fea)  map (URL_TO_INSERT_RECORD_5672 https://fairsharing.org/FAIRsharing.53edcc) ping with direct user inputs.
alt: OxO (URL_TO_INSERT_RECORD_5675 https://fairsharing.org/FAIRsharing.0c6fea)  map (URL_TO_INSERT_RECORD_5674 https://fairsharing.org/FAIRsharing.53edcc) ping with direct user inputs
---
OxO map (URL_TO_INSERT_RECORD_5676 https://fairsharing.org/FAIRsharing.53edcc) ping with direct user inputs
```
````

Figure 3 shows the corresponding map (URL_TO_INSERT_RECORD_5677 https://fairsharing.org/FAIRsharing.53edcc) ping results. Both terms have been map (URL_TO_INSERT_RECORD_5678 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_5680 https://fairsharing.org/FAIRsharing.31385c)  to 'MONDO (URL_TO_INSERT_RECORD_5679 https://fairsharing.org/FAIRsharing.b2979t) :0005148'. The results can be downloaded as flat-table(tsv) files.


````{dropdown} 
:open:
```{figure} ../../../images/l1z8OgL.png
---
width: 600px
name: OxO (URL_TO_INSERT_RECORD_5682 https://fairsharing.org/FAIRsharing.0c6fea)  map (URL_TO_INSERT_RECORD_5681 https://fairsharing.org/FAIRsharing.53edcc) ping results tabular view
alt: OxO (URL_TO_INSERT_RECORD_5684 https://fairsharing.org/FAIRsharing.0c6fea)  map (URL_TO_INSERT_RECORD_5683 https://fairsharing.org/FAIRsharing.53edcc) ping results tabular view
---
OxO map (URL_TO_INSERT_RECORD_5685 https://fairsharing.org/FAIRsharing.53edcc) ping results tabular view.
```
````

### Step 4: Review mapping results

To ensure the quality of the map (URL_TO_INSERT_RECORD_5690 https://fairsharing.org/FAIRsharing.53edcc) ping, users are recommended to review the map (URL_TO_INSERT_RECORD_5691 https://fairsharing.org/FAIRsharing.53edcc) ping results, especially when the map (URL_TO_INSERT_RECORD_5692 https://fairsharing.org/FAIRsharing.53edcc) ping distance increases. OxO (URL_TO_INSERT_RECORD_5693 https://fairsharing.org/FAIRsharing.0c6fea)  allows users to explore vocabulary term relationships (see figure 4) by providing a network view of all linked terms. Users can also find more informat (URL_TO_INSERT_TERM_5686 https://fairsharing.org/search?recordType=model_and_format) ion about each term in the [Ontology (URL_TO_INSERT_TERM_5687 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_5688 https://fairsharing.org/FAIRsharing.Mkl9RR) ](https://www.ebi.ac.uk/ols/index (URL_TO_INSERT_RECORD_5689 https://fairsharing.org/FAIRsharing.Mkl9RR) ).

````{dropdown} 
:open:
```{figure} ../../../images/937iuPV.png
---
width: 600px
name: OxO (URL_TO_INSERT_RECORD_5696 https://fairsharing.org/FAIRsharing.0c6fea)  map (URL_TO_INSERT_RECORD_5694 https://fairsharing.org/FAIRsharing.53edcc) ping results review - MONDO (URL_TO_INSERT_RECORD_5695 https://fairsharing.org/FAIRsharing.b2979t)  example
alt: OxO (URL_TO_INSERT_RECORD_5699 https://fairsharing.org/FAIRsharing.0c6fea)  map (URL_TO_INSERT_RECORD_5697 https://fairsharing.org/FAIRsharing.53edcc) ping results review - MONDO (URL_TO_INSERT_RECORD_5698 https://fairsharing.org/FAIRsharing.b2979t)  example
---
OxO map (URL_TO_INSERT_RECORD_5700 https://fairsharing.org/FAIRsharing.53edcc) ping results review - MONDO (URL_TO_INSERT_RECORD_5701 https://fairsharing.org/FAIRsharing.b2979t)  example.
```
````

## Using OxO service programmatically

Besides the graphical user interface offered by OxO (URL_TO_INSERT_RECORD_5702 https://fairsharing.org/FAIRsharing.0c6fea)  at EMBL-EBI, a REST style API is also available.
It is therefore possible to invoke the map (URL_TO_INSERT_RECORD_5703 https://fairsharing.org/FAIRsharing.53edcc) ping service from the command line. See the [OxO API documentation](https://www.ebi.ac.uk/spot/oxo (URL_TO_INSERT_RECORD_5704 https://fairsharing.org/FAIRsharing.0c6fea) /docs/api) page.

In the following code snippet, an API request invoked via `curl` performed the same map (URL_TO_INSERT_RECORD_5705 https://fairsharing.org/FAIRsharing.53edcc) ping presented in the section above, at step 3:

```bash
curl 'https://www.ebi.ac.uk/spot/oxo/api/search' -i 
-X POST 
-H 'Content-Type: application/json' 
-H 'Accept: application/json' 
-d '{
  "ids" : [ "DOID:9352","MeSH:D003924"],
  "inputSource" : null,
  "mappingTarget" : [ "MONDO" ],
  "mappingSource" : [ "MONDO" ],
  "distance" : 1
}'
```

The corresponding results are as follows:

```bash
{
      "queryId" : "DOID:9352",
      "querySource" : null,
      "curie" : "DOID:9352",
      "label" : "type 2 diabetes mellitus",
      "mappingResponseList" : [ {
        "curie" : "MONDO:0005148",
        "label" : "type 2 diabetes mellitus",
        "sourcePrefixes" : [ "MONDO" ],
        "targetPrefix" : "MONDO",
        "distance" : 1
      } ],
      "_links" : {
        "self" : {
          "href" : "https://www.ebi.ac.uk/spot/oxo/api/terms/DOID:9352"
        },
        "mappings" : {
          "href" : "https://www.ebi.ac.uk/spot/oxo/api/mappings?fromId=DOID:9352"
        }
      }
    }
```



### Common questions about OxO

1. What about incorrect map (URL_TO_INSERT_RECORD_5706 https://fairsharing.org/FAIRsharing.53edcc) pings?

    OxO (URL_TO_INSERT_RECORD_5711 https://fairsharing.org/FAIRsharing.0c6fea)  imports term map (URL_TO_INSERT_RECORD_5710 https://fairsharing.org/FAIRsharing.53edcc) ping informat (URL_TO_INSERT_TERM_5708 https://fairsharing.org/search?recordType=model_and_format) ion from ontologies (URL_TO_INSERT_TERM_5709 https://fairsharing.org/search?recordType=terminology_artefact)  and other curated database (URL_TO_INSERT_TERM_5707 https://fairsharing.org/search?fairsharingRegistry=Database) s. 
    **It doesn't validate the map (URL_TO_INSERT_RECORD_5712 https://fairsharing.org/FAIRsharing.53edcc) ping evidence**.
    Users are recommended to check the map (URL_TO_INSERT_RECORD_5713 https://fairsharing.org/FAIRsharing.53edcc) ping results manually, especially when the map (URL_TO_INSERT_RECORD_5714 https://fairsharing.org/FAIRsharing.53edcc) ping distance is above 1.
    
2. Why is no map (URL_TO_INSERT_RECORD_5715 https://fairsharing.org/FAIRsharing.53edcc) ping found?

    OxO (URL_TO_INSERT_RECORD_5721 https://fairsharing.org/FAIRsharing.0c6fea)  relies on the ontology (URL_TO_INSERT_TERM_5717 https://fairsharing.org/search?recordType=terminology_artefact)  and other curated database (URL_TO_INSERT_TERM_5716 https://fairsharing.org/search?fairsharingRegistry=Database) s to improve the map (URL_TO_INSERT_RECORD_5719 https://fairsharing.org/FAIRsharing.53edcc) ping coverage. Some terms describing the same concept might not be aligned in OxO (URL_TO_INSERT_RECORD_5722 https://fairsharing.org/FAIRsharing.0c6fea) . In this case, users are recommended to identify possible map (URL_TO_INSERT_RECORD_5720 https://fairsharing.org/FAIRsharing.53edcc) pings by search (URL_TO_INSERT_RECORD_5723 https://fairsharing.org/FAIRsharing.52b22c) ing in OLS (URL_TO_INSERT_RECORD_5718 https://fairsharing.org/FAIRsharing.Mkl9RR) . 
    
    To help the ontology (URL_TO_INSERT_TERM_5724 https://fairsharing.org/search?recordType=terminology_artefact)  community improve the map (URL_TO_INSERT_RECORD_5726 https://fairsharing.org/FAIRsharing.53edcc) ping, users can also submit an update request in corresponding ontologies (URL_TO_INSERT_TERM_5725 https://fairsharing.org/search?recordType=terminology_artefact) . The guidance can be found here {ref}`fcb-interop-ontorequest`
    
3. Ontology (URL_TO_INSERT_TERM_5728 https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD_5729 https://fairsharing.org/FAIRsharing.53edcc) ping service for internal database (URL_TO_INSERT_TERM_5727 https://fairsharing.org/search?fairsharingRegistry=Database) s

    OxO (URL_TO_INSERT_RECORD_5732 https://fairsharing.org/FAIRsharing.0c6fea)  has been dockerized for local deployment and licensed under [Apache License 2.0](https://github.com (URL_TO_INSERT_RECORD_5730 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/OXO/blob/master/LICENSE). The source code can be found [here](https://github.com (URL_TO_INSERT_RECORD_5731 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/OXO).


## Conclusion

This recipe presented OxO (URL_TO_INSERT_RECORD_5737 https://fairsharing.org/FAIRsharing.0c6fea) , EMBL-EBI tool for performing ontology (URL_TO_INSERT_TERM_5733 https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD_5735 https://fairsharing.org/FAIRsharing.53edcc) ping as an example to demonstrate the ontology (URL_TO_INSERT_TERM_5734 https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD_5736 https://fairsharing.org/FAIRsharing.53edcc) ping workflow.
In the context of a FAIR (URL_TO_INSERT_RECORD_5739 https://fairsharing.org/FAIRsharing.WWI10U) ification workflow, a tool such as OxO (URL_TO_INSERT_RECORD_5738 https://fairsharing.org/FAIRsharing.0c6fea)  comes particurlary handy to augment a dataset with cross-references or replace an annotation set with another in a data integration exercice for instance. 

### What to read next?

* [How to build a data dictionary?](fcb-interop-datadictionary)
* [How to build an ontology (URL_TO_INSERT_TERM_5740 https://fairsharing.org/search?recordType=terminology_artefact)  using robot?](fcb-interop-ontorobot)

````{rdmkit_panel}
````


## References
````{dropdown} **References**
```{footbibliography}
```
````


## Authors

````{authors_fairplus}
Fuqi: Writing - Original Draft
Karsten: Writing - Original Draft
Peter: Writing - Original Draft
Philippe: Writing - Review & Editing
````


## License

````{license_fairplus}
CC-BY-4.0
````
