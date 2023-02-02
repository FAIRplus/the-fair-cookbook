(fcb-find-seo)=
# Search Engine Optimization (SEO)



````{panels_fairplus}
:identifier_text: FCB010
:identifier_link: 'https://w3id.org/faircookbook/FCB010'
:difficulty_level: 2
:recipe_type: guidance
:reading_time_minutes: 10
:intended_audience: software_developer, data_scientist
:maturity_level: 0
:maturity_indicator: 0
:has_executable_code: nope
:recipe_name: Introducing Search Engine Optimization (SEO) 
```` 

## Main Objectives

The main purpose of this recipe is:

> to describe what `search (URL_TO_INSERT_RECORD_2621 https://fairsharing.org/FAIRsharing.52b22c)  engine optimization` is and show how to implement markup with the [`Schema.org (URL_TO_INSERT_RECORD_2623 https://fairsharing.org/FAIRsharing.hzdzq8) `](http://schema.org (URL_TO_INSERT_RECORD_2624 https://fairsharing.org/FAIRsharing.hzdzq8) ) vocabulary, and [`Bioschemas`](https://bioschemas.org (URL_TO_INSERT_RECORD_2622 https://fairsharing.org/3517) ) extension, to improve page discovery and visibility by web page indexers.

There are sub-recipes for embedding search (URL_TO_INSERT_RECORD_2625 https://fairsharing.org/FAIRsharing.52b22c)  engine optimization into specific web pages about a specific type or resource:
- [Data catalog](fcb-find-bs-catalog)
- [Dataset](fcb-find-bs-dataset)
- [Resource specific page](fcb-find-bs-data) (Gene, Molecular Entity, Protein (URL_TO_INSERT_RECORD_2626 https://fairsharing.org/FAIRsharing.rtndct) )

---


## Graphical Overview

<!--
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgQShIVE1MIHBhZ2UpOjo6Ym94IC0tPnwgU2VhcmNoIEVuZ2luZSBPcHRpbWl6YXRpb258IEJ7V2hhdCA8YnI-dHlwZSA8YnI-IG9mPGJyPiBwYWdlP306Ojpib3hcbiAgQiAtLT4gQyhEYXRhc2V0KTo6OmJveFxuICBCIC0tPiBEKERhdGEgY2F0YWxvZyk6Ojpib3hcbiAgQiAtLT4gRShEYXRhIHBhZ2UpOjo6Ym94XG4gIEUgLS0-IEZ7V2hhdCA8YnI-IHR5cGUgb2YgPGJyPiBkYXRhIDxicj4gcGFnZX06Ojpib3hcbiAgRiAtLT4gRyhDaGVtaWNhbCBTdWJzdGFuY2UpOjo6Ym94XG4gIEYgLS0-IEgoR2VuZSk6Ojpib3hcbiAgRiAtLT4gSShNb2xlY3VsYXIgZW50aXR5KTo6OmJveFxuICBGIC0tPiBKKFByb3RlaW4pOjo6Ym94XG4gIEYgLS0-IEsoU2FtcGxlKTo6OmJveFxuICBGIC0tPiBMKFRheG9uKTo6OmJveFxuICBDIC0tPiBNXG4gIEQgLS0-IE1cbiAgRyAtLT4gTVxuICBIXHQtLT4gTVxuICBJIC0tPiBNXG4gIEogLS0-IE1cbiAgSyAtLT4gTVxuICBMIC0tPiBNKFNjaGVtYS5vcmcgYXVnbWVudGVkIEhUTUwgcGFnZSk6Ojpib3hcbiAgTSAtLT4gTihmYTpmYS1zZWFyY2ggZmE6ZmEtY29nIGZhOmZhLWZpZ2h0ZXItamV0IGltcHJvdmVkIGRpc2NvdmVyYWJpbGl0eSk6Ojpib3hcbmNsYXNzRGVmIGJveCBmb250LWZhbWlseTphdmVuaXIsZm9udC1zaXplOjE0cHgsZmlsbDojMmE5ZmM5LHN0cm9rZTojMjIyLGNvbG9yOiNmZmYsc3Ryb2tlLXdpZHRoOjFweFxubGlua1N0eWxlIDAsMSwyLDMsNCw1LDYsNyw4LDksMTAsMTEsMTIsMTMsMTQsMTUsMTYsMTcsMTgsMTkgc3Ryb2tlOiMyYTlmYzksc3Ryb2tlLXdpZHRoOjFweCxjb2xvcjojMmE5ZmM5LGZvbnQtZmFtaWx5OmF2ZW5pcjsiLCJtZXJtYWlkIjp7InRoZW1lIjpudWxsfSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiAgQShIVE1MIHBhZ2UpOjo6Ym94IC0tPnwgU2VhcmNoIEVuZ2luZSBPcHRpbWl6YXRpb258IEJ7V2hhdCA8YnI-dHlwZSA8YnI-IG9mPGJyPiBwYWdlP306Ojpib3hcbiAgQiAtLT4gQyhEYXRhc2V0KTo6OmJveFxuICBCIC0tPiBEKERhdGEgY2F0YWxvZyk6Ojpib3hcbiAgQiAtLT4gRShEYXRhIHBhZ2UpOjo6Ym94XG4gIEUgLS0-IEZ7V2hhdCA8YnI-IHR5cGUgb2YgPGJyPiBkYXRhIDxicj4gcGFnZX06Ojpib3hcbiAgRiAtLT4gRyhDaGVtaWNhbCBTdWJzdGFuY2UpOjo6Ym94XG4gIEYgLS0-IEgoR2VuZSk6Ojpib3hcbiAgRiAtLT4gSShNb2xlY3VsYXIgZW50aXR5KTo6OmJveFxuICBGIC0tPiBKKFByb3RlaW4pOjo6Ym94XG4gIEYgLS0-IEsoU2FtcGxlKTo6OmJveFxuICBGIC0tPiBMKFRheG9uKTo6OmJveFxuICBDIC0tPiBNXG4gIEQgLS0-IE1cbiAgRyAtLT4gTVxuICBIXHQtLT4gTVxuICBJIC0tPiBNXG4gIEogLS0-IE1cbiAgSyAtLT4gTVxuICBMIC0tPiBNKFNjaGVtYS5vcmcgYXVnbWVudGVkIEhUTUwgcGFnZSk6Ojpib3hcbiAgTSAtLT4gTihmYTpmYS1zZWFyY2ggZmE6ZmEtY29nIGZhOmZhLWZpZ2h0ZXItamV0IGltcHJvdmVkIGRpc2NvdmVyYWJpbGl0eSk6Ojpib3hcbmNsYXNzRGVmIGJveCBmb250LWZhbWlseTphdmVuaXIsZm9udC1zaXplOjE0cHgsZmlsbDojMmE5ZmM5LHN0cm9rZTojMjIyLGNvbG9yOiNmZmYsc3Ryb2tlLXdpZHRoOjFweFxubGlua1N0eWxlIDAsMSwyLDMsNCw1LDYsNyw4LDksMTAsMTEsMTIsMTMsMTQsMTUsMTYsMTcsMTgsMTkgc3Ryb2tlOiMyYTlmYzksc3Ryb2tlLXdpZHRoOjFweCxjb2xvcjojMmE5ZmM5LGZvbnQtZmFtaWx5OmF2ZW5pcjsiLCJtZXJtYWlkIjp7InRoZW1lIjpudWxsfSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)
-->

````{dropdown} 
:open:
```{figure} images/seo-mermaid.png
---
height: 750px
name: Search (URL_TO_INSERT_RECORD_2627 https://fairsharing.org/FAIRsharing.52b22c)  Engine Optimization
alt: Search (URL_TO_INSERT_RECORD_2628 https://fairsharing.org/FAIRsharing.52b22c)  Engine Optimization
---
Search (URL_TO_INSERT_RECORD_2629 https://fairsharing.org/FAIRsharing.52b22c)  Engine Optimization.
```
````

---

## Main body of the recipe

### Finding web pages

Providers of content for the Internet serve documents format (URL_TO_INSERT_TERM_2630 https://fairsharing.org/search?recordType=model_and_format) ted or rendered in [`HTML (URL_TO_INSERT_RECORD_2631 https://fairsharing.org/FAIRsharing.YugnuL) ` format](https://en.wikipedia.org/wiki/HTML). The web pages are hosted on servers, which are accessed via the [`HTTP protocol`](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol). HTML (URL_TO_INSERT_RECORD_2632 https://fairsharing.org/FAIRsharing.YugnuL)  pages can be styled with [`cascading stylesheets (CSS)`](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) and interactivity can be delivered via scripting languages such as [`Javascript`](https://en.wikipedia.org/wiki/JavaScript).

With billions of web pages served, a key issue is finding content. To assist in this task, search (URL_TO_INSERT_RECORD_2634 https://fairsharing.org/FAIRsharing.52b22c)  engines (e.g. Bing, Google, Yandex, Qwantt) have been built. They work by crawling the web, performing brute force keyword indexing or specific files served by the server (e.g. site map (URL_TO_INSERT_RECORD_2633 https://fairsharing.org/FAIRsharing.53edcc) ), or by targeting specific data structures embedded in the web pages themselves.

### What is search engine optimization

Search (URL_TO_INSERT_RECORD_2635 https://fairsharing.org/FAIRsharing.52b22c)  engine index pages based on their content, as identified by web crawlers. So any misclassification or errors in concept identification can affect where a given pages appears in a search (URL_TO_INSERT_RECORD_2636 https://fairsharing.org/FAIRsharing.52b22c)  results. Various techniques have been therefore been development by website designers, maintainers and engineers to improve ranking in search (URL_TO_INSERT_RECORD_2637 https://fairsharing.org/FAIRsharing.52b22c)  results. As ranking in search (URL_TO_INSERT_RECORD_2638 https://fairsharing.org/FAIRsharing.52b22c)  results significantly impact trafic to a web site and possibly revenues, especially if these are dependent on advertising, `search (URL_TO_INSERT_RECORD_2639 https://fairsharing.org/FAIRsharing.52b22c)  engine optimization` covers any of the practices which aim at improving the position of a web page in a search (URL_TO_INSERT_RECORD_2640 https://fairsharing.org/FAIRsharing.52b22c)  result. 


### Schema.org Vocabulary

A few years back, a consortium of search (URL_TO_INSERT_RECORD_2641 https://fairsharing.org/FAIRsharing.52b22c)  engines decided to combine forces to generate a structured vocabulary to identify and annotation entities, so search (URL_TO_INSERT_RECORD_2642 https://fairsharing.org/FAIRsharing.52b22c)  engine can index those more efficiently, bringing the power of semantics in the picture. The priorities for content addition to this vocabulary are defined by various factors, mostly driven between content advertising and relevance.
Compared to plain keyword based indexing, annotation with structured vocabulary affords gains such as query expansion or improved content validation.

### How does Schema.org work in practice:

The principle is actually fairly simple. It relies on embedding machine readable content into the HTML (URL_TO_INSERT_RECORD_2652 https://fairsharing.org/FAIRsharing.YugnuL)  file. A variety of options are available (RDF (URL_TO_INSERT_RECORD_2644 https://fairsharing.org/FAIRsharing.p77ph9) a (URL_TO_INSERT_RECORD_2649 https://fairsharing.org/663) , microformat (URL_TO_INSERT_TERM_2643 https://fairsharing.org/search?recordType=model_and_format) , JSO (URL_TO_INSERT_RECORD_2647 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_2645 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2650 https://fairsharing.org/FAIRsharing.8f9bbb) ). `JSO (URL_TO_INSERT_RECORD_2648 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_2646 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2651 https://fairsharing.org/FAIRsharing.8f9bbb) ` is widely recommended as the most suitable approach.

Below is a regular plain vanilla HTML (URL_TO_INSERT_RECORD_2655 https://fairsharing.org/FAIRsharing.YugnuL)  page providing informat (URL_TO_INSERT_TERM_2654 https://fairsharing.org/search?recordType=model_and_format) ion about an scientific journal (URL_TO_INSERT_TERM_2653 https://fairsharing.org/search?recordType=journal)  article.

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

Now, we are presenting the same informat (URL_TO_INSERT_TERM_2656 https://fairsharing.org/search?recordType=model_and_format) ion augmented with the JSO (URL_TO_INSERT_RECORD_2658 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_2657 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2659 https://fairsharing.org/FAIRsharing.8f9bbb)  file using Schema.org (URL_TO_INSERT_RECORD_2661 https://fairsharing.org/FAIRsharing.hzdzq8)  `ScholarlyArticle` profile. Note how the file is provided with the HTML (URL_TO_INSERT_RECORD_2660 https://fairsharing.org/FAIRsharing.YugnuL)  `script` tag

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


`JSO (URL_TO_INSERT_RECORD_2664 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_2663 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2665 https://fairsharing.org/FAIRsharing.8f9bbb) ` is an official serialization of `RDF (URL_TO_INSERT_RECORD_2662 https://fairsharing.org/FAIRsharing.p77ph9) ` and the document is recognized as a `graph` holding a set of `triples`. The availability of such semantic statements from a web page are exploited by the indexing algorithms of search (URL_TO_INSERT_RECORD_2666 https://fairsharing.org/FAIRsharing.52b22c)  engines to provide improved search (URL_TO_INSERT_RECORD_2667 https://fairsharing.org/FAIRsharing.52b22c)  results. 


### Tools supporting creation and validation of `structured data`

Google has produced an online tool allowing developers to test the annotation they produce before rolling them out to production. 
The tool is known as the [`Google Structured Data Testing Tool`](https://search.google.com/structured-data/testing-tool)
<!-- 
![](/images/Ge8gsWL.png =650px)

<div style="display: flex; justify-content: center;">
<img src="/images/Ge8gsWL.png" width="650" style="border:1px solid black"/>
</div> -->

````{dropdown} 
:open:
```{figure} /images/Ge8gsWL.png
---
height: 580px
name: Google Structured Data Testing Tool
alt: Google Structured Data Testing Tool
---
Google Structured Data Testing Tool.
```
````


### Bioschemas: trying to address the coverage gap

`Schema.org (URL_TO_INSERT_RECORD_2673 https://fairsharing.org/FAIRsharing.hzdzq8) ` development is mainly driven by commercial applications. The scientific use case was not very high until recently. The Covid-19 pandemic exposed the needs to find datasets and disease related informat (URL_TO_INSERT_TERM_2668 https://fairsharing.org/search?recordType=model_and_format) ion more effectively. This proves to be a good timing for the [`Bioschemas (URL_TO_INSERT_RECORD_2670 https://fairsharing.org/3517)  project`](https://bioschemas.org (URL_TO_INSERT_RECORD_2672 https://fairsharing.org/3517) /), which has been running for a few years with the support of the [`EU-Elixir organization`](https://elixir-europe.org (URL_TO_INSERT_RECORD_2669 https://fairsharing.org/3531) /). `Bioschemas (URL_TO_INSERT_RECORD_2671 https://fairsharing.org/3517) ` focuses on making Schema.org (URL_TO_INSERT_RECORD_2674 https://fairsharing.org/FAIRsharing.hzdzq8)  more relevant for the life sciences community by providing:

1. `types` for life sciences entities such as chemicals, genes, and proteins.
1. `profiles` that identify the most pertinent properties for marking up a life sciences resources of a specific type to enable it to be more findable.

The [main profiles](https://bioschemas.org (URL_TO_INSERT_RECORD_2676 https://fairsharing.org/3517) /profiles/) currently specified by the `Bioschemas (URL_TO_INSERT_RECORD_2675 https://fairsharing.org/3517) ` organisation are as follows:

* [Chemical Substance](https://bioschemas.org (URL_TO_INSERT_RECORD_2677 https://fairsharing.org/3517) /profiles/ChemicalSubstance)
* [DataCatalog](https://bioschemas.org (URL_TO_INSERT_RECORD_2678 https://fairsharing.org/3517) /profiles/DataCatalog)
* [Dataset](https://bioschemas.org (URL_TO_INSERT_RECORD_2680 https://fairsharing.org/3517) /profiles/Dataset (URL_TO_INSERT_RECORD_2679 https://fairsharing.org/FAIRsharing.20sbr9) )
* [Gene](https://bioschemas.org (URL_TO_INSERT_RECORD_2681 https://fairsharing.org/3517) /profiles/Gene)
* [Molecular Entity](https://bioschemas.org (URL_TO_INSERT_RECORD_2682 https://fairsharing.org/3517) /profiles/MolecularEntity)
* [Protein (URL_TO_INSERT_RECORD_2683 https://fairsharing.org/FAIRsharing.rtndct) ](https://bioschemas.org (URL_TO_INSERT_RECORD_2684 https://fairsharing.org/3517) /profiles/Protein)
* [Sample](https://bioschemas.org (URL_TO_INSERT_RECORD_2685 https://fairsharing.org/3517) /profiles/Sample)
* [Taxon](https://bioschemas.org (URL_TO_INSERT_RECORD_2686 https://fairsharing.org/3517) /profiles/Taxon)

---
## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [text annotation](http://edamontology.org (URL_TO_INSERT_RECORD_2687 https://fairsharing.org/FAIRsharing.a6r7zs) /operation_3778)  | [Schema.org (URL_TO_INSERT_RECORD_2691 https://fairsharing.org/FAIRsharing.hzdzq8) ](https://fairsharing.org (URL_TO_INSERT_RECORD_2689 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2690 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2692 https://fairsharing.org/3538) /FAIRsharing.hzdzq8)  | [annotated text](http://edamontology.org (URL_TO_INSERT_RECORD_2688 https://fairsharing.org/FAIRsharing.a6r7zs) /data_3779)  |
| [validation](http://edamontology.org (URL_TO_INSERT_RECORD_2693 https://fairsharing.org/FAIRsharing.a6r7zs) /operation_2428)  | [Schema.org (URL_TO_INSERT_RECORD_2697 https://fairsharing.org/FAIRsharing.hzdzq8) ](https://fairsharing.org (URL_TO_INSERT_RECORD_2695 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2696 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2698 https://fairsharing.org/3538) /FAIRsharing.hzdzq8)  | [report](http://edamontology.org (URL_TO_INSERT_RECORD_2694 https://fairsharing.org/FAIRsharing.a6r7zs) /data_2048)  |



## Table of Data Standards

| Data Format (URL_TO_INSERT_TERM_2700 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_2701 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_2699 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
|  [JSON-LD](http://edamontology.org (URL_TO_INSERT_RECORD_2702 https://fairsharing.org/FAIRsharing.a6r7zs) /format_3749)  | [Schema.org (URL_TO_INSERT_RECORD_2706 https://fairsharing.org/FAIRsharing.hzdzq8) ](https://fairsharing.org (URL_TO_INSERT_RECORD_2704 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2705 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2707 https://fairsharing.org/3538) /FAIRsharing.hzdzq8) | [RDF](http://edamontology.org (URL_TO_INSERT_RECORD_2703 https://fairsharing.org/FAIRsharing.a6r7zs) /data_2353)  |
| [JSON-LD](http://edamontology.org (URL_TO_INSERT_RECORD_2708 https://fairsharing.org/FAIRsharing.a6r7zs) /format_3749)  | [Bioschemas](https://fairsharing.org (URL_TO_INSERT_RECORD_2710 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2711 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2712 https://fairsharing.org/3538) /FAIRsharing.20sbr9) | [RDF](http://edamontology.org (URL_TO_INSERT_RECORD_2709 https://fairsharing.org/FAIRsharing.a6r7zs) /data_2353)  |



## Conclusion


### What to read next?

- {ref}`fcb-find-bs-data`
- {ref}`fcb-find-bs-catalog`
- {ref}`fcb-find-bs-dataset`

````{rdmkit_panel}
````


## References
````{dropdown} **References**
````



## Authors

````{authors_fairplus}
Philippe: Writing - Original Draft, Conceptualization
Alasdair: Writing - Original Draft, Writing - Review & Editing
Leyla: Writing - Review & Editing
````


## License

````{license_fairplus}
CC-BY-4.0
````
