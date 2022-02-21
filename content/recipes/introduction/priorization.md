(fcb-prioritization)=
# Prioritisation of projects for FAIRification

+++
<br/>

````{panels_fairplus}
:identifier_text: FCB055
:identifier_link: 'https://w3id.org/faircookbook/FCB055'
:difficulty_level: 2
:recipe_type: guidance
:reading_time_minutes: 10
:intended_audience:  everyone 
:has_executable_code: nope
:recipe_name: Prioritisation of projects for FAIRification
```` 


## Main Objectives 

The main purpose of this recipe is:

> To provide an overview of elements that should be considered in prioritisation and selection of potential projects, processes, or data for FAIRification. For each of these elements, we provide comparative benefits and  highlight the key reasons for making datasets FAIR.

---
## Introduction
With the increased awareness of the FAIR principles, the drive to implement them can be felt in projects and programs. However, considering the volume and variety of such projects and the finite nature of available resources, it is also necessary to establish a *principled approach* to prioritise datasets for data FAIRification. The present recipe aims to provide insights into how to implement this process by showcasing essential criteria which have been considered and are "battle-tested".  

The structure of the recipe is as follows:
* We begin by identifying reasons why an individual or a project team should make a data set FAIR. 
* Following this, a brief overview of the corpus or dataset formulation that needs to be done by a small group of people. Once “the team” has collected all the necessary data, it can now pass through the prioritisation phase. Here, a thorough assessment of the dataset based on defined criteria is performed. This assessment is, in turn, recorded by means  of a “scorecard”.
* Finally, ranking based on the score each dataset has earned in the scorecard is established and ranked projects or datasets can be prioritised for FAIRification.

---
## Graphical Overview 

<!--
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBKGZhOmZhLXVzZXJzIElkZW50aWZpY2F0aW9uIG9mIHByb2plY3Qgc2VsZWN0aW9uIDxicj4gYW5kIHByaW9yaXRpemF0aW9uIHRlYW0pLS0-IHxDb2xsZWN0IGRhdGFzZXQgcmVsZXZhbnQgaW5mb3JtYXRpb258QlsoUHJvamVjdCBjb3JwdXMgY3JlYXRpb24pXVxuICAgIEItLT4gfENyZWF0aW5nIGZhY3RvciBjaGVja2xpc3R8IEMoZmE6ZmEtdGgtbGlzdCBQcmlvcml0aXphdGlvbiBvZiBwcm9qZWN0cyBiYXNlZCA8YnI-IG9uIGZhY3RvciBsaXN0KVxuICAgIEMtLT4gfEFkZGluZyBwb2ludHMgZm9yIGZhY3RvcnMgaW50byBhIHNjb3JlYm9hcmR8IEQoZmE6ZmEtc29ydCBTY29yZWNhcmQgZm9ybXVsYXRpb24gYW5kIHByb2plY3QgPGJyPiByYW5raW5nKVxuICAiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlLCJhdXRvU3luYyI6dHJ1ZSwidXBkYXRlRGlhZ3JhbSI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/edit#eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBKGZhOmZhLXVzZXJzIElkZW50aWZpY2F0aW9uIG9mIHByb2plY3Qgc2VsZWN0aW9uIDxicj4gYW5kIHByaW9yaXRpemF0aW9uIHRlYW0pLS0-IHxDb2xsZWN0IGRhdGFzZXQgcmVsZXZhbnQgaW5mb3JtYXRpb258QlsoUHJvamVjdCBjb3JwdXMgY3JlYXRpb24pXVxuICAgIEItLT4gfENyZWF0aW5nIGZhY3RvciBjaGVja2xpc3R8IEMoZmE6ZmEtdGgtbGlzdCBQcmlvcml0aXphdGlvbiBvZiBwcm9qZWN0cyBiYXNlZCA8YnI-IG9uIGZhY3RvciBsaXN0KVxuICAgIEMtLT4gfEFkZGluZyBwb2ludHMgZm9yIGZhY3RvcnMgaW50byBhIHNjb3JlYm9hcmR8IEQoZmE6ZmEtc29ydCBTY29yZWNhcmQgZm9ybXVsYXRpb24gYW5kIHByb2plY3QgPGJyPiByYW5raW5nKVxuICAiLCJtZXJtYWlkIjoie1xuICBcInRoZW1lXCI6IFwiZGVmYXVsdFwiXG59IiwidXBkYXRlRWRpdG9yIjpmYWxzZSwiYXV0b1N5bmMiOnRydWUsInVwZGF0ZURpYWdyYW0iOmZhbHNlfQ)
-->

```{figure} images/prioritization-mermaid.png
---
height: 550px
name: Prioritisation overview
alt: Prioritisation overview
---
Prioritisation overview.
```

---
## Determining the need for FAIRification

Before understanding why and how to *prioritise* projects for the FAIR pipeline, it is essential to understand *the need* for the FAIRification of data {footcite}`d3_report`. The list below identifies key reasons why one should make data FAIR: 
* Increase impact and visibility:
	- Standardising published project/dataset metadata using a well-accepted metadata model and becoming indexed by major community resources, helps to increase the visibility and impact of the data within the wider scientific community.
* Harmonise data:
	- Multiple independent resources can be unified into one larger resource with help of common terminologies and ontologies, thereby contributing towards data interoperability.
* Encourages community collaboration:
	- Standardised schemas are the end-result of the FAIRification process. These standardised schemas can bring multiple independent research communities together for potential collaboration.
* Increases the return on investment in R&D:
	- FAIRified data is potentially reusable, meaning that initial investment and newly generated data assets are protected but also that additional investment in redoing research can be avoided.
* Prepares data for downstream tasks:
	- FAIRification aids in the establishment of synergies between downstream tasks. If correctly formatted, this FAIRified data could potentially be machine-readable thereby making its translation into machine learning (ML) or artificial intelligence (AI) models easier. 


Alternatively, there are a number of important ethical benefits to related data FAIRfication. These can be found in a dedicated recipe called [Values of FAIR](https://fairplus.github.io/the-fair-cookbook/content/recipes/introduction/FAIRplus-values.html).

---
## Dataset selection

To ascertain whether a project data set requires FAIRification or not, it is essential to first gather all relevant information about the project and then analyse the resultant information in a stepwise manner. At this moment, it is essential to assemble a group who would take care of the prioritisation process called the **Project Selection and Prioritisation (PSP)** team. This team is an ensemble of people belonging to a wider expertise domain who can provide directionality to the prioritisation task, along with independent feedback.

Project relevant basic information is collected by the PSP team for assisting them in the conceptualisation of a filtering or prioritisation schema. The following basic information can be collected for each of the suitable projects that need to be FAIRified. 
<ol>
	<li>Name</li>
	<li>Objective or aim</li>
	<li>Project timeline (For e.g. start/end date)</li>
	<li>Types of partners involved (For e.g., industry and/or academic partners)</li>
	<li>Contact information of the lead personnel</li>
	<li>Availability of data management plan (Yes/No)</li>
<li>Data accessibility</li>
</ol>

The subsequent sections direct the readers to a possible approach for achieving the prioritisation schema using the information mentioned above.

---
## Scorecard formulation

Once the basic information is collected, the PSP team can start to score each project based on different factors such as data source and type, project timeline, etc.  Below we list examples of different project-based factors and how one can create a score for these factors.  

#### 1. Prioritisation based on project focus area

When dealing with many projects, the PSP team can get an overview of the research or focus area of the given projects. In cases where the aim of the goal is not directly available, a number of approaches can be used to exact this information. If the number of projects under consideration are small (< 15 projects), the team can manually curate this information with help of project leads. In contrast, if a larger number of projects are under consideration, the team can make use of advanced techniques such as natural language processing (NLP) based models to extract the project focus details. Within IMI, we built a small tool, which can be found on [GitHub](https://github.com/Fraunhofer-ITMP/IMI-Project-Prioritization), for mining of project focus area from project summaries.

Based on this focus area, the PSP team can generate an *in-house scoring schema* by enlisting the different focus areas and sorting them based on the team’s interest or objective. Eventually, this in-house scoring schema would be used to score each of the projects.  


#### 2. Prioritisation based on project’s timeline

The process for FAIRification could be done either to the data present in a project or to a processing pipeline that is part of the project. In situations where the project involves external data owners, there is a need to consider the project timeline within the project prioritisation schema since the data would only be available within the defined time span, assuming that no dissemination of data into public repositories is done. 

Furthermore, taking into account the interdependence between the data and project timeline of the data or process within the project, the time span at which a project runs is also an important criteria to understand the availability of the data or pipeline. The project can be divided into three stages of development on the basis of its duration: 
- **Early stage** : A project is in early stages of development when the data requirements for the given project are being listed and simultaneously being collected. At this stage, the amount of data available is at its lowest, and it is easier to design a data model or schema, choose definite ontologies, etc. thereby ensuring creation of ‘FAIR data by design'.
- **Middle stage** : In the middle stage, data relevant for the given project have been collected and need to be standardised for downstream analysis tasks such as inputs into machine learning approaches. This is a stage where there is maximum availability of data, and the project's focus is on algorithmic models or data-based prediction models.
- **End stage**: Lastly, in the end stage, data has either been deposited into public or private repositories or handed over to the respective project heads or consortium leaders. This indicates  that the project is near its termination. Furthermore, it is at this stage that the risk of organisation restructuring is highest, with staff reassignment or departure. 

It becomes essential to mention at this point that based on the time interval the PSP team decides to engage, the FAIRification process coils be prospective or retrospective. If the PSP team undertakes FAIRification process at the early stages of the project, the process is *prospective* as there remains the flexibility to define and lay out the metadata standards for the data and process thereby eliminating many of the downstream logistical and financial problems.. Meanwhile, if the PSP team undertakes the FAIRification process at the end stages of the project, the details of process and data generated may have been lost or are no longer accessible.

the best time of engaging a project into the FAIR pipeline would be dependent on its retrospective and prospective aspects of the data for that project. In conclusion, starting a FAIRification process at a project end stage could be the least favourable as it could place large demands in time and resources on key personnel, including corresponding data stewards and data generators, at a time of effort wind down. Alternatively, starting the FAIRification process in the early or middle stages could be beneficial given the flexibility of data and process structuring, besides providing direct contact with both data owners and generators to gain a better understanding of the data. Thus, with a scoring schema (3 = early stage, 2 = middle stage, 1 = end stage), we can score each of the projects based on the time interval they belong to.

#### 3. Prioritisation based on partners involved in the project
	
A project has the potential to involve a large number of people each coming from various institutions. Since the impact of the FAIRification process would be to benefit as many people as possible, the PSP team can consider the benefits accruable to a wider consortium involved, as a criteria for scoring the projects. 

Thus, projects that have diverse partners involved (e.g.  academic, industrial, start-up, and so on)  should be prioritised over singleton partners, that is those projects that involve people from the same institute or industrial group. The main reason for this priority is the impact of the FAIRification process. 

Within an intra-organization group, the data generators, maintainers, and depositors might have the same terminology and definitions related to the data and hence, a FAIRification process would only be needed when the data has to be deposited on public repositories or databases. 

While in an inter-organization group, definitions and terminologies aren't likely to be consistent, and the transfer of data from data generators to depositors might be time-consuming. As a result, the FAIRification process would be beneficial by increasing transparency between intra-organizational groups.

#### 4. Prioritisation based on existence of data management plan 

A Data Management Plan (DMP) is a document that describes the life cycle of a data beginning from its generation, followed by processing and collection, dissemination, and finally the usage (more details can be found in the [Data Management Plan](https://rdmkit.elixir-europe.org/data_management_plan.html) recipe). This established document gives the data owners and FAIR experts an overview of the data and process resources under study. 

On the basis of this DMP document, a FAIRification process can be determined and established. In case of the absence of a DMP, the FAIR experts lack the ability to find the best FAIRification process for the given data thereby leading to inefficient results. Overall, the DMP plan would potentially point to the data regulatory aspect, considering the data usage as well as dissemination of the data into public resources. 

Thus, projects that have their DMP documents established should get a higher score over those projects that do not have such a plan in place. Furthermore, the scoring can also be considered based on the detailed explanation of the data and process plan thereby providing a definite directionality to the FAIRification process.

#### 5. Prioritisation based on data availability and access

Even when the data is available, it does not necessarily mean that the data is accessible and thus it is essential to ensure both data availability and accessibility aspects of the data before the FAIRification process. For instance, in some situations, data would only be accessible to users within the institute, while in other situations the data is strictly restricted to data producers. An example of such a restricted type of data would be patient health records which contain sensitive data.

The best practice in such situations is to have at least one member from the consortium in the PSP team. This enables easing the FAIRification process in two ways: firstly, it removes the limitation on data accessibility (in cases where the data can only be accessed by an individual within the institute) and secondly, it mediates direct contact with data owners and generators, thus guaranteeing better understanding of the data. 

In the context of data accessibility, different levels or approaches for access can be classified as follows:
- **Accessing via web-interface** : The data is hosted in a cloud system by the data owner, and the access to the data can be done by simply using the web.
- **Programmatic access** : The data is made available via programmatic services such as a REST API. This is mainly of interest to data handlers within the PSP team who can, with a few lines of programmatic code, access the data.
- **No access** : Given the potential confidentiality and legal aspects involved in dealing with the data, certain data owners will be reluctant to provide access to the data. One such example could be a potential lead compound in a pharmaceutical company. Here, the company would give no access to the data either until they have patented the compound or given the compound to clinical trials.

In summary, projects where the PSP team can get access to data and process should have a higher score than those that have limitations on data access as this would be the major driving force for the FAIRification process.

#### 6. Prioritisation based on presence of data champions

**Data champions** can be defined as a group of people that have scientific domain related expertise in dealing with certain processes, data, or pipelines. It is beneficial if such an expert with previous experience in dealing with processes and data is a member of the PSP team. The direct benefit of the presence of a data champion in the PSP team is for determination of the timeline for FAIRification process, prior to its beginning. In turn, this enables the PSP team to set milestones for accomplishing a FAIR process or data. Thus, a higher score should be assigned to projects with in-house (with the PSP team) data champions compared to those where the PSP team lacks data experts.


#### 7. Prioritisation based on data types

Each project may produce a range of data that may be available in a number of different formats. For instance, sequencing data can be in distributed in *FASTQ* format while associated metadata can be described using *INSDC SRA* format or imaging data in *DICOM* format. It is therefore possible to score projects based on this information and more precisely, one may use a resources such as [FAIRsharing](https://fairsharing.org) to do two things:
i. Identify the community approved data type format and terminologies supporting a data type
ii. Identify a funder or publisher recommended repository accepting this data type (e.g. EMBL EBI Array Express for Transcriptomics data)

Hence, projects that have the above two pointers addressed should be prioritised over those that do not and thus, should contain a higher score.

In summation, each project gets a score based on the aforementioned factors and this score-based assessment of projects would in turn lead to development of a scorecard {footcite}`prioritization_template`.

## Prioritisation between different project-based factors

Along with the above project-based factors, two more factors play a crucial role in the scoring process:
-  **Time management**: The FAIRification process can depend on a number of factors, it is important to acknowledge the time required for the process to be completed. 
- **Risk management**: This involves the assessment of potential roadblocks that could interfere being essential and such roadblocks should be identified and rectified, ideally prior to starting a FAIRification process. 

Each of these criteria are treated independently when creating a scorecard, and a personalised priority between these factors needs to be made by the PSP team. Thus, based on the criteria priority selected, the prioritisation between the different project factors can be made. For example, if the PSP team prioritises time management, the “data champions” factor should be at a higher priority over the “data availability and access” factor.


Another prioritisation schema that could be used for intra-factor ranking could be the cost and value benefits of each of the factors {footcite}`10.1162/dint_a_00109`. The cost factors refer to the set of indicators or aspects that influence the costs associated with the FAIRification process, while the value factors can be defined as the value proposition for performing the FAIRification. To provide a granular overview of this criteria, classification based on two factors, cost and value, has been shown in the table below.

<div style="text-align: center;">

| Domain | Criteria |
| ----------- | ----------- |
| Project focus | Value |
| Data champion  | Value |
| Data Type   | Value  |
| Data availability and access | Cost |
| Availability of DMP | Cost |
| Partners involved | Cost  |

</div>

---
## Project ranking and prioritisation

Overall, in the scorecard, each project is assigned a score based on certain criteria. To enable ranking of projects, an additive sum of each of these criteria should be used, thereby assigning each project with one final score. In the end, a descending ranking of the projects can be achieved, and the top projects can be selected for FAIRification by the PSP team and handed over to the people responsible for the FAIRification process. 

The prioritisation and selection schema mentioned in this recipe was successfully adapted and applied for the FAIRification process within IMI {footcite}`d1_report`. A snapshot of the scorecard used within IMI for selecting and prioritising FAIRification projects can be seen below {footcite}`prioritization_template`.

<div style="justify-content: center;">
<img src="/images/score_card_ref.png" style="border:1px solid black"/>
</div> -->

```{figure} score_card_ref.png
---
name: Scorecard template
alt: Scorecard template
---
Scorecard template.
```

---
## Conclusion

> When faced with a large number of projects that need to be FAIRified, it is necessary to establish a process for ranking and prioritising projects based on a scoring metric. This recipe, besides providing a reminder of the benefits of making data FAIR, provides suggestions for assisting in establishing a prioritisation procedure. 

> 
> ## What to read next section
> * [Data Catalogue](fcb-find-bs-catalog)
> * [The Value of FAIR](fcb-intro-fair-values)
> * [Data Management Plan](https://rdmkit.elixir-europe.org/data_management_plan.html)

---
## References

```{footbibliography}
```

---
## Authors

````{authors_fairplus}
Yojana: Writing - Original Draft, Editing, Conceptualization
David: Writing - Review & Editing
Wei: Writing - Review & Editing
AndreaZaliani: Writing - Review & Editing
Philippe: Writing - Review & Editing
Danielle: Review
NickJuty: Review
Philip: Review
````

---
## License

````{license_fairplus}
CC-BY-4.0
````
