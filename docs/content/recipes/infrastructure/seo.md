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

> to describe what `search engine optimisation` is and show how to implement markup with `schema.org` vocabulary to improve page discovery and visibility by web page indexers.

___


## Graphical Overview of the FAIRification Recipe Objectives
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgQVtIVE1MIHBhZ2VdIC0tPnwgU2VhcmNoIEVuZ2luZSBPcHRpbWl6YXRpb258IEIoZmE6ZmEtc2VhcmNoIFNjaGVtYS5vcmcgYXVnbWVudGVkIEhUTUwgcGFnZSlcbiAgQiAtLT4gQ3t3aGljaCB0ZWNobmlxdWU_fVxuICBDIC0tPnxPbmV8IERbZmE6ZmEtc3RhciBmYTpmYS1zdGFyIGZhOmZhLXN0YXIgSlNPTi1MRF1cbiAgQyAtLT58VHdvfCBFW2ZhOmZhLXN0YXIgZmE6ZmEtc3RhciBSREZhXVxuICBDIC0tPnxUaHJlZXwgRltmYTpmYS1zdGFyIG1pY3JvZm9ybWF0XVxuICBEIC0tPiBHXG5cdEUgLS0-IEdcbiAgRlx0LS0-IEdbZmE6ZmEtc2VhcmNoIGZhOmZhLWNvZyBmYTpmYS1maWdodGVyLWpldCBpbXByb3ZlZCBkaXNjb3ZlcmFiaWxpdHldIiwibWVybWFpZCI6eyJ0aGVtZSI6Im5ldXRyYWwifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiAgQVtIVE1MIHBhZ2VdIC0tPnwgU2VhcmNoIEVuZ2luZSBPcHRpbWl6YXRpb258IEIoZmE6ZmEtc2VhcmNoIFNjaGVtYS5vcmcgYXVnbWVudGVkIEhUTUwgcGFnZSlcbiAgQiAtLT4gQ3t3aGljaCB0ZWNobmlxdWU_fVxuICBDIC0tPnxPbmV8IERbZmE6ZmEtc3RhciBmYTpmYS1zdGFyIGZhOmZhLXN0YXIgSlNPTi1MRF1cbiAgQyAtLT58VHdvfCBFW2ZhOmZhLXN0YXIgZmE6ZmEtc3RhciBSREZhXVxuICBDIC0tPnxUaHJlZXwgRltmYTpmYS1zdGFyIG1pY3JvZm9ybWF0XVxuICBEIC0tPiBHXG5cdEUgLS0-IEdcbiAgRlx0LS0-IEdbZmE6ZmEtc2VhcmNoIGZhOmZhLWNvZyBmYTpmYS1maWdodGVyLWpldCBpbXByb3ZlZCBkaXNjb3ZlcmFiaWxpdHldIiwibWVybWFpZCI6eyJ0aGVtZSI6Im5ldXRyYWwifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)


```
graph TD
  A[HTML page] -->| Search Engine Optimization| B(Schema.org augmented HTML page)
  B --> C{which technique?}
  C -->|One| D[fa:fa-star fa:fa-star fa:fa-star JSON-LD]
  C -->|Two| E[fa:fa-star fa:fa-star RDFa]
  C -->|Three| F[fa:fa-star microformat]
  D --> G
	E --> G
  F	--> G[fa:fa-search fa:fa-cog fa:fa-fighter-jet improved discoverability]
```  
  
___

## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Findabililty | minimal | repeatable |

----

## Main body of the recipe

### Finding web pages

Providers of content for the Internet serve documents formatted or rendered in [`HTML` format](https://en.wikipedia.org/wiki/HTML). The web pages are hosted on servers, which are accessed via the [`HTTP protocol`](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol). HTML pages can be styled with `cascading stylesheets (CSS)[https://en.wikipedia.org/wiki/Cascading_Style_Sheets]` and interactivity can be delivered via scripting language, in particular [`Javascript`](https://en.wikipedia.org/wiki/JavaScript).
With billions of web pages served, a key issue is finding content. To assist in this task, search engines (e.g. Bing, Google, Yandex, Qwantt) have been built. They work by crawling the web, performing brute force keyword indexing or specific files served by the server (.e.g site map), or by targeting specific data structures embedded in the web pages themselves.

### What is search engine optimization

Search engine index pages based on their content, as identified by web crawlers. So any misclassification or errors in concept identification can affect where a given pages appears in a search results. Various techniques have been therefore been development by website designers, maintainers and engineers to improve ranking in search results. As ranking in search results significantly impact trafic to a web site and possibly revenues, especially if these are dependent on advertising, `search engine optimization` covers any of the practises which aim at improving the position of a web page in a search result. 


### Schema.org Vocabulary

A few years back, a consortium of search engines decided to combine forces to generate a structured vocabulary to identify and annotation entities, so search engine can index those more efficiently, bringing the power of semantics in the picture. The priorities for content addition to this vocabulary are defined by various factors, mostly driven between content advertising and relevance.
Compared to plain keyword based indexing, annotation with structured vocabulary affords gains such as query expansion or improved content validation

### How does schema.org works in practice:

The principle is actually fairly simple. It essentially relies on embebbed a file into the HTML content. A variety of options are available (RDFa, microformat, JSON-LD). `JSON-LD` is fast becoming a very popular way to representing key entities served by the page.

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


'JSON-LD' is an official serialization of RDF and the document is recognized as a `graph` holding a set of `triples`. These availability of such semantic statements from web page are exploited by the indexing algorithm to place the pages in a semantic search space moree accurately. 


### Tools supported creation and validation to `structured data`

Google has produced a online tool allowing developers to test the annotation they produce before rolling them out to production. 
The tool is known as the [`Google Structured Data Testing Tool`](https://search.google.com/structured-data/testing-tool)

![](https://i.imgur.com/Ge8gsWL.png)



### Bioschema: trying to address the coverage gap

`Schema.org` development is mainly driven by commercial applications. The scientific use case was not very high until recently. The Covid-19 pandemic exposed the needs to find datasets and disease related information more effectively. This proves to be a good timing for the [`Bioschemas project`](https://bioschemas.org/), which has been running for a few years with the support of the [`EU-Elixir organization`](https://elixir-europe.org/). `Bioschema` concerned itself with providing `types` addressing the unmeet needs of Bioinformiticians and `Findability` of biological information via search engine searches. The [main profiles](https://bioschemas.org/profiles/) currently specified by the `Bioschema` organisation are as follows:

* [Dataset]()
* [Chemical Substance]()
* [Molecular Entity]()
* [Gene]()
* [Protein]()
* [Taxon]()
* [Sample]()






----
## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [text annotation](http://edamontology.org/operation_3778)  | [schema.org](https://fairsharing.org/FAIRsharing.hzdzq8)  | [annotated text](http://edamontology.org/data_3779)  |
| [validation](http://edamontology.org/operation_2428)  | [schema.org](https://fairsharing.org/FAIRsharing.hzdzq8)  | [report](http://edamontology.org/data_2048)  |



## Table of Data Standards

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
|  [JSON-LD](https://fairsharing.org/bsg-s001214/)  | [schema.org](https://fairsharing.org/FAIRsharing.hzdzq8) | [RDF](https://fairsharing.org/FAIRsharing.qk984b)  |
|   |  |   |

___



## Authors:

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Philippe Rocca-Serra |  University of Oxford, Data Readiness Group| [0000-0001-9853-5668](https://orcid.org/orcid.org/0000-0001-9853-5668) | Writing - Original Draft | 

___


## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
