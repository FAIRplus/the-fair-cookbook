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

> Present an inventory of a selection of popular tools for converting datasets in different format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s (e.g. CSV(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc4180), JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259), RDBMs, XML(URL_TO_INSERT_RECORD https://www.w3.org/TR/xml/)) to RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/), and to provide guidance for choosing the right tool.

---


## Graphical Overview of the FAIRification Recipe Objectives

Figure {numref}`rdf-conversion-figure1` shows an example ETL workflow.


````{dropdown} 
:open:
```{figure} rdf-conversion.md-figure1.mmd.png
---
name: rdf-conversion-figure1
alt: Building an ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) with Robot tool
---
Building an ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) with Robot tool.
```
````

---


## Requirements

* recipe dependency:
    * This recipe is an example of how to perform ETL with the RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format). For tools on general ETL process. Please check recipe {ref}`fcb-interop-etl`
* knowledge requirement:
  * basic understanding of: command line syntax, RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/), configuration using YAML
* other:
  * plan/model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) of how to map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map) your source entities/properties to classes/types/properties, and how to create resource URI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)s <!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO would be nice to link out to a recipe about minting -->

---

## Table of Data Standards

| Data Format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s  | Terminologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) | Model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s  |
| :------------- | :------------- | :------------- |
| R2R(URL_TO_INSERT_RECORD https://www.rvdata.us/)ML<!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO needs a link -->    |   |   |
| RML<!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO needs a link -->      |   |   |
| YARRRML<!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO needs a link -->  |   |   |
| YAML<!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO needs a link -->     |   |   |

---

## Introduction

Research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) data is produced in a range of different format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s, such as spreadsheets, delimiter-separated files (CVS, TSV(URL_TO_INSERT_RECORD http://www.iana.org/assignments/media-types/text/tab-separated-values)), or (relational) database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)s. To improve reusability of data and make them more FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/), these data sets can be published in the _de facto_ standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) for reusable data, RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/). 

There are many tools available to convert non-RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) data to RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/), a process also known as ‘triplification’ or ‘RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/)izing’ of data. See for instance the lists maintained by W3C at [ConverterToRdf](https://www.w3.org/wiki/ConverterToRdf), [RDFImportersAndAdapters](https://www.w3.org/wiki/RDFImportersAndAdapters) (outdated), and [RdfAndSql](https://www.w3.org/wiki/RdfAndSql), or perform a quick Google search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/). 

However, finding the right tool for a particular scenario can be difficult and time-consuming. A user needs to try the tool and invest some time in understanding it, while its limitations may only be discovered later. Many tools are limited to a particular input format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) or come with a particular application; are no longer supported, maintained or suffer from bugs; need a significant time investment to learn the specifics of their use or configuration options; or lack sufficient documentation. 

This recipe aims to address these problems by presenting a selection of conversion tools, and giving guidance on choosing the right tool, that adhere to the following (somewhat subjective) criteria:

*   Generic applicability (e.g. not limited to OWL(URL_TO_INSERT_RECORD http://www.w3.org/TR/owl-overview/) or SKOS(URL_TO_INSERT_RECORD http://www.w3.org/TR/skos-reference))
*   Multiple format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s: tabular (Excel, CSV(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc4180) etc), hierarch(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ical (XML(URL_TO_INSERT_RECORD https://www.w3.org/TR/xml/), JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259)), RDBs
*   Well documented
*   Actively maintained
*   Easy to install and use (i.e. no compilation or docker needed)
*   Reasonably stable/bug free
*   Available for all major platforms (Windows, Mac, Linux)

## Step by step process

### Step 1: consider requirements

To choose the best tool for your conversion task consider the following:

*   Is a GUI preferred, or a command line interface? Should it be possible to automate the conversion?
*   Should the map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping be reused (repeated)? Should map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)pings be defined in an open standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) independently from a particular tool?
*   Is the data messy or does it require significant transformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion before conversion?
*   Might it be better to present the data as a virtual graph (mainly for database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)s) than performing an actual conversion?

Based on these criteria, find the right tool in the table below. Jump to the section on that tool to read about additional considerations and details.

|                                           | GUI | CL(URL_TO_INSERT_RECORD https://github.com/obophenotype/cell-ontology)I, automation | Reuse map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)pings | Messy data | Virtual graph |
| ----------------------------------------- | --- | --------------- | -------------- | ---------- | ------------- |
| OpenRefine + RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) extension                | ✅   | +/-         | +/-        | ✅          |               |
| TopBraid Composer (ME)1                   | ✅   |                 |                |            |               |
| RML-based tools (RML map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)per, SDM-RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/)izer) |     | ✅               | ✅              |            |               |
| SP(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/SP)ARQL(URL_TO_INSERT_RECORD http://www.w3.org/TR/sparql11-overview/)-Generate                           |     | ✅               | ✅              |            |               |
| Ontop (RDB only)                          |     | ✅               | ✅              |            | ✅             |
| Virtuoso (proprietary tool)                                 |     |                 | ✅              |            | ✅             |
| Custom code                               |     | ✅               |                | ✅          |               |

Except for OpenRefine and writing your own code, most tools make use of a map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping language to declare the rules for conversion to RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/). Read the section on transformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion/map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping languages to find out more about these languages and why it makes sense to prefer YARRRML as the map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping language of choice.

### Step 2: select/install tool

Select one or more tools to install and evaluate, go through the tutorials, and try the tool for conversion of a small selection of your data.


## Tools


### OpenRefine with RDF extension

OpenRefine is an open source data transformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion tool for exploring, cleaning, and transforming all kinds of structured data. It offers a spreadsheet-like user interface that allows users to interactively explore and transform their data. Data can be manipulated through menu actions and GREL (Google Refine Expression Language) or Python/Jython expressions. It keeps a undo/redo history which can also be used to ‘replay’ transformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion and configuration steps.

OpenRefine is open source and has an active community. Additional functionality is provided through extensions and custom distributions. For instance, the ability to work with RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) is provided by installing the RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) extension. Publication to FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) data point(URL_TO_INSERT_RECORD https://github.com/DTL-FAIRData/FAIRDataPoint)s is provided through the FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) metadata extension.


When you should use this application:

*   When you are more fam(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#fam)iliar with working with a user interface and not so much with configuration scripts or coding, and want to interactively explore and manipulate your data
*   When you have data that needs some manipulation, i.e. messy data, before conversion to RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/)


Installation:

*   For working with RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/), a plugin is needed.
*   It is possible to use a distribution of openrefine that comes prepackaged with this plugin and other useful features. However, this package is not maintained anymore.
*   It is therefore advised to download the latest version of OpenRefine and RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) plugin and install the plugin yourself.


Details:

*   [website](https://openrefine.org/), [GitHub(URL_TO_INSERT_RECORD https://github.com/)(URL_TO_INSERT_RECORD https://github.com/)](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/OpenRefine/OpenRefine)
*   [download](https://openrefine.org/download.html), [installation instructions](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/OpenRefine/OpenRefine/wiki/Installation-Instructions)
*   [documentation](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/OpenRefine/OpenRefine/wiki) 
*   Tutorial(s), see [OpenRefine Foundation course](https://courses.tranzf.org/course/view.php?id=18), [screencast](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/OpenRefine/OpenRefine/wiki/Screencasts), [curated list](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/OpenRefine/OpenRefine/wiki/External-Resources)
*   Input format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)(s): Excel, CVS/TSV(URL_TO_INSERT_RECORD http://www.iana.org/assignments/media-types/text/tab-separated-values), XML(URL_TO_INSERT_RECORD https://www.w3.org/TR/xml/), JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259), (relational) database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)s
*   It is possible to automate, see [FAQ](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/OpenRefine/OpenRefine/wiki/FAQ#can-openrefine-be-used-as-a-piece-of-a-larger-etl-pipeline)
*   Complex manipulation of data is possible with [GREL](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/OpenRefine/OpenRefine/wiki/General-Refine-Expression-Language) or Python ([Jython](https://www.jython.org/)) expressions
*   It is possible to reuse map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)pings through exporting part of the undo/redo history that led to the RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) export, see [replaying operations](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/OpenRefine/OpenRefine/wiki/History#replaying-operations)


Installing the RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) extension:

*   Download on GitHub(URL_TO_INSERT_RECORD https://github.com/)(URL_TO_INSERT_RECORD https://github.com/) ([wiki](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/stkenny/grefine-rdf-extension/wiki))
*   Enables graphical map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping of data to an RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) skeleton for export (with autocomplete)
*   Import and export to Turtle(URL_TO_INSERT_RECORD http://www.w3.org/TR/turtle/) and RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/)/XML(URL_TO_INSERT_RECORD https://www.w3.org/TR/xml/)(URL_TO_INSERT_RECORD http://www.w3.org/TR/rdf-syntax-grammar/)
*   Query against a Sparql endpoint

Notes on how to install extensions: [install extensions](https://docs.openrefine.org/manual/installing#installing-extensions)


#### OpenRefine metadata extension

The OpenRefine metadata extension adds support for uploading metadata of a dataset to a so-called [FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) Data Point(URL_TO_INSERT_RECORD https://github.com/DTL-FAIRData/FAIRDataPoint)](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/FAIRDataTeam/FAIRDataPoint-Spec) (FDP(URL_TO_INSERT_RECORD https://github.com/DTL-FAIRData/FAIRDataPoint)). A FDP(URL_TO_INSERT_RECORD https://github.com/DTL-FAIRData/FAIRDataPoint) is a metadata repository (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository) that provides access to metadata in a FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) way. This extension can be used in conjunction with the RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) extension.

*   OpenRefine-metadata-extension ([GitHub](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/FAIRDataTeam/OpenRefine-metadata-extension), [download](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/FAIRDataTeam/OpenRefine-metadata-extension/releases))


### Transformation/mapping languages

Some users may favor a text-based approach over a graphical tool. In addition, graphical tools may come with several disadvantages: map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping and generation is tied to that particular application, exchange of map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)pings (between users or applications) may be difficult, and automation or integration in a built pipeline may not be possible. 

A more flexible approach is offered by transformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion or map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping languages. These languages allow to declare map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)pings and RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) generation independent from a particular application. 


#### D2RQ

[D2RQ](http://d2rq.org/d2rq-language) is a map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping language to describe direct map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)pings between the tables and columns of a relational database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database) (RDB) to classes and properties.


#### R2RML

A well-known map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping language is [R2RML](https://www.w3.org/TR/r2rml/) (RDB to RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) Map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping Language), which is an RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) vocabulary to describe map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)pings from relational database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)s to RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/). R2R(URL_TO_INSERT_RECORD https://www.rvdata.us/)ML is an official W3C recommendation and is supported by many tools.


#### RML

[RML](https://rml.io/specs/rml/) (Rule markup Language) is a map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping language that extends R2R(URL_TO_INSERT_RECORD https://www.rvdata.us/)ML to also support map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)pings from other structured format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s such as CSV(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc4180) and JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) (it is a superset of R2R(URL_TO_INSERT_RECORD https://www.rvdata.us/)ML). 

*   Online graphical editor for creating RML map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)pings: [RMLEditor](https://app.rml.io/rmleditor/) (beta, with some size limitations)

Downside of RML and R2R(URL_TO_INSERT_RECORD https://www.rvdata.us/)ML is that they are designed to be processed by machines: manual definition of rules using these RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) vocabularies is complex, time-consuming, and comes with a steep learning curve. To address these problems, the map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping language YARRRML was created.


#### YARRRML

YARRRML is a human-readable text-based representation for generation rules that can be directly translated to RML. It is a subset of [YAML](https://en.wikipedia.org/wiki/YAML), which is a human-friendly data serialization standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) that is commonly used for configuration files. 

YAML uses Python-style indentation to indicate nesting(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) (no tabs), has compact notations for lists and map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)s and is a superset of JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259). YARRRML hides the complexity of machine-processable rules while it remains interoperable with existing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) tools.



*   YARRRML [tutorial](https://rml.io/yarrrml/tutorial/getting-started/) and [specs](https://rml.io/yarrrml/spec/).

There’s an online YARRRML editor/playground called Matey that allows you to interactively edit YARRRML files and see the results of the conversion on a small sample dataset. It also exports YARRRML as RML and R2R(URL_TO_INSERT_RECORD https://www.rvdata.us/)ML.



*   [Matey](https://rml.io/yarrrml/matey/#)

A YARRRML parser is also available ([GitHub](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/rmlio/yarrrml-parser), [download](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/RMLio/yarrrml-parser/releases)) that converts to RML/R2R(URL_TO_INSERT_RECORD https://www.rvdata.us/)ML so that map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping/translation rules can be executed by any tool that accepts RML/R2R(URL_TO_INSERT_RECORD https://www.rvdata.us/)ML.

Defining your map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)pings in YARRRML is advisable, considering it’s easy to understand and can be converted to RML or its subset R2R(URL_TO_INSERT_RECORD https://www.rvdata.us/)ML, used by many tools for declarative map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)pings.


### RML-based tools


#### RMLMapper

RMLMap(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)per is the reference implementation for RML-based map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping tools. It has the option to generate PRO(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD http://www.sparontologies.net/ontologies/pro)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD https://proconsortium.org/)(URL_TO_INSERT_RECORD https://w3id.org/ro/)V-O(URL_TO_INSERT_RECORD http://www.w3.org/TR/prov-o/) metadata for the conversion, suitable as FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) metadata. Although easy to use/configure, it has the downside that it loads all data in memory, which means there is a limit on the size of the data that can be converted.

*   Download: [rmlmap(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)per-java releases](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/RMLio/rmlmapper-java/releases)


#### SDM-RDFizer

SDM-RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/)izer is a Python-based tool which is similar to RMLMap(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)per but is suited for large datasets. It requires some additional configurations for settings like intermediary file locations.

*   For download and instructions, see [SDM-RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/)izer (GitHub(URL_TO_INSERT_RECORD https://github.com/)(URL_TO_INSERT_RECORD https://github.com/))](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/SDM-TIB/SDM-RDFizer).

### Morph-KGC

Morph-KGC is a powerful engine to generate RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) and RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/)-star knowledge graphs. It supports a wide range of relational database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)s and data file format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s. It scales to large volumes of data and runs from the command line or as a python library (creating [RDFLib](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/RDFLib/rdflib) or [Oxigraph](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/oxigraph/oxigraph) graphs). It is also integrated in [kglab](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/DerwenAI/kglab), an abstraction layer for working with knowledge graphs using popular libraries.

* Download: [Morph-KGC](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/oeg-upm/morph-kgc).
* Documentation: [readthedocs](https://morph-kgc.readthedocs.io).

  
#### Other RML-based tools

There are other RML-based conversion tools that are more tailored to particular scenarios, for instance [RMLStreamer](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/RMLio/RMLStreamer) for streaming data. For an overview of feature completeness of tools, see the [RML Implementation Report](https://rml.io/implementation-report/).


#### SPARQL-Generate

[SPARQL-Generate](https://ci.mines-stetienne.fr/sparql-generate/) is a template-based language for generating RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) streams from a range of input format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s, such as tabular data, JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259), XML(URL_TO_INSERT_RECORD https://www.w3.org/TR/xml/), and relational database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)s. It extends SP(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/SP)ARQL(URL_TO_INSERT_RECORD http://www.w3.org/TR/sparql11-overview/) 1.1, which means it should feel fam(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#fam)iliar for everyone already fam(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#fam)iliar with SP(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/SP)ARQL(URL_TO_INSERT_RECORD http://www.w3.org/TR/sparql11-overview/) queries.

*   To quickly write and test queries (on small datasets), use the [SP(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/SP)ARQL(URL_TO_INSERT_RECORD http://www.w3.org/TR/sparql11-overview/)-Generate Playground](https://ci.mines-stetienne.fr/sparql-generate/playground.html) web-application.
*   The [SP(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/SP)ARQL(URL_TO_INSERT_RECORD http://www.w3.org/TR/sparql11-overview/)-Generate executable jar](https://ci.mines-stetienne.fr/sparql-generate/language-cli.html) is a CL(URL_TO_INSERT_RECORD https://github.com/obophenotype/cell-ontology)I (command line interface) tool for executing SP(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/SP)ARQL(URL_TO_INSERT_RECORD http://www.w3.org/TR/sparql11-overview/)-Generate queries. 


### Virtual graph

Tools that dynamically render a relational database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database) as virtual RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) graph.


#### Ontop

[Ontop](https://ontop-vkg.org/) is a virtual knowledge graph system for arbitrary database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)s. It has its own map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping language but also supports R2R(URL_TO_INSERT_RECORD https://www.rvdata.us/)ML. It runs as a command line tool, but there is also an Ontop plugin for Protégé to define map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)pings and import triples using a GUI application.

Although triples are exposed as a virtual graph, it is possible to export to RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) using a ‘materialize’ command.


### Proprietary tools

A proprietary tool is a commercial tool for which licenses need to be obtained


#### TopBraid Composer

[TopBraid Composer Maestro Edition](https://www.topquadrant.com/products/topbraid-composer/) (commercial license) is an Integrated development environment (IDE) for working with semantic web technologies, such as RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) and OWL(URL_TO_INSERT_RECORD http://www.w3.org/TR/owl-overview/). It has support for converting a range of format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s to RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/), including tabular/spreadsheet data, XML(URL_TO_INSERT_RECORD https://www.w3.org/TR/xml/), JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259), and RDB. It uses a straightforward conversion to RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/), which doesn’t allow for extensive customization: sheets and tabular data are directly map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ped(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) to a spreadsheet ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), XML(URL_TO_INSERT_RECORD https://www.w3.org/TR/xml/) directly according to an XML(URL_TO_INSERT_RECORD https://www.w3.org/TR/xml/) vocabulary, and relational database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)s are map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ped(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) using direct map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping with [D2RQ](http://d2rq.org/d2rq-language). 

The resulting RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) directly reflects the structure and schema of the database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database). However, once loaded as RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/), transformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ions and elaborate map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)pings can be applied using TopBraids visual scripting language [SPARQLMotion](https://www.topquadrant.com/technology/sparqlmotion/), or SP(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/SP)IN/Sparql construct queries.


#### Virtuoso Universal Serve

[Virtuoso Universal Server](http://virtuoso.openlinksw.com/) is a "universal server" that combines a database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database) engine, web server, triple/quat store, and more. It powers many nodes of the Linked Open Data cloud, for instance [dbpedia](https://www.dbpedia.org(URL_TO_INSERT_RECORD https://www.dbpedia.org/)/). 

The Virtuoso “Sponger” (RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/)izer) and it’s predefined “cartridges” (containing an Entity Extractor and an Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) Map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)per) are responsible for generating linked data from various forms of data (tabular and RDB). These cartridges are highly customizable, but it is also possible to write new ones. It is also possible to generate linked data views from relational database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)s using R2R(URL_TO_INSERT_RECORD https://www.rvdata.us/)ML. Linked data is generated on-the-fly but may be ingested into Virtuoso’s quad store.

There is also an open-source edition available, known as OpenLink Virtuoso.

*   [OpenLink Virtuoso (GitHub(URL_TO_INSERT_RECORD https://github.com/)(URL_TO_INSERT_RECORD https://github.com/))](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/openlink/virtuoso-opensource)


## Alternative approaches

### Coding yourself

Instead of relying on a tool, most programmers may prefer to write their own conversion code/scripts using their language of choice (e.g. Python, Java). This is probably the fastest, most accessible option because it capitalizes on existing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) programming skills and avoids the overhea(URL_TO_INSERT_RECORD http://www.rhea-db.org)d of learning another tool or map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping language. It offers great flexibility: it is highly customizable, any input and output format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) is possible, and it can be scaled to large datasets. Downside is that it may not be easy to adapt existing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) code to changing map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping requirements. Also, it may be difficult for others to understand the map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping. In addition, custom code may be susceptible to bugs, while established tools have been tested thoroughly.

Although it is possible to generate RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) by constructing triples using basic string(URL_TO_INSERT_RECORD https://string-db.org/) operations, it pays off to use a RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) library for these tasks.

For python there’s the [RDFLib](https://rdflib.dev/) package. Working in Jupyter notebook(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059)s with one of the common data manipulation libraries (e.g. pandas) allows you to interactively explore and manipulate the data before converting it into RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/).

For Java the two most common libraries for working with RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) are [Apache Jena](https://jena.apache.org/) and [Eclipse RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/)4J](https://rdf4j.org/).


## What to read next?

* [A data engineer's guide to semantic model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ling - Ilaria Maresi](https://doi.org/10.5281/zenodo.3898519) (Zenodo(URL_TO_INSERT_RECORD https://www.zenodo.org)(URL_TO_INSERT_RECORD https://www.zenodo.org))

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
