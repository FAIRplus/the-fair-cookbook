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

Different ontology (URL_TO_INSERT_TERM_3769 https://fairsharing.org/search?recordType=terminology_artefact)  terms can describe the same concept, which makes it difficult for data integration.
`Ontology (URL_TO_INSERT_TERM_3770 https://fairsharing.org/search?recordType=terminology_artefact)  mapping`, or ontology (URL_TO_INSERT_TERM_3771 https://fairsharing.org/search?recordType=terminology_artefact)  alignment, is the process of determining correspondences between equivalent
concepts in alternative ontologies (URL_TO_INSERT_TERM_3772 https://fairsharing.org/search?recordType=terminology_artefact)  and distinct vocabularies. 

OxO (URL_TO_INSERT_RECORD-ABBREV_3775 https://fairsharing.org/FAIRsharing.0c6fea)  maps terms in different ontologies (URL_TO_INSERT_TERM_3774 https://fairsharing.org/search?recordType=terminology_artefact) , vocabularies and coding standard (URL_TO_INSERT_TERM_3773 https://fairsharing.org/search?fairsharingRegistry=Standard) s using evidence collected mainly 
from the Ontology (URL_TO_INSERT_TERM_3776 https://fairsharing.org/search?recordType=terminology_artefact)  Lookup Service (URL_TO_INSERT_RECORD-NAME_3777 https://fairsharing.org/FAIRsharing.Mkl9RR)  (OLS (URL_TO_INSERT_RECORD-ABBREV_3778 https://fairsharing.org/FAIRsharing.Mkl9RR) ), Unified Medical Language System (UMLS), but also from other sources. 

This recipe shows how to use the [EMBL-EBI Ontology Xref Service (OxO)](https://www.ebi.ac.uk/spot/oxo/) service
to map (URL_TO_INSERT_RECORD-NAME_3780 https://fairsharing.org/FAIRsharing.53edcc)  ontology (URL_TO_INSERT_TERM_3779 https://fairsharing.org/search?recordType=terminology_artefact)  terms between source and target vocabularies {footcite}`oxo` .

## Graphical Overview


````{dropdown} 
:open:
```{figure} ontology-align-oxo.mmd.svg
---
height: 550px
name: Aligning Ontologies (URL_TO_INSERT_TERM_3781 https://fairsharing.org/search?recordType=terminology_artefact) 
alt: An overview of the ontology (URL_TO_INSERT_TERM_3782 https://fairsharing.org/search?recordType=terminology_artefact)  alignment process
---
An overview of the ontology (URL_TO_INSERT_TERM_3783 https://fairsharing.org/search?recordType=terminology_artefact)  alignment process
```
````


## Requirements
* recipe dependency:
   * {ref}`fcb-introduction-terminologies (URL_TO_INSERT_TERM_3784 https://fairsharing.org/search?recordType=terminology_artefact) -ontologies (URL_TO_INSERT_TERM_3785 https://fairsharing.org/search?recordType=terminology_artefact) `
   * {ref}`fcb-selecting-ontologies (URL_TO_INSERT_TERM_3786 https://fairsharing.org/search?recordType=terminology_artefact) `
* knowledge requirements:
   * Familiar with metadata curation
   * Familiar with ontology (URL_TO_INSERT_TERM_3787 https://fairsharing.org/search?recordType=terminology_artefact)  and other vocabularies
* technical requirements:
    * Experience with API or Bash scripts allows users to try the automated solutions.



## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [ID mapping](http://edamontology.org/operation_3282)  | [Ontology (URL_TO_INSERT_TERM_3788 https://fairsharing.org/search?recordType=terminology_artefact)  term](http://edamontology.org/data_0966)  | [Ontology (URL_TO_INSERT_TERM_3789 https://fairsharing.org/search?recordType=terminology_artefact)  term](http://edamontology.org/data_0966)  |
| [Annotation](http://edamontology.org/operation_0226)  | [Ontology (URL_TO_INSERT_TERM_3790 https://fairsharing.org/search?recordType=terminology_artefact)  term](http://edamontology.org/data_0966)  | [Ontology (URL_TO_INSERT_TERM_3791 https://fairsharing.org/search?recordType=terminology_artefact)  term](http://edamontology.org/data_0966)  |

## Table of Data Standards

| Data Format (URL_TO_INSERT_TERM_3793 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_3794 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_3792 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
|  | [Mondo Disease ontology](https://www.ebi.ac.uk/ols/ontologies/mondo)  | |
| | [Human Disease ontology](https://www.ebi.ac.uk/ols/ontologies/doid)  |  |
|| [Medical Subject Headings](https://meshb.nlm.nih.gov/search)


## Using EMBL-EBI OXO

Ontology (URL_TO_INSERT_TERM_3795 https://fairsharing.org/search?recordType=terminology_artefact)  cross Ontology (URL_TO_INSERT_TERM_3796 https://fairsharing.org/search?recordType=terminology_artefact)  or OxO (URL_TO_INSERT_RECORD-ABBREV_3797 https://fairsharing.org/FAIRsharing.0c6fea)  service is available from a web interface or a programmatic interface. The following sections show both.

### OXO Web Interface:

#### Step 1: Identify source vocabulary and target vocabulary

For pathology data annotation, vocabularies, such as [MeSH](https://meshb.nlm.nih.gov/search), [NCI thesaurus (URL_TO_INSERT_RECORD-NAME_3802 https://fairsharing.org/FAIRsharing.4cvwxa) ](https://www.ebi.ac.uk/ols/ontologies/ncit), [ICD-10](https://www.who.int/standards/classifications/classification-of-diseases), [UMLS](https://www.nlm.nih.gov/research/umls/index.html), [Human Disease Ontology (URL_TO_INSERT_TERM_3798 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD-NAME_3803 https://fairsharing.org/FAIRsharing.8b6wfq) (DOI (URL_TO_INSERT_RECORD-ABBREV_3805 https://fairsharing.org/FAIRsharing.8b6wfq) D)](https://www.ebi.ac.uk/ols/ontologies/doid), and [MONDO (URL_TO_INSERT_RECORD-ABBREV_3800 https://fairsharing.org/FAIRsharing.b2979t)  disease ontology (URL_TO_INSERT_RECORD-NAME_3804 https://fairsharing.org/FAIRsharing.8b6wfq) ](https://www.ebi.ac.uk/ols/ontologies/mondo), are widely used. In this example, we use **MeSH and DOID (URL_TO_INSERT_RECORD-ABBREV_3806 https://fairsharing.org/FAIRsharing.8b6wfq) ** as `source vocabularies` and **MONDO (URL_TO_INSERT_RECORD-ABBREV_3801 https://fairsharing.org/FAIRsharing.b2979t) ** as the `target vocabulary` to demonstrate the ontology (URL_TO_INSERT_TERM_3799 https://fairsharing.org/search?recordType=terminology_artefact)  mapping workflow. 

Obviously, a target vocabulary needs to be selected before mapping. A variety of factors can influence the selection of a terminology (URL_TO_INSERT_TERM_3808 https://fairsharing.org/search?recordType=terminology_artefact)  resource for a specific purpose or curation context. For more informat (URL_TO_INSERT_TERM_3807 https://fairsharing.org/search?recordType=model_and_format) ion about this topic, more detailed guidance on how to select vocabularies can be found [here](https://fairplus.github.io/the-fair-cookbook/content/recipes/interoperability/selecting-ontologies.html). 


OxO (URL_TO_INSERT_RECORD-ABBREV_3812 https://fairsharing.org/FAIRsharing.0c6fea)  allows users to explore the mapping status between the target vocabulary and other vocabularies. Figure 1 shows how terms in MONDO (URL_TO_INSERT_RECORD-ABBREV_3810 https://fairsharing.org/FAIRsharing.b2979t)  are linked to terms in other ontologies (URL_TO_INSERT_TERM_3809 https://fairsharing.org/search?recordType=terminology_artefact) . MONDO (URL_TO_INSERT_RECORD-ABBREV_3811 https://fairsharing.org/FAIRsharing.b2979t)  has over 16,000 mappings to terms in UMLS. It is also mapped to terms in DOID (URL_TO_INSERT_RECORD-ABBREV_3813 https://fairsharing.org/FAIRsharing.8b6wfq) , Ophanet, OMIM (URL_TO_INSERT_RECORD-ABBREV_3814 https://fairsharing.org/FAIRsharing.9qkaz9) , MeSH, etc.


````{dropdown} 
:open:
```{figure} ../../../images/bi5WoIf.png
---
width: 600px
name: OxO (URL_TO_INSERT_RECORD-ABBREV_3815 https://fairsharing.org/FAIRsharing.0c6fea)  summary result overview
alt: OxO (URL_TO_INSERT_RECORD-ABBREV_3816 https://fairsharing.org/FAIRsharing.0c6fea)  summary result overview
---
OxO (URL_TO_INSERT_RECORD-ABBREV_3817 https://fairsharing.org/FAIRsharing.0c6fea)  summary result overview.
```
````

### Step 2: Provide the source vocabulary term ID

OxO (URL_TO_INSERT_RECORD-ABBREV_3821 https://fairsharing.org/FAIRsharing.0c6fea)  takes ontology (URL_TO_INSERT_TERM_3818 https://fairsharing.org/search?recordType=terminology_artefact)  term IDs as inputs for ontology (URL_TO_INSERT_TERM_3819 https://fairsharing.org/search?recordType=terminology_artefact)  mapping, which assumes the (meta)data has been annotated. If the data is not annotated, please check the ontology (URL_TO_INSERT_TERM_3820 https://fairsharing.org/search?recordType=terminology_artefact)  annotation recipe first. 

In this example, we use terms for ***type 2 diabetes*** from 2 distinct sources. The corresponding term IDs are listed in the table below.

|Text|Corresponding term in MeSH| Corresponding term in DOID (URL_TO_INSERT_RECORD-ABBREV_3822 https://fairsharing.org/FAIRsharing.8b6wfq) |
|--|--|--|
|type 2 diabetes|[MeSH:D003924](https://www.ncbi.nlm.nih.gov/mesh/68003924)|[DOID:9352](https://www.ebi.ac.uk/ols/ontologies/doid/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FDOID_9352)

### Step 3: Perform mapping

Figure 2 shows how to map (URL_TO_INSERT_RECORD-NAME_3827 https://fairsharing.org/FAIRsharing.53edcc)  the MeSH and DOID (URL_TO_INSERT_RECORD-ABBREV_3826 https://fairsharing.org/FAIRsharing.8b6wfq)  terms to the MONDO (URL_TO_INSERT_RECORD-ABBREV_3824 https://fairsharing.org/FAIRsharing.b2979t)  disease ontology (URL_TO_INSERT_TERM_3823 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD-NAME_3825 https://fairsharing.org/FAIRsharing.8b6wfq) . Users are expected to:
- specify the target ontology (URL_TO_INSERT_TERM_3828 https://fairsharing.org/search?recordType=terminology_artefact) 
- provide a list of source term IDs
- indicate the expected mapping distance.

In this example, we set the `mapping distance` to 1, which uses high confidence mapping evidence only.
Having greater mapping distance returns more mappings but decreases the mapping confidence. 


````{dropdown} 
:open:
```{figure} ../../../images/1EepmN9.png
---
width: 600px
name: OxO (URL_TO_INSERT_RECORD-ABBREV_3829 https://fairsharing.org/FAIRsharing.0c6fea)  mapping with direct user inputs.
alt: OxO (URL_TO_INSERT_RECORD-ABBREV_3830 https://fairsharing.org/FAIRsharing.0c6fea)  mapping with direct user inputs
---
OxO (URL_TO_INSERT_RECORD-ABBREV_3831 https://fairsharing.org/FAIRsharing.0c6fea)  mapping with direct user inputs
```
````

Figure 3 shows the corresponding mapping results. Both terms have been mapped to 'MONDO (URL_TO_INSERT_RECORD-ABBREV_3832 https://fairsharing.org/FAIRsharing.b2979t) :0005148'. The results can be downloaded as flat-table(tsv) files.


````{dropdown} 
:open:
```{figure} ../../../images/l1z8OgL.png
---
width: 600px
name: OxO (URL_TO_INSERT_RECORD-ABBREV_3833 https://fairsharing.org/FAIRsharing.0c6fea)  mapping results tabular view
alt: OxO (URL_TO_INSERT_RECORD-ABBREV_3834 https://fairsharing.org/FAIRsharing.0c6fea)  mapping results tabular view
---
OxO (URL_TO_INSERT_RECORD-ABBREV_3835 https://fairsharing.org/FAIRsharing.0c6fea)  mapping results tabular view.
```
````

### Step 4: Review mapping results

To ensure the quality of the mapping, users are recommended to review the mapping results, especially when the mapping distance increases. OxO (URL_TO_INSERT_RECORD-ABBREV_3837 https://fairsharing.org/FAIRsharing.0c6fea)  allows users to explore vocabulary term relationships (see figure 4) by providing a network view of all linked terms. Users can also find more informat (URL_TO_INSERT_TERM_3836 https://fairsharing.org/search?recordType=model_and_format) ion about each term in the [Ontology lookup service](https://www.ebi.ac.uk/ols/index).

````{dropdown} 
:open:
```{figure} ../../../images/937iuPV.png
---
width: 600px
name: OxO (URL_TO_INSERT_RECORD-ABBREV_3839 https://fairsharing.org/FAIRsharing.0c6fea)  mapping results review - MONDO (URL_TO_INSERT_RECORD-ABBREV_3838 https://fairsharing.org/FAIRsharing.b2979t)  example
alt: OxO (URL_TO_INSERT_RECORD-ABBREV_3841 https://fairsharing.org/FAIRsharing.0c6fea)  mapping results review - MONDO (URL_TO_INSERT_RECORD-ABBREV_3840 https://fairsharing.org/FAIRsharing.b2979t)  example
---
OxO (URL_TO_INSERT_RECORD-ABBREV_3843 https://fairsharing.org/FAIRsharing.0c6fea)  mapping results review - MONDO (URL_TO_INSERT_RECORD-ABBREV_3842 https://fairsharing.org/FAIRsharing.b2979t)  example.
```
````

## Using OxO service programmatically

Besides the graphical user interface offered by OxO (URL_TO_INSERT_RECORD-ABBREV_3844 https://fairsharing.org/FAIRsharing.0c6fea)  at EMBL-EBI, a REST style API is also available.
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

    OxO (URL_TO_INSERT_RECORD-ABBREV_3848 https://fairsharing.org/FAIRsharing.0c6fea)  imports term mapping informat (URL_TO_INSERT_TERM_3846 https://fairsharing.org/search?recordType=model_and_format) ion from ontologies (URL_TO_INSERT_TERM_3847 https://fairsharing.org/search?recordType=terminology_artefact)  and other curated database (URL_TO_INSERT_TERM_3845 https://fairsharing.org/search?fairsharingRegistry=Database) s. 
    **It doesn't validate the mapping evidence**.
    Users are recommended to check the mapping results manually, especially when the mapping distance is above 1.
    
2. Why is no mapping found?

    OxO (URL_TO_INSERT_RECORD-ABBREV_3852 https://fairsharing.org/FAIRsharing.0c6fea)  relies on the ontology (URL_TO_INSERT_TERM_3850 https://fairsharing.org/search?recordType=terminology_artefact)  and other curated database (URL_TO_INSERT_TERM_3849 https://fairsharing.org/search?fairsharingRegistry=Database) s to improve the mapping coverage. Some terms describing the same concept might not be aligned in OxO (URL_TO_INSERT_RECORD-ABBREV_3853 https://fairsharing.org/FAIRsharing.0c6fea) . In this case, users are recommended to identify possible mappings by searching in OLS (URL_TO_INSERT_RECORD-ABBREV_3851 https://fairsharing.org/FAIRsharing.Mkl9RR) . 
    
    To help the ontology (URL_TO_INSERT_TERM_3854 https://fairsharing.org/search?recordType=terminology_artefact)  community improve the mapping, users can also submit an update request in corresponding ontologies (URL_TO_INSERT_TERM_3855 https://fairsharing.org/search?recordType=terminology_artefact) . The guidance can be found here {ref}`fcb-interop-ontorequest`
    
3. Ontology (URL_TO_INSERT_TERM_3857 https://fairsharing.org/search?recordType=terminology_artefact)  mapping service for internal database (URL_TO_INSERT_TERM_3856 https://fairsharing.org/search?fairsharingRegistry=Database) s

    OxO (URL_TO_INSERT_RECORD-ABBREV_3858 https://fairsharing.org/FAIRsharing.0c6fea)  has been dockerized for local deployment and licensed under [Apache License 2.0](https://github.com/EBISPOT/OXO/blob/master/LICENSE). The source code can be found [here](https://github.com/EBISPOT/OXO).


## Conclusion

This recipe presented OxO (URL_TO_INSERT_RECORD-ABBREV_3861 https://fairsharing.org/FAIRsharing.0c6fea) , EMBL-EBI tool for performing ontology (URL_TO_INSERT_TERM_3859 https://fairsharing.org/search?recordType=terminology_artefact)  mapping as an example to demonstrate the ontology (URL_TO_INSERT_TERM_3860 https://fairsharing.org/search?recordType=terminology_artefact)  mapping workflow.
In the context of a FAIRification workflow, a tool such as OxO (URL_TO_INSERT_RECORD-ABBREV_3862 https://fairsharing.org/FAIRsharing.0c6fea)  comes particurlary handy to augment a dataset with cross-references or replace an annotation set with another in a data integration exercice for instance. 

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
