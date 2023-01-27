(fcb-infra-idres)=
# Identifier resolution services

````{panels_fairplus}
:identifier_text: FCB046
:identifier_link: 'https://w3id.org/faircookbook/FCB046'
:difficulty_level: 2
:recipe_type: background_information
:reading_time_minutes: 15
:intended_audience: principal_investigator, data_manager, data_scientist, funder 
:maturity_level: 1
:maturity_indicator: 6
:has_executable_code: nope
:recipe_name: Introducing identifier resolution services
```` 

## Main Objective

Linked Data require on URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630) and HTTP protocols to ensure linking. 

## Introduction

CoolURI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986) don't change

## Identifier Resolution - Enabling persistence through indirection


This relates to the following FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) principle mentioned in the introduction:

> A1. (Meta)data are retrievable by their identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) using a standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)ised communications protocol.


```{admonition} Tip
:class: tip
 **`URI resolution` is fundamentally about directing requests to the relevant identified entity.** 
```

The standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) approach would be resolving a `HTTP GET` request using content negotiation to choose between different representations of the resource.

A PURL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)(URL_TO_INSERT_RECORD http://purlz.org) is a **`persistent URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)`**, meaning that it provides a **permanent address to access a resource on the web**.

To understand the notion of PURL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)(URL_TO_INSERT_RECORD http://purlz.org), one needs to first get fam(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#fam)iliar with the notion of `url indirection` (also known as `url redirect` or `url forwarding` ), which refers to the practice of providing a stable, fixed web address/url, but setting it up so that it points to another content, which may be periodically modified.

When a user retrieves a PURL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)(URL_TO_INSERT_RECORD http://purlz.org), they will be **`redirected`** to the current location of the resource.
When an author needs to move a page, they can update the PURL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)(URL_TO_INSERT_RECORD http://purlz.org) to point to the new location.

```{admonition} Tip
:class: tip
The practice of **indirection** comes handy as it ensures invariant url address for resources which are known to change, owing to version changes for instance or owing to change in ownership. 
```

We can see this practice in action with the reliance on purl.org url for identifying OBO(URL_TO_INSERT_RECORD http://www.obofoundry.org/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059) Foundry(URL_TO_INSERT_RECORD http://www.obofoundry.org/) resources. For instance, the following url [`http://purl.obolibrary.org/obo/stato.owl`](http://purl.obolibrary.org/obo/stato.owl) is a redirect to the latest release of the file, which is [https://raw.githubusercontent.com/ISA-tools/stato/dev/releases/latest_release/stato.owl](https://raw.githubusercontent.com/ISA-tools/stato/dev/releases/latest_release/stato.owl).

PURL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)(URL_TO_INSERT_RECORD http://purlz.org)s with a `common prefix` are grouped(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) together into **domains**. Each domain has a single maintainer who can add new PURL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)(URL_TO_INSERT_RECORD http://purlz.org)s to the domain and make changes to existing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) PURL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)(URL_TO_INSERT_RECORD http://purlz.org)s within the domain.


FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) Principle A1 states that:
>(meta)data should be retrievable by its identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema).

When the identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) is not a resolvable URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630), then `Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) Resolution Services` are required that know how to map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map) an IRI to a location for the data.



### Introducing CURIEs or Compact URIs

CURI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)E(URL_TO_INSERT_RECORD https://www.w3.org/TR/2010/NOTE-curie-20101216/)s (short for compact URI(URL_TO_INSERT_RECORD https://www.w3.org/TR/2010/NOTE-curie-20101216/)(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)s) are defined by a World Wide Web Consortium Working Group Note [CURI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)E(URL_TO_INSERT_RECORD https://www.w3.org/TR/2010/NOTE-curie-20101216/) Syntax 1.0](https://www.w3.org/TR/2010/NOTE-curie-20101216(URL_TO_INSERT_RECORD https://www.w3.org/TR/2010/NOTE-curie-20101216/)/), and provide a human readable shortening of IRIs.

The CURI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)E(URL_TO_INSERT_RECORD https://www.w3.org/TR/2010/NOTE-curie-20101216/) consists of a **`namespace prefix`** followed by the **`local identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)`**.

There are some widely used and defined CURI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)E(URL_TO_INSERT_RECORD https://www.w3.org/TR/2010/NOTE-curie-20101216/)s such as DOI(URL_TO_INSERT_RECORD https://www.doi.org)s and ISBN numbers. For example the DOI(URL_TO_INSERT_RECORD https://www.doi.org) `[doi:10.1038/sdata.2016.18]` refers to the FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) Principles(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) paper. The Digital Object Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)(URL_TO_INSERT_RECORD https://www.doi.org) System web site (https://www.doi.org(URL_TO_INSERT_RECORD https://www.doi.org)/) provides a resolution service for DOI(URL_TO_INSERT_RECORD https://www.doi.org)s. The service is available as a web form on the site or can be used by appending a DOI(URL_TO_INSERT_RECORD https://www.doi.org) to the website.The client will be redirected to the URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630) where the resource about the concept is located, e.g. for the FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) Data Principles paper we can use the URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630) https://www.doi.org(URL_TO_INSERT_RECORD https://www.doi.org)/10.1038/sdata.2016.18 to resolve the paper's DOI(URL_TO_INSERT_RECORD https://www.doi.org). This results in the client being taken to the page at https://www.nature.com/articles/sdata201618.

`Namespaces` can be defined *by convention*, such as the case with `doi`, and registered with services to allow for the resolution of CURI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)E(URL_TO_INSERT_RECORD https://www.w3.org/TR/2010/NOTE-curie-20101216/)s (see [Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) Resolution Services](##identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)-resolution-services) below). These are extensively used to map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map) CURI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)E(URL_TO_INSERT_RECORD https://www.w3.org/TR/2010/NOTE-curie-20101216/)s to URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)s that can be resolved.

Going back to our *Life Science context*, we can use the following CURI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)E(URL_TO_INSERT_RECORD https://www.w3.org/TR/2010/NOTE-curie-20101216/) `[uniprot:P38398]` to refer to the UniProt record for the protein.

This is very useful for including unambiguous, global identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s in scientific articles.

[^safe-CURI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)E(URL_TO_INSERT_RECORD https://www.w3.org/TR/2010/NOTE-curie-20101216/)]: The CURI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)E(URL_TO_INSERT_RECORD https://www.w3.org/TR/2010/NOTE-curie-20101216/)S are included in square brackets to make them *safe CURI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)E(URL_TO_INSERT_RECORD https://www.w3.org/TR/2010/NOTE-curie-20101216/)s*, meaning that they should not be confused for URI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)s.


### Identifier Resolution services

* [purl.org](https://archive.org/services/purl/)

  > The PURL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)(URL_TO_INSERT_RECORD http://purlz.org) system is a service of the Internet Arch(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ive, which provides an interface to administer domain. For more informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion about the service, visit https://archive.org/services/purl/help
>

* [w3id(URL_TO_INSERT_RECORD https://w3id.org/)s](https://w3id.org(URL_TO_INSERT_RECORD https://w3id.org/)/)

  > Permanent Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s for the Web. Secure, permanent URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)s for your Web application that will stand the test of time.
  > - authority registration service
  > - resolution service
  > - redirection service:
  >
  > Send a request to add a redirect to the public-perma-id@w3.org mailing list. Make sure to include the URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630) that you want on w3id(URL_TO_INSERT_RECORD https://w3id.org/).org(URL_TO_INSERT_RECORD https://w3id.org/), the URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630) that you want to redirect to, and the HTTP code that you want to use when redirecting. An administrator will then create the redirect for you.


* [Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s.org](http://identifiers.org/)

  > [Identifiers.org](https://identifiers.org) is a **Resolution Service** provides consistent access to life science data using [`Compact Uniform Resource Identifier(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)s`](https://www.w3.org/TR/2010/NOTE-curie-20101216(URL_TO_INSERT_RECORD https://www.w3.org/TR/2010/NOTE-curie-20101216/)/), hosted by the EBI provides a resolution service, both as a web form and through the URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630) pattern {footcite}`Juty2012`.
  >`Compact Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s` consist of an `assigned`, `unique` `prefix` and a `local provider designated` **`accession number`** (prefix:accession).
  > The resolving location of `Compact Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s` is determined using informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion that is stored in the [Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s.org Registry](http://identifiers.org/).
  > Datasets can register their *namespace `prefix`* together with their `identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) pattern`. The service can then be used in the same way as the DOI(URL_TO_INSERT_RECORD https://www.doi.org) resolution service. So for the UniProt page about BRCA1, we can resolve the CURI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)E(URL_TO_INSERT_RECORD https://www.w3.org/TR/2010/NOTE-curie-20101216/) `[uniprot:P38938]` using Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s.org. This means that the URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630) https://identifiers.org/uniprot:P38938 resolves to the UniProt page https://www.uniprot.org(URL_TO_INSERT_RECORD https://www.uniprot.org)/uniprot/P38938.



* [Name-to-Thing](https://n2t.net/)

  > [Name-to-Thing](https://n2t.net/) (N2T) is a **Resolution Service**, maintained at the California Digital Library (CDL) within the University of California (UC) Office of the President. CDL supports electronic library services for ten UC campuses and affiliated law schools, medical centers, and national laboratories, as well as hundreds of museums, herbaria, botanical gardens, etc. Similar to URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630) shorteners like bit.ly, N2T serves content **indirectly**.
  > N2T can store more than one "target" (forwarding link) for an identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema), as well as any kind or amount of metadata (descriptive informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion)
  > N2T.net is also a "meta-resolver". In collaboration with identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s.org, it recognizes over 600 well-known identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) types and knows where their respective servers are. Failing to find forwarding informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion for a specific individual identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema), it uses the identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)'s type to look for an overall target rule.



* [Bioregistry(URL_TO_INSERT_RECORD https://bioregistry.io)](https://bioregistry.io(URL_TO_INSERT_RECORD https://bioregistry.io)/)

  > The [Bioregistry](https://bioregistry.io(URL_TO_INSERT_RECORD https://bioregistry.io)/) is a **Resolution Service**, developed(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) in a [GitHub(URL_TO_INSERT_RECORD https://github.com/)(URL_TO_INSERT_RECORD https://github.com/) repository](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/biopragmatics/bioregistry) {footcite}`Hoyt2022`. Like Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s.org, it has a registry, but also a registry of registries, and it imports data from Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s.org,  Name-to-Thing, and 20+ other registries that extends beyond identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s for things but also supports, for example, ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact). As a community effort, new namespace prefixes and their identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) patterns can be [registered via GitHub(URL_TO_INSERT_RECORD https://github.com/)(URL_TO_INSERT_RECORD https://github.com/) issues](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/biopragmatics/bioregistry/issues/new/choose). Compact identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s are supported and the URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630) https://bioregistry.io(URL_TO_INSERT_RECORD https://bioregistry.io)/chebi:138488 resolves to the ChEBI(URL_TO_INSERT_RECORD http://www.ebi.ac.uk/chebi/) page https://www.ebi.ac.uk/chebi(URL_TO_INSERT_RECORD http://www.ebi.ac.uk/chebi/)/searchId.do?chebiId=CHEBI:138488. Bioregistry(URL_TO_INSERT_RECORD https://bioregistry.io) provides an [API to query the registry](https://bioregistry.io(URL_TO_INSERT_RECORD https://bioregistry.io)/apidocs/) itself.


### PURL stands for Persistent URL

As defined in https://archive.org/services/purl/help, PURL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)(URL_TO_INSERT_RECORD http://purlz.org) are `persistent URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)` and they provide a permanent http address to access a  resource on the web [https://archive.org/services/purl/help].
The PURL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)(URL_TO_INSERT_RECORD http://purlz.org) service is administered by the Internet Arch(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ive. Users can request domains from the service under which to administer and mint persistent url.



## Conclusion



## References
````{dropdown} **References**
```{footbibliography}
```
````


## Authors

````{authors_fairplus}
Philippe: Writing - Original Draft
````

## License

````{license_fairplus}
CC-BY-4.0
````
