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

> To markup a webpage representing a data record with `Bioschemas(URL_TO_INSERT_RECORD https://bioschemas.org)(URL_TO_INSERT_RECORD https://bioschemas.org)` compliant markup.


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
alt: The process of annotated a webpage with Bioschemas(URL_TO_INSERT_RECORD https://bioschemas.org)(URL_TO_INSERT_RECORD https://bioschemas.org) markup to support machine processing of the page
---
The process of annotated a webpage with Bioschemas(URL_TO_INSERT_RECORD https://bioschemas.org)(URL_TO_INSERT_RECORD https://bioschemas.org) markup to support machine processing of the page.
```
````

---

## Method

We will outline the steps for embedding machine processable mark up within a web page in your site. As a specific example, we will use the Wikidata(URL_TO_INSERT_RECORD http://wikidata.org/)(URL_TO_INSERT_RECORD http://wikidata.org/) page for [BRCA1](https://www.wikidata.org(URL_TO_INSERT_RECORD http://wikidata.org/)/wiki/Q227339).

1. Identify a data page in your site for which you will develop markup

2. Open the [Bioschemas(URL_TO_INSERT_RECORD https://bioschemas.org)(URL_TO_INSERT_RECORD https://bioschemas.org) Generator](https://www.macs.hw.ac.uk/SWeL/BioschemasGenerator/)

   1.  Select the type of data page that you are marking up, i.e. the primary subject of the page. In the example we will use `Gene`. Here are the Bioschemas(URL_TO_INSERT_RECORD https://bioschemas.org)(URL_TO_INSERT_RECORD https://bioschemas.org) [profiles](https://bioschemas.org(URL_TO_INSERT_RECORD https://bioschemas.org)/profiles/) that you can choose from<sup>[1](#draft-profiles)</sup>. 

        - `ChemicalSubstance` for a page about a chemical substance composed of molecular entities

        - `Gene` for a page about a gene

        - `MolecularEntity` for a page about a single molecular entity

        - `Protein(URL_TO_INSERT_RECORD http://www.ncbi.nlm.nih.gov/protein)` for a page about a protein

        - `BioSample(URL_TO_INSERT_RECORD https://www.ncbi.nlm.nih.gov/biosample)` for a page about a biological sample
        
        - `Taxon` for a page about a taxon
      
   2. Enter the URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630) of the page in URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630) box, e.g. `https://www.wikidata.org(URL_TO_INSERT_RECORD http://wikidata.org/)/wiki/Q227339`. Note that this URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630) will be used as the identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) for the resource being described in the markup.

   3. Click on the `Show Form` button
    
    ````{dropdown} 
    :open:
    ```{figure} Bioschemas(URL_TO_INSERT_RECORD https://bioschemas.org)(URL_TO_INSERT_RECORD https://bioschemas.org)Generator.png
    ---
    name: bioschemas(URL_TO_INSERT_RECORD https://bioschemas.org)-generator-start-screen-2
    alt: Bioschemas(URL_TO_INSERT_RECORD https://bioschemas.org)(URL_TO_INSERT_RECORD https://bioschemas.org) Generator start screen.
    
    ---
    Bioschemas(URL_TO_INSERT_RECORD https://bioschemas.org)(URL_TO_INSERT_RECORD https://bioschemas.org) Generator start screen.
    ```
    ````
    
3. Complete the profile form with the data relevant for your page. Once completed, click on the `Generate Markup`  button

   - You should complete all *Minimum* properties and as many *Recommended* properties as possible. You can show/hide properties using the `Additional Properties` buttons.
   - The form defaults to the data type with the first alphabetical character, e.g. for `identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)` this defaults to `PropertyValue` but `Text` or `URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630) ` will be more appropriate in most cases
   - The right side of the screen gives examples for properties, where these have been provided by the Bioschemas(URL_TO_INSERT_RECORD https://bioschemas.org)(URL_TO_INSERT_RECORD https://bioschemas.org) profile authors. Click on the `Show` button to see the example for a specific property. Click on `Minimum`, `Recommended`, or `Optional` to expand/contract the section and see the properties contained at that marginality level
    
    ````{dropdown} 
    :open:
    ```{figure} Bioschemas(URL_TO_INSERT_RECORD https://bioschemas.org)(URL_TO_INSERT_RECORD https://bioschemas.org)GeneratorGeneForm.png
    ---
    height: 550px
    name: Bioschemas(URL_TO_INSERT_RECORD https://bioschemas.org)(URL_TO_INSERT_RECORD https://bioschemas.org) Generator Gene profile form
    alt: Bioschemas(URL_TO_INSERT_RECORD https://bioschemas.org)(URL_TO_INSERT_RECORD https://bioschemas.org) Generator Gene profile form
    ---
    Bioschemas(URL_TO_INSERT_RECORD https://bioschemas.org)(URL_TO_INSERT_RECORD https://bioschemas.org) Generator Gene profile form.
    ```
    ````
    
4. You should now see the generated markup in `JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259)-LD(URL_TO_INSERT_RECORD https://json-ld.org/spec/latest/json-ld/)` format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format). You can click on the `Microdata` and `RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/)a(URL_TO_INSERT_RECORD https://www.w3.org/TR/rdfa-primer/)` tabs to see the same content rendered in the different format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s. However, we recommend the use of `JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259)-LD(URL_TO_INSERT_RECORD https://json-ld.org/spec/latest/json-ld/)`. For our Wikidata(URL_TO_INSERT_RECORD http://wikidata.org/)(URL_TO_INSERT_RECORD http://wikidata.org/) example, we get the following markup

    ```html
    <script type="application/ld+json" >
    {
      "@context": "https://schema.org(URL_TO_INSERT_RECORD http://schema.org/)",
      "@id": "https://www.wikidata.org(URL_TO_INSERT_RECORD http://wikidata.org/)/wiki/Q227339",
      "@type": "Gene",
      "alternateName": [
        "breast cancer 1, early onset",
        "BRCAI",
        "BRCC1",
        "BRO(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/BRO)(URL_TO_INSERT_RECORD https://w3id.org/ro/)VCA1",
        "IRIS(URL_TO_INSERT_RECORD https://web.archive.org/web/20170707033254/http://www.researcherid.com/resources/html/help_upload.htm)(URL_TO_INSERT_RECORD https://www.iris-database.org)",
        "PNCA4",
        "PP(URL_TO_INSERT_RECORD https://bitbucket.org/PlantExpAssay/ontology)P1R53",
        "PSCP(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/complexportal/)",
        "RNF53",
        "FANCS",
        "breast cancer 1",
        "BRCA1, DNA repair associated",
        "BRCA1 DNA repair associated"
      ],
      "dct:conformsTo": "https://bioschemas.org(URL_TO_INSERT_RECORD https://bioschemas.org)/profiles/Gene/0.7-RELEASE",
      "description": "protein-coding gene in the species Homo sapiens",
      "encodesBioChemEntity": {
        "@type": "BioChemEntity",
        "@id": "https://www.wikidata.org(URL_TO_INSERT_RECORD http://wikidata.org/)/wiki/Q17487737"
      },
      "identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)": "https://www.wikidata.org(URL_TO_INSERT_RECORD http://wikidata.org/)/wiki/Q227339",
      "identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)": "Q227339",
      "image": {
        "@type": "ImageObject",
        "@id": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Protein_BRCA1_PDB_1jm7.png/220px-Protein_BRCA1_PDB_1jm7.png"
      },
      "isPartOfBioChemEntity": {
        "@type": "BioChemEntity",
        "@id": "https://www.wikidata.org(URL_TO_INSERT_RECORD http://wikidata.org/)/wiki/Q220677"
      },
      "name": "BRCA1", 
      "sameAs": [
        "https://meshb.nlm.nih.gov/#/record/ui?ui=D019398",
        "https://www.ncbi.nlm.nih.gov/nuccore/NR_027676",
        "https://identifiers.org/ensembl/ENSG00000012048",
        "https://www.ncbi.nlm.nih.gov/gene(URL_TO_INSERT_RECORD https://www.ncbi.nlm.nih.gov/gene)/672",
        "https://identifiers.org/ncbigene/672"
      ],
      "taxonomicRange": {
        "@type": "Taxon",
        "@id": "https://www.wikidata.org(URL_TO_INSERT_RECORD http://wikidata.org/)/wiki/Q15978631"
      },
      "url": "https://www.wikidata.org(URL_TO_INSERT_RECORD http://wikidata.org/)/wiki/Q227339"
    }
    </script >
    ```
    
5. Download or copy and paste the generated markup
    
6. Make adjustments for any bits that could not be properly entered through the form. 

     For example, for our generated markup we would change

    ```
    "encodesBioChemEntity": {
      "@type": "BioChemEntity",
      "@id": "https://www.wikidata.org(URL_TO_INSERT_RECORD http://wikidata.org/)/wiki/Q17487737"
    },
    ```

    to

    ```
    "encodesBioChemEntity": {
      "@type": "Protein(URL_TO_INSERT_RECORD http://www.ncbi.nlm.nih.gov/protein)",
      "@id": "https://www.wikidata.org(URL_TO_INSERT_RECORD http://wikidata.org/)/wiki/Q17487737"
    },
    ```

    You can test that your JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259)-LD(URL_TO_INSERT_RECORD https://json-ld.org/spec/latest/json-ld/) is valid syntax, and visualise your markup using the [JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259)-LD(URL_TO_INSERT_RECORD https://json-ld.org/spec/latest/json-ld/) Playground](https://json-ld.org/playground/).

    
7. Once you are happy with your markup, include the `JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259)-LD(URL_TO_INSERT_RECORD https://json-ld.org/spec/latest/json-ld/)`, script tags and all, at the bottom of your HTML(URL_TO_INSERT_RECORD https://www.w3.org/TR/html53/) page template. Make sure that this is before the closing `</html>` tag
    
   1. Replace the values in your markup with variables that your web page templating system will replace with values from your database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database). For example, the follow snippet uses variables of the form `%%%PAGEURL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)%%%`

       ```html
       <script type="application/ld+json" >
       {
         "@context": "https://schema.org(URL_TO_INSERT_RECORD http://schema.org/)",
         "@id": "%%%PAGEURL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)%%%",
         "@type": "Gene",
         "dct:conformsTo": "https://bioschemas.org(URL_TO_INSERT_RECORD https://bioschemas.org)/profiles/Gene/0.7-RELEASE",
         "identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)": "%%%PAGEURL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)%%%",
         "description": "%%%DESCRIPTION%%%",
         ...
       }
       ```
   
       Your site should now generate data pages with embedded markup.

       You should complete this process for each different type of data that you include in your site, e.g. ChEMB(URL_TO_INSERT_RECORD http://www.Metabase.net)L(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/chembl)(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/chembl) would
       have `MolecularEntity` markup on their chemical pages and `Protein(URL_TO_INSERT_RECORD http://www.ncbi.nlm.nih.gov/protein)` markup on their target pages so would need to 
       complete this process twice.
    
       Once you have deployed this on your web server, you can test it with the [Bioschemas(URL_TO_INSERT_RECORD https://bioschemas.org)(URL_TO_INSERT_RECORD https://bioschemas.org) Validator](https://www.macs.hw.ac.uk/SWeL/BioschemasValidator/) which scrapes the markup from your page and allows you to test it against various Bioschemas(URL_TO_INSERT_RECORD https://bioschemas.org)(URL_TO_INSERT_RECORD https://bioschemas.org) profiles<sup>[2](#bioschemas(URL_TO_INSERT_RECORD https://bioschemas.org)-validator)</sup>.

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

