(fcb-selecting-ontologies (URL_TO_INSERT_TERM_6617 https://fairsharing.org/search?recordType=terminology_artefact) )=
# Selecting terminologies and ontologies


````{panels_fairplus}
:identifier_text: FCB020
:identifier_link: 'https://w3id.org/faircookbook/FCB020'
:difficulty_level: 1
:recipe_type: guidance
:reading_time_minutes: 15
:intended_audience: principal_investigator, data_manager, terminology_manager, data_scientist, ontologist
:maturity_level: 3
:maturity_indicator: 33
:has_executable_code: nope
:recipe_name: Selecting terminologies and ontologies
```` 


## Main Objectives

The main purpose of this recipe is to provide guidance on how to select the most suitable semantic artefacts given a specific research (URL_TO_INSERT_RECORD_6619 https://fairsharing.org/FAIRsharing.52b22c)  context in general, and when it comes to life and biomedical sciences project (URL_TO_INSERT_TERM_6618 https://fairsharing.org/search?recordType=project) s, their main themes, i.e. *risk assessment*, *clinical trial*, *drug discovery* or *fundamental research (URL_TO_INSERT_RECORD_6620 https://fairsharing.org/FAIRsharing.52b22c) *.


## Graphical Overview


````{dropdown} 
:open:
```{figure} selecting-ontologies.md-figure1.mmd.svg
---
width: 1000px
name: selecting-ontologies (URL_TO_INSERT_TERM_6621 https://fairsharing.org/search?recordType=terminology_artefact) -figure1
alt:  Which ontology (URL_TO_INSERT_TERM_6622 https://fairsharing.org/search?recordType=terminology_artefact)  should be used?
---
 Which ontology (URL_TO_INSERT_TERM_6625 https://fairsharing.org/search?recordType=terminology_artefact)  should be used? Depending on dataset context, domain specific resources may be mandated, such as Clinical Data Interchange Standard (URL_TO_INSERT_TERM_6623 https://fairsharing.org/search?fairsharingRegistry=Standard) s Consortium (CDISC (URL_TO_INSERT_RECORD_6629 https://fairsharing.org/3525) ), Observational Health Data Sciences and Informat (URL_TO_INSERT_TERM_6624 https://fairsharing.org/search?recordType=model_and_format) ics (OHDSI) or Open Biomedical Ontologies (URL_TO_INSERT_TERM_6627 https://fairsharing.org/search?recordType=terminology_artefact)  (OBO). The Experimantal Factor Ontology (URL_TO_INSERT_TERM_6626 https://fairsharing.org/search?recordType=terminology_artefact)  (EFO) is specifically used by EMBL-EBI ArrayExpress (URL_TO_INSERT_RECORD_6628 https://fairsharing.org/FAIRsharing.6k0kwd)  to annotated dataset.
```
````

---

## Context is everything

The domain of operation will generally dictate the semantic framework that is most suited to a given dataset. This is simply due to the fact that the advances in data standard (URL_TO_INSERT_TERM_6630 https://fairsharing.org/search?fairsharingRegistry=Standard) ization in specific fields are such that it is a sound decision to adopt a complete stack of standard (URL_TO_INSERT_TERM_6631 https://fairsharing.org/search?fairsharingRegistry=Standard) s, both syntactic and semantic.

Here, we present the three most common scenarios in biomedical research (URL_TO_INSERT_RECORD_6632 https://fairsharing.org/FAIRsharing.52b22c) , based on experience garnered during IMI eTRIKS (URL_TO_INSERT_RECORD_6633 https://fairsharing.org/3510)  {footcite}`philippe_rocca_serra_2016_50825`:
- [Clinical Trial Data](#clinical-trial-data)
- [Observational Health Data](#observational-health-data)
- [Basic research (URL_TO_INSERT_RECORD_6634 https://fairsharing.org/FAIRsharing.52b22c)  context](#basic-research (URL_TO_INSERT_RECORD_6635 https://fairsharing.org/FAIRsharing.52b22c) -context)

### Clinical Trial Data

Operating in the field of Clinical Trials means that datasets are generated during `interventional studies`, meaning that research (URL_TO_INSERT_RECORD_6636 https://fairsharing.org/FAIRsharing.52b22c) ers influence and control the predictor variables, which are usually different intensity levels of therapeutic agents, in order to gain insights in terms of benefits in patient outcomes.
In this context, regulator (URL_TO_INSERT_RECORD_6639 https://fairsharing.org/FAIRsharing.ey49c6) y requirements make it so that data must be recorded in standard (URL_TO_INSERT_TERM_6637 https://fairsharing.org/search?fairsharingRegistry=Standard)  forms to allow for review and appraisal by regulator (URL_TO_INSERT_RECORD_6640 https://fairsharing.org/FAIRsharing.ey49c6) s such as FDA reviewers in the US. The [CDISC (URL_TO_INSERT_RECORD_6641 https://fairsharing.org/3525)  standards](https://www.cdisc.org (URL_TO_INSERT_RECORD_6642 https://fairsharing.org/3525) /standards) are the *`de-facto standard (URL_TO_INSERT_TERM_6638 https://fairsharing.org/search?fairsharingRegistry=Standard) `* in this area, which mandates the use of semantics resources such as:

| Semantic Resource | Domain  | Service |
| -- | -- | -- | 
| CDI (URL_TO_INSERT_RECORD_6643 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_6644 https://fairsharing.org/3525)  vocabulary|clinical trial data| EVS |
| NCI Thesaurus (URL_TO_INSERT_RECORD_6646 https://fairsharing.org/FAIRsharing.4cvwxa) |biomedicine|EVS,Bioportal (URL_TO_INSERT_RECORD_6645 https://fairsharing.org/FAIRsharing.4m97ah) ,OLS|
| SNOMED-CT|pathology|EVS,Bioportal (URL_TO_INSERT_RECORD_6647 https://fairsharing.org/FAIRsharing.4m97ah) (§)|
| UMLS|pathology|EVS,Bioportal (URL_TO_INSERT_RECORD_6648 https://fairsharing.org/FAIRsharing.4m97ah) (§)|
| LOINC (URL_TO_INSERT_RECORD_6649 https://fairsharing.org/FAIRsharing.2mk2zb) |laboratory tests|Loinc|
| RxNORM (URL_TO_INSERT_RECORD_6651 https://fairsharing.org/FAIRsharing.36pf8q) |drugs|Bioportal (URL_TO_INSERT_RECORD_6650 https://fairsharing.org/FAIRsharing.4m97ah) |
| GUDID (URL_TO_INSERT_RECORD_6652 https://fairsharing.org/FAIRsharing.ennep4) |instruments|FDA|

All available from the [NCBI EVS system](https://evs.nci.nih.gov/), [LOINC](https://loinc.org (URL_TO_INSERT_RECORD_6656 https://fairsharing.org/FAIRsharing.2mk2zb) /), [OLS](https://www.ebi.ac.uk/ols/index (URL_TO_INSERT_RECORD_6653 https://fairsharing.org/FAIRsharing.Mkl9RR) ) or [Bioportal (URL_TO_INSERT_RECORD_6654 https://fairsharing.org/FAIRsharing.4m97ah) ](https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_6655 https://fairsharing.org/FAIRsharing.4m97ah) /).
 

```{warning}
Some resources are only available under restrictive licences, which prevent derivative work, which may limit access and use. Furthermore, some licenses are expensive.  
```

### Observational Health Data

This context refers to data collected during `observational studies`, which in contrast to `interventional studies`, draw inferences from a sample to a population where the independent variable is not under the control of the research (URL_TO_INSERT_RECORD_6657 https://fairsharing.org/FAIRsharing.52b22c) er because of ethical concerns or logistical constraints [1]. This is typically the case in epidemiological work or exposure follow-up studies in the context of risk assessment and evaluation of clinical outcomes. `Observational health data` can also include `electronic health records (EHR)` or ` administrative insurance claims` and allow research (URL_TO_INSERT_RECORD_6658 https://fairsharing.org/FAIRsharing.52b22c)  around acquiring *`real world evidence`* from large corpora of data.
In this specific context, one model (URL_TO_INSERT_TERM_6661 https://fairsharing.org/search?recordType=model_and_format)  and associated set of standard (URL_TO_INSERT_TERM_6659 https://fairsharing.org/search?fairsharingRegistry=Standard) s has been particularly successful. With several hundred millions of patients' informat (URL_TO_INSERT_TERM_6663 https://fairsharing.org/search?recordType=model_and_format) ion structured using the **Observational Medical Outcomes Partnership ([OMOP](https://ohdsi.org/omop/))**, the Observational Health Data Sciences and Informat (URL_TO_INSERT_TERM_6664 https://fairsharing.org/search?recordType=model_and_format) ics ([ODHSI](https://ohdsi.org/)) `open-science community` has laid the foundation for a widely adopted data model (URL_TO_INSERT_TERM_6662 https://fairsharing.org/search?recordType=model_and_format) . Therefore, building a FAIR (URL_TO_INSERT_RECORD_6665 https://fairsharing.org/FAIRsharing.WWI10U) ification process around the standard (URL_TO_INSERT_TERM_6660 https://fairsharing.org/search?fairsharingRegistry=Standard)  stack produced by the ODHSI community needs to be considered if operating in such a `data context`.


|Semantic Resource|Domain |Service|
|--- |---  |--- |
|CDISC (URL_TO_INSERT_RECORD_6666 https://fairsharing.org/3525)  vocabulary|clinical trial data|EVS|
|NCI Thesaurus (URL_TO_INSERT_RECORD_6668 https://fairsharing.org/FAIRsharing.4cvwxa) |biomedicine|EVS,Bioportal (URL_TO_INSERT_RECORD_6667 https://fairsharing.org/FAIRsharing.4m97ah) ,OLS|
|SNOMED-CT|pathology|EVS,Bioportal (URL_TO_INSERT_RECORD_6669 https://fairsharing.org/FAIRsharing.4m97ah) (§)|
|UMLS|pathology|EVS,Bioportal (URL_TO_INSERT_RECORD_6670 https://fairsharing.org/FAIRsharing.4m97ah) (§)|
|LOINC (URL_TO_INSERT_RECORD_6671 https://fairsharing.org/FAIRsharing.2mk2zb) |laboratory tests| LOINC (URL_TO_INSERT_RECORD_6672 https://fairsharing.org/FAIRsharing.2mk2zb)  |
|RxNORM (URL_TO_INSERT_RECORD_6674 https://fairsharing.org/FAIRsharing.36pf8q) |drugs|Bioportal (URL_TO_INSERT_RECORD_6673 https://fairsharing.org/FAIRsharing.4m97ah) |


For a more detailed overview and deep-dive into the ODHSI and OMOP semantic support, we recommend the reading of the chapter dedicated to the `controlled terminology (URL_TO_INSERT_TERM_6675 https://fairsharing.org/search?recordType=terminology_artefact) ` [in the **`Book of OHDSI`**](https://ohdsi.github.io/TheBookOfOhdsi/StandardizedVocabularies.html) {footcite}`pmid27274072`


### Basic research context

This refers to datasets and research (URL_TO_INSERT_RECORD_6678 https://fairsharing.org/FAIRsharing.52b22c)  output being generated using model (URL_TO_INSERT_TERM_6676 https://fairsharing.org/search?recordType=model_and_format)  organisms and cellular systems in the context of basic, fundamental research (URL_TO_INSERT_RECORD_6679 https://fairsharing.org/FAIRsharing.52b22c) . In this arena, the regulator (URL_TO_INSERT_RECORD_6677 https://fairsharing.org/FAIRsharing.ey49c6) y pressure is much less present but this does not rule out data management best practices and proper arch (URL_TO_INSERT_RECORD_6680 https://fairsharing.org/FAIRsharing.52b22c) ival requirements.
As a consequence of fewer constraints, research (URL_TO_INSERT_RECORD_6681 https://fairsharing.org/FAIRsharing.52b22c) ers are often confronted with a sea of options. This and the next sections aim to provide some guidance when tasked with deciding on which semantic resource to use.

```{admonition} Tip
:class: tip
 **An important consideration** 
to bear in mind when selecting semantic resources is to assess whether or not `data archival in public repositories will be required`. For instance, submitting to NCBI Gene Expression Omnibus Data archive places no particular constraints on data annotations but if depositing to EMBL-EBI ArrayExpress, then selecting a resource such as the Experimental Factor Ontology ([EFO](https://www.ebi.ac.uk/efo/)) for annotating data could ease deposition.
```

```{admonition} Tip
:class: tip
 **[The FAIRsharing registry](https://fairsharing.org)** {footcite}`pmid30940948` is an ELIXIR resource which provides invaluable content as the catalogue offers an overview of the various semantics artefact used by public data repositories.
```

## Selecting Terminologies 


### Use Cases and General Recommendations

1. The use and implementation of common terminologies (URL_TO_INSERT_TERM_6683 https://fairsharing.org/search?recordType=terminology_artefact)  enables the normalisation and harmonisation of both variable labels and allowed values for each field. Implementing the use of common terminologies (URL_TO_INSERT_TERM_6684 https://fairsharing.org/search?recordType=terminology_artefact)  in the data collection (URL_TO_INSERT_TERM_6682 https://fairsharing.org/search?recordType=collection)  or curation workflow will ensure consistency of the annotation across all data. This is particularly important if data is generated at multiple partner sites and/or by multiple individuals. 

2. If data fields are annotated with terms from freely chosen ontologies (URL_TO_INSERT_TERM_6690 https://fairsharing.org/search?recordType=terminology_artefact)  (rather than those dictated by a common model (URL_TO_INSERT_TERM_6685 https://fairsharing.org/search?recordType=model_and_format)  such as CDSIC), care should be taken to avoid picking terms from ontologies (URL_TO_INSERT_TERM_6691 https://fairsharing.org/search?recordType=terminology_artefact)  at random. If a set of concepts are all available in one ontology (URL_TO_INSERT_TERM_6686 https://fairsharing.org/search?recordType=terminology_artefact) , this ontology (URL_TO_INSERT_TERM_6687 https://fairsharing.org/search?recordType=terminology_artefact)  should be preferred over a set of ontologies (URL_TO_INSERT_TERM_6692 https://fairsharing.org/search?recordType=terminology_artefact) . Map (URL_TO_INSERT_RECORD_6693 https://fairsharing.org/FAIRsharing.53edcc) ping services such as [OxO](https://www.ebi.ac.uk/spot/oxo (URL_TO_INSERT_RECORD_6694 https://fairsharing.org/FAIRsharing.0c6fea) /) are available to verify whether a term of interest in one ontology (URL_TO_INSERT_TERM_6688 https://fairsharing.org/search?recordType=terminology_artefact)  has an equivalent term in another ontology (URL_TO_INSERT_TERM_6689 https://fairsharing.org/search?recordType=terminology_artefact) .

3. Restrictions of allowed values for a given field should ideally be limited to a single ontology (URL_TO_INSERT_TERM_6695 https://fairsharing.org/search?recordType=terminology_artefact)  and better yet, to a single branch of a chosen ontology (URL_TO_INSERT_TERM_6696 https://fairsharing.org/search?recordType=terminology_artefact) . This will vastly improve the semantic queryability as well as the consistency and interoperability of the data. 

4. Many ontologies (URL_TO_INSERT_TERM_6699 https://fairsharing.org/search?recordType=terminology_artefact)  and vocabularies reuse concepts from other ontologies (URL_TO_INSERT_TERM_6700 https://fairsharing.org/search?recordType=terminology_artefact) , in line with best practice in ontology (URL_TO_INSERT_TERM_6697 https://fairsharing.org/search?recordType=terminology_artefact)  design, to limit duplication of efforts and proliferation of parallel synonymous concepts. Care should however be taken to use concepts in the most appropriate environment. This is usually their original source unless they are used as part of a larger set of terms. As an example, the Experimental Factor Ontology (URL_TO_INSERT_TERM_6698 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_6707 https://fairsharing.org/FAIRsharing.1gr4tz)  (EFO) reuses concepts from a range of ontologies (URL_TO_INSERT_TERM_6701 https://fairsharing.org/search?recordType=terminology_artefact) , including species from the NCBI taxonomy (URL_TO_INSERT_RECORD_6702 https://fairsharing.org/FAIRsharing.fj07xj) , assays from OBI (URL_TO_INSERT_RECORD_6704 https://fairsharing.org/FAIRsharing.284e1z) , and diseases and phenotypes from MONDO (URL_TO_INSERT_RECORD_6705 https://fairsharing.org/FAIRsharing.b2979t)  and HP (URL_TO_INSERT_RECORD_6706 https://fairsharing.org/FAIRsharing.kbtt7f) O. If annotating a dataset or resource which covers all of these concepts, it therefore makes sense to use EFO (URL_TO_INSERT_RECORD_6708 https://fairsharing.org/FAIRsharing.1gr4tz)  as the primary annotation source. However, if only annotations for species are required, the NCBI taxonomy (URL_TO_INSERT_RECORD_6703 https://fairsharing.org/FAIRsharing.fj07xj)  should be used directly to ensure completeness, since not all species in NCBItaxon will have been imported into EFO (URL_TO_INSERT_RECORD_6709 https://fairsharing.org/FAIRsharing.1gr4tz) .



### Selection Criteria

A set of widely accepted criteria for selecting terminologies (URL_TO_INSERT_TERM_6713 https://fairsharing.org/search?recordType=terminology_artefact)  (or other reporting standard (URL_TO_INSERT_TERM_6710 https://fairsharing.org/search?fairsharingRegistry=Standard) s) does not exist. There are however a number of excellent publications such as ["A sea of standard (URL_TO_INSERT_TERM_6711 https://fairsharing.org/search?fairsharingRegistry=Standard) s for omics data: sink or swim?"](https://doi.org/10.1136/amiajnl-2013-002066) {footcite}`pmid24076747` and ["Ten Simple Rules for Selection a Bio-ontology"](https://doi.org/10.1371/journal.pcbi.1004743) {footcite}`pmid26867217` providing some guidance on the subject. Below are a set of suggested criteria for evaluating the suitability of a terminology (URL_TO_INSERT_TERM_6712 https://fairsharing.org/search?recordType=terminology_artefact)  resource.


*   **Exclusion criteria**:
    * 🔸 Absent licence or terms of use (_indicator of usability_)
    * 🔸 Restrictive licences or terms of use with restrictions on redistribution and reuse 
    * 🔸 Absence of term definitions 
    * 🔸 Absence of sufficient class metadata (_indicator of quality_)
    * 🔸 Absence of sustainability indicators (_absence of funding records_) 
 
*   **Inclusion criteria**:
    * 🔰  Scope and coverage meets the requirements of the concept identified
    * 🔰  Unique URI (URL_TO_INSERT_RECORD_6714 https://fairsharing.org/FAIRsharing.d261e1) , textual definition and IDs for each term
    * 🔰  Resource releases are versioned
    * 🔰  Size of resource (_indicator of coverage_)
    * 🔰  Number of classes and subclasses (_indicator of depth_)
    * 🔰  Number of terms having definitions and synonyms (_indicator of richness_)
    * 🔰  Presence of a help desk and contact point (_indicator of community support_)
    * 🔰  Presence of term submission tracker/issue tracker (_indicator of resource agility and capability to grow upon request_)
    * 🔰  Potential integrative nature of the resource (_as indicator of translational application potential_)
    * 🔰  Licensing informat (URL_TO_INSERT_TERM_6715 https://fairsharing.org/search?recordType=model_and_format) ion available (_as indicator of freedom to use_)
    * 🔰  Use of a top level ontology (URL_TO_INSERT_TERM_6716 https://fairsharing.org/search?recordType=terminology_artefact)  (_as indicator of a resource built for generic use_)
    * 🔰  Pragmatism (_as indicator of actual, current real life practice)_
    * 🔰  Possibility of collaborating: the resource accepts complaints/remarks that aim to fix or improve the terminology (URL_TO_INSERT_TERM_6717 https://fairsharing.org/search?recordType=terminology_artefact) , while the resource organisation commits to fix or improve the terminology (URL_TO_INSERT_TERM_6718 https://fairsharing.org/search?recordType=terminology_artefact)  in brief delays (one month after receipt?)


### Set of Core Terminologies 

The terminologies (URL_TO_INSERT_TERM_6719 https://fairsharing.org/search?recordType=terminology_artefact)  presented here have been organized by theme and scope. When possible, sections are organized by `granularity levels`, progressing from `macroscopic scale` (organism) to `microscopic scale` (tissue, cells) and `molecular scale` (macromolecules, proteins, small molecules, xenobiotic chemicals).
Domains also cover `processes` or `actions` and their `participants` or `agents` but also can be organized from `general/generic` (disease) to `specialized/specific` (infectious disease).


#### Organism, Organism Parts and Developmental Stages

The resources listed here focus on providing structured vocabularies to describe `taxonomic` and `anatomical` informat (URL_TO_INSERT_TERM_6720 https://fairsharing.org/search?recordType=model_and_format) ion. 

|Scope|Name|File location|Top-Level Ontology (URL_TO_INSERT_TERM_6721 https://fairsharing.org/search?recordType=terminology_artefact) |Licence|Issue Tracker URI (URL_TO_INSERT_RECORD_6722 https://fairsharing.org/FAIRsharing.d261e1) |Comment|
|--- |--- |--- |--- |--- |--- |--- |
|**Organism**|NCBITaxonomy|http://purl.obolibrary.org/obo/ncbitaxon.owl|none specified| [UMLS license](https://uts.nlm.nih.gov/license.html)|||
|**Vertebrate Anatomy**|UBERON|http://purl.obolibrary.org/obo/uberon/ext.owl http://purl.obolibrary.org/obo/uberon/ext.obo|BFO| [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) |https://github.com (URL_TO_INSERT_RECORD_6723 https://fairsharing.org/FAIRsharing.c55d5e) /obophenotype/uberon/issues|Integrative Resource engineered to go across species|
|**Human Anatomy**| Foundational Model (URL_TO_INSERT_TERM_6724 https://fairsharing.org/search?recordType=model_and_format)  of Anatomy (URL_TO_INSERT_RECORD_6725 https://fairsharing.org/FAIRsharing.x56jsy)  (FMA) | http://purl.obolibrary.org/obo/fma.owl | | [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) |https://sourceforge.net (URL_TO_INSERT_RECORD_6726 https://fairsharing.org/FAIRsharing.b138b5) /p/obo/foundational-model-of-anatomy-fma-requests/| Excellent cross-referencing with Uberon|
| **Human Developmental Stages** | Human Developmental Stages | http://purl.obolibrary.org/obo/hsapdv.owl | | [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) |
|**Mouse Anatomy**| Mouse Anatomy (MA)| http://purl.obolibrary.org/obo/ma.owl| |[CC-by 4.0](https://creativecommons.org/licenses/by/4.0/)| https://github.com (URL_TO_INSERT_RECORD_6727 https://fairsharing.org/FAIRsharing.c55d5e) /obophenotype/mouse-anatomy-ontology/issues ||
|**Strain**|Rat Strain Ontology (URL_TO_INSERT_RECORD_6729 https://fairsharing.org/FAIRsharing.vajn3f) |http://purl.obolibrary.org/obo/rs.owl| | [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/) | https://github.com (URL_TO_INSERT_RECORD_6728 https://fairsharing.org/FAIRsharing.c55d5e) /rat-genome-database/RS-Rat-Strain-Ontology/issues ||


In research (URL_TO_INSERT_RECORD_6732 https://fairsharing.org/FAIRsharing.52b22c) , many different model (URL_TO_INSERT_TERM_6730 https://fairsharing.org/search?recordType=model_and_format)  organisms are used (e.g. Dogs, Monkeys...) and specialized resources are available for many model (URL_TO_INSERT_TERM_6731 https://fairsharing.org/search?recordType=model_and_format)  organisms, including C. elegans, Drosophila, Xenopus, Zebrafish, plants and fungi. Use the selection criteria introduced earlier to gauge their value in the data management workflow and their impact on data integration tasks.




#### Diseases and Phenotype

Biology is a complex field and observable manifestations of biological processes in living organisms vary, dependant on genetic background and environmental factors. Working on correlating genetic features with observable (phenotypic) ones, biologists rely heavily on such variables in the quest of disease biomarkers, which could be used to identify possible therapeutic targets. The main challenge is to ensure efficient machine actionable descriptions of these observable features.


|Scope|Name|File location|Top-Level Ontology (URL_TO_INSERT_TERM_6733 https://fairsharing.org/search?recordType=terminology_artefact) |Licence|Issue Tracker URI (URL_TO_INSERT_RECORD_6734 https://fairsharing.org/FAIRsharing.d261e1) |
|--- |--- |--- |--- |--- |--- | 
|**Pathology/Disease (generic)**|||||
| |SNOMED-CT| View on [Bioportal](https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_6735 https://fairsharing.org/FAIRsharing.4m97ah) /ontologies/SNOMEDCT?p=summary) | |[SNOMED license](http://www.nlm.nih.gov/databases/umls.html) - part of the UMLS license|| |
| |NCI Thesaurus (URL_TO_INSERT_RECORD_6736 https://fairsharing.org/FAIRsharing.4cvwxa) |http://evs.nci.nih.gov/ftp1/NCI_Thesaurus| | [NCI license](http://evs.nci.nih.gov/ftp1/NCI_Thesaurus/ThesaurusTermsofUse.htm)|| |
| |International Classification of Diseases (ICD-10 (URL_TO_INSERT_RECORD_6737 https://fairsharing.org/FAIRsharing.nj16g) )| View on [WHO site](https://icd.who.int/browse10/2010/en)| | [WHO license](http://www.who.int (URL_TO_INSERT_RECORD_6738 https://fairsharing.org/3498) /about/copyright/en/)|||
| | Unified Medical Language System (UMLS) | https://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html | |[UMLS license](http://www.nlm.nih.gov/databases/umls.html)|||
| | Disease Ontology (URL_TO_INSERT_TERM_6739 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_6742 https://fairsharing.org/FAIRsharing.8b6wfq)  Identifier (URL_TO_INSERT_TERM_6740 https://fairsharing.org/search?recordType=identifier_schema) s (DOID (URL_TO_INSERT_RECORD_6743 https://fairsharing.org/FAIRsharing.8b6wfq) ) |http://purl.obolibrary.org/obo/doid.owl|BFO| [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) |https://github.com (URL_TO_INSERT_RECORD_6741 https://fairsharing.org/FAIRsharing.c55d5e) /DiseaseOntology/HumanDiseaseOntology/issues| | 
| |MONDO (URL_TO_INSERT_RECORD_6746 https://fairsharing.org/FAIRsharing.b2979t)  Disease Ontology (URL_TO_INSERT_TERM_6744 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_6747 https://fairsharing.org/FAIRsharing.8b6wfq) <sup>*</sup> |http://purl.obolibrary.org/obo/mondo.owl|BFO| [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) |https://github.com (URL_TO_INSERT_RECORD_6745 https://fairsharing.org/FAIRsharing.c55d5e) /monarch-initiative/mondo/issues| 
| |Infectious Disease Ontology (URL_TO_INSERT_TERM_6748 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_6749 https://fairsharing.org/FAIRsharing.8b6wfq)  (IDO) |https://code.google.com/p/infectious-disease-ontology/source/browse/trunk/src/ontology/ido-core/ido-main.owl|BFO| [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) |https://code.google.com/p/infectious-disease-ontology/issues/list| |
|**Phenotype**|||||
| | Human Phenotype (HP) |http://purl.obolibrary.org/obo/hp.owl|BFO| [HPO Licence](https://hpo.jax.org (URL_TO_INSERT_RECORD_6751 https://fairsharing.org/FAIRsharing.kbtt7f) /app/license) |https://github.com (URL_TO_INSERT_RECORD_6750 https://fairsharing.org/FAIRsharing.c55d5e) /obophenotype/human-phenotype-ontology/issues/|
| |Medical Dictionary for Regulator (URL_TO_INSERT_RECORD_6754 https://fairsharing.org/FAIRsharing.ey49c6) y Activities Terminology (URL_TO_INSERT_TERM_6752 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_6755 https://fairsharing.org/FAIRsharing.ad3137)  (MedDRA (URL_TO_INSERT_RECORD_6756 https://fairsharing.org/FAIRsharing.ad3137) )| View on [Bioportal](https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_6753 https://fairsharing.org/FAIRsharing.4m97ah) /ontologies/MEDDRA) || Academic: Free accessible <br/> Commercial contact MSSO|https://mssotools.com/webcr/ login required|
| | Mammalian Phenotype (MP) | http://purl.obolibrary.org/obo/mp.owl | | [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) | https://github.com (URL_TO_INSERT_RECORD_6757 https://fairsharing.org/FAIRsharing.c55d5e) /obophenotype/mammalian-phenotype-ontology/issues | 


> _<sup>*</sup>MONDO (URL_TO_INSERT_RECORD_6770 https://fairsharing.org/FAIRsharing.b2979t)  was born of an effort to harmonise disease definitions from a number sources, includig [OMIM](https://www.omim.org (URL_TO_INSERT_RECORD_6774 https://fairsharing.org/FAIRsharing.b084yh)  (URL_TO_INSERT_RECORD_6778 https://fairsharing.org/FAIRsharing.9qkaz9) /) (Online Mendelian Inheritance in Man (URL_TO_INSERT_RECORD_6777 https://fairsharing.org/FAIRsharing.9qkaz9) ), [Orphanet](https://www.orpha.net/), EFO (URL_TO_INSERT_RECORD_6775 https://fairsharing.org/FAIRsharing.1gr4tz)  and DOI (URL_TO_INSERT_RECORD_6762 https://fairsharing.org/FAIRsharing.hFLKCn) D (URL_TO_INSERT_RECORD_6772 https://fairsharing.org/FAIRsharing.8b6wfq) , with work in progress to include NCIt (URL_TO_INSERT_RECORD_6764 https://fairsharing.org/FAIRsharing.4cvwxa) . The OWL (URL_TO_INSERT_RECORD_6763 https://fairsharing.org/FAIRsharing.atygwy)  version includes axiomatisation using CL (URL_TO_INSERT_RECORD_6768 https://fairsharing.org/FAIRsharing.j9y503) , Uberon, GO (URL_TO_INSERT_RECORD_6766 https://fairsharing.org/FAIRsharing.6xq0ee) , HP (URL_TO_INSERT_RECORD_6773 https://fairsharing.org/FAIRsharing.kbtt7f) , RO (URL_TO_INSERT_RECORD_6769 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_6771 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_6776 https://fairsharing.org/FAIRsharing.cp0ybc)  & NCBITaxon. The ontology (URL_TO_INSERT_TERM_6758 https://fairsharing.org/search?recordType=terminology_artefact)  is under active development by a range of ontology (URL_TO_INSERT_TERM_6759 https://fairsharing.org/search?recordType=terminology_artefact)  and domain experts. If no other limiting requirements dictate the use of an alternative ontology (URL_TO_INSERT_TERM_6760 https://fairsharing.org/search?recordType=terminology_artefact)  (e.g. use of NCIt (URL_TO_INSERT_RECORD_6765 https://fairsharing.org/FAIRsharing.4cvwxa) axon as part of a CDI (URL_TO_INSERT_RECORD_6767 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_6779 https://fairsharing.org/3525) -compliant dataset), it is therefore the most recommended open source ontology (URL_TO_INSERT_TERM_6761 https://fairsharing.org/search?recordType=terminology_artefact)  from the above list._

As with anatomy in the previous section, there is a growing body of organism-specific phenotype resources, such as C. elegans, Drosophila, Fission Yeast, Xenopus and Zebrafish. 


#### Pathology and Disease Specific Resources

There is a wide range of ontologies (URL_TO_INSERT_TERM_6782 https://fairsharing.org/search?recordType=terminology_artefact)  available for specific diseases or disease types. Some examples are given below but this list is by no means exhaustive. Check ontology (URL_TO_INSERT_TERM_6781 https://fairsharing.org/search?recordType=terminology_artefact)  repositories (URL_TO_INSERT_TERM_6780 https://fairsharing.org/search?recordType=repository)  such as [OLS](https://www.ebi.ac.uk/ols/ontologies), [Bioportal](https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_6784 https://fairsharing.org/FAIRsharing.4m97ah) /ontologies) or the [OBO Foundry (URL_TO_INSERT_RECORD_6785 https://fairsharing.org/FAIRsharing.847069) ](http://obofoundry.org/) for up-to-date lists of available ontologies (URL_TO_INSERT_TERM_6783 https://fairsharing.org/search?recordType=terminology_artefact) 

|Scope|Name|File location|Top-Level Ontology (URL_TO_INSERT_TERM_6786 https://fairsharing.org/search?recordType=terminology_artefact) |Licence|Issue Tracker URI (URL_TO_INSERT_RECORD_6787 https://fairsharing.org/FAIRsharing.d261e1) |
|--- |--- |--- |--- |--- |--- |
|**Malaria**|Malaria Ontology (URL_TO_INSERT_TERM_6788 https://fairsharing.org/search?recordType=terminology_artefact)  (IDOMAL (URL_TO_INSERT_RECORD_6789 https://fairsharing.org/FAIRsharing.2q8c28) )||BFO| [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)  ||
|**Alzheimer Disease**| Alzheimer's Disease Ontology (URL_TO_INSERT_TERM_6790 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_6791 https://fairsharing.org/FAIRsharing.8b6wfq)  (URL_TO_INSERT_RECORD_6792 https://fairsharing.org/FAIRsharing.ckd4rf)  (ADO) |https://www.scai.fraunhofer.de/content/dam/scai/de/downloads/bioinformatik/ontologies/ADO/ADO.zip|BFO|||
|**Rare disorder**| Orphanet (URL_TO_INSERT_RECORD_6797 https://fairsharing.org/FAIRsharing.6bd5k6)  Rare Disease Ontology (URL_TO_INSERT_TERM_6793 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_6796 https://fairsharing.org/FAIRsharing.8b6wfq)  (ORDO (URL_TO_INSERT_RECORD_6795 https://fairsharing.org/FAIRsharing.1566e7)  (URL_TO_INSERT_RECORD_6798 https://fairsharing.org/FAIRsharing.pbbnwa) ) | View on [Bioportal](https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_6794 https://fairsharing.org/FAIRsharing.4m97ah) /ontologies/ORDO)||[CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)||



#### Cellular entities

Following on through our review of semantic resources by granularity levels, this section details a number of reference resources which provide coverage for the describing `cell types`, `cell lines` {footcite}`pmid29805321` and `cellular phenotypes`.

|Scope|Name|File location|Top-Level Ontology (URL_TO_INSERT_TERM_6799 https://fairsharing.org/search?recordType=terminology_artefact) |Licence|Issue Tracker URI (URL_TO_INSERT_RECORD_6800 https://fairsharing.org/FAIRsharing.d261e1) |
|--- |--- |--- |--- |--- |--- |
|**Cell**| Cell Ontology (URL_TO_INSERT_TERM_6801 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_6802 https://fairsharing.org/FAIRsharing.j9y503)  (CL) |http://purl.obolibrary.org/obo/cl.owl http://purl.obolibrary.org/obo/cl.obo|BFO| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/)|https://code.google.com/p/cell-ontology/issues/list|
|**Cell Lines**| 
| | Cellosaurus|ftp://ftp.expasy.org/databases/cellosaurus/cellosaurus.obo ftp://ftp.expasy.org/databases/cellosaurus|| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/)||
| | Cell Line Ontology (URL_TO_INSERT_TERM_6803 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_6807 https://fairsharing.org/FAIRsharing.4dvtcz)  (CLO) |[https://github.com (URL_TO_INSERT_RECORD_6804 https://fairsharing.org/FAIRsharing.c55d5e) /CLO-ontology/CLO/blob/master/src/ontology/clo.owl](https://github.com (URL_TO_INSERT_RECORD_6805 https://fairsharing.org/FAIRsharing.c55d5e) /CLO-ontology/CLO/blob/master/src/ontology/clo.owl)|BFO| [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) |https://github.com (URL_TO_INSERT_RECORD_6806 https://fairsharing.org/FAIRsharing.c55d5e) /CLO-ontology/CLO/issues|
|**Cell Molecular Phenotype**|Cell Molecular Phenotype Ontology (URL_TO_INSERT_TERM_6808 https://fairsharing.org/search?recordType=terminology_artefact)  (CMPO (URL_TO_INSERT_RECORD_6809 https://fairsharing.org/FAIRsharing.knp11s) ) |https://github.com (URL_TO_INSERT_RECORD_6810 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/CMPO/releases/| | | https://github.com (URL_TO_INSERT_RECORD_6811 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/CMPO/issues |




#### Molecular Entities

This section highlights the major and most widely used OBO (URL_TO_INSERT_RECORD_6813 https://fairsharing.org/FAIRsharing.847069)  Foundry (URL_TO_INSERT_RECORD_6812 https://fairsharing.org/FAIRsharing.847069)  resources for `molecules of biological relevance` as well as `molecular structures`, `biological processes` and `cellular components` 


|Scope|Name|File location|Top-Level Ontology (URL_TO_INSERT_TERM_6814 https://fairsharing.org/search?recordType=terminology_artefact) |Licence|Issue Tracker URI (URL_TO_INSERT_RECORD_6815 https://fairsharing.org/FAIRsharing.d261e1) |
|--- |--- |--- |--- |--- |--- |
|**Chemicals and Small Molecules**| Chemical Entities of Biological Interest (URL_TO_INSERT_RECORD_6816 https://fairsharing.org/FAIRsharing.62qk8w)  (ChEBI)|[ChEBI](https://www.ebi.ac.uk/chebi (URL_TO_INSERT_RECORD_6817 https://fairsharing.org/FAIRsharing.62qk8w) /)| BFO|[CC-by 4.0](https://creativecommons.org/licenses/by/4.0/) |https://github.com (URL_TO_INSERT_RECORD_6818 https://fairsharing.org/FAIRsharing.c55d5e) /ebi-chebi/ChEBI/issues|
|**Gene Function, Molecular Component, Biological Process**| Gene Ontology (URL_TO_INSERT_TERM_6819 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_6820 https://fairsharing.org/FAIRsharing.6xq0ee)  (GO) |http://purl.obolibrary.org/obo/go.obo http://purl.obolibrary.org/obo/go.owl|BFO| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/) |http://sourceforge.net (URL_TO_INSERT_RECORD_6821 https://fairsharing.org/FAIRsharing.b138b5) /p/geneontology/ontology-requests/|
|**Protein (URL_TO_INSERT_RECORD_6823 https://fairsharing.org/FAIRsharing.rtndct) /peptide**| Protein (URL_TO_INSERT_RECORD_6824 https://fairsharing.org/FAIRsharing.rtndct)  Ontology (URL_TO_INSERT_TERM_6822 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_6826 https://fairsharing.org/FAIRsharing.4ndncv)  (PRO) |https://proconsortium.org (URL_TO_INSERT_RECORD_6827 https://fairsharing.org/FAIRsharing.4ndncv)  |BFO| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/) |https://github.com (URL_TO_INSERT_RECORD_6825 https://fairsharing.org/FAIRsharing.c55d5e) /PROconsortium/PRoteinOntology/issues|


Besides, these open ontologies (URL_TO_INSERT_TERM_6828 https://fairsharing.org/search?recordType=terminology_artefact) , in the context of clinically relevant work where drug formulation require recording and description, the following resources are relevant.

|Scope|Name|File location|Top-Level Ontology (URL_TO_INSERT_TERM_6829 https://fairsharing.org/search?recordType=terminology_artefact) |Licence|Issue Tracker URI (URL_TO_INSERT_RECORD_6830 https://fairsharing.org/FAIRsharing.d261e1) |
|--- |--- |--- |--- |--- |--- |
| **Drug** |
| | National Drug File (URL_TO_INSERT_RECORD_6832 https://fairsharing.org/FAIRsharing.901nkj) | View on [Bioportal](https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_6831 https://fairsharing.org/FAIRsharing.4m97ah) /ontologies/NDFRT (URL_TO_INSERT_RECORD_6833 https://fairsharing.org/FAIRsharing.901nkj) ) ||[NIH license](https://uts.nlm.nih.gov/license.html)||
| | The Drug Ontology (URL_TO_INSERT_TERM_6834 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_6835 https://fairsharing.org/FAIRsharing.w5ntfd)  (DRON) |  http://purl.obolibrary.org/obo/dron.owl | BFO | [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) | https://ontology.atlassian.net/browse/DRON |
| | RxNORM (URL_TO_INSERT_RECORD_6837 https://fairsharing.org/FAIRsharing.36pf8q)  |View on [Bioportal](https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_6836 https://fairsharing.org/FAIRsharing.4m97ah) /ontologies/RXNORM) | |[RxNORM (URL_TO_INSERT_RECORD_6838 https://fairsharing.org/FAIRsharing.36pf8q)  license](http://www.nlm.nih.gov/databases/umls.html) - part of the UMLS license||


#### Assays and Technologies

The resources listed in this section are providing key descriptors bridging data acquisition procedures (as used in a clinical setting and wet lab work) with instruments, units of measurements, endpoints as well as sometimes the biological process or molecular entities of biological significance.
Some of the resources are specialized semantic artefacts developed (URL_TO_INSERT_RECORD_6840 https://fairsharing.org/FAIRsharing.31385c)  to support the standard (URL_TO_INSERT_TERM_6839 https://fairsharing.org/search?fairsharingRegistry=Standard) ized reporting of data modalities.

|Scope|Name|File location|Top-Level Ontology (URL_TO_INSERT_TERM_6841 https://fairsharing.org/search?recordType=terminology_artefact) |Licence|Issue Tracker URI (URL_TO_INSERT_RECORD_6842 https://fairsharing.org/FAIRsharing.d261e1) |
|--- |--- |--- |--- |--- |--- |
|**Radiology**| Radiology Lexicon (URL_TO_INSERT_RECORD_6844 https://fairsharing.org/FAIRsharing.shm2f2)  (RADLex) | View on [Bioportal](https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_6843 https://fairsharing.org/FAIRsharing.4m97ah) /ontologies/RADLEX) ||||
|**Medical Imaging**|DICOM (URL_TO_INSERT_RECORD_6845 https://fairsharing.org/FAIRsharing.b7z8by) |http://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_D.html (URL_TO_INSERT_RECORD_6846 https://fairsharing.org/FAIRsharing.p1ss22) ||||
|**Sample Processing/Reagents/Instruments Assay Definition**| Ontology (URL_TO_INSERT_TERM_6847 https://fairsharing.org/search?recordType=terminology_artefact)  for Biomedical Investigations (URL_TO_INSERT_RECORD_6849 https://fairsharing.org/FAIRsharing.284e1z)  (OBI) |http://purl.obolibrary.org/obo/obi.owl|BFO| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/)|https://github.com (URL_TO_INSERT_RECORD_6848 https://fairsharing.org/FAIRsharing.c55d5e) /obi-ontology/obi/issues|
|**Biological screening assays and their results including high-throughput screening (HTS)**| BioAssay Ontology (URL_TO_INSERT_TERM_6850 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_6852 https://fairsharing.org/FAIRsharing.mye76w)  (BAO) |http://www.bioassayontology.org (URL_TO_INSERT_RECORD_6851 https://fairsharing.org/FAIRsharing.farr39)  (URL_TO_INSERT_RECORD_6853 https://fairsharing.org/FAIRsharing.mye76w) /bao/bao_complete_bfo_dev.owl|BFO| [CC-by-SA 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) ||
|**Mass Spectrometry (instrument/acquisition parameter/spectrum related informat (URL_TO_INSERT_TERM_6855 https://fairsharing.org/search?recordType=model_and_format) ion)**| HUPO Proteomics Standard (URL_TO_INSERT_TERM_6854 https://fairsharing.org/search?fairsharingRegistry=Standard) s Initiative (URL_TO_INSERT_RECORD_6856 https://fairsharing.org/3514) -Mass Spectrometry controlled vocabulary (PSI-MS) |https://github.com (URL_TO_INSERT_RECORD_6857 https://fairsharing.org/FAIRsharing.c55d5e) /HUPO-PSI/psi-ms-CV |none specified| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/)|https://github.com (URL_TO_INSERT_RECORD_6858 https://fairsharing.org/FAIRsharing.c55d5e) /HUPO-PSI/psi-ms-CV/issues |
|**NMR Spectroscopy (instrument/acquisition parameter/spectrum related informat (URL_TO_INSERT_TERM_6859 https://fairsharing.org/search?recordType=model_and_format) ion)**| Nuclear Magnetic Resonance Controlled Vocabulary (URL_TO_INSERT_RECORD_6862 https://fairsharing.org/FAIRsharing.xm7tkj)  (NMR-CV) |http://nmrml.org (URL_TO_INSERT_RECORD_6860 https://fairsharing.org/FAIRsharing.es03fk) /cv (URL_TO_INSERT_RECORD_6863 https://fairsharing.org/FAIRsharing.xm7tkj) /v1.0.rc1/nmrCV.owl|BFO| [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) |https://github.com (URL_TO_INSERT_RECORD_6861 https://fairsharing.org/FAIRsharing.c55d5e) /nmrML/nmrML/issues?state=open|
|**Laboratory test**| Logical Observation Identifier (URL_TO_INSERT_TERM_6864 https://fairsharing.org/search?recordType=identifier_schema)  Names and Codes (URL_TO_INSERT_RECORD_6865 https://fairsharing.org/FAIRsharing.2mk2zb)  (LOINC (URL_TO_INSERT_RECORD_6866 https://fairsharing.org/FAIRsharing.2mk2zb) ) | LOINC (URL_TO_INSERT_RECORD_6867 https://fairsharing.org/FAIRsharing.2mk2zb)  and RELMA Complete Download File https://loinc.org (URL_TO_INSERT_RECORD_6868 https://fairsharing.org/FAIRsharing.2mk2zb) /downloads/ |none specified| [RELMA license](https://uts.nlm.nih.gov/license.html) ||
|**Units** | Units Ontology (URL_TO_INSERT_TERM_6869 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_6871 https://fairsharing.org/FAIRsharing.mjnypw)  (UO) | http://purl.obolibrary.org/obo/uo.owl | | [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) | https://github.com (URL_TO_INSERT_RECORD_6870 https://fairsharing.org/FAIRsharing.c55d5e) /bio-ontology-research-group/unit-ontology (URL_TO_INSERT_RECORD_6872 https://fairsharing.org/FAIRsharing.mjnypw) /issues |

Some multi-domain ontologies (URL_TO_INSERT_TERM_6876 https://fairsharing.org/search?recordType=terminology_artefact)  such as the NCI Thesaurus (URL_TO_INSERT_RECORD_6877 https://fairsharing.org/FAIRsharing.4cvwxa)  (NCIt (URL_TO_INSERT_RECORD_6878 https://fairsharing.org/FAIRsharing.4cvwxa) ) and the Experimental Factor Ontology (URL_TO_INSERT_TERM_6874 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_6879 https://fairsharing.org/FAIRsharing.1gr4tz)  (EFO) also cover aspects of the above domains such as assays and sample collection (URL_TO_INSERT_TERM_6873 https://fairsharing.org/search?recordType=collection)  and processing. Depending on the overall context of a resource selection process, it can make more sense to use a multi-domain ontology (URL_TO_INSERT_TERM_6875 https://fairsharing.org/search?recordType=terminology_artefact)  with suitable coverage to improve consistency and interoperability within a resource or dataset.


Finally, a resource exists that describes statistical measures, statistical tests or methods as well as statistically relevant graphical representations. It may be used for reporting results and annotating experimental results (URL_TO_INSERT_RECORD_6880 https://fairsharing.org/FAIRsharing.QlUiql) .



|Scope|Name|File location|Top-Level Ontology (URL_TO_INSERT_TERM_6881 https://fairsharing.org/search?recordType=terminology_artefact) |Licence|Issue Tracker URI (URL_TO_INSERT_RECORD_6882 https://fairsharing.org/FAIRsharing.d261e1) |
|--- |--- |--- |--- |--- |--- |
| **Experimental Design, Statistical Methods and Statistical Measures**| Statistical Methods Ontology (URL_TO_INSERT_TERM_6883 https://fairsharing.org/search?recordType=terminology_artefact)  (STATO (URL_TO_INSERT_RECORD_6885 https://fairsharing.org/FAIRsharing.na5xp) ) |[http://stato-ontology.org (URL_TO_INSERT_RECORD_6886 https://fairsharing.org/FAIRsharing.na5xp) ](http://stato-ontology.org (URL_TO_INSERT_RECORD_6887 https://fairsharing.org/FAIRsharing.na5xp) )|BFO| [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/)|https://github.com (URL_TO_INSERT_RECORD_6884 https://fairsharing.org/FAIRsharing.c55d5e) /ISA-tools/stato/issues?state=open|




### Relations

Also known as `OWL Properties`, their importance may be overlooked by `data scientists` who are not `knowledge engineers` or `ontologists`. These are essential components as, when correctly crafted with a proper understanding of the logical constraints available to semantic languages such as OWL (URL_TO_INSERT_RECORD_6888 https://fairsharing.org/FAIRsharing.atygwy) , are exploited by tools known as `reasoners` to carry the following key tasks:

* `Ontology (URL_TO_INSERT_TERM_6889 https://fairsharing.org/search?recordType=terminology_artefact)  logical consistency` checks
* `Automatic classification` and `inference` tasks
* `Entailments`, i.e. detection of logical consequences resulting from axiomatic definitions (closely related to the point above)

This is particularly important when processing billions of facts expressed as RDF (URL_TO_INSERT_RECORD_6890 https://fairsharing.org/FAIRsharing.p77ph9)  statements. 

One also needs to understand the current limitations in expressivity afforded by the current semantic web languages and the associated axiomatics as well as computational constraints associated with inference. For more *in-depth* review of such topics, the reader is invited to consults the following work {footcite}`pmid15892874` <!--[by Smith et al](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2005-6-5-r46)-->.

In the field of Biology and Biomedicine, the [OBO Foundry (URL_TO_INSERT_RECORD_6892 https://fairsharing.org/FAIRsharing.847069) ](http://obofoundry.org) coordinates the development of interoperable ontologies (URL_TO_INSERT_TERM_6891 https://fairsharing.org/search?recordType=terminology_artefact) . At the core (URL_TO_INSERT_RECORD_6894 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_6895 https://fairsharing.org/FAIRsharing.xMmOCL)  of this interoperation lies the **[Relation Ontology](http://www.obofoundry.org (URL_TO_INSERT_RECORD_6893 https://fairsharing.org/FAIRsharing.847069) /ontology/ro.html)** released under the [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) license.

| Relation Ontology (URL_TO_INSERT_TERM_6896 https://fairsharing.org/search?recordType=terminology_artefact)                | File  | Variant                                                                        |
|---------------------------------|---|--------------------------------------------------------------------------------|
| Relation Ontology (URL_TO_INSERT_TERM_6897 https://fairsharing.org/search?recordType=terminology_artefact)                | [ro.owl](http://purl.obolibrary.org/obo/ro.owl)  | Canonical edition                                                              |
| Relation Ontology (URL_TO_INSERT_TERM_6899 https://fairsharing.org/search?recordType=terminology_artefact)  in obo format (URL_TO_INSERT_TERM_6898 https://fairsharing.org/search?recordType=model_and_format)  | [ro.obo](http://purl.obolibrary.org/obo/ro.obo)  | Has imports merged in                                                          |
| RO (URL_TO_INSERT_RECORD_6901 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_6904 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_6905 https://fairsharing.org/FAIRsharing.cp0ybc)  Core (URL_TO_INSERT_RECORD_6900 https://fairsharing.org/FAIRsharing.xMmOCL)  relations               | [ro/core.owl](http://purl.obolibrary.org/obo/ro/core.owl)  | Minimal subset intended to work with BFO-classes [page](https://github.com (URL_TO_INSERT_RECORD_6903 https://fairsharing.org/FAIRsharing.c55d5e) /oborel/obo-relations (URL_TO_INSERT_RECORD_6902 https://fairsharing.org/FAIRsharing.9w8ea0) /wiki/ROCore)                        |
| RO (URL_TO_INSERT_RECORD_6908 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_6911 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_6913 https://fairsharing.org/FAIRsharing.cp0ybc)  base ontology (URL_TO_INSERT_TERM_6906 https://fairsharing.org/search?recordType=terminology_artefact)                 | [ro/ro-base.owl](http://purl.obolibrary.org/obo/ro/ro-base.owl)  | Axioms defined within RO (URL_TO_INSERT_RECORD_6909 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_6912 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_6914 https://fairsharing.org/FAIRsharing.cp0ybc)  and to be used in imports for other ontologies (URL_TO_INSERT_TERM_6907 https://fairsharing.org/search?recordType=terminology_artefact)  [page](https://github.com (URL_TO_INSERT_RECORD_6910 https://fairsharing.org/FAIRsharing.c55d5e) /INCATools/ontology-development-kit/issues/50) |
| Interaction relations           | [ro/subsets/ro-interaction.owl](http://purl.obolibrary.org/obo/ro/subsets/ro-interaction.owl)  |                                                                                |
| Ecology subset                  | [ro/subsets/ro-eco.owl](http://purl.obolibrary.org/obo/ro/subsets/ro-eco.owl)  | For use in ecology and environmental science                                   |
| Neuroscience subset             | [ro/subsets/ro-neuro.owl](http://purl.obolibrary.org/obo/ro/subsets/ro-neuro.owl)  | For use in neuroscience [page](http://bioinformatics.oxfordjournals.org/content/28/9/1262.long) 

As `knowledge graphs` and `property graphs` gain importance, we can expect the range and depth of relations to mature and expand as more expressivity is needed and progress is made by reasoner technology to fully exploit their benefits.
This would also have to be placed in the context of advances in `Text Mining` and `Machine Learning`, where unsupervised methods start to demonstrate strong potential to detect relations between entities.

The following is an example of how a `defined class` may be created in an ontology (URL_TO_INSERT_TERM_6915 https://fairsharing.org/search?recordType=terminology_artefact) . The code snippet shows one such class being expressed to create a type by specifying a number of `axioms`. These use `relations` (aka OWL (URL_TO_INSERT_RECORD_6916 https://fairsharing.org/FAIRsharing.atygwy)  Properties), which may be set to 

```bash
'B cell, CD19-positive'
equivalentClass :
    'lymphocyte of B lineage, CD19-positive' 
    and ( 'has plasma membrane part' some 'CD19 molecule') 
    and ( 'in taxon' some Mammalia) 
    and ( 'capable of' some 'B cell mediated immunity')
```

Any class satisfying these patterns may be classified by an OWL (URL_TO_INSERT_RECORD_6917 https://fairsharing.org/FAIRsharing.atygwy)  reasoner as a child of that class. So the following class, with such properties that they all satisfy the requirements of the `defined class` declared above (e.g. "Homo sapiens" is_a type of "Mammalia", etc...), will be classified automatically (i.e. without human intervention) by a reasoner such as ELK or Hermit as a child of 'B cell, CD19-positive' .

```bash
'human B cell, CD19-positive'
Class:
    ( 'has plasma membrane part' some 'B-lymphocyte antigen CD19 isoform h2')
    and ( 'in taxon' some 'Homo sapiens') 
    and ( 'capable of' some 'B cell tolerance induction in mucosal-associated lymphoid tissue')

```

The notion is important to grasp as it also explains why not all ontologies (URL_TO_INSERT_TERM_6918 https://fairsharing.org/search?recordType=terminology_artefact)  are compatible, because they may significantly differ in the underlying axioms they rely on to establish their hierarch (URL_TO_INSERT_RECORD_6919 https://fairsharing.org/FAIRsharing.52b22c) ies using reasoners.



## Conclusions

> Selecting semantic resources depends on many different factors. However, the most important factor remains the `context` of the data and associated landscape of data standard (URL_TO_INSERT_TERM_6920 https://fairsharing.org/search?fairsharingRegistry=Standard) s as well as the ultimate integration goal, which will dictate the final choice.
> 
>The selection process remains guided by the need to maximize the potential of data integration with datasets of similar nature and similar value. It also requires a good understanding of the technical and sometimes legal implications these choices will have.

<!-- 
TODO : fill in the links to what-should-I-read-next recipes -->

### What to read next?

* How to build an application ontology (URL_TO_INSERT_TERM_6921 https://fairsharing.org/search?recordType=terminology_artefact) ? {ref}`fcb-interop-ontorobot`
* How to select on ontology (URL_TO_INSERT_TERM_6922 https://fairsharing.org/search?recordType=terminology_artefact)  service? {ref}`fcb-select-onto-service`
* How to deploy an ontology (URL_TO_INSERT_TERM_6923 https://fairsharing.org/search?recordType=terminology_artefact)  server? {ref}`fcb-select-onto-service-criteria`
* [How to establish a minimal metadata profile?] {ref}`fcb-interop-covid-metadata` 

````{rdmkit_panel}
````


<!-- {download}`bibliography-identifier-mapping.bib <./bibref/bibliography-identifier-mapping.bib>` -->

## References
````{dropdown} **References**
```{footbibliography}
```
````

<!-- Smith, B., Ceusters, W., Klagges, B. et al. Relations in biomedical ontologies. Genome Biol 6, R46 (2005). https://doi.org/10.1186/gb-2005-6-5-r46

Rocca-Serra P, Bratfalean D, Richard F, Marshall C, Romacker M., Auffray C, ., … on the behalf of the eTRIKS consortium, . (2016, April 25). eTRIKS Standards Starter Pack Release 1.1 April 2016. Zenodo. http://doi.org/10.5281/zenodo.50825

Malone J, Stevens R, Jupp S, Hancocks T, Parkinson H, Brooksbank C. Ten Simple Rules for Selecting a Bio-ontology. PLoS Comput Biol. 2016;12(2):e1004743. Published 2016 Feb 11. http://doi.org/10.1371/journal.pcbi.1004743

Bairoch A. The Cellosaurus, a cell line knowledge resource. J. Biomol. Tech. (2018) 29:25-38. http://doi.org/10.7171/jbt.18-2902-002.

Sansone, S.-A., McQuilton, P., Rocca-Serra, P., Gonzalez-Beltran, A., Izzo, M., Lister, A.L. and Thurston, M. (2019) FAIRsharing as a community approach to standards, repositories and policies. Nature biotechnology, 37, 358: http://doi.org/10.1038/s41587-019-0080-8.

Hripcsak, G., Ryan, P. B., Duke, J. D., Shah, N. H., Park, R. W., Huser, V., Suchard, M. A., Schuemie, M. J., DeFalco, F. J., Perotte, A., Banda, J. M., Reich, C. G., Schilling, L. M., Matheny, M. E., Meeker, D., Pratt, N., & Madigan, D. (2016). Characterizing treatment pathways at scale using the OHDSI network. Proceedings of the National Academy of Sciences of the United States of America, 113(27), 7329-7336. https://doi.org/10.1073/pnas.1510502113

Hripcsak, George et al. “Observational Health Data Sciences and Informatics (OHDSI): Opportunities for Observational Researchers.” Studies in health technology and informatics vol. 216 (2015): 574-8.
 -->



## Authors

````{authors_fairplus}
Philippe: Writing - Original Draft
Susanna: Writing - Review & Editing, Funding Acquisition
Danielle: Writing - Review & Editing
Alasdair: Writing - Review & Editing
````


## License

````{license_fairplus}
CC-BY-4.0
````
