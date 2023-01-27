(fcb-eubopen)=
#  IMI EUBOPEN FAIR High-Content Screening data deposition


````{panels_fairplus}
```` 


## Abstract

This datatype-specific recipe for **bio-imaging data**, specifically **High-Content Screening data** for compound libraries,
provides:
* informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion on available data and metadata standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s, as well as on missing pieces.
* recommends domain-specific repositories (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository). 
* ways to structure your data.

If you run high-content screens to test the effect of compounds on cells and want to make your data FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/), 
this recipe is for you.


## Background

[High-content screening (HCS)](https://en.wikipedia.org/wiki/High-content_screening) is about detecting a phenotypic
change in living cells following exposure to a test compound.

HC(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/1020)S typically generates data with a large volume rate (60 GB / hour). 

Typically, 384-well plates are imaged regularly in an automated microscope to investigate the time-dependent
phenotypic change after treatment with test compound, compared to a placebo treatment.

Thus, hundreds of different compounds might be tested in parallel, and a typical experiment might run for 48 hours, giving rise
to high-volume, high-velocity, complex data. 

Automated analysis is therefore key to providing interpretable results fast.

### Additional reading

*  More Background on the datatype "BioImaging(URL_TO_INSERT_RECORD http://bioimg.weizmann.ac.il)" and associated methods.


## Table of Data Standards

|Data Format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s|Terminologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)|Model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)|
|--- |--- |--- |
|[OME(URL_TO_INSERT_RECORD https://openmicroscopy.org)-TIFF(URL_TO_INSERT_RECORD http://www.openmicroscopy.org/site/support/ome-model/ome-tiff/)](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.cq8tg2)|||
|||[REMB(URL_TO_INSERT_RECORD http://www.Metabase.net)I(URL_TO_INSERT_RECORD https://doi.org/10.1038/s41592-021-01166-8)](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/523)|




## Table of Software and Tools

|Tool Name|
|--- |
|[tiffutil](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/ncsuarc/tiffutils)|
|[BioImage Arch(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ive(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/bioimage-archive/)(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/bioimage-archive/)](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.x38D2k)|
|[BioStudies(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/biostudies/)(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/biostudies/)](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.mtjvme)|
|[Aspera](https://www.ibm.com/products/aspera)|



## (Meta-)Data standards for images

There is not a single data standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) for microscopy images.

One of the advanced open community standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s is [OME(URL_TO_INSERT_RECORD https://openmicroscopy.org)-TIFF(URL_TO_INSERT_RECORD http://www.openmicroscopy.org/site/support/ome-model/ome-tiff/)](https://docs.openmicroscopy.org(URL_TO_INSERT_RECORD https://openmicroscopy.org)/ome-model/5.6.3/ome-tiff/index.html).

Ideally, your HC(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/1020)S instrument produces an open data format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) by default, and not a proprietary vendor-specific format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format). 
To find out, you can consult the user manual of your instrument, or try to work with tools like
["tiffutil"](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/ncsuarc/tiffutils) to investigate the produced files.

Possibly, multiple images are combined into one file, e.g. [z-stacks](https://en.wikipedia.org/wiki/Focus_stacking), 
time series, or versions with different resolutions of the same image.

For some use cases this might be beneficial, for others undesired. 

Some are optimized for cloud compute, others for local compute. 

Transfer and conversion of data sets is typically a challenge because of the high data volume. 

You might need to resort to high-speed transfer tooling to transfer data fast enough, such as 
[Aspera](https://www.ibm.com/products/aspera), especially when in industrial settings.

(Meta-)Data might be embedded into the file containing the image, e.g. in OME(URL_TO_INSERT_RECORD https://openmicroscopy.org)-TIFF(URL_TO_INSERT_RECORD http://www.openmicroscopy.org/site/support/ome-model/ome-tiff/) format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format).

This might include "identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s", e.g. a URN in OME(URL_TO_INSERT_RECORD https://openmicroscopy.org)-TIFF(URL_TO_INSERT_RECORD http://www.openmicroscopy.org/site/support/ome-model/ome-tiff/), but also further informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion, 
e.g. about the employed excitation/emission filters during the imaging.

In some format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s, e.g. OME(URL_TO_INSERT_RECORD https://openmicroscopy.org)-XML(URL_TO_INSERT_RECORD https://www.w3.org/TR/xml/)(URL_TO_INSERT_RECORD https://docs.openmicroscopy.org/ome-model/6.2.2/ome-xml/index.html), this informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion is held in separate files, linking to other files through their identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s.

Strict definitions of "data" and "metadata" did not reach community-consensus in the field yet, and can be generally 
assumed missing.


## (Meta-)Data standard for high-content screening experiments

There is not a single specification around a metadata standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) for high-content screening experiments.

The most advanced recommendation is [REMBI](http://bit.ly/rembi_v1), the "Recommended Metadata for Biological Images(URL_TO_INSERT_RECORD https://doi.org/10.1038/s41592-021-01166-8)" 
{footcite}`Sarkans2021` .

REMB(URL_TO_INSERT_RECORD http://www.Metabase.net)I(URL_TO_INSERT_RECORD https://doi.org/10.1038/s41592-021-01166-8) spans different layers of granularity, from study, over samples, to images and even analyzed data. 
This granularity is not necessarily reflected in the ways available to store informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion in files.

Strict definitions of "data" vs. "metadata" did not reach community-consensus in the field.


## Repositories for high-content screening data

Given the high volume and velocity of HC(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/1020)S data, you might find yourself wanting to deposit your data as soon as
possible into a public repository (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository), away from your HC(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/1020)S instrument.

A typical alternative set-up is the availability of large network-connected storage, which is used to store the 
intermediate data until it is analyzed by automated methods.

A possibility to start is the BioImage Arch(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ive(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/bioimage-archive/)(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/bioimage-archive/), which allows to deposit any files in a submission. 

Each submission receives a persistent identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) in the sense of an URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630) promised to be persistent; 
individual files do not receive individual identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s, but are accessible via HTTP-resolvable URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)s.

You will need to find your own way to represent your data in BioImage Arch(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ive(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/bioimage-archive/)(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/bioimage-archive/) or similar repositories (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository),
as no community-agreed standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s exist.

An exemplar of a data deposition including informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion about the assayed compounds and links to raw data,
description of the analysis pipeline, and processed images can be retrieved using this 
[BioStudies](https://www.ebi.ac.uk/biostudies(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/biostudies/)/) accession number:
[S-BIAD145](https://www.ebi.ac.uk/biostudies(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/biostudies/)/studies/S-BIAD145)


## Tips for pragmatic Research Data Management in High-Content Screening

To enable automated compound assessment, the authors of this recipe found it helpful to separate the following entities 
conceptually: experiments, imaging data acquisitions, compounds, compound batches, compound map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)s.

Those entities can be described in a database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)-like Excel file for each of your experiments,
and can be easily quality-controlled.

The IT footprint of this solution is minimal, and might be perfectly suited if you do not work in a company 
performing exclusively HC(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/1020)S experiments.

This should allow you to connect your final results with the underlying "metadata" about the actual experiments.

An exemplar of an implementation is described in the published protocol "High-Content Live-Cell Multiplex Screen 
for Chemogenomics Compound Annotation based on Nuclear Morphology" *(in preparation)*, 
with the corresponding Python code available on Zenodo(URL_TO_INSERT_RECORD https://www.zenodo.org)(URL_TO_INSERT_RECORD https://www.zenodo.org): 
[doi:10.5281/zenodo(URL_TO_INSERT_RECORD https://www.zenodo.org).6325622](https://doi.org/10.5281/zenodo.6325622)


## Step-by-step recipe

1. Download the Python scripts and the metadata template Excel sheet from [doi:10.5281/zenodo(URL_TO_INSERT_RECORD https://www.zenodo.org).6325622](https://doi.org/10.5281/zenodo.6325622).
or this [GitHub(URL_TO_INSERT_RECORD https://github.com/)(URL_TO_INSERT_RECORD https://github.com/) repository (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository)](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/rgiessmann/data-management-for-high-content-screening)
2. Organize your metadata according to the metadata template sheet.


````{dropdown}
```{figure} ../../../images/bioimage-excel.png
---
width: 800px
name: fbioimage-excel
alt: Overview of the bioimage-excel
---
Overview of the bioimage-excel.
```
````


3. Generate file lists with the Python scripts.

```python
```


4. Zip the raw data, and upload the zip files as well as the individual processed images to [BioImage Arch(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ive(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/bioimage-archive/)(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/bioimage-archive/)](https://www.ebi.ac.uk/bioimage-archive(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/bioimage-archive/)/).


5. Run the automated analysis of your data with the Python scripts.

```python
```


6. Upload your analysis data and the aggregated version to Zenodo(URL_TO_INSERT_RECORD https://www.zenodo.org)(URL_TO_INSERT_RECORD https://www.zenodo.org).


## Conclusion

With this content and the associated python scripts, we highlight path to deposit HC(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/1020)S imaging data the EMB(URL_TO_INSERT_RECORD http://www.Metabase.net)L-EBI BioImage Arch(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ive(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/bioimage-archive/)(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/bioimage-archive/).
This therefore improves **Findability** and **Reusability** of such data.

### What to read next?
- {ref}`fcb-access-aspera`
- {ref}`fcb-find-zenodo(URL_TO_INSERT_RECORD https://www.zenodo.org)`
````{rdmkit_panel}
```` 



## References
````{dropdown} **References**
```{footbibliography}
```
````


## Authors

````{authors_fairplus}
````


## License

````{license_fairplus}
````
