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
OPSIN has [a website](https://opsin.ch.cam.ac.uk/) where IUPAC names are converted into other representations, including an InChIKey.

### Automating translations with Google Colab

[Google Colaboratory](https://colab.research.google.com/) (Colab for short) allows us to use Python to automate conversions of IUPAC names.
In Colab we can use [Bacting](https://github.com/egonw/bacting) {footcite}`Willighagen2021`
to access the OPSIN library. We would first download the Bacting libraries and create the Bacting manager objects:

```python
from scyjava import config, jimport
config.endpoints.append('io.github.egonw.bacting:managers-inchi:0.1.0')
config.endpoints.append('io.github.egonw.bacting:managers-opsin:0.1.0')

inchi_cls = jimport("net.bioclipse.managers.InChIManager")
inchi = inchi_cls(".")
opsin_cls = jimport("net.bioclipse.managers.OpsinManager")
opsin = opsin_cls(".")
```

After that, we use the manager API to parse the IUPAC name and generate an InChI and InChIKey:

```python
anInChI = inchi.generate(opsin.parseIUPACName("methane"))
print(f"InChI: {anInChI.getValue()}")
print(f"InchIKey: {anInChI.getKey()}")
```

The full Jupyter notebook can be found [here](https://gist.github.com/egonw/e4c788437a827407457deb764ce8eb93),
including a button to open the notebook in Colab.

### Automating translations with Apache Groovy



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

