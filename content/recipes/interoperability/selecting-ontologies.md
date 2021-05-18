(fcb-interop-selectonto)=
# Selecting terminologies and ontologies

+++
<br/>

````{panels_fairplus}
:identifier_text: FCB020
:identifier_link: 'https://w3id.org/faircookbook/FCB020'
:difficulty_level: 1
:recipe_type: guidance
:reading_time_minutes: 15
:intended_audience: principal_investigator, data_manager, terminology_manager, data_scientist, ontologist  
:has_executable_code: nope
:recipe_name: Selecting terminologies and ontologies
```` 


## Main Objectives

The main purpose of this recipe is to provide guidance on how to select the most suitable semantic artefacts given a specific research context in general, and when it comes to life and biomedical sciences projects, their main themes, i.e. *risk assessment*, *clinical trial*, *drug discovery* or *fundamental research*.


## Graphical Overview

<!-- [![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgSTEoZmE6ZmEtdW5pdmVyc2l0eSB3aGF0IGlzIHRoZSBjb250ZXh0Pyk6Ojpib3ggLS0-fGZyYW1ld29ya3wgTTEoZmE6ZmEtY3ViZSBjbGluaWNhbCB0cmlhbCBjb250ZXh0KTo6OmJveFxuICBJMShmYTpmYS11bml2ZXJzaXR5IHdoYXQgaXMgdGhlIGNvbnRleHQ_KSAtLT58ZnJhbWV3b3JrfCBNMihmYTpmYS1jdWJlIG9ic2VydmF0aW9uYWwgcGF0aWVudCBvdXRjb21lKTo6OmJveFxuICBJMShmYTpmYS11bml2ZXJzaXR5IHdoYXQgaXMgdGhlIGNvbnRleHQ_KSAtLT58ZnJhbWV3b3JrfCBNMyhmYTpmYS1jdWJlIGJhc2ljIHJlc2VhcmNoKTo6OmJveFxuXG4gIE0xIC0tPiB8Y29uc2lkZXJ8IFIxKGZhOmZhLWN1YmVzIENESVNDIFZvY2FidWxhcnkpOjo6Ym94XG4gIE0yIC0tPiB8Y29uc2lkZXJ8IFIyKGZhOmZhLWN1YmVzIE9IRFNJIEF0aGVuYSB0ZXJtaW5vbG9naWVzKTo6OmJveFxuICBNMyAtLT4gfGNvbnNpZGVyfCBSMyhmYTpmYS1jdWJlcyBPQk8gRm91bmRyeSByZXNvdXJjZXMpOjo6Ym94XG4gIFxuICBJMntmYTpmYS11bml2ZXJzaXR5IGlzIHB1YmxpYzxicj4gYXJjaGl2ZTxicj4gZGVwb3NpdGlvbiA8YnI-cmVxdWlyZWQ_IH06Ojpib3ggLS0-fE5vIHxSMzo6OmJveFxuICBJMntmYTpmYS11bml2ZXJzaXR5IGlzIHB1YmxpYzxicj4gYXJjaGl2ZTxicj4gZGVwb3NpdGlvbiA8YnI-cmVxdWlyZWQ_IH0gLS0-fFllc3xNNChjb25zdWx0IEZBSVJzaGFyaW5nKTo6OmJveFxuXG4gIE00IC0tPiB8RUJJIHJlc291cmNlc3xNNShFRk8pOjo6Ym94XG5cbiAgbGlua1N0eWxlIDAsMSwyLDMsNCw1LDYsNyw4IHN0cm9rZTojMmE5ZmM5LHN0cm9rZS13aWR0aDoxcHgsY29sb3I6IzJhOWZjOSxmb250LWZhbWlseTphdmVuaXI7XG4gIGNsYXNzRGVmIGJveCBmb250LWZhbWlseTphdmVuaXIsZm9udC1zaXplOjE0cHgsZmlsbDojMmE5ZmM5LHN0cm9rZTojMjIyLGNvbG9yOiNmZmYsc3Ryb2tlLXdpZHRoOjFweFxuXHRcdCIsIm1lcm1haWQiOnsidGhlbWUiOiJuZXV0cmFsIn0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiAgSTEoZmE6ZmEtdW5pdmVyc2l0eSB3aGF0IGlzIHRoZSBjb250ZXh0Pyk6Ojpib3ggLS0-fGZyYW1ld29ya3wgTTEoZmE6ZmEtY3ViZSBjbGluaWNhbCB0cmlhbCBjb250ZXh0KTo6OmJveFxuICBJMShmYTpmYS11bml2ZXJzaXR5IHdoYXQgaXMgdGhlIGNvbnRleHQ_KSAtLT58ZnJhbWV3b3JrfCBNMihmYTpmYS1jdWJlIG9ic2VydmF0aW9uYWwgcGF0aWVudCBvdXRjb21lKTo6OmJveFxuICBJMShmYTpmYS11bml2ZXJzaXR5IHdoYXQgaXMgdGhlIGNvbnRleHQ_KSAtLT58ZnJhbWV3b3JrfCBNMyhmYTpmYS1jdWJlIGJhc2ljIHJlc2VhcmNoKTo6OmJveFxuXG4gIE0xIC0tPiB8Y29uc2lkZXJ8IFIxKGZhOmZhLWN1YmVzIENESVNDIFZvY2FidWxhcnkpOjo6Ym94XG4gIE0yIC0tPiB8Y29uc2lkZXJ8IFIyKGZhOmZhLWN1YmVzIE9IRFNJIEF0aGVuYSB0ZXJtaW5vbG9naWVzKTo6OmJveFxuICBNMyAtLT4gfGNvbnNpZGVyfCBSMyhmYTpmYS1jdWJlcyBPQk8gRm91bmRyeSByZXNvdXJjZXMpOjo6Ym94XG4gIFxuICBJMntmYTpmYS11bml2ZXJzaXR5IGlzIHB1YmxpYzxicj4gYXJjaGl2ZTxicj4gZGVwb3NpdGlvbiA8YnI-cmVxdWlyZWQ_IH06Ojpib3ggLS0-fE5vIHxSMzo6OmJveFxuICBJMntmYTpmYS11bml2ZXJzaXR5IGlzIHB1YmxpYzxicj4gYXJjaGl2ZTxicj4gZGVwb3NpdGlvbiA8YnI-cmVxdWlyZWQ_IH0gLS0-fFllc3xNNChjb25zdWx0IEZBSVJzaGFyaW5nKTo6OmJveFxuXG4gIE00IC0tPiB8RUJJIHJlc291cmNlc3xNNShFRk8pOjo6Ym94XG5cbiAgbGlua1N0eWxlIDAsMSwyLDMsNCw1LDYsNyw4IHN0cm9rZTojMmE5ZmM5LHN0cm9rZS13aWR0aDoxcHgsY29sb3I6IzJhOWZjOSxmb250LWZhbWlseTphdmVuaXI7XG4gIGNsYXNzRGVmIGJveCBmb250LWZhbWlseTphdmVuaXIsZm9udC1zaXplOjE0cHgsZmlsbDojMmE5ZmM5LHN0cm9rZTojMjIyLGNvbG9yOiNmZmYsc3Ryb2tlLXdpZHRoOjFweFxuXHRcdCIsIm1lcm1haWQiOnsidGhlbWUiOiJuZXV0cmFsIn0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9) -->



```{figure} select-onto.png
---
width: 800px
name: Which ontology should be used?
alt:  Which ontology should be used?
---
 Which ontology should be used?.
```


___

## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Interoperability | minimal | repeatable |


----

## Context is everything

The domain of operation will generally dictate the semantic framework that is most suited to a given dataset. This is simply due to the fact that the advances in data standardization in specific fields are such that it is a sound decision to adopt a complete stack of standards, both syntactic and semantic.

Here, we present the three most common scenarios in biomedical research, based on experience garnered during IMI eTRIKS {cite}`philippe_rocca_serra_2016_50825` :

### Clinical Trial Data

Operating in the field of Clinical Trials means that datasets are generated during `interventional studies`, meaning that researchers influence and control the predictor variables, which are usually different intensity levels of therapeutic agents, in order to gain insights in terms of benefits in patient outcomes.
In this context, regulatory requirements make it so that data must be recorded in standard forms to allow for review and appraisal by regulators such as FDA reviewers in the US. The [CDISC standards](https://www.cdisc.org/standards) are the *`de-facto standard`* in this area, which mandates the use of semantics resources such as:

| Semantic Resource | Domain  | Service |
| -- | -- | -- | 
| CDISC vocabulary|clinical trial data| EVS |
| NCI Thesaurus|biomedicine|EVS,Bioportal,OLS|
| SNOMED-CT|pathology|EVS,Bioportal(§)|
| UMLS|pathology|EVS,Bioportal(§)|
| LOINC|laboratory tests|Loinc|
| RxNORM|drugs|Bioportal|
| GUDID|instruments|FDA|

All available from the [NCBI EVS system](https://evs.nci.nih.gov/), [LOINC](https://loinc.org/), [OLS](https://www.ebi.ac.uk/ols/index) or [Bioportal](https://bioportal.bioontology.org/).
 

```{warning}
Some resources are only available under restrictive licences, which prevent derivative work, which may limit access and use. Furthermore, some licenses are expensive.  
```

### Observational Health Data

This context refers to data collected during `observational studies`, which in contrast to `interventional studies`, draw inferences from a sample to a population where the independent variable is not under the control of the researcher because of ethical concerns or logistical constraints [1]. This is typically the case in epidemiological work or exposure follow-up studies in the context of risk assessment and evaluation of clinical outcomes. `Observational health data` can also include `electronic health records (EHR)` or ` administrative insurance claims` and allow research around acquiring *`real world evidence`* from large corpora of data.
In this specific context, one model and associated set of standards has been particularly successful. With several hundred millions of patients' information structured using the **Observational Medical Outcomes Partnership (OMOP)**, the Observational Health Data Sciences and Informatics (ODHSI) `open-science community` has laid the foundation for a widely adopted data model. Therefore, building a FAIRification process around the standard stack produced by the ODHSI community needs to be considered if operating in such a `data context`.


|Semantic Resource|Domain |Service|
|--- |---  |--- |
|CDISC vocabulary|clinical trial data|EVS|
|NCI Thesaurus|biomedicine|EVS,Bioportal,OLS|
|SNOMED-CT|pathology|EVS,Bioportal(§)|
|UMLS|pathology|EVS,Bioportal(§)|
|LOINC|laboratory tests| LOINC |
|RxNORM|drugs|Bioportal|


For a more detailed overview and deep-dive into the ODHSI and OMOP semantic support, we recommend the reading of the chapter dedicated to the `controlled terminology` [in the **`Book of OHDSI`**](https://ohdsi.github.io/TheBookOfOhdsi/StandardizedVocabularies.html) {cite}`pmid27274072`


### Basic research context

This refers to datasets and research output being generated using model organisms and cellular systems in the context of basic, fundamental research. In this arena, the regulatory pressure is much less present but this does not rule out data management best practices and proper archival requirements.
As a consequence of fewer constraints, researchers are often confronted with a sea of options. This and the next sections aim to provide some guidance when tasked with deciding on which semantic resource to use.

<!-- Dead link -->
```{admonition} Tip
:class: tip
 **An important consideration** 
to bear in mind when selecting semantic resources is to assess whether or not `data archival in public repositories will be required`. For instance, submitting to NCBI Gene Expression Omnibus Data archive places no particular constraints on data annotations but if depositing to EMBL-EBI ArrayExpress, then selecting a resource such as the [Experimental Factor Ontology](https://efo.owl) for annotating data could ease deposition.
```

```{admonition} Tip
:class: tip
 **[The FAIRsharing registry](https://fairsharing.org)** {cite}`pmid30940948` is an ELIXIR resource which provides invaluable content as the catalogue offers an overview of the various semantics artefacts used by public data repositories.
````

## Selecting Terminologies 


### Use Cases and General Recommendations

1. The use and implementation of common terminologies enables the normalisation and harmonisation of both variable labels and allowed values for each field. Implementing the use of common terminologies in the data collection or curation workflow will ensure consistency of the annotation across all data. This is particularly important if data is generated at multiple partner sites and/or by multiple individuals. 

1. If data fields are annotated with terms from freely chosen ontologies (rather than those dictated by a common model such as CDSIC), care should be taken to avoid picking terms from ontologies at random. If a set of concepts are all available in one ontology, this ontology should be preferred over a set of ontologies. Mapping services such as [Oxo](https://www.ebi.ac.uk/spot/oxo/) are available to verify whether a term of interest in one ontology has an equivalent term in another ontology.

1. Restrictions of allowed values for a given field should ideally be limited to a single ontology and better yet, to a single branch of a chosen ontology. This will vastly improve the semantic queryability as well as the consistency and interoperability of the data. 

1. Many ontologies and vocabularies reuse concepts from other ontologies, in line with best practice in ontology design, to limit duplication of efforts and proliferation of parallel synonymous concepts. Care should however be taken to use concepts in the most appropriate environment. This is usually their original source unless they are used as part of a larger set of terms. As an example, the Experimental Factor Ontology (EFO) reuses concepts from a range of ontologies, including species from the NCBI taxonomy, assays from OBI, and diseases and phenotypes from MONDO and HPO. If annotating a dataset or resource which covers all of these concepts, it therefore makes sense to use EFO as the primary annotation source. However, if only annotations for species are required, the NCBI taxonomy should be used directly to ensure completeness, since not all species in NCBItaxon will have been imported into EFO.



### Selection Criteria

A set of widely accepted criteria for selecting terminologies (or other reporting standards) does not exist. There are however a number of excellent publications such as ["A sea of standards for omics data: sink or swim?"](https://doi.org/10.1136/amiajnl-2013-002066) {cite}`pmid24076747` and ["Ten Simple Rules for Selection a Bio-ontology"](https://doi.org/10.1371/journal.pcbi.1004743) } {cite}`pmid26867217` providing some guidance on the subject. Below are a set of suggested criteria for evaluating the suitability of a terminology resource.


*   **Exclusion criteria**:
    * 🔸 absent licence or terms of use (_indicator of usability_)
    * 🔸 restrictive licences or terms of use with restrictions on redistribution and reuse 
    * 🔸 absence of term definitions 
    * 🔸 absence of sufficient class metadata (_indicator of quality_)
    * 🔸 absence of sustainability indicators (_absence of funding records_) 
 
*   **Inclusion criteria**:
    * 🔰  scope and coverage meets the requirements of the concept identified
    * 🔰  unique URI, textual definition and IDs for each term
    * 🔰  resource releases are versioned
    * 🔰  size of resource (_indicator of coverage_)
    * 🔰  number of classes and subclasses (_indicator of depth_)
    * 🔰  number of terms having definitions and synonyms (_indicator of richness_)
    * 🔰  presence of a help desk and contact point (_indicator of community support_)
    * 🔰  presence of term submission tracker / issue tracker (_indicator of resource agility and capability to grow upon request_)
    * 🔰  potential integrative nature of the resource (_as indicator of translational application potential_)
    * 🔰  licensing information available (_as indicator of freedom to use_)
    * 🔰  use of a top level ontology (_as indicator of a resource built for generic use_)
    * 🔰  pragmatism (_as indicator of actual, current real life practice)_
    * 🔰  possibility of collaborating: the resource accepts complaints/remarks that aim to fix or improve the terminology, while the resource organisation commits to fix or improve the terminology in brief delays (one month after receipt?)


### Set of Core Terminologies 

The terminologies presented here have been organized by theme and scope. When possible, sections are organized by `granularity levels`, progressing from `macroscopic scale` (organism) to `microscopic scale` (tissue, cells) and `molecular scale` (macromolecules, proteins, small molecules, xenobiotic chemicals).
Domains also cover `processes` or `actions` and their `participants` or `agents` but also can be organized from `general/generic` (disease) to `specialized/specific` (infectious disease).


### Organism, Organism Parts and Developmental Stages

The resources listed here focus on providing structured vocabularies to describe `taxonomic` and `anatomical` information. The table below also shows 

|Scope|Name|File location|Top-Level Ontology|Licence|Issue Tracker URI|Comment|
|--- |--- |--- |--- |--- |--- |--- |
|**Organism**|NCBITaxonomy|http://purl.obolibrary.org/obo/ncbitaxon.owl|none specified|This ontology is made available via the UMLS. Users of all UMLS ontologies must abide by the terms of the [UMLS license](https://uts.nlm.nih.gov/license.html)|||
|**Vertebrate Anatomy**|UBERON|http://purl.obolibrary.org/obo/uberon/ext.owl http://purl.obolibrary.org/obo/uberon/ext.obo|BFO| [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) |https://github.com/obophenotype/uberon/issues|Integrative Resource engineered to go across species|
|**Human Anatomy**|FMA| http://purl.obolibrary.org/obo/fma.owl | | [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) |https://sourceforge.net/p/obo/foundational-model-of-anatomy-fma-requests/| Excellent cross-referencing with Uberon|
| **Human Developmental Stages** | http://purl.obolibrary.org/obo/hsapdv.owl | | [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) | |
|**Mouse Anatomy**|MA| http://purl.obolibrary.org/obo/ma.owl| |[CC-by 4.0](https://creativecommons.org/licenses/by/4.0/)| https://github.com/obophenotype/mouse-anatomy-ontology/issues ||
|**Strain**|Rat Strain Ontology|http://purl.obolibrary.org/obo/rs.owl| | [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/) | https://github.com/rat-genome-database/RS-Rat-Strain-Ontology/issues ||


In research, many different model organism are used (e.g. Dogs, Monkeys...) and specialized resources are available for many model organisms, including C. elegans, Drosophila, Xenopus, Zebrafish, plants and fungi. Use the selection criteria introduced earlier to gauge their value in the data management workflow and their impact on data integration tasks.




### Diseases and Phenotype

Biology is a complex field and observable manifestations of biological processes in living organisms vary, dependant on genetic background and environmental factors. Working on correlating genetic features with observable (phenotypic) ones, biologists rely heavily on such variables in the quest of disease biomarkers, which could be used to identify possible therapeutic targets. The main challenge is to ensure efficient machine actionable descriptions of these observable features.


|Scope|Name|File location|Top-Level Ontology|Licence|Issue Tracker URI|
|--- |--- |--- |--- |--- |--- | 
|**Pathology/Disease (generic)**|||||
| |SNOMED-CT| View on [Bioportal](https://bioportal.bioontology.org/ontologies/SNOMEDCT?p=summary) | |[SNOMED license](http://www.nlm.nih.gov/databases/umls.html) - part of the UMLS license|| |
| |NCI thesaurus|http://evs.nci.nih.gov/ftp1/NCI_Thesaurus| | [NCI license](http://evs.nci.nih.gov/ftp1/NCI_Thesaurus/ThesaurusTermsofUse.htm)|| |
| |ICD-10| login required| | [WHO license](http://www.who.int/about/copyright/en/)|||
| |UMLS| https://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html | |[UMLS license](http://www.nlm.nih.gov/databases/umls.html)|||
| |DOID|http://purl.obolibrary.org/obo/doid.owl|BFO| [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) |https://github.com/DiseaseOntology/HumanDiseaseOntology/issues| | 
| |MONDO*|http://purl.obolibrary.org/obo/mondo.owl|BFO| [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) |https://github.com/monarch-initiative/mondo/issues| 
| |IDO|https://code.google.com/p/infectious-disease-ontology/source/browse/trunk/src/ontology/ido-core/ido-main.owl|BFO| [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) |https://code.google.com/p/infectious-disease-ontology/issues/list| |
|**Phenotype**|||||
| | HP|http://purl.obolibrary.org/obo/hp.owl|BFO| [HPO Licence](https://hpo.jax.org/app/license) |https://github.com/obophenotype/human-phenotype-ontology/issues/|
| |MedDRA|||This ontology is freely accessible on [Bioportal](https://bioportal.bioontology.org/ontologies/MEDDRA) for academic and other non-commercial uses. Users anticipating any commercial use of MedDRA must contact the MSSO to obtain a license.|https://mssotools.com/webcr/ login required|
| | MP | http://purl.obolibrary.org/obo/mp.owl | | [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) | https://github.com/obophenotype/mammalian-phenotype-ontology/issues | 


*MONDO was born of an effort to harmonise disease definitions from a number sources, includig OMIM, Orphanet, EFO and DOID, with work in progress to include NCIt. The OWL version includes axiomatisation using CL, Uberon, GO, HP, RO & NCBITaxon. The ontology is under active development by a range of ontology and domain experts. If no other limiting requirements dictate the use of an alternative ontology (eg use of NCIt as part of a CDISC-compliant dataset), it is therefore the most recommended open source ontology from the above list.

As with anatomy in the previous section, there is a growing body of organism-specific phenotype resources, such as C. elegans, Drosophila, Fission Yeast, Xenopus and Zebrafish. 


### Pathology and Disease Specific Resources

There is a wide range of ontologies available for specific diseases or disease types. Some examples are given below but this list is by no means exhaustive. Check ontology repositories such as [OLS](https://www.ebi.ac.uk/ols/ontologies), [Bioportal](https://bioportal.bioontology.org/ontologies) or the [OBO Foundry](http://obofoundry.org/) for up-to-date lists of available ontologies

|Scope|Name|File location|Top-Level Ontology|Licence|Issue Tracker URI|
|--- |--- |--- |--- |--- |--- |
|**Malaria**|IDOMAL||BFO| [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)  ||
|**Alzheimer Disease**|ADO|https://www.scai.fraunhofer.de/content/dam/scai/de/downloads/bioinformatik/ontologies/ADO/ADO.zip|BFO|||
|**Rare disorder**|ORDO|||[CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)||



### Cellular entities

Following on through our review of semantic resources by granularity levels, this section details a number of reference resources which provide coverage for the describing `cell types`, `cell lines` {cite}`pmid29805321` and `cellular phenotypes`.

|Scope|Name|File location|Top-Level Ontology|Licence|Issue Tracker URI|
|--- |--- |--- |--- |--- |--- |
|**Cell**|CL|http://purl.obolibrary.org/obo/cl.owl http://purl.obolibrary.org/obo/cl.obo|BFO| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/)|https://code.google.com/p/cell-ontology/issues/list|
|**Cell Lines**| 
| | Cellosaurus|ftp://ftp.expasy.org/databases/cellosaurus/cellosaurus.obo ftp://ftp.expasy.org/databases/cellosaurus|| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/)||
| |CLO|[https://github.com/CLO-ontology/CLO/blob/master/src/ontology/clo.owl](https://github.com/CLO-ontology/CLO/blob/master/src/ontology/clo.owl)|BFO| [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) |https://github.com/CLO-ontology/CLO/issues|
|**Cell Molecular Phenotype Ontology**|CMPO|[last release](https://github.com/EBISPOT/CMPO/releases/tag/2017-12-19)| https://github.com/EBISPOT/CMPO/issues |




### Molecular Entities

This section highlights the major and most widely used OBO Foundry resources for `molecules of biological relevance` as well as `molecular structures`, `biological processes` and `cellular components` 


|Scope|Name|File location|Top-Level Ontology|Licence|Issue Tracker URI|
|--- |--- |--- |--- |--- |--- |
|**Chemicals and Small Molecules**|CHEBI|[CHEBI](https://www.ebi.ac.uk/chebi/)| BFO|[CC-by 4.0](https://creativecommons.org/licenses/by/4.0/) |https://github.com/ebi-chebi/ChEBI/issues|
|**Gene Function, Molecular Component, Biological Process**|GO|http://purl.obolibrary.org/obo/go.obo http://purl.obolibrary.org/obo/go.owl|BFO| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/) |http://sourceforge.net/p/geneontology/ontology-requests/|
|**Protein/peptide**|PRO|[Protein Ontology](https://proconsortium.org)|BFO| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/) |https://github.com/PROconsortium/PRoteinOntology/issues|


Besides these open ontologies, in the context of clinically relevant work where drug formulation require recording and description, the following resource is relevant.

|Scope|Name|File location|Top-Level Ontology|Licence|Issue Tracker URI|
|--- |--- |--- |--- |--- |--- |
| **Drug** |
| | National Drug File|||[NIH license](https://uts.nlm.nih.gov/license.html)||
| | DRON |  http://purl.obolibrary.org/obo/dron.owl | BFO | [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) | https://ontology.atlassian.net/browse/DRON |
| | RxNORM |View on [Bioportal](https://bioportal.bioontology.org/ontologies/RXNORM) | |[RxNORM license](http://www.nlm.nih.gov/databases/umls.html) - part of the UMLS license||


### Assays and Technologies

The resources listed in this section are providing key descriptors bridging data acquisition procedures (as used in a clinical setting and wet lab work) with instruments, units of measurements, endpoints as well as sometimes the biological process or molecular entities of biological significance.
Some of the resources are specialized semantic artefacts developed to support the standardized reporting of data modalities.

|Scope|Name|File location|Top-Level Ontology|Licence|Issue Tracker URI|
|--- |--- |--- |--- |--- |--- |
|**Radiology**|RADLex|https://data.bioontology.org/ontologies/RADLEX/submissions/41/download?apikey=8b5b7825-538d-40e0-9e9e-5ab9274a9aeb||||
|**Medical Imaging**|DICOM|http://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_D.html||||
|**Sample Processing/Reagents/Instruments Assay Definition**|OBI|http://purl.obolibrary.org/obo/obi.owl|BFO| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/)|https://github.com/obi-ontology/obi/issues|
|**Biological screening assays and their results including high-throughput screening (HTS)**|BAO|http://www.bioassayontology.org/bao/bao_complete_bfo_dev.owl|BFO| [CC-by-SA 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) ||
|**Mass Spectrometry (instrument/acquisition parameter/spectrum related information)**|PSI-MS|https://github.com/HUPO-PSI/psi-ms-CV |none specified| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/)|https://github.com/HUPO-PSI/psi-ms-CV/issues |
|**NMR Spectroscopy (instrument/acquisition parameter/spectrum related information)**|NMR-CV|http://nmrml.org/cv/v1.0.rc1/nmrCV.owl|BFO| [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) |https://github.com/nmrML/nmrML/issues?state=open|
|**Laboratory test**|LOINC|LOINC and RELMA Complete Download File (All Formats Included)|none specified| [RELMA license](https://uts.nlm.nih.gov/license.html) ||
|**Units** | UO | http://purl.obolibrary.org/obo/uo.owl | | [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) | https://github.com/bio-ontology-research-group/unit-ontology/issues |

Some multi-domain ontologies such as the NCI Thesaurus (NCIt) and the Experimental Factor Ontology (EFO) cover also aspects of the above domains such as assays and sample collection and processing. Depending on the overall context of a resource selection process, it can make more sense to use a multi-domain ontology with suitable coverage to improve consistency and interoperability within a resource or dataset.


Finally, a resource exists that describes statistical measures, statistical tests or methods as well as statistically relevant graphical representations. It may be used for reporting results and annotating experimental results.



|Scope|Name|File location|Top-Level Ontology|Licence|Issue Tracker URI|
|--- |--- |--- |--- |--- |--- |
| **Experimental Design, Statistical Methods and Statistical Measures**|STATO|[http://stato-ontology.org](http://stato-ontology.org)|BFO| [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/)|https://github.com/ISA-tools/stato/issues?state=open|




### Relations

Also known as OWL.Properties, their importance may be overlooked by `data scientists` who are not `knowledge engineers` or `ontologists`  but these are essential components as, when correctly crafted with a proper understanding of the logical constraints available to semantic languages such as OWL, are exploited by `automatic reasoners` to carry the following key tasks:

* `ontology logical consistency` checks
* `automatic classification` and `inference` tasks
* `entailments`, i.e. detection of logical consequences resulting from axiomatics

This is particularly important when processing billions of facts expressed as RDF statements. 

One also needs to understand the current limitations in expressivity afforded by the current semantic web languages and the associated axiomatics as well as computational constraints associated with inference. For more *in-depth* review of such topics, the reader is invited to consults the following work {cite}`pmid15892874` <!--[by Smith et al](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2005-6-5-r46)-->.

In the field of Biology and Biomedicine, the [OBO Foundry](http://obofoundry.org) coordinates the development of interoperable ontologies. At the core of this interoperation lies the **[Relation Ontology](http://www.obofoundry.org/ontology/ro.html)**

|Scope| File                        | Relation Ontology               | Variant                                                              | License  | 
|---|-------------------------------|---------------------------------|--------------------------------------------------------------------------------|---|
|**relations**| ro.owl                        | Relation Ontology               | Canonical edition                                                              | [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)  | 
|**relations**| ro.obo                        | Relation Ontology in obo format | Has imports merged in                                                          |  [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) |
|**relations**| ro/core.owl                   | RO Core relations               | Minimal subset intended to work with BFO-classes [page]                        |  [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) | 
|**relations**| ro/ro-base.owl                | RO base ontology                | Axioms defined within RO and to be used in imports for other ontologies [page] | [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)  | 
|**relations**| ro/subsets/ro-interaction.owl | Interaction relations           |                                   |  [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) |
|**relations**| ro/subsets/ro-eco.owl         | Ecology subset                  |   For use in ecology and environmental science  | [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)  | 
|**relations**| ro/subsets/ro-neuro.owl       | Neuroscience subset             | For use in neuroscience [page]                                                 | [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)  |    


As `knowledge graphs` and `property graphs` gain importance, we can expect the range and depth of relations to mature and expands as more expressivity is needed and progress is made by reasoner technology to fully exploit their benefits.
This would also have to be placed in the context of advances in `Text Mining` and `Machine Learning`, where unsupervised methods start to demonstrate strong potential to detect relations between entities.

```bash
B cell, CD19-positive
equivalentClass :
    lymphocyte of B lineage, CD19-positive 
    and ( has plasma membrane part some CD19 molecule) 
    and ( in taxon some Mammalia) 
    and ( capable of some B cell mediated immunity)
```


---
## Conclusions

> Selecting semantic resources depends on many different factors. However, the most important factor remains the `context` of the data and associated landscape of data standards as well as the ultimate integration goal, which will dictate the final choice.
> 
>The selection process remains guided by the need to maximize the potential of data integration with datasets of similar nature and similar value. It also requires a good understanding of the technical and sometimes legal implications these choice will have.    

> ### What should I read next?
> * [How to build an application ontology?]()
> * [How to select on ontology service?]()
> * [How to deploy an ontology server?]()
> * [How to establish a minimal metadata profile?]()
___

<!-- {download}`bibliography-identifier-mapping.bib <./bibref/bibliography-identifier-mapping.bib>` -->

## References
<!-- ../../../_bibliography/bibliography-identifier-mapping.bib -->
```{bibliography} 
:filter: docname in docnames
```

<!-- Smith, B., Ceusters, W., Klagges, B. et al. Relations in biomedical ontologies. Genome Biol 6, R46 (2005). https://doi.org/10.1186/gb-2005-6-5-r46

Rocca-Serra P, Bratfalean D, Richard F, Marshall C, Romacker M., Auffray C, ., … on the behalf of the eTRIKS consortium, . (2016, April 25). eTRIKS Standards Starter Pack Release 1.1 April 2016. Zenodo. http://doi.org/10.5281/zenodo.50825

Malone J, Stevens R, Jupp S, Hancocks T, Parkinson H, Brooksbank C. Ten Simple Rules for Selecting a Bio-ontology. PLoS Comput Biol. 2016;12(2):e1004743. Published 2016 Feb 11. http://doi.org/10.1371/journal.pcbi.1004743

Bairoch A. The Cellosaurus, a cell line knowledge resource. J. Biomol. Tech. (2018) 29:25-38. http://doi.org/10.7171/jbt.18-2902-002.

Sansone, S.-A., McQuilton, P., Rocca-Serra, P., Gonzalez-Beltran, A., Izzo, M., Lister, A.L. and Thurston, M. (2019) FAIRsharing as a community approach to standards, repositories and policies. Nature biotechnology, 37, 358: http://doi.org/10.1038/s41587-019-0080-8.

Hripcsak, G., Ryan, P. B., Duke, J. D., Shah, N. H., Park, R. W., Huser, V., Suchard, M. A., Schuemie, M. J., DeFalco, F. J., Perotte, A., Banda, J. M., Reich, C. G., Schilling, L. M., Matheny, M. E., Meeker, D., Pratt, N., & Madigan, D. (2016). Characterizing treatment pathways at scale using the OHDSI network. Proceedings of the National Academy of Sciences of the United States of America, 113(27), 7329–7336. https://doi.org/10.1073/pnas.1510502113

Hripcsak, George et al. “Observational Health Data Sciences and Informatics (OHDSI): Opportunities for Observational Researchers.” Studies in health technology and informatics vol. 216 (2015): 574-8.
 -->


___

## Authors

| Name                                                                                                                                                                            | Orcid                                                                                                         | Affiliation              | Type                                                                              |                                                              Elixir Node                                                              | Credit Role
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|--------------------------|-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------:|:----------------:|
| <div class="firstCol"><a target="_blank" href='https://github.com/proccaserra'><img class='avatar-style' src='https://avatars.githubusercontent.com/proccaserra'></img><div class="d-block">Philippe Rocca-Serra</div></a>  </div>         | <a target="_blank" href='https://orcid.org/0000-0001-9853-5668'><i class='fab fa-orcid fa-2x text--orange'></i></a> | University of Oxford     | <i class="fas fa-graduation-cap fa-1x text--orange" alt="Academic"></i> | <img class='elixir-style' src='/the-fair-cookbook/_static/images/logo/Elixir/ELIXIR-UK.svg' ></img> | Writing - Original Draft |
| <div class="firstCol"><a target="_blank" href='https://github.com/susannasansone'><img class='avatar-style' src='https://avatars.githubusercontent.com/susannasansone'></img><div class="d-block">Susanna-Assunta Sansone</div></a> </div> | <a target="_blank" href='https://orcid.org/0000-0001-5306-5690'><i class='fab fa-orcid fa-2x text--orange'></i></a> | University of Oxford     | <i class="fas fa-graduation-cap fa-1x text--orange" alt="Academic"></i> | <img class='elixir-style' src='/the-fair-cookbook/_static/images/logo/Elixir/ELIXIR-UK.svg' ></img> | Writing - Review & Editing, Funding acquisition
| <div class="firstCol"><a target="_blank" href='https://github.com/daniwelter'><img class='avatar-style' src='https://avatars.githubusercontent.com/daniwelter'></img><div class="d-block">Danielle Welter</div></a>   </div>      | <a target="_blank" href='https://orcid.org/0000-0003-1058-2668'><i class='fab fa-orcid fa-2x text--orange'></i></a> | University of Luxembourg        | <i class="fas fa-graduation-cap fa-1x text--orange" alt="Academic"></i> | <img class='elixir-style' src='/the-fair-cookbook/_static/images/logo/Elixir/ELIXIR-LU.svg' ></img> | Writing – Review & Editing


___

## License

This page is released under the Creative Commons 4.0 BY license.

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png" height="20"/></a>
