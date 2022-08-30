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

Another goal of this recipe is to highlight the existence of a semantic resource providing the necessary support to enable
the structuring of regulatory compliant information in a machine-readable form.

The framework therefore represents an important resource to consider for anyone in charge of such aspects of data management.

> Learn to provide a Data Protection Impact Assessment Report in RDF.

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

Data management, especially the data management of personal information, is a sensitive activity which require a number of
specific considerations to be taken and depending on part of the world where the operations are taking place, specific legal
frameworks will apply. Since its adoption in 2018, the European Union General Data Protection Regulation (GDPR) by
inscribing privacy of information as fundamental right, trail blazes the domain by providing boundaries to what has been 
for a long time an unregulated space.

What does the GDPR imply for the Research practice and why does it matter for Healthcare Research? 
The regulation means that prior to conducting any data collection, a **Data Protection Impact Assessment (DPIA)** needs to be carried out. The
Failing to do so may result in research proposals to be turned down or fines issued to failure to respect the regulation.

In the following sections, we will examine the key steps which needs to be considered when performing a DPIA and 
on how to code such information in machine-readable form thanks to the 'Data Privacy Vocabulary' and its extensions 
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

In this step, if it becomes clear that patient centric and personal information will be collected and patients are citizens of EU country
then the GDPR regulation applies.

In the context of scientific research, the **purpose** of the research can be explicitly determined as a justification for the data colletion activity.

```turtle
@prefix dpv: <https://w3id.org/dpv#> .
@prefix dpv-nace: <https://w3id.org/dpv-nace#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ex: <http://example.org/> .

ex:research_purpose a dpv:Purpose ;
    rdfs:Label "Identifying therapeutic targets among solute carrier genes to cure rare diseases" ;
    dpv:has_sector dpv-nace:M72 .
```

### Understand the legal restrictions of the project

Under GDPR rules, the first requirement is to nominate and identify physical or legal entities which will perform key functions.
These functions are:

- Data Protection Officer: An entity within or authorised by an organisation to monitor internal compliance, inform and advise on data protection obligations and act as a contact point for data subjects and the supervisory authority.
- Data Controller: The individual or organisation that decides (or controls) the purpose(s) of processing personal data.
- Data Processor: A ‘processor’ means a natural or legal person, public authority, agency or other body which processes personal data on behalf of the controller.
- Data Subject: The individual (or category of individuals) whose personal data is being processed.

Then, it is necessary to declare all the anticipated use and action on the collected data, so these can be clearly listed and documented.
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

With the previous steps performed, the next step consists in understanding the risks to privacy associated with the data collection and processing Scenarios
defined by the research program. For each of these identified risks, a mitigation plan must be established.

a risk is defined as "A risk or possibility or uncertainty of negative effects, impacts, or consequences".


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

Situations can be de-risked by implementing technical solutions. In the following snippets, we show how 'data anonymization'
and 'data encryption' are explicitly declared as means to prevent patient re-identification or information retrieval in case of unauthorized access,

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
ex:UnAuthorisedAccess rdf:type dpv:Risk ;
    dpv:isMitigatedByMeasure ex:RBACCredential .
```

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



#### DPIA in the context of Data Access Agreement:

Data access requests need to be considered when devising a data protection impact assessment as part of the data governance

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

TODO



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


> ### What should I read next?
>  We highly recommend following up this recipe with another relevant content type which looks at how to express permitted data uses
> by relying on two standards, the W3C Open Digital Rights Language (ODRL) and the GA4GH Data Use Ontology (DUO).
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

