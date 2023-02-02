(fcb-find-bs-catalog)=
# Marking up Data Catalogue page with Schema.org & Bioschemas for SEO


````{panels_fairplus}
:identifier_text: FCB013
:identifier_link: 'https://w3id.org/faircookbook/FCB013'
:difficulty_level: 2
:recipe_type: guidance
:reading_time_minutes: 10
:intended_audience: software_developer, data_scientist
:maturity_level: 2
:maturity_indicator: 24
:has_executable_code: nope
:recipe_name: Marking up Data Catalogue page with Schema.org & Bioschemas for SEO
```` 

## Main Objectives

The main purpose of this recipe is:

> To embed `Schema.org (URL_TO_INSERT_RECORD_1925 https://fairsharing.org/FAIRsharing.hzdzq8) ` markup in a web page that publishes multiple datasets in a single page.


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
```{figure} ./bs-datacatalog-mermaid.png
---
width: 500px
name: 
alt: The process of annotating a data catalog webpage with bioschema markup for Search (URL_TO_INSERT_RECORD_1926 https://fairsharing.org/FAIRsharing.52b22c)  Engine discovery
---
The process of annotating a data catalog webpage with bioschema markup for Search (URL_TO_INSERT_RECORD_1927 https://fairsharing.org/FAIRsharing.52b22c)  Engine discovery.
```
````


---

## Method

We will outline the steps for marking up a page in your site that is about multiple datasets. The resulting markup will be compliant with both [Google's Dataset markup guidelines](https://developers.google.com/search/docs/data-types/dataset#publication) and the [Bioschemas (URL_TO_INSERT_RECORD_1929 https://fairsharing.org/3517)  DataCatalog Profile (URL_TO_INSERT_RECORD_1928 https://fairsharing.org/FAIRsharing.2037b2) ](https://bioschemas.org (URL_TO_INSERT_RECORD_1930 https://fairsharing.org/3517) /profiles/DataCatalog). 

We will use [FAIRsharing](https://fairsharing.org (URL_TO_INSERT_RECORD_1931 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_1932 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_1933 https://fairsharing.org/3538) /) as an example for this recipe which makes three datasets available within its markup.

1. Identify the page in your site about a specific dataset, e.g. https://fairsharing.org (URL_TO_INSERT_RECORD_1934 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_1935 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_1936 https://fairsharing.org/3538) /

2. Open the  [Bioschemas Generator](https://www.macs.hw.ac.uk/SWeL/BioschemasGenerator/)

   1.  Select `DataCatalog` from the Bioschemas (URL_TO_INSERT_RECORD_1937 https://fairsharing.org/3517)  Profile dropdown

   2.  Enter the URL (URL_TO_INSERT_RECORD_1938 https://fairsharing.org/FAIRsharing.9d38e2)  of the page in URL (URL_TO_INSERT_RECORD_1939 https://fairsharing.org/FAIRsharing.9d38e2)  box, e.g. `https://fairsharing.org (URL_TO_INSERT_RECORD_1940 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_1941 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_1942 https://fairsharing.org/3538) /`

   3.  Click on the `Show Form` button
   
   ````{dropdown} 
   :open:
   ```{figure} Bioschemas (URL_TO_INSERT_RECORD_1943 https://fairsharing.org/3517) Generator.png
   ---
   name: bioschemas (URL_TO_INSERT_RECORD_1944 https://fairsharing.org/3517) -generator-start-screen-1
   alt: Bioschemas (URL_TO_INSERT_RECORD_1945 https://fairsharing.org/3517)  Generator start screen.
   
   ---
   Bioschemas (URL_TO_INSERT_RECORD_1946 https://fairsharing.org/3517)  Generator start screen.
   ```
   ````

3. Complete the profile form with the informat (URL_TO_INSERT_TERM_1947 https://fairsharing.org/search?recordType=model_and_format) ion relevant for your page. Once completed, click on the `Generate Markup`  button

   - You should complete all *Minimum* properties and as many *Recommended* properties as possible. You can show/hide properties using the `Additional Properties` buttons.
   - Where possible you should link to other resources. The Bioschemas (URL_TO_INSERT_RECORD_1948 https://fairsharing.org/3517)  Generator does not make this as simple as it could, but you can do it in step 5 once you have generated your markup, e.g. our dataset will link to a page with DataCatalog markup in rather than repeating all the properties for now we will just enter a `url` and no other properties.
     - If there are separate pages for your datasets then you should link to them using an `@id` link
     - Otherwise, you can include the markup within the `DataCatalog` markup
   - The form defaults to the data type with the first alphabetical character, e.g. for `identifier (URL_TO_INSERT_TERM_1949 https://fairsharing.org/search?recordType=identifier_schema) `, this defaults to `PropertyValue` but `Text` or `URL ` will be more appropriate in most cases
   - The right side of the screen gives examples for properties, where these have been provided by the Bioschemas (URL_TO_INSERT_RECORD_1950 https://fairsharing.org/3517)  profile authors. Click on the `Show` button to see the example for a specific property. Click on `Minimum`, `Recommended`, or `Optional` to expand/contract the section and see the properties contained at that marginality level

   ````{dropdown} 
   :open:
   ```{figure} Bioschemas (URL_TO_INSERT_RECORD_1951 https://fairsharing.org/3517) GeneratorDataCatalogForm.png
   ---
   height: 550px
   name: Bioschemas (URL_TO_INSERT_RECORD_1952 https://fairsharing.org/3517)  Generator DataCatalog profile form
   alt: Bioschemas (URL_TO_INSERT_RECORD_1953 https://fairsharing.org/3517)  Generator DataCatalog profile form
   ---
   Bioschemas (URL_TO_INSERT_RECORD_1954 https://fairsharing.org/3517)  Generator DataCatalog profile form.
   ```   
   ````

4. You will now see the generated markup in `JSON (URL_TO_INSERT_RECORD_1957 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_1960 https://fairsharing.org/FAIRsharing.8f9bbb) ` format (URL_TO_INSERT_TERM_1955 https://fairsharing.org/search?recordType=model_and_format) . You can click on the `Microdata` and `RDFa (URL_TO_INSERT_RECORD_1959 https://fairsharing.org/663) ` tabs to see the same content rendered in the different format (URL_TO_INSERT_TERM_1956 https://fairsharing.org/search?recordType=model_and_format) s. However, we recommend the use of `JSON (URL_TO_INSERT_RECORD_1958 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_1961 https://fairsharing.org/FAIRsharing.8f9bbb) `. For our FAIR (URL_TO_INSERT_RECORD_1963 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_1962 https://fairsharing.org/FAIRsharing.2abjs5) .org example, we get the following markup

   ```
   <script type="application/ld+json" >
   {
     "@context": "https://schema.org (URL_TO_INSERT_RECORD_1964 https://fairsharing.org/FAIRsharing.hzdzq8) ",
     "@id": "https://fairsharing.org (URL_TO_INSERT_RECORD_1965 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_1966 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_1967 https://fairsharing.org/3538) /",
     "@type": "DataCatalog",
     "alternateName": [
       "BioSharing.org"
     ],
     "citation": [
       {
         "@id": "https://doi.org/10.1038/s41587-019-0080-8",
         "@type": "CreativeWork"
       }
     ],
     "dataset": [
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD_1968 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Dataset",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_1970 https://fairsharing.org/3517) /profiles/Dataset (URL_TO_INSERT_RECORD_1969 https://fairsharing.org/FAIRsharing.20sbr9) /0.3-RELEASE-2019_06_14",
         "description": "A manually curated registry of standard (URL_TO_INSERT_TERM_1971 https://fairsharing.org/search?fairsharingRegistry=Standard) s, split into three types - Terminology (URL_TO_INSERT_TERM_1982 https://fairsharing.org/search?recordType=terminology_artefact)  Artifacts (ontologies (URL_TO_INSERT_TERM_1984 https://fairsharing.org/search?recordType=terminology_artefact) , e.g. Gene Ontology (URL_TO_INSERT_TERM_1983 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_1987 https://fairsharing.org/FAIRsharing.6xq0ee) ), Model (URL_TO_INSERT_TERM_1978 https://fairsharing.org/search?recordType=model_and_format) s and Format (URL_TO_INSERT_TERM_1980 https://fairsharing.org/search?recordType=model_and_format) s (conceptual schema, format (URL_TO_INSERT_TERM_1981 https://fairsharing.org/search?recordType=model_and_format) s, data model (URL_TO_INSERT_TERM_1979 https://fairsharing.org/search?recordType=model_and_format) s, e.g. FAST (URL_TO_INSERT_RECORD_1988 https://fairsharing.org/FAIRsharing.p5df9c) A (URL_TO_INSERT_RECORD_1989 https://fairsharing.org/FAIRsharing.rz4vfg) ), and Reporting Guideline (URL_TO_INSERT_TERM_1974 https://fairsharing.org/search?recordType=reporting_guideline)  (URL_TO_INSERT_TERM_1985 https://fairsharing.org/search?recordType=reporting_guideline) s (e.g. the ARRIVE (URL_TO_INSERT_RECORD_1990 https://fairsharing.org/FAIRsharing.t58zhj)  guideline (URL_TO_INSERT_TERM_1986 https://fairsharing.org/search?recordType=reporting_guideline) s for in vivo animal testing). These are linked to the database (URL_TO_INSERT_TERM_1972 https://fairsharing.org/search?fairsharingRegistry=Database) s that implement them and the funder (URL_TO_INSERT_TERM_1977 https://fairsharing.org/search?recordType=funder)  and journal (URL_TO_INSERT_TERM_1975 https://fairsharing.org/search?recordType=journal)  publisher (URL_TO_INSERT_TERM_1976 https://fairsharing.org/search?recordType=journal_publisher)  data policies (URL_TO_INSERT_TERM_1973 https://fairsharing.org/search?fairsharingRegistry=Policy)  that recommend or endorse their use.",
         "identifier (URL_TO_INSERT_TERM_1991 https://fairsharing.org/search?recordType=identifier_schema) ": [
           "https://www.fairsharing.org (URL_TO_INSERT_RECORD_1992 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD_1993 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_1994 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_1995 https://fairsharing.org/3538) /bsg-sXXXXXX"
         ],
         "keywords": [
           "Standard (URL_TO_INSERT_TERM_1996 https://fairsharing.org/search?fairsharingRegistry=Standard) s",
           "Metadata",
           "Format (URL_TO_INSERT_TERM_1997 https://fairsharing.org/search?recordType=model_and_format) s",
           "Ontologies (URL_TO_INSERT_TERM_1998 https://fairsharing.org/search?recordType=terminology_artefact) ",
           "Terminology (URL_TO_INSERT_TERM_1999 https://fairsharing.org/search?recordType=terminology_artefact)  Artifacts",
           "Reporting Guideline (URL_TO_INSERT_TERM_2000 https://fairsharing.org/search?recordType=reporting_guideline)  (URL_TO_INSERT_TERM_2001 https://fairsharing.org/search?recordType=reporting_guideline) s"
         ],
         "name": "Metadata Standard (URL_TO_INSERT_TERM_2002 https://fairsharing.org/search?fairsharingRegistry=Standard) ",
         "url": "https://fairsharing.org (URL_TO_INSERT_RECORD_2003 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2004 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2005 https://fairsharing.org/3538) /standards"
       },
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD_2006 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Dataset",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2008 https://fairsharing.org/3517) /profiles/Dataset (URL_TO_INSERT_RECORD_2007 https://fairsharing.org/FAIRsharing.20sbr9) /0.3-RELEASE-2019_06_14",
         "description": "A manually curated registry of database (URL_TO_INSERT_TERM_2011 https://fairsharing.org/search?fairsharingRegistry=Database) s/data repositories (URL_TO_INSERT_TERM_2013 https://fairsharing.org/search?recordType=repository) , conforming to the BioDBcore (URL_TO_INSERT_RECORD_2017 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_2018 https://fairsharing.org/FAIRsharing.xMmOCL)  standard (URL_TO_INSERT_TERM_2009 https://fairsharing.org/search?fairsharingRegistry=Standard)  (from the Life Sciences). These are linked to the standard (URL_TO_INSERT_TERM_2010 https://fairsharing.org/search?fairsharingRegistry=Standard) s that they use and the funder (URL_TO_INSERT_TERM_2016 https://fairsharing.org/search?recordType=funder)  and journal (URL_TO_INSERT_TERM_2014 https://fairsharing.org/search?recordType=journal)  publisher (URL_TO_INSERT_TERM_2015 https://fairsharing.org/search?recordType=journal_publisher)  data policies (URL_TO_INSERT_TERM_2012 https://fairsharing.org/search?fairsharingRegistry=Policy)  that recommend or endorse their use.",
         "identifier (URL_TO_INSERT_TERM_2019 https://fairsharing.org/search?recordType=identifier_schema) ": [
           "https://www.fairsharing.org (URL_TO_INSERT_RECORD_2020 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD_2021 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2022 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2023 https://fairsharing.org/3538) /bsg-dXXXXXX"
         ],
         "keywords": [
           "Database (URL_TO_INSERT_TERM_2024 https://fairsharing.org/search?fairsharingRegistry=Database) ",
           "Data repository (URL_TO_INSERT_TERM_2025 https://fairsharing.org/search?recordType=repository) "
         ],
         "name": "Database (URL_TO_INSERT_TERM_2026 https://fairsharing.org/search?fairsharingRegistry=Database) ",
         "url": "https://fairsharing.org (URL_TO_INSERT_RECORD_2027 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2028 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2029 https://fairsharing.org/3538) /databases"
       },
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD_2030 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Dataset",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2032 https://fairsharing.org/3517) /profiles/Dataset (URL_TO_INSERT_RECORD_2031 https://fairsharing.org/FAIRsharing.20sbr9) /0.3-RELEASE-2019_06_14",
         "description": "A manually curated registry of data policies (URL_TO_INSERT_TERM_2035 https://fairsharing.org/search?fairsharingRegistry=Policy)  from research (URL_TO_INSERT_RECORD_2040 https://fairsharing.org/FAIRsharing.52b22c)  funder (URL_TO_INSERT_TERM_2039 https://fairsharing.org/search?recordType=funder) s, journal (URL_TO_INSERT_TERM_2036 https://fairsharing.org/search?recordType=journal)  publisher (URL_TO_INSERT_TERM_2038 https://fairsharing.org/search?recordType=journal_publisher) s, societies (URL_TO_INSERT_TERM_2037 https://fairsharing.org/search?recordType=society) , and other organisations. These are linked to the database (URL_TO_INSERT_TERM_2034 https://fairsharing.org/search?fairsharingRegistry=Database) s and standard (URL_TO_INSERT_TERM_2033 https://fairsharing.org/search?fairsharingRegistry=Standard) s that they recommend for use",
         "identifier (URL_TO_INSERT_TERM_2041 https://fairsharing.org/search?recordType=identifier_schema) ": [
           "https://www.fairsharing.org (URL_TO_INSERT_RECORD_2042 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD_2043 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2044 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2045 https://fairsharing.org/3538) /bsg-pXXXXXX"
         ],
         "keywords": [
           "Data policy (URL_TO_INSERT_TERM_2046 https://fairsharing.org/search?fairsharingRegistry=Policy) ",
           "journal (URL_TO_INSERT_TERM_2047 https://fairsharing.org/search?recordType=journal) ",
           "funder (URL_TO_INSERT_TERM_2048 https://fairsharing.org/search?recordType=funder) ",
           "society (URL_TO_INSERT_TERM_2049 https://fairsharing.org/search?recordType=society) "
         ],
         "name": "Data Policy (URL_TO_INSERT_TERM_2050 https://fairsharing.org/search?fairsharingRegistry=Policy) ",
         "url": "https://fairsharing.org (URL_TO_INSERT_RECORD_2051 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2052 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2053 https://fairsharing.org/3538) /policies"
       }
     ],
     "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2055 https://fairsharing.org/3517) /profiles/DataCatalog/0.3-RELEASE-2019_07_01 (URL_TO_INSERT_RECORD_2054 https://fairsharing.org/FAIRsharing.2037b2) ",
     "description": "A manually curated, informat (URL_TO_INSERT_TERM_2063 https://fairsharing.org/search?recordType=model_and_format) ive and educational resource on data and metadata standard (URL_TO_INSERT_TERM_2056 https://fairsharing.org/search?fairsharingRegistry=Standard) s, inter-related to database (URL_TO_INSERT_TERM_2057 https://fairsharing.org/search?fairsharingRegistry=Database) s/data repositories (URL_TO_INSERT_TERM_2059 https://fairsharing.org/search?recordType=repository)  and funder (URL_TO_INSERT_TERM_2062 https://fairsharing.org/search?recordType=funder)  and journal (URL_TO_INSERT_TERM_2060 https://fairsharing.org/search?recordType=journal)  publisher (URL_TO_INSERT_TERM_2061 https://fairsharing.org/search?recordType=journal_publisher)  data policies (URL_TO_INSERT_TERM_2058 https://fairsharing.org/search?fairsharingRegistry=Policy)  from across disciplines. FAIR (URL_TO_INSERT_RECORD_2066 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_2065 https://fairsharing.org/FAIRsharing.2abjs5)  is an ELIXIR-UK node resource and has an active role in the RDA (URL_TO_INSERT_RECORD_2064 https://fairsharing.org/FAIRsharing.2g5kcb)  and Force11 data initiatives.",
     "identifier (URL_TO_INSERT_TERM_2067 https://fairsharing.org/search?recordType=identifier_schema) ": [
       "https://identifiers.org/MIR:00000364"
     ],
     "keywords": [
       "registry",
       "life science",
       "natural science",
       "social science"
     ],
     "license": {
       "@id": "https://creativecommons.org/licenses/by-sa/4.0/",
       "@type": "CreativeWork"
     },
     "name": "FAIR (URL_TO_INSERT_RECORD_2069 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_2068 https://fairsharing.org/FAIRsharing.2abjs5) .org",
     "provider": [
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD_2070 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Organization",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2071 https://fairsharing.org/3517) /profiles/Organization/0.2-DRAFT-2019_07_19",
         "description": "",
         "name": "FAIR (URL_TO_INSERT_RECORD_2073 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_2072 https://fairsharing.org/FAIRsharing.2abjs5) .org Registry"
       }
     ],
     "url": "https://fairsharing.org (URL_TO_INSERT_RECORD_2074 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2075 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2076 https://fairsharing.org/3538) /"
   }
   </script >
   ```
   
5. Download or copy and paste the generated markup
   
6. Make adjustments for any bits that could not be properly entered through the form. 
   
   For example, for our generated markup we would change the `provider` so that it provides a direct link rather than repeating the properties. We would replace

   ```
   "provider": [
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD_2077 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Organization",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2078 https://fairsharing.org/3517) /profiles/Organization/0.2-DRAFT-2019_07_19",
         "description": "",
         "name": "FAIR (URL_TO_INSERT_RECORD_2080 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_2079 https://fairsharing.org/FAIRsharing.2abjs5) .org Registry"
       }
     ],
   ```
   
   with

   ```
   "provider": [
       {
         "@type": "Organization",
         "@id": "https://fairsharing.org (URL_TO_INSERT_RECORD_2081 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2082 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2083 https://fairsharing.org/3538) /communities"
       }
     ],
   ```
   
   You can test that your JSON (URL_TO_INSERT_RECORD_2084 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2085 https://fairsharing.org/FAIRsharing.8f9bbb)  is valid syntax, and visualise your markup using the [JSON-LD Playground](https://json-ld.org/playground/).

7. Once you are happy with your markup, include the `JSON (URL_TO_INSERT_RECORD_2086 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2087 https://fairsharing.org/FAIRsharing.8f9bbb) `, script tags and all, at the bottom of your HTML (URL_TO_INSERT_RECORD_2088 https://fairsharing.org/FAIRsharing.YugnuL)  page template. 

   Make sure that this is before the closing `</html>` tag.
   
   Your site should now include DataCatalog markup. 
   
   Once you have deployed this on your web server, you can test it with the [Bioschemas Validator](https://www.macs.hw.ac.uk/SWeL/BioschemasValidator/) which scrapes the markup from your page and allows you to test it against various Bioschemas (URL_TO_INSERT_RECORD_2089 https://fairsharing.org/3517)  profiles<sup>[1](#bioschemas (URL_TO_INSERT_RECORD_2090 https://fairsharing.org/3517) -validator)</sup>.

---



## Conclusion


### What to read next?

- {ref}`fcb-find-bs-data`
- {ref}`fcb-find-bs-dataset`
 
````{rdmkit_panel}
````






## References
````{dropdown} **References**
<a name="bioschemas-validator">1</a>: The Bioschemas Validator is currently in an early alpha release and does not include all the profiles
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


