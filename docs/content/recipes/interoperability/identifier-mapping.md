---
dummy: dummy
---

# Why mappings between identifiers are necessary?

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

The main goals of this recipe are therefore:

> To understand the where the need arises for mapping between data instance identifiers and identify some of the services available to support this.

This recipe assumes that you are already familiar with identifiers and the minting of identifiers.

*For more details on identifiers, see the [How to generate globally unique, resolvable and persistent identifiers](https://fairplus.github.io/cookbook-dev/recipes/findability/identifiers.html) recipe.*

___


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

___

## Identifier Mappings

> :notebook_with_decorative_cover: **"Identifiers are used to tag, identify, find and retrieve entities which are part of a collection or a resource maintained by some organization. "**

Organisations must create identifiers for namespaces for which they are the `authority` and this is often done in isolation of other organisations. This results in each organisation independently creating identifiers for the same concept, although there may be subtleties in the representation that mean that they are in fact unique concepts.



 



#### Identifier Mapping services

**ToDo:** Update the content of this section with available identifier mapping services

* [purl.org](https://archive.org/services/purl/)

    > The PURL system is a service of the Internet Archive, which provides an interface to administer domain. For more information about the service, visit https://archive.org/services/purl/help
    >

* [w3ids](https://w3id.org/)
  
    > Permanent Identifiers for the Web. Secure, permanent URLs for your Web application that will stand the test of time.
    > - authority registration service
    > - resolution service
    > - redirection service:
    > 
    > Send a request to add a redirect to the public-perma-id@w3.org mailing list. Make sure to include the URL that you want on w3id.org, the URL that you want to redirect to, and the HTTP code that you want to use when redirecting. An administrator will then create the redirect for you.


* [Identifiers.org](http://identifiers.org/)

    > [Identifiers.org](https://identifiers.org) is a **Resolution Service** provides consistent access to life science data using [`Compact Uniform Resource Identifiers`](https://www.w3.org/TR/2010/NOTE-curie-20101216/), hosted by the EBI provides a resolution service, both as a web form and through the URL pattern. 
    >`Compact Identifiers` consist of an `assigned`, `unique` `prefix` and a `local provider designated` **`accession number`** (prefix:accession).
    > The resolving location of `Compact Identifiers` is determined using information that is stored in the [Identifiers.org Registry](http://identifiers.org/).
    > Datasets can register their *namespace `prefix`* together with their `identifier pattern`. The service can then be used in the same way as the DOI resolution service. So for the UniProt page about BRCA1, we can resolve the CURIE `[uniprot:P38938]` using Identifiers.org. This means that the URL https://identifiers.org/uniprot:P38938 resolves to the UniProt page https://www.uniprot.org/uniprot/P38938.



* [Name2Things](https://n2t.net/)

    > [Name2Things](https://n2t.net/) (N2T) is a **Resolution Service**, maintained at the California Digital Library (CDL) within the University of California (UC) Office of the President. CDL supports electronic library services for ten UC campuses and affiliated law schools, medical centers, and national laboratories, as well as hundreds of museums, herbaria, botanical gardens, etc. Similar to URL shorteners like bit.ly, N2T serves content **indirectly**.
    > N2T can store more than one "target" (forwarding link) for an identifier, as well as any kind or amount of metadata (descriptive information)
        > N2T.net is also a "meta-resolver". In collaboration with identifiers.org, it recognizes over 600 well-known identifier types and knows where their respective servers are. Failing to find forwarding information for a specific individual identifier, it uses the identifier's type to look for an overall target rule.

*For more details, see the [Identifier Resolution Services recipe](./identifier-services/id-resolution.html).*

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

1. IRI. [https://tools.ietf.org/html/rfc3987](https://tools.ietf.org/html/rfc3987)
2. CURIE. [https://www.w3.org/TR/2010/NOTE-curie-20101216/](https://www.w3.org/TR/2010/NOTE-curie-20101216/)
3. URL. [https://tools.ietf.org/html/rfc1738](https://tools.ietf.org/html/rfc1738)
4. RDF concepts. https://www.w3.org/TR/rdf-concepts/ 
5. MD5 specifications. https://tools.ietf.org/html/rfc1321
6. Blake2 specifications. https://tools.ietf.org/html/rfc7693
7. Cool URIs don't change. https://www.w3.org/Provider/Style/URI
8. Leo Sauermann and Richard Cyganiak (eds.) (2008 December 3). Cool URIs for the Semantic Web, W3C Semantic Web Education and Outreach Interest Group Note, http://w3.org/TR/cooluris/
9. https://blog.adamretter.org.uk/archival-identifiers-for-digital-files/
10. https://blog.adamretter.org.uk/archival-catalog-identifiers/
11. Identifiers for the 21st century: How to design, provision, and reuse persistent identifiers to maximize utility and impact of life science data. https://doi.org/10.1371/journal.pbio.2001414
12. Nick Juty, Sarala M Wimalaratne, Stian Soiland-Reyes, John Kunze, Carole A Goble, and Tim Clark. 2020. Unique, persistent, resolvable: Identifiers as the foundation of FAIR. Data Intelligence (2020), 30–39. https://doi.org/10.1162/dint_a_00025
13. Nick Juty, Nicolas Le Novere, and Camille Laibe. 2012. Identifiers.org and MIRIAM Registry: Community resources to provide persistent identification. Nucleic Acids Research 40, D1 (2012), D580–D586. https://doi.org/10.1093/nar/gkr1097
14. Rachana Ananthakrishnan, Kyle  Chard, Mike  D'Arcy, Ian T Foster, Carl F Kesselman , Brendan  McCollam , Jim Christopher Pruyne , Philippe  Rocca-Serra, Robert E Schuler, Rick P Wagner. An Open Ecosystem for Pervasive Use of Persistent Identifiers. https://doi.org/10.1145/3311790.3396660


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
