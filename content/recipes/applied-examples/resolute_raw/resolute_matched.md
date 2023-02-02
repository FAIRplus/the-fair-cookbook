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
    *   raw data: SRA (URL_TO_INSERT_RECORD_1437 https://fairsharing.org/FAIRsharing.g7t2hv)  [Transcriptomics]
    *   ProteomeXchange (URL_TO_INSERT_RECORD_1438 https://fairsharing.org/FAIRsharing.92dt9d)  (URL_TO_INSERT_RECORD_1439 https://fairsharing.org/FAIRsharing.92dt9d)  [Proteomics]
    *   Samples metadata: BioSample (URL_TO_INSERT_RECORD_1440 https://fairsharing.org/FAIRsharing.qr6pqk) s
*   Data standard (URL_TO_INSERT_TERM_1441 https://fairsharing.org/search?fairsharingRegistry=Standard) s
    *   Transcriptomics community standard (URL_TO_INSERT_TERM_1442 https://fairsharing.org/search?fairsharingRegistry=Standard) : [MINSEQE (URL_TO_INSERT_RECORD_1443 https://fairsharing.org/FAIRsharing.a55z32) ](http://fged.org/projects/minseqe/)
    *   Sample metadata schema: [BioSample (URL_TO_INSERT_RECORD_1447 https://fairsharing.org/FAIRsharing.qr6pqk) s JSO (URL_TO_INSERT_RECORD_1445 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_1444 https://fairsharing.org/FAIRsharing.5bbab9)  schema](https://github.com (URL_TO_INSERT_RECORD_1446 https://fairsharing.org/FAIRsharing.c55d5e) /EBIBioSamples/biosamples-v4/blob/dev/webapps/core/src/main/resources/schemas/core/sample.json)
    *   [Data submission portal](https://www.ebi.ac.uk/submission/) schema
*   FAIR (URL_TO_INSERT_RECORD_1449 https://fairsharing.org/FAIRsharing.WWI10U)  evaluation standard (URL_TO_INSERT_TERM_1448 https://fairsharing.org/search?fairsharingRegistry=Standard) : 
    *   [RDA (URL_TO_INSERT_RECORD_1450 https://fairsharing.org/FAIRsharing.2g5kcb)  FAIR (URL_TO_INSERT_RECORD_1452 https://fairsharing.org/FAIRsharing.WWI10U)  indicators](https://github.com (URL_TO_INSERT_RECORD_1451 https://fairsharing.org/FAIRsharing.c55d5e) /RDA-FAIR/FAIR-data-maturity-model-WG/tree/master/results%20of%20preliminary%20analysis)

This recipe provides an example of sample metadata extraction and curation practices, suggests a community standard (URL_TO_INSERT_TERM_1453 https://fairsharing.org/search?fairsharingRegistry=Standard)  for 
transcriptomics data and proposes a transcriptomics JSO (URL_TO_INSERT_RECORD_1455 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_1454 https://fairsharing.org/FAIRsharing.5bbab9)  schema, which allows direct submission of transcriptomics data 
to the public database (URL_TO_INSERT_TERM_1456 https://fairsharing.org/search?fairsharingRegistry=Database) s. Different approaches to assess the FAIR (URL_TO_INSERT_RECORD_1457 https://fairsharing.org/FAIRsharing.WWI10U)  level of the dataset is also discussed.


## Sample metadata ETL pipeline

The ReSO (URL_TO_INSERT_RECORD_1461 https://fairsharing.org/FAIRsharing.6bc7h9) LUTE datasets include 21 samples of seven cell lines. Each cell line has three replicates. The first draft of cell line metadata was first submitted to the NCBI SRA (URL_TO_INSERT_RECORD_1464 https://fairsharing.org/FAIRsharing.g7t2hv)  database (URL_TO_INSERT_TERM_1458 https://fairsharing.org/search?fairsharingRegistry=Database)  and stored in the NCBI BioSample (URL_TO_INSERT_RECORD_1462 https://fairsharing.org/FAIRsharing.qr6pqk)  (URL_TO_INSERT_RECORD_1463 https://fairsharing.org/FAIRsharing.qr6pqk)  database (URL_TO_INSERT_TERM_1459 https://fairsharing.org/search?fairsharingRegistry=Database) . The raw sample metadata includes cell line name, provider and other administrative informat (URL_TO_INSERT_TERM_1460 https://fairsharing.org/search?recordType=model_and_format) ion.

To avoid ambiguity and provide detailed cell line informat (URL_TO_INSERT_TERM_1466 https://fairsharing.org/search?recordType=model_and_format) ion, the ReSO (URL_TO_INSERT_RECORD_1469 https://fairsharing.org/FAIRsharing.6bc7h9) LUTE cell lines were linked to cell lines in the [Cellosaurus](https://web.expasy.org/cellosaurus/) database (URL_TO_INSERT_TERM_1465 https://fairsharing.org/search?fairsharingRegistry=Database)  by the Cellosaurus (URL_TO_INSERT_RECORD_1473 https://fairsharing.org/FAIRsharing.hkk309)  (URL_TO_INSERT_RECORD_1476 https://fairsharing.org/FAIRsharing.hkk309)  accession ID, for example, cell line “HCT 116” was linked to accession “CVCL (URL_TO_INSERT_RECORD_1470 https://fairsharing.org/FAIRsharing.j9y503) _0291”. Cellosaurus (URL_TO_INSERT_RECORD_1474 https://fairsharing.org/FAIRsharing.hkk309)  (URL_TO_INSERT_RECORD_1477 https://fairsharing.org/FAIRsharing.hkk309)  also provided enriched cell line informat (URL_TO_INSERT_TERM_1467 https://fairsharing.org/search?recordType=model_and_format) ion, including disease, species of origin, cell line category. Such informat (URL_TO_INSERT_TERM_1468 https://fairsharing.org/search?recordType=model_and_format) ion was fetched from the Cellosaurus (URL_TO_INSERT_RECORD_1475 https://fairsharing.org/FAIRsharing.hkk309)  (URL_TO_INSERT_RECORD_1478 https://fairsharing.org/FAIRsharing.hkk309)  website and map (URL_TO_INSERT_RECORD_1471 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_1472 https://fairsharing.org/FAIRsharing.31385c)  to corresponding samples. 

Besides the cell line enriched cell line annotation, the ReSO (URL_TO_INSERT_RECORD_1482 https://fairsharing.org/FAIRsharing.6bc7h9) LUTE Data Release Plan also specified the cell line provider, culturing conditions and quality control informat (URL_TO_INSERT_TERM_1479 https://fairsharing.org/search?recordType=model_and_format) ion. Such informat (URL_TO_INSERT_TERM_1480 https://fairsharing.org/search?recordType=model_and_format) ion is also added to the cell line. License informat (URL_TO_INSERT_TERM_1481 https://fairsharing.org/search?recordType=model_and_format) ion was also map (URL_TO_INSERT_RECORD_1483 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_1484 https://fairsharing.org/FAIRsharing.31385c)  to the metadata.

The sample metadata can be found in the EBI Biosamples database (URL_TO_INSERT_TERM_1485 https://fairsharing.org/search?fairsharingRegistry=Database)  with additional curation. For example, in sample [SAMN11893688](https://www.ebi.ac.uk/biosamples (URL_TO_INSERT_RECORD_1489 https://fairsharing.org/FAIRsharing.ewjdq6) /samples/SAMN11893688), all missing values were omitted. Attribute cell line, organism, sex and tissue were map (URL_TO_INSERT_RECORD_1491 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_1492 https://fairsharing.org/FAIRsharing.31385c)  to ontologies (URL_TO_INSERT_TERM_1487 https://fairsharing.org/search?recordType=terminology_artefact)  in the OLS (URL_TO_INSERT_RECORD_1488 https://fairsharing.org/FAIRsharing.Mkl9RR)  database (URL_TO_INSERT_TERM_1486 https://fairsharing.org/search?fairsharingRegistry=Database) . All curations can record can be found [here](https://www.ebi.ac.uk/biosamples (URL_TO_INSERT_RECORD_1490 https://fairsharing.org/FAIRsharing.ewjdq6) /samples/SAMN11893688/curationlinks). 


## Transcriptomics data community standard

[Minimum Informat (URL_TO_INSERT_TERM_1494 https://fairsharing.org/search?recordType=model_and_format) ion about a high-throughput SEQuencing Experiment (MINSEQE)](http://fged.org/projects/minseqe/) is a recommended community standard (URL_TO_INSERT_TERM_1493 https://fairsharing.org/search?fairsharingRegistry=Standard)  of transcriptomics data. It defines five elements of transcriptomics data that shall be harvested, including metadata, sequence read data, final processed data and experimental protocols. 

FAIR (URL_TO_INSERT_RECORD_1509 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_1505 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD_1507 https://fairsharing.org/FAIRsharing.2abjs5)  organization interpreted the MINSEQE (URL_TO_INSERT_RECORD_1496 https://fairsharing.org/FAIRsharing.a55z32)  guideline (URL_TO_INSERT_TERM_1495 https://fairsharing.org/search?recordType=reporting_guideline) s and translated them into a machine-readable [MINSEQE (URL_TO_INSERT_RECORD_1497 https://fairsharing.org/FAIRsharing.a55z32)  recommended JSO (URL_TO_INSERT_RECORD_1501 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_1499 https://fairsharing.org/FAIRsharing.5bbab9)  schema](https://github.com (URL_TO_INSERT_RECORD_1504 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRsharing/mircat/tree/master/minseqe). The FAIR (URL_TO_INSERT_RECORD_1510 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_1506 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD_1508 https://fairsharing.org/FAIRsharing.2abjs5)  MINSEQE (URL_TO_INSERT_RECORD_1498 https://fairsharing.org/FAIRsharing.a55z32)  JSO (URL_TO_INSERT_RECORD_1502 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_1500 https://fairsharing.org/FAIRsharing.5bbab9)  schema provided a framework of transcriptomics data. When it comes to different experiments, the actual data can be extended. [Here](https://raw.githubusercontent.com/ebi-ait/FAIRPlus/master/RESOLUTE/transcriptomics/data/RESOLUTE_transcriptomics_metadata_MINSEQE.json) is an example of ReSO (URL_TO_INSERT_RECORD_1503 https://fairsharing.org/FAIRsharing.6bc7h9) LUTE transcriptomics data following this schema

One limitation of the FAIR (URL_TO_INSERT_RECORD_1522 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_1518 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD_1520 https://fairsharing.org/FAIRsharing.2abjs5)  MINSEQE (URL_TO_INSERT_RECORD_1516 https://fairsharing.org/FAIRsharing.a55z32)  schema is that it is incompatible to the submission standard (URL_TO_INSERT_TERM_1511 https://fairsharing.org/search?fairsharingRegistry=Standard) s of popular transcriptomics database (URL_TO_INSERT_TERM_1513 https://fairsharing.org/search?fairsharingRegistry=Database) s, like the European Nucleotide Arch (URL_TO_INSERT_RECORD_1524 https://fairsharing.org/FAIRsharing.52b22c) ive (URL_TO_INSERT_RECORD_1514 https://fairsharing.org/FAIRsharing.dj8nt8)  (ENA (URL_TO_INSERT_RECORD_1515 https://fairsharing.org/FAIRsharing.dj8nt8) ). Transcriptomics data following the FAIR (URL_TO_INSERT_RECORD_1523 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_1519 https://fairsharing.org/FAIRsharing.2abjs5)  (URL_TO_INSERT_RECORD_1521 https://fairsharing.org/FAIRsharing.2abjs5)  MINSEQE (URL_TO_INSERT_RECORD_1517 https://fairsharing.org/FAIRsharing.a55z32)  standard (URL_TO_INSERT_TERM_1512 https://fairsharing.org/search?fairsharingRegistry=Standard)  must be modified to be submitted. 


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

To solve this problem, we proposed a [transcriptomics schema](https://github.com (URL_TO_INSERT_RECORD_1525 https://fairsharing.org/FAIRsharing.c55d5e) /ebi-ait/FAIRPlus/tree/master/schemas/transcriptomics_schema) 
which follows the EBI Data Submission Portal (DSP (URL_TO_INSERT_RECORD_1529 https://fairsharing.org/FAIRsharing.s63y3p) ) standard (URL_TO_INSERT_TERM_1526 https://fairsharing.org/search?fairsharingRegistry=Standard) , as well as compatible with the MINSEQE (URL_TO_INSERT_RECORD_1528 https://fairsharing.org/FAIRsharing.a55z32)  guideline (URL_TO_INSERT_TERM_1527 https://fairsharing.org/search?recordType=reporting_guideline) s. T
he new transcriptomics schema is based on the MINSEQE (URL_TO_INSERT_RECORD_1531 https://fairsharing.org/FAIRsharing.a55z32)  standard (URL_TO_INSERT_TERM_1530 https://fairsharing.org/search?fairsharingRegistry=Standard) , also allows enriched sample, cell lines, 
project (URL_TO_INSERT_TERM_1532 https://fairsharing.org/search?recordType=project)  metadata as different building blocks ({numref}`resolute-figure1`). 
This schema is compatible with the DSP (URL_TO_INSERT_RECORD_1533 https://fairsharing.org/FAIRsharing.s63y3p)  schema which allows data validated against this schema to be directly submitted 
to the DSP (URL_TO_INSERT_RECORD_1535 https://fairsharing.org/FAIRsharing.s63y3p)  and distributed to all related database (URL_TO_INSERT_TERM_1534 https://fairsharing.org/search?fairsharingRegistry=Database) s. _(Note: This schema is still actively updated. Feedback welcomed)_


## FAIR assessment 

The level of “FAIR (URL_TO_INSERT_RECORD_1538 https://fairsharing.org/FAIRsharing.WWI10U) ness” of the ReSO (URL_TO_INSERT_RECORD_1537 https://fairsharing.org/FAIRsharing.6bc7h9) LUTE transcriptomics was first determined using the CMMI maturity model (URL_TO_INSERT_TERM_1536 https://fairsharing.org/search?recordType=model_and_format)  described
[in this document.](https://docs.google.com/document/d/1URLfNpBYkCrICpizKZJ7NE29FddNNcoR0T0o_SQza7U/edit#heading=h.w0g0276fq5i6) 
The results of this first assessment can be found [here](https://docs.google.com/document/d/1Q_Su8kY9uNYfCV30jSIoWNdeV8GxA_DTGAcGOSZscQM/edit?usp=sharing). 
In a follow-up meeting, we defined actions that could be taken to increase the level for certain indicators
(see [this document](https://docs.google.com/document/d/1yYDcUvyXzYLfq9NZX23tbgIjCSOenSURjcRj61FMdzQ/edit?usp=sharing)).
These actions were defined within Github (URL_TO_INSERT_RECORD_1539 https://fairsharing.org/FAIRsharing.c55d5e) .

A [new FAIR (URL_TO_INSERT_RECORD_1541 https://fairsharing.org/FAIRsharing.WWI10U) plus maturity model](https://docs.google.com/spreadsheets/d/11-jDoMbuxw8Nreurk7yKzk3EHJ54APAQnBl6VTKZPBk/edit#gid=1559176954) was set up, based on the RDA (URL_TO_INSERT_RECORD_1540 https://fairsharing.org/FAIRsharing.2g5kcb)  indicators.
The focus was only on the indicators regarding Findability/Discoverability at that point. 
Before we could use this model (URL_TO_INSERT_TERM_1542 https://fairsharing.org/search?recordType=model_and_format)  however, the indicators were updated within the RDA (URL_TO_INSERT_RECORD_1543 https://fairsharing.org/FAIRsharing.2g5kcb)  initiative. 
We used their [new indicators](https://docs.google.com/spreadsheets/d/1mkjElFrTBPBH0QViODexNur0xNGhJqau0zkL4w8RRAw/edit?usp=sharing)
(for findability, v0.01) and their level definition to determine the levels for both the transcriptomics and proteomics datasets.
The results can be found [here](https://docs.google.com/spreadsheets/d/1abQ5_sOmBWbxAZhQVEUxQ_ybI1yTi0t-tJAVY5J5VY8/edit?usp=sharing).

In the meantime, an improved version of the RDA (URL_TO_INSERT_RECORD_1544 https://fairsharing.org/FAIRsharing.2g5kcb)  indicators was released (v0.02). In the results document a comparison/map (URL_TO_INSERT_RECORD_1545 https://fairsharing.org/FAIRsharing.53edcc) ping is made between v0.02 and v0.01 for possible future reference. \
We have updated the scoring for the transcriptomics data to this new version (v0.02).


*   Results of the scoring (to v0.01):
    *   transcriptomics data set (as in SRA (URL_TO_INSERT_RECORD_1546 https://fairsharing.org/FAIRsharing.g7t2hv) )
        *   58% for the mandatory indicators
        *   63% for the recommended indicators
        *   4 indicators were thought to be not applicable
    *   proteomics data set (as in OwnCloud)
        *   42% for the mandatory indicators
        *   44% for the recommended indicators
        *   6 indicators were thought to be not applicable

The FAIR (URL_TO_INSERT_RECORD_1547 https://fairsharing.org/FAIRsharing.WWI10U) ness level of the transcriptomics dataset for the HUH-7 cell line (as published on SRA (URL_TO_INSERT_RECORD_1548 https://fairsharing.org/FAIRsharing.g7t2hv) ) was also determined
using the [FAIR (URL_TO_INSERT_RECORD_1549 https://fairsharing.org/FAIRsharing.WWI10U)  evaluation services](https://fairsharing.github.io/FAIR-Evaluator-FrontEnd/#!/#%2F!) 
(an online evaluator) {footcite}`pmid26978244`,{footcite}`pmid31541130`. 

The result was that this dataset only passed for 3 out of the 22 indicators tested. 

This was, however, mainly due to the limitations of machine readability of the metadata and the license details within SRA (URL_TO_INSERT_RECORD_1550 https://fairsharing.org/FAIRsharing.g7t2hv) . 

The complete results can be viewed <a href="https://fairsharing.github.io/FAIR-Evaluator-FrontEnd/#!/evaluations/170">here</a>. 


## Conclusion


1. Cellosaurus (URL_TO_INSERT_RECORD_1552 https://fairsharing.org/FAIRsharing.hkk309)  (URL_TO_INSERT_RECORD_1553 https://fairsharing.org/FAIRsharing.hkk309)  accession number is recommended as an identifier (URL_TO_INSERT_TERM_1551 https://fairsharing.org/search?recordType=identifier_schema)  for cell lines.
Cellosaurus (URL_TO_INSERT_RECORD_1555 https://fairsharing.org/FAIRsharing.hkk309)  (URL_TO_INSERT_RECORD_1556 https://fairsharing.org/FAIRsharing.hkk309)  also provides enriched informat (URL_TO_INSERT_TERM_1554 https://fairsharing.org/search?recordType=model_and_format) ion about different cell lines.
2. EBI BioSample (URL_TO_INSERT_RECORD_1559 https://fairsharing.org/FAIRsharing.qr6pqk) s database (URL_TO_INSERT_TERM_1557 https://fairsharing.org/search?fairsharingRegistry=Database)  is the master hosting platform for sample metadata, allowing curation and basic ontology (URL_TO_INSERT_TERM_1558 https://fairsharing.org/search?recordType=terminology_artefact)  annotation. 
3. MINSEQE (URL_TO_INSERT_RECORD_1561 https://fairsharing.org/FAIRsharing.a55z32)  is the recommended community standard (URL_TO_INSERT_TERM_1560 https://fairsharing.org/search?fairsharingRegistry=Standard)  for transcriptomics data. 
4. A new transcriptomics schema was proposed which reflects the transcriptomics community guideline (URL_TO_INSERT_TERM_1562 https://fairsharing.org/search?recordType=reporting_guideline) s 
and is supported by the EBI database (URL_TO_INSERT_TERM_1563 https://fairsharing.org/search?fairsharingRegistry=Database)  submission platform.


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
