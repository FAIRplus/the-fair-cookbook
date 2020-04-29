# Findability: Data Page Markup with Bioschemas 

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

> To markup a webpage representing a data record with Bioschemas compliant markup.

___


## Graphical Overview of the FAIRification Recipe Objectives

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiBBW0hUTUwgcGFnZV0gLS0-IHxDcmVhdGUgbWFya3VwIHRlbXBsYXRlfCBCe3doYXQgdHlwZSBvZiByZXNvdXJjZT99XG4gQiAtLT4gQ1tDaGVtaWNhbCBTdWJzdGFuY2VdXG4gQiAtLT4gRFtHZW5lXVxuIEIgLS0-IEVbTW9sZWN1bGFyIEVudGl0eV1cbiBCIC0tPiBGW1Byb3RlaW5dXG4gQiAtLT4gR1tTYW1wbGVdXG4gQiAtLT4gSFtUYXhvbl1cbiBDIC0tPiBJXG4gRCAtLT4gSVxuIEUgLS0-IElcbiBGIC0tPiBJXG4gRyAtLT4gSVxuIEggLS0-IEkoTWFya3VwIHRlbXBsYXRlKVxuIEkgLS0-IHxFbWJlZCB0ZW1wbGF0ZSBpbiB3ZWJzaXRlfCBKW2ZhOmZhLXNlYXJjaCBmYTpmYS1jb2cgZmE6ZmEtZmlnaHRlci1qZXQgU2NoZW1hLm9yZyBhdWdtZW50ZWQgSFRNTCBwYWdlXSIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiBBW0hUTUwgcGFnZV0gLS0-IHxDcmVhdGUgbWFya3VwIHRlbXBsYXRlfCBCe3doYXQgdHlwZSBvZiByZXNvdXJjZT99XG4gQiAtLT4gQ1tDaGVtaWNhbCBTdWJzdGFuY2VdXG4gQiAtLT4gRFtHZW5lXVxuIEIgLS0-IEVbTW9sZWN1bGFyIEVudGl0eV1cbiBCIC0tPiBGW1Byb3RlaW5dXG4gQiAtLT4gR1tTYW1wbGVdXG4gQiAtLT4gSFtUYXhvbl1cbiBDIC0tPiBJXG4gRCAtLT4gSVxuIEUgLS0-IElcbiBGIC0tPiBJXG4gRyAtLT4gSVxuIEggLS0-IEkoTWFya3VwIHRlbXBsYXRlKVxuIEkgLS0-IHxFbWJlZCB0ZW1wbGF0ZSBpbiB3ZWJzaXRlfCBKW2ZhOmZhLXNlYXJjaCBmYTpmYS1jb2cgZmE6ZmEtZmlnaHRlci1qZXQgU2NoZW1hLm9yZyBhdWdtZW50ZWQgSFRNTCBwYWdlXSIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

```
graph TD
 A[HTML page] --> |Create markup template| B{what type of resource?}
 B --> C[Chemical Substance]
 B --> D[Gene]
 B --> E[Molecular Entity]
 B --> F[Protein]
 B --> G[Sample]
 B --> H[Taxon]
 C --> I
 D --> I
 E --> I
 F --> I
 G --> I
 H --> I(Markup template)
 I --> |Embed template in website| J[fa:fa-search fa:fa-cog fa:fa-fighter-jet Schema.org augmented HTML page]
```



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

Once you have deployed this on your web server, you can test it with the [Bioschemas Validator](http://www.macs.hw.ac.uk/SWeL/BioschemasValidator/) which scapes the markup from your page and allows you to test it against various Bioschemas profiles<sup>[2](#bioschemas-validator)</sup>.

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

___


## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>

## Footnotes

<a name="draft-profiles">1</a>: If you do not see your data type listed, tick the `Include Draft Profiles` to see if there is a draft profile for your data type. Otherwise contact the Bioschemas community to suggest development of a new profile.  
<a name="bioschemas-validator">2</a>: The Bioschemas Validator is currently in an early alpha release and does not include all the profiles.