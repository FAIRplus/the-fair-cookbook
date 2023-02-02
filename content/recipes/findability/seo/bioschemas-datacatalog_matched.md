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

> To embed `Schema.org (URL_TO_INSERT_RECORD_2353 https://fairsharing.org/FAIRsharing.hzdzq8) ` markup in a web page that publishes multiple datasets in a single page.


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
alt: The process of annotating a data catalog webpage with bioschema markup for Search (URL_TO_INSERT_RECORD_2354 https://fairsharing.org/FAIRsharing.52b22c)  Engine discovery
---
The process of annotating a data catalog webpage with bioschema markup for Search (URL_TO_INSERT_RECORD_2355 https://fairsharing.org/FAIRsharing.52b22c)  Engine discovery.
```
````


---

## Method

We will outline the steps for marking up a page in your site that is about multiple datasets. The resulting markup will be compliant with both [Google's Dataset markup guidelines](https://developers.google.com/search/docs/data-types/dataset#publication) and the [Bioschemas (URL_TO_INSERT_RECORD_2357 https://fairsharing.org/3517)  DataCatalog Profile (URL_TO_INSERT_RECORD_2356 https://fairsharing.org/FAIRsharing.2037b2) ](https://bioschemas.org (URL_TO_INSERT_RECORD_2358 https://fairsharing.org/3517) /profiles/DataCatalog). 

We will use [FAIRsharing](https://fairsharing.org (URL_TO_INSERT_RECORD_2359 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2360 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2361 https://fairsharing.org/3538) /) as an example for this recipe which makes three datasets available within its markup.

1. Identify the page in your site about a specific dataset, e.g. https://fairsharing.org (URL_TO_INSERT_RECORD_2362 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2363 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2364 https://fairsharing.org/3538) /

2. Open the  [Bioschemas (URL_TO_INSERT_RECORD_2365 https://fairsharing.org/3517)  Generator](https://www.macs.hw.ac.uk/SWeL/BioschemasGenerator/)

   1.  Select `DataCatalog` from the Bioschemas (URL_TO_INSERT_RECORD_2366 https://fairsharing.org/3517)  Profile dropdown

   2.  Enter the URL (URL_TO_INSERT_RECORD_2367 https://fairsharing.org/FAIRsharing.9d38e2)  of the page in URL (URL_TO_INSERT_RECORD_2368 https://fairsharing.org/FAIRsharing.9d38e2)  box, e.g. `https://fairsharing.org (URL_TO_INSERT_RECORD_2369 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2370 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2371 https://fairsharing.org/3538) /`

   3.  Click on the `Show Form` button
   
   ````{dropdown} 
   :open:
   ```{figure} Bioschemas (URL_TO_INSERT_RECORD_2372 https://fairsharing.org/3517) Generator.png
   ---
   name: bioschemas (URL_TO_INSERT_RECORD_2373 https://fairsharing.org/3517) -generator-start-screen-1
   alt: Bioschemas (URL_TO_INSERT_RECORD_2374 https://fairsharing.org/3517)  Generator start screen.
   
   ---
   Bioschemas (URL_TO_INSERT_RECORD_2375 https://fairsharing.org/3517)  Generator start screen.
   ```
   ````

3. Complete the profile form with the informat (URL_TO_INSERT_TERM_2376 https://fairsharing.org/search?recordType=model_and_format) ion relevant for your page. Once completed, click on the `Generate Markup`  button

   - You should complete all *Minimum* properties and as many *Recommended* properties as possible. You can show/hide properties using the `Additional Properties` buttons.
   - Where possible you should link to other resources. The Bioschemas (URL_TO_INSERT_RECORD_2377 https://fairsharing.org/3517)  Generator does not make this as simple as it could, but you can do it in step 5 once you have generated your markup, e.g. our dataset will link to a page with DataCatalog markup in rather than repeating all the properties for now we will just enter a `url` and no other properties.
     - If there are separate pages for your datasets then you should link to them using an `@id` link
     - Otherwise, you can include the markup within the `DataCatalog` markup
   - The form defaults to the data type with the first alphabetical character, e.g. for `identifier (URL_TO_INSERT_TERM_2378 https://fairsharing.org/search?recordType=identifier_schema) `, this defaults to `PropertyValue` but `Text` or `URL (URL_TO_INSERT_RECORD_2379 https://fairsharing.org/FAIRsharing.9d38e2)  ` will be more appropriate in most cases
   - The right side of the screen gives examples for properties, where these have been provided by the Bioschemas (URL_TO_INSERT_RECORD_2380 https://fairsharing.org/3517)  profile authors. Click on the `Show` button to see the example for a specific property. Click on `Minimum`, `Recommended`, or `Optional` to expand/contract the section and see the properties contained at that marginality level

   ````{dropdown} 
   :open:
   ```{figure} Bioschemas (URL_TO_INSERT_RECORD_2381 https://fairsharing.org/3517) GeneratorDataCatalogForm.png
   ---
   height: 550px
   name: Bioschemas (URL_TO_INSERT_RECORD_2382 https://fairsharing.org/3517)  Generator DataCatalog profile form
   alt: Bioschemas (URL_TO_INSERT_RECORD_2383 https://fairsharing.org/3517)  Generator DataCatalog profile form
   ---
   Bioschemas (URL_TO_INSERT_RECORD_2384 https://fairsharing.org/3517)  Generator DataCatalog profile form.
   ```   
   ````

4. You will now see the generated markup in `JSO (URL_TO_INSERT_RECORD_2390 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_2388 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2393 https://fairsharing.org/FAIRsharing.8f9bbb) ` format (URL_TO_INSERT_TERM_2385 https://fairsharing.org/search?recordType=model_and_format) . You can click on the `Microdata` and `RDF (URL_TO_INSERT_RECORD_2387 https://fairsharing.org/FAIRsharing.p77ph9) a (URL_TO_INSERT_RECORD_2392 https://fairsharing.org/663) ` tabs to see the same content rendered in the different format (URL_TO_INSERT_TERM_2386 https://fairsharing.org/search?recordType=model_and_format) s. However, we recommend the use of `JSO (URL_TO_INSERT_RECORD_2391 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_2389 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2394 https://fairsharing.org/FAIRsharing.8f9bbb) `. For our FAIR (URL_TO_INSERT_RECORD_2396 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_2395 https://fairsharing.org/FAIRsharing.2abjs5) .org example, we get the following markup

   ```
   <script type="application/ld+json" >
   {
     "@context": "https://schema.org (URL_TO_INSERT_RECORD_2397 https://fairsharing.org/FAIRsharing.hzdzq8) ",
     "@id": "https://fairsharing.org (URL_TO_INSERT_RECORD_2398 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2399 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2400 https://fairsharing.org/3538) /",
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
         "@context": "https://schema.org (URL_TO_INSERT_RECORD_2401 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Dataset",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2403 https://fairsharing.org/3517) /profiles/Dataset (URL_TO_INSERT_RECORD_2402 https://fairsharing.org/FAIRsharing.20sbr9) /0.3-RELEASE-2019_06_14",
         "description": "A manually curated registry of standard (URL_TO_INSERT_TERM_2404 https://fairsharing.org/search?fairsharingRegistry=Standard) s, split into three types - Terminology (URL_TO_INSERT_TERM_2415 https://fairsharing.org/search?recordType=terminology_artefact)  Artifacts (ontologies (URL_TO_INSERT_TERM_2417 https://fairsharing.org/search?recordType=terminology_artefact) , e.g. Gene Ontology (URL_TO_INSERT_TERM_2416 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_2420 https://fairsharing.org/FAIRsharing.6xq0ee) ), Model (URL_TO_INSERT_TERM_2411 https://fairsharing.org/search?recordType=model_and_format) s and Format (URL_TO_INSERT_TERM_2413 https://fairsharing.org/search?recordType=model_and_format) s (conceptual schema, format (URL_TO_INSERT_TERM_2414 https://fairsharing.org/search?recordType=model_and_format) s, data model (URL_TO_INSERT_TERM_2412 https://fairsharing.org/search?recordType=model_and_format) s, e.g. FAST (URL_TO_INSERT_RECORD_2421 https://fairsharing.org/FAIRsharing.p5df9c) A (URL_TO_INSERT_RECORD_2422 https://fairsharing.org/FAIRsharing.rz4vfg) ), and Reporting Guideline (URL_TO_INSERT_TERM_2407 https://fairsharing.org/search?recordType=reporting_guideline)  (URL_TO_INSERT_TERM_2418 https://fairsharing.org/search?recordType=reporting_guideline) s (e.g. the ARRIVE (URL_TO_INSERT_RECORD_2423 https://fairsharing.org/FAIRsharing.t58zhj)  guideline (URL_TO_INSERT_TERM_2419 https://fairsharing.org/search?recordType=reporting_guideline) s for in vivo animal testing). These are linked to the database (URL_TO_INSERT_TERM_2405 https://fairsharing.org/search?fairsharingRegistry=Database) s that implement them and the funder (URL_TO_INSERT_TERM_2410 https://fairsharing.org/search?recordType=funder)  and journal (URL_TO_INSERT_TERM_2408 https://fairsharing.org/search?recordType=journal)  publisher (URL_TO_INSERT_TERM_2409 https://fairsharing.org/search?recordType=journal_publisher)  data policies (URL_TO_INSERT_TERM_2406 https://fairsharing.org/search?fairsharingRegistry=Policy)  that recommend or endorse their use.",
         "identifier (URL_TO_INSERT_TERM_2424 https://fairsharing.org/search?recordType=identifier_schema) ": [
           "https://www.fairsharing.org (URL_TO_INSERT_RECORD_2425 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD_2426 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2427 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2428 https://fairsharing.org/3538) /bsg-sXXXXXX"
         ],
         "keywords": [
           "Standard (URL_TO_INSERT_TERM_2429 https://fairsharing.org/search?fairsharingRegistry=Standard) s",
           "Metadata",
           "Format (URL_TO_INSERT_TERM_2430 https://fairsharing.org/search?recordType=model_and_format) s",
           "Ontologies (URL_TO_INSERT_TERM_2431 https://fairsharing.org/search?recordType=terminology_artefact) ",
           "Terminology (URL_TO_INSERT_TERM_2432 https://fairsharing.org/search?recordType=terminology_artefact)  Artifacts",
           "Reporting Guideline (URL_TO_INSERT_TERM_2433 https://fairsharing.org/search?recordType=reporting_guideline)  (URL_TO_INSERT_TERM_2434 https://fairsharing.org/search?recordType=reporting_guideline) s"
         ],
         "name": "Metadata Standard (URL_TO_INSERT_TERM_2435 https://fairsharing.org/search?fairsharingRegistry=Standard) ",
         "url": "https://fairsharing.org (URL_TO_INSERT_RECORD_2436 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2437 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2438 https://fairsharing.org/3538) /standards"
       },
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD_2439 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Dataset",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2441 https://fairsharing.org/3517) /profiles/Dataset (URL_TO_INSERT_RECORD_2440 https://fairsharing.org/FAIRsharing.20sbr9) /0.3-RELEASE-2019_06_14",
         "description": "A manually curated registry of database (URL_TO_INSERT_TERM_2444 https://fairsharing.org/search?fairsharingRegistry=Database) s/data repositories (URL_TO_INSERT_TERM_2446 https://fairsharing.org/search?recordType=repository) , conforming to the BioDBcore (URL_TO_INSERT_RECORD_2450 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_2451 https://fairsharing.org/FAIRsharing.xMmOCL)  standard (URL_TO_INSERT_TERM_2442 https://fairsharing.org/search?fairsharingRegistry=Standard)  (from the Life Sciences). These are linked to the standard (URL_TO_INSERT_TERM_2443 https://fairsharing.org/search?fairsharingRegistry=Standard) s that they use and the funder (URL_TO_INSERT_TERM_2449 https://fairsharing.org/search?recordType=funder)  and journal (URL_TO_INSERT_TERM_2447 https://fairsharing.org/search?recordType=journal)  publisher (URL_TO_INSERT_TERM_2448 https://fairsharing.org/search?recordType=journal_publisher)  data policies (URL_TO_INSERT_TERM_2445 https://fairsharing.org/search?fairsharingRegistry=Policy)  that recommend or endorse their use.",
         "identifier (URL_TO_INSERT_TERM_2452 https://fairsharing.org/search?recordType=identifier_schema) ": [
           "https://www.fairsharing.org (URL_TO_INSERT_RECORD_2453 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD_2454 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2455 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2456 https://fairsharing.org/3538) /bsg-dXXXXXX"
         ],
         "keywords": [
           "Database (URL_TO_INSERT_TERM_2457 https://fairsharing.org/search?fairsharingRegistry=Database) ",
           "Data repository (URL_TO_INSERT_TERM_2458 https://fairsharing.org/search?recordType=repository) "
         ],
         "name": "Database (URL_TO_INSERT_TERM_2459 https://fairsharing.org/search?fairsharingRegistry=Database) ",
         "url": "https://fairsharing.org (URL_TO_INSERT_RECORD_2460 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2461 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2462 https://fairsharing.org/3538) /databases"
       },
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD_2463 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Dataset",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2465 https://fairsharing.org/3517) /profiles/Dataset (URL_TO_INSERT_RECORD_2464 https://fairsharing.org/FAIRsharing.20sbr9) /0.3-RELEASE-2019_06_14",
         "description": "A manually curated registry of data policies (URL_TO_INSERT_TERM_2468 https://fairsharing.org/search?fairsharingRegistry=Policy)  from research (URL_TO_INSERT_RECORD_2473 https://fairsharing.org/FAIRsharing.52b22c)  funder (URL_TO_INSERT_TERM_2472 https://fairsharing.org/search?recordType=funder) s, journal (URL_TO_INSERT_TERM_2469 https://fairsharing.org/search?recordType=journal)  publisher (URL_TO_INSERT_TERM_2471 https://fairsharing.org/search?recordType=journal_publisher) s, societies (URL_TO_INSERT_TERM_2470 https://fairsharing.org/search?recordType=society) , and other organisations. These are linked to the database (URL_TO_INSERT_TERM_2467 https://fairsharing.org/search?fairsharingRegistry=Database) s and standard (URL_TO_INSERT_TERM_2466 https://fairsharing.org/search?fairsharingRegistry=Standard) s that they recommend for use",
         "identifier (URL_TO_INSERT_TERM_2474 https://fairsharing.org/search?recordType=identifier_schema) ": [
           "https://www.fairsharing.org (URL_TO_INSERT_RECORD_2475 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD_2476 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2477 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2478 https://fairsharing.org/3538) /bsg-pXXXXXX"
         ],
         "keywords": [
           "Data policy (URL_TO_INSERT_TERM_2479 https://fairsharing.org/search?fairsharingRegistry=Policy) ",
           "journal (URL_TO_INSERT_TERM_2480 https://fairsharing.org/search?recordType=journal) ",
           "funder (URL_TO_INSERT_TERM_2481 https://fairsharing.org/search?recordType=funder) ",
           "society (URL_TO_INSERT_TERM_2482 https://fairsharing.org/search?recordType=society) "
         ],
         "name": "Data Policy (URL_TO_INSERT_TERM_2483 https://fairsharing.org/search?fairsharingRegistry=Policy) ",
         "url": "https://fairsharing.org (URL_TO_INSERT_RECORD_2484 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2485 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2486 https://fairsharing.org/3538) /policies"
       }
     ],
     "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2488 https://fairsharing.org/3517) /profiles/DataCatalog/0.3-RELEASE-2019_07_01 (URL_TO_INSERT_RECORD_2487 https://fairsharing.org/FAIRsharing.2037b2) ",
     "description": "A manually curated, informat (URL_TO_INSERT_TERM_2496 https://fairsharing.org/search?recordType=model_and_format) ive and educational resource on data and metadata standard (URL_TO_INSERT_TERM_2489 https://fairsharing.org/search?fairsharingRegistry=Standard) s, inter-related to database (URL_TO_INSERT_TERM_2490 https://fairsharing.org/search?fairsharingRegistry=Database) s/data repositories (URL_TO_INSERT_TERM_2492 https://fairsharing.org/search?recordType=repository)  and funder (URL_TO_INSERT_TERM_2495 https://fairsharing.org/search?recordType=funder)  and journal (URL_TO_INSERT_TERM_2493 https://fairsharing.org/search?recordType=journal)  publisher (URL_TO_INSERT_TERM_2494 https://fairsharing.org/search?recordType=journal_publisher)  data policies (URL_TO_INSERT_TERM_2491 https://fairsharing.org/search?fairsharingRegistry=Policy)  from across disciplines. FAIR (URL_TO_INSERT_RECORD_2499 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_2498 https://fairsharing.org/FAIRsharing.2abjs5)  is an ELIXIR-UK node resource and has an active role in the RDA (URL_TO_INSERT_RECORD_2497 https://fairsharing.org/FAIRsharing.2g5kcb)  and Force11 data initiatives.",
     "identifier (URL_TO_INSERT_TERM_2500 https://fairsharing.org/search?recordType=identifier_schema) ": [
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
     "name": "FAIR (URL_TO_INSERT_RECORD_2502 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_2501 https://fairsharing.org/FAIRsharing.2abjs5) .org",
     "provider": [
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD_2503 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Organization",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2504 https://fairsharing.org/3517) /profiles/Organization/0.2-DRAFT-2019_07_19",
         "description": "",
         "name": "FAIR (URL_TO_INSERT_RECORD_2506 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_2505 https://fairsharing.org/FAIRsharing.2abjs5) .org Registry"
       }
     ],
     "url": "https://fairsharing.org (URL_TO_INSERT_RECORD_2507 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2508 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2509 https://fairsharing.org/3538) /"
   }
   </script >
   ```
   
5. Download or copy and paste the generated markup
   
6. Make adjustments for any bits that could not be properly entered through the form. 
   
   For example, for our generated markup we would change the `provider` so that it provides a direct link rather than repeating the properties. We would replace

   ```
   "provider": [
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD_2510 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Organization",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2511 https://fairsharing.org/3517) /profiles/Organization/0.2-DRAFT-2019_07_19",
         "description": "",
         "name": "FAIR (URL_TO_INSERT_RECORD_2513 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_2512 https://fairsharing.org/FAIRsharing.2abjs5) .org Registry"
       }
     ],
   ```
   
   with

   ```
   "provider": [
       {
         "@type": "Organization",
         "@id": "https://fairsharing.org (URL_TO_INSERT_RECORD_2514 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2515 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2516 https://fairsharing.org/3538) /communities"
       }
     ],
   ```
   
   You can test that your JSO (URL_TO_INSERT_RECORD_2519 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_2517 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2521 https://fairsharing.org/FAIRsharing.8f9bbb)  is valid syntax, and visualise your markup using the [JSO (URL_TO_INSERT_RECORD_2520 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_2518 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2522 https://fairsharing.org/FAIRsharing.8f9bbb)  Playground](https://json-ld.org/playground/).

7. Once you are happy with your markup, include the `JSO (URL_TO_INSERT_RECORD_2524 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_2523 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2525 https://fairsharing.org/FAIRsharing.8f9bbb) `, script tags and all, at the bottom of your HTML (URL_TO_INSERT_RECORD_2526 https://fairsharing.org/FAIRsharing.YugnuL)  page template. 

   Make sure that this is before the closing `</html>` tag.
   
   Your site should now include DataCatalog markup. 
   
   Once you have deployed this on your web server, you can test it with the [Bioschemas (URL_TO_INSERT_RECORD_2527 https://fairsharing.org/3517)  Validator](https://www.macs.hw.ac.uk/SWeL/BioschemasValidator/) which scrapes the markup from your page and allows you to test it against various Bioschemas (URL_TO_INSERT_RECORD_2528 https://fairsharing.org/3517)  profiles<sup>[1](#bioschemas (URL_TO_INSERT_RECORD_2529 https://fairsharing.org/3517) -validator)</sup>.

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


