(fcb-fairification-process)=
# A framework for FAIRification processes




````{panels_fairplus}
:identifier_text: FCB079
:identifier_link: 'https://w3id.org/faircookbook/FCB079'
:difficulty_level: 2
:recipe_type: applied_example
:reading_time_minutes: 20
:intended_audience: everyone
:maturity_level: 0  
:maturity_indicator: 0
:has_executable_code: nope
:recipe_name: Introducing our FAIRification framework
```` 


## Main Objectives

This recipe provides a general introduction to the FAIR (URL_TO_INSERT_RECORD_9781 https://fairsharing.org/FAIRsharing.WWI10U) ification Framework developed (URL_TO_INSERT_RECORD_9783 https://fairsharing.org/FAIRsharing.31385c)  by FAIR (URL_TO_INSERT_RECORD_9782 https://fairsharing.org/FAIRsharing.WWI10U) plus. 

The recipe will cover the following elements:

>* The components of the framework
>* Some practical considerations for applying the framework 

This recipe will not provide instructions on how to practically implement the framework as this is covered elsewhere in this Cookbook (URL_TO_INSERT_RECORD_9784 https://fairsharing.org/FAIRsharing.cbz72b) .

<!--TO (URL_TO_INSERT_RECORD_9785 https://fairsharing.org/FAIRsharing.w69t6r)  DO add link to BYOD recipe once it is available -->

---


## Graphical Overview

<!-- [FAIR (URL_TO_INSERT_RECORD_9786 https://fairsharing.org/FAIRsharing.WWI10U) ification Framework](./FAIR (URL_TO_INSERT_RECORD_9787 https://fairsharing.org/FAIRsharing.WWI10U) ificationFramework.png) -->

````{dropdown} **FAIRification framework**
:open:

```{figure} ./FAIRificationFramework.png
---
width: 800px
name: fairification-process
alt: FAIR (URL_TO_INSERT_RECORD_9788 https://fairsharing.org/FAIRsharing.WWI10U) ification framework
---
FAIR (URL_TO_INSERT_RECORD_9789 https://fairsharing.org/FAIRsharing.WWI10U) ification framework
```
````

---


## The FAIRification Framework

The FAIR (URL_TO_INSERT_RECORD_9791 https://fairsharing.org/FAIRsharing.WWI10U) plus FAIR (URL_TO_INSERT_RECORD_9792 https://fairsharing.org/FAIRsharing.WWI10U) ification Framework was developed (URL_TO_INSERT_RECORD_9795 https://fairsharing.org/FAIRsharing.31385c)  to address the significant demand for hands-on, practical advice on how to translate general and high-level FAIR (URL_TO_INSERT_RECORD_9793 https://fairsharing.org/FAIRsharing.WWI10U)  principles into actionable, "tried and tested" processes. The framework was developed (URL_TO_INSERT_RECORD_9796 https://fairsharing.org/FAIRsharing.31385c)  in an iterative fashion by a multi-disciplinary team of research (URL_TO_INSERT_RECORD_9794 https://fairsharing.org/FAIRsharing.52b22c)  scientists, data managers and software engineers from both academia and the pharmaceutical industry, and tested on a range of IMI partner project (URL_TO_INSERT_TERM_9790 https://fairsharing.org/search?recordType=project) s.

The framework consists of 3 components:
>* a reusable  FAIR (URL_TO_INSERT_RECORD_9797 https://fairsharing.org/FAIRsharing.WWI10U) ification Process, which outlines the main phases of a FAIR (URL_TO_INSERT_RECORD_9798 https://fairsharing.org/FAIRsharing.WWI10U) ification activity
>* a FAIR (URL_TO_INSERT_RECORD_9800 https://fairsharing.org/FAIRsharing.WWI10U) ification Template, which breaks down key elements of the process into a series of steps to follow when undertaking a FAIR (URL_TO_INSERT_RECORD_9801 https://fairsharing.org/FAIRsharing.WWI10U)  transformat (URL_TO_INSERT_TERM_9799 https://fairsharing.org/search?recordType=model_and_format) ion
>* a FAIR (URL_TO_INSERT_RECORD_9803 https://fairsharing.org/FAIRsharing.WWI10U) ification Workplan layout, which provides a structure for organising FAIR (URL_TO_INSERT_RECORD_9804 https://fairsharing.org/FAIRsharing.WWI10U)  implementation work tailored to the needs of a specific project (URL_TO_INSERT_TERM_9802 https://fairsharing.org/search?recordType=project) .


### The FAIRification Process

The **FAIR (URL_TO_INSERT_RECORD_9805 https://fairsharing.org/FAIRsharing.WWI10U) ification process**  can be divided into four phases:
> 1. FAIR (URL_TO_INSERT_RECORD_9806 https://fairsharing.org/FAIRsharing.WWI10U) ification goal definition
> 2. Requirement examination
> 3. Design and Implementation
> 4. Review

<!-- [FAIR (URL_TO_INSERT_RECORD_9807 https://fairsharing.org/FAIRsharing.WWI10U) ification Process](./FAIR (URL_TO_INSERT_RECORD_9808 https://fairsharing.org/FAIRsharing.WWI10U) ificationProcess.png) -->

```{note}
Each of these phases are sequential dependent on each other and involve two to three groups working on them:
1. The first group is the data or project owner who plays the major role in definition of goals and reviewing the impact of the goals. 
   
2. The second group involves the technicians who specialize in processing and analyzing the data to work towards the goal.
They might be a subset of the data owner group, but a clear distinct between these groups should be made to delegate 
responsibilities and to attain results efficiently. 

3. The third group is assessment group who are responsible for checking the alignment of the task done by the technician
team and the goals set by the FAIRification team. The individuals involved in this team are not part of discussions 
between the data owners and technicians and hence act as peer-reviewers. 
```

In the following sections, we will discuss in depth the work involved in the individual phases of the FAIR (URL_TO_INSERT_RECORD_9809 https://fairsharing.org/FAIRsharing.WWI10U) Ification pipeline.

#### Phase 1: define FAIRification goals

This phase involves the identification of outcomes and planning of goals that data or project (URL_TO_INSERT_TERM_9810 https://fairsharing.org/search?recordType=project)  owner would want to achieve
upon FAIR (URL_TO_INSERT_RECORD_9811 https://fairsharing.org/FAIRsharing.WWI10U) ification of the data. 
These goals are either **centric to one aspect of FAIR (URL_TO_INSERT_RECORD_9812 https://fairsharing.org/FAIRsharing.WWI10U) **, for example *deposition of data to
Zenodo (URL_TO_INSERT_RECORD_9813 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_9814 https://fairsharing.org/FAIRsharing.wy4egf) * to increase its findability, or they could cover **multiple aspects of FAIR (URL_TO_INSERT_RECORD_9815 https://fairsharing.org/FAIRsharing.WWI10U) **, such as *use of consistent 
terminologies (URL_TO_INSERT_TERM_9816 https://fairsharing.org/search?recordType=terminology_artefact)  and controlled vocabularies to represent the data (interoperability aspect) along with deposition of data
in relevant repositories (URL_TO_INSERT_TERM_9817 https://fairsharing.org/search?recordType=repository)  (findability aspect)*. 

Sometimes, the data/project (URL_TO_INSERT_TERM_9818 https://fairsharing.org/search?recordType=project)  owner may be at a loss when tasked with spelling out a clear FAIR (URL_TO_INSERT_RECORD_9819 https://fairsharing.org/FAIRsharing.WWI10U) ification goal. 
In that case, tools such as the [Dataset Maturity (DSM) model](https://fairplus.github.io/Data-Maturity/) can assist in identification of goals.
Check out the [DSM recipe](../maturity.md) for more details on how the tool is able to accomplish it.

#### Phase 2: examine requirements

Upon identification of the goal by the data owners, a discussion with the technical team is done.
The technical team then start with collection (URL_TO_INSERT_TERM_9820 https://fairsharing.org/search?recordType=collection)  of the data to ensure that they have access to the data that needs to be FAIR (URL_TO_INSERT_RECORD_9821 https://fairsharing.org/FAIRsharing.WWI10U) ified. 
If the technical team is external, certain legal aspects need to be placed for efficient transition of data between the
data owners and technicians (for example a DPIA may be needed, see this recipe (dpia.md) for more details).

Following this, the technical team identifies tools and expertise required for the implementation of the work and start
cataloging this material. Lastly, the team collectively decides on the individuals that would be assigned the FAIR (URL_TO_INSERT_RECORD_9822 https://fairsharing.org/FAIRsharing.WWI10U) ification task.

At the end of this phase, an "action" team (subset of the technical team whose goal is to perform the FAIR (URL_TO_INSERT_RECORD_9823 https://fairsharing.org/FAIRsharing.WWI10U) ification tasks)
is in place along with a catalog of tools and resources that would be used for achieving this goal.

#### Phase 3: assess, design, implement, repeat

Following the selection of the "action" team, an iterative cycle of assessment, design, and implementation in put in place. 

**Assessment :**
Prior to starting the work, the assessment of goals is done to ensure that individuals in the action team are updated and clear 
with the FAIR (URL_TO_INSERT_RECORD_9824 https://fairsharing.org/FAIRsharing.WWI10U) ification goals formulated by the data owners. This assessment is carried out by review team which could
be an independent team or certain individuals from the technical team who are not involved in the action team. 
The assessment involves a binary decision of "GO (URL_TO_INSERT_RECORD_9825 https://fairsharing.org/FAIRsharing.6xq0ee) " or "NO GO (URL_TO_INSERT_RECORD_9826 https://fairsharing.org/FAIRsharing.6xq0ee) " based on the FAIR (URL_TO_INSERT_RECORD_9827 https://fairsharing.org/FAIRsharing.WWI10U) ification goals and the catalog provided.
At this stage, the reviews can also provide suggestion based on their experiences on the resources, tool, or goals.

**Design :**
Once the team receives a "GO (URL_TO_INSERT_RECORD_9828 https://fairsharing.org/FAIRsharing.6xq0ee) " decision from the review team, the action team now starts by enlisting (URL_TO_INSERT_RECORD_9829 https://fairsharing.org/FAIRsharing.q7bkqr)  the steps that 
need to be done performed to achieve the goal. For each task, the resources, an estimate time duration, 
as well as the responsible person is selected. 

**Implementation :**
Once the tasks have been selected and assigned, the actual work begins. 
To ensure that the action team is working smoothly, weekly or bi-weekly meetings is recommended so that the team is
aware of the progress.

Once the implementation of task listed in the design phase are done, the action team assess the work done and checks the
aligned with the FAIR (URL_TO_INSERT_RECORD_9830 https://fairsharing.org/FAIRsharing.WWI10U) ification goal. In case more tasks are needed to achieve the goal, a second round of the 
assess-review-implement cycle takes place as described above with the starting point as the FAIR (URL_TO_INSERT_RECORD_9831 https://fairsharing.org/FAIRsharing.WWI10U) ification goals,
the completed tasks and the proposed task

This phase is usually run in short sprints (URL_TO_INSERT_RECORD_9832 https://fairsharing.org/FAIRsharing.h8r843)  of 3-month.

#### Phase 4: review against the goals

At this phase, the FAIR (URL_TO_INSERT_RECORD_9833 https://fairsharing.org/FAIRsharing.WWI10U) ification work has been completed by the team. The technical team and the data owners now come 
together to assess the output of FAIR (URL_TO_INSERT_RECORD_9834 https://fairsharing.org/FAIRsharing.WWI10U) ification. At this point, the technical team packages all the work done and hands
it over to the data owners. Decisions on the key learning as well as future aspects of the work take place. 
Finally, to ensure that the work done is sustainable, the deposition of workflows and the informat (URL_TO_INSERT_TERM_9835 https://fairsharing.org/search?recordType=model_and_format) ion on steps is 
deposited on online catalogs and recipe book (URL_TO_INSERT_RECORD_9836 https://fairsharing.org/FAIRsharing.cbz72b) s such as teh Cookbook (URL_TO_INSERT_RECORD_9837 https://fairsharing.org/FAIRsharing.cbz72b) , RDMKit, IMI Data Catalog (URL_TO_INSERT_RECORD_9838 https://fairsharing.org/FAIRsharing.de533c)  to name a few.

### The FAIRification Template

The FAIR (URL_TO_INSERT_RECORD_9839 https://fairsharing.org/FAIRsharing.WWI10U) ification template provide an outline of possible FAIR (URL_TO_INSERT_RECORD_9840 https://fairsharing.org/FAIRsharing.WWI10U) ification aspects a dataset could be considered for. 

```{note}
This template was formulated based on retrospective and prospective experiences of FAIRification of 
datasets within IMI FAIRplus and does not represent the exhaustive list of all potential FAIRification aspects.
```

The template provides an overview on the data from 3 perspectives: Contents related, Representation and format (URL_TO_INSERT_TERM_9841 https://fairsharing.org/search?recordType=model_and_format) , and the 
hosting (URL_TO_INSERT_RECORD_9842 https://fairsharing.org/FAIRsharing.q7bkqr)  environment capabilities. Covering these three aspects, 8 steps are required for the implementation of the 
FAIR (URL_TO_INSERT_RECORD_9843 https://fairsharing.org/FAIRsharing.WWI10U) ification template as shown in Figure 3. We discuss each of the steps below in detail:

````{dropdown} **FAIRification template**
:open:

```{figure} ./FAIRificationTemplate.png
---
width: 800px
name: fairification-template
alt: FAIR (URL_TO_INSERT_RECORD_9844 https://fairsharing.org/FAIRsharing.WWI10U) ification template
---
FAIR (URL_TO_INSERT_RECORD_9845 https://fairsharing.org/FAIRsharing.WWI10U) ification template
```
````

>
>- **Step 1: Get the data**: This step involves getting access to the underlying dataset via a restricted or open access
>    API and capturing informat (URL_TO_INSERT_TERM_9846 https://fairsharing.org/search?recordType=model_and_format) ion on how to query the data via the API.
>
>- **Step 2: Model (URL_TO_INSERT_TERM_9847 https://fairsharing.org/search?recordType=model_and_format)  the domain**: Here, the data types involved in the dataset are identified. 
>    Also, the community or domain standard (URL_TO_INSERT_TERM_9848 https://fairsharing.org/search?fairsharingRegistry=Standard) s for representation of the data are also captured to align the FAIR (URL_TO_INSERT_RECORD_9849 https://fairsharing.org/FAIRsharing.WWI10U) ification work, if any, along those lines.
>
>- **Step 3: Select the identifier (URL_TO_INSERT_TERM_9850 https://fairsharing.org/search?recordType=identifier_schema)  scheme**: Here, the establishment of an identifier (URL_TO_INSERT_TERM_9851 https://fairsharing.org/search?recordType=identifier_schema)  for identification of the dataset is done.
>    This could be achieved by generation of new identifier (URL_TO_INSERT_TERM_9852 https://fairsharing.org/search?recordType=identifier_schema) s or reusing of existing (URL_TO_INSERT_RECORD_9853 https://fairsharing.org/FAIRsharing.q7bkqr)  ones.
>
>- **Step 4: Apply data standard (URL_TO_INSERT_TERM_9854 https://fairsharing.org/search?fairsharingRegistry=Standard) s**: At this step, data standard (URL_TO_INSERT_TERM_9855 https://fairsharing.org/search?fairsharingRegistry=Standard)  validation and identification is done to ensure that the
>    representation of the data is in community or domain specified format (URL_TO_INSERT_TERM_9856 https://fairsharing.org/search?recordType=model_and_format) s for interoperability purposes.
>
>- **Step 5: Choose data vocabularies**: At this step, you would look in depth about the data content and harmonize it
>    with ontologies (URL_TO_INSERT_TERM_9858 https://fairsharing.org/search?recordType=terminology_artefact)  either pre-existing (URL_TO_INSERT_RECORD_9859 https://fairsharing.org/FAIRsharing.q7bkqr)  or formulate an application ontology (URL_TO_INSERT_TERM_9857 https://fairsharing.org/search?recordType=terminology_artefact)  for your use case.
>
>- **Step 6: Transform data for interoperability**: Not only would you represent the data in one ontology (URL_TO_INSERT_TERM_9860 https://fairsharing.org/search?recordType=terminology_artefact)  but also link
>    or map (URL_TO_INSERT_RECORD_9863 https://fairsharing.org/FAIRsharing.53edcc)  to corresponding ontologies (URL_TO_INSERT_TERM_9862 https://fairsharing.org/search?recordType=terminology_artefact)  such that the data is interoperable with multiple vocabularies and terminologies (URL_TO_INSERT_TERM_9861 https://fairsharing.org/search?recordType=terminology_artefact)  rather than just one.
>
>- **Step 7: Host your data**: Once the dataset is ready, hosting (URL_TO_INSERT_RECORD_9864 https://fairsharing.org/FAIRsharing.q7bkqr)  and search (URL_TO_INSERT_RECORD_9865 https://fairsharing.org/FAIRsharing.52b22c)  engine optimization inputs for the dataset
>    need to be in place. Alongside hosting (URL_TO_INSERT_RECORD_9867 https://fairsharing.org/FAIRsharing.q7bkqr) , data versioning and data format (URL_TO_INSERT_TERM_9866 https://fairsharing.org/search?recordType=model_and_format) s need to also be considered.
>
>- **Step 8: Share your data**: Now that the dataset is FAIR (URL_TO_INSERT_RECORD_9868 https://fairsharing.org/FAIRsharing.WWI10U) ified, one can share this data to the community with licensing.
>    In case of dealing with sensitive data, data anonymization considerations should be placed prior to sharing.


<!-- [FAIR (URL_TO_INSERT_RECORD_9869 https://fairsharing.org/FAIRsharing.WWI10U) ification Template](./FAIR (URL_TO_INSERT_RECORD_9870 https://fairsharing.org/FAIRsharing.WWI10U) ificationTemplate.png) -->


### The FAIRification Workplan

The FAIR (URL_TO_INSERT_RECORD_9872 https://fairsharing.org/FAIRsharing.WWI10U) ification Workplan is a specific design and implementation plan generated for a specific project (URL_TO_INSERT_TERM_9871 https://fairsharing.org/search?recordType=project)  based on the 
goals set in phase 1 and requirements identified in phase 2 of the Process. 
Relevant elements from the FAIR (URL_TO_INSERT_RECORD_9873 https://fairsharing.org/FAIRsharing.WWI10U) ification Template are selected and broken down into concrete tasks. 
These tasks are then completed within the agreed cycle time frame as per the FAIR (URL_TO_INSERT_RECORD_9874 https://fairsharing.org/FAIRsharing.WWI10U) ification Process.

The diagram below shows the bespoke FAIR (URL_TO_INSERT_RECORD_9877 https://fairsharing.org/FAIRsharing.WWI10U) ification Workplan for the CARE (URL_TO_INSERT_RECORD_9876 https://fairsharing.org/FAIRsharing.zgqy0v)  project (URL_TO_INSERT_TERM_9875 https://fairsharing.org/search?recordType=project) . 
The  Workplan follows the general outline of the FAIR (URL_TO_INSERT_RECORD_9878 https://fairsharing.org/FAIRsharing.WWI10U) ification Process, with the goals listed in section 1 (red),
the outcomes of the project (URL_TO_INSERT_TERM_9879 https://fairsharing.org/search?recordType=project)  examination on section 2 (orange) and the pre-FAIR (URL_TO_INSERT_RECORD_9880 https://fairsharing.org/FAIRsharing.WWI10U) ification assessment outcomes in section 3.
It can also be beneficial to explicitly list the indicators targeted for improvement in this section in order to keep
this informat (URL_TO_INSERT_TERM_9881 https://fairsharing.org/search?recordType=model_and_format) ion easily accessible in one place.

The key parts of the workplan are section 4 (Design Decisions) and 5 (Implementation).
Section 4 lists the specific steps from the FAIR (URL_TO_INSERT_RECORD_9882 https://fairsharing.org/FAIRsharing.WWI10U) ification Template that will be addressed in this FAIR (URL_TO_INSERT_RECORD_9883 https://fairsharing.org/FAIRsharing.WWI10U) ification cycle
(dark purple) and refines them into more concrete steps relevant for this context (light purple).

In section 5, these concrete steps are broken down into clear implementable tasks, which are recorded in colour coded boxes to track progress. 
If a Cookbook (URL_TO_INSERT_RECORD_9884 https://fairsharing.org/FAIRsharing.cbz72b)  recipe already exists to address a task, this can be linked here. 

Following a FAIR (URL_TO_INSERT_RECORD_9885 https://fairsharing.org/FAIRsharing.WWI10U) ification cycle, the results of the post-FAIR (URL_TO_INSERT_RECORD_9886 https://fairsharing.org/FAIRsharing.WWI10U) ification assessment are recorded in section 6. 

If more than one FAIR (URL_TO_INSERT_RECORD_9887 https://fairsharing.org/FAIRsharing.WWI10U) ification cycle is performed, a new version of the Workplan should be produced for each cycle,
in particular if there are changes in sections 4 and 5.


<!-- [FAIR (URL_TO_INSERT_RECORD_9890 https://fairsharing.org/FAIRsharing.WWI10U) ification Workplan CARE (URL_TO_INSERT_RECORD_9889 https://fairsharing.org/FAIRsharing.zgqy0v)  project (URL_TO_INSERT_TERM_9888 https://fairsharing.org/search?recordType=project) ](./FAIR (URL_TO_INSERT_RECORD_9891 https://fairsharing.org/FAIRsharing.WWI10U) ificationWorkplanCare.png) -->


````{dropdown} **FAIRification Workplan CARE project**
:open:

```{figure} ./FAIRificationWorkplanCare.png
---
width: 800px
name: fairification-workplancare
alt: FAIR (URL_TO_INSERT_RECORD_9894 https://fairsharing.org/FAIRsharing.WWI10U) ification Workplan CARE (URL_TO_INSERT_RECORD_9893 https://fairsharing.org/FAIRsharing.zgqy0v)  project (URL_TO_INSERT_TERM_9892 https://fairsharing.org/search?recordType=project) 
---
FAIR (URL_TO_INSERT_RECORD_9897 https://fairsharing.org/FAIRsharing.WWI10U) ification Workplan CARE (URL_TO_INSERT_RECORD_9896 https://fairsharing.org/FAIRsharing.zgqy0v)  project (URL_TO_INSERT_TERM_9895 https://fairsharing.org/search?recordType=project) 
```
````


## Practical considerations

While this recipe does not deal in detail with how to implement the FAIR (URL_TO_INSERT_RECORD_9898 https://fairsharing.org/FAIRsharing.WWI10U) ification framework, as this is covered elsewhere,
it is worth highlighting a few important practical considerations:

* **The importance of good goal setting**. Throughout the development of the framework, we tested iterative versions of the framework on a range of use cases brought to us by other IMI project (URL_TO_INSERT_TERM_9899 https://fairsharing.org/search?recordType=project) s. One of the standout lessons from these collaborations was that good FAIR (URL_TO_INSERT_RECORD_9900 https://fairsharing.org/FAIRsharing.WWI10U) ification goals lead to good FAIR (URL_TO_INSERT_RECORD_9901 https://fairsharing.org/FAIRsharing.WWI10U) ification goals. The characteristics of a good FAIR (URL_TO_INSERT_RECORD_9902 https://fairsharing.org/FAIRsharing.WWI10U) ification goals are:
	* Actionability: goals need to be translatable into concrete tasks. A goal that is too vague can be difficult to implement as it is unclear what steps are involved in its completion. 
	* Defined scope: a good goal has a clearly defined scope or endpoint. Without this, work on an open-ended goal is likely going to carry on indefinitely with diminishing benefits.
	* Scientific value: FAIR (URL_TO_INSERT_RECORD_9904 https://fairsharing.org/FAIRsharing.WWI10U) ification work comes at a cost so a good FAIR (URL_TO_INSERT_RECORD_9905 https://fairsharing.org/FAIRsharing.WWI10U) ification goal needs to explicitly state why the work will increase the data's scientific value. Investing (URL_TO_INSERT_RECORD_9903 https://fairsharing.org/FAIRsharing.q7bkqr)  a great deal of effort to FAIR (URL_TO_INSERT_RECORD_9906 https://fairsharing.org/FAIRsharing.WWI10U) ify a single-use internal dataset that is not intended to ever be shared or reused would not constitute a prudent investment of resources. 
 
* **Multi-disciplinary task teams**. FAIR (URL_TO_INSERT_RECORD_9911 https://fairsharing.org/FAIRsharing.WWI10U)  considerations range across a range of skill levels, from highly technical work such as the practicals of data access control or ontology (URL_TO_INSERT_TERM_9910 https://fairsharing.org/search?recordType=terminology_artefact)  maintenance to data management aspects such as the creation of data dictionaries to project (URL_TO_INSERT_TERM_9907 https://fairsharing.org/search?recordType=project) -level governance issues like data licensing and reuse conditions. A successful FAIR (URL_TO_INSERT_RECORD_9912 https://fairsharing.org/FAIRsharing.WWI10U) ification process will therefore involve the assembly of a multi-discplinary task team of data managers, software developers, research (URL_TO_INSERT_RECORD_9915 https://fairsharing.org/FAIRsharing.52b22c)  scientists and project (URL_TO_INSERT_TERM_9908 https://fairsharing.org/search?recordType=project)  managers, to name just a few. The exact composition of a task team depends on the nature of the FAIR (URL_TO_INSERT_RECORD_9913 https://fairsharing.org/FAIRsharing.WWI10U) ification tasks and may change over the course of the FAIR (URL_TO_INSERT_RECORD_9914 https://fairsharing.org/FAIRsharing.WWI10U) ification process, with different skills required in the goal setting and project (URL_TO_INSERT_TERM_9909 https://fairsharing.org/search?recordType=project)  examiniation phases than during task implementations.

* **Flexibility of the framework with regards to specific FAIR (URL_TO_INSERT_RECORD_9916 https://fairsharing.org/FAIRsharing.WWI10U)  approaches or implementations**. The FAIR (URL_TO_INSERT_RECORD_9917 https://fairsharing.org/FAIRsharing.WWI10U) ification Framework described here is agnostic of any specific FAIR (URL_TO_INSERT_RECORD_9918 https://fairsharing.org/FAIRsharing.WWI10U)  implementation such as different FAIR (URL_TO_INSERT_RECORD_9919 https://fairsharing.org/FAIRsharing.WWI10U)  assessment methodologies. During the development of the framework, we trialed a range of methodologies including [RDA](https://www.rd-alliance.org (URL_TO_INSERT_RECORD_9923 https://fairsharing.org/3529) /group/fair-data-maturity-model-wg/post/fair-data-maturity-model-indicators), [FAIRsFAIR](https://fairsfair.eu/fairsfair-data-object-assessment-metrics-request-comments) and [FAIR (URL_TO_INSERT_RECORD_9920 https://fairsharing.org/FAIRsharing.WWI10U)  Dataset Maturity (DSM)](https://fairplus.github.io/Data-Maturity/) indicators to assess FAIR (URL_TO_INSERT_RECORD_9921 https://fairsharing.org/FAIRsharing.WWI10U) ification as well as a range of tools to support the definition of FAIR (URL_TO_INSERT_RECORD_9922 https://fairsharing.org/FAIRsharing.WWI10U) ification goals and their translation into a workplan.

---

## Conclusion
The key take-homes of this recipe are:

1. **Tailor the generic FAIR (URL_TO_INSERT_RECORD_9926 https://fairsharing.org/FAIRsharing.WWI10U) ification process to individual needs**. There is no single right way to "do FAIR (URL_TO_INSERT_RECORD_9927 https://fairsharing.org/FAIRsharing.WWI10U) " and every project (URL_TO_INSERT_TERM_9924 https://fairsharing.org/search?recordType=project)  will have a distinct set of needs and requirements. Customising the relevant template elements allows the building of a coherent workplan that optimally supports a project (URL_TO_INSERT_TERM_9925 https://fairsharing.org/search?recordType=project) 's needs. 
1. **Carefully define FAIR (URL_TO_INSERT_RECORD_9929 https://fairsharing.org/FAIRsharing.WWI10U) ification goals, focusing on incrementally achievable targets**. Focus on achieving elements of FAIR (URL_TO_INSERT_RECORD_9930 https://fairsharing.org/FAIRsharing.WWI10U) ness that matter most to the needs of the project (URL_TO_INSERT_TERM_9928 https://fairsharing.org/search?recordType=project)  to reach a balanced **“FAIR (URL_TO_INSERT_RECORD_9931 https://fairsharing.org/FAIRsharing.WWI10U)  enough”** status.
1. **Assemble a multi-disciplinary team**. A successful FAIR (URL_TO_INSERT_RECORD_9932 https://fairsharing.org/FAIRsharing.WWI10U) ification process starts with bringing together diverse teams that include the data owners as well professionals who can tackle the legal, curatorial and technical infrastructure aspects. 

### What to read next?
* [Prioritization of project (URL_TO_INSERT_TERM_9933 https://fairsharing.org/search?recordType=project) s for FAIR (URL_TO_INSERT_RECORD_9934 https://fairsharing.org/FAIRsharing.WWI10U) ification](../introduction/priorization.md)
* [Depositing in Zenodo (URL_TO_INSERT_RECORD_9936 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_9938 https://fairsharing.org/FAIRsharing.wy4egf)  generic repository (URL_TO_INSERT_TERM_9935 https://fairsharing.org/search?recordType=repository) ](../findability/zenodo (URL_TO_INSERT_RECORD_9937 https://fairsharing.org/FAIRsharing.wy4egf) -deposition.md)
* [Introduction to terminologies (URL_TO_INSERT_TERM_9939 https://fairsharing.org/search?recordType=terminology_artefact)  and ontologies (URL_TO_INSERT_TERM_9941 https://fairsharing.org/search?recordType=terminology_artefact) ](../interoperability/introduction-terminologies (URL_TO_INSERT_TERM_9940 https://fairsharing.org/search?recordType=terminology_artefact) -ontologies (URL_TO_INSERT_TERM_9942 https://fairsharing.org/search?recordType=terminology_artefact) .md)
* [Creating data/variable dictionary](../interoperability/creating-data-dictionary.md)
* [Interlinking data from different sources](../interoperability/identifier (URL_TO_INSERT_TERM_9943 https://fairsharing.org/search?recordType=identifier_schema) -map (URL_TO_INSERT_RECORD_9944 https://fairsharing.org/FAIRsharing.53edcc) ping.md)
* [Maturity model (URL_TO_INSERT_TERM_9945 https://fairsharing.org/search?recordType=model_and_format) s](../maturity.md)

````{rdmkit_panel}
````

## References:

````{dropdown} **References**

````



## Authors


````{authors_fairplus}
Danielle: Writing - Original Draft
Yojana: Writing - Original Draft
````


## License
````{license_fairplus}
CC-BY-4.0
````

