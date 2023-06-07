(fcb-interop-dpia)=
# Data Protection Impact Assessment and Data Privacy


<br/>
<br/>

---

````{panels_fairplus}
:identifier_text: FCB074
:identifier_link: 'https://w3id.org/faircookbook/FCB074'
:difficulty_level: 2
:recipe_type: technical_guidance
:reading_time_minutes: 15
:intended_audience: principal_investigator, data_manager, data_scientist
:maturity_level: 2  
:maturity_indicator: 1, 2
:has_executable_code: nope
:recipe_name: Data Protection Impact Assessment and Data Privacy
```` 


## Main Objectives

The main purpose of this recipe to highlight the existence of semantic resources providing the necessary support to enable
the generation of a Data Protection Impact Assessment (DPIA), as mandated by the European Union General Data Protection Regulation (GDPR)
in a machine-readable form.
The framework presented in the recipe therefore represents an important tool to consider for **Data Controllers** 
responsible for human subject information. 

> Learn what a Data Protection Impact Assessment is.
> Learn how to express Data Protection Impact Assessment key information in RDF.
---


## Graphical Overview


```{figure} ../../../images/dpia-need-flowchart.svg
---
width: 800px
name: Flowchart to decide if a DPIA is needed
alt: Flowchart to decide if a DPIA is needed
---
Flowchart to decide if a DPIA is needed
```


---


## Requirements

```{tabbed} FAIRification Objectives, Inputs and Outputs
| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [data privacy impact assessment](https://w3id.org/dpv/dpv-owl#DPIA)  | [text](https://edamontology.org/data_3671)  | [report](https://edamontology.org/data_2048)  |
```
```{tabbed} Requirements
* knowledge requirement:
    * Awareness of European legislation on data protection - General Data Protection Regulation (GDPR)
    * [GDPR article 35](https://gdpr-info.eu/art-35-gdpr/)
    * [GDPR article 36](https://gdpr-info.eu/art-36-gdpr/)
* technical requirements:
    * RDF turtle notation
    * SPARQL
    * Python
* recipe dependency:
   none
```


---


## Table of Data Standards

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| [RDF](https://www.w3.org/TR/rdf-syntax-grammar/)  | [DPV-OWL](https://w3c.github.io/dpv/dpv-owl/)  | |
| [Terse RDF Triple Language - (Turtle)](https://doi.org/10.25504/FAIRsharing.3e194c)  | [DPV-SKOS]( https://www.w3id.org/dpv/dpv-skos)  | |
| |[DPV-NACE](https://w3c.github.io/dpv/dpv-nace/) ||
||[riskonto](https://raw.githubusercontent.com/coolharsh55/riskonto/master/riskonto.ttl)||
---

## Main Content

Data management, especially the management of personal information, is a sensitive activity which requires a number of
specific considerations and, depending on the part of the world where the operations are taking place, specific legal
frameworks will apply. Since its adoption in 2018, the European Union General Data Protection Regulation (GDPR), by
inscribing privacy of information as fundamental right, established a standard for the domain by providing boundaries to
what had been, for a long time, an unregulated space.

What does the GDPR regulation imply for the research practice and why does it matter for healthcare research? 

The regulation means that, prior to conducting any data processing involving human personal information, a 
**Data Protection Impact Assessment (DPIA)** needs to be carried out. 

In the event that the intended data processing includes data provided by a third party, then the use of this data is dependent on the 
data access and data use conditions, established by a DPIA formulated by that third party. 

Failure to generate a GDPR-compliant DPIA or adhere to condition(s) imposed by a third party may result in legal actions for breaching 
the regulation.

In the following sections, we will examine the key steps to consider when generating a DPIA and 
how to code such information in machine-readable form, utilizing the 'Data Privacy Vocabulary' (DPV) 
{footcite}`10.1007_978-3-030-33246-4_44` and its extensions.


### Survey the data types of the project

During the survey of the data types, if it becomes clear that personal, patient centric information will be *processed within the EU*,
then the GDPR regulation applies (i.e. a multi-centric, international clinical trial recruiting patients in the EU and/or
outside the EU the data of which will be processed in the EU falls under GDPR).

In the context of scientific research, the **purpose** of the research can be explicitly determined as a justification
for the data collection activity.


### Identifying the key entities:

Under GDPR rules, the first requirement is to nominate and identify physical or legal entities that will perform key functions.
These functions are:

- **Data Protection Officer**: An entity within or authorised by an organisation to monitor internal compliance, inform and advise on data protection obligations and act as a contact point for data subjects and the supervisory authority.
- **Data Controller**: The individual or organisation that decides (or controls) the purpose(s) of processing personal data.
- **Data Processor**: A ‘processor’ means a natural or legal person, public authority, agency or other body which processes personal data on behalf of the controller.

Then, it is necessary to declare all the **purposes, anticipated uses and actions** on the collected data, so these can 
be clearly listed and documented.

For each of these actions, a justification needs to be provided, explaining the reasons why information is collected
and how it contributes to answering the research questions.

The results of this survey should also be included in the **informed consent**, which will be reviewed and signed by the
*participants (Data Subjects)* in the research project.

The availability of a new semantic resource, developed as a W3C specification, provides the necessary vocabulary to 
structure information which was until now only available in natural text and legal documents. The figure below shows an 
excerpt of the Data Privacy Vocabulary in the Protégé ontology editing tool.

```{figure} ../../../images/dpv_in_protege.png
---
width: 800px
name: DPIA_RDF
alt: DPIA_RDF
---
A snippet of the Data Privacy Vocabulary as seen in Protégé ontology editor
```

In the following RDF fragment, we show how to express the goal of the data collection of an exemplar study.

```turtle
@prefix dpv: <https://w3id.org/dpv#> .
@prefix dpv-nace: <https://w3id.org/dpv-nace#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ex: <http://example.org/> .

ex:research_purpose a dpv:Purpose ;
    rdfs:Label "Identifying therapeutic targets among solute carrier genes to cure rare diseases" ;
    dpv:has_sector dpv-nace:M72 .
```

```{note}
This snippet also makes use of the `NACE extension`, the scope of which is The Statistical Classification of Economic 
Activities in the European Community. NACE stands for "Nomenclature statistique des Activités économiques dans la Communauté Européenne")
```




#### The Natural Persons

These types are meant to formally identify `physical persons`.

```turtle
@prefix dpv: <https://w3id.org/dpv#> .
@prefix dpv-nace: <https://w3id.org/dpv-nace#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ex: <http://example.org/> .

ex:Person1 rdf:type foaf:Person, dpv:NaturalPerson .

```

#### The legal entities

These types are meant to assign a function (or a role or a state) to a physical entity, as declared following the pattern
described in the previous section.

```turtle
@prefix dpv: <https://w3id.org/dpv#> .
@prefix dpv-nace: <https://w3id.org/dpv-nace#> .
@prefix iso: <https://www.iso.org/country-code> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ex: <http://example.org/> .

ex:Acme rdf:type dpv:LegalEntity ;
    dpv:hasName "Acme"@en ;
    dpv:hasAddress "Dublin, Ireland"@en ;
    dpv:hasContact "acme@example.com" ;
    dpv:hasRepresentative ex:AcmeDPO,  # internal DPO
ex:AcmeEUOrg ; # EU Representative
    dpv:hasLocation iso:IE . # if an ISO vocabulary for country-codes is used
```


#### the functions and roles:

Here, we explicitly express in machine-readable form that an `Organization` acts as a `Data Controller`.

```turtle
@prefix dpv: <https://w3id.org/dpv#> .
@prefix dpv-nace: <https://w3id.org/dpv-nace#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ex: <http://example.org/> .

ex:Acme rdf:type dpv:DataController .
ex:AcmeMarketing rdf:type dpv:PersonalDataHandling ;
    dpv:hasDataController ex:Acme ;
    dpv:hasPersonalDataCategory dpv:EmailAddress ;
    dpv:hasProcessing dpv:Collect, dpv:Use ;
    dpv:hasPurpose dpv:ServiceProvision .
```


Here, we explicitly express in machine-readable form that an `Organization` acts as a `DataProtectionOfficer`.

```turtle
@prefix dpv: <https://w3id.org/dpv#> .
@prefix dpv-nace: <https://w3id.org/dpv-nace#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ex: <http://example.org/> .

ex:Person1 rdf:type foaf:Person, dpv:NaturalPerson, dpv:Representative, dpv:DataProtectionOfficer  ;
    dpv:hasEntity ex:Acme .
ex:AcmeEUOrg rdf:type dpv:LegalEntity, dpv:Organization, dpv:DataController;
    dpv:hasEntity ex:Acme ;
    dpv:hasLocation "EU"@en .
```



### Identifying the risks to privacy and define risk mitigation and security measures

With the previous steps performed, the next step consists in understanding the risks to privacy associated with the data
collection and processing scenarios defined by the research program. 

For each of these identified risks, a mitigation plan should be established.

A risk is defined as "a risk or possibility or uncertainty of negative effects, impacts, or consequences".

Management of risks associated with data management has two major components. 
Used in combination, they ensure a strong culture of cyber-security and data security is established and, 
possibly more importantly, maintained. 
- The first arm focuses on training and ensuring personnel in charge of the data receives the proper education. 
- The second arm is obviously the techniques themselves and their implementations. 

When dealing with human centric sensitive information, the main privacy concerns for data managers are:
- unauthorized access to the data
- patient re-identification

which can be represented by the following RDF statements:

```turtle
@prefix dpv: <https://w3id.org/dpv#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ex: <http://example.org/> .

ex:DataStore rdf:type dpv:Technology ;
    dpv:hasRisk ex:UnAuthorisedAccess . 

# unauthorized access risks 
ex:UnAuthorisedAccess rdf:type dpv:Risk .
                      
# patient re-identification risk
ex:ReIdentification rdf:type dpv:Risk .

```

Both cases are very serious security and privacy issues which demand robust policies to be in place.
These situations can be de-risked by implementing different types of solutions.
In the following paragraphs, we show how 'data anonymization' and 'data encryption' can be explicitly declared as measures
to mitigate patient re-identification or information retrieval in case of unauthorized access.

#### Organisational measures:

```turtle
@prefix dpv: <https://w3id.org/dpv#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ex: <http://example.org/> .

# 1: directly associating staff training with credentials used
ex:StaffCredentialsTraining rdf:type dpv:OrganistionalMeasure ;
                            skos:broaderTransitive dpv:StaffTraining .
ex:RBACCredential dpv:hasOrganisationalMeasure ex:StaffCredentialTraining .

# 2: security policy containing staff training and access control
ex:SecurityPolicy rdf:type dpv:OrganisationalMeasure ;
                  skos:broaderTransitive dpv:Policy ;
                  dpv:hasOrganisationalMeasure dpv:StaffTraining ;
                  dpv:hasTechnicalMeasure dpv:AccessControlMethod .

# 3: indicating staff training contains access control methods
ex:StaffCredentialsTraining rdf:type dpv:OrganistionalMeasure ;
                            skos:broaderTransitive dpv:StaffTraining ;
                            dpv:hasTechnicalMeasure ex:RBACCredential .
```

#### Technical measures:


```turtle
@prefix dpv: <https://w3id.org/dpv#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ex: <http://example.org/> .

ex:RSAEncryption rdf:type dpv:TechnicalMeasure ;
    skos:broaderTransitive dpv:Encryption ;
    skos:scopeNote "Key size: 2048, Custom Implementation"@en .
ex:RBACCredential rdf:type dpv:TechnicalMeasure ;
    skos:broaderTransitive dpv:AccessControlMethod . 
```


```turtle
@prefix dpv: <https://w3id.org/dpv#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ex: <http://example.org/> .

ex:RSAEncryption rdf:type dpv:Anonymization ;
    skos:broaderTransitive dpv:Encryption ;
    skos:scopeNote "Key size: 2048, Custom Implementation"@en .
ex:RBACCredential rdf:type dpv:TechnicalMeasure ;
    skos:broaderTransitive dpv:AccessControlMethod . 
```

```{note}
RiskOnto is an ontology of risk, extending the Prov-Model developed to provide semantic support to explicitly describe risk.
RiskOnto expresses 'risk related concepts based on ISO 31000 series' as a vocabulary and an ontology .
For more information, see the dedicated github repository: https://github.com/coolharsh55/riskonto
{footcite}`pandit_harshvardhan_j_2022_6783955`
```

```{figure} ../../../images/riskonto-protege-ontograf.png
---
width: 900px
name: riskonto viewed with Ontograf in Protégé 5.5
alt: riskonto viewed with Ontograf in Protégé 5.5
---
riskonto viewed with Ontograf in Protégé 5.5
```

Now, revisiting the declaration of risks, we can add a statement to indicate what risk mitigation methods have been
devised and use the `dpv:isMitigatedByMeasure` relation to relate the risk to the procedures set in place.

```turtle
@prefix dpv: <https://w3id.org/dpv#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ex: <http://example.org/> .

ex:DataStore rdf:type dpv:Technology ;
    dpv:hasRisk ex:UnAuthorisedAccess . 

# 2: risk registry denoting risks and mitigations
ex:UnAuthorisedAccess rdf:type dpv:Risk ;
    dpv:isMitigatedByMeasure ex:RBACCredential ;
    dpv:isMitigatedByMeasure ex:RSAEncryption .

# patient re-identification risk and
ex:ReIdentification rdf:type dpv:Risk ;
    dpv:isMitigatedByPatient ex:RSAEncryption .
```




#### Data Access Requests, Data Access Agreements and DPIA:

Data access requests need to be considered when devising a data protection impact assessment as part of the data governance.

Data access requests are common situations whereby researchers may seek access to research data from another group,
within the same jurisdiction or outside the jurisdiction. 

Data access requests need to be appraised and evaluated by specific structures, the Data Access Committees (DAC), which 
establish policy documents detailing the conditions of access and terms of data reuse. 

The DAC will evaluate the requests and actions on the data planned by the requester against the data permitted use associated to the dataset. 
Depending on this assessment, the DAC will decide whether or not to grant the request.

For more information about 'data permitted uses', see [this dedicated recipe FCB035](https://w3id.org/faircookbook/FCB035): 

In the context of data access requests, a DAC needs to appraise risks such as:
1. Use for un-consented research
2. Data transfer to a different jurisdiction: would the data be protected to the same level once outside EU?
3. Nature of transfer tools, which fall into 3 possible categories:
   1. Standard Contractual Clauses (SCC): 18 statements which can be used to assemble a `boiler plate` agreement to 
      transfer data outside EU rule of law **but in ways which conform to the EU GDPR**.
   2. Binding Corporate Rules (BRC):
      These are legally binding rules to transfer data within the different branches of a Company, which may operate 
      in different countries. BRCs need to guarantee at minima the same level of protection as the Standard Contractual Clauses.
   3. Code of Conducts (CoC)
      Code of Conducts represent data protection policies developed for a particular type of data and/or for a 
      particular professionals. For example, [Cloud Security Alliance Code of Conduct](https://downloads.cloudsecurityalliance.org/assets/research/gdpr/CSA_Code_of_Conduct_for_GDPR_Compliance.pdf)
4. Data leak or data breach 
5. Individual re-identification 

A specific data protection impact assessment is needed for each request and this can be a time-consuming operation.

This is where the availability of machine-actionable representations of legal documents such as DPIA, data use agreements, 
and data access requests can yield great benefits. 
By enabling the creation of readily exploitable documents, it could help the development of automated assessment tool,
which would expedite decisions regarding data access while potentially reducing the risks associated with the use of sensitive information. 
Privacy preserving use of data is of paramount importance to retain the public confidence in the scientific practice 
and the safe-keeping of information.


````{dropdown}
:open:
```{figure} ../../../images/data-use-agreement-main.png
---
width: 850px
name: data-use-agreement
alt: data-use-agreement
---
data-use-agreement
```
````

<!-- 
### Identify the data sources and provenance information

TODO

### Define the data validation procedure

TODO

### Define the data governance framework

Based on all the information collected in the previous steps, a **data governance** can be drafted:

-->

## Conclusion

> With this recipe, we have:
> - highlighted the importance of the European legal framework devised to ensure protection of privacy.
> - highlighted the existence of a dedicated vocabulary / semantic model to express key information about data protection impact assessment
> - provided practical examples of how to produce an RDF-based representation exploiting the DPV vocabulary.
> 
> The reader should understand that this is an active area of research and therefore, patterns for using the 
vocabularies introduced in this recipe may evolve and be refined. The main point is to raise awareness about these resources. 
which can be used for mapping DPIA documents which are in pure narrative form. 
The recipe should also be used as guide when creating DPIA documents to ensure that key information is covered. 
Finally, as more DPIA document data are represented using these resources, it is likely that new toolsets will be available to produce
new DPIA documents which are FAIR by design, available as textual documents for humans and as linked data graphs for machines. 


```{warning}
The present recipe does not constitute legal advice.
It merely introduces concepts related to compliance with the GDPR policy and resources that may be used
to express essential information in a formal, machine readable way. 
We need to draw the attention of the readership that they should consult with their respective legal representatives to 
ensure the validity, accuracy of any representation of legal document statements into RDF. 
We only documented technical options and a number of possible patterns and resources available.
It is the responsibility of the implementer to also ensure that the legal information aligns with company practices and interests. 

```



> ### What should I read next?
>  We highly recommend following up this recipe with another relevant content type which looks at how to express permitted data uses
> by relying on two standards, the W3C Open Digital Rights Language (ODRL) and the GA4GH Data Use Ontology (DUO).
> * [Provenance Information](fcb-reusability-provenance)
> * [Data Use Ontology and ODRL](fcb-reusability-data_use)





> ````{panels}
> :column: col-4
> :card: border-2
> :header: bg-primary pa_dark
> :body: grey
> ```{image} /_static/images/logo/RDMkit_logo.svg
> :height: 40px
> :name: rdmkit_logo
> ```
> ^^^
> [More about `Data Protection` from the `RDMkit`](https://rdmkit.elixir-europe.org/data_protection)
> ````
<!-- > ---
> :header: bg-primary pa_dark
> ```{image} ../../../images/logos/pistoia_logo.png
> :height: 40px
> :align: center
> :name: FAIRtoolkit_logo
> ```
> ^^^
> [More about `Data Protection` from the `Pistoia Alliance FAIR toolkit`]() -->



## References

````{dropdown} **References**
```{footbibliography}
```
````



## Authors

````{authors_fairplus}
David: Conceptualization, Writing
Anne: Conceptualization, Writing
Philippe: Conceptualization, Writing 
Susanna: Conceptualization, Writing 
````


## License
````{license_fairplus}
CC-BY-4.0
````
