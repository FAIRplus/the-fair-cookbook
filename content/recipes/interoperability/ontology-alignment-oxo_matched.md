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

Different ontology (URL_TO_INSERT_TERM_7171 https://fairsharing.org/search?recordType=terminology_artefact)  terms can describe the same concept, which makes it difficult for data integration.
`Ontology (URL_TO_INSERT_TERM_7172 https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD_7174 https://fairsharing.org/FAIRsharing.53edcc) ping`, or ontology (URL_TO_INSERT_TERM_7173 https://fairsharing.org/search?recordType=terminology_artefact)  alignment, is the process of determining correspondences between equivalent
concepts in alternative ontologies (URL_TO_INSERT_TERM_7175 https://fairsharing.org/search?recordType=terminology_artefact)  and distinct vocabularies. 

OxO (URL_TO_INSERT_RECORD_7179 https://fairsharing.org/FAIRsharing.0c6fea)  map (URL_TO_INSERT_RECORD_7178 https://fairsharing.org/FAIRsharing.53edcc) s terms in different ontologies (URL_TO_INSERT_TERM_7177 https://fairsharing.org/search?recordType=terminology_artefact) , vocabularies and coding standard (URL_TO_INSERT_TERM_7176 https://fairsharing.org/search?fairsharingRegistry=Standard) s using evidence collected mainly 
from the Ontology (URL_TO_INSERT_TERM_7180 https://fairsharing.org/search?recordType=terminology_artefact)  Lookup Service (URL_TO_INSERT_RECORD_7181 https://fairsharing.org/FAIRsharing.Mkl9RR)  (OLS (URL_TO_INSERT_RECORD_7182 https://fairsharing.org/FAIRsharing.Mkl9RR) ), Unified Medical Language System (UMLS), but also from other sources. 

This recipe shows how to use the [EMB (URL_TO_INSERT_RECORD_7185 https://fairsharing.org/FAIRsharing.a1rp4c) L-EBI Ontology (URL_TO_INSERT_TERM_7183 https://fairsharing.org/search?recordType=terminology_artefact)  Xref Service (OxO)](https://www.ebi.ac.uk/spot/oxo (URL_TO_INSERT_RECORD_7184 https://fairsharing.org/FAIRsharing.0c6fea) /) service
to map (URL_TO_INSERT_RECORD_7187 https://fairsharing.org/FAIRsharing.53edcc)  ontology (URL_TO_INSERT_TERM_7186 https://fairsharing.org/search?recordType=terminology_artefact)  terms between source and target vocabularies {footcite}`oxo` .

## Graphical Overview


````{dropdown} 
:open:
```{figure} ontology-align-oxo.mmd.svg
---
height: 550px
name: Aligning Ontologies (URL_TO_INSERT_TERM_7188 https://fairsharing.org/search?recordType=terminology_artefact) 
alt: An overview of the ontology (URL_TO_INSERT_TERM_7189 https://fairsharing.org/search?recordType=terminology_artefact)  alignment process
---
An overview of the ontology (URL_TO_INSERT_TERM_7190 https://fairsharing.org/search?recordType=terminology_artefact)  alignment process
```
````


## Requirements
* recipe dependency:
   * {ref}`fcb-introduction-terminologies (URL_TO_INSERT_TERM_7191 https://fairsharing.org/search?recordType=terminology_artefact) -ontologies (URL_TO_INSERT_TERM_7192 https://fairsharing.org/search?recordType=terminology_artefact) `
   * {ref}`fcb-selecting-ontologies (URL_TO_INSERT_TERM_7193 https://fairsharing.org/search?recordType=terminology_artefact) `
* knowledge requirements:
   * Fam (URL_TO_INSERT_RECORD_7194 https://fairsharing.org/FAIRsharing.d0886a) iliar with metadata curation
   * Fam (URL_TO_INSERT_RECORD_7196 https://fairsharing.org/FAIRsharing.d0886a) iliar with ontology (URL_TO_INSERT_TERM_7195 https://fairsharing.org/search?recordType=terminology_artefact)  and other vocabularies
* technical requirements:
    * Experience with API or Bash scripts allows users to try the automated solutions.



## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [ID mapping](http://edamontology.org (URL_TO_INSERT_RECORD_7199 https://fairsharing.org/FAIRsharing.a6r7zs) /operation_3282)  | [Ontology (URL_TO_INSERT_TERM_7197 https://fairsharing.org/search?recordType=terminology_artefact)  term](http://edamontology.org (URL_TO_INSERT_RECORD_7200 https://fairsharing.org/FAIRsharing.a6r7zs) /data_0966)  | [Ontology (URL_TO_INSERT_TERM_7198 https://fairsharing.org/search?recordType=terminology_artefact)  term](http://edamontology.org (URL_TO_INSERT_RECORD_7201 https://fairsharing.org/FAIRsharing.a6r7zs) /data_0966)  |
| [Annotation](http://edamontology.org (URL_TO_INSERT_RECORD_7204 https://fairsharing.org/FAIRsharing.a6r7zs) /operation_0226)  | [Ontology (URL_TO_INSERT_TERM_7202 https://fairsharing.org/search?recordType=terminology_artefact)  term](http://edamontology.org (URL_TO_INSERT_RECORD_7205 https://fairsharing.org/FAIRsharing.a6r7zs) /data_0966)  | [Ontology (URL_TO_INSERT_TERM_7203 https://fairsharing.org/search?recordType=terminology_artefact)  term](http://edamontology.org (URL_TO_INSERT_RECORD_7206 https://fairsharing.org/FAIRsharing.a6r7zs) /data_0966)  |

## Table of Data Standards

| Data Format (URL_TO_INSERT_TERM_7208 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_7209 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_7207 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
|  | [Mondo Disease ontology (URL_TO_INSERT_RECORD_7210 https://fairsharing.org/FAIRsharing.8b6wfq) ](https://www.ebi.ac.uk/ols/ontologies/mondo)  | |
| | [Human Disease ontology (URL_TO_INSERT_RECORD_7211 https://fairsharing.org/FAIRsharing.8b6wfq) ](https://www.ebi.ac.uk/ols/ontologies/doid)  |  |
|| [Medical Subject Headings (URL_TO_INSERT_RECORD_7212 https://fairsharing.org/FAIRsharing.qnkw45) ](https://meshb.nlm.nih.gov/search)


## Using EMBL-EBI OXO

Ontology (URL_TO_INSERT_TERM_7213 https://fairsharing.org/search?recordType=terminology_artefact)  cross Ontology (URL_TO_INSERT_TERM_7214 https://fairsharing.org/search?recordType=terminology_artefact)  or OxO (URL_TO_INSERT_RECORD_7215 https://fairsharing.org/FAIRsharing.0c6fea)  service is available from a web interface or a programmatic interface. The following sections show both.

### OXO Web Interface:

#### Step 1: Identify source vocabulary and target vocabulary

For pathology data annotation, vocabularies, such as [MeSH](https://meshb.nlm.nih.gov/search), [NCI thesaurus (URL_TO_INSERT_RECORD_7218 https://fairsharing.org/FAIRsharing.4cvwxa) ](https://www.ebi.ac.uk/ols/ontologies/ncit), [ICD-10](https://www.who.int (URL_TO_INSERT_RECORD_7227 https://fairsharing.org/3498) /standards/classifications/classification-of-diseases), [UMLS](https://www.nlm.nih.gov/research/umls/index.html), [Human Disease Ontology (URL_TO_INSERT_RECORD_7222 https://fairsharing.org/FAIRsharing.8b6wfq) (DOID)](https://www.ebi.ac.uk/ols/ontologies/doid), and [MO (URL_TO_INSERT_RECORD_7225 https://fairsharing.org/FAIRsharing.qs4x5m) NDO (URL_TO_INSERT_RECORD_7220 https://fairsharing.org/FAIRsharing.b2979t)  disease ontology (URL_TO_INSERT_RECORD_7223 https://fairsharing.org/FAIRsharing.8b6wfq) ](https://www.ebi.ac.uk/ols/ontologies/mondo), are widely used. In this example, we use **MeSH and DOI (URL_TO_INSERT_RECORD_7217 https://fairsharing.org/FAIRsharing.hFLKCn) D (URL_TO_INSERT_RECORD_7224 https://fairsharing.org/FAIRsharing.8b6wfq) ** as `source vocabularies` and **MO (URL_TO_INSERT_RECORD_7226 https://fairsharing.org/FAIRsharing.qs4x5m) NDO (URL_TO_INSERT_RECORD_7221 https://fairsharing.org/FAIRsharing.b2979t) ** as the `target vocabulary` to demonstrate the ontology (URL_TO_INSERT_TERM_7216 https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD_7219 https://fairsharing.org/FAIRsharing.53edcc) ping workflow. 

Obviously, a target vocabulary needs to be selected before map (URL_TO_INSERT_RECORD_7230 https://fairsharing.org/FAIRsharing.53edcc) ping. A variety of factors can influence the selection of a terminology (URL_TO_INSERT_TERM_7229 https://fairsharing.org/search?recordType=terminology_artefact)  resource for a specific purpose or curation context. For more informat (URL_TO_INSERT_TERM_7228 https://fairsharing.org/search?recordType=model_and_format) ion about this topic, more detailed guidance on how to select vocabularies can be found [here](https://fairplus.github.io/the-fair-cookbook/content/recipes/interoperability/selecting-ontologies.html). 


OxO (URL_TO_INSERT_RECORD_7238 https://fairsharing.org/FAIRsharing.0c6fea)  allows users to explore the map (URL_TO_INSERT_RECORD_7233 https://fairsharing.org/FAIRsharing.53edcc) ping status between the target vocabulary and other vocabularies. Figure 1 shows how terms in MO (URL_TO_INSERT_RECORD_7242 https://fairsharing.org/FAIRsharing.qs4x5m) NDO (URL_TO_INSERT_RECORD_7236 https://fairsharing.org/FAIRsharing.b2979t)  are linked to terms in other ontologies (URL_TO_INSERT_TERM_7231 https://fairsharing.org/search?recordType=terminology_artefact) . MO (URL_TO_INSERT_RECORD_7243 https://fairsharing.org/FAIRsharing.qs4x5m) NDO (URL_TO_INSERT_RECORD_7237 https://fairsharing.org/FAIRsharing.b2979t)  has over 16,000 map (URL_TO_INSERT_RECORD_7234 https://fairsharing.org/FAIRsharing.53edcc) pings to terms in UMLS. It is also map (URL_TO_INSERT_RECORD_7235 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_7241 https://fairsharing.org/FAIRsharing.31385c)  to terms in DOI (URL_TO_INSERT_RECORD_7232 https://fairsharing.org/FAIRsharing.hFLKCn) D (URL_TO_INSERT_RECORD_7240 https://fairsharing.org/FAIRsharing.8b6wfq) , Ophanet, OMIM (URL_TO_INSERT_RECORD_7239 https://fairsharing.org/FAIRsharing.azq2t6)  (URL_TO_INSERT_RECORD_7244 https://fairsharing.org/FAIRsharing.9qkaz9) , MeSH, etc.


````{dropdown} 
:open:
```{figure} ../../../images/bi5WoIf.png
---
width: 600px
name: OxO (URL_TO_INSERT_RECORD_7245 https://fairsharing.org/FAIRsharing.0c6fea)  summary result overview
alt: OxO (URL_TO_INSERT_RECORD_7246 https://fairsharing.org/FAIRsharing.0c6fea)  summary result overview
---
OxO (URL_TO_INSERT_RECORD_7247 https://fairsharing.org/FAIRsharing.0c6fea)  summary result overview.
```
````

### Step 2: Provide the source vocabulary term ID

OxO (URL_TO_INSERT_RECORD_7252 https://fairsharing.org/FAIRsharing.0c6fea)  takes ontology (URL_TO_INSERT_TERM_7248 https://fairsharing.org/search?recordType=terminology_artefact)  term IDs as inputs for ontology (URL_TO_INSERT_TERM_7249 https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD_7251 https://fairsharing.org/FAIRsharing.53edcc) ping, which assumes the (meta)data has been annotated. If the data is not annotated, please check the ontology (URL_TO_INSERT_TERM_7250 https://fairsharing.org/search?recordType=terminology_artefact)  annotation recipe first. 

In this example, we use terms for ***type 2 diabetes*** from 2 distinct sources. The corresponding term IDs are listed in the table below.

|Text|Corresponding term in MeSH| Corresponding term in DOI (URL_TO_INSERT_RECORD_7253 https://fairsharing.org/FAIRsharing.hFLKCn) D (URL_TO_INSERT_RECORD_7254 https://fairsharing.org/FAIRsharing.8b6wfq) |
|--|--|--|
|type 2 diabetes|[MeSH:D003924](https://www.ncbi.nlm.nih.gov/mesh/68003924)|[DOID:9352](https://www.ebi.ac.uk/ols/ontologies/doid/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FDOID_9352)

### Step 3: Perform mapping

Figure 2 shows how to map (URL_TO_INSERT_RECORD_7257 https://fairsharing.org/FAIRsharing.53edcc)  the MeSH and DOI (URL_TO_INSERT_RECORD_7256 https://fairsharing.org/FAIRsharing.hFLKCn) D (URL_TO_INSERT_RECORD_7260 https://fairsharing.org/FAIRsharing.8b6wfq)  terms to the MO (URL_TO_INSERT_RECORD_7261 https://fairsharing.org/FAIRsharing.qs4x5m) NDO (URL_TO_INSERT_RECORD_7258 https://fairsharing.org/FAIRsharing.b2979t)  disease ontology (URL_TO_INSERT_TERM_7255 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_7259 https://fairsharing.org/FAIRsharing.8b6wfq) . Users are expected to:
- specify the target ontology (URL_TO_INSERT_TERM_7262 https://fairsharing.org/search?recordType=terminology_artefact) 
- provide a list of source term IDs
- indicate the expected map (URL_TO_INSERT_RECORD_7263 https://fairsharing.org/FAIRsharing.53edcc) ping distance.

In this example, we set the `map (URL_TO_INSERT_RECORD_7264 https://fairsharing.org/FAIRsharing.53edcc) ping distance` to 1, which uses high confidence map (URL_TO_INSERT_RECORD_7265 https://fairsharing.org/FAIRsharing.53edcc) ping evidence only.
Having greater map (URL_TO_INSERT_RECORD_7266 https://fairsharing.org/FAIRsharing.53edcc) ping distance returns more map (URL_TO_INSERT_RECORD_7267 https://fairsharing.org/FAIRsharing.53edcc) pings but decreases the map (URL_TO_INSERT_RECORD_7268 https://fairsharing.org/FAIRsharing.53edcc) ping confidence. 


````{dropdown} 
:open:
```{figure} ../../../images/1EepmN9.png
---
width: 600px
name: OxO (URL_TO_INSERT_RECORD_7270 https://fairsharing.org/FAIRsharing.0c6fea)  map (URL_TO_INSERT_RECORD_7269 https://fairsharing.org/FAIRsharing.53edcc) ping with direct user inputs.
alt: OxO (URL_TO_INSERT_RECORD_7272 https://fairsharing.org/FAIRsharing.0c6fea)  map (URL_TO_INSERT_RECORD_7271 https://fairsharing.org/FAIRsharing.53edcc) ping with direct user inputs
---
OxO (URL_TO_INSERT_RECORD_7274 https://fairsharing.org/FAIRsharing.0c6fea)  map (URL_TO_INSERT_RECORD_7273 https://fairsharing.org/FAIRsharing.53edcc) ping with direct user inputs
```
````

Figure 3 shows the corresponding map (URL_TO_INSERT_RECORD_7275 https://fairsharing.org/FAIRsharing.53edcc) ping results. Both terms have been map (URL_TO_INSERT_RECORD_7276 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_7278 https://fairsharing.org/FAIRsharing.31385c)  to 'MO (URL_TO_INSERT_RECORD_7279 https://fairsharing.org/FAIRsharing.qs4x5m) NDO (URL_TO_INSERT_RECORD_7277 https://fairsharing.org/FAIRsharing.b2979t) :0005148'. The results can be downloaded as flat-table(tsv) files.


````{dropdown} 
:open:
```{figure} ../../../images/l1z8OgL.png
---
width: 600px
name: OxO (URL_TO_INSERT_RECORD_7281 https://fairsharing.org/FAIRsharing.0c6fea)  map (URL_TO_INSERT_RECORD_7280 https://fairsharing.org/FAIRsharing.53edcc) ping results tabular view
alt: OxO (URL_TO_INSERT_RECORD_7283 https://fairsharing.org/FAIRsharing.0c6fea)  map (URL_TO_INSERT_RECORD_7282 https://fairsharing.org/FAIRsharing.53edcc) ping results tabular view
---
OxO (URL_TO_INSERT_RECORD_7285 https://fairsharing.org/FAIRsharing.0c6fea)  map (URL_TO_INSERT_RECORD_7284 https://fairsharing.org/FAIRsharing.53edcc) ping results tabular view.
```
````

### Step 4: Review mapping results

To ensure the quality of the map (URL_TO_INSERT_RECORD_7290 https://fairsharing.org/FAIRsharing.53edcc) ping, users are recommended to review the map (URL_TO_INSERT_RECORD_7291 https://fairsharing.org/FAIRsharing.53edcc) ping results, especially when the map (URL_TO_INSERT_RECORD_7292 https://fairsharing.org/FAIRsharing.53edcc) ping distance increases. OxO (URL_TO_INSERT_RECORD_7293 https://fairsharing.org/FAIRsharing.0c6fea)  allows users to explore vocabulary term relationships (see figure 4) by providing a network view of all linked terms. Users can also find more informat (URL_TO_INSERT_TERM_7286 https://fairsharing.org/search?recordType=model_and_format) ion about each term in the [Ontology (URL_TO_INSERT_TERM_7287 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_7288 https://fairsharing.org/FAIRsharing.Mkl9RR) ](https://www.ebi.ac.uk/ols/index (URL_TO_INSERT_RECORD_7289 https://fairsharing.org/FAIRsharing.Mkl9RR) ).

````{dropdown} 
:open:
```{figure} ../../../images/937iuPV.png
---
width: 600px
name: OxO (URL_TO_INSERT_RECORD_7296 https://fairsharing.org/FAIRsharing.0c6fea)  map (URL_TO_INSERT_RECORD_7294 https://fairsharing.org/FAIRsharing.53edcc) ping results review - MO (URL_TO_INSERT_RECORD_7297 https://fairsharing.org/FAIRsharing.qs4x5m) NDO (URL_TO_INSERT_RECORD_7295 https://fairsharing.org/FAIRsharing.b2979t)  example
alt: OxO (URL_TO_INSERT_RECORD_7300 https://fairsharing.org/FAIRsharing.0c6fea)  map (URL_TO_INSERT_RECORD_7298 https://fairsharing.org/FAIRsharing.53edcc) ping results review - MO (URL_TO_INSERT_RECORD_7301 https://fairsharing.org/FAIRsharing.qs4x5m) NDO (URL_TO_INSERT_RECORD_7299 https://fairsharing.org/FAIRsharing.b2979t)  example
---
OxO (URL_TO_INSERT_RECORD_7304 https://fairsharing.org/FAIRsharing.0c6fea)  map (URL_TO_INSERT_RECORD_7302 https://fairsharing.org/FAIRsharing.53edcc) ping results review - MO (URL_TO_INSERT_RECORD_7305 https://fairsharing.org/FAIRsharing.qs4x5m) NDO (URL_TO_INSERT_RECORD_7303 https://fairsharing.org/FAIRsharing.b2979t)  example.
```
````

## Using OxO service programmatically

Besides the graphical user interface offered by OxO (URL_TO_INSERT_RECORD_7306 https://fairsharing.org/FAIRsharing.0c6fea)  at EMB (URL_TO_INSERT_RECORD_7307 https://fairsharing.org/FAIRsharing.a1rp4c) L-EBI, a REST style API is also available.
It is therefore possible to invoke the map (URL_TO_INSERT_RECORD_7308 https://fairsharing.org/FAIRsharing.53edcc) ping service from the command line. See the [OxO (URL_TO_INSERT_RECORD_7309 https://fairsharing.org/FAIRsharing.0c6fea)  API documentation](https://www.ebi.ac.uk/spot/oxo (URL_TO_INSERT_RECORD_7310 https://fairsharing.org/FAIRsharing.0c6fea) /docs/api) page.

In the following code snippet, an API request invoked via `curl` performed the same map (URL_TO_INSERT_RECORD_7311 https://fairsharing.org/FAIRsharing.53edcc) ping presented in the section above, at step 3:

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

1. What about incorrect map (URL_TO_INSERT_RECORD_7312 https://fairsharing.org/FAIRsharing.53edcc) pings?

    OxO (URL_TO_INSERT_RECORD_7317 https://fairsharing.org/FAIRsharing.0c6fea)  imports term map (URL_TO_INSERT_RECORD_7316 https://fairsharing.org/FAIRsharing.53edcc) ping informat (URL_TO_INSERT_TERM_7314 https://fairsharing.org/search?recordType=model_and_format) ion from ontologies (URL_TO_INSERT_TERM_7315 https://fairsharing.org/search?recordType=terminology_artefact)  and other curated database (URL_TO_INSERT_TERM_7313 https://fairsharing.org/search?fairsharingRegistry=Database) s. 
    **It doesn't validate the map (URL_TO_INSERT_RECORD_7318 https://fairsharing.org/FAIRsharing.53edcc) ping evidence**.
    Users are recommended to check the map (URL_TO_INSERT_RECORD_7319 https://fairsharing.org/FAIRsharing.53edcc) ping results manually, especially when the map (URL_TO_INSERT_RECORD_7320 https://fairsharing.org/FAIRsharing.53edcc) ping distance is above 1.
    
2. Why is no map (URL_TO_INSERT_RECORD_7321 https://fairsharing.org/FAIRsharing.53edcc) ping found?

    OxO (URL_TO_INSERT_RECORD_7327 https://fairsharing.org/FAIRsharing.0c6fea)  relies on the ontology (URL_TO_INSERT_TERM_7323 https://fairsharing.org/search?recordType=terminology_artefact)  and other curated database (URL_TO_INSERT_TERM_7322 https://fairsharing.org/search?fairsharingRegistry=Database) s to improve the map (URL_TO_INSERT_RECORD_7325 https://fairsharing.org/FAIRsharing.53edcc) ping coverage. Some terms describing the same concept might not be aligned in OxO (URL_TO_INSERT_RECORD_7328 https://fairsharing.org/FAIRsharing.0c6fea) . In this case, users are recommended to identify possible map (URL_TO_INSERT_RECORD_7326 https://fairsharing.org/FAIRsharing.53edcc) pings by search (URL_TO_INSERT_RECORD_7329 https://fairsharing.org/FAIRsharing.52b22c) ing in OLS (URL_TO_INSERT_RECORD_7324 https://fairsharing.org/FAIRsharing.Mkl9RR) . 
    
    To help the ontology (URL_TO_INSERT_TERM_7330 https://fairsharing.org/search?recordType=terminology_artefact)  community improve the map (URL_TO_INSERT_RECORD_7332 https://fairsharing.org/FAIRsharing.53edcc) ping, users can also submit an update request in corresponding ontologies (URL_TO_INSERT_TERM_7331 https://fairsharing.org/search?recordType=terminology_artefact) . The guidance can be found here {ref}`fcb-interop-ontorequest`
    
3. Ontology (URL_TO_INSERT_TERM_7334 https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD_7335 https://fairsharing.org/FAIRsharing.53edcc) ping service for internal database (URL_TO_INSERT_TERM_7333 https://fairsharing.org/search?fairsharingRegistry=Database) s

    OxO (URL_TO_INSERT_RECORD_7338 https://fairsharing.org/FAIRsharing.0c6fea)  has been dockerized for local deployment and licensed under [Apache License 2.0](https://github.com (URL_TO_INSERT_RECORD_7336 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/OXO/blob/master/LICENSE). The source code can be found [here](https://github.com (URL_TO_INSERT_RECORD_7337 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/OXO).


## Conclusion

This recipe presented OxO (URL_TO_INSERT_RECORD_7343 https://fairsharing.org/FAIRsharing.0c6fea) , EMB (URL_TO_INSERT_RECORD_7344 https://fairsharing.org/FAIRsharing.a1rp4c) L-EBI tool for performing ontology (URL_TO_INSERT_TERM_7339 https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD_7341 https://fairsharing.org/FAIRsharing.53edcc) ping as an example to demonstrate the ontology (URL_TO_INSERT_TERM_7340 https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD_7342 https://fairsharing.org/FAIRsharing.53edcc) ping workflow.
In the context of a FAIR (URL_TO_INSERT_RECORD_7346 https://fairsharing.org/FAIRsharing.WWI10U) ification workflow, a tool such as OxO (URL_TO_INSERT_RECORD_7345 https://fairsharing.org/FAIRsharing.0c6fea)  comes particurlary handy to augment a dataset with cross-references or replace an annotation set with another in a data integration exercice for instance. 

### What to read next?

* [How to build a data dictionary?](fcb-interop-datadictionary)
* [How to build an ontology (URL_TO_INSERT_TERM_7347 https://fairsharing.org/search?recordType=terminology_artefact)  using robot?](fcb-interop-ontorobot)

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
