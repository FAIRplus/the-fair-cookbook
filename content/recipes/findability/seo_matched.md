(fcb-find-seo)=
# Search Engine Optimization (SEO)



````{panels_fairplus}
```` 

## Main Objectives

The main purpose of this recipe is:

> to describe what `search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) engine optimization` is and show how to implement markup with the [`Schema.org(URL_TO_INSERT_RECORD http://schema.org/)`](http://schema.org(URL_TO_INSERT_RECORD http://schema.org/)) vocabulary, and [`Bioschemas`](https://bioschemas.org(URL_TO_INSERT_RECORD https://bioschemas.org)) extension, to improve page discovery and visibility by web page indexers.

There are sub-recipes for embedding search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) engine optimization into specific web pages about a specific type or resource:
- [Data catalog](fcb-find-bs-catalog)
- [Dataset](fcb-find-bs-dataset)
- [Resource specific page](fcb-find-bs-data) (Gene, Molecular Entity, Protein(URL_TO_INSERT_RECORD http://www.ncbi.nlm.nih.gov/protein))

---


## Graphical Overview

<!--
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgQShIVE1MIHBhZ2UpOjo6Ym94IC0tPnwgU2VhcmNoIEVuZ2luZSBPcHRpbWl6YXRpb258IEJ7V2hhdCA8YnI-dHlwZSA8YnI-IG9mPGJyPiBwYWdlP306Ojpib3hcbiAgQiAtLT4gQyhEYXRhc2V0KTo6OmJveFxuICBCIC0tPiBEKERhdGEgY2F0YWxvZyk6Ojpib3hcbiAgQiAtLT4gRShEYXRhIHBhZ2UpOjo6Ym94XG4gIEUgLS0-IEZ7V2hhdCA8YnI-IHR5cGUgb2YgPGJyPiBkYXRhIDxicj4gcGFnZX06Ojpib3hcbiAgRiAtLT4gRyhDaGVtaWNhbCBTdWJzdGFuY2UpOjo6Ym94XG4gIEYgLS0-IEgoR2VuZSk6Ojpib3hcbiAgRiAtLT4gSShNb2xlY3VsYXIgZW50aXR5KTo6OmJveFxuICBGIC0tPiBKKFByb3RlaW4pOjo6Ym94XG4gIEYgLS0-IEsoU2FtcGxlKTo6OmJveFxuICBGIC0tPiBMKFRheG9uKTo6OmJveFxuICBDIC0tPiBNXG4gIEQgLS0-IE1cbiAgRyAtLT4gTVxuICBIXHQtLT4gTVxuICBJIC0tPiBNXG4gIEogLS0-IE1cbiAgSyAtLT4gTVxuICBMIC0tPiBNKFNjaGVtYS5vcmcgYXVnbWVudGVkIEhUTUwgcGFnZSk6Ojpib3hcbiAgTSAtLT4gTihmYTpmYS1zZWFyY2ggZmE6ZmEtY29nIGZhOmZhLWZpZ2h0ZXItamV0IGltcHJvdmVkIGRpc2NvdmVyYWJpbGl0eSk6Ojpib3hcbmNsYXNzRGVmIGJveCBmb250LWZhbWlseTphdmVuaXIsZm9udC1zaXplOjE0cHgsZmlsbDojMmE5ZmM5LHN0cm9rZTojMjIyLGNvbG9yOiNmZmYsc3Ryb2tlLXdpZHRoOjFweFxubGlua1N0eWxlIDAsMSwyLDMsNCw1LDYsNyw4LDksMTAsMTEsMTIsMTMsMTQsMTUsMTYsMTcsMTgsMTkgc3Ryb2tlOiMyYTlmYzksc3Ryb2tlLXdpZHRoOjFweCxjb2xvcjojMmE5ZmM5LGZvbnQtZmFtaWx5OmF2ZW5pcjsiLCJtZXJtYWlkIjp7InRoZW1lIjpudWxsfSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiAgQShIVE1MIHBhZ2UpOjo6Ym94IC0tPnwgU2VhcmNoIEVuZ2luZSBPcHRpbWl6YXRpb258IEJ7V2hhdCA8YnI-dHlwZSA8YnI-IG9mPGJyPiBwYWdlP306Ojpib3hcbiAgQiAtLT4gQyhEYXRhc2V0KTo6OmJveFxuICBCIC0tPiBEKERhdGEgY2F0YWxvZyk6Ojpib3hcbiAgQiAtLT4gRShEYXRhIHBhZ2UpOjo6Ym94XG4gIEUgLS0-IEZ7V2hhdCA8YnI-IHR5cGUgb2YgPGJyPiBkYXRhIDxicj4gcGFnZX06Ojpib3hcbiAgRiAtLT4gRyhDaGVtaWNhbCBTdWJzdGFuY2UpOjo6Ym94XG4gIEYgLS0-IEgoR2VuZSk6Ojpib3hcbiAgRiAtLT4gSShNb2xlY3VsYXIgZW50aXR5KTo6OmJveFxuICBGIC0tPiBKKFByb3RlaW4pOjo6Ym94XG4gIEYgLS0-IEsoU2FtcGxlKTo6OmJveFxuICBGIC0tPiBMKFRheG9uKTo6OmJveFxuICBDIC0tPiBNXG4gIEQgLS0-IE1cbiAgRyAtLT4gTVxuICBIXHQtLT4gTVxuICBJIC0tPiBNXG4gIEogLS0-IE1cbiAgSyAtLT4gTVxuICBMIC0tPiBNKFNjaGVtYS5vcmcgYXVnbWVudGVkIEhUTUwgcGFnZSk6Ojpib3hcbiAgTSAtLT4gTihmYTpmYS1zZWFyY2ggZmE6ZmEtY29nIGZhOmZhLWZpZ2h0ZXItamV0IGltcHJvdmVkIGRpc2NvdmVyYWJpbGl0eSk6Ojpib3hcbmNsYXNzRGVmIGJveCBmb250LWZhbWlseTphdmVuaXIsZm9udC1zaXplOjE0cHgsZmlsbDojMmE5ZmM5LHN0cm9rZTojMjIyLGNvbG9yOiNmZmYsc3Ryb2tlLXdpZHRoOjFweFxubGlua1N0eWxlIDAsMSwyLDMsNCw1LDYsNyw4LDksMTAsMTEsMTIsMTMsMTQsMTUsMTYsMTcsMTgsMTkgc3Ryb2tlOiMyYTlmYzksc3Ryb2tlLXdpZHRoOjFweCxjb2xvcjojMmE5ZmM5LGZvbnQtZmFtaWx5OmF2ZW5pcjsiLCJtZXJtYWlkIjp7InRoZW1lIjpudWxsfSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)
-->

````{dropdown} 
```{figure} images/seo-mermaid.png
---
height: 750px
name: Search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) Engine Optimization
alt: Search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) Engine Optimization
---
Search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) Engine Optimization.
```
````

---

## Main body of the recipe

### Finding web pages

Providers of content for the Internet serve documents format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ted or rendered in [`HTML(URL_TO_INSERT_RECORD https://www.w3.org/TR/html53/)` format](https://en.wikipedia.org/wiki/HTML). The web pages are hosted on servers, which are accessed via the [`HTTP protocol`](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol). HTML(URL_TO_INSERT_RECORD https://www.w3.org/TR/html53/) pages can be styled with [`cascading stylesheets (CSS)`](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) and interactivity can be delivered via scripting languages such as [`Javascript`](https://en.wikipedia.org/wiki/JavaScript).

With billions of web pages served, a key issue is finding content. To assist in this task, search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) engines (e.g. Bing, Google, Yandex, Qwantt) have been built. They work by crawling the web, performing brute force keyword indexing or specific files served by the server (e.g. site map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)), or by targeting specific data structures embedded in the web pages themselves.

### What is search engine optimization

Search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) engine index pages based on their content, as identified by web crawlers. So any misclassification or errors in concept identification can affect where a given pages appears in a search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) results. Various techniques have been therefore been development by website designers, maintainers and engineers to improve ranking in search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) results. As ranking in search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) results significantly impact trafic to a web site and possibly revenues, especially if these are dependent on advertising, `search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) engine optimization` covers any of the practices which aim at improving the position of a web page in a search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) result. 


### Schema.org Vocabulary

A few years back, a consortium of search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) engines decided to combine forces to generate a structured vocabulary to identify and annotation entities, so search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) engine can index those more efficiently, bringing the power of semantics in the picture. The priorities for content addition to this vocabulary are defined by various factors, mostly driven between content advertising and relevance.
Compared to plain keyword based indexing, annotation with structured vocabulary affords gains such as query expansion or improved content validation.

### How does Schema.org work in practice:

The principle is actually fairly simple. It relies on embedding machine readable content into the HTML(URL_TO_INSERT_RECORD https://www.w3.org/TR/html53/) file. A variety of options are available (RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/)a(URL_TO_INSERT_RECORD https://www.w3.org/TR/rdfa-primer/), microformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format), JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259)-LD(URL_TO_INSERT_RECORD https://json-ld.org/spec/latest/json-ld/)). `JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259)-LD(URL_TO_INSERT_RECORD https://json-ld.org/spec/latest/json-ld/)` is widely recommended as the most suitable approach.

Below is a regular plain vanilla HTML(URL_TO_INSERT_RECORD https://www.w3.org/TR/html53/) page providing informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion about an scientific journal (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=journal) article.

```HTML
```

Now, we are presenting the same informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion augmented with the JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259)-LD(URL_TO_INSERT_RECORD https://json-ld.org/spec/latest/json-ld/) file using Schema.org(URL_TO_INSERT_RECORD http://schema.org/)(URL_TO_INSERT_RECORD http://schema.org/) `ScholarlyArticle` profile. Note how the file is provided with the HTML(URL_TO_INSERT_RECORD https://www.w3.org/TR/html53/) `script` tag

```bash

```


`JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259)-LD(URL_TO_INSERT_RECORD https://json-ld.org/spec/latest/json-ld/)` is an official serialization of `RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/)` and the document is recognized as a `graph` holding a set of `triples`. The availability of such semantic statements from a web page are exploited by the indexing algorithms of search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) engines to provide improved search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) results. 


### Tools supporting creation and validation of `structured data`

Google has produced an online tool allowing developers to test the annotation they produce before rolling them out to production. 
The tool is known as the [`Google Structured Data Testing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) Tool`](https://search.google.com/structured-data/testing-tool)
<!-- 
![](/images/Ge8gsWL.png =650px)

<div style="display: flex; justify-content: center;">
<img src="/images/Ge8gsWL.png" width="650" style="border:1px solid black"/>
</div> -->

````{dropdown} 
```{figure} /images/Ge8gsWL.png
---
height: 580px
name: Google Structured Data Testing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) Tool
alt: Google Structured Data Testing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) Tool
---
Google Structured Data Testing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) Tool.
```
````


### Bioschemas: trying to address the coverage gap

`Schema.org(URL_TO_INSERT_RECORD http://schema.org/)(URL_TO_INSERT_RECORD http://schema.org/)` development is mainly driven by commercial applications. The scientific use case was not very high until recently. The Covid-19 pandemic exposed the needs to find datasets and disease related informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion more effectively. This proves to be a good timing for the [`Bioschemas(URL_TO_INSERT_RECORD https://bioschemas.org)(URL_TO_INSERT_RECORD https://bioschemas.org) project`](https://bioschemas.org(URL_TO_INSERT_RECORD https://bioschemas.org)/), which has been running for a few years with the support of the [`EU-Elixir organization`](https://elixir-europe.org(URL_TO_INSERT_RECORD https://elixir-europe.org/)/). `Bioschemas(URL_TO_INSERT_RECORD https://bioschemas.org)(URL_TO_INSERT_RECORD https://bioschemas.org)` focuses on making Schema.org(URL_TO_INSERT_RECORD http://schema.org/)(URL_TO_INSERT_RECORD http://schema.org/) more relevant for the life sciences community by providing:

1. `types` for life sciences entities such as chemicals, genes, and proteins.
1. `profiles` that identify the most pertinent properties for marking up a life sciences resources of a specific type to enable it to be more findable.

The [main profiles](https://bioschemas.org(URL_TO_INSERT_RECORD https://bioschemas.org)/profiles/) currently specified by the `Bioschemas(URL_TO_INSERT_RECORD https://bioschemas.org)(URL_TO_INSERT_RECORD https://bioschemas.org)` organisation are as follows:

* [Chemical Substance](https://bioschemas.org(URL_TO_INSERT_RECORD https://bioschemas.org)/profiles/ChemicalSubstance)
* [DataCatalog](https://bioschemas.org(URL_TO_INSERT_RECORD https://bioschemas.org)/profiles/DataCatalog)
* [Dataset](https://bioschemas.org(URL_TO_INSERT_RECORD https://bioschemas.org)/profiles/Dataset(URL_TO_INSERT_RECORD https://bioschemas.org/profiles/Dataset/))
* [Gene](https://bioschemas.org(URL_TO_INSERT_RECORD https://bioschemas.org)/profiles/Gene)
* [Molecular Entity](https://bioschemas.org(URL_TO_INSERT_RECORD https://bioschemas.org)/profiles/MolecularEntity)
* [Protein(URL_TO_INSERT_RECORD http://www.ncbi.nlm.nih.gov/protein)](https://bioschemas.org(URL_TO_INSERT_RECORD https://bioschemas.org)/profiles/Protein)
* [Sample](https://bioschemas.org(URL_TO_INSERT_RECORD https://bioschemas.org)/profiles/Sample)
* [Taxon](https://bioschemas.org(URL_TO_INSERT_RECORD https://bioschemas.org)/profiles/Taxon)

---
## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [text annotation](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/operation_3778)  | [Schema.org(URL_TO_INSERT_RECORD http://schema.org/)](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.hzdzq8)  | [annotated text](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/data_3779)  |
| [validation](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/operation_2428)  | [Schema.org(URL_TO_INSERT_RECORD http://schema.org/)](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.hzdzq8)  | [report](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/data_2048)  |



## Table of Data Standards

| Data Format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s  | Terminologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) | Model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s  |
| :------------- | :------------- | :------------- |
|  [JSON-LD](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/format_3749)  | [Schema.org(URL_TO_INSERT_RECORD http://schema.org/)](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.hzdzq8) | [RDF](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/data_2353)  |
| [JSON-LD](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/format_3749)  | [Bioschemas](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.20sbr9) | [RDF](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/data_2353)  |



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
````


## License

````{license_fairplus}
````
