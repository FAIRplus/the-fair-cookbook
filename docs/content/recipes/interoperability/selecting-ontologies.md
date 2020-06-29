# Which ontology should I use? 

<!-- **identifier:** [RX.X](RX.X)

**version:** [v1.0](v1.0)

___

**_Difficulty level:_** :triangular_flag_on_post: :white_circle: :white_circle:  :white_circle: :white_circle:

**_Reading time:_** 15 minutes 

**_Intended Audience:_** 

> :heavy_check_mark: Principal Investigators

> :heavy_check_mark: Data Managers

> :heavy_check_mark: Data Scientists

**_Recipe Type_**: Guideline

**_Executable code_**: No -->

___

<div class="row">

  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-qrcode fa-2x" style="color:#7e0038;"></i>
        <h4><b>Recipe metadata</b></h4>
        <p> identifier: <a href="">RX.x</a> </p>
        <p> version: <a href="">v0.1</a> </p>
      </div>
    </div>
  </div>
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-fire fa-2x" style="color:#7e0038;"></i>
        <h4><b>Difficulty level</b></h4>
        <i class="fa fa-fire fa-lg" style="color:#7e0038;"></i>
        <i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
        <i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
        <i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
        <i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
  <!--       <p><span data-v-013baba1="" title="" class=""><svg data-v-013baba1="" viewBox="0 0 16 16" width="1em" height="1em" focusable="false" role="img" alt="icon" xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi-bar-chart-fill b-icon bi medium-level"><g data-v-013baba1=""><rect width="4" height="5" x="1" y="10" rx="1"></rect><rect width="4" height="9" x="6" y="6" rx="1"></rect><rect width="4" height="14" x="11" y="1" rx="1"></rect></g></svg> Medium </span></p> -->
      </div>
    </div>
  </div>  
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-clock-o fa-2x" style="color:#7e0038;"></i>
        <h4><b>Reading Time</b></h4>
        <p><i class="fa fa-clock-o fa-lg" style="color:#7e0038;"></i> 15 minutes</p>
        <h4><b>Recipe Type</b></h4>
        <p><i class="fa fa-globe fa-lg" style="color:#7e0038;"></i> Guidance</p>
        <h4><b>Executable Code</b></h4>
        <p><i class="fa fa-play-circle" style="color:#fc7a4a;"></i> No</p>
      </div>
    </div>
  </div>
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-group fa-2x" style="color:#7e0038;"></i>
        <h4><b>Intended Audience</b></h4>
        <p> <i class="fa fa-user-md fa-lg" style="color:#7e0038;"></i> Principal Investigators </p>
        <p> <i class="fa fa-database fa-lg" style="color:#7e0038;"></i> Data Managers </p>
        <p> <i class="fa fa-tags fa-lg" style="color:#7e0038;"></i> Terminology Managers </p> 
        <p> <i class="fa fa-wrench fa-lg" style="color:#7e0038;"></i> Data Scientists </p>
        <p> <i class="fa fa-cogs fa-lg" style="color:#7e0038;"></i> Ontologists </p>
<!--         <p> <i class="fa fa-terminal fa-lg" style="color:#7e0038;"></i> System Administrators</p>  -->       
      </div>
    </div>
  </div>
</div>

___


[TOC]

<!-- # Table of Contents
1. [Main FAIRification Objectives](#Main%20FAIRification%20Objectives)
2. [Graphical Overview of the FAIRification Recipe Objectives](#Graphical%20Overview%20of%20the%20FAIRification%20Recipe%20Objectives)
3. [FAIRification Objectives, Inputs and Outputs](#FAIRification%20Objectives,%20Inputs%20and%20Outputs)
4. [Capability & Maturity Table](#Capability%20&%20Maturity%20Table)
5. [Table of Data Standards](#Table%20of%20Data%20Standards)
6. [Executable Code in Notebook](#Executable%20Code%20in%20Notebook)
7. [How to create workflow figures](#How%20to%20create%20workflow%20figures)
8. [License](#License)
 -->
---

## Main Objectives

The main purpose of this recipe to provide guidances on how to select the most suitable semantic artefacts given a specific research context in general, and when it comes to IMI projects, their main themes, i.e. *risk assessment*, *clinical trial*, *drug discovery* or *fundamental research*.


## Graphical Overview of the FAIRification Recipe Objectives

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgSTEoZmE6ZmEtdW5pdmVyc2l0eSB3aGF0IGlzIHRoZSBjb250ZXh0Pyk6Ojpib3ggLS0-fGZyYW1ld29ya3wgTTEoZmE6ZmEtY3ViZSBjbGluaWNhbCB0cmlhbCBjb250ZXh0KTo6OmJveFxuICBJMShmYTpmYS11bml2ZXJzaXR5IHdoYXQgaXMgdGhlIGNvbnRleHQ_KSAtLT58ZnJhbWV3b3JrfCBNMihmYTpmYS1jdWJlIG9ic2VydmF0aW9uYWwgcGF0aWVudCBvdXRjb21lKTo6OmJveFxuICBJMShmYTpmYS11bml2ZXJzaXR5IHdoYXQgaXMgdGhlIGNvbnRleHQ_KSAtLT58ZnJhbWV3b3JrfCBNMyhmYTpmYS1jdWJlIGJhc2ljIHJlc2VhcmNoKTo6OmJveFxuXG4gIE0xIC0tPiB8Y29uc2lkZXJ8IFIxKGZhOmZhLWN1YmVzIENESVNDIFZvY2FidWxhcnkpOjo6Ym94XG4gIE0yIC0tPiB8Y29uc2lkZXJ8IFIyKGZhOmZhLWN1YmVzIE9IRFNJIEF0aGVuYSB0ZXJtaW5vbG9naWVzKTo6OmJveFxuICBNMyAtLT4gfGNvbnNpZGVyfCBSMyhmYTpmYS1jdWJlcyBPQk8gRm91bmRyeSByZXNvdXJjZXMpOjo6Ym94XG4gIFxuICBJMntmYTpmYS11bml2ZXJzaXR5IGlzIHB1YmxpYzxicj4gYXJjaGl2ZTxicj4gZGVwb3NpdGlvbiA8YnI-cmVxdWlyZWQ_IH06Ojpib3ggLS0-fE5vIHxSMzo6OmJveFxuICBJMntmYTpmYS11bml2ZXJzaXR5IGlzIHB1YmxpYzxicj4gYXJjaGl2ZTxicj4gZGVwb3NpdGlvbiA8YnI-cmVxdWlyZWQ_IH0gLS0-fFllc3xNNChjb25zdWx0IEZBSVJzaGFyaW5nKTo6OmJveFxuXG4gIE00IC0tPiB8RUJJIHJlc291cmNlc3xNNShFRk8pOjo6Ym94XG5cbiAgbGlua1N0eWxlIDAsMSwyLDMsNCw1LDYsNyw4IHN0cm9rZTojMmE5ZmM5LHN0cm9rZS13aWR0aDoxcHgsY29sb3I6IzJhOWZjOSxmb250LWZhbWlseTphdmVuaXI7XG4gIGNsYXNzRGVmIGJveCBmb250LWZhbWlseTphdmVuaXIsZm9udC1zaXplOjE0cHgsZmlsbDojMmE5ZmM5LHN0cm9rZTojMjIyLGNvbG9yOiNmZmYsc3Ryb2tlLXdpZHRoOjFweFxuXHRcdCIsIm1lcm1haWQiOnsidGhlbWUiOiJuZXV0cmFsIn0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiAgSTEoZmE6ZmEtdW5pdmVyc2l0eSB3aGF0IGlzIHRoZSBjb250ZXh0Pyk6Ojpib3ggLS0-fGZyYW1ld29ya3wgTTEoZmE6ZmEtY3ViZSBjbGluaWNhbCB0cmlhbCBjb250ZXh0KTo6OmJveFxuICBJMShmYTpmYS11bml2ZXJzaXR5IHdoYXQgaXMgdGhlIGNvbnRleHQ_KSAtLT58ZnJhbWV3b3JrfCBNMihmYTpmYS1jdWJlIG9ic2VydmF0aW9uYWwgcGF0aWVudCBvdXRjb21lKTo6OmJveFxuICBJMShmYTpmYS11bml2ZXJzaXR5IHdoYXQgaXMgdGhlIGNvbnRleHQ_KSAtLT58ZnJhbWV3b3JrfCBNMyhmYTpmYS1jdWJlIGJhc2ljIHJlc2VhcmNoKTo6OmJveFxuXG4gIE0xIC0tPiB8Y29uc2lkZXJ8IFIxKGZhOmZhLWN1YmVzIENESVNDIFZvY2FidWxhcnkpOjo6Ym94XG4gIE0yIC0tPiB8Y29uc2lkZXJ8IFIyKGZhOmZhLWN1YmVzIE9IRFNJIEF0aGVuYSB0ZXJtaW5vbG9naWVzKTo6OmJveFxuICBNMyAtLT4gfGNvbnNpZGVyfCBSMyhmYTpmYS1jdWJlcyBPQk8gRm91bmRyeSByZXNvdXJjZXMpOjo6Ym94XG4gIFxuICBJMntmYTpmYS11bml2ZXJzaXR5IGlzIHB1YmxpYzxicj4gYXJjaGl2ZTxicj4gZGVwb3NpdGlvbiA8YnI-cmVxdWlyZWQ_IH06Ojpib3ggLS0-fE5vIHxSMzo6OmJveFxuICBJMntmYTpmYS11bml2ZXJzaXR5IGlzIHB1YmxpYzxicj4gYXJjaGl2ZTxicj4gZGVwb3NpdGlvbiA8YnI-cmVxdWlyZWQ_IH0gLS0-fFllc3xNNChjb25zdWx0IEZBSVJzaGFyaW5nKTo6OmJveFxuXG4gIE00IC0tPiB8RUJJIHJlc291cmNlc3xNNShFRk8pOjo6Ym94XG5cbiAgbGlua1N0eWxlIDAsMSwyLDMsNCw1LDYsNyw4IHN0cm9rZTojMmE5ZmM5LHN0cm9rZS13aWR0aDoxcHgsY29sb3I6IzJhOWZjOSxmb250LWZhbWlseTphdmVuaXI7XG4gIGNsYXNzRGVmIGJveCBmb250LWZhbWlseTphdmVuaXIsZm9udC1zaXplOjE0cHgsZmlsbDojMmE5ZmM5LHN0cm9rZTojMjIyLGNvbG9yOiNmZmYsc3Ryb2tlLXdpZHRoOjFweFxuXHRcdCIsIm1lcm1haWQiOnsidGhlbWUiOiJuZXV0cmFsIn0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

<<div class="mermaid">
graph TD
  I1(fa:fa-university what is the context?):::box -->|framework| M1(fa:fa-cube clinical trial context):::box
  I1(fa:fa-university what is the context?) -->|framework| M2(fa:fa-cube observational patient outcome):::box
  I1(fa:fa-university what is the context?) -->|framework| M3(fa:fa-cube basic research):::box

  M1 --> |consider| R1(fa:fa-cubes CDISC Vocabulary):::box
  M2 --> |consider| R2(fa:fa-cubes OHDSI Athena terminologies):::box
  M3 --> |consider| R3(fa:fa-cubes OBO Foundry resources):::box
  
  I2{fa:fa-university is public<br> archive<br> deposition <br>required? }:::box -->|No |R3:::box
  I2{fa:fa-university is public<br> archive<br> deposition <br>required? } -->|Yes|M4(consult FAIRsharing):::box

  M4 --> |EBI resources|M5(EFO):::box

  linkStyle 0,1,2,3,4,5,6,7,8 stroke:#2a9fc9,stroke-width:1px,color:#2a9fc9,font-family:avenir;
  classDef box font-family:avenir,font-size:14px,fill:#2a9fc9,stroke:#222,color:#fff,stroke-width:1px
	
</div>
___

## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Interoperability | minimal | repeatable |


----
## The context is everything:

The domain of operation will somehow dictate the semantic framework that makes most sense selecting. This is simply a consequence of the fact that the advances in data standardization in specific fields is such that it is a sound decision to adopt a complete stack of standards, both syntactic and semantic.

We will be giving two examples of such situations now:

### Clinical Trial Data:

Operating in the field of Clinical Trials means that datasets are generated during `interventional studies`, meaning that researchers influence and control the predictor variables, which are usually different intensity levels of therapeutic agents in order to gain insights in terms of benefits in patient outcomes.
In this context, regulatory requirements make it so that data must be recorded in standard forms to allow for review and appraisal by US FDA reviewers. This means that the [CDISC standards]() are the *`de-facto standard`* in the area, which mandates the use of semantics resources such as:

| Semantic Resource|Domain |License |Format |Service|
|--|--|--|--|--|
|CDISC vocabulary|clinical trial data|||EVA|
|NCI Thesaurus|biomedicine|||EVA,Bioportal,OLS|
|SNOMED-CT|pathology|||EVA,Bioportal(§)|
|UMLS|pathology|||EVA,Bioportal(§)|
|LOINC|laboratory tests||||
|RxNORM|drugs|||Bioportal|
|GUDID|instruments|||FDA|

All available from the NCBI EVA system.

> :bomb:  Some resources are only available under restrictive licences, which prevent derivative work, which may limit access and use. Furthermore, some licenses are expensive.     


### Observational Health Data:

This context refers to data collected during observation studies, which in constrat to `interventional studies`, draws inferences from a sample to a population where the independent variable is not under the control of the researcher because of ethical concerns or logistical constraints [1]. This is typically the case in the context of epidemiological work or exposure follow-up studies in the context of risk assessment and evaluation of clinical outcomes. `Observational health data` can also include `electronic health records (EHR)` or ` administrative insurance claims` and allow research around acquiring *`real world evidence`* from large corpora of data.
In this specific context, a model and associated set of standards has been particularly successful. With several hundred millions of patient information structured using the **Observational Medical Outcomes Partnership (OMOP)**, the Observational Health Data Sciences and Informatics (ODHSI) `open-science community` has been particularly successful. Therefore, building a FAIRification process around the standard stack produced by the ODHSI community needs to be considered if operated in such a `data context`.


| Semantic Resource|Domain |License |Format |Service|
|--|--|--|--|--|
|CDISC vocabulary|clinical trial data|||EVA|
|NCI Thesaurus|biomedicine|||EVA,Bioportal,OLS|
|SNOMED-CT|pathology|||EVA,Bioportal(§)|
|UMLS|pathology|||EVA,Bioportal(§)|
|LOINC|laboratory tests||||
|RxNORM|drugs|||Bioportal|


For a more detail view and deep-dive into the ODHSI and OMOP semantic support, the reading the chapter dedicated to the [`controlled terminology` in the **`Book of OHDSI`**](https://ohdsi.github.io/TheBookOfOhdsi/StandardizedVocabularies.html)


### Basic research context:

This refers to datasets and research output being generated using model organisms and cellular systems in the context of basic, fundamental research. In this arena, the regulatory pressure is much less present but this does not rule out data management good practice and proper archival requirements.
As a consequence of fewer constraints, researchers are often confronted with a sea of options. This section aims to provide some guidance when tasked with deciding on which semantic resource to use.

#### :bell: **An important consideration** 
to bear in mind when writing selecting semantic resources is to assess whether or not `data archival in public repositories will be required`. For instance, submitting to NCBI Gene Expression Omnibus Data archive places no requirement but if depositing to EMBL-EBI ArrayExpress, then selecting a resource such as the [Experimental Factor Ontology](https://efo.owl) could ease deposition.

#### :bell: **[the FAIRsharing registry](https://fairsharing.org)** 
is an ELIXIR resources which provides invaluable content as the catalogue offers an overview of the various semantics artefacts used by public data repositories.


## Selecting Terminologies 


### Use Cases and Iterative Approach  



1. The use and implementation of common terminologies will enable a normalization/harmonization of variable labels (data label) and allowed values (data term) when querying the eTRIKS database. Implementing use of common terminologies in the curation workflow will ensure consistency of the annotation across all studies.
2. The clusters of dependent annotations (related data label) also follows the eTRIKS Minimal Information Guidelines (MIGs), a set of core descriptors ensuring that a consistent breadth and depth of information is reported.  Continuous feedback will be sought from WP2 and 4 and relevant users. The iterations will feedback into both MIGs and the terminology selections.
3. As part of this iterative process, the eTRIKS use cases and query cases will be documented in order to evaluate, revise and refine the set of terminologies, and where relevant, the associated selection criteria.


### Selection Criteria

A set of widely accepted criteria for selecting terminologies (or other reporting standards) do not exists. However, the initial work by the Clinical and Translational Science Awards’ (CTSA) Omics Data Standards Working Group and BioSharing ([http://jamia.bmj.com/content/early/2013/10/03/amiajnl-2013-002066.long](http://jamia.bmj.com/content/early/2013/10/03/amiajnl-2013-002066.long)) has been used as starting point top define the eTRIKS criteria for excluding and/or including a terminology resource.



*   **Exclusion criteria**:
    * :x:  absent licence or terms of use (_indicator of usability_)
    * :x: restrictive licences or terms of use with restrictions on redistribution and reuse 
    * :x: absence of term definitions 
    * :x: absence of sufficient class metadata (_indicator of quality_)
    * :x:  absence of sustainability indicators (_absence of funding records_) 
 
*   **Inclusion criteria**:
    * :heavy_check_mark:  scope and coverage meets the requirements of the concept identified
    * :heavy_check_mark:  unique URI, textual definition and IDs for each term
    * :heavy_check_mark:  resource releases are versioned
    * :heavy_check_mark:  size of resource (_indicator of coverage_)
    * :heavy_check_mark:  number of classes and subclasses (_indicator of depth_)
    * :heavy_check_mark:  number of terms having definitions and synonyms (_indicator of richness_)
    * :heavy_check_mark:  presence of an help desk and contact point (_indicator of community support_)
    * :heavy_check_mark:  presence of term submission tracker / issue tracker (_indicator of resource agility and capability to grow upon request_)
    * :heavy_check_mark:  potential integrative nature of the resource (_as indicator of translational application potential_)
    * :heavy_check_mark:  licensing information available (_as indicator of freedom to use_)
    * :heavy_check_mark:  use of of top level ontology (_as indicator of a resource built for generic use_)
    * :heavy_check_mark:  pragmatism (_as indicator of actual, current real life practice)_
    * :heavy_check_mark:  possibility of collaborating: the resource accepts complaints/remarks that aim to fix or improve the terminology, while the resource organisation commits to fix or improve the terminology in brief delays (one month after receipt?)


### Set of Core Terminologies 

The terminologies have been organized by theme and scope. When possible, sections are organized by `granularity levels`, progressing from `macroscopic scale` (organism) to `microscopic scale` (tissue, cells) and `molecular scale` (macromolecules, proteins, small molecules, xenobiotic chemicals).
Domains also cover `Processes` or `Action` and their `participants` or `agents` but also can be organized from `general/generic` (disease) to `specialized/specific` (infectious disease).


### Organism, Organism Parts and Developmental Stages

The resources listed here focus on providing structured vocabularies to describe `taxonomic` and `anatomical` information. The table below also shows 

<table>
  <tr>
   <td><strong>Scope</strong>
   </td>
   <td><strong>Name</strong>
   </td>
   <td><strong>File location</strong>
   </td>
   <td><strong>Top-Level Ontology</strong>
   </td>
   <td><strong>Licence</strong>
   </td>
   <td><strong>Issue Tracker URI </strong>
   </td>
   <td><strong>Comment</strong>
   </td>
  </tr>
  <tr>
   <td><strong>Organism</strong>
   </td>
   <td>NCBITaxonomy
   </td>
   <td><a href="http://purl.obolibrary.org/obo/ncbitaxon.owl">http://purl.obolibrary.org/obo/ncbitaxon.owl</a>
   </td>
   <td>none specified
   </td>
   <td>This ontology is made available via the UMLS. Users of all UMLS ontologies must abide by the terms of the UMLS license, available at <a href="https://uts.nlm.nih.gov/license.html">https://uts.nlm.nih.gov/license.html</a>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
    <tr>
   <td><strong>Vertebrate </strong>
<p>
<strong>Anatomy</strong>
   </td>
   <td>UBERON
   </td>
   <td><a href="http://purl.obolibrary.org/obo/uberon/ext.owl">http://purl.obolibrary.org/obo/uberon/ext.owl</a>
<p>
<a href="http://purl.obolibrary.org/obo/uberon/ext.obo">http://purl.obolibrary.org/obo/uberon/ext.obo</a>
   </td>
   <td>BFO
   </td>
   <td><a href="https://creativecommons.org/licenses/by/3.0/">CC-by 3.0 Unported Licence</a>
   </td>
   <td>https://github.com/obophenotype/uberon/issues
   </td>
   <td><em>Integrative Resource</em>
<p>
<em>engineered to go across species </em>
   </td>
  </tr>
<tr>
   <td><strong>Mouse Anatomy</strong>
   </td>
   <td>MA
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>  
  <tr>
   <td><strong>Strain</strong>
   </td>
   <td>Rat Strain Ontology
   </td>
   <td>http://data.bioontology.org/ontologies/RS/submissions/46/download?apikey=4ea81d74-8960-4525-810b-fa1baab576ff
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  
</table>


In research, many different model organism are used (e.g. Dogs, Monkeys...) and specialized resources may be available. Use the selection criteria introduced earlier to gauge their value in the data management workflow and their impact on data integration tasks.




### Diseases and Phenotype

Biology is a complex field and observable manifestations of biological processes in living organisms vary, dependant on genetic background and environmental factors. Working on correlating genetic features with observable (phenotypic) ones,  biologists rely heavily on such variables in the quest of disease biomarkers, which could be used to identify possible therapeutic targets. The main challenge is to ensure efficient machine actionable descriptions of these observable features.

<table>
  <tr>
   <td><strong>Scope</strong>
   </td>
   <td><strong>Name</strong>
   </td>
   <td><strong>File location</strong>
   </td>
   <td><strong>Top-Level Ontology</strong>
   </td>
   <td><strong>Licence</strong>
   </td>
   <td><strong>Issue Tracker URI </strong>
   </td>
  </tr>
  <tr>
   <td><strong>Pathology/Disease (generic)</strong>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>SNOMED-CT
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>http://www.ihtsdo.org/licensing/
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>NCI thesaurus
   </td>
   <td><a href="http://evs.nci.nih.gov/ftp1/NCI_Thesaurus">http://evs.nci.nih.gov/ftp1/NCI_Thesaurus</a>
   </td>
   <td>
   </td>
   <td>http://evs.nci.nih.gov/ftp1/NCI_Thesaurus/ThesaurusTermsofUse.htm
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>ICD-10
   </td>
   <td>
   </td>
   <td>login required [http://apps.who.int/classifications/apps/icd/ClassificationDownloadNR/login.aspx?ReturnUrl=%2fclassifications%2fapps%2ficd%2fClassificationDownload%2fdefault.aspx]
   </td>
   <td><a href="http://www.who.int/about/copyright/en/">http://www.who.int/about/copyright/en/</a>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>UMLS
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>http://www.nlm.nih.gov/databases/umls.html
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Disease Ontology
   </td>
   <td><a href="http://purl.obolibrary.org/obo/doid.owl">http://purl.obolibrary.org/obo/doid.owl</a>
   </td>
   <td>BFO
   </td>
   <td><a href="https://creativecommons.org/licenses/by/3.0/">CC-by 3.0 Unported Licence</a>
   </td>
   <td>http://sourceforge.net/p/diseaseontology/feature-requests/
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>Infection Disease Ontology
   </td>
   <td><a href="https://code.google.com/p/infectious-disease-ontology/source/browse/trunk/src/ontology/ido-core/ido-main.owl">https://code.google.com/p/infectious-disease-ontology/source/browse/trunk/src/ontology/ido-core/ido-main.owl</a>
   </td>
   <td>BFO
   </td>
   <td>most probably:
<p>
<a href="https://creativecommons.org/licenses/by/3.0/">CC-by 3.0 Unported Licence</a>
   </td>
   <td>https://code.google.com/p/infectious-disease-ontology/issues/list
   </td>
  </tr>
  <tr>
   <td><strong>Phenotype</strong>
   </td>
   <td>Human Phenotype Ontology
   </td>
   <td><a href="http://compbio.charite.de/hudson/job/hpo/lastStableBuild/">http://compbio.charite.de/hudson/job/hpo/lastStableBuild/</a>
   </td>
   <td>BFO
   </td>
   <td>most probably:
<p>
<a href="https://creativecommons.org/licenses/by/3.0/">CC-by 3.0 Unported Licence</a>
   </td>
   <td>http://sourceforge.net/p/obo/human-phenotype-requests/
   </td>
  </tr>
  <tr>
   <td><strong>Mouse Phenotype</strong>
   </td>
   <td>MPO
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>PATO
   </td>
   <td>
   </td>
   <td>BFO
   </td>
   <td>
   </td>
   <td>http://sourceforge.net/p/obo/phenotypic-quality-pato-requests/
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>MedDRA
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>This ontology is freely accessible on this site for academic and other non-commercial uses. Users anticipating any commercial use of MedDRA must contact the MSSO to obtain a license.
   </td>
   <td><a href="https://mssotools.com/webcr/">https://mssotools.com/webcr/</a>
<p>
Login required
   </td>
  </tr>
</table>



### Pathology and Disease Specific Resources


<table>
  <tr>
   <td><strong>Scope</strong>
   </td>
   <td><strong>Name</strong>
   </td>
   <td><strong>File location</strong>
   </td>
   <td><strong>Top-Level Ontology</strong>
   </td>
   <td><strong>Licence</strong>
   </td>
   <td><strong>Issue Tracker URI </strong>
   </td>
  </tr>
  <tr>
   <td><strong>Influenza</strong>
   </td>
   <td>FLU
   </td>
   <td>
   </td>
   <td>BFO
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong>Malaria</strong>
   </td>
   <td>IDOMAL
   </td>
   <td>
   </td>
   <td>BFO
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong>Dengue Fever</strong>
   </td>
   <td>IDODEN
   </td>
   <td>
   </td>
   <td>BFO
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong>Alzheimer Disease</strong>
   </td>
   <td>
   ADO
   </td>
   <td>
      <a href="https://www.scai.fraunhofer.de/content/dam/scai/de/downloads/bioinformatik/ontologies/ADO/ADO.zip">https://www.scai.fraunhofer.de/content/dam/scai/de/downloads/bioinformatik/ontologies/ADO/ADO.zip</a>
   </td>
   <td>
   BFO
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
 
   <td><strong>Immune disorder</strong>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong>Rare disorder</strong>
   </td>
   <td>ORDO
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
</table>



### Cellular entities

Following on through our review of semantic resources by granularity levels, this section details a number of reference resources which provide coverage for the describing `cell types`, `cell lines` and `cellular phenotypes`.


<table>
  <tr>
   <td><strong>Scope</strong>
   </td>
   <td><strong>Name</strong>
   </td>
   <td><strong>File location</strong>
   </td>
   <td><strong>Top-Level Ontology</strong>
   </td>
   <td><strong>Licence</strong>
   </td>
   <td><strong>Issue Tracker URI </strong>
   </td>
   </tr>

<tr>
   <td><strong>Cell</strong>
   </td>
   <td>CL
   </td>
   <td><a href="http://purl.obolibrary.org/obo/cl.owl">http://purl.obolibrary.org/obo/cl.owl</a>
<p>
<a href="http://purl.obolibrary.org/obo/cl.obo">http://purl.obolibrary.org/obo/cl.obo</a>
   </td>
   <td>BFO
   </td>
   <td>most probably:
<p>
<a href="https://creativecommons.org/licenses/by/3.0/">CC-by 3.0 Unported Licence</a>
   </td>
   <td>https://code.google.com/p/cell-ontology/issues/list
   </td>
  </tr>
  <tr>
  <td>
  <strong>Cell Lines</strong>
</td>
<td>
Cellosaurus
</td>

<td>
<a href="ftp://ftp.expasy.org/databases/cellosaurus/cellosaurus.obo">ftp://ftp.expasy.org/databases/cellosaurus/cellosaurus.obo</a>

<a href="ftp://ftp.expasy.org/databases/cellosaurus">ftp://ftp.expasy.org/databases/cellosaurus</a>
</td>
<td>
</td>
<td><a href="https://creativecommons.org/licenses/by/4.0/">https://creativecommons.org/licenses/by/4.0/</a>
</td>
<td>
</td>
</tr>  
  <tr>
   <td><strong>Cell Lines</strong>
   </td>
   <td>CLO
   </td>
   <td><a href="http://clo-ontology.googlecode.com/svn/trunk/src/ontology/clo.owl">http://clo-ontology.googlecode.com/svn/trunk/src/ontology/clo.owl</a>
   </td>
   <td>BFO
   </td>
   <td>most probably:
<p>
<a href="https://creativecommons.org/licenses/by/3.0/">CC-by 3.0 Unported Licence</a>
   </td>
   <td>https://code.google.com/p/clo-ontology/issues/list
   </td>
  </tr>
  <tr>
   <td><strong>Cell Molecular Phenotype Ontology</strong>
   </td>
   <td>CMPO
   </td>
   <td>https://github.com/EBISPOT/CMPO/tree/master/release
   </td>
   <td>BFO
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
</table>


### Molecular Entities

This section highlights the major and most widely used OBO Foundry resources for `molecules of biological relevance` as well as `molecular structures`, `biological processes` and `cellular components` 


<table>
  <tr>
   <td><strong>Scope</strong>
   </td>
   <td><strong>Name</strong>
   </td>
   <td><strong>File location</strong>
   </td>
   <td><strong>Top-Level Ontology</strong>
   </td>
   <td><strong>Licence</strong>
   </td>
   <td><strong>Issue Tracker URI </strong>
   </td>
  </tr>
  <tr>
   <td><strong>Chemicals and Small Molecules</strong>
   </td>
   <td>CHEBI
   </td>
   <td><a href="http://ftp.ebi.ac.uk/chebi.owl">http://ftp.ebi.ac.uk/chebi.owl</a>
<p>
<a href="http://ftp.ebi.ac.uk/chebi.obo">http://ftp.ebi.ac.uk/chebi.obo</a>
   </td>
   <td>BFO
   </td>
   <td>most probably:
<p>
<a href="https://creativecommons.org/licenses/by/3.0/">CC-by 3.0 Unported Licence</a>
   </td>
   <td>http://sourceforge.net/p/chebi/annotation-issues/
   </td>
  </tr>
 
  <tr>
   <td><strong>Gene Function, Molecular Component, Biological Process</strong>
   </td>
   <td>GO
   </td>
   <td><a href="http://purl.obolibrary.org/obo/go.obo">http://purl.obolibrary.org/obo/go.obo</a>
<p>
<a href="http://purl.obolibrary.org/obo/go.owl">http://purl.obolibrary.org/obo/go.owl</a>
   </td>
   <td>BFO
   </td>
   <td>CC-by 4.0<a href="https://creativecommons.org/licenses/by/4.0/legalcode"> Unported License</a>
   </td>
   <td>http://sourceforge.net/p/geneontology/ontology-requests/
   </td>
  </tr>
  <tr>
   <td><strong>Protein/peptide</strong>
   </td>
   <td>PRO
   </td>
   <td><a href="http://ftp.pir.georgetown.edu/pro.obo">http://ftp.pir.georgetown.edu/pro.obo</a>
   </td>
   <td>BFO
   </td>
   <td><a href="https://creativecommons.org/licenses/by/3.0/">CC-by 3.0 Unported Licence</a>
   </td>
   <td>
   </td>
  </tr>
</table>

Besides these open ontologies, in the context of clinically relevant work where drug formulation require recording and description, the following resource is relevant.


<table>
<tr>
   <td><strong>Scope</strong>
   </td>
   <td><strong>Name</strong>
   </td>
   <td><strong>File location</strong>
   </td>
   <td><strong>Top-Level Ontology</strong>
   </td>
   <td><strong>Licence</strong>
   </td>
   <td><strong>Issue Tracker URI </strong>
   </td>
  </tr>
 <tr>
   <td><strong>Drug</strong>
   </td>
   <td>National Drug File
   </td>
   <td>
   </td>
   <td>
   </td>
   <td><a href="https://uts.nlm.nih.gov/license.html">https://uts.nlm.nih.gov/license.html</a>
   </td>
   <td>
   </td>
  </tr>
</table>

### Assays and Technologies

The resources listed in the section are providing key descriptors bridging data acquisition procedures (as used in clinical setting and wet lab work) with instruments, units of measurements, endpoints as well as sometimes the biological process or molecular entities of biological significance.
Some of the resources are specialized semantic artefact developed to support the standardized reporting of data modalities.

<table>
<tr>
   <td><strong>Scope</strong>
   </td>
   <td><strong>Name</strong>
   </td>
   <td><strong>File location</strong>
   </td>
   <td><strong>Top-Level Ontology</strong>
   </td>
   <td><strong>Licence</strong>
   </td>
   <td><strong>Issue Tracker URI </strong>
   </td>
  </tr>
<tr>
   <td><strong>Radiology</strong>
   </td>
   <td>RADLex
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong>Medical Imaging</strong>
   </td>
   <td>DICOM
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
</table>

<table>
  <tr>
   <td><strong>Scope</strong>
   </td>
   <td><strong>Name</strong>
   </td>
   <td><strong>File location</strong>
   </td>
   <td><strong>Top-Level Ontology</strong>
   </td>
   <td><strong>Licence</strong>
   </td>
   <td><strong>Issue Tracker URI </strong>
   </td>
  </tr>
  <tr>
   <td><strong>Sample Processing/Reagents/Instruments</strong>
<p>
<strong>Assay Definition</strong>
   </td>
   <td>OBI
   </td>
   <td><a href="http://svn.code.sf.net/p/obi/code/releases/2014-03-29/obi.owl">http://svn.code.sf.net/p/obi/code/releases/2014-03-29/obi.owl</a>
   </td>
   <td>BFO
   </td>
   <td><a href="https://creativecommons.org/licenses/by/3.0/">CC-by 3.0 Unported Licence</a>
   </td>
   <td><a href="http://sourceforge.net/p/obi/obi-terms/">http://sourceforge.net/p/obi/obi-terms/</a>
   </td>
  </tr>
  <tr>
   <td><strong>Biological screening assays and their results including high-throughput screening (HTS) </strong>
   </td>
   <td>BAO
   </td>
   <td>http://www.bioassayontology.org/bao/bao_complete_bfo_dev.owl
   </td>
   <td>BFO
   </td>
   <td><a href="https://creativecommons.org/licenses/by/3.0/">CC-by 3.0 Unported Licence</a>
   </td>
   <td>
   </td>
  </tr>
   
  <tr>
   <td><strong>Mass Spectrometry (instrument/acquisition parameter/spectrum related information)</strong>
   </td>
   <td>PSI-MS
   </td>
   <td><a href="http://psidev.cvs.sourceforge.net/viewvc/psidev/psi/psi-ms/mzML/controlledVocabulary/psi-ms.obo">http://psidev.cvs.sourceforge.net/viewvc/psidev/psi/psi-ms/mzML/controlledVocabulary/psi-ms.obo</a>
<p>
(No OWL file)
   </td>
   <td>none specified
   </td>
   <td><a href="https://creativecommons.org/licenses/by/3.0/">CC-by 3.0 Unported Licence</a>
   </td>
   <td>https://lists.sourceforge.net/lists/listinfo/psidev-vocab
   </td>
  </tr>
  <tr>
   <td><strong>NMR Spectroscopy (instrument/acquisition parameter/spectrum related information)</strong>
   </td>
   <td>NMR-CV
   </td>
   <td><a href="http://nmrml.org/cv/v1.0.rc1/nmrCV.owl">http://nmrml.org/cv/v1.0.rc1/nmrCV.owl</a>
   </td>
   <td>BFO
   </td>
   <td>Creative Commons Public Domain Mark 1.0
   </td>
   <td><a href="https://github.com/nmrML/nmrML/issues?state=open">https://github.com/nmrML/nmrML/issues?state=open</a
   </td>
  </tr>
  <tr>
   <td><strong>Laboratory test</strong>
   </td>
   <td><strong>LOINC</strong>
   </td>
   <td><a href="http://loinc.org/downloads/resolveuid/d5a127cbbecbd1660bb91cec9ef4a26c">LOINC and RELMA Complete Download File (All Formats Included)</a>
   </td>
   <td>none specified
   </td>
   <td><a href="https://uts.nlm.nih.gov/license.html">https://uts.nlm.nih.gov/license.html</a>
   </td>
   <td>wait for Bron ‘s feedback regarding CDISC lab test descriptors to handle/avoid overlap with LOINC coverage
   </td>
  </tr>
</table>

Finally, a resource exists that describes statistical measures, statistical tests or methods as well as statistically relevant graphical representations. It may be used for reporting results and annotating experimental results.

<table>
<tr>
   <td><strong>Scope</strong>
   </td>
   <td><strong>Name</strong>
   </td>
   <td><strong>File location</strong>
   </td>
   <td><strong>Top-Level Ontology</strong>
   </td>
   <td><strong>Licence</strong>
   </td>
   <td><strong>Issue Tracker URI </strong>
   </td>
  </tr>
<tr>
   <td><strong>Experimental Design, Statistical Methods and Statistical Measures</strong>
   </td>
   <td>STATO
   </td>
   <td><a href="https://raw.githubusercontent.com/ISA-tools/stato/dev/src/ontology/stato.owl">https://raw.githubusercontent.com/ISA-tools/stato/dev/src/ontology/stato.owl</a>
   </td>
   <td>BFO
   </td>
   <td><a href="https://creativecommons.org/licenses/by/3.0/">CC-by 3.0 Unported Licence</a>
   </td>
   <td>https://github.com/ISA-tools/stato/issues?state=open
   </td>
  </tr>
</table>



### Relations

Also known as OWL.Properties, their importance may be overlooked by `data scientists` who are not `knowledge engineers` or `ontologists`  but these are essential components as, when correctly crafted with a proper understanding of the logical constraints available to semantic language such as OWL, are exploited by `automatic reasoners` to carry the following key tasks:

* `ontology logical consistency` checks
* `automatic classification` and `inference` tasks
* `entailments`, i.e. detection of logical consequences resulting from axiomatic

This is particularly important when processing billions of facts expressed as RDF statements. 

One also needs to understand the current limitations in expressivity afforded by the current semantic web languages and the associated axiomatics as well as computational constraints associated with inference. For more *in-depth* review of such topics, the reader is invited to consults the following work [ref].

In the field of Biology and Biomedicine, the [OBO Foundry](http://obofoundry.org) coordinates the development of interoperable ontologies. At the core of this interoperation lies the **[Relation Ontology](http://www.obofoundry.org/ontology/ro.html)**

|Scope| File                        | Relation Ontology               | Variant                                                              | License  | 
|---|-------------------------------|---------------------------------|--------------------------------------------------------------------------------|---|
|**relations**| ro.owl                        | Relation Ontology               | Canonical edition                                                              | https://creativecommons.org/publicdomain/zero/1.0/  | 
|**relations**| ro.obo                        | Relation Ontology in obo format | Has imports merged in                                                          |  https://creativecommons.org/publicdomain/zero/1.0/ |
|**relations**| ro/core.owl                   | RO Core relations               | Minimal subset intended to work with BFO-classes [page]                        |  https://creativecommons.org/publicdomain/zero/1.0/ | 
|**relations**| ro/ro-base.owl                | RO base ontology                | Axioms defined within RO and to be used in imports for other ontologies [page] | https://creativecommons.org/publicdomain/zero/1.0/  | 
|**relations**| ro/subsets/ro-interaction.owl | Interaction relations           |                                   |  https://creativecommons.org/publicdomain/zero/1.0/ |
|**relations**| ro/subsets/ro-eco.owl         | Ecology subset                  |   For use in ecology and environmental science  | https://creativecommons.org/publicdomain/zero/1.0/  | 
|**relations**| ro/subsets/ro-neuro.owl       | Neuroscience subset             | For use in neuroscience [page]                                                 | https://creativecommons.org/publicdomain/zero/1.0/  |    


As [knowledge graphs]() and [property graphs]() gain importance, we  can expect the range and depth of relations to mature and expands are more expressivity is needed and progress is made by reasoner technology to fully exploit their benefits.
This would also have to placed in the context of advances in `Text Mining` and `Machine Learning`, where unsupervised methods start to demonstrate strong potential to detecting relations between entities.

```rdf
B cell, CD19-positive
equivalentClass :
    lymphocyte of B lineage, CD19-positive 
    and ( has plasma membrane part some CD19 molecule) 
    and ( in taxon some Mammalia) 
    and ( capable of some B cell mediated immunity)
```


---
## Conclusions:

> Selecting semantic resources depends on many different factors. However, the most important factor remains the `context` of the data and associated landscape of data standards as well as the ultimate integration goal, which will dictate the final choice.
> 
>The selection process remains guided by the need to maximize the potential of data integration with datasets of similar nature and similar value. It aslo requires a good understanding of the technical and sometimes legals implications these choice will have.    

> #### What should I read next?
> * [How to build an application ontology?]()
> * [How to select on ontology service?]()
> * [How to deploy an ontology server?]()
> * [How to establish a minimal metadata profile?]()
___


## References:

Smith, B., Ceusters, W., Klagges, B. et al. Relations in biomedical ontologies. Genome Biol 6, R46 (2005). https://doi.org/10.1186/gb-2005-6-5-r46

Rocca-Serra P, Bratfalean D, Richard F, Marshall C, Romacker M., Auffray C, ., … on the behalf of the eTRIKS consortium, . (2016, April 25). eTRIKS Standards Starter Pack Release 1.1 April 2016. Zenodo. http://doi.org/10.5281/zenodo.50825

Malone J, Stevens R, Jupp S, Hancocks T, Parkinson H, Brooksbank C. Ten Simple Rules for Selecting a Bio-ontology. PLoS Comput Biol. 2016;12(2):e1004743. Published 2016 Feb 11. http://doi.org/10.1371/journal.pcbi.1004743

Bairoch A. The Cellosaurus, a cell line knowledge resource. J. Biomol. Tech. (2018) 29:25-38. http://doi.org/10.7171/jbt.18-2902-002.

Sansone, S.-A., McQuilton, P., Rocca-Serra, P., Gonzalez-Beltran, A., Izzo, M., Lister, A.L. and Thurston, M. (2019) FAIRsharing as a community approach to standards, repositories and policies. Nature biotechnology, 37, 358: http://doi.org/10.1038/s41587-019-0080-8.

Hripcsak, G., Ryan, P. B., Duke, J. D., Shah, N. H., Park, R. W., Huser, V., Suchard, M. A., Schuemie, M. J., DeFalco, F. J., Perotte, A., Banda, J. M., Reich, C. G., Schilling, L. M., Matheny, M. E., Meeker, D., Pratt, N., & Madigan, D. (2016). Characterizing treatment pathways at scale using the OHDSI network. Proceedings of the National Academy of Sciences of the United States of America, 113(27), 7329–7336. https://doi.org/10.1073/pnas.1510502113

Hripcsak, George et al. “Observational Health Data Sciences and Informatics (OHDSI): Opportunities for Observational Researchers.” Studies in health technology and informatics vol. 216 (2015): 574-8.




___
## Authors:

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Philippe Rocca-Serra |  University of Oxford, Data Readiness Group| [0000-0001-9853-5668](https://orcid.org/orcid.org/0000-0001-9853-5668) | Writing - Original Draft |
| Susanna-Assunta Sansone |  University of Oxford, Data Readiness Group | | Writing - Review & Editing, Funding acquisition | 

___
## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
