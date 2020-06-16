# Identifiers

**identifier:** [RX.X_FIXME](RX.X_FIXME)

**version:** v0.1

___

**_Difficulty level:_** easy :triangular_flag_on_post: :white_circle: :white_circle:  :white_circle: :white_circle: 

**_Reading time:_** _FIXME minutes 

**_Intended Audience:_** 

> :heavy_check_mark: Everyone

**_Recipe Type_**: Information

**_Executable code_**: No


[TOC]
## Table of Contents
1. [Main FAIRification Objectives](#Main%20FAIRification%20Objectives)
2. [Graphical Overview of the FAIRification Recipe Objectives](#Graphical%20Overview%20of%20the%20FAIRification%20Recipe%20Objectives)
3. Requirements
4. [FAIRification Objectives, Inputs and Outputs](#FAIRification%20Objectives,%20Inputs%20and%20Outputs)
5. [Capability & Maturity Table](#Capability%20&%20Maturity%20Table)
6. [Table of Data Standards](#Table%20of%20Data%20Standards)
7. [Main Content goes here...](#Main%20Content)
    * [... writing executable code](#Executable%20Code%20in%20Notebook)
    * [... creating workflow figures](#How%20to%20create%20workflow%20figures)
8. [License](#License)

---

## Main Objectives

The main purpose of this recipe is:

> To understand the purpose of a globally unique and persistent identifier and how they can be used to retrieve the associated (meta)data using a standardized communication protocol.

___


## Graphical Overview of the FAIRification Recipe Objectives

Note: use this section to provide a decision tree for the overall process described in the recipe
For more information about the syntax used to generate the diagram, please refer to the [following documentation](https://mermaid-js.github.io/mermaid/#/flowchart)

<!--
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFI7XG4gICAgQShEYXRhIEFjcXVpc2l0aW9uKTo6OmJveCAtLT5CKFJhdyBEYXRhKTo6OmJveFxuICAgIEIgLS0-IEN7RkFJUiBieSBEZXNpZ259XG4gICAgQzo6OmJveC0tPnxZZXN8IEQoU3RhbmRhcmQgQ29tcGxpYW50IERhdGEpOjo6Ym94XG4gICAgQzo6OmJveCAtLT58Tm98IEUoVmVuZG9yIGxvY2tlZCBEYXRhKTo6OmJveFxuICAgIGNsYXNzRGVmIGJveCBmb250LWZhbWlseTphdmVuaXIsZm9udC1zaXplOjE0cHgsZmlsbDojMmE5ZmM5LHN0cm9rZTojMjIyLGNvbG9yOiNmZmYsc3Ryb2tlLXdpZHRoOjFweFxuICAgIGxpbmtTdHlsZSAwLDEsMiwzIHN0cm9rZTojMmE5ZmM5LHN0cm9rZS13aWR0aDoxcHgsY29sb3I6IzJhOWZjOSxmb250LWZhbWlseTphdmVuaXI7IiwibWVybWFpZCI6eyJ0aGVtZSI6bnVsbH0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggTFI7XG4gICAgQShEYXRhIEFjcXVpc2l0aW9uKTo6OmJveCAtLT5CKFJhdyBEYXRhKTo6OmJveFxuICAgIEIgLS0-IEN7RkFJUiBieSBEZXNpZ259XG4gICAgQzo6OmJveC0tPnxZZXN8IEQoU3RhbmRhcmQgQ29tcGxpYW50IERhdGEpOjo6Ym94XG4gICAgQzo6OmJveCAtLT58Tm98IEUoVmVuZG9yIGxvY2tlZCBEYXRhKTo6OmJveFxuICAgIGNsYXNzRGVmIGJveCBmb250LWZhbWlseTphdmVuaXIsZm9udC1zaXplOjE0cHgsZmlsbDojMmE5ZmM5LHN0cm9rZTojMjIyLGNvbG9yOiNmZmYsc3Ryb2tlLXdpZHRoOjFweFxuICAgIGxpbmtTdHlsZSAwLDEsMiwzIHN0cm9rZTojMmE5ZmM5LHN0cm9rZS13aWR0aDoxcHgsY29sb3I6IzJhOWZjOSxmb250LWZhbWlseTphdmVuaXI7IiwibWVybWFpZCI6eyJ0aGVtZSI6bnVsbH0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)
-->


<div class="mermaid">
graph LR;
    A(Data Acquisition):::box -->B(Raw Data):::box
    B --> C{FAIR by Design}
    C:::box-->|Yes| D(Standard Compliant Data):::box
    C:::box -->|No| E(Vendor locked Data):::box
    classDef box font-family:avenir,font-size:14px,fill:#2a9fc9,stroke:#222,color:#fff,stroke-width:1px
    linkStyle 0,1,2,3 stroke:#2a9fc9,stroke-width:1px,color:#2a9fc9,font-family:avenir;
</div>
___


## Requirements

* technical requirements:
   * bash knowledge
   * ...
* recipe dependency:
   * read Recipe 1 first!
* knowledge requirement:
   * be sure to know what OBO is, or read it here: ...link to knowledge...

---

## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Findability | minimal | repeatable |

----

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [Identifier](http://edamontology.org/data_0842) |   |   |


## Table of Data Standards

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| [IRI](https://tools.ietf.org/html/rfc3987) |   |   |
| [CURIE](https://www.w3.org/TR/2010/NOTE-curie-20101216/) |   |   |
| [URL](https://tools.ietf.org/html/rfc1738) |  |  |

___

## Main Content

With regard to identifiers, the FAIR principles state:

> F1. (Meta)data are assigned a globally unique and persistent identifier
>
> A1. (Meta)data are retrievable by their identifier using a standardised communications protocol

In this recipe we give a brief overview of the main ideas around identifiers and provide links to more detailed recipes on how to work with them.

### Properties of Identifiers

Identifiers allow for the unambiguous reference of items in a dataset, e.g. in the context of the UniProt dataset the accession number [P38398](https://www.uniprot.org/uniprot/P38398) allows us to identify the BRCA1 Breast cancer type 1 susceptibility protein. It is the only protein in the dataset with that accession number, i.e. it is *unique*. 

The UniProt accession number is described as an *opaque* identifier. This means that no interpretation about what is identified can be gleaned from the identifier itself. This is in contrast to the Wikipedia page about BRCA1 which uses the  gene name as the identifier ([BRCA1](https://en.wikipedia.org/wiki/BRCA1)). In this case the identifier is *transparent*, since meaning can be inferred from the identifier. Within a scientific context, opaque identifiers are preferred since names and labels can vary over time as our understanding of the concept evolves.

There is an expectation that identifiers will be *persistent*. This pertains to two criteria. First that the identifier will be available going into the future and second that the identifier will not be reused for another concept.

### Global and Local Identifiers

While P38398 is unique within UniProt, i.e. there is only one protein in UniProt that has the accession number P38398, it is not globally unique. For example the same accession number is used as the identifier in several different datasets including Protein Data Bank (http://www.rcsb.org/pdb/protein/P38398), SignaLink (http://signalink.org/protein/P38398), and string-db (http://string-db.org/newstring_cgi/show_network_section.pl?identifier=P38398). Although in these cases they are referring to the same or broadly similar protein. However, the identifier also refers to a 'Satin Chrome 2-way Light Switch' ([Tool Station](https://www.toolstation.com/satin-chrome-white-switch-10a/p38398)). 

### Converting a Local Identifier into a Global Identifier

To make the UniProt accession number globally unique, we need to provide the context in which the accession number is unique. This can either be done by converting it into an International Resource Identifier (IRI – commonly referred to as a URL), or by turning it into a CURIE – a form of compact identifier.

To convert a local identifier into an IRI, we simply need to provide a namespace to the identifier. This should be a namespace for which you have ownership, otherwise you cannot guarantee that the minted IRI will be globally unique; the organization or person who owns the namespace may already, or at some point in the future, use the IRI that you created for some other purpose. In the case of UniProt, they have provided IRIs for each page about a protein as well as separate IRIs for the protein itself. This is achieved by using different namespaces for the different types of resource.

- UniProt P38398 web page IRI: https://www.uniprot.org/uniprot/P38398
- UniProt protein P38398 IRI: http://purl.uniprot.org/uniprot/P38398

CURIEs (short for compact URIs) are defined by a World Wide Web Consortium Working Group Note [CURIE Syntax 1.0](https://www.w3.org/TR/2010/NOTE-curie-20101216/), and provide a human readable shortening of IRIs. The CURIE consists of a namespace prefix followed by the local identifier. There are some widely used and defined CURIEs such as DOIs and ISBN numbers. For example the DOI `[doi:10.1038/sdata.2016.18]` refers to the FAIR Principles paper[^safe-CURIE]. Namespaces can be defined by convention, such as the case with `doi`, and registered with services to allow for the resolution of CURIEs (see [Identifier Resolution Services](#identifier-resolution-services) below). Therefore, we can use the CURIE `[uniprot:P38398]` to refer to the UniProt record for the protein. This is very useful for including unambiguous, global identifiers in scientific articles.

[^safe-CURIE]: The CURIES are included in square brackets to make them *safe CURIEs*, meaning that they should not be confused for URIs.

### Identifier Services

#### Persistent Identifier Services

- [ ] pURL
- [ ] w3id

#### Identifier Resolution Services

FAIR Principle A1 states that (meta)data should be retrievable by its identifier. When the identifier is not a resolvable URL, then Identifier Resolution Services are required that know how to map an IRI to a location for the data. These are extensively used to map CURIEs to URLs that can be resolved. 

The Digital Object Identifier System web site (https://www.doi.org/) provides a resolution service for DOIs. The service is available as a web form on the site or can be used by appending a DOI to the website.The client will be redirected to the URL where the resource about the concept is located, e.g. for the FAIR Data Principles paper we can use the URL https://www.doi.org/10.1038/sdata.2016.18 to resolve the paper's DOI. This results in the client being taken to the page at https://www.nature.com/articles/sdata201618.

Within the life sciences, [Identifiers.org](https://identifiers.org) hosted by the EBI provides a resolution service, both as a web form and through the URL pattern. Datasets can register their namespace prefix together with their identifier pattern. The service can then be used in the same way as the DOI resolution service. So for the UniProt page about BRCA1, we can resolve the CURIE `[uniprot:P38938]` using Identifiers.org. This means that the URL https://identifiers.org/uniprot:P38938 resolves to the UniProt page https://www.uniprot.org/uniprot/P38938.

The Name-to-Thing ([N2T](http://n2t.net/)) service provided by the California Digital Library offers similar functionality and collaborates with Identifiers.org in order to ensure consistency of namespace registrations.

*For more details, see the [Identifier Resolution Services recipe](./identifier-services/id-resolution.html).*

#### Identifier Equivalence/Mapping Services

The consequence of each database minting their own identifiers is that we end up with a large number of identifiers notionally for the same concept. Although in reality there will be subtle differences, e.g. a chemical may be different salt form, which may affect applications using the data. 

Databases often contain lists of equivalent identifiers in other data sources but these can also be extracted into services that provide mappings between identifiers. That is, you can ask these services for all identifiers that are equivalent to your identifier. The following is an incomplete list of such services

- [BridgeDb](https://bridgedb.github.io/)
- [sameAs.org](http://sameas.org)
- [UniChem](https://www.ebi.ac.uk/unichem/)

*For more details, see the [Identifier Mapping Services recipe](./identifier-services/identifier-mapping.html).*

___

## Conclusion:

> In this recipe we have given an overview of globally unique and persistent identifier, i.e. FAIR principle F1. We have covered:
>
> - The difference between global and local identifiers;
> - How to convert a local identifier into a global one;
> - Opaque and transparent identifiers
>
> We have given an overview of the different services available for handling identifiers.
>
> Suggest further reading using the following:
> #### What should I read next?
> * Identifiers for the 21st century: How to design, provision, and reuse persistent identifiers to maximize utility and impact of life science data ([doi:10.1371/journal.pbio.2001414](https://doi.org/10.1371/journal.pbio.2001414))
> * [Persistent Identifier Services](TODO)
> * [Identifier Resolution Services](TODO)
> * [Identifier Mapping/Equivalence Services](TODO)

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