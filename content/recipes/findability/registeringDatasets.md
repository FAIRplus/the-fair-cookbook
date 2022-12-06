# Registering Datasets in Wikidata

 ````{panels_fairplus}
:identifier_text: FCB060
:identifier_link: 'https://w3id.org/faircookbook/FCB060'
:difficulty_level: 2
:recipe_type: hands_on
:reading_time_minutes: 15
:intended_audience: bioinformatician, data_scientist, data_engineer
:maturity_level: 1
:maturity_indicator: 5, 8
:has_executable_code: nope
:recipe_name: Registering datasets with Wikidata 
```` 

[comment]: <> ("UCnn.x Registering a dataset in Wikidata.")


## Main Objectives

Useful datasets become more useful when they are easily found. The **FAIR principles** state that: 

> F1. (Meta)data are assigned a globally unique and persistent identifier
> 
> A1. (Meta)data are retrievable by their identifier using a standardised communications protocol 

This recipe is about making an already archived dataset metadata more **Findable** by getting the metadata distributed into other databases:

> Learn how to register a published dataset on Wikidata with the appropriate citation to increase its findability.



## Requirements

Register datasets in [Wikidata](https://www.wikidata.org/) {footcite}`Waagmeester2020` requires that the dataset is already archived somewhere that provides
an DOI for the datasets, and it also requires that you have a Wikidata account ([create one](https://www.wikidata.org/wiki/Special:CreateAccount)).



## Main Content

Archiving a dataset can be an important step in making data FAIR (see *Depositing in Zenodo generic repository*, [fcb:FCB009](https://w3id.org/faircookbook/FCB009)),
but by sharing the metadata, you make the dataset even more Findable. Sharing the metadata in Wikidata has the advantage that the dataset can
be linked to many other life sciences databases.

This recipe takes an interest in datasets with information about small chemical compounds, particularly datasets with an [SDF](https://fairsharing.org/FAIRsharing.ew26v7)
file or spreadsheets containing chemical identifiers in the form of [SMILES](https://fairsharing.org/FAIRsharing.qv4b3c) strings.
But the **Wikidata registration process** itself, to increase **Findability**, works for any dataset.
This [Wikidata:Introduction](https://www.wikidata.org/wiki/Wikidata:Introduction) describes the principle ideas and data model that will make this
recipe easier to follow.

Importantly, registering a dataset in Wikidata allows it to be used as reference to support other Wikidata statements (existing or newly created ones).
For example, if the dataset contains a **logP** value,
then this logP value can be associated to the compound in Wikidata with a statement, with the dataset itself as reference.
<!-- TODO: add screenshot of example -->

### Finding Datasets

There are several ways to locate datasets to be registered into Wikidata. One needs to take into consideration the following two requirements:
the dataset should have a compatible license and the dataset should have an identifier.

Examples of where open datasets with information about chemical compounds can be found include:

* [Figshare](https://figshare.com/)
* [Zenodo](https://zenodo.org/)
* [Joint Research Centre Data Catalogue](https://data.jrc.ec.europa.eu/dataset)

Of course, there are also general data search engines now that may help find the data you are looking for:

* [Google Dataset Search](https://datasetsearch.research.google.com/)
* [DataCite Commons](https://commons.datacite.org/)

If you have a new dataset and would like to deposit it because it is not listed in any of the above resources,
please check out the [Depositing in Zenodo generic repository](https://w3id.org/faircookbook/FCB009) recipe.

<!--
TODO: add below statement when that recipe is included too:

For details related to finding datasets and determining the correct licenses, please refer to Finding Compounds. 
-->

### Dataset Registration in Wikidata

After locating a dataset, check the availability of the details of the dataset. Essential attributes include:

* the DOI
* the title of the dataset
* the author(s) of the dataset
* the publication date of the dataset
* links to the dataset source.

  You may need these later, during the Wikidata registration process.

With the DOI, there is a good chance that [Scholia](https://scholia.toolforge.org/) {footcite}`Nielsen2017` can help you register the dataset in Wikidata.
You can use the `https://scholia.toolforge.org/doi/$DOI` pattern ('$DOI' in the link must be replaced with the
DOI of the dataset you are registering) to check if your dataset is already listed in
Wikidata.
If not, this page will use the DOI to convert the associated metadata and translate them into a Wikidata compatible Scholia **Quickstatements**.

### Adding a dataset with Quickstatements

[Quickstatements](https://quickstatements.toolforge.org/) is a layer on top of Wikidata, a tool developed by Magnus Manske, research in Cambridge/UK to
make it easier to edit Wikidata in an automated way. We use this here to automate the registering of
a dataset in Wikidata too. We first generate **Quickstatements** which
can be added to Wikidata using
the [https://quickstatements.toolforge.org/](https://quickstatements.toolforge.org/) website.
This is the step which requires a **Wikidata account**.

#### Step 1: Wikidata login

First, [log in to Wikidata](https://www.wikidata.org/w/index.php?title=Special:UserLogin&returnto=Wikidata%3AMain+Page).

#### Step 2: Authorize Quickstatements

Then, authorize Quickstatements with your Wikidata account using the "Log in" button
in the top right corner of the Quickstatements website.

#### Step 3: Open the Scholia page

If your dataset is not already Wikidata, use the `https://scholia.toolforge.org/doi/$DOI` Scholia
page to create Quickstatements. The result should look something like this:

````{dropdown}
:open:
```{figure} images/scholia.png
---
width: 1200px
name: scholia
alt: Scholia page showing Quickstatements for a dataset not yet in Wikidata
---
Scholia page showing Quickstatements for a dataset not yet in Wikidata.
```
````

#### Step 4: Execute the Quickstatements

On the page from Step 3, click the blue "Submit to Quickstatements" button which will take you to the
Quickstatements website, which will look something like this:

````{dropdown}
:open:
```{figure} images/quickstatements.png
---
width: 1200px
name: quickstatements
alt: Quickstatements showing the same Quickstatements but now parsed and ready for applying to Wikidata
---
Quickstatements showing the same Quickstatements but now parsed and ready for applying to Wikidata.
```
````

After you click "Run", Quickstatements starts making edits in Wikidata, and when done, it should look
like this:

````{dropdown}
:open:
```{figure} images/quickstatements2.png
---
width: 1200px
name: quickstatements2
alt: Quickstatements showing the same Quickstatements after applying to Wikidata
---
Quickstatements showing the same Quickstatements after applying to Wikidata.
```
````

### Optional: adding additional information

The result page from Step 4 will include a link to the newly created Wikidata item. It will have
a Wikidata identifier starting with an "Q", for example [Q108653787](https://www.wikidata.org/wiki/Q108653787).

Additional information that can be provided include:

* links to Wikidata items for authors using the P50 property for "author"
* keywords
* other metadata

This [Use Scholia and Wikidata to find scientific literature](https://laurendupuis.github.io/Scholia_tutorial/)
tutorial provides more information on how Wikidata uses keywords to further expose literature,
but works identical to other research output, such as datasets.

## References
````{dropdown} **References**
```{footbibliography}
```
````


## Authors

````{authors_fairplus}
Egon: Writing
Zachary: Writing - Original Draft
Philippe: Writing - Review & Editing
````


## License

````{license_fairplus}
CC-BY-4.0
````
