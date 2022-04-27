(fcb-infra-iupac)=
# Generating InChIKeys for IUPAC names

+++
<br/>

````{panels_fairplus}
:identifier_text: FCBxxx
:identifier_link: 'https://w3id.org/faircookbook/FCBxxx'
:difficulty_level: 2
:recipe_type: hands_on
:reading_time_minutes: 15
:intended_audience: chemoinformatician, data_curator, data_manager, data_scientist  
:maturity_level: 2
:maturity_indicator: 1, 2
:has_executable_code: yeah
:recipe_name: Generating InChIKeys for IUPAC names
```` 

## Main Objectives

The main purpose of this recipe is:

> To take an IUPAC name and generate an InChIKey

---

### Using the OPSIN website

The OPSIN library is an open source tool to parse IUPAC names into chemical graphs {footcite}`Lowe2011Chemical`.

### Automating translations with Google Colab

Google Colab allows us to use Python to automate conversions of IUPAC names.
In Google Colab we can use [Bacting](https://github.com/egonw/bacting) {footcite}`Willighagen2021`
to access the OPSIN library.

Similarly, InChIKeys can be generated:

```bash
groovy inchikeys.groovy -f foo.sdf
```


## Conclusion


### What should I read next?
* [Identifier mapping with BridgeDb](https://w3id.org/faircookbook/FCB017)


## References

````{dropdown} **References**
```{footbibliography}
```
````

## Authors

````{authors_fairplus}
Egon: Writing - Original Draft
````


## License

````{license_fairplus}
CC-BY-4.0
````

