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

Different ontology terms can describe the same concept, which makes it difficult for data integration.
`Ontology mapping`, or ontology alignment, is the process of determining correspondences between equivalent
concepts in alternative ontologies and distinct vocabularies. 

OxO maps terms in different ontologies, vocabularies and coding standards using evidence collected mainly 
from the Ontology Lookup Service (OLS), Unified Medical Language System (UMLS), but also from other sources. 

This recipe shows how to use the [EMBL-EBI Ontology Xref Service (OxO)](https://www.ebi.ac.uk/spot/oxo/) service
to map ontology terms between source and target vocabularies {footcite}`oxo` .

## Graphical Overview


````{dropdown} 
:open:
```{figure} ontology-align-oxo.mmd.svg
---
height: 550px
name: Aligning Ontologies
alt: An overview of the ontology alignment process
---
An overview of the ontology alignment process
```
````


## Requirements
* recipe dependency:
   * {ref}`fcb-introduction-terminologies-ontologies`
   * {ref}`fcb-selecting-ontologies`
* knowledge requirements:
   * Familiar with metadata curation
   * Familiar with ontology and other vocabularies
* technical requirements:
    * Experience with API or Bash scripts allows users to try the automated solutions.



## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [ID mapping](http://edamontology.org/operation_3282)  | [Ontology term](http://edamontology.org/data_0966)  | [Ontology term](http://edamontology.org/data_0966)  |
| [Annotation](http://edamontology.org/operation_0226)  | [Ontology term](http://edamontology.org/data_0966)  | [Ontology term](http://edamontology.org/data_0966)  |

## Table of Data Standards

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
|  | [Mondo Disease ontology](https://www.ebi.ac.uk/ols/ontologies/mondo)  | |
| | [Human Disease ontology](https://www.ebi.ac.uk/ols/ontologies/doid)  |  |
|| [Medical Subject Headings](https://meshb.nlm.nih.gov/search)


## Using EMBL-EBI OXO

Ontology cross Ontology or OxO service is available from a web interface or a programmatic interface. The following sections show both.

### OXO Web Interface:

#### Step 1: Identify source vocabulary and target vocabulary

For pathology data annotation, vocabularies, such as [MeSH](https://meshb.nlm.nih.gov/search), [NCI thesaurus](https://www.ebi.ac.uk/ols/ontologies/ncit), [ICD-10](https://www.who.int/standards/classifications/classification-of-diseases), [UMLS](https://www.nlm.nih.gov/research/umls/index.html), [Human Disease Ontology(DOID)](https://www.ebi.ac.uk/ols/ontologies/doid), and [MONDO disease ontology](https://www.ebi.ac.uk/ols/ontologies/mondo), are widely used. In this example, we use **MeSH and DOID** as `source vocabularies` and **MONDO** as the `target vocabulary` to demonstrate the ontology mapping workflow. 

Obviously, a target vocabulary needs to be selected before mapping. A variety of factors can influence the selection of a terminology resource for a specific purpose or curation context. For more information about this topic, more detailed guidance on how to select vocabularies can be found [here](https://fairplus.github.io/the-fair-cookbook/content/recipes/interoperability/selecting-ontologies.html). 


OxO allows users to explore the mapping status between the target vocabulary and other vocabularies. Figure 1 shows how terms in MONDO are linked to terms in other ontologies. MONDO has over 16,000 mappings to terms in UMLS. It is also mapped to terms in DOID, Ophanet, OMIM, MeSH, etc.


````{dropdown} 
:open:
```{figure} ../../../images/bi5WoIf.png
---
width: 600px
name: OxO summary result overview
alt: OxO summary result overview
---
OxO summary result overview.
```
````

### Step 2: Provide the source vocabulary term ID

OxO takes ontology term IDs as inputs for ontology mapping, which assumes the (meta)data has been annotated. If the data is not annotated, please check the ontology annotation recipe first. 

In this example, we use terms for ***type 2 diabetes*** from 2 distinct sources. The corresponding term IDs are listed in the table below.

|Text|Corresponding term in MeSH| Corresponding term in DOID|
|--|--|--|
|type 2 diabetes|[MeSH:D003924](https://www.ncbi.nlm.nih.gov/mesh/68003924)|[DOID:9352](https://www.ebi.ac.uk/ols/ontologies/doid/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FDOID_9352)

### Step 3: Perform mapping

Figure 2 shows how to map the MeSH and DOID terms to the MONDO disease ontology. Users are expected to:
- specify the target ontology
- provide a list of source term IDs
- indicate the expected mapping distance.

In this example, we set the `mapping distance` to 1, which uses high confidence mapping evidence only.
Having greater mapping distance returns more mappings but decreases the mapping confidence. 


````{dropdown} 
:open:
```{figure} ../../../images/1EepmN9.png
---
width: 600px
name: OxO mapping with direct user inputs.
alt: OxO mapping with direct user inputs
---
OxO mapping with direct user inputs
```
````

Figure 3 shows the corresponding mapping results. Both terms have been mapped to 'MONDO:0005148'. The results can be downloaded as flat-table(tsv) files.


````{dropdown} 
:open:
```{figure} ../../../images/l1z8OgL.png
---
width: 600px
name: OxO mapping results tabular view
alt: OxO mapping results tabular view
---
OxO mapping results tabular view.
```
````

### Step 4: Review mapping results

To ensure the quality of the mapping, users are recommended to review the mapping results, especially when the mapping distance increases. OxO allows users to explore vocabulary term relationships (see figure 4) by providing a network view of all linked terms. Users can also find more information about each term in the [Ontology lookup service](https://www.ebi.ac.uk/ols/index).

````{dropdown} 
:open:
```{figure} ../../../images/937iuPV.png
---
width: 600px
name: OxO mapping results review - MONDO example
alt: OxO mapping results review - MONDO example
---
OxO mapping results review - MONDO example.
```
````

## Using OxO service programmatically

Besides the graphical user interface offered by OxO at EMBL-EBI, a REST style API is also available.
It is therefore possible to invoke the mapping service from the command line. See the [OxO API documentation](https://www.ebi.ac.uk/spot/oxo/docs/api) page.

In the following code snippet, an API request invoked via `curl` performed the same mapping presented in the section above, at step 3:

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

1. What about incorrect mappings?

    OxO imports term mapping information from ontologies and other curated databases. 
    **It doesn't validate the mapping evidence**.
    Users are recommended to check the mapping results manually, especially when the mapping distance is above 1.
    
2. Why is no mapping found?

    OxO relies on the ontology and other curated databases to improve the mapping coverage. Some terms describing the same concept might not be aligned in OxO. In this case, users are recommended to identify possible mappings by searching in OLS. 
    
    To help the ontology community improve the mapping, users can also submit an update request in corresponding ontologies. The guidance can be found here {ref}`fcb-interop-ontorequest`
    
3. Ontology mapping service for internal databases

    OxO has been dockerized for local deployment and licensed under [Apache License 2.0](https://github.com/EBISPOT/OXO/blob/master/LICENSE). The source code can be found [here](https://github.com/EBISPOT/OXO).


## Conclusion

This recipe presented OxO, EMBL-EBI tool for performing ontology mapping as an example to demonstrate the ontology mapping workflow.
In the context of a FAIRification workflow, a tool such as OxO comes particurlary handy to augment a dataset with cross-references or replace an annotation set with another in a data integration exercice for instance. 

### What to read next?

* [How to build a data dictionary?](fcb-interop-datadictionary)
* [How to build an ontology using robot?](fcb-interop-ontorobot)

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
