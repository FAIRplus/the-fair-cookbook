(fcb-infra-chemid)=
# InChI and SMILES identifiers for chemical structures



````{panels_fairplus}
```` 

## Main Objectives

The main purpose of this recipe is:

> To take an SDF(URL_TO_INSERT_RECORD http://en.wikipedia.org/wiki/SD_format#SDF) file, validate the content for chemical inconsistencies, and generate
> InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/)s, InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/)Keys, and SMILES(URL_TO_INSERT_RECORD http://opensmiles.org/opensmiles.html) for each entry in the SDF(URL_TO_INSERT_RECORD http://en.wikipedia.org/wiki/SD_format#SDF) file.

---

```{tabbed} FAIRification Objectives, Inputs and Outputs
```
```{tabbed} Requirements
```

## Creating InChI and SMILES identifiers for chemical structures

To run the below scripts, you need a [Groovy](https://groovy.apache.org/download.html) installation.
The Groovy scripts use version 2.7.1 of the [Chemistry(URL_TO_INSERT_RECORD https://www.go-fair.org/implementation-networks/overview/chemistryin/)(URL_TO_INSERT_RECORD https://www.go-fair.org/implementation-networks/overview/chemistryin/) Development Kit](https://cdk.github.io/)
(see {footcite}`Willighagen2017`). This library and its use in Groovy is further explain in
the book(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059) [Groovy Cheminformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ics with the Chemistry(URL_TO_INSERT_RECORD https://www.go-fair.org/implementation-networks/overview/chemistryin/)(URL_TO_INSERT_RECORD https://www.go-fair.org/implementation-networks/overview/chemistryin/) Development Kit](https://egonw.github.io/cdkbook/).
Check this git repository (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository) for more detailed use instructions and where to find the tools:
[https://github.com(URL_TO_INSERT_RECORD https://github.com/)/FAIRplus/fairplus-sdf](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/FAIRplus/fairplus-sdf)

### Record validation

When generating InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/)s, the InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/) library (see {footcite}`Goodman2021InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/)`) may return several success states reflecting issues with
the compound record in the SDF(URL_TO_INSERT_RECORD http://en.wikipedia.org/wiki/SD_format#SDF) file, including: WARNING and ERRO(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD https://w3id.org/ro/)R(URL_TO_INSERT_RECORD https://ror.org). This first script reports such issues:

```bash
```

The output may look like this:

```
```

### Calculate InChls

Similarly, InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/)Keys can be generated:

```bash
```

When the success state is ERRO(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD https://w3id.org/ro/)R(URL_TO_INSERT_RECORD https://ror.org), nothing is outputted.

### Calculate SMILES strings

The last script calculates a SMILES(URL_TO_INSERT_RECORD http://opensmiles.org/opensmiles.html) for each entry in the SDF(URL_TO_INSERT_RECORD http://en.wikipedia.org/wiki/SD_format#SDF) file:

```bash
```

## Conclusion

This recipe explained who to validate the chemical structures in an SDF(URL_TO_INSERT_RECORD http://en.wikipedia.org/wiki/SD_format#SDF) file,
and convert them to SMILES(URL_TO_INSERT_RECORD http://opensmiles.org/opensmiles.html), InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/), and InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/)Key. The latter can then be used
with BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io) and its metabolite ID map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)s to get additional identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s.

### What to read next?

* [Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping with BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io)](https://w3id.org(URL_TO_INSERT_RECORD https://w3id.org/)/faircookbook/FCB017)

````{rdmkit_panel}
````


## References

````{dropdown} **References**
```{footbibliography}
```
````

## Authors

````{authors_fairplus}
````


## License

````{license_fairplus}
````

