# Findability: Data Page Markup with Bioschemas 

<!-- **identifier:** [RX.X](RX.X)

**version:** [v0.1](v0.1)

___

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
        <p> version: <a href="">v0.1</a> </p>
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


<!-- 
___

# Table of Contents

1. [Main FAIRification Objectives](#Main%20Objectives)
2. [Graphical Overview of the FAIRification Recipe Objectives](#Graphical%20Overview%20of%20the%20FAIRification%20Recipe%20Objectives)
3. [FAIRification Objectives, Inputs and Outputs](#FAIRification%20Objectives,%20Inputs%20and%20Outputs)
4. [Capability & Maturity Table](#Capability%20&%20Maturity%20Table)
5. [Table of Data Standards](#Table%20of%20Data%20Standards)
6. [Executable Code in Notebook](#Executable%20Code%20in%20Notebook)
7. [How to create workflow figures](#How%20to%20create%20workflow%20figures)
8. [License](#License) -->

---

## Main Objectives

The main purpose of this recipe is:

> To markup a webpage representing a data record with `Bioschemas` compliant markup.

___


## Graphical Overview of the FAIRification Recipe Objectives
<!--
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiBBKEhUTUwgcGFnZSk6Ojpib3ggLS0-IHxDcmVhdGUgbWFya3VwIHRlbXBsYXRlfCBCe3doYXQgdHlwZSA8YnI-IG9mIHJlc291cmNlID99Ojo6Ym94XG4gQiAtLT4gQyhDaGVtaWNhbCBTdWJzdGFuY2UpOjo6Ym94XG4gQiAtLT4gRChHZW5lKTo6OmJveFxuIEIgLS0-IEUoTW9sZWN1bGFyIEVudGl0eSk6Ojpib3hcbiBCIC0tPiBGKFByb3RlaW4pOjo6Ym94XG4gQiAtLT4gRyhTYW1wbGUpOjo6Ym94XG4gQiAtLT4gSChUYXhvbik6Ojpib3hcbiBDIC0tPiBJXG4gRCAtLT4gSVxuIEUgLS0-IElcbiBGIC0tPiBJXG4gRyAtLT4gSVxuIEggLS0-IEkoTWFya3VwIHRlbXBsYXRlKTo6OmJveFxuIEkgLS0-IHxFbWJlZCB0ZW1wbGF0ZSBpbiB3ZWJzaXRlfCBKKGZhOmZhLXNlYXJjaCBmYTpmYS1jb2cgZmE6ZmEtZmlnaHRlci1qZXQgU2NoZW1hLm9yZyBhdWdtZW50ZWQgSFRNTCBwYWdlKTo6OmJveFxuICBjbGFzc0RlZiBib3ggZm9udC1mYW1pbHk6YXZlbmlyLGZvbnQtc2l6ZToxNHB4LGZpbGw6IzJhOWZjOSxzdHJva2U6IzIyMixjb2xvcjojZmZmLHN0cm9rZS13aWR0aDoxcHhcbiBsaW5rU3R5bGUgMCwxLDIsMyw0LDUsNiw3LDgsOSwxMCwxMSwxMiwxMyBzdHJva2U6IzJhOWZjOSxzdHJva2Utd2lkdGg6MXB4LGNvbG9yOiMyYTlmYzksZm9udC1mYW1pbHk6YXZlbmlyOyIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In19)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiBBKEhUTUwgcGFnZSk6Ojpib3ggLS0-IHxDcmVhdGUgbWFya3VwIHRlbXBsYXRlfCBCe3doYXQgdHlwZSA8YnI-IG9mIHJlc291cmNlID99Ojo6Ym94XG4gQiAtLT4gQyhDaGVtaWNhbCBTdWJzdGFuY2UpOjo6Ym94XG4gQiAtLT4gRChHZW5lKTo6OmJveFxuIEIgLS0-IEUoTW9sZWN1bGFyIEVudGl0eSk6Ojpib3hcbiBCIC0tPiBGKFByb3RlaW4pOjo6Ym94XG4gQiAtLT4gRyhTYW1wbGUpOjo6Ym94XG4gQiAtLT4gSChUYXhvbik6Ojpib3hcbiBDIC0tPiBJXG4gRCAtLT4gSVxuIEUgLS0-IElcbiBGIC0tPiBJXG4gRyAtLT4gSVxuIEggLS0-IEkoTWFya3VwIHRlbXBsYXRlKTo6OmJveFxuIEkgLS0-IHxFbWJlZCB0ZW1wbGF0ZSBpbiB3ZWJzaXRlfCBKKGZhOmZhLXNlYXJjaCBmYTpmYS1jb2cgZmE6ZmEtZmlnaHRlci1qZXQgU2NoZW1hLm9yZyBhdWdtZW50ZWQgSFRNTCBwYWdlKTo6OmJveFxuICBjbGFzc0RlZiBib3ggZm9udC1mYW1pbHk6YXZlbmlyLGZvbnQtc2l6ZToxNHB4LGZpbGw6IzJhOWZjOSxzdHJva2U6IzIyMixjb2xvcjojZmZmLHN0cm9rZS13aWR0aDoxcHhcbiBsaW5rU3R5bGUgMCwxLDIsMyw0LDUsNiw3LDgsOSwxMCwxMSwxMiwxMyBzdHJva2U6IzJhOWZjOSxzdHJva2Utd2lkdGg6MXB4LGNvbG9yOiMyYTlmYzksZm9udC1mYW1pbHk6YXZlbmlyOyIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In19)
-->

<div class="mermaid">
graph TD
 A(HTML page):::box --> |Create markup template| B{what type <br> of resource ?}:::box
 B --> C(Chemical Substance):::box
 B --> D(Gene):::box
 B --> E(Molecular Entity):::box
 B --> F(Protein):::box
 B --> G(Sample):::box
 B --> H(Taxon):::box
 C --> I
 D --> I
 E --> I
 F --> I
 G --> I
 H --> I(Markup template):::box
 I --> |Embed template in website| J(fa:fa-search fa:fa-cog fa:fa-fighter-jet Schema.org augmented HTML page):::box
  classDef box font-family:avenir,font-size:14px,fill:#2a9fc9,stroke:#222,color:#fff,stroke-width:1px
 linkStyle 0,1,2,3,4,5,6,7,8,9,10,11,12,13 stroke:#2a9fc9,stroke-width:1px,color:#2a9fc9,font-family:avenir;
</div>



___

## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Findability | minimal | repeatable |
| Interoperability | minimal |  |

----

## Method

We will outline the steps for marking up a page in your site. As a specific example, we will use the Wikidata page for [BRCA1](https://www.wikidata.org/wiki/Q227339).

1. Identify a data page in your site for which you will develop markup

2. Open the [Bioschemas Generator](http://www.macs.hw.ac.uk/SWeL/BioschemasGenerator/)

   1.  Select the type of data page that you are marking up. In the example we will use `GeneRecord`. Here are the main data record profiles to choose from <sup>[1](#draft-profiles)</sup>. 

      - `ChemicalSubstanceRecord` for a page about a chemical substance composed of molecular entities

      - `GeneRecord` for a page about a gene

      - `MolecularEntityRecord` for a page about a single molecular entity

      - `ProteinRecord` for a page about a protein

      - `Sample` for a page about a biological sample
      
      - `Taxon` for a page about a taxon
      
   2. Enter the URL of the page in URL box, e.g. `https://www.wikidata.org/wiki/Q227339`

   3. Click on the `Show Form` button

   ![Bioschemas Generator start screen](BioschemasGenerator.png)

3. Complete the profile form with the data relevant for your page. Once completed, click on the `Generate Markup`  button

   - You should complete all *Minimum* properties and as many *Recommended* properties as possible. You can show/hide properties using the `Additional Properties` buttons.
   - The form defaults to the data type with the first alphabetical character, e.g. for `identifier` this defaults to `PropertyValue` but `Text` or `URL ` will be more appropriate in most cases
   - For XXXRecord pages, the first `identifier` property refers to the web page while the second `identifier` property refers to the chemical, gene, protein, ...
   - The right side of the screen gives examples for properties, where these have been provided by the Bioschemas profile authors. Click on the `Show` button to see the example for a specific property. Click on `Minimum`, `Recommended`, or `Optional` to expand/contract the section and see the properties contained at that marginality level

   ![Bioschemas Generator GeneRecord profile form](BioschemasGeneratorGeneRecordForm.png)
   
4. You should now see the generated markup in `JSON-LD` format. You can click on the `Microdata` and `RDFa` tabs to see the same content rendered in the different formats. However, we recommend the use of `JSON-LD`. For our Wikidata example, we get the following markup

     ```json
     <script type="application/ld+json" >
     {
       "@context": "http://schema.org",
       "@id": "https://www.wikidata.org/wiki/Q227339",
       "@type": "DataRecord",
       "dct:conformsTo": "https://bioschemas.org/profiles/DataRecord/0.2-DRAFT-2019_06_14",
       "identifier": "https://www.wikidata.org/wiki/Q227339",
       "mainEntity": {
         "@type": "Gene",
         "dct:conformsTo": "https://bioschemas.org/profiles/Gene/0.7-RELEASE",
         "identifier": "Q227339",
         "description": "protein-coding gene in the species Homo sapiens",
         "encodesBioChemEntity": {
           "@type": "BioChemEntity",
           "@id": "https://www.wikidata.org/wiki/Q17487737"
         },
         "isPartOfBioChemEntity": {
           "@type": "BioChemEntity",
           "@id": "https://www.wikidata.org/wiki/Q220677"
         },
         "url": "https://www.wikidata.org/wiki/Q227339",
         "alternateName": [
           "breast cancer 1, early onset",
           "BRCAI",
     			"BRCC1",
     			"BROVCA1",
     			"IRIS",
     			"PNCA4",
     			"PPP1R53",
     			"PSCP",
     			"RNF53",
     			"FANCS",
     			"breast cancer 1",
     			"BRCA1, DNA repair associated",
     			"BRCA1 DNA repair associated"
         ],
         "image": {
           "@type": "ImageObject",
           "@id": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Protein_BRCA1_PDB_1jm7.png/220px-Protein_BRCA1_PDB_1jm7.png"
         },
         "taxonomicRange": {
           "@type": "Taxon",
           "@id": "https://www.wikidata.org/wiki/Q15978631"
         },
         "sameAs": [
           "https://meshb.nlm.nih.gov/#/record/ui?ui=D019398",
           "https://www.ncbi.nlm.nih.gov/nuccore/NR_027676",
           "http://identifiers.org/ensembl/ENSG00000012048",
           "https://www.ncbi.nlm.nih.gov/gene/672"
         ]
       },
       "sameAs": [
         "http://identifiers.org/ncbigene/672"
       ]
     }
     </script >
     ```

5. Download or copy and paste the generated markup

6. Make adjustments for any bits that could not be properly entered through the form. 

     For example, for our generated markup we would change

     ```json
     "encodesBioChemEntity": {
           "@type": "BioChemEntity",
           "@id": "https://www.wikidata.org/wiki/Q17487737"
         },
     ```

     to

     ```json
     "encodesBioChemEntity": {
           "@type": "Protein",
           "@id": "https://www.wikidata.org/wiki/Q17487737"
         },
     ```

     You can test that your JSON-LD is valid syntax, and visualise your markup using the [JSON-LD Playground](https://json-ld.org/playground/).

7. Once you are happy with your markup, include the `JSON-LD`, script tags and all, at the bottom of your HTML page template. Make sure that this is before the closing `</html>` tag

8. Replace the values in your markup with variables that your web page templating system will replace with values from your database. For example, the follow snippet uses variables of the form `%%%PAGEURL%%%`

     ```json
     <script type="application/ld+json" >
     {
       "@context": "http://schema.org",
       "@id": "%%%PAGEURL%%%",
       "@type": "DataRecord",
       "dct:conformsTo": "https://bioschemas.org/profiles/DataRecord/0.2-DRAFT-2019_06_14",
       "identifier": "%%%PAGEURL%%%",
       "mainEntity": {
         "@type": "Gene",
         "dct:conformsTo": "https://bioschemas.org/profiles/Gene/0.7-RELEASE",
         "identifier": "%%%ACCESSIONNUMBER%%%",
         "description": "%%%DESCRIPTION%%%",
         ...
     }
     ```

     

Your site should now generate data pages with embedded markup. 

You should complete this process for each different type of data that you include in your site, e.g. ChEMBL would have `MolecularEntity` markup on their chemical pages and `Protein` markup on their target pages so would need to complete this process twice.

Once you have deployed this on your web server, you can test it with the [Bioschemas Validator](http://www.macs.hw.ac.uk/SWeL/BioschemasValidator/) which scrapes the markup from your page and allows you to test it against various Bioschemas profiles<sup>[2](#bioschemas-validator)</sup>.

----

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [text annotation](http://edamontology.org/operation_3778)  | [Bioschemas](https://fairsharing.org/FAIRsharing.20sbr9) | [annotated text](http://edamontology.org/data_3779)  |
| [validation](http://edamontology.org/operation_2428) | [schema.org](https://fairsharing.org/FAIRsharing.hzdzq8) | [report](http://edamontology.org/data_2048) |


## Table of Data Standards

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| [JSON-LD](http://edamontology.org/format_3749)  | [Bioschemas](https://fairsharing.org/FAIRsharing.20sbr9) | [RDF](http://edamontology.org/data_2353)  |
| [HTML](http://edamontology.org/format_2331) | | |
___

## Authors:

| Name          | Affiliation                                                  | orcid                                                        | CrediT role              |
| :------------ | :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------- |
| Alasdair Gray | Bioschemas Community Lead / Heriot-Watt Unviersity / ELIXIR-UK | [0000-0002-5711-4872](https://orcid.org/0000-0002-5711-4872) | Writing - Original Draft |
| Leyla Garcia | Bioschemas Community / ZB MED Information Centre for life sciences, Knowledge Management Group | [0000-0003-3986-0510](https://orcid.org/0000-0003-3986-0510) | External review |

___

## Footnotes

<a name="draft-profiles">1</a>: If you do not see your data type listed, tick the `Include Draft Profiles` to see if there is a draft profile for your data type. Otherwise contact the Bioschemas community to suggest development of a new profile.  
<a name="bioschemas-validator">2</a>: The Bioschemas Validator is currently in an early alpha release and does not include all the profiles.

___

## License:

This page is released under the Creative Commons 4.0 BY license.

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png" height="20"/></a>

