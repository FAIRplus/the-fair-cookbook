(fcb-find-seo)=
# Search engine optimization

+++
<br/>

````{panels_fairplus}
:identifier_text: FCB010
:identifier_link: 'https://w3id.org/faircookbook/FCB010'
:difficulty_level: 2
:recipe_type: guidance
:reading_time_minutes: 10
:intended_audience: software_developer, data_scientist  
:has_executable_code: nope
:recipe_name: Search engine optimization
```` 

## Main Objectives

The main purpose of this recipe is:

> to describe what `search engine optimization` is and show how to implement markup with the [`Schema.org`](http://schema.org) vocabulary, and [`Bioschemas`](https://bioschemas.org) extension, to improve page discovery and visibility by web page indexers.

There are sub-recipes for embedding search engine optimization into specific web pages about a specific type or resource:
- [Data catalog](fcb-find-bs-catalog)
- [Dataset](fcb-find-bs-dataset)
- [Resource specific page](fcb-find-bs-data) (Gene, Molecular Entity, Protein)

---


## Graphical Overview

<!--
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgQShIVE1MIHBhZ2UpOjo6Ym94IC0tPnwgU2VhcmNoIEVuZ2luZSBPcHRpbWl6YXRpb258IEJ7V2hhdCA8YnI-dHlwZSA8YnI-IG9mPGJyPiBwYWdlP306Ojpib3hcbiAgQiAtLT4gQyhEYXRhc2V0KTo6OmJveFxuICBCIC0tPiBEKERhdGEgY2F0YWxvZyk6Ojpib3hcbiAgQiAtLT4gRShEYXRhIHBhZ2UpOjo6Ym94XG4gIEUgLS0-IEZ7V2hhdCA8YnI-IHR5cGUgb2YgPGJyPiBkYXRhIDxicj4gcGFnZX06Ojpib3hcbiAgRiAtLT4gRyhDaGVtaWNhbCBTdWJzdGFuY2UpOjo6Ym94XG4gIEYgLS0-IEgoR2VuZSk6Ojpib3hcbiAgRiAtLT4gSShNb2xlY3VsYXIgZW50aXR5KTo6OmJveFxuICBGIC0tPiBKKFByb3RlaW4pOjo6Ym94XG4gIEYgLS0-IEsoU2FtcGxlKTo6OmJveFxuICBGIC0tPiBMKFRheG9uKTo6OmJveFxuICBDIC0tPiBNXG4gIEQgLS0-IE1cbiAgRyAtLT4gTVxuICBIXHQtLT4gTVxuICBJIC0tPiBNXG4gIEogLS0-IE1cbiAgSyAtLT4gTVxuICBMIC0tPiBNKFNjaGVtYS5vcmcgYXVnbWVudGVkIEhUTUwgcGFnZSk6Ojpib3hcbiAgTSAtLT4gTihmYTpmYS1zZWFyY2ggZmE6ZmEtY29nIGZhOmZhLWZpZ2h0ZXItamV0IGltcHJvdmVkIGRpc2NvdmVyYWJpbGl0eSk6Ojpib3hcbmNsYXNzRGVmIGJveCBmb250LWZhbWlseTphdmVuaXIsZm9udC1zaXplOjE0cHgsZmlsbDojMmE5ZmM5LHN0cm9rZTojMjIyLGNvbG9yOiNmZmYsc3Ryb2tlLXdpZHRoOjFweFxubGlua1N0eWxlIDAsMSwyLDMsNCw1LDYsNyw4LDksMTAsMTEsMTIsMTMsMTQsMTUsMTYsMTcsMTgsMTkgc3Ryb2tlOiMyYTlmYzksc3Ryb2tlLXdpZHRoOjFweCxjb2xvcjojMmE5ZmM5LGZvbnQtZmFtaWx5OmF2ZW5pcjsiLCJtZXJtYWlkIjp7InRoZW1lIjpudWxsfSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiAgQShIVE1MIHBhZ2UpOjo6Ym94IC0tPnwgU2VhcmNoIEVuZ2luZSBPcHRpbWl6YXRpb258IEJ7V2hhdCA8YnI-dHlwZSA8YnI-IG9mPGJyPiBwYWdlP306Ojpib3hcbiAgQiAtLT4gQyhEYXRhc2V0KTo6OmJveFxuICBCIC0tPiBEKERhdGEgY2F0YWxvZyk6Ojpib3hcbiAgQiAtLT4gRShEYXRhIHBhZ2UpOjo6Ym94XG4gIEUgLS0-IEZ7V2hhdCA8YnI-IHR5cGUgb2YgPGJyPiBkYXRhIDxicj4gcGFnZX06Ojpib3hcbiAgRiAtLT4gRyhDaGVtaWNhbCBTdWJzdGFuY2UpOjo6Ym94XG4gIEYgLS0-IEgoR2VuZSk6Ojpib3hcbiAgRiAtLT4gSShNb2xlY3VsYXIgZW50aXR5KTo6OmJveFxuICBGIC0tPiBKKFByb3RlaW4pOjo6Ym94XG4gIEYgLS0-IEsoU2FtcGxlKTo6OmJveFxuICBGIC0tPiBMKFRheG9uKTo6OmJveFxuICBDIC0tPiBNXG4gIEQgLS0-IE1cbiAgRyAtLT4gTVxuICBIXHQtLT4gTVxuICBJIC0tPiBNXG4gIEogLS0-IE1cbiAgSyAtLT4gTVxuICBMIC0tPiBNKFNjaGVtYS5vcmcgYXVnbWVudGVkIEhUTUwgcGFnZSk6Ojpib3hcbiAgTSAtLT4gTihmYTpmYS1zZWFyY2ggZmE6ZmEtY29nIGZhOmZhLWZpZ2h0ZXItamV0IGltcHJvdmVkIGRpc2NvdmVyYWJpbGl0eSk6Ojpib3hcbmNsYXNzRGVmIGJveCBmb250LWZhbWlseTphdmVuaXIsZm9udC1zaXplOjE0cHgsZmlsbDojMmE5ZmM5LHN0cm9rZTojMjIyLGNvbG9yOiNmZmYsc3Ryb2tlLXdpZHRoOjFweFxubGlua1N0eWxlIDAsMSwyLDMsNCw1LDYsNyw4LDksMTAsMTEsMTIsMTMsMTQsMTUsMTYsMTcsMTgsMTkgc3Ryb2tlOiMyYTlmYzksc3Ryb2tlLXdpZHRoOjFweCxjb2xvcjojMmE5ZmM5LGZvbnQtZmFtaWx5OmF2ZW5pcjsiLCJtZXJtYWlkIjp7InRoZW1lIjpudWxsfSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)
-->


```{figure} images/seo-mermaid.png
---
height: 550px
name: Search Engine Optimization
alt: Search Engine Optimization
---
Search Engine Optimization.
```

---

## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Findabililty | minimal | repeatable |
| Interoperability | minimal | |

---

## Main body of the recipe

### Finding web pages

Providers of content for the Internet serve documents formatted or rendered in [`HTML` format](https://en.wikipedia.org/wiki/HTML). The web pages are hosted on servers, which are accessed via the [`HTTP protocol`](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol). HTML pages can be styled with [`cascading stylesheets (CSS)`](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) and interactivity can be delivered via scripting languages such as [`Javascript`](https://en.wikipedia.org/wiki/JavaScript).

With billions of web pages served, a key issue is finding content. To assist in this task, search engines (e.g. Bing, Google, Yandex, Qwantt) have been built. They work by crawling the web, performing brute force keyword indexing or specific files served by the server (e.g. site map), or by targeting specific data structures embedded in the web pages themselves.

### What is search engine optimization

Search engine index pages based on their content, as identified by web crawlers. So any misclassification or errors in concept identification can affect where a given pages appears in a search results. Various techniques have been therefore been development by website designers, maintainers and engineers to improve ranking in search results. As ranking in search results significantly impact trafic to a web site and possibly revenues, especially if these are dependent on advertising, `search engine optimization` covers any of the practices which aim at improving the position of a web page in a search result. 


### Schema.org Vocabulary

A few years back, a consortium of search engines decided to combine forces to generate a structured vocabulary to identify and annotation entities, so search engine can index those more efficiently, bringing the power of semantics in the picture. The priorities for content addition to this vocabulary are defined by various factors, mostly driven between content advertising and relevance.
Compared to plain keyword based indexing, annotation with structured vocabulary affords gains such as query expansion or improved content validation.

### How does Schema.org work in practice:

The principle is actually fairly simple. It relies on embedding machine readable content into the HTML file. A variety of options are available (RDFa, microformat, JSON-LD). `JSON-LD` is widely recommended as the most suitable approach.

Below is a regular plain vanilla HTML page providing information about an scientific journal article.

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

```bash
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


### Tools supporting creation and validation of `structured data`

Google has produced an online tool allowing developers to test the annotation they produce before rolling them out to production. 
The tool is known as the [`Google Structured Data Testing Tool`](https://search.google.com/structured-data/testing-tool)
<!-- 
![](/images/Ge8gsWL.png =650px)

<div style="display: flex; justify-content: center;">
<img src="/images/Ge8gsWL.png" width="650" style="border:1px solid black"/>
</div> -->


```{figure} /images/Ge8gsWL.png
---
height: 580px
name: Google Structured Data Testing Tool
alt: Google Structured Data Testing Tool
---
Google Structured Data Testing Tool.
```


### Bioschemas: trying to address the coverage gap

`Schema.org` development is mainly driven by commercial applications. The scientific use case was not very high until recently. The Covid-19 pandemic exposed the needs to find datasets and disease related information more effectively. This proves to be a good timing for the [`Bioschemas project`](https://bioschemas.org/), which has been running for a few years with the support of the [`EU-Elixir organization`](https://elixir-europe.org/). `Bioschemas` focuses on making Schema.org more relevant for the life sciences community by providing:

1. `types` for life sciences entities such as chemicals, genes, and proteins.
1. `profiles` that identify the most pertinent properties for marking up a life sciences resources of a specific type to enable it to be more findable.

The [main profiles](https://bioschemas.org/profiles/) currently specified by the `Bioschemas` organisation are as follows:

* [Chemical Substance](https://bioschemas.org/profiles/ChemicalSubstance)
* [DataCatalog](https://bioschemas.org/profiles/DataCatalog)
* [Dataset](https://bioschemas.org/profiles/Dataset)
* [Gene](https://bioschemas.org/profiles/Gene)
* [Molecular Entity](https://bioschemas.org/profiles/MolecularEntity)
* [Protein](https://bioschemas.org/profiles/Protein)
* [Sample](https://bioschemas.org/profiles/Sample)
* [Taxon](https://bioschemas.org/profiles/Taxon)

---
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

---



## Authors

````{authors_fairplus}
Philippe: Writing - Original Draft, Conceptualization
Alasdair: Writing - Original Draft, Writing - Review & Editing
Leyla: Writing - Review & Editing
````


---

## License

````{license_fairplus}
CC-BY-4.0
````
