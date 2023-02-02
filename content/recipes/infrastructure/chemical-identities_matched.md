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

> To take an SDF (URL_TO_INSERT_RECORD_2381 https://fairsharing.org/FAIRsharing.ew26v7)  file, validate the content for chemical inconsistencies, and generate
> InChI (URL_TO_INSERT_RECORD_2383 https://fairsharing.org/FAIRsharing.ddk9t9) s, InChI (URL_TO_INSERT_RECORD_2384 https://fairsharing.org/FAIRsharing.ddk9t9) Keys, and SMILES (URL_TO_INSERT_RECORD_2382 https://fairsharing.org/FAIRsharing.qv4b3c)  for each entry in the SDF (URL_TO_INSERT_RECORD_2385 https://fairsharing.org/FAIRsharing.ew26v7)  file.

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
Check this git repository (URL_TO_INSERT_TERM_2386 https://fairsharing.org/search?recordType=repository)  for more detailed use instructions and where to find the tools:
[https://github.com (URL_TO_INSERT_RECORD_2387 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/fairplus-sdf](https://github.com (URL_TO_INSERT_RECORD_2388 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/fairplus-sdf)

### Record validation

When generating InChI (URL_TO_INSERT_RECORD_2389 https://fairsharing.org/FAIRsharing.ddk9t9) s, the InChI (URL_TO_INSERT_RECORD_2390 https://fairsharing.org/FAIRsharing.ddk9t9)  library (see {footcite}`Goodman2021InChI (URL_TO_INSERT_RECORD_2391 https://fairsharing.org/FAIRsharing.ddk9t9) `) may return several success states reflecting issues with
the compound record in the SDF (URL_TO_INSERT_RECORD_2392 https://fairsharing.org/FAIRsharing.ew26v7)  file, including: WARNING and ERROR. This first script reports such issues:

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

Similarly, InChI (URL_TO_INSERT_RECORD_2393 https://fairsharing.org/FAIRsharing.ddk9t9) Keys can be generated:

```bash
groovy inchikeys.groovy -f foo.sdf
```

When the success state is ERROR, nothing is outputted.

### Calculate SMILES strings

The last script calculates a SMILES (URL_TO_INSERT_RECORD_2394 https://fairsharing.org/FAIRsharing.qv4b3c)  for each entry in the SDF (URL_TO_INSERT_RECORD_2395 https://fairsharing.org/FAIRsharing.ew26v7)  file:

```bash
groovy smiles.groovy -f foo.sdf
```

## Conclusion

This recipe explained who to validate the chemical structures in an SDF (URL_TO_INSERT_RECORD_2396 https://fairsharing.org/FAIRsharing.ew26v7)  file,
and convert them to SMILES (URL_TO_INSERT_RECORD_2397 https://fairsharing.org/FAIRsharing.qv4b3c) , InChI (URL_TO_INSERT_RECORD_2398 https://fairsharing.org/FAIRsharing.ddk9t9) , and InChI (URL_TO_INSERT_RECORD_2399 https://fairsharing.org/FAIRsharing.ddk9t9) Key. The latter can then be used
with BridgeDb (URL_TO_INSERT_RECORD_2402 https://fairsharing.org/FAIRsharing.5ry74y)  and its metabolite ID map (URL_TO_INSERT_RECORD_2403 https://fairsharing.org/FAIRsharing.53edcc) ping database (URL_TO_INSERT_TERM_2400 https://fairsharing.org/search?fairsharingRegistry=Database) s to get additional identifier (URL_TO_INSERT_TERM_2401 https://fairsharing.org/search?recordType=identifier_schema) s.

### What to read next?

* [Identifier mapping with BridgeDb](https://w3id.org (URL_TO_INSERT_RECORD_2404 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB017)

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

