(fcb-rdf-conversion)=
# An inventory of tools for converting data to RDF



````{panels_fairplus}
:identifier_text: FCB051
:identifier_link: 'https://w3id.org/faircookbook/FCB051'
:difficulty_level: 3
:recipe_type: inventory
:reading_time_minutes: 30
:intended_audience: data_producer, data_engineer
:maturity_level: 4
:maturity_indicator: 57
:has_executable_code: nope
:recipe_name: Inventorying tools for converting data to RDF
```` 

## Main Objectives

The main purpose of this recipe is:

> Present an inventory of a selection of popular tools for converting datasets in different format (URL_TO_INSERT_TERM_6080 https://fairsharing.org/search?recordType=model_and_format) s (e.g. CSV (URL_TO_INSERT_RECORD_6081 https://fairsharing.org/FAIRsharing.1943d4) , JSON (URL_TO_INSERT_RECORD_6084 https://fairsharing.org/FAIRsharing.5bbab9) , RDBMs, XML (URL_TO_INSERT_RECORD_6082 https://fairsharing.org/FAIRsharing.b5cc91) ) to RDF (URL_TO_INSERT_RECORD_6083 https://fairsharing.org/FAIRsharing.p77ph9) , and to provide guidance for choosing the right tool.

---


## Graphical Overview of the FAIRification Recipe Objectives

Figure {numref}`rdf-conversion-figure1` shows an example ETL workflow.


````{dropdown} 
:open:
```{figure} rdf-conversion.md-figure1.mmd.png
---
name: rdf-conversion-figure1
alt: Building an ontology (URL_TO_INSERT_TERM_6085 https://fairsharing.org/search?recordType=terminology_artefact)  with Robot tool
---
Building an ontology (URL_TO_INSERT_TERM_6086 https://fairsharing.org/search?recordType=terminology_artefact)  with Robot tool.
```
````

---


## Requirements

* recipe dependency:
    * This recipe is an example of how to perform ETL with the RDF (URL_TO_INSERT_RECORD_6088 https://fairsharing.org/FAIRsharing.p77ph9)  model (URL_TO_INSERT_TERM_6087 https://fairsharing.org/search?recordType=model_and_format) . For tools on general ETL process. Please check recipe {ref}`fcb-interop-etl`
* knowledge requirement:
  * basic understanding of: command line syntax, RDF (URL_TO_INSERT_RECORD_6089 https://fairsharing.org/FAIRsharing.p77ph9) , configuration using YAML
* other:
  * plan/model of how to map your source entities/properties to classes/types/properties, and how to create resource URIs <!-- TODO would be nice to link out to a recipe about minting -->

---

## Table of Data Standards

| Data Format (URL_TO_INSERT_TERM_6091 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_6092 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_6090 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
| R2RML<!-- TODO needs a link -->    |   |   |
| RML<!-- TODO needs a link -->      |   |   |
| YARRRML<!-- TODO needs a link -->  |   |   |
| YAML<!-- TODO needs a link -->     |   |   |

---

## Introduction

Research (URL_TO_INSERT_RECORD_6099 https://fairsharing.org/FAIRsharing.52b22c)  data is produced in a range of different format (URL_TO_INSERT_TERM_6095 https://fairsharing.org/search?recordType=model_and_format) s, such as spreadsheets, delimiter-separated files (CVS, TSV (URL_TO_INSERT_RECORD_6096 https://fairsharing.org/FAIRsharing.a978c9) ), or (relational) database (URL_TO_INSERT_TERM_6094 https://fairsharing.org/search?fairsharingRegistry=Database) s. To improve reusability of data and make them more FAIR (URL_TO_INSERT_RECORD_6098 https://fairsharing.org/FAIRsharing.WWI10U) , these data sets can be published in the _de facto_ standard (URL_TO_INSERT_TERM_6093 https://fairsharing.org/search?fairsharingRegistry=Standard)  for reusable data, RDF (URL_TO_INSERT_RECORD_6097 https://fairsharing.org/FAIRsharing.p77ph9) . 

There are many tools available to convert non-RDF data to RDF (URL_TO_INSERT_RECORD_6100 https://fairsharing.org/FAIRsharing.p77ph9) , a process also known as ‘triplification’ or ‘RDFizing’ of data. See for instance the lists maintained by W3C at [ConverterToRdf](https://www.w3.org/wiki/ConverterToRdf), [RDFImportersAndAdapters](https://www.w3.org/wiki/RDFImportersAndAdapters) (outdated), and [RdfAndSql](https://www.w3.org/wiki/RdfAndSql), or perform a quick Google search (URL_TO_INSERT_RECORD_6101 https://fairsharing.org/FAIRsharing.52b22c) . 

However, finding the right tool for a particular scenario can be difficult and time-consuming. A user needs to try the tool and invest some time in understanding it, while its limitations may only be discovered later. Many tools are limited to a particular input format (URL_TO_INSERT_TERM_6102 https://fairsharing.org/search?recordType=model_and_format)  or come with a particular application; are no longer supported, maintained or suffer from bugs; need a significant time investment to learn the specifics of their use or configuration options; or lack sufficient documentation. 

This recipe aims to address these problems by presenting a selection of conversion tools, and giving guidance on choosing the right tool, that adhere to the following (somewhat subjective) criteria:

*   Generic applicability (e.g. not limited to OWL (URL_TO_INSERT_RECORD_6103 https://fairsharing.org/FAIRsharing.atygwy)  or SKOS (URL_TO_INSERT_RECORD_6104 https://fairsharing.org/FAIRsharing.48e326) )
*   Multiple format (URL_TO_INSERT_TERM_6105 https://fairsharing.org/search?recordType=model_and_format) s: tabular (Excel, CSV (URL_TO_INSERT_RECORD_6106 https://fairsharing.org/FAIRsharing.1943d4)  etc), hierarch (URL_TO_INSERT_RECORD_6108 https://fairsharing.org/FAIRsharing.52b22c) ical (XML, JSON (URL_TO_INSERT_RECORD_6107 https://fairsharing.org/FAIRsharing.5bbab9) ), RDBs
*   Well documented
*   Actively maintained
*   Easy to install and use (i.e. no compilation or docker needed)
*   Reasonably stable/bug free
*   Available for all major platforms (Windows, Mac, Linux)

## Step by step process

### Step 1: consider requirements

To choose the best tool for your conversion task consider the following:

*   Is a GUI preferred, or a command line interface? Should it be possible to automate the conversion?
*   Should the map (URL_TO_INSERT_RECORD_6110 https://fairsharing.org/FAIRsharing.53edcc) ping be reused (repeated)? Should map (URL_TO_INSERT_RECORD_6111 https://fairsharing.org/FAIRsharing.53edcc) pings be defined in an open standard (URL_TO_INSERT_TERM_6109 https://fairsharing.org/search?fairsharingRegistry=Standard)  independently from a particular tool?
*   Is the data messy or does it require significant transformat (URL_TO_INSERT_TERM_6112 https://fairsharing.org/search?recordType=model_and_format) ion before conversion?
*   Might it be better to present the data as a virtual graph (mainly for database (URL_TO_INSERT_TERM_6113 https://fairsharing.org/search?fairsharingRegistry=Database) s) than performing an actual conversion?

Based on these criteria, find the right tool in the table below. Jump to the section on that tool to read about additional considerations and details.

|                                           | GUI | CL (URL_TO_INSERT_RECORD_6114 https://fairsharing.org/FAIRsharing.j9y503) I, automation | Reuse map (URL_TO_INSERT_RECORD_6115 https://fairsharing.org/FAIRsharing.53edcc) pings | Messy data | Virtual graph |
| ----------------------------------------- | --- | --------------- | -------------- | ---------- | ------------- |
| OpenRefine + RDF (URL_TO_INSERT_RECORD_6116 https://fairsharing.org/FAIRsharing.p77ph9)  extension                | ✅   | +/-         | +/-        | ✅          |               |
| TopBraid Composer (ME)1                   | ✅   |                 |                |            |               |
| RML-based tools (RML map (URL_TO_INSERT_RECORD_6117 https://fairsharing.org/FAIRsharing.53edcc) per, SDM-RDFizer) |     | ✅               | ✅              |            |               |
| SP (URL_TO_INSERT_RECORD_6119 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_6118 https://fairsharing.org/FAIRsharing.87ccfd) -Generate                           |     | ✅               | ✅              |            |               |
| Ontop (RDB only)                          |     | ✅               | ✅              |            | ✅             |
| Virtuoso (proprietary tool)                                 |     |                 | ✅              |            | ✅             |
| Custom code                               |     | ✅               |                | ✅          |               |

Except for OpenRefine and writing your own code, most tools make use of a map (URL_TO_INSERT_RECORD_6122 https://fairsharing.org/FAIRsharing.53edcc) ping language to declare the rules for conversion to RDF (URL_TO_INSERT_RECORD_6121 https://fairsharing.org/FAIRsharing.p77ph9) . Read the section on transformat (URL_TO_INSERT_TERM_6120 https://fairsharing.org/search?recordType=model_and_format) ion/map (URL_TO_INSERT_RECORD_6123 https://fairsharing.org/FAIRsharing.53edcc) ping languages to find out more about these languages and why it makes sense to prefer YARRRML as the map (URL_TO_INSERT_RECORD_6124 https://fairsharing.org/FAIRsharing.53edcc) ping language of choice.

### Step 2: select/install tool

Select one or more tools to install and evaluate, go through the tutorials, and try the tool for conversion of a small selection of your data.


## Tools


### OpenRefine with RDF extension

OpenRefine is an open source data transformat (URL_TO_INSERT_TERM_6125 https://fairsharing.org/search?recordType=model_and_format) ion tool for exploring, cleaning, and transforming all kinds of structured data. It offers a spreadsheet-like user interface that allows users to interactively explore and transform their data. Data can be manipulated through menu actions and GREL (Google Refine Expression Language) or Python/Jython expressions. It keeps a undo/redo history which can also be used to ‘replay’ transformat (URL_TO_INSERT_TERM_6126 https://fairsharing.org/search?recordType=model_and_format) ion and configuration steps.

OpenRefine is open source and has an active community. Additional functionality is provided through extensions and custom distributions. For instance, the ability to work with RDF (URL_TO_INSERT_RECORD_6127 https://fairsharing.org/FAIRsharing.p77ph9)  is provided by installing the RDF (URL_TO_INSERT_RECORD_6128 https://fairsharing.org/FAIRsharing.p77ph9)  extension. Publication to FAIR (URL_TO_INSERT_RECORD_6130 https://fairsharing.org/FAIRsharing.WWI10U)  data point (URL_TO_INSERT_RECORD_6129 https://fairsharing.org/298) s is provided through the FAIR (URL_TO_INSERT_RECORD_6131 https://fairsharing.org/FAIRsharing.WWI10U)  metadata extension.


When you should use this application:

*   When you are more fam (URL_TO_INSERT_RECORD_6132 https://fairsharing.org/FAIRsharing.d0886a) iliar with working with a user interface and not so much with configuration scripts or coding, and want to interactively explore and manipulate your data
*   When you have data that needs some manipulation, i.e. messy data, before conversion to RDF (URL_TO_INSERT_RECORD_6133 https://fairsharing.org/FAIRsharing.p77ph9) 


Installation:

*   For working with RDF (URL_TO_INSERT_RECORD_6134 https://fairsharing.org/FAIRsharing.p77ph9) , a plugin is needed.
*   It is possible to use a distribution of openrefine that comes prepackaged with this plugin and other useful features. However, this package is not maintained anymore.
*   It is therefore advised to download the latest version of OpenRefine and RDF (URL_TO_INSERT_RECORD_6135 https://fairsharing.org/FAIRsharing.p77ph9)  plugin and install the plugin yourself.


Details:

*   [website](https://openrefine.org/), [GitHub](https://github.com (URL_TO_INSERT_RECORD_6136 https://fairsharing.org/FAIRsharing.c55d5e) /OpenRefine/OpenRefine)
*   [download](https://openrefine.org/download.html), [installation instructions](https://github.com (URL_TO_INSERT_RECORD_6137 https://fairsharing.org/FAIRsharing.c55d5e) /OpenRefine/OpenRefine/wiki/Installation-Instructions)
*   [documentation](https://github.com (URL_TO_INSERT_RECORD_6138 https://fairsharing.org/FAIRsharing.c55d5e) /OpenRefine/OpenRefine/wiki) 
*   Tutorial(s), see [OpenRefine Foundation course](https://courses.tranzf.org/course/view.php?id=18), [screencast](https://github.com (URL_TO_INSERT_RECORD_6139 https://fairsharing.org/FAIRsharing.c55d5e) /OpenRefine/OpenRefine/wiki/Screencasts), [curated list](https://github.com (URL_TO_INSERT_RECORD_6140 https://fairsharing.org/FAIRsharing.c55d5e) /OpenRefine/OpenRefine/wiki/External-Resources)
*   Input format (URL_TO_INSERT_TERM_6142 https://fairsharing.org/search?recordType=model_and_format) (s): Excel, CVS/TSV, XML (URL_TO_INSERT_RECORD_6143 https://fairsharing.org/FAIRsharing.b5cc91) , JSON (URL_TO_INSERT_RECORD_6144 https://fairsharing.org/FAIRsharing.5bbab9) , (relational) database (URL_TO_INSERT_TERM_6141 https://fairsharing.org/search?fairsharingRegistry=Database) s
*   It is possible to automate, see [FAQ](https://github.com (URL_TO_INSERT_RECORD_6145 https://fairsharing.org/FAIRsharing.c55d5e) /OpenRefine/OpenRefine/wiki/FAQ#can-openrefine-be-used-as-a-piece-of-a-larger-etl-pipeline)
*   Complex manipulation of data is possible with [GREL](https://github.com (URL_TO_INSERT_RECORD_6146 https://fairsharing.org/FAIRsharing.c55d5e) /OpenRefine/OpenRefine/wiki/General-Refine-Expression-Language) or Python ([Jython](https://www.jython.org/)) expressions
*   It is possible to reuse map (URL_TO_INSERT_RECORD_6148 https://fairsharing.org/FAIRsharing.53edcc) pings through exporting part of the undo/redo history that led to the RDF (URL_TO_INSERT_RECORD_6147 https://fairsharing.org/FAIRsharing.p77ph9)  export, see [replaying operations](https://github.com (URL_TO_INSERT_RECORD_6149 https://fairsharing.org/FAIRsharing.c55d5e) /OpenRefine/OpenRefine/wiki/History#replaying-operations)


Installing the RDF (URL_TO_INSERT_RECORD_6150 https://fairsharing.org/FAIRsharing.p77ph9)  extension:

*   Download on GitHub (URL_TO_INSERT_RECORD_6151 https://fairsharing.org/FAIRsharing.c55d5e)  ([wiki](https://github.com (URL_TO_INSERT_RECORD_6152 https://fairsharing.org/FAIRsharing.c55d5e) /stkenny/grefine-rdf-extension/wiki))
*   Enables graphical map (URL_TO_INSERT_RECORD_6154 https://fairsharing.org/FAIRsharing.53edcc) ping of data to an RDF (URL_TO_INSERT_RECORD_6153 https://fairsharing.org/FAIRsharing.p77ph9)  skeleton for export (with autocomplete)
*   Import and export to Turtle (URL_TO_INSERT_RECORD_6155 https://fairsharing.org/FAIRsharing.3e194c)  and RDF (URL_TO_INSERT_RECORD_6156 https://fairsharing.org/FAIRsharing.p77ph9) /XML (URL_TO_INSERT_RECORD_6157 https://fairsharing.org/336) 
*   Query against a Sparql endpoint

Notes on how to install extensions: [install extensions](https://docs.openrefine.org/manual/installing#installing-extensions)


#### OpenRefine metadata extension

The OpenRefine metadata extension adds support for uploading metadata of a dataset to a so-called [FAIR Data Point](https://github.com (URL_TO_INSERT_RECORD_6160 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRDataTeam/FAIRDataPoint-Spec) (FDP). A FDP (URL_TO_INSERT_RECORD_6161 https://fairsharing.org/298)  is a metadata repository (URL_TO_INSERT_TERM_6158 https://fairsharing.org/search?recordType=repository)  that provides access to metadata in a FAIR (URL_TO_INSERT_RECORD_6162 https://fairsharing.org/FAIRsharing.WWI10U)  way. This extension can be used in conjunction with the RDF (URL_TO_INSERT_RECORD_6159 https://fairsharing.org/FAIRsharing.p77ph9)  extension.

*   OpenRefine-metadata-extension ([GitHub](https://github.com (URL_TO_INSERT_RECORD_6163 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRDataTeam/OpenRefine-metadata-extension), [download](https://github.com (URL_TO_INSERT_RECORD_6164 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRDataTeam/OpenRefine-metadata-extension/releases))


### Transformation/mapping languages

Some users may favor a text-based approach over a graphical tool. In addition, graphical tools may come with several disadvantages: map (URL_TO_INSERT_RECORD_6165 https://fairsharing.org/FAIRsharing.53edcc) ping and generation is tied to that particular application, exchange of map (URL_TO_INSERT_RECORD_6166 https://fairsharing.org/FAIRsharing.53edcc) pings (between users or applications) may be difficult, and automation or integration in a built pipeline may not be possible. 

A more flexible approach is offered by transformat (URL_TO_INSERT_TERM_6167 https://fairsharing.org/search?recordType=model_and_format) ion or map (URL_TO_INSERT_RECORD_6169 https://fairsharing.org/FAIRsharing.53edcc) ping languages. These languages allow to declare map (URL_TO_INSERT_RECORD_6170 https://fairsharing.org/FAIRsharing.53edcc) pings and RDF (URL_TO_INSERT_RECORD_6168 https://fairsharing.org/FAIRsharing.p77ph9)  generation independent from a particular application. 


#### D2RQ

[D2RQ](http://d2rq.org/d2rq-language) is a map (URL_TO_INSERT_RECORD_6172 https://fairsharing.org/FAIRsharing.53edcc) ping language to describe direct map (URL_TO_INSERT_RECORD_6173 https://fairsharing.org/FAIRsharing.53edcc) pings between the tables and columns of a relational database (URL_TO_INSERT_TERM_6171 https://fairsharing.org/search?fairsharingRegistry=Database)  (RDB) to classes and properties.


#### R2RML

A well-known map (URL_TO_INSERT_RECORD_6179 https://fairsharing.org/FAIRsharing.53edcc) ping language is [R2RML](https://www.w3.org/TR/r2rml/) (RDB to RDF (URL_TO_INSERT_RECORD_6176 https://fairsharing.org/FAIRsharing.p77ph9)  Map (URL_TO_INSERT_RECORD_6180 https://fairsharing.org/FAIRsharing.53edcc) ping Language), which is an RDF (URL_TO_INSERT_RECORD_6177 https://fairsharing.org/FAIRsharing.p77ph9)  vocabulary to describe map (URL_TO_INSERT_RECORD_6181 https://fairsharing.org/FAIRsharing.53edcc) pings from relational database (URL_TO_INSERT_TERM_6174 https://fairsharing.org/search?fairsharingRegistry=Database) s to RDF (URL_TO_INSERT_RECORD_6178 https://fairsharing.org/FAIRsharing.p77ph9) . R2R (URL_TO_INSERT_RECORD_6175 https://fairsharing.org/FAIRsharing.ZEbjok) ML is an official W3C recommendation and is supported by many tools.


#### RML

[RML](https://rml.io/specs/rml/) (Rule markup Language) is a map (URL_TO_INSERT_RECORD_6187 https://fairsharing.org/FAIRsharing.53edcc) ping language that extends R2R (URL_TO_INSERT_RECORD_6184 https://fairsharing.org/FAIRsharing.ZEbjok) ML to also support map (URL_TO_INSERT_RECORD_6188 https://fairsharing.org/FAIRsharing.53edcc) pings from other structured format (URL_TO_INSERT_TERM_6182 https://fairsharing.org/search?recordType=model_and_format) s such as CSV (URL_TO_INSERT_RECORD_6183 https://fairsharing.org/FAIRsharing.1943d4)  and JSON (URL_TO_INSERT_RECORD_6186 https://fairsharing.org/FAIRsharing.5bbab9)  (it is a superset of R2R (URL_TO_INSERT_RECORD_6185 https://fairsharing.org/FAIRsharing.ZEbjok) ML). 

*   Online graphical editor for creating RML map (URL_TO_INSERT_RECORD_6189 https://fairsharing.org/FAIRsharing.53edcc) pings: [RMLEditor](https://app.rml.io/rmleditor/) (beta, with some size limitations)

Downside of RML and R2R (URL_TO_INSERT_RECORD_6190 https://fairsharing.org/FAIRsharing.ZEbjok) ML is that they are designed to be processed by machines: manual definition of rules using these RDF (URL_TO_INSERT_RECORD_6191 https://fairsharing.org/FAIRsharing.p77ph9)  vocabularies is complex, time-consuming, and comes with a steep learning curve. To address these problems, the map (URL_TO_INSERT_RECORD_6192 https://fairsharing.org/FAIRsharing.53edcc) ping language YARRRML was created.


#### YARRRML

YARRRML is a human-readable text-based representation for generation rules that can be directly translated to RML. It is a subset of [YAML](https://en.wikipedia.org/wiki/YAML), which is a human-friendly data serialization standard (URL_TO_INSERT_TERM_6193 https://fairsharing.org/search?fairsharingRegistry=Standard)  that is commonly used for configuration files. 

YAML uses Python-style indentation to indicate nesting (no tabs), has compact notations for lists and map (URL_TO_INSERT_RECORD_6195 https://fairsharing.org/FAIRsharing.53edcc) s and is a superset of JSON (URL_TO_INSERT_RECORD_6194 https://fairsharing.org/FAIRsharing.5bbab9) . YARRRML hides the complexity of machine-processable rules while it remains interoperable with existing tools.



*   YARRRML [tutorial](https://rml.io/yarrrml/tutorial/getting-started/) and [specs](https://rml.io/yarrrml/spec/).

There’s an online YARRRML editor/playground called Matey that allows you to interactively edit YARRRML files and see the results of the conversion on a small sample dataset. It also exports YARRRML as RML and R2R (URL_TO_INSERT_RECORD_6196 https://fairsharing.org/FAIRsharing.ZEbjok) ML.



*   [Matey](https://rml.io/yarrrml/matey/#)

A YARRRML parser is also available ([GitHub](https://github.com (URL_TO_INSERT_RECORD_6198 https://fairsharing.org/FAIRsharing.c55d5e) /rmlio/yarrrml-parser), [download](https://github.com (URL_TO_INSERT_RECORD_6199 https://fairsharing.org/FAIRsharing.c55d5e) /RMLio/yarrrml-parser/releases)) that converts to RML/R2RML so that map (URL_TO_INSERT_RECORD_6197 https://fairsharing.org/FAIRsharing.53edcc) ping/translation rules can be executed by any tool that accepts RML/R2RML.

Defining your map (URL_TO_INSERT_RECORD_6201 https://fairsharing.org/FAIRsharing.53edcc) pings in YARRRML is advisable, considering it’s easy to understand and can be converted to RML or its subset R2R (URL_TO_INSERT_RECORD_6200 https://fairsharing.org/FAIRsharing.ZEbjok) ML, used by many tools for declarative map (URL_TO_INSERT_RECORD_6202 https://fairsharing.org/FAIRsharing.53edcc) pings.


### RML-based tools


#### RMLMapper

RMLMap (URL_TO_INSERT_RECORD_6204 https://fairsharing.org/FAIRsharing.53edcc) per is the reference implementation for RML-based map (URL_TO_INSERT_RECORD_6205 https://fairsharing.org/FAIRsharing.53edcc) ping tools. It has the option to generate PRO (URL_TO_INSERT_RECORD_6203 https://fairsharing.org/FAIRsharing.3e88d6)  (URL_TO_INSERT_RECORD_6206 https://fairsharing.org/FAIRsharing.4ndncv) V-O (URL_TO_INSERT_RECORD_6208 https://fairsharing.org/FAIRsharing.2rm2b3)  metadata for the conversion, suitable as FAIR (URL_TO_INSERT_RECORD_6207 https://fairsharing.org/FAIRsharing.WWI10U)  metadata. Although easy to use/configure, it has the downside that it loads all data in memory, which means there is a limit on the size of the data that can be converted.

*   Download: [rmlmapper-java releases](https://github.com (URL_TO_INSERT_RECORD_6209 https://fairsharing.org/FAIRsharing.c55d5e) /RMLio/rmlmapper-java/releases)


#### SDM-RDFizer

SDM-RDFizer is a Python-based tool which is similar to RMLMap (URL_TO_INSERT_RECORD_6210 https://fairsharing.org/FAIRsharing.53edcc) per but is suited for large datasets. It requires some additional configurations for settings like intermediary file locations.

*   For download and instructions, see [SDM-RDFizer (GitHub)](https://github.com (URL_TO_INSERT_RECORD_6211 https://fairsharing.org/FAIRsharing.c55d5e) /SDM-TIB/SDM-RDFizer).

### Morph-KGC

Morph-KGC is a powerful engine to generate RDF (URL_TO_INSERT_RECORD_6214 https://fairsharing.org/FAIRsharing.p77ph9)  and RDF (URL_TO_INSERT_RECORD_6215 https://fairsharing.org/FAIRsharing.p77ph9) -star knowledge graphs. It supports a wide range of relational database (URL_TO_INSERT_TERM_6212 https://fairsharing.org/search?fairsharingRegistry=Database) s and data file format (URL_TO_INSERT_TERM_6213 https://fairsharing.org/search?recordType=model_and_format) s. It scales to large volumes of data and runs from the command line or as a python library (creating [RDFLib](https://github.com (URL_TO_INSERT_RECORD_6216 https://fairsharing.org/FAIRsharing.c55d5e) /RDFLib/rdflib) or [Oxigraph](https://github.com (URL_TO_INSERT_RECORD_6217 https://fairsharing.org/FAIRsharing.c55d5e) /oxigraph/oxigraph) graphs). It is also integrated in [kglab](https://github.com (URL_TO_INSERT_RECORD_6218 https://fairsharing.org/FAIRsharing.c55d5e) /DerwenAI/kglab), an abstraction layer for working with knowledge graphs using popular libraries.

* Download: [Morph-KGC](https://github.com (URL_TO_INSERT_RECORD_6219 https://fairsharing.org/FAIRsharing.c55d5e) /oeg-upm/morph-kgc).
* Documentation: [readthedocs](https://morph-kgc.readthedocs.io).

  
#### Other RML-based tools

There are other RML-based conversion tools that are more tailored to particular scenarios, for instance [RMLStreamer](https://github.com (URL_TO_INSERT_RECORD_6220 https://fairsharing.org/FAIRsharing.c55d5e) /RMLio/RMLStreamer) for streaming data. For an overview of feature completeness of tools, see the [RML Implementation Report](https://rml.io/implementation-report/).


#### SPARQL-Generate

[SPARQL-Generate](https://ci.mines-stetienne.fr/sparql-generate/) is a template-based language for generating RDF (URL_TO_INSERT_RECORD_6224 https://fairsharing.org/FAIRsharing.p77ph9)  streams from a range of input format (URL_TO_INSERT_TERM_6222 https://fairsharing.org/search?recordType=model_and_format) s, such as tabular data, JSON (URL_TO_INSERT_RECORD_6225 https://fairsharing.org/FAIRsharing.5bbab9) , XML (URL_TO_INSERT_RECORD_6223 https://fairsharing.org/FAIRsharing.b5cc91) , and relational database (URL_TO_INSERT_TERM_6221 https://fairsharing.org/search?fairsharingRegistry=Database) s. It extends SP (URL_TO_INSERT_RECORD_6230 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_6226 https://fairsharing.org/FAIRsharing.87ccfd)  1.1, which means it should feel fam (URL_TO_INSERT_RECORD_6228 https://fairsharing.org/FAIRsharing.d0886a) iliar for everyone already fam (URL_TO_INSERT_RECORD_6229 https://fairsharing.org/FAIRsharing.d0886a) iliar with SP (URL_TO_INSERT_RECORD_6231 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_6227 https://fairsharing.org/FAIRsharing.87ccfd)  queries.

*   To quickly write and test queries (on small datasets), use the [SPARQL-Generate Playground](https://ci.mines-stetienne.fr/sparql-generate/playground.html) web-application.
*   The [SPARQL-Generate executable jar](https://ci.mines-stetienne.fr/sparql-generate/language-cli.html) is a CL (URL_TO_INSERT_RECORD_6232 https://fairsharing.org/FAIRsharing.j9y503) I (command line interface) tool for executing SP (URL_TO_INSERT_RECORD_6234 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_6233 https://fairsharing.org/FAIRsharing.87ccfd) -Generate queries. 


### Virtual graph

Tools that dynamically render a relational database (URL_TO_INSERT_TERM_6235 https://fairsharing.org/search?fairsharingRegistry=Database)  as virtual RDF (URL_TO_INSERT_RECORD_6236 https://fairsharing.org/FAIRsharing.p77ph9)  graph.


#### Ontop

[Ontop](https://ontop-vkg.org/) is a virtual knowledge graph system for arbitrary database (URL_TO_INSERT_TERM_6237 https://fairsharing.org/search?fairsharingRegistry=Database) s. It has its own map (URL_TO_INSERT_RECORD_6239 https://fairsharing.org/FAIRsharing.53edcc) ping language but also supports R2R (URL_TO_INSERT_RECORD_6238 https://fairsharing.org/FAIRsharing.ZEbjok) ML. It runs as a command line tool, but there is also an Ontop plugin for Protégé to define map (URL_TO_INSERT_RECORD_6240 https://fairsharing.org/FAIRsharing.53edcc) pings and import triples using a GUI application.

Although triples are exposed as a virtual graph, it is possible to export to RDF (URL_TO_INSERT_RECORD_6241 https://fairsharing.org/FAIRsharing.p77ph9)  using a ‘materialize’ command.


### Proprietary tools

A proprietary tool is a commercial tool for which licenses need to be obtained


#### TopBraid Composer

[TopBraid Composer Maestro Edition](https://www.topquadrant.com/products/topbraid-composer/) (commercial license) is an Integrated development environment (IDE) for working with semantic web technologies, such as RDF (URL_TO_INSERT_RECORD_6249 https://fairsharing.org/FAIRsharing.p77ph9)  and OWL (URL_TO_INSERT_RECORD_6248 https://fairsharing.org/FAIRsharing.atygwy) . It has support for converting a range of format (URL_TO_INSERT_TERM_6243 https://fairsharing.org/search?recordType=model_and_format) s to RDF (URL_TO_INSERT_RECORD_6250 https://fairsharing.org/FAIRsharing.p77ph9) , including tabular/spreadsheet data, XML (URL_TO_INSERT_RECORD_6245 https://fairsharing.org/FAIRsharing.b5cc91) , JSON (URL_TO_INSERT_RECORD_6252 https://fairsharing.org/FAIRsharing.5bbab9) , and RDB. It uses a straightforward conversion to RDF (URL_TO_INSERT_RECORD_6251 https://fairsharing.org/FAIRsharing.p77ph9) , which doesn’t allow for extensive customization: sheets and tabular data are directly map (URL_TO_INSERT_RECORD_6253 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_6256 https://fairsharing.org/FAIRsharing.31385c)  to a spreadsheet ontology (URL_TO_INSERT_TERM_6244 https://fairsharing.org/search?recordType=terminology_artefact) , XML (URL_TO_INSERT_RECORD_6246 https://fairsharing.org/FAIRsharing.b5cc91)  directly according to an XML (URL_TO_INSERT_RECORD_6247 https://fairsharing.org/FAIRsharing.b5cc91)  vocabulary, and relational database (URL_TO_INSERT_TERM_6242 https://fairsharing.org/search?fairsharingRegistry=Database) s are map (URL_TO_INSERT_RECORD_6254 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_6257 https://fairsharing.org/FAIRsharing.31385c)  using direct map (URL_TO_INSERT_RECORD_6255 https://fairsharing.org/FAIRsharing.53edcc) ping with [D2RQ](http://d2rq.org/d2rq-language). 

The resulting RDF (URL_TO_INSERT_RECORD_6260 https://fairsharing.org/FAIRsharing.p77ph9)  directly reflects the structure and schema of the database (URL_TO_INSERT_TERM_6258 https://fairsharing.org/search?fairsharingRegistry=Database) . However, once loaded as RDF (URL_TO_INSERT_RECORD_6261 https://fairsharing.org/FAIRsharing.p77ph9) , transformat (URL_TO_INSERT_TERM_6259 https://fairsharing.org/search?recordType=model_and_format) ions and elaborate map (URL_TO_INSERT_RECORD_6262 https://fairsharing.org/FAIRsharing.53edcc) pings can be applied using TopBraids visual scripting language [SPARQLMotion](https://www.topquadrant.com/technology/sparqlmotion/), or SP (URL_TO_INSERT_RECORD_6263 https://fairsharing.org/FAIRsharing.s63y3p) IN/Sparql construct queries.


#### Virtuoso Universal Serve

[Virtuoso Universal Server](http://virtuoso.openlinksw.com/) is a "universal server" that combines a database (URL_TO_INSERT_TERM_6264 https://fairsharing.org/search?fairsharingRegistry=Database)  engine, web server, triple/quat store, and more. It powers many nodes of the Linked Open Data cloud, for instance [dbpedia](https://www.dbpedia.org (URL_TO_INSERT_RECORD_6265 https://fairsharing.org/FAIRsharing.cUG0cV) /). 

The Virtuoso “Sponger” (RDFizer) and it’s predefined “cartridges” (containing an Entity Extractor and an Ontology (URL_TO_INSERT_TERM_6267 https://fairsharing.org/search?recordType=terminology_artefact)  Map (URL_TO_INSERT_RECORD_6269 https://fairsharing.org/FAIRsharing.53edcc) per) are responsible for generating linked data from various forms of data (tabular and RDB). These cartridges are highly customizable, but it is also possible to write new ones. It is also possible to generate linked data views from relational database (URL_TO_INSERT_TERM_6266 https://fairsharing.org/search?fairsharingRegistry=Database) s using R2R (URL_TO_INSERT_RECORD_6268 https://fairsharing.org/FAIRsharing.ZEbjok) ML. Linked data is generated on-the-fly but may be ingested into Virtuoso’s quad store.

There is also an open-source edition available, known as OpenLink Virtuoso.

*   [OpenLink Virtuoso (GitHub)](https://github.com (URL_TO_INSERT_RECORD_6270 https://fairsharing.org/FAIRsharing.c55d5e) /openlink/virtuoso-opensource)


## Alternative approaches

### Coding yourself

Instead of relying on a tool, most programmers may prefer to write their own conversion code/scripts using their language of choice (e.g. Python, Java). This is probably the fastest, most accessible option because it capitalizes on existing programming skills and avoids the overhea (URL_TO_INSERT_RECORD_6275 https://fairsharing.org/FAIRsharing.pn1sr5) d of learning another tool or map (URL_TO_INSERT_RECORD_6272 https://fairsharing.org/FAIRsharing.53edcc) ping language. It offers great flexibility: it is highly customizable, any input and output format (URL_TO_INSERT_TERM_6271 https://fairsharing.org/search?recordType=model_and_format)  is possible, and it can be scaled to large datasets. Downside is that it may not be easy to adapt existing code to changing map (URL_TO_INSERT_RECORD_6273 https://fairsharing.org/FAIRsharing.53edcc) ping requirements. Also, it may be difficult for others to understand the map (URL_TO_INSERT_RECORD_6274 https://fairsharing.org/FAIRsharing.53edcc) ping. In addition, custom code may be susceptible to bugs, while established tools have been tested thoroughly.

Although it is possible to generate RDF (URL_TO_INSERT_RECORD_6276 https://fairsharing.org/FAIRsharing.p77ph9)  by constructing triples using basic string (URL_TO_INSERT_RECORD_6278 https://fairsharing.org/FAIRsharing.9b7wvk)  operations, it pays off to use a RDF (URL_TO_INSERT_RECORD_6277 https://fairsharing.org/FAIRsharing.p77ph9)  library for these tasks.

For python there’s the [RDFLib](https://rdflib.dev/) package. Working in Jupyter notebooks with one of the common data manipulation libraries (e.g. pandas) allows you to interactively explore and manipulate the data before converting it into RDF (URL_TO_INSERT_RECORD_6279 https://fairsharing.org/FAIRsharing.p77ph9) .

For Java the two most common libraries for working with RDF (URL_TO_INSERT_RECORD_6280 https://fairsharing.org/FAIRsharing.p77ph9)  are [Apache Jena](https://jena.apache.org/) and [Eclipse RDF4J](https://rdf4j.org/).


## What to read next?

* [A data engineer's guide to semantic modelling - Ilaria Maresi](https://doi.org/10.5281/zenodo.3898519) (Zenodo (URL_TO_INSERT_RECORD_6281 https://fairsharing.org/FAIRsharing.wy4egf) )

````{rdmkit_panel}
````

````{dropdown} **References**
````

## Authors
````{authors_fairplus}
Eelke: Writing - Original Draft
Jolanda: Writing - Review & Editing
Kees: Writing - Review & Editing
````


## License

````{license_fairplus}
CC-BY-4.0
````
