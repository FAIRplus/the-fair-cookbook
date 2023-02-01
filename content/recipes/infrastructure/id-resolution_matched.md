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

Linked Data require on URL (URL_TO_INSERT_RECORD_3818 https://fairsharing.org/FAIRsharing.9d38e2)  and HTTP protocols to ensure linking. 

## Introduction

CoolURI (URL_TO_INSERT_RECORD_3819 https://fairsharing.org/FAIRsharing.d261e1)  don't change

## Identifier Resolution - Enabling persistence through indirection


This relates to the following FAIR (URL_TO_INSERT_RECORD_3820 https://fairsharing.org/FAIRsharing.WWI10U)  principle mentioned in the introduction:

> A1. (Meta)data are retrievable by their identifier (URL_TO_INSERT_TERM_3822 https://fairsharing.org/search?recordType=identifier_schema)  using a standard (URL_TO_INSERT_TERM_3821 https://fairsharing.org/search?fairsharingRegistry=Standard) ised communications protocol.


```{admonition} Tip
:class: tip
 **`URI resolution` is fundamentally about directing requests to the relevant identified entity.** 
```

The standard (URL_TO_INSERT_TERM_3823 https://fairsharing.org/search?fairsharingRegistry=Standard)  approach would be resolving a `HTTP GET` request using content negotiation to choose between different representations of the resource.

A PURL (URL_TO_INSERT_RECORD_3824 https://fairsharing.org/FAIRsharing.3e603c)  (URL_TO_INSERT_RECORD_3825 https://fairsharing.org/FAIRsharing.9d38e2)  is a **`persistent URL (URL_TO_INSERT_RECORD_3826 https://fairsharing.org/FAIRsharing.9d38e2) `**, meaning that it provides a **permanent address to access a resource on the web**.

To understand the notion of PURL (URL_TO_INSERT_RECORD_3827 https://fairsharing.org/FAIRsharing.3e603c)  (URL_TO_INSERT_RECORD_3828 https://fairsharing.org/FAIRsharing.9d38e2) , one needs to first get fam (URL_TO_INSERT_RECORD_3829 https://fairsharing.org/FAIRsharing.d0886a) iliar with the notion of `url indirection` (also known as `url redirect` or `url forwarding` ), which refers to the practice of providing a stable, fixed web address/url, but setting it up so that it points to another content, which may be periodically modified.

When a user retrieves a PURL (URL_TO_INSERT_RECORD_3830 https://fairsharing.org/FAIRsharing.3e603c)  (URL_TO_INSERT_RECORD_3831 https://fairsharing.org/FAIRsharing.9d38e2) , they will be **`redirected`** to the current location of the resource.
When an author needs to move a page, they can update the PURL (URL_TO_INSERT_RECORD_3832 https://fairsharing.org/FAIRsharing.3e603c)  (URL_TO_INSERT_RECORD_3833 https://fairsharing.org/FAIRsharing.9d38e2)  to point to the new location.

```{admonition} Tip
:class: tip
The practice of **indirection** comes handy as it ensures invariant url address for resources which are known to change, owing to version changes for instance or owing to change in ownership. 
```

We can see this practice in action with the reliance on purl.org url for identifying OBO (URL_TO_INSERT_RECORD_3835 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_3836 https://fairsharing.org/FAIRsharing.cbz72b)  Foundry (URL_TO_INSERT_RECORD_3834 https://fairsharing.org/FAIRsharing.847069)  resources. For instance, the following url [`http://purl.obolibrary.org/obo/stato.owl`](http://purl.obolibrary.org/obo/stato.owl) is a redirect to the latest release of the file, which is [https://raw.githubusercontent.com/ISA-tools/stato/dev/releases/latest_release/stato.owl](https://raw.githubusercontent.com/ISA-tools/stato/dev/releases/latest_release/stato.owl).

PURL (URL_TO_INSERT_RECORD_3837 https://fairsharing.org/FAIRsharing.3e603c)  (URL_TO_INSERT_RECORD_3840 https://fairsharing.org/FAIRsharing.9d38e2) s with a `common prefix` are grouped (URL_TO_INSERT_RECORD_3844 https://fairsharing.org/FAIRsharing.31385c)  together into **domains**. Each domain has a single maintainer who can add new PURL (URL_TO_INSERT_RECORD_3838 https://fairsharing.org/FAIRsharing.3e603c)  (URL_TO_INSERT_RECORD_3841 https://fairsharing.org/FAIRsharing.9d38e2) s to the domain and make changes to existing (URL_TO_INSERT_RECORD_3843 https://fairsharing.org/FAIRsharing.q7bkqr)  PURL (URL_TO_INSERT_RECORD_3839 https://fairsharing.org/FAIRsharing.3e603c)  (URL_TO_INSERT_RECORD_3842 https://fairsharing.org/FAIRsharing.9d38e2) s within the domain.


FAIR (URL_TO_INSERT_RECORD_3845 https://fairsharing.org/FAIRsharing.WWI10U)  Principle A1 states that:
>(meta)data should be retrievable by its identifier (URL_TO_INSERT_TERM_3846 https://fairsharing.org/search?recordType=identifier_schema) .

When the identifier (URL_TO_INSERT_TERM_3847 https://fairsharing.org/search?recordType=identifier_schema)  is not a resolvable URL (URL_TO_INSERT_RECORD_3849 https://fairsharing.org/FAIRsharing.9d38e2) , then `Identifier (URL_TO_INSERT_TERM_3848 https://fairsharing.org/search?recordType=identifier_schema)  Resolution Services` are required that know how to map (URL_TO_INSERT_RECORD_3850 https://fairsharing.org/FAIRsharing.53edcc)  an IRI to a location for the data.



### Introducing CURIEs or Compact URIs

CURI (URL_TO_INSERT_RECORD_3851 https://fairsharing.org/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD_3855 https://fairsharing.org/FAIRsharing.af21db) s (short for compact URI (URL_TO_INSERT_RECORD_3852 https://fairsharing.org/FAIRsharing.d261e1)  (URL_TO_INSERT_RECORD_3854 https://fairsharing.org/FAIRsharing.af21db) s) are defined by a World Wide Web Consortium Working Group Note [CURI (URL_TO_INSERT_RECORD_3853 https://fairsharing.org/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD_3856 https://fairsharing.org/FAIRsharing.af21db)  Syntax 1.0](https://www.w3.org/TR/2010/NOTE-curie-20101216 (URL_TO_INSERT_RECORD_3857 https://fairsharing.org/FAIRsharing.af21db) /), and provide a human readable shortening of IRIs.

The CURI (URL_TO_INSERT_RECORD_3859 https://fairsharing.org/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD_3860 https://fairsharing.org/FAIRsharing.af21db)  consists of a **`namespace prefix`** followed by the **`local identifier (URL_TO_INSERT_TERM_3858 https://fairsharing.org/search?recordType=identifier_schema) `**.

There are some widely used and defined CURI (URL_TO_INSERT_RECORD_3862 https://fairsharing.org/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD_3871 https://fairsharing.org/FAIRsharing.af21db) s such as DOI (URL_TO_INSERT_RECORD_3864 https://fairsharing.org/FAIRsharing.hFLKCn) s and ISBN numbers. For example the DOI (URL_TO_INSERT_RECORD_3865 https://fairsharing.org/FAIRsharing.hFLKCn)  `[doi:10.1038/sdata.2016.18]` refers to the FAIR (URL_TO_INSERT_RECORD_3875 https://fairsharing.org/FAIRsharing.WWI10U)  Principles (URL_TO_INSERT_RECORD_3874 https://fairsharing.org/FAIRsharing.WWI10U)  paper. The Digital Object Identifier (URL_TO_INSERT_TERM_3861 https://fairsharing.org/search?recordType=identifier_schema)  (URL_TO_INSERT_RECORD_3863 https://fairsharing.org/FAIRsharing.hFLKCn)  System web site (https://www.doi.org (URL_TO_INSERT_RECORD_3869 https://fairsharing.org/FAIRsharing.hFLKCn) /) provides a resolution service for DOI (URL_TO_INSERT_RECORD_3866 https://fairsharing.org/FAIRsharing.hFLKCn) s. The service is available as a web form on the site or can be used by appending a DOI (URL_TO_INSERT_RECORD_3867 https://fairsharing.org/FAIRsharing.hFLKCn)  to the website.The client will be redirected to the URL (URL_TO_INSERT_RECORD_3872 https://fairsharing.org/FAIRsharing.9d38e2)  where the resource about the concept is located, e.g. for the FAIR (URL_TO_INSERT_RECORD_3876 https://fairsharing.org/FAIRsharing.WWI10U)  Data Principles paper we can use the URL (URL_TO_INSERT_RECORD_3873 https://fairsharing.org/FAIRsharing.9d38e2)  https://www.doi.org (URL_TO_INSERT_RECORD_3870 https://fairsharing.org/FAIRsharing.hFLKCn) /10.1038/sdata.2016.18 to resolve the paper's DOI (URL_TO_INSERT_RECORD_3868 https://fairsharing.org/FAIRsharing.hFLKCn) . This results in the client being taken to the page at https://www.nature.com/articles/sdata201618.

`Namespaces` can be defined *by convention*, such as the case with `doi`, and registered with services to allow for the resolution of CURI (URL_TO_INSERT_RECORD_3879 https://fairsharing.org/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD_3881 https://fairsharing.org/FAIRsharing.af21db) s (see [Identifier (URL_TO_INSERT_TERM_3877 https://fairsharing.org/search?recordType=identifier_schema)  Resolution Services](##identifier (URL_TO_INSERT_TERM_3878 https://fairsharing.org/search?recordType=identifier_schema) -resolution-services) below). These are extensively used to map (URL_TO_INSERT_RECORD_3884 https://fairsharing.org/FAIRsharing.53edcc)  CURI (URL_TO_INSERT_RECORD_3880 https://fairsharing.org/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD_3882 https://fairsharing.org/FAIRsharing.af21db) s to URL (URL_TO_INSERT_RECORD_3883 https://fairsharing.org/FAIRsharing.9d38e2) s that can be resolved.

Going back to our *Life Science context*, we can use the following CURI (URL_TO_INSERT_RECORD_3885 https://fairsharing.org/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD_3886 https://fairsharing.org/FAIRsharing.af21db)  `[uniprot:P38398]` to refer to the UniProt record for the protein.

This is very useful for including unambiguous, global identifier (URL_TO_INSERT_TERM_3887 https://fairsharing.org/search?recordType=identifier_schema) s in scientific articles.

[^safe-CURI (URL_TO_INSERT_RECORD_3888 https://fairsharing.org/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD_3892 https://fairsharing.org/FAIRsharing.af21db) ]: The CURI (URL_TO_INSERT_RECORD_3889 https://fairsharing.org/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD_3893 https://fairsharing.org/FAIRsharing.af21db) S are included in square brackets to make them *safe CURI (URL_TO_INSERT_RECORD_3890 https://fairsharing.org/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD_3894 https://fairsharing.org/FAIRsharing.af21db) s*, meaning that they should not be confused for URI (URL_TO_INSERT_RECORD_3891 https://fairsharing.org/FAIRsharing.d261e1) s.


### Identifier Resolution services

* [purl.org](https://archive.org/services/purl/)

  > The PURL (URL_TO_INSERT_RECORD_3896 https://fairsharing.org/FAIRsharing.3e603c)  (URL_TO_INSERT_RECORD_3897 https://fairsharing.org/FAIRsharing.9d38e2)  system is a service of the Internet Arch (URL_TO_INSERT_RECORD_3898 https://fairsharing.org/FAIRsharing.52b22c) ive, which provides an interface to administer domain. For more informat (URL_TO_INSERT_TERM_3895 https://fairsharing.org/search?recordType=model_and_format) ion about the service, visit https://archive.org/services/purl/help
>

* [w3id (URL_TO_INSERT_RECORD_3899 https://fairsharing.org/FAIRsharing.S6BoUk) s](https://w3id.org (URL_TO_INSERT_RECORD_3900 https://fairsharing.org/FAIRsharing.S6BoUk) /)

  > Permanent Identifier (URL_TO_INSERT_TERM_3901 https://fairsharing.org/search?recordType=identifier_schema) s for the Web. Secure, permanent URL (URL_TO_INSERT_RECORD_3902 https://fairsharing.org/FAIRsharing.9d38e2) s for your Web application that will stand the test of time.
  > - authority registration service
  > - resolution service
  > - redirection service:
  >
  > Send a request to add a redirect to the public-perma-id@w3.org mailing list. Make sure to include the URL (URL_TO_INSERT_RECORD_3905 https://fairsharing.org/FAIRsharing.9d38e2)  that you want on w3id (URL_TO_INSERT_RECORD_3904 https://fairsharing.org/FAIRsharing.S6BoUk) .org (URL_TO_INSERT_RECORD_3903 https://fairsharing.org/FAIRsharing.S6BoUk) , the URL (URL_TO_INSERT_RECORD_3906 https://fairsharing.org/FAIRsharing.9d38e2)  that you want to redirect to, and the HTTP code that you want to use when redirecting. An administrator will then create the redirect for you.


* [Identifier (URL_TO_INSERT_TERM_3907 https://fairsharing.org/search?recordType=identifier_schema) s.org](http://identifiers.org/)

  > [Identifiers.org](https://identifiers.org) is a **Resolution Service** provides consistent access to life science data using [`Compact Uniform Resource Identifier (URL_TO_INSERT_RECORD_3908 https://fairsharing.org/FAIRsharing.d261e1) s`](https://www.w3.org/TR/2010/NOTE-curie-20101216 (URL_TO_INSERT_RECORD_3909 https://fairsharing.org/FAIRsharing.af21db) /), hosted by the EBI provides a resolution service, both as a web form and through the URL (URL_TO_INSERT_RECORD_3910 https://fairsharing.org/FAIRsharing.9d38e2)  pattern {footcite}`Juty2012`.
  >`Compact Identifier (URL_TO_INSERT_TERM_3911 https://fairsharing.org/search?recordType=identifier_schema) s` consist of an `assigned`, `unique` `prefix` and a `local provider designated` **`accession number`** (prefix:accession).
  > The resolving location of `Compact Identifier (URL_TO_INSERT_TERM_3913 https://fairsharing.org/search?recordType=identifier_schema) s` is determined using informat (URL_TO_INSERT_TERM_3912 https://fairsharing.org/search?recordType=model_and_format) ion that is stored in the [Identifier (URL_TO_INSERT_TERM_3914 https://fairsharing.org/search?recordType=identifier_schema) s.org Registry](http://identifiers.org/).
  > Datasets can register their *namespace `prefix`* together with their `identifier (URL_TO_INSERT_TERM_3915 https://fairsharing.org/search?recordType=identifier_schema)  pattern`. The service can then be used in the same way as the DOI (URL_TO_INSERT_RECORD_3918 https://fairsharing.org/FAIRsharing.hFLKCn)  resolution service. So for the UniProt page about BRCA1, we can resolve the CURI (URL_TO_INSERT_RECORD_3917 https://fairsharing.org/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD_3919 https://fairsharing.org/FAIRsharing.af21db)  `[uniprot:P38938]` using Identifier (URL_TO_INSERT_TERM_3916 https://fairsharing.org/search?recordType=identifier_schema) s.org. This means that the URL (URL_TO_INSERT_RECORD_3920 https://fairsharing.org/FAIRsharing.9d38e2)  https://identifiers.org/uniprot:P38938 resolves to the UniProt page https://www.uniprot.org (URL_TO_INSERT_RECORD_3921 https://fairsharing.org/FAIRsharing.s1ne3g) /uniprot/P38938.



* [Name-to-Thing](https://n2t.net/)

  > [Name-to-Thing](https://n2t.net/) (N2T) is a **Resolution Service**, maintained at the California Digital Library (CDL) within the University of California (UC) Office of the President. CDL supports electronic library services for ten UC campuses and affiliated law schools, medical centers, and national laboratories, as well as hundreds of museums, herbaria, botanical gardens, etc. Similar to URL (URL_TO_INSERT_RECORD_3922 https://fairsharing.org/FAIRsharing.9d38e2)  shorteners like bit.ly, N2T serves content **indirectly**.
  > N2T can store more than one "target" (forwarding link) for an identifier (URL_TO_INSERT_TERM_3924 https://fairsharing.org/search?recordType=identifier_schema) , as well as any kind or amount of metadata (descriptive informat (URL_TO_INSERT_TERM_3923 https://fairsharing.org/search?recordType=model_and_format) ion)
  > N2T.net is also a "meta-resolver". In collaboration with identifier (URL_TO_INSERT_TERM_3926 https://fairsharing.org/search?recordType=identifier_schema) s.org, it recognizes over 600 well-known identifier (URL_TO_INSERT_TERM_3927 https://fairsharing.org/search?recordType=identifier_schema)  types and knows where their respective servers are. Failing to find forwarding informat (URL_TO_INSERT_TERM_3925 https://fairsharing.org/search?recordType=model_and_format) ion for a specific individual identifier (URL_TO_INSERT_TERM_3928 https://fairsharing.org/search?recordType=identifier_schema) , it uses the identifier (URL_TO_INSERT_TERM_3929 https://fairsharing.org/search?recordType=identifier_schema) 's type to look for an overall target rule.



* [Bioregistry (URL_TO_INSERT_RECORD_3930 https://fairsharing.org/FAIRsharing.250a8c) ](https://bioregistry.io (URL_TO_INSERT_RECORD_3931 https://fairsharing.org/FAIRsharing.250a8c) /)

  > The [Bioregistry](https://bioregistry.io (URL_TO_INSERT_RECORD_3942 https://fairsharing.org/FAIRsharing.250a8c) /) is a **Resolution Service**, developed (URL_TO_INSERT_RECORD_3951 https://fairsharing.org/FAIRsharing.31385c)  in a [GitHub (URL_TO_INSERT_RECORD_3945 https://fairsharing.org/FAIRsharing.c55d5e)  (URL_TO_INSERT_RECORD_3947 https://fairsharing.org/FAIRsharing.c55d5e)  repository](https://github.com (URL_TO_INSERT_RECORD_3949 https://fairsharing.org/FAIRsharing.c55d5e) /biopragmatics/bioregistry) {footcite}`Hoyt2022`. Like Identifier (URL_TO_INSERT_TERM_3933 https://fairsharing.org/search?recordType=identifier_schema) s.org, it has a registry, but also a registry of registries, and it imports data from Identifier (URL_TO_INSERT_TERM_3934 https://fairsharing.org/search?recordType=identifier_schema) s.org,  Name-to-Thing, and 20+ other registries that extends beyond identifier (URL_TO_INSERT_TERM_3935 https://fairsharing.org/search?recordType=identifier_schema) s for things but also supports, for example, ontologies (URL_TO_INSERT_TERM_3932 https://fairsharing.org/search?recordType=terminology_artefact) . As a community effort, new namespace prefixes and their identifier (URL_TO_INSERT_TERM_3936 https://fairsharing.org/search?recordType=identifier_schema)  patterns can be [registered via GitHub (URL_TO_INSERT_RECORD_3946 https://fairsharing.org/FAIRsharing.c55d5e)  (URL_TO_INSERT_RECORD_3948 https://fairsharing.org/FAIRsharing.c55d5e)  issues](https://github.com (URL_TO_INSERT_RECORD_3950 https://fairsharing.org/FAIRsharing.c55d5e) /biopragmatics/bioregistry/issues/new/choose). Compact identifier (URL_TO_INSERT_TERM_3937 https://fairsharing.org/search?recordType=identifier_schema) s are supported and the URL (URL_TO_INSERT_RECORD_3940 https://fairsharing.org/FAIRsharing.9d38e2)  https://bioregistry.io (URL_TO_INSERT_RECORD_3943 https://fairsharing.org/FAIRsharing.250a8c) /chebi:138488 resolves to the ChEBI (URL_TO_INSERT_RECORD_3938 https://fairsharing.org/FAIRsharing.62qk8w)  page https://www.ebi.ac.uk/chebi (URL_TO_INSERT_RECORD_3939 https://fairsharing.org/FAIRsharing.62qk8w) /searchId.do?chebiId=CHEBI:138488. Bioregistry (URL_TO_INSERT_RECORD_3941 https://fairsharing.org/FAIRsharing.250a8c)  provides an [API to query the registry](https://bioregistry.io (URL_TO_INSERT_RECORD_3944 https://fairsharing.org/FAIRsharing.250a8c) /apidocs/) itself.


### PURL stands for Persistent URL

As defined in https://archive.org/services/purl/help, PURL (URL_TO_INSERT_RECORD_3952 https://fairsharing.org/FAIRsharing.3e603c)  (URL_TO_INSERT_RECORD_3953 https://fairsharing.org/FAIRsharing.9d38e2)  are `persistent URL (URL_TO_INSERT_RECORD_3954 https://fairsharing.org/FAIRsharing.9d38e2) ` and they provide a permanent http address to access a  resource on the web [https://archive.org/services/purl/help].
The PURL (URL_TO_INSERT_RECORD_3955 https://fairsharing.org/FAIRsharing.3e603c)  (URL_TO_INSERT_RECORD_3956 https://fairsharing.org/FAIRsharing.9d38e2)  service is administered by the Internet Arch (URL_TO_INSERT_RECORD_3957 https://fairsharing.org/FAIRsharing.52b22c) ive. Users can request domains from the service under which to administer and mint persistent url.



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
