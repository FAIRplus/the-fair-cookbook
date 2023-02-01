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

> to describe what `search (URL_TO_INSERT_RECORD_2984 https://fairsharing.org/FAIRsharing.52b22c)  engine optimization` is and show how to implement markup with the [`Schema.org (URL_TO_INSERT_RECORD_2986 https://fairsharing.org/FAIRsharing.hzdzq8) `](http://schema.org (URL_TO_INSERT_RECORD_2987 https://fairsharing.org/FAIRsharing.hzdzq8) ) vocabulary, and [`Bioschemas`](https://bioschemas.org (URL_TO_INSERT_RECORD_2985 https://fairsharing.org/3517) ) extension, to improve page discovery and visibility by web page indexers.

There are sub-recipes for embedding search (URL_TO_INSERT_RECORD_2988 https://fairsharing.org/FAIRsharing.52b22c)  engine optimization into specific web pages about a specific type or resource:
- [Data catalog](fcb-find-bs-catalog)
- [Dataset](fcb-find-bs-dataset)
- [Resource specific page](fcb-find-bs-data) (Gene, Molecular Entity, Protein (URL_TO_INSERT_RECORD_2989 https://fairsharing.org/FAIRsharing.rtndct) )

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
name: Search (URL_TO_INSERT_RECORD_2990 https://fairsharing.org/FAIRsharing.52b22c)  Engine Optimization
alt: Search (URL_TO_INSERT_RECORD_2991 https://fairsharing.org/FAIRsharing.52b22c)  Engine Optimization
---
Search (URL_TO_INSERT_RECORD_2992 https://fairsharing.org/FAIRsharing.52b22c)  Engine Optimization.
```
````

---

## Main body of the recipe

### Finding web pages

Providers of content for the Internet serve documents format (URL_TO_INSERT_TERM_2993 https://fairsharing.org/search?recordType=model_and_format) ted or rendered in [`HTML (URL_TO_INSERT_RECORD_2994 https://fairsharing.org/FAIRsharing.YugnuL) ` format](https://en.wikipedia.org/wiki/HTML). The web pages are hosted on servers, which are accessed via the [`HTTP protocol`](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol). HTML (URL_TO_INSERT_RECORD_2995 https://fairsharing.org/FAIRsharing.YugnuL)  pages can be styled with [`cascading stylesheets (CSS)`](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) and interactivity can be delivered via scripting languages such as [`Javascript`](https://en.wikipedia.org/wiki/JavaScript).

With billions of web pages served, a key issue is finding content. To assist in this task, search (URL_TO_INSERT_RECORD_2997 https://fairsharing.org/FAIRsharing.52b22c)  engines (e.g. Bing, Google, Yandex, Qwantt) have been built. They work by crawling the web, performing brute force keyword indexing or specific files served by the server (e.g. site map (URL_TO_INSERT_RECORD_2996 https://fairsharing.org/FAIRsharing.53edcc) ), or by targeting specific data structures embedded in the web pages themselves.

### What is search engine optimization

Search (URL_TO_INSERT_RECORD_2998 https://fairsharing.org/FAIRsharing.52b22c)  engine index pages based on their content, as identified by web crawlers. So any misclassification or errors in concept identification can affect where a given pages appears in a search (URL_TO_INSERT_RECORD_2999 https://fairsharing.org/FAIRsharing.52b22c)  results. Various techniques have been therefore been development by website designers, maintainers and engineers to improve ranking in search (URL_TO_INSERT_RECORD_3000 https://fairsharing.org/FAIRsharing.52b22c)  results. As ranking in search (URL_TO_INSERT_RECORD_3001 https://fairsharing.org/FAIRsharing.52b22c)  results significantly impact trafic to a web site and possibly revenues, especially if these are dependent on advertising, `search (URL_TO_INSERT_RECORD_3002 https://fairsharing.org/FAIRsharing.52b22c)  engine optimization` covers any of the practices which aim at improving the position of a web page in a search (URL_TO_INSERT_RECORD_3003 https://fairsharing.org/FAIRsharing.52b22c)  result. 


### Schema.org Vocabulary

A few years back, a consortium of search (URL_TO_INSERT_RECORD_3004 https://fairsharing.org/FAIRsharing.52b22c)  engines decided to combine forces to generate a structured vocabulary to identify and annotation entities, so search (URL_TO_INSERT_RECORD_3005 https://fairsharing.org/FAIRsharing.52b22c)  engine can index those more efficiently, bringing the power of semantics in the picture. The priorities for content addition to this vocabulary are defined by various factors, mostly driven between content advertising and relevance.
Compared to plain keyword based indexing, annotation with structured vocabulary affords gains such as query expansion or improved content validation.

### How does Schema.org work in practice:

The principle is actually fairly simple. It relies on embedding machine readable content into the HTML (URL_TO_INSERT_RECORD_3015 https://fairsharing.org/FAIRsharing.YugnuL)  file. A variety of options are available (RDF (URL_TO_INSERT_RECORD_3007 https://fairsharing.org/FAIRsharing.p77ph9) a (URL_TO_INSERT_RECORD_3012 https://fairsharing.org/663) , microformat (URL_TO_INSERT_TERM_3006 https://fairsharing.org/search?recordType=model_and_format) , JSO (URL_TO_INSERT_RECORD_3010 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_3008 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_3013 https://fairsharing.org/FAIRsharing.8f9bbb) ). `JSO (URL_TO_INSERT_RECORD_3011 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_3009 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_3014 https://fairsharing.org/FAIRsharing.8f9bbb) ` is widely recommended as the most suitable approach.

Below is a regular plain vanilla HTML (URL_TO_INSERT_RECORD_3018 https://fairsharing.org/FAIRsharing.YugnuL)  page providing informat (URL_TO_INSERT_TERM_3017 https://fairsharing.org/search?recordType=model_and_format) ion about an scientific journal (URL_TO_INSERT_TERM_3016 https://fairsharing.org/search?recordType=journal)  article.

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

Now, we are presenting the same informat (URL_TO_INSERT_TERM_3019 https://fairsharing.org/search?recordType=model_and_format) ion augmented with the JSO (URL_TO_INSERT_RECORD_3021 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_3020 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_3022 https://fairsharing.org/FAIRsharing.8f9bbb)  file using Schema.org (URL_TO_INSERT_RECORD_3024 https://fairsharing.org/FAIRsharing.hzdzq8)  (URL_TO_INSERT_RECORD_3025 https://fairsharing.org/FAIRsharing.hzdzq8)  `ScholarlyArticle` profile. Note how the file is provided with the HTML (URL_TO_INSERT_RECORD_3023 https://fairsharing.org/FAIRsharing.YugnuL)  `script` tag

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


`JSO (URL_TO_INSERT_RECORD_3028 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_3027 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_3029 https://fairsharing.org/FAIRsharing.8f9bbb) ` is an official serialization of `RDF (URL_TO_INSERT_RECORD_3026 https://fairsharing.org/FAIRsharing.p77ph9) ` and the document is recognized as a `graph` holding a set of `triples`. The availability of such semantic statements from a web page are exploited by the indexing algorithms of search (URL_TO_INSERT_RECORD_3030 https://fairsharing.org/FAIRsharing.52b22c)  engines to provide improved search (URL_TO_INSERT_RECORD_3031 https://fairsharing.org/FAIRsharing.52b22c)  results. 


### Tools supporting creation and validation of `structured data`

Google has produced an online tool allowing developers to test the annotation they produce before rolling them out to production. 
The tool is known as the [`Google Structured Data Testing (URL_TO_INSERT_RECORD_3032 https://fairsharing.org/FAIRsharing.q7bkqr)  Tool`](https://search.google.com/structured-data/testing-tool)
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
name: Google Structured Data Testing (URL_TO_INSERT_RECORD_3033 https://fairsharing.org/FAIRsharing.q7bkqr)  Tool
alt: Google Structured Data Testing (URL_TO_INSERT_RECORD_3034 https://fairsharing.org/FAIRsharing.q7bkqr)  Tool
---
Google Structured Data Testing (URL_TO_INSERT_RECORD_3035 https://fairsharing.org/FAIRsharing.q7bkqr)  Tool.
```
````


### Bioschemas: trying to address the coverage gap

`Schema.org (URL_TO_INSERT_RECORD_3043 https://fairsharing.org/FAIRsharing.hzdzq8)  (URL_TO_INSERT_RECORD_3045 https://fairsharing.org/FAIRsharing.hzdzq8) ` development is mainly driven by commercial applications. The scientific use case was not very high until recently. The Covid-19 pandemic exposed the needs to find datasets and disease related informat (URL_TO_INSERT_TERM_3036 https://fairsharing.org/search?recordType=model_and_format) ion more effectively. This proves to be a good timing for the [`Bioschemas (URL_TO_INSERT_RECORD_3038 https://fairsharing.org/3517)  (URL_TO_INSERT_RECORD_3040 https://fairsharing.org/3517)  project`](https://bioschemas.org (URL_TO_INSERT_RECORD_3042 https://fairsharing.org/3517) /), which has been running for a few years with the support of the [`EU-Elixir organization`](https://elixir-europe.org (URL_TO_INSERT_RECORD_3037 https://fairsharing.org/3531) /). `Bioschemas (URL_TO_INSERT_RECORD_3039 https://fairsharing.org/3517)  (URL_TO_INSERT_RECORD_3041 https://fairsharing.org/3517) ` focuses on making Schema.org (URL_TO_INSERT_RECORD_3044 https://fairsharing.org/FAIRsharing.hzdzq8)  (URL_TO_INSERT_RECORD_3046 https://fairsharing.org/FAIRsharing.hzdzq8)  more relevant for the life sciences community by providing:

1. `types` for life sciences entities such as chemicals, genes, and proteins.
1. `profiles` that identify the most pertinent properties for marking up a life sciences resources of a specific type to enable it to be more findable.

The [main profiles](https://bioschemas.org (URL_TO_INSERT_RECORD_3049 https://fairsharing.org/3517) /profiles/) currently specified by the `Bioschemas (URL_TO_INSERT_RECORD_3047 https://fairsharing.org/3517)  (URL_TO_INSERT_RECORD_3048 https://fairsharing.org/3517) ` organisation are as follows:

* [Chemical Substance](https://bioschemas.org (URL_TO_INSERT_RECORD_3050 https://fairsharing.org/3517) /profiles/ChemicalSubstance)
* [DataCatalog](https://bioschemas.org (URL_TO_INSERT_RECORD_3051 https://fairsharing.org/3517) /profiles/DataCatalog)
* [Dataset](https://bioschemas.org (URL_TO_INSERT_RECORD_3053 https://fairsharing.org/3517) /profiles/Dataset (URL_TO_INSERT_RECORD_3052 https://fairsharing.org/FAIRsharing.20sbr9) )
* [Gene](https://bioschemas.org (URL_TO_INSERT_RECORD_3054 https://fairsharing.org/3517) /profiles/Gene)
* [Molecular Entity](https://bioschemas.org (URL_TO_INSERT_RECORD_3055 https://fairsharing.org/3517) /profiles/MolecularEntity)
* [Protein (URL_TO_INSERT_RECORD_3056 https://fairsharing.org/FAIRsharing.rtndct) ](https://bioschemas.org (URL_TO_INSERT_RECORD_3057 https://fairsharing.org/3517) /profiles/Protein)
* [Sample](https://bioschemas.org (URL_TO_INSERT_RECORD_3058 https://fairsharing.org/3517) /profiles/Sample)
* [Taxon](https://bioschemas.org (URL_TO_INSERT_RECORD_3059 https://fairsharing.org/3517) /profiles/Taxon)

---
## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [text annotation](http://edamontology.org (URL_TO_INSERT_RECORD_3060 https://fairsharing.org/FAIRsharing.a6r7zs) /operation_3778)  | [Schema.org (URL_TO_INSERT_RECORD_3064 https://fairsharing.org/FAIRsharing.hzdzq8) ](https://fairsharing.org (URL_TO_INSERT_RECORD_3062 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_3063 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_3065 https://fairsharing.org/3538) /FAIRsharing.hzdzq8)  | [annotated text](http://edamontology.org (URL_TO_INSERT_RECORD_3061 https://fairsharing.org/FAIRsharing.a6r7zs) /data_3779)  |
| [validation](http://edamontology.org (URL_TO_INSERT_RECORD_3066 https://fairsharing.org/FAIRsharing.a6r7zs) /operation_2428)  | [Schema.org (URL_TO_INSERT_RECORD_3070 https://fairsharing.org/FAIRsharing.hzdzq8) ](https://fairsharing.org (URL_TO_INSERT_RECORD_3068 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_3069 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_3071 https://fairsharing.org/3538) /FAIRsharing.hzdzq8)  | [report](http://edamontology.org (URL_TO_INSERT_RECORD_3067 https://fairsharing.org/FAIRsharing.a6r7zs) /data_2048)  |



## Table of Data Standards

| Data Format (URL_TO_INSERT_TERM_3073 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_3074 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_3072 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
|  [JSON-LD](http://edamontology.org (URL_TO_INSERT_RECORD_3075 https://fairsharing.org/FAIRsharing.a6r7zs) /format_3749)  | [Schema.org (URL_TO_INSERT_RECORD_3079 https://fairsharing.org/FAIRsharing.hzdzq8) ](https://fairsharing.org (URL_TO_INSERT_RECORD_3077 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_3078 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_3080 https://fairsharing.org/3538) /FAIRsharing.hzdzq8) | [RDF](http://edamontology.org (URL_TO_INSERT_RECORD_3076 https://fairsharing.org/FAIRsharing.a6r7zs) /data_2353)  |
| [JSON-LD](http://edamontology.org (URL_TO_INSERT_RECORD_3081 https://fairsharing.org/FAIRsharing.a6r7zs) /format_3749)  | [Bioschemas](https://fairsharing.org (URL_TO_INSERT_RECORD_3083 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_3084 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_3085 https://fairsharing.org/3538) /FAIRsharing.20sbr9) | [RDF](http://edamontology.org (URL_TO_INSERT_RECORD_3082 https://fairsharing.org/FAIRsharing.a6r7zs) /data_2353)  |



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
