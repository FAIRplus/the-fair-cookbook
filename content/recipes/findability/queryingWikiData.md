# Querying WikiData


 ````{panels_fairplus}
:identifier_text: FCB053 
:identifier_link: 'https://w3id.org/faircookbook/FCB053'
:difficulty_level: 3
:recipe_type: hands_on
:reading_time_minutes: 15
:intended_audience: bioinformatician, data_scientist, data_engineer
:has_executable_code: nope
:recipe_name: How to Query WikiData
```` 

## Main Objectives



The primary purpose of this recipe is:

> How to generate globally unique, resolvable, and persistent identifiers, starting from an InChIKey

Globally unique keys are crucial to the maintenance of an open-source database such as WikiData. They ensure that entities such as chemical compounds are not duplicated throughout the database. For chemical compounds, many identifiers can label a compound. However, many of these are not unique to the compound described. For example, the formula for compounds may be the same for several different compounds. Moreover, for other identifiers such as the canonical smiles, a compound may multiple smiles associated with it. Both of these scenarios are problematic to add entities to an open source database. 

Therefore, before we desire the identifier for our compound to be globally unique, resolvable, and persistent, the InChI key is used as the identifier.

___


When creating a resolvable identifier for a compound without the inChIkey already present, another identifier is required. This  identifier could be any one of the following

* Smiles
* InChI
* IUPACName

The following scripts support CSV files with headers. They take in a CSV with one of the identifiers listed above and output a list of InChiKeys in a separate output file. 

The script requires that the column with the identifier is specified and the specification of the type of identifier.

For example:

groovy fileName -sep '\t' outputFileName identiferColumnName identifierType 


## Requirements

---


## Main Content


## Conclusion



## Authors


| Name                                                                                                                                                                                                                                       | Orcid                                                                                                                        | Affiliation                           | Type                                                                              |                                                              Elixir Node                                                              | Credit Role
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------:|:----------------:|
| <div class="firstCol"><a target="_blank" href='https://github.com/'><img class='avatar-style' src='https://avatars.githubusercontent.com/no_github'></img><div class="d-block">Zachary Warnes</div></a>  </div>         | <a target="_blank" href='https://orcid.org/0000-0000-0000-0000'><i class='fab fa-orcid fa-2x text--orange'></i></a> | Maastricht University     | <i class="fas fa-graduation-cap fa-1x text--orange" alt="Academic"></i> | <img class='elixir-style' src='/the-fair-cookbook/_static/images/logo/Elixir/ELIXIR-UK.svg' ></img> | Writing – Review & Editing, Conceptualization

---

## License

This page is released under the Creative Commons 4.0 BY license.

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png" height="20"/></a>