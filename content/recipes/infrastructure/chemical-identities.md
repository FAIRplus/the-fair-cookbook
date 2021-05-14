(fcb-infra-chemid)=
# Chemical Identity - InChI and SMILES

+++
<br/>

````{panels_fairplus}
:identifier_text: F1
:identifier_link: 'https://example.com'
:difficulty_level: 2
:recipe_type: hands_on
:reading_time_minutes: 15
:intended_audience: chemoinformatician, data_curator, data_manager, data_scientist  
:has_executable_code: yeah
:recipe_name: Chemical Identity - InChI and SMILES
```` 

## Standards:

* SDF file (FairSharing doi:[10.25504/fairsharing.ew26v7](https://doi.org/10.25504/fairsharing.ew26v7))
* SMILES (FairSharing doi:[10.25504/fairsharing.qv4b3c](https://doi.org/10.25504/fairsharing.qv4b3c))
* InChI (FairSharing doi:[10.25504/fairsharing.ddk9t9](https://doi.org/10.25504/fairsharing.ddk9t9))

## Databases:

* PubChem (FairSharing doi:[10.25504/fairsharing.qt3w7z](https://doi.org/10.25504/fairsharing.qt3w7z))
* ChemSpider (FairSharing doi:[10.25504/fairsharing.96f3gm](https://doi.org/10.25504/fairsharing.96f3gm))
* Wikidata (FairSharing doi:[10.25504/fairsharing.6s749p](https://doi.org/10.25504/fairsharing.6s749p))

## Identifiers:

* International Chemical Identifier (InChI)

## Tools:

* Programming Language: Groovy
* Dependencies: CDK 2.3
* FAIRPlus SDF tools

### Requirements

To run the below scripts, you need a [Groovy](https://groovy.apache.org/download.html) installation.
The Groovy scripts use version 2.3 of the [Chemistry Development Kit](https://cdk.github.io/)
(see also doi:[10.1186/s13321-017-0220-4](https://doi.org/10.1186/s13321-017-0220-4)).
This library and its use in Groovy is further explain in
the book [Groovy Cheminformatics with the Chemistry Development Kit](https://egonw.github.io/cdkbook/).


Click here for more detailed use instructions and where to find the tools:
[https://github.com/FAIRplus/fairplus-sdf](https://github.com/FAIRplus/fairplus-sdf)

### Record validation

When generating InChIs, the InChI library may return two success states reflecting issues with
the compound record in the SDF file: WARNING and ERROR. This first script reports such issues:

```bash
groovy badRecords.groovy -f foo.sdf
```

* Input: SDF file
* Output: Reports validation issues


### Calculate InChls

Similarly, InChIKeys can be generated:

```bash
groovy inchikeys.groovy -f foo.sdf
```

* Input: SDF file
* Output: list of InChIs

When the success state is ERROR, nothing is outputted.

### Calculate SMILES strings

The last script calculates a SMILES for each entry in the SDF file:

```bash
groovy smiles.groovy -f foo.sdf
```

* Input: SD file
* Output: list of SMILES strings



## Authors:

| Name                                                                                                                                                                                                                                       | Orcid                                                                                                                        | Affiliation                           | Type                                                                              |                                                              Elixir Node                                                              | Credit Role
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------:|:----------------:|
| <div class="firstCol"><a target="_blank" href='https://github.com/egonw'><img class='avatar-style' src='https://avatars.githubusercontent.com/egonw'></img><div class="d-block">Egon Willighagen</div></a>  </div>        | <a target="_blank" href='https://orcid.org/0000-0001-7542-0286'><i class='fab fa-orcid fa-2x text--orange'></i></a> | University of Maastricht        | <i class="fas fa-graduation-cap fa-1x text--orange" alt="Academic"></i> | <img class='elixir-style' src='/the-fair-cookbook/_static/images/logo/Elixir/ELIXIR-NL.svg' ></img> | Writing - Original Draft, Conceptualization
| <div class="firstCol"><a target="_blank" href='https://github.com/proccaserra'><img class='avatar-style' src='https://avatars.githubusercontent.com/proccaserra'></img><div class="d-block">Philippe Rocca-Serra</div></a>  </div>         | <a target="_blank" href='https://orcid.org/0000-0001-9853-5668'><i class='fab fa-orcid fa-2x text--orange'></i></a> | University of Oxford     | <i class="fas fa-graduation-cap fa-1x text--orange" alt="Academic"></i> | <img class='elixir-style' src='/the-fair-cookbook/_static/images/logo/Elixir/ELIXIR-UK.svg' ></img> | Writing – Review & Editing

___

## License:

This page is released under the Creative Commons 4.0 BY license.

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png" height="20"/></a>


