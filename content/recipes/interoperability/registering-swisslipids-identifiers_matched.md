# Registering SwissLipids identifiers in Wikidata

 ````{panels_fairplus}
:identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)_text: FCBxxx
:identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)_link: 'https://w3id.org(URL_TO_INSERT_RECORD https://w3id.org/)/faircookbook/FCBxxx'
:difficulty_level: 5
:recipe_type: hands_on
:reading_time_minutes: 15
:intended_audience: bioinformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ician, data_scientist, data_engineer
:maturity_level: 1
:maturity_indicator: 8
:has_executable_code: nope
:recipe_name: Registering SwissLipids(URL_TO_INSERT_RECORD http://www.swisslipids.org/#/)(URL_TO_INSERT_RECORD http://www.swisslipids.org/#/) identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s in Wikidata(URL_TO_INSERT_RECORD http://wikidata.org/)(URL_TO_INSERT_RECORD http://wikidata.org/)
```` 

## Main Objectives




## Requirements




## Main Content






### Step 1: getting the data






### Step 2: extract Swiss Lipid ID <> InChIKey tuples


```shell
csvtool -t TAB col 1,11 swisslipids(URL_TO_INSERT_RECORD http://www.swisslipids.org/#/).tsv
```


```shell
csvtool -t TAB col 1,11 swisslipids(URL_TO_INSERT_RECORD http://www.swisslipids.org/#/).tsv  | sed 's/InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/)Key=//' | grep -v "none" | grep -v ",-$" | grep -v ",$" | tee swisslipids(URL_TO_INSERT_RECORD http://www.swisslipids.org/#/)_ids.tsv
```


```shell
$ wc -l swiss*tsv
   592412 swisslipids(URL_TO_INSERT_RECORD http://www.swisslipids.org/#/)_ids.tsv
   777957 swisslipids(URL_TO_INSERT_RECORD http://www.swisslipids.org/#/).tsv
```

### Step 3: creating a ShEx model


### Step 4: creating QuickStatements



```{note}
This script uses a federated query against https://beta.sparql.swisslipids.org/sparql/ after a suggestion by Dr [Jerven Bolleman](https://orcid.org(URL_TO_INSERT_RECORD http://orcid.org/)/0000-0002-7449-1266)
who indicated that the [RDF4J](https://rdf4j.org/) backing this SP(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/SP)ARQL(URL_TO_INSERT_RECORD http://www.w3.org/TR/sparql11-overview/) endpoint will automatically batch the query against Wikidata(URL_TO_INSERT_RECORD http://wikidata.org/)(URL_TO_INSERT_RECORD http://wikidata.org/), overcoming
limitations of the Wikidata(URL_TO_INSERT_RECORD http://wikidata.org/)(URL_TO_INSERT_RECORD http://wikidata.org/) Query Service:
```

```sparql
PREFIX(URL_TO_INSERT_RECORD http://purl.bioontology.org/ontology/FIX) wdt: <http://www.wikidata.org(URL_TO_INSERT_RECORD http://wikidata.org/)/prop/direct/>
SELECT ?wd ?key ?value WHERE {
  SERVICE <https://query.wikidata.org(URL_TO_INSERT_RECORD http://wikidata.org/)/sparql> {
    SELECT (substr(str(?compound),32) as ?wd) ?key ?value WHERE {
      ?compound wdt:P235 ?key .
      OPTIONAL { ?compound wdt:P8691 ?value . }
    }
  }
}
```


```shell
Q76738581       P8691   "SLM:000163948" S248    Q41165322       S854    "https://www.swisslipids.org/#(URL_TO_INSERT_RECORD http://www.swisslipids.org/#/)/downloads"       S813    +2021-11-06T00:00:00Z/11
Q76865359       P8691   "SLM:000163954" S248    Q41165322       S854    "https://www.swisslipids.org/#(URL_TO_INSERT_RECORD http://www.swisslipids.org/#/)/downloads"       S813    +2021-11-06T00:00:00Z/11
Q76865370       P8691   "SLM:000163964" S248    Q41165322       S854    "https://www.swisslipids.org/#(URL_TO_INSERT_RECORD http://www.swisslipids.org/#/)/downloads"       S813    +2021-11-06T00:00:00Z/11
Q76866423       P8691   "SLM:000163966" S248    Q41165322       S854    "https://www.swisslipids.org/#(URL_TO_INSERT_RECORD http://www.swisslipids.org/#/)/downloads"       S813    +2021-11-06T00:00:00Z/11
Q76865004       P8691   "SLM:000163968" S248    Q41165322       S854    "https://www.swisslipids.org/#(URL_TO_INSERT_RECORD http://www.swisslipids.org/#/)/downloads"       S813    +2021-11-06T00:00:00Z/11
Q76733356       P8691   "SLM:000164019" S248    Q41165322       S854    "https://www.swisslipids.org/#(URL_TO_INSERT_RECORD http://www.swisslipids.org/#/)/downloads"       S813    +2021-11-06T00:00:00Z/11
Q76733312       P8691   "SLM:000164023" S248    Q41165322       S854    "https://www.swisslipids.org/#(URL_TO_INSERT_RECORD http://www.swisslipids.org/#/)/downloads"       S813    +2021-11-06T00:00:00Z/11
Q76737210       P8691   "SLM:000164026" S248    Q41165322       S854    "https://www.swisslipids.org/#(URL_TO_INSERT_RECORD http://www.swisslipids.org/#/)/downloads"       S813    +2021-11-06T00:00:00Z/11
Q76736881       P8691   "SLM:000164032" S248    Q41165322       S854    "https://www.swisslipids.org/#(URL_TO_INSERT_RECORD http://www.swisslipids.org/#/)/downloads"       S813    +2021-11-06T00:00:00Z/11
Q76735022       P8691   "SLM:000164034" S248    Q41165322       S854    "https://www.swisslipids.org/#(URL_TO_INSERT_RECORD http://www.swisslipids.org/#/)/downloads"       S813    +2021-11-06T00:00:00Z/11
```


### Step 5: running the QuickStatements


## Conclusion





## References
````{dropdown} **Reference**
```{footbibliography}
```
````

## Authors

````{authors_fairplus}
Egon: Writing - Original Draft
Philippe:  Review & Editing
````


## License

````{license_fairplus}
CC-BY-4.0
````
