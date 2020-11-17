---
dummy: dummy
---

# How to interlink data from different sources?

___

<div class="row">

  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-qrcode fa-2x" style="color:#7e0038"></i>
        <h4><b>Recipe metadata</b></h4>
        <p> identifier: <a href="">RX.X</a> </p>
        <p> version: <a href="">v1.0</a> </p>
      </div>
    </div>
  </div>
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-fire fa-2x" style="color:#7e0038"></i>
        <h4><b>Difficulty level</b></h4>
        <i class="fa fa-fire fa-lg" style="color:#7e0038"></i>
        <i class="fa fa-fire fa-lg" style="color:#7e0038"></i>
        <i class="fa fa-fire fa-lg" style="color:#7e0038"></i>
        <i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
        <i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
  <!--       <p><span data-v-013baba1="" title="" class=""><svg data-v-013baba1="" viewBox="0 0 16 16" width="1em" height="1em" focusable="false" role="img" alt="icon" xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi-bar-chart-fill b-icon bi medium-level"><g data-v-013baba1=""><rect width="4" height="5" x="1" y="10" rx="1"></rect><rect width="4" height="9" x="6" y="6" rx="1"></rect><rect width="4" height="14" x="11" y="1" rx="1"></rect></g></svg> Medium </span></p> -->
      </div>
    </div>
  </div>  
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-clock-o fa-2x" style="color:#7e0038;"></i>
        <h4><b>Reading Time</b></h4>
        <p><i class="fa fa-clock-o fa-lg" style="color:#7e0038;"></i> 30 minutes</p>
        <h4><b>Recipe Type</b></h4>
        <p><i class="fa fa-laptop fa-lg" style="color:#7e0038;"></i> Background Information</p>
        <h4><b>Executable Code</b></h4>
        <p><i class="fa fa-play-circle fa-lg" style="color:#7e0038;"></i> No</p>
      </div>
    </div>
  </div>
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-group fa-2x" style="color:#7e0038;"></i>
        <h4><b>Intended Audience</b></h4>
        <p> <i class="fa fa-user-md fa-lg" style="color:#7e0038;"></i> Principal Investigators </p>
        <p> <i class="fa fa-database fa-lg" style="color:#7e0038;"></i> Data Managers </p>
        <p> <i class="fa fa-wrench fa-lg" style="color:#7e0038;"></i> Data Scientists </p>
<!--         <p> <i class="fa fa-money fa-lg" style="color:#7e0038;"></i> Funders</p> -->
      </div>
    </div>
  </div>
</div>

___


The **FAIR principles**, under `Interoperability` state that: 
> I3. (Meta)data include qualified references to other (meta)data 
> 

## Main Objectives

The main goals of this recipe are:

> - To understand where the need arises for mapping between data identifiers;
> - How to represent equivalences for use by others; and
> - Know what services are available to support data interoperability.

This recipe assumes that you are already familiar with identifiers and the minting of identifiers.

*For more details on identifiers, see the [How to generate globally unique, resolvable and persistent identifiers](https://fairplus.github.io/cookbook-dev/recipes/findability/identifiers.html) recipe.*

___

**ToDo:** Update diagram


<div class="mermaid">
graph TD

  Process2[Identifier Minting]:::bix --> A1(authority decide identity):::box
  Process2 --> Process3
  Process3[URI construction]:::bix --> A2(scoping the authority):::box
  Process3 --> Process4
  Process4[URI resolution]:::bix --> A3(directing requests to the relevant identified entity):::box

  classDef bix font-family:avenir,font-size:14px,fill:#7e0038,stroke:#222,color:#fff,stroke-width:1px
  classDef box font-family:avenir,font-size:14px,fill:#2a9fc9,stroke:#222,color:#fff,stroke-width:1px
</div>

---


## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Interoperability | minimal | repeatable |
| Identifier mapping ||repeatable|

----
<!-- 
## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [Identifier](http://edamontology.org/data_0842) |   |   |
 -->

## Table of Data Standards

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| [IRI](https://tools.ietf.org/html/rfc3987) |   |   |
| [CURIE](https://www.w3.org/TR/2010/NOTE-curie-20101216/) |   |   |
| [URL](https://tools.ietf.org/html/rfc1738) |  |  |
| [HTTP]() |  |  |
| [RDF]() |  |  |
| [CSV]() |  |  |
| [TSV]() |  |  |
| [VoID Linkset]() |  |  |

___

## Identifier Mappings

> :notebook_with_decorative_cover: **"Identifiers are used to tag, identify, find and retrieve entities which are part of a collection or a resource maintained by some organization. "**

To satisfy the Findability criteria F1, organisations must create identifiers for the concepts within their database. This generates locally unique identifiers which can in turn be transformed into globally unique identifiers using namespaces for which the database organisation are the `authority`. 

Databases often contain data that exists in, or is closely related to, the content of other databases. For example, the genome database [Ensembl](http://ensembl.org/) contains data about genes that are related to entries in databases such as HUGO Gene Nomenclature Committee (https://www.genenames.org/) or [NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/); or a database about drugs, e.g. [DrugBank](https://drugbank.com/), often contains details of the chemical substance that forms the drug which are also contained in chemical databases such as [ChEBI](https://www.ebi.ac.uk/chebi/) or [PubChem](https://pubchem.ncbi.nlm.nih.gov/). This results in a large number of unique identifiers notionally for the same concept. This large number of identifiers for the same concept prevents interoperability of the data, since additional knowledge is needed to know which identifiers represent the same concept from different databases. 

The need for each database to mint their own identifier is a result of each taking a different perspective on the concept, e.g. a chemical may be in a different salt form. These subtle differences can affect applications using the data. Ideally, the database owners should not pre-determine for the users of the data what identifiers in another database are equivalent, but they should provide indications together with provenance information as to why they are deemed equivalent (see *Scientific Lenses paper* for more details).

While the minting of identifiers is often done in isolation of other organisations,  there are instances of databases who reuse identifiers from a well known community database. For example, the [Human Protein Atlas](https://www.proteinatlas.org/) database reuses [Ensembl](https://www.ensembl.org/) identifiers for their data records. In these cases there is no need to map between the data instances in the two databases, the data is already connected through the common identifier. However, this means that the Human Protein Atlas must ensure that their definition of the concept is exactly aligned with the Ensembl identifier for **all** application uses.

### Identifier Equivalences

Identifier equivalences can come about in several ways and capture different forms of relationship.



### Exchanging Identifier Mappings

There are several file format for exchanging identifier equivalences. We will discuss the most widely used formats and demonstrate them with a sample of data derived from [ChEMBL](https://www.ebi.ac.uk/chembl/) which provides two database cross-reference equivalences as asserted by ChEMBL.

#### Text File

The simplest way to exchange equivalences is in a simple text file, which could be structured as a tab-separated-value (TSV) file. Such a file usually consists of two columns with lists of identifiers. The interpretation is that they are equivalent. These files tend to carry little to no metadata about the mappings.

The following example shows the mapping equivalences between ChEMBL target components (proteins) and UniProt proteins.

```
CHEMBL_TC_4803    A0ZX81
CHEMBL_TC_2584    A1ZA98 
```

#### Vocabulary of Interlinked Datasets Linkset Files

The Vocabulary of Interlinked Datasets ([VoID](http://www.w3.org/TR/void/)) provides an ontology of terms for describing RDF datasets. These descriptions include basic information about the dataset, e.g. its name, description, license, etc, but also introduces a mechanism for exchanging data instance mappings called `linksets`.

A `linkset` contains the identifier mappings together with either the metadata at the top of the file or a link to a VoID file describing the data source. The Open PHACTS project defined a usage profile for use within the life sciences community [Open PHACTS Dataset Descriptions](http://www.openphacts.org/specs/datadesc/) which was later refined by the W3C Health Care and Life Sciences Community Group ([W3C HCLS Linksets](https://www.w3.org/TR/hcls-dataset/#linksets)).

The following example shows a VoID Linkset in turtle notation with the minimum metadata given in the header.

```xml
@prefix bdb: <http://vocabularies.bridgedb.org/ops#> .
@prefix chembl: <http://rdf.ebi.ac.uk/resource/chembl/> .
@prefix chembl_target_cmpt: <http://rdf.ebi.ac.uk/resource/chembl/targetcomponent/> .
@prefix sio: <https://semanticscience.org/resource/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix uniprot: <http://purl.uniprot.org/uniprot/> .
@prefix void: <http://rdfs.org/ns/void#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:chembl17-uniprot-exactMatch-linkset a void:Linkset ;
    void:subjectsTarget :chembl-rdf ;
    void:objectsTarget <http://purl.uniprot.org/void#UniProtDataset_2015_03> ;
    void:linkPredicate skos:exactMatch ;
    bdb:linksetJustification sio:database-cross-reference
    void:triples "6367"^^xsd:integer .

chembl_target_cmpt:CHEMBL_TC_4803 skos:exactMatch uniprot:A0ZX81 .
chembl_target_cmpt:CHEMBL_TC_2584 skos:exactMatch uniprot:A1ZA98 .
...
```


#### Simple Standard for Sharing Ontology Mappings (SSSOM)

The OBOFoundry Simple Standard for Sharing Ontology Mappings ([SSSOM](https://github.com/OBOFoundry/SSSOM)) is a newly emerging standard for exchanging mapping information with minimal metadata. It consists of a tab-separated-value file (TSV) with each row representing a mapping. The columns in the file have been defined by the community ([latest version](https://github.com/OBOFoundry/SSSOM/blob/master/SSSOM.md)) and provide the mapping together with its provenance. At present, four columns are required (`subject_id`, `predicate_id`, `object_id`, `match_type`) with optional columns to provide more provenance to support the mapping, e.g. licensing information, author information, creation method. The use of CURIEs within the TSV is strongly encouraged.

The following TSV shows our example data as a mapping file using the minimal columns.

```
subject_id    predicate_id    object_id    match_type
chembl:CHEMBL_TC_4803    skos:exactMatch    uniprot:A0ZX81    sio:database-cross-reference
chembl:CHEMBL_TC_2584    skos:exactMatch    uniprot:A1ZA98    sio:database-cross-reference
```

#### Discussion

The VoID Linkset approach for exchanging mappings separates the metadata from the data mappings. This eliminates duplication of metadata. However, as currently defined, the VoID Linksets can only be used for RDF data.

SSSOM is an emerging community standard that is still not finalised. 

The above has shown that the two formats can represent the same information. Both VoID and SSSOM can be used to provide very rich metadata for exchanging data.

### Identifier Mapping services

Identifier mapping services are databases that contain lists of identifiers, often from different databases, that are known to be equivalent. For example, they may contain lists of entries similar to the following example between Ensembl and UniProt.

> | Ensembl         | UniProt |
> | --------------- | ------- |
> | ENSG00000171105 | P06213  |
> | ENSG00000012048 | P38398  |
> | ...             | ...     |

The basic functionality offered by these services is to return a set of equivalent identifiers for a given identifier. That is, you can ask these services for all identifiers that are equivalent to your identifier. The following is an incomplete list of such services.

* [bridgedb.org](https://bridgedb.org/)

    >

* [UniChem](https://www.ebi.ac.uk/unichem/)

* [sameas.org](https://sameas.org/)
  
    > 


* [Identifiers.org](http://identifiers.org/)

    > [Identifiers.org](https://identifiers.org) is a **Resolution Service** provides consistent access to life science data using [`Compact Uniform Resource Identifiers`](https://www.w3.org/TR/2010/NOTE-curie-20101216/), hosted by the EBI provides a resolution service, both as a web form and through the URL pattern. 
    >`Compact Identifiers` consist of an `assigned`, `unique` `prefix` and a `local provider designated` **`accession number`** (prefix:accession).
    > The resolving location of `Compact Identifiers` is determined using information that is stored in the [Identifiers.org Registry](http://identifiers.org/).
    > Datasets can register their *namespace `prefix`* together with their `identifier pattern`. The service can then be used in the same way as the DOI resolution service. So for the UniProt page about BRCA1, we can resolve the CURIE `[uniprot:P38938]` using Identifiers.org. This means that the URL https://identifiers.org/uniprot:P38938 resolves to the UniProt page https://www.uniprot.org/uniprot/P38938.  
    > *For more details, see the [Identifier Resolution Services recipe](./identifier-services/id-resolution.html).*







___

## Conclusion:

**ToDo:** Update the text in this section

> In this recipe, we have given an overview of globally unique and persistent identifier, i.e. FAIR principle F1. We have covered:
>
> - The difference between global and local identifiers;
> - How to convert a local identifier into a global one;
> - Opaque and transparent identifiers
>
> We have given an overview of the different services available for handling identifiers.
> 
> But we can not conclude this section on persistent identifiers without stressing how central they are to the production of Linked Data or Linked Open Data, which rely on 3 W3C standards: URI, RDF and HTTP.
> 
>
> #### What should I read next?
> * [The Pistoia Alliance FAIRtoolkit use cases: Adoption and Impact of an identifier policy at Astra-Zeneca](https://fairtoolkit.pistoiaalliance.org/use-cases/adoption-and-impact-of-an-identifier-policy-astrazeneca/)
> * [Identifier Minting with Minid Client
](./infrastructure/minids.html)
> * [Why resolvable identifiers matter?](./findability/why-identifiers.html)
> * [Identifier Resolution Services](./identifier-services/id-resolution.html)
> * [Identifier Mapping Services](./identifier-services/identifier-mapping.html)


___

## References:

1. Colin Batchelor, Christian Y. A. Brenninkmeijer, Christine Chichester, Mark Davies, Daniela Digles, Ian Dunlop, Chris T. Evelo, Anna Gaulton, Carole Goble, Alasdair J. G. Gray, Paul Groth, Lee Harland, Karen Karapetyan, Antonis Loizou, John P. Overington, Steve Pettifer, Jon Steele, Robert Stevens, Valery Tkachenko, Andra Waagmeester, Antony Williams, Egon L. Willighagen. Scientific Lenses to Support Multiple Views over Linked Chemistry Data. In ISWC 2014: The Semantic Web – ISWC 2014 pp 98-113. https://doi.org/10.1007/978-3-319-11964-9_7


___

## Authors:

| Name | Affiliation  | orcid | CrediT role  | specific contribution |
| :------------- | :------------- | :------------- |:------------- |:------------- |
| Alasdair Gray | Heriot-Watt University / ELIXIR-UK | [0000-0002-5711-4872](https://orcid.org/0000-0002-5711-4872) | Writing - Original Draft | Original format<br />Converting to online format |
| Chris Evelo | Maastricht University | [0000-0002-5301-3142](https://orcid.org/0000-0002-5301-3142) | Writing - Original Draft | Original format |
| Egon Willighagen | Maastricht University | [0000-0001-7542-0286](https://orcid.org/0000-0001-7542-0286) | Writing - Original Draft | Original format |

___

## License:

This page is released under the Creative Commons 4.0 BY license.

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
