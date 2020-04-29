# Findability: Dataset Markup

# Table of Contents

1. [Main FAIRification Objectives](#Main%20FAIRification%20Objectives)
2. [Graphical Overview of the FAIRification Recipe Objectives](#Graphical%20Overview%20of%20the%20FAIRification%20Recipe%20Objectives)
3. [FAIRification Objectives, Inputs and Outputs](#FAIRification%20Objectives,%20Inputs%20and%20Outputs)
4. [Capability & Maturity Table](#Capability%20&%20Maturity%20Table)
5. [Table of Data Standards](#Table%20of%20Data%20Standards)
6. [Executable Code in Notebook](#Executable%20Code%20in%20Notebook)
7. [How to create workflow figures](#How%20to%20create%20workflow%20figures)
8. [License](#License)

---

## Main Objectives

The main purpose of this recipe is:

> To embed Schema.org markup in a web page representing a dataset.

___


## Graphical Overview of the FAIRification Recipe Objectives

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiBBW0hUTUwgcGFnZV0gLS0-IEJ7UGFnZSBqdXN0IGFib3V0IG9uZSBkYXRhc2V0P31cbiBCIC0tPnxZRVN8IEMoQ3JlYXRlIG1hcmt1cCBmb3IgZGF0YXNldClcbiBCIC0tPnxOT3wgRltVc2UgRGF0YUNhdGFsb2cgUmVjaXBlXVxuIEMgLS0-IEQoTWFya3VwIFRlbXBsYXRlKVxuIEQgLS0-fEVtYmVkIHRlbXBsYXRlIGluIHdlYnNpdGV8IEVbZmE6ZmEtc2VhcmNoIGZhOmZhLWNvZyBmYTpmYS1maWdodGVyLWpldCBTY2hlbWEub3JnIGF1Z21lbnRlZCBIVE1MIHBhZ2VdIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiBBW0hUTUwgcGFnZV0gLS0-IEJ7UGFnZSBqdXN0IGFib3V0IG9uZSBkYXRhc2V0P31cbiBCIC0tPnxZRVN8IEMoQ3JlYXRlIG1hcmt1cCBmb3IgZGF0YXNldClcbiBCIC0tPnxOT3wgRltVc2UgRGF0YUNhdGFsb2cgUmVjaXBlXVxuIEMgLS0-IEQoTWFya3VwIFRlbXBsYXRlKVxuIEQgLS0-fEVtYmVkIHRlbXBsYXRlIGluIHdlYnNpdGV8IEVbZmE6ZmEtc2VhcmNoIGZhOmZhLWNvZyBmYTpmYS1maWdodGVyLWpldCBTY2hlbWEub3JnIGF1Z21lbnRlZCBIVE1MIHBhZ2VdIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)

```
graph TD
 A[HTML page] --> B{Page just about one dataset?}
 B -->|YES| C(Create markup for dataset)
 B -->|NO| F[Use DataCatalog Recipe]
 C --> D(Markup Template)
 D -->|Embed template in website| E[fa:fa-search fa:fa-cog fa:fa-fighter-jet Schema.org augmented HTML page]
```

___

## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Findability | minimal | repeatable |
| Interoperability | minimal |  |

----


## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [text annotation](http://edamontology.org/operation_3778)  | [Bioschemas](https://fairsharing.org/FAIRsharing.20sbr9) | [annotated text](http://edamontology.org/data_3779)  |
| [validation](http://edamontology.org/operation_2428) | [schema.org](https://fairsharing.org/FAIRsharing.hzdzq8) | [report](http://edamontology.org/data_2048) |


## Table of Data Standards

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| [JSON-LD](http://edamontology.org/format_3749)  | [Bioschemas](https://fairsharing.org/FAIRsharing.20sbr9) | [RDF](http://edamontology.org/data_2353)  |
| [HTML](http://edamontology.org/format_2331) | | |
___

## Authors:

| Name          | Affiliation                                                  | orcid                                                        | CrediT role              |
| :------------ | :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------- |
| Alasdair Gray | Bioschemas Community Lead / Heriot-Watt Unviersity / ELIXIR-UK | [0000-0002-5711-4872](https://orcid.org/0000-0002-5711-4872) | Writing - Original Draft |

___


## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
