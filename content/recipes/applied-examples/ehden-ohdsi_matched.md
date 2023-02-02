(fcb-ehden-ohdsi)=
# FAIRification of observational studies and databases: the EHDEN and OHDSI use case


````{panels_fairplus}
:identifier_text: FCB054
:identifier_link: 'https://w3id.org/faircookbook/FCB054'
:difficulty_level: 1
:recipe_type: applied_example
:reading_time_minutes: 15
:intended_audience: terminology_manager, data_manager, data_scientist, ontologist 
:maturity_level: 2 
:maturity_indicator: 1, 2
:has_executable_code: nope
:recipe_name: Enhancing discoverability of EHDEN OHDSI data with Schema.org markup
```` 


## Main objectives

In this recipe, an example will be described on how to make observational health database (URL_TO_INSERT_TERM_157 https://fairsharing.org/search?fairsharingRegistry=Database) s and observational studies
more Findable (notably the FAIR (URL_TO_INSERT_RECORD_159 https://fairsharing.org/FAIRsharing.WWI10U)  principles (URL_TO_INSERT_RECORD_158 https://fairsharing.org/FAIRsharing.WWI10U)  [F2](https://www.go-fair.org/fair-principles (URL_TO_INSERT_RECORD_160 https://fairsharing.org/FAIRsharing.WWI10U) /f2-data-described-rich-metadata/)
and [F4](https://www.go-fair.org/fair-principles (URL_TO_INSERT_RECORD_161 https://fairsharing.org/FAIRsharing.WWI10U) /f4-metadata-registered-indexed-searchable-resource/)) and
interoperability (principles [I1](https://www.go-fair.org/fair-principles (URL_TO_INSERT_RECORD_162 https://fairsharing.org/FAIRsharing.WWI10U) /i1-metadata-use-formal-accessible-shared-broadly-applicable-language-knowledge-representation/)
and [I2](https://www.go-fair.org/fair-principles (URL_TO_INSERT_RECORD_163 https://fairsharing.org/FAIRsharing.WWI10U) /i2-metadata-use-vocabularies-follow-fair-principles/)), by creating 
a metadata model (URL_TO_INSERT_TERM_164 https://fairsharing.org/search?recordType=model_and_format)  and a human and machine readable website for dissemination of these resources. 

The output of the [COVID-19](https://www.ohdsi.org/covid-19-updates) [study-a-thon](https://www.thehyve.nl/articles/studyathon-multidisciplinary-collaboration-in-biomedical-open-science) 
(a OHD (URL_TO_INSERT_RECORD_166 https://fairsharing.org/FAIRsharing.bg7bb6) SI community [initiative](https://www.ohdsi.org/88-hours), involving the IMI [EHDEN](https://ehden.eu) project (URL_TO_INSERT_TERM_165 https://fairsharing.org/search?recordType=project) ) 
held in March (URL_TO_INSERT_RECORD_167 https://fairsharing.org/FAIRsharing.52b22c)  2020, is used as proof-of-concept.


### Abbreviations

*   [EHDEN](https://ehden.eu): European Health Data & Evidence Network
*   ETL: Extract Transform Load
*   [JSON-LD](https://www.w3.org/TR/json-ld11): JSO (URL_TO_INSERT_RECORD_169 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_168 https://fairsharing.org/FAIRsharing.5bbab9)  - Linked Data
*   [OHDSI](https://www.ohdsi.org): Observational Health Data Sciences and Informat (URL_TO_INSERT_TERM_170 https://fairsharing.org/search?recordType=model_and_format) ics
*   [OMOP (URL_TO_INSERT_RECORD_173 https://fairsharing.org/FAIRsharing.mct09a)  CDM (URL_TO_INSERT_RECORD_172 https://fairsharing.org/FAIRsharing.qk984b) ](https://ohdsi.github.io/CommonDataModel): Observational Medical Outcomes Partnership Common Data Model (URL_TO_INSERT_TERM_171 https://fairsharing.org/search?recordType=model_and_format) 
*   [RDF](https://www.w3.org/TR/rdf-concepts): Resource Description Framework (URL_TO_INSERT_RECORD_174 https://fairsharing.org/FAIRsharing.p77ph9) 
*   [YAML](https://yaml.org): YAML Ain’t Markup Language (human-readable data-serialization language)


## Introduction

This recipe is based on work done on OMOP (URL_TO_INSERT_RECORD_176 https://fairsharing.org/FAIRsharing.mct09a)  Common Data Model (URL_TO_INSERT_TERM_175 https://fairsharing.org/search?recordType=model_and_format)  data as used during the Covid 19 Study-a-thon, a OHD (URL_TO_INSERT_RECORD_177 https://fairsharing.org/FAIRsharing.bg7bb6) SI
community initiative, organised in collaboration with the IMI EHDEN project (URL_TO_INSERT_TERM_178 https://fairsharing.org/search?recordType=project) . The background informat (URL_TO_INSERT_TERM_179 https://fairsharing.org/search?recordType=model_and_format) ion was previously
described in this [use case](https://fairtoolkit.pistoiaalliance.org/use-cases/fairifying-collaborative-research-on-real-world-data-the-hyve/)
on the Pistoia Alliance FAIR (URL_TO_INSERT_RECORD_180 https://fairsharing.org/FAIRsharing.WWI10U)  toolkit website, and also published in an EHDEN Deliverable, 
[D4.5 - Roadmap (URL_TO_INSERT_RECORD_181 https://fairsharing.org/FAIRsharing.53edcc)  for interoperability](https://zenodo.org/record/4474373). 
Briefly, the IMI2 EHDEN project (URL_TO_INSERT_TERM_182 https://fairsharing.org/search?recordType=project) 's main aim is to reduce the time to produce medical evidence for health outcomes 
research (URL_TO_INSERT_RECORD_183 https://fairsharing.org/FAIRsharing.52b22c)  and to do so, EHDEN has prioritized data harmonization at source.

However, data standard (URL_TO_INSERT_TERM_184 https://fairsharing.org/search?fairsharingRegistry=Standard) ization and harmonization does not necessarily equate with FAIR (URL_TO_INSERT_RECORD_185 https://fairsharing.org/FAIRsharing.WWI10U)  data 
(see for example this [article](https://www.thehyve.nl/articles/data-quality-with-fair-principles)). 
This is where the interaction with the IMI2 FAIR (URL_TO_INSERT_RECORD_187 https://fairsharing.org/FAIRsharing.WWI10U) plus project (URL_TO_INSERT_TERM_186 https://fairsharing.org/search?recordType=project)  can bring benefits.

The purpose of the present content is to highlight how to improve dataset Findability after the data harmonization
has taken place.

The methods described in this recipe are however generally applicable for observational health database (URL_TO_INSERT_TERM_188 https://fairsharing.org/search?fairsharingRegistry=Database) s and studies,
not just data in the OMOP (URL_TO_INSERT_RECORD_191 https://fairsharing.org/FAIRsharing.mct09a)  CDM (URL_TO_INSERT_RECORD_190 https://fairsharing.org/FAIRsharing.qk984b)  format (URL_TO_INSERT_TERM_189 https://fairsharing.org/search?recordType=model_and_format) .

In March (URL_TO_INSERT_RECORD_194 https://fairsharing.org/FAIRsharing.52b22c)  2020 the OHD (URL_TO_INSERT_RECORD_195 https://fairsharing.org/FAIRsharing.bg7bb6) SI community organized a [study-a-thon focussed on CO (URL_TO_INSERT_RECORD_192 https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD_193 https://fairsharing.org/FAIRsharing.thskvr) VID-19](https://www.ohdsi.org/ohdsi-news-updates/covid19-studyathon/),
which was aimed at addressing a number of key medical questions around CO (URL_TO_INSERT_RECORD_196 https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD_197 https://fairsharing.org/FAIRsharing.thskvr) VID-19, such as predicting hospitalization
and drug safety and effectiveness. For this purpose, a large collection (URL_TO_INSERT_TERM_199 https://fairsharing.org/search?recordType=collection)  of healthcare database (URL_TO_INSERT_TERM_198 https://fairsharing.org/search?fairsharingRegistry=Database) s around the world were
investigated. Many important digital assets were produced during the [study-a-thon](https://ohdsi.org/ohdsi-kicks-off-international-collaborative-to-generate-real-world-evidence-on-covid-19-with-virtual-study-a-thon/),
such as study protocols, database (URL_TO_INSERT_TERM_200 https://fairsharing.org/search?fairsharingRegistry=Database)  metadata and characterizations, study results, and publications. 

From the FAIR (URL_TO_INSERT_RECORD_202 https://fairsharing.org/FAIRsharing.WWI10U)  assessment performed in order to better understand the current state of FAIR (URL_TO_INSERT_RECORD_203 https://fairsharing.org/FAIRsharing.WWI10U) ness of studies and database (URL_TO_INSERT_TERM_201 https://fairsharing.org/search?fairsharingRegistry=Database) s
used in OHD (URL_TO_INSERT_RECORD_206 https://fairsharing.org/FAIRsharing.bg7bb6) SI and in the CO (URL_TO_INSERT_RECORD_204 https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD_205 https://fairsharing.org/FAIRsharing.thskvr) VID-19 study-a-thon in particular, it was found that there was room for improvement on both 
Findability and Reusability. Since increasing Findability was a common denominator for both studies and data sources, 
the main focus of the FAIR (URL_TO_INSERT_RECORD_207 https://fairsharing.org/FAIRsharing.WWI10U) ification was on developing structured metadata, specifically tailored for studies and data sources.

This recipe will describe a proof-of-concept that shows the step-by-step process of making resources more FAIR (URL_TO_INSERT_RECORD_208 https://fairsharing.org/FAIRsharing.WWI10U)  by:

*   Inventory and prioritisation of digital resources; 
*   Adding metadata to the resources using existing ontologies (URL_TO_INSERT_TERM_209 https://fairsharing.org/search?recordType=terminology_artefact)  and defining new entities to make them findable by humans and machines;
*   Creating a website for FAIR (URL_TO_INSERT_RECORD_210 https://fairsharing.org/FAIRsharing.WWI10U)  dissemination of selected digital resources.


## Tools

| Tool Name| capability|
|:--|:--|
|[Apache Jena RDF (URL_TO_INSERT_RECORD_212 https://fairsharing.org/FAIRsharing.p77ph9)  validator](https://jena.apache.org/)|RDF format (URL_TO_INSERT_TERM_211 https://fairsharing.org/search?recordType=model_and_format)  validators|
|[Rich Results Test for JSON-LD](https://search.google.com/test/rich-results)|RDF format (URL_TO_INSERT_TERM_213 https://fairsharing.org/search?recordType=model_and_format)  validators|
|[EMIF Catalogue (URL_TO_INSERT_RECORD_214 https://fairsharing.org/FAIRsharing.GeWcY6) ](https://emif-catalogue.eu (URL_TO_INSERT_RECORD_215 https://fairsharing.org/FAIRsharing.GeWcY6) /)|Database|
|[HUGO](https://gohugo.io/)|Static website generator|


## Table of Data Standards

| Data Format (URL_TO_INSERT_TERM_217 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_218 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_216 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
|  [JSON-LD](https://www.w3.org/TR/json-ld11/) |  [Schema.org (URL_TO_INSERT_RECORD_223 https://fairsharing.org/FAIRsharing.hzdzq8) ](https://schema.org (URL_TO_INSERT_RECORD_224 https://fairsharing.org/FAIRsharing.hzdzq8) ) and [Custom OHD (URL_TO_INSERT_RECORD_221 https://fairsharing.org/FAIRsharing.bg7bb6) SI extension](https://github.com (URL_TO_INSERT_RECORD_220 https://fairsharing.org/FAIRsharing.c55d5e) /thehyve/ohdsi-schemas/blob/master/models/ohdsi_model/ohdsi_semantic_model.ttl) to schema.org (URL_TO_INSERT_RECORD_222 https://fairsharing.org/FAIRsharing.hzdzq8)   | RDF (URL_TO_INSERT_RECORD_219 https://fairsharing.org/FAIRsharing.p77ph9)   |
| [YAML](https://yaml.org/spec/1.2/spec.html) | Custom HUGO (URL_TO_INSERT_RECORD_225 https://fairsharing.org/FAIRsharing.6xq0ee)  template | NA |


## Graphical Overview of the FAIRification Recipe Objectives

````{dropdown}
:open:
```{figure} ehden-ohdsi.md-figure0.mmd.png
---
name: ehden-ohdsi-figure0
alt: Recipe Steps
---
Recipe Steps
```
````


## Step-by-Step process

### Inventory and prioritization of digital resources

In order to start the FAIR (URL_TO_INSERT_RECORD_226 https://fairsharing.org/FAIRsharing.WWI10U) ification process of digital resources in OHD (URL_TO_INSERT_RECORD_227 https://fairsharing.org/FAIRsharing.bg7bb6) SI, it was important to take inventory of which 
kind of digital resources reside in the OHD (URL_TO_INSERT_RECORD_230 https://fairsharing.org/FAIRsharing.bg7bb6) SI ecosystem. Digital resources in OHD (URL_TO_INSERT_RECORD_231 https://fairsharing.org/FAIRsharing.bg7bb6) SI include for example the OMOP (URL_TO_INSERT_RECORD_229 https://fairsharing.org/FAIRsharing.mct09a)  CDM (URL_TO_INSERT_RECORD_228 https://fairsharing.org/FAIRsharing.qk984b)  
itself, the OMOP (URL_TO_INSERT_RECORD_234 https://fairsharing.org/FAIRsharing.mct09a)  Standard (URL_TO_INSERT_TERM_232 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabularies (URL_TO_INSERT_RECORD_233 https://fairsharing.org/FAIRsharing.658tcg) , studies, cohort definitions and many more. 
Each digital resource itself can consist of multiple (sub) digital resources, as shown in {numref}`ehden-ohdsi-figure1`.

````{dropdown}
:open:
```{figure} ehden-ohdsi.md-figure1.jpg
---
name: ehden-ohdsi-figure1
alt: Inventory and prioritization of digital resources
---
Inventory and prioritization of digital resources. Example of digital resources that are part of an OHD (URL_TO_INSERT_RECORD_235 https://fairsharing.org/FAIRsharing.bg7bb6) SI study (from [EHDEN D4.5](https://zenodo.org/record/4474373)).
```
````


Prioritization of initial digital resources to FAIR (URL_TO_INSERT_RECORD_236 https://fairsharing.org/FAIRsharing.WWI10U) ify was important, as the OHD (URL_TO_INSERT_RECORD_237 https://fairsharing.org/FAIRsharing.bg7bb6) SI ecosystem is quite extensive.
In light of the study-a-thon on CO (URL_TO_INSERT_RECORD_238 https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD_239 https://fairsharing.org/FAIRsharing.thskvr) VID-19 held in March (URL_TO_INSERT_RECORD_240 https://fairsharing.org/FAIRsharing.52b22c)  2020 by OHD (URL_TO_INSERT_RECORD_241 https://fairsharing.org/FAIRsharing.bg7bb6) SI and after a 
[community inventory](https://forums.ohdsi.org/t/implementing-the-fair-principles-in-the-ohdsi-approach-and-tools/10387),
studies and database (URL_TO_INSERT_TERM_242 https://fairsharing.org/search?fairsharingRegistry=Database) s were selected as relevant digital resources to FAIR (URL_TO_INSERT_RECORD_243 https://fairsharing.org/FAIRsharing.WWI10U) ify, as these are important resources for the
research (URL_TO_INSERT_RECORD_246 https://fairsharing.org/FAIRsharing.52b22c) ers studying observational health data on CO (URL_TO_INSERT_RECORD_244 https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD_245 https://fairsharing.org/FAIRsharing.thskvr) VID-19 and related topics. 


### Current status of database and study dissemination in OHDSI

**Database (URL_TO_INSERT_TERM_247 https://fairsharing.org/search?fairsharingRegistry=Database) s in OHD (URL_TO_INSERT_RECORD_248 https://fairsharing.org/FAIRsharing.bg7bb6) SI**

General sources that provide informat (URL_TO_INSERT_TERM_250 https://fairsharing.org/search?recordType=model_and_format) ion on observational health database (URL_TO_INSERT_TERM_249 https://fairsharing.org/search?fairsharingRegistry=Database) s that are conformed to the OMOP (URL_TO_INSERT_RECORD_252 https://fairsharing.org/FAIRsharing.mct09a)  CDM (URL_TO_INSERT_RECORD_251 https://fairsharing.org/FAIRsharing.qk984b)  are the
[data network page](https://www.ohdsi.org/web/wiki/doku.php?id=resources:2020_data_network), 
the [EMIF catalogue](https://emif-catalogue.eu (URL_TO_INSERT_RECORD_253 https://fairsharing.org/FAIRsharing.GeWcY6) /) and the [EHDEN Portal](https://portal.ehden.eu) (under development). 

The data network page of OHD (URL_TO_INSERT_RECORD_257 https://fairsharing.org/FAIRsharing.bg7bb6) SI shows some metadata on database (URL_TO_INSERT_TERM_254 https://fairsharing.org/search?fairsharingRegistry=Database) s converted to the OMOP (URL_TO_INSERT_RECORD_256 https://fairsharing.org/FAIRsharing.mct09a)  CDM (URL_TO_INSERT_RECORD_255 https://fairsharing.org/FAIRsharing.qk984b) .

The [EMIF catalogue](https://emif-catalogue.eu (URL_TO_INSERT_RECORD_259 https://fairsharing.org/FAIRsharing.GeWcY6) /) is developed (URL_TO_INSERT_RECORD_260 https://fairsharing.org/FAIRsharing.31385c)  by the European Medical Informat (URL_TO_INSERT_TERM_258 https://fairsharing.org/search?recordType=model_and_format) ion Framework (EMIF) and
enables publishing and sharing of metadata on health data sources. Different consortia implementing the OMOP (URL_TO_INSERT_RECORD_262 https://fairsharing.org/FAIRsharing.mct09a)  CDM (URL_TO_INSERT_RECORD_261 https://fairsharing.org/FAIRsharing.qk984b)  
disseminate metadata on database (URL_TO_INSERT_TERM_263 https://fairsharing.org/search?fairsharingRegistry=Database) s in this catalogue. The EHDEN Portal builds on technology from the EMIF catalogue and
further expands this with functionality to compare database (URL_TO_INSERT_TERM_264 https://fairsharing.org/search?fairsharingRegistry=Database) s and run studies in the network.

**Studies in OHD (URL_TO_INSERT_RECORD_265 https://fairsharing.org/FAIRsharing.bg7bb6) SI**

Studies are currently disseminated through [data.ohdsi.org](https://data.ohdsi.org/). This web page links to the study
results and [GitHub (URL_TO_INSERT_RECORD_267 https://fairsharing.org/FAIRsharing.c55d5e)  repositories (URL_TO_INSERT_TERM_266 https://fairsharing.org/search?recordType=repository)  of studies](https://github.com (URL_TO_INSERT_RECORD_268 https://fairsharing.org/FAIRsharing.c55d5e) /ohdsi-studies) that are performed in the OHD (URL_TO_INSERT_RECORD_269 https://fairsharing.org/FAIRsharing.bg7bb6) SI community.
The web application [data.ohdsi.org/OhdsiStudies](https://data.ohdsi.org/OhdsiStudies/) gives an overview of all studies
in OHD (URL_TO_INSERT_RECORD_270 https://fairsharing.org/FAIRsharing.bg7bb6) SI with some associated metadata, such as study status, study leads and relevant dates.


### Defining a (semantic) model for relevant metadata elements

To increase the findability we captured the structured and rich metadata, by developing a semantic model (URL_TO_INSERT_TERM_271 https://fairsharing.org/search?recordType=model_and_format)  in RDF (URL_TO_INSERT_RECORD_272 https://fairsharing.org/FAIRsharing.p77ph9)  for the
observational studies and database (URL_TO_INSERT_TERM_273 https://fairsharing.org/search?fairsharingRegistry=Database) s. The model (URL_TO_INSERT_TERM_275 https://fairsharing.org/search?recordType=model_and_format)  contained all relevant metadata elements for studies, database (URL_TO_INSERT_TERM_274 https://fairsharing.org/search?fairsharingRegistry=Database) s, as well
as persons associated with those studies and database (URL_TO_INSERT_TERM_276 https://fairsharing.org/search?fairsharingRegistry=Database) s. 

Model (URL_TO_INSERT_TERM_277 https://fairsharing.org/search?recordType=model_and_format) ling metadata elements in RDF (URL_TO_INSERT_RECORD_278 https://fairsharing.org/FAIRsharing.p77ph9)  has the advantage that the metadata elements are properly semantically described,
structured and linked. In addition, RDF (URL_TO_INSERT_RECORD_279 https://fairsharing.org/FAIRsharing.p77ph9)  is easily expandable and modifiable. 

The Turtle (URL_TO_INSERT_RECORD_282 https://fairsharing.org/FAIRsharing.3e194c)  serialization format (URL_TO_INSERT_TERM_280 https://fairsharing.org/search?recordType=model_and_format)  was chosen as the RDF (URL_TO_INSERT_RECORD_283 https://fairsharing.org/FAIRsharing.p77ph9)  format (URL_TO_INSERT_TERM_281 https://fairsharing.org/search?recordType=model_and_format) . Metadata elements were defined and map (URL_TO_INSERT_RECORD_284 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_285 https://fairsharing.org/FAIRsharing.31385c)  to 
[Schema.org (URL_TO_INSERT_RECORD_287 https://fairsharing.org/FAIRsharing.hzdzq8) ](http://schema.org (URL_TO_INSERT_RECORD_288 https://fairsharing.org/FAIRsharing.hzdzq8) ) types and properties. Schema.org (URL_TO_INSERT_RECORD_286 https://fairsharing.org/FAIRsharing.hzdzq8)  is a vocabulary that can be used to create structured
data on the internet and to make the data discoverable. 

Relevant Schema.org (URL_TO_INSERT_RECORD_290 https://fairsharing.org/FAIRsharing.hzdzq8)  types for studies and database (URL_TO_INSERT_TERM_289 https://fairsharing.org/search?fairsharingRegistry=Database) s included: 

*   [Dataset](https://schema.org (URL_TO_INSERT_RECORD_292 https://fairsharing.org/FAIRsharing.hzdzq8) /Dataset): represents a data file or database (URL_TO_INSERT_TERM_291 https://fairsharing.org/search?fairsharingRegistry=Database)  resulting from the study
*   [MedicalObservationalStudy](https://schema.org (URL_TO_INSERT_RECORD_293 https://fairsharing.org/FAIRsharing.hzdzq8) /MedicalObservationalStudy): main type that represents the medical study itself
*   [MedicalObservationalStudyDesign](https://schema.org (URL_TO_INSERT_RECORD_294 https://fairsharing.org/FAIRsharing.hzdzq8) /MedicalObservationalStudyDesign): provides details about the design of the study
*   [MedicalStudyStatus](https://schema.org (URL_TO_INSERT_RECORD_295 https://fairsharing.org/FAIRsharing.hzdzq8) /MedicalStudyStatus): provides the status of the study (although this is based on clinical trials, and observational studies will not use all statuses)
*   [MedicalCondition](https://schema.org (URL_TO_INSERT_RECORD_296 https://fairsharing.org/FAIRsharing.hzdzq8) /MedicalCondition): used to link the study to the specific medical condition(s) it covers
*   [Drug](https://schema.org (URL_TO_INSERT_RECORD_297 https://fairsharing.org/FAIRsharing.hzdzq8) /Drug): used to link the study to any pharmaceutical products it covers
*   [Organization](https://schema.org (URL_TO_INSERT_RECORD_298 https://fairsharing.org/FAIRsharing.hzdzq8) /Organization): represents an organization, such as a university
*   [Person](https://schema.org (URL_TO_INSERT_RECORD_300 https://fairsharing.org/FAIRsharing.hzdzq8) /Person): represents a person and is mainly used to indicate the authors of / research (URL_TO_INSERT_RECORD_299 https://fairsharing.org/FAIRsharing.52b22c) ers involved in the study

{numref}`ehden-ohdsi-figure-2` shows part of the relevant metadata elements in the model (URL_TO_INSERT_TERM_301 https://fairsharing.org/search?recordType=model_and_format) .

````{dropdown}
:open:
```{figure} ehden-ohdsi.md-figure2.jpg
---
name: ehden-ohdsi-figure-2
alt: Part of the metadata model (URL_TO_INSERT_TERM_302 https://fairsharing.org/search?recordType=model_and_format) . Here, each class (orange) and relationship is represented as a schema.org (URL_TO_INSERT_RECORD_304 https://fairsharing.org/FAIRsharing.hzdzq8)  concept. Literals (yellow) are data types, e.g integers or string (URL_TO_INSERT_RECORD_303 https://fairsharing.org/FAIRsharing.9b7wvk) s. 
---
Part of the metadata model (URL_TO_INSERT_TERM_305 https://fairsharing.org/search?recordType=model_and_format) . Here, each class (orange) and relationship is represented as a schema.org (URL_TO_INSERT_RECORD_307 https://fairsharing.org/FAIRsharing.hzdzq8)  concept. Literals (yellow) are data types, e.g integers or string (URL_TO_INSERT_RECORD_306 https://fairsharing.org/FAIRsharing.9b7wvk) s. 
```
````

RDF (URL_TO_INSERT_RECORD_309 https://fairsharing.org/FAIRsharing.p77ph9)  representation of two Schema.org (URL_TO_INSERT_RECORD_310 https://fairsharing.org/FAIRsharing.hzdzq8)  types, written in Turtle (URL_TO_INSERT_RECORD_308 https://fairsharing.org/FAIRsharing.3e194c) :

````{dropdown}
:open:
```
schema:MedicalObservationalStudy a owl:Class ;
       rdfs:isDefinedBy  
<https://health-lifesci.schema.org (URL_TO_INSERT_RECORD_311 https://fairsharing.org/FAIRsharing.hzdzq8) /MedicalObservationalStudy> ;
       rdfs:label  "MedicalObservationalStudy"@en ;
       rdfs:subClassOf schema:MedicalStudy .

schema:Drug a owl:Class ;
       rdfs:isDefinedBy  
<https://health-lifesci.schema.org (URL_TO_INSERT_RECORD_312 https://fairsharing.org/FAIRsharing.hzdzq8) /Drug> ;
       rdfs:label  "Drug"@en ;
       rdfs:subClassOf schema:Substance .
```
````

### OHDSI extension to Schema.org vocabulary

[Schema.org (URL_TO_INSERT_RECORD_314 https://fairsharing.org/FAIRsharing.hzdzq8) ](https://schema.org (URL_TO_INSERT_RECORD_315 https://fairsharing.org/FAIRsharing.hzdzq8) /) is a general purpose vocabulary for search (URL_TO_INSERT_RECORD_313 https://fairsharing.org/FAIRsharing.52b22c) ing entities on the internet, so metadata
elements specific for some OHD (URL_TO_INSERT_RECORD_316 https://fairsharing.org/FAIRsharing.bg7bb6) SI assets were not present. To be able to capture metadata as extensive as necessary,
custom types and properties had to be created. These included: 

*   Properties specific for OHD (URL_TO_INSERT_RECORD_317 https://fairsharing.org/FAIRsharing.bg7bb6) SI studies(e.g. study types and study use cases)
*   Database (URL_TO_INSERT_TERM_318 https://fairsharing.org/search?fairsharingRegistry=Database)  properties (e.g. database (URL_TO_INSERT_TERM_319 https://fairsharing.org/search?fairsharingRegistry=Database)  characteristics and population size) 
*   Author properties (e.g. GitHub (URL_TO_INSERT_RECORD_320 https://fairsharing.org/FAIRsharing.c55d5e)  handle (URL_TO_INSERT_RECORD_321 https://fairsharing.org/FAIRsharing.0b7e54)  and forum profile). 

The resulting metadata model (URL_TO_INSERT_TERM_323 https://fairsharing.org/search?recordType=model_and_format)  was shared in a public [GitHub (URL_TO_INSERT_RECORD_324 https://fairsharing.org/FAIRsharing.c55d5e)  repository (URL_TO_INSERT_TERM_322 https://fairsharing.org/search?recordType=repository) ](https://github.com (URL_TO_INSERT_RECORD_325 https://fairsharing.org/FAIRsharing.c55d5e) /thehyve/ohdsi-schemas/blob/d18a9a924cd13fc4525b5965e6ecb43c5d22a333/models/ohdsi_model/ohdsi_semantic_model.ttl).

For OHD (URL_TO_INSERT_RECORD_326 https://fairsharing.org/FAIRsharing.bg7bb6) SI specific types and properties the namespace [http://data.ohdsi.org/](http://data.ohdsi.org/) is used, using the `ohdsi` prefix. 

The RDF (URL_TO_INSERT_RECORD_328 https://fairsharing.org/FAIRsharing.p77ph9)  model (URL_TO_INSERT_TERM_327 https://fairsharing.org/search?recordType=model_and_format)  was validated using Apache Jena RIOT (version 3.15.0), using the following command:

```bash
riot.bat --validate ohdsi_semantic_model.ttl
```


### Metadata capture using YAML

In principle, the RDF (URL_TO_INSERT_RECORD_330 https://fairsharing.org/FAIRsharing.p77ph9)  classes defined in the above Turtle (URL_TO_INSERT_RECORD_329 https://fairsharing.org/FAIRsharing.3e194c)  file can directly be used to set up the JSO (URL_TO_INSERT_RECORD_332 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_331 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_333 https://fairsharing.org/FAIRsharing.8f9bbb)  file needed 
for the website metadata. But in this example, we used an extra step by first capturing the metadata of studies, 
database (URL_TO_INSERT_TERM_334 https://fairsharing.org/search?fairsharingRegistry=Database) s and authors, in the more data entry friendly YAML format (URL_TO_INSERT_TERM_335 https://fairsharing.org/search?recordType=model_and_format) . The YAML format (URL_TO_INSERT_TERM_336 https://fairsharing.org/search?recordType=model_and_format)  can be annotated with comments
to guide the person submitting their metadata. 

The following figure shows the metadata in Turtle (URL_TO_INSERT_RECORD_337 https://fairsharing.org/FAIRsharing.3e194c)  and in YAML. YAML uses slightly different wording and syntax, 
to make it easier for end users / science bloggers to understand what kind of metadata is expected to be filled in. 

In YAML, the data looks like this:

```yaml
# Study identifier, specifically created for the website.
# The identifier is the last part of the URL directing to the particular study
study_id: ‘Covid19Icarius’
# Analytics Use Case of the Study, choose 0, 1, 2 or 3:
# 0: Characterization
# 1: Population-Level Estimation
# 2: Patient-Level Prediction
# 3: Characterization and Population-Level Estimation
study_usecase: [1]
# Conditions studied; if multiple conditions are being studied,
# duplicate all keys under "conditions"
conditions:
- concept_name: "Disease caused by 2019-nCoV"
  concept_id: "37311061"
  code:
    concept_code: "840539006"
    vocabulary_id: "SNOMED CT"
    concept_code_url: "http://snomed.info/id/840539006"
# Drug studied; if multiple subjects are being studied,
# duplicate all keys under "study_subject"
study_subject:
- concept_name: "quinaprilat"
  concept_id: "45775375"
  code:
    concept_code: "1546359"
    vocabulary_id: "RxNorm"
    concept_code_url: "http://purl.bioontology.org/ontology/RXNORM/1546359"
```

The data in YAML gets converted into Turtle (URL_TO_INSERT_RECORD_338 https://fairsharing.org/FAIRsharing.3e194c)  programatically:

```text
@prefix ohdsi: <http://data.ohdsi.org/> .
@prefix concept: <http://data.ohdsi.org/concept/> .
@prefix study: <https://covid19.ohdsi.app/study/> .
@prefix schema: <http://schema.org/> .
study:Covid19Icarius a schema:MedicalObservationalStudy ;
ohdsi:analyticsUseCase ohdsi:PopulationLevelEstimation ;
schema:healthCondition concept:37311061 ;
schema:studySubject concept:45775375 .
concept:37311061 a schema:MedicalCondition ;
schema:name "Disease caused by 2019-nCoV" ;
schema:identifier "37311061" ;
schema:code [ a schema:MedicalCode ;
schema:codeValue "840539006" ;
schema:codingSystem "SNOMED CT" ;
schema:sameAs "http://snomed.info/id/840539006" ] .
concept:45775375 a schema:Drug ;
schema:name "quinaprilat" ;
schema:identifier "1777087" ;
schema:code [ a schema:MedicalCode ;
schema:codeValue “1546359" ;
schema:codingSystem "RxNorm" ;
schema:sameAs "http://purl.bioontology.org/ontology/RXNORM/“1546359" ] .
```

The Hugo backend that we created, reads in the study articles, including the YAML metadata, and produces an HTML (URL_TO_INSERT_RECORD_339 https://fairsharing.org/FAIRsharing.YugnuL)  output
from that which contains the article text but also embeds the entered metadata as JSO (URL_TO_INSERT_RECORD_341 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_340 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_342 https://fairsharing.org/FAIRsharing.8f9bbb)  
(see {numref}`ehden-ohdsi-figure3`). In order to do this, we have written custom processing logic that takes the YAML 
data as input and format (URL_TO_INSERT_TERM_344 https://fairsharing.org/search?recordType=model_and_format) s this into RDF (URL_TO_INSERT_RECORD_345 https://fairsharing.org/FAIRsharing.p77ph9)  in accordance with the metadata model (URL_TO_INSERT_TERM_343 https://fairsharing.org/search?recordType=model_and_format) .

````{dropdown}
:open:
```{figure} ehden-ohdsi.md-figure3.jpg
---
name: ehden-ohdsi-figure3
alt: Relationship between the use of Turtle (URL_TO_INSERT_RECORD_347 https://fairsharing.org/FAIRsharing.3e194c) , JSO (URL_TO_INSERT_RECORD_349 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_348 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_350 https://fairsharing.org/FAIRsharing.8f9bbb)  and YAML in this proof-of-concept project (URL_TO_INSERT_TERM_346 https://fairsharing.org/search?recordType=project) .
---
Relationship between the use of Turtle (URL_TO_INSERT_RECORD_352 https://fairsharing.org/FAIRsharing.3e194c) , JSO (URL_TO_INSERT_RECORD_354 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_353 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_355 https://fairsharing.org/FAIRsharing.8f9bbb)  and YAML in this proof-of-concept project (URL_TO_INSERT_TERM_351 https://fairsharing.org/search?recordType=project) .
```
````


### Embedding the metadata in the website as JSON-LD

JSO (URL_TO_INSERT_RECORD_361 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_360 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_362 https://fairsharing.org/FAIRsharing.8f9bbb)  is a format (URL_TO_INSERT_TERM_356 https://fairsharing.org/search?recordType=model_and_format)  for structured and linked data and, like Turtle (URL_TO_INSERT_RECORD_358 https://fairsharing.org/FAIRsharing.3e194c) , a serialization format (URL_TO_INSERT_TERM_357 https://fairsharing.org/search?recordType=model_and_format)  of RDF (URL_TO_INSERT_RECORD_359 https://fairsharing.org/FAIRsharing.p77ph9) . 

It can be embedded in the HTML (URL_TO_INSERT_RECORD_363 https://fairsharing.org/FAIRsharing.YugnuL)  code in the back end of a website. Search (URL_TO_INSERT_RECORD_364 https://fairsharing.org/FAIRsharing.52b22c)  engines like Google 
(including [Google dataset search](https://datasetsearch.research.google.com/)) use this structured data to find 
and understand the data. Understanding the data goes hand in hand with using the [Schema.org (URL_TO_INSERT_RECORD_365 https://fairsharing.org/FAIRsharing.hzdzq8) ](http://schema.org (URL_TO_INSERT_RECORD_366 https://fairsharing.org/FAIRsharing.hzdzq8) ) 
vocabulary, because annotating metadata with Schema.org (URL_TO_INSERT_RECORD_367 https://fairsharing.org/FAIRsharing.hzdzq8)  types and properties gives meaning to the data. 
This search (URL_TO_INSERT_RECORD_369 https://fairsharing.org/FAIRsharing.52b22c)  engine optimization (SEO (URL_TO_INSERT_RECORD_371 https://fairsharing.org/FAIRsharing.d1zzym) , see the [Search (URL_TO_INSERT_RECORD_370 https://fairsharing.org/FAIRsharing.52b22c)  Engine optimization recipe](https://w3id.org (URL_TO_INSERT_RECORD_368 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB010)) 
enables better Findability of the data.

For this proof-of-concept project (URL_TO_INSERT_TERM_372 https://fairsharing.org/search?recordType=project) , a website was created for dissemination of metadata on studies, 
database (URL_TO_INSERT_TERM_373 https://fairsharing.org/search?fairsharingRegistry=Database) s and authors, generated and used during the OHD (URL_TO_INSERT_RECORD_377 https://fairsharing.org/FAIRsharing.bg7bb6) SI CO (URL_TO_INSERT_RECORD_375 https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD_376 https://fairsharing.org/FAIRsharing.thskvr) VID-19 "study-a-thon". Metadata on studies, database (URL_TO_INSERT_TERM_374 https://fairsharing.org/search?fairsharingRegistry=Database) s and
authors is displayed on this [website](https://covid19.ohdsi.app/), and is embedded as JSO (URL_TO_INSERT_RECORD_379 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_378 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_380 https://fairsharing.org/FAIRsharing.8f9bbb)  in the HTML (URL_TO_INSERT_RECORD_381 https://fairsharing.org/FAIRsharing.YugnuL)  code as well.
<!-- TODO: Give example of a page with markup -->

Embedding metadata in JSO (URL_TO_INSERT_RECORD_383 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_382 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_384 https://fairsharing.org/FAIRsharing.8f9bbb)  in HTML (URL_TO_INSERT_RECORD_385 https://fairsharing.org/FAIRsharing.YugnuL)  will enable web crawlers to scrape the metadata and will increase Findability 
by search (URL_TO_INSERT_RECORD_386 https://fairsharing.org/FAIRsharing.52b22c)  engines. When for example querying 
[https://datasetsearch.research.google.com/](https://datasetsearch.research.google.com/),
the data should pop up when JSO (URL_TO_INSERT_RECORD_388 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_387 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_389 https://fairsharing.org/FAIRsharing.8f9bbb)  is embedded, but only when the `schema:Dataset` class is included
(see also the next section for details on this).


### Making a sitemap file and letting crawlers know

Setting up a `robots.txt` file at the root of a website will give search (URL_TO_INSERT_RECORD_390 https://fairsharing.org/FAIRsharing.52b22c)  engine crawlers a guide on which web pages can
be crawled, and which pages can’t be crawled. Crawling all pages is possible by adding this line to the `robots.txt` file:

```text
User-agent: *
```

The Hugo framework automatically generates a sitemap (URL_TO_INSERT_RECORD_391 https://fairsharing.org/FAIRsharing.53edcc)  when building a website 
(in this example: [https://covid19.ohdsi.app/sitemap.xml](https://covid19.ohdsi.app/sitemap.xml))

The generated JSO (URL_TO_INSERT_RECORD_393 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_392 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_394 https://fairsharing.org/FAIRsharing.8f9bbb)  files can be validated using [Google’s Rich Result Test](https://search.google.com/test/rich-results).
This tool can easily validate JSO (URL_TO_INSERT_RECORD_398 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_395 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_402 https://fairsharing.org/FAIRsharing.8f9bbb)  code, by either submitting a URL (URL_TO_INSERT_RECORD_401 https://fairsharing.org/FAIRsharing.9d38e2)  directing to the JSO (URL_TO_INSERT_RECORD_399 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_396 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_403 https://fairsharing.org/FAIRsharing.8f9bbb) , or by pasting JSO (URL_TO_INSERT_RECORD_400 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_397 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_404 https://fairsharing.org/FAIRsharing.8f9bbb)  code.
<!-- TODO give an example link to a page being validated -->

An important note to make here is that to make the data findable for Google Dataset search (URL_TO_INSERT_RECORD_406 https://fairsharing.org/FAIRsharing.52b22c)  the model (URL_TO_INSERT_TERM_405 https://fairsharing.org/search?recordType=model_and_format)  and final
JSO (URL_TO_INSERT_RECORD_408 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_407 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_409 https://fairsharing.org/FAIRsharing.8f9bbb)  markup needed to mention the `schema:Dataset` class. In a first iteration, we had used our new 
`ohdsi:database (URL_TO_INSERT_TERM_410 https://fairsharing.org/search?fairsharingRegistry=Database) ` class and the website was not found (even if the `ohdsi:database (URL_TO_INSERT_TERM_411 https://fairsharing.org/search?fairsharingRegistry=Database)  is-a schema:Dataset` statement from
the model (URL_TO_INSERT_TERM_412 https://fairsharing.org/search?recordType=model_and_format)  is repeated in the JSO (URL_TO_INSERT_RECORD_414 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_413 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_415 https://fairsharing.org/FAIRsharing.8f9bbb) ; 
Google's Schema.org (URL_TO_INSERT_RECORD_419 https://fairsharing.org/FAIRsharing.hzdzq8)  tools used a fixed context file, ignoring any additional statements included in your own JSO (URL_TO_INSERT_RECORD_417 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_416 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_418 https://fairsharing.org/FAIRsharing.8f9bbb) ).

To illustrate, the JSO (URL_TO_INSERT_RECORD_421 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_420 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_422 https://fairsharing.org/FAIRsharing.8f9bbb)  representation of metadata instantiation of the OHD (URL_TO_INSERT_RECORD_423 https://fairsharing.org/FAIRsharing.bg7bb6) SI Covid19 Icarius study looks like this in
JSO (URL_TO_INSERT_RECORD_427 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_426 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_428 https://fairsharing.org/FAIRsharing.8f9bbb)  (compare the metadata presented above in YAML and Turtle (URL_TO_INSERT_RECORD_425 https://fairsharing.org/FAIRsharing.3e194c)  format (URL_TO_INSERT_TERM_424 https://fairsharing.org/search?recordType=model_and_format) ):

```
{ "@graph" : [ 
     { "@id" : "study:Covid19Icarius",
       "@type" : "schema:MedicalObservationalStudy",
       "analyticsUseCase" : "ohdsi:PopulationLevelEstimation",
       "healthCondition" : "concept:37311061",
       "studySubject" : "concept:45775375"  },
    {
      "@id": "concept:37311061",
      "@type": "schema:MedicalCondition",
      "code": {
           "@type": "schema:MedicalCode",
           "codeValue": "840539006",S
           "codingSystem": "SNOMED",
           "sameAs": "http://snomed.info/id/840539006"
      },
      "identifier": "37311061",
      "name": "Disease caused by 2019-nCoV"
     },
   {
      "@id": "concept:45775375",
      "@type": "schema:Drug",
      "code": {
           "@type": "schema:MedicalCode",
           "codeValue": "1546359",
           "codingSystem": "RxNorm"
      },
      "identifier": "45775375",
      "name": "quinaprilat"
     }
   ],
 "@context" : {
     "analyticsUseCase" : {
          "@id" : "http://data.ohdsi.org/analyticsUseCase",
          "@type" : "@id" },
      "healthCondition" : {
          "@id" : "http://schema.org/healthCondition",
          "@type" : "@id"},
      "studySubject" : {
          "@id" : "http://schema.org/studySubject",
          "@type" : "@id" },
      "name" : {
          "@id" : "http://schema.org/name" },
      "identifier" : {
          "@id" : "http://schema.org/identifier" },
      "code" : {
          "@id" : "http://schema.org/code",
          "@type" : "@id" }}
}
```


### Generate final website version using HUGO

The static site generator [HUGO](https://gohugo.io/) was used to create the 
[covid19.ohdsi.app](https://covid19.ohdsi.app/) website. To populate the website with metadata, so-called
[archetypes](https://gohugo.io/content-management/archetypes/) were created. These arch (URL_TO_INSERT_RECORD_429 https://fairsharing.org/FAIRsharing.52b22c) etypes are content templates 
that use the YAML format (URL_TO_INSERT_TERM_430 https://fairsharing.org/search?recordType=model_and_format) , as the JSO (URL_TO_INSERT_RECORD_434 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_433 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_435 https://fairsharing.org/FAIRsharing.8f9bbb)  format (URL_TO_INSERT_TERM_431 https://fairsharing.org/search?recordType=model_and_format)  is not the easiest format (URL_TO_INSERT_TERM_432 https://fairsharing.org/search?recordType=model_and_format)  to enter data, to manually populate the static
website pages with metadata. Hence, these arch (URL_TO_INSERT_RECORD_436 https://fairsharing.org/FAIRsharing.52b22c) etype templates are used for metadata instantiation of the website. 
(see the previous sections of this recipe). 

Part of the content is populated automatically, by scraping informat (URL_TO_INSERT_TERM_437 https://fairsharing.org/search?recordType=model_and_format) ion from the 
[OHD (URL_TO_INSERT_RECORD_439 https://fairsharing.org/FAIRsharing.bg7bb6) SI forum](https://forums.ohdsi.org/) and [README files](https://github.com (URL_TO_INSERT_RECORD_438 https://fairsharing.org/FAIRsharing.c55d5e) /ohdsi-studies/StudyRepoTemplate) in the 
study-specific GitHub (URL_TO_INSERT_RECORD_444 https://fairsharing.org/FAIRsharing.c55d5e)  repositories (URL_TO_INSERT_TERM_440 https://fairsharing.org/search?recordType=repository) . The metadata in YAML is converted to JSO (URL_TO_INSERT_RECORD_442 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_441 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_443 https://fairsharing.org/FAIRsharing.8f9bbb)  in the back end of the website. 
In the front end of the website, this metadata is shown in a human-readable way. 

The source code of the website can be found on [https://github.com (URL_TO_INSERT_RECORD_445 https://fairsharing.org/FAIRsharing.c55d5e) /thehyve/ohdsi-covid19-site](https://github.com (URL_TO_INSERT_RECORD_446 https://fairsharing.org/FAIRsharing.c55d5e) /thehyve/ohdsi-covid19-site). 


### Final result

The final result of applying all these steps looks like this: an HTML (URL_TO_INSERT_RECORD_450 https://fairsharing.org/FAIRsharing.YugnuL)  page in the browser with JSO (URL_TO_INSERT_RECORD_448 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_447 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_449 https://fairsharing.org/FAIRsharing.8f9bbb)  metadata under
the hood. 
A screenshot of the HTML (URL_TO_INSERT_RECORD_451 https://fairsharing.org/FAIRsharing.YugnuL)  page is presented in {numref}`ehden-ohdsi-figure6`.

````{dropdown}
:open:
```{figure} ehden-ohdsi.md-figure6.png
---
name: ehden-ohdsi-figure6
alt: This screenshot shows the "study" view of the Hugo covid19 app, here the entry "covid19icarius" (https://covid19.ohdsi.app/study/covid19icarius/). The selected tab shows collapsed details sections, whereas the "JSO (URL_TO_INSERT_RECORD_454 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_452 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_456 https://fairsharing.org/FAIRsharing.8f9bbb) " tab would allow to see the corresponding JSO (URL_TO_INSERT_RECORD_455 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_453 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_457 https://fairsharing.org/FAIRsharing.8f9bbb)  for this record.
---
This screenshot shows the "study" view of the Hugo covid19 app, here the entry "covid19icarius" (https://covid19.ohdsi.app/study/covid19icarius/). The selected tab shows collapsed details sections, whereas the "JSO (URL_TO_INSERT_RECORD_460 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_458 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_462 https://fairsharing.org/FAIRsharing.8f9bbb) " tab would allow to see the corresponding JSO (URL_TO_INSERT_RECORD_461 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_459 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_463 https://fairsharing.org/FAIRsharing.8f9bbb)  for this record.
```
````

In the HTML (URL_TO_INSERT_RECORD_467 https://fairsharing.org/FAIRsharing.YugnuL)  page of the record, the HTML (URL_TO_INSERT_RECORD_468 https://fairsharing.org/FAIRsharing.YugnuL)  head element is augmented with a script element which embeds the same JSO (URL_TO_INSERT_RECORD_465 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_464 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_466 https://fairsharing.org/FAIRsharing.8f9bbb) 
informat (URL_TO_INSERT_TERM_469 https://fairsharing.org/search?recordType=model_and_format) ion payload and makes it available to search (URL_TO_INSERT_RECORD_470 https://fairsharing.org/FAIRsharing.52b22c)  engines’ crawlers.

Finally, with all this in place, one may now use the dedicated Google Dataset Search (URL_TO_INSERT_RECORD_471 https://fairsharing.org/FAIRsharing.52b22c)  site to discover new covid-related
datasets. {numref}`ehden-ohdsi-figure7` shows the ICARIUS dataset, which was highlighted in the previous sections, 
as indexed in Google Dataset Search (URL_TO_INSERT_RECORD_472 https://fairsharing.org/FAIRsharing.52b22c) .

````{dropdown}
:open:
```{figure} ehden-ohdsi.md-figure7.png
---
name: ehden-ohdsi-figure7
alt: The OHD (URL_TO_INSERT_RECORD_477 https://fairsharing.org/FAIRsharing.bg7bb6) SI covid19 datasets can be found in Google Dataset Search (URL_TO_INSERT_RECORD_476 https://fairsharing.org/FAIRsharing.52b22c) , because Google indexed the JSO (URL_TO_INSERT_RECORD_474 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_473 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_475 https://fairsharing.org/FAIRsharing.8f9bbb)  descriptions provided by the Hugo covid19 app. Highlighted is the ICARIUS study which was extensively discussed in this recipe. 
---
The OHD (URL_TO_INSERT_RECORD_482 https://fairsharing.org/FAIRsharing.bg7bb6) SI covid19 datasets can be found in Google Dataset Search (URL_TO_INSERT_RECORD_481 https://fairsharing.org/FAIRsharing.52b22c) , because Google indexed the JSO (URL_TO_INSERT_RECORD_479 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_478 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_480 https://fairsharing.org/FAIRsharing.8f9bbb)  descriptions provided by the Hugo covid19 app. Highlighted is the ICARIUS study which was extensively discussed in this recipe.
```
````

## Conclusion

The key reusable element in this recipe is the use of Schema.org (URL_TO_INSERT_RECORD_486 https://fairsharing.org/FAIRsharing.hzdzq8)  JSO (URL_TO_INSERT_RECORD_484 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_483 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_485 https://fairsharing.org/FAIRsharing.8f9bbb)  statements in any website to promote
findability of metadata in search (URL_TO_INSERT_RECORD_487 https://fairsharing.org/FAIRsharing.52b22c)  engines. Using the Hugo site generator has the advantage that it is very versatile
and includes a lot of scientific/blogging authoring tools out of the box. 
However, the particular implementation of using YAML as input format (URL_TO_INSERT_TERM_488 https://fairsharing.org/search?recordType=model_and_format)  (which is ‘canonical Hugo’) and converting this 
during the static website generation process to JSO (URL_TO_INSERT_RECORD_490 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_489 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_491 https://fairsharing.org/FAIRsharing.8f9bbb)  is quite laborious and also potentially introduces issues during
the conversion. Therefore, it is probably easier and more scalable to let the scientists write their metadata directly
in JSO (URL_TO_INSERT_RECORD_493 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_492 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_494 https://fairsharing.org/FAIRsharing.8f9bbb) , helped (URL_TO_INSERT_RECORD_495 https://fairsharing.org/FAIRsharing.31385c)  by some good examples and templates, and the Hugo software could even be extended to facilitate 
that as well.

Another next step that could be taken, besides publishing the JSO (URL_TO_INSERT_RECORD_497 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_496 https://fairsharing.org/FAIRsharing.5bbab9) -LD (URL_TO_INSERT_RECORD_498 https://fairsharing.org/FAIRsharing.8f9bbb)  metadata directly on the web, is to wrap it 
into a container such as [RO-CRATE](https://www.researchobject.org/ro-crate/) and publish these directly into a 
scientific artefact repository (URL_TO_INSERT_TERM_499 https://fairsharing.org/search?recordType=repository) . This would also help to sustain the availability of the data, because for all its
great properties, static websites only live as long as the web-host stays up, and the average website disappears after
a few years. 
Hosting the website on [IPFS](https://ipfs.io/) and using a pinning service could be yet another remedy to fix this
problem, but this is out of scope of this recipe.


### What to read next?

* Findability of data by search (URL_TO_INSERT_RECORD_501 https://fairsharing.org/FAIRsharing.52b22c)  engines: [Search (URL_TO_INSERT_RECORD_502 https://fairsharing.org/FAIRsharing.52b22c)  Engine Optimization](https://w3id.org (URL_TO_INSERT_RECORD_500 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB010) recipe,
describing web crawling, robots.txt, sitemap (URL_TO_INSERT_RECORD_503 https://fairsharing.org/FAIRsharing.53edcc) s and possible roadblocks.
* [Recipe](https://w3id.org (URL_TO_INSERT_RECORD_504 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB026) on how to create a metadata profile.
* [EHDEN Deliverable D4.5 - Interoperability roadmap (URL_TO_INSERT_RECORD_505 https://fairsharing.org/FAIRsharing.53edcc) ](https://zenodo.org/record/4474373).
````{rdmkit_panel}
````



````{dropdown} **References**
````

## Authors

````{authors_fairplus}
Kees: Writing - Original Draft, Conceptualization
Emma: Writing - Original Draft
Jolanda: Writing - Original Draft
Philippe: Writing - Review & Editing
Alasdair: Writing - Review & Editing
Robert: Writing - Review & Editing
````


## License

````{license_fairplus}
CC-BY-4.0
````
