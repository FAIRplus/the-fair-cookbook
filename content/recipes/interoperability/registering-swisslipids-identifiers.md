# Registering SwissLipids identifiers in Wikidata

 ````{panels_fairplus}
:identifier_text: FCBxxx
:identifier_link: 'https://w3id.org/faircookbook/FCBxxx'
:difficulty_level: 2
:recipe_type: hands_on
:reading_time_minutes: 15
:intended_audience: bioinformatician, data_scientist, data_engineer
:has_executable_code: nope
:recipe_name: Registering SwissLipids identifiers in Wikidata
```` 

## Main Objectives

___


## Requirements


---


## Main Content

Previously, we already proposed a [Swiss Lipid property for Wikidata](https://www.wikidata.org/wiki/Wikidata:Property_proposal/SwissLipids_identifier)
which was approved and created in [just before the 2020 BioHackathon Europe](https://www.wikidata.org/w/index.php?title=Property:P8691&oldid=1287579005).
But populating Wikidata with identifiers got stuck.

The intention for this BioHackathon is the add them, using SwissLipid ID <> InChIKey tuples and [Bacting](https://github.com/egonw/bacting) code
(doi:[10.21105/joss.02558](https://doi.org/10.21105/joss.02558)). This page will describe the process.

### Step 1: getting the data

The data is CC-BY but it was agreed that adding the SwissLipid identifiers to Wikidata (CCZero) is okay.

* Download `lipids.tsv` from the [Downloads](https://www.swisslipids.org/#/downloads) page
* Gunzip the file

### Step 2: extract Swiss Lipid ID <> InChIKey tuples

For this step I use `csvtool` (`apt get install csvtool`):

```shell
csvtool -t TAB col 1,11 swisslipids.tsv
```

The output needs some further clean up, like removing lines without InChIKeys or "none" and "-" as value. Also,
the "InChIKey=" prefix is removed in preparation for the next step. The full used code is:

```shell
csvtool -t TAB col 1,11 swisslipids.tsv  | sed 's/InChIKey=//' | grep -v "none" | grep -v ",-$" | grep -v ",$" | tee swisslipids_ids.tsv
```

This results in almost 600k tuples:

```shell
$ wc -l swiss*tsv
   592412 swisslipids_ids.tsv
   777957 swisslipids.tsv
```

### Step 3: creating a ShEx model

Skipping this step for later this week, but here the task is to create a shape expression for Wikidata, to model how
the identifiers will be added to Wikidata. See _A protocol for adding knowledge to Wikidata: aligning resources on human coronaviruses_
(doi:[10.1186/s12915-020-00940-y](https://doi.org/10.1186/s12915-020-00940-y)).

### Step 4: creating QuickStatements

Now we have the mappings and the data model in Wikidata, we can create QuickStatements to allow us to enter the
data into Wikidata. This is not the only approach, and the process can be further automated using "Wikidata bots".
For this, see [Project 32](https://github.com/elixir-europe/biohackathon-projects-2021/tree/main/projects/32):
Connecting ELIXIR-related open data on Wikidata via WikiProject ELIXIR.

Based on existing Bacting scripts, a script is created to take the `swisslipids_ids.tsv` file as input and create
QuickStatements: [https://github.com/egonw/ons-wikidata/blob/master/ExtIdentifiers/swisslipids.groovy](https://github.com/egonw/ons-wikidata/blob/master/ExtIdentifiers/swisslipids.groovy) This script is using [Apache Groovy](http://www.groovy-lang.org/)
but Bacting can also be using in Python, see [https://github.com/cthoyt/pybacting](https://github.com/cthoyt/pybacting).

This script uses a federated query against https://beta.sparql.swisslipids.org/sparql/ after a suggestion by Jerven
who indicated that the RDF4J backing this SPARQL endpoint will automatically batch the query against Wikidata, overcoming
limitations of the Wikidata Query Service:

```sparql
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
SELECT ?wd ?key ?value WHERE {
  SERVICE <https://query.wikidata.org/sparql> {
    SELECT (substr(str(?compound),32) as ?wd) ?key ?value WHERE {
      ?compound wdt:P235 ?key .
      OPTIONAL { ?compound wdt:P8691 ?value . }
    }
  }
}
```

This creates a file that looks like:

```shell
Q76738581       P8691   "SLM:000163948" S248    Q41165322       S854    "https://www.swisslipids.org/#/downloads"       S813    +2021-11-06T00:00:00Z/11
Q76865359       P8691   "SLM:000163954" S248    Q41165322       S854    "https://www.swisslipids.org/#/downloads"       S813    +2021-11-06T00:00:00Z/11
Q76865370       P8691   "SLM:000163964" S248    Q41165322       S854    "https://www.swisslipids.org/#/downloads"       S813    +2021-11-06T00:00:00Z/11
Q76866423       P8691   "SLM:000163966" S248    Q41165322       S854    "https://www.swisslipids.org/#/downloads"       S813    +2021-11-06T00:00:00Z/11
Q76865004       P8691   "SLM:000163968" S248    Q41165322       S854    "https://www.swisslipids.org/#/downloads"       S813    +2021-11-06T00:00:00Z/11
Q76733356       P8691   "SLM:000164019" S248    Q41165322       S854    "https://www.swisslipids.org/#/downloads"       S813    +2021-11-06T00:00:00Z/11
Q76733312       P8691   "SLM:000164023" S248    Q41165322       S854    "https://www.swisslipids.org/#/downloads"       S813    +2021-11-06T00:00:00Z/11
Q76737210       P8691   "SLM:000164026" S248    Q41165322       S854    "https://www.swisslipids.org/#/downloads"       S813    +2021-11-06T00:00:00Z/11
Q76736881       P8691   "SLM:000164032" S248    Q41165322       S854    "https://www.swisslipids.org/#/downloads"       S813    +2021-11-06T00:00:00Z/11
Q76735022       P8691   "SLM:000164034" S248    Q41165322       S854    "https://www.swisslipids.org/#/downloads"       S813    +2021-11-06T00:00:00Z/11
```

This resulted in about 17.5 thousand mappings. These are based on exact InChIKey match. 

### Step 5: running the QuickStatements

The resulting mappings are being added via the [QuickStatements website](https://quickstatements.toolforge.org/).



## References


---

## Authors

````{authors_fairplus}
Egon: Writing - Original Draft
````


---

## License

````{license_fairplus}
CC-BY-4.0
````
