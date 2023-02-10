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

> To embed `Schema.org (URL_TO_INSERT_RECORD-NAME_1299 https://fairsharing.org/FAIRsharing.hzdzq8) ` markup in a web page that publishes multiple datasets in a single page.


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
alt: The process of annotating a data catalog webpage with bioschema markup for Search Engine discovery
---
The process of annotating a data catalog webpage with bioschema markup for Search Engine discovery.
```
````


---

## Method

We will outline the steps for marking up a page in your site that is about multiple datasets. The resulting markup will be compliant with both [Google's Dataset markup guidelines](https://developers.google.com/search/docs/data-types/dataset#publication) and the [Bioschemas (URL_TO_INSERT_RECORD-NAME_1301 https://fairsharing.org/3517)  DataCatalog Profile (URL_TO_INSERT_RECORD-NAME_1300 https://fairsharing.org/FAIRsharing.2037b2) ](https://bioschemas.org/profiles/DataCatalog). 

We will use [FAIRsharing](https://fairsharing.org/) as an example for this recipe which makes three datasets available within its markup.

1. Identify the page in your site about a specific dataset, e.g. https://fairsharing.org (URL_TO_INSERT_RECORD-HOMEPAGE_1302 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD-HOMEPAGE_1303 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD-HOMEPAGE_1304 https://fairsharing.org/3538) /

2. Open the  [Bioschemas Generator](https://www.macs.hw.ac.uk/SWeL/BioschemasGenerator/)

   1.  Select `DataCatalog` from the Bioschemas (URL_TO_INSERT_RECORD-NAME_1305 https://fairsharing.org/3517)  Profile dropdown

   2.  Enter the URL (URL_TO_INSERT_RECORD-ABBREV_1306 https://fairsharing.org/FAIRsharing.9d38e2)  of the page in URL (URL_TO_INSERT_RECORD-ABBREV_1307 https://fairsharing.org/FAIRsharing.9d38e2)  box, e.g. `https://fairsharing.org (URL_TO_INSERT_RECORD-HOMEPAGE_1308 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD-HOMEPAGE_1309 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD-HOMEPAGE_1310 https://fairsharing.org/3538) /`

   3.  Click on the `Show Form` button
   
   ````{dropdown} 
   :open:
   ```{figure} BioschemasGenerator.png
   ---
   name: bioschemas (URL_TO_INSERT_RECORD-NAME_1311 https://fairsharing.org/3517) -generator-start-screen-1
   alt: Bioschemas (URL_TO_INSERT_RECORD-NAME_1312 https://fairsharing.org/3517)  Generator start screen.
   
   ---
   Bioschemas (URL_TO_INSERT_RECORD-NAME_1313 https://fairsharing.org/3517)  Generator start screen.
   ```
   ````

3. Complete the profile form with the informat (URL_TO_INSERT_TERM_1314 https://fairsharing.org/search?recordType=model_and_format) ion relevant for your page. Once completed, click on the `Generate Markup`  button

   - You should complete all *Minimum* properties and as many *Recommended* properties as possible. You can show/hide properties using the `Additional Properties` buttons.
   - Where possible you should link to other resources. The Bioschemas (URL_TO_INSERT_RECORD-NAME_1315 https://fairsharing.org/3517)  Generator does not make this as simple as it could, but you can do it in step 5 once you have generated your markup, e.g. our dataset will link to a page with DataCatalog markup in rather than repeating all the properties for now we will just enter a `url` and no other properties.
     - If there are separate pages for your datasets then you should link to them using an `@id` link
     - Otherwise, you can include the markup within the `DataCatalog` markup
   - The form defaults to the data type with the first alphabetical character, e.g. for `identifier (URL_TO_INSERT_TERM_1316 https://fairsharing.org/search?recordType=identifier_schema) `, this defaults to `PropertyValue` but `Text` or `URL (URL_TO_INSERT_RECORD-ABBREV_1317 https://fairsharing.org/FAIRsharing.9d38e2)  ` will be more appropriate in most cases
   - The right side of the screen gives examples for properties, where these have been provided by the Bioschemas (URL_TO_INSERT_RECORD-NAME_1318 https://fairsharing.org/3517)  profile authors. Click on the `Show` button to see the example for a specific property. Click on `Minimum`, `Recommended`, or `Optional` to expand/contract the section and see the properties contained at that marginality level

   ````{dropdown} 
   :open:
   ```{figure} BioschemasGeneratorDataCatalogForm.png
   ---
   height: 550px
   name: Bioschemas (URL_TO_INSERT_RECORD-NAME_1319 https://fairsharing.org/3517)  Generator DataCatalog profile form
   alt: Bioschemas (URL_TO_INSERT_RECORD-NAME_1320 https://fairsharing.org/3517)  Generator DataCatalog profile form
   ---
   Bioschemas (URL_TO_INSERT_RECORD-NAME_1321 https://fairsharing.org/3517)  Generator DataCatalog profile form.
   ```   
   ````

4. You will now see the generated markup in `JSON (URL_TO_INSERT_RECORD-ABBREV_1324 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD-ABBREV_1327 https://fairsharing.org/FAIRsharing.8f9bbb) ` format (URL_TO_INSERT_TERM_1322 https://fairsharing.org/search?recordType=model_and_format) . You can click on the `Microdata` and `RDFa (URL_TO_INSERT_RECORD-ABBREV_1326 https://fairsharing.org/663) ` tabs to see the same content rendered in the different format (URL_TO_INSERT_TERM_1323 https://fairsharing.org/search?recordType=model_and_format) s. However, we recommend the use of `JSON (URL_TO_INSERT_RECORD-ABBREV_1325 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD-ABBREV_1328 https://fairsharing.org/FAIRsharing.8f9bbb) `. For our FAIRsharing (URL_TO_INSERT_RECORD-NAME_1329 https://fairsharing.org/FAIRsharing.2abjs5) .org example, we get the following markup

   ```
   <script type="application/ld+json" >
   {
     "@context": "https://schema.org (URL_TO_INSERT_RECORD-HOMEPAGE_1330 https://fairsharing.org/FAIRsharing.hzdzq8) ",
     "@id": "https://fairsharing.org (URL_TO_INSERT_RECORD-HOMEPAGE_1331 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD-HOMEPAGE_1332 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD-HOMEPAGE_1333 https://fairsharing.org/3538) /",
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
         "@context": "https://schema.org (URL_TO_INSERT_RECORD-HOMEPAGE_1334 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Dataset",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD-HOMEPAGE_1336 https://fairsharing.org/3517) /profiles/Dataset (URL_TO_INSERT_RECORD-HOMEPAGE_1335 https://fairsharing.org/FAIRsharing.20sbr9) /0.3-RELEASE-2019_06_14",
         "description": "A manually curated registry of standard (URL_TO_INSERT_TERM_1337 https://fairsharing.org/search?fairsharingRegistry=Standard) s, split into three types - Terminology (URL_TO_INSERT_TERM_1348 https://fairsharing.org/search?recordType=terminology_artefact)  Artifacts (ontologies (URL_TO_INSERT_TERM_1350 https://fairsharing.org/search?recordType=terminology_artefact) , e.g. Gene Ontology (URL_TO_INSERT_TERM_1349 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD-NAME_1353 https://fairsharing.org/FAIRsharing.6xq0ee) ), Model (URL_TO_INSERT_TERM_1344 https://fairsharing.org/search?recordType=model_and_format) s and Format (URL_TO_INSERT_TERM_1346 https://fairsharing.org/search?recordType=model_and_format) s (conceptual schema, format (URL_TO_INSERT_TERM_1347 https://fairsharing.org/search?recordType=model_and_format) s, data model (URL_TO_INSERT_TERM_1345 https://fairsharing.org/search?recordType=model_and_format) s, e.g. FASTA (URL_TO_INSERT_RECORD-ABBREV_1354 https://fairsharing.org/FAIRsharing.rz4vfg) ), and Reporting Guideline (URL_TO_INSERT_TERM_1340 https://fairsharing.org/search?recordType=reporting_guideline)  (URL_TO_INSERT_TERM_1351 https://fairsharing.org/search?recordType=reporting_guideline) s (e.g. the ARRIVE (URL_TO_INSERT_RECORD-ABBREV_1355 https://fairsharing.org/FAIRsharing.t58zhj)  guideline (URL_TO_INSERT_TERM_1352 https://fairsharing.org/search?recordType=reporting_guideline) s for in vivo animal testing). These are linked to the database (URL_TO_INSERT_TERM_1338 https://fairsharing.org/search?fairsharingRegistry=Database) s that implement them and the funder (URL_TO_INSERT_TERM_1343 https://fairsharing.org/search?recordType=funder)  and journal (URL_TO_INSERT_TERM_1341 https://fairsharing.org/search?recordType=journal)  publisher (URL_TO_INSERT_TERM_1342 https://fairsharing.org/search?recordType=journal_publisher)  data policies (URL_TO_INSERT_TERM_1339 https://fairsharing.org/search?fairsharingRegistry=Policy)  that recommend or endorse their use.",
         "identifier (URL_TO_INSERT_TERM_1356 https://fairsharing.org/search?recordType=identifier_schema) ": [
           "https://www.fairsharing.org (URL_TO_INSERT_RECORD-HOMEPAGE_1357 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD-HOMEPAGE_1358 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD-HOMEPAGE_1359 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD-HOMEPAGE_1360 https://fairsharing.org/3538) /bsg-sXXXXXX"
         ],
         "keywords": [
           "Standard (URL_TO_INSERT_TERM_1361 https://fairsharing.org/search?fairsharingRegistry=Standard) s",
           "Metadata",
           "Format (URL_TO_INSERT_TERM_1362 https://fairsharing.org/search?recordType=model_and_format) s",
           "Ontologies (URL_TO_INSERT_TERM_1363 https://fairsharing.org/search?recordType=terminology_artefact) ",
           "Terminology (URL_TO_INSERT_TERM_1364 https://fairsharing.org/search?recordType=terminology_artefact)  Artifacts",
           "Reporting Guideline (URL_TO_INSERT_TERM_1365 https://fairsharing.org/search?recordType=reporting_guideline)  (URL_TO_INSERT_TERM_1366 https://fairsharing.org/search?recordType=reporting_guideline) s"
         ],
         "name": "Metadata Standard (URL_TO_INSERT_TERM_1367 https://fairsharing.org/search?fairsharingRegistry=Standard) ",
         "url": "https://fairsharing.org (URL_TO_INSERT_RECORD-HOMEPAGE_1368 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD-HOMEPAGE_1369 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD-HOMEPAGE_1370 https://fairsharing.org/3538) /standards"
       },
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD-HOMEPAGE_1371 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Dataset",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD-HOMEPAGE_1373 https://fairsharing.org/3517) /profiles/Dataset (URL_TO_INSERT_RECORD-HOMEPAGE_1372 https://fairsharing.org/FAIRsharing.20sbr9) /0.3-RELEASE-2019_06_14",
         "description": "A manually curated registry of database (URL_TO_INSERT_TERM_1376 https://fairsharing.org/search?fairsharingRegistry=Database) s/data repositories (URL_TO_INSERT_TERM_1378 https://fairsharing.org/search?recordType=repository) , conforming to the BioDBcore standard (URL_TO_INSERT_TERM_1374 https://fairsharing.org/search?fairsharingRegistry=Standard)  (from the Life Sciences). These are linked to the standard (URL_TO_INSERT_TERM_1375 https://fairsharing.org/search?fairsharingRegistry=Standard) s that they use and the funder (URL_TO_INSERT_TERM_1381 https://fairsharing.org/search?recordType=funder)  and journal (URL_TO_INSERT_TERM_1379 https://fairsharing.org/search?recordType=journal)  publisher (URL_TO_INSERT_TERM_1380 https://fairsharing.org/search?recordType=journal_publisher)  data policies (URL_TO_INSERT_TERM_1377 https://fairsharing.org/search?fairsharingRegistry=Policy)  that recommend or endorse their use.",
         "identifier (URL_TO_INSERT_TERM_1382 https://fairsharing.org/search?recordType=identifier_schema) ": [
           "https://www.fairsharing.org (URL_TO_INSERT_RECORD-HOMEPAGE_1383 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD-HOMEPAGE_1384 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD-HOMEPAGE_1385 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD-HOMEPAGE_1386 https://fairsharing.org/3538) /bsg-dXXXXXX"
         ],
         "keywords": [
           "Database (URL_TO_INSERT_TERM_1387 https://fairsharing.org/search?fairsharingRegistry=Database) ",
           "Data repository (URL_TO_INSERT_TERM_1388 https://fairsharing.org/search?recordType=repository) "
         ],
         "name": "Database (URL_TO_INSERT_TERM_1389 https://fairsharing.org/search?fairsharingRegistry=Database) ",
         "url": "https://fairsharing.org (URL_TO_INSERT_RECORD-HOMEPAGE_1390 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD-HOMEPAGE_1391 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD-HOMEPAGE_1392 https://fairsharing.org/3538) /databases"
       },
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD-HOMEPAGE_1393 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Dataset",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD-HOMEPAGE_1395 https://fairsharing.org/3517) /profiles/Dataset (URL_TO_INSERT_RECORD-HOMEPAGE_1394 https://fairsharing.org/FAIRsharing.20sbr9) /0.3-RELEASE-2019_06_14",
         "description": "A manually curated registry of data policies (URL_TO_INSERT_TERM_1398 https://fairsharing.org/search?fairsharingRegistry=Policy)  from research funder (URL_TO_INSERT_TERM_1402 https://fairsharing.org/search?recordType=funder) s, journal (URL_TO_INSERT_TERM_1399 https://fairsharing.org/search?recordType=journal)  publisher (URL_TO_INSERT_TERM_1401 https://fairsharing.org/search?recordType=journal_publisher) s, societies (URL_TO_INSERT_TERM_1400 https://fairsharing.org/search?recordType=society) , and other organisations. These are linked to the database (URL_TO_INSERT_TERM_1397 https://fairsharing.org/search?fairsharingRegistry=Database) s and standard (URL_TO_INSERT_TERM_1396 https://fairsharing.org/search?fairsharingRegistry=Standard) s that they recommend for use",
         "identifier (URL_TO_INSERT_TERM_1403 https://fairsharing.org/search?recordType=identifier_schema) ": [
           "https://www.fairsharing.org (URL_TO_INSERT_RECORD-HOMEPAGE_1404 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD-HOMEPAGE_1405 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD-HOMEPAGE_1406 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD-HOMEPAGE_1407 https://fairsharing.org/3538) /bsg-pXXXXXX"
         ],
         "keywords": [
           "Data policy (URL_TO_INSERT_TERM_1408 https://fairsharing.org/search?fairsharingRegistry=Policy) ",
           "journal (URL_TO_INSERT_TERM_1409 https://fairsharing.org/search?recordType=journal) ",
           "funder (URL_TO_INSERT_TERM_1410 https://fairsharing.org/search?recordType=funder) ",
           "society (URL_TO_INSERT_TERM_1411 https://fairsharing.org/search?recordType=society) "
         ],
         "name": "Data Policy (URL_TO_INSERT_TERM_1412 https://fairsharing.org/search?fairsharingRegistry=Policy) ",
         "url": "https://fairsharing.org (URL_TO_INSERT_RECORD-HOMEPAGE_1413 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD-HOMEPAGE_1414 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD-HOMEPAGE_1415 https://fairsharing.org/3538) /policies"
       }
     ],
     "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD-HOMEPAGE_1417 https://fairsharing.org/3517) /profiles/DataCatalog/0.3-RELEASE-2019_07_01 (URL_TO_INSERT_RECORD-HOMEPAGE_1416 https://fairsharing.org/FAIRsharing.2037b2) ",
     "description": "A manually curated, informat (URL_TO_INSERT_TERM_1425 https://fairsharing.org/search?recordType=model_and_format) ive and educational resource on data and metadata standard (URL_TO_INSERT_TERM_1418 https://fairsharing.org/search?fairsharingRegistry=Standard) s, inter-related to database (URL_TO_INSERT_TERM_1419 https://fairsharing.org/search?fairsharingRegistry=Database) s/data repositories (URL_TO_INSERT_TERM_1421 https://fairsharing.org/search?recordType=repository)  and funder (URL_TO_INSERT_TERM_1424 https://fairsharing.org/search?recordType=funder)  and journal (URL_TO_INSERT_TERM_1422 https://fairsharing.org/search?recordType=journal)  publisher (URL_TO_INSERT_TERM_1423 https://fairsharing.org/search?recordType=journal_publisher)  data policies (URL_TO_INSERT_TERM_1420 https://fairsharing.org/search?fairsharingRegistry=Policy)  from across disciplines. FAIRsharing (URL_TO_INSERT_RECORD-NAME_1427 https://fairsharing.org/FAIRsharing.2abjs5)  is an ELIXIR-UK node resource and has an active role in the RDA (URL_TO_INSERT_RECORD-ABBREV_1426 https://fairsharing.org/FAIRsharing.2g5kcb)  and Force11 data initiatives.",
     "identifier (URL_TO_INSERT_TERM_1428 https://fairsharing.org/search?recordType=identifier_schema) ": [
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
     "name": "FAIRsharing (URL_TO_INSERT_RECORD-NAME_1429 https://fairsharing.org/FAIRsharing.2abjs5) .org",
     "provider": [
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD-HOMEPAGE_1430 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Organization",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD-HOMEPAGE_1431 https://fairsharing.org/3517) /profiles/Organization/0.2-DRAFT-2019_07_19",
         "description": "",
         "name": "FAIRsharing (URL_TO_INSERT_RECORD-NAME_1432 https://fairsharing.org/FAIRsharing.2abjs5) .org Registry"
       }
     ],
     "url": "https://fairsharing.org (URL_TO_INSERT_RECORD-HOMEPAGE_1433 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD-HOMEPAGE_1434 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD-HOMEPAGE_1435 https://fairsharing.org/3538) /"
   }
   </script >
   ```
   
5. Download or copy and paste the generated markup
   
6. Make adjustments for any bits that could not be properly entered through the form. 
   
   For example, for our generated markup we would change the `provider` so that it provides a direct link rather than repeating the properties. We would replace

   ```
   "provider": [
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD-HOMEPAGE_1436 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Organization",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD-HOMEPAGE_1437 https://fairsharing.org/3517) /profiles/Organization/0.2-DRAFT-2019_07_19",
         "description": "",
         "name": "FAIRsharing (URL_TO_INSERT_RECORD-NAME_1438 https://fairsharing.org/FAIRsharing.2abjs5) .org Registry"
       }
     ],
   ```
   
   with

   ```
   "provider": [
       {
         "@type": "Organization",
         "@id": "https://fairsharing.org (URL_TO_INSERT_RECORD-HOMEPAGE_1439 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD-HOMEPAGE_1440 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD-HOMEPAGE_1441 https://fairsharing.org/3538) /communities"
       }
     ],
   ```
   
   You can test that your JSON (URL_TO_INSERT_RECORD-ABBREV_1442 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD-ABBREV_1443 https://fairsharing.org/FAIRsharing.8f9bbb)  is valid syntax, and visualise your markup using the [JSON-LD Playground](https://json-ld.org/playground/).

7. Once you are happy with your markup, include the `JSON (URL_TO_INSERT_RECORD-ABBREV_1444 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD-ABBREV_1446 https://fairsharing.org/FAIRsharing.8f9bbb) `, script tags and all, at the bottom of your HTML (URL_TO_INSERT_RECORD-ABBREV_1445 https://fairsharing.org/FAIRsharing.YugnuL)  page template. 

   Make sure that this is before the closing `</html>` tag.
   
   Your site should now include DataCatalog markup. 
   
   Once you have deployed this on your web server, you can test it with the [Bioschemas Validator](https://www.macs.hw.ac.uk/SWeL/BioschemasValidator/) which scrapes the markup from your page and allows you to test it against various Bioschemas (URL_TO_INSERT_RECORD-NAME_1447 https://fairsharing.org/3517)  profiles<sup>[1](#biosche (URL_TO_INSERT_RECORD-NAME_1448 https://fairsharing.org/3517) mas-validator)</sup>.

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


