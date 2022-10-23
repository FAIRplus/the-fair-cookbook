(fcb-infra-redcap)=
# Capturing research data with RedCap


<br/>
<br/>


---

````{panels_fairplus}
:identifier_text: FCB0__
:identifier_link: 'https://w3id.org/faircookbook/FCB0__'
:difficulty_level: 2
:recipe_type: background_information
:reading_time_minutes: 15
:intended_audience: principal_investigator, data_manager, data_scientist, funder
:maturity_level: 0  
:maturity_indicator: 0
:has_executable_code: nope
:recipe_name: Capturing research data with RedCap
```` 


## Main Objectives

The main purpose of this recipe is:

> To provide a brief introduction about a popular resource used to define electronic data capture forms. [Redcap](https://projectredcap.org/) is a 
> software tool which allows data manager define forms, known as instruments, to record patient information.
> 
---


## Graphical Overview

```{note} 
use this section to provide a decision tree for the overall process described in the recipe
For more information about the syntax used to generate the diagram, please refer to the [following documentation](https://mermaid-js.github.io/mermaid/#/flowchart)
```



one may use the following **[mermaid](https://mermaid-js.github.io/mermaid/#/)** syntax:
`````
````{panels} 
:container: container-lg pb-3
:column: col-lg-12 p-2
:card: rounded

```
graph LR;
    A[Data Acquisition] -->B(Raw Data)
    B --> C{FAIR by Design}
    C -->|Yes| D[Standard Compliant Data]
    C -->|No| E[Vendor locked Data]
```
````
`````


---


## Requirements

* technical requirements:
    * administrator: sysadmin skills + understanding of the license & legal terms
    * user: familiarity with web applications
* knowledge requirement:
    * Data Management and Good Clinical Data Practice
    * Regulatory requirements for handling sensitive data


---

## FAIRification Objectives, Inputs and Outputs


| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [text annotation](http://edamontology.org/operation_3778)  | []()  | [annotated text](http://edamontology.org/data_3779)  |
| [validation](http://edamontology.org/operation_2428)  | []()  | [report](http://edamontology.org/data_2048)  |

## Table of Data Standards

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| [FHIR](https://fairsharing.org/FAIRsharing.25k4yp)  |  |   |
|  |   |    |

---

## Main Content

### What is RedCap?  

Redcap is a tool developed by Vanderbilt University, in the USA, for the purpose of collecting clinical 
research data taking into account the needs for regulatory compliance with HIPAA legislation. Since its first release back in 2004, 
the group of developers has grown into a large consortium for users, developers and advocates.

The key features of RedCap software are:
- the resource is freely available under a [dedicated license](https://projectredcap.org/partners/termsofuse/).
- the resource offers a simple, easy to use web based user interface for clinical researchers.
- the resource is secure and regulation compliant with support for HIPAA, 21 CFR Part 11, or FISMA.
- the resource is highly customizable, allowing users to shape the data capture forms to their needs.
- the resource has capabilities to export to third party analysis environment (e.g. SSPS, STATA, SAS, R formats).
- the resource is interoperable with HL7 FHIR compliant resources, by pulling information into RedCap via a webservice client.
- the resource provides a wealth of training material, documentation and support, backed by years of experience and a large
community of users.
- the resource is available in languages other than English, thus enabling clinical data capture in environments which aren't anglophone
- the resource offers mobile applications to interact with the RedCap backends, which presents a number of advantages for field operations.
- the resource is domain agnostics, thus can be used in non-clinical context {footcite}`OBEID2013259`.


<!-- [img.png](img.png) -->


```{figure} ../../../images/redcap-tool.png
---
width: 700px
name: RedCap Tool
alt: RedCap Tool
---
RedCap Tool
```

### How to get RedCap and how to use it?

The RedCap is a server application which requires a dedicated physical or virtual hosting (on a local machine or a cloud based one)

* Web server with PHP 7.2.5 or higher (including support for PHP 8).
Apache (any OS) or Microsoft IIS (Windows).
* MySQL database server (MySQL 5.5.5+, MariaDB 5.5.5+, or Percona Server 5.5.5+). 
A MySQL client (e.g., phpMyAdmin, MySQL Workbench) is required for performing installation/upgrades
*SMTP email server.
Configure PHP with an institutional SMTP server or install an SMTP to use for sending emails out of REDCap.
*File server (optional). 
A separate server may be utilized for housing files uploaded/stored in REDCap via secure communication using WebDAV protocol (SSL supported). Consult your local policy first in case your institution has regulations or mandates regarding file storage practices.



### RedCap catalogue of instruments:

Available from the following link, https://redcap.vanderbilt.edu/consortium/library/search.php, the RedCap Share Library
is a catalogue of data capture forms (designated as 'instruments' by RedCap). 
The resource was established to promote information and practice sharing among clinical researchers. 
Therefore, users will find in the catalogue a number of curated resources given by fellow researchers. The data capture
forms can be searched by area of interests (e.g. disease, syndrome) or date or by languages.
As the resource is a curated one, not everything that is sent to the RedCap Shared Library will necessarily be published there.
A oversight and curation committee checks the quality and suitability of the submissions for inclusion in the archive.



<!--[redcap-instrument-library.png](redcap-instrument-library.png) -->
 
```{figure} ../../../images/redcap-instrument-library.png
---
width: 700px
name: RedCap Share Library
alt: RedCap Share Library
---
RedCap Share Library.
```





---

## Conclusion

With this content, we have highlighted RedCap, a popular tool for collecting clinical data in the context of biomedical studies.

```{warning}
Due to the sensitive nature of the data collected in clinical research, it is critical that users of RedCap are trained 
in handling data in a privacy protecting fashion and that they understand the risk and duties associated with such tasks.
The responsibilities are down to the data managers but also down to the system administrator of the server. Indeed, RedCap is
a tool which has been designed to support multi-centric, and multi-project data collection. Therefore, it is down to the institution
administrators watching over the deployment of the server to ensure the following critical points are met:
- compliance with the terms of uses defined by the RedCap licensing terms.
- compliance with cyber-security fundamentals.
- compliance with regulatory requirements, something RedCap has been designed for but which may requires specific tuning during installation
of the servers.
```


> 
> ### What should I read next?
> In keeping with the issue of data protection, we suggest the readership to also consider the following content:
> * [Data Privacy Impact Assessment](https://www.w3id.org/faircoobook/FCB074)
> 
> 
>  This is particular relevance when starting a project, to clearly identify key functions within an organization as well perform the due diligence.
> 
> The content is also important as it delineates the tasks to perform in a scenario of request for access.
> 
> This is a common scenario and data managers, data stewards and data owners need to be familiar with the regulation, 
> especially the EU General Data Protection Regulation, which is currently the most advanced in the world. 


> ````{panels}
> :column: col-4
> :card: border-2
> :header: bg-primary pa_dark
> :body: grey
> ```{image} ../../../images/logos/RDMkit_logo.svg
> :height: 40px
> :name: rdmkit_logo
> ```
> ^^^
> [More about `Data Quality` from the `RDMkit`](https://rdmkit.elixir-europe.org/data_quality#how-do-you-ensure-the-quality-of-research-data)
> ---
> :header: bg-primary pa_dark
> ```{image} ../../../images/logos/rdmbites-logo.png
> :height: 75px
> :align: center
> :name: RDMbites_logo
> ```
> ^^^
> [More about `RedCap` from the `RDM Bites`](https://www.youtube.com/watch?v=YktqkkK8IaY&t=29s&ab_channel=ELIXIR-UK)
> ````


## References:

````{dropdown} **References**
```{footbibliography}
```
````



## Authors


````{authors_fairplus}
Wei: Writing - Review & Editing
Philippe: Writing - Review & Editing
````


## License
````{license_fairplus}
CC-BY-4.0
````

