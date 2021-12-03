(fcb-interop-bioimaging)=
# Bioimaging data formats and metadata standards


````{panels_fairplus}
:identifier_text: TBA
:identifier_link: TBA
:difficulty_level: 3
:recipe_type: technical_guidance
:reading_time_minutes: 30
:intended_audience: principal_investigator, data_manager, data_scientist  
:has_executable_code: nope
:recipe_name: bioimaging data for and metadata standards
```` 

<!-- # Table of Contents
1. [Main FAIRification Objectives](#Main%20FAIRification%20Objectives)
2. [User Stories](#User%20Stories)
3. [Capability & Maturity Table](#Capability%20&%20Maturity%20Table)
4. [FAIRification Objectives, Inputs and Outputs](#FAIRification%20Objectives,%20Inputs%20and%20Outputs)
5. [Characteristics of three binary containers for imaging data](#Characteristics%20of%20three%20binary%20containers%20for%20imaging%20data)
6. [Metadata structure](#Metadata%20structure) -->

## Main FAIRification Objectives

This is a datatype specific recipe for bio-imaging data.

The main purposes of this recipe are:

> - Provide a list of current community recommendations on file format of bio-imaging data. 
> - Provide links to community recommended metadata templates

---

## User Stories

The establishment of a community-agreed standardized data format is the key to improve the Findability, Accessibilty and Interoperbility of bio-imaging data and catch up the rapid pace of innovation in biological imaging technology.

The content of this recipe is mainly adapted from [Moore, J., Allan, C., Besson, S. et al. OME-NGFF: a next-generation file format for expanding bioimaging data-access strategies. Nat Methods (2021)](https://doi.org/10.1038/s41592-021-01326-w)

---

## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Interoperability | minimal | repeatable |

---

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks | Input | Output  |
| :------------- | :------------- | :------------- |
| TBA | TBA | TBA |

## Characteristics of three binary containers for imaging data 


| Format | [TIFF](https://en.wikipedia.org/wiki/TIFF)  | [HDF5](https://www.hdfgroup.org/solutions/hdf5/) | [NGFF](https://ngff.openmicroscopy.org/latest/)  |
| :------------- | :------------- | :------------- |:------------- |
| First release | 1986  | 1998  | 2016|
| Maturity (in imaging) | Ubiquitous | Well-supported | Emerging|
| Base structure | Sequence of 2D planes | Hierarchy of ND arrays | Hierarchy of ND arrays |
| Multi-file support | With OME metadata | With internal links | Natively |
| Pyramidal images | With OME metadata |BDV, Imaris|OME-Zarr|
| Advantages|Tool support|Feature rich format|Simplicity|
| Limitations |Scalability|Parallel writes|Large number of small files|
| Ideal use case |Laptop|Powerful workstation, or cluster |Online archive, or public resource|



## Metadata structure

The Detail descriptions of the NGFF metadata can be found [here](https://ngff.openmicroscopy.org/latest/#metadata).

---


### What to read next?

> - [Next-generation file formats (NGFF) specifications](https://ngff.openmicroscopy.org/latest/#intro)
> - [OME files](http://www.openmicroscopy.org/ome-files/)
> - [OME-NGFF: a next-generation file format for expanding bioimaging data-access strategies](https://doi.org/10.1038/s41592-021-01326-w)


---

## Authors

````{authors_fairplus}
Wei: Writing - Original Draft
Philippe: Writing - Original Draft
````


---


## License

````{license_fairplus}
CC-BY-4.0
````
