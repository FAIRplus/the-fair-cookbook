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

This recipe provides **guidance on the selection and exploitation of ontology lookup services** . 

>* **[Objective of the recipe: introduction to ontology lookup services](#heading=h.bb3h294tvdau)**
>
>* **[Selecting an ontology lookup service](#bookmark=id.okwm6u2vsbft)**
>
>* **[Overview of widespread ontology lookup services](#bookmark=id.x42hawpkzgd3)**

An ***ontology lookup service*** 
refers to *any type of application, standalone or Web-based, that enables the use of existing ontologies to support knowledge 
formalization and sharing, by fostering ontology-based descriptions of knowledge*. 




Tools useful to build, edit or maintain ontologies are not considered ontology lookup services and thus are out of the scope of this recipe. 

In essence, an ontology lookup service is a platform that provides users with the possibility to **search in a set of
ontologies, the most suitable concepts to describe the semantics of a piece of knowledge of interest,
usually available in the form of one or more keywords or a text excerpt**. 

Most ontology lookup services are available as Web applications: most of them also support programmatic access to their 
capabilities by means of (REST) APIs. Ontology lookup services can vary in the features that are provided, but often include:



* **Complex searching for concepts of interest**: most services implement advanced search features (i.e. scoping the search to specific ontologies or to specific parts of an ontology) or allow users to specify fine-grained patterns to aggregate or restrict the scope of search results.
* **Advanced browsing capabilities**, to explore the contents of a specific ontology by means of custom data navigation widgets such as tree-based views.
* **Managing distinct versions** of an ontology and alert its users when specific concepts become obsolete. 
* **Importing** user-provided ontologies, giving consumers the ability to leverage a service for other terminologies beyond those included.
* Programmatic means to **access and deploy instances of the ontology lookup service in the premises of its users** represents another differentiating feature, using relevant documentation.
* **Recommending ontologies** based on the input of a given term, with ontologies ranked according to custom-weighted criteria.
* Access to an **active user community** that supports and exploits a specific ontology lookup service, serving as an indication of widespread adoption and selection.

This recipe presents guidelines and relevant considerations when choosing an ontology lookup service, followed by
overview of existing public ontology lookup services and a comparison of their core features.


## Selecting An Ontology Lookup Service

This section provides guidelines and suggestions on how to select and leverage an ontology lookup service, on the basis
of the knowledge needs and ontology use patterns that characterize a specific knowledge-intensive project. 

Several aspects to consider when choosing an ontology lookup service are derived based on a series of commonly asked questions;



* **Is the set of ontologies incorporated in the ontology lookup service suitable to formally describe the knowledge domain my project is interested in?**

    Ontology lookup services usually provide access and enable users to search and reference classes and properties of _a specific set of ontologies related to a specific knowledge domain_ (i.e. biomedical knowledge).
    When choosing an ontology lookup service it is important to verify whether the ontologies covered by a specific service are suitable to describe the content of our knowledge-intensive project. 
    Besides, a list of the ontologies covered, and interactive widgets to explore such ontologies (e.g. tree-based views), 
    some ontology lookup services also provide _ontology recommendation capabilities:_ given some “sample” 
    (i.e. text excerpt or list of keywords) of the knowledge we need to describe by means of available ontologies, 
    the ontology lookup service ‘recommender’ suggests which are the best ontologies to use to this propose.

* **Do I need to consider / rely on private ontologies in my project? Do I need to use ontologies that are not already 
    imported and thus available in the ontology lookup service of my choice?**

    Some ontology lookup services enable users to import external (i.e. user-provided) ontologies in order to incorporate
    the content of these ontologies in their search and recommendation capabilities. 
    This feature could represent a key factor to consider when choosing an ontology lookup service since several 
    knowledge-intensive projects rely on private ontologies or need to consider a set of additional ontologies not 
    natively covered by a specific ontology lookup service.

* **Because of data privacy or data protection issues, do I need to use an instance of the ontology lookup service that
is deployed locally on my private computing infrastructure?**

    Several ontology-lookup services provide the possibility to deploy the service on the private computing 
    infrastructure of its users. This feature would be particularly relevant when private ontologies are adopted in a 
    knowledge-intensive project.

* **Which are the usage patterns I will rely on in order to exploit the ontology lookup service? Will the 1)
massive and systematic exploitation of the ontology search, 2) the recommendation features of the ontology lookup
service or 3) the integration of its capabilities in more complex systems, require the possibility to programmatically 
access the service by means of an application programming interface (API)?**

    Ontology lookup services usually provide a (Web-based) user interface as the preferred way to interact with them to
    browse and search for ontologies, or recommend relevant concepts to describe contents of interest. 
    In several scenarios, the possibility to programmatically interact with ontology lookup services would be extremely
    valuable; to this purpose, several ontology-lookup services implement an API (mostly based on REST interactions)
    that enable the user to programmatically invoke the majority of ontology search features of the same service. 
    In order to simplify the integration of the ontology lookup service support into external applications,  
   several-ontology lookup services provide users with language-specific clients to interact with them through their API. 

* **Is the distribution license of the ontology lookup service compatible with the way I plan to exploit the 
features provided the same service in my project or with the way I plan to integrate the same service in my project?**

    The licencing terms of the ontology lookup service of choice intended for use in a given context and 
    knowledge-intensive project, is a key consideration when selecting an ontology lookup service: available 
    ontology lookup services range from open-source applications to commercial tools, and it is best to choose one with funding in mind.

* **Does the ontology lookup service manage ontology versioning and updates so that I can easily reflect any ontology 
update into my knowledge-intensive project? **

    Ontologies and terminologies usually evolve over time: when a new, updated version of an ontology used in a 
    knowledge-intensive project becomes available, best practice suggests that we should also update the part of our 
    projects that rely on such ontology. Some ontology lookup services implement specific procedures and tools to manage
    and propagate ontology updates; the availability of such tools would simplify the implementation of changes deriving
    from ontology updates in the projects under consideration.

* **Is the ontology lookup service supported by an active community of developers
or by an active company? Which are the available channels I can rely on to receive support on the usage and integration 
of the ontology lookup service?**

    The support of an active community of developers and users is a key aspect to take into account when choosing an 
    ontology lookup service. This could be quantified by evaluating several factors of an ontology lookup service including:
    (i) availability of mailing or support lists; (ii) for open-source projects, using metrics such as the star-rating,
    the number of forks and followers and the frequency of commits of the project on the code-sharing platform used 
    (e.g. GitHub); (iii) size of the community of users of the ontology lookup service (e.g. how many followers on social
    media accounts, how many clients advertised on the Website).

## Key Selection Criteria

The above questions have highlighted 20 factors which should be taken into account when choosing a service. 
These factors can be categorised into 3 groups; **ontology information, functionality** and **interfaces**, and include;

### **Ontology Information**



1. **URL**: the main URL where the ontology lookup service can be accessed
2. **Latest version of service / data / code (where applicable**): the most recent version of both the content (i.e. ontologies) and the code of the ontology lookup service
3. **Host Organisation**: the organisation responsible for the maintenance of the ontology lookup service
4. **Public / private**: is the ontology lookup service a public or private infrastructure?
5. **Licence**: the licence that regulates the use and cost of the ontology lookup service
6. **Domain**: which is the knowledge domain covered by the ontologies referenced in the ontology lookup service?
7. **Quantification of community of users**: objective measures to quantify the community of users supporting and consuming an ontology lookup service, including: number of stars and forks on GitHub, number of social media followers

### **Functionality**



8. **Number and complexity of ontologies covered**: how many ontologies does the ontology lookup service cover and how complex are they?
9. **Ontology formats supported**: which ontology formats are supported by the ontology lookup service?
10. **Ontology importing capabilities**: if and how ontologies can be imported and thus indexed by the ontology lookup service?
11. **Ontology browsing capabilities**: which interaction patterns are available to browse the set of ontologies contemplated by the ontology lookup service?
12. **Ontology search capabilities**: which search patterns are provided by the ontology lookup service to identify the best concept useful to represent the semantic of a term? When searching against a term, does the ontology give an indication of whether the term has been derived from a different ontology?
13. **Ontology recommendation capabilities**: does the ontology lookup service provide users with a recommendation concerning the most suitable ontologies to semantically characterize the contents of some text / a set of keywords? 
14. **Ontology update capabilities**: how are terms and/or relationships updated in a given ontology and how is this governed? Is this an automatic or manual update and what happens to terms that are considered obsolete?
15. **Ontology versioning capabilities**: are there predefined patterns to identify, manage and compare distinct versions of an ontology? 

### **Interfaces**



16. **Description of Web-based access to service**: which ontology browsing  and search patterns are available to the (Web-based) user interface of the ontology lookup service? Does the ontology lookup service also provide programmatic access to its data and services (e.g. by means of a REST API)?
17. **Description of API**: reference to the documentation of the (REST) API provided by the ontology lookup service, if any
18. **Developer resources**: description of resources provided to developers in order to ease the programmatic access to the features of the ontology lookup service (i.e. libraries to query the REST API from a specific programming language).
19. **Local deploy of service**: possibility to locally deploy the ontology lookup service
20. **Source code reference**: if available, link to the source code of the ontology lookup service
4. **Overview of Widespread Ontology Lookup Services**

---

Here, we have used the selection criteria above to provide an overview and comparison of four widespread ontology lookup services, namely:



-  [EBI Ontology Lookup Service](https://www.ebi.ac.uk/ols/index)
-  [BioPortal](https://bioportal.bioontology.org)
-  [OHDSI Athena](https://athena.ohdsi.org/search-terms/start)
-  [Ontobee and the OBO Foundry](http://www.ontobee.org)

The results of the analysis can be found below, else in tabular format [here](https://docs.google.com/spreadsheets/d/1kn1oEhsYJPiLI5gA12B1UsbLBRoSLGbOYcOMDG4614o/edit#gid=0).

Note, the _‘last update of this table_’ field provides the date on which the ontology lookup service was last assessed.

### **The EBI Ontology Lookup Service** {footcite}`pmid20460452`

<!-- **Overview by Francesco** -->


<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td>Ontology Lookup Service
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
   <td><strong>URL</strong>
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/index">https://www.ebi.ac.uk/ols/index</a>
   </td>
  </tr>
  <tr>
   <td><strong>Latest version of service / data / code (where applicable)</strong>
   </td>
   <td>Content: last update 12 Apr 2020 11:39
<p>
Code: Maven POV version (from GitHub): 3.2.1-SNAPSHOT
<p>
<a href="https://github.com/EBISPOT/OLS">https://github.com/EBISPOT/OLS</a>
<p>
Last commit on GitHub: April 2020
   </td>
  </tr>
  <tr>
   <td><strong>Host organisation</strong>
   </td>
   <td><a href="http://www.ebi.ac.uk/about/spot-team">Samples, Phenotypes and Ontologies Team</a> at EMBL-EBI
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
   <td>A repository for biomedical ontologies that aims to provide a single point of access to the latest ontology versions
   </td>
  </tr>
  <tr>
   <td><strong>Set of ontologies covered</strong>
   </td>
   <td>245 ontologies / 6,119,228 terms / 27,778 properties / 485,541 individuals
<p>
Whole list at: <a href="https://www.ebi.ac.uk/ols/ontologies">https://www.ebi.ac.uk/ols/ontologies</a>
   </td>
  </tr>
  <tr>
   <td><strong>Onto. formats supported</strong>
   </td>
   <td>OWL 2 and OBO
   </td>
  </tr>
  <tr>
   <td><strong>Onto. importing capabilities</strong>
   </td>
   <td>By means of a local installation it is possible to import ontologies in OWL 2 and OBO format
   </td>
  </tr>
  <tr>
   <td><strong>Onto. browsing capabilities</strong>
   </td>
   <td>Tree-view based browsing of hierarchies of classes and properties of ontologies. The modifications added by different version of each ontology are shown by means of distinct background colors in ontology browsing tree-views
   </td>
  </tr>
  <tr>
   <td><strong>Onto. search capabilities</strong>
   </td>
   <td>Search by term to gather all the ontologies where the term is found. It is possible to restrict search results to one or more ontologies, to a specific type of result (i.e. class, property or individual) or to exact or partial term match
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
   <td>OLS updates nightly to always provide the latest ontology versions
   </td>
  </tr>
  <tr>
   <td><strong>Onto. versioning capabilities</strong>
   </td>
   <td>Obsoleted ontology terms are spotted by means of a boolean flag (is_obsolete)
   </td>
  </tr>
  <tr>
   <td><strong>Description of Web-based access to service</strong>
   </td>
   <td>Besides a Web-based user interface useful to browse ontologies and search for ontology concepts, free-access by means of a REST API is provided to the users
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
   <td><a href="https://github.com/EBISPOT/OLS">https://github.com/EBISPOT/OLS</a>
   </td>
  </tr>
  <tr>
   <td><strong>Quantification of community of users</strong>
   </td>
   <td>GitHub: 49 stars and 19 forks
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
   <td>Bioportal 
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
   <td><strong>URL</strong>
   </td>
   <td><a href="https://bioportal.bioontology.org/">https://bioportal.bioontology.org/</a>
   </td>
  </tr>
  <tr>
   <td><strong>Latest version of service / data / code (where applicable)</strong>
   </td>
   <td><em>Content</em>: last update 12 Apr 2020 11:39
<p>
<em>Code</em>: 
<ul>

<li>Web UI: <a href="https://github.com/ncbo/bioportal_web_ui">https://github.com/ncbo/bioportal_web_ui</a>

<li>REST API: <a href="https://github.com/ncbo/ontologies_api">https://github.com/ncbo/ontologies_api</a>

<li>Linked Data: <a href="https://github.com/ncbo/ontologies_linked_data">https://github.com/ncbo/ontologies_linked_data</a>

<p>
Latest commit on GitHub: April 2020
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td><strong>Host organisation</strong>
   </td>
   <td><a href="https://ncbo.bioontology.org/about-ncbo">U.S. National Center for Biomedical Ontology</a>
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
   <td>Available at: <a href="https://github.com/ncbo/ontologies_api/blob/master/LICENSE.txt">https://github.com/ncbo/ontologies_api/blob/master/LICENSE.txt</a>
   </td>
  </tr>
  <tr>
   <td><strong>Domain</strong>
   </td>
   <td>A Web-based application for searching, sharing, visualizing, and analyzing a large repository of biomedical ontologies, terminologies, and ontology-based annotations
   </td>
  </tr>
  <tr>
   <td><strong>Set of ontologies covered</strong>
   </td>
   <td>Ontologies: 842 / Classes: 11,324,508 
<p>
Whole list at: <a href="https://bioportal.bioontology.org/ontologies">https://bioportal.bioontology.org/ontologies</a>
   </td>
  </tr>
  <tr>
   <td><strong>Onto. formats supported</strong>
   </td>
   <td>OWL, OBO, SKOS
   </td>
  </tr>
  <tr>
   <td><strong>Onto. importing capabilities</strong>
   </td>
   <td>It is possible to upload / submit new ontologies or new versions of existing ontologies that will be indexed in BioPortal. Ontology metadata will be provided in the <a href="http://omv.ontoware.org">Ontology Metadata Vocabulary</a> (OMV) format
   </td>
  </tr>
  <tr>
   <td><strong>Onto. browsing capabilities</strong>
   </td>
   <td>For each ontology / terminology an overview of its content is provided together with separate tree-views tailored to explore its hierarchies of classes and properties. The set of available mappings to other ontologies / terminologies can be explored by a custom view
   </td>
  </tr>
  <tr>
   <td><strong>Onto. search capabilities</strong>
   </td>
   <td>Search by term to gather all the ontologies where the term is found. It is possible to restrict search results to one or more ontologies, to a specific type of result (i.e. class, property or individual) or to exact or partial term match
   </td>
  </tr>
  <tr>
   <td><strong>Onto. recommendation capabilities</strong>
   </td>
   <td>An ontology recommender is available: it retrieves recommendations for the most relevant ontologies based on an excerpt from a biomedical text or a list of keywords.
<p>
Recommendations are based on: (i) <em>coverage</em> of the input text / set of keywords; (ii) <em>acceptance</em> of the ontologies; (iii) <em>detail of knowledge</em> available in the ontology to describe input data and (iv) <em>specialization</em> of the ontology to the specific domain under consideration
   </td>
  </tr>
  <tr>
   <td><strong>Onto. update capabilities</strong>
   </td>
   <td>Each ontology can be manually updated by accessing the BioPortal or automatically updated by BioPortal by continuously monitoring a URL where the ontology and its new versions are published
   </td>
  </tr>
  <tr>
   <td><strong>Onto. versioning capabilities</strong>
   </td>
   <td>Each ontology is characterized by a version number in its metadata, useful to track distinct versions of the same ontology
   </td>
  </tr>
  <tr>
   <td><strong>Description of Web based access to service</strong>
   </td>
   <td>Besides a Web-based interface that supports ontology search, annotation, recommendation and mapping, also a free-after-registration access by means of a REST API is provided to the users
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
   <td>Sample code to access REST API in distinct languages is available at: <a href="https://github.com/ncbo/ncbo_rest_sample_code">https://github.com/ncbo/ncbo_rest_sample_code</a>
   </td>
  </tr>
  <tr>
   <td><strong>Local deploy of service</strong>
   </td>
   <td>In principle, local deploy of services is possible, even if not extensively documented. Source code (Rails) for Web UI, REST API and Linked Data management is available on NCBO GiHub account, <a href="https://github.com/ncbo">https://github.com/ncbo</a>
   </td>
  </tr>
  <tr>
   <td><strong>Source code reference</strong>
   </td>
   <td><a href="https://github.com/ncbo">https://github.com/ncbo</a>
   </td>
  </tr>
  <tr>
   <td><strong>Quantification of community of users</strong>
   </td>
   <td>GitHub: 
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
   <td><strong>URL</strong>
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
<em>Code</em>: Maven POV version (from GitHub): 1.10.0
<p>
<a href="https://github.com/OHDSI/Athena">https://github.com/OHDSI/Athena</a>
<p>
Latest commit on GitHub: September 2019
   </td>
  </tr>
  <tr>
   <td><strong>Host organisation</strong>
   </td>
   <td><a href="https://www.ohdsi.org/">Observational Health Data Sciences and Informatics (OHDSI) initiative</a>
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
   <td>Useful to browse the set of Standardized Vocabularies which are part of the OMOP Common Data Model (CDM), version 5.x. They are maintained by the Observational Health Data Science and Informatics (OHDSI, pronounced “Odyssey”) initiative
   </td>
  </tr>
  <tr>
   <td><strong>Set of ontologies covered</strong>
   </td>
   <td>Standardized Vocabularies which are part of the<a href="https://www.ohdsi.org/web/wiki/doku.php?id=documentation:vocabulary_etl"> OMOP Common Data Model (CDM)</a>, version 5.x. It integrates several source vocabularies including UMLS, SNOMED, RxNorm, NDFRT, VA Product, VA Class, ATC, MeSH, ICD10, GCN_SEQNO, ETC, Indication, ICD9CM, ICD9Proc, ICD10CM, LOiNC, etc.
   </td>
  </tr>
  <tr>
   <td><strong>Onto. formats supported</strong>
   </td>
   <td>Not a specific format, a collection of ontology concepts / classes assigned to a specific domain and imported from a specific source vocabulary 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. importing capabilities</strong>
   </td>
   <td>Tailored to browse the Standardized Vocabularies which are part of the OMOP Common Data Model (CDM)
   </td>
  </tr>
  <tr>
   <td><strong>Onto. browsing capabilities</strong>
   </td>
   <td>Table based views are available to browse all the concepts belonging to a specific source vocabulary 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. search capabilities</strong>
   </td>
   <td>Search by term to gather all the source vocabularies where the term is found. It is possible to restrict search results by domain, class and source vocabulary
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
   <td>Each time a new version of the Standardized Vocabularies which are part of the OMOP Common Data Model (CDM) is available an updated the core set of concept is available
   </td>
  </tr>
  <tr>
   <td><strong>Onto. versioning capabilities</strong>
   </td>
   <td>The latest version of the Standardized Vocabulary is V5.0
   </td>
  </tr>
  <tr>
   <td><strong>Description of Web-based access to service</strong>
   </td>
   <td>Athena is a Web interface available to browse concepts of the Standardized Vocabulary (V5.0). Both search results and the whole dataset can be downloaded after registration
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
   <td>In principle, local deploy of services is possible, even if not extensively documented. Source code on GitHub account <a href="https://github.com/OHDSI/Athena">https://github.com/OHDSI/Athena</a> 
   </td>
  </tr>
  <tr>
   <td><strong>Source code reference</strong>
   </td>
   <td><a href="https://github.com/OHDSI/Athena">https://github.com/OHDSI/Athena</a>
   </td>
  </tr>
  <tr>
   <td><strong>Quantification of community of users</strong>
   </td>
   <td>GitHub: 29 stars and 6 forks
<p>
Twitter: 1.284 followers of the Observational Health Data Sciences and Informatics (OHDSI) account
   </td>
  </tr>
</table>


### **Ontobee and the OBO Foundry** {footcite}`pmid27733503ontobee`

<!-- **Overview by Francesco** -->



<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td>OBO Foundry
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
   <td><strong>URL</strong>
   </td>
   <td><a href="http://www.ontobee.org/">http://www.ontobee.org/</a> (<a href="http://obofoundry.org/">http://obofoundry.org/</a>)
   </td>
  </tr>
  <tr>
   <td><strong>Latest version of service / data / code (where applicable)</strong>
   </td>
   <td><em>Content (OBO Foundry)</em>: last update April 2020
<p>
<em>Code (Ontobee)</em>: <a href="https://github.com/OntoZoo/ontobee">https://github.com/OntoZoo/ontobee</a>
<p>
Latest commit on GitHub: August 2018
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
   <td>Ontobee has been used as the default ontology Linked Data server for most <a href="http://obofoundry.org/">Open Biological and Biomedical Ontology (OBO) Foundry</a> library ontologies. The OBO Foundry is a collective of ontology developers that are committed to collaboration and adherence to shared principles
   </td>
  </tr>
  <tr>
   <td><strong>Set of ontologies covered</strong>
   </td>
   <td>164 active ontologies, 5 orphaned ontologies and 57 inactive ontologies (in OBO Foundry)
   </td>
  </tr>
  <tr>
   <td><strong>Onto. formats supported</strong>
   </td>
   <td>OWL and OBO
   </td>
  </tr>
  <tr>
   <td><strong>Onto. importing capabilities</strong>
   </td>
   <td>Ontobee can import both OWL and OBO ontologies. New ontologies can be proposed tired to the set of OBO Foundry ontologies; a committee will review the ontology to check if it adheres to all the OBO Foundry principles
   </td>
  </tr>
  <tr>
   <td><strong>Onto. browsing capabilities</strong>
   </td>
   <td>The OBO Foundry portal provides a set of metadata describing each ontology together with the possibility to download the same ontology in several formats. To browse ontologies, the OBO Foundry portal points to the ontology browsing pages of other Web platforms including <a href="http://www.ontobee.org/">Ontobee</a>, <a href="https://bioportal.bioontology.org/">BioPortal</a> and the <a href="https://www.ebi.ac.uk/ols">Ontology Lookup Service</a>.
   </td>
  </tr>
  <tr>
   <td><strong>Onto. search capabilities</strong>
   </td>
   <td>The OBO Foundry portal exploits <a href="http://www.ontobee.org/">Ontobee</a> to provide users with ontology search capabilities.Ontobee enables users to search ontology concepts by term, eventually restricting the search to a specific ontology
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
   <td>An established <a href="http://obofoundry.org/principles/fp-004-versioning.html">PURL system to publish new versions / updates of an ontology</a> is defined; new versions of an ontologies should be accessible at PURLs with the following format: <code>http://purl.obolibrary.org/obo/idspace/YYYY-MM-DD/idspace.owl</code> or <code>.obo</code>, for instance: <code><a href="https://raw.githubusercontent.com/BiodiversityOntologies/bco/2020-03-27/bco.owl">https://raw.githubusercontent.com/BiodiversityOntologies/bco/2020-03-27/bco.owl</a></code>
   </td>
  </tr>
  <tr>
   <td><strong>Onto. versioning capabilities</strong>
   </td>
   <td>The OBO principles, implemented by the ontologies available in OBO Foundry, enforces a system of versioning systems, with each ontology version receiving an unique identifier (by means of numbers, dates, tags)
   </td>
  </tr>
  <tr>
   <td><strong>Description of Web-based access to service</strong>
   </td>
   <td>Ontobee provides a web interface that supports, besides searching for ontology concepts, the execution of SPARQL queries and the annotation of text excerpts
   </td>
  </tr>
  <tr>
   <td><strong>Description of API</strong>
   </td>
   <td>No specific REST API is provided; users can retrieve both HTML and RDF descriptions of concepts that belongs to Ontobee ontologies, in adherence to the principles of Linked Data community
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
   <td>In principle, local deploy of services is possible, even if not extensively documented. Source code on GiHub account <a href="https://github.com/OntoZoo/ontobee">https://github.com/OntoZoo/ontobee</a>
   </td>
  </tr>
  <tr>
   <td><strong>Source code reference</strong>
   </td>
   <td><a href="https://github.com/OntoZoo/ontobee">https://github.com/OntoZoo/ontobee</a>
   </td>
  </tr>
  <tr>
   <td><strong>Quantification of community of users</strong>
   </td>
   <td>GitHub: 12 stars and 4 forks
<p>
Twitter OBOFoundry account: 220 followers
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
