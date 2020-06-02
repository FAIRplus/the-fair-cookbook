<!---
title: 'UC9.3 Transcriptomics metadata'
tags:
  - FAIR cookbook
  - UC9
  - metadata
--->

# UC9.3 Transcriptomics metadata

[TOC]

## Main Objectives:

The main purpose of this recipe is:

> To provide guidance on the minimum set of metadata and semantics required to describe any transcriptomics experiments, from standard case-control to dosage-response designs, and from microarrays to single cell RNA sequencing. 


### Who is this recipe aimed at?

This document is aimed at anyone interested in the metadata, and specifically the ontology annotations, required to capture variables and experimental factors related to a transcriptomics experiment. General knowledge of transcriptomics experiments would be beneficial. No specific technical knowledge is required.



___

## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Interoperability | minimal | repeatable |

___

## Transcriptomics Data model 

Large sections of any transcriptomics data model are not unique to transcriptomics experiments but are common to a wide range of experiments in the biomedical domain. This includes general project- and sample-level information, which will be briefly covered in this recipe but will also be covered in more depth elsewhere.

Where possible, metadata should be mapped to ontologies to maximise the FAIRness of any dataset. This recipe will suggest possible ontologies for metadata fields where these are available. These lists may however not be exhaustive as new ontologies emerge regularly.

### Existing standards and checklists

A set of well-established standards and minimum metadata checklists exist for various aspects of transcriptomics. They include:

Minimum Information About a Microarray Experiment (MIAME) - MIAME is intended to specify all the information necessary for an unambiguous interpretation of a microarray experiment, and potentially to reproduce it. MIAME defines the content but not the format for this information. The MIAME standard has been in existence for over 20 years and has been widely adopted across the scientific community. The data models of the major transcriptomics repositories such as ArrayExpress, the Expression Atlas and the Gene Expression Omnibus (GEO) are MIAME-compliant.

Minimum Information about a high-throughput nucleotide SEQuencing Experiment (MINSEQE) - MINSEQE describes the minimum metadata that is needed to enable the unambiguous interpretation and facilitate reproduction of the results of the experiment. By analogy to the MIAME guidelines for microarray experiments, adherence to the MINSEQE guidelines will improve integration of multiple experiments across different modalities, thereby maximising the value of high-throughput research. MINSEQE has been integrated into a number of transcriptomics and sequencing archives.

Functional Annotation of Animal Genomes (FAANG) - FAANG provides a set of orthogonal standards for the capture of well-structured metadata for experiments, samples and analyses in the animal genomics domain. The FAANG standards support the MIAME and MINSEQE guidelines, and aim to convert them to a concrete specification.

Human Cell Atlas Metadata (HCA-Metadata) - the HCA metadata model provides a concrete specification for capturing the metadata for single cell sequencing experiments. It is based on the three standards above, while focusing on the specific requirements of the single cell space.

### Minimum metadata vs desirable metadata

A minimum metadata set constitutes metadata items that always need to be supplied with any experimental data. For validation purposes, these should not be omittable. Desirable or recommended metadata items on the other hand should be supplied if available but will not cause a validation failure if absent. 

### Common metadata

Common metadata include any information that is not specific to transcriptomics experiments but applies to most experiments in the biomedical domain. They include:

- Project level metadata
- Common sample level metadata such as species, tissue, cell type etc.


#### Suggested metadata fields

The following table contains a non-exhaustive list of suggested minimum metadata fields for biological samples. The collection is based on a range of existing metadata standards, including MIAME, MINSEQE, FAANG and HCA. Fields were included if they occurred in at least two of the standards.

|Metadata field|Required|Comment|
|--------|--------|--------|
|unique ID|required||
|sample type|required|ontology field - eg OBI or EFO|
|species|required|ontolofy field - NCBITaxonomy|
|tissue/organism part|required|ontology field - eg Uberon|
|disease|required|ontology field - eg MONDO or DO|
|sex|required|ontology field - eg PATO|
|development stage|required|ontology field - eg Uberon or Hsadpdv; species dependent|
|collection date|required||
|external accessions|recommended|eg Biosamples, Biostudies|
|strain|recommended|ontology field - eg NCBITaxonomy|
|ancestry/ethnicity|recommended|ontology field - eg HANCESTRO|
|age |recommended||
|age unit|recommended|ontology field - eg UO|
|BMI|recommended||
|treatment category|recommended|ontology field - eg OBI, NCIt or OGMS|
|cell type|recommended|ontology field - eg CL|
|growth conditions|recommended||
|strain|recommended|ontology field - species dependent|
|genetic variation|recommended||
|sample collection technique|recommended|ontology field - eg EFO or OBI|
|phenotype|recommended|ontology field - eg HP or MP; species dependent|
|cell cycle|recommended|ontology field - eg GO|
|cell location|recommended|ontology field - eg GO|


### Assay metadata

Assay-level metadata covers any metadata directly related to the preparation of the biomaterial undergoing the assay and the process of performing the assay. Most, though not all, of this metadata is specific to transcriptomics. Examples include:
- Library information, including what sample the library was originally derived from and whether any replicates are biological or technical
- Process (wet experiment) metadata
- Technology type (e.g. bulk RNA-Seq, scRNA-Seq, CITE-Seq)
- Instrument metadata
- Other assay-specific metadata
- QC information
- Workflow metadata

#### Suggested metadata fields

The following table contains a non-exhaustive list of suggested minimum metadata fields for assays. The collection is based on a range of existing metadata standards, including MIAME, MINSEQE and HCA. This list can and should be further broken down based on specific technologies used, such as microarrays or whole genome sequencing.

|Metadata field|Required|Comment|
|--------|--------|--------|
|unique ID|required||
|experiment type|required|ontology field - eg EFO or OBI|
|extracted nucleic acid/material type|required|ontology field - eg ChEBI or EFO|
|platform|required|ontology field - eg EFO or OBI|
|instrument model|required|ontology field - eg EFO or OBI|
|nucleic acid extraction method|required|ontology field - eg EFO or OBI|
|cDNA library amplication method|required|ontology field - eg EFO or OBI|
|array or sequencing method|required|ontology field - eg EFO or OBI|
|biological or technical replicate|required|boolean or CV|
|end bias|required|standardised field or ontology|
|external accessions|recommended|eg protocols.io, AE|
|assay start time|recommended||
|assay end time|recommended||
|assay duration|recommended||
|array quality|recommended||
|cell quality|recommended||
|chemical compound|recommended|ontology field - eg ChEBI|
|labeling molecule used|recommended|ontology field - eg ChEBI|
|spike-in kit used|recommended||
|cDNA primer|recommended|standardised field or ontology|
|library strandedness|recommended|standardised field or ontology|
|cell quality|recommended|standardised field or ontology|
|cell barcode|recommended||
|UMI barcode|recommended||

### Analysis metadata

Analysis-level metadata includes any metadata related to the files that come out of the experiment, from the sequencing or imaging files generated directly by the machine to files generated during the various stages of processing and analysis, as well as details of any analyses performed. It is very important to always capture versions of software and reference genomes used in order to allow accurate replication of results. Analysis metadata includes
- Type of analysis
- File formats, e.g. BAM, fastq or gene count
- File location e.g. URL
- Summarisation of data, e.g. enrichment analysis

#### Suggested metadata fields

The following table contains a non-exhaustive list of suggested minimum metadata fields for analyses. The collection is based on a range of existing metadata standards, including MIAME, MINSEQE and HCA. This list can and should be further broken down based on the specific analysis type (primary, secondary or teriatry analysis, meta-analysis etc)

|Metadata field|Required|Comment|
|--------|--------|--------|
|analysis type|required|ontology field - eg EFO, OBI or EDAM|
|computational method|required|ontology field - eg EFO or EDAM|
|normalisation strategy|required|ontology field - eg EFO or EDAM|
|file format|required|ontology field - eg EDAM|
|file storage location|required||
|software package|recommended||
|software version|recommended||
|analysis date|recommended||
|read index|recommended||
|read length|recommended||
|assembly type|recommended||
|reference genome version|recommended||

## Ontologies for transcriptomics data

While it is essential that any transcriptomics metadata be annotated with ontology terms wherever possible, there is no absolute set of ontologies that must be used above all others. There is however a consensus set of ontologies and other standardised resources that are commonly used in transcriptomics metadata, including in the main data archives. The most commonly used ontologies and fields they apply to are listed below. This table represents an absolute minimum of ontology annotations that should be included in a transcriptomics metadata set for it to be considered as FAIR. Not all fields suggested for ontology annotation in the previous section are repeated here for this reason.

|Data type|Ontology/Entity sources|Type|Notes|
|---|---|---|---|
|Species |NCBI taxonomy Scientific name + ID|Ontology||
|Tissue |Uberon term and Id|Ontology||
|Cell type| CL term and Id|Ontology||
|Disease|MONDO, DO or MeSH|Ontology|no single solution - options vary depending on resource and individual requirements |
|Phenotype/Trait|HPO (human),  MP(other mammals), various others for model organisms (yeast, zebrafish, Xenopus, C. elegans)|Ontology||
|Experiment Type|EFO, OBI|Ontology| e.g. RNASeq, CITESeq etc. - |
|Cell location/cycle| GO|Ontology||
|Developmental stage|HSAPDV/Uberon|Ontology||
|Chemical compound| ChEBI|Ontology||
|Chemical compound| UniChem, SMILE, InChi|Entity||
|Gene/protein|ENSEMBL, ENTREZ_GENE, UNIPROT, HGNC ID, INSDC|Entity||
|Metabolites| MetaboLights compound accession, ChEBI|Entity||
|Nucleotide reference sequence|ReqSeq|Entity||


## Summary

Using common transcriptomics metadata standards, in particular the fields listed above as guidance, it is possible to easily define a comprehensive metadata template to capture all the experimental variables to describe any transcriptomics experiment in a FAIR-compliant way. A generic step-by-step guide for designing a metadata template is provided [here](creating-minimal-metadata-profiles.md)

___



## Authors:

| Name | Affiliation  | Orcid | Credit role  |
| :------------- | :------------- | :------------- |:------------- |
| Danielle Welter |  LCSB, University of Luxembourg| [0000-0003-1058-2668](https://orcid.org/orcid.org/0000-0003-1058-2668) | Writing - Original Draft |
|Karsten Quast|||
|Peter Woollard|||


___


## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>