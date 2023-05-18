(fcb-selecting-ontologies)=
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

The main purpose of this recipe is to provide guidance on how to select the most suitable semantic artefacts given a specific research context in general, and when it comes to life and biomedical sciences projects, their main themes, i.e. *risk assessment*, *clinical trial*, *drug discovery* or *fundamental research*.


## Graphical Overview


````{dropdown} 
:open:
```{figure} selecting-ontologies.md-figure1.mmd.svg
---
width: 1000px
name: selecting-ontologies-figure1
alt:  Which ontology should be used?
---
 Which ontology should be used? Depending on dataset context, domain specific resources may be mandated, such as Clinical Data Interchange Standards Consortium (CDISC), Observational Health Data Sciences and Informatics (OHDSI) or Open Biomedical Ontologies (OBO). The Experimantal Factor Ontology (EFO) is specifically used by EMBL-EBI ArrayExpress to annotated dataset.
```
````

---

## Context is everything

The domain of operation will generally dictate the semantic framework that is most suited to a given dataset. This is simply due to the fact that the advances in data standardization in specific fields are such that it is a sound decision to adopt a complete stack of standards, both syntactic and semantic.

Here, we present the three most common scenarios in biomedical research, based on experience garnered during IMI eTRIKS (URL_TO_INSERT_RECORD-ABBREV_1915 https://fairsharing.org/3510)  {footcite}`philippe_rocca_serra_2016_50825`:
- [Clinical Trial Data](#clinical-trial-data)
- [Observational Health Data](#observational-health-data)
- [Basic research context](#basic-research-context)

### Clinical Trial Data

Operating in the field of Clinical Trials means that datasets are generated during `interventional studies`, meaning that researchers influence and control the predictor variables, which are usually different intensity levels of therapeutic agents, in order to gain insights in terms of benefits in patient outcomes.
In this context, regulatory requirements make it so that data must be recorded in standard forms to allow for review and appraisal by regulators such as FDA reviewers in the US. The [CDISC standards](https://www.cdisc.org/standards) are the *`de-facto standard`* in this area, which mandates the use of semantics resources such as:

| Semantic Resource | Domain  | Service |
| -- | -- | -- | 
| CDISC (URL_TO_INSERT_RECORD-NAME_1916 https://fairsharing.org/3525)  vocabulary|clinical trial data| EVS |
| NCI Thesaurus (URL_TO_INSERT_RECORD-NAME_1917 https://fairsharing.org/FAIRsharing.4cvwxa) |biomedicine|EVS,Bioporta (URL_TO_INSERT_RECORD-NAME_1919 https://fairsharing.org/FAIRsharing.4m97ah) l,OL (URL_TO_INSERT_RECORD-ABBREV_1918 https://fairsharing.org/FAIRsharing.Mkl9RR) S|
| SNOMED-CT|pathology|EVS,Bioporta (URL_TO_INSERT_RECORD-NAME_1920 https://fairsharing.org/FAIRsharing.4m97ah) l(§)|
| UMLS|pathology|EVS,Bioporta (URL_TO_INSERT_RECORD-NAME_1921 https://fairsharing.org/FAIRsharing.4m97ah) l(§)|
| LOINC (URL_TO_INSERT_RECORD-ABBREV_1922 https://fairsharing.org/FAIRsharing.2mk2zb) |laboratory tests|Loinc|
| RxNORM (URL_TO_INSERT_RECORD-NAME_1924 https://fairsharing.org/FAIRsharing.36pf8q) |drugs|Bioporta (URL_TO_INSERT_RECORD-NAME_1923 https://fairsharing.org/FAIRsharing.4m97ah) l|
| GUDID (URL_TO_INSERT_RECORD-ABBREV_1925 https://fairsharing.org/FAIRsharing.ennep4) |instruments|FDA|

All available from the [NCBI EVS system](https://evs.nci.nih.gov/), [LOINC](https://loinc.org/), [OLS](https://www.ebi.ac.uk/ols/index) or [Bioportal](https://bioportal.bioontology.org/).
 

```{warning}
Some resources are only available under restrictive licences, which prevent derivative work, which may limit access and use. Furthermore, some licenses are expensive.  
```

### Observational Health Data

This context refers to data collected during `observational studies`, which in contrast to `interventional studies`, draw inferences from a sample to a population where the independent variable is not under the control of the researcher because of ethical concerns or logistical constraints [1]. This is typically the case in epidemiological work or exposure follow-up studies in the context of risk assessment and evaluation of clinical outcomes. `Observational health data` can also include `electronic health records (EHR)` or ` administrative insurance claims` and allow research around acquiring *`real world evidence`* from large corpora of data.
In this specific context, one model and associated set of standards has been particularly successful. With several hundred millions of patients' information structured using the **Observational Medical Outcomes Partnership ([OMOP](https://ohdsi.org/omop/))**, the Observational Health Data Sciences and Informatics ([ODHSI](https://ohdsi.org/)) `open-science community` has laid the foundation for a widely adopted data model. Therefore, building a FAIRification process around the standard stack produced by the ODHSI community needs to be considered if operating in such a `data context`.


|Semantic Resource|Domain |Service|
|--- |---  |--- |
|CDISC (URL_TO_INSERT_RECORD-NAME_1926 https://fairsharing.org/3525)  vocabulary|clinical trial data|EVS|
|NCI Thesaurus (URL_TO_INSERT_RECORD-NAME_1927 https://fairsharing.org/FAIRsharing.4cvwxa) |biomedicine|EVS,Bioporta (URL_TO_INSERT_RECORD-NAME_1929 https://fairsharing.org/FAIRsharing.4m97ah) l,OL (URL_TO_INSERT_RECORD-ABBREV_1928 https://fairsharing.org/FAIRsharing.Mkl9RR) S|
|SNOMED-CT|pathology|EVS,Bioporta (URL_TO_INSERT_RECORD-NAME_1930 https://fairsharing.org/FAIRsharing.4m97ah) l(§)|
|UMLS|pathology|EVS,Bioporta (URL_TO_INSERT_RECORD-NAME_1931 https://fairsharing.org/FAIRsharing.4m97ah) l(§)|
|LOINC (URL_TO_INSERT_RECORD-ABBREV_1932 https://fairsharing.org/FAIRsharing.2mk2zb) |laboratory tests| LOINC (URL_TO_INSERT_RECORD-ABBREV_1933 https://fairsharing.org/FAIRsharing.2mk2zb)  |
|RxNORM (URL_TO_INSERT_RECORD-NAME_1935 https://fairsharing.org/FAIRsharing.36pf8q) |drugs|Bioporta (URL_TO_INSERT_RECORD-NAME_1934 https://fairsharing.org/FAIRsharing.4m97ah) l|


For a more detailed overview and deep-dive into the ODHSI and OMOP semantic support, we recommend the reading of the chapter dedicated to the `controlled terminology` [in the **`Book of OHDSI`**](https://ohdsi.github.io/TheBookOfOhdsi/StandardizedVocabularies.html) {footcite}`pmid27274072`


### Basic research context

This refers to datasets and research output being generated using model organisms and cellular systems in the context of basic, fundamental research. In this arena, the regulatory pressure is much less present but this does not rule out data management best practices and proper archival requirements.
As a consequence of fewer constraints, researchers are often confronted with a sea of options. This and the next sections aim to provide some guidance when tasked with deciding on which semantic resource to use.

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

1. The use and implementation of common terminologies enables the normalisation and harmonisation of both variable labels and allowed values for each field. Implementing the use of common terminologies in the data collection or curation workflow will ensure consistency of the annotation across all data. This is particularly important if data is generated at multiple partner sites and/or by multiple individuals. 

2. If data fields are annotated with terms from freely chosen ontologies (rather than those dictated by a common model such as CDSIC), care should be taken to avoid picking terms from ontologies at random. If a set of concepts are all available in one ontology, this ontology should be preferred over a set of ontologies. Mapping services such as [OxO](https://www.ebi.ac.uk/spot/oxo/) are available to verify whether a term of interest in one ontology has an equivalent term in another ontology.

3. Restrictions of allowed values for a given field should ideally be limited to a single ontology and better yet, to a single branch of a chosen ontology. This will vastly improve the semantic queryability as well as the consistency and interoperability of the data. 

4. Many ontologies and vocabularies reuse concepts from other ontologies, in line with best practice in ontology design, to limit duplication of efforts and proliferation of parallel synonymous concepts. Care should however be taken to use concepts in the most appropriate environment. This is usually their original source unless they are used as part of a larger set of terms. As an example, the Experimental Factor Ontology (URL_TO_INSERT_RECORD-NAME_1937 https://fairsharing.org/FAIRsharing.1gr4tz)  (EFO (URL_TO_INSERT_RECORD-ABBREV_1938 https://fairsharing.org/FAIRsharing.1gr4tz) ) reuses concepts from a range of ontologies, including species from the NCBI taxonomy (URL_TO_INSERT_RECORD-NAME_1941 https://fairsharing.org/FAIRsharing.fj07xj) , assays from OBI (URL_TO_INSERT_RECORD-ABBREV_1943 https://fairsharing.org/FAIRsharing.284e1z) , and diseases and phenotypes from MONDO (URL_TO_INSERT_RECORD-ABBREV_1936 https://fairsharing.org/FAIRsharing.b2979t)  and HPO. If annotating a dataset or resource which covers all of these concepts, it therefore makes sense to use EFO (URL_TO_INSERT_RECORD-ABBREV_1939 https://fairsharing.org/FAIRsharing.1gr4tz)  as the primary annotation source. However, if only annotations for species are required, the NCBI taxonomy (URL_TO_INSERT_RECORD-NAME_1942 https://fairsharing.org/FAIRsharing.fj07xj)  should be used directly to ensure completeness, since not all species in NCBItaxon will have been imported into EFO (URL_TO_INSERT_RECORD-ABBREV_1940 https://fairsharing.org/FAIRsharing.1gr4tz) .



### Selection Criteria

A set of widely accepted criteria for selecting terminologies (or other reporting standards) does not exist. There are however a number of excellent publications such as ["A sea of standards for omics data: sink or swim?"](https://doi.org/10.1136/amiajnl-2013-002066) {footcite}`pmid24076747` and ["Ten Simple Rules for Selection a Bio-ontology"](https://doi.org/10.1371/journal.pcbi.1004743) {footcite}`pmid26867217` providing some guidance on the subject. Below are a set of suggested criteria for evaluating the suitability of a terminology resource.


*   **Exclusion criteria**:
    * 🔸 Absent licence or terms of use (_indicator of usability_)
    * 🔸 Restrictive licences or terms of use with restrictions on redistribution and reuse 
    * 🔸 Absence of term definitions 
    * 🔸 Absence of sufficient class metadata (_indicator of quality_)
    * 🔸 Absence of sustainability indicators (_absence of funding records_) 
 
*   **Inclusion criteria**:
    * 🔰  Scope and coverage meets the requirements of the concept identified
    * 🔰  Unique URI (URL_TO_INSERT_RECORD-ABBREV_1944 https://fairsharing.org/FAIRsharing.d261e1) , textual definition and IDs for each term
    * 🔰  Resource releases are versioned
    * 🔰  Size of resource (_indicator of coverage_)
    * 🔰  Number of classes and subclasses (_indicator of depth_)
    * 🔰  Number of terms having definitions and synonyms (_indicator of richness_)
    * 🔰  Presence of a help desk and contact point (_indicator of community support_)
    * 🔰  Presence of term submission tracker/issue tracker (_indicator of resource agility and capability to grow upon request_)
    * 🔰  Potential integrative nature of the resource (_as indicator of translational application potential_)
    * 🔰  Licensing information available (_as indicator of freedom to use_)
    * 🔰  Use of a top level ontology (_as indicator of a resource built for generic use_)
    * 🔰  Pragmatism (_as indicator of actual, current real life practice)_
    * 🔰  Possibility of collaborating: the resource accepts complaints/remarks that aim to fix or improve the terminology, while the resource organisation commits to fix or improve the terminology in brief delays (one month after receipt?)


### Set of Core Terminologies 

The terminologies presented here have been organized by theme and scope. When possible, sections are organized by `granularity levels`, progressing from `macroscopic scale` (organism) to `microscopic scale` (tissue, cells) and `molecular scale` (macromolecules, proteins, small molecules, xenobiotic chemicals).
Domains also cover `processes` or `actions` and their `participants` or `agents` but also can be organized from `general/generic` (disease) to `specialized/specific` (infectious disease).


#### Organism, Organism Parts and Developmental Stages

The resources listed here focus on providing structured vocabularies to describe `taxonomic` and `anatomical` information. 

|Scope|Name|File location|Top-Level Ontology|Licence|Issue Tracker URI (URL_TO_INSERT_RECORD-ABBREV_1945 https://fairsharing.org/FAIRsharing.d261e1) |Comment|
|--- |--- |--- |--- |--- |--- |--- |
|**Organism**|NCBITaxonomy|http://purl.obolibrary.org/obo/ncbitaxon.owl|none specified| [UMLS license](https://uts.nlm.nih.gov/license.html)|||
|**Vertebrate Anatomy**|UBERON|http://purl.obolibrary.org/obo/uberon/ext.owl http://purl.obolibrary.org/obo/uberon/ext.obo|BFO| [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) |https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_1946 https://fairsharing.org/FAIRsharing.c55d5e) /obophenotype/uberon/issues|Integrative Resource engineered to go across species|
|**Human Anatomy**| Foundational Model of Anatomy (URL_TO_INSERT_RECORD-NAME_1947 https://fairsharing.org/FAIRsharing.x56jsy)  (FMA (URL_TO_INSERT_RECORD-ABBREV_1948 https://fairsharing.org/FAIRsharing.x56jsy) ) | http://purl.obolibrary.org/obo/fma.owl | | [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) |https://sourceforge.net (URL_TO_INSERT_RECORD-HOMEPAGE_1949 https://fairsharing.org/FAIRsharing.b138b5) /p/obo/foundational-model-of-anatomy-fma-requests/| Excellent cross-referencing with Uberon|
| **Human Developmental Stages** | Human Developmental Stages | http://purl.obolibrary.org/obo/hsapdv.owl | | [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) |
|**Mouse Anatomy**| Mouse Anatomy (MA (URL_TO_INSERT_RECORD-ABBREV_1950 https://fairsharing.org/FAIRsharing.pdwqcr) )| http://purl.obolibrary.org/obo/ma.owl| |[CC-by 4.0](https://creativecommons.org/licenses/by/4.0/)| https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_1951 https://fairsharing.org/FAIRsharing.c55d5e) /obophenotype/mouse-anatomy-ontology/issues ||
|**Strain**|Rat Strain Ontol (URL_TO_INSERT_RECORD-NAME_1953 https://fairsharing.org/FAIRsharing.vajn3f) ogy|http://purl.obolibrary.org/obo/rs.owl| | [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/) | https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_1952 https://fairsharing.org/FAIRsharing.c55d5e) /rat-genome-database/RS-Rat-Strain-Ontology/issues ||


In research, many different model organisms are used (e.g. Dogs, Monkeys...) and specialized resources are available for many model organisms, including C. elegans, Drosophila, Xenopus, Zebrafish, plants and fungi. Use the selection criteria introduced earlier to gauge their value in the data management workflow and their impact on data integration tasks.




#### Diseases and Phenotype

Biology is a complex field and observable manifestations of biological processes in living organisms vary, dependant on genetic background and environmental factors. Working on correlating genetic features with observable (phenotypic) ones, biologists rely heavily on such variables in the quest of disease biomarkers, which could be used to identify possible therapeutic targets. The main challenge is to ensure efficient machine actionable descriptions of these observable features.


|Scope|Name|File location|Top-Level Ontology|Licence|Issue Tracker URI (URL_TO_INSERT_RECORD-ABBREV_1954 https://fairsharing.org/FAIRsharing.d261e1) |
|--- |--- |--- |--- |--- |--- | 
|**Pathology/Disease (generic)**|||||
| |SNOMED-CT| View on [Bioportal](https://bioportal.bioontology.org/ontologies/SNOMEDCT?p=summary) | |[SNOMED license](http://www.nlm.nih.gov/databases/umls.html) - part of the UMLS license|| |
| |NCI Thesaurus (URL_TO_INSERT_RECORD-NAME_1955 https://fairsharing.org/FAIRsharing.4cvwxa) |http://evs.nci.nih.gov/ftp1/NCI_Thesaurus| | [NCI license](http://evs.nci.nih.gov/ftp1/NCI_Thesaurus/ThesaurusTermsofUse.htm)|| |
| |International Classification of Diseases (ICD-10 (URL_TO_INSERT_RECORD-ABBREV_1956 https://fairsharing.org/FAIRsharing.nj16g) )| View on [WHO site](https://icd.who.int/browse10/2010/en)| | [WHO license](http://www.who.int/about/copyright/en/)|||
| | Unified Medical Language System (UMLS) | https://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html | |[UMLS license](http://www.nlm.nih.gov/databases/umls.html)|||
| | Disease Ontology (URL_TO_INSERT_RECORD-NAME_1958 https://fairsharing.org/FAIRsharing.8b6wfq)  Identifiers (DOID (URL_TO_INSERT_RECORD-ABBREV_1959 https://fairsharing.org/FAIRsharing.8b6wfq) ) |http://purl.obolibrary.org/obo/doid.owl|BFO| [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) |https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_1957 https://fairsharing.org/FAIRsharing.c55d5e) /DiseaseOntology/HumanDiseaseOntology/issues| | 
| |MONDO (URL_TO_INSERT_RECORD-ABBREV_1960 https://fairsharing.org/FAIRsharing.b2979t)  Disease Ontology (URL_TO_INSERT_RECORD-NAME_1962 https://fairsharing.org/FAIRsharing.8b6wfq) <sup>*</sup> |http://purl.obolibrary.org/obo/mondo.owl|BFO| [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) |https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_1961 https://fairsharing.org/FAIRsharing.c55d5e) /monarch-initiative/mondo/issues| 
| |Infectious Disease Ontology (URL_TO_INSERT_RECORD-NAME_1963 https://fairsharing.org/FAIRsharing.8b6wfq)  (IDO (URL_TO_INSERT_RECORD-ABBREV_1964 https://fairsharing.org/FAIRsharing.aae3v6) ) |https://code.google.com/p/infectious-disease-ontology/source/browse/trunk/src/ontology/ido-core/ido-main.owl|BFO| [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) |https://code.google.com/p/infectious-disease-ontology/issues/list| |
|**Phenotype**|||||
| | Human Phenotype (HP (URL_TO_INSERT_RECORD-ABBREV_1966 https://fairsharing.org/FAIRsharing.kbtt7f) ) |http://purl.obolibrary.org/obo/hp.owl|BFO| [HPO Licence](https://hpo.jax.org/app/license) |https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_1965 https://fairsharing.org/FAIRsharing.c55d5e) /obophenotype/human-phenotype-ontology/issues/|
| |Medical Dictionary for Regulatory Activities Terminology (URL_TO_INSERT_RECORD-NAME_1967 https://fairsharing.org/FAIRsharing.ad3137)  (MedDRA (URL_TO_INSERT_RECORD-ABBREV_1968 https://fairsharing.org/FAIRsharing.ad3137) )| View on [Bioportal](https://bioportal.bioontology.org/ontologies/MEDDRA) || Academic: Free accessible <br/> Commercial contact MSSO|https://mssotools.com/webcr/ login required|
| | Mammalian Phenotype (MP (URL_TO_INSERT_RECORD-ABBREV_1970 https://fairsharing.org/FAIRsharing.kg1x4z) ) | http://purl.obolibrary.org/obo/mp.owl | | [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) | https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_1969 https://fairsharing.org/FAIRsharing.c55d5e) /obophenotype/mammalian-phenotype-ontology/issues | 


> _<sup>*</sup>MOND (URL_TO_INSERT_RECORD-ABBREV_1971 https://fairsharing.org/FAIRsharing.b2979t) O was born of an effort to harmonise disease definitions from a number sources, includig [OMIM](https://www.omim.org/) (Online Mendelian Inheritance in Man (URL_TO_INSERT_RECORD-NAME_1982 https://fairsharing.org/FAIRsharing.9qkaz9) ), [Orphanet](https://www.orpha.net/), EFO (URL_TO_INSERT_RECORD-ABBREV_1973 https://fairsharing.org/FAIRsharing.1gr4tz)  and DOID (URL_TO_INSERT_RECORD-ABBREV_1976 https://fairsharing.org/FAIRsharing.8b6wfq) , with work in progress to include NCIt (URL_TO_INSERT_RECORD-ABBREV_1972 https://fairsharing.org/FAIRsharing.4cvwxa) . The OWL (URL_TO_INSERT_RECORD-ABBREV_1977 https://fairsharing.org/FAIRsharing.atygwy)  version includes axiomatisation using CL (URL_TO_INSERT_RECORD-ABBREV_1975 https://fairsharing.org/FAIRsharing.j9y503) , Uberon, GO (URL_TO_INSERT_RECORD-ABBREV_1974 https://fairsharing.org/FAIRsharing.6xq0ee) , HP (URL_TO_INSERT_RECORD-ABBREV_1981 https://fairsharing.org/FAIRsharing.kbtt7f) , RO (URL_TO_INSERT_RECORD-ABBREV_1978 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD-ABBREV_1979 https://fairsharing.org/FAIRsharing.cp0ybc)  (URL_TO_INSERT_RECORD-ABBREV_1980 https://fairsharing.org/FAIRsharing.504c6c)  & NCBITaxon. The ontology is under active development by a range of ontology and domain experts. If no other limiting requirements dictate the use of an alternative ontology (e.g. use of NCItaxon as part of a CDISC (URL_TO_INSERT_RECORD-NAME_1983 https://fairsharing.org/3525) -compliant dataset), it is therefore the most recommended open source ontology from the above list._

As with anatomy in the previous section, there is a growing body of organism-specific phenotype resources, such as C. elegans, Drosophila, Fission Yeast, Xenopus and Zebrafish. 


#### Pathology and Disease Specific Resources

There is a wide range of ontologies available for specific diseases or disease types. Some examples are given below but this list is by no means exhaustive. Check ontology repositories such as [OLS](https://www.ebi.ac.uk/ols/ontologies), [Bioportal](https://bioportal.bioontology.org/ontologies) or the [OBO Foundry (URL_TO_INSERT_RECORD-NAME_1984 https://fairsharing.org/FAIRsharing.847069) ](http://obofoundry.org/) for up-to-date lists of available ontologies

|Scope|Name|File location|Top-Level Ontology|Licence|Issue Tracker URI (URL_TO_INSERT_RECORD-ABBREV_1985 https://fairsharing.org/FAIRsharing.d261e1) |
|--- |--- |--- |--- |--- |--- |
|**Malaria**|Malaria Ontology (IDOMAL (URL_TO_INSERT_RECORD-ABBREV_1986 https://fairsharing.org/FAIRsharing.2q8c28) )||BFO| [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)  ||
|**Alzheimer Disease**| Alzheimer's Disease Ontology (URL_TO_INSERT_RECORD-NAME_1987 https://fairsharing.org/FAIRsharing.ckd4rf)  (URL_TO_INSERT_RECORD-NAME_1989 https://fairsharing.org/FAIRsharing.8b6wfq)  (ADO (URL_TO_INSERT_RECORD-ABBREV_1988 https://fairsharing.org/FAIRsharing.ckd4rf) ) |https://www.scai.fraunhofer.de/content/dam/scai/de/downloads/bioinformatik/ontologies/ADO/ADO.zip|BFO|||
|**Rare disorder**| Orphanet (URL_TO_INSERT_RECORD-NAME_1990 https://fairsharing.org/FAIRsharing.6bd5k6)  Rare Disease Ontology (URL_TO_INSERT_RECORD-NAME_1993 https://fairsharing.org/FAIRsharing.8b6wfq)  (ORDO (URL_TO_INSERT_RECORD-ABBREV_1991 https://fairsharing.org/FAIRsharing.pbbnwa)  (URL_TO_INSERT_RECORD-ABBREV_1992 https://fairsharing.org/FAIRsharing.1566e7) ) | View on [Bioportal](https://bioportal.bioontology.org/ontologies/ORDO)||[CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)||



#### Cellular entities

Following on through our review of semantic resources by granularity levels, this section details a number of reference resources which provide coverage for the describing `cell types`, `cell lines` {footcite}`pmid29805321` and `cellular phenotypes`.

|Scope|Name|File location|Top-Level Ontology|Licence|Issue Tracker URI (URL_TO_INSERT_RECORD-ABBREV_1994 https://fairsharing.org/FAIRsharing.d261e1) |
|--- |--- |--- |--- |--- |--- |
|**Cell**| Cell Ontology (URL_TO_INSERT_RECORD-NAME_1995 https://fairsharing.org/FAIRsharing.j9y503)  (CL (URL_TO_INSERT_RECORD-ABBREV_1996 https://fairsharing.org/FAIRsharing.j9y503) ) |http://purl.obolibrary.org/obo/cl.owl http://purl.obolibrary.org/obo/cl.obo|BFO| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/)|https://code.google.com/p/cell-ontology/issues/list|
|**Cell Lines**| 
| | Cellosaurus|ftp://ftp.expasy.org/databases/cellosaurus/cellosaurus.obo ftp://ftp.expasy.org/databases/cellosaurus|| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/)||
| | Cell Line Ontology (URL_TO_INSERT_RECORD-NAME_1997 https://fairsharing.org/FAIRsharing.4dvtcz)  (CLO (URL_TO_INSERT_RECORD-ABBREV_1998 https://fairsharing.org/FAIRsharing.4dvtcz) ) |[https://github.com/CLO-ontology/CLO/blob/master/src/ontology/clo.owl](https://github.com/CLO-ontology/CLO/blob/master/src/ontology/clo.owl)|BFO| [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) |https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2000 https://fairsharing.org/FAIRsharing.c55d5e) /CLO-ontology/CLO (URL_TO_INSERT_RECORD-HOMEPAGE_1999 https://fairsharing.org/FAIRsharing.4dvtcz) /issues|
|**Cell Molecular Phenotype**|Cell Molecular Phenotype Ontology (CMPO (URL_TO_INSERT_RECORD-ABBREV_2001 https://fairsharing.org/FAIRsharing.knp11s) ) |https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2002 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/CMPO/releases/| | | https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2003 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/CMPO/issues |




#### Molecular Entities

This section highlights the major and most widely used OBO Foundry (URL_TO_INSERT_RECORD-NAME_2004 https://fairsharing.org/FAIRsharing.847069)  resources for `molecules of biological relevance` as well as `molecular structures`, `biological processes` and `cellular components` 


|Scope|Name|File location|Top-Level Ontology|Licence|Issue Tracker URI (URL_TO_INSERT_RECORD-ABBREV_2005 https://fairsharing.org/FAIRsharing.d261e1) |
|--- |--- |--- |--- |--- |--- |
|**Chemicals and Small Molecules**| Chemical Entities of Biological Interest (URL_TO_INSERT_RECORD-NAME_2006 https://fairsharing.org/FAIRsharing.62qk8w)  (ChEBI (URL_TO_INSERT_RECORD-ABBREV_2007 https://fairsharing.org/FAIRsharing.62qk8w) )|[ChEBI](https://www.ebi.ac.uk/chebi/)| BFO|[CC-by 4.0](https://creativecommons.org/licenses/by/4.0/) |https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2008 https://fairsharing.org/FAIRsharing.c55d5e) /ebi-chebi/ChEBI/issues|
|**Gene Function, Molecular Component, Biological Process**| Gene Ontology (URL_TO_INSERT_RECORD-NAME_2010 https://fairsharing.org/FAIRsharing.6xq0ee)  (GO (URL_TO_INSERT_RECORD-ABBREV_2011 https://fairsharing.org/FAIRsharing.6xq0ee) ) |http://purl.obolibrary.org/obo/go.obo http://purl.obolibrary.org/obo/go.owl|BFO| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/) |http://sourceforge.net (URL_TO_INSERT_RECORD-HOMEPAGE_2009 https://fairsharing.org/FAIRsharing.b138b5) /p/geneontology/ontology-requests/|
|**Protein (URL_TO_INSERT_RECORD-ABBREV_2013 https://fairsharing.org/FAIRsharing.rtndct) /peptide**| Protein (URL_TO_INSERT_RECORD-ABBREV_2014 https://fairsharing.org/FAIRsharing.rtndct)  Ontology (URL_TO_INSERT_RECORD-NAME_2016 https://fairsharing.org/FAIRsharing.4ndncv)  (PRO (URL_TO_INSERT_RECORD-ABBREV_2012 https://fairsharing.org/FAIRsharing.3e88d6)  (URL_TO_INSERT_RECORD-ABBREV_2017 https://fairsharing.org/FAIRsharing.4ndncv) ) |https://proconsortium.org (URL_TO_INSERT_RECORD-HOMEPAGE_2018 https://fairsharing.org/FAIRsharing.4ndncv)  |BFO| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/) |https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2015 https://fairsharing.org/FAIRsharing.c55d5e) /PROconsortium/PRoteinOntology/issues|


Besides, these open ontologies, in the context of clinically relevant work where drug formulation require recording and description, the following resources are relevant.

|Scope|Name|File location|Top-Level Ontology|Licence|Issue Tracker URI (URL_TO_INSERT_RECORD-ABBREV_2019 https://fairsharing.org/FAIRsharing.d261e1) |
|--- |--- |--- |--- |--- |--- |
| **Drug** |
| | National Drug File (URL_TO_INSERT_RECORD-NAME_2020 https://fairsharing.org/FAIRsharing.901nkj) | View on [Bioportal](https://bioportal.bioontology.org/ontologies/NDFRT) ||[NIH license](https://uts.nlm.nih.gov/license.html)||
| | The Drug Ontology (URL_TO_INSERT_RECORD-NAME_2021 https://fairsharing.org/FAIRsharing.w5ntfd)  (DRON) |  http://purl.obolibrary.org/obo/dron.owl | BFO | [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) | https://ontology.atlassian.net/browse/DRON |
| | RxNORM (URL_TO_INSERT_RECORD-NAME_2022 https://fairsharing.org/FAIRsharing.36pf8q)  |View on [Bioportal](https://bioportal.bioontology.org/ontologies/RXNORM) | |[RxNORM (URL_TO_INSERT_RECORD-NAME_2023 https://fairsharing.org/FAIRsharing.36pf8q)  license](http://www.nlm.nih.gov/databases/umls.html) - part of the UMLS license||


#### Assays and Technologies

The resources listed in this section are providing key descriptors bridging data acquisition procedures (as used in a clinical setting and wet lab work) with instruments, units of measurements, endpoints as well as sometimes the biological process or molecular entities of biological significance.
Some of the resources are specialized semantic artefacts developed to support the standardized reporting of data modalities.

|Scope|Name|File location|Top-Level Ontology|Licence|Issue Tracker URI (URL_TO_INSERT_RECORD-ABBREV_2024 https://fairsharing.org/FAIRsharing.d261e1) |
|--- |--- |--- |--- |--- |--- |
|**Radiology**| Radiology Lexicon (URL_TO_INSERT_RECORD-NAME_2025 https://fairsharing.org/FAIRsharing.shm2f2)  (RADLex) | View on [Bioportal](https://bioportal.bioontology.org/ontologies/RADLEX) ||||
|**Medical Imaging**|DI (URL_TO_INSERT_RECORD-ABBREV_2026 https://fairsharing.org/FAIRsharing.b7z8by) COM|http://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_D.html (URL_TO_INSERT_RECORD-HOMEPAGE_2027 https://fairsharing.org/FAIRsharing.p1ss22) ||||
|**Sample Processing/Reagents/Instruments Assay Definition**| Ontology for Biomedical Investigations (URL_TO_INSERT_RECORD-NAME_2028 https://fairsharing.org/FAIRsharing.284e1z)  (OBI (URL_TO_INSERT_RECORD-ABBREV_2029 https://fairsharing.org/FAIRsharing.284e1z) ) |http://purl.obolibrary.org/obo/obi.owl|BFO| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/)|https://github.com/obi-ontology/obi/issues|
|**Biological screening assays and their results including high-throughput screening (HTS)**| BioAssay Ontology (URL_TO_INSERT_RECORD-NAME_2031 https://fairsharing.org/FAIRsharing.mye76w)  (BAO (URL_TO_INSERT_RECORD-ABBREV_2032 https://fairsharing.org/FAIRsharing.mye76w) ) |http://www.bioassayontology.org (URL_TO_INSERT_RECORD-HOMEPAGE_2030 https://fairsharing.org/FAIRsharing.farr39)  (URL_TO_INSERT_RECORD-HOMEPAGE_2033 https://fairsharing.org/FAIRsharing.mye76w) /bao/bao_complete_bfo_dev.owl|BFO| [CC-by-SA 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) ||
|**Mass Spectrometry (instrument/acquisition parameter/spectrum related information)**| HUPO Proteomics Standards Initiative (URL_TO_INSERT_RECORD-NAME_2035 https://fairsharing.org/3514) -Mass Spectrometry controlled vocabulary (PSI-MS) |https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2034 https://fairsharing.org/FAIRsharing.c55d5e) /HUPO-PSI/psi-ms-CV |none specified| [CC-by 4.0](https://creativecommons.org/licenses/by/4.0/)|https://github.com/HUPO-PSI/psi-ms-CV/issues |
|**NMR Spectroscopy (instrument/acquisition parameter/spectrum related information)**| Nuclear Magnetic Resonance Controlled Vocabulary (URL_TO_INSERT_RECORD-NAME_2036 https://fairsharing.org/FAIRsharing.xm7tkj)  (NMR-CV) |http://nmrml.org (URL_TO_INSERT_RECORD-HOMEPAGE_2039 https://fairsharing.org/FAIRsharing.es03fk) /cv (URL_TO_INSERT_RECORD-HOMEPAGE_2037 https://fairsharing.org/FAIRsharing.xm7tkj) /v1.0.rc1/nmrCV.owl|BFO| [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) |https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2038 https://fairsharing.org/FAIRsharing.c55d5e) /nmrML/nmrML/issues?state=open|
|**Laboratory test**| Logical Observation Identifier Names and Codes (URL_TO_INSERT_RECORD-NAME_2040 https://fairsharing.org/FAIRsharing.2mk2zb)  (LOINC (URL_TO_INSERT_RECORD-ABBREV_2041 https://fairsharing.org/FAIRsharing.2mk2zb) ) | LOINC (URL_TO_INSERT_RECORD-ABBREV_2042 https://fairsharing.org/FAIRsharing.2mk2zb)  and RELMA Complete Download File https://loinc.org (URL_TO_INSERT_RECORD-HOMEPAGE_2043 https://fairsharing.org/FAIRsharing.2mk2zb) /downloads/ |none specified| [RELMA license](https://uts.nlm.nih.gov/license.html) ||
|**Units** | Units Ontology (URL_TO_INSERT_RECORD-NAME_2044 https://fairsharing.org/FAIRsharing.mjnypw)  (UO (URL_TO_INSERT_RECORD-ABBREV_2045 https://fairsharing.org/FAIRsharing.mjnypw) ) | http://purl.obolibrary.org/obo/uo.owl | | [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/) | https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2047 https://fairsharing.org/FAIRsharing.c55d5e) /bio-ontology-research-group/unit-ontology (URL_TO_INSERT_RECORD-HOMEPAGE_2046 https://fairsharing.org/FAIRsharing.mjnypw) /issues |

Some multi-domain ontologies such as the NCI Thesaurus (URL_TO_INSERT_RECORD-NAME_2048 https://fairsharing.org/FAIRsharing.4cvwxa)  (NCIt (URL_TO_INSERT_RECORD-ABBREV_2049 https://fairsharing.org/FAIRsharing.4cvwxa) ) and the Experimental Factor Ontology (URL_TO_INSERT_RECORD-NAME_2050 https://fairsharing.org/FAIRsharing.1gr4tz)  (EFO (URL_TO_INSERT_RECORD-ABBREV_2051 https://fairsharing.org/FAIRsharing.1gr4tz) ) also cover aspects of the above domains such as assays and sample collection and processing. Depending on the overall context of a resource selection process, it can make more sense to use a multi-domain ontology with suitable coverage to improve consistency and interoperability within a resource or dataset.


Finally, a resource exists that describes statistical measures, statistical tests or methods as well as statistically relevant graphical representations. It may be used for reporting results and annotating experimental results (URL_TO_INSERT_RECORD-NAME_2052 https://fairsharing.org/FAIRsharing.QlUiql) .



|Scope|Name|File location|Top-Level Ontology|Licence|Issue Tracker URI (URL_TO_INSERT_RECORD-ABBREV_2053 https://fairsharing.org/FAIRsharing.d261e1) |
|--- |--- |--- |--- |--- |--- |
| **Experimental Design, Statistical Methods and Statistical Measures**| Statistical Methods Ontology (STATO (URL_TO_INSERT_RECORD-ABBREV_2054 https://fairsharing.org/FAIRsharing.na5xp) ) |[http://stato-ontology.org](http://stato-ontology.org)|BFO| [CC-by 3.0 Unported Licence](https://creativecommons.org/licenses/by/3.0/)|https://github.com/ISA-tools/stato/issues?state=open|




### Relations

Also known as `OWL (URL_TO_INSERT_RECORD-ABBREV_2055 https://fairsharing.org/FAIRsharing.atygwy)  Properties`, their importance may be overlooked by `data scientists` who are not `knowledge engineers` or `ontologists`. These are essential components as, when correctly crafted with a proper understanding of the logical constraints available to semantic languages such as OWL (URL_TO_INSERT_RECORD-ABBREV_2056 https://fairsharing.org/FAIRsharing.atygwy) , are exploited by tools known as `reasoners` to carry the following key tasks:

* `Ontology logical consistency` checks
* `Automatic classification` and `inference` tasks
* `Entailments`, i.e. detection of logical consequences resulting from axiomatic definitions (closely related to the point above)

This is particularly important when processing billions of facts expressed as RDF (URL_TO_INSERT_RECORD-ABBREV_2057 https://fairsharing.org/FAIRsharing.p77ph9)  statements. 

One also needs to understand the current limitations in expressivity afforded by the current semantic web languages and the associated axiomatics as well as computational constraints associated with inference. For more *in-depth* review of such topics, the reader is invited to consults the following work {footcite}`pmid15892874` <!--[by Smith et al](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2005-6-5-r46)-->.

In the field of Biology and Biomedicine, the [OBO Foundry](http://obofoundry.org) coordinates the development of interoperable ontologies. At the core (URL_TO_INSERT_RECORD-ABBREV_2058 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD-NAME_2059 https://fairsharing.org/FAIRsharing.xMmOCL)  of this interoperation lies the **[Relation Ontology](http://www.obofoundry.org/ontology/ro.html)** released under the [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) license.

| Relation Ontology               | File  | Variant                                                                        |
|---------------------------------|---|--------------------------------------------------------------------------------|
| Relation Ontology               | [ro.owl](http://purl.obolibrary.org/obo/ro.owl)  | Canonical edition                                                              |
| Relation Ontology in obo format | [ro.obo](http://purl.obolibrary.org/obo/ro.obo)  | Has imports merged in                                                          |
| RO (URL_TO_INSERT_RECORD-ABBREV_2061 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD-ABBREV_2062 https://fairsharing.org/FAIRsharing.cp0ybc)  (URL_TO_INSERT_RECORD-ABBREV_2063 https://fairsharing.org/FAIRsharing.504c6c)  Core (URL_TO_INSERT_RECORD-NAME_2060 https://fairsharing.org/FAIRsharing.xMmOCL)  relations               | [ro/core.owl](http://purl.obolibrary.org/obo/ro/core.owl)  | Minimal subset intended to work with BFO-classes [page](https://github.com/oborel/obo-relations/wiki/ROCore)                        |
| RO (URL_TO_INSERT_RECORD-ABBREV_2064 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD-ABBREV_2066 https://fairsharing.org/FAIRsharing.cp0ybc)  (URL_TO_INSERT_RECORD-ABBREV_2068 https://fairsharing.org/FAIRsharing.504c6c)  base ontology                | [ro/ro-base.owl](http://purl.obolibrary.org/obo/ro/ro-base.owl)  | Axioms defined within RO (URL_TO_INSERT_RECORD-ABBREV_2065 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD-ABBREV_2067 https://fairsharing.org/FAIRsharing.cp0ybc)  (URL_TO_INSERT_RECORD-ABBREV_2069 https://fairsharing.org/FAIRsharing.504c6c)  and to be used in imports for other ontologies [page](https://github.com/INCATools/ontology-development-kit/issues/50) |
| Interaction relations           | [ro/subsets/ro-interaction.owl](http://purl.obolibrary.org/obo/ro/subsets/ro-interaction.owl)  |                                                                                |
| Ecology subset                  | [ro/subsets/ro-eco.owl](http://purl.obolibrary.org/obo/ro/subsets/ro-eco.owl)  | For use in ecology and environmental science                                   |
| Neuroscience subset             | [ro/subsets/ro-neuro.owl](http://purl.obolibrary.org/obo/ro/subsets/ro-neuro.owl)  | For use in neuroscience [page](http://bioinformatics.oxfordjournals.org/content/28/9/1262.long) 

As `knowledge graphs` and `property graphs` gain importance, we can expect the range and depth of relations to mature and expand as more expressivity is needed and progress is made by reasoner technology to fully exploit their benefits.
This would also have to be placed in the context of advances in `Text Mining` and `Machine Learning`, where unsupervised methods start to demonstrate strong potential to detect relations between entities.

The following is an example of how a `defined class` may be created in an ontology. The code snippet shows one such class being expressed to create a type by specifying a number of `axioms`. These use `relations` (aka OWL (URL_TO_INSERT_RECORD-ABBREV_2070 https://fairsharing.org/FAIRsharing.atygwy)  Properties), which may be set to 

```bash
'B cell, CD19-positive'
equivalentClass :
    'lymphocyte of B lineage, CD19-positive' 
    and ( 'has plasma membrane part' some 'CD19 molecule') 
    and ( 'in taxon' some Mammalia) 
    and ( 'capable of' some 'B cell mediated immunity')
```

Any class satisfying these patterns may be classified by an OWL (URL_TO_INSERT_RECORD-ABBREV_2071 https://fairsharing.org/FAIRsharing.atygwy)  reasoner as a child of that class. So the following class, with such properties that they all satisfy the requirements of the `defined class` declared above (e.g. "Homo sapiens" is_a type of "Mammalia", etc...), will be classified automatically (i.e. without human intervention) by a reasoner such as ELK or Hermit as a child of 'B cell, CD19-positive' .

```bash
'human B cell, CD19-positive'
Class:
    ( 'has plasma membrane part' some 'B-lymphocyte antigen CD19 isoform h2')
    and ( 'in taxon' some 'Homo sapiens') 
    and ( 'capable of' some 'B cell tolerance induction in mucosal-associated lymphoid tissue')

```

The notion is important to grasp as it also explains why not all ontologies are compatible, because they may significantly differ in the underlying axioms they rely on to establish their hierarchies using reasoners.



## Conclusions

> Selecting semantic resources depends on many different factors. However, the most important factor remains the `context` of the data and associated landscape of data standards as well as the ultimate integration goal, which will dictate the final choice.
> 
>The selection process remains guided by the need to maximize the potential of data integration with datasets of similar nature and similar value. It also requires a good understanding of the technical and sometimes legal implications these choices will have.

<!-- 
TODO : fill in the links to what-should-I-read-next recipes -->

### What to read next?

* How to build an application ontology? {ref}`fcb-interop-ontorobot`
* How to select on ontology service? {ref}`fcb-select-onto-service`
* How to deploy an ontology server? {ref}`fcb-select-onto-service-criteria`
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
