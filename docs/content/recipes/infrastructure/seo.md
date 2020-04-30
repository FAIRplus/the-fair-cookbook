# Findability: Search Engine Optimization


# Table of Contents
1. [Main FAIRification Objectives](#Main%20FAIRification%20Objectives)
2. [Graphical Overview of the FAIRification Recipe Objectives](#Graphical%20Overview%20of%20the%20FAIRification%20Recipe%20Objectives)
3. [FAIRification Objectives, Inputs and Outputs](#FAIRification%20Objectives,%20Inputs%20and%20Outputs)
4. [Capability & Maturity Table](#Capability%20&%20Maturity%20Table)
5. [Table of Data Standards](#Table%20of%20Data%20Standards)
6. [Executable Code in Notebook](#Executable%20Code%20in%20Notebook)
7. [How to create workflow figures](#How%20to%20create%20workflow%20figures)
8. [License](#License)

---

## Main Objectives

The main purpose of this recipe is:

> to describe what `search engine optimisation` is and show how to implement markup with the `Schema.org` vocabulary, and Bioschemas extension, to improve page discovery and visibility by web page indexers.

There are sub-recipes for embedding search engine optimisation into specific web pages about a specific type or resource:
- [Data catalog](bioschemas-datacatalog)
- [Dataset](bioschemas-dataset)
- [Resource specific page](bioschemas-protein) (Gene, Molecular Entity, Protein)

___


## Graphical Overview of the FAIRification Recipe Objectives
![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgQVtIVE1MIHBhZ2VdIC0tPnwgU2VhcmNoIEVuZ2luZSBPcHRpbWl6YXRpb258IEJ7d2hhdCB0eXBlIG9mIHBhZ2U_fVxuICBCIC0tPiBDW0RhdGFzZXRdXG4gIEIgLS0-IERbRGF0YSBjYXRhbG9nXVxuICBCIC0tPiBFW0RhdGEgcGFnZV1cbiAgRSAtLT4gRntXaGF0IHR5cGUgb2YgZGF0YSBwYWdlfVxuICBGIC0tPiBHW0NoZW1pY2FsIFN1YnN0YW5jZV1cbiAgRiAtLT4gSFtHZW5lXVxuICBGIC0tPiBJW01vbGVjdWxhciBlbnRpdHldXG4gIEYgLS0-IEpbUHJvdGVpbl1cbiAgRiAtLT4gS1tTYW1wbGVdXG4gIEYgLS0-IExbVGF4b25dXG4gIEMgLS0-IE1cbiAgRCAtLT4gTVxuICBHIC0tPiBNXG4gIEhcdC0tPiBNXG4gIEkgLS0-IE1cbiAgSiAtLT4gTVxuICBLIC0tPiBNXG4gIEwgLS0-IE1bU2NoZW1hLm9yZyBhdWdtZW50ZWQgSFRNTCBwYWdlXVxuICBNIC0tPiBOW2ZhOmZhLXNlYXJjaCBmYTpmYS1jb2cgZmE6ZmEtZmlnaHRlci1qZXQgaW1wcm92ZWQgZGlzY292ZXJhYmlsaXR5XSIsIm1lcm1haWQiOnsidGhlbWUiOiJuZXV0cmFsIn0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

```
graph TD
  A[HTML page] -->| Search Engine Optimization| B{what type of page?}
  B --> C[Dataset]
  B --> D[Data catalog]
  B --> E[Data page]
  E --> F{What type of data page}
  F --> G[Chemical Substance]
  F --> H[Gene]
  F --> I[Molecular entity]
  F --> J[Protein]
  F --> K[Sample]
  F --> L[Taxon]
  C --> M
  D --> M
  G --> M
  H	--> M
  I --> M
  J --> M
  K --> M
  L --> M[Schema.org augmented HTML page]
  M --> N[fa:fa-search fa:fa-cog fa:fa-fighter-jet improved discoverability]
```

___

## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Findabililty | minimal | repeatable |
| Interoperability | minimal | |

----

## Main body of the recipe

### Finding web pages

Providers of content for the Internet serve documents formatted or rendered in [`HTML` format](https://en.wikipedia.org/wiki/HTML). The web pages are hosted on servers, which are accessed via the [`HTTP protocol`](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol). HTML pages can be styled with [`cascading stylesheets (CSS)`](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) and interactivity can be delivered via scripting languages such as [`Javascript`](https://en.wikipedia.org/wiki/JavaScript).

With billions of web pages served, a key issue is finding content. To assist in this task, search engines (e.g. Bing, Google, Yandex, Qwantt) have been built. They work by crawling the web, performing brute force keyword indexing or specific files served by the server (e.g. site map), or by targeting specific data structures embedded in the web pages themselves.

### What is search engine optimization

Search engine index pages based on their content, as identified by web crawlers. So any misclassification or errors in concept identification can affect where a given pages appears in a search results. Various techniques have been therefore been development by website designers, maintainers and engineers to improve ranking in search results. As ranking in search results significantly impact trafic to a web site and possibly revenues, especially if these are dependent on advertising, `search engine optimization` covers any of the practises which aim at improving the position of a web page in a search result. 


### Schema.org Vocabulary

A few years back, a consortium of search engines decided to combine forces to generate a structured vocabulary to identify and annotation entities, so search engine can index those more efficiently, bringing the power of semantics in the picture. The priorities for content addition to this vocabulary are defined by various factors, mostly driven between content advertising and relevance.
Compared to plain keyword based indexing, annotation with structured vocabulary affords gains such as query expansion or improved content validation

### How does Schema.org work in practice:

The principle is actually fairly simple. It relies on embedding machine readable content into the HTML file. A variety of options are available (RDFa, microformat, JSON-LD). `JSON-LD` is widely recommended as the most suitable approach.

Below is a regular plain vanilla HTML page providing information about an scientific joournal article.

```HTML
<!-- A list of the issues for a single volume of a given periodical. -->
<div>
 <h1>The Lancet</h1>
 <p>Volume 376, July 2010-December 2010</p>
 <p>Published by Elsevier
 <ul>
   <li>ISSN: 0140-6736</li>
 </ul>
 <h3>Issues:</h3>
 <ul>
   <li>No. 9734 Jul 3, 2010 p 1-68</li>
   <li>No. 9735 Jul 10, 2010 p 69-140</li>
 </ul>
</div>
```

Now, we are presenting the same information augmented with the JSON-LD file using Schema.org `ScholarlyArticle` profile. Note how the file is provided with the HTML `script` tag

```JSON-LD
<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "@graph": [
    {
        "@id": "#issue",
        "@type": "PublicationIssue",
        "issueNumber": "5",
        "datePublished": "2012",
        "isPartOf": {
            "@id": "#periodical",
            "@type": [
                "PublicationVolume",
                "Periodical"
            ],
            "name": "Cataloging & Classification Quarterly",
            "issn": [
                "1544-4554",
                "0163-9374"
            ],
            "volumeNumber": "50",
            "publisher": "Taylor & Francis Group"
        }
    },
    {
        "@type": "ScholarlyArticle",
        "isPartOf": "#issue",
        "description": "The library catalog as a catalog of works was an infectious idea, which together with research led to reconceptualization in the form of the FRBR conceptual model. Two categories of lacunae emerge--the expression entity, and gaps in the model such as aggregates and dynamic documents. Evidence needed to extend the FRBR model is available in contemporary research on instantiation. The challenge for the bibliographic community is to begin to think of FRBR as a form of knowledge organization system, adding a final dimension to classification. The articles in the present special issue offer a compendium of the promise of the FRBR model.",
        "sameAs": "https://doi.org/10.1080/01639374.2012.682254",
        "about": [
            "Works",
            "Catalog"
        ],
        "pageEnd": "368",
        "pageStart": "360",
        "name": "Be Careful What You Wish For: FRBR, Some Lacunae, A Review",
        "author": "Smiraglia, Richard P."
    }
  ]
}
</script>

```


`JSON-LD` is an official serialization of `RDF` and the document is recognized as a `graph` holding a set of `triples`. The availability of such semantic statements from a web page are exploited by the indexing algorithms of search engines to provide improved search results. 


### Tools supported creation and validation to `structured data`

Google has produced an online tool allowing developers to test the annotation they produce before rolling them out to production. 
The tool is known as the [`Google Structured Data Testing Tool`](https://search.google.com/structured-data/testing-tool)

![](https://i.imgur.com/Ge8gsWL.png)



### Bioschemas: trying to address the coverage gap

`Schema.org` development is mainly driven by commercial applications. The scientific use case was not very high until recently. The Covid-19 pandemic exposed the needs to find datasets and disease related information more effectively. This proves to be a good timing for the [`Bioschemas project`](https://bioschemas.org/), which has been running for a few years with the support of the [`EU-Elixir organization`](https://elixir-europe.org/). `Bioschemas` focused on making Schema.org more relevant for the life sciences community by providing:

1. `types` for life sciences entities such as chemicals, genes, and proteins.
1. `profiles` that identify the most pertinent properties for marking up a life sciences resources of a specific type to enable it to be more findable

The [main profiles](https://bioschemas.org/profiles/) currently specified by the `Bioschemas` organisation are as follows:

* [Chemical Substance](https://bioschemas.org/profiles/ChemicalSubstance)
* [DataCatalog](https://bioschemas.org/profiles/DataCatalog)
* [Dataset](https://bioschemas.org/profiles/Dataset)
* [Gene](https://bioschemas.org/profiles/Gene)
* [Molecular Entity](https://bioschemas.org/profiles/MolecularEntity)
* [Protein](https://bioschemas.org/profiles/Protein)
* [Sample](https://bioschemas.org/profiles/Sample)
* [Taxon](https://bioschemas.org/profiles/Taxon)

----
## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [text annotation](http://edamontology.org/operation_3778)  | [Schema.org](https://fairsharing.org/FAIRsharing.hzdzq8)  | [annotated text](http://edamontology.org/data_3779)  |
| [validation](http://edamontology.org/operation_2428)  | [Schema.org](https://fairsharing.org/FAIRsharing.hzdzq8)  | [report](http://edamontology.org/data_2048)  |



## Table of Data Standards

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
|  [JSON-LD](http://edamontology.org/format_3749)  | [Schema.org](https://fairsharing.org/FAIRsharing.hzdzq8) | [RDF](http://edamontology.org/data_2353)  |
| [JSON-LD](http://edamontology.org/format_3749)  | [Bioschemas](https://fairsharing.org/FAIRsharing.20sbr9) | [RDF](http://edamontology.org/data_2353)  |

___



## Authors:

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Philippe Rocca-Serra |  University of Oxford, Data Readiness Group| [0000-0001-9853-5668](https://orcid.org/orcid.org/0000-0001-9853-5668) | Writing - Original Draft |
| Alasdair Gray | Bioschemas Community Lead / Heriot-Watt Unviersity / ELIXIR-UK | [0000-0002-5711-4872](https://orcid.org/0000-0002-5711-4872) | Contributions to text |
| Leyla Garcia | Bioschemas Community / ZBMED Information Centre for life sciences, Knowledge Management Group | [0000-0003-3986-0510](https://orcid.org/0000-0003-3986-0510) | External review |

___


## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
