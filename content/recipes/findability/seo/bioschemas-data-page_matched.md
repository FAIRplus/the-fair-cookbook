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

> To markup a webpage representing a data record with `Bioschemas (URL_TO_INSERT_RECORD_1958 https://fairsharing.org/3517) ` compliant markup.


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
alt: The process of annotated a webpage with Bioschemas (URL_TO_INSERT_RECORD_1959 https://fairsharing.org/3517)  markup to support machine processing of the page
---
The process of annotated a webpage with Bioschemas (URL_TO_INSERT_RECORD_1960 https://fairsharing.org/3517)  markup to support machine processing of the page.
```
````

---

## Method

We will outline the steps for embedding machine processable mark up within a web page in your site. As a specific example, we will use the Wikidata (URL_TO_INSERT_RECORD_1961 https://fairsharing.org/FAIRsharing.6s749p)  page for [BRCA1](https://www.wikidata.org (URL_TO_INSERT_RECORD_1962 https://fairsharing.org/FAIRsharing.6s749p) /wiki/Q227339).

1. Identify a data page in your site for which you will develop markup

2. Open the [Bioschemas (URL_TO_INSERT_RECORD_1963 https://fairsharing.org/3517)  Generator](https://www.macs.hw.ac.uk/SWeL/BioschemasGenerator/)

   1.  Select the type of data page that you are marking up, i.e. the primary subject of the page. In the example we will use `Gene`. Here are the Bioschemas (URL_TO_INSERT_RECORD_1964 https://fairsharing.org/3517)  [profiles](https://bioschemas.org (URL_TO_INSERT_RECORD_1965 https://fairsharing.org/3517) /profiles/) that you can choose from<sup>[1](#draft-profiles)</sup>. 

        - `ChemicalSubstance` for a page about a chemical substance composed of molecular entities

        - `Gene` for a page about a gene

        - `MolecularEntity` for a page about a single molecular entity

        - `Protein (URL_TO_INSERT_RECORD_1966 https://fairsharing.org/FAIRsharing.rtndct) ` for a page about a protein

        - `BioSample (URL_TO_INSERT_RECORD_1967 https://fairsharing.org/FAIRsharing.qr6pqk) ` for a page about a biological sample
        
        - `Taxon` for a page about a taxon
      
   2. Enter the URL (URL_TO_INSERT_RECORD_1970 https://fairsharing.org/FAIRsharing.9d38e2)  of the page in URL (URL_TO_INSERT_RECORD_1971 https://fairsharing.org/FAIRsharing.9d38e2)  box, e.g. `https://www.wikidata.org (URL_TO_INSERT_RECORD_1969 https://fairsharing.org/FAIRsharing.6s749p) /wiki/Q227339`. Note that this URL (URL_TO_INSERT_RECORD_1972 https://fairsharing.org/FAIRsharing.9d38e2)  will be used as the identifier (URL_TO_INSERT_TERM_1968 https://fairsharing.org/search?recordType=identifier_schema)  for the resource being described in the markup.

   3. Click on the `Show Form` button
    
    ````{dropdown} 
    :open:
    ```{figure} Bioschemas (URL_TO_INSERT_RECORD_1973 https://fairsharing.org/3517) Generator.png
    ---
    name: bioschemas (URL_TO_INSERT_RECORD_1974 https://fairsharing.org/3517) -generator-start-screen-2
    alt: Bioschemas (URL_TO_INSERT_RECORD_1975 https://fairsharing.org/3517)  Generator start screen.
    
    ---
    Bioschemas (URL_TO_INSERT_RECORD_1976 https://fairsharing.org/3517)  Generator start screen.
    ```
    ````
    
3. Complete the profile form with the data relevant for your page. Once completed, click on the `Generate Markup`  button

   - You should complete all *Minimum* properties and as many *Recommended* properties as possible. You can show/hide properties using the `Additional Properties` buttons.
   - The form defaults to the data type with the first alphabetical character, e.g. for `identifier (URL_TO_INSERT_TERM_1977 https://fairsharing.org/search?recordType=identifier_schema) ` this defaults to `PropertyValue` but `Text` or `URL ` will be more appropriate in most cases
   - The right side of the screen gives examples for properties, where these have been provided by the Bioschemas (URL_TO_INSERT_RECORD_1978 https://fairsharing.org/3517)  profile authors. Click on the `Show` button to see the example for a specific property. Click on `Minimum`, `Recommended`, or `Optional` to expand/contract the section and see the properties contained at that marginality level
    
    ````{dropdown} 
    :open:
    ```{figure} Bioschemas (URL_TO_INSERT_RECORD_1979 https://fairsharing.org/3517) GeneratorGeneForm.png
    ---
    height: 550px
    name: Bioschemas (URL_TO_INSERT_RECORD_1980 https://fairsharing.org/3517)  Generator Gene profile form
    alt: Bioschemas (URL_TO_INSERT_RECORD_1981 https://fairsharing.org/3517)  Generator Gene profile form
    ---
    Bioschemas (URL_TO_INSERT_RECORD_1982 https://fairsharing.org/3517)  Generator Gene profile form.
    ```
    ````
    
4. You should now see the generated markup in `JSON (URL_TO_INSERT_RECORD_1986 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_1989 https://fairsharing.org/FAIRsharing.8f9bbb) ` format (URL_TO_INSERT_TERM_1983 https://fairsharing.org/search?recordType=model_and_format) . You can click on the `Microdata` and `RDFa (URL_TO_INSERT_RECORD_1988 https://fairsharing.org/663) ` tabs to see the same content rendered in the different format (URL_TO_INSERT_TERM_1984 https://fairsharing.org/search?recordType=model_and_format) s. However, we recommend the use of `JSON (URL_TO_INSERT_RECORD_1987 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_1990 https://fairsharing.org/FAIRsharing.8f9bbb) `. For our Wikidata (URL_TO_INSERT_RECORD_1985 https://fairsharing.org/FAIRsharing.6s749p)  example, we get the following markup

    ```html
    <script type="application/ld+json" >
    {
      "@context": "https://schema.org (URL_TO_INSERT_RECORD_1991 https://fairsharing.org/FAIRsharing.hzdzq8) ",
      "@id": "https://www.wikidata.org (URL_TO_INSERT_RECORD_1992 https://fairsharing.org/FAIRsharing.6s749p) /wiki/Q227339",
      "@type": "Gene",
      "alternateName": [
        "breast cancer 1, early onset",
        "BRCAI",
        "BRCC1",
        "BROVCA1",
        "IRIS (URL_TO_INSERT_RECORD_1993 https://fairsharing.org/FAIRsharing.e20b79) ",
        "PNCA4",
        "PPP1R53",
        "PSCP",
        "RNF53",
        "FANCS",
        "breast cancer 1",
        "BRCA1, DNA repair associated",
        "BRCA1 DNA repair associated"
      ],
      "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_1994 https://fairsharing.org/3517) /profiles/Gene/0.7-RELEASE",
      "description": "protein-coding gene in the species Homo sapiens",
      "encodesBioChemEntity": {
        "@type": "BioChemEntity",
        "@id": "https://www.wikidata.org (URL_TO_INSERT_RECORD_1995 https://fairsharing.org/FAIRsharing.6s749p) /wiki/Q17487737"
      },
      "identifier (URL_TO_INSERT_TERM_1996 https://fairsharing.org/search?recordType=identifier_schema) ": "https://www.wikidata.org (URL_TO_INSERT_RECORD_1997 https://fairsharing.org/FAIRsharing.6s749p) /wiki/Q227339",
      "identifier (URL_TO_INSERT_TERM_1998 https://fairsharing.org/search?recordType=identifier_schema) ": "Q227339",
      "image": {
        "@type": "ImageObject",
        "@id": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Protein_BRCA1_PDB_1jm7.png/220px-Protein_BRCA1_PDB_1jm7.png"
      },
      "isPartOfBioChemEntity": {
        "@type": "BioChemEntity",
        "@id": "https://www.wikidata.org (URL_TO_INSERT_RECORD_1999 https://fairsharing.org/FAIRsharing.6s749p) /wiki/Q220677"
      },
      "name": "BRCA1", 
      "sameAs": [
        "https://meshb.nlm.nih.gov/#/record/ui?ui=D019398",
        "https://www.ncbi.nlm.nih.gov/nuccore/NR_027676",
        "https://identifiers.org/ensembl/ENSG00000012048",
        "https://www.ncbi.nlm.nih.gov/gene (URL_TO_INSERT_RECORD_2000 https://fairsharing.org/FAIRsharing.5h3maw) /672",
        "https://identifiers.org/ncbigene/672"
      ],
      "taxonomicRange": {
        "@type": "Taxon",
        "@id": "https://www.wikidata.org (URL_TO_INSERT_RECORD_2001 https://fairsharing.org/FAIRsharing.6s749p) /wiki/Q15978631"
      },
      "url": "https://www.wikidata.org (URL_TO_INSERT_RECORD_2002 https://fairsharing.org/FAIRsharing.6s749p) /wiki/Q227339"
    }
    </script >
    ```
    
5. Download or copy and paste the generated markup
    
6. Make adjustments for any bits that could not be properly entered through the form. 

     For example, for our generated markup we would change

    ```
    "encodesBioChemEntity": {
      "@type": "BioChemEntity",
      "@id": "https://www.wikidata.org (URL_TO_INSERT_RECORD_2003 https://fairsharing.org/FAIRsharing.6s749p) /wiki/Q17487737"
    },
    ```

    to

    ```
    "encodesBioChemEntity": {
      "@type": "Protein (URL_TO_INSERT_RECORD_2004 https://fairsharing.org/FAIRsharing.rtndct) ",
      "@id": "https://www.wikidata.org (URL_TO_INSERT_RECORD_2005 https://fairsharing.org/FAIRsharing.6s749p) /wiki/Q17487737"
    },
    ```

    You can test that your JSON (URL_TO_INSERT_RECORD_2006 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2008 https://fairsharing.org/FAIRsharing.8f9bbb)  is valid syntax, and visualise your markup using the [JSON (URL_TO_INSERT_RECORD_2007 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2009 https://fairsharing.org/FAIRsharing.8f9bbb)  Playground](https://json-ld.org/playground/).

    
7. Once you are happy with your markup, include the `JSON (URL_TO_INSERT_RECORD_2010 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2011 https://fairsharing.org/FAIRsharing.8f9bbb) `, script tags and all, at the bottom of your HTML (URL_TO_INSERT_RECORD_2012 https://fairsharing.org/FAIRsharing.YugnuL)  page template. Make sure that this is before the closing `</html>` tag
    
   1. Replace the values in your markup with variables that your web page templating system will replace with values from your database (URL_TO_INSERT_TERM_2013 https://fairsharing.org/search?fairsharingRegistry=Database) . For example, the follow snippet uses variables of the form `%%%PAGEURL%%%`

       ```html
       <script type="application/ld+json" >
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD_2014 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@id": "%%%PAGEURL%%%",
         "@type": "Gene",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2015 https://fairsharing.org/3517) /profiles/Gene/0.7-RELEASE",
         "identifier (URL_TO_INSERT_TERM_2016 https://fairsharing.org/search?recordType=identifier_schema) ": "%%%PAGEURL%%%",
         "description": "%%%DESCRIPTION%%%",
         ...
       }
       ```
   
       Your site should now generate data pages with embedded markup.

       You should complete this process for each different type of data that you include in your site, e.g. ChEMBL (URL_TO_INSERT_RECORD_2017 https://fairsharing.org/FAIRsharing.m3jtpg)  would
       have `MolecularEntity` markup on their chemical pages and `Protein (URL_TO_INSERT_RECORD_2018 https://fairsharing.org/FAIRsharing.rtndct) ` markup on their target pages so would need to 
       complete this process twice.
    
       Once you have deployed this on your web server, you can test it with the [Bioschemas (URL_TO_INSERT_RECORD_2019 https://fairsharing.org/3517)  Validator](https://www.macs.hw.ac.uk/SWeL/BioschemasValidator/) which scrapes the markup from your page and allows you to test it against various Bioschemas (URL_TO_INSERT_RECORD_2020 https://fairsharing.org/3517)  profiles<sup>[2](#bioschemas (URL_TO_INSERT_RECORD_2021 https://fairsharing.org/3517) -validator)</sup>.

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

