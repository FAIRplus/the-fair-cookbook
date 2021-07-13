# Update Chemical Identities

 ````{panels_fairplus}
:identifier_text: FCB053 
:identifier_link: 'https://w3id.org/faircookbook/FCB053'
:difficulty_level: 2
:recipe_type: hands_on
:reading_time_minutes: 10
:intended_audience: bioinformatician, data_scientist, data_engineer
:has_executable_code: yes
:recipe_name: How to update chemical identities
```` 

## Main Objectives

The primary purpose of this recipe is:

> Determine chemical identifiers, given a compound
> Updating chemical compounds in WikiData


## 1 Requirements

1) Bash Knowledge
2) Groovy Knowledge
3) WikiStatement Knowledge (Optional)

---


## 2 Main Content

**Where should I place scripts for recipes?*


### 2.1 Generating Compound Identifiers
Updating chemical identifiers requires the existing knowledge of at least one chemical identifier. 

From this identifier, other compound identifiers can be determined using the following script:

```
groovy -identifier <Identifier> -identifierType <IdentifierType>
```
This script is available from the chemistry development kit/


### 2.2 Updating WikiData
With the available identifiers of a compound the compound can be updated within WikiData using any of the following:

- Direct edits to the compound page from the compound's WikiData page using the 'edit' functionality 
- Quick statements at https://quickstatements.toolforge.org/



## Conclusion
This recipe discussed several aspects of updating chemical compounds
- How to retrieve chemical identifiers given an original identifier
- How to update chemical identification properties in WikiData 


## Authors


| Name                                                                                                                                                                                                                                       | Orcid                                                                                                                        | Affiliation                           | Type                                                                              |                                                              Elixir Node                                                              | Credit Role
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------:|:----------------:|
| <div class="firstCol"><a target="_blank" href='https://github.com/'><img class='avatar-style' src='https://avatars.githubusercontent.com/no_github'></img><div class="d-block">Zachary Warnes</div></a>  </div>         | <a target="_blank" href='https://orcid.org/0000-0000-0000-0000'><i class='fab fa-orcid fa-2x text--orange'></i></a> | Maastricht University     | <i class="fas fa-graduation-cap fa-1x text--orange" alt="Academic"></i> | <img class='elixir-style' src='/the-fair-cookbook/_static/images/logo/Elixir/ELIXIR-UK.svg' ></img> | Writing – Review & Editing, Conceptualization

---

## License

This page is released under the Creative Commons 4.0 BY license.

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png" height="20"/></a>