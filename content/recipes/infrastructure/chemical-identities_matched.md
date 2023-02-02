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

> To take an SDF (URL_TO_INSERT_RECORD_2492 https://fairsharing.org/FAIRsharing.ew26v7)  file, validate the content for chemical inconsistencies, and generate
> InChI (URL_TO_INSERT_RECORD_2494 https://fairsharing.org/FAIRsharing.ddk9t9) s, InChI (URL_TO_INSERT_RECORD_2495 https://fairsharing.org/FAIRsharing.ddk9t9) Keys, and SMILES (URL_TO_INSERT_RECORD_2493 https://fairsharing.org/FAIRsharing.qv4b3c)  for each entry in the SDF (URL_TO_INSERT_RECORD_2496 https://fairsharing.org/FAIRsharing.ew26v7)  file.

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
The Groovy scripts use version 2.7.1 of the [Chemistry (URL_TO_INSERT_RECORD_2497 https://fairsharing.org/3524)  Development Kit](https://cdk.github.io/)
(see {footcite}`Willighagen2017`). This library and its use in Groovy is further explain in
the book [Groovy Cheminformat (URL_TO_INSERT_TERM_2498 https://fairsharing.org/search?recordType=model_and_format) ics with the Chemistry (URL_TO_INSERT_RECORD_2499 https://fairsharing.org/3524)  Development Kit](https://egonw.github.io/cdkbook/).
Check this git repository (URL_TO_INSERT_TERM_2500 https://fairsharing.org/search?recordType=repository)  for more detailed use instructions and where to find the tools:
[https://github.com (URL_TO_INSERT_RECORD_2501 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/fairplus-sdf](https://github.com (URL_TO_INSERT_RECORD_2502 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/fairplus-sdf)

### Record validation

When generating InChI (URL_TO_INSERT_RECORD_2503 https://fairsharing.org/FAIRsharing.ddk9t9) s, the InChI (URL_TO_INSERT_RECORD_2504 https://fairsharing.org/FAIRsharing.ddk9t9)  library (see {footcite}`Goodman2021InChI (URL_TO_INSERT_RECORD_2505 https://fairsharing.org/FAIRsharing.ddk9t9) `) may return several success states reflecting issues with
the compound record in the SDF (URL_TO_INSERT_RECORD_2506 https://fairsharing.org/FAIRsharing.ew26v7)  file, including: WARNING and ERROR. This first script reports such issues:

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

Similarly, InChI (URL_TO_INSERT_RECORD_2507 https://fairsharing.org/FAIRsharing.ddk9t9) Keys can be generated:

```bash
groovy inchikeys.groovy -f foo.sdf
```

When the success state is ERROR, nothing is outputted.

### Calculate SMILES strings

The last script calculates a SMILES (URL_TO_INSERT_RECORD_2508 https://fairsharing.org/FAIRsharing.qv4b3c)  for each entry in the SDF (URL_TO_INSERT_RECORD_2509 https://fairsharing.org/FAIRsharing.ew26v7)  file:

```bash
groovy smiles.groovy -f foo.sdf
```

## Conclusion

This recipe explained who to validate the chemical structures in an SDF (URL_TO_INSERT_RECORD_2510 https://fairsharing.org/FAIRsharing.ew26v7)  file,
and convert them to SMILES (URL_TO_INSERT_RECORD_2511 https://fairsharing.org/FAIRsharing.qv4b3c) , InChI (URL_TO_INSERT_RECORD_2512 https://fairsharing.org/FAIRsharing.ddk9t9) , and InChI (URL_TO_INSERT_RECORD_2513 https://fairsharing.org/FAIRsharing.ddk9t9) Key. The latter can then be used
with BridgeDb (URL_TO_INSERT_RECORD_2516 https://fairsharing.org/FAIRsharing.5ry74y)  and its metabolite ID map (URL_TO_INSERT_RECORD_2517 https://fairsharing.org/FAIRsharing.53edcc) ping database (URL_TO_INSERT_TERM_2514 https://fairsharing.org/search?fairsharingRegistry=Database) s to get additional identifier (URL_TO_INSERT_TERM_2515 https://fairsharing.org/search?recordType=identifier_schema) s.

### What to read next?

* [Identifier (URL_TO_INSERT_TERM_2518 https://fairsharing.org/search?recordType=identifier_schema)  map (URL_TO_INSERT_RECORD_2521 https://fairsharing.org/FAIRsharing.53edcc) ping with BridgeDb (URL_TO_INSERT_RECORD_2520 https://fairsharing.org/FAIRsharing.5ry74y) ](https://w3id.org (URL_TO_INSERT_RECORD_2519 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB017)

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

