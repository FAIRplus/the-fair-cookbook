# Registering Datasets

 ````{panels_fairplus}
:identifier_text: FCBxxx
:identifier_link: 'https://w3id.org/faircookbook/FCBxxx'
:difficulty_level: 2
:recipe_type: hands_on
:reading_time_minutes: 15
:intended_audience: bioinformatician, data_scientist, data_engineer
:has_executable_code: nope
:recipe_name: How to Register a Dataset with Wikidata
```` 

"UCnn.x Registering a dataset in Wikidata."


## Main Objectives

Useful datasets become more useful when they are easily found. The **FAIR principles** state that: 

> F1. (Meta)data are assigned a globally unique and persistent identifier
> 
> A1. (Meta)data are retrievable by their identifier using a standardised communications protocol 

This recipe is about making the dataset metadata more FAIR:

> Learn how to register a published dataset on Wikidata with the appropriate citation to increase its findability.

___


## Requirements

To register datasets to [Wikidata](https://www.wikidata.org/) requires a Wikidata account ([create one](https://www.wikidata.org/wiki/Special:CreateAccount)).

---


## Main Content

This recipes takes an interest in datasets with information about small chemical compounds, particularly datasets with an SDF file or spreadsheet with SMILES.
But the registration itself in Wikidata to make it more findable works for any dataset. The registration in Wikidata makes the metadata more findable by
itself {footcite}`Waagmeester2020`. This [Wikidata:Introduction](https://www.wikidata.org/wiki/Wikidata:Introduction) describes the principle ideas and data model that will make this
recipe easier to follow.

Importantly, Wikidata allows the dataset to be used as reference in Wikidata to support statements. For example, if the dataset contains a logP value,
then this logP value can be associated to the compound in Wikidata with a statement, with the dataset itself as reference.
<!-- TODO: add screenshot of example -->

### Finding Datasets

There are several ways to locate datasets to be registered into Wikidata. One consideration is that the dataset has the recommended license and an identifier.

Example of where open datasets with information about chemical compounds can be found include:

* [Figshare](https://figshare.com/)
* [Zenodo](https://zenodo.org/)
* [Joint Research Centre Data Catalogue](https://data.jrc.ec.europa.eu/dataset)

Of course, there are also general data search engines now that may help find the data you are looking for:

* [Google Dataset Search](https://datasetsearch.research.google.com/)
* [DataCite Commons](https://commons.datacite.org/)

If you have a new dataset and like to deposit it because it is not listed in any of the above resources,
please check out the [Depositing in Zenodo generic repository](https://w3id.org/faircookbook/FCB009) recipe.

<!--
TODO: add below statement when that recipe is included too:

For details related to finding datasets and determining the correct licenses, please refer to Finding Compounds. 
-->

### Dataset Registration in Wikidata

After locating a dataset, check the availability of the details of the dataset. Essential attributes include the
DOI, the title of the dataset, the author(s) of the dataset, publication date of the dataset, and links to the
dataset source. You may need this later.

With the DOI, there is a good chance that Scholia {footcite}`Nielsen2017` can help you register the dataset in Wikidata.
You can use the `https://scholia.toolforge.org/doi/\$DOI` pattern ('\$DOI' in the link must be replaced with the
DOI of the dataset you are registering) to check if your dataset is already listed in
Wikidata. If not this page will use the DOI to convert the metadata transformed into a Quickstatements.

### Adding a dataset with Quickstatements

With the Quickstatements of the dataset, the dataset can be added to Wikidata using
the https://quickstatements.toolforge.org/ website. This is the step which requires a Wikidata account.

### Step 1: Wikidata login

First, log in with Wikidata or check if you already are.

### Step 2: Authorize Quickstatements

After step 1, authorize Quickstatements with your Wikidata account using the "Log in" button
in the top right corner of the Quickstatements website.

### Step 3: Open the Scholia page

If your dataset is not already Wikidata, use the `https://scholia.toolforge.org/doi/\$DOI` Scholia
page to create Quickstatements. The result should look something like this:

```{figure} images/scholia.png
---
name: scholia
alt: Scholia page showing Quickstatements for a dataset not yet in Wikidata
---
Scholia page showing Quickstatements for a dataset not yet in Wikidata.
```



## References

```{footbibliography}
```


---

## Authors

````{authors_fairplus}
Egon: Writing
Zachary: Writing - Original Draft
````


---

## License

````{license_fairplus}
CC-BY-4.0
````
