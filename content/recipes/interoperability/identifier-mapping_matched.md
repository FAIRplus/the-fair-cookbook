(fcb-identifier (URL_TO_INSERT_TERM_5223 https://fairsharing.org/search?recordType=identifier_schema) -map (URL_TO_INSERT_RECORD_5224 https://fairsharing.org/FAIRsharing.53edcc) ping)=
# Interlinking data from different sources


````{panels_fairplus}
:identifier_text: FCB016
:identifier_link: 'https://w3id.org/faircookbook/FCB016'
:difficulty_level: 2
:recipe_type: background_information
:reading_time_minutes: 30
:intended_audience: principal_investigator, data_manager, data_scientist  
:maturity_level: 4
:maturity_indicator: 49
:has_executable_code: nope
:recipe_name: Interlinking data from different sources
```` 


## Main Objectives

The **FAIR (URL_TO_INSERT_RECORD_5225 https://fairsharing.org/FAIRsharing.WWI10U)  principles**, under `Interoperability` state that: 
> I3. (Meta)data include qualified references to other (meta)data 

This is understood as providing metadata with machine readable cross-references when possible.

The main goals of this recipe are:

> - To understand where the need arises for map (URL_TO_INSERT_RECORD_5227 https://fairsharing.org/FAIRsharing.53edcc) ping between data identifier (URL_TO_INSERT_TERM_5226 https://fairsharing.org/search?recordType=identifier_schema) s.
> - How to represent equivalences for use by others.
> - Know what services are available to support data interoperability.

This recipe assumes that you are already fam (URL_TO_INSERT_RECORD_5230 https://fairsharing.org/FAIRsharing.d0886a) iliar with identifier (URL_TO_INSERT_TERM_5228 https://fairsharing.org/search?recordType=identifier_schema) s and the minting of identifier (URL_TO_INSERT_TERM_5229 https://fairsharing.org/search?recordType=identifier_schema) s.

*For more details on identifier (URL_TO_INSERT_TERM_5231 https://fairsharing.org/search?recordType=identifier_schema) s, see the {ref}`fcb-find-identifier (URL_TO_INSERT_TERM_5232 https://fairsharing.org/search?recordType=identifier_schema) s` recipe.*


## Graphical Overview

This recipe will cover the topics highlighted in orange:


````{dropdown} 
:open:
```{figure} identifier-mapping.md-figure1.mmd.png
---
width: 850px
name: identifier (URL_TO_INSERT_TERM_5233 https://fairsharing.org/search?recordType=identifier_schema) -map (URL_TO_INSERT_RECORD_5234 https://fairsharing.org/FAIRsharing.53edcc) ping-figure1
alt: Overview of key aspects in Identifier (URL_TO_INSERT_TERM_5235 https://fairsharing.org/search?recordType=identifier_schema)  Map (URL_TO_INSERT_RECORD_5236 https://fairsharing.org/FAIRsharing.53edcc) ping
---
Overview of key aspects in Identifier (URL_TO_INSERT_TERM_5237 https://fairsharing.org/search?recordType=identifier_schema)  Map (URL_TO_INSERT_RECORD_5238 https://fairsharing.org/FAIRsharing.53edcc) ping
```
````

---
<!-- 
## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [Identifier](http://edamontology.org/data_0842) |   |   |
 -->

## Table of Data Standards

| Data Format (URL_TO_INSERT_TERM_5240 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_5241 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_5239 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
| [IRI](https://tools.ietf.org/html/rfc3987) |   |   |
| [CURIE](https://www.w3.org/TR/2010/NOTE-curie-20101216 (URL_TO_INSERT_RECORD_5242 https://fairsharing.org/FAIRsharing.af21db) /) |   |   |
| [URL](https://tools.ietf.org/html/rfc1738) |  |  |
| [HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview) |  |  |
| [RDF](https://www.w3.org/RDF/) |  |  |
| [CSV](https://tools.ietf.org/html/rfc4180 (URL_TO_INSERT_RECORD_5243 https://fairsharing.org/FAIRsharing.1943d4) ) |  |  |
| [TSV](https://www.iana.org/assignments/media-types/text/tab-separated-values (URL_TO_INSERT_RECORD_5244 https://fairsharing.org/FAIRsharing.a978c9) ) |  |  |
| [VoID Linkset](https://www.w3.org/TR/void/) |  |  |

---

## Mappings

Before diving into identifier (URL_TO_INSERT_TERM_5245 https://fairsharing.org/search?recordType=identifier_schema)  map (URL_TO_INSERT_RECORD_5246 https://fairsharing.org/FAIRsharing.53edcc) ping, it is important to understand the possible types of map (URL_TO_INSERT_RECORD_5247 https://fairsharing.org/FAIRsharing.53edcc) pings that can be performed between entities.
While initially we might think of map (URL_TO_INSERT_RECORD_5250 https://fairsharing.org/FAIRsharing.53edcc) ping as simply linking identical entities in different database (URL_TO_INSERT_TERM_5248 https://fairsharing.org/search?fairsharingRegistry=Database) s/format (URL_TO_INSERT_TERM_5249 https://fairsharing.org/search?recordType=model_and_format) s, sometimes related entities might also be of interest. 
When these map (URL_TO_INSERT_RECORD_5251 https://fairsharing.org/FAIRsharing.53edcc) pings might only be interesting depending on the context in which data is being used, we run into a situation that has been described as "scientific lenses" (see {footcite}`batchelor_scientific_nodate`). 
These lenses allow us to dynamically select which map (URL_TO_INSERT_RECORD_5252 https://fairsharing.org/FAIRsharing.53edcc) pings to consider relevant and which to ignore.
For example allowing or disallowing map (URL_TO_INSERT_RECORD_5253 https://fairsharing.org/FAIRsharing.53edcc) pings between stereoisomers or between genes and proteins.

Examples of types of map (URL_TO_INSERT_RECORD_5254 https://fairsharing.org/FAIRsharing.53edcc) pings are:
* **Content map (URL_TO_INSERT_RECORD_5257 https://fairsharing.org/FAIRsharing.53edcc) ping**: where we are map (URL_TO_INSERT_RECORD_5258 https://fairsharing.org/FAIRsharing.53edcc) ping the actual entities by using techniques such as BLAST in biological sequences or comparing InChI (URL_TO_INSERT_RECORD_5256 https://fairsharing.org/FAIRsharing.ddk9t9)  identifier (URL_TO_INSERT_TERM_5255 https://fairsharing.org/search?recordType=identifier_schema) s for chemical compounds.
* **Ontology (URL_TO_INSERT_TERM_5259 https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD_5260 https://fairsharing.org/FAIRsharing.53edcc) ping**: this can either be: 
    * As a direct 1-to-1 map (URL_TO_INSERT_RECORD_5262 https://fairsharing.org/FAIRsharing.53edcc) ping between equivalent terms in different ontologies (URL_TO_INSERT_TERM_5261 https://fairsharing.org/search?recordType=terminology_artefact) .
    * As a complex m-to-m map (URL_TO_INSERT_RECORD_5264 https://fairsharing.org/FAIRsharing.53edcc) ping between terms in different ontologies (URL_TO_INSERT_TERM_5263 https://fairsharing.org/search?recordType=terminology_artefact)  taking into account their hierarch (URL_TO_INSERT_RECORD_5265 https://fairsharing.org/FAIRsharing.52b22c) ical structure, see {footcite}.`wang_concept_2010`.
* **Identifier (URL_TO_INSERT_TERM_5266 https://fairsharing.org/search?recordType=identifier_schema)  map (URL_TO_INSERT_RECORD_5267 https://fairsharing.org/FAIRsharing.53edcc) ping**: The focus of this recipe. This can either be:
    * Map (URL_TO_INSERT_RECORD_5272 https://fairsharing.org/FAIRsharing.53edcc) ping between differently formed identifier (URL_TO_INSERT_TERM_5268 https://fairsharing.org/search?recordType=identifier_schema) s that resolve to the same entity. (e.g. the same gene with different identifier (URL_TO_INSERT_TERM_5269 https://fairsharing.org/search?recordType=identifier_schema) s under HGNC (URL_TO_INSERT_RECORD_5271 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5273 https://fairsharing.org/FAIRsharing.29we0s)  and Ensembl (URL_TO_INSERT_RECORD_5270 https://fairsharing.org/FAIRsharing.fx0mw7) ).
    * Map (URL_TO_INSERT_RECORD_5278 https://fairsharing.org/FAIRsharing.53edcc) ping between identical local identifier (URL_TO_INSERT_TERM_5275 https://fairsharing.org/search?recordType=identifier_schema) s with different namespaces (e.g. PDB (URL_TO_INSERT_RECORD_5277 https://fairsharing.org/FAIRsharing.9y4cqw)  where there exist regional mirrors of the database (URL_TO_INSERT_TERM_5274 https://fairsharing.org/search?fairsharingRegistry=Database)  so accesion/local identifier (URL_TO_INSERT_TERM_5276 https://fairsharing.org/search?recordType=identifier_schema)  is the same but namespace is different).
    * Map (URL_TO_INSERT_RECORD_5280 https://fairsharing.org/FAIRsharing.53edcc) ping between entities that are related enough to be usefully connected (e.g. linking informat (URL_TO_INSERT_TERM_5279 https://fairsharing.org/search?recordType=model_and_format) ion on proteins, genes, RNA and reporter sequences for these).
    * Map (URL_TO_INSERT_RECORD_5286 https://fairsharing.org/FAIRsharing.53edcc) ping between database (URL_TO_INSERT_TERM_5281 https://fairsharing.org/search?fairsharingRegistry=Database) s containing different informat (URL_TO_INSERT_TERM_5284 https://fairsharing.org/search?recordType=model_and_format) ion about the same entity (e.g. links between the protein sequence database (URL_TO_INSERT_TERM_5282 https://fairsharing.org/search?fairsharingRegistry=Database)  UniProt and the protein 3D structure database (URL_TO_INSERT_TERM_5283 https://fairsharing.org/search?fairsharingRegistry=Database)  PDB (URL_TO_INSERT_RECORD_5285 https://fairsharing.org/FAIRsharing.9y4cqw) ).


---

## Identifier Mappings

```{note} 
**"Identifiers are used to tag, identify, find and retrieve entities which are part of a collection or a resource maintained by some organization. "**
```

To satisfy the Findability criteria F1, organisations must create identifier (URL_TO_INSERT_TERM_5289 https://fairsharing.org/search?recordType=identifier_schema) s for the concepts within their database (URL_TO_INSERT_TERM_5287 https://fairsharing.org/search?fairsharingRegistry=Database) . This generates locally unique identifier (URL_TO_INSERT_TERM_5290 https://fairsharing.org/search?recordType=identifier_schema) s which can in turn be transformed into globally unique identifier (URL_TO_INSERT_TERM_5291 https://fairsharing.org/search?recordType=identifier_schema) s using namespaces for which the database (URL_TO_INSERT_TERM_5288 https://fairsharing.org/search?fairsharingRegistry=Database)  organisation are the `authority`. 

Database (URL_TO_INSERT_TERM_5292 https://fairsharing.org/search?fairsharingRegistry=Database) s often contain data that exists in, or is closely related to, the content of other database (URL_TO_INSERT_TERM_5293 https://fairsharing.org/search?fairsharingRegistry=Database) s. For example, the genome database (URL_TO_INSERT_TERM_5294 https://fairsharing.org/search?fairsharingRegistry=Database)  [Ensembl](http://ensembl.org/) contains data about genes that are related to entries in database (URL_TO_INSERT_TERM_5295 https://fairsharing.org/search?fairsharingRegistry=Database) s such as HUGO Gene Nomenclature Committee (URL_TO_INSERT_RECORD_5309 https://fairsharing.org/FAIRsharing.29we0s)  (https://www.genenames.org (URL_TO_INSERT_RECORD_5307 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_5310 https://fairsharing.org/FAIRsharing.29we0s) /) or [NCBI Gene (URL_TO_INSERT_RECORD_5305 https://fairsharing.org/FAIRsharing.5h3maw) ](https://www.ncbi.nlm.nih.gov/gene (URL_TO_INSERT_RECORD_5306 https://fairsharing.org/FAIRsharing.5h3maw) /); or a database (URL_TO_INSERT_TERM_5296 https://fairsharing.org/search?fairsharingRegistry=Database)  about drugs, e.g. [DrugBank](https://drugbank.com/), often contains details of the chemical substance that forms the drug which are also contained in chemical database (URL_TO_INSERT_TERM_5297 https://fairsharing.org/search?fairsharingRegistry=Database) s such as [ChEBI](https://www.ebi.ac.uk/chebi (URL_TO_INSERT_RECORD_5304 https://fairsharing.org/FAIRsharing.62qk8w) /) or [PubChem](https://pubchem.ncbi.nlm.nih.gov (URL_TO_INSERT_RECORD_5308 https://fairsharing.org/FAIRsharing.qt3w7z) /). This results in a large number of unique identifier (URL_TO_INSERT_TERM_5301 https://fairsharing.org/search?recordType=identifier_schema) s notionally for the same concept. This large number of identifier (URL_TO_INSERT_TERM_5302 https://fairsharing.org/search?recordType=identifier_schema) s for the same concept prevents interoperability of the data, since additional knowledge is needed to know which identifier (URL_TO_INSERT_TERM_5303 https://fairsharing.org/search?recordType=identifier_schema) s represent the same concept from different database (URL_TO_INSERT_TERM_5298 https://fairsharing.org/search?fairsharingRegistry=Database) s. However, the database (URL_TO_INSERT_TERM_5299 https://fairsharing.org/search?fairsharingRegistry=Database) s often contain `cross-reference` links to other database (URL_TO_INSERT_TERM_5300 https://fairsharing.org/search?fairsharingRegistry=Database) s to represent these `equivalences`.

The need for each database (URL_TO_INSERT_TERM_5311 https://fairsharing.org/search?fairsharingRegistry=Database)  to mint their own identifier (URL_TO_INSERT_TERM_5314 https://fairsharing.org/search?recordType=identifier_schema)  is a result of each taking a different perspective on the concept. For example, a chemical database (URL_TO_INSERT_TERM_5312 https://fairsharing.org/search?fairsharingRegistry=Database)  will distinguish between different salt forms of the chemical whereas a drug database (URL_TO_INSERT_TERM_5313 https://fairsharing.org/search?fairsharingRegistry=Database)  may not contain this differentiation. These differences in perspective are driven by the goal of the databse in terms of the data that they store. The interlinking of these data items can affect the reuse of the data in applications. As such, the declaration of cross-references should be done in a way that allows others to understand the nature of the equivalence declared, and therefore determine if it is appropriate for their use (see {footcite}`batchelor_scientific_nodate` for more details).

While the minting of identifier (URL_TO_INSERT_TERM_5319 https://fairsharing.org/search?recordType=identifier_schema) s is often done in isolation of other organisations,  there are instances of database (URL_TO_INSERT_TERM_5315 https://fairsharing.org/search?fairsharingRegistry=Database) s who reuse identifier (URL_TO_INSERT_TERM_5320 https://fairsharing.org/search?recordType=identifier_schema) s from a well known community database (URL_TO_INSERT_TERM_5316 https://fairsharing.org/search?fairsharingRegistry=Database) . For example, the [Human Protein (URL_TO_INSERT_RECORD_5326 https://fairsharing.org/FAIRsharing.rtndct)  Atlas](https://www.proteinatlas.org (URL_TO_INSERT_RECORD_5329 https://fairsharing.org/FAIRsharing.j0t0pe) /) database (URL_TO_INSERT_TERM_5317 https://fairsharing.org/search?fairsharingRegistry=Database)  reuses [Ensembl](https://www.ensembl.org (URL_TO_INSERT_RECORD_5325 https://fairsharing.org/FAIRsharing.fx0mw7) /) identifier (URL_TO_INSERT_TERM_5321 https://fairsharing.org/search?recordType=identifier_schema) s for their data records. In these cases there is no need to map (URL_TO_INSERT_RECORD_5330 https://fairsharing.org/FAIRsharing.53edcc)  between the data instances in the two database (URL_TO_INSERT_TERM_5318 https://fairsharing.org/search?fairsharingRegistry=Database) s, the data is already connected through the common identifier (URL_TO_INSERT_TERM_5322 https://fairsharing.org/search?recordType=identifier_schema) . However, this means that the Human Protein (URL_TO_INSERT_RECORD_5327 https://fairsharing.org/FAIRsharing.rtndct)  Atlas (URL_TO_INSERT_RECORD_5328 https://fairsharing.org/FAIRsharing.j0t0pe)  must ensure that their definition of the concept is exactly aligned with the Ensembl (URL_TO_INSERT_RECORD_5324 https://fairsharing.org/FAIRsharing.fx0mw7)  identifier (URL_TO_INSERT_TERM_5323 https://fairsharing.org/search?recordType=identifier_schema)  for **all** application uses.

## Identifier Equivalences

Identifier (URL_TO_INSERT_TERM_5331 https://fairsharing.org/search?recordType=identifier_schema)  equivalences can come about in several ways and capture different forms of relationship as presented in [Map (URL_TO_INSERT_RECORD_5332 https://fairsharing.org/FAIRsharing.53edcc) pings](#Map (URL_TO_INSERT_RECORD_5333 https://fairsharing.org/FAIRsharing.53edcc) pings).
For example, a database (URL_TO_INSERT_TERM_5334 https://fairsharing.org/search?fairsharingRegistry=Database)  may declare that their record is the same as an entry in another because they share the same name, or they may declare it based on a common representation (gene sequence or InChI (URL_TO_INSERT_RECORD_5335 https://fairsharing.org/FAIRsharing.ddk9t9) ).
To support reuse of the data, the `provenance` of the cross-references needs to be made explicit. 

Depending on the nature of the data, there are different ways that equivalences can be computed. 

Some elements to take into consideration are:

1. a **map (URL_TO_INSERT_RECORD_5337 https://fairsharing.org/FAIRsharing.53edcc) ping predicate** taken from a well known ontology (URL_TO_INSERT_TERM_5336 https://fairsharing.org/search?recordType=terminology_artefact) , e.g. `owl:sameAs` or `skos:narrower`.
2. the **evidence** behind the equivalence claims, e.g. a similarity score (URL_TO_INSERT_RECORD_5339 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_5340 https://fairsharing.org/FAIRsharing.xMmOCL)  or the property on which the equivalence is based such as InChI (URL_TO_INSERT_RECORD_5338 https://fairsharing.org/FAIRsharing.ddk9t9)  Key for chemicals.
1. **audit trail informat (URL_TO_INSERT_TERM_5341 https://fairsharing.org/search?recordType=model_and_format) ion**, i.e. who, what, when, e.g. `agent X using map (URL_TO_INSERT_RECORD_5344 https://fairsharing.org/FAIRsharing.53edcc) ping tool Y on YYYY-MM-DD`. PRO (URL_TO_INSERT_RECORD_5343 https://fairsharing.org/FAIRsharing.3e88d6)  (URL_TO_INSERT_RECORD_5345 https://fairsharing.org/FAIRsharing.4ndncv) V-O (URL_TO_INSERT_RECORD_5346 https://fairsharing.org/FAIRsharing.2rm2b3)  ontology (URL_TO_INSERT_TERM_5342 https://fairsharing.org/search?recordType=terminology_artefact)  could be used to support such statements.



## Exchanging Identifier Mappings

There are several file format (URL_TO_INSERT_TERM_5347 https://fairsharing.org/search?recordType=model_and_format)  for exchanging identifier (URL_TO_INSERT_TERM_5348 https://fairsharing.org/search?recordType=identifier_schema)  equivalences.
 We will discuss the most widely used format (URL_TO_INSERT_TERM_5350 https://fairsharing.org/search?recordType=model_and_format) s and demonstrate them with a sample of data derived from [ChEMBL](https://www.ebi.ac.uk/chembl (URL_TO_INSERT_RECORD_5352 https://fairsharing.org/FAIRsharing.m3jtpg) /) which provides cross-reference equivalences for two records in the ChEMBL (URL_TO_INSERT_RECORD_5351 https://fairsharing.org/FAIRsharing.m3jtpg)  database (URL_TO_INSERT_TERM_5349 https://fairsharing.org/search?fairsharingRegistry=Database)  to UniProt proteins.

### Using Text File

The simplest way to exchange equivalences is in a simple text file, which could be structured as a tab-separated-value (TSV) file. Such a file usually consists of two columns, one per dataset, and each row represents an equivalence declaration. The interpretation is that the two identifier (URL_TO_INSERT_TERM_5353 https://fairsharing.org/search?recordType=identifier_schema) s on the same row are equivalent in some way. These files tend to carry little to no metadata about the map (URL_TO_INSERT_RECORD_5354 https://fairsharing.org/FAIRsharing.53edcc) pings, i.e. the mechanism by which the map (URL_TO_INSERT_RECORD_5355 https://fairsharing.org/FAIRsharing.53edcc) ping was derived is not given, nor are details of the version of the datasets that were linked.

The following example shows the map (URL_TO_INSERT_RECORD_5357 https://fairsharing.org/FAIRsharing.53edcc) ping equivalences between ChEMBL (URL_TO_INSERT_RECORD_5356 https://fairsharing.org/FAIRsharing.m3jtpg)  target components (proteins) and UniProt proteins.

```bash
ChEMBL_Target_Component	UniProt
CHEMBL_TC_4803	A0ZX81
CHEMBL_TC_2584	A1ZA98 
```


### Using Simple Standard for Sharing Ontology Mappings (SSSOM) formatted text files

The OBO (URL_TO_INSERT_RECORD_5367 https://fairsharing.org/FAIRsharing.847069) Foundry Simple Standard (URL_TO_INSERT_TERM_5358 https://fairsharing.org/search?fairsharingRegistry=Standard)  for Sharing Ontology (URL_TO_INSERT_TERM_5364 https://fairsharing.org/search?recordType=terminology_artefact)  Map (URL_TO_INSERT_RECORD_5368 https://fairsharing.org/FAIRsharing.53edcc) pings (URL_TO_INSERT_RECORD_5375 https://fairsharing.org/1411)  ([SSSOM](https://github.com (URL_TO_INSERT_RECORD_5373 https://fairsharing.org/FAIRsharing.c55d5e) /OBOFoundry/SSSOM)) is a newly emerging standard (URL_TO_INSERT_TERM_5359 https://fairsharing.org/search?fairsharingRegistry=Standard)  for exchanging map (URL_TO_INSERT_RECORD_5369 https://fairsharing.org/FAIRsharing.53edcc) ping informat (URL_TO_INSERT_TERM_5361 https://fairsharing.org/search?recordType=model_and_format) ion with minimal metadata, although the minimal model (URL_TO_INSERT_TERM_5360 https://fairsharing.org/search?recordType=model_and_format)  is extensible. It consists of a tab-separated-value file (TSV) with each row representing a map (URL_TO_INSERT_RECORD_5370 https://fairsharing.org/FAIRsharing.53edcc) ping. The columns in the file have been defined by the community ([latest version](https://github.com (URL_TO_INSERT_RECORD_5374 https://fairsharing.org/FAIRsharing.c55d5e) /OBOFoundry/SSSOM/blob/master/SSSOM.md)) and provide the map (URL_TO_INSERT_RECORD_5371 https://fairsharing.org/FAIRsharing.53edcc) ping together with its provenance. At present, four columns are required (`subject_id`, `predicate_id`, `object_id`, `match_type`) with optional columns to provide more provenance to support the map (URL_TO_INSERT_RECORD_5372 https://fairsharing.org/FAIRsharing.53edcc) ping, e.g. licensing informat (URL_TO_INSERT_TERM_5362 https://fairsharing.org/search?recordType=model_and_format) ion, author informat (URL_TO_INSERT_TERM_5363 https://fairsharing.org/search?recordType=model_and_format) ion, creation method. The use of CURIE (URL_TO_INSERT_RECORD_5366 https://fairsharing.org/FAIRsharing.af21db) s within the TSV (URL_TO_INSERT_RECORD_5365 https://fairsharing.org/FAIRsharing.a978c9)  is strongly encouraged.

The following TSV (URL_TO_INSERT_RECORD_5378 https://fairsharing.org/FAIRsharing.a978c9)  shows our example data as a map (URL_TO_INSERT_RECORD_5379 https://fairsharing.org/FAIRsharing.53edcc) ping file using the minimal columns (correct as of November 2020). The informat (URL_TO_INSERT_TERM_5377 https://fairsharing.org/search?recordType=model_and_format) ion provided is less than the minimal VoID model (URL_TO_INSERT_TERM_5376 https://fairsharing.org/search?recordType=model_and_format)  above.

```bash
subject_id  predicate_id  object_id match_type
chembl:CHEMBL_TC_4803 skos:exactMatch uniprot:A0ZX81  sio:database-cross-reference
chembl:CHEMBL_TC_2584 skos:exactMatch uniprot:A1ZA98  sio:database-cross-reference
```


### Using Vocabulary of Interlinked Datasets Linkset Files

The Vocabulary of Interlinked Datasets ([VoID](http://www.w3.org/TR/void/)) provides an ontology (URL_TO_INSERT_TERM_5381 https://fairsharing.org/search?recordType=terminology_artefact)  of terms for describing RDF (URL_TO_INSERT_RECORD_5382 https://fairsharing.org/FAIRsharing.p77ph9)  datasets. These descriptions include basic informat (URL_TO_INSERT_TERM_5380 https://fairsharing.org/search?recordType=model_and_format) ion about the dataset, e.g. its name, description, license, etc, but also introduces a mechanism for exchanging data instance map (URL_TO_INSERT_RECORD_5383 https://fairsharing.org/FAIRsharing.53edcc) pings called `linksets`.

A `linkset` contains the identifier (URL_TO_INSERT_TERM_5385 https://fairsharing.org/search?recordType=identifier_schema)  map (URL_TO_INSERT_RECORD_5387 https://fairsharing.org/FAIRsharing.53edcc) pings together with either the metadata at the top of the file or a link to a VoID file describing the data source. The Open PHACTS project (URL_TO_INSERT_TERM_5384 https://fairsharing.org/search?recordType=project)  defined a usage profile for use within the life sciences community [Open PHACTS Dataset Descriptions](http://www.openphacts.org/specs/datadesc/) which was later refined by the W3C Health Care and Life Sciences Community Group ([W3C HCLS Linksets](https://www.w3.org/TR/hcls-dataset (URL_TO_INSERT_RECORD_5386 https://fairsharing.org/FAIRsharing.s248mf) /#linksets)).

The following example shows a VoID Linkset in turtle notation with the minimum metadata given in the header. The metadata block links to the ChEMBL (URL_TO_INSERT_RECORD_5390 https://fairsharing.org/FAIRsharing.m3jtpg)  17 RDF (URL_TO_INSERT_RECORD_5389 https://fairsharing.org/FAIRsharing.p77ph9)  description and the UniProt March (URL_TO_INSERT_RECORD_5391 https://fairsharing.org/FAIRsharing.52b22c)  2015 release. The `linkPredicate` tells us that the link is an exact match, i.e. the linked instances can be deemed equivalent for most applications, and the `linksetJustification` property states that the link is declared as a Database (URL_TO_INSERT_TERM_5388 https://fairsharing.org/search?fairsharingRegistry=Database)  Cross Reference assertion, rather than being computed based on an equivalent protein sequence. These properties allow consuming applications to make more informed choices about their reuse of the data.

```bash
@prefix bdb: <http://vocabularies.bridgedb.org/ops#> .
@prefix chembl: <http://rdf.ebi.ac.uk/resource/chembl/> .
@prefix chembl_target_cmpt: <http://rdf.ebi.ac.uk/resource/chembl/targetcomponent/> .
@prefix sio: <https://semanticscience.org/resource/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix uniprot: <http://purl.uniprot.org/uniprot/> .
@prefix void: <http://rdfs.org/ns/void#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:chembl17-uniprot-exactMatch-linkset a void:Linkset ;
    void:subjectsTarget :chembl17-rdf ;
    void:objectsTarget <http://purl.uniprot.org/void#UniProtDataset_2015_03> ;
    void:linkPredicate skos:exactMatch ;
    bdb:linksetJustification sio:database-cross-reference
    void:triples "6367"^^xsd:integer .

chembl_target_cmpt:CHEMBL_TC_4803 skos:exactMatch uniprot:A0ZX81 .
chembl_target_cmpt:CHEMBL_TC_2584 skos:exactMatch uniprot:A1ZA98 .
...
```

### A couple of observations


> - SSSOM (URL_TO_INSERT_RECORD_5393 https://fairsharing.org/1411)  is an emerging community standard (URL_TO_INSERT_TERM_5392 https://fairsharing.org/search?fairsharingRegistry=Standard)  that is still not finalised.
> While the basic metadata model (URL_TO_INSERT_TERM_5394 https://fairsharing.org/search?recordType=model_and_format)  has less informat (URL_TO_INSERT_TERM_5395 https://fairsharing.org/search?recordType=model_and_format) ion than the VoID file, there are additional properties for providing more detail.
> Properties that related to the set of map (URL_TO_INSERT_RECORD_5397 https://fairsharing.org/FAIRsharing.53edcc) pings can can be included as a comment block at the start of the TSV (URL_TO_INSERT_RECORD_5396 https://fairsharing.org/FAIRsharing.a978c9) .
> - The VoID Linkset approach for exchanging map (URL_TO_INSERT_RECORD_5398 https://fairsharing.org/FAIRsharing.53edcc) pings separates the metadata from the data map (URL_TO_INSERT_RECORD_5399 https://fairsharing.org/FAIRsharing.53edcc) pings. 
> This eliminates duplication of metadata. However, as currently defined, the VoID Linksets can only be used for RDF (URL_TO_INSERT_RECORD_5400 https://fairsharing.org/FAIRsharing.p77ph9)  data.
> The above has shown that the two format (URL_TO_INSERT_TERM_5401 https://fairsharing.org/search?recordType=model_and_format) s can represent the same informat (URL_TO_INSERT_TERM_5402 https://fairsharing.org/search?recordType=model_and_format) ion. Both VoID and SSSOM (URL_TO_INSERT_RECORD_5403 https://fairsharing.org/1411)  can be used to provide very rich metadata for exchanging data.

## Identifier Mapping services

Identifier (URL_TO_INSERT_TERM_5407 https://fairsharing.org/search?recordType=identifier_schema)  map (URL_TO_INSERT_RECORD_5409 https://fairsharing.org/FAIRsharing.53edcc) ping services are database (URL_TO_INSERT_TERM_5404 https://fairsharing.org/search?fairsharingRegistry=Database) s that contain lists of identifier (URL_TO_INSERT_TERM_5408 https://fairsharing.org/search?recordType=identifier_schema) s, often from different database (URL_TO_INSERT_TERM_5405 https://fairsharing.org/search?fairsharingRegistry=Database) s, that are known to be equivalent. These are consumed from original data sources and third parties in one of the format (URL_TO_INSERT_TERM_5406 https://fairsharing.org/search?recordType=model_and_format) s provided above.

The common functionality offered by these services is to return a set of equivalent identifier (URL_TO_INSERT_TERM_5410 https://fairsharing.org/search?recordType=identifier_schema) s for a given identifier (URL_TO_INSERT_TERM_5411 https://fairsharing.org/search?recordType=identifier_schema) . That is, you can ask these services for all identifier (URL_TO_INSERT_TERM_5412 https://fairsharing.org/search?recordType=identifier_schema) s that are equivalent to your identifier (URL_TO_INSERT_TERM_5413 https://fairsharing.org/search?recordType=identifier_schema) . The services will vary in the response depending on their coverage of data sources and whether they decide to compute the transitive closure of the identifier (URL_TO_INSERT_TERM_5414 https://fairsharing.org/search?recordType=identifier_schema) s. That is, if data source A declares that `A:id1` is equivalent to `B:acc32`, and data source C declares that `C:67cb2865-781f-4450-a99c-e9b33bf4d5b5` is equivalent to `B:acc32`, should a lookup for equivalent identifier (URL_TO_INSERT_TERM_5415 https://fairsharing.org/search?recordType=identifier_schema) s for `A:id1` return `C:67cb2865-781f-4450-a99c-e9b33bf4d5b5` since `A:id1 <=> B:acc32` and `B:acc32 <=> C:67cb2865-781f-4450-a99c-e9b33bf4d5b5`.

The following is an incomplete list of identifier (URL_TO_INSERT_TERM_5416 https://fairsharing.org/search?recordType=identifier_schema)  map (URL_TO_INSERT_RECORD_5417 https://fairsharing.org/FAIRsharing.53edcc) ping services.

* [bridgedb.org](https://bridgedb.github.io (URL_TO_INSERT_RECORD_5418 https://fairsharing.org/FAIRsharing.5ry74y) /) 

    > [BridgeDb](https://bridgedb.github.io (URL_TO_INSERT_RECORD_5421 https://fairsharing.org/FAIRsharing.5ry74y) /) {footcite}`van_iersel_bridgedb (URL_TO_INSERT_RECORD_5420 https://fairsharing.org/FAIRsharing.5ry74y) _2010` is a framework for identifier (URL_TO_INSERT_TERM_5419 https://fairsharing.org/search?recordType=identifier_schema)  map (URL_TO_INSERT_RECORD_5422 https://fairsharing.org/FAIRsharing.53edcc) ping within the life sciences which covers genes, proteins, genetic variants, metabolites, and metabolic reactions. It is provided as a web service, a standalone application that can be installed locally, a Java library or an R Package.
    > 
    > It permits users to lookup equivalent database (URL_TO_INSERT_TERM_5423 https://fairsharing.org/search?fairsharingRegistry=Database)  identifier (URL_TO_INSERT_TERM_5425 https://fairsharing.org/search?recordType=identifier_schema) s for a given database (URL_TO_INSERT_TERM_5424 https://fairsharing.org/search?fairsharingRegistry=Database)  identifier (URL_TO_INSERT_TERM_5426 https://fairsharing.org/search?recordType=identifier_schema)  within a specified organism. The following `curl` command to the REST API retrieves the equivalent identifier (URL_TO_INSERT_TERM_5427 https://fairsharing.org/search?recordType=identifier_schema) s for the EntrezGene (now known as NCBI Gene (URL_TO_INSERT_RECORD_5430 https://fairsharing.org/FAIRsharing.5h3maw) ) `L` identifier (URL_TO_INSERT_TERM_5428 https://fairsharing.org/search?recordType=identifier_schema)  `1234` for the `Human` gene [CCR5](https://www.ncbi.nlm.nih.gov/gene (URL_TO_INSERT_RECORD_5431 https://fairsharing.org/FAIRsharing.5h3maw) /1234) as a TSV (URL_TO_INSERT_RECORD_5429 https://fairsharing.org/FAIRsharing.a978c9)  file.
    >```bash
    >curl -X GET "https://webservice.bridgedb.org/Human/xrefs/L/1234" -H "accept: */*"
    >```
    > * [BridgeDb (URL_TO_INSERT_RECORD_5432 https://fairsharing.org/FAIRsharing.5ry74y) R Tutorial](https://bioconductor.org (URL_TO_INSERT_RECORD_5433 https://fairsharing.org/FAIRsharing.81ettx) /packages/release/bioc/vignettes/BridgeDbR/inst/doc/tutorial.html)

* [UniChem](https://www.ebi.ac.uk/unichem/)
    > [UniChem](https://www.ebi.ac.uk/unichem/) {footcite}`chambers_unichem_2013` is a specialised identifier (URL_TO_INSERT_TERM_5434 https://fairsharing.org/search?recordType=identifier_schema)  map (URL_TO_INSERT_RECORD_5439 https://fairsharing.org/FAIRsharing.53edcc) ping service for chemical structures. For a chemical structure -- specified as an identifier (URL_TO_INSERT_TERM_5435 https://fairsharing.org/search?recordType=identifier_schema) , InChI (URL_TO_INSERT_RECORD_5437 https://fairsharing.org/FAIRsharing.ddk9t9) , or InChI (URL_TO_INSERT_RECORD_5438 https://fairsharing.org/FAIRsharing.ddk9t9)  Key -- it will equivalent structures found in the [EMBL-EBI](https://www.ebi.ac.uk/) chemistry (URL_TO_INSERT_RECORD_5436 https://fairsharing.org/3524)  resources.
    > 
    > The following `curl` command retrieves the equivalent database (URL_TO_INSERT_TERM_5440 https://fairsharing.org/search?fairsharingRegistry=Database)  identifier (URL_TO_INSERT_TERM_5441 https://fairsharing.org/search?recordType=identifier_schema) s for the ChEMBL (URL_TO_INSERT_RECORD_5444 https://fairsharing.org/FAIRsharing.m3jtpg)  identifier (URL_TO_INSERT_TERM_5442 https://fairsharing.org/search?recordType=identifier_schema)  `CHEMBL (URL_TO_INSERT_RECORD_5445 https://fairsharing.org/FAIRsharing.m3jtpg) 12` [DIAZEPAM](https://www.ebi.ac.uk/chembl (URL_TO_INSERT_RECORD_5446 https://fairsharing.org/FAIRsharing.m3jtpg) /compound_report_card/CHEMBL12/) and returns the result as a JSON (URL_TO_INSERT_RECORD_5443 https://fairsharing.org/FAIRsharing.5bbab9)  object.
    > ```bash
    > curl -X GET "https://www.ebi.ac.uk/unichem/rest/src_compound_id/CHEMBL12/1" -H "accept: */*"
    > ```

    > For more informat (URL_TO_INSERT_TERM_5447 https://fairsharing.org/search?recordType=model_and_format) ion including the available methods, see the [UniChem REST documentation](https://www.ebi.ac.uk/unichem/info/webservices).
* [sameas.org](http://sameas.org/)
  
    > [sameas.org](http://sameas.org/) is a general purpose service that will return a set of equivalent URL (URL_TO_INSERT_RECORD_5448 https://fairsharing.org/FAIRsharing.9d38e2) s for a given URL (URL_TO_INSERT_RECORD_5449 https://fairsharing.org/FAIRsharing.9d38e2) . The equivalences are based on an incomplete set of `owl:sameAs` statements contained in data available on the web.
    > 
    > The following `curl` command retrieves the equivalent URL (URL_TO_INSERT_RECORD_5452 https://fairsharing.org/FAIRsharing.9d38e2) s for EBI RDF (URL_TO_INSERT_RECORD_5450 https://fairsharing.org/FAIRsharing.p77ph9)  Platform representation of ChEMBL (URL_TO_INSERT_RECORD_5453 https://fairsharing.org/FAIRsharing.m3jtpg)  [DIAZEPAM](https://rdf.ebi.ac.uk/resource/chembl/molecule/CHEMBL12) as a JSON (URL_TO_INSERT_RECORD_5451 https://fairsharing.org/FAIRsharing.5bbab9)  object.
    > ```bash
    > curl -iLH "Accept: application/json" "http://sameas.org/?uri=http://rdf.ebi.ac.uk/resource/chembl/molecule/CHEMBL12"
    > ```
    > Note that the coverage of http://sameas.org within the life sciences is very small.


<!-- * [Identifiers.org](https://identifiers.org/)

    > [Identifiers.org](https://identifiers.org) is a **Resolution Service** that provides access to alternative mirrors of the same database which are located at different URLs on the web. For example, the UniProt database is based as the Swiss Institute of Bioinformatics but is also mirrored on the NCBI in the States.
    > 
    > The following URL https://identifiers.org/uniprot:P38938 resolves to the UniProt page https://www.uniprot.org/uniprot/P38938 by default (meaning that these identifiers are equivalent) but if the SIB service is unavailable will resolve to https://www.ncbi.nlm.nih.gov/protein/P38938. -->



## Conclusion

In this recipe, we have given an overview of the need to map (URL_TO_INSERT_RECORD_5455 https://fairsharing.org/FAIRsharing.53edcc)  between globally unique and persistent identifier (URL_TO_INSERT_TERM_5454 https://fairsharing.org/search?recordType=identifier_schema) s from different data sources where they cover the same concept, i.e. FAIR (URL_TO_INSERT_RECORD_5456 https://fairsharing.org/FAIRsharing.WWI10U)  principle I3. We have covered:

- The idea of data identifier (URL_TO_INSERT_TERM_5457 https://fairsharing.org/search?recordType=identifier_schema)  equivalence;
- How to publish and exchange data identifier (URL_TO_INSERT_TERM_5458 https://fairsharing.org/search?recordType=identifier_schema)  equivalences;
- Data identifier (URL_TO_INSERT_TERM_5459 https://fairsharing.org/search?recordType=identifier_schema)  map (URL_TO_INSERT_RECORD_5461 https://fairsharing.org/FAIRsharing.53edcc) ping services which can be queried to find equivalences for a given identifier (URL_TO_INSERT_TERM_5460 https://fairsharing.org/search?recordType=identifier_schema) .

Data identifier (URL_TO_INSERT_TERM_5462 https://fairsharing.org/search?recordType=identifier_schema)  equivalences increase the interoperability between data sources since it allows data about an individual to be integrated together. 
As a minimum, you should aim to link your dataset's persistant data identifier (URL_TO_INSERT_TERM_5463 https://fairsharing.org/search?recordType=identifier_schema) s to one major dataset within the community. The [ELIXIR Core (URL_TO_INSERT_RECORD_5464 https://fairsharing.org/FAIRsharing.xMmOCL)  Data Resources](https://elixir-europe.org (URL_TO_INSERT_RECORD_5465 https://fairsharing.org/3531) /platforms/data/core-data-resources) provide a useful list of major datasets within the life sciences.

### What to read next?

* {ref}`fcb-find-identifier (URL_TO_INSERT_TERM_5466 https://fairsharing.org/search?recordType=identifier_schema) s`
* [The Pistoia Alliance FAIR (URL_TO_INSERT_RECORD_5469 https://fairsharing.org/FAIRsharing.WWI10U) toolkit use cases: Adoption and Impact of an identifier (URL_TO_INSERT_TERM_5468 https://fairsharing.org/search?recordType=identifier_schema)  policy (URL_TO_INSERT_TERM_5467 https://fairsharing.org/search?fairsharingRegistry=Policy)  at Astra-Zeneca](https://fairtoolkit.pistoiaalliance.org/use-cases/adoption-and-impact-of-an-identifier-policy-astrazeneca/)
* {ref}`fcb-bridgedb (URL_TO_INSERT_RECORD_5470 https://fairsharing.org/FAIRsharing.5ry74y) -recipe`
* [Dataset Descriptions for the Open Pharmacological Space](http://www.openphacts.org/specs/datadesc/)

````{rdmkit_panel}
````
<!-- 
    > * [Identifier Resolution Services](./findability/id-resolution.html) 
-->



## References
````{dropdown} **References**
```{footbibliography}
```
````

<!-- ```{bibliography}
:filter: docname in docnames
:style: alpha
``` -->


## Authors
````{authors_fairplus}
Alasdair: Writing - Original Draft
Chris: Writing - Original Draft
Egon: Writing - Original Draft
Lucas: Writing - Review & Editing
Philippe: Writing - Review & Editing
````


## License
````{license_fairplus}
CC-BY-4.0
````
