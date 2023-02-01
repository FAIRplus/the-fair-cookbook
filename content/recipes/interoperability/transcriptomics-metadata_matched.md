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
> from standard (URL_TO_INSERT_TERM_8946 https://fairsharing.org/search?fairsharingRegistry=Standard)  case-control to dosage-response designs, and from microarrays to single cell RNA sequencing. 


### Who is this recipe aimed at?

This document is aimed at anyone interested in the metadata, and specifically the ontology (URL_TO_INSERT_TERM_8947 https://fairsharing.org/search?recordType=terminology_artefact)  annotations, required to capture variables and experimental factors related to a transcriptomics experiment. General knowledge of transcriptomics experiments would be beneficial. No specific technical knowledge is required.


---

## Transcriptomics Data model 

Large sections of any transcriptomics data model (URL_TO_INSERT_TERM_8949 https://fairsharing.org/search?recordType=model_and_format)  are not unique to transcriptomics experiments but are common to a wide range of experiments in the biomedical domain. This includes general project (URL_TO_INSERT_TERM_8948 https://fairsharing.org/search?recordType=project) - and sample-level informat (URL_TO_INSERT_TERM_8950 https://fairsharing.org/search?recordType=model_and_format) ion, which will be briefly covered in this recipe but will also be covered in more depth elsewhere.

Where possible, metadata should be map (URL_TO_INSERT_RECORD_8954 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_8956 https://fairsharing.org/FAIRsharing.31385c)  to ontologies (URL_TO_INSERT_TERM_8951 https://fairsharing.org/search?recordType=terminology_artefact)  to maximise the FAIR (URL_TO_INSERT_RECORD_8955 https://fairsharing.org/FAIRsharing.WWI10U) ness of any dataset. This recipe will suggest possible ontologies (URL_TO_INSERT_TERM_8952 https://fairsharing.org/search?recordType=terminology_artefact)  for metadata fields where these are available. These lists may however not be exhaustive as new ontologies (URL_TO_INSERT_TERM_8953 https://fairsharing.org/search?recordType=terminology_artefact)  emerge regularly.

### Existing standards and checklists

A set of well-established standard (URL_TO_INSERT_TERM_8957 https://fairsharing.org/search?fairsharingRegistry=Standard) s and minimum metadata checklists exist for various aspects of transcriptomics. They include:

Minimum Informat (URL_TO_INSERT_TERM_8961 https://fairsharing.org/search?recordType=model_and_format) ion About a Microarray Experiment (URL_TO_INSERT_RECORD_8971 https://fairsharing.org/FAIRsharing.32b10v)  (MIAME (URL_TO_INSERT_RECORD_8972 https://fairsharing.org/FAIRsharing.32b10v) ) - MIAME (URL_TO_INSERT_RECORD_8973 https://fairsharing.org/FAIRsharing.32b10v)  is intended to specify all the informat (URL_TO_INSERT_TERM_8962 https://fairsharing.org/search?recordType=model_and_format) ion necessary for an unambiguous interpretation of a microarray experiment, and potentially to reproduce it. MIAME (URL_TO_INSERT_RECORD_8974 https://fairsharing.org/FAIRsharing.32b10v)  defines the content but not the format (URL_TO_INSERT_TERM_8963 https://fairsharing.org/search?recordType=model_and_format)  for this informat (URL_TO_INSERT_TERM_8964 https://fairsharing.org/search?recordType=model_and_format) ion. The MIAME (URL_TO_INSERT_RECORD_8975 https://fairsharing.org/FAIRsharing.32b10v)  standard (URL_TO_INSERT_TERM_8958 https://fairsharing.org/search?fairsharingRegistry=Standard)  has been in existence for over 20 years and has been widely adopted across the scientific community. The data model (URL_TO_INSERT_TERM_8960 https://fairsharing.org/search?recordType=model_and_format) s of the major transcriptomics repositories (URL_TO_INSERT_TERM_8959 https://fairsharing.org/search?recordType=repository)  such as ArrayExpress (URL_TO_INSERT_RECORD_8969 https://fairsharing.org/FAIRsharing.6k0kwd)  (URL_TO_INSERT_RECORD_8970 https://fairsharing.org/FAIRsharing.6k0kwd) , the Expression Atlas (URL_TO_INSERT_RECORD_8978 https://fairsharing.org/FAIRsharing.f5zx00)  (URL_TO_INSERT_RECORD_8979 https://fairsharing.org/FAIRsharing.f5zx00)  and the Gene Expression Omnibus (URL_TO_INSERT_RECORD_8967 https://fairsharing.org/FAIRsharing.5hc8vt)  (GEO (URL_TO_INSERT_RECORD_8965 https://fairsharing.org/FAIRsharing.27rndz)  (URL_TO_INSERT_RECORD_8966 https://fairsharing.org/FAIRsharing.w7a76x)  (URL_TO_INSERT_RECORD_8968 https://fairsharing.org/FAIRsharing.5hc8vt)  (URL_TO_INSERT_RECORD_8977 https://fairsharing.org/FAIRsharing.d1zzym) ) are MIAME (URL_TO_INSERT_RECORD_8976 https://fairsharing.org/FAIRsharing.32b10v) -compliant.

Minimum Informat (URL_TO_INSERT_TERM_8980 https://fairsharing.org/search?recordType=model_and_format) ion about a high-throughput nucleotide SEQuencing Experiment (MINSEQE (URL_TO_INSERT_RECORD_8983 https://fairsharing.org/FAIRsharing.a55z32) ) - MINSEQE (URL_TO_INSERT_RECORD_8984 https://fairsharing.org/FAIRsharing.a55z32)  describes the minimum metadata that is needed to enable the unambiguous interpretation and facilitate reproduction of the results of the experiment. By analogy to the MIAME (URL_TO_INSERT_RECORD_8987 https://fairsharing.org/FAIRsharing.32b10v)  guideline (URL_TO_INSERT_TERM_8981 https://fairsharing.org/search?recordType=reporting_guideline) s for microarray experiments, adherence to the MINSEQE (URL_TO_INSERT_RECORD_8985 https://fairsharing.org/FAIRsharing.a55z32)  guideline (URL_TO_INSERT_TERM_8982 https://fairsharing.org/search?recordType=reporting_guideline) s will improve integration of multiple experiments across different modalities, thereby maximising the value of high-throughput research (URL_TO_INSERT_RECORD_8988 https://fairsharing.org/FAIRsharing.52b22c) . MINSEQE (URL_TO_INSERT_RECORD_8986 https://fairsharing.org/FAIRsharing.a55z32)  has been integrated into a number of transcriptomics and sequencing arch (URL_TO_INSERT_RECORD_8989 https://fairsharing.org/FAIRsharing.52b22c) ives.

Functional Annotation of Animal Genomes (FAANG) - FAANG provides a set of orthogonal standard (URL_TO_INSERT_TERM_8990 https://fairsharing.org/search?fairsharingRegistry=Standard) s for the capture of well-structured metadata for experiments, samples and analyses in the animal genomics domain. The FAANG standard (URL_TO_INSERT_TERM_8991 https://fairsharing.org/search?fairsharingRegistry=Standard) s support the MIAME (URL_TO_INSERT_RECORD_8994 https://fairsharing.org/FAIRsharing.32b10v)  and MINSEQE (URL_TO_INSERT_RECORD_8993 https://fairsharing.org/FAIRsharing.a55z32)  guideline (URL_TO_INSERT_TERM_8992 https://fairsharing.org/search?recordType=reporting_guideline) s, and aim to convert them to a concrete specification.

Human Cell Atlas Metadata (HC (URL_TO_INSERT_RECORD_8997 https://fairsharing.org/FAIRsharing.24yjfc) A-Metadata) - the HC (URL_TO_INSERT_RECORD_8998 https://fairsharing.org/FAIRsharing.24yjfc) A metadata model (URL_TO_INSERT_TERM_8996 https://fairsharing.org/search?recordType=model_and_format)  provides a concrete specification for capturing the metadata for single cell sequencing experiments. It is based on the three standard (URL_TO_INSERT_TERM_8995 https://fairsharing.org/search?fairsharingRegistry=Standard) s above, while focusing on the specific requirements of the single cell space.

### Minimum metadata vs desirable metadata

A minimum metadata set constitutes metadata items that always need to be supplied with any experimental data. For validation purposes, these should not be omittable. Desirable or recommended metadata items on the other hand should be supplied if available but will not cause a validation failure if absent. 

### Common metadata

Common metadata include any informat (URL_TO_INSERT_TERM_8999 https://fairsharing.org/search?recordType=model_and_format) ion that is not specific to transcriptomics experiments but applies to most experiments in the biomedical domain. They include:

- Project (URL_TO_INSERT_TERM_9000 https://fairsharing.org/search?recordType=project)  level metadata
- Common sample level metadata such as species, tissue, cell type etc.


#### Suggested metadata fields

The following table contains a non-exhaustive list of suggested minimum metadata fields for biological samples. The collection (URL_TO_INSERT_TERM_9003 https://fairsharing.org/search?recordType=collection)  is based on a range of existing (URL_TO_INSERT_RECORD_9006 https://fairsharing.org/FAIRsharing.q7bkqr)  metadata standard (URL_TO_INSERT_TERM_9001 https://fairsharing.org/search?fairsharingRegistry=Standard) s, including MIAME (URL_TO_INSERT_RECORD_9007 https://fairsharing.org/FAIRsharing.32b10v) , MINSEQE (URL_TO_INSERT_RECORD_9004 https://fairsharing.org/FAIRsharing.a55z32) , FAANG and HC (URL_TO_INSERT_RECORD_9005 https://fairsharing.org/FAIRsharing.24yjfc) A. Field (URL_TO_INSERT_RECORD_9008 https://fairsharing.org/FAIRsharing.wcfkac) s were included if they occurred in at least two of the standard (URL_TO_INSERT_TERM_9002 https://fairsharing.org/search?fairsharingRegistry=Standard) s.

|Metadata field|Required?|Definition|Comment|
|--------|--------|--------|--------|
|unique ID|required|Identifier (URL_TO_INSERT_TERM_9010 https://fairsharing.org/search?recordType=identifier_schema)  for a sample that is at least unique within the project (URL_TO_INSERT_TERM_9009 https://fairsharing.org/search?recordType=project) ||
|sample type|required|The type of the collected specimen, eg tissue biopsy, blood draw or throat swab|`ontology (URL_TO_INSERT_TERM_9011 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. OBI (URL_TO_INSERT_RECORD_9012 https://fairsharing.org/FAIRsharing.284e1z)  or EFO (URL_TO_INSERT_RECORD_9013 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_9014 https://fairsharing.org/FAIRsharing.ca63ce) |
|species|required|The primary species of the specimen, preferably the taxonomic identifier (URL_TO_INSERT_TERM_9016 https://fairsharing.org/search?recordType=identifier_schema) |This may not be the same as the "host" organism, eg in the case of a PDX tissue sample, the host may be a mouse but the tissue may be human. Ontology (URL_TO_INSERT_TERM_9015 https://fairsharing.org/search?recordType=terminology_artefact)  field - NCBITaxonomy|
|tissue/organism part|required|The tissue from which the sample was taken|`ontology (URL_TO_INSERT_TERM_9017 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. Uberon|
|disease|required|Any diseases that may affect the sample|This may not necessarily be the same as the host's disease, eg healthy brain tissue might be collected from a host with type II diabetes while cirrhotic liver tissue might be collected from an otherwise healthy individual. Ontology (URL_TO_INSERT_TERM_9018 https://fairsharing.org/search?recordType=terminology_artefact)  field - e.g. MO (URL_TO_INSERT_RECORD_9020 https://fairsharing.org/FAIRsharing.qs4x5m) NDO (URL_TO_INSERT_RECORD_9019 https://fairsharing.org/FAIRsharing.b2979t)  or DO|
|sex|required|The biological/genetic sex of the sample|`ontology (URL_TO_INSERT_TERM_9021 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. PATO (URL_TO_INSERT_RECORD_9022 https://fairsharing.org/FAIRsharing.ayjdsm)  (URL_TO_INSERT_RECORD_9023 https://fairsharing.org/FAIRsharing.w69t6r)  (URL_TO_INSERT_RECORD_9024 https://fairsharing.org/FAIRsharing.ezwdhz) |
|development stage|required|The developmental stage of the sample|`ontology (URL_TO_INSERT_TERM_9025 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. Uberon or Hsadpdv; species dependent|
|collection (URL_TO_INSERT_TERM_9027 https://fairsharing.org/search?recordType=collection)  date|required|The date on which the sample was collected, in a standard (URL_TO_INSERT_TERM_9026 https://fairsharing.org/search?fairsharingRegistry=Standard) ised format (URL_TO_INSERT_TERM_9029 https://fairsharing.org/search?recordType=model_and_format) |Collection (URL_TO_INSERT_TERM_9028 https://fairsharing.org/search?recordType=collection)  date in combination with other fields such as location and disease may be sufficient to de-anonymise a sample|
|external accessions|recommended|Accession numbers from any external resources to which the sample was submitted|eg Biosamples, Biostudies (URL_TO_INSERT_RECORD_9030 https://fairsharing.org/FAIRsharing.mtjvme) |
|strain|recommended|Strain of the species from which the sample was collected, if applicable|`ontology (URL_TO_INSERT_TERM_9031 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. NCBITaxonomy|
|ancestry/ethnicity|recommended|Ancestry or ethnic group of the individual from which the sample was collected|`ontology (URL_TO_INSERT_TERM_9032 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. HANCESTRO (URL_TO_INSERT_RECORD_9033 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_9034 https://fairsharing.org/FAIRsharing.rja8qp)  (URL_TO_INSERT_RECORD_9035 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_9036 https://fairsharing.org/FAIRsharing.cp0ybc) |
|age |recommended|Age of the organism from which the sample was collected||
|age unit|recommended|Unit of the value of the age field|`ontology (URL_TO_INSERT_TERM_9037 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. UO (URL_TO_INSERT_RECORD_9038 https://fairsharing.org/FAIRsharing.mjnypw) |
|BMI|recommended|Body mass index of the individual from which the sample was collected|Only applies to human samples|
|treatment category|recommended|Treatments that the sample might have undergone after collection (URL_TO_INSERT_TERM_9039 https://fairsharing.org/search?recordType=collection) |`ontology (URL_TO_INSERT_TERM_9040 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. OBI (URL_TO_INSERT_RECORD_9043 https://fairsharing.org/FAIRsharing.284e1z) , NCIt (URL_TO_INSERT_RECORD_9041 https://fairsharing.org/FAIRsharing.4cvwxa)  or OGMS (URL_TO_INSERT_RECORD_9042 https://fairsharing.org/FAIRsharing.rvz0m9) |
|cell type|recommended|The cell type(s) known or selected to be present in the sample|`ontology (URL_TO_INSERT_TERM_9044 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. CL (URL_TO_INSERT_RECORD_9045 https://fairsharing.org/FAIRsharing.j9y503) |
|growth conditions|recommended|Features relating to the growth and/or maintenance of the sample||
|genetic variation|recommended|Any relevant genetic differences from the specimen or sample to the expected genomic informat (URL_TO_INSERT_TERM_9046 https://fairsharing.org/search?recordType=model_and_format) ion for this species, eg abnormal chromosome counts, major translocations or indels||
|sample collection (URL_TO_INSERT_TERM_9047 https://fairsharing.org/search?recordType=collection)  technique|recommended|The technique used to collect the specimen, eg blood draw or surgical resection|`ontology (URL_TO_INSERT_TERM_9048 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD_9050 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_9051 https://fairsharing.org/FAIRsharing.ca63ce)  or OBI (URL_TO_INSERT_RECORD_9049 https://fairsharing.org/FAIRsharing.284e1z) |
|phenotype|recommended|Any relevant (usually abnormal) phenotypes of the specimen or sample |`ontology (URL_TO_INSERT_TERM_9052 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. HP (URL_TO_INSERT_RECORD_9054 https://fairsharing.org/FAIRsharing.kbtt7f)  or MP (URL_TO_INSERT_RECORD_9053 https://fairsharing.org/FAIRsharing.kg1x4z) ; species dependent|
|cell cycle|recommended|The cell cycle phase of the sample (for synchronized growing cells or a single-cell sample), if known|`ontology (URL_TO_INSERT_TERM_9055 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. GO (URL_TO_INSERT_RECORD_9056 https://fairsharing.org/FAIRsharing.6xq0ee) |
|cell location|recommended|The cell location from which genetic material was collected (usually either nucleus or mitochondria)|`ontology (URL_TO_INSERT_TERM_9057 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. GO (URL_TO_INSERT_RECORD_9058 https://fairsharing.org/FAIRsharing.6xq0ee) |


### Assay metadata

Assay-level metadata covers any metadata directly related to the preparation of the biomaterial undergoing the assay and the process of performing the assay. Most, though not all, of this metadata is specific to transcriptomics. Examples include:
- Library informat (URL_TO_INSERT_TERM_9059 https://fairsharing.org/search?recordType=model_and_format) ion, including what sample the library was originally derived from and whether any replicates are biological or technical
- Process (wet experiment) metadata
- Technology type (e.g. bulk RNA-Seq, scRNA-Seq, CITE-Seq)
- Instrument metadata
- Other assay-specific metadata
- QC informat (URL_TO_INSERT_TERM_9060 https://fairsharing.org/search?recordType=model_and_format) ion
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
name: hca_library_amplification_ontology (URL_TO_INSERT_TERM_9061 https://fairsharing.org/search?recordType=terminology_artefact) _json_schema
alt: hca_library_amplification_ontology (URL_TO_INSERT_TERM_9062 https://fairsharing.org/search?recordType=terminology_artefact) _json_schema.
---
human cell atlas sequencing json schema.
```
````

```{note}
Note how the `ontology` element defines a `graph restriction` pointing to a branch in a semantic resource, (EFO in this case).
```

#### Suggested metadata fields

The following table contains a non-exhaustive list of suggested minimum metadata fields for assays. The collection (URL_TO_INSERT_TERM_9064 https://fairsharing.org/search?recordType=collection)  is based on a range of existing (URL_TO_INSERT_RECORD_9067 https://fairsharing.org/FAIRsharing.q7bkqr)  metadata standard (URL_TO_INSERT_TERM_9063 https://fairsharing.org/search?fairsharingRegistry=Standard) s, including MIAME (URL_TO_INSERT_RECORD_9068 https://fairsharing.org/FAIRsharing.32b10v) , MINSEQE (URL_TO_INSERT_RECORD_9065 https://fairsharing.org/FAIRsharing.a55z32)  and HC (URL_TO_INSERT_RECORD_9066 https://fairsharing.org/FAIRsharing.24yjfc) A. This list can and should be further broken down based on specific technologies used, such as microarrays or whole genome sequencing.

|Metadata field|Required?|Definition|Comment|
|--------|--------|--------|--------|
|unique ID|required|Identifier (URL_TO_INSERT_TERM_9070 https://fairsharing.org/search?recordType=identifier_schema)  for the assay that is at least unique within the project (URL_TO_INSERT_TERM_9069 https://fairsharing.org/search?recordType=project) ||
|experiment type|required|The type of experiment performed, eg ATAC (URL_TO_INSERT_RECORD_9074 https://fairsharing.org/FAIRsharing.md3e78) -seq or seqFISH|`ontology (URL_TO_INSERT_TERM_9071 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD_9073 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_9075 https://fairsharing.org/FAIRsharing.ca63ce)  or OBI (URL_TO_INSERT_RECORD_9072 https://fairsharing.org/FAIRsharing.284e1z) |
|extracted nucleic acid/material type|required|The type of material that was extracted from the sample, eg polyA RNA|`ontology (URL_TO_INSERT_TERM_9076 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. ChEBI (URL_TO_INSERT_RECORD_9077 https://fairsharing.org/FAIRsharing.62qk8w)  or EFO (URL_TO_INSERT_RECORD_9078 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_9079 https://fairsharing.org/FAIRsharing.ca63ce) |
|platform|required|The type of instrument used to perform the assay, eg Illumina HiSeq 4000 or Fluidigm C1 microfluidics platform|`ontology (URL_TO_INSERT_TERM_9080 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD_9082 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_9083 https://fairsharing.org/FAIRsharing.ca63ce)  or OBI (URL_TO_INSERT_RECORD_9081 https://fairsharing.org/FAIRsharing.284e1z) |
|nucleic acid extraction method|required|Technique used to extract the nucleic acid from the cell|`ontology (URL_TO_INSERT_TERM_9084 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD_9086 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_9087 https://fairsharing.org/FAIRsharing.ca63ce)  or OBI (URL_TO_INSERT_RECORD_9085 https://fairsharing.org/FAIRsharing.284e1z) |
|cDNA library amplication method|required|Technique used to amplify a cDNA library|`ontology (URL_TO_INSERT_TERM_9088 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD_9090 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_9091 https://fairsharing.org/FAIRsharing.ca63ce)  or OBI (URL_TO_INSERT_RECORD_9089 https://fairsharing.org/FAIRsharing.284e1z) |
|array or sequencing method|required|The array or sequencing technology used - may be the same as `experiment type` or can be a more specific term|`ontology (URL_TO_INSERT_TERM_9092 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD_9094 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_9095 https://fairsharing.org/FAIRsharing.ca63ce)  or OBI (URL_TO_INSERT_RECORD_9093 https://fairsharing.org/FAIRsharing.284e1z) |
|biological or technical replicate|required|Informat (URL_TO_INSERT_TERM_9096 https://fairsharing.org/search?recordType=model_and_format) ion whether the sample on which the assay was performed was biological or technical replicate.|boolean or CV|
|end bias|required|The type of tag or end bias the library has, eg 3 prime tag or 5 prime end bias|standard (URL_TO_INSERT_TERM_9097 https://fairsharing.org/search?fairsharingRegistry=Standard) ised field or ontology (URL_TO_INSERT_TERM_9098 https://fairsharing.org/search?recordType=terminology_artefact) |
|external accessions|recommended|Accession numbers from external resources to which assay or protocol informat (URL_TO_INSERT_TERM_9099 https://fairsharing.org/search?recordType=model_and_format) ion was submitted|eg protocols.io (URL_TO_INSERT_RECORD_9100 https://fairsharing.org/FAIRsharing.132b10) , AE|
|instrument model (URL_TO_INSERT_TERM_9101 https://fairsharing.org/search?recordType=model_and_format) |required|The specific instrument on which the assay was performed. Essential for QC purposes.|`ontology (URL_TO_INSERT_TERM_9102 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD_9104 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_9105 https://fairsharing.org/FAIRsharing.ca63ce)  or OBI (URL_TO_INSERT_RECORD_9103 https://fairsharing.org/FAIRsharing.284e1z) |
|assay start time|recommended|The exact time at which the assay was started||
|assay end time|recommended|The exact time at which the assay was completed||
|assay duration|recommended|The duration, in a relevant time unit (eg minutes or hours), of the assay from start to finish||
|array quality|recommended|The overall quality of the array||
|chemical compound|recommended|Any relevant chemical compounds used in the assay|`ontology (URL_TO_INSERT_TERM_9106 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. ChEBI (URL_TO_INSERT_RECORD_9107 https://fairsharing.org/FAIRsharing.62qk8w) |
|labeling molecule used|recommended|The type of labeling molecule used in an array-based experiment|`ontology (URL_TO_INSERT_TERM_9108 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. ChEBI (URL_TO_INSERT_RECORD_9109 https://fairsharing.org/FAIRsharing.62qk8w) |
|spike-in kit used|recommended|Informat (URL_TO_INSERT_TERM_9110 https://fairsharing.org/search?recordType=model_and_format) ion about the spike-in kit used during sequencing library preparation||
|cDNA primer|recommended|Type of primer used for cDNA synthesis from RNA, eg polyA or random|standard (URL_TO_INSERT_TERM_9111 https://fairsharing.org/search?fairsharingRegistry=Standard) ised field or ontology (URL_TO_INSERT_TERM_9112 https://fairsharing.org/search?recordType=terminology_artefact) |
|library strandedness|recommended|The strandedness of the cDNA library |standard (URL_TO_INSERT_TERM_9113 https://fairsharing.org/search?fairsharingRegistry=Standard) ised field or ontology (URL_TO_INSERT_TERM_9114 https://fairsharing.org/search?recordType=terminology_artefact) |
|cell quality|recommended|Informat (URL_TO_INSERT_TERM_9116 https://fairsharing.org/search?recordType=model_and_format) ion about the quality of a single cell such as morphology or percent viability|standard (URL_TO_INSERT_TERM_9115 https://fairsharing.org/search?fairsharingRegistry=Standard) ised field or ontology (URL_TO_INSERT_TERM_9117 https://fairsharing.org/search?recordType=terminology_artefact) |
|cell barcode|recommended|Informat (URL_TO_INSERT_TERM_9118 https://fairsharing.org/search?recordType=model_and_format) ion about the cell identifier (URL_TO_INSERT_TERM_9119 https://fairsharing.org/search?recordType=identifier_schema)  barcode used to tag individual cells in single cell sequencing||
|UMI barcode|recommended|Informat (URL_TO_INSERT_TERM_9120 https://fairsharing.org/search?recordType=model_and_format) ion about the Unique Molecular Identifier (URL_TO_INSERT_TERM_9121 https://fairsharing.org/search?recordType=identifier_schema)  barcodes used to tag DNA fragments||

### Analysis metadata

Analysis-level metadata includes any metadata related to the files that come out of the experiment, from the sequencing or imaging files generated directly by the machine to files generated during the various stages of processing and analysis, as well as details of any analyses performed. It is very important to always capture versions of software and reference genomes used in order to allow accurate replication of results. Analysis metadata includes
- Type of analysis
- File format (URL_TO_INSERT_TERM_9122 https://fairsharing.org/search?recordType=model_and_format) s, e.g. BAM (URL_TO_INSERT_RECORD_9123 https://fairsharing.org/FAIRsharing.hza1ec) , fastq or gene count
- File location e.g. URL (URL_TO_INSERT_RECORD_9124 https://fairsharing.org/FAIRsharing.9d38e2) 
- Summarisation of data, e.g. enrichment analysis

#### Suggested metadata fields

The following table contains a non-exhaustive list of suggested minimum metadata fields for analyses. The collection (URL_TO_INSERT_TERM_9126 https://fairsharing.org/search?recordType=collection)  is based on a range of existing (URL_TO_INSERT_RECORD_9129 https://fairsharing.org/FAIRsharing.q7bkqr)  metadata standard (URL_TO_INSERT_TERM_9125 https://fairsharing.org/search?fairsharingRegistry=Standard) s, including MIAME (URL_TO_INSERT_RECORD_9130 https://fairsharing.org/FAIRsharing.32b10v) , MINSEQE (URL_TO_INSERT_RECORD_9127 https://fairsharing.org/FAIRsharing.a55z32)  and HC (URL_TO_INSERT_RECORD_9128 https://fairsharing.org/FAIRsharing.24yjfc) A. This list can and should be further broken down based on the specific analysis type (primary, secondary or teriatry analysis, meta-analysis etc)

|Metadata field|Required?|Definition|Comment|
|--------|--------|--------|--------|
|analysis type|required|The type of analysis performed, eg genome assembly or variant calling  |`ontology (URL_TO_INSERT_TERM_9131 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD_9134 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_9135 https://fairsharing.org/FAIRsharing.ca63ce) , OBI (URL_TO_INSERT_RECORD_9133 https://fairsharing.org/FAIRsharing.284e1z)  or EDAM (URL_TO_INSERT_RECORD_9132 https://fairsharing.org/FAIRsharing.a6r7zs) |
|computational method|required|The specific computational method or algorithm used as part of the analysis|`ontology (URL_TO_INSERT_TERM_9136 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD_9138 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_9139 https://fairsharing.org/FAIRsharing.ca63ce)  or EDAM (URL_TO_INSERT_RECORD_9137 https://fairsharing.org/FAIRsharing.a6r7zs) |
|normalisation strategy|required|The approach used to normalise the data|`ontology (URL_TO_INSERT_TERM_9140 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EFO (URL_TO_INSERT_RECORD_9142 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_9143 https://fairsharing.org/FAIRsharing.ca63ce)  or EDAM (URL_TO_INSERT_RECORD_9141 https://fairsharing.org/FAIRsharing.a6r7zs) |
|file format (URL_TO_INSERT_TERM_9144 https://fairsharing.org/search?recordType=model_and_format) |required|The file format (URL_TO_INSERT_TERM_9145 https://fairsharing.org/search?recordType=model_and_format)  in which the analysis is provided|`ontology (URL_TO_INSERT_TERM_9146 https://fairsharing.org/search?recordType=terminology_artefact)  field` - e.g. EDAM (URL_TO_INSERT_RECORD_9147 https://fairsharing.org/FAIRsharing.a6r7zs) |
|file storage location|required|The location in which the data files are stored||
|software package|recommended|The software package used for data analysis||
|software version|recommended|The exact version number of the software package ||
|analysis date|recommended|The date on which the analysis was performed||
|read index|recommended|The sequencing read a specific file represents, eg read1 or index1||
|read length|recommended|The length of a sequenced read in this file, in nucleotides.||
|assembly type|recommended|The assembly type of the genome reference file, eg primary, complete or patch assembly.|standard (URL_TO_INSERT_TERM_9148 https://fairsharing.org/search?fairsharingRegistry=Standard) ised field or ontology (URL_TO_INSERT_TERM_9149 https://fairsharing.org/search?recordType=terminology_artefact) |
|reference genome version|recommended|The genome version of the reference file.||

## Ontologies for transcriptomics data

While it is essential that any transcriptomics metadata be annotated with ontology (URL_TO_INSERT_TERM_9151 https://fairsharing.org/search?recordType=terminology_artefact)  terms wherever possible, there is no absolute set of ontologies (URL_TO_INSERT_TERM_9154 https://fairsharing.org/search?recordType=terminology_artefact)  that must be used above all others. There is however a consensus set of ontologies (URL_TO_INSERT_TERM_9155 https://fairsharing.org/search?recordType=terminology_artefact)  and other standard (URL_TO_INSERT_TERM_9150 https://fairsharing.org/search?fairsharingRegistry=Standard) ised resources that are commonly used in transcriptomics metadata, including in the main data arch (URL_TO_INSERT_RECORD_9158 https://fairsharing.org/FAIRsharing.52b22c) ives. The most commonly used ontologies (URL_TO_INSERT_TERM_9156 https://fairsharing.org/search?recordType=terminology_artefact)  and fields they apply to are listed below. This table represents an absolute minimum of ontology (URL_TO_INSERT_TERM_9152 https://fairsharing.org/search?recordType=terminology_artefact)  annotations that should be included in a transcriptomics metadata set for it to be considered as FAIR (URL_TO_INSERT_RECORD_9157 https://fairsharing.org/FAIRsharing.WWI10U) . Not all fields suggested for ontology (URL_TO_INSERT_TERM_9153 https://fairsharing.org/search?recordType=terminology_artefact)  annotation in the previous section are repeated here for this reason.

|Data type|Ontology (URL_TO_INSERT_TERM_9159 https://fairsharing.org/search?recordType=terminology_artefact) /Entity sources|Type|Notes|
|---|---|---|---|
|Species |NCBI taxonomy (URL_TO_INSERT_RECORD_9161 https://fairsharing.org/FAIRsharing.fj07xj)  Scientific name + ID|Ontology (URL_TO_INSERT_TERM_9160 https://fairsharing.org/search?recordType=terminology_artefact) ||
|Tissue |Uberon term and Id|Ontology (URL_TO_INSERT_TERM_9162 https://fairsharing.org/search?recordType=terminology_artefact) ||
|Cell type| CL (URL_TO_INSERT_RECORD_9164 https://fairsharing.org/FAIRsharing.j9y503)  term and Id|Ontology (URL_TO_INSERT_TERM_9163 https://fairsharing.org/search?recordType=terminology_artefact) ||
|Disease|MO (URL_TO_INSERT_RECORD_9167 https://fairsharing.org/FAIRsharing.qs4x5m) NDO (URL_TO_INSERT_RECORD_9166 https://fairsharing.org/FAIRsharing.b2979t) , DO or MeSH|Ontology (URL_TO_INSERT_TERM_9165 https://fairsharing.org/search?recordType=terminology_artefact) |no single solution - options vary depending on resource and individual requirements |
|Phenotype/Trait|HP (URL_TO_INSERT_RECORD_9172 https://fairsharing.org/FAIRsharing.kbtt7f) O (URL_TO_INSERT_RECORD_9171 https://fairsharing.org/FAIRsharing.3ngg40)  (human),  MP (URL_TO_INSERT_RECORD_9170 https://fairsharing.org/FAIRsharing.kg1x4z) (other mammals), various others for model (URL_TO_INSERT_TERM_9168 https://fairsharing.org/search?recordType=model_and_format)  organisms (yeast, zebrafish, Xenopus, C. elegans)|Ontology (URL_TO_INSERT_TERM_9169 https://fairsharing.org/search?recordType=terminology_artefact) ||
|Experiment Type|EFO (URL_TO_INSERT_RECORD_9176 https://fairsharing.org/FAIRsharing.1gr4tz)  (URL_TO_INSERT_RECORD_9177 https://fairsharing.org/FAIRsharing.ca63ce) , OBI (URL_TO_INSERT_RECORD_9174 https://fairsharing.org/FAIRsharing.284e1z) |Ontology (URL_TO_INSERT_TERM_9173 https://fairsharing.org/search?recordType=terminology_artefact) | e.g. RNASeq, CITES (URL_TO_INSERT_RECORD_9175 https://fairsharing.org/3025) eq etc. - |
|Cell location/cycle| GO (URL_TO_INSERT_RECORD_9179 https://fairsharing.org/FAIRsharing.6xq0ee) |Ontology (URL_TO_INSERT_TERM_9178 https://fairsharing.org/search?recordType=terminology_artefact) ||
|Developmental stage|HSAPD (URL_TO_INSERT_RECORD_9182 https://fairsharing.org/FAIRsharing.ctwd7b) V (URL_TO_INSERT_RECORD_9181 https://fairsharing.org/FAIRsharing.c6vhm3) /Uberon|Ontology (URL_TO_INSERT_TERM_9180 https://fairsharing.org/search?recordType=terminology_artefact) ||
|Chemical compound| ChEBI (URL_TO_INSERT_RECORD_9184 https://fairsharing.org/FAIRsharing.62qk8w) |Ontology (URL_TO_INSERT_TERM_9183 https://fairsharing.org/search?recordType=terminology_artefact) ||
|Chemical compound| UniChem, SMILE, InChi|Entity||
|Gene/protein|ENSEMB (URL_TO_INSERT_RECORD_9193 https://fairsharing.org/FAIRsharing.a1rp4c) L (URL_TO_INSERT_RECORD_9185 https://fairsharing.org/FAIRsharing.fx0mw7) , ENTR (URL_TO_INSERT_RECORD_9195 https://fairsharing.org/2932) EZ_GENE, UNIPRO (URL_TO_INSERT_RECORD_9186 https://fairsharing.org/FAIRsharing.3e88d6)  (URL_TO_INSERT_RECORD_9189 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_9191 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_9192 https://fairsharing.org/FAIRsharing.4ndncv)  (URL_TO_INSERT_RECORD_9196 https://fairsharing.org/FAIRsharing.cp0ybc) T, HGNC (URL_TO_INSERT_RECORD_9188 https://fairsharing.org/FAIRsharing.amcv1e)  (URL_TO_INSERT_RECORD_9197 https://fairsharing.org/FAIRsharing.29we0s)  ID, INSD (URL_TO_INSERT_RECORD_9187 https://fairsharing.org/FAIRsharing.mKDii0) C (URL_TO_INSERT_RECORD_9190 https://fairsharing.org/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD_9194 https://fairsharing.org/3547) |Entity||
|Metabolites| MetaboLights (URL_TO_INSERT_RECORD_9199 https://fairsharing.org/FAIRsharing.kkdpxe)  compound accession, ChEBI (URL_TO_INSERT_RECORD_9198 https://fairsharing.org/FAIRsharing.62qk8w) |Entity||
|Nucleotide reference sequence|ReqSeq|Entity||


## Conclusion

Using common transcriptomics metadata standard (URL_TO_INSERT_TERM_9200 https://fairsharing.org/search?fairsharingRegistry=Standard) s, in particular the fields listed above as guidance, it is possible to
easily define a comprehensive metadata template to capture all the experimental variables to describe any 
transcriptomics experiment in a FAIR (URL_TO_INSERT_RECORD_9201 https://fairsharing.org/FAIRsharing.WWI10U) -compliant way. A generic step-by-step guide for designing a metadata
template is provided [here](creating-minimal-metadata-profiles.md)

````{dropdown} **References**
````

## Authors

<!-- TO (URL_TO_INSERT_RECORD_9202 https://fairsharing.org/FAIRsharing.w69t6r) DO clarify the contribution of Karsten and Peter -->
````{authors_fairplus}
Danielle: Writing - Review & Editing
Karsten: <!-- TODO -->
Peter: <!-- TODO -->
````


## License
````{license_fairplus}
CC-BY-4.0
````
