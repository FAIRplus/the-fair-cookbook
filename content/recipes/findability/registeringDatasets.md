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


Learn how to register a dataset on Wikidata with the appropriate citation.

___


## Requirements

To run the below scripts, you need a Groovy installation. The Groovy script use version X.X of the Chemistry Development Kit (add the link here) (see also doi:10.1186/s13321-017-0220-4). (Add link here) This library and its use in Groovy is further explained in the book Groovy Cheminformatics with the Chemistry Development Kit. (add the link here)

Click here for more detailed use instructions and where to find the tools:
https://github.com/FAIRplus/fairplus-sdf(add the link here)

To register datasets to Wikidata requires a Wikidata account.

---


## Main Content


### Finding Datasets

There are several ways to locate datasets to be registered into Wikidata. A consideration is that the dataset has the recommended license. For details related to finding datasets and determining the correct licenses, please refer to Finding Compounds(add the link here)

[Link identifiers] 

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
