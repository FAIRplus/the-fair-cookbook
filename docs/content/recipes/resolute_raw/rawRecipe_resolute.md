RESOLUTE FAIRification Recipe

## RESOLUTE metadata description

The RESOLUTE metadata are stored in Owncloud. There are two datasets in the RESOUTE project,  the transcriptomics dataset and proteomics dataset (Oct, 2019). The transcriptomics dataset includes: license file, gene TPM levels and transcript TPM levels, data release information (sample metadata, sequencing experiment details, data analysis protocols, etc.) The proteomics dataset includes: license file, protein expression levels, data release information.

Currently, there is no publication in the RESOLUTE project. The RESOLUTE data and metadata are distributed under the [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).

The data release plan of RESOLUTE transcriptomics dataset includes project description, study background, study summary and the metadata of three studies: RNA-Seq measurement of parental cell lines, mapping of RNA-Seq to reference genome and gene expression analysis in parent cell lines. The data creation, identification, annotation, quality control and sustainability are explained in each study.

## FAIR assessment 

The level of "FAIRness" of the RESOLUTE transcriptomics was first determined using the CMMI maturity model described [in this document.](https://docs.google.com/document/d/1URLfNpBYkCrICpizKZJ7NE29FddNNcoR0T0o_SQza7U/edit#heading=h.w0g0276fq5i6) The results of this first assessment can be found [here](https://docs.google.com/document/d/1Q_Su8kY9uNYfCV30jSIoWNdeV8GxA_DTGAcGOSZscQM/edit?usp=sharing). In a follow up meeting we defined actions that could be taken to increase the level for certain indicators (see [this document](https://docs.google.com/document/d/1yYDcUvyXzYLfq9NZX23tbgIjCSOenSURjcRj61FMdzQ/edit?usp=sharing)). These actions were defined within Github.

A [new FAIRplus maturity model](https://docs.google.com/spreadsheets/d/11-jDoMbuxw8Nreurk7yKzk3EHJ54APAQnBl6VTKZPBk/edit#gid=1559176954) was set up, based on the RDA indicators. The focus was only on the indicators regarding Findability/Discoverability at that point. Before we could use this model however, the indicators were updated within the RDA initiative. We used their [new indicators](https://docs.google.com/spreadsheets/d/1mkjElFrTBPBH0QViODexNur0xNGhJqau0zkL4w8RRAw/edit?usp=sharing)) (for findability, v0.01) and their level definition to determine the levels for both the transcriptomics and proteomics datasets. The result can be found [here](https://docs.google.com/spreadsheets/d/1abQ5_sOmBWbxAZhQVEUxQ_ybI1yTi0t-tJAVY5J5VY8/edit?usp=sharing).

In the meantime, an improved version of the RDA indicators was released (v0.02). In the results document a comparison/mapping is made between v0.02 and v0.01 for possible future reference.We have updated the scoring for the transcriptomics data to this new version (v0.02).

* Results of the scoring (to v0.01):

    * transcriptomics data set (as in SRA)

        * 58% for the mandatory indicators

        * 63% for the recommended indicators

        * 4 indicators were thought to be not applicable

    * proteomics data set (as in OwnCloud)

        * 42% for the mandatory indicators

        * 44% for the recommended indicators

        * 6 indicators were thought to be not applicable

The FAIRness level of the transcriptomics dataset for the HUH-7 cell line (as published on SRA) was also determined using the [FAIR evaluation services](https://fairsharing.github.io/FAIR-Evaluator-FrontEnd/#!/#%2F!) (an online evaluator). The result was this dataset only passed for 3 out of the 22 indicators tested. This was mainly due to the limitations on machine readability of metadata and license details within SRA. The complete results can be viewed [here](https://fairsharing.github.io/FAIR-Evaluator-FrontEnd/#!/evaluations/170). 

## ETL pipeline (transcriptomics data set)

The metadata of RESOLUTE transcriptomics dataset are firstly extracted [using yaml format](https://raw.githubusercontent.com/ebi-ait/FAIRPlus/master/RESOLUTE/transcriptomics/scripts/transcriptomics_metadata_extract.py) using key:value pairs. An alternative option is to store the metadata in a spreadsheet. However, the RESOLUTE metadata structure is complicated, which limits the applicability of spreadsheet format. Yaml format is preferred than JSON for its clarity and readability. The Yaml files can be converted to JSON format with [PyYAML](https://pypi.org/project/PyYAML/).

The RESOLUTE transcriptomics raw metadata are informative. Two principles are used in metadata extraction.The first one is to maintain as detailed metadata as possible, though some metadata is not supported in database submission. Secondly, the metadata should support reproducing the analysis. 

The [metadata](https://github.com/ebi-ait/FAIRPlus/blob/master/RESOLUTE/transcriptomics/data/RESOLUTE_transcriptomics_metadata_raw.json) of the RESOLUTE project was extracted from the data release description into JSON files. 

The metadata was parsed according to transcriptomics community metadata standard [MINSEQE](http://fged.org/projects/minseqe/). The MINSEQE schema we used can be found [here](https://github.com/FAIRsharing/mircat/tree/master/minseqe). This version of [metadata](https://github.com/ebi-ait/FAIRPlus/blob/master/RESOLUTE/transcriptomics/data/RESOLUTE_transcriptomics_metadata_MINSEQE.json) can not be submitted to EBI databases.

To support metadata submission, we modified the [samples metadata](https://github.com/ebi-ait/FAIRPlus/blob/master/RESOLUTE/transcriptomics/data/samples_BSD.json) based on [EBI BioSamples JSON schema requirements](https://github.com/EBIBioSamples/biosamples-v4/blob/dev/webapps/core/src/main/resources/schemas/core/sample.json). BioSamples database doesn’t support nested JSON data, so we flattened the metadata before submission. To further submit study, assay, and other metadata, we used [EBI Data Submission Portal](https://www.ebi.ac.uk/submission/) to submit [study, assay, sequencing Run, sample data](https://github.com/ebi-ait/FAIRPlus/tree/master/RESOLUTE/transcriptomics/data/data_for_USI) together. We also checked if the new metadata compatible with the MINSEQE guidelines. Note! DSP doesn’t support external ontology annotation URLs currently, so we didn’t include ontology mapping in this version.

We created a [transcriptomics metadata schema](https://github.com/ebi-ait/FAIRPlus/tree/master/schemas/transcriptomics_schema), which not only follows the MINSEQE guidelines, but also compatible with [EBI DSP schema](https://github.com/ebi-ait/FAIRPlus/blob/master/schemas/EBI_database_schemas/USI_schemas/USI_root_schema.json). Example data and submission guide will be added soon.

For future metadata submission, we created [easyUSI](https://github.com/FuqiX/easyUSI), an EBI DSP submission tool to simplify the sample metadata submission process and make the submission scalable.

## Data acquisition

* identifiers

* initial, local data QC

## Data transfer

* SFTP server

* OneDrive

* Amazon S3 Buckets

## Data processing & analysis

* raw data → processed data → interpreted data

* workflow / pipeline annotation

* data provenance

## Data annotation

* According to our Data Management Plan (DMP)

* Word document (as temporary solution until we finished schema definition for the RESOLUTE repository)

    * JSON schemas

* FAIR aspects

## Data release

* consortium internal QC and discussion (RESOLUTE’s *"data annotation & release workshop"*)

* decision on license

## Data submission:

* raw data: SRA [Transcriptomics], ProteomeXchange [Proteomics]

* interpreted data: ?

* source annotation: BioSamples

    * automatic via SRA → ENA

    * extension?

