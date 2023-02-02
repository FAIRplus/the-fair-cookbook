(fcb-select-onto-service-criteria)=
# Portals and lookup services



````{panels_fairplus}
:identifier_text: FCB003
:identifier_link: 'https://w3id.org/faircookbook/FCB003'
:difficulty_level: 2
:recipe_type: technical_guidance
:reading_time_minutes: 20
:intended_audience: data_manager, data_scientist, terminology_manager, system_administrator  
:maturity_level: 0
:maturity_indicator: 0
:has_executable_code: nope
:recipe_name: Introducing vocabulary portals and lookup services
```` 

## Main Objective

This recipe provides guidance on making a decision about the feasibility of a local deployment of existing open source
ontology (URL_TO_INSERT_TERM_3599 https://fairsharing.org/search?recordType=terminology_artefact)  service software. 

By the expression **"ontology (URL_TO_INSERT_TERM_3600 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3601 https://fairsharing.org/FAIRsharing.Mkl9RR) "**, we refer **to any type of application, 
standalone or Web-based, that enables the use of existing ontologies (URL_TO_INSERT_TERM_3602 https://fairsharing.org/search?recordType=terminology_artefact)  to support knowledge formalization and sharing,
by fostering ontology (URL_TO_INSERT_TERM_3603 https://fairsharing.org/search?recordType=terminology_artefact) -based descriptions of knowledge**.

Therefore, tools useful to build, edit or maintain ontologies (URL_TO_INSERT_TERM_3604 https://fairsharing.org/search?recordType=terminology_artefact)  
are not considered as ontology (URL_TO_INSERT_TERM_3605 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3606 https://fairsharing.org/FAIRsharing.Mkl9RR) s and thus are out of the scope of this document.

The recipe will:

- define the most common selection criteria to be considered
- provide general selection recommendations
- provide recommendations for applying those selection criteria
- give an overview about the most common open source ontology (URL_TO_INSERT_TERM_3607 https://fairsharing.org/search?recordType=terminology_artefact)  service software

## Software selection criteria

This section presents the minimal criteria to take in account when analyzing alternatives for ontology (URL_TO_INSERT_TERM_3608 https://fairsharing.org/search?recordType=terminology_artefact) -based services
development and deployment. Additional criteria, including a more detailed analysis of technical features can be found 
on the resources mentioned in section **Additional resources**.

### Functionality

Functionality of a software determines the range of capabilities and functions it can perform. 
Please note that specific functional selection criteria are beyond the scope of this recipe.
Because functionality plays a very important role in the overall selection process it was added to show how it relates
to the technical & arch (URL_TO_INSERT_RECORD_3609 https://fairsharing.org/FAIRsharing.52b22c) itecture selection process.  
Functional selection criteria are covered by Recipe [FCB004](https://w3id.org (URL_TO_INSERT_RECORD_3610 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB004   ) 

### Interfaces

Interfaces allow read or write data from outside the ontology (URL_TO_INSERT_TERM_3611 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3612 https://fairsharing.org/FAIRsharing.Mkl9RR)  either by a human being or application.

For an ontology (URL_TO_INSERT_TERM_3613 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3614 https://fairsharing.org/FAIRsharing.Mkl9RR)  the most important interface features are:

- Supported import and export ontology (URL_TO_INSERT_TERM_3616 https://fairsharing.org/search?recordType=terminology_artefact)  format (URL_TO_INSERT_TERM_3615 https://fairsharing.org/search?recordType=model_and_format) s, e.g. OWL (URL_TO_INSERT_RECORD_3618 https://fairsharing.org/FAIRsharing.atygwy)  for uploading and downloading of ontologies (URL_TO_INSERT_TERM_3617 https://fairsharing.org/search?recordType=terminology_artefact) .
- Flexible query interface, e.g. to answer very specific ontology (URL_TO_INSERT_TERM_3619 https://fairsharing.org/search?recordType=terminology_artefact)  questions or to extend functional gaps of the ontology (URL_TO_INSERT_TERM_3620 https://fairsharing.org/search?recordType=terminology_artefact)  service.
Currently, the most prominent query interface is SP (URL_TO_INSERT_RECORD_3622 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_3621 https://fairsharing.org/FAIRsharing.87ccfd)  endpoint.
- Application Programming Interface (API) technology, if you want to integrate other applications with the ontology (URL_TO_INSERT_TERM_3623 https://fairsharing.org/search?recordType=terminology_artefact)  
lookup service it is essential that you can use widely used and supported technical standard (URL_TO_INSERT_TERM_3624 https://fairsharing.org/search?fairsharingRegistry=Standard) s. 
Currently, the most prominent API technology is REST API. 

Please note that this recipe does not focus on specific interface functionality. It looks at interfaces only from an
arch (URL_TO_INSERT_RECORD_3625 https://fairsharing.org/FAIRsharing.52b22c) itectural and technical view. 

## Software Architecture

The software arch (URL_TO_INSERT_RECORD_3626 https://fairsharing.org/FAIRsharing.52b22c) itecture shows the used hardware and software components and their relationship.

Regarding ontology (URL_TO_INSERT_TERM_3627 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3628 https://fairsharing.org/FAIRsharing.Mkl9RR)  selection the most important arch (URL_TO_INSERT_RECORD_3629 https://fairsharing.org/FAIRsharing.52b22c) itectural aspects are:

- *Overall arch (URL_TO_INSERT_RECORD_3630 https://fairsharing.org/FAIRsharing.52b22c) itecture complexity*
It gives you an idea whether the complexity is appropriate for solving your requirements.
If you are trying to solve simple requirements with a very complex solution you might be on the wrong way. 
- *Used tools and programming languages*
It gives you an idea what knowledge you will need for supporting the system or extending the functionality. 
You also get an overview of the impact to the overall complexity of the IT tools and programming languages used in your organization.
- *Modularity*
It gives you an idea whether you could replace few of the components by software/hardware preferred as standard (URL_TO_INSERT_TERM_3631 https://fairsharing.org/search?fairsharingRegistry=Standard)  in your company.
It can give you also a hint, whether you can scale the application by adding more hardware/software resources.

## Deployment model

The deployment model (URL_TO_INSERT_TERM_3632 https://fairsharing.org/search?recordType=model_and_format)  shows where and how the software can be installed and who owns the service.

Regarding ontology (URL_TO_INSERT_TERM_3633 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3634 https://fairsharing.org/FAIRsharing.Mkl9RR)  selection the most important deployment aspects are:

- **On premise versus cloud deployment**
Depending on your organisation policies (URL_TO_INSERT_TERM_3635 https://fairsharing.org/search?fairsharingRegistry=Policy)  and best practices, it might be the case that you want to install and maintain 
the software on your own infrastructure (***on premise***) or you prefer to buy it as a service on the cloud. 
- ** **Manual** versus **containerized** versus **virtual image** installation**
    - With a **manual installation**, you have full control over the installation, but you need typically more time. 
      - A **virtual image installation**` bundles software together with the operating system, so it is easier to install,
  but typically you would need additional infrastructure and knowledge in your organisation to maintain all virtual images.
    - A **docker based installation** is also easy to install and typically saves more hardware resources than a virtual
  image installation, because you share the operating system amongst multiple docker applications.
  Similar to virtual image installation you would need additional infrastructure and knowledge in your organisation to
  run and maintain all docker images.

## Hardware and software requirements

The hardware requirements have mainly an impact on the costs. The software requirements have an impact on knowledge 
and costs (e.g. licences for operating systems).

The specific requirements of your organisation for data processing and storage will also influence the costs.

### License model

The license model (URL_TO_INSERT_TERM_3636 https://fairsharing.org/search?recordType=model_and_format)  defines the consumer rights and the usage costs.

So it is essential that the licence model (URL_TO_INSERT_TERM_3637 https://fairsharing.org/search?recordType=model_and_format) :

- matches with your intended use 
- produces costs that  are acceptable for your organisation from a price/performance point of view.

### Database Technology for storing knowledge representation resources

The **terminology (URL_TO_INSERT_TERM_3639 https://fairsharing.org/search?recordType=terminology_artefact)  database (URL_TO_INSERT_TERM_3638 https://fairsharing.org/search?fairsharingRegistry=Database) ** is a central component of knowledge management stack as it will store the ontologies (URL_TO_INSERT_TERM_3640 https://fairsharing.org/search?recordType=terminology_artefact) . 

The database (URL_TO_INSERT_TERM_3641 https://fairsharing.org/search?fairsharingRegistry=Database)  system will typically also have a major impact on performance and scalability, because the bulk of ontology (URL_TO_INSERT_TERM_3642 https://fairsharing.org/search?recordType=terminology_artefact) 
query processing will take place within the database (URL_TO_INSERT_TERM_3643 https://fairsharing.org/search?fairsharingRegistry=Database)  system.

An ontology (URL_TO_INSERT_TERM_3646 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3647 https://fairsharing.org/FAIRsharing.Mkl9RR)  is defined to be **database (URL_TO_INSERT_TERM_3644 https://fairsharing.org/search?fairsharingRegistry=Database)  agnostic** if its database (URL_TO_INSERT_TERM_3645 https://fairsharing.org/search?fairsharingRegistry=Database)  component:

- provides interfaces that use standard (URL_TO_INSERT_TERM_3648 https://fairsharing.org/search?fairsharingRegistry=Standard)  communication protocols.
- provides a configurable access to the database (URL_TO_INSERT_TERM_3649 https://fairsharing.org/search?fairsharingRegistry=Database) . 
- allows any database (URL_TO_INSERT_TERM_3651 https://fairsharing.org/search?fairsharingRegistry=Database)  product supporting a specific standard (URL_TO_INSERT_TERM_3650 https://fairsharing.org/search?fairsharingRegistry=Standard) s(e.g. SQL, SP (URL_TO_INSERT_RECORD_3653 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_3652 https://fairsharing.org/FAIRsharing.87ccfd) ) to be used

A database (URL_TO_INSERT_TERM_3655 https://fairsharing.org/search?fairsharingRegistry=Database)  agnostic ontology (URL_TO_INSERT_TERM_3657 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3658 https://fairsharing.org/FAIRsharing.Mkl9RR)  software will give you therefore the maximum freedom to use your defined database (URL_TO_INSERT_TERM_3656 https://fairsharing.org/search?fairsharingRegistry=Database)  type standard (URL_TO_INSERT_TERM_3654 https://fairsharing.org/search?fairsharingRegistry=Standard) .

#### Relational databases:
- For storing metadata representable in flat taxonomies often Relational Database (URL_TO_INSERT_TERM_3659 https://fairsharing.org/search?fairsharingRegistry=Database)  Management Systems (RDBMS) are used 
which represent data in tabular format (URL_TO_INSERT_TERM_3660 https://fairsharing.org/search?recordType=model_and_format) .

#### Graph databases
From an ontology (URL_TO_INSERT_TERM_3661 https://fairsharing.org/search?recordType=terminology_artefact)  perspective, state of the art is to use a [**graph database**](https://en.wikipedia.org/wiki/Graph_database).
Two types of graph database (URL_TO_INSERT_TERM_3662 https://fairsharing.org/search?fairsharingRegistry=Database) s are currently available:

- **Labeled-Property**
A **labeled-property graph model (URL_TO_INSERT_TERM_3663 https://fairsharing.org/search?recordType=model_and_format) ** is represented by a set of nodes, relationships, properties, and labels. 
- **Triple store**
A **triple store database (URL_TO_INSERT_TERM_3664 https://fairsharing.org/search?fairsharingRegistry=Database) ** allows to store documents in [RDF](https://www.w3.org/TR/rdf-concepts/#section-data-model) or
[OWL/RDF format](https://www.w3.org/TR/owl2-rdf-based-semantics/) natively and use the **query from remote** flexibility of
a [**SPARQL endpoint**](https://www.w3.org/TR/rdf-sparql-query/). 
Also, [**Shape Constraint Language (SHACL)**](https://www.w3.org/TR/shacl (URL_TO_INSERT_RECORD_3666 https://fairsharing.org/FAIRsharing.f1449d) /) W3C standard (URL_TO_INSERT_TERM_3665 https://fairsharing.org/search?fairsharingRegistry=Standard)  could help to add quality checks.



### Ontology language

The following ontology (URL_TO_INSERT_TERM_3668 https://fairsharing.org/search?recordType=terminology_artefact)  languages are widely used in the pharma research (URL_TO_INSERT_RECORD_3670 https://fairsharing.org/FAIRsharing.52b22c)  arena to model (URL_TO_INSERT_TERM_3667 https://fairsharing.org/search?recordType=model_and_format)  ontologies (URL_TO_INSERT_TERM_3669 https://fairsharing.org/search?recordType=terminology_artefact) :

- **Simple Knowledge Organization System (URL_TO_INSERT_RECORD_3671 https://fairsharing.org/FAIRsharing.48e326)  (SKOS (URL_TO_INSERT_RECORD_3672 https://fairsharing.org/FAIRsharing.48e326) )**
SKOS (URL_TO_INSERT_RECORD_3676 https://fairsharing.org/FAIRsharing.48e326)  is a W3C standard (URL_TO_INSERT_TERM_3673 https://fairsharing.org/search?fairsharingRegistry=Standard)  which provides a standard (URL_TO_INSERT_TERM_3674 https://fairsharing.org/search?fairsharingRegistry=Standard)  way to represent knowledge organization systems using the Resource Description Framework (URL_TO_INSERT_RECORD_3675 https://fairsharing.org/FAIRsharing.p77ph9)  (RDF). 
Encoding this informat (URL_TO_INSERT_TERM_3677 https://fairsharing.org/search?recordType=model_and_format) ion in RDF (URL_TO_INSERT_RECORD_3678 https://fairsharing.org/FAIRsharing.p77ph9)  allows it to be passed between computer applications in an interoperable way {footcite}`SkosReference2008`
- **Web Ontology (URL_TO_INSERT_TERM_3679 https://fairsharing.org/search?recordType=terminology_artefact)  Language (URL_TO_INSERT_RECORD_3680 https://fairsharing.org/FAIRsharing.atygwy)  (OWL)** 
OWL is defined by W3C and has become the de facto standard (URL_TO_INSERT_TERM_3681 https://fairsharing.org/search?fairsharingRegistry=Standard)  for ontology (URL_TO_INSERT_TERM_3683 https://fairsharing.org/search?recordType=terminology_artefact)  model (URL_TO_INSERT_TERM_3682 https://fairsharing.org/search?recordType=model_and_format) ling. 
Therefore, OWL (URL_TO_INSERT_RECORD_3686 https://fairsharing.org/FAIRsharing.atygwy)  support is considered as a must for the ontology (URL_TO_INSERT_TERM_3684 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3685 https://fairsharing.org/FAIRsharing.Mkl9RR) . 
- **OBO**
The OBO (URL_TO_INSERT_RECORD_3690 https://fairsharing.org/FAIRsharing.847069)  file format (URL_TO_INSERT_TERM_3687 https://fairsharing.org/search?recordType=model_and_format)  is a biology-oriented language for building ontologies (URL_TO_INSERT_TERM_3688 https://fairsharing.org/search?recordType=terminology_artefact) , based on the principles of OWL (URL_TO_INSERT_RECORD_3689 https://fairsharing.org/FAIRsharing.atygwy) .
A standard (URL_TO_INSERT_TERM_3691 https://fairsharing.org/search?fairsharingRegistry=Standard)  common map (URL_TO_INSERT_RECORD_3693 https://fairsharing.org/FAIRsharing.53edcc) ping has been created for lossless round-trip transformat (URL_TO_INSERT_TERM_3692 https://fairsharing.org/search?recordType=model_and_format) ions among both languages. 


Persisting semantics artefacts expressed in various languages and representation frameworks in the same management 
system isn't straightforward and conversions may be necessary. Even then, transformat (URL_TO_INSERT_TERM_3694 https://fairsharing.org/search?recordType=model_and_format) ions may lead to informat (URL_TO_INSERT_TERM_3695 https://fairsharing.org/search?recordType=model_and_format) ion loss or 
difficulty in rendering informat (URL_TO_INSERT_TERM_3696 https://fairsharing.org/search?recordType=model_and_format) ion consistently.



### Programming language

Programming languages are used to implement the data processing logic and user interface logic of the ontology (URL_TO_INSERT_TERM_3697 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3698 https://fairsharing.org/FAIRsharing.Mkl9RR) .

The used programming languages will impact:

- Required programming language knowledge you need for customization or support
- Customization effort

### Support

Important support aspects for a vocabulary service/ontology (URL_TO_INSERT_TERM_3699 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3700 https://fairsharing.org/FAIRsharing.Mkl9RR)  are: 

- Ongoing development of the tool 
- Frequency of issues and how fast they are solved
- Which organization you can get support from, and what is the associated cost?

## General selection considerations

Before looking into a concrete ontology (URL_TO_INSERT_TERM_3701 https://fairsharing.org/search?recordType=terminology_artefact)  service, some general thoughts are recommended. Two types of portal tools are available:

- **Open data portal tool**
**Open data portals** provide web-based interfaces designed to make it easier to find and access re-usable informat (URL_TO_INSERT_TERM_3702 https://fairsharing.org/search?recordType=model_and_format) ion. 
Some of them also support importing and exporting ontologies (URL_TO_INSERT_TERM_3704 https://fairsharing.org/search?recordType=terminology_artefact) , including a SP (URL_TO_INSERT_RECORD_3706 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_3705 https://fairsharing.org/FAIRsharing.87ccfd)  endpoint and provide ontology (URL_TO_INSERT_TERM_3703 https://fairsharing.org/search?recordType=terminology_artefact)  lookup 
service core (URL_TO_INSERT_RECORD_3707 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_3708 https://fairsharing.org/FAIRsharing.xMmOCL)  functionality.
An **Open Portal Tool**` is the underlying software that is used to implement the ontology (URL_TO_INSERT_TERM_3709 https://fairsharing.org/search?recordType=terminology_artefact)  portal functionalities.
- **Ontology (URL_TO_INSERT_TERM_3710 https://fairsharing.org/search?recordType=terminology_artefact)  portal tool**
A formal definition of an **Ontology (URL_TO_INSERT_TERM_3711 https://fairsharing.org/search?recordType=terminology_artefact)  Portal** does not exist. In the context of this document, an **Ontology (URL_TO_INSERT_TERM_3712 https://fairsharing.org/search?recordType=terminology_artefact)  Portal** is
defined as an Open Data Portal that is specialized to ontologies (URL_TO_INSERT_TERM_3713 https://fairsharing.org/search?recordType=terminology_artefact)  as data and typically provides out of the box more fine
granular ontology (URL_TO_INSERT_TERM_3714 https://fairsharing.org/search?recordType=terminology_artefact)  based functions.
An Ontology (URL_TO_INSERT_TERM_3715 https://fairsharing.org/search?recordType=terminology_artefact)  Portal Tool is the underlying software that is used to implement the ontology (URL_TO_INSERT_TERM_3716 https://fairsharing.org/search?recordType=terminology_artefact)  portal functionalities.

If you have only minimum functional requirements in sharing ontologies (URL_TO_INSERT_TERM_3717 https://fairsharing.org/search?recordType=terminology_artefact)  it might be also an option for you to use an 
open data portal tool. In this case you could extend the functionality by developing additional web pages using the
SPARQL (URL_TO_INSERT_RECORD_3719 https://fairsharing.org/FAIRsharing.87ccfd)  endpoint. Having data and metadata in one database (URL_TO_INSERT_TERM_3718 https://fairsharing.org/search?fairsharingRegistry=Database) , such a solution would allow adding functionality that needs 
to combine ontologies (URL_TO_INSERT_TERM_3720 https://fairsharing.org/search?recordType=terminology_artefact)  with data (e.g. by annotation).

If you need **fine granular ontology (URL_TO_INSERT_TERM_3721 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3723 https://fairsharing.org/FAIRsharing.Mkl9RR)  functionality**, an ontology (URL_TO_INSERT_TERM_3722 https://fairsharing.org/search?recordType=terminology_artefact)  portal tool is recommended.

An additional option would be to combine an Open data platform tool with an Ontology (URL_TO_INSERT_TERM_3724 https://fairsharing.org/search?recordType=terminology_artefact)  portal tool in parallel. 
If both tools use a triplestore database (URL_TO_INSERT_TERM_3725 https://fairsharing.org/search?fairsharingRegistry=Database) , this should be possible in principle. The challenge will be that you would
need additional customisation.

## Choosing an ontology service software

As each organization may have its own preferences and requirements, there is no standard (URL_TO_INSERT_TERM_3726 https://fairsharing.org/search?fairsharingRegistry=Standard)  way to select the best
suitable ontology (URL_TO_INSERT_TERM_3727 https://fairsharing.org/search?recordType=terminology_artefact)  service software. This section presents a general selection process based on the aforementioned
selection criteria and gives guidance on a set of questions that should be answered in order to filter out tools that
do not fit to use case at an early stage.

## Overall Selection Process

A three-step selection approach is proposed: 

- `High Level Gap Analysis`
First, it should be checked on a high level whether the tool does match the high level requirements. 
- `Low Level Gap Analysis`
Only if the tool matches on a high level, more efforts should be invested in a finer analysis to find out whether the
tool is still a suitable candidate. 
- `From Candidates Selection` 
Once the tool candidates have been identified, a ranking process can start by assigning fulfillment numbers to the
weighted criteria reflecting the importance for the requesting organization.  Finally, completing the ranking by 
summing up the total numbers from each atomic ranking criteria will allow to choose the tool, based on the highest score (URL_TO_INSERT_RECORD_3728 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_3729 https://fairsharing.org/FAIRsharing.xMmOCL) r. 

Following figure shows the overall process:


````{dropdown}
:open:  
```{figure} onto-services-figure1.svg
---
name: onto-services-figure1
width: 450px
alt: Overall Process for Selecting Ontology (URL_TO_INSERT_TERM_3730 https://fairsharing.org/search?recordType=terminology_artefact)  Services 
---
Overall Process for Selecting Ontology (URL_TO_INSERT_TERM_3731 https://fairsharing.org/search?recordType=terminology_artefact)  Services 
```
````



### High Level Gap Analysis

As guidance for the **High Level Gap Analysis**, an analysis order based on selection criteria is proposed. 
The most important selection criteria contains one major question that has to be answered positively, 
either by the offerings of the tool or by some additional tool customization.

````{dropdown}
:open:
```{figure} onto-services-figure2.svg
---
name: onto-services-figure2
alt: Ontology (URL_TO_INSERT_TERM_3732 https://fairsharing.org/search?recordType=terminology_artefact)  Services High Level Gap Analysis
---
Ontology (URL_TO_INSERT_TERM_3733 https://fairsharing.org/search?recordType=terminology_artefact)  Services High Level Gap Analysis
```
````


<!-- Figure 2: High Level Gap Analysis -->

### Low Level Gap Analysis 

For a single **low level selection criteria**, no common recommendation for the “tool does not fit” decision can be
given, because the decision highly depends on the preferences set in your specific context.

Instead, a set of questions  will be presented per selection criteria. 
One has then to pick out those questions that are absolutely mandatory in a  local context.

If such an absolutely mandatory question can not be solved by the tool or by tool customization, the “Tool does not fit” will fire.

```{warning}
Please note that for **ontology functionality**, no questions will be presented, because functionality is out
of the scope of this recipe.
```

````{dropdown}
:open:
```{figure} onto-services-figure3.svg
---
name: onto-services-figure3
alt: Ontology (URL_TO_INSERT_TERM_3734 https://fairsharing.org/search?recordType=terminology_artefact)  Services  Low Level Gap Analysis
---
Ontology (URL_TO_INSERT_TERM_3735 https://fairsharing.org/search?recordType=terminology_artefact)  Services Low Level Gap Analysis
```
````



<!-- Figure 3: Low Level Gap Analysis -->

The following figures are showing typical questions one would have to answer for the low level analysis.

These questions may have to be adapted or extended depending on the local, specific needs.

````{dropdown} functional questions
:open:
```{figure} onto-services-figure4.svg
---
name: onto-services-figure4
alt: Typical Low Level Functional Questions
---
Typical Low Level Functional Questions
```
````

<!-- Figure 4: Typical Low Level Functional Questions -->


````{dropdown} user interface questions
:open:
```{figure} onto-services-figure5.svg
---
name: onto-services-figure5
alt: Typical Low Level Interface Questions
---
Typical Low Level Interface Questions
```
````

<!-- Figure 5: Typical Low Level Interface Questions -->



````{dropdown} Architecture questions
:open:
```{figure} onto-services-figure6.svg
---
name: onto-services-figure6
alt: Typical Low Level Arch (URL_TO_INSERT_RECORD_3736 https://fairsharing.org/FAIRsharing.52b22c) itecture Questions
---
Typical Low Level Arch (URL_TO_INSERT_RECORD_3737 https://fairsharing.org/FAIRsharing.52b22c) itecture Questions
```
````

<!-- Figure 6: Typical Low Level Architecture Questions -->


````{dropdown} Costs questions
:open:
```{figure} onto-services-figure7.svg
---
name: onto-services-figure7
alt:  Typical Low Level Costs Questions
---
 Typical Low Level Costs Questions
```
````

<!-- Figure 7: Typical Low Level Costs Questions -->


````{dropdown} Performance questions
:open:
```{figure} onto-services-figure8.svg
---
name: onto-services-figure8
alt:  Typical Low Level Performance Questions
---
 Typical Low Level Performance Questions
```
````

<!-- Figure 8: Typical Low Level Performance Questions -->


````{dropdown} Delivery questions
:open:
```{figure} onto-services-figure9.svg
---
name: onto-services-figure9
alt:  Typical Low Level Delivery Questions
---
 Typical Low Level Delivery Questions
```
````

<!-- Figure 9: Typical Low Level Delivery Questions -->


````{dropdown} Support questions
:open:
```{figure} onto-services-figure10.svg
---
name: onto-services-figure10
alt:  Typical Low Level Support Questions
---
 Typical Low Level Support Questions
```
````

<!-- Figure 10: Typical Low Level Support Questions -->

## Available  open source software

### EMBL-EBI Ontology Lookup Service

#### Overview

It is a repository (URL_TO_INSERT_TERM_3738 https://fairsharing.org/search?recordType=repository)  for biomedical ontologies (URL_TO_INSERT_TERM_3740 https://fairsharing.org/search?recordType=terminology_artefact)  that aims to provide a single point of access to the latest ontology (URL_TO_INSERT_TERM_3739 https://fairsharing.org/search?recordType=terminology_artefact)  versions. It allows browsing the ontologies (URL_TO_INSERT_TERM_3741 https://fairsharing.org/search?recordType=terminology_artefact)  through the website as well as programmatically via the OLS (URL_TO_INSERT_RECORD_3742 https://fairsharing.org/FAIRsharing.Mkl9RR)  API. It is part of the ELIXIR interoperability service.

#### Details

1. **Functionality**: `Ontology (URL_TO_INSERT_TERM_3743 https://fairsharing.org/search?recordType=terminology_artefact)  Portal Tool`
2. **Interface**: REST-style API supported, SP (URL_TO_INSERT_RECORD_3745 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_3744 https://fairsharing.org/FAIRsharing.87ccfd)  endpoint under development.
3. **Arch (URL_TO_INSERT_RECORD_3747 https://fairsharing.org/FAIRsharing.52b22c) itecture**: OLS (URL_TO_INSERT_RECORD_3746 https://fairsharing.org/FAIRsharing.Mkl9RR)  has been developed (URL_TO_INSERT_RECORD_3748 https://fairsharing.org/FAIRsharing.31385c)  with the Spring Data and Spring Boot framework.
    1. Tomcat is used as a web server.
    2. MongoDB is used for storing configuration yaml files.
    3. Neo4J node-property graph database (URL_TO_INSERT_TERM_3749 https://fairsharing.org/search?fairsharingRegistry=Database)  is used for storing and accessing the ontologies (URL_TO_INSERT_TERM_3751 https://fairsharing.org/search?recordType=terminology_artefact) . OWL (URL_TO_INSERT_RECORD_3752 https://fairsharing.org/FAIRsharing.atygwy)  format (URL_TO_INSERT_TERM_3750 https://fairsharing.org/search?recordType=model_and_format)  is converted to a node-property representation.
4. **Deployment model (URL_TO_INSERT_TERM_3753 https://fairsharing.org/search?recordType=model_and_format) **: It is available both as an on-premises and cloud-based solution. Docker based deployment is supported.
5. **Requirements**:
    1. Hardware requirements. It requires a standard (URL_TO_INSERT_TERM_3754 https://fairsharing.org/search?fairsharingRegistry=Standard)  workstation, 1 GB main memory, and about 100 MB hard disk.
    2. Software requirements. It is implemented as a Java Web Application to be deployed to the Tomcat 7.5 Java Application Container. It requires Java 8, Maven 3+ as dependency manager and build environment, MongoDB 2.7.8+ as database (URL_TO_INSERT_TERM_3755 https://fairsharing.org/search?fairsharingRegistry=Database) ; and solr 5.2.1+ as indexing and search (URL_TO_INSERT_RECORD_3756 https://fairsharing.org/FAIRsharing.52b22c)  engine.
    3. License model (URL_TO_INSERT_TERM_3757 https://fairsharing.org/search?recordType=model_and_format) . Apache Software Licence (v. 2.0).
6. **Database (URL_TO_INSERT_TERM_3758 https://fairsharing.org/search?fairsharingRegistry=Database) s**: It supports the Neo4J graph store, which allows querying using Cypher query language. Reasoning supports two profiles: OWL (URL_TO_INSERT_RECORD_3759 https://fairsharing.org/FAIRsharing.atygwy) 2 and EL. Default is EL. The reasoners supported are HermiT and ELK.
7. **Ontology (URL_TO_INSERT_TERM_3761 https://fairsharing.org/search?recordType=terminology_artefact)  Language**: Custom translation of OBO (URL_TO_INSERT_RECORD_3763 https://fairsharing.org/FAIRsharing.847069)  and OWL (URL_TO_INSERT_RECORD_3762 https://fairsharing.org/FAIRsharing.atygwy)  2 languages to the Neo4J graph model (URL_TO_INSERT_TERM_3760 https://fairsharing.org/search?recordType=model_and_format) .
8. **Programming Language**: Java.

### NCBO Bioportal Virtual Appliance<!-- TODO add a link to corresponding document --> (Ontology Portal Tool)

#### Overview

The National Center for Biomedical Ontology (URL_TO_INSERT_TERM_3764 https://fairsharing.org/search?recordType=terminology_artefact)  (NCBO).

#### Details

1. **Functionality**: `Ontology (URL_TO_INSERT_TERM_3765 https://fairsharing.org/search?recordType=terminology_artefact)  Portal Tool`
2. **Interface**: REST-style API supported, SP (URL_TO_INSERT_RECORD_3767 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_3766 https://fairsharing.org/FAIRsharing.87ccfd)  endpoint 
3. **Arch (URL_TO_INSERT_RECORD_3768 https://fairsharing.org/FAIRsharing.52b22c) itecture**: Virtual Appliance defines the framework for the Web Service. The system internally uses the following components
    1. A set of additional ruby based modules that implement the user interface and additional functionality can be found [here](https://github.com (URL_TO_INSERT_RECORD_3769 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo).
    2. 4Store triple store database (URL_TO_INSERT_TERM_3770 https://fairsharing.org/search?fairsharingRegistry=Database)  is used to store and access ontologies (URL_TO_INSERT_TERM_3771 https://fairsharing.org/search?recordType=terminology_artefact) . 
    3. Solr is used to create indexes out of description text metadata.  
    4. MySQL is used to store additional metadata.
    5. MGrep is used for annotating text to ontologies (URL_TO_INSERT_TERM_3772 https://fairsharing.org/search?recordType=terminology_artefact) .
4. **Deployment model (URL_TO_INSERT_TERM_3773 https://fairsharing.org/search?recordType=model_and_format) **: It is available both as an on-premises and cloud-based solution. It is available as virtual VMWare Virtual Appliance or Amazon AWS AMI. 
5. **Requirements**:
    1. Hardware requirements. 
        1. Minimum: 2 CP (URL_TO_INSERT_RECORD_3774 https://fairsharing.org/FAIRsharing.wP3t2L) U (2 GHz), 4GB RAM, 20GB hard disk space.
        2. Recommended for heavier usage: 3 CP (URL_TO_INSERT_RECORD_3777 https://fairsharing.org/FAIRsharing.wP3t2L) U (3 GHz), 8GB RAM (or more depending on the size/number of ontologies (URL_TO_INSERT_TERM_3775 https://fairsharing.org/search?recordType=terminology_artefact) ), 20GB hard disk space (or more depending on number/size of ontologies (URL_TO_INSERT_TERM_3776 https://fairsharing.org/search?recordType=terminology_artefact) )
    2. Software requirements. All software is already contained in the virtual image
        1. Operating system: CentOS (Linux)
        2. License model (URL_TO_INSERT_TERM_3778 https://fairsharing.org/search?recordType=model_and_format) . Apache Software Licence (v. 2.0).
6. **Database (URL_TO_INSERT_TERM_3779 https://fairsharing.org/search?fairsharingRegistry=Database) s**: It supports the 4Store triple store and MySQL
7. **Ontology (URL_TO_INSERT_TERM_3780 https://fairsharing.org/search?recordType=terminology_artefact)  Language**: OBO (URL_TO_INSERT_RECORD_3782 https://fairsharing.org/FAIRsharing.847069) , OWL (URL_TO_INSERT_RECORD_3781 https://fairsharing.org/FAIRsharing.atygwy) 
8. **Programming Language**: Ruby, Java.

### [Apache Marmotta](https://marmotta.apache.org/) (Open Data Platform Tool)

#### Overview

It is an Open Data Platform for Linked Data, which provides an open implementation of 
a Linked Data Platform that can be used, extended and deployed easily by organizations who want to publish 
Linked Data or build custom applications on Linked Data {footcite}`apache_marmotta`. 
It provides:
> * a) read-write Linked Data server for the **Java EE (URL_TO_INSERT_RECORD_3783 https://fairsharing.org/FAIRsharing.0b711a)  stack** 
> * b) custom triple store built on top of RDBMS, with transactions, versioning and rule-based reasoning support
> * c) pluggable RDF (URL_TO_INSERT_RECORD_3784 https://fairsharing.org/FAIRsharing.p77ph9)  triple stores based on [**Eclipse RDF4J**](https://projects.eclipse.org/projects/technology.rdf4j),
> * d) LDP, SP (URL_TO_INSERT_RECORD_3786 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_3785 https://fairsharing.org/FAIRsharing.87ccfd)  and LD Path querying
> * e) transparent Linked Data Caching
> * f) Integrated basic security mechanisms.

```{warning}
This project is now retired and is no longer supported or developed.
```

#### Details

1. **Functionality**: `Open (Linked) Data Platform`.
2. **Interface**: REST-style API, SP (URL_TO_INSERT_RECORD_3788 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_3787 https://fairsharing.org/FAIRsharing.87ccfd)  endpoint supported.
3. **Arch (URL_TO_INSERT_RECORD_3789 https://fairsharing.org/FAIRsharing.52b22c) itecture**, the arch (URL_TO_INSERT_RECORD_3790 https://fairsharing.org/FAIRsharing.52b22c) itecture comprises the following tiers:
    1. User Interface Layer. It mostly consists of admin and development interfaces and is not intended for end users.
    2. Web-service Layer. It offers REST web-services to access most of the server functionality.
    3. Service Layer. It offers CDI (URL_TO_INSERT_RECORD_3791 https://fairsharing.org/FAIRsharing.yzagph)  services to develop custom Java applications.
    4. Model (URL_TO_INSERT_TERM_3792 https://fairsharing.org/search?recordType=model_and_format)  Layer. It offers persistence and data access functionality.
    5. Persistence Layer. It is outside the Apache Marmotta Platform, which can use a number of Open Source database (URL_TO_INSERT_TERM_3793 https://fairsharing.org/search?fairsharingRegistry=Database)  systems.
4. **Deployment Model (URL_TO_INSERT_TERM_3794 https://fairsharing.org/search?recordType=model_and_format) **: It is available both as an on-premises and cloud-based solution. Docker based deployment is supported.
5. **Requirements**:
    1. Hardware requirements. It requires a standard (URL_TO_INSERT_TERM_3795 https://fairsharing.org/search?fairsharingRegistry=Standard)  workstation, 1 GB main memory, and about 100 MB hard disk.
    2. Software requirements. It is implemented as a Java Web Application that can, in principle, be deployed to any 
   Java Application Container. It has been tested under Jetty 6.x and Tomcat 7.x. It requires Java JDK 6 or higher,
   Java Application Server (Tomcat 7.x or Jetty 6.x), and a database (URL_TO_INSERT_TERM_3796 https://fairsharing.org/search?fairsharingRegistry=Database)  (PostgreSQL, MySQL). If not explicitly configured, 
   an embedded H2 database (URL_TO_INSERT_TERM_3797 https://fairsharing.org/search?fairsharingRegistry=Database)  will be used.
    3. License model (URL_TO_INSERT_TERM_3798 https://fairsharing.org/search?recordType=model_and_format) . Apache Software Licence (v. 2.0).
6. **Database (URL_TO_INSERT_TERM_3799 https://fairsharing.org/search?fairsharingRegistry=Database) s**: It supports the following triple store backends: (a.) KiWi Triple Store, (b.) Sesame Native, and (c.) 
BigData triple store. The default backend is the KiWi triple store, which stores all data in a relational database (URL_TO_INSERT_TERM_3800 https://fairsharing.org/search?fairsharingRegistry=Database) , and
it is the only option that supports reasoning and versioning.
7. **Ontology (URL_TO_INSERT_TERM_3801 https://fairsharing.org/search?recordType=terminology_artefact)  Language**: OWL (URL_TO_INSERT_RECORD_3803 https://fairsharing.org/FAIRsharing.atygwy)  serialized as RDF (URL_TO_INSERT_RECORD_3804 https://fairsharing.org/FAIRsharing.p77ph9) /RDFS (URL_TO_INSERT_RECORD_3802 https://fairsharing.org/FAIRsharing.v9n3gk)  triples. 
8. **Programming Language**: Java.

### European Data Portal<!-- TODO add a link to corresponding document --> (Open Data Platform Tool)

#### Overview

[European data portal](https://www.europeandataportal.eu/en (URL_TO_INSERT_RECORD_3805 https://fairsharing.org/2940) )  (EDP) is an initiative by 
the [Publications Office of the European Union](https://op.europa.eu/da/home) and by the [European Commission](https://ec.europa.eu/info/index_en) that aims to increase the impact of open data by making it easy to find and re-use by everyone.

It uses only open source software with extensions that are all available to the public for own use. 

As a core (URL_TO_INSERT_RECORD_3806 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_3807 https://fairsharing.org/FAIRsharing.xMmOCL)  component,
[CKAN open data portal software](https://ckan.org/) with [DCAT-AP](https://op.europa.eu/da/web/eu-vocabularies/dcat-ap)
RDF extension is used. 

It allows sharing various data format (URL_TO_INSERT_TERM_3808 https://fairsharing.org/search?recordType=model_and_format) s e.g. tabular data, RDF (URL_TO_INSERT_RECORD_3810 https://fairsharing.org/FAIRsharing.p77ph9)  data (e.g. ontologies (URL_TO_INSERT_TERM_3809 https://fairsharing.org/search?recordType=terminology_artefact) ) combining
relational and semantic technologies.

The [Triple Store database Virtuoso](https://virtuoso.openlinksw.com/) is used 
for storing ontologies (URL_TO_INSERT_TERM_3811 https://fairsharing.org/search?recordType=terminology_artefact) . 

For metadata in relational format (URL_TO_INSERT_TERM_3813 https://fairsharing.org/search?recordType=model_and_format) , the [PostgreSQL](https://www.postgresql.org/) database (URL_TO_INSERT_TERM_3812 https://fairsharing.org/search?fairsharingRegistry=Database)  is used as part of CKAN.

#### Details

1. **Functionality**: `Open Data Portal` 
2. **Interface**: REST-style API, SP (URL_TO_INSERT_RECORD_3815 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_3814 https://fairsharing.org/FAIRsharing.87ccfd)  endpoint supported.
3. **Arch (URL_TO_INSERT_RECORD_3816 https://fairsharing.org/FAIRsharing.52b22c) itecture**:
    1. CKAN manages and provides metadata content (datasets) in a central repository (URL_TO_INSERT_TERM_3817 https://fairsharing.org/search?recordType=repository) . 
    2. DR (URL_TO_INSERT_RECORD_3818 https://fairsharing.org/FAIRsharing.1sfhp3) UPAL provides the Portal’s Home Page with editorial content (e.g. Portal’s objectives, articles, news, events, tweets, etc.) 
    and links to an *Adapt Framework* based training platform. 
    3. The CKAN metadata is replicated into a Virtuoso triple store database (URL_TO_INSERT_TERM_3819 https://fairsharing.org/search?fairsharingRegistry=Database)  via a CKAN synchronisation extension, in order
    to ensure that both repositories (URL_TO_INSERT_TERM_3820 https://fairsharing.org/search?recordType=repository)  have the same set of metadata. 
    4. The SP (URL_TO_INSERT_RECORD_3824 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_3822 https://fairsharing.org/FAIRsharing.87ccfd)  Manager component allows the user to enter and run SP (URL_TO_INSERT_RECORD_3825 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_3823 https://fairsharing.org/FAIRsharing.87ccfd)  queries on the Virtuoso linked data repository (URL_TO_INSERT_TERM_3821 https://fairsharing.org/search?recordType=repository) . 
    5. The portal uses the SO (URL_TO_INSERT_RECORD_3826 https://fairsharing.org/FAIRsharing.6bc7h9) LR search (URL_TO_INSERT_RECORD_3828 https://fairsharing.org/FAIRsharing.52b22c)  engine in order to separately search (URL_TO_INSERT_RECORD_3829 https://fairsharing.org/FAIRsharing.52b22c)  for editorial content in DR (URL_TO_INSERT_RECORD_3827 https://fairsharing.org/FAIRsharing.1sfhp3) UPAL and for 
    datasets in the CKAN repository (URL_TO_INSERT_TERM_3830 https://fairsharing.org/search?recordType=repository) . 
    6. The Harvester is a separate component that is able to harvest data from multiple data sources with different format (URL_TO_INSERT_TERM_3831 https://fairsharing.org/search?recordType=model_and_format) s and APIs. 
4. **Deployment model (URL_TO_INSERT_TERM_3832 https://fairsharing.org/search?recordType=model_and_format) **: It is available both as an on-premises and cloud-based solution.
5. **Requirements**:
    1. The setup of the EDP (URL_TO_INSERT_RECORD_3833 https://fairsharing.org/2940)  consists of 20 virtual servers per computer room and environment (PROD, TEST)
6. **Database (URL_TO_INSERT_TERM_3834 https://fairsharing.org/search?fairsharingRegistry=Database) s**: PostgreSQL RDBMS for CKAN catalogue, Virtuoso for RDF (URL_TO_INSERT_RECORD_3835 https://fairsharing.org/FAIRsharing.p77ph9)  data
7. **Ontology (URL_TO_INSERT_TERM_3836 https://fairsharing.org/search?recordType=terminology_artefact)  Language**: RDF (URL_TO_INSERT_RECORD_3839 https://fairsharing.org/FAIRsharing.p77ph9) , RDF (URL_TO_INSERT_RECORD_3840 https://fairsharing.org/FAIRsharing.p77ph9) S (URL_TO_INSERT_RECORD_3837 https://fairsharing.org/FAIRsharing.v9n3gk) , OWL (URL_TO_INSERT_RECORD_3838 https://fairsharing.org/FAIRsharing.atygwy)  2
8. **Programming Language**: Python(CKAN), PHP(Drupal)

---
## Conclusions

Determining which infrastructure to rely on for service terminologies (URL_TO_INSERT_TERM_3841 https://fairsharing.org/search?recordType=terminology_artefact)  and ontologies (URL_TO_INSERT_TERM_3842 https://fairsharing.org/search?recordType=terminology_artefact)  is a complex issue. 

This FAIR (URL_TO_INSERT_RECORD_3843 https://fairsharing.org/FAIRsharing.WWI10U)  Cookbook recipe gave an overview of non-functional criteria to take into consideration when appraising a software solution.

To complement this recipe, reading the following chapter is highly encouraged.

### What to read next?

* [Key functional requirements to consider when selecting an ontology service?](https://w3id.org (URL_TO_INSERT_RECORD_3844 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB004)
* [Deploying EMBL-EBI Ontology Lookup Service](https://w3id.org (URL_TO_INSERT_RECORD_3845 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB005)
* [Introduction to terminologies and ontologies](https://w3id.org (URL_TO_INSERT_RECORD_3846 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB019)
* [How to select an ontology?](https://w3id.org (URL_TO_INSERT_RECORD_3847 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB020)
* [How to build an application ontology?](https://w3id.org (URL_TO_INSERT_RECORD_3848 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB023)

````{rdmkit_panel}
````
## References
````{dropdown} **References**
```{footbibliography}
```
````


## Authors

````{authors_fairplus}
Kurt: Writing - Original Draft
Emiliano: Writing - Original Draft
Petros: Writing - Review & Editing
Karsten: Writing - Review & Editing
Philippe: Writing - Review & Editing
````



## License

````{license_fairplus}
CC-BY-4.0
````
