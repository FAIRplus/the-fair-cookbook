(fcb-infra-iupac)=
# Creating InChIKeys for IUPAC names



````{panels_fairplus}
```` 

## Main Objectives

The main purpose of this recipe is:

> To take an IUPAC(URL_TO_INSERT_RECORD https://ac.tdwg.org/introduction/) name and generate an InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/)Key

---

### Using the OPSIN website

The OPSIN library is an open source tool to parse IUPAC(URL_TO_INSERT_RECORD https://ac.tdwg.org/introduction/) names into chemical graphs {footcite}`Lowe2011Chemical`.
OPSIN has [a website](https://opsin.ch.cam.ac.uk/) where IUPAC(URL_TO_INSERT_RECORD https://ac.tdwg.org/introduction/) names are converted into other representations, including an InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/)Key.
The latter is done by the offical InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/) library {footcite}`Goodman2021InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/)`.

### Automating translations with Google Colab

[Google Colaboratory](https://colab.research.google.com/) (Colab for short) allows us to use Python to automate conversions of IUPAC(URL_TO_INSERT_RECORD https://ac.tdwg.org/introduction/) names.
In Colab we can use [Bacting](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/egonw/bacting) {footcite}`Willighagen2021`
to access the OPSIN library. We would first download the Bacting libraries and create the Bacting manager objects:

```python

```

After that, we use the manager API to parse the IUPAC(URL_TO_INSERT_RECORD https://ac.tdwg.org/introduction/) name and generate an InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/) and InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/)Key:

```python
```

The full Jupyter notebook(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059) can be found [here](https://gist.github.com(URL_TO_INSERT_RECORD https://github.com/)/egonw/e4c788437a827407457deb764ce8eb93),
including a button to open the notebook(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059) in Colab.

### Automating translations with Apache Groovy

Because Bacting is written in Java and the libraries being available from
[Maven Central](https://search.maven.org/), it also be used in
[Apache Groovy](http://www.groovy-lang.org/) and other Java-based environments.
The above code in Groovy looks like:

```groovy


```

## Conclusion

Cheminformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ics provides us the tools to parse IUPAC(URL_TO_INSERT_RECORD https://ac.tdwg.org/introduction/) names and convert them to
chemical graph based identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s, such as the InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/)Key. The InChI(URL_TO_INSERT_RECORD https://www.inchi-trust.org/)Key identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)
can be used to find more informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion about the chemicals represented by the
original IUPAC(URL_TO_INSERT_RECORD https://ac.tdwg.org/introduction/) names.

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

