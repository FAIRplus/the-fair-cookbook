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

Linked Data require on URL (URL_TO_INSERT_RECORD-ABBREV_1098 https://fairsharing.org/FAIRsharing.9d38e2)  and HTTP protocols to ensure linking. 

## Introduction

CoolURI don't change

## Identifier Resolution - Enabling persistence through indirection


This relates to the following FAIR (URL_TO_INSERT_RECORD-ABBREV_1099 https://fairsharing.org/FAIRsharing.WWI10U)  principle mentioned in the introduction:

> A1. (Meta)data are retrievable by their identifier using a standardised communications protocol.


```{admonition} Tip
:class: tip
 **`URI resolution` is fundamentally about directing requests to the relevant identified entity.** 
```

The standard approach would be resolving a `HTTP GET` request using content negotiation to choose between different representations of the resource.

A PURL (URL_TO_INSERT_RECORD-ABBREV_1100 https://fairsharing.org/FAIRsharing.3e603c)  is a **`persistent URL (URL_TO_INSERT_RECORD-ABBREV_1101 https://fairsharing.org/FAIRsharing.9d38e2) `**, meaning that it provides a **permanent address to access a resource on the web**.

To understand the notion of PURL (URL_TO_INSERT_RECORD-ABBREV_1102 https://fairsharing.org/FAIRsharing.3e603c) , one needs to first get familiar with the notion of `url indirection` (also known as `url redirect` or `url forwarding` ), which refers to the practice of providing a stable, fixed web address/url, but setting it up so that it points to another content, which may be periodically modified.

When a user retrieves a PURL (URL_TO_INSERT_RECORD-ABBREV_1103 https://fairsharing.org/FAIRsharing.3e603c) , they will be **`redirected`** to the current location of the resource.
When an author needs to move a page, they can update the PURL (URL_TO_INSERT_RECORD-ABBREV_1104 https://fairsharing.org/FAIRsharing.3e603c)  to point to the new location.

```{admonition} Tip
:class: tip
The practice of **indirection** comes handy as it ensures invariant url address for resources which are known to change, owing to version changes for instance or owing to change in ownership. 
```

We can see this practice in action with the reliance on purl.org url for identifying OBO Foundry (URL_TO_INSERT_RECORD-NAME_1105 https://fairsharing.org/FAIRsharing.847069)  resources. For instance, the following url [`http://purl.obolibrary.org/obo/stato.owl`](http://purl.obolibrary.org/obo/stato.owl) is a redirect to the latest release of the file, which is [https://raw.githubusercontent.com/ISA-tools/stato/dev/releases/latest_release/stato.owl](https://raw.githubusercontent.com/ISA-tools/stato/dev/releases/latest_release/stato.owl).

PURLs with a `common prefix` are grouped together into **domains**. Each domain has a single maintainer who can add new PURLs to the domain and make changes to existing PURLs within the domain.


FAIR (URL_TO_INSERT_RECORD-ABBREV_1106 https://fairsharing.org/FAIRsharing.WWI10U)  Principle A1 states that:
>(meta)data should be retrievable by its identifier.

When the identifier is not a resolvable URL (URL_TO_INSERT_RECORD-ABBREV_1107 https://fairsharing.org/FAIRsharing.9d38e2) , then `Identifier Resolution Services` are required that know how to map (URL_TO_INSERT_RECORD-NAME_1108 https://fairsharing.org/FAIRsharing.53edcc)  an IRI to a location for the data.



### Introducing CURIEs or Compact URIs

CURIEs (short for compact URIs) are defined by a World Wide Web Consortium Working Group Note [CURIE Syntax 1.0](https://www.w3.org/TR/2010/NOTE-curie-20101216/), and provide a human readable shortening of IRIs.

The CURIE (URL_TO_INSERT_RECORD-ABBREV_1109 https://fairsharing.org/FAIRsharing.af21db)  consists of a **`namespace prefix`** followed by the **`local identifier`**.

There are some widely used and defined CURIEs such as DOIs and ISBN numbers. For example the DOI (URL_TO_INSERT_RECORD-ABBREV_1111 https://fairsharing.org/FAIRsharing.hFLKCn)  `[doi:10.1038/sdata.2016.18]` refers to the FAIR (URL_TO_INSERT_RECORD-ABBREV_1118 https://fairsharing.org/FAIRsharing.WWI10U)  Principles (URL_TO_INSERT_RECORD-NAME_1117 https://fairsharing.org/FAIRsharing.WWI10U)  paper. The Digital Object Identifier (URL_TO_INSERT_RECORD-NAME_1110 https://fairsharing.org/FAIRsharing.hFLKCn)  System web site (https://www.doi.org/) provides a resolution service for DOIs. The service is available as a web form on the site or can be used by appending a DOI (URL_TO_INSERT_RECORD-ABBREV_1112 https://fairsharing.org/FAIRsharing.hFLKCn)  to the website.The client will be redirected to the URL (URL_TO_INSERT_RECORD-ABBREV_1115 https://fairsharing.org/FAIRsharing.9d38e2)  where the resource about the concept is located, e.g. for the FAIR (URL_TO_INSERT_RECORD-ABBREV_1119 https://fairsharing.org/FAIRsharing.WWI10U)  Data Principles paper we can use the URL (URL_TO_INSERT_RECORD-ABBREV_1116 https://fairsharing.org/FAIRsharing.9d38e2)  https://www.doi.org (URL_TO_INSERT_RECORD-HOMEPAGE_1114 https://fairsharing.org/FAIRsharing.hFLKCn) /10.1038/sdata.2016.18 to resolve the paper's DOI (URL_TO_INSERT_RECORD-ABBREV_1113 https://fairsharing.org/FAIRsharing.hFLKCn) . This results in the client being taken to the page at https://www.nature.com/articles/sdata201618.

`Namespaces` can be defined *by convention*, such as the case with `doi`, and registered with services to allow for the resolution of CURIEs (see [Identifier Resolution Services](##identifier-resolution-services) below). These are extensively used to map (URL_TO_INSERT_RECORD-NAME_1120 https://fairsharing.org/FAIRsharing.53edcc)  CURIEs to URLs that can be resolved.

Going back to our *Life Science context*, we can use the following CURIE (URL_TO_INSERT_RECORD-ABBREV_1121 https://fairsharing.org/FAIRsharing.af21db)  `[uniprot:P38398]` to refer to the UniProt record for the protein.

This is very useful for including unambiguous, global identifiers in scientific articles.

[^safe-CURIE]: The CURIES are included in square brackets to make them *safe CURIEs*, meaning that they should not be confused for URIs.


### Identifier Resolution services

* [purl.org](https://archive.org/services/purl/)

  > The PURL (URL_TO_INSERT_RECORD-ABBREV_1122 https://fairsharing.org/FAIRsharing.3e603c)  system is a service of the Internet Archive, which provides an interface to administer domain. For more information about the service, visit https://archive.org/services/purl/help
>

* [w3ids](https://w3id.org/)

  > Permanent Identifiers for the Web. Secure, permanent URLs for your Web application that will stand the test of time.
  > - authority registration service
  > - resolution service
  > - redirection service:
  >
  > Send a request to add a redirect to the public-perma-id@w3.org mailing list. Make sure to include the URL (URL_TO_INSERT_RECORD-ABBREV_1124 https://fairsharing.org/FAIRsharing.9d38e2)  that you want on w3id.org (URL_TO_INSERT_RECORD-NAME_1123 https://fairsharing.org/FAIRsharing.S6BoUk) , the URL (URL_TO_INSERT_RECORD-ABBREV_1125 https://fairsharing.org/FAIRsharing.9d38e2)  that you want to redirect to, and the HTTP code that you want to use when redirecting. An administrator will then create the redirect for you.


* [Identifiers.org](http://identifiers.org/)

  > [Identifiers.org](https://identifiers.org) is a **Resolution Service** provides consistent access to life science data using [`Compact Uniform Resource Identifiers`](https://www.w3.org/TR/2010/NOTE-curie-20101216/), hosted by the EBI provides a resolution service, both as a web form and through the URL (URL_TO_INSERT_RECORD-ABBREV_1126 https://fairsharing.org/FAIRsharing.9d38e2)  pattern {footcite}`Juty2012`.
  >`Compact Identifiers` consist of an `assigned`, `unique` `prefix` and a `local provider designated` **`accession number`** (prefix:accession).
  > The resolving location of `Compact Identifiers` is determined using information that is stored in the [Identifiers.org Registry](http://identifiers.org/).
  > Datasets can register their *namespace `prefix`* together with their `identifier pattern`. The service can then be used in the same way as the DOI (URL_TO_INSERT_RECORD-ABBREV_1127 https://fairsharing.org/FAIRsharing.hFLKCn)  resolution service. So for the UniProt page about BRCA1, we can resolve the CURIE (URL_TO_INSERT_RECORD-ABBREV_1128 https://fairsharing.org/FAIRsharing.af21db)  `[uniprot:P38938]` using Identifiers.org. This means that the URL (URL_TO_INSERT_RECORD-ABBREV_1129 https://fairsharing.org/FAIRsharing.9d38e2)  https://identifiers.org/uniprot:P38938 resolves to the UniProt page https://www.uniprot.org (URL_TO_INSERT_RECORD-HOMEPAGE_1130 https://fairsharing.org/FAIRsharing.s1ne3g) /uniprot/P38938.



* [Name-to-Thing](https://n2t.net/)

  > [Name-to-Thing](https://n2t.net/) (N2T) is a **Resolution Service**, maintained at the California Digital Library (CDL) within the University of California (UC) Office of the President. CDL supports electronic library services for ten UC campuses and affiliated law schools, medical centers, and national laboratories, as well as hundreds of museums, herbaria, botanical gardens, etc. Similar to URL (URL_TO_INSERT_RECORD-ABBREV_1131 https://fairsharing.org/FAIRsharing.9d38e2)  shorteners like bit.ly, N2T serves content **indirectly**.
  > N2T can store more than one "target" (forwarding link) for an identifier, as well as any kind or amount of metadata (descriptive information)
  > N2T.net is also a "meta-resolver". In collaboration with identifiers.org, it recognizes over 600 well-known identifier types and knows where their respective servers are. Failing to find forwarding information for a specific individual identifier, it uses the identifier's type to look for an overall target rule.



* [Bioregistry](https://bioregistry.io/)

  > The [Bioregistry](https://bioregistry.io/) is a **Resolution Service**, developed in a [GitHub (URL_TO_INSERT_RECORD-NAME_1137 https://fairsharing.org/FAIRsharing.c55d5e)  repository](https://github.com/biopragmatics/bioregistry) {footcite}`Hoyt2022`. Like Identifiers.org, it has a registry, but also a registry of registries, and it imports data from Identifiers.org,  Name-to-Thing, and 20+ other registries that extends beyond identifiers for things but also supports, for example, ontologies. As a community effort, new namespace prefixes and their identifier patterns can be [registered via GitHub (URL_TO_INSERT_RECORD-NAME_1138 https://fairsharing.org/FAIRsharing.c55d5e)  issues](https://github.com/biopragmatics/bioregistry/issues/new/choose). Compact identifiers are supported and the URL (URL_TO_INSERT_RECORD-ABBREV_1134 https://fairsharing.org/FAIRsharing.9d38e2)  https://bioregistry.io (URL_TO_INSERT_RECORD-HOMEPAGE_1136 https://fairsharing.org/FAIRsharing.250a8c) /chebi:138488 resolves to the ChEBI (URL_TO_INSERT_RECORD-ABBREV_1132 https://fairsharing.org/FAIRsharing.62qk8w)  page https://www.ebi.ac.uk/chebi (URL_TO_INSERT_RECORD-HOMEPAGE_1133 https://fairsharing.org/FAIRsharing.62qk8w) /searchId.do?chebiId=CHEBI:138488. Bioregistry (URL_TO_INSERT_RECORD-NAME_1135 https://fairsharing.org/FAIRsharing.250a8c)  provides an [API to query the registry](https://bioregistry.io/apidocs/) itself.


### PURL stands for Persistent URL

As defined in https://archive.org/services/purl/help, PURL (URL_TO_INSERT_RECORD-ABBREV_1139 https://fairsharing.org/FAIRsharing.3e603c)  are `persistent URL (URL_TO_INSERT_RECORD-ABBREV_1140 https://fairsharing.org/FAIRsharing.9d38e2) ` and they provide a permanent http address to access a  resource on the web [https://archive.org/services/purl/help].
The PURL (URL_TO_INSERT_RECORD-ABBREV_1141 https://fairsharing.org/FAIRsharing.3e603c)  service is administered by the Internet Archive. Users can request domains from the service under which to administer and mint persistent url.



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
