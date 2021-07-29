(fcb-intro-model-sharing)=
# High level data sharing models

+++
<br/>

````{panels_fairplus}
:identifier_text: RX.X
:identifier_link: 'https://example.com'
:difficulty_level: 2
:recipe_type: background_information
:reading_time_minutes: 15
:intended_audience: principal_investigator, data_manager, data_scientist, funder  
:has_executable_code: nope
:recipe_name: High level data sharing models
````

## Main Objectives

The main purpose of this recipe is to evaluate the current Data Sharing procedure offered by the Luxembourg Centre for Systems Biomedicine ([LCSB](https://www.uni.lu/lcsb)) of the University of Luxembourg as found [here](https://r3.pages.uni.lu/howto-cards/stable/).

To provide a transparent Evaluation the recipe will:
* Define an abstract model to explain what data sharing is
* Define the common criteria for evaluating data sharing procedures
* Evaluate the common criteria against the LCSB offering
* Propose potential improvements for the LCSB offering 

---

## Capability & Maturity Table

<!-- TO DO -->

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
|  |  |  |

----

## Data Sharing
This chapter explains what data sharing is. It defines a high-level logical data sharing model, to help a user who is not familiar with data sharing get an overview of the major components. Please note that in the real world the defined components are not always explicitly defined. Often implicit concept definitions are used and people are not always aware of the implicit definitions. Sometimes some of the components may even not exist, because for the given data sharing use case they might not be needed.

<!-- 
````{panels} 
:container: container-lg pb-3
:column: col-lg-12 p-2
:card: rounded

<div class="mermaid" align="left">
classDiagram
  SharedData <-- DataOwner: owns
  SharedData <-- DataConsumer: consumes
  SharedData <-- DataProvider: provides
  class SharedData
  class DataOwner
  class DataProvider
  class DataConsumer
  
</div>
```` -->
<!-- 
*Figure 1: The core model of data sharing*
 -->

```{figure} ./data-sharing-fig1.svg
---
height: 200px
name: 
alt: Data Sharing Model 1
---
_data sharing_ Data Sharing Model 1.
```


The Figure 1 depicts the three roles that can be distinguished in a data sharing context: ***DataOwner***, ***DataConsumer***, and ***DataProvider***. The roles are typically played by different entities, which can be both organizations or persons. Then, a brief description of the roles is presented.  

The ***DataOwner*** role is played by the entity that has legal ownership of the data being shared.

The ***DataConsumer*** role is played by the entity that has been granted access to the data being shared, according to the license agreement signed with the Data Owner.

The ***DataProvider*** role is played by the entity that provides the technical infrastructure to support the sharing of data.

<!-- 
````{panels} 
:container: container-lg pb-3
:column: col-lg-12 p-2
:card: rounded
<div class="mermaid" align="left">
classDiagram
SharedData "1" *-- "1..*" Dataset: has
Dataset "1" *-- "1" Data: has
Dataset "1" *-- "0..1" DatasetProfile: has
Dataset "1" *-- "1" DatasetMetadata: has
SharedData "1..*" *-- "1" ConsumerLicenceDefinition: has
SharedData "1..*" *-- "0..1" ProviderLicenceDefinition: has
DatasetMetadata "1" *-- "1" DatasetLevelMetadata: has
DatasetMetadata "1" *-- "0..*" ColumnMetadata: has
DatasetMetadata "1" *-- "0..1" ProvenanceMetadata: has
DatasetMetadata "1" *-- "0..1" QualityMetadata: has
class SharedData
class Dataset
class Data
class DatasetMetadata
class ProviderLicenceDefinition
class ConsumerLicenceDefinition
class DatasetLevelMetadata
class ColumnMetadata
class ProvenanceMetadata
</div>
```` -->

<!-- *Figure 2: The SharedData entity components* -->

```{figure} ./data-sharing-fig2.svg
---
height: 300px
name: 
alt: Data Sharing Model 2
---
_data sharing_ Data Sharing Model 2.
```



The Figure 2 depicts the structure of the bundle of the data being shared, represented by the ***SharedData*** entity. It has a complex structure, as depicted following.

The ***DataSet*** entity is the main component of the SharedData entity, and it comprises the ***Data***, ***DatasetProfile***, and ***DatasetMetadata*** entities.

The ***Data*** entity represents the data object of the exchange. 

The ***DatasetProfile*** depicts statistics and informative summaries about that data being shared. 

The ***DatasetMetadata***, is structured information that describes, explains, locates, or otherwise makes it easier to retrieve, use, or manage an information resource (More information can be found in [European Data Portal](https://www.europeandataportal.eu/) and the [National Information Standards Organization](https://www.niso.org/)). The metadata categories are depicted following.

The ***DatasetLevelMetadata*** entity briefly depicts the dataset the metadata is related to. It presents general information on the dataset level, e.g., summary or description, author, date of creation, date of sharing, main concepts, size, etc. 

The ***ColumnMetadata*** entity describes the features or attributes of the dataset. This metadata can include external sources of knowledge - e.g., upper or domain ontologies, taxonomies, vocabularies, standards, etc. - to establish the type of entities a specific dataset attribute/feature is related to, or to constrain the set of values or data-types the attribute/feature is associated with. A label, tag, or column header for each dataset attribute/feature is a ColumnMetadata minimal requirement.

The ***ProvenanceMatadata*** entity describes entities and processes involved in producing, delivering, and/or otherwise influencing the dataset. Provenance provides a critical foundation for assessing authenticity, enabling trust, and allowing reproducibility. 
The required provenance metadata strongly depends on the subject matter the dataset belongs to. For example, establishing the origin and ownership of a cultural artifact is sufficient to determine its authenticity.  Instead, a scientific context establishes data integration pipelines according to the collection and pre-processing methods used, and the reproducibility of the experiment requires details about protocols, instruments, etc. 

The ***QualityMetadata*** entity depicts dataset quality measures and indicators. Jointly with provenance metadata, it should provide a basis for enabling the trust and reproducibility of the results depicted by the dataset.


<!-- ````{panels} 
:container: container-lg pb-3
:column: col-lg-12 p-2
:card: rounded

<div class="mermaid" align="left">
classDiagram
SharedData *-- ConsumerLicenceDefinition: has
SharedData *-- ProviderLicenceDefinition: has
DataSharingAgreement <-- DataConsumer: agrees to
DataSharingAgreement <-- DataOwner: agrees to
SharedData <-- DataSharingAgreement: refers to
DataProvisioningAgreement <-- DataProvider: agrees to
DataProvisioningAgreement <-- DataOwner: agrees to
SharedData <-- DataProvisioningAgreement: refers to  
ProviderLicenceDefinition <-- DataProvisioningAgreement: confirms
ConsumerLicenceDefinition <-- DataSharingAgreement : confirms
class DataSharingAgreement
class DataProvisioningAgreement
class SharedData
class DataProvider
class DataOwner
class DataConsumer
class ProviderLicenceDefinition
class ConsumerLicenceDefinition
  
</div>
```` -->

<!-- *Figure 3: The data sharing agreements* -->


```{figure} ./data-sharing-fig3.svg
---
height: 400px
name: 
alt: Data Sharing Model 3
---
_data sharing_ Data Sharing Model 3.
```


The Figure 3 depicts the agreements that must be reached for the sharing of data, and the artifacts generated as results of the commitment signed by the involved roles. The sharing of data implies the definition of two different agreements formally established through specific licenses.

The ***ConsumerLicenseDefinition*** establishes the terms under which the data being shared can be used by the DataConsumer. These terms are agreed upon by the DataOwner and the DataConsumer by signing the ***DataSharingAgreement***. 
This agreement can be negotiated and signed on a per sharing basis, i.e. the DataOwner and the DataConsumer negotiate the terms of the license for a specific SharedData entity or set of SharedData entities. On the other hand, the DataOwner could establish a specific license or set of licenses for sharing a SharedData entity or set of SharedData entities the DataConsumer must agree to get access to the data.

The ***ProviderLicenseDefinition*** establishes the terms under which the data being shared can be made available on the DataProvider infrastructure. These terms are agreed by the DataOwner and the DataProvider by signing the ***DataProvisioningAgreement***. 



```{figure} ./data-sharing-fig4.svg
---
height: 600px
name: 
alt: Data Sharing Model 4
---
_data sharing_ Data Sharing Model 4.
```


The Figure 4 depicts the ***DataSharingPlatform*** components, which is hosted by the  ***DataProvider*** role as the technical infrastructure aimed to support the sharing of data. The platform components are depicted following.

The ***DataCatalog*** provides a way to register the SharedData. 

The ***DataProcessingPlatform*** provides the infrastructure to host and execute data processing pipelines. Typically, such infrastructure provides an environment or sandbox - through virtual machines and/or container-based technology- where the DataConsumer can deploy custom data processing workflows and the corresponding technological stack.  

The ***DataQueryInterface*** supports the execution of queries over the dataset and its associated metadata, e.g. by providing a SPARQL endpoint.

The ***DataSharingCommunication*** provides an informal communication channel to the roles involved in the sharing of data. A chat, wiki, comments platform, or any environment allowing those involved to interact with each other could be used in this way.

The ***DataSharingWorkflow*** provides the environment to reach an agreement (DataSharingAgreement or DataProvisioningAgreement) and establish a license (***ConsumerLicenseDefinition*** or ***ProviderLicenseDefinition*** ), and to cancel an agreement when the agreed conditions have not been satisfied by either party.

The ***DataOwnerInterface*** provides the DataOwner a unified interface to interact with the DataSharingPlatform.

<!-- 
````{panels} 
:container: container-lg pb-3
:column: col-lg-12 p-2
:card: rounded

<div class="mermaid"  align="left">
classDiagram
DataSharingPlatform *-- DataOwnerInterface: provides
DataSharingPlatform *-- DataSharingWorkflow: provides
DataSharingPlatform *-- DataSharingCommunication: provides 
DataOwnerInterface *-- GetAccessWorkflow: provides
DataOwnerInterface *-- Connect: provides
DataOwnerInterface *-- Upload: provides
DataOwnerInterface *-- AdminDataSharing: provides
GetAccessWorkflow *-- FirstAccessWorkflow: has
GetAccessWorkflow *-- SecurityUpdateWorkflow: has
AdminDataSharing *-- SharedData: administrate
AdminDataSharing *-- DataSharingConsumptionReport: provide   
class SharedData
claas GetAccessWorkflow
class SecurityUpdateWorkflow
class FirstAccessWorkflow
class AdminDataSharing
class DataSharingConsumptionReport
class Upload
class Connect
class DataOwnerInterface
class DataSharingPlatform
</div>

````

*Figure 5: The DataOwnerInterface components*
 -->

```{figure} ./data-sharing-fig5.svg
---
height: 400px
name: 
alt: Data Sharing Model 5
---
_data sharing_ Data Sharing Model 5.
```



The Figure 5 depicts the ***DataOwnerInterface*** components, which provides the DataOwner a unified interface to interact with the DataSharingPlatform. The interface components are depicted following.

The ***Connect*** module allows the DataOwner to initiate an authenticated session on the DataSharingPlatform.

The ***GetAccessWorkflow*** module allows the DataOwner to set the authentication details to get access to the platform through the ***FirstAccessWorkflow*** module - e.g. setting of username a passwords accounts-, and to perform security maintenance tasks - e.g., reset a password account- by using the ***SecurityUpdateWorkflow***.

The ***Upload*** module allows the DataOwner to provide access to physical data so that it can be physically consumed. This does not necessarily mean uploading the SharedData to the DataSharingPlatform. Granting access to the data stored on the infrastructure of the DataOwner is also a possible alternative.

The ***AdminDataSharing*** module allows the DataOwner to manage the SharedData and to get summaries and statistics about the usage and consumption of the data being shared through the ***DataSharingConsumptionReport***. The usage and consumption reports can be generated on different levels of granularity: from a per sharing agreement to the set of all SharedData managed by the DataOwner.

<!-- 
````{panels} 
:container: container-lg pb-3
:column: col-lg-12 p-2
:card: rounded

<div class="mermaid"  align="left">
classDiagram
DataSharingPlatform *-- DataCatalogue: provides
DataSharingPlatform *-- DataProcessingPlatform: provides
DataSharingPlatform *-- DataQueryInterface: provides
DataSharingPlatform *-- DataSharingWorkflow: provides
DataSharingPlatform *-- DataSharingCommunication: provides
DataSharingPlatform *-- DataConsumerInterface: provides
DataConsumerInterface *-- GetAccessWorkflow: provides
DataConsumerInterface *-- Connect: provides
DataConsumerInterface *-- Download: provides
DataConsumerInterface *-- DataSharingConsumptionReport: provides
GetAccessWorkflow --* FirstAccessWorkflow: provides
GetAccessWorkflow --* SecurityUpdateWorkflow: provides 
class GetAccessWorkflow
class SecurityUpdateWorkflow
class FirstAccessWorkflow
class DataSharingConsumptionReport
class DataSharingCommunication
class Download
class Connect
class DataCatalogue
class DataProcessingPlatform
class DataQueryInterface
class DataConsumerInterface
class DataSharingPlatform
</div>
````
 -->
<!-- *Figure 6: The DataConsumerInterface components* -->


```{figure} ./data-sharing-fig6.svg
---
height: 600px
name: 
alt: Data Sharing Model 6
---
_data sharing_ Data Sharing Model 6.
```



The Figure 6 depicts the ***DataConsumerInterface*** components, which provides the DataConsumer a unified interface to interact with the DataSharingPlatform. The interface components are depicted following.



The ***Connect*** module allows the DataConsumer to initiate an authenticated session on the DataSharingPlatform.

The ***GetAccessWorkflow*** module allows the DataConsumer to set the authentication details to get access to the platform through the ***FirstAccessWorkflow*** module - e.g. setting of username a passwords accounts-, and to perform security maintenance tasks - e.g., reset a password account- by using the ***SecurityUpdateWorkflow***.

The ***Download*** module allows the DataConsumer to get access to physical data so that it can be physically consumed. This does not necessarily mean downloading the SharedData from the DataSharingPlatform. Getting access to the data stored on the infrastructure of the DataOwner is also a possible alternative.

The ***DataSharingConsumptionReport*** module allows the DataConsumer to get a summary and statistics about its usage and consumption of the data being shared. Typically, the usage and consumption reports are generated in a per sharing agreement granularity level.

---


## Data Sharing Process Evaluation Criteria
This chapter will define the main criteria for evaluating the given data sharing processes.
Because there is a wide range of different data sharing solutions driven by a broad range of different use cases, the goal is to define those characteristics that are common for all data sharing processes.
For a specific data sharing process evaluation, the classification criteria might be further refined and weighted according to the specific patterns of the use case.

Evaluating a single data sharing workflow has always to look at two aspects:
* Does the workflow support the final goal defined by the data sharing role?
* How optimal do the workflow steps support the data sharing role to reach the goal?

The workflows that are evaluated are:
* Data Sharing Workflow
* Upload/Download
* Maintaining Shared Data
* Using common platform components

The evaluation criteria are classified into the following major categories:
* **Generic criteria**
These are criteria that are given by the inherent structure of the shared data and the data sharing roles.
* **Platform criteria**
These criteria define how optimal the given platform supports the data sharing workflows.

### Generic criteria
1. **Role Perspective**
The data sharing workflows have to be evaluated from a data sharing role perspective because they might be very different per role. The  DataPlatformOwner role is seen only as a role that finally enables data sharing and will be ignored. The evaluation will only be done for the DataOwner and DataConsumer perspectives.

2. **Data Profile**
The data profile classifies the base structural properties of the shared data that have a major impact on the sharing workflows. The following properties are considered:
    * **Dynamic versus static data**
Static data are loaded only once and not changed afterward.
Dynamic data is changed typically periodically after the first upload.
A high update frequency may lead to an automatic workflow requirement.
    * **Data Volume**
The volume of the shared data may have a big impact on the processing time of some of the workflows.
    * **Number of Files**
A high number of shared datasets may lead to automatic workflow requirements because manual interaction might become impractical. Also, a completeness overview can become a challenge.
    * **Complexity of metadata**
The complexity of metadata also has an impact on the practicability of workflows. E.g. maintenance of metadata might get challenging if metadata complexity is increasing.

3. **Understandability**
Evaluates how easy it is to understand the workflow(s). Two levels of understanding are considered:
    * **Single Workflow**
Evaluates how easy a single workflow is understood
    * **Overall Workflow**
Evaluates how easy the overall approach of the workflows is understood.

### Platform criteria
1. **Speed** 
Evaluates how fast a workflow is processed on the platform
2. **Simplicity** 
Evaluates how simple a workflow is implemented on the platform
3. **Completeness**
Evaluates whether there are any gaps  not provided by the platform workflow implementation
4. **Reliability**
Evaluates how reliable workflows are implemented by the platform
5. **Robustness**
Evaluates how easy temporary malfunctioning of the platform workflow processing can be overcome
6. **Security**
Evaluates how secure the platform workflows are implemented

---

## Data Sharing Process Evaluation Workflow


```{figure} ./data-sharing-fig7.svg
---
height: 950px
name: 
alt: Data Sharing Model 7
---
_data sharing_ Data Sharing Model 7.
```



The figure shows the proposed evaluation steps group into the following major steps:
1. **Analyse Use Cases**
First, you have to understand the analyzed data sharing solution from a data owner and data consumer perspective.
2. **Evaluation Criteria Scoping**
Depending on the analysis result of the use cases, you decide which criteria are relevant for your analysis and weigh them. E.g. not all data sharing workflows might be relevant for the specific use case. Some might be more important and some might be less important for your use case. It could also make sense to refine at least some of the important for your use case.  
3. **Evaluation of Single Workflows**
In these steps, you analyse in detail the data sharing workflows you defined in the scoping.
4. **Perform Overall Evaluation**
Finally, you look with an overall perspective to the data sharing solution and evaluate against overall criteria e.g. overall understandability.




## Evaluation of LCSB Data Sharing Procedure

This chapter assesses the LSCB Data Sharing Procedure according to the previously depicted criteria. The evaluation is performed in terms of the generic, data profile, and platform criteria. These outcomes have to be further refined and weighted according to the specific characteristics of the use case being addressed.

1. **Analyse Use Cases**
* *What data sharing use cases are supported?*
No explicit described use cases could be identified.

* *What data are shared?*
What data is shared is not explicitly mentioned. The How-to Cards introduction text indicates that “biomedical research data” are shared. Also, How-to Cards are shared that give practical guidance of data management, data protection, lab support, and others. Please note that within this evaluation we consider the How-to Cards also as data. 

* *Who are the data owners?*
The data owners are not explicitly mentioned. It is assumed from the introduction text that researchers from the LCSB are the data owners. From the found portal pages it is unclear whether a broader audience of data owners is supported.

* *What are the requirements of the data owners?*
This is not explicitly stated. The assumption from text wording is that they:
    * are cooperating with other data consumers 
    * need a platform for the cooperation 
    * are willing to share their biomedical research data or knowledge about data management, data protection, lab support, etc. 
    * have an interest for a data consumer role 

* *Who are the data consumers?*
This is not explicitly stated. The assumption from text wording is that it is the same audience as the data owners. From the found portal pages it is unclear whether a broader audience of data consumers (e.g. outside the LCSB organisation) is supported.

* *What are the requirements of the data consumers?*
This is not explicitly stated. The assumption from text wording is that they:
    * have typically difficulties implementing data management, data protection, lab support, etc, and they want to get practical knowledge to improve their processes and setup
    * want to reuse biomedical research data

2. **Evaluation Criteria Scoping**
Some criteria are not used or only partly applied as described in the text below.
No refinement or weighting for the evaluation criteria was done because no argument was found for doing this.
The evaluation is done per data platform/data asset type because the two offerings are implemented independently.
* **Generic criteria**
    * *Role perspective*  
Evaluation is done only from a data owner perspective because the LCBS How-to Cards are purely data owner oriented.
    * *Data Profile*
All subcriteria are considered besides:
        * *Complexity of metadata*
Because none of the data sharing platforms supports the management of metadata. So the only way to share metadata for biomedical research data would be to share them as data, without having any common agreements for their format and contents.

* **Platform criteria**
All criteria will be used.

* **Evaluated workflows**
	Only data owner data sharing workflows are evaluated.
Following data sharing workflows are not evaluated because they seem out of scope of the offered data sharing platforms
    * *Shared Data*
Please note that the offered platforms don’t provide any common metadata approach. Shared Data is limited to the upload and download of data. Therefore any workflows to access the shared data besides uploading and downloading are out of the scope of the evaluated solution.
    * *Data Sharing Communication*
    * *Sharing Consumption Report*
    * *Admin Data Sharing*
Please note that no metadata are shared in a structured way

3. **Evaluation of Single Workflows**

**Biomedical Research Data Sharing**
The LCSB Biomedical Research Data Sharing Procedure provides two platforms:
* *AsperaWEB* 
which is an IBM Aspera deployment at the LCSB supporting end-to-end encrypted data transfer and can handle high data volumes. 
* *ownCloud*
which is a private cloud storage service for the use of LCSB staff and collaborators, suitable for exchanging up to 2 gigabyte-sized files. All communication with the LCSB ownCloud server is SSL encrypted.
Derived from a further documentation link within the LCSB web pages it seems to be based on the server product available [here](http://owncloud.com).

Both platforms are described on the start page under the “Exchange Channels” category.
As a new data owner, you will ask which option to use best. A direct comparison between both is not given for guiding the data owner to a platform recommendation. From reading both texts, the assumption is that for huge data you have to use AsperaWEB. For files up to 2 gigabytes, you could use both without noticing a major difference.

* **First Access Workflow**
    * *Aspera Web*
As described under “Start Page->Aspera Web Quick Guide” you contact your research collaborator at the LCSB-University, so that he initiates the creation of access for you. You will then get an email that contains an URL.
You can access the URL only once to read your password. After you have accessed the URL, this URL is no longer accessible. Although this is not explicitly mentioned, the assumption is that this protects you from somebody else getting access to your email from also getting access to your password.
How much time the workflow typically takes is not mentioned.
    * *ownCloud*
As described under “Start Page->Owncloud” you have to send an email to the LCSB admin team for getting access to the platform. It is not described what email contents the support team expects from you to accept an account creation, what the next steps are, and how much time it takes until you finally get an account. In the end, you will get a so-called LUMS account, which is a different account then for Aspera Web.
External collaborators need also a VPN account so that they can access the LCSB servers. 

* **Security Update Workflow**
For ownCloud, an explanation to managing the credentials can be found [here](https://r3.pages.uni.lu/howto-cards/stable/external/access/passwords). Also for the VPN account, a password change and reset are supported. For AsperaWeb no explanation was found in the LCSB web pages.

* **Connect Workflow**
    * *Aspera Web*
As described under “Start Page->Aspera Web Quick Guide” you have two different connections options.
        * *Standard Web Browser*
    It is defined as the preferred connection option. Firefox 66.x web browser or later is recommended in “Start Page->Aspera Web Quick Guide->section of the guide”.
For the first time, you have to install the “IBM Aspera Connect” client. No further explanation of the "IBM Aspera Connect" client. A Google search leading to [this page](https://www.ibm.com/de-de/products/aspera/technology), explained that it is optimized for high-speed cloud data transfer with lots of capabilities. More details can be found in [this](https://www.ibm.com/downloads/cas/AWOQXB8G) IBM Cloud Technical whitepaper.
If your client Operating System is Windows and you want to use Microsoft Edge as browser, you need a different IBM Aspera Connect client. This you will find only by occasion if you scroll down the documentation.
The documentation is not precise about client operating system requirements for Aspera. From Google search results it seems that Aspera connect is quite independent of client operating systems.
[Here](https://www.ibm.com/aspera/platform-support/) you can find all supported browsers/client operating systems.

        * *Command-Line Tool*
“Start Page->Aspera Web Quick Guide->section of the guide” explains that you will typically use this option if a web browser would not be an option in your environment. It shows how to use the command-line tool, but not how to install it. From Google search {results](https://downloads.asperasoft.com/en/downloads/2) it seems that Aspera client is meant, which supports all common operating systems. 
Besides you can use a diagnostic tool from IBM for troubleshooting connectivity issues. The ICBS pages provide a link to the [IBM Aspera Diagnostic Tool](https://test-connect.asperasoft.com/) tool, but no further explanation or recommendation. 

    * *ownCloud*
For getting access to the platform, you have to send an email to the LCSB admin team. It is not described what email contents they expect to accept an account creation, what the next steps are, and how long it takes until you finally get an account.
As described under “Start Page->Owncloud” you have two different connections options:
        * *Standard Web Browser*
There is no further documentation given, so it seems to be that no additional software is needed. Also, no further web browser release information is given.
A Google search led to [this page](https://doc.owncloud.com/server/user_manual/webinterface.html) which shows exactly what versions are supported, with some uncertainty for the LCBS server version. 
        * *Client Tool*
For the client tool installation documentation is found under “Start Page->Owncloud” 
Installation steps are combined with upload/download steps, so you have to scroll if you are interested in the help of only one topic.

* **Upload Workflow**
The upload workflow is supported by the underlying commonly used platform tools. 
For Aspera Web, the LCBS pages give no upload use explanation. For ownCloud, they give an upload example showing you how data is synchronized between the source and data sharing platform. For Aspera Web, you have to look to the web pages of the tool to get familiar with the offering.
    * *Dynamic versus static data*
No specific explanations are found for the smooth handling of dynamic files, so the assumption is that the data owner has to get familiar with the tool and investigate for himself what dynamic pattern is supported by each platform.
The assumption is therefore that for the handled use cases there are low dynamic requirements and the data owner can find a solution in a reasonable time by looking at the referred tool web pages.
    * *Data Volume*
The AsperaWEB platform supports data transfer in the terabytes range. The ownCloud platform is suitable for exchanging up to 2 gigabyte-sized files.
    * *Number of files*
No specific explanations are found on how to handle a high number of files best. Therefore the assumption is if you would ever have a high number of files for the found use cases they could be combined to a compressed file as part of a common data sharing agreement.
For the ownCloud solution, some directory organisation standards are given that will help to make files more findable. Of course, this approach is limited as anybody knows from searching files on a big file server.
    * *Speed*
Quality features inherited from the deployed platforms (AsperaWeb, Owncloud). No details provided by the How-to Cards. As described above a Google search led for Aspera Web to a white paper, that gave a lot of explanation about speed improvements. For the data owner, it would be useful to know what networking speeds the platforms are offering for uploading huge data. This can have a high impact on the usability of the upload workflow.  
    * *Simplicity*
The upload workflows are implemented through widely known tools, which can be used by non-expert users.
    * *Reliability*
Quality features inherited from the deployed platforms (Aspera, ownCloud). No details provided by the How-to Cards. 
    * *Robustness*
Quality features inherited from the deployed platforms (Aspera, Owncloud). No details provided by the How-to Cards. Especially for high volumes, it would be interesting to know whether in case of errors you can continue a broken upload avoiding to retransmit already successfully transferred data blocks.

    Both platforms seem to offer a technical upload infrastructure. Questions going beyond the technical sharing mechanism can not be answered by the offered LCSB portal pages e.g. data related questions similar to:
    * *How long is the data stored?*
    * *Where is the data stored?*
    * *Are they any replicas, where are they stored, who has access to it?*
    * *What is the process of data deletion and can I rely on it?*

* **Data Sharing Agreement Workflow**
The data sharing workflow is limited to giving access to the data consumers by the underlying commonly used platform tools. Several options are documented on how the underlying password can be sent in a securely.
So there is only an implicit agreement by the data owner by giving access to the data to a user. Any specific constraints for the data use are up to the data owner to communicate and are not supported by the platform.

**Overall Understandability**
For a new user, it is hard to get an overview of the overall approach and pick out some topics of interest. The detailed explanations are very precise, but sometimes only technical component focused, not always designed for the user perspective.


**Overall Security**
Best practices on security issues are spread over different How-to cards. Some of them are reinforced by the workflow and platforms, while others are just recommended practices.

**How-To Card Data Sharing**
The How-To Card data Sharing Procedure is provided by the ownCloud platform. First Access Workflow, Security Update, and Connect Workflows are described as made above for the ownCloud platform.

For the Upload and Data Sharing workflow also a git client is required. Several GUI clients and integrated development environments are proposed. Moreover, URLs are added to the LCBS webpages for getting installation documentation and additional help.
Markdown lightweight markup language is used for text formatting of the How-To cards. Some tips are added to the LCSB web pages on how to write in markdown and for what purposes it should be used. A list of editors is also proposed.

* **Upload Workflow**
For the upload workflow, an explanation is given on how to add and edit a How-To card. 
This How-To card is limited to the formal technical steps that are required, no content-related or structural uniformness guidelines are given.

* **Data Sharing Agreement Workflow**
The data sharing agreement workflow is implicitly done by the push of the data owner to the GitLab platform. He accepts by the push that anybody who has access to target GitLab can read. All additional data sharing agreements are out of the scope of the platform. 

---

## Recommendations for LCSB Data Sharing Procedure Improvement
The offered data sharing workflows can be seen as a kind of providing core IT infrastructure components for offering:
* Data space.
* Encrypted network transfer.
* User account management.
* Sharing data to a limited number of people working commonly for a program/project.
 
It does not contain as part of the data sharing platforms any capability regarding data profiles or metadata or workflows that cover use-case specific data sharing aspects.

Because no background information is available regarding the underlying use cases no speculation is done regarding what could be improved from a use case perspective.

From a FAIR data sharing perspective often many improvement options regarding metadata, data profiles, data standardisation, data cleansing, platform enhancements do exist. On the other hand, additional improvement options require additional resource effort that has to be balanced against the earned business value.

From FAIR principles perspective, the platforms and workflows only provide minimum functionality for data sharing.

Therefore for this section assumption is, that the offerings are good enough for the existing use cases and only recommendations are made for the existing use.

Given this context these are our recommendations to improve the existing LCSB data sharing workflows:

* **Add platform goals and use case types**
    For a new user, it is hard to understand what the data sharing platforms and workflows are used for. If he gets only technical information it is hard to understand for him whether it is the right platform for his data sharing requirements. Some base policies for using the platforms and workflows would also be appreciated. 

* **Overall overview**
    It is hard for a new user to get an overview of the overall setup, the different platform offerings, and intended use. In the given structure of the web pages, the user is lost in cascading pages and technical details and it is hard for him to get an overview and find detailed information for a specific topic of interest. This can lead also to misunderstanding.
It would be useful to get an overall architecture figure and understand from this figure what additional detailed information is related to the shown components.

* **Detailed descriptions**
    The current pages are organized more by technical components and categories and not by a user-centric view. The data sharing model and defined data sharing workflows of this recipe should give an idea of how a data owner looks at data sharing workflows. In our opinion, it would help users to understand portal offerings much better if the documentation would be organized related to the model components we explained at the beginning.

* **Answering typically user questions directly**
    In the analysis part of the recipe, you will also find questions for which the data owner currently finds not a direct answer without further Google search and trying for himself. This should be checked against the current use cases, to find out whether the current explanations should be improved.
Often it is very time-consuming for a user to find from complex tool documents answers for core questions. 

* **Overall security overview**
    It would be useful for a user to get an overall security overview. This would increase confidence for the offered platform. Sometimes very detailed information (e.g. for forwarding of passwords) is there, whereas for other important security aspects information is missing (e.g. data protection of datasets, retention period, who has access).

* **How-To cards**
    For the How-To cards, it would be useful to understand the intent to write and share it. The data management topic is a very broad topic where you find already a lot of information on the web. The assumption is that it is about sharing special aspects for the management of biomedical research data. Also at least showing example workflows, or giving guidance about the content structure and quality would help to promote people for sharing.
Depending on the number of shared How-To cards we could imagine that introduction of metadata would help to make them more findable.

---


## Authors

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Kurt Dauth |  Boehringer Ingelheim | | Writing - Original Draft |
| Emiliano Reynares |  Boehringer Ingelheim | [0000-0002-5109-3716](https://orcid.org/0000-0002-5109-3716) | Writing - Review & Editing. | 

---


## License

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png" height="20"/></a>


