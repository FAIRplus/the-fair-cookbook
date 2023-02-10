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

> To take an SDF (URL_TO_INSERT_RECORD-ABBREV_1661 https://fairsharing.org/FAIRsharing.ew26v7)  file, validate the content for chemical inconsistencies, and generate
> InChIs, InChIKeys, and SMILES (URL_TO_INSERT_RECORD-ABBREV_1662 https://fairsharing.org/FAIRsharing.qv4b3c)  for each entry in the SDF (URL_TO_INSERT_RECORD-ABBREV_1663 https://fairsharing.org/FAIRsharing.ew26v7)  file.

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
The Groovy scripts use version 2.7.1 of the [Chemistry Development Kit](https://cdk.github.io/)
(see {footcite}`Willighagen2017`). This library and its use in Groovy is further explain in
the book [Groovy Cheminformatics with the Chemistry Development Kit](https://egonw.github.io/cdkbook/).
Check this git repository (URL_TO_INSERT_TERM_1664 https://fairsharing.org/search?recordType=repository)  for more detailed use instructions and where to find the tools:
[https://github.com/FAIRplus/fairplus-sdf](https://github.com/FAIRplus/fairplus-sdf)

### Record validation

When generating InChIs, the InChI (URL_TO_INSERT_RECORD-ABBREV_1665 https://fairsharing.org/FAIRsharing.ddk9t9)  library (see {footcite}`Goodman2021InChI`) may return several success states reflecting issues with
the compound record in the SDF (URL_TO_INSERT_RECORD-ABBREV_1666 https://fairsharing.org/FAIRsharing.ew26v7)  file, including: WARNING and ERROR. This first script reports such issues:

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

Similarly, InChIKeys can be generated:

```bash
groovy inchikeys.groovy -f foo.sdf
```

When the success state is ERROR, nothing is outputted.

### Calculate SMILES strings

The last script calculates a SMILES (URL_TO_INSERT_RECORD-ABBREV_1667 https://fairsharing.org/FAIRsharing.qv4b3c)  for each entry in the SDF (URL_TO_INSERT_RECORD-ABBREV_1668 https://fairsharing.org/FAIRsharing.ew26v7)  file:

```bash
groovy smiles.groovy -f foo.sdf
```

## Conclusion

This recipe explained who to validate the chemical structures in an SDF (URL_TO_INSERT_RECORD-ABBREV_1669 https://fairsharing.org/FAIRsharing.ew26v7)  file,
and convert them to SMILES (URL_TO_INSERT_RECORD-ABBREV_1670 https://fairsharing.org/FAIRsharing.qv4b3c) , InChI (URL_TO_INSERT_RECORD-ABBREV_1671 https://fairsharing.org/FAIRsharing.ddk9t9) , and InChIKey. The latter can then be used
with BridgeDb (URL_TO_INSERT_RECORD-NAME_1674 https://fairsharing.org/FAIRsharing.5ry74y)  and its metabolite ID mapping database (URL_TO_INSERT_TERM_1672 https://fairsharing.org/search?fairsharingRegistry=Database) s to get additional identifier (URL_TO_INSERT_TERM_1673 https://fairsharing.org/search?recordType=identifier_schema) s.

### What to read next?

* [Identifier mapping with BridgeDb](https://w3id.org/faircookbook/FCB017)

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

