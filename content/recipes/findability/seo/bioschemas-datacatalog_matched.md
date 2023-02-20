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

> To embed `Schema.org (URL_TO_INSERT_RECORD-NAME_712 https://fairsharing.org/FAIRsharing.hzdzq8) ` markup in a web page that publishes multiple datasets in a single page.


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

We will outline the steps for marking up a page in your site that is about multiple datasets. The resulting markup will be compliant with both [Google's Dataset markup guidelines](https://developers.google.com/search/docs/data-types/dataset#publication) and the [Bioschemas (URL_TO_INSERT_RECORD-NAME_714 https://fairsharing.org/3517)  DataCatalog Profile (URL_TO_INSERT_RECORD-NAME_713 https://fairsharing.org/FAIRsharing.2037b2) ](https://bioschemas.org/profiles/DataCatalog). 

We will use [FAIRsharing](https://fairsharing.org/) as an example for this recipe which makes three datasets available within its markup.

1. Identify the page in your site about a specific dataset, e.g. https://fairsharing.org (URL_TO_INSERT_RECORD-HOMEPAGE_715 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD-HOMEPAGE_716 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD-HOMEPAGE_717 https://fairsharing.org/3538) /

2. Open the  [Bioschemas Generator](https://www.macs.hw.ac.uk/SWeL/BioschemasGenerator/)

   1.  Select `DataCatalog` from the Bioschemas (URL_TO_INSERT_RECORD-NAME_718 https://fairsharing.org/3517)  Profile dropdown

   2.  Enter the URL (URL_TO_INSERT_RECORD-ABBREV_719 https://fairsharing.org/FAIRsharing.9d38e2)  of the page in URL (URL_TO_INSERT_RECORD-ABBREV_720 https://fairsharing.org/FAIRsharing.9d38e2)  box, e.g. `https://fairsharing.org (URL_TO_INSERT_RECORD-HOMEPAGE_721 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD-HOMEPAGE_722 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD-HOMEPAGE_723 https://fairsharing.org/3538) /`

   3.  Click on the `Show Form` button
   
   ````{dropdown} 
   :open:
   ```{figure} BioschemasGenerator.png
   ---
   name: bioschemas (URL_TO_INSERT_RECORD-NAME_724 https://fairsharing.org/3517) -generator-start-screen-1
   alt: Bioschemas (URL_TO_INSERT_RECORD-NAME_725 https://fairsharing.org/3517)  Generator start screen.
   
   ---
   Bioschemas (URL_TO_INSERT_RECORD-NAME_726 https://fairsharing.org/3517)  Generator start screen.
   ```
   ````

3. Complete the profile form with the information relevant for your page. Once completed, click on the `Generate Markup`  button

   - You should complete all *Minimum* properties and as many *Recommended* properties as possible. You can show/hide properties using the `Additional Properties` buttons.
   - Where possible you should link to other resources. The Bioschemas (URL_TO_INSERT_RECORD-NAME_727 https://fairsharing.org/3517)  Generator does not make this as simple as it could, but you can do it in step 5 once you have generated your markup, e.g. our dataset will link to a page with DataCatalog markup in rather than repeating all the properties for now we will just enter a `url` and no other properties.
     - If there are separate pages for your datasets then you should link to them using an `@id` link
     - Otherwise, you can include the markup within the `DataCatalog` markup
   - The form defaults to the data type with the first alphabetical character, e.g. for `identifier`, this defaults to `PropertyValue` but `Text` or `URL (URL_TO_INSERT_RECORD-ABBREV_728 https://fairsharing.org/FAIRsharing.9d38e2)  ` will be more appropriate in most cases
   - The right side of the screen gives examples for properties, where these have been provided by the Bioschemas (URL_TO_INSERT_RECORD-NAME_729 https://fairsharing.org/3517)  profile authors. Click on the `Show` button to see the example for a specific property. Click on `Minimum`, `Recommended`, or `Optional` to expand/contract the section and see the properties contained at that marginality level

   ````{dropdown} 
   :open:
   ```{figure} BioschemasGeneratorDataCatalogForm.png
   ---
   height: 550px
   name: Bioschemas (URL_TO_INSERT_RECORD-NAME_730 https://fairsharing.org/3517)  Generator DataCatalog profile form
   alt: Bioschemas (URL_TO_INSERT_RECORD-NAME_731 https://fairsharing.org/3517)  Generator DataCatalog profile form
   ---
   Bioschemas (URL_TO_INSERT_RECORD-NAME_732 https://fairsharing.org/3517)  Generator DataCatalog profile form.
   ```   
   ````

4. You will now see the generated markup in `JSON (URL_TO_INSERT_RECORD-ABBREV_733 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD-ABBREV_736 https://fairsharing.org/FAIRsharing.8f9bbb) ` format. You can click on the `Microdata` and `RDFa (URL_TO_INSERT_RECORD-ABBREV_735 https://fairsharing.org/663) ` tabs to see the same content rendered in the different formats. However, we recommend the use of `JSON (URL_TO_INSERT_RECORD-ABBREV_734 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD-ABBREV_737 https://fairsharing.org/FAIRsharing.8f9bbb) `. For our FAIRsharing (URL_TO_INSERT_RECORD-NAME_738 https://fairsharing.org/FAIRsharing.2abjs5) .org example, we get the following markup

   ```
   <script type="application/ld+json" >
   {
     "@context": "https://schema.org (URL_TO_INSERT_RECORD-HOMEPAGE_739 https://fairsharing.org/FAIRsharing.hzdzq8) ",
     "@id": "https://fairsharing.org (URL_TO_INSERT_RECORD-HOMEPAGE_740 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD-HOMEPAGE_741 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD-HOMEPAGE_742 https://fairsharing.org/3538) /",
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
         "@context": "https://schema.org (URL_TO_INSERT_RECORD-HOMEPAGE_743 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Dataset",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD-HOMEPAGE_745 https://fairsharing.org/3517) /profiles/Dataset (URL_TO_INSERT_RECORD-HOMEPAGE_744 https://fairsharing.org/FAIRsharing.20sbr9) /0.3-RELEASE-2019_06_14",
         "description": "A manually curated registry of standards, split into three types - Terminology Artifacts (ontologies, e.g. Gene Ontology (URL_TO_INSERT_RECORD-NAME_746 https://fairsharing.org/FAIRsharing.6xq0ee) ), Models and Formats (conceptual schema, formats, data models, e.g. FASTA (URL_TO_INSERT_RECORD-ABBREV_747 https://fairsharing.org/FAIRsharing.rz4vfg) ), and Reporting Guidelines (e.g. the ARRIVE (URL_TO_INSERT_RECORD-ABBREV_748 https://fairsharing.org/FAIRsharing.t58zhj)  guidelines for in vivo animal testing). These are linked to the databases that implement them and the funder and journal publisher data policies that recommend or endorse their use.",
         "identifier": [
           "https://www.fairsharing.org (URL_TO_INSERT_RECORD-HOMEPAGE_749 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD-HOMEPAGE_750 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD-HOMEPAGE_751 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD-HOMEPAGE_752 https://fairsharing.org/3538) /bsg-sXXXXXX"
         ],
         "keywords": [
           "Standards",
           "Metadata",
           "Formats",
           "Ontologies",
           "Terminology Artifacts",
           "Reporting Guidelines"
         ],
         "name": "Metadata Standard",
         "url": "https://fairsharing.org (URL_TO_INSERT_RECORD-HOMEPAGE_753 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD-HOMEPAGE_754 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD-HOMEPAGE_755 https://fairsharing.org/3538) /standards"
       },
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD-HOMEPAGE_756 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Dataset",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD-HOMEPAGE_758 https://fairsharing.org/3517) /profiles/Dataset (URL_TO_INSERT_RECORD-HOMEPAGE_757 https://fairsharing.org/FAIRsharing.20sbr9) /0.3-RELEASE-2019_06_14",
         "description": "A manually curated registry of databases/data repositories, conforming to the BioDBcore standard (from the Life Sciences). These are linked to the standards that they use and the funder and journal publisher data policies that recommend or endorse their use.",
         "identifier": [
           "https://www.fairsharing.org (URL_TO_INSERT_RECORD-HOMEPAGE_759 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD-HOMEPAGE_760 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD-HOMEPAGE_761 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD-HOMEPAGE_762 https://fairsharing.org/3538) /bsg-dXXXXXX"
         ],
         "keywords": [
           "Database",
           "Data repository"
         ],
         "name": "Database",
         "url": "https://fairsharing.org (URL_TO_INSERT_RECORD-HOMEPAGE_763 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD-HOMEPAGE_764 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD-HOMEPAGE_765 https://fairsharing.org/3538) /databases"
       },
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD-HOMEPAGE_766 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Dataset",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD-HOMEPAGE_768 https://fairsharing.org/3517) /profiles/Dataset (URL_TO_INSERT_RECORD-HOMEPAGE_767 https://fairsharing.org/FAIRsharing.20sbr9) /0.3-RELEASE-2019_06_14",
         "description": "A manually curated registry of data policies from research funders, journal publishers, societies, and other organisations. These are linked to the databases and standards that they recommend for use",
         "identifier": [
           "https://www.fairsharing.org (URL_TO_INSERT_RECORD-HOMEPAGE_769 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD-HOMEPAGE_770 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD-HOMEPAGE_771 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD-HOMEPAGE_772 https://fairsharing.org/3538) /bsg-pXXXXXX"
         ],
         "keywords": [
           "Data policy",
           "journal",
           "funder",
           "society"
         ],
         "name": "Data Policy",
         "url": "https://fairsharing.org (URL_TO_INSERT_RECORD-HOMEPAGE_773 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD-HOMEPAGE_774 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD-HOMEPAGE_775 https://fairsharing.org/3538) /policies"
       }
     ],
     "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD-HOMEPAGE_777 https://fairsharing.org/3517) /profiles/DataCatalog/0.3-RELEASE-2019_07_01 (URL_TO_INSERT_RECORD-HOMEPAGE_776 https://fairsharing.org/FAIRsharing.2037b2) ",
     "description": "A manually curated, informative and educational resource on data and metadata standards, inter-related to databases/data repositories and funder and journal publisher data policies from across disciplines. FAIRsharing (URL_TO_INSERT_RECORD-NAME_779 https://fairsharing.org/FAIRsharing.2abjs5)  is an ELIXIR-UK node resource and has an active role in the RDA (URL_TO_INSERT_RECORD-ABBREV_778 https://fairsharing.org/FAIRsharing.2g5kcb)  and Force11 data initiatives.",
     "identifier": [
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
     "name": "FAIRsharing (URL_TO_INSERT_RECORD-NAME_780 https://fairsharing.org/FAIRsharing.2abjs5) .org",
     "provider": [
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD-HOMEPAGE_781 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Organization",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD-HOMEPAGE_782 https://fairsharing.org/3517) /profiles/Organization/0.2-DRAFT-2019_07_19",
         "description": "",
         "name": "FAIRsharing (URL_TO_INSERT_RECORD-NAME_783 https://fairsharing.org/FAIRsharing.2abjs5) .org Registry"
       }
     ],
     "url": "https://fairsharing.org (URL_TO_INSERT_RECORD-HOMEPAGE_784 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD-HOMEPAGE_785 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD-HOMEPAGE_786 https://fairsharing.org/3538) /"
   }
   </script >
   ```
   
5. Download or copy and paste the generated markup
   
6. Make adjustments for any bits that could not be properly entered through the form. 
   
   For example, for our generated markup we would change the `provider` so that it provides a direct link rather than repeating the properties. We would replace

   ```
   "provider": [
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD-HOMEPAGE_787 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Organization",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD-HOMEPAGE_788 https://fairsharing.org/3517) /profiles/Organization/0.2-DRAFT-2019_07_19",
         "description": "",
         "name": "FAIRsharing (URL_TO_INSERT_RECORD-NAME_789 https://fairsharing.org/FAIRsharing.2abjs5) .org Registry"
       }
     ],
   ```
   
   with

   ```
   "provider": [
       {
         "@type": "Organization",
         "@id": "https://fairsharing.org (URL_TO_INSERT_RECORD-HOMEPAGE_790 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD-HOMEPAGE_791 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD-HOMEPAGE_792 https://fairsharing.org/3538) /communities"
       }
     ],
   ```
   
   You can test that your JSON (URL_TO_INSERT_RECORD-ABBREV_793 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD-ABBREV_794 https://fairsharing.org/FAIRsharing.8f9bbb)  is valid syntax, and visualise your markup using the [JSON-LD Playground](https://json-ld.org/playground/).

7. Once you are happy with your markup, include the `JSON (URL_TO_INSERT_RECORD-ABBREV_795 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD-ABBREV_797 https://fairsharing.org/FAIRsharing.8f9bbb) `, script tags and all, at the bottom of your HTML (URL_TO_INSERT_RECORD-ABBREV_796 https://fairsharing.org/FAIRsharing.YugnuL)  page template. 

   Make sure that this is before the closing `</html>` tag.
   
   Your site should now include DataCatalog markup. 
   
   Once you have deployed this on your web server, you can test it with the [Bioschemas Validator](https://www.macs.hw.ac.uk/SWeL/BioschemasValidator/) which scrapes the markup from your page and allows you to test it against various Bioschemas (URL_TO_INSERT_RECORD-NAME_798 https://fairsharing.org/3517)  profiles<sup>[1](#biosche (URL_TO_INSERT_RECORD-NAME_799 https://fairsharing.org/3517) mas-validator)</sup>.

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


