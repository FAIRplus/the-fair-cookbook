(fcb-interop-vcf_fhir)=
# Converting VCF file to HL7 FHIR JSON Genomic Report profile 


````{panels_fairplus}
:identifier_text: FCB058
:identifier_link: 'https://w3id.org/faircookbook/FCB058'
:difficulty_level: 2
:recipe_type: hands_on
:reading_time_minutes: 15
:intended_audience: principal_investigator, data_manager, data_scientist  
:maturity_level: 2
:maturity_indicator: 1, 2
:has_executable_code: yeah
:recipe_name: Expressing Clinical Genetic Information as FHIR JSON
```` 

## Main Objectives

The main purpose of this recipe is to provide FAIR (URL_TO_INSERT_RECORD-ABBREV_2875 https://fairsharing.org/FAIRsharing.WWI10U)  guidance relevant to the clinical domain by:

> - providing a tool to convert Variant Call Files (VCF (URL_TO_INSERT_RECORD-ABBREV_2877 https://fairsharing.org/FAIRsharing.cfzz0h) ) to a HL7 (URL_TO_INSERT_RECORD-ABBREV_2878 https://fairsharing.org/FAIRsharing.ka5tfc)  FHIR (URL_TO_INSERT_RECORD-ABBREV_2876 https://fairsharing.org/FAIRsharing.25k4yp)  message
> - highlighting known limitations of the solution
> - raising awareness of the FHIR (URL_TO_INSERT_RECORD-ABBREV_2880 https://fairsharing.org/FAIRsharing.25k4yp)  standard (URL_TO_INSERT_TERM_2879 https://fairsharing.org/search?fairsharingRegistry=Standard)  in the context of clinically relevant data. 
> - discussing the benefits of obtaining genetic variation informat (URL_TO_INSERT_TERM_2881 https://fairsharing.org/search?recordType=model_and_format) ion in a regularized form and available in a well-known syntax.

## Graphical Overview


````{dropdown} 
:open:
```{figure} vcf2fhir-json-overview.png
---
width: 1200px
name: Converting a VCF (URL_TO_INSERT_RECORD-ABBREV_2885 https://fairsharing.org/FAIRsharing.cfzz0h)  open standard (URL_TO_INSERT_TERM_2882 https://fairsharing.org/search?fairsharingRegistry=Standard)  file to a HL7 (URL_TO_INSERT_RECORD-ABBREV_2886 https://fairsharing.org/FAIRsharing.ka5tfc)  FHIR (URL_TO_INSERT_RECORD-ABBREV_2884 https://fairsharing.org/FAIRsharing.25k4yp)  format (URL_TO_INSERT_TERM_2883 https://fairsharing.org/search?recordType=model_and_format) ted payload
alt: Converting a VCF (URL_TO_INSERT_RECORD-ABBREV_2890 https://fairsharing.org/FAIRsharing.cfzz0h)  open standard (URL_TO_INSERT_TERM_2887 https://fairsharing.org/search?fairsharingRegistry=Standard)  file to a HL7 (URL_TO_INSERT_RECORD-ABBREV_2891 https://fairsharing.org/FAIRsharing.ka5tfc)  FHIR (URL_TO_INSERT_RECORD-ABBREV_2889 https://fairsharing.org/FAIRsharing.25k4yp)  format (URL_TO_INSERT_TERM_2888 https://fairsharing.org/search?recordType=model_and_format) ted payload
---
Context for a scenario requiring converting a VCF (URL_TO_INSERT_RECORD-ABBREV_2895 https://fairsharing.org/FAIRsharing.cfzz0h)  open standard (URL_TO_INSERT_TERM_2892 https://fairsharing.org/search?fairsharingRegistry=Standard)  file to a HL7 (URL_TO_INSERT_RECORD-ABBREV_2896 https://fairsharing.org/FAIRsharing.ka5tfc)  FHIR (URL_TO_INSERT_RECORD-ABBREV_2894 https://fairsharing.org/FAIRsharing.25k4yp)  format (URL_TO_INSERT_TERM_2893 https://fairsharing.org/search?recordType=model_and_format) ted payload.
```
````


## User Stories

The table below lists relevant use cases.

|As a ..| I want to .. |So that I can ..|
|---|--|--|
|Data owner| Convert VCF (URL_TO_INSERT_RECORD-ABBREV_2902 https://fairsharing.org/FAIRsharing.cfzz0h)  to a FHIR (URL_TO_INSERT_RECORD-ABBREV_2901 https://fairsharing.org/FAIRsharing.25k4yp)  message| Produce an informat (URL_TO_INSERT_TERM_2898 https://fairsharing.org/search?recordType=model_and_format) ion payload carrying patient genotyping informat (URL_TO_INSERT_TERM_2899 https://fairsharing.org/search?recordType=model_and_format) ion in a standard (URL_TO_INSERT_TERM_2897 https://fairsharing.org/search?fairsharingRegistry=Standard) ized format (URL_TO_INSERT_TERM_2900 https://fairsharing.org/search?recordType=model_and_format)  compatible with EHR|
|Data consumer| Integrate patient genetic informat (URL_TO_INSERT_TERM_2903 https://fairsharing.org/search?recordType=model_and_format) ion| Have seamless integration with other FHIR (URL_TO_INSERT_RECORD-ABBREV_2904 https://fairsharing.org/FAIRsharing.25k4yp)  messages from other sources| 
|Data manager| Unify clinical informat (URL_TO_INSERT_TERM_2905 https://fairsharing.org/search?recordType=model_and_format) ion in one format (URL_TO_INSERT_TERM_2906 https://fairsharing.org/search?recordType=model_and_format) | Facilitate reuse and mining by clinicians|

---

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [Format conversion](http://edamontology.org/operation_3434)  | [FHIR (URL_TO_INSERT_RECORD-ABBREV_2907 https://fairsharing.org/FAIRsharing.25k4yp)  format](https://fairsharing.org/FAIRsharing.25k4yp)  | Conversion results, Error report  |


## Table of Data Standards

| Data Format (URL_TO_INSERT_TERM_2909 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_2910 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_2908 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
| [VCF](http://edamontology.org/format_3016)  | |
| [BCF](http://edamontology.org/format_3020)  | |
| [FHIR](https://fairsharing.org/FAIRsharing.25k4yp)  | |
| [Compressed Format](http://edamontology.org/format_4006)| |
||[LOINC](https://fairsharing.org/FAIRsharing.2mk2zb)||
---

The `Variant Call File` or [VCF](http://edamontology.org/format_3016) is a file format (URL_TO_INSERT_TERM_2911 https://fairsharing.org/search?recordType=model_and_format)  specified by the [Global Alliance for Genomic Health](https://www.ga4gh.org/genomic-data-toolkit/) to report on genetic variation as detected by a range of molecular biology techniques (e.g., PCR, GeneChip, nucleic acid sequencing). 
It is considered to be the _de facto_ standard (URL_TO_INSERT_TERM_2912 https://fairsharing.org/search?fairsharingRegistry=Standard)  for reporting genetic variations in their various forms. It is therefore the output for most genetic analysis pipelines (e.g., the [Galaxy Worflow](https://toolshed.g2.bx.psu.edu/) tool [`affy2vcf`](https://github.com/gregvonkuster/galaxy_tools/tree/master/tools/convert_formats/affy2vcf) )

The latest version of `Variant Call File` format (URL_TO_INSERT_TERM_2913 https://fairsharing.org/search?recordType=model_and_format)  is v4.3, the detailed specifications of which can be found [here](http://samtools.github.io/hts-specs/VCFv4.3.pdf) 

The VCF (URL_TO_INSERT_RECORD-ABBREV_2924 https://fairsharing.org/FAIRsharing.cfzz0h)  format (URL_TO_INSERT_TERM_2915 https://fairsharing.org/search?recordType=model_and_format)  is species agnostic, making it suitable for use in any context, from agronomy to clinical practice. In fact, it is this last use case that this particular recipe will be focusing on. Indeed, this is when bioinformat (URL_TO_INSERT_TERM_2916 https://fairsharing.org/search?recordType=model_and_format) ics meets medical informat (URL_TO_INSERT_TERM_2917 https://fairsharing.org/search?recordType=model_and_format) ics and the need to translate data into different format (URL_TO_INSERT_TERM_2918 https://fairsharing.org/search?recordType=model_and_format)  arises. In the world of clinical informat (URL_TO_INSERT_TERM_2919 https://fairsharing.org/search?recordType=model_and_format) ics, exchanging informat (URL_TO_INSERT_TERM_2920 https://fairsharing.org/search?recordType=model_and_format) ion between systems increasingly relies on Health Level 7 data standard (URL_TO_INSERT_TERM_2914 https://fairsharing.org/search?fairsharingRegistry=Standard) s and in particular on the Fast Healthcare Interoperability Resource (FHIR (URL_TO_INSERT_RECORD-ABBREV_2922 https://fairsharing.org/FAIRsharing.25k4yp) ). A number of working groups focus on how to best fit clinical informat (URL_TO_INSERT_TERM_2921 https://fairsharing.org/search?recordType=model_and_format) ion within the paradigm of the HL7 (URL_TO_INSERT_RECORD-ABBREV_2925 https://fairsharing.org/FAIRsharing.ka5tfc)  FHIR (URL_TO_INSERT_RECORD-ABBREV_2923 https://fairsharing.org/FAIRsharing.25k4yp)  representation.

In this FAIR (URL_TO_INSERT_RECORD-ABBREV_2930 https://fairsharing.org/FAIRsharing.WWI10U)  Cookbook recipe, we will highlight a software component allowing to convert a specific type of genetic variation informat (URL_TO_INSERT_TERM_2926 https://fairsharing.org/search?recordType=model_and_format) ion stored in VCF (URL_TO_INSERT_RECORD-ABBREV_2931 https://fairsharing.org/FAIRsharing.cfzz0h)  files into an HL7 (URL_TO_INSERT_RECORD-ABBREV_2932 https://fairsharing.org/FAIRsharing.ka5tfc)  FHIR (URL_TO_INSERT_RECORD-ABBREV_2928 https://fairsharing.org/FAIRsharing.25k4yp)  compliant, JSON (URL_TO_INSERT_RECORD-ABBREV_2929 https://fairsharing.org/FAIRsharing.5bbab9)  format (URL_TO_INSERT_TERM_2927 https://fairsharing.org/search?recordType=model_and_format) ed message. 

The aptly named `vcf2fhir` library is a python package designed to perform this task. It is the result of work recently published by Dolin et al, 2021. {footcite}`pmid33653260`.


```{warning}
In its current form, `vcf2fhir` :
 - supports `simple variants` (SNVs, MNVs, Indels)
 - **does not** support `structural variants`
 - This software is not intended for use in production systems
 - This software is mainly a prototype for evaluation, testing and refinement of the conversion process and the FHIR message payload
 - This software does not deal with patient reidentification issues, which needs to be carefully considered if dealing with real patient data, and not test data.
```





### Requirements

Users should be at ease with command line interfaces.

In order for the `vcf2fhir` python library to run, the following libraries need to be present on the system.

|Software|Description|Version|
|--|--|--|
|[cython](https://cython.org/)|C-Extensions for Python |0.29.24
|[wheel](https://github.com/nunofonseca/fastq_utils)| wheel|0.37.0
|[wget](https://www.gnu.org/software/wget/)|File downloader|1.19.4|


Users running a python environment (virtual or otherwise) need to install `cython` and `wheel`, which respectively provide C-implemented extensions for speed and a code packaging library which allows installations to run without the need for building and compiling. The 'wget' component will be used to obtain test files from a web address via a command line call.

Both python modules can be installed with a single invokation of the python installation `pip` command as follows:

```bash
pip install cython wheel
```


### Installing `vcf2fhir` python library:

Since the `vcf2fhir` is available from [pypi.org](https://pypi.org), we can also install the vcf2fhir binary using `pip`.

```bash
pip install vcf2fhir
```



### Using `vcf2fhir` package:

In order to use the `VCF (URL_TO_INSERT_RECORD-ABBREV_2934 https://fairsharing.org/FAIRsharing.cfzz0h)  to FHIR (URL_TO_INSERT_RECORD-ABBREV_2933 https://fairsharing.org/FAIRsharing.25k4yp)  converter` function provided by the library, one needs to first obtain VCF (URL_TO_INSERT_RECORD-ABBREV_2935 https://fairsharing.org/FAIRsharing.cfzz0h)  files.
Not only that, but as we indicated in the introduction, the version of the VCF (URL_TO_INSERT_RECORD-ABBREV_2937 https://fairsharing.org/FAIRsharing.cfzz0h)  files should be at least v4.1. Furthermore, they should be such that they contain only `simple variant` informat (URL_TO_INSERT_TERM_2936 https://fairsharing.org/search?recordType=model_and_format) ion and not `structural variants` (a type of genetic variations which aren't currently supported by the `vcf2fhir` library).

```{admonition} Note
:class: tip
*  The following section shows how to download VCF files available from public location, the VCF2FHIR github repository in this instance. 
```

Obtaining an exemplar VCF (URL_TO_INSERT_RECORD-ABBREV_2938 https://fairsharing.org/FAIRsharing.cfzz0h)  file from the [vcf2fhir github repository](https://github.com/elimuinformatics/vcf2fhir) using the `wget` command:

```bash
wget -c https://raw.githubusercontent.com/elimuinformatics/vcf2fhir/master/vcf2fhir/test/vcf_example1.vcf
```


```bash
more vcf_example1

```

will show the following:

```
##fileformat=VCFv4.1
#CHROM  POS ID  REF ALT QUAL    FILTER  INFO    FORMAT  TEST001
1   15  .   .   G   .   .   .   GT:PS   0/1:.
1   16  .   A,T G   .   .   .   GT:PS   0/1:.
1   17  .   A   G   .   27  .   GT:PS   0/1:.
1   18  .   A   G   .   .   SVTYPE=INV  GT:PS   0/1:.
1   20  .       G   .   .   .   GT:PS   0/1:.
1   25  .   A   G   .   .   .   PS  .
1   26  .   A   G   .   .   .   GT:PS   ./.:.
1   27  .   A   G   .   .   .   GT:PS   .|.:.
1   28  .   A   <CGA_CNVWIN>    .   .   .   GT:PS   0/1:.
chr1    301 .   A   G   .   .   .   GT:PS   0/1:.
1   400 .   A   G   .   .   .   GT:PS   1/1:.
1   500 .   A   G   .   PASS    .   GT:PS   0|1:500
1   600 .   A   G   .   .   .   GT:PS   1|0:500
1   700 .   A   G   .   .   .   GT:PS   0|1:700

```



### Conversion from VCF to FHIR

The conversion command can be issued as follows:


```python
import vcf2fhir

vcf_fhir_converter = vcf2fhir.Converter('vcf_example1.vcf', 'GRCh37')
vcf_fhir_converter.convert()

```

The result of the conversion is a so-called `FHIR (URL_TO_INSERT_RECORD-ABBREV_2940 https://fairsharing.org/FAIRsharing.25k4yp)  Genomics report`, the specifications of which are available [here](http://hl7.org/fhir/uv/genomics-reporting/index.html). A number of options are available from the converter to allow users to modify and tune the output to contains specific informat (URL_TO_INSERT_TERM_2939 https://fairsharing.org/search?recordType=model_and_format) ion depending on the use cases. The conversion can be restricted to a subset of records found in a VCF (URL_TO_INSERT_RECORD-ABBREV_2941 https://fairsharing.org/FAIRsharing.cfzz0h)  file by specifying particular portions, e.g., conversion regions, studied regions, clinical annotations, or uncallable regions.

For a full and detailed overview of these options, we direct the readers to the [original manual](https://github.com/elimuinformatics/vcf2fhir/blob/master/docs/Manual.md) for the `vcf2fhir` library.

Depending on the options specified by the user, different types of 'FHIR (URL_TO_INSERT_RECORD-ABBREV_2943 https://fairsharing.org/FAIRsharing.25k4yp)  genomics report' may be generated. They will differ in content and layout but all rely on a number of normative patterns and terminologies (URL_TO_INSERT_TERM_2942 https://fairsharing.org/search?recordType=terminology_artefact)  (e.g. LOINC (URL_TO_INSERT_RECORD-ABBREV_2944 https://fairsharing.org/FAIRsharing.2mk2zb) ).

* Create FHIR (URL_TO_INSERT_RECORD-ABBREV_2945 https://fairsharing.org/FAIRsharing.25k4yp)  Diagnostic Report
* Create RegionStudied observations
* Create Variant observations
* Create SequencePhaseRelationship observations
* Create DiagnosticImplication observations 


More examples to instantiate the converter

-  Converts all variants in VCF (URL_TO_INSERT_RECORD-ABBREV_2947 https://fairsharing.org/FAIRsharing.cfzz0h) . FHIR (URL_TO_INSERT_RECORD-ABBREV_2946 https://fairsharing.org/FAIRsharing.25k4yp)  report contains no region-studied observation.

```python
vcf2fhir.Converter('vcftests.vcf','GRCh37', 'aabc')
```

-  Converts all variants in VCF (URL_TO_INSERT_RECORD-ABBREV_2949 https://fairsharing.org/FAIRsharing.cfzz0h) . FHIR (URL_TO_INSERT_RECORD-ABBREV_2948 https://fairsharing.org/FAIRsharing.25k4yp)  report assign homoplasmic vs. heteroplasmic based on:

   If allelic depth (FORMAT (URL_TO_INSERT_TERM_2950 https://fairsharing.org/search?recordType=model_and_format) .AD)/ read depth (FORMAT (URL_TO_INSERT_TERM_2951 https://fairsharing.org/search?recordType=model_and_format) .DP) is greater than 0.89 then allelic state is homoplasmic; otherwise, it is heteroplasmic.

   **Note** : the default value of ratio_ad_dp = 0.99 and the ratio_ad_dp is considered valid only when its value lies between 0 and 1.

```python
vcf2fhir.Converter('vcftests.vcf','GRCh37', 'aabc', ratio_ad_dp = 0.89)
```

-  Submitting only noncallable region without other regions generates an error.

```python
vcf2fhir.Converter('vcftests.vcf','GRCh37', 'babc', nocall_filename='WGS_b37_region_noncallable.bed')
```

-  Converts all variants in VCF (URL_TO_INSERT_RECORD-ABBREV_2953 https://fairsharing.org/FAIRsharing.cfzz0h) . FHIR (URL_TO_INSERT_RECORD-ABBREV_2952 https://fairsharing.org/FAIRsharing.25k4yp)  report contains one region-studied observation per studied chromosome.

```python
vcf2fhir.Converter('vcftests.vcf','GRCh37', 'cabc', region_studied_filename='WGS_b37_region_studied.bed')
```

-  Converts all variants in VCF (URL_TO_INSERT_RECORD-ABBREV_2955 https://fairsharing.org/FAIRsharing.cfzz0h) . FHIR (URL_TO_INSERT_RECORD-ABBREV_2954 https://fairsharing.org/FAIRsharing.25k4yp)  report contains one region-studied observation per studied chromosome.

```python
vcf2fhir.Converter('vcftests.vcf','GRCh37', 'dabc', region_studied_filename='WGS_b37_region_studied.bed', nocall_filename='WGS_b37_region_noncallable.bed')
```

-  Converts all variants in conversion region. FHIR (URL_TO_INSERT_RECORD-ABBREV_2956 https://fairsharing.org/FAIRsharing.25k4yp)  report contains no region-studied observation.

```python
vcf2fhir.Converter('vcftests.vcf','GRCh37', 'eabc', conv_region_filename='WGS_b37_convert_everything.bed')
```

-  Submitting only noncallable region without other regions generates an error.

```python
vcf2fhir.Converter('vcftests.vcf','GRCh37', 'fabc', conv_region_filename='WGS_b37_convert_everything.bed', nocall_filename='WGS_b37_region_noncallable.bed')
```

-  Converts all variants in conversion region. FHIR (URL_TO_INSERT_RECORD-ABBREV_2957 https://fairsharing.org/FAIRsharing.25k4yp)  report contains one region-studied observation per studied chromosome, intersected with
   conversion region.

```python
vcf2fhir.Converter('vcftests.vcf','GRCh37', 'gabc', conv_region_filename='WGS_b37_convert_everything.bed', region_studied_filename='WGS_b37_region_studied.bed')
```

-  Converts all variants in conversion region. FHIR (URL_TO_INSERT_RECORD-ABBREV_2958 https://fairsharing.org/FAIRsharing.25k4yp)  report contains one region-studied observation per studied chromosome, intersected with
   conversion region.

```python
vcf2fhir.Converter('vcftests.vcf','GRCh37', 'habc', conv_region_filename='WGS_b37_convert_everything.bed', region_studied_filename='WGS_b37_region_studied.bed', nocall_filename='WGS_b37_region_noncallable.bed')
```

-  Conversion of a bgzipped VCF (URL_TO_INSERT_RECORD-ABBREV_2959 https://fairsharing.org/FAIRsharing.cfzz0h) 

```python
vcf2fhir.Converter('vcf_example4.vcf.gz','GRCh37', 'kabc', has_tabix=True)
```

Below is a typical output of the `vcf2fhir` tool: a HL7 (URL_TO_INSERT_RECORD-ABBREV_2961 https://fairsharing.org/FAIRsharing.ka5tfc)  FHIR (URL_TO_INSERT_RECORD-ABBREV_2960 https://fairsharing.org/FAIRsharing.25k4yp)  message compliant with the Genomics Report pattern. 
Note the use of [LOINC](https://fairsharing.org/FAIRsharing.2mk2zb) terminology (URL_TO_INSERT_TERM_2962 https://fairsharing.org/search?recordType=terminology_artefact)  for key descriptors.


```JSON
{
    "resourceType": "DiagnosticReport",
    "id": "",
    "meta": {
        "profile": [
            "http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/genomics-report"
        ]
    },
    "contained": [
        {
            "resourceType": "Observation",
            "id": "",
            "meta": {
                "profile": [
                    "http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/region-studied"
                ]
            },
            "status": "final",
            "category": [
                {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                            "code": "laboratory"
                        }
                    ]
                }
            ],
            "code": {
                "coding": [
                    {
                        "system": "http://loinc.org",
                        "code": "53041-0",
                        "display": "DNA region of interest panel"
                    }
                ]
            },
            "subject": {
                "reference": "Patient/NB6TK328"
            },
            "component": [
                {
                    "code": {
                        "coding": [
                            {
                                "system": "http://loinc.org",
                                "code": "92822-6",
                                "display": "Genomic coord system"
                            }
                        ]
                    },
                    "valueCodeableConcept": {
                        "coding": [
                            {
                                "system": "http://loinc.org",
                                "code": "LA30102-0",
                                "display": "1-based character counting"
                            }
                        ]
                    }
                },
                {
                    "code": {
                        "coding": [
                            {
                                "system": "http://loinc.org",
                                "code": "48013-7",
                                "display": "Genomic reference sequence ID"
                            }
                        ]
                    },
                    "valueCodeableConcept": {
                        "coding": [
                            {
                                "system": "http://www.ncbi.nlm.nih.gov/nuccore",
                                "code": "NC_000001.11"
                            }
                        ]
                    }
                },
                {
                    "code": {
                        "coding": [
                            {
                                "system": "http://loinc.org",
                                "code": "51959-5",
                                "display": "Range(s) of DNA sequence examined"
                            }
                        ]
                    },
                    "valueRange": {
                        "high": {
                            "value": 201113567.0
                        },
                        "low": {
                            "value": 201038512.0
                        }
                    }
                },
                {
                    "code": {
                        "coding": [
                            {
                                "system": "http://loinc.org",
                                "code": "51959-5",
                                "display": "Range(s) of DNA sequence examined"
                            }
                        ]
                    },
                    "valueRange": {
                        "high": {
                            "value": 201378701.0
                        },
                        "low": {
                            "value": 201358008.0
                        }
                    }
                }
            ]
        }
    ]
}   

```



#### Built-in Support Conversion Error Logging

No conversion tool is failsafe. Therefore, the `vcf2fhir` library provides 2 distinct logging functions, which plug naturally into the python generic error logging package.

-  **vcf2fhir.general**: this mode provides the standard (URL_TO_INSERT_TERM_2963 https://fairsharing.org/search?fairsharingRegistry=Standard)  library logging functions. 

-  **vcf2fhir.invalidrecord**: this mode logs all the `records` from the input vcf file which are in present in the `conversion region` but are not converted to `fhir format (URL_TO_INSERT_TERM_2964 https://fairsharing.org/search?recordType=model_and_format) `.


To take advantage of this mechanism, users can invoke each of the `vcf2fhir` loggers in the manner described below:


```python

import logging

# create logger
logger = logging.getLogger('vcf2fhir.invalidrecord')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.FileHandler('invalidrecord.log')
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)

```



### Take home message from using the `vcf2fhir` python library

* an `initial capability` supporting generation of `HL7 (URL_TO_INSERT_RECORD-ABBREV_2967 https://fairsharing.org/FAIRsharing.ka5tfc)  FHIR (URL_TO_INSERT_RECORD-ABBREV_2965 https://fairsharing.org/FAIRsharing.25k4yp)  Genomics Report message` from VCF (URL_TO_INSERT_RECORD-ABBREV_2966 https://fairsharing.org/FAIRsharing.cfzz0h)  files.
* generation of LOINC (URL_TO_INSERT_RECORD-ABBREV_2971 https://fairsharing.org/FAIRsharing.2mk2zb) -annotated, JSON (URL_TO_INSERT_RECORD-ABBREV_2970 https://fairsharing.org/FAIRsharing.5bbab9)  format (URL_TO_INSERT_TERM_2968 https://fairsharing.org/search?recordType=model_and_format) ted documents containing simple genetic variation informat (URL_TO_INSERT_TERM_2969 https://fairsharing.org/search?recordType=model_and_format) ion.
* availability of a conversion error log, for quality control and error tracking tasks.



 
## Conclusion


**Why does this matter and how does it relate to FAIR (URL_TO_INSERT_RECORD-ABBREV_2972 https://fairsharing.org/FAIRsharing.WWI10U) ?**

The conversion from VCF (URL_TO_INSERT_RECORD-ABBREV_2976 https://fairsharing.org/FAIRsharing.cfzz0h)  to HL7 (URL_TO_INSERT_RECORD-ABBREV_2977 https://fairsharing.org/FAIRsharing.ka5tfc)  FHIR (URL_TO_INSERT_RECORD-ABBREV_2973 https://fairsharing.org/FAIRsharing.25k4yp)  JSON (URL_TO_INSERT_RECORD-ABBREV_2974 https://fairsharing.org/FAIRsharing.5bbab9)  message has to do with the `**I and R**` of `FAIR (URL_TO_INSERT_RECORD-ABBREV_2975 https://fairsharing.org/FAIRsharing.WWI10U) `, that is `interoperability` and `reusability`.
- From a syntactic standpoint, the availability of genetic variation informat (URL_TO_INSERT_TERM_2978 https://fairsharing.org/search?recordType=model_and_format) ion at a granular level in an easily parseable form (JSON (URL_TO_INSERT_RECORD-ABBREV_2980 https://fairsharing.org/FAIRsharing.5bbab9) ) is a gain for anyone looking at merging this informat (URL_TO_INSERT_TERM_2979 https://fairsharing.org/search?recordType=model_and_format) ion with other clinical messages.
- From a semantic standpoint, the reliance on `LOINC (URL_TO_INSERT_RECORD-ABBREV_2982 https://fairsharing.org/FAIRsharing.2mk2zb) ` vocabulary to mark up the patterns defined in the HL7 (URL_TO_INSERT_RECORD-ABBREV_2983 https://fairsharing.org/FAIRsharing.ka5tfc)  FHIR (URL_TO_INSERT_RECORD-ABBREV_2981 https://fairsharing.org/FAIRsharing.25k4yp)  Genomics Reports enhances interoperation between systems by provided unambiguous annotations.
- Finally, as more systems are able to produce FHIR (URL_TO_INSERT_RECORD-ABBREV_2984 https://fairsharing.org/FAIRsharing.25k4yp)  messages from a variety of instruments or data sources, the availability of a FHIR (URL_TO_INSERT_RECORD-ABBREV_2985 https://fairsharing.org/FAIRsharing.25k4yp)  message covering a subset of genetic variation available from testing facilities makes investigating and mining phenotypic and genotypic relations more straightforward.
- However, one needs to remember that the capability afforded by the `vcf2fhir` library is at an early stage and only supports simple cases. More efforts and more efforts is needed before a functionality is available at a Technical Readiness Level compatible with production systems.

**Any other important issues?**

- We have highlighted the existing limitations surrounding the use of the open source conversion tool and that users should **carefully** assess the nature of the informat (URL_TO_INSERT_TERM_2986 https://fairsharing.org/search?recordType=model_and_format) ion present in the input VCF (URL_TO_INSERT_RECORD-ABBREV_2988 https://fairsharing.org/FAIRsharing.cfzz0h)  files prior to executing the code. Bearing this in mind, the `vcf2fhir` tool provides an easy to deploy and easy to use solution for anyone interested in adding a FHIR (URL_TO_INSERT_RECORD-ABBREV_2987 https://fairsharing.org/FAIRsharing.25k4yp)  message capability to a clinical genetic analysis pipeline,for instance on consuming DNA microarray GeneChip genotyping solutions. The authors of the tool aim to expand its capabilities to include `enhancing the conversion logic to accommodate VCF (URL_TO_INSERT_RECORD-ABBREV_2989 https://fairsharing.org/FAIRsharing.cfzz0h)  rows representing structural variants (i.e. rows that contain an INFO.SVTYPE field)`.

- Finally, it is important to realize that the resulting JSON (URL_TO_INSERT_RECORD-ABBREV_2992 https://fairsharing.org/FAIRsharing.5bbab9)  message, as it is, lacks important metadata to be fully and properly FAIR (URL_TO_INSERT_RECORD-ABBREV_2994 https://fairsharing.org/FAIRsharing.WWI10U)  (e.g., `licence informat (URL_TO_INSERT_TERM_2990 https://fairsharing.org/search?recordType=model_and_format) ion`). One has therefore to see this `capability` as one of the many elements that needs to be put together to build and deliver a FAIR (URL_TO_INSERT_RECORD-ABBREV_2995 https://fairsharing.org/FAIRsharing.WWI10U)  infrastructure. For instance, this HL7 (URL_TO_INSERT_RECORD-ABBREV_2997 https://fairsharing.org/FAIRsharing.ka5tfc)  JSON (URL_TO_INSERT_RECORD-ABBREV_2993 https://fairsharing.org/FAIRsharing.5bbab9)  message could be embedded in a more complex system, which would package informat (URL_TO_INSERT_TERM_2991 https://fairsharing.org/search?recordType=model_and_format) ion and deliver a FAIR (URL_TO_INSERT_RECORD-ABBREV_2996 https://fairsharing.org/FAIRsharing.WWI10U)  payload.



### What to read next?

- [From Electronic Health Records Notes to FHIR](https://github.com/FAIRplus/the-fair-cookbook/blob/mzml-format/docs/content/recipes/interoperability/EHRN2FHIR.md) 
- Pistoia Alliance FAIR4Clinical Guidance - An Introduction
- Pistoia Alliance FAIR4Clin - Metadata
- [HL7 FHIR for FAIR implementation guidelines](https://build.fhir.org/ig/HL7/fhir-for-fair/index.html)

````{rdmkit_panel}
````

## References
````{dropdown} **References**
```{footbibliography}
```
````

## Authors
````{authors_fairplus}
Philippe: Writing - Original Draft
Vassilios: Writing - Review & Editing
Danielle: Writing - Review & Editing
````

## License
````{license_fairplus}
CC-BY-4.0
````
