(fcb-prioritization)=
# Prioritization of projects for FAIRification

+++

````{panels_fairplus}
:identifier_text: FCB055
:identifier_link: 'https://w3id.org/faircookbook/FCB055'
:difficulty_level: 2
:recipe_type: guidance
:reading_time_minutes: 10
:intended_audience:  everyone 
:maturity_level: 2
:maturity_indicator: 1, 2
:has_executable_code: nope
:recipe_name: Prioritizing projects for FAIRification
```` 


## Main Objectives 

The main purpose of this recipe is:

> To provide an overview of elements that could help users in prioritization and selection of potential project (URL_TO_INSERT_TERM_8783 https://fairsharing.org/search?recordType=project) s,
> processes, or data for FAIR (URL_TO_INSERT_RECORD_8784 https://fairsharing.org/FAIRsharing.WWI10U) ification. 
> For each of these elements, we provide comparative benefits between different stages and justify the order of the 
> stages required for FAIR (URL_TO_INSERT_RECORD_8785 https://fairsharing.org/FAIRsharing.WWI10U) ification. Finally, we also highlight the reasons for making the data FAIR (URL_TO_INSERT_RECORD_8786 https://fairsharing.org/FAIRsharing.WWI10U) .


## Introduction
With the increased awareness of the FAIR (URL_TO_INSERT_RECORD_8789 https://fairsharing.org/FAIRsharing.WWI10U)  principles (URL_TO_INSERT_RECORD_8788 https://fairsharing.org/FAIRsharing.WWI10U) , the drive to implement them can be felt in project (URL_TO_INSERT_TERM_8787 https://fairsharing.org/search?recordType=project) s and programs. 
However, considering the volume and variety of such project (URL_TO_INSERT_TERM_8790 https://fairsharing.org/search?recordType=project) s and the finite nature of available resources, it is also
necessary to establish a *principled approach* to prioritizing datasets for data FAIR (URL_TO_INSERT_RECORD_8791 https://fairsharing.org/FAIRsharing.WWI10U) ification.
The present recipe aims to provide insights into how to go about this process by showcasing essential criteria which 
have been considered and "battle-tested".  

The recipe is structured in the following way:
* We begin by pointing out the reasons why one should to make their dataset FAIR (URL_TO_INSERT_RECORD_8792 https://fairsharing.org/FAIRsharing.WWI10U) . 
* Following this, a brief overview of the dataset corpus formulation. Once "the team" has collected all the necessary data,
it can now pass through the prioritization phase. Here, a thorough assessment of the dataset based on certain criteria is done. 
This assessment, in turn, leads to the development of a "score (URL_TO_INSERT_RECORD_8793 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_8794 https://fairsharing.org/FAIRsharing.xMmOCL) card".
* Finally, with the points each dataset has earned in the score (URL_TO_INSERT_RECORD_8796 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_8797 https://fairsharing.org/FAIRsharing.xMmOCL) card, a ranking can be established and project (URL_TO_INSERT_TERM_8795 https://fairsharing.org/search?recordType=project) s or 
datasets can be prioritized.


## Graphical Overview 

<!--
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBKGZhOmZhLXVzZXJzIElkZW50aWZpY2F0aW9uIG9mIHByb2plY3Qgc2VsZWN0aW9uIDxicj4gYW5kIHByaW9yaXRpemF0aW9uIHRlYW0pLS0-IHxDb2xsZWN0IGRhdGFzZXQgcmVsZXZhbnQgaW5mb3JtYXRpb258QlsoUHJvamVjdCBjb3JwdXMgY3JlYXRpb24pXVxuICAgIEItLT4gfENyZWF0aW5nIGZhY3RvciBjaGVja2xpc3R8IEMoZmE6ZmEtdGgtbGlzdCBQcmlvcml0aXphdGlvbiBvZiBwcm9qZWN0cyBiYXNlZCA8YnI-IG9uIGZhY3RvciBsaXN0KVxuICAgIEMtLT4gfEFkZGluZyBwb2ludHMgZm9yIGZhY3RvcnMgaW50byBhIHNjb3JlYm9hcmR8IEQoZmE6ZmEtc29ydCBTY29yZWNhcmQgZm9ybXVsYXRpb24gYW5kIHByb2plY3QgPGJyPiByYW5raW5nKVxuICAiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlLCJhdXRvU3luYyI6dHJ1ZSwidXBkYXRlRGlhZ3JhbSI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/edit#eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBKGZhOmZhLXVzZXJzIElkZW50aWZpY2F0aW9uIG9mIHByb2plY3Qgc2VsZWN0aW9uIDxicj4gYW5kIHByaW9yaXRpemF0aW9uIHRlYW0pLS0-IHxDb2xsZWN0IGRhdGFzZXQgcmVsZXZhbnQgaW5mb3JtYXRpb258QlsoUHJvamVjdCBjb3JwdXMgY3JlYXRpb24pXVxuICAgIEItLT4gfENyZWF0aW5nIGZhY3RvciBjaGVja2xpc3R8IEMoZmE6ZmEtdGgtbGlzdCBQcmlvcml0aXphdGlvbiBvZiBwcm9qZWN0cyBiYXNlZCA8YnI-IG9uIGZhY3RvciBsaXN0KVxuICAgIEMtLT4gfEFkZGluZyBwb2ludHMgZm9yIGZhY3RvcnMgaW50byBhIHNjb3JlYm9hcmR8IEQoZmE6ZmEtc29ydCBTY29yZWNhcmQgZm9ybXVsYXRpb24gYW5kIHByb2plY3QgPGJyPiByYW5raW5nKVxuICAiLCJtZXJtYWlkIjoie1xuICBcInRoZW1lXCI6IFwiZGVmYXVsdFwiXG59IiwidXBkYXRlRWRpdG9yIjpmYWxzZSwiYXV0b1N5bmMiOnRydWUsInVwZGF0ZURpYWdyYW0iOmZhbHNlfQ)
-->

````{dropdown}
:open:
```{figure} prioritization-mermaid.png
---
height: 450px
name: Prioritization overview
alt: Prioritization overview
---
Prioritization overview.
```
````

<br/>

## Determining the need for FAIRification

Before understanding why and how to *prioritize* project (URL_TO_INSERT_TERM_8798 https://fairsharing.org/search?recordType=project) s for the FAIR (URL_TO_INSERT_RECORD_8799 https://fairsharing.org/FAIRsharing.WWI10U)  pipeline, it is essential to understand 
*the need* for FAIR (URL_TO_INSERT_RECORD_8800 https://fairsharing.org/FAIRsharing.WWI10U) ification of data {footcite}`d3_report`. The list below identifies key reasons why one should make data FAIR (URL_TO_INSERT_RECORD_8801 https://fairsharing.org/FAIRsharing.WWI10U) : 
* Increase impact and visibility:
    - Standard (URL_TO_INSERT_TERM_8802 https://fairsharing.org/search?fairsharingRegistry=Standard) ising published project (URL_TO_INSERT_TERM_8803 https://fairsharing.org/search?recordType=project) /dataset metadata using a well-accepted metadata model (URL_TO_INSERT_TERM_8804 https://fairsharing.org/search?recordType=model_and_format)  and getting indexed by
  major community resources helps in increasing the visibility and impact of the data within the scientific community.
* Harmonise data:
    - When creating a tool with the help of multiple independent resources, FAIR (URL_TO_INSERT_RECORD_8805 https://fairsharing.org/FAIRsharing.WWI10U) ification can help in easing the 
  integration of data sources, for instance with the help of a common terminology (URL_TO_INSERT_TERM_8806 https://fairsharing.org/search?recordType=terminology_artefact) .
* Encourages community collaboration:
    - The FAIR (URL_TO_INSERT_RECORD_8807 https://fairsharing.org/FAIRsharing.WWI10U) ification process can attract communities together for potential collaboration as each of the independent
  communities would now have a structured data format (URL_TO_INSERT_TERM_8808 https://fairsharing.org/search?recordType=model_and_format)  to map (URL_TO_INSERT_RECORD_8809 https://fairsharing.org/FAIRsharing.53edcc)  their data for integration.
* Prepare data for downstream tasks:
    - A FAIR (URL_TO_INSERT_RECORD_8810 https://fairsharing.org/FAIRsharing.WWI10U) ified data is machine-readable and hence can potentially be used by software agents such as machine learning
    (ML) or artificial intelligence (AI) model (URL_TO_INSERT_TERM_8811 https://fairsharing.org/search?recordType=model_and_format) s for analysis with help of downstream.
* Adds to the capitalization on research (URL_TO_INSERT_RECORD_8812 https://fairsharing.org/FAIRsharing.52b22c)  investment:
    - A FAIR (URL_TO_INSERT_RECORD_8813 https://fairsharing.org/FAIRsharing.WWI10U) ified data is reusable, meaning that initial investment and newly generated data assets are protected but
    also that additional investment in redoing research (URL_TO_INSERT_RECORD_8814 https://fairsharing.org/FAIRsharing.52b22c)  can be avoided.

Additional reasons for the need of FAIR (URL_TO_INSERT_RECORD_8815 https://fairsharing.org/FAIRsharing.WWI10U) ification encompass ethical reasons for doing so. These are more fully described 
in a dedicated recipe called [Values of FAIR (URL_TO_INSERT_RECORD_8816 https://fairsharing.org/FAIRsharing.WWI10U) ](https://fairplus.github.io/the-fair-cookbook/content/recipes/introduction/FAIRplus-values.html).


## Dataset selection

To answer whether a project (URL_TO_INSERT_TERM_8817 https://fairsharing.org/search?recordType=project)  requires FAIR (URL_TO_INSERT_RECORD_8819 https://fairsharing.org/FAIRsharing.WWI10U) ification or not, it is essential to first gather all relevant informat (URL_TO_INSERT_TERM_8818 https://fairsharing.org/search?recordType=model_and_format) ion 
about the project (URL_TO_INSERT_TERM_8820 https://fairsharing.org/search?recordType=project) s and then analyze the resultant informat (URL_TO_INSERT_TERM_8821 https://fairsharing.org/search?recordType=model_and_format) ion in a stepwise manner. 

Prior to digging deeper into the selection and prioritization process, it is essential to assemble a group of people who
would take care of the prioritization process, the **Project (URL_TO_INSERT_TERM_8822 https://fairsharing.org/search?recordType=project)  Selection and Prioritization (PSP (URL_TO_INSERT_RECORD_8823 https://fairsharing.org/FAIRsharing.x8xt3k)  (URL_TO_INSERT_RECORD_8824 https://fairsharing.org/FAIRsharing.s63y3p) )** team. 
This team is an ensembl (URL_TO_INSERT_RECORD_8825 https://fairsharing.org/FAIRsharing.fx0mw7) e of people both within and outside the organization (if possible) to provide better directionality 
to the prioritization task.

The informat (URL_TO_INSERT_TERM_8827 https://fairsharing.org/search?recordType=model_and_format) ion that PSP (URL_TO_INSERT_RECORD_8828 https://fairsharing.org/FAIRsharing.x8xt3k)  (URL_TO_INSERT_RECORD_8829 https://fairsharing.org/FAIRsharing.s63y3p)  team users can collect about the project (URL_TO_INSERT_TERM_8826 https://fairsharing.org/search?recordType=project) s covered:
<ol>
	<li>Name</li>
	<li>Objective or aim</li>
	<li>Timeline (For e.g. start/end date)</li>
	<li>Types of partners involved (For e.g., industry and/or academic partners)</li>
	<li>Contact informat (URL_TO_INSERT_TERM_8830 https://fairsharing.org/search?recordType=model_and_format) ion of the leads</li>
	<li>Data and the data types involved</li>
</ol>

With the help of the above-mentioned list, the PSP (URL_TO_INSERT_RECORD_8831 https://fairsharing.org/FAIRsharing.x8xt3k)  (URL_TO_INSERT_RECORD_8832 https://fairsharing.org/FAIRsharing.s63y3p)  team can formulate a filtering or prioritization schema.
The next sections discuss different methods for achieving this. 


## Project prioritization

Once the basic informat (URL_TO_INSERT_TERM_8834 https://fairsharing.org/search?recordType=model_and_format) ion is collected, the PSP (URL_TO_INSERT_RECORD_8835 https://fairsharing.org/FAIRsharing.x8xt3k)  (URL_TO_INSERT_RECORD_8836 https://fairsharing.org/FAIRsharing.s63y3p)  team can now describe project (URL_TO_INSERT_TERM_8833 https://fairsharing.org/search?recordType=project) s through a [scoreboard](https://zenodo.org/record/5778431#.YbikDxNKhH1). 

This score (URL_TO_INSERT_RECORD_8838 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_8839 https://fairsharing.org/FAIRsharing.xMmOCL) board serves the purpose for prioritization of the project (URL_TO_INSERT_TERM_8837 https://fairsharing.org/search?recordType=project) s that would go through the FAIR (URL_TO_INSERT_RECORD_8840 https://fairsharing.org/FAIRsharing.WWI10U) ification process.

Enlisted below are the different aspects that can be considered while creating the score (URL_TO_INSERT_RECORD_8841 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_8842 https://fairsharing.org/FAIRsharing.xMmOCL) board.

This list is not extensive and the PSP (URL_TO_INSERT_RECORD_8843 https://fairsharing.org/FAIRsharing.x8xt3k)  (URL_TO_INSERT_RECORD_8844 https://fairsharing.org/FAIRsharing.s63y3p)  team can modify the criteria based on their needs.

### 1. Prioritization based on focus

When dealing with large number of project (URL_TO_INSERT_TERM_8845 https://fairsharing.org/search?recordType=project) s, the PSP (URL_TO_INSERT_RECORD_8847 https://fairsharing.org/FAIRsharing.x8xt3k)  (URL_TO_INSERT_RECORD_8849 https://fairsharing.org/FAIRsharing.s63y3p)  team can get an overview of the research (URL_TO_INSERT_RECORD_8848 https://fairsharing.org/FAIRsharing.52b22c)  area or focus area of the given project (URL_TO_INSERT_TERM_8846 https://fairsharing.org/search?recordType=project) .

Specifically, project (URL_TO_INSERT_TERM_8850 https://fairsharing.org/search?recordType=project) s from biomedical or clinical areas tend to be associated with a comorbidity or pathology, and
the team can leverage this specific informat (URL_TO_INSERT_TERM_8851 https://fairsharing.org/search?recordType=model_and_format) ion to create a customised prioritization schema. 

If the focus area of the project (URL_TO_INSERT_TERM_8852 https://fairsharing.org/search?recordType=project)  is not available directly, one  makes use of manual curation or certain natural
language processing (NLP) pipelines to extract this informat (URL_TO_INSERT_TERM_8854 https://fairsharing.org/search?recordType=model_and_format) ion from project (URL_TO_INSERT_TERM_8853 https://fairsharing.org/search?recordType=project)  documents. 

One such example of the tool used by IMI is demonstrated on [GitHub (URL_TO_INSERT_RECORD_8855 https://fairsharing.org/FAIRsharing.c55d5e) ](https://github.com (URL_TO_INSERT_RECORD_8856 https://fairsharing.org/FAIRsharing.c55d5e) /Fraunhofer-ITMP/IMI-Project-Prioritization).

An *in-house* prioritization scheme can be established by FAIR (URL_TO_INSERT_RECORD_8858 https://fairsharing.org/FAIRsharing.WWI10U)  experts for selection of relevant project (URL_TO_INSERT_TERM_8857 https://fairsharing.org/search?recordType=project) s for the FAIR (URL_TO_INSERT_RECORD_8859 https://fairsharing.org/FAIRsharing.WWI10U) ification process.

This involves a two-step approach:
<ol>
	<li>Identification of certain priority disease areas, such as CO (URL_TO_INSERT_RECORD_8860 https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD_8861 https://fairsharing.org/FAIRsharing.thskvr) VID-19, neurodegenerative diseases, cardiovascular diseases, etc.</li>
	<li>Prioritizing project (URL_TO_INSERT_TERM_8862 https://fairsharing.org/search?recordType=project) s falling into these priority areas compared to others.</li>
</ol>

### 2. Prioritization based on timeline

The process for FAIR (URL_TO_INSERT_RECORD_8864 https://fairsharing.org/FAIRsharing.WWI10U) ification could be done either to the data present in a project (URL_TO_INSERT_TERM_8863 https://fairsharing.org/search?recordType=project)  or to a processing pipeline that is
part of the project (URL_TO_INSERT_TERM_8865 https://fairsharing.org/search?recordType=project) . 
Due to the interdependence of the data or process with the project (URL_TO_INSERT_TERM_8866 https://fairsharing.org/search?recordType=project) , the time range at which a project (URL_TO_INSERT_TERM_8867 https://fairsharing.org/search?recordType=project)  runs is an 
important criteria to understand the availability of the data or pipeline. 
Taking a deeper look into the data dependency for the FAIR (URL_TO_INSERT_RECORD_8869 https://fairsharing.org/FAIRsharing.WWI10U) ification process, a project (URL_TO_INSERT_TERM_8868 https://fairsharing.org/search?recordType=project)  can be divided into three stages
of development: early stage, middle stage, and end stage.
- A project (URL_TO_INSERT_TERM_8870 https://fairsharing.org/search?recordType=project)  is in early stages of development when the data requirements for the given project (URL_TO_INSERT_TERM_8871 https://fairsharing.org/search?recordType=project)  are being listed and 
simultaneously being collected. At this stage, the data availability is the lowest, and it is easier to design a data model (URL_TO_INSERT_TERM_8872 https://fairsharing.org/search?recordType=model_and_format) ,
choose ontologies (URL_TO_INSERT_TERM_8873 https://fairsharing.org/search?recordType=terminology_artefact)  etc. that ensures creation of FAIR (URL_TO_INSERT_RECORD_8874 https://fairsharing.org/FAIRsharing.WWI10U)  data by design.
- In the middle stage, all the data relevant for the given project (URL_TO_INSERT_TERM_8876 https://fairsharing.org/search?recordType=project)  has been collected and now needs to be standard (URL_TO_INSERT_TERM_8875 https://fairsharing.org/search?fairsharingRegistry=Standard) ised 
for downstream tasks such as for predictions using machine learning approaches. 
This is a stage where there is maximum availability of data. 
- Lastly, in the end stage, data has either been deposited or handed over to the respective heads and the project (URL_TO_INSERT_TERM_8877 https://fairsharing.org/search?recordType=project)  is 
near its termination. Furthermore, it is at this stage that the risk  of organisation restructuring is highest, 
with staff reassignment or departure. Hence, starting a FAIR (URL_TO_INSERT_RECORD_8879 https://fairsharing.org/FAIRsharing.WWI10U) ification process at a project (URL_TO_INSERT_TERM_8878 https://fairsharing.org/search?recordType=project)   end stage could be the
least favourable as this could place large demands in time and resources on key personnel, such as for corresponding
data owners and data generators, at a time of effort wind down.

Hence, the best time of engaging a project (URL_TO_INSERT_TERM_8880 https://fairsharing.org/search?recordType=project)  into the FAIR (URL_TO_INSERT_RECORD_8881 https://fairsharing.org/FAIRsharing.WWI10U)  pipeline would be dependent on the retrospective and 
prospective aspects of the project (URL_TO_INSERT_TERM_8882 https://fairsharing.org/search?recordType=project) . **The best time to FAIR (URL_TO_INSERT_RECORD_8884 https://fairsharing.org/FAIRsharing.WWI10U) ify prospective project (URL_TO_INSERT_TERM_8883 https://fairsharing.org/search?recordType=project) s is the early stage**.
This stage is the best time to define and layout metadata standard (URL_TO_INSERT_TERM_8885 https://fairsharing.org/search?fairsharingRegistry=Standard) s that need to be followed during the project (URL_TO_INSERT_TERM_8886 https://fairsharing.org/search?recordType=project) 's trajectory. 
As a result, it eliminates many of the downstream logistical and financial problems.
On the other hand, **the best time to engage in FAIR (URL_TO_INSERT_RECORD_8888 https://fairsharing.org/FAIRsharing.WWI10U) ification of retrospective project (URL_TO_INSERT_TERM_8887 https://fairsharing.org/search?recordType=project) s is in the middle stage.**
This is because it is a data-rich stage and contact with both data owners and generators could be established for a
better understanding of the data.

### 3. Prioritization based on partners
	
A project (URL_TO_INSERT_TERM_8889 https://fairsharing.org/search?recordType=project)  has the potential to involve a large number of people each coming from various institution (URL_TO_INSERT_TERM_8890 https://fairsharing.org/search?recordType=institution) s. 
Consequently, users can also consider the wider consortia involved as a criteria for prioritizing project (URL_TO_INSERT_TERM_8891 https://fairsharing.org/search?recordType=project) s from a list
of project (URL_TO_INSERT_TERM_8892 https://fairsharing.org/search?recordType=project) s. In the end, the FAIR (URL_TO_INSERT_RECORD_8893 https://fairsharing.org/FAIRsharing.WWI10U) ification process should benefit as many people as possible.

**Thus, project (URL_TO_INSERT_TERM_8894 https://fairsharing.org/search?recordType=project) s that have diverse partners involved (e.g.  academic, industrial, start-up, and so on) should be 
prioritized over singleton partners, that is those project (URL_TO_INSERT_TERM_8895 https://fairsharing.org/search?recordType=project) s that involve people from the same institute or industrial group.** 
The main reason for this priority is the impact of the FAIR (URL_TO_INSERT_RECORD_8896 https://fairsharing.org/FAIRsharing.WWI10U) ification process. 
Within an intra-organization group, the data generators, maintainers, and depositors might have the same terminology (URL_TO_INSERT_TERM_8897 https://fairsharing.org/search?recordType=terminology_artefact) 
and definitions related to the data and hence, a FAIR (URL_TO_INSERT_RECORD_8898 https://fairsharing.org/FAIRsharing.WWI10U) ification process would only be needed when the data has to be 
deposited on public repositories (URL_TO_INSERT_TERM_8900 https://fairsharing.org/search?recordType=repository)  or database (URL_TO_INSERT_TERM_8899 https://fairsharing.org/search?fairsharingRegistry=Database) s. 
On the other hand, in an inter-organization group, definitions and terminologies (URL_TO_INSERT_TERM_8901 https://fairsharing.org/search?recordType=terminology_artefact)  aren't likely to be consistent, 
and the transfer of data from data generators to depositors might be time-consuming. 
As a result, the FAIR (URL_TO_INSERT_RECORD_8902 https://fairsharing.org/FAIRsharing.WWI10U) ification process would be beneficial by increasing transparency between intra-organizational groups.

### 4. Prioritization based on existence of Data Management Plan (DMP)

A data management plan (DMP (URL_TO_INSERT_RECORD_8903 https://fairsharing.org/FAIRsharing.kg1x4z) ) is a document that describes the life cycle of a data beginning from its generation, 
followed by processing and collection (URL_TO_INSERT_TERM_8904 https://fairsharing.org/search?recordType=collection) , then dissemination, and finally the usage 
(More details in [Data Management Plan](https://rdmkit.elixir-europe.org (URL_TO_INSERT_RECORD_8905 https://fairsharing.org/3531) /data_management_plan.html) recipe). 
This established document gives the data owners and FAIR (URL_TO_INSERT_RECORD_8906 https://fairsharing.org/FAIRsharing.WWI10U)  experts an overview of the resource under study. 
On the basis of this DMP (URL_TO_INSERT_RECORD_8907 https://fairsharing.org/FAIRsharing.kg1x4z)  document, a FAIR (URL_TO_INSERT_RECORD_8908 https://fairsharing.org/FAIRsharing.WWI10U) ification process can be determined and established. 
In case of the absence of a DMP (URL_TO_INSERT_RECORD_8909 https://fairsharing.org/FAIRsharing.kg1x4z) , the FAIR (URL_TO_INSERT_RECORD_8910 https://fairsharing.org/FAIRsharing.WWI10U)  experts lack the ability to find the best FAIR (URL_TO_INSERT_RECORD_8911 https://fairsharing.org/FAIRsharing.WWI10U) ification process for the given 
data thereby leading to inefficient results. 
Overall, the DMP (URL_TO_INSERT_RECORD_8912 https://fairsharing.org/FAIRsharing.kg1x4z)  plan would potentially point to the data regulator (URL_TO_INSERT_RECORD_8913 https://fairsharing.org/FAIRsharing.ey49c6) y aspect, considering the data usage as well as
dissemination of the data into public resources.
**Thus, project (URL_TO_INSERT_TERM_8914 https://fairsharing.org/search?recordType=project) s that have their DMP (URL_TO_INSERT_RECORD_8916 https://fairsharing.org/FAIRsharing.kg1x4z)  documents established should be prioritized over those project (URL_TO_INSERT_TERM_8915 https://fairsharing.org/search?recordType=project) s that do not have one ready yet.**

### 5. Prioritization based on data availability and access

Even when the data is available, it does not necessarily mean that the data is accessible, and thus it is essential 
to ensure both data availability and accessibility before the FAIR (URL_TO_INSERT_RECORD_8917 https://fairsharing.org/FAIRsharing.WWI10U) ification process. 
In most situations, the data would only be accessible to users within the consortium, while in other situations the 
data is strictly restricted to data producers such as health records, especially for sensitive data.

The best practice in such situations is to have at least one member from the consortium in the **FAIR (URL_TO_INSERT_RECORD_8918 https://fairsharing.org/FAIRsharing.WWI10U)  experts team**,
the team involved in the FAIR (URL_TO_INSERT_RECORD_8919 https://fairsharing.org/FAIRsharing.WWI10U) ification process. This enables easing the FAIR (URL_TO_INSERT_RECORD_8920 https://fairsharing.org/FAIRsharing.WWI10U) ification process in 2 ways: 
first, it removes the limitation for data availability (in cases the data can only be accessed by an individual within the consortium)
and second, it allows direct contact with data owners and generators, a guarantee for better understanding of the data. 

When mentioned data accessibility, this could be broadly classified into three categories:
- **Accessing via web-interface** - Here, the data is hosted by the data owner in a cloud system and the relevant data
can be accessed using the web simply.
- **Programmatic access** - Here, the data is made available via programmatic services such as REST API. 
This is mainly of interest to data handle (URL_TO_INSERT_RECORD_8922 https://fairsharing.org/FAIRsharing.0b7e54) rs within the FAIR (URL_TO_INSERT_RECORD_8921 https://fairsharing.org/FAIRsharing.WWI10U)  expert team who can with few lines of programmatic code access the data.
- **No access** - Here, given the confidentiality and legal aspects involved in dealing with the data, certain data
owners will be reluctant to provide access to the data. One such example in this case could be a potential lead
compound in a pharmaceutical company. Here, the company would give no access to the data until they have patented
the compound or given the compound to clinical trial.

**In summary, project (URL_TO_INSERT_TERM_8923 https://fairsharing.org/search?recordType=project) s that FAIR (URL_TO_INSERT_RECORD_8924 https://fairsharing.org/FAIRsharing.WWI10U)  experts can get access to data should be at a higher priority than those that have
limitations on data access.**

### 6. Prioritization based on presence of data champions

**Data champions** can be defined as a group of people that have an expertise in dealing with certain processes, data,
or pipeline. When dealing with specific processes or data types, it is beneficial if an expert who has experience in 
dealing with such processes or data already exists within the FAIR (URL_TO_INSERT_RECORD_8925 https://fairsharing.org/FAIRsharing.WWI10U)  expert team.

**Prioritization of project (URL_TO_INSERT_TERM_8926 https://fairsharing.org/search?recordType=project) s with consideration of expertise required in dealing with FAIR (URL_TO_INSERT_RECORD_8927 https://fairsharing.org/FAIRsharing.WWI10U) ification tasks should be done.** 
Such project (URL_TO_INSERT_TERM_8928 https://fairsharing.org/search?recordType=project) s can then have a predetermined timeline involved, making the step-by-step approach for accomplishing a 
FAIR (URL_TO_INSERT_RECORD_8929 https://fairsharing.org/FAIRsharing.WWI10U)  process or data comparatively easy.

### 7. Prioritization based on data types

Each project (URL_TO_INSERT_TERM_8930 https://fairsharing.org/search?recordType=project)  may produce a range of data that may be available in a number of different format (URL_TO_INSERT_TERM_8931 https://fairsharing.org/search?recordType=model_and_format) s. 
For instance, sequencing data can be in distributed in *FAST (URL_TO_INSERT_RECORD_8933 https://fairsharing.org/FAIRsharing.p5df9c) Q* format (URL_TO_INSERT_TERM_8932 https://fairsharing.org/search?recordType=model_and_format)  while associated metadata be described using
*INSD (URL_TO_INSERT_RECORD_8937 https://fairsharing.org/FAIRsharing.mKDii0) C (URL_TO_INSERT_RECORD_8939 https://fairsharing.org/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD_8942 https://fairsharing.org/3547)  SRA (URL_TO_INSERT_RECORD_8943 https://fairsharing.org/FAIRsharing.g7t2hv) * format (URL_TO_INSERT_TERM_8934 https://fairsharing.org/search?recordType=model_and_format)  or imaging data in *DICO (URL_TO_INSERT_RECORD_8936 https://fairsharing.org/FAIRsharing.b9znd5)  (URL_TO_INSERT_RECORD_8940 https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD_8941 https://fairsharing.org/FAIRsharing.thskvr) M (URL_TO_INSERT_RECORD_8938 https://fairsharing.org/FAIRsharing.b7z8by) * format (URL_TO_INSERT_TERM_8935 https://fairsharing.org/search?recordType=model_and_format) . 
It is therefore possible to rank project (URL_TO_INSERT_TERM_8944 https://fairsharing.org/search?recordType=project) s based on this informat (URL_TO_INSERT_TERM_8945 https://fairsharing.org/search?recordType=model_and_format) ion and more precisely, one may use a resources
such as [FAIRsharing](https://fairsharing.org (URL_TO_INSERT_RECORD_8946 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_8947 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_8948 https://fairsharing.org/3538) ) to do two things:

i. Identify the community approved data type format (URL_TO_INSERT_TERM_8949 https://fairsharing.org/search?recordType=model_and_format)  and terminologies (URL_TO_INSERT_TERM_8950 https://fairsharing.org/search?recordType=terminology_artefact)  supporting a data type

ii. Identify a funder (URL_TO_INSERT_TERM_8952 https://fairsharing.org/search?recordType=funder)  or publisher recommended repository (URL_TO_INSERT_TERM_8951 https://fairsharing.org/search?recordType=repository)  accepting this data type (e.g. EMBL EBI Array Express for Transcriptomics data)

**Hence, project (URL_TO_INSERT_TERM_8953 https://fairsharing.org/search?recordType=project) s that have the above two pointers addressed should be prioritized over those that do not.**

In summation, each project (URL_TO_INSERT_TERM_8954 https://fairsharing.org/search?recordType=project)  gets a score (URL_TO_INSERT_RECORD_8956 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_8958 https://fairsharing.org/FAIRsharing.xMmOCL)  based on the aforementioned factors and this score (URL_TO_INSERT_RECORD_8957 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_8959 https://fairsharing.org/FAIRsharing.xMmOCL) -based assessment of project (URL_TO_INSERT_TERM_8955 https://fairsharing.org/search?recordType=project) s 
would in turn lead to development of a score (URL_TO_INSERT_RECORD_8960 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_8961 https://fairsharing.org/FAIRsharing.xMmOCL) card {footcite}`prioritization_template`.

## Prioritisation between different project-based factors

Along with the above criteria, two more factors play a crucial role in the prioritization process:

- The first is the **time management**. Since the FAIR (URL_TO_INSERT_RECORD_8962 https://fairsharing.org/FAIRsharing.WWI10U) ification process can depend on a number of factors,
it is important to acknowledge the time required for the process to complete. 

- The second is  **risk management**, with the assessment of potential roadblocks that could interfere essential. 
Such roadblocks should be identified and rectified if possible prior to starting a FAIR (URL_TO_INSERT_RECORD_8963 https://fairsharing.org/FAIRsharing.WWI10U) ification process. 

 
Each of these criteria have an independent stance and when creating a score (URL_TO_INSERT_RECORD_8964 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_8965 https://fairsharing.org/FAIRsharing.xMmOCL) board, a personalized priority between 
these factors need to be made. For example, if people have data champions within their FAIR (URL_TO_INSERT_RECORD_8966 https://fairsharing.org/FAIRsharing.WWI10U) ification team, they would 
prioritize data availability and access factor over the data champions factor. 

Another prioritisation schema that could be used for intra-factor ranking could be the cost and value benefits of each of the factors {footcite}`10.1162/dint_a_00109`. 
The cost factors refer to the set of indicators or aspects that influence the costs associated with the FAIR (URL_TO_INSERT_RECORD_8967 https://fairsharing.org/FAIRsharing.WWI10U) ification
process, while the value factors can be defined as the value proposition for performing the FAIR (URL_TO_INSERT_RECORD_8968 https://fairsharing.org/FAIRsharing.WWI10U) ification. 
To provide a granular overview of this criteria, classification based on two factors, cost and value, has been shown in the table below.


| Value criteria | Cost criteria |
| ----------- | ----------- |
| Project (URL_TO_INSERT_TERM_8969 https://fairsharing.org/search?recordType=project)  focus | Data availability and access |
| Data champion  | Availability of DMP (URL_TO_INSERT_RECORD_8970 https://fairsharing.org/FAIRsharing.kg1x4z)  |
| Data Type   | Partners involved |

---

## Project ranking and prioritisation

Overall, in the score (URL_TO_INSERT_RECORD_8972 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_8974 https://fairsharing.org/FAIRsharing.xMmOCL) card, each project (URL_TO_INSERT_TERM_8971 https://fairsharing.org/search?recordType=project)  is assigned a score (URL_TO_INSERT_RECORD_8973 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_8975 https://fairsharing.org/FAIRsharing.xMmOCL)  based on certain criteria. 
To enable ranking of project (URL_TO_INSERT_TERM_8976 https://fairsharing.org/search?recordType=project) s, an additive sum of each of these criteria should be used, thereby assigning each 
project (URL_TO_INSERT_TERM_8977 https://fairsharing.org/search?recordType=project)  with one final score (URL_TO_INSERT_RECORD_8978 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_8979 https://fairsharing.org/FAIRsharing.xMmOCL) . 
In the end, a descending ranking of the project (URL_TO_INSERT_TERM_8980 https://fairsharing.org/search?recordType=project) s can be achieved, and the top project (URL_TO_INSERT_TERM_8981 https://fairsharing.org/search?recordType=project) s can be selected for FAIR (URL_TO_INSERT_RECORD_8982 https://fairsharing.org/FAIRsharing.WWI10U) ification
by the PSP (URL_TO_INSERT_RECORD_8983 https://fairsharing.org/FAIRsharing.x8xt3k)  (URL_TO_INSERT_RECORD_8985 https://fairsharing.org/FAIRsharing.s63y3p)  team and handed over to the people responsible for the FAIR (URL_TO_INSERT_RECORD_8984 https://fairsharing.org/FAIRsharing.WWI10U) ification process.

The prioritisation and selection schema mentioned in this recipe was successfully adapted and applied for the 
FAIR (URL_TO_INSERT_RECORD_8986 https://fairsharing.org/FAIRsharing.WWI10U) ification process within IMI {footcite}`d1_report`.
A snapshot of the score (URL_TO_INSERT_RECORD_8988 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_8989 https://fairsharing.org/FAIRsharing.xMmOCL) card used within IMI for selecting and prioritising FAIR (URL_TO_INSERT_RECORD_8990 https://fairsharing.org/FAIRsharing.WWI10U) ification project (URL_TO_INSERT_TERM_8987 https://fairsharing.org/search?recordType=project) s
can be seen below {footcite}`prioritization_template`.


<!--
<div style="justify-content: center;">
<img src="/images/score_card_ref.png" style="border:1px solid black"/>
</div> -->

````{dropdown}
:open:
```{figure} ../../../images/score_card_ref.png
---
width: 550px
name: Score (URL_TO_INSERT_RECORD_8991 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_8992 https://fairsharing.org/FAIRsharing.xMmOCL)  card template
alt: Score (URL_TO_INSERT_RECORD_8993 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_8994 https://fairsharing.org/FAIRsharing.xMmOCL)  card template
---
Score (URL_TO_INSERT_RECORD_8995 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_8996 https://fairsharing.org/FAIRsharing.xMmOCL)  card template.
```
````


---
## Conclusion

Faced with a larger number of project (URL_TO_INSERT_TERM_8997 https://fairsharing.org/search?recordType=project) s needing FAIR (URL_TO_INSERT_RECORD_8999 https://fairsharing.org/FAIRsharing.WWI10U) ification, it is necessary to establish a process for ranking and prioritizing these project (URL_TO_INSERT_TERM_8998 https://fairsharing.org/search?recordType=project) s. The recipe, besides reminding the benefits of making their data FAIR (URL_TO_INSERT_RECORD_9000 https://fairsharing.org/FAIRsharing.WWI10U) , provided suggestions for assisting in establishing a prioritization procedure. 
Hence, the aim of the recipe was to provide the readers with a wider perspective of criteria they could use for ordering project (URL_TO_INSERT_TERM_9001 https://fairsharing.org/search?recordType=project) s or datasets for FAIR (URL_TO_INSERT_RECORD_9002 https://fairsharing.org/FAIRsharing.WWI10U) ification and enable them to personalize the ranking of factors based on their needs or requirements. 
Additionally, it provides the readers with a score (URL_TO_INSERT_RECORD_9003 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_9004 https://fairsharing.org/FAIRsharing.xMmOCL) card template that may be translated and used for their use cases.
 
### What to read next?
* [Data catalog](fcb-find-bs-catalog)
* [The Value of FAIR (URL_TO_INSERT_RECORD_9005 https://fairsharing.org/FAIRsharing.WWI10U) ](fcb-intro-fair-values)
* [Data Management Plan](https://rdmkit.elixir-europe.org (URL_TO_INSERT_RECORD_9006 https://fairsharing.org/3531) /data_management_plan.html)

````{rdmkit_panel}
````

## References
````{dropdown} **Reference**
```{footbibliography}
```
````
<!--
1. [Report on IMI projects for data types and current technical solutions](https://zenodo.org/record/4428721#.YbmWNL3MJPZ)
1. [The first 15 IMI data sets selected and available for inclusion in WP 2](https://zenodo.org/record/4428746#.YboFUr3MJPZ)
1. [Exploring the current practices: Cost and Benefits](https://direct.mit.edu/dint/article/3/4/507/107429/Exploring-the-Current-Practices-Costs-and-Benefits)
1. [Scorecard formulation template](https://zenodo.org/record/5778431#.YbikDxNKhH1)
-->

## Authors

````{authors_fairplus}
Yojana: Writing - Original Draft, Editing, Conceptualization
David: Writing - Review & Editing
Wei: Writing - Review & Editing
AndreaZaliani: Writing - Review & Editing
Philippe: Writing - Review & Editing
````

## License

````{license_fairplus}
CC-BY-4.0
````


