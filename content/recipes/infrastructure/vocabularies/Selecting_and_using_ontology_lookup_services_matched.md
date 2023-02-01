(fcb-select-onto-service)=
# Selecting an ontology lookup service



````{panels_fairplus}
:identifier_text: FCB004
:identifier_link: 'https://w3id.org/faircookbook/FCB004'
:difficulty_level: 1
:recipe_type: survey_review
:reading_time_minutes: 20
:intended_audience: data_manager, data_scientist, terminology_manager, system_administrator, procurement_officer
:maturity_level: 0
:maturity_indicator: 0
:has_executable_code: nope
:recipe_name: Selecting an ontology lookup service
````




## Main Objective: 

This recipe provides **guidance on the selection and exploitation of ontology (URL_TO_INSERT_TERM_4191 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4192 https://fairsharing.org/FAIRsharing.Mkl9RR) s** . 

>* **[Objective of the recipe: introduction to ontology (URL_TO_INSERT_TERM_4193 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4194 https://fairsharing.org/FAIRsharing.Mkl9RR) s](#heading=h.bb3h294tvdau)**
>
>* **[Selecting an ontology (URL_TO_INSERT_TERM_4195 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4196 https://fairsharing.org/FAIRsharing.Mkl9RR) ](#book (URL_TO_INSERT_RECORD_4197 https://fairsharing.org/FAIRsharing.cbz72b) mark=id.okwm6u2vsbft)**
>
>* **[Overview of widespread ontology (URL_TO_INSERT_TERM_4198 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4199 https://fairsharing.org/FAIRsharing.Mkl9RR) s](#book (URL_TO_INSERT_RECORD_4200 https://fairsharing.org/FAIRsharing.cbz72b) mark=id.x42hawpkzgd3)**

An ***ontology (URL_TO_INSERT_TERM_4201 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4202 https://fairsharing.org/FAIRsharing.Mkl9RR) *** 
refers to *any type of application, standalone or Web-based, that enables the use of existing (URL_TO_INSERT_RECORD_4204 https://fairsharing.org/FAIRsharing.q7bkqr)  ontologies (URL_TO_INSERT_TERM_4203 https://fairsharing.org/search?recordType=terminology_artefact)  to support knowledge 
formalization and sharing, by fostering ontology (URL_TO_INSERT_TERM_4205 https://fairsharing.org/search?recordType=terminology_artefact) -based descriptions of knowledge*. 




Tools useful to build, edit or maintain ontologies (URL_TO_INSERT_TERM_4207 https://fairsharing.org/search?recordType=terminology_artefact)  are not considered ontology (URL_TO_INSERT_TERM_4206 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4208 https://fairsharing.org/FAIRsharing.Mkl9RR) s and thus are out of the scope of this recipe. 

In essence, an ontology (URL_TO_INSERT_TERM_4209 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4210 https://fairsharing.org/FAIRsharing.Mkl9RR)  is a platform that provides users with the possibility to **search (URL_TO_INSERT_RECORD_4211 https://fairsharing.org/FAIRsharing.52b22c)  in a set of
ontologies (URL_TO_INSERT_TERM_4212 https://fairsharing.org/search?recordType=terminology_artefact) , the most suitable concepts to describe the semantics of a piece of knowledge of interest,
usually available in the form of one or more keywords or a text excerpt**. 

Most ontology (URL_TO_INSERT_TERM_4213 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4214 https://fairsharing.org/FAIRsharing.Mkl9RR) s are available as Web applications: most of them also support programmatic access to their 
capabilities by means of (REST) APIs. Ontology (URL_TO_INSERT_TERM_4215 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4216 https://fairsharing.org/FAIRsharing.Mkl9RR) s can vary in the features that are provided, but often include:



* **Complex search (URL_TO_INSERT_RECORD_4219 https://fairsharing.org/FAIRsharing.52b22c) ing for concepts of interest**: most services implement advanced search (URL_TO_INSERT_RECORD_4220 https://fairsharing.org/FAIRsharing.52b22c)  features (i.e. scoping the search (URL_TO_INSERT_RECORD_4221 https://fairsharing.org/FAIRsharing.52b22c)  to specific ontologies (URL_TO_INSERT_TERM_4218 https://fairsharing.org/search?recordType=terminology_artefact)  or to specific parts of an ontology (URL_TO_INSERT_TERM_4217 https://fairsharing.org/search?recordType=terminology_artefact) ) or allow users to specify fine-grained patterns to aggregate or restrict the scope of search (URL_TO_INSERT_RECORD_4222 https://fairsharing.org/FAIRsharing.52b22c)  results.
* **Advanced browsing capabilities**, to explore the contents of a specific ontology (URL_TO_INSERT_TERM_4223 https://fairsharing.org/search?recordType=terminology_artefact)  by means of custom data navigation widgets such as tree-based views.
* **Managing distinct versions** of an ontology (URL_TO_INSERT_TERM_4224 https://fairsharing.org/search?recordType=terminology_artefact)  and alert its users when specific concepts become obsolete. 
* **Importing** user-provided ontologies (URL_TO_INSERT_TERM_4226 https://fairsharing.org/search?recordType=terminology_artefact) , giving consumers the ability to leverage a service for other terminologies (URL_TO_INSERT_TERM_4225 https://fairsharing.org/search?recordType=terminology_artefact)  beyond those included.
* Programmatic means to **access and deploy instances of the ontology (URL_TO_INSERT_TERM_4227 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4228 https://fairsharing.org/FAIRsharing.Mkl9RR)  in the premises of its users** represents another differentiating feature, using relevant documentation.
* **Recommending ontologies (URL_TO_INSERT_TERM_4229 https://fairsharing.org/search?recordType=terminology_artefact) ** based on the input of a given term, with ontologies (URL_TO_INSERT_TERM_4230 https://fairsharing.org/search?recordType=terminology_artefact)  ranked according to custom-weighted criteria.
* Access to an **active user community** that supports and exploits a specific ontology (URL_TO_INSERT_TERM_4231 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4232 https://fairsharing.org/FAIRsharing.Mkl9RR) , serving as an indication of widespread adoption and selection.

This recipe presents guideline (URL_TO_INSERT_TERM_4234 https://fairsharing.org/search?recordType=reporting_guideline) s and relevant considerations when choosing an ontology (URL_TO_INSERT_TERM_4233 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4235 https://fairsharing.org/FAIRsharing.Mkl9RR) , followed by
overview of existing (URL_TO_INSERT_RECORD_4240 https://fairsharing.org/FAIRsharing.q7bkqr)  public ontology (URL_TO_INSERT_TERM_4236 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4237 https://fairsharing.org/FAIRsharing.Mkl9RR) s and a comparison of their core (URL_TO_INSERT_RECORD_4238 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_4239 https://fairsharing.org/FAIRsharing.xMmOCL)  features.


## Selecting An Ontology Lookup Service

This section provides guideline (URL_TO_INSERT_TERM_4242 https://fairsharing.org/search?recordType=reporting_guideline) s and suggestions on how to select and leverage an ontology (URL_TO_INSERT_TERM_4241 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4243 https://fairsharing.org/FAIRsharing.Mkl9RR) , on the basis
of the knowledge needs and ontology (URL_TO_INSERT_TERM_4245 https://fairsharing.org/search?recordType=terminology_artefact)  use patterns that characterize a specific knowledge-intensive project (URL_TO_INSERT_TERM_4244 https://fairsharing.org/search?recordType=project) . 

Several aspects to consider when choosing an ontology (URL_TO_INSERT_TERM_4246 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4247 https://fairsharing.org/FAIRsharing.Mkl9RR)  are derived based on a series of commonly asked questions;



* **Is the set of ontologies (URL_TO_INSERT_TERM_4250 https://fairsharing.org/search?recordType=terminology_artefact)  incorporated in the ontology (URL_TO_INSERT_TERM_4249 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4251 https://fairsharing.org/FAIRsharing.Mkl9RR)  suitable to formally describe the knowledge domain my project (URL_TO_INSERT_TERM_4248 https://fairsharing.org/search?recordType=project)  is interested in?**

    Ontology (URL_TO_INSERT_TERM_4252 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4254 https://fairsharing.org/FAIRsharing.Mkl9RR) s usually provide access and enable users to search (URL_TO_INSERT_RECORD_4255 https://fairsharing.org/FAIRsharing.52b22c)  and reference classes and properties of _a specific set of ontologies (URL_TO_INSERT_TERM_4253 https://fairsharing.org/search?recordType=terminology_artefact)  related to a specific knowledge domain_ (i.e. biomedical knowledge).
    When choosing an ontology (URL_TO_INSERT_TERM_4257 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4259 https://fairsharing.org/FAIRsharing.Mkl9RR)  it is important to verify whether the ontologies (URL_TO_INSERT_TERM_4258 https://fairsharing.org/search?recordType=terminology_artefact)  covered by a specific service are suitable to describe the content of our knowledge-intensive project (URL_TO_INSERT_TERM_4256 https://fairsharing.org/search?recordType=project) . 
    Besides, a list of the ontologies (URL_TO_INSERT_TERM_4260 https://fairsharing.org/search?recordType=terminology_artefact)  covered, and interactive widgets to explore such ontologies (URL_TO_INSERT_TERM_4261 https://fairsharing.org/search?recordType=terminology_artefact)  (e.g. tree-based views), 
    some ontology (URL_TO_INSERT_TERM_4262 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4264 https://fairsharing.org/FAIRsharing.Mkl9RR) s also provide _ontology (URL_TO_INSERT_TERM_4263 https://fairsharing.org/search?recordType=terminology_artefact)  recommendation capabilities:_ given some “sample” 
    (i.e. text excerpt or list of keywords) of the knowledge we need to describe by means of available ontologies (URL_TO_INSERT_TERM_4265 https://fairsharing.org/search?recordType=terminology_artefact) , 
    the ontology (URL_TO_INSERT_TERM_4266 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4268 https://fairsharing.org/FAIRsharing.Mkl9RR)  ‘recommender’ suggests which are the best ontologies (URL_TO_INSERT_TERM_4267 https://fairsharing.org/search?recordType=terminology_artefact)  to use to this propose.

* **Do I need to consider / rely on private ontologies (URL_TO_INSERT_TERM_4270 https://fairsharing.org/search?recordType=terminology_artefact)  in my project (URL_TO_INSERT_TERM_4269 https://fairsharing.org/search?recordType=project) ? Do I need to use ontologies (URL_TO_INSERT_TERM_4271 https://fairsharing.org/search?recordType=terminology_artefact)  that are not already 
    imported and thus available in the ontology (URL_TO_INSERT_TERM_4272 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4273 https://fairsharing.org/FAIRsharing.Mkl9RR)  of my choice?**

    Some ontology (URL_TO_INSERT_TERM_4274 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4276 https://fairsharing.org/FAIRsharing.Mkl9RR) s enable users to import external (i.e. user-provided) ontologies (URL_TO_INSERT_TERM_4275 https://fairsharing.org/search?recordType=terminology_artefact)  in order to incorporate
    the content of these ontologies (URL_TO_INSERT_TERM_4277 https://fairsharing.org/search?recordType=terminology_artefact)  in their search (URL_TO_INSERT_RECORD_4278 https://fairsharing.org/FAIRsharing.52b22c)  and recommendation capabilities. 
    This feature could represent a key factor to consider when choosing an ontology (URL_TO_INSERT_TERM_4279 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4280 https://fairsharing.org/FAIRsharing.Mkl9RR)  since several 
    knowledge-intensive project (URL_TO_INSERT_TERM_4281 https://fairsharing.org/search?recordType=project) s rely on private ontologies (URL_TO_INSERT_TERM_4282 https://fairsharing.org/search?recordType=terminology_artefact)  or need to consider a set of additional ontologies (URL_TO_INSERT_TERM_4283 https://fairsharing.org/search?recordType=terminology_artefact)  not 
    natively covered by a specific ontology (URL_TO_INSERT_TERM_4284 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4285 https://fairsharing.org/FAIRsharing.Mkl9RR) .

* **Because of data privacy or data protection issues, do I need to use an instance of the ontology (URL_TO_INSERT_TERM_4286 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4287 https://fairsharing.org/FAIRsharing.Mkl9RR)  that
is deployed locally on my private computing infrastructure?**

    Several ontology (URL_TO_INSERT_TERM_4288 https://fairsharing.org/search?recordType=terminology_artefact) -lookup services provide the possibility to deploy the service on the private computing 
    infrastructure of its users. This feature would be particularly relevant when private ontologies (URL_TO_INSERT_TERM_4289 https://fairsharing.org/search?recordType=terminology_artefact)  are adopted in a 
    knowledge-intensive project (URL_TO_INSERT_TERM_4290 https://fairsharing.org/search?recordType=project) .

* **Which are the usage patterns I will rely on in order to exploit the ontology (URL_TO_INSERT_TERM_4291 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4292 https://fairsharing.org/FAIRsharing.Mkl9RR) ? Will the 1)
massive and systematic exploitation of the ontology (URL_TO_INSERT_TERM_4293 https://fairsharing.org/search?recordType=terminology_artefact)  search (URL_TO_INSERT_RECORD_4295 https://fairsharing.org/FAIRsharing.52b22c) , 2) the recommendation features of the ontology (URL_TO_INSERT_TERM_4294 https://fairsharing.org/search?recordType=terminology_artefact)  lookup
service or 3) the integration of its capabilities in more complex systems, require the possibility to programmatically 
access the service by means of an application programming interface (API)?**

    Ontology (URL_TO_INSERT_TERM_4296 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4297 https://fairsharing.org/FAIRsharing.Mkl9RR) s usually provide a (Web-based) user interface as the preferred way to interact with them to
    browse and search (URL_TO_INSERT_RECORD_4299 https://fairsharing.org/FAIRsharing.52b22c)  for ontologies (URL_TO_INSERT_TERM_4298 https://fairsharing.org/search?recordType=terminology_artefact) , or recommend relevant concepts to describe contents of interest. 
    In several scenarios, the possibility to programmatically interact with ontology (URL_TO_INSERT_TERM_4300 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4301 https://fairsharing.org/FAIRsharing.Mkl9RR) s would be extremely
    valuable; to this purpose, several ontology (URL_TO_INSERT_TERM_4302 https://fairsharing.org/search?recordType=terminology_artefact) -lookup services implement an API (mostly based on REST interactions)
    that enable the user to programmatically invoke the majority of ontology (URL_TO_INSERT_TERM_4303 https://fairsharing.org/search?recordType=terminology_artefact)  search (URL_TO_INSERT_RECORD_4304 https://fairsharing.org/FAIRsharing.52b22c)  features of the same service. 
    In order to simplify the integration of the ontology (URL_TO_INSERT_TERM_4305 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4306 https://fairsharing.org/FAIRsharing.Mkl9RR)  support into external applications,  
   several-ontology (URL_TO_INSERT_TERM_4307 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4308 https://fairsharing.org/FAIRsharing.Mkl9RR) s provide users with language-specific clients to interact with them through their API. 

* **Is the distribution license of the ontology (URL_TO_INSERT_TERM_4309 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4310 https://fairsharing.org/FAIRsharing.Mkl9RR)  compatible with the way I plan to exploit the 
features provided the same service in my project (URL_TO_INSERT_TERM_4311 https://fairsharing.org/search?recordType=project)  or with the way I plan to integrate the same service in my project (URL_TO_INSERT_TERM_4312 https://fairsharing.org/search?recordType=project) ?**

    The licencing terms of the ontology (URL_TO_INSERT_TERM_4313 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4314 https://fairsharing.org/FAIRsharing.Mkl9RR)  of choice intended for use in a given context and 
    knowledge-intensive project (URL_TO_INSERT_TERM_4315 https://fairsharing.org/search?recordType=project) , is a key consideration when selecting an ontology (URL_TO_INSERT_TERM_4316 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4317 https://fairsharing.org/FAIRsharing.Mkl9RR) : available 
    ontology (URL_TO_INSERT_TERM_4318 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4319 https://fairsharing.org/FAIRsharing.Mkl9RR) s range from open-source applications to commercial tools, and it is best to choose one with funding in mind.

* **Does the ontology (URL_TO_INSERT_TERM_4320 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4323 https://fairsharing.org/FAIRsharing.Mkl9RR)  manage ontology (URL_TO_INSERT_TERM_4321 https://fairsharing.org/search?recordType=terminology_artefact)  versioning and updates so that I can easily reflect any ontology (URL_TO_INSERT_TERM_4322 https://fairsharing.org/search?recordType=terminology_artefact)  
update into my knowledge-intensive project (URL_TO_INSERT_TERM_4324 https://fairsharing.org/search?recordType=project) ? **

    Ontologies (URL_TO_INSERT_TERM_4327 https://fairsharing.org/search?recordType=terminology_artefact)  and terminologies (URL_TO_INSERT_TERM_4325 https://fairsharing.org/search?recordType=terminology_artefact)  usually evolve over time: when a new, updated version of an ontology (URL_TO_INSERT_TERM_4326 https://fairsharing.org/search?recordType=terminology_artefact)  used in a 
    knowledge-intensive project (URL_TO_INSERT_TERM_4328 https://fairsharing.org/search?recordType=project)  becomes available, best practice suggests that we should also update the part of our 
    project (URL_TO_INSERT_TERM_4329 https://fairsharing.org/search?recordType=project) s that rely on such ontology (URL_TO_INSERT_TERM_4330 https://fairsharing.org/search?recordType=terminology_artefact) . Some ontology (URL_TO_INSERT_TERM_4331 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4332 https://fairsharing.org/FAIRsharing.Mkl9RR) s implement specific procedures and tools to manage
    and propagate ontology (URL_TO_INSERT_TERM_4333 https://fairsharing.org/search?recordType=terminology_artefact)  updates; the availability of such tools would simplify the implementation of changes deriving
    from ontology (URL_TO_INSERT_TERM_4335 https://fairsharing.org/search?recordType=terminology_artefact)  updates in the project (URL_TO_INSERT_TERM_4334 https://fairsharing.org/search?recordType=project) s under consideration.

* **Is the ontology (URL_TO_INSERT_TERM_4336 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4337 https://fairsharing.org/FAIRsharing.Mkl9RR)  supported by an active community of developers
or by an active company? Which are the available channels I can rely on to receive support on the usage and integration 
of the ontology (URL_TO_INSERT_TERM_4338 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4339 https://fairsharing.org/FAIRsharing.Mkl9RR) ?**

    The support of an active community of developers and users is a key aspect to take into account when choosing an 
    ontology (URL_TO_INSERT_TERM_4340 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4342 https://fairsharing.org/FAIRsharing.Mkl9RR) . This could be quantified by evaluating several factors of an ontology (URL_TO_INSERT_TERM_4341 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4343 https://fairsharing.org/FAIRsharing.Mkl9RR)  including:
    (i) availability of mailing or support lists; (ii) for open-source project (URL_TO_INSERT_TERM_4345 https://fairsharing.org/search?recordType=project) s, using metric (URL_TO_INSERT_TERM_4344 https://fairsharing.org/search?recordType=metric) s such as the star-rating,
    the number of forks and followers and the frequency of commits of the project (URL_TO_INSERT_TERM_4346 https://fairsharing.org/search?recordType=project)  on the code-sharing platform used 
    (e.g. GitHub (URL_TO_INSERT_RECORD_4349 https://fairsharing.org/FAIRsharing.c55d5e)  (URL_TO_INSERT_RECORD_4350 https://fairsharing.org/FAIRsharing.c55d5e) ); (iii) size of the community of users of the ontology (URL_TO_INSERT_TERM_4347 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4348 https://fairsharing.org/FAIRsharing.Mkl9RR)  (e.g. how many followers on social
    media accounts, how many clients advertised on the Website).

## Key Selection Criteria

The above questions have highlighted 20 factors which should be taken into account when choosing a service. 
These factors can be categorised into 3 groups; **ontology (URL_TO_INSERT_TERM_4352 https://fairsharing.org/search?recordType=terminology_artefact)  informat (URL_TO_INSERT_TERM_4351 https://fairsharing.org/search?recordType=model_and_format) ion, functionality** and **interfaces**, and include;

### **Ontology Information**



1. **URL (URL_TO_INSERT_RECORD_4355 https://fairsharing.org/FAIRsharing.9d38e2) **: the main URL (URL_TO_INSERT_RECORD_4356 https://fairsharing.org/FAIRsharing.9d38e2)  where the ontology (URL_TO_INSERT_TERM_4353 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4354 https://fairsharing.org/FAIRsharing.Mkl9RR)  can be accessed
2. **Latest version of service / data / code (where applicable**): the most recent version of both the content (i.e. ontologies (URL_TO_INSERT_TERM_4358 https://fairsharing.org/search?recordType=terminology_artefact) ) and the code of the ontology (URL_TO_INSERT_TERM_4357 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4359 https://fairsharing.org/FAIRsharing.Mkl9RR) 
3. **Host Organisation**: the organisation responsible for the maintenance of the ontology (URL_TO_INSERT_TERM_4360 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4361 https://fairsharing.org/FAIRsharing.Mkl9RR) 
4. **Public / private**: is the ontology (URL_TO_INSERT_TERM_4362 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4363 https://fairsharing.org/FAIRsharing.Mkl9RR)  a public or private infrastructure?
5. **Licence**: the licence that regulates the use and cost of the ontology (URL_TO_INSERT_TERM_4364 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4365 https://fairsharing.org/FAIRsharing.Mkl9RR) 
6. **Domain**: which is the knowledge domain covered by the ontologies (URL_TO_INSERT_TERM_4367 https://fairsharing.org/search?recordType=terminology_artefact)  referenced in the ontology (URL_TO_INSERT_TERM_4366 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4368 https://fairsharing.org/FAIRsharing.Mkl9RR) ?
7. **Quantification of community of users**: objective measures to quantify the community of users supporting and consuming an ontology (URL_TO_INSERT_TERM_4369 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4370 https://fairsharing.org/FAIRsharing.Mkl9RR) , including: number of stars and forks on GitHub (URL_TO_INSERT_RECORD_4371 https://fairsharing.org/FAIRsharing.c55d5e)  (URL_TO_INSERT_RECORD_4372 https://fairsharing.org/FAIRsharing.c55d5e) , number of social media followers

### **Functionality**



8. **Number and complexity of ontologies (URL_TO_INSERT_TERM_4374 https://fairsharing.org/search?recordType=terminology_artefact)  covered**: how many ontologies (URL_TO_INSERT_TERM_4375 https://fairsharing.org/search?recordType=terminology_artefact)  does the ontology (URL_TO_INSERT_TERM_4373 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4376 https://fairsharing.org/FAIRsharing.Mkl9RR)  cover and how complex are they?
9. **Ontology (URL_TO_INSERT_TERM_4379 https://fairsharing.org/search?recordType=terminology_artefact)  format (URL_TO_INSERT_TERM_4377 https://fairsharing.org/search?recordType=model_and_format) s supported**: which ontology (URL_TO_INSERT_TERM_4380 https://fairsharing.org/search?recordType=terminology_artefact)  format (URL_TO_INSERT_TERM_4378 https://fairsharing.org/search?recordType=model_and_format) s are supported by the ontology (URL_TO_INSERT_TERM_4381 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4382 https://fairsharing.org/FAIRsharing.Mkl9RR) ?
10. **Ontology (URL_TO_INSERT_TERM_4383 https://fairsharing.org/search?recordType=terminology_artefact)  importing capabilities**: if and how ontologies (URL_TO_INSERT_TERM_4385 https://fairsharing.org/search?recordType=terminology_artefact)  can be imported and thus indexed by the ontology (URL_TO_INSERT_TERM_4384 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4386 https://fairsharing.org/FAIRsharing.Mkl9RR) ?
11. **Ontology (URL_TO_INSERT_TERM_4387 https://fairsharing.org/search?recordType=terminology_artefact)  browsing capabilities**: which interaction patterns are available to browse the set of ontologies (URL_TO_INSERT_TERM_4389 https://fairsharing.org/search?recordType=terminology_artefact)  contemplated by the ontology (URL_TO_INSERT_TERM_4388 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4390 https://fairsharing.org/FAIRsharing.Mkl9RR) ?
12. **Ontology (URL_TO_INSERT_TERM_4391 https://fairsharing.org/search?recordType=terminology_artefact)  search (URL_TO_INSERT_RECORD_4396 https://fairsharing.org/FAIRsharing.52b22c)  capabilities**: which search (URL_TO_INSERT_RECORD_4397 https://fairsharing.org/FAIRsharing.52b22c)  patterns are provided by the ontology (URL_TO_INSERT_TERM_4392 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4395 https://fairsharing.org/FAIRsharing.Mkl9RR)  to identify the best concept useful to represent the semantic of a term? When search (URL_TO_INSERT_RECORD_4398 https://fairsharing.org/FAIRsharing.52b22c) ing against a term, does the ontology (URL_TO_INSERT_TERM_4393 https://fairsharing.org/search?recordType=terminology_artefact)  give an indication of whether the term has been derived from a different ontology (URL_TO_INSERT_TERM_4394 https://fairsharing.org/search?recordType=terminology_artefact) ?
13. **Ontology (URL_TO_INSERT_TERM_4399 https://fairsharing.org/search?recordType=terminology_artefact)  recommendation capabilities**: does the ontology (URL_TO_INSERT_TERM_4400 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4402 https://fairsharing.org/FAIRsharing.Mkl9RR)  provide users with a recommendation concerning the most suitable ontologies (URL_TO_INSERT_TERM_4401 https://fairsharing.org/search?recordType=terminology_artefact)  to semantically characterize the contents of some text / a set of keywords? 
14. **Ontology (URL_TO_INSERT_TERM_4403 https://fairsharing.org/search?recordType=terminology_artefact)  update capabilities**: how are terms and/or relationships updated in a given ontology (URL_TO_INSERT_TERM_4404 https://fairsharing.org/search?recordType=terminology_artefact)  and how is this governed? Is this an automatic or manual update and what happens to terms that are considered obsolete?
15. **Ontology (URL_TO_INSERT_TERM_4405 https://fairsharing.org/search?recordType=terminology_artefact)  versioning capabilities**: are there predefined patterns to identify, manage and compare distinct versions of an ontology (URL_TO_INSERT_TERM_4406 https://fairsharing.org/search?recordType=terminology_artefact) ? 

### **Interfaces**



16. **Description of Web-based access to service**: which ontology (URL_TO_INSERT_TERM_4407 https://fairsharing.org/search?recordType=terminology_artefact)  browsing  and search (URL_TO_INSERT_RECORD_4412 https://fairsharing.org/FAIRsharing.52b22c)  patterns are available to the (Web-based) user interface of the ontology (URL_TO_INSERT_TERM_4408 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4410 https://fairsharing.org/FAIRsharing.Mkl9RR) ? Does the ontology (URL_TO_INSERT_TERM_4409 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4411 https://fairsharing.org/FAIRsharing.Mkl9RR)  also provide programmatic access to its data and services (e.g. by means of a REST API)?
17. **Description of API**: reference to the documentation of the (REST) API provided by the ontology (URL_TO_INSERT_TERM_4413 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4414 https://fairsharing.org/FAIRsharing.Mkl9RR) , if any
18. **Developer resources**: description of resources provided to developers in order to ease the programmatic access to the features of the ontology (URL_TO_INSERT_TERM_4415 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4416 https://fairsharing.org/FAIRsharing.Mkl9RR)  (i.e. libraries to query the REST API from a specific programming language).
19. **Local deploy of service**: possibility to locally deploy the ontology (URL_TO_INSERT_TERM_4417 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4418 https://fairsharing.org/FAIRsharing.Mkl9RR) 
20. **Source code reference**: if available, link to the source code of the ontology (URL_TO_INSERT_TERM_4419 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4420 https://fairsharing.org/FAIRsharing.Mkl9RR) 
4. **Overview of Widespread Ontology (URL_TO_INSERT_TERM_4421 https://fairsharing.org/search?recordType=terminology_artefact)  Lookup Service (URL_TO_INSERT_RECORD_4422 https://fairsharing.org/FAIRsharing.Mkl9RR) s**

---

Here, we have used the selection criteria above to provide an overview and comparison of four widespread ontology (URL_TO_INSERT_TERM_4423 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4424 https://fairsharing.org/FAIRsharing.Mkl9RR) s, namely:



-  [EBI Ontology (URL_TO_INSERT_TERM_4425 https://fairsharing.org/search?recordType=terminology_artefact)  Lookup Service (URL_TO_INSERT_RECORD_4426 https://fairsharing.org/FAIRsharing.Mkl9RR) ](https://www.ebi.ac.uk/ols/index (URL_TO_INSERT_RECORD_4427 https://fairsharing.org/FAIRsharing.Mkl9RR) )
-  [BioPortal (URL_TO_INSERT_RECORD_4428 https://fairsharing.org/FAIRsharing.4m97ah)  (URL_TO_INSERT_RECORD_4429 https://fairsharing.org/FAIRsharing.4m97ah) ](https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_4430 https://fairsharing.org/FAIRsharing.4m97ah) )
-  [OHD (URL_TO_INSERT_RECORD_4431 https://fairsharing.org/FAIRsharing.bg7bb6) SI Athena](https://athena.ohdsi.org/search-terms/start)
-  [Ontobee (URL_TO_INSERT_RECORD_4435 https://fairsharing.org/FAIRsharing.q8fx1b)  (URL_TO_INSERT_RECORD_4436 https://fairsharing.org/FAIRsharing.q8fx1b)  and the OBO (URL_TO_INSERT_RECORD_4433 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_4434 https://fairsharing.org/FAIRsharing.cbz72b)  Foundry (URL_TO_INSERT_RECORD_4432 https://fairsharing.org/FAIRsharing.847069) ](http://www.ontobee.org (URL_TO_INSERT_RECORD_4437 https://fairsharing.org/FAIRsharing.q8fx1b) )

The results of the analysis can be found below, else in tabular format (URL_TO_INSERT_TERM_4438 https://fairsharing.org/search?recordType=model_and_format)  [here](https://docs.google.com/spreadsheets/d/1kn1oEhsYJPiLI5gA12B1UsbLBRoSLGbOYcOMDG4614o/edit#gid=0).

Note, the _‘last update of this table_’ field provides the date on which the ontology (URL_TO_INSERT_TERM_4439 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_4440 https://fairsharing.org/FAIRsharing.Mkl9RR)  was last assessed.

### **The EBI Ontology Lookup Service** {footcite}`pmid20460452`

<!-- **Overview by Francesco** -->


<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td>Ontology (URL_TO_INSERT_TERM_4441 https://fairsharing.org/search?recordType=terminology_artefact)  Lookup Service (URL_TO_INSERT_RECORD_4442 https://fairsharing.org/FAIRsharing.Mkl9RR) 
   </td>
  </tr>
  <tr>
   <td>
<strong>Last update of this table</strong>
   </td>
   <td>14/04/2020
   </td>
  </tr>
  <tr>
   <td><strong>URL (URL_TO_INSERT_RECORD_4443 https://fairsharing.org/FAIRsharing.9d38e2) </strong>
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/index (URL_TO_INSERT_RECORD_4444 https://fairsharing.org/FAIRsharing.Mkl9RR) ">https://www.ebi.ac.uk/ols/index (URL_TO_INSERT_RECORD_4445 https://fairsharing.org/FAIRsharing.Mkl9RR) </a>
   </td>
  </tr>
  <tr>
   <td><strong>Latest version of service / data / code (where applicable)</strong>
   </td>
   <td>Content: last update 12 Apr 2020 11:39
<p>
Code: Maven PO (URL_TO_INSERT_RECORD_4446 https://fairsharing.org/FAIRsharing.3ngg40) V version (from GitHub (URL_TO_INSERT_RECORD_4447 https://fairsharing.org/FAIRsharing.c55d5e)  (URL_TO_INSERT_RECORD_4448 https://fairsharing.org/FAIRsharing.c55d5e) ): 3.2.1-SNAPSHOT
<p>
<a href="https://github.com (URL_TO_INSERT_RECORD_4449 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/OLS">https://github.com (URL_TO_INSERT_RECORD_4450 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/OLS</a>
<p>
Last commit on GitHub (URL_TO_INSERT_RECORD_4451 https://fairsharing.org/FAIRsharing.c55d5e)  (URL_TO_INSERT_RECORD_4452 https://fairsharing.org/FAIRsharing.c55d5e) : April 2020
   </td>
  </tr>
  <tr>
   <td><strong>Host organisation</strong>
   </td>
   <td><a href="http://www.ebi.ac.uk/about/spot-team">Samples, Phenotypes and Ontologies (URL_TO_INSERT_TERM_4453 https://fairsharing.org/search?recordType=terminology_artefact)  Team</a> at EMB (URL_TO_INSERT_RECORD_4454 https://fairsharing.org/FAIRsharing.a1rp4c) L-EBI
   </td>
  </tr>
  <tr>
   <td><strong>Public / private</strong>
   </td>
   <td>Public
   </td>
  </tr>
  <tr>
   <td><strong>Licence</strong>
   </td>
   <td>Apache 2.0
   </td>
  </tr>
  <tr>
   <td><strong>Domain</strong>
   </td>
   <td>A repository (URL_TO_INSERT_TERM_4455 https://fairsharing.org/search?recordType=repository)  for biomedical ontologies (URL_TO_INSERT_TERM_4457 https://fairsharing.org/search?recordType=terminology_artefact)  that aims to provide a single point of access to the latest ontology (URL_TO_INSERT_TERM_4456 https://fairsharing.org/search?recordType=terminology_artefact)  versions
   </td>
  </tr>
  <tr>
   <td><strong>Set of ontologies (URL_TO_INSERT_TERM_4458 https://fairsharing.org/search?recordType=terminology_artefact)  covered</strong>
   </td>
   <td>245 ontologies (URL_TO_INSERT_TERM_4459 https://fairsharing.org/search?recordType=terminology_artefact)  / 6,119,228 terms / 27,778 properties / 485,541 individuals
<p>
Whole list at: <a href="https://www.ebi.ac.uk/ols/ontologies">https://www.ebi.ac.uk/ols/ontologies</a>
   </td>
  </tr>
  <tr>
   <td><strong>Onto. format (URL_TO_INSERT_TERM_4460 https://fairsharing.org/search?recordType=model_and_format) s supported</strong>
   </td>
   <td>OWL (URL_TO_INSERT_RECORD_4461 https://fairsharing.org/FAIRsharing.atygwy)  2 and OBO (URL_TO_INSERT_RECORD_4462 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_4463 https://fairsharing.org/FAIRsharing.cbz72b) 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. importing capabilities</strong>
   </td>
   <td>By means of a local installation it is possible to import ontologies (URL_TO_INSERT_TERM_4465 https://fairsharing.org/search?recordType=terminology_artefact)  in OWL (URL_TO_INSERT_RECORD_4466 https://fairsharing.org/FAIRsharing.atygwy)  2 and OBO (URL_TO_INSERT_RECORD_4467 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_4468 https://fairsharing.org/FAIRsharing.cbz72b)  format (URL_TO_INSERT_TERM_4464 https://fairsharing.org/search?recordType=model_and_format) 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. browsing capabilities</strong>
   </td>
   <td>Tree-view based browsing of hierarch (URL_TO_INSERT_RECORD_4472 https://fairsharing.org/FAIRsharing.52b22c) ies of classes and properties of ontologies (URL_TO_INSERT_TERM_4471 https://fairsharing.org/search?recordType=terminology_artefact) . The modifications added by different version of each ontology (URL_TO_INSERT_TERM_4469 https://fairsharing.org/search?recordType=terminology_artefact)  are shown by means of distinct background colors in ontology (URL_TO_INSERT_TERM_4470 https://fairsharing.org/search?recordType=terminology_artefact)  browsing tree-views
   </td>
  </tr>
  <tr>
   <td><strong>Onto. search (URL_TO_INSERT_RECORD_4473 https://fairsharing.org/FAIRsharing.52b22c)  capabilities</strong>
   </td>
   <td>Search (URL_TO_INSERT_RECORD_4476 https://fairsharing.org/FAIRsharing.52b22c)  by term to gather all the ontologies (URL_TO_INSERT_TERM_4474 https://fairsharing.org/search?recordType=terminology_artefact)  where the term is found. It is possible to restrict search (URL_TO_INSERT_RECORD_4477 https://fairsharing.org/FAIRsharing.52b22c)  results to one or more ontologies (URL_TO_INSERT_TERM_4475 https://fairsharing.org/search?recordType=terminology_artefact) , to a specific type of result (i.e. class, property or individual) or to exact or partial term match
   </td>
  </tr>
  <tr>
   <td><strong>Onto. recommendation capabilities</strong>
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td><strong>Onto. update capabilities</strong>
   </td>
   <td>OLS (URL_TO_INSERT_RECORD_4479 https://fairsharing.org/FAIRsharing.Mkl9RR)  updates nightly to always provide the latest ontology (URL_TO_INSERT_TERM_4478 https://fairsharing.org/search?recordType=terminology_artefact)  versions
   </td>
  </tr>
  <tr>
   <td><strong>Onto. versioning capabilities</strong>
   </td>
   <td>Obsoleted ontology (URL_TO_INSERT_TERM_4480 https://fairsharing.org/search?recordType=terminology_artefact)  terms are spotted by means of a boolean flag (is_obsolete)
   </td>
  </tr>
  <tr>
   <td><strong>Description of Web-based access to service</strong>
   </td>
   <td>Besides a Web-based user interface useful to browse ontologies (URL_TO_INSERT_TERM_4482 https://fairsharing.org/search?recordType=terminology_artefact)  and search (URL_TO_INSERT_RECORD_4483 https://fairsharing.org/FAIRsharing.52b22c)  for ontology (URL_TO_INSERT_TERM_4481 https://fairsharing.org/search?recordType=terminology_artefact)  concepts, free-access by means of a REST API is provided to the users
   </td>
  </tr>
  <tr>
   <td><strong>Description of API</strong>
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/docs/api">https://www.ebi.ac.uk/ols/docs/api</a>
   </td>
  </tr>
  <tr>
   <td><strong>Developer resources</strong>
   </td>
   <td>Java and R clients / Javascript widgets
   </td>
  </tr>
  <tr>
   <td><strong>Local deploy of service</strong>
   </td>
   <td>Possible, documentation at: <a href="https://www.ebi.ac.uk/ols/docs/installation-guide">https://www.ebi.ac.uk/ols/docs/installation-guide</a>
   </td>
  </tr>
  <tr>
   <td><strong>Source code reference</strong>
   </td>
   <td><a href="https://github.com (URL_TO_INSERT_RECORD_4484 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/OLS">https://github.com (URL_TO_INSERT_RECORD_4485 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/OLS</a>
   </td>
  </tr>
  <tr>
   <td><strong>Quantification of community of users</strong>
   </td>
   <td>GitHub (URL_TO_INSERT_RECORD_4486 https://fairsharing.org/FAIRsharing.c55d5e)  (URL_TO_INSERT_RECORD_4487 https://fairsharing.org/FAIRsharing.c55d5e) : 49 stars and 19 forks
<p>
Twitter: 116 followers
   </td>
  </tr>
</table>


### **NCBO BioPortal** {footcite}`pmid23734708bioportal`

<!-- **Overview by Francesco** -->

<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td>Bioportal (URL_TO_INSERT_RECORD_4488 https://fairsharing.org/FAIRsharing.4m97ah)  
   </td>
  </tr>
  <tr>
   <td>
<strong>Last update of this table</strong>
   </td>
   <td>14/04/2020
   </td>
  </tr>
  <tr>
   <td><strong>URL (URL_TO_INSERT_RECORD_4489 https://fairsharing.org/FAIRsharing.9d38e2) </strong>
   </td>
   <td><a href="https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_4490 https://fairsharing.org/FAIRsharing.4m97ah) /">https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_4491 https://fairsharing.org/FAIRsharing.4m97ah) /</a>
   </td>
  </tr>
  <tr>
   <td><strong>Latest version of service / data / code (where applicable)</strong>
   </td>
   <td><em>Content</em>: last update 12 Apr 2020 11:39
<p>
<em>Code</em>: 
<ul>

<li>Web UI: <a href="https://github.com (URL_TO_INSERT_RECORD_4492 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/bioportal_web_ui">https://github.com (URL_TO_INSERT_RECORD_4493 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/bioportal_web_ui</a>

<li>REST API: <a href="https://github.com (URL_TO_INSERT_RECORD_4494 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_api">https://github.com (URL_TO_INSERT_RECORD_4495 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_api</a>

<li>Linked Data: <a href="https://github.com (URL_TO_INSERT_RECORD_4496 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_linked_data">https://github.com (URL_TO_INSERT_RECORD_4497 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_linked_data</a>

<p>
Latest commit on GitHub (URL_TO_INSERT_RECORD_4498 https://fairsharing.org/FAIRsharing.c55d5e)  (URL_TO_INSERT_RECORD_4499 https://fairsharing.org/FAIRsharing.c55d5e) : April 2020
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td><strong>Host organisation</strong>
   </td>
   <td><a href="https://ncbo.bioontology.org/about-ncbo">U.S. National Center for Biomedical Ontology (URL_TO_INSERT_TERM_4500 https://fairsharing.org/search?recordType=terminology_artefact) </a>
   </td>
  </tr>
  <tr>
   <td><strong>Public / private</strong>
   </td>
   <td>Public
   </td>
  </tr>
  <tr>
   <td><strong>Licence</strong>
   </td>
   <td>Available at: <a href="https://github.com (URL_TO_INSERT_RECORD_4501 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_api/blob/master/LICENSE.txt">https://github.com (URL_TO_INSERT_RECORD_4502 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_api/blob/master/LICENSE.txt</a>
   </td>
  </tr>
  <tr>
   <td><strong>Domain</strong>
   </td>
   <td>A Web-based application for search (URL_TO_INSERT_RECORD_4507 https://fairsharing.org/FAIRsharing.52b22c) ing, sharing, visualizing, and analyzing a large repository (URL_TO_INSERT_TERM_4503 https://fairsharing.org/search?recordType=repository)  of biomedical ontologies (URL_TO_INSERT_TERM_4506 https://fairsharing.org/search?recordType=terminology_artefact) , terminologies (URL_TO_INSERT_TERM_4504 https://fairsharing.org/search?recordType=terminology_artefact) , and ontology (URL_TO_INSERT_TERM_4505 https://fairsharing.org/search?recordType=terminology_artefact) -based annotations
   </td>
  </tr>
  <tr>
   <td><strong>Set of ontologies (URL_TO_INSERT_TERM_4508 https://fairsharing.org/search?recordType=terminology_artefact)  covered</strong>
   </td>
   <td>Ontologies (URL_TO_INSERT_TERM_4509 https://fairsharing.org/search?recordType=terminology_artefact) : 842 / Classes: 11,324,508 
<p>
Whole list at: <a href="https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_4510 https://fairsharing.org/FAIRsharing.4m97ah) /ontologies">https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_4511 https://fairsharing.org/FAIRsharing.4m97ah) /ontologies</a>
   </td>
  </tr>
  <tr>
   <td><strong>Onto. format (URL_TO_INSERT_TERM_4512 https://fairsharing.org/search?recordType=model_and_format) s supported</strong>
   </td>
   <td>OWL (URL_TO_INSERT_RECORD_4513 https://fairsharing.org/FAIRsharing.atygwy) , OBO (URL_TO_INSERT_RECORD_4514 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_4515 https://fairsharing.org/FAIRsharing.cbz72b) , SKOS (URL_TO_INSERT_RECORD_4516 https://fairsharing.org/FAIRsharing.48e326) 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. importing capabilities</strong>
   </td>
   <td>It is possible to upload / submit new ontologies (URL_TO_INSERT_TERM_4519 https://fairsharing.org/search?recordType=terminology_artefact)  or new versions of existing (URL_TO_INSERT_RECORD_4523 https://fairsharing.org/FAIRsharing.q7bkqr)  ontologies (URL_TO_INSERT_TERM_4520 https://fairsharing.org/search?recordType=terminology_artefact)  that will be indexed in BioPortal (URL_TO_INSERT_RECORD_4521 https://fairsharing.org/FAIRsharing.4m97ah)  (URL_TO_INSERT_RECORD_4522 https://fairsharing.org/FAIRsharing.4m97ah) . Ontology (URL_TO_INSERT_TERM_4518 https://fairsharing.org/search?recordType=terminology_artefact)  metadata will be provided in the <a href="http://omv.ontoware.org">Ontology Metadata Vocabulary</a> (OMV (URL_TO_INSERT_RECORD_4524 https://fairsharing.org/FAIRsharing.wqy605) ) format (URL_TO_INSERT_TERM_4517 https://fairsharing.org/search?recordType=model_and_format) 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. browsing capabilities</strong>
   </td>
   <td>For each ontology (URL_TO_INSERT_TERM_4527 https://fairsharing.org/search?recordType=terminology_artefact)  / terminology (URL_TO_INSERT_TERM_4525 https://fairsharing.org/search?recordType=terminology_artefact)  an overview of its content is provided together with separate tree-views tailored to explore its hierarch (URL_TO_INSERT_RECORD_4530 https://fairsharing.org/FAIRsharing.52b22c) ies of classes and properties. The set of available map (URL_TO_INSERT_RECORD_4529 https://fairsharing.org/FAIRsharing.53edcc) pings to other ontologies (URL_TO_INSERT_TERM_4528 https://fairsharing.org/search?recordType=terminology_artefact)  / terminologies (URL_TO_INSERT_TERM_4526 https://fairsharing.org/search?recordType=terminology_artefact)  can be explored by a custom view
   </td>
  </tr>
  <tr>
   <td><strong>Onto. search (URL_TO_INSERT_RECORD_4531 https://fairsharing.org/FAIRsharing.52b22c)  capabilities</strong>
   </td>
   <td>Search (URL_TO_INSERT_RECORD_4534 https://fairsharing.org/FAIRsharing.52b22c)  by term to gather all the ontologies (URL_TO_INSERT_TERM_4532 https://fairsharing.org/search?recordType=terminology_artefact)  where the term is found. It is possible to restrict search (URL_TO_INSERT_RECORD_4535 https://fairsharing.org/FAIRsharing.52b22c)  results to one or more ontologies (URL_TO_INSERT_TERM_4533 https://fairsharing.org/search?recordType=terminology_artefact) , to a specific type of result (i.e. class, property or individual) or to exact or partial term match
   </td>
  </tr>
  <tr>
   <td><strong>Onto. recommendation capabilities</strong>
   </td>
   <td>An ontology (URL_TO_INSERT_TERM_4536 https://fairsharing.org/search?recordType=terminology_artefact)  recommender is available: it retrieves recommendations for the most relevant ontologies (URL_TO_INSERT_TERM_4537 https://fairsharing.org/search?recordType=terminology_artefact)  based on an excerpt from a biomedical text or a list of keywords.
<p>
Recommendations are based on: (i) <em>coverage</em> of the input text / set of keywords; (ii) <em>acceptance</em> of the ontologies (URL_TO_INSERT_TERM_4540 https://fairsharing.org/search?recordType=terminology_artefact) ; (iii) <em>detail of knowledge</em> available in the ontology (URL_TO_INSERT_TERM_4538 https://fairsharing.org/search?recordType=terminology_artefact)  to describe input data and (iv) <em>specialization</em> of the ontology (URL_TO_INSERT_TERM_4539 https://fairsharing.org/search?recordType=terminology_artefact)  to the specific domain under consideration
   </td>
  </tr>
  <tr>
   <td><strong>Onto. update capabilities</strong>
   </td>
   <td>Each ontology (URL_TO_INSERT_TERM_4541 https://fairsharing.org/search?recordType=terminology_artefact)  can be manually updated by accessing the BioPortal (URL_TO_INSERT_RECORD_4543 https://fairsharing.org/FAIRsharing.4m97ah)  (URL_TO_INSERT_RECORD_4545 https://fairsharing.org/FAIRsharing.4m97ah)  or automatically updated by BioPortal (URL_TO_INSERT_RECORD_4544 https://fairsharing.org/FAIRsharing.4m97ah)  (URL_TO_INSERT_RECORD_4546 https://fairsharing.org/FAIRsharing.4m97ah)  by continuously monitoring a URL (URL_TO_INSERT_RECORD_4547 https://fairsharing.org/FAIRsharing.9d38e2)  where the ontology (URL_TO_INSERT_TERM_4542 https://fairsharing.org/search?recordType=terminology_artefact)  and its new versions are published
   </td>
  </tr>
  <tr>
   <td><strong>Onto. versioning capabilities</strong>
   </td>
   <td>Each ontology (URL_TO_INSERT_TERM_4548 https://fairsharing.org/search?recordType=terminology_artefact)  is characterized by a version number in its metadata, useful to track distinct versions of the same ontology (URL_TO_INSERT_TERM_4549 https://fairsharing.org/search?recordType=terminology_artefact) 
   </td>
  </tr>
  <tr>
   <td><strong>Description of Web based access to service</strong>
   </td>
   <td>Besides a Web-based interface that supports ontology (URL_TO_INSERT_TERM_4550 https://fairsharing.org/search?recordType=terminology_artefact)  search (URL_TO_INSERT_RECORD_4552 https://fairsharing.org/FAIRsharing.52b22c) , annotation, recommendation and map (URL_TO_INSERT_RECORD_4551 https://fairsharing.org/FAIRsharing.53edcc) ping, also a free-after-registration access by means of a REST API is provided to the users
   </td>
  </tr>
  <tr>
   <td><strong>Description of API</strong>
   </td>
   <td><a href="http://data.bioontology.org/documentation#nav_home">http://data.bioontology.org/documentation#nav_home</a>
   </td>
  </tr>
  <tr>
   <td><strong>Developer resources</strong>
   </td>
   <td>Sample code to access REST API in distinct languages is available at: <a href="https://github.com (URL_TO_INSERT_RECORD_4553 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ncbo_rest_sample_code">https://github.com (URL_TO_INSERT_RECORD_4554 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ncbo_rest_sample_code</a>
   </td>
  </tr>
  <tr>
   <td><strong>Local deploy of service</strong>
   </td>
   <td>In principle, local deploy of services is possible, even if not extensively documented. Source code (Rails) for Web UI, REST API and Linked Data management is available on NCBO (URL_TO_INSERT_RECORD_4555 https://fairsharing.org/FAIRsharing.cbz72b)  (URL_TO_INSERT_RECORD_4558 https://fairsharing.org/FAIRsharing.y2dt83)  GiHub account, <a href="https://github.com (URL_TO_INSERT_RECORD_4556 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo">https://github.com (URL_TO_INSERT_RECORD_4557 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo</a>
   </td>
  </tr>
  <tr>
   <td><strong>Source code reference</strong>
   </td>
   <td><a href="https://github.com (URL_TO_INSERT_RECORD_4559 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo">https://github.com (URL_TO_INSERT_RECORD_4560 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo</a>
   </td>
  </tr>
  <tr>
   <td><strong>Quantification of community of users</strong>
   </td>
   <td>GitHub (URL_TO_INSERT_RECORD_4561 https://fairsharing.org/FAIRsharing.c55d5e)  (URL_TO_INSERT_RECORD_4562 https://fairsharing.org/FAIRsharing.c55d5e) : 
<ul>

<li>Web UI: 12 stars and 6 forks

<li>REST API: 17 stars and 7 forks

<li>Linked Data: 10 stars and 5 forks

<p>
Twitter: 192 followers
</li>
</ul>
   </td>
  </tr>
</table>


### **OHDSI Athena** {footcite}`ohdsi_athena`

<!-- **Overview by Francesco** -->



<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td>Athena
   </td>
  </tr>
  <tr>
   <td>
<strong>Last update of this table</strong>
   </td>
   <td>14/04/2020
   </td>
  </tr>
  <tr>
   <td><strong>URL (URL_TO_INSERT_RECORD_4563 https://fairsharing.org/FAIRsharing.9d38e2) </strong>
   </td>
   <td><a href="https://www.ohdsi.org/analytic-tools/athena-standardized-vocabularies/">https://www.ohdsi.org/analytic-tools/athena-standardized-vocabularies/</a>
<p>
<a href="http://athena.ohdsi.org/">http://athena.ohdsi.org/</a>
   </td>
  </tr>
  <tr>
   <td><strong>Latest version of service / data / code (where applicable)</strong>
   </td>
   <td><em>Content</em>: last update 12 Apr 2020 11:39
<p>
<em>Code</em>: Maven PO (URL_TO_INSERT_RECORD_4564 https://fairsharing.org/FAIRsharing.3ngg40) V version (from GitHub (URL_TO_INSERT_RECORD_4565 https://fairsharing.org/FAIRsharing.c55d5e)  (URL_TO_INSERT_RECORD_4566 https://fairsharing.org/FAIRsharing.c55d5e) ): 1.10.0
<p>
<a href="https://github.com (URL_TO_INSERT_RECORD_4567 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena">https://github.com (URL_TO_INSERT_RECORD_4568 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena</a>
<p>
Latest commit on GitHub (URL_TO_INSERT_RECORD_4569 https://fairsharing.org/FAIRsharing.c55d5e)  (URL_TO_INSERT_RECORD_4570 https://fairsharing.org/FAIRsharing.c55d5e) : September 2019
   </td>
  </tr>
  <tr>
   <td><strong>Host organisation</strong>
   </td>
   <td><a href="https://www.ohdsi.org/">Observational Health Data Sciences and Informat (URL_TO_INSERT_TERM_4571 https://fairsharing.org/search?recordType=model_and_format) ics (OHD (URL_TO_INSERT_RECORD_4572 https://fairsharing.org/FAIRsharing.bg7bb6) SI) initiative</a>
   </td>
  </tr>
  <tr>
   <td><strong>Public / private</strong>
   </td>
   <td>Public
   </td>
  </tr>
  <tr>
   <td><strong>Licence</strong>
   </td>
   <td>Not explicitly specified
   </td>
  </tr>
  <tr>
   <td><strong>Domain</strong>
   </td>
   <td>Useful to browse the set of Standard (URL_TO_INSERT_TERM_4573 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabularies which are part of the OMO (URL_TO_INSERT_RECORD_4578 https://fairsharing.org/FAIRsharing.qs4x5m) P (URL_TO_INSERT_RECORD_4576 https://fairsharing.org/FAIRsharing.mct09a)  Common Data Model (URL_TO_INSERT_TERM_4574 https://fairsharing.org/search?recordType=model_and_format)  (CDM), version 5.x. They are maintained by the Observational Health Data Science and Informat (URL_TO_INSERT_TERM_4575 https://fairsharing.org/search?recordType=model_and_format) ics (OHD (URL_TO_INSERT_RECORD_4577 https://fairsharing.org/FAIRsharing.bg7bb6) SI, pronounced “Odyssey”) initiative
   </td>
  </tr>
  <tr>
   <td><strong>Set of ontologies (URL_TO_INSERT_TERM_4579 https://fairsharing.org/search?recordType=terminology_artefact)  covered</strong>
   </td>
   <td>Standard (URL_TO_INSERT_TERM_4580 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabularies which are part of the<a href="https://www.ohdsi.org/web/wiki/doku.php?id=documentation:vocabulary_etl"> OMO (URL_TO_INSERT_RECORD_4590 https://fairsharing.org/FAIRsharing.qs4x5m) P (URL_TO_INSERT_RECORD_4586 https://fairsharing.org/FAIRsharing.mct09a)  Common Data Model (URL_TO_INSERT_TERM_4581 https://fairsharing.org/search?recordType=model_and_format)  (CDM)</a>, version 5.x. It integrates several source vocabularies including UMLS, SNOME (URL_TO_INSERT_RECORD_4582 https://fairsharing.org/3502) D, RxNorm (URL_TO_INSERT_RECORD_4587 https://fairsharing.org/FAIRsharing.36pf8q) , NDF (URL_TO_INSERT_RECORD_4583 https://fairsharing.org/FAIRsharing.cfcd4r) R (URL_TO_INSERT_RECORD_4585 https://fairsharing.org/FAIRsharing.e7e609) T (URL_TO_INSERT_RECORD_4588 https://fairsharing.org/FAIRsharing.901nkj) , VA Product, VA Class, ATC (URL_TO_INSERT_RECORD_4589 https://fairsharing.org/FAIRsharing.1a27h8) , MeSH, ICD10, GCN (URL_TO_INSERT_RECORD_4584 https://fairsharing.org/FAIRsharing.b7gm54) _SEQNO, ETC, Indication, ICD9CM, ICD9Proc, ICD10CM, LOiNC, etc.
   </td>
  </tr>
  <tr>
   <td><strong>Onto. format (URL_TO_INSERT_TERM_4591 https://fairsharing.org/search?recordType=model_and_format) s supported</strong>
   </td>
   <td>Not a specific format (URL_TO_INSERT_TERM_4593 https://fairsharing.org/search?recordType=model_and_format) , a collection (URL_TO_INSERT_TERM_4592 https://fairsharing.org/search?recordType=collection)  of ontology (URL_TO_INSERT_TERM_4594 https://fairsharing.org/search?recordType=terminology_artefact)  concepts / classes assigned to a specific domain and imported from a specific source vocabulary 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. importing capabilities</strong>
   </td>
   <td>Tailored to browse the Standard (URL_TO_INSERT_TERM_4595 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabularies which are part of the OMO (URL_TO_INSERT_RECORD_4598 https://fairsharing.org/FAIRsharing.qs4x5m) P (URL_TO_INSERT_RECORD_4597 https://fairsharing.org/FAIRsharing.mct09a)  Common Data Model (URL_TO_INSERT_TERM_4596 https://fairsharing.org/search?recordType=model_and_format)  (CDM)
   </td>
  </tr>
  <tr>
   <td><strong>Onto. browsing capabilities</strong>
   </td>
   <td>Table based views are available to browse all the concepts belonging to a specific source vocabulary 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. search (URL_TO_INSERT_RECORD_4599 https://fairsharing.org/FAIRsharing.52b22c)  capabilities</strong>
   </td>
   <td>Search (URL_TO_INSERT_RECORD_4600 https://fairsharing.org/FAIRsharing.52b22c)  by term to gather all the source vocabularies where the term is found. It is possible to restrict search (URL_TO_INSERT_RECORD_4601 https://fairsharing.org/FAIRsharing.52b22c)  results by domain, class and source vocabulary
   </td>
  </tr>
  <tr>
   <td><strong>Onto. recommendation capabilities</strong>
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td><strong>Onto. update capabilities</strong>
   </td>
   <td>Each time a new version of the Standard (URL_TO_INSERT_TERM_4602 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabularies which are part of the OMO (URL_TO_INSERT_RECORD_4607 https://fairsharing.org/FAIRsharing.qs4x5m) P (URL_TO_INSERT_RECORD_4606 https://fairsharing.org/FAIRsharing.mct09a)  Common Data Model (URL_TO_INSERT_TERM_4603 https://fairsharing.org/search?recordType=model_and_format)  (CDM) is available an updated the core (URL_TO_INSERT_RECORD_4604 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_4605 https://fairsharing.org/FAIRsharing.xMmOCL)  set of concept is available
   </td>
  </tr>
  <tr>
   <td><strong>Onto. versioning capabilities</strong>
   </td>
   <td>The latest version of the Standard (URL_TO_INSERT_TERM_4608 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabulary is V5.0
   </td>
  </tr>
  <tr>
   <td><strong>Description of Web-based access to service</strong>
   </td>
   <td>Athena is a Web interface available to browse concepts of the Standard (URL_TO_INSERT_TERM_4609 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabulary (V5.0). Both search (URL_TO_INSERT_RECORD_4610 https://fairsharing.org/FAIRsharing.52b22c)  results and the whole dataset can be downloaded after registration
   </td>
  </tr>
  <tr>
   <td><strong>Description of API</strong>
   </td>
   <td>No API available
   </td>
  </tr>
  <tr>
   <td><strong>Developer resources</strong>
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td><strong>Local deploy of service</strong>
   </td>
   <td>In principle, local deploy of services is possible, even if not extensively documented. Source code on GitHub (URL_TO_INSERT_RECORD_4611 https://fairsharing.org/FAIRsharing.c55d5e)  (URL_TO_INSERT_RECORD_4612 https://fairsharing.org/FAIRsharing.c55d5e)  account <a href="https://github.com (URL_TO_INSERT_RECORD_4613 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena">https://github.com (URL_TO_INSERT_RECORD_4614 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena</a> 
   </td>
  </tr>
  <tr>
   <td><strong>Source code reference</strong>
   </td>
   <td><a href="https://github.com (URL_TO_INSERT_RECORD_4615 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena">https://github.com (URL_TO_INSERT_RECORD_4616 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena</a>
   </td>
  </tr>
  <tr>
   <td><strong>Quantification of community of users</strong>
   </td>
   <td>GitHub (URL_TO_INSERT_RECORD_4617 https://fairsharing.org/FAIRsharing.c55d5e)  (URL_TO_INSERT_RECORD_4618 https://fairsharing.org/FAIRsharing.c55d5e) : 29 stars and 6 forks
<p>
Twitter: 1.284 followers of the Observational Health Data Sciences and Informat (URL_TO_INSERT_TERM_4619 https://fairsharing.org/search?recordType=model_and_format) ics (OHD (URL_TO_INSERT_RECORD_4620 https://fairsharing.org/FAIRsharing.bg7bb6) SI) account
   </td>
  </tr>
</table>


### **Ontobee and the OBO Foundry** {footcite}`pmid27733503ontobee`

<!-- **Overview by Francesco** -->



<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td>OBO (URL_TO_INSERT_RECORD_4622 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_4623 https://fairsharing.org/FAIRsharing.cbz72b)  Foundry (URL_TO_INSERT_RECORD_4621 https://fairsharing.org/FAIRsharing.847069) 
   </td>
  </tr>
  <tr>
   <td>
<strong>Last update of this table</strong>
   </td>
   <td>14/04/2020
   </td>
  </tr>
  <tr>
   <td><strong>URL (URL_TO_INSERT_RECORD_4624 https://fairsharing.org/FAIRsharing.9d38e2) </strong>
   </td>
   <td><a href="http://www.ontobee.org (URL_TO_INSERT_RECORD_4625 https://fairsharing.org/FAIRsharing.q8fx1b) /">http://www.ontobee.org (URL_TO_INSERT_RECORD_4626 https://fairsharing.org/FAIRsharing.q8fx1b) /</a> (<a href="http://obofoundry.org/">http://obofoundry.org/</a>)
   </td>
  </tr>
  <tr>
   <td><strong>Latest version of service / data / code (where applicable)</strong>
   </td>
   <td><em>Content (OBO (URL_TO_INSERT_RECORD_4628 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_4629 https://fairsharing.org/FAIRsharing.cbz72b)  Foundry (URL_TO_INSERT_RECORD_4627 https://fairsharing.org/FAIRsharing.847069) )</em>: last update April 2020
<p>
<em>Code (Ontobee (URL_TO_INSERT_RECORD_4630 https://fairsharing.org/FAIRsharing.q8fx1b)  (URL_TO_INSERT_RECORD_4631 https://fairsharing.org/FAIRsharing.q8fx1b) )</em>: <a href="https://github.com (URL_TO_INSERT_RECORD_4632 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee">https://github.com (URL_TO_INSERT_RECORD_4633 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee</a>
<p>
Latest commit on GitHub (URL_TO_INSERT_RECORD_4634 https://fairsharing.org/FAIRsharing.c55d5e)  (URL_TO_INSERT_RECORD_4635 https://fairsharing.org/FAIRsharing.c55d5e) : August 2018
   </td>
  </tr>
  <tr>
   <td><strong>Host Organisation</strong>
   </td>
   <td><a href="http://www.hegroup.org/">He Group</a>, University of Michigan Medical School, Ann Arbor, MI, USA
   </td>
  </tr>
  <tr>
   <td><strong>Public / private</strong>
   </td>
   <td>Public
   </td>
  </tr>
  <tr>
   <td><strong>Licence</strong>
   </td>
   <td>Apache 2.0
   </td>
  </tr>
  <tr>
   <td><strong>Domain</strong>
   </td>
   <td>Ontobee (URL_TO_INSERT_RECORD_4645 https://fairsharing.org/FAIRsharing.q8fx1b)  (URL_TO_INSERT_RECORD_4646 https://fairsharing.org/FAIRsharing.q8fx1b)  has been used as the default ontology (URL_TO_INSERT_TERM_4636 https://fairsharing.org/search?recordType=terminology_artefact)  Linked Data server for most <a href="http://obofoundry.org/">Open Biological and Biomedical Ontology (URL_TO_INSERT_TERM_4637 https://fairsharing.org/search?recordType=terminology_artefact)  (OBO (URL_TO_INSERT_RECORD_4641 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_4643 https://fairsharing.org/FAIRsharing.cbz72b) ) Foundry</a> library ontologies (URL_TO_INSERT_TERM_4639 https://fairsharing.org/search?recordType=terminology_artefact) . The OBO (URL_TO_INSERT_RECORD_4642 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_4644 https://fairsharing.org/FAIRsharing.cbz72b)  Foundry (URL_TO_INSERT_RECORD_4640 https://fairsharing.org/FAIRsharing.847069)  is a collective of ontology (URL_TO_INSERT_TERM_4638 https://fairsharing.org/search?recordType=terminology_artefact)  developers that are committed to collaboration and adherence to shared principles
   </td>
  </tr>
  <tr>
   <td><strong>Set of ontologies (URL_TO_INSERT_TERM_4647 https://fairsharing.org/search?recordType=terminology_artefact)  covered</strong>
   </td>
   <td>164 active ontologies (URL_TO_INSERT_TERM_4648 https://fairsharing.org/search?recordType=terminology_artefact) , 5 orphaned ontologies (URL_TO_INSERT_TERM_4649 https://fairsharing.org/search?recordType=terminology_artefact)  and 57 inactive ontologies (URL_TO_INSERT_TERM_4650 https://fairsharing.org/search?recordType=terminology_artefact)  (in OBO (URL_TO_INSERT_RECORD_4652 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_4653 https://fairsharing.org/FAIRsharing.cbz72b)  Foundry (URL_TO_INSERT_RECORD_4651 https://fairsharing.org/FAIRsharing.847069) )
   </td>
  </tr>
  <tr>
   <td><strong>Onto. format (URL_TO_INSERT_TERM_4654 https://fairsharing.org/search?recordType=model_and_format) s supported</strong>
   </td>
   <td>OWL (URL_TO_INSERT_RECORD_4655 https://fairsharing.org/FAIRsharing.atygwy)  and OBO (URL_TO_INSERT_RECORD_4656 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_4657 https://fairsharing.org/FAIRsharing.cbz72b) 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. importing capabilities</strong>
   </td>
   <td>Ontobee (URL_TO_INSERT_RECORD_4671 https://fairsharing.org/FAIRsharing.q8fx1b)  (URL_TO_INSERT_RECORD_4672 https://fairsharing.org/FAIRsharing.q8fx1b)  can import both OWL (URL_TO_INSERT_RECORD_4662 https://fairsharing.org/FAIRsharing.atygwy)  and OBO (URL_TO_INSERT_RECORD_4665 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_4668 https://fairsharing.org/FAIRsharing.cbz72b)  ontologies (URL_TO_INSERT_TERM_4659 https://fairsharing.org/search?recordType=terminology_artefact) . New ontologies (URL_TO_INSERT_TERM_4660 https://fairsharing.org/search?recordType=terminology_artefact)  can be proposed tired to the set of OBO (URL_TO_INSERT_RECORD_4666 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_4669 https://fairsharing.org/FAIRsharing.cbz72b)  Foundry (URL_TO_INSERT_RECORD_4663 https://fairsharing.org/FAIRsharing.847069)  ontologies (URL_TO_INSERT_TERM_4661 https://fairsharing.org/search?recordType=terminology_artefact) ; a committee will review the ontology (URL_TO_INSERT_TERM_4658 https://fairsharing.org/search?recordType=terminology_artefact)  to check if it adheres to all the OBO (URL_TO_INSERT_RECORD_4667 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_4670 https://fairsharing.org/FAIRsharing.cbz72b)  Foundry (URL_TO_INSERT_RECORD_4664 https://fairsharing.org/FAIRsharing.847069)  principles
   </td>
  </tr>
  <tr>
   <td><strong>Onto. browsing capabilities</strong>
   </td>
   <td>The OBO (URL_TO_INSERT_RECORD_4681 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_4683 https://fairsharing.org/FAIRsharing.cbz72b)  Foundry (URL_TO_INSERT_RECORD_4679 https://fairsharing.org/FAIRsharing.847069)  portal provides a set of metadata describing each ontology (URL_TO_INSERT_TERM_4674 https://fairsharing.org/search?recordType=terminology_artefact)  together with the possibility to download the same ontology (URL_TO_INSERT_TERM_4675 https://fairsharing.org/search?recordType=terminology_artefact)  in several format (URL_TO_INSERT_TERM_4673 https://fairsharing.org/search?recordType=model_and_format) s. To browse ontologies (URL_TO_INSERT_TERM_4677 https://fairsharing.org/search?recordType=terminology_artefact) , the OBO (URL_TO_INSERT_RECORD_4682 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_4684 https://fairsharing.org/FAIRsharing.cbz72b)  Foundry (URL_TO_INSERT_RECORD_4680 https://fairsharing.org/FAIRsharing.847069)  portal points to the ontology (URL_TO_INSERT_TERM_4676 https://fairsharing.org/search?recordType=terminology_artefact)  browsing pages of other Web platforms including <a href="http://www.ontobee.org (URL_TO_INSERT_RECORD_4685 https://fairsharing.org/FAIRsharing.q8fx1b) /">Ontobee</a>, <a href="https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_4678 https://fairsharing.org/FAIRsharing.4m97ah) /">BioPortal</a> and the <a href="https://www.ebi.ac.uk/ols">Ontology Lookup Service</a>.
   </td>
  </tr>
  <tr>
   <td><strong>Onto. search (URL_TO_INSERT_RECORD_4686 https://fairsharing.org/FAIRsharing.52b22c)  capabilities</strong>
   </td>
   <td>The OBO (URL_TO_INSERT_RECORD_4691 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_4692 https://fairsharing.org/FAIRsharing.cbz72b)  Foundry (URL_TO_INSERT_RECORD_4690 https://fairsharing.org/FAIRsharing.847069)  portal exploits <a href="http://www.ontobee.org (URL_TO_INSERT_RECORD_4695 https://fairsharing.org/FAIRsharing.q8fx1b) /">Ontobee</a> to provide users with ontology (URL_TO_INSERT_TERM_4687 https://fairsharing.org/search?recordType=terminology_artefact)  search (URL_TO_INSERT_RECORD_4696 https://fairsharing.org/FAIRsharing.52b22c)  capabilities.Ontobee (URL_TO_INSERT_RECORD_4693 https://fairsharing.org/FAIRsharing.q8fx1b)  (URL_TO_INSERT_RECORD_4694 https://fairsharing.org/FAIRsharing.q8fx1b)  enables users to search (URL_TO_INSERT_RECORD_4697 https://fairsharing.org/FAIRsharing.52b22c)  ontology (URL_TO_INSERT_TERM_4688 https://fairsharing.org/search?recordType=terminology_artefact)  concepts by term, eventually restricting the search (URL_TO_INSERT_RECORD_4698 https://fairsharing.org/FAIRsharing.52b22c)  to a specific ontology (URL_TO_INSERT_TERM_4689 https://fairsharing.org/search?recordType=terminology_artefact) 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. recommendation capabilities</strong>
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td><strong>Onto. update capabilities</strong>
   </td>
   <td>An established <a href="http://obofoundry.org/principles/fp-004-versioning.html">PURL system to publish new versions / updates of an ontology (URL_TO_INSERT_TERM_4700 https://fairsharing.org/search?recordType=terminology_artefact) </a> is defined; new versions of an ontologies (URL_TO_INSERT_TERM_4701 https://fairsharing.org/search?recordType=terminology_artefact)  should be accessible at PURL (URL_TO_INSERT_RECORD_4702 https://fairsharing.org/FAIRsharing.3e603c)  (URL_TO_INSERT_RECORD_4703 https://fairsharing.org/FAIRsharing.9d38e2) s with the following format (URL_TO_INSERT_TERM_4699 https://fairsharing.org/search?recordType=model_and_format) : <code>http://purl.obolibrary.org/obo/idspace/YYYY-MM-DD/idspace.owl</code> or <code>.obo</code>, for instance: <code><a href="https://raw.githubusercontent.com/BiodiversityOntologies/bco/2020-03-27/bco.owl">https://raw.githubusercontent.com/BiodiversityOntologies/bco/2020-03-27/bco.owl</a></code>
   </td>
  </tr>
  <tr>
   <td><strong>Onto. versioning capabilities</strong>
   </td>
   <td>The OBO (URL_TO_INSERT_RECORD_4708 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_4710 https://fairsharing.org/FAIRsharing.cbz72b)  principles, implemented by the ontologies (URL_TO_INSERT_TERM_4705 https://fairsharing.org/search?recordType=terminology_artefact)  available in OBO (URL_TO_INSERT_RECORD_4709 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_4711 https://fairsharing.org/FAIRsharing.cbz72b)  Foundry (URL_TO_INSERT_RECORD_4707 https://fairsharing.org/FAIRsharing.847069) , enforces a system of versioning systems, with each ontology (URL_TO_INSERT_TERM_4704 https://fairsharing.org/search?recordType=terminology_artefact)  version receiving an unique identifier (URL_TO_INSERT_TERM_4706 https://fairsharing.org/search?recordType=identifier_schema)  (by means of numbers, dates, tags)
   </td>
  </tr>
  <tr>
   <td><strong>Description of Web-based access to service</strong>
   </td>
   <td>Ontobee (URL_TO_INSERT_RECORD_4713 https://fairsharing.org/FAIRsharing.q8fx1b)  (URL_TO_INSERT_RECORD_4714 https://fairsharing.org/FAIRsharing.q8fx1b)  provides a web interface that supports, besides search (URL_TO_INSERT_RECORD_4716 https://fairsharing.org/FAIRsharing.52b22c) ing for ontology (URL_TO_INSERT_TERM_4712 https://fairsharing.org/search?recordType=terminology_artefact)  concepts, the execution of SP (URL_TO_INSERT_RECORD_4717 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_4715 https://fairsharing.org/FAIRsharing.87ccfd)  queries and the annotation of text excerpts
   </td>
  </tr>
  <tr>
   <td><strong>Description of API</strong>
   </td>
   <td>No specific REST API is provided; users can retrieve both HTML (URL_TO_INSERT_RECORD_4722 https://fairsharing.org/FAIRsharing.YugnuL)  and RDF (URL_TO_INSERT_RECORD_4719 https://fairsharing.org/FAIRsharing.p77ph9)  descriptions of concepts that belongs to Ontobee (URL_TO_INSERT_RECORD_4720 https://fairsharing.org/FAIRsharing.q8fx1b)  (URL_TO_INSERT_RECORD_4721 https://fairsharing.org/FAIRsharing.q8fx1b)  ontologies (URL_TO_INSERT_TERM_4718 https://fairsharing.org/search?recordType=terminology_artefact) , in adherence to the principles of Linked Data community
   </td>
  </tr>
  <tr>
   <td><strong>Developer resources</strong>
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td><strong>Local deploy of service</strong>
   </td>
   <td>In principle, local deploy of services is possible, even if not extensively documented. Source code on GiHub account <a href="https://github.com (URL_TO_INSERT_RECORD_4723 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee">https://github.com (URL_TO_INSERT_RECORD_4724 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee</a>
   </td>
  </tr>
  <tr>
   <td><strong>Source code reference</strong>
   </td>
   <td><a href="https://github.com (URL_TO_INSERT_RECORD_4725 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee">https://github.com (URL_TO_INSERT_RECORD_4726 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee</a>
   </td>
  </tr>
  <tr>
   <td><strong>Quantification of community of users</strong>
   </td>
   <td>GitHub (URL_TO_INSERT_RECORD_4727 https://fairsharing.org/FAIRsharing.c55d5e)  (URL_TO_INSERT_RECORD_4728 https://fairsharing.org/FAIRsharing.c55d5e) : 12 stars and 4 forks
<p>
Twitter OBO (URL_TO_INSERT_RECORD_4729 https://fairsharing.org/FAIRsharing.847069)  (URL_TO_INSERT_RECORD_4730 https://fairsharing.org/FAIRsharing.cbz72b) F (URL_TO_INSERT_RECORD_4731 https://fairsharing.org/FAIRsharing.rnckxp)  (URL_TO_INSERT_RECORD_4732 https://fairsharing.org/FAIRsharing.t6y94s) oundry account: 220 followers
   </td>
  </tr>
</table>



## References
````{dropdown} **References**
```{footbibliography}
```
````



## Authors

````{authors_fairplus}
Francesco: Writing - Original Draft
Ashni: Writing - Original Draft
Kurt: Writing - Original Draft
Philippe: Writing - Review & Editing
````


## License

````{license_fairplus}
CC-BY-4.0
````
