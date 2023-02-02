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
    *   raw data: SRA (URL_TO_INSERT_RECORD_942 https://fairsharing.org/FAIRsharing.g7t2hv)  [Transcriptomics]
    *   ProteomeXchange (URL_TO_INSERT_RECORD_943 https://fairsharing.org/FAIRsharing.92dt9d)  [Proteomics]
    *   Samples metadata: BioSample (URL_TO_INSERT_RECORD_944 https://fairsharing.org/FAIRsharing.qr6pqk) s
*   Data standard (URL_TO_INSERT_TERM_945 https://fairsharing.org/search?fairsharingRegistry=Standard) s
    *   Transcriptomics community standard (URL_TO_INSERT_TERM_946 https://fairsharing.org/search?fairsharingRegistry=Standard) : [MINSEQE](http://fged.org/projects/minseqe/)
    *   Sample metadata schema: [BioSamples JSON schema](https://github.com/EBIBioSamples/biosamples-v4/blob/dev/webapps/core/src/main/resources/schemas/core/sample.json)
    *   [Data submission portal](https://www.ebi.ac.uk/submission/) schema
*   FAIR (URL_TO_INSERT_RECORD_948 https://fairsharing.org/FAIRsharing.WWI10U)  evaluation standard (URL_TO_INSERT_TERM_947 https://fairsharing.org/search?fairsharingRegistry=Standard) : 
    *   [RDA FAIR indicators](https://github.com/RDA-FAIR/FAIR-data-maturity-model-WG/tree/master/results%20of%20preliminary%20analysis)

This recipe provides an example of sample metadata extraction and curation practices, suggests a community standard (URL_TO_INSERT_TERM_949 https://fairsharing.org/search?fairsharingRegistry=Standard)  for 
transcriptomics data and proposes a transcriptomics JSON (URL_TO_INSERT_RECORD_950 https://fairsharing.org/FAIRsharing.5bbab9)  schema, which allows direct submission of transcriptomics data 
to the public database (URL_TO_INSERT_TERM_951 https://fairsharing.org/search?fairsharingRegistry=Database) s. Different approaches to assess the FAIR (URL_TO_INSERT_RECORD_952 https://fairsharing.org/FAIRsharing.WWI10U)  level of the dataset is also discussed.


## Sample metadata ETL pipeline

The ReSOLUTE datasets include 21 samples of seven cell lines. Each cell line has three replicates. The first draft of cell line metadata was first submitted to the NCBI SRA (URL_TO_INSERT_RECORD_958 https://fairsharing.org/FAIRsharing.g7t2hv)  database (URL_TO_INSERT_TERM_953 https://fairsharing.org/search?fairsharingRegistry=Database)  and stored in the NCBI BioSample (URL_TO_INSERT_RECORD_956 https://fairsharing.org/FAIRsharing.qr6pqk)  (URL_TO_INSERT_RECORD_957 https://fairsharing.org/FAIRsharing.qr6pqk)  database (URL_TO_INSERT_TERM_954 https://fairsharing.org/search?fairsharingRegistry=Database) . The raw sample metadata includes cell line name, provider and other administrative informat (URL_TO_INSERT_TERM_955 https://fairsharing.org/search?recordType=model_and_format) ion.

To avoid ambiguity and provide detailed cell line informat (URL_TO_INSERT_TERM_960 https://fairsharing.org/search?recordType=model_and_format) ion, the ReSOLUTE cell lines were linked to cell lines in the [Cellosaurus](https://web.expasy.org/cellosaurus/) database (URL_TO_INSERT_TERM_959 https://fairsharing.org/search?fairsharingRegistry=Database)  by the Cellosaurus (URL_TO_INSERT_RECORD_965 https://fairsharing.org/FAIRsharing.hkk309)  accession ID, for example, cell line “HCT 116” was linked to accession “CVCL_0291”. Cellosaurus (URL_TO_INSERT_RECORD_966 https://fairsharing.org/FAIRsharing.hkk309)  also provided enriched cell line informat (URL_TO_INSERT_TERM_961 https://fairsharing.org/search?recordType=model_and_format) ion, including disease, species of origin, cell line category. Such informat (URL_TO_INSERT_TERM_962 https://fairsharing.org/search?recordType=model_and_format) ion was fetched from the Cellosaurus (URL_TO_INSERT_RECORD_967 https://fairsharing.org/FAIRsharing.hkk309)  website and map (URL_TO_INSERT_RECORD_963 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_964 https://fairsharing.org/FAIRsharing.31385c)  to corresponding samples. 

Besides the cell line enriched cell line annotation, the ReSOLUTE Data Release Plan also specified the cell line provider, culturing conditions and quality control informat (URL_TO_INSERT_TERM_968 https://fairsharing.org/search?recordType=model_and_format) ion. Such informat (URL_TO_INSERT_TERM_969 https://fairsharing.org/search?recordType=model_and_format) ion is also added to the cell line. License informat (URL_TO_INSERT_TERM_970 https://fairsharing.org/search?recordType=model_and_format) ion was also map (URL_TO_INSERT_RECORD_971 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_972 https://fairsharing.org/FAIRsharing.31385c)  to the metadata.

The sample metadata can be found in the EBI Biosamples database (URL_TO_INSERT_TERM_973 https://fairsharing.org/search?fairsharingRegistry=Database)  with additional curation. For example, in sample [SAMN11893688](https://www.ebi.ac.uk/biosamples/samples/SAMN11893688), all missing values were omitted. Attribute cell line, organism, sex and tissue were map (URL_TO_INSERT_RECORD_977 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_978 https://fairsharing.org/FAIRsharing.31385c)  to ontologies (URL_TO_INSERT_TERM_975 https://fairsharing.org/search?recordType=terminology_artefact)  in the OLS (URL_TO_INSERT_RECORD_976 https://fairsharing.org/FAIRsharing.Mkl9RR)  database (URL_TO_INSERT_TERM_974 https://fairsharing.org/search?fairsharingRegistry=Database) . All curations can record can be found [here](https://www.ebi.ac.uk/biosamples/samples/SAMN11893688/curationlinks). 


## Transcriptomics data community standard

[Minimum Information about a high-throughput SEQuencing Experiment (MINSEQE)](http://fged.org/projects/minseqe/) is a recommended community standard (URL_TO_INSERT_TERM_979 https://fairsharing.org/search?fairsharingRegistry=Standard)  of transcriptomics data. It defines five elements of transcriptomics data that shall be harvested, including metadata, sequence read data, final processed data and experimental protocols. 

FAIR (URL_TO_INSERT_RECORD_986 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_984 https://fairsharing.org/FAIRsharing.2abjs5)  organization interpreted the MINSEQE (URL_TO_INSERT_RECORD_981 https://fairsharing.org/FAIRsharing.a55z32)  guideline (URL_TO_INSERT_TERM_980 https://fairsharing.org/search?recordType=reporting_guideline) s and translated them into a machine-readable [MINSEQE recommended JSON schema](https://github.com/FAIRsharing/mircat/tree/master/minseqe). The FAIR (URL_TO_INSERT_RECORD_987 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_985 https://fairsharing.org/FAIRsharing.2abjs5)  MINSEQE (URL_TO_INSERT_RECORD_982 https://fairsharing.org/FAIRsharing.a55z32)  JSON (URL_TO_INSERT_RECORD_983 https://fairsharing.org/FAIRsharing.5bbab9)  schema provided a framework of transcriptomics data. When it comes to different experiments, the actual data can be extended. [Here](https://raw.githubusercontent.com/ebi-ait/FAIRPlus/master/RESOLUTE/transcriptomics/data/RESOLUTE_transcriptomics_metadata_MINSEQE.json) is an example of ReSOLUTE transcriptomics data following this schema

One limitation of the FAIR (URL_TO_INSERT_RECORD_996 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_994 https://fairsharing.org/FAIRsharing.2abjs5)  MINSEQE (URL_TO_INSERT_RECORD_992 https://fairsharing.org/FAIRsharing.a55z32)  schema is that it is incompatible to the submission standard (URL_TO_INSERT_TERM_988 https://fairsharing.org/search?fairsharingRegistry=Standard) s of popular transcriptomics database (URL_TO_INSERT_TERM_990 https://fairsharing.org/search?fairsharingRegistry=Database) s, like the European Nucleotide Arch (URL_TO_INSERT_RECORD_998 https://fairsharing.org/FAIRsharing.52b22c) ive (URL_TO_INSERT_RECORD_991 https://fairsharing.org/FAIRsharing.dj8nt8)  (ENA). Transcriptomics data following the FAIR (URL_TO_INSERT_RECORD_997 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_995 https://fairsharing.org/FAIRsharing.2abjs5)  MINSEQE (URL_TO_INSERT_RECORD_993 https://fairsharing.org/FAIRsharing.a55z32)  standard (URL_TO_INSERT_TERM_989 https://fairsharing.org/search?fairsharingRegistry=Standard)  must be modified to be submitted. 


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
which follows the EBI Data Submission Portal (DSP) standard (URL_TO_INSERT_TERM_999 https://fairsharing.org/search?fairsharingRegistry=Standard) , as well as compatible with the MINSEQE (URL_TO_INSERT_RECORD_1001 https://fairsharing.org/FAIRsharing.a55z32)  guideline (URL_TO_INSERT_TERM_1000 https://fairsharing.org/search?recordType=reporting_guideline) s. T
he new transcriptomics schema is based on the MINSEQE (URL_TO_INSERT_RECORD_1003 https://fairsharing.org/FAIRsharing.a55z32)  standard (URL_TO_INSERT_TERM_1002 https://fairsharing.org/search?fairsharingRegistry=Standard) , also allows enriched sample, cell lines, 
project (URL_TO_INSERT_TERM_1004 https://fairsharing.org/search?recordType=project)  metadata as different building blocks ({numref}`resolute-figure1`). 
This schema is compatible with the DSP schema which allows data validated against this schema to be directly submitted 
to the DSP and distributed to all related database (URL_TO_INSERT_TERM_1005 https://fairsharing.org/search?fairsharingRegistry=Database) s. _(Note: This schema is still actively updated. Feedback welcomed)_


## FAIR assessment 

The level of “FAIR (URL_TO_INSERT_RECORD_1007 https://fairsharing.org/FAIRsharing.WWI10U) ness” of the ReSOLUTE transcriptomics was first determined using the CMMI maturity model (URL_TO_INSERT_TERM_1006 https://fairsharing.org/search?recordType=model_and_format)  described
[in this document.](https://docs.google.com/document/d/1URLfNpBYkCrICpizKZJ7NE29FddNNcoR0T0o_SQza7U/edit#heading=h.w0g0276fq5i6) 
The results of this first assessment can be found [here](https://docs.google.com/document/d/1Q_Su8kY9uNYfCV30jSIoWNdeV8GxA_DTGAcGOSZscQM/edit?usp=sharing). 
In a follow-up meeting, we defined actions that could be taken to increase the level for certain indicators
(see [this document](https://docs.google.com/document/d/1yYDcUvyXzYLfq9NZX23tbgIjCSOenSURjcRj61FMdzQ/edit?usp=sharing)).
These actions were defined within Github (URL_TO_INSERT_RECORD_1008 https://fairsharing.org/FAIRsharing.c55d5e) .

A [new FAIRplus maturity model](https://docs.google.com/spreadsheets/d/11-jDoMbuxw8Nreurk7yKzk3EHJ54APAQnBl6VTKZPBk/edit#gid=1559176954) was set up, based on the RDA (URL_TO_INSERT_RECORD_1009 https://fairsharing.org/FAIRsharing.2g5kcb)  indicators.
The focus was only on the indicators regarding Findability/Discoverability at that point. 
Before we could use this model (URL_TO_INSERT_TERM_1010 https://fairsharing.org/search?recordType=model_and_format)  however, the indicators were updated within the RDA (URL_TO_INSERT_RECORD_1011 https://fairsharing.org/FAIRsharing.2g5kcb)  initiative. 
We used their [new indicators](https://docs.google.com/spreadsheets/d/1mkjElFrTBPBH0QViODexNur0xNGhJqau0zkL4w8RRAw/edit?usp=sharing)
(for findability, v0.01) and their level definition to determine the levels for both the transcriptomics and proteomics datasets.
The results can be found [here](https://docs.google.com/spreadsheets/d/1abQ5_sOmBWbxAZhQVEUxQ_ybI1yTi0t-tJAVY5J5VY8/edit?usp=sharing).

In the meantime, an improved version of the RDA (URL_TO_INSERT_RECORD_1012 https://fairsharing.org/FAIRsharing.2g5kcb)  indicators was released (v0.02). In the results document a comparison/map (URL_TO_INSERT_RECORD_1013 https://fairsharing.org/FAIRsharing.53edcc) ping is made between v0.02 and v0.01 for possible future reference. \
We have updated the scoring for the transcriptomics data to this new version (v0.02).


*   Results of the scoring (to v0.01):
    *   transcriptomics data set (as in SRA (URL_TO_INSERT_RECORD_1014 https://fairsharing.org/FAIRsharing.g7t2hv) )
        *   58% for the mandatory indicators
        *   63% for the recommended indicators
        *   4 indicators were thought to be not applicable
    *   proteomics data set (as in OwnCloud)
        *   42% for the mandatory indicators
        *   44% for the recommended indicators
        *   6 indicators were thought to be not applicable

The FAIR (URL_TO_INSERT_RECORD_1015 https://fairsharing.org/FAIRsharing.WWI10U) ness level of the transcriptomics dataset for the HUH-7 cell line (as published on SRA (URL_TO_INSERT_RECORD_1016 https://fairsharing.org/FAIRsharing.g7t2hv) ) was also determined
using the [FAIR evaluation services](https://fairsharing.github.io/FAIR-Evaluator-FrontEnd/#!/#%2F!) 
(an online evaluator) {footcite}`pmid26978244`,{footcite}`pmid31541130`. 

The result was that this dataset only passed for 3 out of the 22 indicators tested. 

This was, however, mainly due to the limitations of machine readability of the metadata and the license details within SRA (URL_TO_INSERT_RECORD_1017 https://fairsharing.org/FAIRsharing.g7t2hv) . 

The complete results can be viewed <a href="https://fairsharing.github.io/FAIR-Evaluator-FrontEnd/#!/evaluations/170">here</a>. 


## Conclusion


1. Cellosaurus (URL_TO_INSERT_RECORD_1019 https://fairsharing.org/FAIRsharing.hkk309)  accession number is recommended as an identifier (URL_TO_INSERT_TERM_1018 https://fairsharing.org/search?recordType=identifier_schema)  for cell lines.
Cellosaurus (URL_TO_INSERT_RECORD_1021 https://fairsharing.org/FAIRsharing.hkk309)  also provides enriched informat (URL_TO_INSERT_TERM_1020 https://fairsharing.org/search?recordType=model_and_format) ion about different cell lines.
2. EBI BioSample (URL_TO_INSERT_RECORD_1024 https://fairsharing.org/FAIRsharing.qr6pqk) s database (URL_TO_INSERT_TERM_1022 https://fairsharing.org/search?fairsharingRegistry=Database)  is the master hosting platform for sample metadata, allowing curation and basic ontology (URL_TO_INSERT_TERM_1023 https://fairsharing.org/search?recordType=terminology_artefact)  annotation. 
3. MINSEQE (URL_TO_INSERT_RECORD_1026 https://fairsharing.org/FAIRsharing.a55z32)  is the recommended community standard (URL_TO_INSERT_TERM_1025 https://fairsharing.org/search?fairsharingRegistry=Standard)  for transcriptomics data. 
4. A new transcriptomics schema was proposed which reflects the transcriptomics community guideline (URL_TO_INSERT_TERM_1027 https://fairsharing.org/search?recordType=reporting_guideline) s 
and is supported by the EBI database (URL_TO_INSERT_TERM_1028 https://fairsharing.org/search?fairsharingRegistry=Database)  submission platform.


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
