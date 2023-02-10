(fcb-interop-txmetadata)=
# Metadata profile for transcriptomics


````{panels_fairplus}
:identifier_text: FCB027
:identifier_link: 'https://w3id.org/faircookbook/FCB027'
:difficulty_level: 3
:recipe_type: guidance
:reading_time_minutes: 30
:intended_audience: principal_investigator, data_manager, terminology_manager, data_scientist, ontologist 
:maturity_level: 3
:maturity_indicator: 30
:has_executable_code: nope
:recipe_name: Outlining a metadata profile for transcriptomics
```` 

## Main Objectives:

The main purpose of this recipe is:

> To provide guidance on the minimum set of metadata and semantics required to describe any transcriptomics experiments,
> from standard (URL_TO_INSERT_TERM_4714 https://fairsharing.org/search?fairsharingRegistry=Standard)  case-control to dosage-response designs, and from microarrays to single cell RNA sequencing. 


### Who is this recipe aimed at?

This document is aimed at anyone interested in the metadata, and specifically the ontology (URL_TO_INSERT_TERM_4715 https://fairsharing.org/search?recordType=terminology_artefact)  annotations, required to capture variables and experimental factors related to a transcriptomics experiment. General knowledge of transcriptomics experiments would be beneficial. No specific technical knowledge is required.


---

## Transcriptomics Data model 

Large sections of any transcriptomics data model (URL_TO_INSERT_TERM_4717 https://fairsharing.org/search?recordType=model_and_format)  are not unique to transcriptomics experiments but are common to a wide range of experiments in the biomedical domain. This includes general project (URL_TO_INSERT_TERM_4716 https://fairsharing.org/search?recordType=project) - and sample-level informat (URL_TO_INSERT_TERM_4718 https://fairsharing.org/search?recordType=model_and_format) ion, which will be briefly covered in this recipe but will also be covered in more depth elsewhere.

Where possible, metadata should be mapped to ontologies (URL_TO_INSERT_TERM_4719 https://fairsharing.org/search?recordType=terminology_artefact)  to maximise the FAIRness of any dataset. This recipe will suggest possible ontologies (URL_TO_INSERT_TERM_4720 https://fairsharing.org/search?recordType=terminology_artefact)  for metadata fields where these are available. These lists may however not be exhaustive as new ontologies (URL_TO_INSERT_TERM_4721 https://fairsharing.org/search?recordType=terminology_artefact)  emerge regularly.

### Existing standards and checklists

A set of well-established standard (URL_TO_INSERT_TERM_4722 https://fairsharing.org/search?fairsharingRegistry=Standard) s and minimum metadata checklists exist for various aspects of transcriptomics. They include:

Minimum Informat (URL_TO_INSERT_TERM_4726 https://fairsharing.org/search?recordType=model_and_format) ion About a Microarray Experiment (URL_TO_INSERT_RECORD-NAME_4734 https://fairsharing.org/FAIRsharing.32b10v)  (MIAME (URL_TO_INSERT_RECORD-ABBREV_4735 https://fairsharing.org/FAIRsharing.32b10v) ) - MIAME (URL_TO_INSERT_RECORD-ABBREV_4736 https://fairsharing.org/FAIRsharing.32b10v)  is intended to specify all the informat (URL_TO_INSERT_TERM_4727 https://fairsharing.org/search?recordType=model_and_format) ion necessary for an unambiguous interpretation of a microarray experiment, and potentially to reproduce it. MIAME (URL_TO_INSERT_RECORD-ABBREV_4737 https://fairsharing.org/FAIRsharing.32b10v)  defines the content but not the format (URL_TO_INSERT_TERM_4728 https://fairsharing.org/search?recordType=model_and_format)  for this informat (URL_TO_INSERT_TERM_4729 https://fairsharing.org/search?recordType=model_and_format) ion. The MIAME (URL_TO_INSERT_RECORD-ABBREV_4738 https://fairsharing.org/FAIRsharing.32b10v)  standard (URL_TO_INSERT_TERM_4723 https://fairsharing.org/search?fairsharingRegistry=Standard)  has been in existence for over 20 years and has been widely adopted across the scientific community. The data model (URL_TO_INSERT_TERM_4725 https://fairsharing.org/search?recordType=model_and_format) s of the major transcriptomics repositories (URL_TO_INSERT_TERM_4724 https://fairsharing.org/search?recordType=repository)  such as ArrayExpress (URL_TO_INSERT_RECORD-NAME_4732 https://fairsharing.org/FAIRsharing.6k0kwd) , the Expression Atlas (URL_TO_INSERT_RECORD-NAME_4740 https://fairsharing.org/FAIRsharing.f5zx00)  and the Gene Expression Omnibus (URL_TO_INSERT_RECORD-NAME_4730 https://fairsharing.org/FAIRsharing.5hc8vt)  (GEO (URL_TO_INSERT_RECORD-ABBREV_4731 https://fairsharing.org/FAIRsharing.5hc8vt)  (URL_TO_INSERT_RECORD-ABBREV_4733 https://fairsharing.org/FAIRsharing.27rndz) ) are MIAME (URL_TO_INSERT_RECORD-ABBREV_4739 https://fairsharing.org/FAIRsharing.32b10v) -compliant.

Minimum Informat (URL_TO_INSERT_TERM_4741 https://fairsharing.org/search?recordType=model_and_format) ion about a high-throughput nucleotide SEQuencing Experiment (MINSEQE (URL_TO_INSERT_RECORD-ABBREV_4744 https://fairsharing.org/FAIRsharing.a55z32) ) - MINSEQE (URL_TO_INSERT_RECORD-ABBREV_4745 https://fairsharing.org/FAIRsharing.a55z32)  describes the minimum metadata that is needed to enable the unambiguous interpretation and facilitate reproduction of the results of the experiment. By analogy to the MIAME (URL_TO_INSERT_RECORD-ABBREV_4748 https://fairsharing.org/FAIRsharing.32b10v)  guideline (URL_TO_INSERT_TERM_4742 https://fairsharing.org/search?recordType=reporting_guideline) s for microarray experiments, adherence to the MINSEQE (URL_TO_INSERT_RECORD-ABBREV_4746 https://fairsharing.org/FAIRsharing.a55z32)  guideline (URL_TO_INSERT_TERM_4743 https://fairsharing.org/search?recordType=reporting_guideline) s will improve integration of multiple experiments across different modalities, thereby maximising the value of high-throughput research. MINSEQE (URL_TO_INSERT_RECORD-ABBREV_4747 https://fairsharing.org/FAIRsharing.a55z32)  has been integrated into a number of transcriptomics and sequencing archives.

Functional Annotation of Animal Genomes (FAANG) - FAANG provides a set of orthogonal standard (URL_TO_INSERT_TERM_4749 https://fairsharing.org/search?fairsharingRegistry=Standard) s for the capture of well-structured metadata for experiments, samples and analyses in the animal genomics domain. The FAANG standard (URL_TO_INSERT_TERM_4750 https://fairsharing.org/search?fairsharingRegistry=Standard) s support the MIAME (URL_TO_INSERT_RECORD-ABBREV_4753 https://fairsharing.org/FAIRsharing.32b10v)  and MINSEQE (URL_TO_INSERT_RECORD-ABBREV_4752 https://fairsharing.org/FAIRsharing.a55z32)  guideline (URL_TO_INSERT_TERM_4751 https://fairsharing.org/search?recordType=reporting_guideline) s, and aim to convert them to a concrete specification.

Human Cell Atlas Metadata (HCA-Metadata) - the HCA metadata model (URL_TO_INSERT_TERM_4755 https://fairsharing.org/search?recordType=model_and_format)  provides a concrete specification for capturing the metadata for single cell sequencing experiments. It is based on the three standard (URL_TO_INSERT_TERM_4754 https://fairsharing.org/search?fairsharingRegistry=Standard) s above, while focusing on the specific requirements of the single cell space.

### Minimum metadata vs desirable metadata

A minimum metadata set constitutes metadata items that always need to be supplied with any experimental data. For validation purposes, these should not be omittable. Desirable or recommended metadata items on the other hand should be supplied if available but will not cause a validation failure if absent. 

### Common metadata

Common metadata include any informat (URL_TO_INSERT_TERM_4756 https://fairsharing.org/search?recordType=model_and_format) ion that is not specific to transcriptomics experiments but applies to most experiments in the biomedical domain. They include:

- Project (URL_TO_INSERT_TERM_4757 https://fairsharing.org/search?recordType=project)  level metadata
- Common sample level metadata such as species, tissue, cell type etc.


#### Suggested metadata fields

The following table contains a non-exhaustive list of suggested minimum metadata fields for biological samples. The collection (URL_TO_INSERT_TERM_4760 https://fairsharing.org/search?recordType=collection)  is based on a range of existing metadata standard (URL_TO_INSERT_TERM_4758 https://fairsharing.org/search?fairsharingRegistry=Standard) s, including MIAME (URL_TO_INSERT_RECORD-ABBREV_4762 https://fairsharing.org/FAIRsharing.32b10v) , MINSEQE (URL_TO_INSERT_RECORD-ABBREV_4761 https://fairsharing.org/FAIRsharing.a55z32) , FAANG and HCA. Fields were included if they occurred in at least two of the standard (URL_TO_INSERT_TERM_4759 https://fairsharing.org/search?fairsharingRegistry=Standard) s.

|Metadata field|Required?|Definition|Comment|
|--------|--------|--------|--------|
|unique ID|required|Identifier (URL_TO_INSERT_TERM_4764 https://fairsharing.org/search?recordType=identifier_schema)  for a sample that is at least unique within the project (URL_TO_INSERT_TERM_4763 https://fairsharing.org/search?recordType=project) ||
|sample type|required|The type of the collected specimen, eg tissue biopsy, blood draw or throat swab|`ontology (URL_TO_INSERT_TERM_4765 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. OBI (URL_TO_INSERT_RECORD-ABBREV_4766 https://fairsharing.org/FAIRsharing.284e1z)  or EFO (URL_TO_INSERT_RECORD-ABBREV_4767 https://fairsharing.org/FAIRsharing.1gr4tz) |
|species|required|The primary species of the specimen, preferably the taxonomic identifier (URL_TO_INSERT_TERM_4769 https://fairsharing.org/search?recordType=identifier_schema) |This may not be the same as the "host" organism, eg in the case of a PDX tissue sample, the host may be a mouse but the tissue may be human. Ontology (URL_TO_INSERT_TERM_4768 https://fairsharing.org/search?recordType=terminology_artefact)  field - NCBITaxonomy|
|tissue/organism part|required|The tissue from which the sample was taken|`ontology (URL_TO_INSERT_TERM_4770 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. Uberon|
|disease|required|Any diseases that may affect the sample|This may not necessarily be the same as the host's disease, eg healthy brain tissue might be collected from a host with type II diabetes while cirrhotic liver tissue might be collected from an otherwise healthy individual. Ontology (URL_TO_INSERT_TERM_4771 https://fairsharing.org/search?recordType=terminology_artefact)  field - e.g. MONDO (URL_TO_INSERT_RECORD-ABBREV_4772 https://fairsharing.org/FAIRsharing.b2979t)  or DO|
|sex|required|The biological/genetic sex of the sample|`ontology (URL_TO_INSERT_TERM_4773 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. PATO (URL_TO_INSERT_RECORD-ABBREV_4774 https://fairsharing.org/FAIRsharing.ezwdhz) |
|development stage|required|The developmental stage of the sample|`ontology (URL_TO_INSERT_TERM_4775 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. Uberon or Hsadpdv; species dependent|
|collection (URL_TO_INSERT_TERM_4777 https://fairsharing.org/search?recordType=collection)  date|required|The date on which the sample was collected, in a standard (URL_TO_INSERT_TERM_4776 https://fairsharing.org/search?fairsharingRegistry=Standard) ised format (URL_TO_INSERT_TERM_4779 https://fairsharing.org/search?recordType=model_and_format) |Collection (URL_TO_INSERT_TERM_4778 https://fairsharing.org/search?recordType=collection)  date in combination with other fields such as location and disease may be sufficient to de-anonymise a sample|
|external accessions|recommended|Accession numbers from any external resources to which the sample was submitted|eg Biosamples, Biostudies (URL_TO_INSERT_RECORD-NAME_4780 https://fairsharing.org/FAIRsharing.mtjvme) |
|strain|recommended|Strain of the species from which the sample was collected, if applicable|`ontology (URL_TO_INSERT_TERM_4781 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. NCBITaxonomy|
|ancestry/ethnicity|recommended|Ancestry or ethnic group of the individual from which the sample was collected|`ontology (URL_TO_INSERT_TERM_4782 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. HANCESTRO (URL_TO_INSERT_RECORD-ABBREV_4783 https://fairsharing.org/FAIRsharing.rja8qp) |
|age |recommended|Age of the organism from which the sample was collected||
|age unit|recommended|Unit of the value of the age field|`ontology (URL_TO_INSERT_TERM_4784 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. UO (URL_TO_INSERT_RECORD-ABBREV_4785 https://fairsharing.org/FAIRsharing.mjnypw) |
|BMI|recommended|Body mass index of the individual from which the sample was collected|Only applies to human samples|
|treatment category|recommended|Treatments that the sample might have undergone after collection (URL_TO_INSERT_TERM_4786 https://fairsharing.org/search?recordType=collection) |`ontology (URL_TO_INSERT_TERM_4787 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. OBI (URL_TO_INSERT_RECORD-ABBREV_4790 https://fairsharing.org/FAIRsharing.284e1z) , NCIt (URL_TO_INSERT_RECORD-ABBREV_4788 https://fairsharing.org/FAIRsharing.4cvwxa)  or OGMS (URL_TO_INSERT_RECORD-ABBREV_4789 https://fairsharing.org/FAIRsharing.rvz0m9) |
|cell type|recommended|The cell type(s) known or selected to be present in the sample|`ontology (URL_TO_INSERT_TERM_4791 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. CL (URL_TO_INSERT_RECORD-ABBREV_4792 https://fairsharing.org/FAIRsharing.j9y503) |
|growth conditions|recommended|Features relating to the growth and/or maintenance of the sample||
|genetic variation|recommended|Any relevant genetic differences from the specimen or sample to the expected genomic informat (URL_TO_INSERT_TERM_4793 https://fairsharing.org/search?recordType=model_and_format) ion for this species, eg abnormal chromosome counts, major translocations or indels||
|sample collection (URL_TO_INSERT_TERM_4794 https://fairsharing.org/search?recordType=collection)  technique|recommended|The technique used to collect the specimen, eg blood draw or surgical resection|`ontology (URL_TO_INSERT_TERM_4795 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD-ABBREV_4797 https://fairsharing.org/FAIRsharing.1gr4tz)  or OBI (URL_TO_INSERT_RECORD-ABBREV_4796 https://fairsharing.org/FAIRsharing.284e1z) |
|phenotype|recommended|Any relevant (usually abnormal) phenotypes of the specimen or sample |`ontology (URL_TO_INSERT_TERM_4798 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. HP (URL_TO_INSERT_RECORD-ABBREV_4800 https://fairsharing.org/FAIRsharing.kbtt7f)  or MP (URL_TO_INSERT_RECORD-ABBREV_4799 https://fairsharing.org/FAIRsharing.kg1x4z) ; species dependent|
|cell cycle|recommended|The cell cycle phase of the sample (for synchronized growing cells or a single-cell sample), if known|`ontology (URL_TO_INSERT_TERM_4801 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. GO (URL_TO_INSERT_RECORD-ABBREV_4802 https://fairsharing.org/FAIRsharing.6xq0ee) |
|cell location|recommended|The cell location from which genetic material was collected (usually either nucleus or mitochondria)|`ontology (URL_TO_INSERT_TERM_4803 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. GO (URL_TO_INSERT_RECORD-ABBREV_4804 https://fairsharing.org/FAIRsharing.6xq0ee) |


### Assay metadata

Assay-level metadata covers any metadata directly related to the preparation of the biomaterial undergoing the assay and the process of performing the assay. Most, though not all, of this metadata is specific to transcriptomics. Examples include:
- Library informat (URL_TO_INSERT_TERM_4805 https://fairsharing.org/search?recordType=model_and_format) ion, including what sample the library was originally derived from and whether any replicates are biological or technical
- Process (wet experiment) metadata
- Technology type (e.g. bulk RNA-Seq, scRNA-Seq, CITE-Seq)
- Instrument metadata
- Other assay-specific metadata
- QC informat (URL_TO_INSERT_TERM_4806 https://fairsharing.org/search?recordType=model_and_format) ion
- Workflow metadata

The figure below shows an excerpt of the Human Cell Atlas json schema for describing the process of sequencing. 


````{dropdown}
:open:
```{figure} hca_sequencing_json_schema.png
---
name: human cell atlas sequencing json schema
alt: human cell atlas sequencing json schema.
---
human cell atlas sequencing json schema.
```
````

```{note}
Note the key attributes for which controlled vocabulary may be directly specified as a: 

`json schema ENUM` 

as found at line 79, or may be specified via a reference to a dedicated ontology schema as in:
 
` "$ref": "module/ontology/biological_macromolecule_ontology.json"`
 
as found at line 82.

```

````{dropdown}
:open:
```{figure} hca_library_amplification_ontology_json_schema.png
---
name: hca_library_amplification_ontology (URL_TO_INSERT_TERM_4807 https://fairsharing.org/search?recordType=terminology_artefact) _json_schema
alt: hca_library_amplification_ontology (URL_TO_INSERT_TERM_4808 https://fairsharing.org/search?recordType=terminology_artefact) _json_schema.
---
human cell atlas sequencing json schema.
```
````

```{note}
Note how the `ontology` element defines a `graph restriction` pointing to a branch in a semantic resource, (EFO in this case).
```

#### Suggested metadata fields

The following table contains a non-exhaustive list of suggested minimum metadata fields for assays. The collection (URL_TO_INSERT_TERM_4810 https://fairsharing.org/search?recordType=collection)  is based on a range of existing metadata standard (URL_TO_INSERT_TERM_4809 https://fairsharing.org/search?fairsharingRegistry=Standard) s, including MIAME (URL_TO_INSERT_RECORD-ABBREV_4812 https://fairsharing.org/FAIRsharing.32b10v) , MINSEQE (URL_TO_INSERT_RECORD-ABBREV_4811 https://fairsharing.org/FAIRsharing.a55z32)  and HCA. This list can and should be further broken down based on specific technologies used, such as microarrays or whole genome sequencing.

|Metadata field|Required?|Definition|Comment|
|--------|--------|--------|--------|
|unique ID|required|Identifier (URL_TO_INSERT_TERM_4814 https://fairsharing.org/search?recordType=identifier_schema)  for the assay that is at least unique within the project (URL_TO_INSERT_TERM_4813 https://fairsharing.org/search?recordType=project) ||
|experiment type|required|The type of experiment performed, eg ATAC-seq or seqFISH|`ontology (URL_TO_INSERT_TERM_4815 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD-ABBREV_4817 https://fairsharing.org/FAIRsharing.1gr4tz)  or OBI (URL_TO_INSERT_RECORD-ABBREV_4816 https://fairsharing.org/FAIRsharing.284e1z) |
|extracted nucleic acid/material type|required|The type of material that was extracted from the sample, eg polyA RNA|`ontology (URL_TO_INSERT_TERM_4818 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. ChEBI (URL_TO_INSERT_RECORD-ABBREV_4819 https://fairsharing.org/FAIRsharing.62qk8w)  or EFO (URL_TO_INSERT_RECORD-ABBREV_4820 https://fairsharing.org/FAIRsharing.1gr4tz) |
|platform|required|The type of instrument used to perform the assay, eg Illumina HiSeq 4000 or Fluidigm C1 microfluidics platform|`ontology (URL_TO_INSERT_TERM_4821 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD-ABBREV_4823 https://fairsharing.org/FAIRsharing.1gr4tz)  or OBI (URL_TO_INSERT_RECORD-ABBREV_4822 https://fairsharing.org/FAIRsharing.284e1z) |
|nucleic acid extraction method|required|Technique used to extract the nucleic acid from the cell|`ontology (URL_TO_INSERT_TERM_4824 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD-ABBREV_4826 https://fairsharing.org/FAIRsharing.1gr4tz)  or OBI (URL_TO_INSERT_RECORD-ABBREV_4825 https://fairsharing.org/FAIRsharing.284e1z) |
|cDNA library amplication method|required|Technique used to amplify a cDNA library|`ontology (URL_TO_INSERT_TERM_4827 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD-ABBREV_4829 https://fairsharing.org/FAIRsharing.1gr4tz)  or OBI (URL_TO_INSERT_RECORD-ABBREV_4828 https://fairsharing.org/FAIRsharing.284e1z) |
|array or sequencing method|required|The array or sequencing technology used - may be the same as `experiment type` or can be a more specific term|`ontology (URL_TO_INSERT_TERM_4830 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD-ABBREV_4832 https://fairsharing.org/FAIRsharing.1gr4tz)  or OBI (URL_TO_INSERT_RECORD-ABBREV_4831 https://fairsharing.org/FAIRsharing.284e1z) |
|biological or technical replicate|required|Informat (URL_TO_INSERT_TERM_4833 https://fairsharing.org/search?recordType=model_and_format) ion whether the sample on which the assay was performed was biological or technical replicate.|boolean or CV|
|end bias|required|The type of tag or end bias the library has, eg 3 prime tag or 5 prime end bias|standard (URL_TO_INSERT_TERM_4834 https://fairsharing.org/search?fairsharingRegistry=Standard) ised field or ontology (URL_TO_INSERT_TERM_4835 https://fairsharing.org/search?recordType=terminology_artefact) |
|external accessions|recommended|Accession numbers from external resources to which assay or protocol informat (URL_TO_INSERT_TERM_4836 https://fairsharing.org/search?recordType=model_and_format) ion was submitted|eg protocols.io (URL_TO_INSERT_RECORD-NAME_4837 https://fairsharing.org/FAIRsharing.132b10) , AE|
|instrument model (URL_TO_INSERT_TERM_4838 https://fairsharing.org/search?recordType=model_and_format) |required|The specific instrument on which the assay was performed. Essential for QC purposes.|`ontology (URL_TO_INSERT_TERM_4839 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD-ABBREV_4841 https://fairsharing.org/FAIRsharing.1gr4tz)  or OBI (URL_TO_INSERT_RECORD-ABBREV_4840 https://fairsharing.org/FAIRsharing.284e1z) |
|assay start time|recommended|The exact time at which the assay was started||
|assay end time|recommended|The exact time at which the assay was completed||
|assay duration|recommended|The duration, in a relevant time unit (eg minutes or hours), of the assay from start to finish||
|array quality|recommended|The overall quality of the array||
|chemical compound|recommended|Any relevant chemical compounds used in the assay|`ontology (URL_TO_INSERT_TERM_4842 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. ChEBI (URL_TO_INSERT_RECORD-ABBREV_4843 https://fairsharing.org/FAIRsharing.62qk8w) |
|labeling molecule used|recommended|The type of labeling molecule used in an array-based experiment|`ontology (URL_TO_INSERT_TERM_4844 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. ChEBI (URL_TO_INSERT_RECORD-ABBREV_4845 https://fairsharing.org/FAIRsharing.62qk8w) |
|spike-in kit used|recommended|Informat (URL_TO_INSERT_TERM_4846 https://fairsharing.org/search?recordType=model_and_format) ion about the spike-in kit used during sequencing library preparation||
|cDNA primer|recommended|Type of primer used for cDNA synthesis from RNA, eg polyA or random|standard (URL_TO_INSERT_TERM_4847 https://fairsharing.org/search?fairsharingRegistry=Standard) ised field or ontology (URL_TO_INSERT_TERM_4848 https://fairsharing.org/search?recordType=terminology_artefact) |
|library strandedness|recommended|The strandedness of the cDNA library |standard (URL_TO_INSERT_TERM_4849 https://fairsharing.org/search?fairsharingRegistry=Standard) ised field or ontology (URL_TO_INSERT_TERM_4850 https://fairsharing.org/search?recordType=terminology_artefact) |
|cell quality|recommended|Informat (URL_TO_INSERT_TERM_4852 https://fairsharing.org/search?recordType=model_and_format) ion about the quality of a single cell such as morphology or percent viability|standard (URL_TO_INSERT_TERM_4851 https://fairsharing.org/search?fairsharingRegistry=Standard) ised field or ontology (URL_TO_INSERT_TERM_4853 https://fairsharing.org/search?recordType=terminology_artefact) |
|cell barcode|recommended|Informat (URL_TO_INSERT_TERM_4854 https://fairsharing.org/search?recordType=model_and_format) ion about the cell identifier (URL_TO_INSERT_TERM_4855 https://fairsharing.org/search?recordType=identifier_schema)  barcode used to tag individual cells in single cell sequencing||
|UMI barcode|recommended|Informat (URL_TO_INSERT_TERM_4856 https://fairsharing.org/search?recordType=model_and_format) ion about the Unique Molecular Identifier (URL_TO_INSERT_TERM_4857 https://fairsharing.org/search?recordType=identifier_schema)  barcodes used to tag DNA fragments||

### Analysis metadata

Analysis-level metadata includes any metadata related to the files that come out of the experiment, from the sequencing or imaging files generated directly by the machine to files generated during the various stages of processing and analysis, as well as details of any analyses performed. It is very important to always capture versions of software and reference genomes used in order to allow accurate replication of results. Analysis metadata includes
- Type of analysis
- File format (URL_TO_INSERT_TERM_4858 https://fairsharing.org/search?recordType=model_and_format) s, e.g. BAM (URL_TO_INSERT_RECORD-ABBREV_4859 https://fairsharing.org/FAIRsharing.hza1ec) , fastq or gene count
- File location e.g. URL (URL_TO_INSERT_RECORD-ABBREV_4860 https://fairsharing.org/FAIRsharing.9d38e2) 
- Summarisation of data, e.g. enrichment analysis

#### Suggested metadata fields

The following table contains a non-exhaustive list of suggested minimum metadata fields for analyses. The collection (URL_TO_INSERT_TERM_4862 https://fairsharing.org/search?recordType=collection)  is based on a range of existing metadata standard (URL_TO_INSERT_TERM_4861 https://fairsharing.org/search?fairsharingRegistry=Standard) s, including MIAME (URL_TO_INSERT_RECORD-ABBREV_4864 https://fairsharing.org/FAIRsharing.32b10v) , MINSEQE (URL_TO_INSERT_RECORD-ABBREV_4863 https://fairsharing.org/FAIRsharing.a55z32)  and HCA. This list can and should be further broken down based on the specific analysis type (primary, secondary or teriatry analysis, meta-analysis etc)

|Metadata field|Required?|Definition|Comment|
|--------|--------|--------|--------|
|analysis type|required|The type of analysis performed, eg genome assembly or variant calling  |`ontology (URL_TO_INSERT_TERM_4865 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD-ABBREV_4868 https://fairsharing.org/FAIRsharing.1gr4tz) , OBI (URL_TO_INSERT_RECORD-ABBREV_4867 https://fairsharing.org/FAIRsharing.284e1z)  or EDAM (URL_TO_INSERT_RECORD-ABBREV_4866 https://fairsharing.org/FAIRsharing.a6r7zs) |
|computational method|required|The specific computational method or algorithm used as part of the analysis|`ontology (URL_TO_INSERT_TERM_4869 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD-ABBREV_4871 https://fairsharing.org/FAIRsharing.1gr4tz)  or EDAM (URL_TO_INSERT_RECORD-ABBREV_4870 https://fairsharing.org/FAIRsharing.a6r7zs) |
|normalisation strategy|required|The approach used to normalise the data|`ontology (URL_TO_INSERT_TERM_4872 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD-ABBREV_4874 https://fairsharing.org/FAIRsharing.1gr4tz)  or EDAM (URL_TO_INSERT_RECORD-ABBREV_4873 https://fairsharing.org/FAIRsharing.a6r7zs) |
|file format (URL_TO_INSERT_TERM_4875 https://fairsharing.org/search?recordType=model_and_format) |required|The file format (URL_TO_INSERT_TERM_4876 https://fairsharing.org/search?recordType=model_and_format)  in which the analysis is provided|`ontology (URL_TO_INSERT_TERM_4877 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EDAM (URL_TO_INSERT_RECORD-ABBREV_4878 https://fairsharing.org/FAIRsharing.a6r7zs) |
|file storage location|required|The location in which the data files are stored||
|software package|recommended|The software package used for data analysis||
|software version|recommended|The exact version number of the software package ||
|analysis date|recommended|The date on which the analysis was performed||
|read index|recommended|The sequencing read a specific file represents, eg read1 or index1||
|read length|recommended|The length of a sequenced read in this file, in nucleotides.||
|assembly type|recommended|The assembly type of the genome reference file, eg primary, complete or patch assembly.|standard (URL_TO_INSERT_TERM_4879 https://fairsharing.org/search?fairsharingRegistry=Standard) ised field or ontology (URL_TO_INSERT_TERM_4880 https://fairsharing.org/search?recordType=terminology_artefact) |
|reference genome version|recommended|The genome version of the reference file.||

## Ontologies for transcriptomics data

While it is essential that any transcriptomics metadata be annotated with ontology (URL_TO_INSERT_TERM_4882 https://fairsharing.org/search?recordType=terminology_artefact)  terms wherever possible, there is no absolute set of ontologies (URL_TO_INSERT_TERM_4885 https://fairsharing.org/search?recordType=terminology_artefact)  that must be used above all others. There is however a consensus set of ontologies (URL_TO_INSERT_TERM_4886 https://fairsharing.org/search?recordType=terminology_artefact)  and other standard (URL_TO_INSERT_TERM_4881 https://fairsharing.org/search?fairsharingRegistry=Standard) ised resources that are commonly used in transcriptomics metadata, including in the main data archives. The most commonly used ontologies (URL_TO_INSERT_TERM_4887 https://fairsharing.org/search?recordType=terminology_artefact)  and fields they apply to are listed below. This table represents an absolute minimum of ontology (URL_TO_INSERT_TERM_4883 https://fairsharing.org/search?recordType=terminology_artefact)  annotations that should be included in a transcriptomics metadata set for it to be considered as FAIR (URL_TO_INSERT_RECORD-ABBREV_4888 https://fairsharing.org/FAIRsharing.WWI10U) . Not all fields suggested for ontology (URL_TO_INSERT_TERM_4884 https://fairsharing.org/search?recordType=terminology_artefact)  annotation in the previous section are repeated here for this reason.

|Data type|Ontology (URL_TO_INSERT_TERM_4889 https://fairsharing.org/search?recordType=terminology_artefact) /Entity sources|Type|Notes|
|---|---|---|---|
|Species |NCBI taxonomy (URL_TO_INSERT_RECORD-NAME_4891 https://fairsharing.org/FAIRsharing.fj07xj)  Scientific name + ID|Ontology (URL_TO_INSERT_TERM_4890 https://fairsharing.org/search?recordType=terminology_artefact) ||
|Tissue |Uberon term and Id|Ontology (URL_TO_INSERT_TERM_4892 https://fairsharing.org/search?recordType=terminology_artefact) ||
|Cell type| CL (URL_TO_INSERT_RECORD-ABBREV_4894 https://fairsharing.org/FAIRsharing.j9y503)  term and Id|Ontology (URL_TO_INSERT_TERM_4893 https://fairsharing.org/search?recordType=terminology_artefact) ||
|Disease|MOND (URL_TO_INSERT_RECORD-ABBREV_4896 https://fairsharing.org/FAIRsharing.b2979t) O, DO or MeSH|Ontology (URL_TO_INSERT_TERM_4895 https://fairsharing.org/search?recordType=terminology_artefact) |no single solution - options vary depending on resource and individual requirements |
|Phenotype/Trait|HPO (human),  MP (URL_TO_INSERT_RECORD-ABBREV_4899 https://fairsharing.org/FAIRsharing.kg1x4z) (other mammals), various others for model (URL_TO_INSERT_TERM_4897 https://fairsharing.org/search?recordType=model_and_format)  organisms (yeast, zebrafish, Xenopus, C. elegans)|Ontology (URL_TO_INSERT_TERM_4898 https://fairsharing.org/search?recordType=terminology_artefact) ||
|Experiment Type|EF (URL_TO_INSERT_RECORD-ABBREV_4902 https://fairsharing.org/FAIRsharing.1gr4tz) O, OBI (URL_TO_INSERT_RECORD-ABBREV_4901 https://fairsharing.org/FAIRsharing.284e1z) |Ontology (URL_TO_INSERT_TERM_4900 https://fairsharing.org/search?recordType=terminology_artefact) | e.g. RNASeq, CITESeq etc. - |
|Cell location/cycle| GO (URL_TO_INSERT_RECORD-ABBREV_4904 https://fairsharing.org/FAIRsharing.6xq0ee) |Ontology (URL_TO_INSERT_TERM_4903 https://fairsharing.org/search?recordType=terminology_artefact) ||
|Developmental stage|HSAPD (URL_TO_INSERT_RECORD-ABBREV_4906 https://fairsharing.org/FAIRsharing.c6vhm3) V/Uberon|Ontology (URL_TO_INSERT_TERM_4905 https://fairsharing.org/search?recordType=terminology_artefact) ||
|Chemical compound| ChEBI (URL_TO_INSERT_RECORD-ABBREV_4908 https://fairsharing.org/FAIRsharing.62qk8w) |Ontology (URL_TO_INSERT_TERM_4907 https://fairsharing.org/search?recordType=terminology_artefact) ||
|Chemical compound| UniChem, SMILE, InChi|Entity||
|Gene/protein|ENSEMB (URL_TO_INSERT_RECORD-NAME_4909 https://fairsharing.org/FAIRsharing.fx0mw7) L, ENTREZ_GENE, UNIPROT, HGNC (URL_TO_INSERT_RECORD-ABBREV_4910 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD-ABBREV_4911 https://fairsharing.org/FAIRsharing.29we0s)  ID, INSDC|Entity||
|Metabolites| MetaboLights (URL_TO_INSERT_RECORD-NAME_4912 https://fairsharing.org/FAIRsharing.kkdpxe)  compound accession, ChEBI (URL_TO_INSERT_RECORD-ABBREV_4913 https://fairsharing.org/FAIRsharing.62qk8w) |Entity||
|Nucleotide reference sequence|ReqSeq|Entity||


## Conclusion

Using common transcriptomics metadata standard (URL_TO_INSERT_TERM_4914 https://fairsharing.org/search?fairsharingRegistry=Standard) s, in particular the fields listed above as guidance, it is possible to
easily define a comprehensive metadata template to capture all the experimental variables to describe any 
transcriptomics experiment in a FAIR (URL_TO_INSERT_RECORD-ABBREV_4915 https://fairsharing.org/FAIRsharing.WWI10U) -compliant way. A generic step-by-step guide for designing a metadata
template is provided [here](creating-minimal-metadata-profiles.md)

````{dropdown} **References**
````

## Authors

<!-- TODO clarify the contribution of Karsten and Peter -->
````{authors_fairplus}
Danielle: Writing - Review & Editing
Karsten: <!-- TODO -->
Peter: <!-- TODO -->
````


## License
````{license_fairplus}
CC-BY-4.0
````
