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

> To embed `Schema.org (URL_TO_INSERT_RECORD_2680 https://fairsharing.org/FAIRsharing.hzdzq8)  (URL_TO_INSERT_RECORD_2681 https://fairsharing.org/FAIRsharing.hzdzq8) ` markup in a web page that publishes multiple datasets in a single page.


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
alt: The process of annotating a data catalog webpage with bioschema markup for Search (URL_TO_INSERT_RECORD_2682 https://fairsharing.org/FAIRsharing.52b22c)  Engine discovery
---
The process of annotating a data catalog webpage with bioschema markup for Search (URL_TO_INSERT_RECORD_2683 https://fairsharing.org/FAIRsharing.52b22c)  Engine discovery.
```
````


---

## Method

We will outline the steps for marking up a page in your site that is about multiple datasets. The resulting markup will be compliant with both [Google's Dataset markup guidelines](https://developers.google.com/search/docs/data-types/dataset#publication) and the [Bioschemas (URL_TO_INSERT_RECORD_2685 https://fairsharing.org/3517)  (URL_TO_INSERT_RECORD_2686 https://fairsharing.org/3517)  DataCatalog Profile (URL_TO_INSERT_RECORD_2684 https://fairsharing.org/FAIRsharing.2037b2) ](https://bioschemas.org (URL_TO_INSERT_RECORD_2687 https://fairsharing.org/3517) /profiles/DataCatalog). 

We will use [FAIRsharing](https://fairsharing.org (URL_TO_INSERT_RECORD_2688 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2689 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2690 https://fairsharing.org/3538) /) as an example for this recipe which makes three datasets available within its markup.

1. Identify the page in your site about a specific dataset, e.g. https://fairsharing.org (URL_TO_INSERT_RECORD_2691 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2692 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2693 https://fairsharing.org/3538) /

2. Open the  [Bioschemas (URL_TO_INSERT_RECORD_2694 https://fairsharing.org/3517)  (URL_TO_INSERT_RECORD_2695 https://fairsharing.org/3517)  Generator](https://www.macs.hw.ac.uk/SWeL/BioschemasGenerator/)

   1.  Select `DataCatalog` from the Bioschemas (URL_TO_INSERT_RECORD_2696 https://fairsharing.org/3517)  (URL_TO_INSERT_RECORD_2697 https://fairsharing.org/3517)  Profile dropdown

   2.  Enter the URL (URL_TO_INSERT_RECORD_2698 https://fairsharing.org/FAIRsharing.9d38e2)  of the page in URL (URL_TO_INSERT_RECORD_2699 https://fairsharing.org/FAIRsharing.9d38e2)  box, e.g. `https://fairsharing.org (URL_TO_INSERT_RECORD_2700 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2701 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2702 https://fairsharing.org/3538) /`

   3.  Click on the `Show Form` button
   
   ````{dropdown} 
   :open:
   ```{figure} Bioschemas (URL_TO_INSERT_RECORD_2703 https://fairsharing.org/3517)  (URL_TO_INSERT_RECORD_2704 https://fairsharing.org/3517) Generator.png
   ---
   name: bioschemas (URL_TO_INSERT_RECORD_2705 https://fairsharing.org/3517) -generator-start-screen-1
   alt: Bioschemas (URL_TO_INSERT_RECORD_2706 https://fairsharing.org/3517)  (URL_TO_INSERT_RECORD_2707 https://fairsharing.org/3517)  Generator start screen.
   
   ---
   Bioschemas (URL_TO_INSERT_RECORD_2708 https://fairsharing.org/3517)  (URL_TO_INSERT_RECORD_2709 https://fairsharing.org/3517)  Generator start screen.
   ```
   ````

3. Complete the profile form with the informat (URL_TO_INSERT_TERM_2710 https://fairsharing.org/search?recordType=model_and_format) ion relevant for your page. Once completed, click on the `Generate Markup`  button

   - You should complete all *Minimum* properties and as many *Recommended* properties as possible. You can show/hide properties using the `Additional Properties` buttons.
   - Where possible you should link to other resources. The Bioschemas (URL_TO_INSERT_RECORD_2711 https://fairsharing.org/3517)  (URL_TO_INSERT_RECORD_2712 https://fairsharing.org/3517)  Generator does not make this as simple as it could, but you can do it in step 5 once you have generated your markup, e.g. our dataset will link to a page with DataCatalog markup in rather than repeating all the properties for now we will just enter a `url` and no other properties.
     - If there are separate pages for your datasets then you should link to them using an `@id` link
     - Otherwise, you can include the markup within the `DataCatalog` markup
   - The form defaults to the data type with the first alphabetical character, e.g. for `identifier (URL_TO_INSERT_TERM_2713 https://fairsharing.org/search?recordType=identifier_schema) `, this defaults to `PropertyValue` but `Text` or `URL (URL_TO_INSERT_RECORD_2714 https://fairsharing.org/FAIRsharing.9d38e2)  ` will be more appropriate in most cases
   - The right side of the screen gives examples for properties, where these have been provided by the Bioschemas (URL_TO_INSERT_RECORD_2715 https://fairsharing.org/3517)  (URL_TO_INSERT_RECORD_2716 https://fairsharing.org/3517)  profile authors. Click on the `Show` button to see the example for a specific property. Click on `Minimum`, `Recommended`, or `Optional` to expand/contract the section and see the properties contained at that marginality level

   ````{dropdown} 
   :open:
   ```{figure} Bioschemas (URL_TO_INSERT_RECORD_2717 https://fairsharing.org/3517)  (URL_TO_INSERT_RECORD_2718 https://fairsharing.org/3517) GeneratorDataCatalogForm.png
   ---
   height: 550px
   name: Bioschemas (URL_TO_INSERT_RECORD_2719 https://fairsharing.org/3517)  (URL_TO_INSERT_RECORD_2720 https://fairsharing.org/3517)  Generator DataCatalog profile form
   alt: Bioschemas (URL_TO_INSERT_RECORD_2721 https://fairsharing.org/3517)  (URL_TO_INSERT_RECORD_2722 https://fairsharing.org/3517)  Generator DataCatalog profile form
   ---
   Bioschemas (URL_TO_INSERT_RECORD_2723 https://fairsharing.org/3517)  (URL_TO_INSERT_RECORD_2724 https://fairsharing.org/3517)  Generator DataCatalog profile form.
   ```   
   ````

4. You will now see the generated markup in `JSO (URL_TO_INSERT_RECORD_2730 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_2728 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2733 https://fairsharing.org/FAIRsharing.8f9bbb) ` format (URL_TO_INSERT_TERM_2725 https://fairsharing.org/search?recordType=model_and_format) . You can click on the `Microdata` and `RDF (URL_TO_INSERT_RECORD_2727 https://fairsharing.org/FAIRsharing.p77ph9) a (URL_TO_INSERT_RECORD_2732 https://fairsharing.org/663) ` tabs to see the same content rendered in the different format (URL_TO_INSERT_TERM_2726 https://fairsharing.org/search?recordType=model_and_format) s. However, we recommend the use of `JSO (URL_TO_INSERT_RECORD_2731 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_2729 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2734 https://fairsharing.org/FAIRsharing.8f9bbb) `. For our FAIR (URL_TO_INSERT_RECORD_2737 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_2735 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD_2736 https://fairsharing.org/FAIRsharing.2abjs5) .org example, we get the following markup

   ```
   <script type="application/ld+json" >
   {
     "@context": "https://schema.org (URL_TO_INSERT_RECORD_2738 https://fairsharing.org/FAIRsharing.hzdzq8) ",
     "@id": "https://fairsharing.org (URL_TO_INSERT_RECORD_2739 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2740 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2741 https://fairsharing.org/3538) /",
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
         "@context": "https://schema.org (URL_TO_INSERT_RECORD_2742 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Dataset",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2744 https://fairsharing.org/3517) /profiles/Dataset (URL_TO_INSERT_RECORD_2743 https://fairsharing.org/FAIRsharing.20sbr9) /0.3-RELEASE-2019_06_14",
         "description": "A manually curated registry of standard (URL_TO_INSERT_TERM_2745 https://fairsharing.org/search?fairsharingRegistry=Standard) s, split into three types - Terminology (URL_TO_INSERT_TERM_2756 https://fairsharing.org/search?recordType=terminology_artefact)  Artifacts (ontologies (URL_TO_INSERT_TERM_2758 https://fairsharing.org/search?recordType=terminology_artefact) , e.g. Gene Ontology (URL_TO_INSERT_TERM_2757 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_2761 https://fairsharing.org/FAIRsharing.6xq0ee) ), Model (URL_TO_INSERT_TERM_2752 https://fairsharing.org/search?recordType=model_and_format) s and Format (URL_TO_INSERT_TERM_2754 https://fairsharing.org/search?recordType=model_and_format) s (conceptual schema, format (URL_TO_INSERT_TERM_2755 https://fairsharing.org/search?recordType=model_and_format) s, data model (URL_TO_INSERT_TERM_2753 https://fairsharing.org/search?recordType=model_and_format) s, e.g. FAST (URL_TO_INSERT_RECORD_2762 https://fairsharing.org/FAIRsharing.p5df9c) A (URL_TO_INSERT_RECORD_2763 https://fairsharing.org/FAIRsharing.rz4vfg) ), and Reporting Guideline (URL_TO_INSERT_TERM_2748 https://fairsharing.org/search?recordType=reporting_guideline)  (URL_TO_INSERT_TERM_2759 https://fairsharing.org/search?recordType=reporting_guideline) s (e.g. the ARRIVE (URL_TO_INSERT_RECORD_2765 https://fairsharing.org/FAIRsharing.t58zhj)  guideline (URL_TO_INSERT_TERM_2760 https://fairsharing.org/search?recordType=reporting_guideline) s for in vivo animal testing (URL_TO_INSERT_RECORD_2764 https://fairsharing.org/FAIRsharing.q7bkqr) ). These are linked to the database (URL_TO_INSERT_TERM_2746 https://fairsharing.org/search?fairsharingRegistry=Database) s that implement them and the funder (URL_TO_INSERT_TERM_2751 https://fairsharing.org/search?recordType=funder)  and journal (URL_TO_INSERT_TERM_2749 https://fairsharing.org/search?recordType=journal)  publisher (URL_TO_INSERT_TERM_2750 https://fairsharing.org/search?recordType=journal_publisher)  data policies (URL_TO_INSERT_TERM_2747 https://fairsharing.org/search?fairsharingRegistry=Policy)  that recommend or endorse their use.",
         "identifier (URL_TO_INSERT_TERM_2766 https://fairsharing.org/search?recordType=identifier_schema) ": [
           "https://www.fairsharing.org (URL_TO_INSERT_RECORD_2767 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD_2768 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2769 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2770 https://fairsharing.org/3538) /bsg-sXXXXXX"
         ],
         "keywords": [
           "Standard (URL_TO_INSERT_TERM_2771 https://fairsharing.org/search?fairsharingRegistry=Standard) s",
           "Metadata",
           "Format (URL_TO_INSERT_TERM_2772 https://fairsharing.org/search?recordType=model_and_format) s",
           "Ontologies (URL_TO_INSERT_TERM_2773 https://fairsharing.org/search?recordType=terminology_artefact) ",
           "Terminology (URL_TO_INSERT_TERM_2774 https://fairsharing.org/search?recordType=terminology_artefact)  Artifacts",
           "Reporting Guideline (URL_TO_INSERT_TERM_2775 https://fairsharing.org/search?recordType=reporting_guideline)  (URL_TO_INSERT_TERM_2776 https://fairsharing.org/search?recordType=reporting_guideline) s"
         ],
         "name": "Metadata Standard (URL_TO_INSERT_TERM_2777 https://fairsharing.org/search?fairsharingRegistry=Standard) ",
         "url": "https://fairsharing.org (URL_TO_INSERT_RECORD_2778 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2779 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2780 https://fairsharing.org/3538) /standards"
       },
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD_2781 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Dataset",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2783 https://fairsharing.org/3517) /profiles/Dataset (URL_TO_INSERT_RECORD_2782 https://fairsharing.org/FAIRsharing.20sbr9) /0.3-RELEASE-2019_06_14",
         "description": "A manually curated registry of database (URL_TO_INSERT_TERM_2786 https://fairsharing.org/search?fairsharingRegistry=Database) s/data repositories (URL_TO_INSERT_TERM_2788 https://fairsharing.org/search?recordType=repository) , conforming to the BioDBcore (URL_TO_INSERT_RECORD_2792 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_2793 https://fairsharing.org/FAIRsharing.xMmOCL)  standard (URL_TO_INSERT_TERM_2784 https://fairsharing.org/search?fairsharingRegistry=Standard)  (from the Life Sciences). These are linked to the standard (URL_TO_INSERT_TERM_2785 https://fairsharing.org/search?fairsharingRegistry=Standard) s that they use and the funder (URL_TO_INSERT_TERM_2791 https://fairsharing.org/search?recordType=funder)  and journal (URL_TO_INSERT_TERM_2789 https://fairsharing.org/search?recordType=journal)  publisher (URL_TO_INSERT_TERM_2790 https://fairsharing.org/search?recordType=journal_publisher)  data policies (URL_TO_INSERT_TERM_2787 https://fairsharing.org/search?fairsharingRegistry=Policy)  that recommend or endorse their use.",
         "identifier (URL_TO_INSERT_TERM_2794 https://fairsharing.org/search?recordType=identifier_schema) ": [
           "https://www.fairsharing.org (URL_TO_INSERT_RECORD_2795 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD_2796 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2797 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2798 https://fairsharing.org/3538) /bsg-dXXXXXX"
         ],
         "keywords": [
           "Database (URL_TO_INSERT_TERM_2799 https://fairsharing.org/search?fairsharingRegistry=Database) ",
           "Data repository (URL_TO_INSERT_TERM_2800 https://fairsharing.org/search?recordType=repository) "
         ],
         "name": "Database (URL_TO_INSERT_TERM_2801 https://fairsharing.org/search?fairsharingRegistry=Database) ",
         "url": "https://fairsharing.org (URL_TO_INSERT_RECORD_2802 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2803 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2804 https://fairsharing.org/3538) /databases"
       },
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD_2805 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Dataset",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2807 https://fairsharing.org/3517) /profiles/Dataset (URL_TO_INSERT_RECORD_2806 https://fairsharing.org/FAIRsharing.20sbr9) /0.3-RELEASE-2019_06_14",
         "description": "A manually curated registry of data policies (URL_TO_INSERT_TERM_2810 https://fairsharing.org/search?fairsharingRegistry=Policy)  from research (URL_TO_INSERT_RECORD_2815 https://fairsharing.org/FAIRsharing.52b22c)  funder (URL_TO_INSERT_TERM_2814 https://fairsharing.org/search?recordType=funder) s, journal (URL_TO_INSERT_TERM_2811 https://fairsharing.org/search?recordType=journal)  publisher (URL_TO_INSERT_TERM_2813 https://fairsharing.org/search?recordType=journal_publisher) s, societies (URL_TO_INSERT_TERM_2812 https://fairsharing.org/search?recordType=society) , and other organisations. These are linked to the database (URL_TO_INSERT_TERM_2809 https://fairsharing.org/search?fairsharingRegistry=Database) s and standard (URL_TO_INSERT_TERM_2808 https://fairsharing.org/search?fairsharingRegistry=Standard) s that they recommend for use",
         "identifier (URL_TO_INSERT_TERM_2816 https://fairsharing.org/search?recordType=identifier_schema) ": [
           "https://www.fairsharing.org (URL_TO_INSERT_RECORD_2817 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD_2818 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2819 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2820 https://fairsharing.org/3538) /bsg-pXXXXXX"
         ],
         "keywords": [
           "Data policy (URL_TO_INSERT_TERM_2821 https://fairsharing.org/search?fairsharingRegistry=Policy) ",
           "journal (URL_TO_INSERT_TERM_2822 https://fairsharing.org/search?recordType=journal) ",
           "funder (URL_TO_INSERT_TERM_2823 https://fairsharing.org/search?recordType=funder) ",
           "society (URL_TO_INSERT_TERM_2824 https://fairsharing.org/search?recordType=society) "
         ],
         "name": "Data Policy (URL_TO_INSERT_TERM_2825 https://fairsharing.org/search?fairsharingRegistry=Policy) ",
         "url": "https://fairsharing.org (URL_TO_INSERT_RECORD_2826 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2827 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2828 https://fairsharing.org/3538) /policies"
       }
     ],
     "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2830 https://fairsharing.org/3517) /profiles/DataCatalog/0.3-RELEASE-2019_07_01 (URL_TO_INSERT_RECORD_2829 https://fairsharing.org/FAIRsharing.2037b2) ",
     "description": "A manually curated, informat (URL_TO_INSERT_TERM_2838 https://fairsharing.org/search?recordType=model_and_format) ive and educational resource on data and metadata standard (URL_TO_INSERT_TERM_2831 https://fairsharing.org/search?fairsharingRegistry=Standard) s, inter-related to database (URL_TO_INSERT_TERM_2832 https://fairsharing.org/search?fairsharingRegistry=Database) s/data repositories (URL_TO_INSERT_TERM_2834 https://fairsharing.org/search?recordType=repository)  and funder (URL_TO_INSERT_TERM_2837 https://fairsharing.org/search?recordType=funder)  and journal (URL_TO_INSERT_TERM_2835 https://fairsharing.org/search?recordType=journal)  publisher (URL_TO_INSERT_TERM_2836 https://fairsharing.org/search?recordType=journal_publisher)  data policies (URL_TO_INSERT_TERM_2833 https://fairsharing.org/search?fairsharingRegistry=Policy)  from across disciplines. FAIR (URL_TO_INSERT_RECORD_2842 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_2840 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD_2841 https://fairsharing.org/FAIRsharing.2abjs5)  is an ELIXIR-UK node resource and has an active role in the RDA (URL_TO_INSERT_RECORD_2839 https://fairsharing.org/FAIRsharing.2g5kcb)  and Force11 data initiatives.",
     "identifier (URL_TO_INSERT_TERM_2843 https://fairsharing.org/search?recordType=identifier_schema) ": [
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
     "name": "FAIR (URL_TO_INSERT_RECORD_2846 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_2844 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD_2845 https://fairsharing.org/FAIRsharing.2abjs5) .org",
     "provider": [
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD_2847 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Organization",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2848 https://fairsharing.org/3517) /profiles/Organization/0.2-DRAFT-2019_07_19",
         "description": "",
         "name": "FAIR (URL_TO_INSERT_RECORD_2851 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_2849 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD_2850 https://fairsharing.org/FAIRsharing.2abjs5) .org Registry"
       }
     ],
     "url": "https://fairsharing.org (URL_TO_INSERT_RECORD_2852 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2853 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2854 https://fairsharing.org/3538) /"
   }
   </script >
   ```
   
5. Download or copy and paste the generated markup
   
6. Make adjustments for any bits that could not be properly entered through the form. 
   
   For example, for our generated markup we would change the `provider` so that it provides a direct link rather than repeating the properties. We would replace

   ```
   "provider": [
       {
         "@context": "https://schema.org (URL_TO_INSERT_RECORD_2855 https://fairsharing.org/FAIRsharing.hzdzq8) ",
         "@type": "Organization",
         "dct:conformsTo": "https://bioschemas.org (URL_TO_INSERT_RECORD_2856 https://fairsharing.org/3517) /profiles/Organization/0.2-DRAFT-2019_07_19",
         "description": "",
         "name": "FAIR (URL_TO_INSERT_RECORD_2859 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_2857 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD_2858 https://fairsharing.org/FAIRsharing.2abjs5) .org Registry"
       }
     ],
   ```
   
   with

   ```
   "provider": [
       {
         "@type": "Organization",
         "@id": "https://fairsharing.org (URL_TO_INSERT_RECORD_2860 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_2861 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_2862 https://fairsharing.org/3538) /communities"
       }
     ],
   ```
   
   You can test that your JSO (URL_TO_INSERT_RECORD_2865 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_2863 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2867 https://fairsharing.org/FAIRsharing.8f9bbb)  is valid syntax, and visualise your markup using the [JSO (URL_TO_INSERT_RECORD_2866 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_2864 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2868 https://fairsharing.org/FAIRsharing.8f9bbb)  Playground](https://json-ld.org/playground/).

7. Once you are happy with your markup, include the `JSO (URL_TO_INSERT_RECORD_2870 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_2869 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_2871 https://fairsharing.org/FAIRsharing.8f9bbb) `, script tags and all, at the bottom of your HTML (URL_TO_INSERT_RECORD_2872 https://fairsharing.org/FAIRsharing.YugnuL)  page template. 

   Make sure that this is before the closing `</html>` tag.
   
   Your site should now include DataCatalog markup. 
   
   Once you have deployed this on your web server, you can test it with the [Bioschemas (URL_TO_INSERT_RECORD_2873 https://fairsharing.org/3517)  (URL_TO_INSERT_RECORD_2876 https://fairsharing.org/3517)  Validator](https://www.macs.hw.ac.uk/SWeL/BioschemasValidator/) which scrapes the markup from your page and allows you to test it against various Bioschemas (URL_TO_INSERT_RECORD_2874 https://fairsharing.org/3517)  (URL_TO_INSERT_RECORD_2877 https://fairsharing.org/3517)  profiles<sup>[1](#bioschemas (URL_TO_INSERT_RECORD_2875 https://fairsharing.org/3517) -validator)</sup>.

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


