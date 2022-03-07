(fcb-eubopen)=
# FAIRification of High-Content Screening data using Bioimage Archive

````{panels_fairplus}
:identifier_text: TODO
:identifier_link: TODO
:difficulty_level: 3
:recipe_type: applied_example
:reading_time_minutes: 15
:intended_audience: data_manager  
:has_executable_code: nope
:recipe_name: FAIR High-Content Screening data
```` 


## Abstract

You run high-content screens to test the effect of compounds on cells. You want to make your data FAIR. This recipe is for you. 


## Recipe

1. Download the Python scripts and the metadata template Excel sheet from [https://doi.org/10.5281/zenodo.6325622](https://doi.org/10.5281/zenodo.6325622).
2. Organize your metadata according to the metadata template sheet.
3. Generate filelists with the Python scripts.
4. Zip the raw data, and upload the zip files as well as the individual processed images to [BioImage Archive](https://www.ebi.ac.uk/bioimage-archive/).
5. Run the automated analysis of your data with the Python scripts.
6. Upload your analysis data and the aggregated version to Zenodo.


## Additional reading

*  Background on the datatype "Bioimaging"


---

## Authors

````{authors_fairplus}
Robert: Writing - Original Draft
````


--- 

## License

````{license_fairplus}
CC-BY-4.0
````
