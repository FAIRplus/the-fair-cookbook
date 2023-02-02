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

> To take an SDF (URL_TO_INSERT_RECORD_2866 https://fairsharing.org/FAIRsharing.ew26v7)  file, validate the content for chemical inconsistencies, and generate
> InChI (URL_TO_INSERT_RECORD_2868 https://fairsharing.org/FAIRsharing.ddk9t9) s, InChI (URL_TO_INSERT_RECORD_2869 https://fairsharing.org/FAIRsharing.ddk9t9) Keys, and SMILES (URL_TO_INSERT_RECORD_2867 https://fairsharing.org/FAIRsharing.qv4b3c)  for each entry in the SDF (URL_TO_INSERT_RECORD_2870 https://fairsharing.org/FAIRsharing.ew26v7)  file.

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
The Groovy scripts use version 2.7.1 of the [Chemistry (URL_TO_INSERT_RECORD_2871 https://fairsharing.org/3524)  Development Kit](https://cdk.github.io/)
(see {footcite}`Willighagen2017`). This library and its use in Groovy is further explain in
the book [Groovy Cheminformat (URL_TO_INSERT_TERM_2872 https://fairsharing.org/search?recordType=model_and_format) ics with the Chemistry (URL_TO_INSERT_RECORD_2873 https://fairsharing.org/3524)  Development Kit](https://egonw.github.io/cdkbook/).
Check this git repository (URL_TO_INSERT_TERM_2874 https://fairsharing.org/search?recordType=repository)  for more detailed use instructions and where to find the tools:
[https://github.com (URL_TO_INSERT_RECORD_2875 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/fairplus-sdf](https://github.com (URL_TO_INSERT_RECORD_2876 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/fairplus-sdf)

### Record validation

When generating InChI (URL_TO_INSERT_RECORD_2877 https://fairsharing.org/FAIRsharing.ddk9t9) s, the InChI (URL_TO_INSERT_RECORD_2878 https://fairsharing.org/FAIRsharing.ddk9t9)  library (see {footcite}`Goodman2021InChI (URL_TO_INSERT_RECORD_2879 https://fairsharing.org/FAIRsharing.ddk9t9) `) may return several success states reflecting issues with
the compound record in the SDF (URL_TO_INSERT_RECORD_2883 https://fairsharing.org/FAIRsharing.ew26v7)  file, including: WARNING and ERRO (URL_TO_INSERT_RECORD_2881 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_2882 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_2884 https://fairsharing.org/FAIRsharing.cp0ybc) R (URL_TO_INSERT_RECORD_2880 https://fairsharing.org/FAIRsharing.1jKfji) . This first script reports such issues:

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

Similarly, InChI (URL_TO_INSERT_RECORD_2885 https://fairsharing.org/FAIRsharing.ddk9t9) Keys can be generated:

```bash
groovy inchikeys.groovy -f foo.sdf
```

When the success state is ERRO (URL_TO_INSERT_RECORD_2887 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_2888 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_2889 https://fairsharing.org/FAIRsharing.cp0ybc) R (URL_TO_INSERT_RECORD_2886 https://fairsharing.org/FAIRsharing.1jKfji) , nothing is outputted.

### Calculate SMILES strings

The last script calculates a SMILES (URL_TO_INSERT_RECORD_2890 https://fairsharing.org/FAIRsharing.qv4b3c)  for each entry in the SDF (URL_TO_INSERT_RECORD_2891 https://fairsharing.org/FAIRsharing.ew26v7)  file:

```bash
groovy smiles.groovy -f foo.sdf
```

## Conclusion

This recipe explained who to validate the chemical structures in an SDF (URL_TO_INSERT_RECORD_2892 https://fairsharing.org/FAIRsharing.ew26v7)  file,
and convert them to SMILES (URL_TO_INSERT_RECORD_2893 https://fairsharing.org/FAIRsharing.qv4b3c) , InChI (URL_TO_INSERT_RECORD_2894 https://fairsharing.org/FAIRsharing.ddk9t9) , and InChI (URL_TO_INSERT_RECORD_2895 https://fairsharing.org/FAIRsharing.ddk9t9) Key. The latter can then be used
with BridgeDb (URL_TO_INSERT_RECORD_2898 https://fairsharing.org/FAIRsharing.5ry74y)  and its metabolite ID map (URL_TO_INSERT_RECORD_2899 https://fairsharing.org/FAIRsharing.53edcc) ping database (URL_TO_INSERT_TERM_2896 https://fairsharing.org/search?fairsharingRegistry=Database) s to get additional identifier (URL_TO_INSERT_TERM_2897 https://fairsharing.org/search?recordType=identifier_schema) s.

### What to read next?

* [Identifier (URL_TO_INSERT_TERM_2900 https://fairsharing.org/search?recordType=identifier_schema)  map (URL_TO_INSERT_RECORD_2903 https://fairsharing.org/FAIRsharing.53edcc) ping with BridgeDb (URL_TO_INSERT_RECORD_2902 https://fairsharing.org/FAIRsharing.5ry74y) ](https://w3id.org (URL_TO_INSERT_RECORD_2901 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB017)

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

