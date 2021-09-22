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
itself. This [Wikidata:Introduction](https://www.wikidata.org/wiki/Wikidata:Introduction) describes the principle ideas and data model that will make this
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

<!--
TODO: add below statement when that recipe is included too:

For details related to finding datasets and determining the correct licenses, please refer to Finding Compounds. 
-->

### Data Set Registration

After locating a dataset, record the details of the dataset. Essential attributes include the DOI, the title of the dataset, the author(s) of the dataset, publication date of the dataset, and links to the dataset source.

Dataset details can be transformed into a Quickstatement using https://scholia.toolforge.org/doi/\$DOI. '\$DOI' in the link must be replaced with the DOI of the dataset you are registering.


### Adding 

With the Quickstatement of the dataset, the dataset can be added to Wikidata using https://quickstatements.toolforge.org/. This step requires a Wikidata account. 


## Authors


| Name                                                                                                                                                                                                                                       | Orcid                                                                                                                        | Affiliation                           | Type                                                                              |                                                              Elixir Node                                                              | Credit Role
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------:|:----------------:|
| <div class="firstCol"><a target="_blank" href='https://github.com/'><img class='avatar-style' src='https://avatars.githubusercontent.com/no_github'></img><div class="d-block">Zachary Warnes</div></a>  </div>         | <a target="_blank" href='https://orcid.org/0000-0000-0000-0000'><i class='fab fa-orcid fa-2x text--orange'></i></a> | Maastricht University     | <i class="fas fa-graduation-cap fa-1x text--orange" alt="Academic"></i> | <img class='elixir-style' src='/the-fair-cookbook/_static/images/logo/Elixir/ELIXIR-UK.svg' ></img> | Writing – Review & Editing, Conceptualization

---

## License

This page is released under the Creative Commons 4.0 BY license.

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png" height="20"/></a>
