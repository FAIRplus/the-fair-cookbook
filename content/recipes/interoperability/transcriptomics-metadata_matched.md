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
> from standard (URL_TO_INSERT_TERM_7856 https://fairsharing.org/search?fairsharingRegistry=Standard)  case-control to dosage-response designs, and from microarrays to single cell RNA sequencing. 


### Who is this recipe aimed at?

This document is aimed at anyone interested in the metadata, and specifically the ontology (URL_TO_INSERT_TERM_7857 https://fairsharing.org/search?recordType=terminology_artefact)  annotations, required to capture variables and experimental factors related to a transcriptomics experiment. General knowledge of transcriptomics experiments would be beneficial. No specific technical knowledge is required.


---

## Transcriptomics Data model 

Large sections of any transcriptomics data model (URL_TO_INSERT_TERM_7859 https://fairsharing.org/search?recordType=model_and_format)  are not unique to transcriptomics experiments but are common to a wide range of experiments in the biomedical domain. This includes general project (URL_TO_INSERT_TERM_7858 https://fairsharing.org/search?recordType=project) - and sample-level informat (URL_TO_INSERT_TERM_7860 https://fairsharing.org/search?recordType=model_and_format) ion, which will be briefly covered in this recipe but will also be covered in more depth elsewhere.

Where possible, metadata should be map (URL_TO_INSERT_RECORD_7864 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_7866 https://fairsharing.org/FAIRsharing.31385c)  to ontologies (URL_TO_INSERT_TERM_7861 https://fairsharing.org/search?recordType=terminology_artefact)  to maximise the FAIR (URL_TO_INSERT_RECORD_7865 https://fairsharing.org/FAIRsharing.WWI10U) ness of any dataset. This recipe will suggest possible ontologies (URL_TO_INSERT_TERM_7862 https://fairsharing.org/search?recordType=terminology_artefact)  for metadata fields where these are available. These lists may however not be exhaustive as new ontologies (URL_TO_INSERT_TERM_7863 https://fairsharing.org/search?recordType=terminology_artefact)  emerge regularly.

### Existing standards and checklists

A set of well-established standard (URL_TO_INSERT_TERM_7867 https://fairsharing.org/search?fairsharingRegistry=Standard) s and minimum metadata checklists exist for various aspects of transcriptomics. They include:

Minimum Informat (URL_TO_INSERT_TERM_7871 https://fairsharing.org/search?recordType=model_and_format) ion About a Microarray Experiment (URL_TO_INSERT_RECORD_7879 https://fairsharing.org/FAIRsharing.32b10v)  (MIAME (URL_TO_INSERT_RECORD_7880 https://fairsharing.org/FAIRsharing.32b10v) ) - MIAME (URL_TO_INSERT_RECORD_7881 https://fairsharing.org/FAIRsharing.32b10v)  is intended to specify all the informat (URL_TO_INSERT_TERM_7872 https://fairsharing.org/search?recordType=model_and_format) ion necessary for an unambiguous interpretation of a microarray experiment, and potentially to reproduce it. MIAME (URL_TO_INSERT_RECORD_7882 https://fairsharing.org/FAIRsharing.32b10v)  defines the content but not the format (URL_TO_INSERT_TERM_7873 https://fairsharing.org/search?recordType=model_and_format)  for this informat (URL_TO_INSERT_TERM_7874 https://fairsharing.org/search?recordType=model_and_format) ion. The MIAME (URL_TO_INSERT_RECORD_7883 https://fairsharing.org/FAIRsharing.32b10v)  standard (URL_TO_INSERT_TERM_7868 https://fairsharing.org/search?fairsharingRegistry=Standard)  has been in existence for over 20 years and has been widely adopted across the scientific community. The data model (URL_TO_INSERT_TERM_7870 https://fairsharing.org/search?recordType=model_and_format) s of the major transcriptomics repositories (URL_TO_INSERT_TERM_7869 https://fairsharing.org/search?recordType=repository)  such as ArrayExpress (URL_TO_INSERT_RECORD_7878 https://fairsharing.org/FAIRsharing.6k0kwd) , the Expression Atlas (URL_TO_INSERT_RECORD_7886 https://fairsharing.org/FAIRsharing.f5zx00)  and the Gene Expression Omnibus (URL_TO_INSERT_RECORD_7876 https://fairsharing.org/FAIRsharing.5hc8vt)  (GEO (URL_TO_INSERT_RECORD_7875 https://fairsharing.org/FAIRsharing.27rndz)  (URL_TO_INSERT_RECORD_7877 https://fairsharing.org/FAIRsharing.5hc8vt)  (URL_TO_INSERT_RECORD_7885 https://fairsharing.org/FAIRsharing.d1zzym) ) are MIAME (URL_TO_INSERT_RECORD_7884 https://fairsharing.org/FAIRsharing.32b10v) -compliant.

Minimum Informat (URL_TO_INSERT_TERM_7887 https://fairsharing.org/search?recordType=model_and_format) ion about a high-throughput nucleotide SEQuencing Experiment (MINSEQE (URL_TO_INSERT_RECORD_7890 https://fairsharing.org/FAIRsharing.a55z32) ) - MINSEQE (URL_TO_INSERT_RECORD_7891 https://fairsharing.org/FAIRsharing.a55z32)  describes the minimum metadata that is needed to enable the unambiguous interpretation and facilitate reproduction of the results of the experiment. By analogy to the MIAME (URL_TO_INSERT_RECORD_7894 https://fairsharing.org/FAIRsharing.32b10v)  guideline (URL_TO_INSERT_TERM_7888 https://fairsharing.org/search?recordType=reporting_guideline) s for microarray experiments, adherence to the MINSEQE (URL_TO_INSERT_RECORD_7892 https://fairsharing.org/FAIRsharing.a55z32)  guideline (URL_TO_INSERT_TERM_7889 https://fairsharing.org/search?recordType=reporting_guideline) s will improve integration of multiple experiments across different modalities, thereby maximising the value of high-throughput research (URL_TO_INSERT_RECORD_7895 https://fairsharing.org/FAIRsharing.52b22c) . MINSEQE (URL_TO_INSERT_RECORD_7893 https://fairsharing.org/FAIRsharing.a55z32)  has been integrated into a number of transcriptomics and sequencing arch (URL_TO_INSERT_RECORD_7896 https://fairsharing.org/FAIRsharing.52b22c) ives.

Functional Annotation of Animal Genomes (FAANG) - FAANG provides a set of orthogonal standard (URL_TO_INSERT_TERM_7897 https://fairsharing.org/search?fairsharingRegistry=Standard) s for the capture of well-structured metadata for experiments, samples and analyses in the animal genomics domain. The FAANG standard (URL_TO_INSERT_TERM_7898 https://fairsharing.org/search?fairsharingRegistry=Standard) s support the MIAME (URL_TO_INSERT_RECORD_7901 https://fairsharing.org/FAIRsharing.32b10v)  and MINSEQE (URL_TO_INSERT_RECORD_7900 https://fairsharing.org/FAIRsharing.a55z32)  guideline (URL_TO_INSERT_TERM_7899 https://fairsharing.org/search?recordType=reporting_guideline) s, and aim to convert them to a concrete specification.

Human Cell Atlas Metadata (HCA-Metadata) - the HCA metadata model (URL_TO_INSERT_TERM_7903 https://fairsharing.org/search?recordType=model_and_format)  provides a concrete specification for capturing the metadata for single cell sequencing experiments. It is based on the three standard (URL_TO_INSERT_TERM_7902 https://fairsharing.org/search?fairsharingRegistry=Standard) s above, while focusing on the specific requirements of the single cell space.

### Minimum metadata vs desirable metadata

A minimum metadata set constitutes metadata items that always need to be supplied with any experimental data. For validation purposes, these should not be omittable. Desirable or recommended metadata items on the other hand should be supplied if available but will not cause a validation failure if absent. 

### Common metadata

Common metadata include any informat (URL_TO_INSERT_TERM_7904 https://fairsharing.org/search?recordType=model_and_format) ion that is not specific to transcriptomics experiments but applies to most experiments in the biomedical domain. They include:

- Project (URL_TO_INSERT_TERM_7905 https://fairsharing.org/search?recordType=project)  level metadata
- Common sample level metadata such as species, tissue, cell type etc.


#### Suggested metadata fields

The following table contains a non-exhaustive list of suggested minimum metadata fields for biological samples. The collection (URL_TO_INSERT_TERM_7908 https://fairsharing.org/search?recordType=collection)  is based on a range of existing metadata standard (URL_TO_INSERT_TERM_7906 https://fairsharing.org/search?fairsharingRegistry=Standard) s, including MIAME (URL_TO_INSERT_RECORD_7910 https://fairsharing.org/FAIRsharing.32b10v) , MINSEQE (URL_TO_INSERT_RECORD_7909 https://fairsharing.org/FAIRsharing.a55z32) , FAANG and HCA. Fields were included if they occurred in at least two of the standard (URL_TO_INSERT_TERM_7907 https://fairsharing.org/search?fairsharingRegistry=Standard) s.

|Metadata field|Required?|Definition|Comment|
|--------|--------|--------|--------|
|unique ID|required|Identifier (URL_TO_INSERT_TERM_7912 https://fairsharing.org/search?recordType=identifier_schema)  for a sample that is at least unique within the project (URL_TO_INSERT_TERM_7911 https://fairsharing.org/search?recordType=project) ||
|sample type|required|The type of the collected specimen, eg tissue biopsy, blood draw or throat swab|`ontology (URL_TO_INSERT_TERM_7913 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. OBI (URL_TO_INSERT_RECORD_7914 https://fairsharing.org/FAIRsharing.284e1z)  or EFO (URL_TO_INSERT_RECORD_7915 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_7916 https://fairsharing.org/FAIRsharing.ca63ce) |
|species|required|The primary species of the specimen, preferably the taxonomic identifier (URL_TO_INSERT_TERM_7918 https://fairsharing.org/search?recordType=identifier_schema) |This may not be the same as the "host" organism, eg in the case of a PDX tissue sample, the host may be a mouse but the tissue may be human. Ontology (URL_TO_INSERT_TERM_7917 https://fairsharing.org/search?recordType=terminology_artefact)  field - NCBITaxonomy|
|tissue/organism part|required|The tissue from which the sample was taken|`ontology (URL_TO_INSERT_TERM_7919 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. Uberon|
|disease|required|Any diseases that may affect the sample|This may not necessarily be the same as the host's disease, eg healthy brain tissue might be collected from a host with type II diabetes while cirrhotic liver tissue might be collected from an otherwise healthy individual. Ontology (URL_TO_INSERT_TERM_7920 https://fairsharing.org/search?recordType=terminology_artefact)  field - e.g. MONDO (URL_TO_INSERT_RECORD_7921 https://fairsharing.org/FAIRsharing.b2979t)  or DO|
|sex|required|The biological/genetic sex of the sample|`ontology (URL_TO_INSERT_TERM_7922 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. PATO (URL_TO_INSERT_RECORD_7923 https://fairsharing.org/FAIRsharing.w69t6r)  (URL_TO_INSERT_RECORD_7924 https://fairsharing.org/FAIRsharing.ezwdhz) |
|development stage|required|The developmental stage of the sample|`ontology (URL_TO_INSERT_TERM_7925 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. Uberon or Hsadpdv; species dependent|
|collection (URL_TO_INSERT_TERM_7927 https://fairsharing.org/search?recordType=collection)  date|required|The date on which the sample was collected, in a standard (URL_TO_INSERT_TERM_7926 https://fairsharing.org/search?fairsharingRegistry=Standard) ised format (URL_TO_INSERT_TERM_7929 https://fairsharing.org/search?recordType=model_and_format) |Collection (URL_TO_INSERT_TERM_7928 https://fairsharing.org/search?recordType=collection)  date in combination with other fields such as location and disease may be sufficient to de-anonymise a sample|
|external accessions|recommended|Accession numbers from any external resources to which the sample was submitted|eg Biosamples, Biostudies (URL_TO_INSERT_RECORD_7930 https://fairsharing.org/FAIRsharing.mtjvme) |
|strain|recommended|Strain of the species from which the sample was collected, if applicable|`ontology (URL_TO_INSERT_TERM_7931 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. NCBITaxonomy|
|ancestry/ethnicity|recommended|Ancestry or ethnic group of the individual from which the sample was collected|`ontology (URL_TO_INSERT_TERM_7932 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. HANCESTRO (URL_TO_INSERT_RECORD_7933 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_7934 https://fairsharing.org/FAIRsharing.rja8qp)  (URL_TO_INSERT_RECORD_7935 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_7936 https://fairsharing.org/FAIRsharing.cp0ybc) |
|age |recommended|Age of the organism from which the sample was collected||
|age unit|recommended|Unit of the value of the age field|`ontology (URL_TO_INSERT_TERM_7937 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. UO (URL_TO_INSERT_RECORD_7938 https://fairsharing.org/FAIRsharing.mjnypw) |
|BMI|recommended|Body mass index of the individual from which the sample was collected|Only applies to human samples|
|treatment category|recommended|Treatments that the sample might have undergone after collection (URL_TO_INSERT_TERM_7939 https://fairsharing.org/search?recordType=collection) |`ontology (URL_TO_INSERT_TERM_7940 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. OBI (URL_TO_INSERT_RECORD_7943 https://fairsharing.org/FAIRsharing.284e1z) , NCIt (URL_TO_INSERT_RECORD_7941 https://fairsharing.org/FAIRsharing.4cvwxa)  or OGMS (URL_TO_INSERT_RECORD_7942 https://fairsharing.org/FAIRsharing.rvz0m9) |
|cell type|recommended|The cell type(s) known or selected to be present in the sample|`ontology (URL_TO_INSERT_TERM_7944 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. CL (URL_TO_INSERT_RECORD_7945 https://fairsharing.org/FAIRsharing.j9y503) |
|growth conditions|recommended|Features relating to the growth and/or maintenance of the sample||
|genetic variation|recommended|Any relevant genetic differences from the specimen or sample to the expected genomic informat (URL_TO_INSERT_TERM_7946 https://fairsharing.org/search?recordType=model_and_format) ion for this species, eg abnormal chromosome counts, major translocations or indels||
|sample collection (URL_TO_INSERT_TERM_7947 https://fairsharing.org/search?recordType=collection)  technique|recommended|The technique used to collect the specimen, eg blood draw or surgical resection|`ontology (URL_TO_INSERT_TERM_7948 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD_7950 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_7951 https://fairsharing.org/FAIRsharing.ca63ce)  or OBI (URL_TO_INSERT_RECORD_7949 https://fairsharing.org/FAIRsharing.284e1z) |
|phenotype|recommended|Any relevant (usually abnormal) phenotypes of the specimen or sample |`ontology (URL_TO_INSERT_TERM_7952 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. HP (URL_TO_INSERT_RECORD_7954 https://fairsharing.org/FAIRsharing.kbtt7f)  or MP (URL_TO_INSERT_RECORD_7953 https://fairsharing.org/FAIRsharing.kg1x4z) ; species dependent|
|cell cycle|recommended|The cell cycle phase of the sample (for synchronized growing cells or a single-cell sample), if known|`ontology (URL_TO_INSERT_TERM_7955 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. GO (URL_TO_INSERT_RECORD_7956 https://fairsharing.org/FAIRsharing.6xq0ee) |
|cell location|recommended|The cell location from which genetic material was collected (usually either nucleus or mitochondria)|`ontology (URL_TO_INSERT_TERM_7957 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. GO (URL_TO_INSERT_RECORD_7958 https://fairsharing.org/FAIRsharing.6xq0ee) |


### Assay metadata

Assay-level metadata covers any metadata directly related to the preparation of the biomaterial undergoing the assay and the process of performing the assay. Most, though not all, of this metadata is specific to transcriptomics. Examples include:
- Library informat (URL_TO_INSERT_TERM_7959 https://fairsharing.org/search?recordType=model_and_format) ion, including what sample the library was originally derived from and whether any replicates are biological or technical
- Process (wet experiment) metadata
- Technology type (e.g. bulk RNA-Seq, scRNA-Seq, CITE-Seq)
- Instrument metadata
- Other assay-specific metadata
- QC informat (URL_TO_INSERT_TERM_7960 https://fairsharing.org/search?recordType=model_and_format) ion
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
name: hca_library_amplification_ontology (URL_TO_INSERT_TERM_7961 https://fairsharing.org/search?recordType=terminology_artefact) _json_schema
alt: hca_library_amplification_ontology (URL_TO_INSERT_TERM_7962 https://fairsharing.org/search?recordType=terminology_artefact) _json_schema.
---
human cell atlas sequencing json schema.
```
````

```{note}
Note how the `ontology` element defines a `graph restriction` pointing to a branch in a semantic resource, (EFO in this case).
```

#### Suggested metadata fields

The following table contains a non-exhaustive list of suggested minimum metadata fields for assays. The collection (URL_TO_INSERT_TERM_7964 https://fairsharing.org/search?recordType=collection)  is based on a range of existing metadata standard (URL_TO_INSERT_TERM_7963 https://fairsharing.org/search?fairsharingRegistry=Standard) s, including MIAME (URL_TO_INSERT_RECORD_7966 https://fairsharing.org/FAIRsharing.32b10v) , MINSEQE (URL_TO_INSERT_RECORD_7965 https://fairsharing.org/FAIRsharing.a55z32)  and HCA. This list can and should be further broken down based on specific technologies used, such as microarrays or whole genome sequencing.

|Metadata field|Required?|Definition|Comment|
|--------|--------|--------|--------|
|unique ID|required|Identifier (URL_TO_INSERT_TERM_7968 https://fairsharing.org/search?recordType=identifier_schema)  for the assay that is at least unique within the project (URL_TO_INSERT_TERM_7967 https://fairsharing.org/search?recordType=project) ||
|experiment type|required|The type of experiment performed, eg ATAC (URL_TO_INSERT_RECORD_7972 https://fairsharing.org/FAIRsharing.md3e78) -seq or seqFISH|`ontology (URL_TO_INSERT_TERM_7969 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD_7971 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_7973 https://fairsharing.org/FAIRsharing.ca63ce)  or OBI (URL_TO_INSERT_RECORD_7970 https://fairsharing.org/FAIRsharing.284e1z) |
|extracted nucleic acid/material type|required|The type of material that was extracted from the sample, eg polyA RNA|`ontology (URL_TO_INSERT_TERM_7974 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. ChEBI (URL_TO_INSERT_RECORD_7975 https://fairsharing.org/FAIRsharing.62qk8w)  or EFO (URL_TO_INSERT_RECORD_7976 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_7977 https://fairsharing.org/FAIRsharing.ca63ce) |
|platform|required|The type of instrument used to perform the assay, eg Illumina HiSeq 4000 or Fluidigm C1 microfluidics platform|`ontology (URL_TO_INSERT_TERM_7978 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD_7980 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_7981 https://fairsharing.org/FAIRsharing.ca63ce)  or OBI (URL_TO_INSERT_RECORD_7979 https://fairsharing.org/FAIRsharing.284e1z) |
|nucleic acid extraction method|required|Technique used to extract the nucleic acid from the cell|`ontology (URL_TO_INSERT_TERM_7982 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD_7984 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_7985 https://fairsharing.org/FAIRsharing.ca63ce)  or OBI (URL_TO_INSERT_RECORD_7983 https://fairsharing.org/FAIRsharing.284e1z) |
|cDNA library amplication method|required|Technique used to amplify a cDNA library|`ontology (URL_TO_INSERT_TERM_7986 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD_7988 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_7989 https://fairsharing.org/FAIRsharing.ca63ce)  or OBI (URL_TO_INSERT_RECORD_7987 https://fairsharing.org/FAIRsharing.284e1z) |
|array or sequencing method|required|The array or sequencing technology used - may be the same as `experiment type` or can be a more specific term|`ontology (URL_TO_INSERT_TERM_7990 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD_7992 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_7993 https://fairsharing.org/FAIRsharing.ca63ce)  or OBI (URL_TO_INSERT_RECORD_7991 https://fairsharing.org/FAIRsharing.284e1z) |
|biological or technical replicate|required|Informat (URL_TO_INSERT_TERM_7994 https://fairsharing.org/search?recordType=model_and_format) ion whether the sample on which the assay was performed was biological or technical replicate.|boolean or CV|
|end bias|required|The type of tag or end bias the library has, eg 3 prime tag or 5 prime end bias|standard (URL_TO_INSERT_TERM_7995 https://fairsharing.org/search?fairsharingRegistry=Standard) ised field or ontology (URL_TO_INSERT_TERM_7996 https://fairsharing.org/search?recordType=terminology_artefact) |
|external accessions|recommended|Accession numbers from external resources to which assay or protocol informat (URL_TO_INSERT_TERM_7997 https://fairsharing.org/search?recordType=model_and_format) ion was submitted|eg protocols.io (URL_TO_INSERT_RECORD_7998 https://fairsharing.org/FAIRsharing.132b10) , AE|
|instrument model (URL_TO_INSERT_TERM_7999 https://fairsharing.org/search?recordType=model_and_format) |required|The specific instrument on which the assay was performed. Essential for QC purposes.|`ontology (URL_TO_INSERT_TERM_8000 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD_8002 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_8003 https://fairsharing.org/FAIRsharing.ca63ce)  or OBI (URL_TO_INSERT_RECORD_8001 https://fairsharing.org/FAIRsharing.284e1z) |
|assay start time|recommended|The exact time at which the assay was started||
|assay end time|recommended|The exact time at which the assay was completed||
|assay duration|recommended|The duration, in a relevant time unit (eg minutes or hours), of the assay from start to finish||
|array quality|recommended|The overall quality of the array||
|chemical compound|recommended|Any relevant chemical compounds used in the assay|`ontology (URL_TO_INSERT_TERM_8004 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. ChEBI (URL_TO_INSERT_RECORD_8005 https://fairsharing.org/FAIRsharing.62qk8w) |
|labeling molecule used|recommended|The type of labeling molecule used in an array-based experiment|`ontology (URL_TO_INSERT_TERM_8006 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. ChEBI (URL_TO_INSERT_RECORD_8007 https://fairsharing.org/FAIRsharing.62qk8w) |
|spike-in kit used|recommended|Informat (URL_TO_INSERT_TERM_8008 https://fairsharing.org/search?recordType=model_and_format) ion about the spike-in kit used during sequencing library preparation||
|cDNA primer|recommended|Type of primer used for cDNA synthesis from RNA, eg polyA or random|standard (URL_TO_INSERT_TERM_8009 https://fairsharing.org/search?fairsharingRegistry=Standard) ised field or ontology (URL_TO_INSERT_TERM_8010 https://fairsharing.org/search?recordType=terminology_artefact) |
|library strandedness|recommended|The strandedness of the cDNA library |standard (URL_TO_INSERT_TERM_8011 https://fairsharing.org/search?fairsharingRegistry=Standard) ised field or ontology (URL_TO_INSERT_TERM_8012 https://fairsharing.org/search?recordType=terminology_artefact) |
|cell quality|recommended|Informat (URL_TO_INSERT_TERM_8014 https://fairsharing.org/search?recordType=model_and_format) ion about the quality of a single cell such as morphology or percent viability|standard (URL_TO_INSERT_TERM_8013 https://fairsharing.org/search?fairsharingRegistry=Standard) ised field or ontology (URL_TO_INSERT_TERM_8015 https://fairsharing.org/search?recordType=terminology_artefact) |
|cell barcode|recommended|Informat (URL_TO_INSERT_TERM_8016 https://fairsharing.org/search?recordType=model_and_format) ion about the cell identifier (URL_TO_INSERT_TERM_8017 https://fairsharing.org/search?recordType=identifier_schema)  barcode used to tag individual cells in single cell sequencing||
|UMI barcode|recommended|Informat (URL_TO_INSERT_TERM_8018 https://fairsharing.org/search?recordType=model_and_format) ion about the Unique Molecular Identifier (URL_TO_INSERT_TERM_8019 https://fairsharing.org/search?recordType=identifier_schema)  barcodes used to tag DNA fragments||

### Analysis metadata

Analysis-level metadata includes any metadata related to the files that come out of the experiment, from the sequencing or imaging files generated directly by the machine to files generated during the various stages of processing and analysis, as well as details of any analyses performed. It is very important to always capture versions of software and reference genomes used in order to allow accurate replication of results. Analysis metadata includes
- Type of analysis
- File format (URL_TO_INSERT_TERM_8020 https://fairsharing.org/search?recordType=model_and_format) s, e.g. BAM (URL_TO_INSERT_RECORD_8021 https://fairsharing.org/FAIRsharing.hza1ec) , fastq or gene count
- File location e.g. URL (URL_TO_INSERT_RECORD_8022 https://fairsharing.org/FAIRsharing.9d38e2) 
- Summarisation of data, e.g. enrichment analysis

#### Suggested metadata fields

The following table contains a non-exhaustive list of suggested minimum metadata fields for analyses. The collection (URL_TO_INSERT_TERM_8024 https://fairsharing.org/search?recordType=collection)  is based on a range of existing metadata standard (URL_TO_INSERT_TERM_8023 https://fairsharing.org/search?fairsharingRegistry=Standard) s, including MIAME (URL_TO_INSERT_RECORD_8026 https://fairsharing.org/FAIRsharing.32b10v) , MINSEQE (URL_TO_INSERT_RECORD_8025 https://fairsharing.org/FAIRsharing.a55z32)  and HCA. This list can and should be further broken down based on the specific analysis type (primary, secondary or teriatry analysis, meta-analysis etc)

|Metadata field|Required?|Definition|Comment|
|--------|--------|--------|--------|
|analysis type|required|The type of analysis performed, eg genome assembly or variant calling  |`ontology (URL_TO_INSERT_TERM_8027 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD_8030 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_8031 https://fairsharing.org/FAIRsharing.ca63ce) , OBI (URL_TO_INSERT_RECORD_8029 https://fairsharing.org/FAIRsharing.284e1z)  or EDAM (URL_TO_INSERT_RECORD_8028 https://fairsharing.org/FAIRsharing.a6r7zs) |
|computational method|required|The specific computational method or algorithm used as part of the analysis|`ontology (URL_TO_INSERT_TERM_8032 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD_8034 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_8035 https://fairsharing.org/FAIRsharing.ca63ce)  or EDAM (URL_TO_INSERT_RECORD_8033 https://fairsharing.org/FAIRsharing.a6r7zs) |
|normalisation strategy|required|The approach used to normalise the data|`ontology (URL_TO_INSERT_TERM_8036 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD_8038 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_8039 https://fairsharing.org/FAIRsharing.ca63ce)  or EDAM (URL_TO_INSERT_RECORD_8037 https://fairsharing.org/FAIRsharing.a6r7zs) |
|file format (URL_TO_INSERT_TERM_8040 https://fairsharing.org/search?recordType=model_and_format) |required|The file format (URL_TO_INSERT_TERM_8041 https://fairsharing.org/search?recordType=model_and_format)  in which the analysis is provided|`ontology (URL_TO_INSERT_TERM_8042 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EDAM (URL_TO_INSERT_RECORD_8043 https://fairsharing.org/FAIRsharing.a6r7zs) |
|file storage location|required|The location in which the data files are stored||
|software package|recommended|The software package used for data analysis||
|software version|recommended|The exact version number of the software package ||
|analysis date|recommended|The date on which the analysis was performed||
|read index|recommended|The sequencing read a specific file represents, eg read1 or index1||
|read length|recommended|The length of a sequenced read in this file, in nucleotides.||
|assembly type|recommended|The assembly type of the genome reference file, eg primary, complete or patch assembly.|standard (URL_TO_INSERT_TERM_8044 https://fairsharing.org/search?fairsharingRegistry=Standard) ised field or ontology (URL_TO_INSERT_TERM_8045 https://fairsharing.org/search?recordType=terminology_artefact) |
|reference genome version|recommended|The genome version of the reference file.||

## Ontologies for transcriptomics data

While it is essential that any transcriptomics metadata be annotated with ontology (URL_TO_INSERT_TERM_8047 https://fairsharing.org/search?recordType=terminology_artefact)  terms wherever possible, there is no absolute set of ontologies (URL_TO_INSERT_TERM_8050 https://fairsharing.org/search?recordType=terminology_artefact)  that must be used above all others. There is however a consensus set of ontologies (URL_TO_INSERT_TERM_8051 https://fairsharing.org/search?recordType=terminology_artefact)  and other standard (URL_TO_INSERT_TERM_8046 https://fairsharing.org/search?fairsharingRegistry=Standard) ised resources that are commonly used in transcriptomics metadata, including in the main data arch (URL_TO_INSERT_RECORD_8054 https://fairsharing.org/FAIRsharing.52b22c) ives. The most commonly used ontologies (URL_TO_INSERT_TERM_8052 https://fairsharing.org/search?recordType=terminology_artefact)  and fields they apply to are listed below. This table represents an absolute minimum of ontology (URL_TO_INSERT_TERM_8048 https://fairsharing.org/search?recordType=terminology_artefact)  annotations that should be included in a transcriptomics metadata set for it to be considered as FAIR (URL_TO_INSERT_RECORD_8053 https://fairsharing.org/FAIRsharing.WWI10U) . Not all fields suggested for ontology (URL_TO_INSERT_TERM_8049 https://fairsharing.org/search?recordType=terminology_artefact)  annotation in the previous section are repeated here for this reason.

|Data type|Ontology (URL_TO_INSERT_TERM_8055 https://fairsharing.org/search?recordType=terminology_artefact) /Entity sources|Type|Notes|
|---|---|---|---|
|Species |NCBI taxonomy (URL_TO_INSERT_RECORD_8057 https://fairsharing.org/FAIRsharing.fj07xj)  Scientific name + ID|Ontology (URL_TO_INSERT_TERM_8056 https://fairsharing.org/search?recordType=terminology_artefact) ||
|Tissue |Uberon term and Id|Ontology (URL_TO_INSERT_TERM_8058 https://fairsharing.org/search?recordType=terminology_artefact) ||
|Cell type| CL (URL_TO_INSERT_RECORD_8060 https://fairsharing.org/FAIRsharing.j9y503)  term and Id|Ontology (URL_TO_INSERT_TERM_8059 https://fairsharing.org/search?recordType=terminology_artefact) ||
|Disease|MONDO (URL_TO_INSERT_RECORD_8062 https://fairsharing.org/FAIRsharing.b2979t) , DO or MeSH|Ontology (URL_TO_INSERT_TERM_8061 https://fairsharing.org/search?recordType=terminology_artefact) |no single solution - options vary depending on resource and individual requirements |
|Phenotype/Trait|HP (URL_TO_INSERT_RECORD_8067 https://fairsharing.org/FAIRsharing.kbtt7f) O (URL_TO_INSERT_RECORD_8066 https://fairsharing.org/FAIRsharing.3ngg40)  (human),  MP (URL_TO_INSERT_RECORD_8065 https://fairsharing.org/FAIRsharing.kg1x4z) (other mammals), various others for model (URL_TO_INSERT_TERM_8063 https://fairsharing.org/search?recordType=model_and_format)  organisms (yeast, zebrafish, Xenopus, C. elegans)|Ontology (URL_TO_INSERT_TERM_8064 https://fairsharing.org/search?recordType=terminology_artefact) ||
|Experiment Type|EFO (URL_TO_INSERT_RECORD_8070 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_8071 https://fairsharing.org/FAIRsharing.ca63ce) , OBI (URL_TO_INSERT_RECORD_8069 https://fairsharing.org/FAIRsharing.284e1z) |Ontology (URL_TO_INSERT_TERM_8068 https://fairsharing.org/search?recordType=terminology_artefact) | e.g. RNASeq, CITESeq etc. - |
|Cell location/cycle| GO (URL_TO_INSERT_RECORD_8073 https://fairsharing.org/FAIRsharing.6xq0ee) |Ontology (URL_TO_INSERT_TERM_8072 https://fairsharing.org/search?recordType=terminology_artefact) ||
|Developmental stage|HSAPDV (URL_TO_INSERT_RECORD_8075 https://fairsharing.org/FAIRsharing.c6vhm3) /Uberon|Ontology (URL_TO_INSERT_TERM_8074 https://fairsharing.org/search?recordType=terminology_artefact) ||
|Chemical compound| ChEBI (URL_TO_INSERT_RECORD_8077 https://fairsharing.org/FAIRsharing.62qk8w) |Ontology (URL_TO_INSERT_TERM_8076 https://fairsharing.org/search?recordType=terminology_artefact) ||
|Chemical compound| UniChem, SMILE, InChi|Entity||
|Gene/protein|ENSEMBL (URL_TO_INSERT_RECORD_8078 https://fairsharing.org/FAIRsharing.fx0mw7) , ENTREZ_GENE, UNIPRO (URL_TO_INSERT_RECORD_8079 https://fairsharing.org/FAIRsharing.3e88d6)  (URL_TO_INSERT_RECORD_8082 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_8084 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_8085 https://fairsharing.org/FAIRsharing.4ndncv)  (URL_TO_INSERT_RECORD_8087 https://fairsharing.org/FAIRsharing.cp0ybc) T, HGNC (URL_TO_INSERT_RECORD_8081 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_8088 https://fairsharing.org/FAIRsharing.29we0s)  ID, INSD (URL_TO_INSERT_RECORD_8080 https://fairsharing.org/FAIRsharing.mKDii0) C (URL_TO_INSERT_RECORD_8083 https://fairsharing.org/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD_8086 https://fairsharing.org/3547) |Entity||
|Metabolites| MetaboLights (URL_TO_INSERT_RECORD_8090 https://fairsharing.org/FAIRsharing.kkdpxe)  compound accession, ChEBI (URL_TO_INSERT_RECORD_8089 https://fairsharing.org/FAIRsharing.62qk8w) |Entity||
|Nucleotide reference sequence|ReqSeq|Entity||


## Conclusion

Using common transcriptomics metadata standard (URL_TO_INSERT_TERM_8091 https://fairsharing.org/search?fairsharingRegistry=Standard) s, in particular the fields listed above as guidance, it is possible to
easily define a comprehensive metadata template to capture all the experimental variables to describe any 
transcriptomics experiment in a FAIR (URL_TO_INSERT_RECORD_8092 https://fairsharing.org/FAIRsharing.WWI10U) -compliant way. A generic step-by-step guide for designing a metadata
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
