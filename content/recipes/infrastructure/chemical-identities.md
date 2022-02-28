(fcb-infra-chemid)=
# InChI and SMILES identifiers for chemical structures

+++
<br/>

````{panels_fairplus}
:identifier_text: FCB007
:identifier_link: 'https://w3id.org/faircookbook/FCB007'
:difficulty_level: 2
:recipe_type: hands_on
:reading_time_minutes: 15
:intended_audience: chemoinformatician, data_curator, data_manager, data_scientist  
:has_executable_code: yeah
:recipe_name: InChI and SMILES identifiers for chemical structures
```` 

## Main Objectives

The main purpose of this recipe is:

> To take an SDF file, validate the content for chemical inconsistencies, and generate
> InChIs, InChIKeys, and SMILES for each entry in the SDF file.

---


## Requirements

* Skill depedency:
   * Bash experience
* Technical requirements:
   * Groovy

---


## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [validation](http://edamontology.org/operation_2428)  | [Structure Data File (SDF)](https://fairsharing.org/FAIRsharing.ew26v7)  | [report](http://edamontology.org/data_2048)  |
| [calculation](http://edamontology.org/operation_3438)  | [Structure Data File (SDF)](https://fairsharing.org/FAIRsharing.ew26v7) | [InChI](https://fairsharing.org/FAIRsharing.ddk9t9) |
| [calculation](http://edamontology.org/operation_3438)  | [Structure Data File (SDF)](https://fairsharing.org/FAIRsharing.ew26v7)  | [SMILES](https://fairsharing.org/FAIRsharing.qv4b3c)  |

---


## Creating InChI and SMILES identifiers for chemical structures

To run the below scripts, you need a [Groovy](https://groovy.apache.org/download.html) installation.
The Groovy scripts use version 2.7.1 of the [Chemistry Development Kit](https://cdk.github.io/)
(see {footcite}`Willighagen2017`). This library and its use in Groovy is further explain in
the book [Groovy Cheminformatics with the Chemistry Development Kit](https://egonw.github.io/cdkbook/).
Check this git repository for more detailed use instructions and where to find the tools:
[https://github.com/FAIRplus/fairplus-sdf](https://github.com/FAIRplus/fairplus-sdf)

### Record validation

When generating InChIs, the InChI library (see {footcite}`Goodman2021InChI`) may return several success states reflecting issues with
the compound record in the SDF file, including: WARNING and ERROR. This first script reports such issues:

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

The last script calculates a SMILES for each entry in the SDF file:

```bash
groovy smiles.groovy -f foo.sdf
```

## Conclusion

This recipe explained who to validate the chemical structures in an SDF file,
and convert them to SMILES, InChI, and InChIKey. The latter can then be used
with BridgeDb and its metabolite ID mapping databases to get additional identifiers.

### What should I read next?
* [Identifier mapping with BridgeDb](https://w3id.org/faircookbook/FCB017)

---

## References

```{footbibliography}
```

---

## Authors

````{authors_fairplus}
Egon: Writing - Original Draft, Conceptualization
Philippe: Writing - Review & Editing
````

---

## License

````{license_fairplus}
CC-BY-4.0
````

