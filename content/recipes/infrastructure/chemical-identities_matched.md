(fcb-infra-chemid)=
# InChI and SMILES identifiers for chemical structures



````{panels_fairplus}
:identifier_text: FCB007
:identifier_link: 'https://w3id.org/faircookbook/FCB007'
:difficulty_level: 2
:recipe_type: hands_on
:reading_time_minutes: 15
:intended_audience: chemoinformatician, data_curator, data_manager, data_scientist  
:maturity_level: 4
:maturity_indicator: 49
:has_executable_code: nope
:recipe_name: Creating InChI & SMILES identifiers for chemical structures 
```` 

## Main Objectives

The main purpose of this recipe is:

> To take an SDF(URL_TO_INSERT_RECORD http://en.wikipedia.org/wiki/SD_format#SDF) file, validate the content for chemical inconsistencies, and generate
> InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/)s, InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/)Keys, and SMILES(URL_TO_INSERT_RECORD http://opensmiles.org/opensmiles.html) for each entry in the SDF(URL_TO_INSERT_RECORD http://en.wikipedia.org/wiki/SD_format#SDF) file.

---

```{tabbed} FAIRification Objectives, Inputs and Outputs
| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [validation](http://edamontology.org/operation_2428)  | [Structure Data File (SDF)](https://fairsharing.org/FAIRsharing.ew26v7)  | [report](http://edamontology.org/data_2048)  |
| [calculation](http://edamontology.org/operation_3438)  | [Structure Data File (SDF)](https://fairsharing.org/FAIRsharing.ew26v7) | [InChI](https://fairsharing.org/FAIRsharing.ddk9t9) |
| [calculation](http://edamontology.org/operation_3438)  | [Structure Data File (SDF)](https://fairsharing.org/FAIRsharing.ew26v7)  | [SMILES](https://fairsharing.org/FAIRsharing.qv4b3c)  |
```
```{tabbed} Requirements
* Skill dependency:
   * Bash experience
* Technical requirements:
   * Groovy
```

## Creating InChI and SMILES identifiers for chemical structures

To run the below scripts, you need a [Groovy](https://groovy.apache.org/download.html) installation.
The Groovy scripts use version 2.7.1 of the [Chemistry(URL_TO_INSERT_RECORD https://www.go-fair.org/implementation-networks/overview/chemistryin/)(URL_TO_INSERT_RECORD https://www.go-fair.org/implementation-networks/overview/chemistryin/) Development Kit](https://cdk.github.io/)
(see {footcite}`Willighagen2017`). This library and its use in Groovy is further explain in
the book(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059) [Groovy Cheminformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ics with the Chemistry(URL_TO_INSERT_RECORD https://www.go-fair.org/implementation-networks/overview/chemistryin/)(URL_TO_INSERT_RECORD https://www.go-fair.org/implementation-networks/overview/chemistryin/) Development Kit](https://egonw.github.io/cdkbook/).
Check this git repository (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository)  for more detailed use instructions and where to find the tools:
[https://github.com(URL_TO_INSERT_RECORD https://github.com/)/FAIRplus/fairplus-sdf](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/FAIRplus/fairplus-sdf)

### Record validation

When generating InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/)s, the InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/) library (see {footcite}`Goodman2021InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/)`) may return several success states reflecting issues with
the compound record in the SDF(URL_TO_INSERT_RECORD http://en.wikipedia.org/wiki/SD_format#SDF) file, including: WARNING and ERRO(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD https://w3id.org/ro/)R(URL_TO_INSERT_RECORD https://ror.org). This first script reports such issues:

```bash
groovy badRecords.groovy -f foo.sdf
```

The output may look like this:

```
Sulfinpyrazone  Omitted undefined stereo        WARNING
Isosorbide mononitrate  Charges were rearranged WARNING
Compound52      Proton(s) added/removed WARNING
```

### Calculate InChls

Similarly, InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/)Keys can be generated:

```bash
groovy inchikeys.groovy -f foo.sdf
```

When the success state is ERRO(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD https://w3id.org/ro/)R(URL_TO_INSERT_RECORD https://ror.org), nothing is outputted.

### Calculate SMILES strings

The last script calculates a SMILES(URL_TO_INSERT_RECORD http://opensmiles.org/opensmiles.html) for each entry in the SDF(URL_TO_INSERT_RECORD http://en.wikipedia.org/wiki/SD_format#SDF) file:

```bash
groovy smiles.groovy -f foo.sdf
```

## Conclusion

This recipe explained who to validate the chemical structures in an SDF(URL_TO_INSERT_RECORD http://en.wikipedia.org/wiki/SD_format#SDF) file,
and convert them to SMILES(URL_TO_INSERT_RECORD http://opensmiles.org/opensmiles.html), InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/), and InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/)Key. The latter can then be used
with BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io) and its metabolite ID map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database) s to get additional identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s.

### What to read next?

* [Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping with BridgeDb(URL_TO_INSERT_RECORD https://bridgedb.github.io)(URL_TO_INSERT_RECORD https://bridgedb.github.io)](https://w3id.org(URL_TO_INSERT_RECORD https://w3id.org/)/faircookbook/FCB017)

````{rdmkit_panel}
````


## References

````{dropdown} **References**
```{footbibliography}
```
````

## Authors

````{authors_fairplus}
Egon: Writing - Original Draft, Conceptualization
Philippe: Writing - Review & Editing
````


## License

````{license_fairplus}
CC-BY-4.0
````

