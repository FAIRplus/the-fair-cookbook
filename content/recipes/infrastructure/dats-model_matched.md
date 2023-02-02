(fcb-dats-model (URL_TO_INSERT_TERM_2236 https://fairsharing.org/search?recordType=model_and_format) )=
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

>* Provide a general introduction to the Data Tag Suite (URL_TO_INSERT_RECORD_2239 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_2238 https://fairsharing.org/search?recordType=model_and_format)  for representing project (URL_TO_INSERT_TERM_2237 https://fairsharing.org/search?recordType=project) , study and dataset metadata
>* Highlight challenges in implementing the model (URL_TO_INSERT_TERM_2240 https://fairsharing.org/search?recordType=model_and_format)  in a data catalogue

---


## Graphical Overview

````{dropdown} **Data Model**
:open:
```{figure} DataModelDiagram.png
---
width: 800px
name: data-model (URL_TO_INSERT_TERM_2241 https://fairsharing.org/search?recordType=model_and_format) -diagram
alt: Data Model (URL_TO_INSERT_TERM_2242 https://fairsharing.org/search?recordType=model_and_format)  Diagram
---
Data Model (URL_TO_INSERT_TERM_2243 https://fairsharing.org/search?recordType=model_and_format)  Diagram
```
````

---


## Table of Data Standards


| Data Format (URL_TO_INSERT_TERM_2245 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_2246 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_2244 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
| [JSON-LD](https://json-ld.org/) | [OBO Foundry (URL_TO_INSERT_RECORD_2247 https://fairsharing.org/FAIRsharing.847069) ](https://obofoundry.org/) | [DATS](https://datatagsuite.github.io/docs/html/dats.html) |
| |  | [DCAT](https://www.w3.org/TR/vocab-dcat-2/) |
| |  | [SDO](https://schema.org/) |

---

## Model overview

Data Tag Suits (DATS (URL_TO_INSERT_RECORD_2252 https://fairsharing.org/FAIRsharing.e20vsd) ) {footcite}`pmid28585923` is a data description model (URL_TO_INSERT_TERM_2251 https://fairsharing.org/search?recordType=model_and_format)  designed and produced to describe datasets being ingested in DataMed (URL_TO_INSERT_RECORD_2258 https://fairsharing.org/FAIRsharing.v5q4zc) , a prototype for data discovery developed (URL_TO_INSERT_RECORD_2256 https://fairsharing.org/FAIRsharing.31385c)  as part of the bioCADDIE (URL_TO_INSERT_RECORD_2254 https://fairsharing.org/3506)  project (URL_TO_INSERT_TERM_2248 https://fairsharing.org/search?recordType=project)  {footcite}`pmid28546571`. DATS (URL_TO_INSERT_RECORD_2253 https://fairsharing.org/FAIRsharing.e20vsd)  was co-developed (URL_TO_INSERT_RECORD_2257 https://fairsharing.org/FAIRsharing.31385c)  by the Oxford e-Research (URL_TO_INSERT_RECORD_2255 https://fairsharing.org/FAIRsharing.52b22c)  Centre and the NIH Data Common Big Data to Knowledge (BD2K) initiative, where it was used to uniformly represent metadata across a number of project (URL_TO_INSERT_TERM_2249 https://fairsharing.org/search?recordType=project) s, including the Genotype-Tissue Expression project (URL_TO_INSERT_TERM_2250 https://fairsharing.org/search?recordType=project)  (GTEx) and Trans-Omics for Precision Medicine (TOPMed).

DATS (URL_TO_INSERT_RECORD_2263 https://fairsharing.org/FAIRsharing.e20vsd)  is semantically compatible with the Data Catalog Vocabulary (URL_TO_INSERT_RECORD_2260 https://fairsharing.org/FAIRsharing.h4j3qm)  (DCAT (URL_TO_INSERT_RECORD_2261 https://fairsharing.org/FAIRsharing.h4j3qm) ), a Resource Description Framework (URL_TO_INSERT_RECORD_2259 https://fairsharing.org/FAIRsharing.p77ph9)  (RDF) vocabulary designed to facilitate interoperability among data catalogues published on the web, as well as schema.org (URL_TO_INSERT_RECORD_2266 https://fairsharing.org/FAIRsharing.hzdzq8)  (SDO), which is a community-driven effort with a similar interoperability goal to DC (URL_TO_INSERT_RECORD_2264 https://fairsharing.org/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD_2265 https://fairsharing.org/3547) AT (URL_TO_INSERT_RECORD_2262 https://fairsharing.org/FAIRsharing.h4j3qm)  but a more general-purpose scope.

The original DATS (URL_TO_INSERT_RECORD_2275 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_2269 https://fairsharing.org/search?recordType=model_and_format)  centered around concept of a "Dataset", an entity that covers technical aspects such as licensing, data types and distributions. The Dataset is produced by or is the input or output of a “Study”, which contains elements that are specific to life, environmental and biomedical science domains, and which model (URL_TO_INSERT_TERM_2270 https://fairsharing.org/search?recordType=model_and_format) s experimental processes, cohorts and protocol informat (URL_TO_INSERT_TERM_2272 https://fairsharing.org/search?recordType=model_and_format) ion. To meet the requirements of project (URL_TO_INSERT_TERM_2267 https://fairsharing.org/search?recordType=project) -generated datasets, the DATS (URL_TO_INSERT_RECORD_2276 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_2271 https://fairsharing.org/search?recordType=model_and_format)  was extended to include the third core (URL_TO_INSERT_RECORD_2274 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_2277 https://fairsharing.org/FAIRsharing.xMmOCL)  concept of “Project (URL_TO_INSERT_TERM_2268 https://fairsharing.org/search?recordType=project) ”, covering general informat (URL_TO_INSERT_TERM_2273 https://fairsharing.org/search?recordType=model_and_format) ion such as title, publications, funding and contributors.


### Core objects

The DATS (URL_TO_INSERT_RECORD_2282 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_2280 https://fairsharing.org/search?recordType=model_and_format)  centres around three core (URL_TO_INSERT_RECORD_2281 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_2283 https://fairsharing.org/FAIRsharing.xMmOCL)  objects, "Project (URL_TO_INSERT_TERM_2278 https://fairsharing.org/search?recordType=project) ", "Study" and "Dataset", each of which contains a set of sub-objects, which in turn can be nested down to the lowest unitary object (which contains no further objects), which is the “Annotation”. Project (URL_TO_INSERT_TERM_2279 https://fairsharing.org/search?recordType=project) , Study and Dataset relate to each other in a triangular fashion as shown in figure 1.

At first glance, the three core (URL_TO_INSERT_RECORD_2291 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_2296 https://fairsharing.org/FAIRsharing.xMmOCL)  objects make the DATS (URL_TO_INSERT_RECORD_2292 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_2285 https://fairsharing.org/search?recordType=model_and_format)  reminiscent of the ISA (Investigation, Study, Assay) model (URL_TO_INSERT_TERM_2286 https://fairsharing.org/search?recordType=model_and_format)  for describing experimental processes. There are however several key differences between the two. For one, ISA has a waterfall structure whereby any instance of the model (URL_TO_INSERT_TERM_2287 https://fairsharing.org/search?recordType=model_and_format)  has to contain a Study object between an Investigation and an Assay. In DATS (URL_TO_INSERT_RECORD_2293 https://fairsharing.org/FAIRsharing.e20vsd)  on the other hand, it is possible for a Dataset to be directly dependent on a Project (URL_TO_INSERT_TERM_2284 https://fairsharing.org/search?recordType=project) , without any Study informat (URL_TO_INSERT_TERM_2289 https://fairsharing.org/search?recordType=model_and_format) ion. This is relevant for datasets such as knowledge graphs or synthetic datasets, for which no study metadata may be available. Additionally, DATS (URL_TO_INSERT_RECORD_2294 https://fairsharing.org/FAIRsharing.e20vsd)  focuses on the technical details, availability and use restrictions of datasets whereas the purpose of the ISA model (URL_TO_INSERT_TERM_2288 https://fairsharing.org/search?recordType=model_and_format)  is to describe experimental procedures in great detail. While the DATS (URL_TO_INSERT_RECORD_2295 https://fairsharing.org/FAIRsharing.e20vsd)  Study covers some of this informat (URL_TO_INSERT_TERM_2290 https://fairsharing.org/search?recordType=model_and_format) ion, it is much less comprehensive or central to the captured data than for ISA.

#### Project

The Project (URL_TO_INSERT_TERM_2297 https://fairsharing.org/search?recordType=project)  object was not part of the original version of DATS (URL_TO_INSERT_RECORD_2302 https://fairsharing.org/FAIRsharing.e20vsd) . It was added in the second version as a means of linking different studies and datasets under one common parent as well as capturing informat (URL_TO_INSERT_TERM_2300 https://fairsharing.org/search?recordType=model_and_format) ion such as project (URL_TO_INSERT_TERM_2298 https://fairsharing.org/search?recordType=project)  contacts or consortium informat (URL_TO_INSERT_TERM_2301 https://fairsharing.org/search?recordType=model_and_format) ion, publications not linked to one specific study, funding sources, project (URL_TO_INSERT_TERM_2299 https://fairsharing.org/search?recordType=project)  websites and start/end dates.

#### Study

The Study object, although part of the original DATS (URL_TO_INSERT_RECORD_2305 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_2303 https://fairsharing.org/search?recordType=model_and_format) , had a less central role in the first iteration than it has in this latest one. Capturing the context in which the Dataset was either generated or used, the Study provides informat (URL_TO_INSERT_TERM_2304 https://fairsharing.org/search?recordType=model_and_format) ion about the type of study undertaken (e.g. clinical trials or chemical toxicity screens), cohorts (or "studyGroups), input materials, selection criteria and the steps involved in the study. 

#### Dataset

The Dataset object was the central concept of the initial DATS (URL_TO_INSERT_RECORD_2312 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_2308 https://fairsharing.org/search?recordType=model_and_format)  but became an equal part in the `Project (URL_TO_INSERT_TERM_2307 https://fairsharing.org/search?recordType=project) -Study-Dataset` triangle in version 2. The object captures technical informat (URL_TO_INSERT_TERM_2310 https://fairsharing.org/search?recordType=model_and_format) ion about the dataset, such as file types, data standard (URL_TO_INSERT_TERM_2306 https://fairsharing.org/search?fairsharingRegistry=Standard) s, versions and licensing as well as links to the actual data if available. It also model (URL_TO_INSERT_TERM_2309 https://fairsharing.org/search?recordType=model_and_format) s informat (URL_TO_INSERT_TERM_2311 https://fairsharing.org/search?recordType=model_and_format) ion related to the creation of the dataset such as input materials, diseases, biological entities and other similar objects, as well as the types of experiments from which the dataset was derived and any associated dimensions (URL_TO_INSERT_RECORD_2313 https://fairsharing.org/FAIRsharing.9af33c)  or components.

### Sub-objects

Each of the three top-level objects references a range of sub-objects, which in turn contain further sub-objects, down to the lowest unitary object (which contains no further objects), which is the “Annotation”. An “Annotation” consists of just two key-value pairs, the “value” and, optionally, the “valueIRI”, designed to capture the Internationalized Resource Identifier (URL_TO_INSERT_TERM_2315 https://fairsharing.org/search?recordType=identifier_schema)  (IRI) of an ontology (URL_TO_INSERT_TERM_2314 https://fairsharing.org/search?recordType=terminology_artefact)  term contextualising the free text “value”. Due to this nested object structure, DATS (URL_TO_INSERT_RECORD_2316 https://fairsharing.org/FAIRsharing.e20vsd)  can be quite opaque to parse for the human reader but allows for easier programmatic processing of the objects. A full overview of the DATS (URL_TO_INSERT_RECORD_2317 https://fairsharing.org/FAIRsharing.e20vsd)  schema can be found on the [DataTagSuite Github repository](https://github.com/datatagsuite/schema).

### Ontology annotations

The provision for ontology (URL_TO_INSERT_TERM_2321 https://fairsharing.org/search?recordType=terminology_artefact)  annotations is at the core (URL_TO_INSERT_RECORD_2324 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_2326 https://fairsharing.org/FAIRsharing.xMmOCL)  of the DATS (URL_TO_INSERT_RECORD_2325 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_2318 https://fairsharing.org/search?recordType=model_and_format) , with the smallest object available in the model (URL_TO_INSERT_TERM_2319 https://fairsharing.org/search?recordType=model_and_format)  being the `Annotation` schema, which simply consists of two key-value pairs: `value`, which can contain a text string (URL_TO_INSERT_RECORD_2327 https://fairsharing.org/FAIRsharing.9b7wvk)  or number (to allow for coded values), and `valueIRI`, which contains a URI (URL_TO_INSERT_RECORD_2323 https://fairsharing.org/FAIRsharing.d261e1) -format (URL_TO_INSERT_TERM_2320 https://fairsharing.org/search?recordType=model_and_format) ted string (URL_TO_INSERT_RECORD_2328 https://fairsharing.org/FAIRsharing.9b7wvk)  representing a concept or ontology (URL_TO_INSERT_TERM_2322 https://fairsharing.org/search?recordType=terminology_artefact)  term associated with the value. It should be noted that the Annotation object has no required properties, so the valueIRI in particular can be empty. 

The model (URL_TO_INSERT_TERM_2329 https://fairsharing.org/search?recordType=model_and_format)  also provides an extension mechanism through a schema object called `CategoryValuesPair`. This allows the addition of extra properties to the entities in cases where there are no specific properties to deal with the desired property. In order to capture the semantics of the category, CategoryValuesPairs capture both a `category` as a free-text string (URL_TO_INSERT_RECORD_2333 https://fairsharing.org/FAIRsharing.9b7wvk)  and a `categoryIRI` for the URI (URL_TO_INSERT_RECORD_2332 https://fairsharing.org/FAIRsharing.d261e1)  of an associated ontology (URL_TO_INSERT_TERM_2330 https://fairsharing.org/search?recordType=terminology_artefact)  context. The `values` are of type `Annotation` and can therefore also have ontology (URL_TO_INSERT_TERM_2331 https://fairsharing.org/search?recordType=terminology_artefact)  annotations.

DATS (URL_TO_INSERT_RECORD_2336 https://fairsharing.org/FAIRsharing.e20vsd)  does not prescribe the use of specific ontologies (URL_TO_INSERT_TERM_2335 https://fairsharing.org/search?recordType=terminology_artefact)  in relation to various properties, although it would be advisable to include this type of restriction in a given implementation of the model (URL_TO_INSERT_TERM_2334 https://fairsharing.org/search?recordType=model_and_format)  in order to simply the interoperability between different objects of the same type.

### Encoding in JSON-LD

DATS (URL_TO_INSERT_RECORD_2348 https://fairsharing.org/FAIRsharing.e20vsd)  objects are encoded in JSON (URL_TO_INSERT_RECORD_2350 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2356 https://fairsharing.org/FAIRsharing.8f9bbb) , a method for encoding linked data in the open standard (URL_TO_INSERT_TERM_2337 https://fairsharing.org/search?fairsharingRegistry=Standard)  file and data interchange format (URL_TO_INSERT_TERM_2341 https://fairsharing.org/search?recordType=model_and_format)  JSON (URL_TO_INSERT_RECORD_2351 https://fairsharing.org/FAIRsharing.5bbab9) . JSON (URL_TO_INSERT_RECORD_2352 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2357 https://fairsharing.org/FAIRsharing.8f9bbb)  is designed around the concept of a "context" to provide additional map (URL_TO_INSERT_RECORD_2354 https://fairsharing.org/FAIRsharing.53edcc) pings from JSON (URL_TO_INSERT_RECORD_2353 https://fairsharing.org/FAIRsharing.5bbab9)  to an RDF (URL_TO_INSERT_RECORD_2343 https://fairsharing.org/FAIRsharing.p77ph9)  model (URL_TO_INSERT_TERM_2338 https://fairsharing.org/search?recordType=model_and_format) . DATS (URL_TO_INSERT_RECORD_2349 https://fairsharing.org/FAIRsharing.e20vsd)  provides three sets of context map (URL_TO_INSERT_RECORD_2355 https://fairsharing.org/FAIRsharing.53edcc) pings, to DC (URL_TO_INSERT_RECORD_2358 https://fairsharing.org/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD_2360 https://fairsharing.org/3547) AT (URL_TO_INSERT_RECORD_2344 https://fairsharing.org/FAIRsharing.h4j3qm) , schema.org (URL_TO_INSERT_RECORD_2362 https://fairsharing.org/FAIRsharing.hzdzq8)  (SDO) and the OBO (URL_TO_INSERT_RECORD_2347 https://fairsharing.org/FAIRsharing.847069)  Foundry (URL_TO_INSERT_RECORD_2346 https://fairsharing.org/FAIRsharing.847069)  Ontologies (URL_TO_INSERT_TERM_2342 https://fairsharing.org/search?recordType=terminology_artefact) . None of the three sets of contexts individually cover all properties in the model (URL_TO_INSERT_TERM_2339 https://fairsharing.org/search?recordType=model_and_format)  but they can be used in combination to maximise the semantic linking of the model (URL_TO_INSERT_TERM_2340 https://fairsharing.org/search?recordType=model_and_format) , likely to increase interoperability, for instance with DC (URL_TO_INSERT_RECORD_2359 https://fairsharing.org/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD_2361 https://fairsharing.org/3547) AT (URL_TO_INSERT_RECORD_2345 https://fairsharing.org/FAIRsharing.h4j3qm)  based catalogues.



## Implementing DATS in a data catalogue

We implemented DATS (URL_TO_INSERT_RECORD_2365 https://fairsharing.org/FAIRsharing.e20vsd)  v2.0 in the [IMI Translational Data Catalog](https://datacatalog.elixir-luxembourg.org/). The DATS (URL_TO_INSERT_RECORD_2366 https://fairsharing.org/FAIRsharing.e20vsd)  model (URL_TO_INSERT_TERM_2363 https://fairsharing.org/search?recordType=model_and_format) 's flexibility presents both a benefit and a challenge in that some concepts could be encoded in a number of ways. Experimental materials for example can be encoded at both the Study level, in `Study.input` or at the Dataset level, in `Dataset.isAbout`. In order to encode metadata consistently and simplify indexing and display processes for the IMI Data Catalog (URL_TO_INSERT_RECORD_2367 https://fairsharing.org/FAIRsharing.de533c) , we therefore made a number of assumptions about how to encode certain metadata entities in the model (URL_TO_INSERT_TERM_2364 https://fairsharing.org/search?recordType=model_and_format) .

### Assumptions

* Study and Dataset objects can't exist without a Project (URL_TO_INSERT_TERM_2368 https://fairsharing.org/search?recordType=project) . This rule was necessary to provide a root for our indexing service.

* The Study object encodes informat (URL_TO_INSERT_TERM_2369 https://fairsharing.org/search?recordType=model_and_format) ion about the input materials to the experiment, such as study subjects in the case of clinical trials or biological molecules in the case of chemical assays. At this level, we collect cohort descriptions, sample sizes, sample sources, types of samples and diseases.
 
* The Dataset object encodes informat (URL_TO_INSERT_TERM_2371 https://fairsharing.org/search?recordType=model_and_format) ion about the dataset, including technical informat (URL_TO_INSERT_TERM_2372 https://fairsharing.org/search?recordType=model_and_format) ion such as version number, creation and update dates, data standard (URL_TO_INSERT_TERM_2370 https://fairsharing.org/search?fairsharingRegistry=Standard) s and file types. The dataset also lists the experiment types that generated the data, the number and types of samples that contributed to the dataset and any diseases in the samples. These properties can be distinct from the ones at Study level as not all samples collected in a Study may be used to generate a given dataset, e.g. blood samples might be used for sequencing experiments, generating a sequencing dataset, while other tissue samples are used in imaging assays, generating an imaging dataset. The number of samples collected can be different from the cohort sample size (i.e. number of subject), either because multiple samples were collected from each subject or because some samples were excluded from the dataset for quality reasons.

* In the implementation of the model (URL_TO_INSERT_TERM_2373 https://fairsharing.org/search?recordType=model_and_format) , preference as given to specific ontologies (URL_TO_INSERT_TERM_2374 https://fairsharing.org/search?recordType=terminology_artefact)  in certain contexts, eg MONDO (URL_TO_INSERT_RECORD_2379 https://fairsharing.org/FAIRsharing.b2979t)  for diseases, UBERON (URL_TO_INSERT_RECORD_2376 https://fairsharing.org/FAIRsharing.4c0b6b)  for anatomical components, NCIt (URL_TO_INSERT_RECORD_2375 https://fairsharing.org/FAIRsharing.4cvwxa) , EFO (URL_TO_INSERT_RECORD_2380 https://fairsharing.org/FAIRsharing.1gr4tz)  and OBI (URL_TO_INSERT_RECORD_2378 https://fairsharing.org/FAIRsharing.284e1z)  for experiment types, UO (URL_TO_INSERT_RECORD_2377 https://fairsharing.org/FAIRsharing.mjnypw)  for units etc.

---

## Conclusion

> * DATS (URL_TO_INSERT_RECORD_2382 https://fairsharing.org/FAIRsharing.e20vsd)  is a flexible data model (URL_TO_INSERT_TERM_2381 https://fairsharing.org/search?recordType=model_and_format)  aimed at biomedical datasets.
> * DATS (URL_TO_INSERT_RECORD_2384 https://fairsharing.org/FAIRsharing.e20vsd)  utilises the power of JSON (URL_TO_INSERT_RECORD_2385 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2386 https://fairsharing.org/FAIRsharing.8f9bbb)  to encode semantics at all levels of the model (URL_TO_INSERT_TERM_2383 https://fairsharing.org/search?recordType=model_and_format) .
> * DATS (URL_TO_INSERT_RECORD_2388 https://fairsharing.org/FAIRsharing.e20vsd) ' flexibility does mean that consistent implementation of the model (URL_TO_INSERT_TERM_2387 https://fairsharing.org/search?recordType=model_and_format)  in a specific context requires assumptions to be made.


### What should I read next?
> * [Building a catalogue of datasets](./data-catalog.md) 
> * [Deploying the IMI data catalog](./data-catalog-deployment.md) 
> * [Introduction to terminologies and ontologies](../interoperability/introduction-terminologies-ontologies.md)

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

