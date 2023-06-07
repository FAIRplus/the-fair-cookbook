(fcb-find-bs-data)=
# Marking up Data pages with Schema.org & Bioschemas for SEO


````{panels_fairplus}
:identifier_text: FCB011
:identifier_link: 'https://w3id.org/faircookbook/FCB011'
:difficulty_level: 2
:recipe_type: guidance
:reading_time_minutes: 10
:intended_audience: software_developer, data_scientist  
:maturity_level: 1
:maturity_indicator: 13, 14
:has_executable_code: nope
:recipe_name: Marking up Data pages with Schema.org & Bioschemas for SEO
```` 

## Main Objectives

The main purpose of this recipe is:

> To markup a webpage representing a data record with `Bioschemas` compliant markup.


```{tabbed} FAIRification Objectives, Inputs and Outputs
| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [text annotation](https://edamontology.org/operation_3778)  | [Bioschemas](https://fairsharing.org/FAIRsharing.20sbr9) | [annotated text](https://edamontology.org/data_3779)  |
| [validation](https://edamontology.org/operation_2428) | [schema.org](https://fairsharing.org/FAIRsharing.hzdzq8) | [report](https://edamontology.org/data_2048) |
```
```{tabbed} Table of Data Standards
| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| [JSON-LD](https://edamontology.org/format_3749)  | [Bioschemas](https://fairsharing.org/FAIRsharing.20sbr9) | [RDF](https://edamontology.org/data_2353)  |
| [HTML](https://edamontology.org/format_2331) | | |
```

---


## Graphical Overview


````{dropdown} 
:open:
```{figure} ./bs-data-mermaid.png
---
width: 800px
name: 
alt: The process of annotated a webpage with Bioschemas markup to support machine processing of the page
---
The process of annotated a webpage with Bioschemas markup to support machine processing of the page.
```
````

---

## Method

We will outline the steps for embedding machine processable mark up within a web page in your site. As a specific example, we will use the Wikidata page for [BRCA1](https://www.wikidata.org/wiki/Q227339).

1. Identify a data page in your site for which you will develop markup

2. Open the [Bioschemas Generator](https://www.macs.hw.ac.uk/SWeL/BioschemasGenerator/)

   1.  Select the type of data page that you are marking up, i.e. the primary subject of the page. In the example we will use `Gene`. Here are the Bioschemas [profiles](https://bioschemas.org/profiles/) that you can choose from<sup>[1](#draft-profiles)</sup>. 

        - `ChemicalSubstance` for a page about a chemical substance composed of molecular entities

        - `Gene` for a page about a gene

        - `MolecularEntity` for a page about a single molecular entity

        - `Protein` for a page about a protein

        - `BioSample` for a page about a biological sample
        
        - `Taxon` for a page about a taxon
      
   2. Enter the URL of the page in URL box, e.g. `https://www.wikidata.org/wiki/Q227339`. Note that this URL will be used as the identifier for the resource being described in the markup.

   3. Click on the `Show Form` button
    
    ````{dropdown} 
    :open:
    ```{figure} BioschemasGenerator.png
    ---
    name: bioschemas-generator-start-screen-2
    alt: Bioschemas Generator start screen.
    
    ---
    Bioschemas Generator start screen.
    ```
    ````
    
3. Complete the profile form with the data relevant for your page. Once completed, click on the `Generate Markup`  button

   - You should complete all *Minimum* properties and as many *Recommended* properties as possible. You can show/hide properties using the `Additional Properties` buttons.
   - The form defaults to the data type with the first alphabetical character, e.g. for `identifier` this defaults to `PropertyValue` but `Text` or `URL ` will be more appropriate in most cases
   - The right side of the screen gives examples for properties, where these have been provided by the Bioschemas profile authors. Click on the `Show` button to see the example for a specific property. Click on `Minimum`, `Recommended`, or `Optional` to expand/contract the section and see the properties contained at that marginality level
    
    ````{dropdown} 
    :open:
    ```{figure} BioschemasGeneratorGeneForm.png
    ---
    height: 550px
    name: Bioschemas Generator Gene profile form
    alt: Bioschemas Generator Gene profile form
    ---
    Bioschemas Generator Gene profile form.
    ```
    ````
    
4. You should now see the generated markup in `JSON-LD` format. You can click on the `Microdata` and `RDFa` tabs to see the same content rendered in the different formats. However, we recommend the use of `JSON-LD`. For our Wikidata example, we get the following markup

    ```html
    <script type="application/ld+json" >
    {
      "@context": "https://schema.org",
      "@id": "https://www.wikidata.org/wiki/Q227339",
      "@type": "Gene",
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
      "dct:conformsTo": "https://bioschemas.org/profiles/Gene/0.7-RELEASE",
      "description": "protein-coding gene in the species Homo sapiens",
      "encodesBioChemEntity": {
        "@type": "BioChemEntity",
        "@id": "https://www.wikidata.org/wiki/Q17487737"
      },
      "identifier": "https://www.wikidata.org/wiki/Q227339",
      "identifier": "Q227339",
      "image": {
        "@type": "ImageObject",
        "@id": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Protein_BRCA1_PDB_1jm7.png/220px-Protein_BRCA1_PDB_1jm7.png"
      },
      "isPartOfBioChemEntity": {
        "@type": "BioChemEntity",
        "@id": "https://www.wikidata.org/wiki/Q220677"
      },
      "name": "BRCA1", 
      "sameAs": [
        "https://meshb.nlm.nih.gov/#/record/ui?ui=D019398",
        "https://www.ncbi.nlm.nih.gov/nuccore/NR_027676",
        "https://identifiers.org/ensembl/ENSG00000012048",
        "https://www.ncbi.nlm.nih.gov/gene/672",
        "https://identifiers.org/ncbigene/672"
      ],
      "taxonomicRange": {
        "@type": "Taxon",
        "@id": "https://www.wikidata.org/wiki/Q15978631"
      },
      "url": "https://www.wikidata.org/wiki/Q227339"
    }
    </script >
    ```
    
5. Download or copy and paste the generated markup
    
6. Make adjustments for any bits that could not be properly entered through the form. 

     For example, for our generated markup we would change

    ```
    "encodesBioChemEntity": {
      "@type": "BioChemEntity",
      "@id": "https://www.wikidata.org/wiki/Q17487737"
    },
    ```

    to

    ```
    "encodesBioChemEntity": {
      "@type": "Protein",
      "@id": "https://www.wikidata.org/wiki/Q17487737"
    },
    ```

    You can test that your JSON-LD is valid syntax, and visualise your markup using the [JSON-LD Playground](https://json-ld.org/playground/).

    
7. Once you are happy with your markup, include the `JSON-LD`, script tags and all, at the bottom of your HTML page template. Make sure that this is before the closing `</html>` tag
    
   1. Replace the values in your markup with variables that your web page templating system will replace with values from your database. For example, the follow snippet uses variables of the form `%%%PAGEURL%%%`

       ```html
       <script type="application/ld+json" >
       {
         "@context": "https://schema.org",
         "@id": "%%%PAGEURL%%%",
         "@type": "Gene",
         "dct:conformsTo": "https://bioschemas.org/profiles/Gene/0.7-RELEASE",
         "identifier": "%%%PAGEURL%%%",
         "description": "%%%DESCRIPTION%%%",
         ...
       }
       ```
   
       Your site should now generate data pages with embedded markup.

       You should complete this process for each different type of data that you include in your site, e.g. ChEMBL would
       have `MolecularEntity` markup on their chemical pages and `Protein` markup on their target pages so would need to 
       complete this process twice.
    
       Once you have deployed this on your web server, you can test it with the [Bioschemas Validator](https://www.macs.hw.ac.uk/SWeL/BioschemasValidator/) which scrapes the markup from your page and allows you to test it against various Bioschemas profiles<sup>[2](#bioschemas-validator)</sup>.

---


## Conclusion


### What to read next?

- {ref}`fcb-find-bs-catalog`
- {ref}`fcb-find-bs-dataset`

````{rdmkit_panel}
````






## References
````{dropdown} **References**
<a name="draft-profiles">1</a>: If you do not see your data type listed, tick the `Include Draft Profiles` to see if there is a draft profile for your data type. Otherwise contact the Bioschemas community to suggest development of a new profile.  
<a name="bioschemas-validator">2</a>: The Bioschemas Validator is currently in an early alpha release and does not include all the profiles.
````


## Authors

````{authors_fairplus}
Alasdair: Writing - Original Draft
Leyla: Writing - Review & Editing
Philippe: Writing - Review & Editing
````


## License

````{license_fairplus}
CC-BY-4.0
````

