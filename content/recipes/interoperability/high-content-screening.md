(fcb-interop-bioimaging)=
# Bioimaging data formats and metadata standards for High-Content Screening


````{panels_fairplus}
:identifier_text: TBA
:identifier_link: TBA
:difficulty_level: 3
:recipe_type: technical_guidance
:reading_time_minutes: 30
:intended_audience: principal_investigator, data_manager, data_curator, data_producer  
:has_executable_code: nope
:recipe_name: High-Content Screening
```` 


## Abstract

This datatype-specific recipe for bio-imaging data, specifically High-Content Screening data for compound libraries, provides information on available data and metadata standards, as well as on missing pieces, and recommends specific repositories and ways to structure your data.


## Background 

[High-content screening](https://en.wikipedia.org/wiki/High-content_screening) (HCS) is about detecting a phenotypic change in living cells upon addition of a test compound. 

HCS typically generates data with a large volume rate (60 GB / hour). Typically, 384 well plates are imaged regularly in an automated microscope to investigate the time-dependent phenotypic change after addition of a test compound, compared to a placebo treatment. Thus, 300 different compounds might be tested in parallel, and an experiment might run 48 hour, giving rise to high-volume, high-velocity, complex data. Automated analysis is thus key to provide interpretable results fast. 


## (Meta-)Data standards for images

There is not a single data standard for microscopy images. One of the advanced open community standards is [https://docs.openmicroscopy.org/ome-model/5.6.3/ome-tiff/index.html](OME-TIFF). Ideally, your HCS instrument produces an open data format by default, and not a proprietary vendor-specific format. To find out, you can consult the user manual of your instrument, or try to work with tools like tiffutil to investigate the produced files.

Possibly, multiple images are combined into one file, e.g. z stacks, time series, or versions with different resolutions of the same image. For some use cases this might be beneficial, for others undesired. Some are optimized for cloud compute, others for local compute. Transfer and conversion of data sets is typically a challenge because of the high data volume. You might need to resort to high-speed transfer tooling to transfer data fast enough, especially when in industrial settings.

(Meta-)Data might be embedded into the file containing the image, e.g. in OME-TIFF format. This might include "identifiers", e.g. a URN in OME-TIFF, but also further information, e.g. about the employed excitation/emission filters during the imaging. In some formats, e.g. OME-XML, this information is held in separate files, linking to other files through their identifiers.

Strict definitions of "data" and "metadata" did not reach community-consensus in the field yet, and can be generally assumed missing.


## (Meta-)Data standard for high-content screening experiments

There is not a single specification around a metadata standard for high-content screening experiments. The most advanced recommendation is [http://bit.ly/rembi_v1](REMBI), the "Recommended Metadata for Biological Images".\footcite{Sarkans2021} REMBI spans different layers of granularity, from study, over samples, to images and even analyzed data. This granularity is not necessarily reflected in the ways available to store information in files.

Strict definitions of "data" vs. "metadata" did not reach community-consensus in the field.


## Repositories for high-content screening data

Given the high volume and velocity of HCS data, you might find yourself wanting to deposit your data as soon as possible into a public repository, away from your HCS instrument. A typical alternative set-up is the availability of large network-connected storage which is used to store the intermediate data until it is analyzed by automated methods.

A possibility to start is the BioImage Archive, which allows to deposit any files in a submission. Each submission receives a persistent identifier in the sense of an URL promised to be persistent; individual files do not receive individual identifiers, but are accessible via HTTP-resolvable URLs.

You will need to find your own way to represent your data in BioImage Archive or similar repositories, as no community-agreed standards exist. An exemplar of a data deposition including information about the assayed compounds and links to raw data, description of the analysis pipeline, and processed images can be found here: [https://www.ebi.ac.uk/biostudies/studies/S-BIAD145](https://www.ebi.ac.uk/biostudies/studies/S-BIAD145)


## Tips for pragmatic Research Data Management in High-Content Screening

To enable automated compound assessmennt, the authors of this recipe found it helpful to separate the following entities conceptually: experiments, imagings, compounds, compound batches, compound maps. Those entities can be described in a database-like Excel file for each of your experiments, and can be easily quality-controlled. The IT footprint of this solution is minimal, and might be perfectly suited if you do not work in a company performing exclusively HCS experiments.

This should allow you to connect your final results with the underlying "metadata" about the actual experiments. An exemplar of an implementation is described in the published protocol "High-Content Live-Cell Multiplex Screen for Chemogenomic Compound Annotation based on Nuclear Morphology" (in preparation), with the corresponding Python code available on Zenodo: [https://doi.org/10.5281/zenodo.6325622](https://doi.org/10.5281/zenodo.6325622)


---

## Authors

````{authors_fairplus}
Wei: Writing - Original Draft
Philippe: Writing - Original Draft
Robert: Writing - Original Draft
````


---

## License

````{license_fairplus}
CC-BY-4.0
````