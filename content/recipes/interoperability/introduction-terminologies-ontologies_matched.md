(fcb-introduction-terminologies (URL_TO_INSERT_TERM_6162 https://fairsharing.org/search?recordType=terminology_artefact) -ontologies (URL_TO_INSERT_TERM_6163 https://fairsharing.org/search?recordType=terminology_artefact) )=
# Introduction to terminologies and ontologies


````{panels_fairplus}
:identifier_text: FCB019
:identifier_link: https://w3id.org/faircookbook/FCB019
:difficulty_level: 2
:recipe_type: survey_review
:reading_time_minutes: 15
:intended_audience: data_curator, data_manager, data_scientist  
:maturity_level: 0
:maturity_indicator: 0
:has_executable_code: nope
:recipe_name: Introducing terminologies and ontologies
```` 

## Main objectives

The aim of this recipe is to provide a compact introduction about `controlled terminologies (URL_TO_INSERT_TERM_6164 https://fairsharing.org/search?recordType=terminology_artefact) ` and `ontologies (URL_TO_INSERT_TERM_6165 https://fairsharing.org/search?recordType=terminology_artefact) `, why these resources are central to the preservation of knowledge and data mining and how such resources are developed (URL_TO_INSERT_RECORD_6166 https://fairsharing.org/FAIRsharing.31385c) .


## Controlled terminology or ontology: what's the difference?

The need for `controlled vocabulary` often arises in situations where validation of textual informat (URL_TO_INSERT_TERM_6167 https://fairsharing.org/search?recordType=model_and_format) ion is necessary 
for operational requirements. 
The main initial driver for data entry harmonization is to increase query recall. 
In its most basic form, `keywords` may be used to perform indexation. 
However, if relying on user input alone, the chances of typographic errors increases with the number of users. 
These unavoidable events accumulate over time and end up  hurting the accuracy of search (URL_TO_INSERT_RECORD_6168 https://fairsharing.org/FAIRsharing.52b22c)  results and this is the reason
for offering sets of predefined values. It reduces the noise. 
However, this can come at the cost of precision, as the predefined terms may not cover the exact thing users 
may need to describe. 
Furthermore, term mis-selection by the user is not eliminated and introduces another type of error.

A `controlled terminology (URL_TO_INSERT_TERM_6171 https://fairsharing.org/search?recordType=terminology_artefact) ` is a *`normative`* collection (URL_TO_INSERT_TERM_6169 https://fairsharing.org/search?recordType=collection)  of terms, the spelling of which is fixed and for which additional informat (URL_TO_INSERT_TERM_6170 https://fairsharing.org/search?recordType=model_and_format) ion may be provided such as a `definition`, a set of `synonyms`, an `editor`, a `version`, as well as a `license` determining the condition of use. 
The set of informat (URL_TO_INSERT_TERM_6172 https://fairsharing.org/search?recordType=model_and_format) ion about a specific controlled terminology (URL_TO_INSERT_TERM_6173 https://fairsharing.org/search?recordType=terminology_artefact)  term is designated as `term metadata`. 
In a controlled terminology (URL_TO_INSERT_TERM_6174 https://fairsharing.org/search?recordType=terminology_artefact) , terms appear as a `flat list`, meaning that no relationship between any of the entities the controlled terminology (URL_TO_INSERT_TERM_6175 https://fairsharing.org/search?recordType=terminology_artefact)  represents is captured in any formal way.
This is the main drawback and limitation of `controlled terminologies (URL_TO_INSERT_TERM_6177 https://fairsharing.org/search?recordType=terminology_artefact) `, which are often developed (URL_TO_INSERT_RECORD_6178 https://fairsharing.org/FAIRsharing.31385c)  to support a data model (URL_TO_INSERT_TERM_6176 https://fairsharing.org/search?recordType=model_and_format)  or an application.

An `ontology (URL_TO_INSERT_TERM_6179 https://fairsharing.org/search?recordType=terminology_artefact) ` on the other hand, is a `formal representation of a domain knowledge where concepts are organized hierarch (URL_TO_INSERT_RECORD_6180 https://fairsharing.org/FAIRsharing.52b22c) ically`.
The qualifier `formal` refers to a set of axioms and rules based on logic (e.g. `first order logic`) to structure,
organize and check the consistency of the term hierarch (URL_TO_INSERT_RECORD_6181 https://fairsharing.org/FAIRsharing.52b22c) y. 
As one can sense right away, ontologies (URL_TO_INSERT_TERM_6182 https://fairsharing.org/search?recordType=terminology_artefact)  are often a more sophisticated artefact, supported by more advanced theoretical frameworks and dedicated tools to develop them (e.g. Protégé, TopBraid Composer, OBO foundry (URL_TO_INSERT_RECORD_6183 https://fairsharing.org/FAIRsharing.847069)  INCAtools or Robot tool).


    
## How are they built and maintained and why does it matter?

In order to improve over simple `controlled terminologies (URL_TO_INSERT_TERM_6184 https://fairsharing.org/search?recordType=terminology_artefact) `, a huge area of research (URL_TO_INSERT_RECORD_6186 https://fairsharing.org/FAIRsharing.52b22c)  has developed (URL_TO_INSERT_RECORD_6188 https://fairsharing.org/FAIRsharing.31385c)  to provide `tools` and `frameworks` supporting the representations of relationships between entities. The field is known as `formal semantics` in knowledge representation circles. One of the most immediately available examples of `entity relationships` found in ontologies (URL_TO_INSERT_TERM_6185 https://fairsharing.org/search?recordType=terminology_artefact) , and their potential for improving search (URL_TO_INSERT_RECORD_6187 https://fairsharing.org/FAIRsharing.52b22c) es, is the `is_a` relationship, which aims to cover the Parent/Child relationship that holds between two entities. For instance:
```
-Vertebrate
--Mammal
---Dolphin
--Bird
---Pigeon
```
In this representation, `classes` are *directly* asserted (placed) under a parent class if and only if the rule `new class is a child of the parent Class` holds. 'Orchid', which in this hierarch (URL_TO_INSERT_RECORD_6189 https://fairsharing.org/FAIRsharing.52b22c) y, would not be nested under 'Vertebrate'.

While working on small structured vocabularies, it is still possible to detect potential errors but this approach does not scale to support real life semantic artefacts which support complex biological and biomedical informat (URL_TO_INSERT_TERM_6190 https://fairsharing.org/search?recordType=model_and_format) ion systems. 
Languages such as [RDF](https://www.w3.org/TR/2014/NOTE-rdf11-primer-20140624/), [SKOS](https://www.w3.org/2004/02/skos/), and [OWL](https://www.w3.org/OWL/), exist to provide the expressivity required to establish relations between entities.
In turn, building on these formal rules, automatic classifiers, known as a `reasoner`, can inspect semantic artefacts to detect inconsistencies and suggest parent classes. 
This is a step known as `inference`, where new knowledge is produced by the software agent rather than direct assertion by humans.
This provides a significant support, even if far from supporting all the subtleties of actual knowledge.

There are `six important features` to consider when selecting a semantic artefact for making FAIR (URL_TO_INSERT_RECORD_6191 https://fairsharing.org/FAIRsharing.WWI10U)  datasets:

1. **What license and terms of use does it mandate?**

1. **What format (URL_TO_INSERT_TERM_6192 https://fairsharing.org/search?recordType=model_and_format)  does it come in?**

1. **Is it well maintained, i.e. frequent release, term requests handling, versioning and deprecation policies (URL_TO_INSERT_TERM_6193 https://fairsharing.org/search?fairsharingRegistry=Policy)  clarified?**

1. **Are there stable persistent resolvable identifier (URL_TO_INSERT_TERM_6194 https://fairsharing.org/search?recordType=identifier_schema) s for all terms?**

1. **Who use it and what resources are being annotated with it?**

1. **Is it well documented?  There should be enough metadata for each class in the artefact and enough metadata about the artefact itself.**
    
## Why are they useful?

As outlined in the introduction, the most immediate use for a controlled terminology (URL_TO_INSERT_TERM_6195 https://fairsharing.org/search?recordType=terminology_artefact)  is to ensure consistency in data entry. Controlled terminologies (URL_TO_INSERT_TERM_6196 https://fairsharing.org/search?recordType=terminology_artefact)  are important tools to improve data indexing and query recall. 
The usefulness of ontologies (URL_TO_INSERT_TERM_6197 https://fairsharing.org/search?recordType=terminology_artefact)  and controlled vocabularies goes beyond this initial use.
The main purpose of biomedical ontologies (URL_TO_INSERT_TERM_6198 https://fairsharing.org/search?recordType=terminology_artefact)  is to structure knowledge so that it can be operated on by software agents.

One needs to also understand that the two processes coexist and operate in parallel. 
As more experiments are performed, new discoveries are made.
This new knowledge needs to be represented in the domain ontology (URL_TO_INSERT_TERM_6199 https://fairsharing.org/search?recordType=terminology_artefact)  so the new notions can be used to annotate the results of earlier experiments in the context of retrospective analysis.

For example, he [Gene Ontology (URL_TO_INSERT_TERM_6200 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_6202 https://fairsharing.org/FAIRsharing.6xq0ee)  (GO)](http://www.obofoundry.org (URL_TO_INSERT_RECORD_6201 https://fairsharing.org/FAIRsharing.847069) /ontology/go.html) is a widely used resource to describe `Molecular Processes`, `Biological Functions` and `Molecular Components`. 
The [Gene Ontology (URL_TO_INSERT_TERM_6203 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_6205 https://fairsharing.org/FAIRsharing.6xq0ee)  Consortium](http://geneontology.org (URL_TO_INSERT_RECORD_6207 https://fairsharing.org/FAIRsharing.h4rs6h) /docs/go-consortium/) maintains the controlled vocabulary and also releases of Genome Wide [Gene Ontology (URL_TO_INSERT_TERM_6204 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_6206 https://fairsharing.org/FAIRsharing.6xq0ee)  Annotations](http://geneontology.org (URL_TO_INSERT_RECORD_6208 https://fairsharing.org/FAIRsharing.h4rs6h) /docs/go-annotations/).
These are resources which associate genes and genomic features found in those genomes with GO (URL_TO_INSERT_RECORD_6209 https://fairsharing.org/FAIRsharing.6xq0ee)  terms. These are very important resources especially in the context of genome wide analysis such as transcriptomics profiling analysis.

A particular type of analysis, [`enrichment analysis`](http://geneontology.org (URL_TO_INSERT_RECORD_6210 https://fairsharing.org/FAIRsharing.h4rs6h) /docs/go-enrichment-analysis/), relies on the availability of such annotations to detect departures from the expected probability distribution in an expression profile and which biological processes are most affected in specific conditions.

The applications are plentiful. The importance of ontologies (URL_TO_INSERT_TERM_6212 https://fairsharing.org/search?recordType=terminology_artefact)  for structuring informat (URL_TO_INSERT_TERM_6211 https://fairsharing.org/search?recordType=model_and_format) ion will only grow with the need to obtain Machine Learning ready datasets and speed up the readiness of datasets. This is what FAIR (URL_TO_INSERT_RECORD_6213 https://fairsharing.org/FAIRsharing.WWI10U)  is all about.

So ontologies (URL_TO_INSERT_TERM_6214 https://fairsharing.org/search?recordType=terminology_artefact)  are of particularly help for the following tasks:
- **Improve query recall:** Given a 'search (URL_TO_INSERT_RECORD_6215 https://fairsharing.org/FAIRsharing.52b22c)  string (URL_TO_INSERT_RECORD_6217 https://fairsharing.org/FAIRsharing.9b7wvk) ', having a resource which holds synonyms can be used by a search (URL_TO_INSERT_RECORD_6216 https://fairsharing.org/FAIRsharing.52b22c)  index to retrieve data annotated with a synonym.
- **Enable query expansion:** Owing to the hierarch (URL_TO_INSERT_RECORD_6222 https://fairsharing.org/FAIRsharing.52b22c) ical (parent/child) structure of ontologies (URL_TO_INSERT_TERM_6220 https://fairsharing.org/search?recordType=terminology_artefact) , a search (URL_TO_INSERT_RECORD_6223 https://fairsharing.org/FAIRsharing.52b22c)  index exploiting this informat (URL_TO_INSERT_TERM_6218 https://fairsharing.org/search?recordType=model_and_format) ion can retrieve all datasets annotated with a child term of items matching the input search (URL_TO_INSERT_RECORD_6224 https://fairsharing.org/FAIRsharing.52b22c)  string (URL_TO_INSERT_RECORD_6228 https://fairsharing.org/FAIRsharing.9b7wvk) . For example, search (URL_TO_INSERT_RECORD_6225 https://fairsharing.org/FAIRsharing.52b22c) ing with the string (URL_TO_INSERT_RECORD_6229 https://fairsharing.org/FAIRsharing.9b7wvk)  "breast cancer" againts an ontology (URL_TO_INSERT_TERM_6219 https://fairsharing.org/search?recordType=terminology_artefact)  aware search (URL_TO_INSERT_RECORD_6226 https://fairsharing.org/FAIRsharing.52b22c)  index could return records annotated with `Paget's Disease` or `ductal carcinoma in-situ (DC (URL_TO_INSERT_RECORD_6221 https://fairsharing.org/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD_6227 https://fairsharing.org/3547) IS)`, both of which are types of mammary gland malignancies.
- **Build knowledge graphs:** Ontology (URL_TO_INSERT_TERM_6232 https://fairsharing.org/search?recordType=terminology_artefact)  languages can be used to represent domain knowledge and build reference terminologies (URL_TO_INSERT_TERM_6231 https://fairsharing.org/search?recordType=terminology_artefact)  but the same technologies constitute powerful tools for model (URL_TO_INSERT_TERM_6230 https://fairsharing.org/search?recordType=model_and_format) ling instance datasets as nodes in a graph and linking resources together.



## Are all ontologies compatible with each other?

There is not a simple answer to that question as it depends heavily on the type of tasks data scientists have in mind.
If the purpose is simply to improve query recall on a limited set of fields, a curation policy (URL_TO_INSERT_TERM_6233 https://fairsharing.org/search?fairsharingRegistry=Policy)  could be devised to mix and match resources to meet the needs at hands, possibly by building an application ontology (URL_TO_INSERT_TERM_6234 https://fairsharing.org/search?recordType=terminology_artefact) , i.e. an ontology (URL_TO_INSERT_TERM_6235 https://fairsharing.org/search?recordType=terminology_artefact)  specifically for designed for the use case with terms drawn from existing ontologies (URL_TO_INSERT_TERM_6236 https://fairsharing.org/search?recordType=terminology_artefact) .

However, in a more integrated framework, it is important to be aware of some of the development choices made by the maintainers of the semantic artefacts.


* **In the context of basic research (URL_TO_INSERT_RECORD_6241 https://fairsharing.org/FAIRsharing.52b22c)  and model (URL_TO_INSERT_TERM_6237 https://fairsharing.org/search?recordType=model_and_format)  organism based research (URL_TO_INSERT_RECORD_6242 https://fairsharing.org/FAIRsharing.52b22c) **, the **`OBO foundry (URL_TO_INSERT_RECORD_6239 https://fairsharing.org/FAIRsharing.847069) `** is an organization which coordinates the development of interoperable resources. GO (URL_TO_INSERT_RECORD_6240 https://fairsharing.org/FAIRsharing.6xq0ee) , mentioned earlier is one of them. The establishment of domain specific reference ontologies (URL_TO_INSERT_TERM_6238 https://fairsharing.org/search?recordType=terminology_artefact)  sharing the same underlying rules means that some level of compositional development can be done. This means that axioms can be built connecting classes from compatible resources.
This point becomes particularly important when considering the role of the `reasoner` when assessing and checking the consistency of artefacts themselves but also when analysing instance datasets themselves.

* **In the context of observation studies**, the Observational Medical Outcomes Partnership ([OMOP](https://ohdsi.org/omop/)) model (URL_TO_INSERT_TERM_6243 https://fairsharing.org/search?recordType=model_and_format)  also relies on controled terminologies (URL_TO_INSERT_TERM_6244 https://fairsharing.org/search?recordType=terminology_artefact)  such as [SNOMED-CT](https://www.snomed.org/snomed-ct/), [RxNORM](https://www.nlm.nih.gov/research/umls/rxnorm (URL_TO_INSERT_RECORD_6246 https://fairsharing.org/FAIRsharing.36pf8q) /index.html) for drugs and [LOINC](https://loinc.org (URL_TO_INSERT_RECORD_6245 https://fairsharing.org/FAIRsharing.2mk2zb) /) for clinical and laboratory test descriptions.

* **In the context of Clinical Data collection (URL_TO_INSERT_TERM_6248 https://fairsharing.org/search?recordType=collection) s**, the Clinical Data Interchange Standard (URL_TO_INSERT_TERM_6247 https://fairsharing.org/search?fairsharingRegistry=Standard) s Consortium ([CDISC](https://www.cdisc.org (URL_TO_INSERT_RECORD_6256 https://fairsharing.org/3525) /)) model (URL_TO_INSERT_TERM_6249 https://fairsharing.org/search?recordType=model_and_format) s work tightly with [CDI (URL_TO_INSERT_RECORD_6252 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_6255 https://fairsharing.org/3525)  Terminology](https://www.cdisc.org (URL_TO_INSERT_RECORD_6257 https://fairsharing.org/3525) /standards/terminology (URL_TO_INSERT_RECORD_6251 https://fairsharing.org/FAIRsharing.szrmev) /controlled-terminology), National Cancer Institute's Enterprise Vocabulary Services ([EVS](https://evs.nci.nih.gov/)) and also recommend use of [SNOMED-CT](https://www.snomed.org/snomed-ct/) and terminologies (URL_TO_INSERT_TERM_6250 https://fairsharing.org/search?recordType=terminology_artefact)  such as [LOINC](https://loinc.org (URL_TO_INSERT_RECORD_6254 https://fairsharing.org/FAIRsharing.2mk2zb) /), both of which come with specific licensing terms users need to be fam (URL_TO_INSERT_RECORD_6253 https://fairsharing.org/FAIRsharing.d0886a) iliar with.


### Use cases and iterative approach  


The use and implementation of common terminologies (URL_TO_INSERT_TERM_6259 https://fairsharing.org/search?recordType=terminology_artefact)  will enable a normalization/harmonization of variable labels (data label) and allowed values (data term) when querying a database (URL_TO_INSERT_TERM_6258 https://fairsharing.org/search?fairsharingRegistry=Database) . Implementing the use of common terminologies (URL_TO_INSERT_TERM_6260 https://fairsharing.org/search?recordType=terminology_artefact)  in the curation workflow will ensure consistency of the annotation across all studies.



### Selection criteria

A set of widely accepted criteria for selecting terminologies (URL_TO_INSERT_TERM_6264 https://fairsharing.org/search?recordType=terminology_artefact)  (or other reporting standard (URL_TO_INSERT_TERM_6261 https://fairsharing.org/search?fairsharingRegistry=Standard) s) does not exists. However, the initial work by the Clinical and Translational Science Awards’ (CTSA) Omics Data Standard (URL_TO_INSERT_TERM_6262 https://fairsharing.org/search?fairsharingRegistry=Standard) s Working Group and FAIR (URL_TO_INSERT_RECORD_6267 https://fairsharing.org/FAIRsharing.WWI10U) S (URL_TO_INSERT_RECORD_6265 https://fairsharing.org/FAIRsharing.f43996)  (URL_TO_INSERT_RECORD_6268 https://fairsharing.org/FAIRsharing.vajn3f) haring (URL_TO_INSERT_RECORD_6266 https://fairsharing.org/FAIRsharing.2abjs5)  ([http://jamia.bmj.com/content/early/2013/10/03/amiajnl-2013-002066.long](http://jamia.bmj.com/content/early/2013/10/03/amiajnl-2013-002066.long)) has been used as starting point to define possible criteria for excluding and/or including a terminology (URL_TO_INSERT_TERM_6263 https://fairsharing.org/search?recordType=terminology_artefact)  resource.


*   **Exclusion criteria**:
    * 🔸 Absent licence or terms of use (_indicator of usability_)
    * 🔸 Restrictive licences or terms of use with restrictions on redistribution and reuse 
    * 🔸 Absence of term definitions 
    * 🔸 Absence of sufficient class metadata (_indicator of quality_)
    * 🔸 Absence of sustainability indicators (_absence of funding records_) 
 
*   **Inclusion criteria**:
    * 🔰  Scope and coverage meets the requirements of the concept identified
    * 🔰  Unique URI (URL_TO_INSERT_RECORD_6269 https://fairsharing.org/FAIRsharing.d261e1) , textual definition and IDs for each term
    * 🔰  Resource releases are versioned
    * 🔰  Size of resource (_indicator of coverage_)
    * 🔰  Number of classes and subclasses (_indicator of depth_)
    * 🔰  Number of terms having definitions and synonyms (_indicator of richness_)
    * 🔰  Presence of a help desk and contact point (_indicator of community support_)
    * 🔰  Presence of term submission tracker/issue tracker (_indicator of resource agility and capability to grow upon request_)
    * 🔰  Potential integrative nature of the resource (_as indicator of translational application potential_)
    * 🔰  Licensing informat (URL_TO_INSERT_TERM_6270 https://fairsharing.org/search?recordType=model_and_format) ion available (_as indicator of freedom to use_)
    * 🔰  Use of a top level ontology (URL_TO_INSERT_TERM_6271 https://fairsharing.org/search?recordType=terminology_artefact)  (_as indicator of a resource built for generic use_)
    * 🔰  Pragmatism (_as indicator of actual, current real life practice)_
    * 🔰  Possibility of collaborating: the resource accepts complaints/remarks that aim to fix or improve the terminology (URL_TO_INSERT_TERM_6272 https://fairsharing.org/search?recordType=terminology_artefact) , while the resource organisation commits to fix or improve the terminology (URL_TO_INSERT_TERM_6273 https://fairsharing.org/search?recordType=terminology_artefact)  in brief delays (one month after receipt?)

These criteria are simply indicative and need to be modulated depending on the `contexts` described in the introduction, as specific constraints (e.g. regulator (URL_TO_INSERT_RECORD_6274 https://fairsharing.org/FAIRsharing.ey49c6) y requirements) may take precedence over some of the criteria listed here. 

---

## Conclusions

Choosing an ontology (URL_TO_INSERT_TERM_6275 https://fairsharing.org/search?recordType=terminology_artefact)  and semantic resources is a complex issue, which requires careful consideration, taking into account the research (URL_TO_INSERT_RECORD_6277 https://fairsharing.org/FAIRsharing.52b22c)  context of the data production workflow and regulator (URL_TO_INSERT_RECORD_6276 https://fairsharing.org/FAIRsharing.ey49c6) y requirements that may apply. The choices made affect the integrative potential of a dataset as they influence the level of `interoperability`. 
Clearly, declaring the semantic resources used to annotate a dataset also influences the `findability` and `reusability` and it is good practice to do so as it allows potential users to gauge the amount of map (URL_TO_INSERT_RECORD_6278 https://fairsharing.org/FAIRsharing.53edcc) ping work that may be required to combine two datasets.

###  What to read next?
* {ref}`fcb-selecting-ontologies (URL_TO_INSERT_TERM_6279 https://fairsharing.org/search?recordType=terminology_artefact) `
* {ref}`fcb-interop-ontorequest`
* {ref}`fcb-interop-ontorobot`
* {ref}`fcb-interop-onto-op`

````{rdmkit_panel}
````

<!-- > * TODO: {ref}`fcb-find-biosolr` -->


## References
````{dropdown} **References**
1. RDF. https://www.w3.org/TR/2014/NOTE-rdf11-primer-20140624/
2. SKOS. https://www.w3.org/2004/02/skos/
3. OWL. https://www.w3.org/OWL/
4. Hermit. http://www.hermit-reasoner.com/
5. Elk. http://www.cs.ox.ac.uk/isg/tools/ELK/
6. OBO Foundry. http://obofoundry.org/
7. CDISC. https://www.cdisc.org/standards
8. CDISC Controlled Terminology. https://www.cdisc.org/standards/terminology
9. LOINC. https://loinc.org/
10. Gene Ontology. http://geneontology.org/
11. Protégé. https://protege.stanford.edu/
12. Topbraid composer. https://www.topquadrant.com/products/topbraid-composer/
13. INCAtools. https://github.com/INCATools
14. ROBOT. [R.C. Jackson, J.P. Balhoff, E. Douglass, N.L. Harris, C.J. Mungall, and J.A. Overton. ROBOT: A tool for automating ontology workflows. BMC Bioinformatics, vol. 20, July 2019.](https://doi.org/10.1186/s12859-019-3002-3)
````


## Authors

````{authors_fairplus}
Philippe: Writing - Original Draft
Alasdair: Writing - Review & Editing
````


## License

````{license_fairplus}
CC-BY-4.0
````



