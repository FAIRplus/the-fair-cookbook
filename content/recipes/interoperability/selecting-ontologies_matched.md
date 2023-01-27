(fcb-selecting-ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact))=
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

The main purpose of this recipe is to provide guidance on how to select the most suitable semantic artefacts given a specific research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) context in general, and when it comes to life and biomedical sciences project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project)s, their main themes, i.e. *risk assessment*, *clinical trial*, *drug discovery* or *fundamental research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)*.


## Graphical Overview


````{dropdown} 
:open:
```{figure} selecting-ontologies.md-figure1.mmd.svg
---
width: 1000px
name: selecting-ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)-figure1
alt:  Which ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) should be used?
---
 Which ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) should be used? Depending on dataset context, domain specific resources may be mandated, such as Clinical Data Interchange Standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s Consortium (CDI(URL_TO_INSERT_RECORD https://www.seadatanet.org/Metadata/CDI-Common-Data-Index)SC(URL_TO_INSERT_RECORD https://www.cdisc.org/)(URL_TO_INSERT_RECORD https://www.cdisc.org/)), Observational Health Data Sciences and Informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ics (OHD(URL_TO_INSERT_RECORD https://purl.obolibrary.org/obo/ohd/home)SI) or Open Biomedical Ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) (OBO(URL_TO_INSERT_RECORD http://www.obofoundry.org/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059)). The Experimantal Factor Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) (EFO(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO)) is specifically used by EMB(URL_TO_INSERT_RECORD http://www.Metabase.net)L-EBI ArrayExpress(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/arrayexpress/)(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/arrayexpress/) to annotated dataset.
```
````

---

## Context is everything

The domain of operation will generally dictate the semantic framework that is most suited to a given dataset. This is simply due to the fact that the advances in data standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)ization in specific fields are such that it is a sound decision to adopt a complete stack of standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s, both syntactic and semantic.

Here, we present the three most common scenarios in biomedical research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/), based on experience garnered during IMI eTRIKS(URL_TO_INSERT_RECORD https://www.etriks.org/standards-starter-pack/) {footcite}`philippe_rocca_serra_2016_50825`:
- [Clinical Trial Data](#clinical-trial-data)
- [Observational Health Data](#observational-health-data)
- [Basic research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) context](#basic-research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)-context)

### Clinical Trial Data

Operating in the field of Clinical Trials means that datasets are generated during `interventional studies`, meaning that research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ers influence and control the predictor variables, which are usually different intensity levels of therapeutic agents, in order to gain insights in terms of benefits in patient outcomes.
In this context, regulator(URL_TO_INSERT_RECORD http://www.bioinformatics.org/regulator)y requirements make it so that data must be recorded in standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) forms to allow for review and appraisal by regulator(URL_TO_INSERT_RECORD http://www.bioinformatics.org/regulator)s such as FDA reviewers in the US. The [CDI(URL_TO_INSERT_RECORD https://www.seadatanet.org/Metadata/CDI-Common-Data-Index)SC(URL_TO_INSERT_RECORD https://www.cdisc.org/)(URL_TO_INSERT_RECORD https://www.cdisc.org/) standards](https://www.cdisc.org(URL_TO_INSERT_RECORD https://www.cdisc.org/)/standards) are the *`de-facto standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)`* in this area, which mandates the use of semantics resources such as:

| Semantic Resource | Domain  | Service |
| -- | -- | -- | 
| CDI(URL_TO_INSERT_RECORD https://www.seadatanet.org/Metadata/CDI-Common-Data-Index)SC(URL_TO_INSERT_RECORD https://www.cdisc.org/)(URL_TO_INSERT_RECORD https://www.cdisc.org/) vocabulary|clinical trial data| EVS |
| NCI Thesaurus(URL_TO_INSERT_RECORD https://ncit.nci.nih.gov)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3034)|biomedicine|EVS,Bioportal(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/),OLS(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/ols/index)|
| SNOME(URL_TO_INSERT_RECORD https://openmicroscopy.org)D-CT|pathology|EVS,Bioportal(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)(§)|
| UMLS|pathology|EVS,Bioportal(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)(§)|
| LOINC(URL_TO_INSERT_RECORD https://loinc.org/)|laboratory tests|Loinc|
| RxNORM(URL_TO_INSERT_RECORD https://www.nlm.nih.gov/research/umls/rxnorm/)(URL_TO_INSERT_RECORD https://www.nlm.nih.gov/research/umls/rxnorm/)|drugs|Bioportal(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)|
| GUDID(URL_TO_INSERT_RECORD https://accessgudid.nlm.nih.gov/)|instruments|FDA|

All available from the [NCBI EVS system](https://evs.nci.nih.gov/), [LOINC](https://loinc.org(URL_TO_INSERT_RECORD https://loinc.org/)/), [OLS](https://www.ebi.ac.uk/ols/index(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/ols/index)) or [Bioportal(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)](https://bioportal.bioontology.org(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)/).
 

```{warning}
Some resources are only available under restrictive licences, which prevent derivative work, which may limit access and use. Furthermore, some licenses are expensive.  
```

### Observational Health Data

This context refers to data collected during `observational studies`, which in contrast to `interventional studies`, draw inferences from a sample to a population where the independent variable is not under the control of the research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)er because of ethical concerns or logistical constraints [1]. This is typically the case in epidemiological work or exposure follow-up studies in the context of risk assessment and evaluation of clinical outcomes. `Observational health data` can also include `electronic health records (EHR)` or ` administrative insurance claims` and allow research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) around acquiring *`real world evidence`* from large corpora of data.
In this specific context, one model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) and associated set of standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s has been particularly successful. With several hundred millions of patients' informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion structured using the **Observational Medical Outcomes Partnership ([OMOP](https://ohdsi.org/omop/))**, the Observational Health Data Sciences and Informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ics ([ODHSI](https://ohdsi.org/)) `open-science community` has laid the foundation for a widely adopted data model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format). Therefore, building a FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)ification process around the standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) stack produced by the ODHSI community needs to be considered if operating in such a `data context`.


|Semantic Resource|Domain |Service|
|--- |---  |--- |
|CDI(URL_TO_INSERT_RECORD https://www.seadatanet.org/Metadata/CDI-Common-Data-Index)SC(URL_TO_INSERT_RECORD https://www.cdisc.org/)(URL_TO_INSERT_RECORD https://www.cdisc.org/) vocabulary|clinical trial data|EVS|
|NCI Thesaurus(URL_TO_INSERT_RECORD https://ncit.nci.nih.gov)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3034)|biomedicine|EVS,Bioportal(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/),OLS(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/ols/index)|
|SNOME(URL_TO_INSERT_RECORD https://openmicroscopy.org)D-CT|pathology|EVS,Bioportal(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)(§)|
|UMLS|pathology|EVS,Bioportal(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)(§)|
|LOINC(URL_TO_INSERT_RECORD https://loinc.org/)|laboratory tests| LOINC(URL_TO_INSERT_RECORD https://loinc.org/) |
|RxNORM(URL_TO_INSERT_RECORD https://www.nlm.nih.gov/research/umls/rxnorm/)(URL_TO_INSERT_RECORD https://www.nlm.nih.gov/research/umls/rxnorm/)|drugs|Bioportal(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)|


For a more detailed overview and deep-dive into the ODHSI and OMO(URL_TO_INSERT_RECORD http://mged.sourceforge.net/ontologies/MGEDontology.php)P(URL_TO_INSERT_RECORD https://github.com/rsc-ontologies/rxno) semantic support, we recommend the reading of the chapter dedicated to the `controlled terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)` [in the **`Book(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059) of OHDSI`**](https://ohdsi.github.io/TheBookOfOhdsi/StandardizedVocabularies.html) {footcite}`pmid27274072`


### Basic research context

This refers to datasets and research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) output being generated using model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) organisms and cellular systems in the context of basic, fundamental research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/). In this arena, the regulator(URL_TO_INSERT_RECORD http://www.bioinformatics.org/regulator)y pressure is much less present but this does not rule out data management best practices and proper arch(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ival requirements.
As a consequence of fewer constraints, research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ers are often confronted with a sea of options. This and the next sections aim to provide some guidance when tasked with deciding on which semantic resource to use.

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

1. The use and implementation of common terminologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) enables the normalisation and harmonisation of both variable labels and allowed values for each field. Implementing the use of common terminologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) in the data collection (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=collection) or curation workflow will ensure consistency of the annotation across all data. This is particularly important if data is generated at multiple partner sites and/or by multiple individuals. 

2. If data fields are annotated with terms from freely chosen ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) (rather than those dictated by a common model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) such as CDSIC), care should be taken to avoid picking terms from ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) at random. If a set of concepts are all available in one ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), this ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) should be preferred over a set of ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact). Map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping services such as [OxO](https://www.ebi.ac.uk/spot/oxo(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/spot/oxo/)/) are available to verify whether a term of interest in one ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) has an equivalent term in another ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact).

3. Restrictions of allowed values for a given field should ideally be limited to a single ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and better yet, to a single branch of a chosen ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact). This will vastly improve the semantic queryability as well as the consistency and interoperability of the data. 

4. Many ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and vocabularies reuse concepts from other ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), in line with best practice in ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) design, to limit duplication of efforts and proliferation of parallel synonymous concepts. Care should however be taken to use concepts in the most appropriate environment. This is usually their original source unless they are used as part of a larger set of terms. As an example, the Experimental Factor Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/) (EFO(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO)) reuses concepts from a range of ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), including species from the NCBI taxonomy(URL_TO_INSERT_RECORD https://www.ncbi.nlm.nih.gov/taxonomy), assays from OBI(URL_TO_INSERT_RECORD http://obi-ontology.org/), and diseases and phenotypes from MO(URL_TO_INSERT_RECORD http://mged.sourceforge.net/ontologies/MGEDontology.php)NDO(URL_TO_INSERT_RECORD https://github.com/monarch-initiative/monarch-disease-ontology) and HP(URL_TO_INSERT_RECORD https://hpo.jax.org/)O(URL_TO_INSERT_RECORD http://plantontology.org/). If annotating a dataset or resource which covers all of these concepts, it therefore makes sense to use EFO(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO) as the primary annotation source. However, if only annotations for species are required, the NCBI taxonomy(URL_TO_INSERT_RECORD https://www.ncbi.nlm.nih.gov/taxonomy) should be used directly to ensure completeness, since not all species in NCBItaxon will have been imported into EFO(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO).



### Selection Criteria

A set of widely accepted criteria for selecting terminologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) (or other reporting standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s) does not exist. There are however a number of excellent publications such as ["A sea of standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s for omics data: sink or swim?"](https://doi.org/10.1136/amiajnl-2013-002066) {footcite}`pmid24076747` and ["Ten Simple Rules for Selection a Bio-ontology"](https://doi.org/10.1371/journal.pcbi.1004743) {footcite}`pmid26867217` providing some guidance on the subject. Below are a set of suggested criteria for evaluating the suitability of a terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) resource.


*   **Exclusion criteria**:
    * 🔸 Absent licence or terms of use (_indicator of usability_)
    * 🔸 Restrictive licences or terms of use with restrictions on redistribution and reuse 
    * 🔸 Absence of term definitions 
    * 🔸 Absence of sufficient class metadata (_indicator of quality_)
    * 🔸 Absence of sustainability indicators (_absence of funding records_) 
 
*   **Inclusion criteria**:
    * 🔰  Scope and coverage meets the requirements of the concept identified
    * 🔰  Unique URI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986), textual definition and IDs for each term
    * 🔰  Resource releases are versioned
    * 🔰  Size of resource (_indicator of coverage_)
    * 🔰  Number of classes and subclasses (_indicator of depth_)
    * 🔰  Number of terms having definitions and synonyms (_indicator of richness_)
    * 🔰  Presence of a help desk and contact point (_indicator of community support_)
    * 🔰  Presence of term submission tracker/issue tracker (_indicator of resource agility and capability to grow upon request_)
    * 🔰  Potential integrative nature of the resource (_as indicator of translational application potential_)
    * 🔰  Licensing informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion available (_as indicator of freedom to use_)
    * 🔰  Use of a top level ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) (_as indicator of a resource built for generic use_)
    * 🔰  Pragmatism (_as indicator of actual, current real life practice)_
    * 🔰  Possibility of collaborating: the resource accepts complaints/remarks that aim to fix or improve the terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), while the resource organisation commits to fix or improve the terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) in brief delays (one month after receipt?)


### Set of Core Terminologies 

The terminologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) presented here have been organized by theme and scope. When possible, sections are organized by `granularity levels`, progressing from `macroscopic scale` (organism) to `microscopic scale` (tissue, cells) and `molecular scale` (macromolecules, proteins, small molecules, xenobiotic chemicals).
Domains also cover `processes` or `actions` and their `participants` or `agents` but also can be organized from `general/generic` (disease) to `specialized/specific` (infectious disease).


#### Organism, Organism Parts and Developmental Stages

The resources listed here focus on providing structured vocabularies to describe `taxonomic` and `anatomical` informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion. 

|Scope|Name|File location|Top-Level Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)|Licence|Issue Tracker URI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)|Comment|
|--- |--- |--- |--- |--- |--- |--- |
|**Organism**|NCBITaxonomy|http://purl.obolibrary.org/obo/ncbitaxon.owl|none specified| [UMLS license](https://uts.nlm.nih.gov/license.html)|||
|**Vertebrate Anatomy**|UBERON|http://purl.obolibrary.org/obo/uberon/ext.owl http://purl.obolibrary.org/obo/uberon/ext.obo|BFO| [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) |https://github.com(URL_TO_INSERT_RECORD https://github.com/)/obophenotype/uberon/issues|Integrative Resource engineered to go across species|
|**Human Anatomy**| Foundational Model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) of Anatomy(URL_TO_INSERT_RECORD http://si.washington.edu/projects/fma) (FMA(URL_TO_INSERT_RECORD http://si.washington.edu/projects/fma)(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/gxd/ma_ontology/)) | http://purl.obolibrary.org/obo/fma.owl | | [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) |https://sourceforge.net(URL_TO_INSERT_RECORD https://sourceforge.net/)/p/obo/foundational-model-of-anatomy-fma-requests/| Excellent cross-referencing with Uberon|
| **Human Developmental Stages** | Human Developmental Stages | http://purl.obolibrary.org/obo/hsapdv.owl | | [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) |
|**Mouse Anatomy**| Mouse Anatomy (MA(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/gxd/ma_ontology/))| http://purl.obolibrary.org/obo/ma.owl| |[CC-by 4.0](https://creativecommons.org/licenses/by/4.0/)| https://github.com(URL_TO_INSERT_RECORD https://github.com/)/obophenotype/mouse-anatomy-ontology/issues ||
|**Strain**|Rat Strain Ontology(URL_TO_INSERT_RECORD http://rgd.mcw.edu/rgdweb/ontology/view.html?acc_id=RS:0000457)|http://purl.obolibrary.org/obo/rs.owl| | [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/) | https://github.com(URL_TO_INSERT_RECORD https://github.com/)/rat-genome-database/RS-Rat-Strain-Ontology/issues ||


In research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/), many different model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) organisms are used (e.g. Dogs, Monkeys...) and specialized resources are available for many model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) organisms, including C. elegans, Drosophila, Xenopus, Zebrafish, plants and fungi. Use the selection criteria introduced earlier to gauge their value in the data management workflow and their impact on data integration tasks.




#### Diseases and Phenotype

Biology is a complex field and observable manifestations of biological processes in living organisms vary, dependant on genetic background and environmental factors. Working on correlating genetic features with observable (phenotypic) ones, biologists rely heavily on such variables in the quest of disease biomarkers, which could be used to identify possible therapeutic targets. The main challenge is to ensure efficient machine actionable descriptions of these observable features.


|Scope|Name|File location|Top-Level Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)|Licence|Issue Tracker URI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)|
|--- |--- |--- |--- |--- |--- | 
|**Pathology/Disease (generic)**|||||
| |SNOME(URL_TO_INSERT_RECORD https://openmicroscopy.org)D-CT| View on [Bioportal](https://bioportal.bioontology.org(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)/ontologies/SNOMEDCT?p=summary) | |[SNOME(URL_TO_INSERT_RECORD https://openmicroscopy.org)D license](http://www.nlm.nih.gov/databases/umls.html) - part of the UMLS license|| |
| |NCI Thesaurus(URL_TO_INSERT_RECORD https://ncit.nci.nih.gov)|http://evs.nci.nih.gov/ftp1/NCI_Thesaurus| | [NCI license](http://evs.nci.nih.gov/ftp1/NCI_Thesaurus/ThesaurusTermsofUse.htm)|| |
| |International Classification of Diseases (ICD-10(URL_TO_INSERT_RECORD http://www.who.int/classifications/icd/en/))| View on [WHO site](https://icd.who.int/browse10/2010/en)| | [WHO license](http://www.who.int(URL_TO_INSERT_RECORD https://www.who.int/)/about/copyright/en/)|||
| | Unified Medical Language System (UMLS) | https://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html | |[UMLS license](http://www.nlm.nih.gov/databases/umls.html)|||
| | Disease Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD http://www.disease-ontology.org) Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s (DOI(URL_TO_INSERT_RECORD https://www.doi.org)D(URL_TO_INSERT_RECORD http://www.disease-ontology.org)) |http://purl.obolibrary.org/obo/doid.owl|BFO| [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) |https://github.com(URL_TO_INSERT_RECORD https://github.com/)/DiseaseOntology/HumanDiseaseOntology/issues| | 
| |MO(URL_TO_INSERT_RECORD http://mged.sourceforge.net/ontologies/MGEDontology.php)NDO(URL_TO_INSERT_RECORD https://github.com/monarch-initiative/monarch-disease-ontology) Disease Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD http://www.disease-ontology.org)<sup>*</sup> |http://purl.obolibrary.org/obo/mondo.owl|BFO| [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) |https://github.com(URL_TO_INSERT_RECORD https://github.com/)/monarch-initiative/mondo/issues| 
| |Infectious Disease Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD http://www.disease-ontology.org) (IDO(URL_TO_INSERT_RECORD https://github.com/infectious-disease-ontology/infectious-disease-ontology)) |https://code.google.com/p/infectious-disease-ontology/source/browse/trunk/src/ontology/ido-core/ido-main.owl|BFO| [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) |https://code.google.com/p/infectious-disease-ontology/issues/list| |
|**Phenotype**|||||
| | Human Phenotype (HP(URL_TO_INSERT_RECORD https://hpo.jax.org/)) |http://purl.obolibrary.org/obo/hp.owl|BFO| [HP(URL_TO_INSERT_RECORD https://hpo.jax.org/)O(URL_TO_INSERT_RECORD http://plantontology.org/) Licence](https://hpo.jax.org(URL_TO_INSERT_RECORD https://hpo.jax.org/)/app/license) |https://github.com(URL_TO_INSERT_RECORD https://github.com/)/obophenotype/human-phenotype-ontology/issues/|
| |Medical Dictionary for Regulator(URL_TO_INSERT_RECORD http://www.bioinformatics.org/regulator)y Activities Terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD http://www.meddra.org/) (MedDR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)A(URL_TO_INSERT_RECORD https://www.ddbj.nig.ac.jp/dra/index-e.html)(URL_TO_INSERT_RECORD http://www.meddra.org/))| View on [Bioportal](https://bioportal.bioontology.org(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)/ontologies/MEDDRA) || Academic: Free accessible <br/> Commercial contact MSSO|https://mssotools.com/webcr/ login required|
| | Mammalian Phenotype (MP(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/mp_ontology)) | http://purl.obolibrary.org/obo/mp.owl | | [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) | https://github.com(URL_TO_INSERT_RECORD https://github.com/)/obophenotype/mammalian-phenotype-ontology/issues | 


> _<sup>*</sup>MO(URL_TO_INSERT_RECORD http://mged.sourceforge.net/ontologies/MGEDontology.php)NDO(URL_TO_INSERT_RECORD https://github.com/monarch-initiative/monarch-disease-ontology) was born of an effort to harmonise disease definitions from a number sources, includig [OMIM](https://www.omim.org(URL_TO_INSERT_RECORD http://omim.org/)(URL_TO_INSERT_RECORD https://omim.org/)/) (Online Mendelian Inheritance in Man(URL_TO_INSERT_RECORD https://omim.org/)), [Orphanet](https://www.orpha.net/), EFO(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO) and DOI(URL_TO_INSERT_RECORD https://www.doi.org)D(URL_TO_INSERT_RECORD http://www.disease-ontology.org), with work in progress to include NCIt(URL_TO_INSERT_RECORD https://ncit.nci.nih.gov). The OWL(URL_TO_INSERT_RECORD http://www.w3.org/TR/owl-overview/) version includes axiomatisation using CL(URL_TO_INSERT_RECORD https://github.com/obophenotype/cell-ontology), Uberon, GO(URL_TO_INSERT_RECORD http://www.geneontology.org), HP(URL_TO_INSERT_RECORD https://hpo.jax.org/), RO(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD https://w3id.org/ro/) & NCBITaxon. The ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) is under active development by a range of ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and domain experts. If no other limiting requirements dictate the use of an alternative ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) (e.g. use of NCIt(URL_TO_INSERT_RECORD https://ncit.nci.nih.gov)axon as part of a CDI(URL_TO_INSERT_RECORD https://www.seadatanet.org/Metadata/CDI-Common-Data-Index)SC(URL_TO_INSERT_RECORD https://www.cdisc.org/)(URL_TO_INSERT_RECORD https://www.cdisc.org/)-compliant dataset), it is therefore the most recommended open source ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) from the above list._

As with anatomy in the previous section, there is a growing body of organism-specific phenotype resources, such as C. elegans, Drosophila, Fission Yeast, Xenopus and Zebrafish. 


#### Pathology and Disease Specific Resources

There is a wide range of ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) available for specific diseases or disease types. Some examples are given below but this list is by no means exhaustive. Check ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) repositories (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository) such as [OLS](https://www.ebi.ac.uk/ols/ontologies), [Bioportal](https://bioportal.bioontology.org(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)/ontologies) or the [OBO(URL_TO_INSERT_RECORD http://www.obofoundry.org/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059) Foundry(URL_TO_INSERT_RECORD http://www.obofoundry.org/)](http://obofoundry.org/) for up-to-date lists of available ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)

|Scope|Name|File location|Top-Level Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)|Licence|Issue Tracker URI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)|
|--- |--- |--- |--- |--- |--- |
|**Malaria**|Malaria Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) (IDO(URL_TO_INSERT_RECORD https://github.com/infectious-disease-ontology/infectious-disease-ontology)MA(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/gxd/ma_ontology/)(URL_TO_INSERT_RECORD http://omabrowser.org/oma/about/)L(URL_TO_INSERT_RECORD https://www.vectorbase.org/ontology-browser))||BFO(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO)| [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)  ||
|**Alzheimer Disease**| Alzheimer's Disease Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD http://www.disease-ontology.org)(URL_TO_INSERT_RECORD https://bioportal.bioontology.org/ontologies/ADO) (ADO(URL_TO_INSERT_RECORD https://bioportal.bioontology.org/ontologies/ADO)) |https://www.scai.fraunhofer.de/content/dam/scai/de/downloads/bioinformatik/ontologies/ADO/ADO.zip|BFO|||
|**Rare disorder**| Orphanet(URL_TO_INSERT_RECORD http://www.orpha.net/consor/cgi-bin/index.php?lng=EN)(URL_TO_INSERT_RECORD http://www.orpha.net/consor/cgi-bin/index.php?lng=EN) Rare Disease Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD http://www.disease-ontology.org) (ORDO(URL_TO_INSERT_RECORD https://ordo.open.ac.uk/)(URL_TO_INSERT_RECORD http://www.orphadata.org/cgi-bin/inc/ordo_orphanet.inc.php)) | View on [Bioportal](https://bioportal.bioontology.org(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)/ontologies/ORDO)||[CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)||



#### Cellular entities

Following on through our review of semantic resources by granularity levels, this section details a number of reference resources which provide coverage for the describing `cell types`, `cell lines` {footcite}`pmid29805321` and `cellular phenotypes`.

|Scope|Name|File location|Top-Level Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)|Licence|Issue Tracker URI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)|
|--- |--- |--- |--- |--- |--- |
|**Cell**| Cell Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD https://github.com/obophenotype/cell-ontology) (CL(URL_TO_INSERT_RECORD https://github.com/obophenotype/cell-ontology)) |http://purl.obolibrary.org/obo/cl.owl http://purl.obolibrary.org/obo/cl.obo|BFO| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/)|https://code.google.com/p/cell-ontology/issues/list|
|**Cell Lines**| 
| | Cellosaurus|ftp://ftp.expasy.org/databases/cellosaurus/cellosaurus.obo ftp://ftp.expasy.org/databases/cellosaurus|| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/)||
| | Cell Line Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD http://www.clo-ontology.org/) (CL(URL_TO_INSERT_RECORD https://github.com/obophenotype/cell-ontology)O(URL_TO_INSERT_RECORD http://www.clo-ontology.org/)) |[https://github.com(URL_TO_INSERT_RECORD https://github.com/)/CLO-ontology/CLO/blob/master/src/ontology/clo.owl](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/CLO-ontology/CLO/blob/master/src/ontology/clo.owl)|BFO| [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) |https://github.com(URL_TO_INSERT_RECORD https://github.com/)/CLO-ontology/CLO/issues|
|**Cell Molecular Phenotype**|Cell Molecular Phenotype Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) (CMP(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/mp_ontology)O(URL_TO_INSERT_RECORD http://www.ebi.ac.uk/cmpo/)(URL_TO_INSERT_RECORD http://plantontology.org/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/MPO)) |https://github.com(URL_TO_INSERT_RECORD https://github.com/)/EBISPOT/CMPO/releases/| | | https://github.com(URL_TO_INSERT_RECORD https://github.com/)/EBISPOT/CMPO/issues |




#### Molecular Entities

This section highlights the major and most widely used OBO(URL_TO_INSERT_RECORD http://www.obofoundry.org/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059) Foundry(URL_TO_INSERT_RECORD http://www.obofoundry.org/) resources for `molecules of biological relevance` as well as `molecular structures`, `biological processes` and `cellular components` 


|Scope|Name|File location|Top-Level Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)|Licence|Issue Tracker URI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)|
|--- |--- |--- |--- |--- |--- |
|**Chemicals and Small Molecules**| Chemical Entities of Biological Interest(URL_TO_INSERT_RECORD http://www.ebi.ac.uk/chebi/) (ChEBI)|[ChEBI](https://www.ebi.ac.uk/chebi(URL_TO_INSERT_RECORD http://www.ebi.ac.uk/chebi/)/)| BFO(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO)|[CC-by 4.0](https://creativecommons.org/licenses/by/4.0/) |https://github.com(URL_TO_INSERT_RECORD https://github.com/)/ebi-chebi/ChEBI/issues|
|**Gene Function, Molecular Component, Biological Process**| Gene Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD http://www.geneontology.org) (GO(URL_TO_INSERT_RECORD http://www.geneontology.org)) |http://purl.obolibrary.org/obo/go.obo http://purl.obolibrary.org/obo/go.owl|BFO| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/) |http://sourceforge.net(URL_TO_INSERT_RECORD https://sourceforge.net/)/p/geneontology/ontology-requests/|
|**Protein(URL_TO_INSERT_RECORD http://www.ncbi.nlm.nih.gov/protein)/peptide**| Protein(URL_TO_INSERT_RECORD http://www.ncbi.nlm.nih.gov/protein) Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD https://proconsortium.org/) (PRO(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD http://www.sparontologies.net/ontologies/pro)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD https://proconsortium.org/)(URL_TO_INSERT_RECORD https://w3id.org/ro/)) |https://proconsortium.org(URL_TO_INSERT_RECORD https://proconsortium.org/) |BFO(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO)| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/) |https://github.com(URL_TO_INSERT_RECORD https://github.com/)/PROconsortium/PRoteinOntology/issues|


Besides, these open ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), in the context of clinically relevant work where drug formulation require recording and description, the following resources are relevant.

|Scope|Name|File location|Top-Level Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)|Licence|Issue Tracker URI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)|
|--- |--- |--- |--- |--- |--- |
| **Drug** |
| | National Drug File(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/NDFRT)| View on [Bioportal](https://bioportal.bioontology.org(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)/ontologies/NDFRT(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/NDFRT)) ||[NIH(URL_TO_INSERT_RECORD http://sweetgum.nybg.org/science/ih/) license](https://uts.nlm.nih.gov/license.html)||
| | The Drug Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD https://ontology.atlassian.net/wiki/display/DRON/Drug+Ontology+Home) (DR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)O(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD https://w3id.org/ro/)N) |  http://purl.obolibrary.org/obo/dron.owl | BFO(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO) | [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) | https://ontology.atlassian.net/browse/DRON |
| | RxNORM(URL_TO_INSERT_RECORD https://www.nlm.nih.gov/research/umls/rxnorm/)(URL_TO_INSERT_RECORD https://www.nlm.nih.gov/research/umls/rxnorm/) |View on [Bioportal](https://bioportal.bioontology.org(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)/ontologies/RXNORM) | |[RxNORM(URL_TO_INSERT_RECORD https://www.nlm.nih.gov/research/umls/rxnorm/)(URL_TO_INSERT_RECORD https://www.nlm.nih.gov/research/umls/rxnorm/) license](http://www.nlm.nih.gov/databases/umls.html) - part of the UMLS license||


#### Assays and Technologies

The resources listed in this section are providing key descriptors bridging data acquisition procedures (as used in a clinical setting and wet lab work) with instruments, units of measurements, endpoints as well as sometimes the biological process or molecular entities of biological significance.
Some of the resources are specialized semantic artefacts developed(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) to support the standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)ized reporting of data modalities.

|Scope|Name|File location|Top-Level Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)|Licence|Issue Tracker URI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)|
|--- |--- |--- |--- |--- |--- |
|**Radiology**| Radiology Lexicon(URL_TO_INSERT_RECORD https://www.rsna.org/en/practice-tools/data-tools-and-standards/radlex-radiology-lexicon) (RADL(URL_TO_INSERT_RECORD https://doi.org/10.5523/bris.1234ym4ulx3r11i2z5b13g93n7)ex) | View on [Bioportal](https://bioportal.bioontology.org(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)/ontologies/RADLEX) ||||
|**Medical Imaging**|DICO(URL_TO_INSERT_RECORD https://github.com/ICO-ontology/ICO)(URL_TO_INSERT_RECORD http://www.cropontology.org/)(URL_TO_INSERT_RECORD https://codeocean.com)M(URL_TO_INSERT_RECORD http://medical.nema.org/)|http://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_D.html(URL_TO_INSERT_RECORD http://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_D.html)||||
|**Sample Processing/Reagents/Instruments Assay Definition**| Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) for Biomedical Investigations(URL_TO_INSERT_RECORD http://obi-ontology.org/) (OBI(URL_TO_INSERT_RECORD http://obi-ontology.org/)) |http://purl.obolibrary.org/obo/obi.owl|BFO| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/)|https://github.com(URL_TO_INSERT_RECORD https://github.com/)/obi-ontology/obi/issues|
|**Biological screening assays and their results including high-throughput screening (HTS)**| BioAssay Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD http://bioassayontology.org) (BAO(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/AO)(URL_TO_INSERT_RECORD http://bioassayontology.org)) |http://www.bioassayontology.org(URL_TO_INSERT_RECORD http://www.bioassayontology.org/)(URL_TO_INSERT_RECORD http://bioassayontology.org)/bao/bao_complete_bfo_dev.owl|BFO| [CC-by-SA 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) ||
|**Mass Spectrometry (instrument/acquisition parameter/spectrum related informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion)**| HUPO(URL_TO_INSERT_RECORD http://plantontology.org/) Proteomics Standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s Initiative(URL_TO_INSERT_RECORD http://www.psidev.info/)-Mass Spectrometry controlled vocabulary (PSI-MS) |https://github.com(URL_TO_INSERT_RECORD https://github.com/)/HUPO-PSI/psi-ms-CV |none specified| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/)|https://github.com(URL_TO_INSERT_RECORD https://github.com/)/HUPO-PSI/psi-ms-CV/issues |
|**NMR Spectroscopy (instrument/acquisition parameter/spectrum related informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion)**| Nuclear Magnetic Resonance Controlled Vocabulary(URL_TO_INSERT_RECORD http://nmrml.org/cv/) (NMR-CV) |http://nmrml.org(URL_TO_INSERT_RECORD http://nmrml.org)/cv(URL_TO_INSERT_RECORD http://nmrml.org/cv/)/v1.0.rc1/nmrCV.owl|BFO| [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) |https://github.com(URL_TO_INSERT_RECORD https://github.com/)/nmrML/nmrML/issues?state=open|
|**Laboratory test**| Logical Observation Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) Names and Codes(URL_TO_INSERT_RECORD https://loinc.org/) (LOINC(URL_TO_INSERT_RECORD https://loinc.org/)) | LOINC(URL_TO_INSERT_RECORD https://loinc.org/) and RELM(URL_TO_INSERT_RECORD http://elm.eu.org)A(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/gxd/ma_ontology/) Complete Download File https://loinc.org(URL_TO_INSERT_RECORD https://loinc.org/)/downloads/ |none specified| [RELM(URL_TO_INSERT_RECORD http://elm.eu.org)A(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/gxd/ma_ontology/) license](https://uts.nlm.nih.gov/license.html) ||
|**Units** | Units Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD https://github.com/bio-ontology-research-group/unit-ontology) (UO(URL_TO_INSERT_RECORD https://github.com/bio-ontology-research-group/unit-ontology)) | http://purl.obolibrary.org/obo/uo.owl | | [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) | https://github.com(URL_TO_INSERT_RECORD https://github.com/)/bio-ontology-research-group/unit-ontology(URL_TO_INSERT_RECORD https://github.com/bio-ontology-research-group/unit-ontology)/issues |

Some multi-domain ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) such as the NCI Thesaurus(URL_TO_INSERT_RECORD https://ncit.nci.nih.gov)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3034) (NCIt(URL_TO_INSERT_RECORD https://ncit.nci.nih.gov)) and the Experimental Factor Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/) (EFO(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO)) also cover aspects of the above domains such as assays and sample collection (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=collection) and processing. Depending on the overall context of a resource selection process, it can make more sense to use a multi-domain ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) with suitable coverage to improve consistency and interoperability within a resource or dataset.


Finally, a resource exists that describes statistical measures, statistical tests or methods as well as statistically relevant graphical representations. It may be used for reporting results and annotating experimental results(URL_TO_INSERT_RECORD https://www.cambridge.org/core/journals/experimental-results).



|Scope|Name|File location|Top-Level Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)|Licence|Issue Tracker URI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)|
|--- |--- |--- |--- |--- |--- |
| **Experimental Design, Statistical Methods and Statistical Measures**| Statistical Methods Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) (STATO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)(URL_TO_INSERT_RECORD http://purl.bioontology.org/ontology/ATO)(URL_TO_INSERT_RECORD http://stato-ontology.org/)) |[http://stato-ontology.org(URL_TO_INSERT_RECORD http://stato-ontology.org/)](http://stato-ontology.org(URL_TO_INSERT_RECORD http://stato-ontology.org/))|BFO| [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/)|https://github.com(URL_TO_INSERT_RECORD https://github.com/)/ISA-tools/stato/issues?state=open|




### Relations

Also known as `OWL(URL_TO_INSERT_RECORD http://www.w3.org/TR/owl-overview/) Properties`, their importance may be overlooked by `data scientists` who are not `knowledge engineers` or `ontologists`. These are essential components as, when correctly crafted with a proper understanding of the logical constraints available to semantic languages such as OWL(URL_TO_INSERT_RECORD http://www.w3.org/TR/owl-overview/), are exploited by tools known as `reasoners` to carry the following key tasks:

* `Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) logical consistency` checks
* `Automatic classification` and `inference` tasks
* `Entailments`, i.e. detection of logical consequences resulting from axiomatic definitions (closely related to the point above)

This is particularly important when processing billions of facts expressed as RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) statements. 

One also needs to understand the current limitations in expressivity afforded by the current semantic web languages and the associated axiomatics as well as computational constraints associated with inference. For more *in-depth* review of such topics, the reader is invited to consults the following work {footcite}`pmid15892874` <!--[by Smith et al](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2005-6-5-r46)-->.

In the field of Biology and Biomedicine, the [OBO(URL_TO_INSERT_RECORD http://www.obofoundry.org/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059) Foundry(URL_TO_INSERT_RECORD http://www.obofoundry.org/)](http://obofoundry.org) coordinates the development of interoperable ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact). At the core(URL_TO_INSERT_RECORD http://purl.uniprot.org/core/)(URL_TO_INSERT_RECORD https://core.ac.uk) of this interoperation lies the **[Relation Ontology](http://www.obofoundry.org(URL_TO_INSERT_RECORD http://www.obofoundry.org/)/ontology/ro.html)** released under the [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) license.

| Relation Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)               | File  | Variant                                                                        |
|---------------------------------|---|--------------------------------------------------------------------------------|
| Relation Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)               | [ro.owl](http://purl.obolibrary.org/obo/ro.owl)  | Canonical edition                                                              |
| Relation Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) in obo format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) | [ro.obo](http://purl.obolibrary.org/obo/ro.obo)  | Has imports merged in                                                          |
| RO(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD https://w3id.org/ro/) Core(URL_TO_INSERT_RECORD https://core.ac.uk) relations               | [ro/core.owl](http://purl.obolibrary.org/obo/ro/core.owl)  | Minimal subset intended to work with BFO(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO)-classes [page](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/oborel/obo-relations(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)/wiki/ROCore)                        |
| RO(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD https://w3id.org/ro/) base ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)                | [ro/ro-base.owl](http://purl.obolibrary.org/obo/ro/ro-base.owl)  | Axioms defined within RO(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD https://w3id.org/ro/) and to be used in imports for other ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) [page](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/INCATools/ontology-development-kit/issues/50) |
| Interaction relations           | [ro/subsets/ro-interaction.owl](http://purl.obolibrary.org/obo/ro/subsets/ro-interaction.owl)  |                                                                                |
| Ecology subset                  | [ro/subsets/ro-eco.owl](http://purl.obolibrary.org/obo/ro/subsets/ro-eco.owl)  | For use in ecology and environmental science                                   |
| Neuroscience subset             | [ro/subsets/ro-neuro.owl](http://purl.obolibrary.org/obo/ro/subsets/ro-neuro.owl)  | For use in neuroscience [page](http://bioinformatics.oxfordjournals.org/content/28/9/1262.long) 

As `knowledge graphs` and `property graphs` gain importance, we can expect the range and depth of relations to mature and expand as more expressivity is needed and progress is made by reasoner technology to fully exploit their benefits.
This would also have to be placed in the context of advances in `Text Mining` and `Machine Learning`, where unsupervised methods start to demonstrate strong potential to detect relations between entities.

The following is an example of how a `defined class` may be created in an ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact). The code snippet shows one such class being expressed to create a type by specifying a number of `axioms`. These use `relations` (aka OWL(URL_TO_INSERT_RECORD http://www.w3.org/TR/owl-overview/) Properties), which may be set to 

```bash
'B cell, CD19-positive'
equivalentClass :
    'lymphocyte of B lineage, CD19-positive' 
    and ( 'has plasma membrane part' some 'CD19 molecule') 
    and ( 'in taxon' some Mammalia) 
    and ( 'capable of' some 'B cell mediated immunity')
```

Any class satisfying these patterns may be classified by an OWL(URL_TO_INSERT_RECORD http://www.w3.org/TR/owl-overview/) reasoner as a child of that class. So the following class, with such properties that they all satisfy the requirements of the `defined class` declared above (e.g. "Homo sapiens" is_a type of "Mammalia", etc...), will be classified automatically (i.e. without human intervention) by a reasoner such as ELK or Hermit as a child of 'B cell, CD19-positive' .

```bash
'human B cell, CD19-positive'
Class:
    ( 'has plasma membrane part' some 'B-lymphocyte antigen CD19 isoform h2')
    and ( 'in taxon' some 'Homo sapiens') 
    and ( 'capable of' some 'B cell tolerance induction in mucosal-associated lymphoid tissue')

```

The notion is important to grasp as it also explains why not all ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) are compatible, because they may significantly differ in the underlying axioms they rely on to establish their hierarch(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ies using reasoners.



## Conclusions

> Selecting semantic resources depends on many different factors. However, the most important factor remains the `context` of the data and associated landscape of data standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s as well as the ultimate integration goal, which will dictate the final choice.
> 
>The selection process remains guided by the need to maximize the potential of data integration with datasets of similar nature and similar value. It also requires a good understanding of the technical and sometimes legal implications these choices will have.

<!-- 
TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO : fill in the links to what-should-I-read-next recipes -->

### What to read next?

* How to build an application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)? {ref}`fcb-interop-ontorobot`
* How to select on ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) service? {ref}`fcb-select-onto-service`
* How to deploy an ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) server? {ref}`fcb-select-onto-service-criteria`
* [How to establish a minimal metadata profile?] {ref}`fcb-interop-covid-metadata` 

````{rdmkit_panel}
````


<!-- {download}`bibliography-identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)-map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping.bib <./bibref/bibliography-identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)-map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping.bib>` -->

## References
````{dropdown} **References**
```{footbibliography}
```
````

<!-- Smith, B., Ceusters, W., Klagges, B. et al. Relations in biomedical ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact). Genome Biol 6, R46 (2005). https://doi.org/10.1186/gb-2005-6-5-r46

Rocca-Serra P, Bratfalean D, Richard F, Marshall C, Romacker M., Auffray C, ., … on the behalf of the eTRIKS(URL_TO_INSERT_RECORD https://www.etriks.org/standards-starter-pack/) consortium, . (2016, April 25). eTRIKS(URL_TO_INSERT_RECORD https://www.etriks.org/standards-starter-pack/) Standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s Starter Pack(URL_TO_INSERT_RECORD https://www.etriks.org/standards-starter-pack/) Release 1.1 April 2016. Zenodo(URL_TO_INSERT_RECORD https://www.zenodo.org)(URL_TO_INSERT_RECORD https://www.zenodo.org). http://doi.org/10.5281/zenodo.50825

Malone J, Stevens R, Jupp S, Hancocks T, Parkinson H, Brooksbank C. Ten Simple Rules for Selecting a Bio-ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact). PLoS Comput Biol. 2016;12(2):e1004743. Published 2016 Feb 11. http://doi.org/10.1371/journal.pcbi.1004743

Bairoch A. The Cellosaurus(URL_TO_INSERT_RECORD https://www.cellosaurus.org)(URL_TO_INSERT_RECORD https://www.cellosaurus.org), a cell line knowledge resource. J. Biomol. Tech. (2018) 29:25-38. http://doi.org/10.7171/jbt.18-2902-002.

Sansone, S.-A., McQuilton, P., Rocca-Serra, P., Gonzalez-Beltran, A., Izzo, M., Lister, A.L. and Thurston, M. (2019) FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)sharing(URL_TO_INSERT_RECORD https://www.FAIRsharing.org)(URL_TO_INSERT_RECORD https://www.FAIRsharing.org) as a community approach to standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s, repositories (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository) and policies (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Policy). Nature biotechnology, 37, 358: http://doi.org/10.1038/s41587-019-0080-8.

Hripcsak, G., Ryan, P. B., Duke, J. D., Shah, N. H., Park, R. W., Huser, V., Suchard, M. A., Schuemie, M. J., DeFalco, F. J., Perotte, A., Banda, J. M., Reich, C. G., Schilling, L. M., Matheny, M. E., Meeker, D., Pratt, N., & Madigan, D. (2016). Characterizing treatment pathways at scale using the OHD(URL_TO_INSERT_RECORD https://purl.obolibrary.org/obo/ohd/home)SI network. Proceedings of the National Academy of Sciences of the Unite(URL_TO_INSERT_RECORD https://unite.ut.ee/index.php)d States of America, 113(27), 7329-7336. https://doi.org/10.1073/pnas.1510502113

Hripcsak, George et al. “Observational Health Data Sciences and Informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ics (OHD(URL_TO_INSERT_RECORD https://purl.obolibrary.org/obo/ohd/home)SI): Opportunities for Observational Research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ers.” Studies in health technology and informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ics vol. 216 (2015): 574-8.
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
