(fcb-interop-txmetadata)=
# Metadata profile for transcriptomics


````{panels_fairplus}
```` 

## Main Objectives:

The main purpose of this recipe is:

> To provide guidance on the minimum set of metadata and semantics required to describe any transcriptomics experiments,
> from standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) case-control to dosage-response designs, and from microarrays to single cell RNA sequencing. 


### Who is this recipe aimed at?

This document is aimed at anyone interested in the metadata, and specifically the ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) annotations, required to capture variables and experimental factors related to a transcriptomics experiment. General knowledge of transcriptomics experiments would be beneficial. No specific technical knowledge is required.


---

## Transcriptomics Data model 

Large sections of any transcriptomics data model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) are not unique to transcriptomics experiments but are common to a wide range of experiments in the biomedical domain. This includes general project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project)- and sample-level informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion, which will be briefly covered in this recipe but will also be covered in more depth elsewhere.

Where possible, metadata should be map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ped(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) to ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) to maximise the FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)ness of any dataset. This recipe will suggest possible ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) for metadata fields where these are available. These lists may however not be exhaustive as new ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) emerge regularly.

### Existing standards and checklists

A set of well-established standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s and minimum metadata checklists exist for various aspects of transcriptomics. They include:

Minimum Informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion About a Microarray Experiment(URL_TO_INSERT_RECORD http://www.fged.org/projects/miame/) (MIAME(URL_TO_INSERT_RECORD http://www.fged.org/projects/miame/)) - MIAME(URL_TO_INSERT_RECORD http://www.fged.org/projects/miame/) is intended to specify all the informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion necessary for an unambiguous interpretation of a microarray experiment, and potentially to reproduce it. MIAME(URL_TO_INSERT_RECORD http://www.fged.org/projects/miame/) defines the content but not the format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) for this informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion. The MIAME(URL_TO_INSERT_RECORD http://www.fged.org/projects/miame/) standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) has been in existence for over 20 years and has been widely adopted across the scientific community. The data model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s of the major transcriptomics repositories (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository) such as ArrayExpress(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/arrayexpress/)(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/arrayexpress/), the Expression Atlas(URL_TO_INSERT_RECORD http://www.ebi.ac.uk/gxa)(URL_TO_INSERT_RECORD http://www.ebi.ac.uk/gxa) and the Gene Expression Omnibus(URL_TO_INSERT_RECORD https://www.ncbi.nlm.nih.gov/geo/) (GEO(URL_TO_INSERT_RECORD https://www.ncbi.nlm.nih.gov/geo/)(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/EO:0007359)(URL_TO_INSERT_RECORD https://github.com/ufbmi/geographical-entity-ontology)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/EO)) are MIAME(URL_TO_INSERT_RECORD http://www.fged.org/projects/miame/)-compliant.

Minimum Informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion about a high-throughput nucleotide SEQuencing Experiment (MINSEQE(URL_TO_INSERT_RECORD https://doi.org/10.5281/zenodo.5706412)) - MINSEQE(URL_TO_INSERT_RECORD https://doi.org/10.5281/zenodo.5706412) describes the minimum metadata that is needed to enable the unambiguous interpretation and facilitate reproduction of the results of the experiment. By analogy to the MIAME(URL_TO_INSERT_RECORD http://www.fged.org/projects/miame/) guideline (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=reporting_guideline)s for microarray experiments, adherence to the MINSEQE(URL_TO_INSERT_RECORD https://doi.org/10.5281/zenodo.5706412) guideline (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=reporting_guideline)s will improve integration of multiple experiments across different modalities, thereby maximising the value of high-throughput research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/). MINSEQE(URL_TO_INSERT_RECORD https://doi.org/10.5281/zenodo.5706412) has been integrated into a number of transcriptomics and sequencing arch(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ives.

Functional Annotation of Animal Genomes (FAANG) - FAANG provides a set of orthogonal standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s for the capture of well-structured metadata for experiments, samples and analyses in the animal genomics domain. The FAANG standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s support the MIAME(URL_TO_INSERT_RECORD http://www.fged.org/projects/miame/) and MINSEQE(URL_TO_INSERT_RECORD https://doi.org/10.5281/zenodo.5706412) guideline (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=reporting_guideline)s, and aim to convert them to a concrete specification.

Human Cell Atlas Metadata (HC(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/1020)A-Metadata) - the HC(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/1020)A metadata model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) provides a concrete specification for capturing the metadata for single cell sequencing experiments. It is based on the three standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s above, while focusing on the specific requirements of the single cell space.

### Minimum metadata vs desirable metadata

A minimum metadata set constitutes metadata items that always need to be supplied with any experimental data. For validation purposes, these should not be omittable. Desirable or recommended metadata items on the other hand should be supplied if available but will not cause a validation failure if absent. 

### Common metadata

Common metadata include any informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion that is not specific to transcriptomics experiments but applies to most experiments in the biomedical domain. They include:

- Project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project) level metadata
- Common sample level metadata such as species, tissue, cell type etc.


#### Suggested metadata fields

The following table contains a non-exhaustive list of suggested minimum metadata fields for biological samples. The collection (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=collection) is based on a range of existing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) metadata standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s, including MIAME(URL_TO_INSERT_RECORD http://www.fged.org/projects/miame/), MINSEQE(URL_TO_INSERT_RECORD https://doi.org/10.5281/zenodo.5706412), FAANG and HC(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/1020)A. Field(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/1369)s were included if they occurred in at least two of the standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s.

|Metadata field|Required?|Definition|Comment|
|--------|--------|--------|--------|
|unique ID|required|Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) for a sample that is at least unique within the project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project)||
|sample type|required|The type of the collected specimen, eg tissue biopsy, blood draw or throat swab|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. OBI(URL_TO_INSERT_RECORD http://obi-ontology.org/) or EFO(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO)|
|species|required|The primary species of the specimen, preferably the taxonomic identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)|This may not be the same as the "host" organism, eg in the case of a PDX tissue sample, the host may be a mouse but the tissue may be human. Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field - NCBITaxonomy|
|tissue/organism part|required|The tissue from which the sample was taken|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. Uberon|
|disease|required|Any diseases that may affect the sample|This may not necessarily be the same as the host's disease, eg healthy brain tissue might be collected from a host with type II diabetes while cirrhotic liver tissue might be collected from an otherwise healthy individual. Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field - e.g. MO(URL_TO_INSERT_RECORD http://mged.sourceforge.net/ontologies/MGEDontology.php)NDO(URL_TO_INSERT_RECORD https://github.com/monarch-initiative/monarch-disease-ontology) or DO|
|sex|required|The biological/genetic sex of the sample|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. PATO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)(URL_TO_INSERT_RECORD http://purl.bioontology.org/ontology/ATO)(URL_TO_INSERT_RECORD https://github.com/pato-ontology/pato/)|
|development stage|required|The developmental stage of the sample|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. Uberon or Hsadpdv; species dependent|
|collection (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=collection) date|required|The date on which the sample was collected, in a standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)ised format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)|Collection (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=collection) date in combination with other fields such as location and disease may be sufficient to de-anonymise a sample|
|external accessions|recommended|Accession numbers from any external resources to which the sample was submitted|eg Biosamples, Biostudies(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/biostudies/)|
|strain|recommended|Strain of the species from which the sample was collected, if applicable|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. NCBITaxonomy|
|ancestry/ethnicity|recommended|Ancestry or ethnic group of the individual from which the sample was collected|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. HANCESTRO(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD https://github.com/EBISPOT/ancestro)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD https://w3id.org/ro/)|
|age |recommended|Age of the organism from which the sample was collected||
|age unit|recommended|Unit of the value of the age field|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. UO(URL_TO_INSERT_RECORD https://github.com/bio-ontology-research-group/unit-ontology)|
|BMI|recommended|Body mass index of the individual from which the sample was collected|Only applies to human samples|
|treatment category|recommended|Treatments that the sample might have undergone after collection (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=collection)|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. OBI(URL_TO_INSERT_RECORD http://obi-ontology.org/), NCIt(URL_TO_INSERT_RECORD https://ncit.nci.nih.gov) or OGMS(URL_TO_INSERT_RECORD https://github.com/OGMS/ogms)|
|cell type|recommended|The cell type(s) known or selected to be present in the sample|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. CL(URL_TO_INSERT_RECORD https://github.com/obophenotype/cell-ontology)|
|growth conditions|recommended|Features relating to the growth and/or maintenance of the sample||
|genetic variation|recommended|Any relevant genetic differences from the specimen or sample to the expected genomic informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion for this species, eg abnormal chromosome counts, major translocations or indels||
|sample collection (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=collection) technique|recommended|The technique used to collect the specimen, eg blood draw or surgical resection|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. EFO(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO) or OBI(URL_TO_INSERT_RECORD http://obi-ontology.org/)|
|phenotype|recommended|Any relevant (usually abnormal) phenotypes of the specimen or sample |`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. HP(URL_TO_INSERT_RECORD https://hpo.jax.org/) or MP(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/mp_ontology); species dependent|
|cell cycle|recommended|The cell cycle phase of the sample (for synchronized growing cells or a single-cell sample), if known|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. GO(URL_TO_INSERT_RECORD http://www.geneontology.org)|
|cell location|recommended|The cell location from which genetic material was collected (usually either nucleus or mitochondria)|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. GO(URL_TO_INSERT_RECORD http://www.geneontology.org)|


### Assay metadata

Assay-level metadata covers any metadata directly related to the preparation of the biomaterial undergoing the assay and the process of performing the assay. Most, though not all, of this metadata is specific to transcriptomics. Examples include:
- Library informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion, including what sample the library was originally derived from and whether any replicates are biological or technical
- Process (wet experiment) metadata
- Technology type (e.g. bulk RNA-Seq, scRNA-Seq, CITE-Seq)
- Instrument metadata
- Other assay-specific metadata
- QC informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion
- Workflow metadata

The figure below shows an excerpt of the Human Cell Atlas json schema for describing the process of sequencing. 


````{dropdown}
```{figure} hca_sequencing_json_schema.png
---
name: human cell atlas sequencing json schema
alt: human cell atlas sequencing json schema.
---
human cell atlas sequencing json schema.
```
````

```{note}



```

````{dropdown}
```{figure} hca_library_amplification_ontology_json_schema.png
---
name: hca_library_amplification_ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)_json_schema
alt: hca_library_amplification_ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)_json_schema.
---
human cell atlas sequencing json schema.
```
````

```{note}
```

#### Suggested metadata fields

The following table contains a non-exhaustive list of suggested minimum metadata fields for assays. The collection (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=collection) is based on a range of existing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) metadata standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s, including MIAME(URL_TO_INSERT_RECORD http://www.fged.org/projects/miame/), MINSEQE(URL_TO_INSERT_RECORD https://doi.org/10.5281/zenodo.5706412) and HC(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/1020)A. This list can and should be further broken down based on specific technologies used, such as microarrays or whole genome sequencing.

|Metadata field|Required?|Definition|Comment|
|--------|--------|--------|--------|
|unique ID|required|Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) for the assay that is at least unique within the project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project)||
|experiment type|required|The type of experiment performed, eg ATAC(URL_TO_INSERT_RECORD https://ac.tdwg.org/introduction/)-seq or seqFISH|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. EFO(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO) or OBI(URL_TO_INSERT_RECORD http://obi-ontology.org/)|
|extracted nucleic acid/material type|required|The type of material that was extracted from the sample, eg polyA RNA|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. ChEBI(URL_TO_INSERT_RECORD http://www.ebi.ac.uk/chebi/) or EFO(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO)|
|platform|required|The type of instrument used to perform the assay, eg Illumina HiSeq 4000 or Fluidigm C1 microfluidics platform|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. EFO(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO) or OBI(URL_TO_INSERT_RECORD http://obi-ontology.org/)|
|nucleic acid extraction method|required|Technique used to extract the nucleic acid from the cell|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. EFO(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO) or OBI(URL_TO_INSERT_RECORD http://obi-ontology.org/)|
|cDNA library amplication method|required|Technique used to amplify a cDNA library|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. EFO(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO) or OBI(URL_TO_INSERT_RECORD http://obi-ontology.org/)|
|array or sequencing method|required|The array or sequencing technology used - may be the same as `experiment type` or can be a more specific term|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. EFO(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO) or OBI(URL_TO_INSERT_RECORD http://obi-ontology.org/)|
|biological or technical replicate|required|Informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion whether the sample on which the assay was performed was biological or technical replicate.|boolean or CV|
|end bias|required|The type of tag or end bias the library has, eg 3 prime tag or 5 prime end bias|standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)ised field or ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)|
|external accessions|recommended|Accession numbers from external resources to which assay or protocol informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion was submitted|eg protocols.io(URL_TO_INSERT_RECORD https://protocols.io/welcome), AE|
|instrument model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)|required|The specific instrument on which the assay was performed. Essential for QC purposes.|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. EFO(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO) or OBI(URL_TO_INSERT_RECORD http://obi-ontology.org/)|
|assay start time|recommended|The exact time at which the assay was started||
|assay end time|recommended|The exact time at which the assay was completed||
|assay duration|recommended|The duration, in a relevant time unit (eg minutes or hours), of the assay from start to finish||
|array quality|recommended|The overall quality of the array||
|chemical compound|recommended|Any relevant chemical compounds used in the assay|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. ChEBI(URL_TO_INSERT_RECORD http://www.ebi.ac.uk/chebi/)|
|labeling molecule used|recommended|The type of labeling molecule used in an array-based experiment|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. ChEBI(URL_TO_INSERT_RECORD http://www.ebi.ac.uk/chebi/)|
|spike-in kit used|recommended|Informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion about the spike-in kit used during sequencing library preparation||
|cDNA primer|recommended|Type of primer used for cDNA synthesis from RNA, eg polyA or random|standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)ised field or ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)|
|library strandedness|recommended|The strandedness of the cDNA library |standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)ised field or ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)|
|cell quality|recommended|Informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion about the quality of a single cell such as morphology or percent viability|standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)ised field or ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)|
|cell barcode|recommended|Informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion about the cell identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) barcode used to tag individual cells in single cell sequencing||
|UMI barcode|recommended|Informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion about the Unique Molecular Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) barcodes used to tag DNA fragments||

### Analysis metadata

Analysis-level metadata includes any metadata related to the files that come out of the experiment, from the sequencing or imaging files generated directly by the machine to files generated during the various stages of processing and analysis, as well as details of any analyses performed. It is very important to always capture versions of software and reference genomes used in order to allow accurate replication of results. Analysis metadata includes
- Type of analysis
- File format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s, e.g. BAM(URL_TO_INSERT_RECORD http://genome.ucsc.edu/goldenPath/help/bam.html), fastq or gene count
- File location e.g. URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)
- Summarisation of data, e.g. enrichment analysis

#### Suggested metadata fields

The following table contains a non-exhaustive list of suggested minimum metadata fields for analyses. The collection (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=collection) is based on a range of existing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) metadata standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s, including MIAME(URL_TO_INSERT_RECORD http://www.fged.org/projects/miame/), MINSEQE(URL_TO_INSERT_RECORD https://doi.org/10.5281/zenodo.5706412) and HC(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/1020)A. This list can and should be further broken down based on the specific analysis type (primary, secondary or teriatry analysis, meta-analysis etc)

|Metadata field|Required?|Definition|Comment|
|--------|--------|--------|--------|
|analysis type|required|The type of analysis performed, eg genome assembly or variant calling  |`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. EFO(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO), OBI(URL_TO_INSERT_RECORD http://obi-ontology.org/) or EDAM(URL_TO_INSERT_RECORD http://edamontology.org)|
|computational method|required|The specific computational method or algorithm used as part of the analysis|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. EFO(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO) or EDAM(URL_TO_INSERT_RECORD http://edamontology.org)|
|normalisation strategy|required|The approach used to normalise the data|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. EFO(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO) or EDAM(URL_TO_INSERT_RECORD http://edamontology.org)|
|file format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)|required|The file format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) in which the analysis is provided|`ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) field` - e.g. EDAM(URL_TO_INSERT_RECORD http://edamontology.org)|
|file storage location|required|The location in which the data files are stored||
|software package|recommended|The software package used for data analysis||
|software version|recommended|The exact version number of the software package ||
|analysis date|recommended|The date on which the analysis was performed||
|read index|recommended|The sequencing read a specific file represents, eg read1 or index1||
|read length|recommended|The length of a sequenced read in this file, in nucleotides.||
|assembly type|recommended|The assembly type of the genome reference file, eg primary, complete or patch assembly.|standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)ised field or ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)|
|reference genome version|recommended|The genome version of the reference file.||

## Ontologies for transcriptomics data

While it is essential that any transcriptomics metadata be annotated with ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) terms wherever possible, there is no absolute set of ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) that must be used above all others. There is however a consensus set of ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and other standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)ised resources that are commonly used in transcriptomics metadata, including in the main data arch(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ives. The most commonly used ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and fields they apply to are listed below. This table represents an absolute minimum of ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) annotations that should be included in a transcriptomics metadata set for it to be considered as FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/). Not all fields suggested for ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) annotation in the previous section are repeated here for this reason.

|Data type|Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)/Entity sources|Type|Notes|
|---|---|---|---|
|Species |NCBI taxonomy(URL_TO_INSERT_RECORD https://www.ncbi.nlm.nih.gov/taxonomy) Scientific name + ID|Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)||
|Tissue |Uberon term and Id|Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)||
|Cell type| CL(URL_TO_INSERT_RECORD https://github.com/obophenotype/cell-ontology) term and Id|Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)||
|Disease|MO(URL_TO_INSERT_RECORD http://mged.sourceforge.net/ontologies/MGEDontology.php)NDO(URL_TO_INSERT_RECORD https://github.com/monarch-initiative/monarch-disease-ontology), DO or MeSH|Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)|no single solution - options vary depending on resource and individual requirements |
|Phenotype/Trait|HP(URL_TO_INSERT_RECORD https://hpo.jax.org/)O(URL_TO_INSERT_RECORD http://plantontology.org/) (human),  MP(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/mp_ontology)(other mammals), various others for model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) organisms (yeast, zebrafish, Xenopus, C. elegans)|Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)||
|Experiment Type|EFO(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO), OBI(URL_TO_INSERT_RECORD http://obi-ontology.org/)|Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)| e.g. RNASeq, CITES(URL_TO_INSERT_RECORD https://tes.jpl.nasa.gov/data)eq etc. - |
|Cell location/cycle| GO(URL_TO_INSERT_RECORD http://www.geneontology.org)|Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)||
|Developmental stage|HSAPD(URL_TO_INSERT_RECORD https://wangapd3.com/main.php)V(URL_TO_INSERT_RECORD https://github.com/obophenotype/developmental-stage-ontologies/wiki/HsapDv)/Uberon|Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)||
|Chemical compound| ChEBI(URL_TO_INSERT_RECORD http://www.ebi.ac.uk/chebi/)|Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)||
|Chemical compound| UniChem, SMILE, InChi|Entity||
|Gene/protein|ENSEMB(URL_TO_INSERT_RECORD http://www.Metabase.net)L(URL_TO_INSERT_RECORD http://www.ensembl.org/), ENTR(URL_TO_INSERT_RECORD https://www.trialregister.nl/)EZ_GENE, UNIPRO(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD http://www.sparontologies.net/ontologies/pro)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD https://proconsortium.org/)(URL_TO_INSERT_RECORD https://w3id.org/ro/)T, HGNC(URL_TO_INSERT_RECORD https://www.genenames.org/)(URL_TO_INSERT_RECORD https://www.genenames.org/) ID, INSD(URL_TO_INSERT_RECORD https://nsd.no/en/)C(URL_TO_INSERT_RECORD http://dublincore.org/documents/dces/)(URL_TO_INSERT_RECORD https://doi.org/10.25504/FAIRsharing.3nx7t)|Entity||
|Metabolites| MetaboLights(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/metabolights/) compound accession, ChEBI(URL_TO_INSERT_RECORD http://www.ebi.ac.uk/chebi/)|Entity||
|Nucleotide reference sequence|ReqSeq|Entity||


## Conclusion

Using common transcriptomics metadata standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s, in particular the fields listed above as guidance, it is possible to
easily define a comprehensive metadata template to capture all the experimental variables to describe any 
transcriptomics experiment in a FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)-compliant way. A generic step-by-step guide for designing a metadata
template is provided [here](creating-minimal-metadata-profiles.md)

````{dropdown} **References**
````

## Authors

<!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO clarify the contribution of Karsten and Peter -->
````{authors_fairplus}
````


## License
````{license_fairplus}
````
