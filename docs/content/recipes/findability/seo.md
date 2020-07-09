# Findability: Search Engine Optimization



<!-- **identifier:** [RX.X](RX.X)

**version:** [v0.1](v0.1)

 **_Difficulty level:_** :triangular_flag_on_post: :white_circle: :white_circle:  :white_circle:  :white_circle:

**_Reading time:_** 10 minutes

**_Intended Audience:_** 

> :heavy_check_mark: Application Developer

> :heavy_check_mark: Data Scientist

**_Recipe Type_**: Guidance

**_Executable code_**: No -->

___

<div class="row">

  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-qrcode fa-2x" style="color:#7e0038;"></i>
        <h4><b>Recipe metadata</b></h4>
        <p> identifier: <a href="">RX.X</a> </p>
        <p> version: <a href="">v1.0</a> </p>
      </div>
    </div>
  </div>
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-fire fa-2x" style="color:#7e0038;"></i>
        <h4><b>Difficulty level</b></h4>
        <i class="fa fa-fire fa-lg" style="color:#7e0038;"></i>
        <i class="fa fa-fire fa-lg" style="color:#7e0038;"></i>
        <i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
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
        <p><i class="fa fa-clock-o fa-lg" style="color:#7e0038;"></i> 10 minutes</p>
        <h4><b>Recipe Type</b></h4>
        <p><i class="fa fa-globe fa-lg" style="color:#7e0038;"></i> Guidance</p>
        <h4><b>Executable Code</b></h4>
        <p><i class="fa fa-play-circle" style="color:#fc7a4a;"></i> No</p>
      </div>
    </div>
  </div>
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-group fa-2x" style="color:#7e0038;"></i>
        <h4><b>Intended Audience</b></h4>
<!--         <p> <i class="fa fa-user-md fa-lg" style="color:#7e0038;"></i> Principal Investigators </p> -->
        <p> <i class="fa fa-cogs fa-lg" style="color:#7e0038;"></i> Software Developers </p>
        <p> <i class="fa fa-wrench fa-lg" style="color:#7e0038;"></i> Data Scientists </p>
 <!--        <p> <i class="fa fa-money fa-lg" style="color:#7e0038;"></i> Funders</p> -->
      </div>
    </div>
  </div>
</div>

___

# Table of Contents
1. [Main FAIRification Objectives](#Main%20Objectives)
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

> to describe what `search engine optimization` is and show how to implement markup with the [`Schema.org`](http://schema.org) vocabulary, and [`Bioschemas`](https://bioschemas.org) extension, to improve page discovery and visibility by web page indexers.

There are sub-recipes for embedding search engine optimization into specific web pages about a specific type or resource:
- [Data catalog](./seo/bioschemas-datacatalog.html)
- [Dataset](./seo/bioschemas-dataset.html)
- [Resource specific page](./seo/bioschemas-data-page.html) (Gene, Molecular Entity, Protein)

___


## Graphical Overview of the FAIRification Recipe Objectives

<!--
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgQShIVE1MIHBhZ2UpOjo6Ym94IC0tPnwgU2VhcmNoIEVuZ2luZSBPcHRpbWl6YXRpb258IEJ7V2hhdCA8YnI-dHlwZSA8YnI-IG9mPGJyPiBwYWdlP306Ojpib3hcbiAgQiAtLT4gQyhEYXRhc2V0KTo6OmJveFxuICBCIC0tPiBEKERhdGEgY2F0YWxvZyk6Ojpib3hcbiAgQiAtLT4gRShEYXRhIHBhZ2UpOjo6Ym94XG4gIEUgLS0-IEZ7V2hhdCA8YnI-IHR5cGUgb2YgPGJyPiBkYXRhIDxicj4gcGFnZX06Ojpib3hcbiAgRiAtLT4gRyhDaGVtaWNhbCBTdWJzdGFuY2UpOjo6Ym94XG4gIEYgLS0-IEgoR2VuZSk6Ojpib3hcbiAgRiAtLT4gSShNb2xlY3VsYXIgZW50aXR5KTo6OmJveFxuICBGIC0tPiBKKFByb3RlaW4pOjo6Ym94XG4gIEYgLS0-IEsoU2FtcGxlKTo6OmJveFxuICBGIC0tPiBMKFRheG9uKTo6OmJveFxuICBDIC0tPiBNXG4gIEQgLS0-IE1cbiAgRyAtLT4gTVxuICBIXHQtLT4gTVxuICBJIC0tPiBNXG4gIEogLS0-IE1cbiAgSyAtLT4gTVxuICBMIC0tPiBNKFNjaGVtYS5vcmcgYXVnbWVudGVkIEhUTUwgcGFnZSk6Ojpib3hcbiAgTSAtLT4gTihmYTpmYS1zZWFyY2ggZmE6ZmEtY29nIGZhOmZhLWZpZ2h0ZXItamV0IGltcHJvdmVkIGRpc2NvdmVyYWJpbGl0eSk6Ojpib3hcbmNsYXNzRGVmIGJveCBmb250LWZhbWlseTphdmVuaXIsZm9udC1zaXplOjE0cHgsZmlsbDojMmE5ZmM5LHN0cm9rZTojMjIyLGNvbG9yOiNmZmYsc3Ryb2tlLXdpZHRoOjFweFxubGlua1N0eWxlIDAsMSwyLDMsNCw1LDYsNyw4LDksMTAsMTEsMTIsMTMsMTQsMTUsMTYsMTcsMTgsMTkgc3Ryb2tlOiMyYTlmYzksc3Ryb2tlLXdpZHRoOjFweCxjb2xvcjojMmE5ZmM5LGZvbnQtZmFtaWx5OmF2ZW5pcjsiLCJtZXJtYWlkIjp7InRoZW1lIjpudWxsfSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiAgQShIVE1MIHBhZ2UpOjo6Ym94IC0tPnwgU2VhcmNoIEVuZ2luZSBPcHRpbWl6YXRpb258IEJ7V2hhdCA8YnI-dHlwZSA8YnI-IG9mPGJyPiBwYWdlP306Ojpib3hcbiAgQiAtLT4gQyhEYXRhc2V0KTo6OmJveFxuICBCIC0tPiBEKERhdGEgY2F0YWxvZyk6Ojpib3hcbiAgQiAtLT4gRShEYXRhIHBhZ2UpOjo6Ym94XG4gIEUgLS0-IEZ7V2hhdCA8YnI-IHR5cGUgb2YgPGJyPiBkYXRhIDxicj4gcGFnZX06Ojpib3hcbiAgRiAtLT4gRyhDaGVtaWNhbCBTdWJzdGFuY2UpOjo6Ym94XG4gIEYgLS0-IEgoR2VuZSk6Ojpib3hcbiAgRiAtLT4gSShNb2xlY3VsYXIgZW50aXR5KTo6OmJveFxuICBGIC0tPiBKKFByb3RlaW4pOjo6Ym94XG4gIEYgLS0-IEsoU2FtcGxlKTo6OmJveFxuICBGIC0tPiBMKFRheG9uKTo6OmJveFxuICBDIC0tPiBNXG4gIEQgLS0-IE1cbiAgRyAtLT4gTVxuICBIXHQtLT4gTVxuICBJIC0tPiBNXG4gIEogLS0-IE1cbiAgSyAtLT4gTVxuICBMIC0tPiBNKFNjaGVtYS5vcmcgYXVnbWVudGVkIEhUTUwgcGFnZSk6Ojpib3hcbiAgTSAtLT4gTihmYTpmYS1zZWFyY2ggZmE6ZmEtY29nIGZhOmZhLWZpZ2h0ZXItamV0IGltcHJvdmVkIGRpc2NvdmVyYWJpbGl0eSk6Ojpib3hcbmNsYXNzRGVmIGJveCBmb250LWZhbWlseTphdmVuaXIsZm9udC1zaXplOjE0cHgsZmlsbDojMmE5ZmM5LHN0cm9rZTojMjIyLGNvbG9yOiNmZmYsc3Ryb2tlLXdpZHRoOjFweFxubGlua1N0eWxlIDAsMSwyLDMsNCw1LDYsNyw4LDksMTAsMTEsMTIsMTMsMTQsMTUsMTYsMTcsMTgsMTkgc3Ryb2tlOiMyYTlmYzksc3Ryb2tlLXdpZHRoOjFweCxjb2xvcjojMmE5ZmM5LGZvbnQtZmFtaWx5OmF2ZW5pcjsiLCJtZXJtYWlkIjp7InRoZW1lIjpudWxsfSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)
-->

<div class="mermaid">
graph TD
  A(HTML page):::box -->| Search Engine Optimization| B{What <br>type <br> of<br> page?}:::box
  B --> C(Dataset):::box
  B --> D(Data catalog):::box
  B --> E(Data page):::box
  E --> F{What <br> type of <br> data <br> page}:::box
  F --> G(Chemical Substance):::box
  F --> H(Gene):::box
  F --> I(Molecular entity):::box
  F --> J(Protein):::box
  F --> K(Sample):::box
  F --> L(Taxon):::box
  C --> M
  D --> M
  G --> M
  H --> M
  I --> M
  J --> M
  K --> M
  L --> M(Schema.org augmented HTML page):::box
  M --> N(fa:fa-search fa:fa-cog fa:fa-fighter-jet improved discoverability):::box
classDef box font-family:avenir,font-size:14px,fill:#300861,stroke:#222,color:#fff,stroke-width:1px
linkStyle 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19 stroke:#2a9fc9,stroke-width:1px,color:#2a9fc9,font-family:avenir;
</div>
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

Search engine index pages based on their content, as identified by web crawlers. So any misclassification or errors in concept identification can affect where a given pages appears in a search results. Various techniques have been therefore been development by website designers, maintainers and engineers to improve ranking in search results. As ranking in search results significantly impact trafic to a web site and possibly revenues, especially if these are dependent on advertising, `search engine optimization` covers any of the practices which aim at improving the position of a web page in a search result. 


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


### Tools supporting creation and validation of `structured data`

Google has produced an online tool allowing developers to test the annotation they produce before rolling them out to production. 
The tool is known as the [`Google Structured Data Testing Tool`](https://search.google.com/structured-data/testing-tool)

![](https://i.imgur.com/Ge8gsWL.png =650px)



### Bioschemas: trying to address the coverage gap

`Schema.org` development is mainly driven by commercial applications. The scientific use case was not very high until recently. The Covid-19 pandemic exposed the needs to find datasets and disease related information more effectively. This proves to be a good timing for the [`Bioschemas project`](https://bioschemas.org/), which has been running for a few years with the support of the [`EU-Elixir organization`](https://elixir-europe.org/). `Bioschemas` focuses on making Schema.org more relevant for the life sciences community by providing:

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
| Leyla Garcia | Bioschemas Community / ZB MED Information Centre for life sciences, Knowledge Management Group | [0000-0003-3986-0510](https://orcid.org/0000-0003-3986-0510) | External review |

___


## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
