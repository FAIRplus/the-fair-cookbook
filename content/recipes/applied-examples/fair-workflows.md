(fcb-fair-workflows)=
# Making Computational Workflows FAIR

+++
<br/>
<br/>

````{panels_fairplus}
:identifier_text: FCBXYZ
:identifier_link: 'https://w3id.org/faircookbook/FCBXYZ'
:difficulty_level: 3
:recipe_type: hands_on
:reading_time_minutes: 15
:intended_audience: principal_investigator, data_manager, data_scientist  
:maturity_level: 2
:maturity_indicator: 1, 2
:has_executable_code: yeah
:recipe_name: FAIR Computational Workflows
```` 


+++
<br/>

## Main Objectives

The main purpose of this recipe is:

> Provide guidance on resources  available to help developers and data scientist make the various workflows
> (for extract-load-transform, quality control, deployment or analytical workflow) available in open format.
> Provide guidance for regulatory submissions for nucleic acid sequence analysis using the BioCompute Object (BCO)
> specification.
> Remind the active nature of the field and the fast evolving environment and platforms developed for these
> tasks, making standardization difficult.
> Provide an example using the Apache Airflow framework to illustrate the progress.


___


## Graphical Overview

Note: use this section to provide a decision tree for the overall process described in the recipe
For more information about the syntax used to generate the diagram, please refer to the
[following documentation](https://mermaid-js.github.io/mermaid/#/flowchart)


```{figure} fair-workflows.png
---
width: 700px
name: fair-workflows
alt: FAIR workflows
---
FAIR workflows
```





## Capability & Maturity Table

This section is meant for authors to describe the specific `capability` which they aim to bring from one `maturity level` to the next.
This is therefore to document the methods used **to enable change** at the level of information process
The table is therefore structure to identify the capability, the **initial** maturity level it is estimated to be and the **final** maturity it has been brought to.


| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Interoperability | minimal | repeatable |


----

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [validation](http://edamontology.org/operation_2428)  | [Common Workflow Language (CWL)](https://fairsharing.org/FAIRsharing.8y5ayx)  | [report](http://edamontology.org/data_2048)  |
| [text annotation](http://edamontology.org/operation_3778)  | [EDAM](https://fairsharing.org/FAIRsharing.a6r7zs)  | [annotated text](http://edamontology.org/data_3779)  |


## Table of Data Standards

Authors should list all the data standards, format specification, syntax and controlled terminologies used in the FAIRification process applied to the IMI project data.
Ideally, authors should mark up the information using either EDAM Ontology URI or FAIRsharing identifiers (which are DOIs)

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| [CWL](https://fairsharing.org/FAIRsharing.8y5ayx) | [EDAM](https://fairsharing.org/FAIRsharing.a6r7zs)  |   |
|[Biocompute Object - IEEE 2791-2020](https://opensource.ieee.org/2791-object/ieee-2791-schema/)|||


## Tools:

|Name | URL| type |
|:--|:--|:--|
|Apache Airflow| [https://airflow.apache.org/](https://airflow.apache.org/) |workflow engine|
|Galaxy| [https://galaxy.aws.biochemistry.gwu.edu/root/login?redirect=%2F](https://galaxy.aws.biochemistry.gwu.edu/root/login?redirect=%2F) |workflow engine|
|Hive| [https://hive.aws.biochemistry.gwu.edu/dna.cgi?cmd=main](https://hive.aws.biochemistry.gwu.edu/dna.cgi?cmd=main) |workflow engine|
|BioCompute Platform| [https://portal.aws.biochemistry.gwu.edu/sign-in](https://portal.aws.biochemistry.gwu.edu/sign-in) |workflow engine|
|SevenBridges BioCompute App| [https://sbg.github.io/biocompute/](https://sbg.github.io/biocompute/) |workflow engine|
|CWL-Airflow| [https://barski-lab.github.io/cwl-airflow/](https://barski-lab.github.io/cwl-airflow/) |adapter|



___

## Main Content

Workflows are ubiquitous is the data science ecosystem. The ability to automate repetitive tasks, thus reducing the 
risk of error associated to human intervention, to build complex pipelines, schedule and distribute tasks to cloud 
infrastructures have popularized the use of workflow engine. Workflow engines such as Galaxy, Snakemake, Cromwell, 
Knime, Apache Airflow, Cavatica and SevenBridge to name a few offerings, have popularized the use of workflows in the 
field of life science computational applications. This can however be source of difficulty when buying in a particular
platform.
Hence, the efforts of the community to define open specifications for the description of workflows as well as converters
between the existing competing offering.

Using an example based on Next Generation Sequencing application, the present content will take the reader through a
number of tools and components in order to help them make workflow more interoperable and reusable thanks to the use of
existing, off the shelf tools.



### CWL: Common Workflow Language

CWL is an open standard developed by a wide consortium, including workflow engine developments, data scientists, 
data analysts and bioinformaticians and is meant to provide for platform-independent workflow description
CWL specifications are available from: https://www.commonwl.org/v1.2/Workflow.html
CWL use YAML syntax to describe workflow steps, tools, input, output and parameters.


```bash
cwlVersion: v1.0
class: Workflow


requirements:
  - class: SubworkflowFeatureRequirement
  - class: ScatterFeatureRequirement
  - class: StepInputExpressionRequirement
  - class: InlineJavascriptRequirement
  - class: MultipleInputFeatureRequirement


inputs:

  indices_folder:
    type: Directory
    label: "BOWTIE indices folder"
    doc: "Path to BOWTIE generated indices folder"

  annotation_file:
    type: File
    label: "Annotation file"
    format: "http://edamontology.org/format_3475"
    doc: "Tab-separated input annotation file"

  genome_size:
    type: string
    label: "Effective genome size"
    doc: "MACS2 effective genome size: hs, mm, ce, dm or number, for example 2.7e9"

  chrom_length:
    type: File
    label: "Chromosome length file"
    format: "http://edamontology.org/format_2330"
    doc: "Chromosome length file"

  control_file:
    type: File?
    default: null
    label: "Control BAM file"
    format: "http://edamontology.org/format_2572"
    doc: "Control BAM file file for MACS2 peak calling"

  fastq_file:
    type: File
    label: "FASTQ input file"
    format: "http://edamontology.org/format_1930"
    doc: "Reads data in a FASTQ format, received after single end sequencing"

...

  remove_duplicates:
    type: boolean?
    default: false
    label: "Remove duplicates"
    doc: "Calls samtools rmdup to remove duplicates from sortesd BAM file"

  threads:
    type: int?
    default: 2
    doc: "Number of threads for those steps that support multithreading"
    label: "Number of threads"

outputs:

  bigwig:
    type: File
    format: "http://edamontology.org/format_3006"
    label: "BigWig file"
    doc: "Generated BigWig file"
    outputSource: bam_to_bigwig/bigwig_file

  fastx_statistics:
    type: File
    label: "FASTQ statistics"
    format: "http://edamontology.org/format_2330"
    doc: "fastx_quality_stats generated FASTQ file quality statistics file"
    outputSource: fastx_quality_stats/statistics_file

  bowtie_log:
    type: File
    label: "BOWTIE alignment log"
    format: "http://edamontology.org/format_2330"
    doc: "BOWTIE generated alignment log"
    outputSource: bowtie_aligner/log_file


steps:

  extract_fastq:
    run: ./tools/extract-fastq.cwl
    in:
      compressed_file: fastq_file
    out: [fastq_file]

  fastx_quality_stats:
    run: ./tools/fastx-quality-stats.cwl
    in:
      input_file: extract_fastq/fastq_file
    out: [statistics_file]

```

* CWL documents can be annotated with schema.org elements to support findability

The block of code below shows how this is done.


```bash
$namespaces:
  s: http://schema.org/

$schemas:
- http://schema.org/docs/schema_org_rdfa.html

s:name: "biowardrobe_chipseq_se"
s:downloadUrl: https://raw.githubusercontent.com/Barski-lab/ga4gh_challenge/master/biowardrobe_chipseq_se.cwl
s:codeRepository: https://github.com/Barski-lab/ga4gh_challenge
s:license: http://www.apache.org/licenses/LICENSE-2.0

s:isPartOf:
  class: s:CreativeWork
  s:name: Common Workflow Language
  s:url: http://commonwl.org/

s:creator:
- class: s:Organization
  s:legalName: "Cincinnati Children's Hospital Medical Center"
  s:location:
  - class: s:PostalAddress
    s:addressCountry: "USA"
    s:addressLocality: "Cincinnati"
    s:addressRegion: "OH"
    s:postalCode: "45229"
    s:streetAddress: "3333 Burnet Ave"
    s:telephone: "+1(513)636-4200"
  s:logo: "https://www.cincinnatichildrens.org/-/media/cincinnati%20childrens/global%20shared/childrens-logo-new.png"
  s:department:
  - class: s:Organization
    s:legalName: "Allergy and Immunology"
    s:department:
    - class: s:Organization
      s:legalName: "Barski Research Lab"
      s:member:
      - class: s:Person
        s:name: Michael Kotliar
        s:email: mailto:misha.kotliar@gmail.com
        s:sameAs:
        - id: http://orcid.org/0000-0002-6486-3898

doc: |
  The workflow is used to run CHIP-Seq basic analysis with single-end input FASTQ file.
  In outputs it returns coordinate sorted BAM file alongside with index BAI file, quality
  statistics of the input FASTQ file, reads coverage in a form of bigWig file, peaks calling
  data in a form of narrowPeak or broadPeak files.

s:about: |
  The workflow is a CWL version of a Python pipeline from BioWardrobe (Kartashov and Barski, 2015).
  It starts by extracting input FASTQ file (in case it was compressed). Next step runs BowTie
  (Langmead et al., 2009) to perform alignment to a reference genome, resulting in an unsorted SAM file.
  The SAM file is then sorted and indexed with samtools (Li et al., 2009) to obtain a BAM file and a BAI index.
  Next MACS2 (Zhang et al., 2008) is used to call peaks and to estimate fragment size. In the last few steps,
  the coverage by estimated fragments is calculated from the BAM file and is reported in bigWig format. The pipeline
  also reports statistics, such as read quality, peak number and base frequency, and other troubleshooting information
  using tools such as fastx-toolkit and bamtools.
```



CWL is currently implemented by an increasing number of platforms, which are listed here

CWL user guide is available here: http://www.commonwl.org/user_guide/

* Conditional Workflow and the `when` keyword:

http://www.commonwl.org/user_guide/24_conditional-workflow/index.html

```bash
class: Workflow
cwlVersion: v1.2
inputs:
  val: int

steps:

  step1:
    in:
      in1: val
      a_new_var: val
    run: foo.cwl
    when: $(inputs.in1 < 1)
    out: [out1]

  step2:
    in:
      in1: val
      a_new_var: val
    run: foo.cwl
    when: $(inputs.a_new_var > 2)
    out: [out1]

outputs:
  out1:
    type: string
    outputSource:
      - step1/out1
      - step2/out1
    pickValue: first_non_null

requirements:
  InlineJavascriptRequirement: {}
  MultipleInputFeatureRequirement: {}
```




### Biocompute Object format, an IEEE specification suited for use in regulatory applications.

If computational analysis on sequence data are performed in the context of clinical trials, for instance to demonstrate
the transcriptomics response to a drug or to show to safety of a compound in populations of distinct genetic background 
using genotyping information, it is a regulatory requirements of the US FDA to submit the computational workflows. 
This has been made possible thanks to the fast track submission of a new data format specifically tailored to ensure
reproducibility and unambiguous description of workflow key descriptors. This is a prerequisite to FDA auditors to
examine the data.
The IEEE 2791-2020, also known as BCO for BioCompute Object is a specification to do this.


```{figure} ./workflow-bco-cloud-tools.png
---
width: 700px
name: Cloud based tools supported BCO specifications
alt: Cloud based tools supported BCO specifications
---
Cloud based tools supported BCO specifications
```

Several tools currently support the BCO format:

* [Hive on AWS](https://hive.aws.biochemistry.gwu.edu/dna.cgi?cmd=main)

* [BioCompute Portal](https://portal.aws.biochemistry.gwu.edu/sign-in)

* [Galaxy on AWS](https://galaxy.aws.biochemistry.gwu.edu/root/login?redirect=%2F)

```{note} Important
A BioCompute Object can be integrated with HL7 FHIR as a Provenance Resource.
```




```{figure} ./workflow-sb-biocompute-app.png
---
width: 700px
name: Seven Bridges Biocompute app
alt: Seven Bridges Biocompute app
---
Seven Bridges Biocompute app.
```



### Publishing Workflows as CWL in WorkflowHub.eu:


Workflows are digital objects which can and should be preserved. A number of repositories exist and may be used to deposit workflows.
One may use a generic repository such as Zenodo to do so (see recipe {ref}`fcb-find-zenodo`).

Alternately, one may use a specialized repository such as [Workflowhub.eu]()


```{figure} workflowhub-eu-1.png
---
width: 700px
name: workflowhub.eu website
alt: workflowhub.eu website
---
The european workflowhub  website.
```



```{figure} ./workflowhub-eu-2.png
---
width: 700px
name: workflowhub.eu website
alt: workflowhub.eu website
---
The european workflowhub website.
```


### Apache AIRflow playing with CWL

Apache Airflow is  `platform created by the community to programmatically author, schedule and monitor workflows` to 
quote the site. It has established itself in industry settings and has broad uptake.
Apache Airflow represents workflows as 'Directed Acyclic Graph' or DAGs and Airflow allows the serialization of these
as JSON documents.
The main thing about Apache Airflow is that code is used to generated the workflows. For more information,
refer to this tutorial: https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html
A tool developed by Michael Kotliar, Andrey V Kartashov, Artem Barski brings CWL support to the Apache Airflow 
framework, meaning that CWL expressed workflow can now be executed on the platform {ref}`Kotliar2019-GigaScience`


```{figure} workflow-cwl-airflow.png
---
width: 700px
name: CWL-Airflow component
alt: CWL-Airflow component
---
the CWL-Airflow component.
```

A key step in this linkage is the conversion of a CWL expressed workflow into an Apache Airflow DAG which can 
then be subsequently executed.
With this example, we aim to bring awareness about the value of having platform independent expression of workflows.



## Conclusion

This recipe focused on highlighting important considerations to bear in mind when dealing with `workflow` as these
digital objects have become essential information carriers to assist data science tasks.
While there is no shortage of tools and frameworks for building, saving, executing `workflow`, making sure these can be
found, interpreted by machine without human intervention and executed are essential aspects of `reusability` and
interoperability. Data Scientists and Information managers should therefore tap into a number of standardization efforts
capable of ensure appropriate provenance tracking and information preservation.
This knowledge could be harnessed to decide whether to trust the results of an analysis or a transformation process,
or to decide whether to perform new ones.

> ### What should I read next?
> * converting from proprietary to open format {ref}`fcb-interop-convertopen`
> * making data matrices FAIR {ref}`fcb-datamtrix`
> * creating minimal metadata profiles {ref}`creating-minimal-metadata-profiles`




## Reference
````{dropdown} **Reference**
[1]. Common Workflow Language, v1.0. Specification, Common Workflow Language working group. https://w3id.org/cwl/v1.0/ doi:10.6084/m9.figshare.3115156.v2

[2]. [Apache airflow](https://airflow.apache.org/)

[3]. Michael Kotliar, Andrey V Kartashov, Artem Barski, CWL-Airflow: a lightweight pipeline manager supporting Common Workflow Language, GigaScience, Volume 8, Issue 7, July 2019, giz084, https://doi.org/10.1093/gigascience/giz084

[4]. https://workflowhub.eu

[5].  Simonyan V, Goecks J, Mazumder R. Biocompute Objects—A Step towards Evaluation and Validation of Biomedical Scientific Computations. PDA journal of pharmaceutical science and technology. 2017;71(2):136-146. doi:10.5731/pdajpst.2016.006734.

[6].BCO App: tools for generating BioCompute Objects from next-generation sequencing workflows and computations.   https://doi.org/10.12688/f1000research.25902.1
````



## Authors
````{authors_fairplus}
Philippe: Writing - Original Draft
Susanna: Writing - Review & Editing, Funding acquisition
````


## License
````{license_fairplus}
CC-BY-4.0
````