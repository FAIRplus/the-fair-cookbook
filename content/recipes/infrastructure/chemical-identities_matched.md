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

> To take an SDF (URL_TO_INSERT_RECORD_3303 https://fairsharing.org/FAIRsharing.ew26v7)  file, validate the content for chemical inconsistencies, and generate
> InChI (URL_TO_INSERT_RECORD_3305 https://fairsharing.org/FAIRsharing.ddk9t9) s, InChI (URL_TO_INSERT_RECORD_3306 https://fairsharing.org/FAIRsharing.ddk9t9) Keys, and SMILES (URL_TO_INSERT_RECORD_3304 https://fairsharing.org/FAIRsharing.qv4b3c)  for each entry in the SDF (URL_TO_INSERT_RECORD_3307 https://fairsharing.org/FAIRsharing.ew26v7)  file.

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
The Groovy scripts use version 2.7.1 of the [Chemistry (URL_TO_INSERT_RECORD_3308 https://fairsharing.org/3524)  (URL_TO_INSERT_RECORD_3309 https://fairsharing.org/3524)  Development Kit](https://cdk.github.io/)
(see {footcite}`Willighagen2017`). This library and its use in Groovy is further explain in
the book (URL_TO_INSERT_RECORD_3313 https://fairsharing.org/FAIRsharing.cbz72b)  [Groovy Cheminformat (URL_TO_INSERT_TERM_3310 https://fairsharing.org/search?recordType=model_and_format) ics with the Chemistry (URL_TO_INSERT_RECORD_3311 https://fairsharing.org/3524)  (URL_TO_INSERT_RECORD_3312 https://fairsharing.org/3524)  Development Kit](https://egonw.github.io/cdkbook/).
Check this git repository (URL_TO_INSERT_TERM_3314 https://fairsharing.org/search?recordType=repository)  for more detailed use instructions and where to find the tools:
[https://github.com (URL_TO_INSERT_RECORD_3315 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/fairplus-sdf](https://github.com (URL_TO_INSERT_RECORD_3316 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/fairplus-sdf)

### Record validation

When generating InChI (URL_TO_INSERT_RECORD_3317 https://fairsharing.org/FAIRsharing.ddk9t9) s, the InChI (URL_TO_INSERT_RECORD_3318 https://fairsharing.org/FAIRsharing.ddk9t9)  library (see {footcite}`Goodman2021InChI (URL_TO_INSERT_RECORD_3319 https://fairsharing.org/FAIRsharing.ddk9t9) `) may return several success states reflecting issues with
the compound record in the SDF (URL_TO_INSERT_RECORD_3323 https://fairsharing.org/FAIRsharing.ew26v7)  file, including: WARNING and ERRO (URL_TO_INSERT_RECORD_3321 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_3322 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_3324 https://fairsharing.org/FAIRsharing.cp0ybc) R (URL_TO_INSERT_RECORD_3320 https://fairsharing.org/FAIRsharing.1jKfji) . This first script reports such issues:

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

Similarly, InChI (URL_TO_INSERT_RECORD_3325 https://fairsharing.org/FAIRsharing.ddk9t9) Keys can be generated:

```bash
groovy inchikeys.groovy -f foo.sdf
```

When the success state is ERRO (URL_TO_INSERT_RECORD_3327 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_3328 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_3329 https://fairsharing.org/FAIRsharing.cp0ybc) R (URL_TO_INSERT_RECORD_3326 https://fairsharing.org/FAIRsharing.1jKfji) , nothing is outputted.

### Calculate SMILES strings

The last script calculates a SMILES (URL_TO_INSERT_RECORD_3330 https://fairsharing.org/FAIRsharing.qv4b3c)  for each entry in the SDF (URL_TO_INSERT_RECORD_3331 https://fairsharing.org/FAIRsharing.ew26v7)  file:

```bash
groovy smiles.groovy -f foo.sdf
```

## Conclusion

This recipe explained who to validate the chemical structures in an SDF (URL_TO_INSERT_RECORD_3332 https://fairsharing.org/FAIRsharing.ew26v7)  file,
and convert them to SMILES (URL_TO_INSERT_RECORD_3333 https://fairsharing.org/FAIRsharing.qv4b3c) , InChI (URL_TO_INSERT_RECORD_3334 https://fairsharing.org/FAIRsharing.ddk9t9) , and InChI (URL_TO_INSERT_RECORD_3335 https://fairsharing.org/FAIRsharing.ddk9t9) Key. The latter can then be used
with BridgeDb (URL_TO_INSERT_RECORD_3338 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_3339 https://fairsharing.org/FAIRsharing.5ry74y)  and its metabolite ID map (URL_TO_INSERT_RECORD_3340 https://fairsharing.org/FAIRsharing.53edcc) ping database (URL_TO_INSERT_TERM_3336 https://fairsharing.org/search?fairsharingRegistry=Database) s to get additional identifier (URL_TO_INSERT_TERM_3337 https://fairsharing.org/search?recordType=identifier_schema) s.

### What to read next?

* [Identifier (URL_TO_INSERT_TERM_3341 https://fairsharing.org/search?recordType=identifier_schema)  map (URL_TO_INSERT_RECORD_3345 https://fairsharing.org/FAIRsharing.53edcc) ping with BridgeDb (URL_TO_INSERT_RECORD_3343 https://fairsharing.org/FAIRsharing.5ry74y)  (URL_TO_INSERT_RECORD_3344 https://fairsharing.org/FAIRsharing.5ry74y) ](https://w3id.org (URL_TO_INSERT_RECORD_3342 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB017)

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

