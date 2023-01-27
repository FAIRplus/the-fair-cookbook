(fcb-interop-vcf_fhir)=
# Converting VCF file to HL7 FHIR JSON Genomic Report profile 


````{panels_fairplus}
```` 

## Main Objectives

The main purpose of this recipe is to provide FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) guidance relevant to the clinical domain by:

> - providing a tool to convert Variant Call Files (VCF(URL_TO_INSERT_RECORD http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41)) to a HL7(URL_TO_INSERT_RECORD http://www.hl7.org/implement/standards/product_brief.cfm?product_id=186) FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) message
> - highlighting known limitations of the solution
> - raising awareness of the FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) in the context of clinically relevant data. 
> - discussing the benefits of obtaining genetic variation informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion in a regularized form and available in a well-known syntax.

## Graphical Overview


````{dropdown} 
```{figure} vcf2fhir-json-overview.png
---
width: 1200px
name: Converting a VCF(URL_TO_INSERT_RECORD http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41) open standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) file to a HL7(URL_TO_INSERT_RECORD http://www.hl7.org/implement/standards/product_brief.cfm?product_id=186) FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ted payload
alt: Converting a VCF(URL_TO_INSERT_RECORD http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41) open standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) file to a HL7(URL_TO_INSERT_RECORD http://www.hl7.org/implement/standards/product_brief.cfm?product_id=186) FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ted payload
---
Context for a scenario requiring converting a VCF(URL_TO_INSERT_RECORD http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41) open standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) file to a HL7(URL_TO_INSERT_RECORD http://www.hl7.org/implement/standards/product_brief.cfm?product_id=186) FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ted payload.
```
````


## User Stories

The table below lists relevant use cases.

|As a ..| I want to .. |So that I can ..|
|---|--|--|
|Data owner| Convert VCF(URL_TO_INSERT_RECORD http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41) to a FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) message| Produce an informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion payload carrying patient genotyping informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion in a standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)ized format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) compatible with EHR|
|Data consumer| Integrate patient genetic informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion| Have seamless integration with other FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) messages from other sources| 
|Data manager| Unify clinical informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion in one format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)| Facilitate reuse and mining by clinicians|

---

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [Format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) conversion](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/operation_3434)  | [FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) format](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.25k4yp)  | Conversion results, Error report  |


## Table of Data Standards

| Data Format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s  | Terminologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) | Model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s  |
| :------------- | :------------- | :------------- |
| [VCF](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/format_3016)  | |
| [BCF](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/format_3020)  | |
| [FHIR](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.25k4yp)  | |
| [Compressed Format](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/format_4006)| |
||[LOINC(URL_TO_INSERT_RECORD https://loinc.org/)](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.2mk2zb)||
---

The `Variant Call File` or [VCF](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/format_3016) is a file format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) specified by the [Global Alliance for Genomic Health](https://www.ga4gh.org/genomic-data-toolkit/) to report on genetic variation as detected by a range of molecular biology techniques (e.g., PC(URL_TO_INSERT_RECORD http://www.pathwaycommons.org)R, GeneChip, nucleic acid sequencing). 
It is considered to be the _de facto_ standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) for reporting genetic variations in their various forms. It is therefore the output for most genetic analysis pipelines (e.g., the [Galaxy Worflow](https://toolshed.g2.bx.psu.edu/) tool [`affy2vcf`](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/gregvonkuster/galaxy_tools/tree/master/tools/convert_formats/affy2vcf) )

The latest version of `Variant Call File` format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) is v4.3, the detailed specifications of which can be found [here](http://samtools.github.io/hts-specs/VCFv4.3.pdf) 

The VCF(URL_TO_INSERT_RECORD http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41) format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) is species agnostic, making it suitable for use in any context, from agronomy to clinical practice. In fact, it is this last use case that this particular recipe will be focusing on. Indeed, this is when bioinformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ics meets medical informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ics and the need to translate data into different format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) arises. In the world of clinical informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ics, exchanging informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion between systems increasingly relies on Health Level 7 data standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s and in particular on the Fast Healthcare Interoperability Resource (FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html)). A number of working groups focus on how to best fit clinical informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion within the paradigm of the HL7(URL_TO_INSERT_RECORD http://www.hl7.org/implement/standards/product_brief.cfm?product_id=186) FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) representation.

In this FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) Cookbook(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059) recipe, we will highlight a software component allowing to convert a specific type of genetic variation informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion stored in VCF(URL_TO_INSERT_RECORD http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41) files into an HL7(URL_TO_INSERT_RECORD http://www.hl7.org/implement/standards/product_brief.cfm?product_id=186) FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) compliant, JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ed message. 

The aptly named `vcf2fhir` library is a python package designed to perform this task. It is the result of work recently published by Dolin et al, 2021. {footcite}`pmid33653260`.


```{warning}
```





### Requirements

Users should be at ease with command line interfaces.

In order for the `vcf2fhir` python library to run, the following libraries need to be present on the system.

|Software|Description|Version|
|--|--|--|
|[cython](https://cython.org/)|C-Extensions for Python |0.29.24
|[wheel](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/nunofonseca/fastq_utils)| wheel|0.37.0
|[wget](https://www.gnu.org/software/wget/)|File downloader|1.19.4|


Users running a python environment (virtual or otherwise) need to install `cython` and `wheel`, which respectively provide C-implemented extensions for speed and a code packaging library which allows installations to run without the need for building and compiling. The 'wget' component will be used to obtain test files from a web address via a command line call.

Both python modules can be installed with a single invokation of the python installation `pip` command as follows:

```bash
```


### Installing `vcf2fhir` python library:

Since the `vcf2fhir` is available from [pypi.org](https://pypi.org), we can also install the vcf2fhir binary using `pip`.

```bash
```



### Using `vcf2fhir` package:

In order to use the `VCF(URL_TO_INSERT_RECORD http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41) to FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) converter` function provided by the library, one needs to first obtain VCF(URL_TO_INSERT_RECORD http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41) files.
Not only that, but as we indicated in the introduction, the version of the VCF(URL_TO_INSERT_RECORD http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41) files should be at least v4.1. Furthermore, they should be such that they contain only `simple variant` informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion and not `structural variants` (a type of genetic variations which aren't currently supported by the `vcf2fhir` library).

```{admonition} Note
```

Obtaining an exemplar VCF(URL_TO_INSERT_RECORD http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41) file from the [vcf2fhir github(URL_TO_INSERT_RECORD https://github.com/) repository](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/elimuinformatics/vcf2fhir) using the `wget` command:

```bash
```


```bash

```

will show the following:

```
##fileformat=VCFv4.1
#CHROM  POS ID  REF ALT QUAL    FILTER  INFO    FORMAT  TEST001

```



### Conversion from VCF to FHIR

The conversion command can be issued as follows:


```python


```

The result of the conversion is a so-called `FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) Genomics report`, the specifications of which are available [here](http://hl7.org/fhir/uv/genomics-reporting/index.html). A number of options are available from the converter to allow users to modify and tune the output to contains specific informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion depending on the use cases. The conversion can be restricted to a subset of records found in a VCF(URL_TO_INSERT_RECORD http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41) file by specifying particular portions, e.g., conversion regions, studied regions, clinical annotations, or uncallable regions.

For a full and detailed overview of these options, we direct the readers to the [original manual](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/elimuinformatics/vcf2fhir/blob/master/docs/Manual.md) for the `vcf2fhir` library.

Depending on the options specified by the user, different types of 'FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) genomics report' may be generated. They will differ in content and layout but all rely on a number of normative patterns and terminologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) (e.g. LOINC(URL_TO_INSERT_RECORD https://loinc.org/)).

* Create FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) Diagnostic Report
* Create RegionStudied observations
* Create Variant observations
* Create SequencePhaseRelationship observations
* Create DiagnosticImplication observations 


More examples to instantiate the converter

-  Converts all variants in VCF(URL_TO_INSERT_RECORD http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41). FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) report contains no region-studied observation.

```python
```

-  Converts all variants in VCF(URL_TO_INSERT_RECORD http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41). FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) report assign homoplasmic vs. heteroplasmic based on:

   If allelic depth (FO(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO)RMA(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/gxd/ma_ontology/)T (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/MAT?p=summary).AD)/ read depth (FO(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO)RMA(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/gxd/ma_ontology/)T (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/MAT?p=summary).DP) is greater than 0.89 then allelic state is homoplasmic; otherwise, it is heteroplasmic.

   **Note** : the default value of ratio_ad_dp = 0.99 and the ratio_ad_dp is considered valid only when its value lies between 0 and 1.

```python
```

-  Submitting only noncallable region without other regions generates an error.

```python
```

-  Converts all variants in VCF(URL_TO_INSERT_RECORD http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41). FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) report contains one region-studied observation per studied chromosome.

```python
```

-  Converts all variants in VCF(URL_TO_INSERT_RECORD http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41). FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) report contains one region-studied observation per studied chromosome.

```python
```

-  Converts all variants in conversion region. FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) report contains no region-studied observation.

```python
```

-  Submitting only noncallable region without other regions generates an error.

```python
```

-  Converts all variants in conversion region. FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) report contains one region-studied observation per studied chromosome, intersected with
   conversion region.

```python
```

-  Converts all variants in conversion region. FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) report contains one region-studied observation per studied chromosome, intersected with
   conversion region.

```python
```

-  Conversion of a bgzipped(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) VCF(URL_TO_INSERT_RECORD http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41)

```python
```

Below is a typical output of the `vcf2fhir` tool: a HL7(URL_TO_INSERT_RECORD http://www.hl7.org/implement/standards/product_brief.cfm?product_id=186) FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) message compliant with the Genomics Report pattern. 
Note the use of [LOINC](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.2mk2zb) terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) for key descriptors.


```JSON

```



#### Built-in Support Conversion Error Logging

No conversion tool is failsafe. Therefore, the `vcf2fhir` library provides 2 distinct logging functions, which plug naturally into the python generic error logging package.

-  **vcf2fhir.general**: this mode provides the standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) library logging functions. 

-  **vcf2fhir.invalidrecord**: this mode logs all the `records` from the input vcf file which are in present in the `conversion region` but are not converted to `fhir format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)`.


To take advantage of this mechanism, users can invoke each of the `vcf2fhir` loggers in the manner described below:


```python


# create logger

# create console handler and set level to debug

# create formatter
# add formatter to ch
# add ch to logger

```



### Take home message from using the `vcf2fhir` python library

* an `initial capability` supporting generation of `HL7(URL_TO_INSERT_RECORD http://www.hl7.org/implement/standards/product_brief.cfm?product_id=186) FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) Genomics Report message` from VCF(URL_TO_INSERT_RECORD http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41) files.
* generation of LOINC(URL_TO_INSERT_RECORD https://loinc.org/)-annotated, JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ted documents containing simple genetic variation informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion.
* availability of a conversion error log, for quality control and error tracking tasks.



 
## Conclusion


**Why does this matter and how does it relate to FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)?**

The conversion from VCF(URL_TO_INSERT_RECORD http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41) to HL7(URL_TO_INSERT_RECORD http://www.hl7.org/implement/standards/product_brief.cfm?product_id=186) FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) message has to do with the `**I and R**` of `FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)`, that is `interoperability` and `reusability`.
- From a syntactic standpoint, the availability of genetic variation informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion at a granular level in an easily parseable form (JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259)) is a gain for anyone looking at merging this informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion with other clinical messages.
- From a semantic standpoint, the reliance on `LOINC(URL_TO_INSERT_RECORD https://loinc.org/)` vocabulary to mark up the patterns defined in the HL7(URL_TO_INSERT_RECORD http://www.hl7.org/implement/standards/product_brief.cfm?product_id=186) FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) Genomics Reports enhances interoperation between systems by provided unambiguous annotations.
- Finally, as more systems are able to produce FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) messages from a variety of instruments or data sources, the availability of a FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) message covering a subset of genetic variation available from testing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) facilities makes investigating and mining phenotypic and genotypic relations more straightforward.
- However, one needs to remember that the capability afforded by the `vcf2fhir` library is at an early stage and only supports simple cases. More efforts and more efforts is needed before a functionality is available at a Technical Readiness Level compatible with production systems.

**Any other important issues?**

- We have highlighted the existing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) limitations surrounding the use of the open source conversion tool and that users should **carefully** assess the nature of the informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion present in the input VCF(URL_TO_INSERT_RECORD http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41) files prior to executing the code. Bearing this in mind, the `vcf2fhir` tool provides an easy to deploy and easy to use solution for anyone interested in adding a FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) message capability to a clinical genetic analysis pipeline,for instance on consuming DNA microarray GeneChip genotyping solutions. The authors of the tool aim to expand its capabilities to include `enhancing the conversion logic to accommodate VCF(URL_TO_INSERT_RECORD http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41) rows representing structural variants (i.e. rows that contain an INFO(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO).SVT(URL_TO_INSERT_RECORD https://github.com/AnimalGenome/vertebrate-trait-ontology)YPE(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/PE) field)`.

- Finally, it is important to realize that the resulting JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) message, as it is, lacks important metadata to be fully and properly FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) (e.g., `licence informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion`). One has therefore to see this `capability` as one of the many elements that needs to be put together to build and deliver a FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) infrastructure. For instance, this HL7(URL_TO_INSERT_RECORD http://www.hl7.org/implement/standards/product_brief.cfm?product_id=186) JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) message could be embedded in a more complex system, which would package informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion and deliver a FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) payload.



### What to read next?

- [From Electronic Health Records Notes to FHIR](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/FAIRplus/the-fair-cookbook/blob/mzml-format/docs/content/recipes/interoperability/EHRN2FHIR.md) 
- Pistoia Alliance FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)4Clinical Guidance - An Introduction
- Pistoia Alliance FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)4Clin - Metadata
- [HL7(URL_TO_INSERT_RECORD http://www.hl7.org/implement/standards/product_brief.cfm?product_id=186) FHIR(URL_TO_INSERT_RECORD https://www.hl7.org/fhir/index.html) for FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) implementation guideline (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=reporting_guideline)s](https://build.fhir.org/ig/HL7/fhir-for-fair/index.html)

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
