# Registering SwissLipids identifiers in Wikidata

 ````{panels_fairplus}
:identifier (URL_TO_INSERT_TERM_8476 https://fairsharing.org/search?recordType=identifier_schema) _text: FCBxxx
:identifier (URL_TO_INSERT_TERM_8477 https://fairsharing.org/search?recordType=identifier_schema) _link: 'https://w3id.org (URL_TO_INSERT_RECORD_8478 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCBxxx'
:difficulty_level: 5
:recipe_type: hands_on
:reading_time_minutes: 15
:intended_audience: bioinformat (URL_TO_INSERT_TERM_8479 https://fairsharing.org/search?recordType=model_and_format) ician, data_scientist, data_engineer
:maturity_level: 1
:maturity_indicator: 8
:has_executable_code: nope
:recipe_name: Registering SwissLipids (URL_TO_INSERT_RECORD_8483 https://fairsharing.org/FAIRsharing.pxr7x2)  (URL_TO_INSERT_RECORD_8484 https://fairsharing.org/FAIRsharing.pxr7x2)  identifier (URL_TO_INSERT_TERM_8480 https://fairsharing.org/search?recordType=identifier_schema) s in Wikidata (URL_TO_INSERT_RECORD_8481 https://fairsharing.org/FAIRsharing.6s749p)  (URL_TO_INSERT_RECORD_8482 https://fairsharing.org/FAIRsharing.6s749p) 
```` 

## Main Objectives

The objective of this recipe is to describe how external identifiers can be added to Wikidata in an automated way.

___


## Requirements

To record identifiers of some resource to make the content more findable and more interoperable, first a [Wikidata](https://www.wikidata.org/) property
needs to be requested. 
That process is described [here](https://www.wikidata.org/wiki/Wikidata:Property_proposal).

---


## Main Content

To make datasets more findable and databases more interoperable, it is recommended to share not just top-level metadata, but also record-level
metadata. 
For example, for chemical databases, one may share the chemical compound identifiers as open data, while keeping the data itself in their own database. 
That allows other resources, like Wikidata, to link to a private database.
First, that makes such data more findable, but it also makes the same data easier to integrate, and therefore more interoperable.

This recipe follows this idea and starts with a [CC0](https://creativecommons.org/publicdomain/zero/1.0/)-licensed mapping file, linking InChIKeys and database identifiers.
Recipe *InChI and SMILES identifiers for chemical structures* ([fcb:FCB007](https://w3id.org/faircookbook/FCB007)) explains how InChIKeys
can be generated for chemical compounds in your database.

As an example, this recipe demonstrates the approach of listing [SwissLipid](http://www.swisslipids.org/#/) {footcite}`Aimo2015SwissLipids`
identifiers in Wikidata, developed at the 2021 BioHackathon Europe. 
Earlier, a [Swiss Lipid property for Wikidata](https://www.wikidata.org/wiki/Wikidata:Property_proposal/SwissLipids_identifier)
was already proposed, later approved, and created in Wikidata [just before the 2020 BioHackathon Europe](https://www.wikidata.org/w/index.php?title=Property:P8691&oldid=1287579005).
An existing Wikidata property is a requirement to adding the external identifiers.

The recipe uses [Bacting](https://github.com/egonw/bacting) {footcite}`Willighagen2021`, which can be used in Groovy and Python. 

We will use the first here. 
The starting point is mappings (tuples) that link the SwissLipid identifiers to InChIKeys. 
The latter is used to find the matching Wikidata items.

### Step 1: getting the data

The SwissLipids data licensed under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/), but because Wikidata
is [CC0](https://creativecommons.org/publicdomain/zero/1.0/), additional permission was needed. Various
strategies can be used here, for example asking the provider:

* to make a subset with identifier mappings available under CC0 ([DrugBank](https://go.drugbank.com/releases/latest#open-data) uses this approach)
* permission to release the mappings to Wikidata (effectively making them CC0)

For SwissLipids an email exchange with the [SIB](https://www.sib.swiss/) gave me
permission to add the SwissLipids identifiers to Wikidata.

With the licensing issue resolved, the following practical steps were taken:

* Download `lipids.tsv` from the [Downloads](https://www.swisslipids.org/#/downloads) page
* Gunzip the file

### Step 2: extract Swiss Lipid ID <> InChIKey tuples

For this step, use `csvtool` (`apt get install csvtool`):

```shell
csvtool -t TAB col 1,11 swisslipids (URL_TO_INSERT_RECORD_8485 https://fairsharing.org/FAIRsharing.pxr7x2) .tsv
```

The output needs some further clean up, like removing lines without InChIKeys or "none" and "-" as value.
Also, the "InChIKey=" prefix is removed in preparation for the next step.
The full used code is:

```shell
csvtool -t TAB col 1,11 swisslipids (URL_TO_INSERT_RECORD_8487 https://fairsharing.org/FAIRsharing.pxr7x2) .tsv  | sed 's/InChI (URL_TO_INSERT_RECORD_8486 https://fairsharing.org/FAIRsharing.ddk9t9) Key=//' | grep -v "none" | grep -v ",-$" | grep -v ",$" | tee swisslipids (URL_TO_INSERT_RECORD_8488 https://fairsharing.org/FAIRsharing.pxr7x2) _ids.tsv
```

This results in almost 600k tuples:

```shell
$ wc -l swiss*tsv
   592412 swisslipids (URL_TO_INSERT_RECORD_8489 https://fairsharing.org/FAIRsharing.pxr7x2) _ids.tsv
   777957 swisslipids (URL_TO_INSERT_RECORD_8490 https://fairsharing.org/FAIRsharing.pxr7x2) .tsv
```

### Step 3: creating a ShEx model

Here the task is to create a *shape expression* for Wikidata, to model how
the identifiers will be added to Wikidata.
See the recipe publication by Waagmeester et al. about _A protocol for adding knowledge to Wikidata: aligning resources on human coronaviruses_
{footcite}`Waagmeester2021`.

### Step 4: creating QuickStatements

Now we have the mappings and the data model in Wikidata, we can create QuickStatements to allow us to enter the
data into Wikidata. 
This is not the only approach, and the process can be further automated using "Wikidata bots".
For this, see BioHackathon Europe [Project 32](https://github.com/elixir-europe/biohackathon-projects-2021/tree/main/projects/32):
Connecting ELIXIR-related open data on Wikidata via [WikiProject ELIXIR](https://www.wikidata.org/wiki/Wikidata:WikiProject_Elixir).

Based on existing Bacting scripts, a script is created to take the `swisslipids_ids.tsv` file as input and create
QuickStatements: [https://github.com/egonw/ons-wikidata/blob/master/ExtIdentifiers/swisslipids.groovy](https://github.com/egonw/ons-wikidata/blob/master/ExtIdentifiers/swisslipids.groovy) This script is using [Apache Groovy](http://www.groovy-lang.org/)
but Bacting can also be using in Python, see [https://github.com/cthoyt/pybacting](https://github.com/cthoyt/pybacting).

```{note}
This script uses a federated query against https://beta.sparql.swisslipids.org/sparql/ after a suggestion by Dr [Jerven Bolleman](https://orcid.org (URL_TO_INSERT_RECORD_8491 https://fairsharing.org/FAIRsharing.nx58jg) /0000-0002-7449-1266)
who indicated that the [RDF4J](https://rdf4j.org/) backing this SP (URL_TO_INSERT_RECORD_8495 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_8494 https://fairsharing.org/FAIRsharing.87ccfd)  endpoint will automatically batch the query against Wikidata (URL_TO_INSERT_RECORD_8492 https://fairsharing.org/FAIRsharing.6s749p)  (URL_TO_INSERT_RECORD_8493 https://fairsharing.org/FAIRsharing.6s749p) , overcoming
limitations of the Wikidata (URL_TO_INSERT_RECORD_8496 https://fairsharing.org/FAIRsharing.6s749p)  (URL_TO_INSERT_RECORD_8497 https://fairsharing.org/FAIRsharing.6s749p)  Query Service:
```

```sparql
PREFIX (URL_TO_INSERT_RECORD_8499 https://fairsharing.org/FAIRsharing.wwy1ns)  wdt: <http://www.wikidata.org (URL_TO_INSERT_RECORD_8498 https://fairsharing.org/FAIRsharing.6s749p) /prop/direct/>
SELECT ?wd ?key ?value WHERE {
  SERVICE <https://query.wikidata.org (URL_TO_INSERT_RECORD_8500 https://fairsharing.org/FAIRsharing.6s749p) /sparql> {
    SELECT (substr(str(?compound),32) as ?wd) ?key ?value WHERE {
      ?compound wdt:P235 ?key .
      OPTIONAL { ?compound wdt:P8691 ?value . }
    }
  }
}
```

This creates a file that looks like:

```shell
Q76738581       P8691   "SLM:000163948" S248    Q41165322       S854    "https://www.swisslipids.org/# (URL_TO_INSERT_RECORD_8501 https://fairsharing.org/FAIRsharing.pxr7x2) /downloads"       S813    +2021-11-06T00:00:00Z/11
Q76865359       P8691   "SLM:000163954" S248    Q41165322       S854    "https://www.swisslipids.org/# (URL_TO_INSERT_RECORD_8502 https://fairsharing.org/FAIRsharing.pxr7x2) /downloads"       S813    +2021-11-06T00:00:00Z/11
Q76865370       P8691   "SLM:000163964" S248    Q41165322       S854    "https://www.swisslipids.org/# (URL_TO_INSERT_RECORD_8503 https://fairsharing.org/FAIRsharing.pxr7x2) /downloads"       S813    +2021-11-06T00:00:00Z/11
Q76866423       P8691   "SLM:000163966" S248    Q41165322       S854    "https://www.swisslipids.org/# (URL_TO_INSERT_RECORD_8504 https://fairsharing.org/FAIRsharing.pxr7x2) /downloads"       S813    +2021-11-06T00:00:00Z/11
Q76865004       P8691   "SLM:000163968" S248    Q41165322       S854    "https://www.swisslipids.org/# (URL_TO_INSERT_RECORD_8505 https://fairsharing.org/FAIRsharing.pxr7x2) /downloads"       S813    +2021-11-06T00:00:00Z/11
Q76733356       P8691   "SLM:000164019" S248    Q41165322       S854    "https://www.swisslipids.org/# (URL_TO_INSERT_RECORD_8506 https://fairsharing.org/FAIRsharing.pxr7x2) /downloads"       S813    +2021-11-06T00:00:00Z/11
Q76733312       P8691   "SLM:000164023" S248    Q41165322       S854    "https://www.swisslipids.org/# (URL_TO_INSERT_RECORD_8507 https://fairsharing.org/FAIRsharing.pxr7x2) /downloads"       S813    +2021-11-06T00:00:00Z/11
Q76737210       P8691   "SLM:000164026" S248    Q41165322       S854    "https://www.swisslipids.org/# (URL_TO_INSERT_RECORD_8508 https://fairsharing.org/FAIRsharing.pxr7x2) /downloads"       S813    +2021-11-06T00:00:00Z/11
Q76736881       P8691   "SLM:000164032" S248    Q41165322       S854    "https://www.swisslipids.org/# (URL_TO_INSERT_RECORD_8509 https://fairsharing.org/FAIRsharing.pxr7x2) /downloads"       S813    +2021-11-06T00:00:00Z/11
Q76735022       P8691   "SLM:000164034" S248    Q41165322       S854    "https://www.swisslipids.org/# (URL_TO_INSERT_RECORD_8510 https://fairsharing.org/FAIRsharing.pxr7x2) /downloads"       S813    +2021-11-06T00:00:00Z/11
```

This resulted in about 17.5 thousand mappings. These are based on exact InChIKey match. 

### Step 5: running the QuickStatements

The resulting mappings are being added via the [QuickStatements website](https://quickstatements.toolforge.org/).

## Conclusion

The main conclusion is that we can automate adding external identifiers routinely to Wikidata using InChIKey matching. 

It will be clear [Bacting tool](https://bio.tools/bacting) can be replaced without too much effort by other tools making the same steps.

What this protocol does not do, however, is create Wikidata items for lipids in the SwissLipids database that
are not yet in Wikidata. 

This is the topic of a future recipe.

## References
````{dropdown} **Reference**
```{footbibliography}
```
````
---

## Authors

````{authors_fairplus}
Egon: Writing - Original Draft
Philippe:  Review & Editing
````

---

## License

````{license_fairplus}
CC-BY-4.0
````
