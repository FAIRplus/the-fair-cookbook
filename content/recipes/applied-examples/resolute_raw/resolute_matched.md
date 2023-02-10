(fcb-resolute)=
# ReSOLUTE - transcriptomics datasets

+++

<!--
TODO clarify authors
TODO make referenced Google Drive documents available
-->

````{panels_fairplus}
:identifier_text: FCB045
:identifier_link: 'https://w3id.org/faircookbook/FCB045'
:difficulty_level: 4
:recipe_type: applied_example
:reading_time_minutes: 10
:intended_audience: data_manager, data_curator, ontologist
:maturity_level: 2
:maturity_indicator: 1, 2
:has_executable_code: nope
:recipe_name: Depositing IMI ReSOLUTE transcriptomics datasets to EBI repositories 
```` 


````{admonition} Editor's summary
The authors of this recipe delivered a set of JSON schemas for describing Transcriptomics experiments. 
````


## Ingredients

*   Data transfer tools: 
    *   SFTP server
    *   OneDrive
    *   Amazon S3 Buckets
*   Data hosting platform: 
    *   raw data: SRA (URL_TO_INSERT_RECORD-ABBREV_701 https://fairsharing.org/FAIRsharing.g7t2hv)  [Transcriptomics]
    *   ProteomeXchange (URL_TO_INSERT_RECORD-NAME_702 https://fairsharing.org/FAIRsharing.92dt9d)  [Proteomics]
    *   Samples metadata: BioSamples
*   Data standard (URL_TO_INSERT_TERM_703 https://fairsharing.org/search?fairsharingRegistry=Standard) s
    *   Transcriptomics community standard (URL_TO_INSERT_TERM_704 https://fairsharing.org/search?fairsharingRegistry=Standard) : [MINSEQE](http://fged.org/projects/minseqe/)
    *   Sample metadata schema: [BioSamples JSON schema](https://github.com/EBIBioSamples/biosamples-v4/blob/dev/webapps/core/src/main/resources/schemas/core/sample.json)
    *   [Data submission portal](https://www.ebi.ac.uk/submission/) schema
*   FAIR (URL_TO_INSERT_RECORD-ABBREV_706 https://fairsharing.org/FAIRsharing.WWI10U)  evaluation standard (URL_TO_INSERT_TERM_705 https://fairsharing.org/search?fairsharingRegistry=Standard) : 
    *   [RDA FAIR indicators](https://github.com/RDA-FAIR/FAIR-data-maturity-model-WG/tree/master/results%20of%20preliminary%20analysis)

This recipe provides an example of sample metadata extraction and curation practices, suggests a community standard (URL_TO_INSERT_TERM_707 https://fairsharing.org/search?fairsharingRegistry=Standard)  for 
transcriptomics data and proposes a transcriptomics JSON (URL_TO_INSERT_RECORD-ABBREV_708 https://fairsharing.org/FAIRsharing.5bbab9)  schema, which allows direct submission of transcriptomics data 
to the public database (URL_TO_INSERT_TERM_709 https://fairsharing.org/search?fairsharingRegistry=Database) s. Different approaches to assess the FAIR (URL_TO_INSERT_RECORD-ABBREV_710 https://fairsharing.org/FAIRsharing.WWI10U)  level of the dataset is also discussed.


## Sample metadata ETL pipeline

The ReSOLUTE datasets include 21 samples of seven cell lines. Each cell line has three replicates. The first draft of cell line metadata was first submitted to the NCBI SRA (URL_TO_INSERT_RECORD-ABBREV_716 https://fairsharing.org/FAIRsharing.g7t2hv)  database (URL_TO_INSERT_TERM_711 https://fairsharing.org/search?fairsharingRegistry=Database)  and stored in the NCBI BioSample (URL_TO_INSERT_RECORD-NAME_714 https://fairsharing.org/FAIRsharing.qr6pqk)  (URL_TO_INSERT_RECORD-ABBREV_715 https://fairsharing.org/FAIRsharing.qr6pqk)  database (URL_TO_INSERT_TERM_712 https://fairsharing.org/search?fairsharingRegistry=Database) . The raw sample metadata includes cell line name, provider and other administrative informat (URL_TO_INSERT_TERM_713 https://fairsharing.org/search?recordType=model_and_format) ion.

To avoid ambiguity and provide detailed cell line informat (URL_TO_INSERT_TERM_718 https://fairsharing.org/search?recordType=model_and_format) ion, the ReSOLUTE cell lines were linked to cell lines in the [Cellosaurus](https://web.expasy.org/cellosaurus/) database (URL_TO_INSERT_TERM_717 https://fairsharing.org/search?fairsharingRegistry=Database)  by the Cellosaurus (URL_TO_INSERT_RECORD-NAME_721 https://fairsharing.org/FAIRsharing.hkk309)  accession ID, for example, cell line “HCT 116” was linked to accession “CVCL_0291”. Cellosaurus (URL_TO_INSERT_RECORD-NAME_722 https://fairsharing.org/FAIRsharing.hkk309)  also provided enriched cell line informat (URL_TO_INSERT_TERM_719 https://fairsharing.org/search?recordType=model_and_format) ion, including disease, species of origin, cell line category. Such informat (URL_TO_INSERT_TERM_720 https://fairsharing.org/search?recordType=model_and_format) ion was fetched from the Cellosaurus (URL_TO_INSERT_RECORD-NAME_723 https://fairsharing.org/FAIRsharing.hkk309)  website and mapped to corresponding samples. 

Besides the cell line enriched cell line annotation, the ReSOLUTE Data Release Plan also specified the cell line provider, culturing conditions and quality control informat (URL_TO_INSERT_TERM_724 https://fairsharing.org/search?recordType=model_and_format) ion. Such informat (URL_TO_INSERT_TERM_725 https://fairsharing.org/search?recordType=model_and_format) ion is also added to the cell line. License informat (URL_TO_INSERT_TERM_726 https://fairsharing.org/search?recordType=model_and_format) ion was also mapped to the metadata.

The sample metadata can be found in the EBI Biosamples database (URL_TO_INSERT_TERM_727 https://fairsharing.org/search?fairsharingRegistry=Database)  with additional curation. For example, in sample [SAMN11893688](https://www.ebi.ac.uk/biosamples/samples/SAMN11893688), all missing values were omitted. Attribute cell line, organism, sex and tissue were mapped to ontologies (URL_TO_INSERT_TERM_729 https://fairsharing.org/search?recordType=terminology_artefact)  in the OLS (URL_TO_INSERT_RECORD-ABBREV_730 https://fairsharing.org/FAIRsharing.Mkl9RR)  database (URL_TO_INSERT_TERM_728 https://fairsharing.org/search?fairsharingRegistry=Database) . All curations can record can be found [here](https://www.ebi.ac.uk/biosamples/samples/SAMN11893688/curationlinks). 


## Transcriptomics data community standard

[Minimum Information about a high-throughput SEQuencing Experiment (MINSEQE)](http://fged.org/projects/minseqe/) is a recommended community standard (URL_TO_INSERT_TERM_731 https://fairsharing.org/search?fairsharingRegistry=Standard)  of transcriptomics data. It defines five elements of transcriptomics data that shall be harvested, including metadata, sequence read data, final processed data and experimental protocols. 

FAIRsharing (URL_TO_INSERT_RECORD-NAME_736 https://fairsharing.org/FAIRsharing.2abjs5)  organization interpreted the MINSEQE (URL_TO_INSERT_RECORD-ABBREV_734 https://fairsharing.org/FAIRsharing.a55z32)  guideline (URL_TO_INSERT_TERM_732 https://fairsharing.org/search?recordType=reporting_guideline) s and translated them into a machine-readable [MINSEQE recommended JSON schema](https://github.com/FAIRsharing/mircat/tree/master/minseqe). The FAIRsharing (URL_TO_INSERT_RECORD-NAME_737 https://fairsharing.org/FAIRsharing.2abjs5)  MINSEQE (URL_TO_INSERT_RECORD-ABBREV_735 https://fairsharing.org/FAIRsharing.a55z32)  JSON (URL_TO_INSERT_RECORD-ABBREV_733 https://fairsharing.org/FAIRsharing.5bbab9)  schema provided a framework of transcriptomics data. When it comes to different experiments, the actual data can be extended. [Here](https://raw.githubusercontent.com/ebi-ait/FAIRPlus/master/RESOLUTE/transcriptomics/data/RESOLUTE_transcriptomics_metadata_MINSEQE.json) is an example of ReSOLUTE transcriptomics data following this schema

One limitation of the FAIRsharing (URL_TO_INSERT_RECORD-NAME_745 https://fairsharing.org/FAIRsharing.2abjs5)  MINSEQE (URL_TO_INSERT_RECORD-ABBREV_741 https://fairsharing.org/FAIRsharing.a55z32)  schema is that it is incompatible to the submission standard (URL_TO_INSERT_TERM_738 https://fairsharing.org/search?fairsharingRegistry=Standard) s of popular transcriptomics database (URL_TO_INSERT_TERM_740 https://fairsharing.org/search?fairsharingRegistry=Database) s, like the European Nucleotide Archive (URL_TO_INSERT_RECORD-NAME_743 https://fairsharing.org/FAIRsharing.dj8nt8)  (ENA (URL_TO_INSERT_RECORD-ABBREV_744 https://fairsharing.org/FAIRsharing.dj8nt8) ). Transcriptomics data following the FAIRsharing (URL_TO_INSERT_RECORD-NAME_746 https://fairsharing.org/FAIRsharing.2abjs5)  MINSEQE (URL_TO_INSERT_RECORD-ABBREV_742 https://fairsharing.org/FAIRsharing.a55z32)  standard (URL_TO_INSERT_TERM_739 https://fairsharing.org/search?fairsharingRegistry=Standard)  must be modified to be submitted. 


````{dropdown}
:open:
```{figure} resolute.md-figure1.png
---
width: 500px    
name: resolute-figure1
alt: A visualization of the entities within the proposed transcriptomics schema.
---
A visualization of the entities within the proposed transcriptomics schema.
```
````

To solve this problem, we proposed a [transcriptomics schema](https://github.com/ebi-ait/FAIRPlus/tree/master/schemas/transcriptomics_schema) 
which follows the EBI Data Submission Portal (DSP) standard (URL_TO_INSERT_TERM_747 https://fairsharing.org/search?fairsharingRegistry=Standard) , as well as compatible with the MINSEQE (URL_TO_INSERT_RECORD-ABBREV_749 https://fairsharing.org/FAIRsharing.a55z32)  guideline (URL_TO_INSERT_TERM_748 https://fairsharing.org/search?recordType=reporting_guideline) s. T
he new transcriptomics schema is based on the MINSEQE (URL_TO_INSERT_RECORD-ABBREV_751 https://fairsharing.org/FAIRsharing.a55z32)  standard (URL_TO_INSERT_TERM_750 https://fairsharing.org/search?fairsharingRegistry=Standard) , also allows enriched sample, cell lines, 
project (URL_TO_INSERT_TERM_752 https://fairsharing.org/search?recordType=project)  metadata as different building blocks ({numref}`resolute-figure1`). 
This schema is compatible with the DSP schema which allows data validated against this schema to be directly submitted 
to the DSP and distributed to all related database (URL_TO_INSERT_TERM_753 https://fairsharing.org/search?fairsharingRegistry=Database) s. _(Note: This schema is still actively updated. Feedback welcomed)_


## FAIR assessment 

The level of “FAIRness” of the ReSOLUTE transcriptomics was first determined using the CMMI maturity model (URL_TO_INSERT_TERM_754 https://fairsharing.org/search?recordType=model_and_format)  described
[in this document.](https://docs.google.com/document/d/1URLfNpBYkCrICpizKZJ7NE29FddNNcoR0T0o_SQza7U/edit#heading=h.w0g0276fq5i6) 
The results of this first assessment can be found [here](https://docs.google.com/document/d/1Q_Su8kY9uNYfCV30jSIoWNdeV8GxA_DTGAcGOSZscQM/edit?usp=sharing). 
In a follow-up meeting, we defined actions that could be taken to increase the level for certain indicators
(see [this document](https://docs.google.com/document/d/1yYDcUvyXzYLfq9NZX23tbgIjCSOenSURjcRj61FMdzQ/edit?usp=sharing)).
These actions were defined within Github (URL_TO_INSERT_RECORD-NAME_755 https://fairsharing.org/FAIRsharing.c55d5e) .

A [new FAIRplus maturity model](https://docs.google.com/spreadsheets/d/11-jDoMbuxw8Nreurk7yKzk3EHJ54APAQnBl6VTKZPBk/edit#gid=1559176954) was set up, based on the RDA (URL_TO_INSERT_RECORD-ABBREV_756 https://fairsharing.org/FAIRsharing.2g5kcb)  indicators.
The focus was only on the indicators regarding Findability/Discoverability at that point. 
Before we could use this model (URL_TO_INSERT_TERM_757 https://fairsharing.org/search?recordType=model_and_format)  however, the indicators were updated within the RDA (URL_TO_INSERT_RECORD-ABBREV_758 https://fairsharing.org/FAIRsharing.2g5kcb)  initiative. 
We used their [new indicators](https://docs.google.com/spreadsheets/d/1mkjElFrTBPBH0QViODexNur0xNGhJqau0zkL4w8RRAw/edit?usp=sharing)
(for findability, v0.01) and their level definition to determine the levels for both the transcriptomics and proteomics datasets.
The results can be found [here](https://docs.google.com/spreadsheets/d/1abQ5_sOmBWbxAZhQVEUxQ_ybI1yTi0t-tJAVY5J5VY8/edit?usp=sharing).

In the meantime, an improved version of the RDA (URL_TO_INSERT_RECORD-ABBREV_759 https://fairsharing.org/FAIRsharing.2g5kcb)  indicators was released (v0.02). In the results document a comparison/mapping is made between v0.02 and v0.01 for possible future reference. \
We have updated the scoring for the transcriptomics data to this new version (v0.02).


*   Results of the scoring (to v0.01):
    *   transcriptomics data set (as in SRA (URL_TO_INSERT_RECORD-ABBREV_760 https://fairsharing.org/FAIRsharing.g7t2hv) )
        *   58% for the mandatory indicators
        *   63% for the recommended indicators
        *   4 indicators were thought to be not applicable
    *   proteomics data set (as in OwnCloud)
        *   42% for the mandatory indicators
        *   44% for the recommended indicators
        *   6 indicators were thought to be not applicable

The FAIRness level of the transcriptomics dataset for the HUH-7 cell line (as published on SRA (URL_TO_INSERT_RECORD-ABBREV_761 https://fairsharing.org/FAIRsharing.g7t2hv) ) was also determined
using the [FAIR evaluation services](https://fairsharing.github.io/FAIR-Evaluator-FrontEnd/#!/#%2F!) 
(an online evaluator) {footcite}`pmid26978244`,{footcite}`pmid31541130`. 

The result was that this dataset only passed for 3 out of the 22 indicators tested. 

This was, however, mainly due to the limitations of machine readability of the metadata and the license details within SRA (URL_TO_INSERT_RECORD-ABBREV_762 https://fairsharing.org/FAIRsharing.g7t2hv) . 

The complete results can be viewed <a href="https://fairsharing.github.io/FAIR-Evaluator-FrontEnd/#!/evaluations/170">here</a>. 


## Conclusion


1. Cellosaurus (URL_TO_INSERT_RECORD-NAME_764 https://fairsharing.org/FAIRsharing.hkk309)  accession number is recommended as an identifier (URL_TO_INSERT_TERM_763 https://fairsharing.org/search?recordType=identifier_schema)  for cell lines.
Cellosaurus (URL_TO_INSERT_RECORD-NAME_766 https://fairsharing.org/FAIRsharing.hkk309)  also provides enriched informat (URL_TO_INSERT_TERM_765 https://fairsharing.org/search?recordType=model_and_format) ion about different cell lines.
2. EBI BioSamples database (URL_TO_INSERT_TERM_767 https://fairsharing.org/search?fairsharingRegistry=Database)  is the master hosting platform for sample metadata, allowing curation and basic ontology (URL_TO_INSERT_TERM_768 https://fairsharing.org/search?recordType=terminology_artefact)  annotation. 
3. MINSEQE (URL_TO_INSERT_RECORD-ABBREV_770 https://fairsharing.org/FAIRsharing.a55z32)  is the recommended community standard (URL_TO_INSERT_TERM_769 https://fairsharing.org/search?fairsharingRegistry=Standard)  for transcriptomics data. 
4. A new transcriptomics schema was proposed which reflects the transcriptomics community guideline (URL_TO_INSERT_TERM_771 https://fairsharing.org/search?recordType=reporting_guideline) s 
and is supported by the EBI database (URL_TO_INSERT_TERM_772 https://fairsharing.org/search?fairsharingRegistry=Database)  submission platform.


## References
````{dropdown} **References**
```{footbibliography}
```
````


## Authors
````{authors_fairplus}
Fuqi: Writing - Original Draft
````

## License
````{license_fairplus}
CC-BY-4.0
````
