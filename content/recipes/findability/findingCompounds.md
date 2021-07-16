# Finding FAIR Experimental Datasets for Chemical Compounds
 "Using Wikidata to find experimental data related chemical compounds in a FAIR dataset."


 ````{panels_fairplus}
:identifier_text: FCB053 
:identifier_link: 'https://w3id.org/faircookbook/FCB053'
:difficulty_level: 2
:recipe_type: hands_on
:reading_time_minutes: 15
:intended_audience: bioinformatician, data_curator, data_scientist, data_engineer
:has_executable_code: nope
:recipe_name: How to find FAIR Datasets
```` 

## Main Objectives

Remove later*

The goal of this recipe is to find compounds from scientific sources to add to Wiki Data. Many different trusted sources and repositories contain research surrounding chemical compounds, and, given the proper licenses, these compounds can be added to WikiData.
___

## Dataset Extensions and Identifiers

Here are some datasets types which are simple to add to WikiData. Each has a well-structured format. 

* SDF file (FairSharing doi:[10.25504/fairsharing.ew26v7](https://doi.org/10.25504/fairsharing.ew26v7))

* csv file (FairSharing [bsg-s001546/](https://fairsharing.org/bsg-s001546/))

## Identifiers
To add other related chemical identifiers to each compound at least universal identifier must be present. For example: 

* SMILES (FairSharing doi:[10.25504/fairsharing.qv4b3c](https://doi.org/10.25504/fairsharing.qv4b3c))
* InChI (FairSharing doi:[10.25504/fairsharing.ddk9t9](https://doi.org/10.25504/fairsharing.ddk9t9))




## Requirements:
* Public license knowledge
* Data format knowledge
---


## Main Content
Adding compounds to WikiData is a multi-step procedure. This process begins with identifying data with the correct licensing. There are many different resources available that have open-source research. Moreover, much of this research has datasets accompanying it: these datasets, or other various supplementary material, may be unstructured, semi-structured, or structured. Ideally, datasets in a standardized format and has some meta-information to help with identification. 

### Process
1) Searching for chemistry papers on Figshare
2) Filter papers via the CCO license search criteria
3) Search for datasets or other supplementary material
4) View the dataset contents to decern the quality


## Conclusion

> Summerize Key Learnings of the recipe.
> * Searching for datasets based on license
> * Identifying data quality
> Suggest further reading using the following:
> ### What should I read next?
> * [Registering Datasets](./.md)
> * [Unique Keys](./.md)

---


## Authors


| Name                                                                                                                                                                                                                                       | Orcid                                                                                                                        | Affiliation                           | Type                                                                              |                                                              Elixir Node                                                              | Credit Role
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------:|:----------------:|
| <div class="firstCol"><a target="_blank" href='https://github.com/'><img class='avatar-style' src='https://avatars.githubusercontent.com/no_github'></img><div class="d-block">Zachary Warnes</div></a>  </div>         | <a target="_blank" href='https://orcid.org/0000-0000-0000-0000'><i class='fab fa-orcid fa-2x text--orange'></i></a> | Maastricht University     | <i class="fas fa-graduation-cap fa-1x text--orange" alt="Academic"></i> | <img class='elixir-style' src='/the-fair-cookbook/_static/images/logo/Elixir/ELIXIR-UK.svg' ></img> | Writing – Review & Editing, Conceptualization

---

## License

This page is released under the Creative Commons 4.0 BY license.

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png" height="20"/></a>