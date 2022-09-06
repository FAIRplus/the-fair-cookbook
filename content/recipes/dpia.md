(fcb-interop-dpia)=
# Data Protection Impact Assessment and Data Privacy


<br/>
<br/>

---

````{panels_fairplus}
:identifier_text: FCB0xx
:identifier_link: 'https://w3id.org/faircookbook/FCB0xx'
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

The main purpose of this recipe is raise awareness in the importance of *data protection*, *data privacy* and the \
european regulatory framework ruling over data management.
In particular when dealing with human subject information, especially in the context of medical or clinical information, 
a number of procedures need to be in place upstream and downstream of data collection.

Another goal of this recipe is to highlight the existence of semantic resources providing the necessary support to enable
the structuring of regulatory compliant information in a machine-readable form. The framework therefore represents an
important tool to consider for anyone in charge of such aspects of data management.

> Learn  about to provide a Data Protection Impact Assessment.
> Learn  about expressing key information of Data Protection Impact Assessment Report in RDF.
---


## Graphical Overview

```{note} 
use this section to provide a decision tree for the overall process described in the recipe
For more information about the syntax used to generate the diagram, please refer to the [following documentation](https://mermaid-js.github.io/mermaid/#/flowchart)
```

```{figure} ./reusability/images/dpia-process-overview.png
---
width: 800px
name: DPIA_overview-TODO
alt: DPIA_overview-TODO
---
DPIA_overview-TODO
```



---


## Requirements

```{tabbed} FAIRification Objectives, Inputs and Outputs
| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [data privacy impact assessment](https://w3id.org/dpv/dpv-owl#DPIA)  | [text](http://edamontology.org/data_3671)  | [report](http://edamontology.org/data_2048)  |
```
```{tabbed} Requirements
* knowledge requirement:
    * Awareness of european legislation on data protection - General Data Protection Regulation (GDPR)
    * [GDPR article 35](https://gdpr-info.eu/art-35-gdpr/)
    * [GDPR article 36](https://gdpr-info.eu/art-36-gdpr/)
* technical requirements:
    * RDF turtle notation
    * python
* recipe dependency:
   none
```


---


## Table of Data Standards

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| [RDF](https://www.w3.org/TR/rdf-syntax-grammar/)  | [DPV-OWL](https://w3c.github.io/dpv/dpv-owl/)  | |
| [Terse RDF Triple Language - (Turtle)](https://doi.org/10.25504/FAIRsharing.3e194c)  | [DPV-SKOS]( https://www.w3id.org/dpv/dpv-skos)  | |
| |[DPV-NACE]https://w3c.github.io/dpv/dpv-nace/) ||
||[riskonto](https://raw.githubusercontent.com/coolharsh55/riskonto/master/riskonto.ttl)||
---

## Main Content

Data management, especially the data management of personal information, is a sensitive activity which requireS a number of
specific considerations to be taken and depending on part of the world where the operations are taking place, specific legal
frameworks will apply. Since its adoption in 2018, the European Union General Data Protection Regulation (GDPR), by
inscribing privacy of information as fundamental right, trail blazes the domain by providing boundaries to what has been 
for a long time an unregulated space.

What does the GDPR regulation imply for the research practice and why does it matter for healthcare research? 
The regulation means that prior to conducting any data collection involving human personal information, a 
**Data Protection Impact Assessment (DPIA)** needs to be carried out. 
Failing to do so may result in research proposals to be turned down or fines issued to failure to respect the regulation.

In the following sections, we will examine the key steps to consider when performing a DPIA and 
how to code such information in machine-readable form thanks to the 'Data Privacy Vocabulary' (DPV) and its extensions 
{footcite}`10.1007_978-3-030-33246-4_44`



```{figure} ./reusability/images/dpv_in_protege.png
---
width: 800px
name: DPIA_RDF
alt: DPIA_RDF
---
DPIA_RDFe
```


### Survey the data types of the project

During the survey of the data types, if it becomes clear that patient centric and personal information will be collected and patients are citizens of EU country
then the GDPR regulation applies.
In the context of scientific research, the **purpose** of the research can be explicitly determined as a justification for the data collection activity.

```turtle
@prefix dpv: <https://w3id.org/dpv#> .
@prefix dpv-nace: <https://w3id.org/dpv-nace#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ex: <http://example.org/> .

ex:research_purpose a dpv:Purpose ;
    rdfs:Label "Identifying therapeutic targets among solute carrier genes to cure rare diseases" ;
    dpv:has_sector dpv-nace:M72 .
```


There are then 2 situations regarding the origin of the data, i.e. its provenance:

1. The data is generated internally.
In this case, and if it involved sensitive information, it is necessary to obtain informed consent from all participants, and this should cover aspect of permitted use.

2. The data is aggregated from external sources. 
In this case, concerns should be about the availability of permitted data uses and licenses as well as a description of the 



### Understand the legal restrictions of the project

Under GDPR rules, the first requirement is to nominate and identify physical or legal entities that will perform key functions.
These functions are:

- **Data Protection Officer**: An entity within or authorised by an organisation to monitor internal compliance, inform and advise on data protection obligations and act as a contact point for data subjects and the supervisory authority.
- **Data Controller**: The individual or organisation that decides (or controls) the purpose(s) of processing personal data.
- **Data Processor**: A ‘processor’ means a natural or legal person, public authority, agency or other body which processes personal data on behalf of the controller.
- **Data Subject**: The individual (or category of individuals) whose personal data is being processed.

Then, it is necessary to declare all the **anticipated uses and actions88 on the collected data, so these can be clearly listed and documented.
For each of these actions, a justification needs to be provided, explaining the reasons why information is collected and how it participates to
answering the research questions.

The goal of this survey is to be able to produce a consent form which can be reviewed and understood by the *Participant* to a research project.


#### The physical entities

```turtle
@prefix dpv: <https://w3id.org/dpv#> .
@prefix dpv-nace: <https://w3id.org/dpv-nace#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ex: <http://example.org/> .

ex:Person1 rdf:type foaf:Person, dpv:DataOwner .
ex:Organization1 rdf:type foaf:Organization, dpv:DataOwner .
ex:Organization2 rdf:type foaf:Organization, dpv:DataController .
```

#### The legal entities

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
@prefix ex: <http://example.org/> .

ex:Wolfgang_Rhim rdf:type dpv:Representative, dpv:DataProtectionOfficer  ;
    dpv:hasEntity ex:Acme .
ex:AcmeEUOrg rdf:type dpv:LegalEntity;
    dpv:hasEntity ex:Acme ;
    dpv:hasLocation "EU"@en .
```



### Identify the risks to privacy and define risk mitigation and security measures

With the previous steps performed, the next step consists in understanding the risks to privacy associated with the data
collection and processing scenarios defined by the research program. 

For each of these identified risks, a mitigation plan must be established.

A risk is defined as "a risk or possibility or uncertainty of negative effects, impacts, or consequences".

Management of risks associated with data management has two major components. Used in combination, they ensure a strong culture 
of cyber-security and data security is established and, possibly more importantly, maintained. 
The first arm focuses on training and ensuring personnel in charge of data receives the proper education. 
The second arm is obviously the techniques themselves and their implementations. 
 

#### organisational measures:


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

Situations can be de-risked by implementing technical solutions.

When dealing with human centric sensitive information, the main privacy concerns for data managers are:
- unauthorized access to the data
- patient re-identification


Step 1: Defining the risk

```turtle
@prefix dpv: <https://w3id.org/dpv#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ex: <http://example.org/> .

ex:DataStore rdf:type dpv:Technology ;
    dpv:hasRisk ex:UnAuthorisedAccess . 

# 2: risk registry denoting risks and mitigations
ex:UnAuthorisedAccess rdf:type dpv:Risk .
                      
# patient re-identification risk and
ex:ReIdentification rdf:type dpv:Risk .

```


Both cases are very serious security and privacy issues which demand robust policies to be in place. In the following
snippets, we show how 'data anonymization' and 'data encryption' are explicitly declared as means to prevent
patient re-identification or information retrieval in case of unauthorized access.



Step 2: Providing the means to mitigate the risk

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

```{figure} ./reusability/images/riskonto-protege-ontograf.png
---
width: 900px
name: riskonto viewed with Ontograf in Protégé 5.5
alt: riskonto viewed with Ontograf in Protégé 5.5
---
riskonto viewed with Ontograf in Protégé 5.5
```

Now, revisiting the declaration of risks, we can now added a statement to indicate what risk mitigation methods have been
devised and use the `dpv:isMitigatedByMeasure` relation.

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

Data access requests are common situations whereby researchers may seek access to research data from another group, within the same jurisdiction or 
outside the jurisdiction. 

Data access requests need to be appraised and evaluated by specific committees overseeing such tasks: Data Access Committees (DAC).

The DAC will evaluate the request and actions on the data planned by the requester against the data permitted use associated to the dataset. 
Depending on this assessment, the DAC will decide whether or not to grant the request.

For more information about 'data permitted uses', see this recipe: 

In the context of data access requests, the DAC needs to appraise the associated risks, which can range from:
1. use for un-consented research
2. data transfer to a different jurisdiction: would the data be protected to the same level once outside EU ?
3. nature of transfer tools
   1. Standard Contractual Clauses (SCC): 18 statements which can be used to assemble a `boiler plate` agreement to 
      transfer data outside EU rule of law but in ways which conform to GDPR.
   2. Binding Corporate Rules (BRC)
      These are legally binding rules to transfer data within the different branches of a Company, which may operate in different countries. 
      BRCs need to guarantee at minima the same level of protection as the Standard Contractual Clauses.
   3. Code of Conducts (CoC)
      Code of Conducts represent data protection policies developed for a particular type of data and/or for a particular professionals.
      For example, [Cloud Security Alliance Code of Conduct](https://downloads.cloudsecurityalliance.org/assets/research/gdpr/CSA_Code_of_Conduct_for_GDPR_Compliance.pdf)
4. data leak or data breach 
5. individual re-identification 

Therefore, a specific data protection impact assessment is needed for each request and this can be a time-consuming operation.

This is where the availability of i.) DPIA, ii.) data use agreements and iii.) data access requests in machine-readable form can be greatly beneficial. 
They can support the development of automated assessment tool which can speed up decision regarding data access and reduce potentially the risks associated with use of
sensitive information. Privacy preserving use of data is of paramount importance as to not erode public confidence.


````{dropdown}
:open:
```{figure} ./reusability/images/data-use-agreement-main.png
---
width: 850px
name: data-use-agreement
alt: data-use-agreement
---
data-use-agreement
```
````
### Identify the data sources and provenance information

TODO

### Define the data validation procedure

TODO

### Define the data governance framework

Based on all the information collected in the previous steps, a **data governance** can be drafted:



## Conclusion

> With this recipe, we have:
> - highlighted the importance of the European legal framework devised to ensure protection of privacy.
> - pointed to the existence of dedicated vocabulary / semantic model to report and structure key information around data protection
> - provided practical examples of how to convert an Excel template guiding the data protection impact assessment into an 
> RDF based representation exploiting the vocabulary mentioned above.
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
ensure the validatity, accurracy of any representation of legal document statements into RDF. 
We only documented technical options and a number of possible patterns and resources available.
It is the responsibility of the implementer to also ensure that the legal information aligns with company practices and interests. 

```



> ### What should I read next?
>  We highly recommend following up this recipe with another relevant content type which looks at how to express permitted data uses
> by relying on two standards, the W3C Open Digital Rights Language (ODRL) and the GA4GH Data Use Ontology (DUO).
> * [Provenance Information](fcb-reusability-provenance)
> * [Data use Ontology and ODRL](fcb-reusability-data_use)





> ````{panels}
> :column: col-4
> :card: border-2
> :header: bg-primary pa_dark
> :body: grey
> ```{image} ../../images/logos/RDMkit_logo.svg
> :height: 40px
> :name: rdmkit_logo
> ```
> ^^^
> [More about `Data Protection` from the `RDMkit`](https://rdmkit.elixir-europe.org/data_protection)
> ---
> :header: bg-primary pa_dark
> ```{image} ../../images/logos/pistoia_logo.png
> :height: 40px
> :align: center
> :name: FAIRtoolkit_logo
> ```
> ^^^
> [More about `Data Protection` from the `Pistoia Alliance FAIR toolkit`]()
> ````


## References:

````{dropdown} **References**
```{footbibliography}
```
````



## Authors

````{authors_fairplus}
Philippe: Conceptualization, Writing 
Susanna: Conceptualization, Writing 
Anne: Conceptualization, Reviewing
David: Reviewing

````


## License
````{license_fairplus}
CC-BY-4.0
````

