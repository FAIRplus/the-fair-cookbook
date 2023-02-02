(fcb-find-bs-dataset)=
# Marking up Dataset page with Schema.org & Bioschemas for SEO


````{panels_fairplus}
:identifier_text: FCB012
:identifier_link: 'https://w3id.org/faircookbook/FCB012'
:difficulty_level: 2
:recipe_type: guidance
:reading_time_minutes: 10
:intended_audience: software_developer, data_scientist  
:maturity_level: 1
:maturity_indicator: 13, 14
:has_executable_code: nope
:recipe_name: Marking up Dataset page with Schema.org & Bioschemas for SEO
```` 


## Main Objectives

The main purpose of this recipe is:

> To embed `Schema.org (URL_TO_INSERT_RECORD_2091 https://fairsharing.org/FAIRsharing.hzdzq8) ` markup in a web page representing a dataset.



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
```{figure} ./bs-dataset-mermaid.png
---
width: 500px
name: 
alt: The process of annotating a dataset webpage with bioschema markup for Search (URL_TO_INSERT_RECORD_2092 https://fairsharing.org/FAIRsharing.52b22c)  Engine discovery
---
The process of annotating a dataset webpage with bioschema markup for Search (URL_TO_INSERT_RECORD_2093 https://fairsharing.org/FAIRsharing.52b22c)  Engine discovery.
```
````

---

## Method

We will outline the steps for marking up a page in your site that is about a specific dataset that you publish.
The resulting markup will be compliant with both [Google's Dataset markup guidelines](https://developers.google.com/search/docs/data-types/dataset) 
and the [Bioschemas Dataset Profile](https://bioschemas.org (URL_TO_INSERT_RECORD_2097 https://fairsharing.org/3517) /profiles/Dataset (URL_TO_INSERT_RECORD_2094 https://fairsharing.org/FAIRsharing.20sbr9) ). The resulting webpage will be indexable by the major search (URL_TO_INSERT_RECORD_2095 https://fairsharing.org/FAIRsharing.52b22c)  engines and should eventually appear in [Google's Dataset Search (URL_TO_INSERT_RECORD_2096 https://fairsharing.org/FAIRsharing.52b22c)  Tool](https://datasetsearch.research.google.com/).

We will use [UniProtKB](https://www.uniprot.org (URL_TO_INSERT_RECORD_2098 https://fairsharing.org/FAIRsharing.s1ne3g) /uniprot/) as an example for this recipe.

1. Identify the page in your site about a specific dataset, e.g. https://www.uniprot.org (URL_TO_INSERT_RECORD_2099 https://fairsharing.org/FAIRsharing.s1ne3g) /uniprot/

2. Open the  [Bioschemas Generator](https://www.macs.hw.ac.uk/SWeL/BioschemasGenerator/)

   1.  Select `Dataset` from the Bioschemas (URL_TO_INSERT_RECORD_2100 https://fairsharing.org/3517)  Profile dropdown

   2.  Enter the URL (URL_TO_INSERT_RECORD_2101 https://fairsharing.org/FAIRsharing.9d38e2)  of the page in URL (URL_TO_INSERT_RECORD_2102 https://fairsharing.org/FAIRsharing.9d38e2)  box, e.g. `https://www.uniprot.org (URL_TO_INSERT_RECORD_2103 https://fairsharing.org/FAIRsharing.s1ne3g) /uniprot/`

   3.  Click on the `Show Form` button


   ````{dropdown} 
   :open:
   ```{figure} Bioschemas (URL_TO_INSERT_RECORD_2104 https://fairsharing.org/3517) Generator.png
   ---
   name: bioschemas (URL_TO_INSERT_RECORD_2105 https://fairsharing.org/3517) -generator-start-screen-3
   alt: Bioschemas (URL_TO_INSERT_RECORD_2106 https://fairsharing.org/3517)  Generator start screen.
   
   ---
   Bioschemas (URL_TO_INSERT_RECORD_2107 https://fairsharing.org/3517)  Generator start screen.
   ```
   ````
   
3. Complete the profile form with the data relevant for your page. Once completed, click on the `Generate Markup`  button

   - You should complete all *Minimum* properties and as many *Recommended* properties as possible. You can show/hide properties using the `Additional Properties` buttons.
   - Where possible you should link to other resources. The Bioschemas (URL_TO_INSERT_RECORD_2108 https://fairsharing.org/3517)  Generator does not make this as simple as it could, but you can do it in step 5 once you have generated your markup, e.g. our dataset will link to a page with DataCatalog markup in rather than repeating all the properties for now we will just enter a `url` and no other properties
   - The form defaults to the data type with the first alphabetical character, e.g. for `identifier (URL_TO_INSERT_TERM_2109 https://fairsharing.org/search?recordType=identifier_schema) `, this defaults to `PropertyValue` but `Text` or `URL ` will be more appropriate in most cases
   - The right side of the screen gives examples for properties, where these have been provided by the Bioschemas (URL_TO_INSERT_RECORD_2110 https://fairsharing.org/3517)  profile authors. Click on the `Show` button to see the example for a specific property. Click on `Minimum`, `Recommended`, or `Optional` to expand/contract the section and see the properties contained at that marginality level

   ````{dropdown} 
   :open:
   ```{figure} Bioschemas (URL_TO_INSERT_RECORD_2111 https://fairsharing.org/3517) GeneratorDatasetForm.png
   ---
   height: 550px
   name: Bioschemas (URL_TO_INSERT_RECORD_2112 https://fairsharing.org/3517)  Generator Dataset profile form
   alt: Bioschemas (URL_TO_INSERT_RECORD_2113 https://fairsharing.org/3517)  Generator Dataset profile form
   ---
   Bioschemas (URL_TO_INSERT_RECORD_2114 https://fairsharing.org/3517)  Generator Dataset profile form.
   ``` 
   ````
   
4. You will now see the generated markup in `JSON (URL_TO_INSERT_RECORD_2117 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2120 https://fairsharing.org/FAIRsharing.8f9bbb) ` format (URL_TO_INSERT_TERM_2115 https://fairsharing.org/search?recordType=model_and_format) . You can click on the `Microdata` and `RDFa (URL_TO_INSERT_RECORD_2119 https://fairsharing.org/663) ` tabs to see the same content rendered in the different format (URL_TO_INSERT_TERM_2116 https://fairsharing.org/search?recordType=model_and_format) s. However, we recommend the use of `JSON (URL_TO_INSERT_RECORD_2118 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2121 https://fairsharing.org/FAIRsharing.8f9bbb) `. For our UniProtKB (URL_TO_INSERT_RECORD_2122 https://fairsharing.org/FAIRsharing.s1ne3g)  example, we get the following markup
   
   ```
   <script type="application/ld+json" >
   {
     "@context": "https://schema.org (URL_TO_INSERT_RECORD_2123 https://fairsharing.org/FAIRsharing.hzdzq8) ",
     "@id": "https://www.uniprot.org (URL_TO_INSERT_RECORD_2124 https://fairsharing.org/FAIRsharing.s1ne3g) /uniprot/",
     "@type": "Dataset",
     "citation": [
       {
         "@id": "https://doi.org/10.1093/nar/gky1049",
         "@type": "CreativeWork"
       }
     ],
     "creator": [
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD_2125 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Organization",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2126 https://fairsharing.org/3517) /profiles/Organization/0.2-DRAFT-2019_07_19",
         "description": "The mission of UniProt is to provide the scientific community with a comprehensive, high quality and freely accessible resource of protein sequence and functional informat (URL_TO_INSERT_TERM_2127 https://fairsharing.org/search?recordType=model_and_format) ion. ",
         "name": "UniProt Consortium"
       }
     ],
     "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2129 https://fairsharing.org/3517) /profiles/Dataset (URL_TO_INSERT_RECORD_2128 https://fairsharing.org/FAIRsharing.20sbr9) /0.3-RELEASE-2019_06_14",
     "description": "The UniProt Knowledgebas (URL_TO_INSERT_RECORD_2137 https://fairsharing.org/FAIRsharing.b94a20) e (URL_TO_INSERT_TERM_2130 https://fairsharing.org/search?recordType=knowledgebase)  (URL_TO_INSERT_RECORD_2138 https://fairsharing.org/FAIRsharing.s1ne3g)  (UniProtKB (URL_TO_INSERT_RECORD_2139 https://fairsharing.org/FAIRsharing.s1ne3g) ) is the central hub for the collection (URL_TO_INSERT_TERM_2131 https://fairsharing.org/search?recordType=collection)  of functional informat (URL_TO_INSERT_TERM_2132 https://fairsharing.org/search?recordType=model_and_format) ion on proteins, with accurate, consistent and rich annotation. In addition to capturing the core (URL_TO_INSERT_RECORD_2135 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_2136 https://fairsharing.org/FAIRsharing.xMmOCL)  data mandatory for each UniProtKB (URL_TO_INSERT_RECORD_2140 https://fairsharing.org/FAIRsharing.s1ne3g)  entry (mainly, the amino acid sequence, protein name or description, taxonomic data and citation informat (URL_TO_INSERT_TERM_2133 https://fairsharing.org/search?recordType=model_and_format) ion), as much annotation informat (URL_TO_INSERT_TERM_2134 https://fairsharing.org/search?recordType=model_and_format) ion as possible is added.",
     "distribution": {
       "@id": "https://www.uniprot.org (URL_TO_INSERT_RECORD_2141 https://fairsharing.org/FAIRsharing.s1ne3g) /downloads#uniprotkblink",
       "@type": "DataDownload"
     },
     "identifier (URL_TO_INSERT_TERM_2142 https://fairsharing.org/search?recordType=identifier_schema) ": [
       "https://www.uniprot.org (URL_TO_INSERT_RECORD_2143 https://fairsharing.org/FAIRsharing.s1ne3g) /uniprot/"
     ],
     "includedInDataCatalog": [
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD_2144 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "DataCatalog",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2146 https://fairsharing.org/3517) /profiles/DataCatalog/0.3-RELEASE-2019_07_01 (URL_TO_INSERT_RECORD_2145 https://fairsharing.org/FAIRsharing.2037b2) ",
         "description": "",
         "keywords": [],
         "name": "",
         "url": "https://uniprot.org"
       }
     ],
     "keywords": [
       "Protein (URL_TO_INSERT_RECORD_2147 https://fairsharing.org/FAIRsharing.rtndct) ",
       "Protein (URL_TO_INSERT_RECORD_2148 https://fairsharing.org/FAIRsharing.rtndct)  annotation"
     ],
     "license": "https://creativecommons.org/licenses/by/4.0/",
     "name": "UniProtKB (URL_TO_INSERT_RECORD_2149 https://fairsharing.org/FAIRsharing.s1ne3g) ",
     "url": "https://www.uniprot.org (URL_TO_INSERT_RECORD_2150 https://fairsharing.org/FAIRsharing.s1ne3g) /uniprot/"
   }
   </script >
   ```
   
5. Download or copy and paste the generated markup
   
6. Make adjustments for any bits that could not be properly entered through the form. 
   
   For example, for our generated markup we would change the `includedInDataCatalog` so that it provides a direct link rather than repeating the properties. We would replace

   ```
   "includedInDataCatalog": [
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD_2151 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "DataCatalog",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2153 https://fairsharing.org/3517) /profiles/DataCatalog/0.3-RELEASE-2019_07_01 (URL_TO_INSERT_RECORD_2152 https://fairsharing.org/FAIRsharing.2037b2) ",
         "description": "",
         "keywords": [],
         "name": "",
         "url": "https://uniprot.org"
       }
     ],
   ```

   with

   ```
   "includedInDataCatalog": {
      "@type": "DataCatalog",
      "@id": "https://uniprot.org"
    },
   ```

   You can test that your JSON (URL_TO_INSERT_RECORD_2154 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2155 https://fairsharing.org/FAIRsharing.8f9bbb)  is valid syntax, and visualise your markup using the [JSON-LD Playground](https://json-ld.org/playground/).

7. Once you are happy with your markup, include the `JSON (URL_TO_INSERT_RECORD_2156 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2157 https://fairsharing.org/FAIRsharing.8f9bbb) `, script tags and all, at the bottom of your HTML (URL_TO_INSERT_RECORD_2158 https://fairsharing.org/FAIRsharing.YugnuL)  page template.

   Make sure that this is before the closing `</html>` tag

8. If you have multiple datasets released through your site, then you should make a template for your datasets. In your template you should replace the values in your markup that will change from dataset to dataset with variables. Your web page templating system will replace the variables with values from your database (URL_TO_INSERT_TERM_2159 https://fairsharing.org/search?fairsharingRegistry=Database) . For example, the follow snippet uses variables of the form `%%%PAGEURL%%%`

   ```
      <script type="application/ld+json">
      {
        "@context": "https://schema.org (URL_TO_INSERT_RECORD_2160 https://fairsharing.org/FAIRsharing.hzdzq8) ",
        "@id": "%%%PAGEURL%%%",
        "@type": "Dataset",
        "citation": [
          {
            "@id": "%%%DOI%%%",
            "@type": "CreativeWork"
          }
        ],
        "creator": [
          {
            "@context": "https://schema.org (URL_TO_INSERT_RECORD_2161 https://fairsharing.org/FAIRsharing.hzdzq8) ",
            "@type": "Organization",
            "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2162 https://fairsharing.org/3517) /profiles/Organization/0.2-DRAFT-2019_07_19",
            "description": "The mission of UniProt is to provide the scientific community with a comprehensive, high quality and freely accessible resource of protein sequence and functional informat (URL_TO_INSERT_TERM_2163 https://fairsharing.org/search?recordType=model_and_format) ion. ",
            "name": "UniProt Consortium"
          }
          ...
        ]
      }
     </script>
   ```

   Your site should now generate dataset pages with embedded markup. 

   Once you have deployed this on your web server, you can test it with the [Bioschemas Validator](https://www.macs.hw.ac.uk/SWeL/BioschemasValidator/) which scrapes the markup from your page and allows you to test it against various Bioschemas (URL_TO_INSERT_RECORD_2164 https://fairsharing.org/3517)  profiles<sup>[1](#bioschemas (URL_TO_INSERT_RECORD_2165 https://fairsharing.org/3517) -validator)</sup>.

---


## Conclusion


### What to read next?

- {ref}`fcb-find-bs-data`
- {ref}`fcb-find-bs-catalog`
- {ref}`fcb-find-bs-dataset`

````{rdmkit_panel}
````



## References
````{dropdown} **References**
<a name="bioschemas-validator">1</a>: The Bioschemas Validator is currently in an early alpha release and does not include all the profiles.
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


