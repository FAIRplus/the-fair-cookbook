# Mapping In-house terms to Another Standard
## Illustrated by In-house Metadata to ENA's Checklists

+++
<br/>


````{panels_fairplus}
:identifier_text: RX.X
:identifier_link: 
:difficulty_level: 2
:recipe_type: Guidance
:reading_time_minutes: 15
:intended_audience: data_manager, Terminology Manager, Data Curator
:has_executable_code: nope
:recipe_name: Recipe Template
````

## Main Objectives

The main purpose of this recipe is:

> To guide how to map in-house metadata to another standard. This is illustrated by mapping in-house
> metadata fields names to those of ENA's sample checklists, to allow one to prepare may samples of 
> metadata collected in an institutional system to be submitted to ENA.
> This is quite simplistic, other recipes are available to do more complex mapping.

---


## Graphical Overview


### Figure: Overview of discovering what metadata you are using(if any), map and analysis, to get a mapping
```mermaid
  graph TD; 
      A([Collected metadata])-->mystds["identify in house systems used\n for storing field names and values"]
      mystds-- "if standard mappings exist" -->mappingsAlreadyExist["Mappings already exist, so done.\n e.g. if your metadata standards are already based on DwC or MIxS"]
      mystds-->myCollation["collate my field names as list"]
      myCollation-->ENAChecklist["choose appropriate ENA sample list"]
      ENAChecklist-->stringMap["manually or programmatically\n map the two lists"]
      stringMap-- "exact or close match" -->sanityReview("sanity review of high confidence mappings")
      
      stringMap-- "No or low confidence mapping" -->manualAnalysis["manual review of low confidence mappings\n and making new mappings were assessed"]
      sanityReview-- "pass" -->mapping("mapping of your and ENA checklist field names")
      sanityReview-- "fail" -->manualAnalysis
      manualAnalysis-- "valid mappings exist" -->mapping
      mappingsAlreadyExist-->mapping
      manualAnalysis-- "no valid mappings exist" -->no("List of your and ENA checklist field names\n where no valid mappings exist")
      
      classDef default fill:#0A749B,stroke:#333,stroke-width:4px;  #blue
```
---


## Requirements

* technical requirements:
   * Excel skills
   * possibly basis scripting to compare terms

* knowledge requirement:
   * know what your source metadata schema is.
   * understand what you are trying to achieve and why this helps 
   * [understand in general about GSC and MIxS](https://www.gensc.org//pages/projects/mixs-gsc-project.html)
   * [understand the ENA metadata model]( https://ena-docs.readthedocs.io/en/latest/submit/general-guide/metadata.html) 

---

## Capability & Maturity Table

| Capability       | Initial Maturity Level | Final Maturity Level |
|:-----------------|:-----------------------|:---------------------|
| Interoperability | minimal                | repeatable           |


---

## FAIRification Objectives, Inputs and Outputs


| Actions.Objectives.Tasks                                  | Input                                                                   | Output                                               |
|:----------------------------------------------------------|:------------------------------------------------------------------------|:-----------------------------------------------------|


## Table of Data Standards

```{admonition} Important
:class: tip
this section is relied upon by another component developed by FAIRplus to enhance search and presentation. It is therefore important to comply with the layout. 
```

| Data Formats   | Terminologies                                                  | Models                                                |
|:---------------|:---------------------------------------------------------------|:------------------------------------------------------|
| TSV/CSV, EXCEL | GSC MIxS                                                       |
---

## Main Content

### Introduction
The European Nucleotide Archive (ENA) is one of the INSDC members where much of the world's nucleotide data is submitted to and archived. 
Sample related metadata submitted via checklist templates. 
The field names on the templates are usually based on [GSC MIxS](https://www.gensc.org//pages/projects/mixs-gsc-project.html) standards. 
This is particularly true of sample related metadata. Project, sequencing experiment and other metadata are collected
separately, usually with manifests.

Well-resourced scientific institutions often have their own sample and sequence data management platforms.
The metadata concepts and metadata architecture will usually be somewhat different to that of the ENA. 
The challenge and the focus of this recipe are the approaches to shape the metadata appropriately.

### In
- Knowledge of what metadata you are currently using
- An appropriate ENA checklist

### Find out what metadata your in-house system is and what standards they follow
```mermaid
  graph TD; 
      A([Collected metadata])-->B[used institutional system]
      A-->C[custom]
      
      subgraph mystds ["systems used for storing field_names and values"]
        C-->D
        B-->D(mainstream standard)
        D-->main-standard[Note what standard]
              main-standard-- "if standard mappings exist" -->mappingsAlreadyExist("Mappings already exist, so done.\n e.g. if your metadata standards are already based on DwC or MIxS")

        B-->E
        C-->E(institutional standard)
        C-->F(no standard)
        end
        
      subgraph "collate field_names"  
        E-->schema[("tables of field_names\n(schema)")]
        F-->IF{"if fields described"}
        categories{{"Categories of metadata\n- study\n- project\n- sample\n- experiment"}}
        end

      schema-->definitions(["table of categories,\n field_names, field_ids\nand descriptions"])
      IF-->definitions
      IF-->no_definitions(["table of categories,\n field names"])
            categories-->definitions
      categories-->no_definitions
      main-standard -..-> definitions
 
      style A fill:#008000,stroke:#333,stroke-width:2px
      style B fill:#FF5733,stroke:#333,stroke-width:2px
      style C fill:#FF5733,stroke:#333,stroke-width:2px
      style D fill:#0A749B,stroke:#333,stroke-width:2px
      style E fill:#0A749B,stroke:#333,stroke-width:2px
      style F fill:#0A749B,stroke:#333,stroke-width:2px
      style main-standard fill:#008000,stroke:#333,stroke-width:2px
      style definitions fill:#008000,stroke:#333,stroke-width:2px
      style mappingsAlreadyExist fill:#008000,stroke:#333,stroke-width:2px
      style no_definitions fill:#008000,stroke:#333,stroke-width:2px
```

### Preparing to Align your Metadata with ENA's

In preparation for aligning your metadata your need to investigate your metadata:
- what type of ENA checklist is closest to your type of study?
- what metadata standards currently apply to your metadata? 

Links
- see checklists in https://www.ebi.ac.uk/ena/browser/checklists
- see https://ena-docs.readthedocs.io/en/latest/submit/samples/interactive.html


```mermaid
  graph TD; 
      A([collected metadata])-->metadata_domain
      
     B["standard \n'GSC MIxS'/\n'DarwinCore'"]-->mappingsAlreadyExist["mappings already exist"]
     B-- "no common standards apply" -->C[custom]
     
      C[custom]-->need_to_map{"need to map"}
      metadata_domain("what type of domain is your study?\n e.g. aquatic environmental?") --> B
      
        mappingsAlreadyExist-->std_mappings{"use the standard mappings"}
        style A fill:#008000,stroke:#333,stroke-width:2px
      style B fill:#FF5733,stroke:#333,stroke-width:2px
      style C fill:#0A749B,stroke:#333,stroke-width:2px
      
      style metadata_domain fill:#FF5733,stroke:#333,stroke-width:2px
      style mappingsAlreadyExist fill:#008000,stroke:#333,stroke-width:2px
      style std_mappings fill:#FF5733,stroke:#333,stroke-width:2px
      style need_to_map fill:#FF5733,stroke:#333,stroke-width:2px
      

```
#### Choose an appropriate ENA Sample Checklist
```mermaid
  graph TD; 
      A([Collected metadata])-->myDomain{"determine what type of study\n domain your metadata is e.g. aquatic"}
      myDomain-->opt1
      subgraph "choose the appropriate ENA Sample sheet"
         opt1["https://www.ebi.ac.uk/ena/browser/checklists"] -->opt2[" click on a checklist "]
         opt2-->opt3[" read the description "]
         opt3-->opt4[" look at the field name and\n even mouse over description "]
         opt4-->opt5["download from here for detail in XML\n if desired"]
         
        end
 
        style A fill:#008000,stroke:#333,stroke-width:2px
       style myDomain fill:#FF5733,stroke:#333,stroke-width:2px
      style opt1 fill:#0A749B,stroke:#333,stroke-width:2px
      style opt2 fill:#0A749B,stroke:#333,stroke-width:2px
      style opt3 fill:#0A749B,stroke:#333,stroke-width:2px
      style opt4 fill:#0A749B,stroke:#333,stroke-width:2px
      style opt5 fill:#0A749B,stroke:#333,stroke-width:2px


```

### If needed: mapping of your field names to ENA checklist field names
Now that you have both your own field names and those of the appropriate ENA checklist, you can then 
proceed with the actual mapping. Unless you only have a small number of field names to map, it is best to utilise some 
computers. Doing exact strong matching is straight forwards.  Many field names differ by something simple like upper or lower case, spaces, dialect 
spelling (American/British English), plurals, etc. Fortunately, "fuzzy string matching" will cope with these simple differences.

- Programmatically, as simple way of doing this is using a fuzzy string matcher library in python such as
https://github.com/rapidfuzz/RapidFuzz and similar exist in R.
- Excel now allows fuzzy string matching too (https://www.microsoft.com/en-gb/download/details.aspx?id=15011).
- For the more techie, there is an even better resource for doing the mappings: https://github.com/cidgoh/DataHarmonizer 
This takes into account more of the other information of the field name that just the string content of it, but using 
associated properties.

Whatever way you choose, the recipe will be very similar. You will always have to do at least do some manual checking. 
Often you will also have to decide whether two field_names are close enough, it is worth reading the definitions/descriptions
to help with this. Sometimes the granularities being captured are different, or there are two field names in your 
metadata and just one in ENA. These can be difficult to decide to map these.

You will end up with a file of pairwise matches of field_names that are equivalent in an ENA checklist and in your 
own metadata. You will often have a list of field names from your own metadata and in ENA that do not match. It is sensible
to prioritise unmapped ENA field_names which are mandatory or recommended, for trying to find conceptually similar terms to map to. 

```mermaid
  graph TD; 
      myCollation["my field names as list"]-->stringMap
     
      ENAChecklist["ENA checklist field names as list"]-->stringMap("Programmatically map the two lists")
      stringMap("appropriate ENA sample list")-- "Exact or close match" -->sanityReview("sanity review of high confidence mappings")
      
      stringMap-- "No or low confidence mapping" -->manualAnalysis("manual review of low confidence mappings\n and making new mappings were assessed")
      sanityReview-- "pass" -->mapping("mapping of your and ENA checklist field names")
      sanityReview-- "fail" -->manualAnalysis
      manualAnalysis-- "valid mappings exist" -->mapping
      mappingsAlreadyExist-->mapping
      manualAnalysis-- "no valid mappings exist" -->no("lists where no valid mappings exist:\n 1) of your field names\n 2) ENA checklist field names\n ")
      
      
      classDef default fill:#0A749B,stroke:#333,stroke-width:4px;  #blue
```


### Once you have your mappings create a Sample Template
Once you have your mappings create a Sample Template and then fill this out

Tip: For any programmers/scripters out there, once you know what the template is you could automate:
- from the template you know the format
- from the mapping file you know which file_names in your metadata correspond to which in the ENA.
- then going forwards you can have a script to automated converting your instutions metadata to a format 
suitable to submit to ENA. 


```mermaid
  graph TD; 
      pairwise_mapping("Mapping table of your\n list vs ENA field names")-->ena_field_names("extracted list of ENA field names")
      your_solo_field_names("list of not mapped to ENA field names")-->apt3
      
      ena_field_names-->apt1["see https://ena-docs.readthedocs.io/en/latest/submit/samples/interactive.html"]
     subgraph "Download and Fill out the ENA Sample TEMPLATE"
         
         apt1-->apt2["go to the checklist,\n and to the checklist template\n you identified before"]
         apt2-->apt3["add any extra sample related field_names"]
         apt3-->apt4["download"]
         apt4-->apt5["in separate TSV or spreadsheet organise\n your sample rows with columns in the same order as the field_names"]
         apt5-- "check that values will likely pass the regex" -->apt5
         apt5-->apt6["add sample rows from row 4 downwards"]

        end  
     apt6-->completed("Completed template with content")

     style pairwise_mapping fill:#008000,stroke:#333,stroke-width:2px
     style ena_field_names fill:#008000,stroke:#333,stroke-width:2px
     style your_solo_field_names fill:#008000,stroke:#333,stroke-width:2px
     style completed fill:#008000,stroke:#333,stroke-width:2px
      style apt1 fill:#0A749B,stroke:#333,stroke-width:2px
      style apt2 fill:#0A749B,stroke:#333,stroke-width:2px
      style apt3 fill:#0A749B,stroke:#333,stroke-width:2px
      style apt4 fill:#0A749B,stroke:#333,stroke-width:2px
      style apt5 fill:#FF5733,stroke:#333,stroke-width:2px
      style apt6 fill:#FF5733,stroke:#333,stroke-width:2px
```

---

## Next Steps
In the case of ENA, there is further metadata to add to other objects, other than sample level. There are 
relatively few metadata fields on each of these, so you may be quicker mapping this manually.
- project/study level e.g. project/study name
- sequencing experiment  e.g. for sequencing instrument and platform


## Conclusion
- Mapping In-house Metadata to other checklists or standards is important.
- For a handful of terms, manual mapping is the quickest.
- When over twenty or so terms, semi-automation is wise as it saves time and 
also means that you are less likely to miss obvious things.
- Some manual checking is essential and almost always needed.
- Once you have the mapping it allows you to automate submission, saving time and reducing errors.

---

## References:

```{footbibliography}
identifier-mapping.md
```


---

## Authors

```{note}
List the recipe contributors following the structure below and using the CASRAI credit vocabulary and do not change the structure of the table.
    - Conceptualization - Peter Woollard
    - Writing - original draft - Peter Woollard
    - Writing - review & editing - Peter Woollard
```

```{admonition} Important
:class: tip
this section is relied upon by another component developed by FAIRplus to enhance search and presentation. It is therefore important to comply with the layout. 
```


| Name                                                                                                                                                                                                                  | Orcid                                                                                                               | Affiliation                           | Type                                                                    |                                             Elixir Node                                             |                  Credit Role                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------|-------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------:|:---------------------------------------------:|
| <div class="firstCol"><a target="_blank" href='https://github.com/'><img class='avatar-style' src='https://avatars.githubusercontent.com/u/115020636?v=4'></img><div class="d-block">Peter Woollard</div></a>  </div> | <a target="_blank" href='https://orcid.org/0000-0002-7654-6902'><i class='fab fa-orcid fa-2x text--orange'></i></a> | European Nucleotide Archive, EMBL-EBI | <i class="fas fa-graduation-cap fa-1x text--orange" alt="Academic"></i> | <img class='elixir-style' src='/the-fair-cookbook/_static/images/logo/Elixir/ELIXIR-UK.svg' ></img> | Writing - Review & Editing, Conceptualization |

---

## License

````{license_fairplus}
CC-BY-4.0
````
