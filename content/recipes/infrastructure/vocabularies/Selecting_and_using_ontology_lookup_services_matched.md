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

This recipe provides **guidance on the selection and exploitation of ontology (URL_TO_INSERT_TERM_3662 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3663 https://fairsharing.org/FAIRsharing.Mkl9RR) s** . 

>* **[Objective of the recipe: introduction to ontology (URL_TO_INSERT_TERM_3664 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3665 https://fairsharing.org/FAIRsharing.Mkl9RR) s](#heading=h.bb3h294tvdau)**
>
>* **[Selecting an ontology (URL_TO_INSERT_TERM_3666 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3667 https://fairsharing.org/FAIRsharing.Mkl9RR) ](#bookmark=id.okwm6u2vsbft)**
>
>* **[Overview of widespread ontology (URL_TO_INSERT_TERM_3668 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3669 https://fairsharing.org/FAIRsharing.Mkl9RR) s](#bookmark=id.x42hawpkzgd3)**

An ***ontology (URL_TO_INSERT_TERM_3670 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3671 https://fairsharing.org/FAIRsharing.Mkl9RR) *** 
refers to *any type of application, standalone or Web-based, that enables the use of existing ontologies (URL_TO_INSERT_TERM_3672 https://fairsharing.org/search?recordType=terminology_artefact)  to support knowledge 
formalization and sharing, by fostering ontology (URL_TO_INSERT_TERM_3673 https://fairsharing.org/search?recordType=terminology_artefact) -based descriptions of knowledge*. 




Tools useful to build, edit or maintain ontologies (URL_TO_INSERT_TERM_3675 https://fairsharing.org/search?recordType=terminology_artefact)  are not considered ontology (URL_TO_INSERT_TERM_3674 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3676 https://fairsharing.org/FAIRsharing.Mkl9RR) s and thus are out of the scope of this recipe. 

In essence, an ontology (URL_TO_INSERT_TERM_3677 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3678 https://fairsharing.org/FAIRsharing.Mkl9RR)  is a platform that provides users with the possibility to **search (URL_TO_INSERT_RECORD_3679 https://fairsharing.org/FAIRsharing.52b22c)  in a set of
ontologies (URL_TO_INSERT_TERM_3680 https://fairsharing.org/search?recordType=terminology_artefact) , the most suitable concepts to describe the semantics of a piece of knowledge of interest,
usually available in the form of one or more keywords or a text excerpt**. 

Most ontology (URL_TO_INSERT_TERM_3681 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3682 https://fairsharing.org/FAIRsharing.Mkl9RR) s are available as Web applications: most of them also support programmatic access to their 
capabilities by means of (REST) APIs. Ontology (URL_TO_INSERT_TERM_3683 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3684 https://fairsharing.org/FAIRsharing.Mkl9RR) s can vary in the features that are provided, but often include:



* **Complex search (URL_TO_INSERT_RECORD_3687 https://fairsharing.org/FAIRsharing.52b22c) ing for concepts of interest**: most services implement advanced search (URL_TO_INSERT_RECORD_3688 https://fairsharing.org/FAIRsharing.52b22c)  features (i.e. scoping the search (URL_TO_INSERT_RECORD_3689 https://fairsharing.org/FAIRsharing.52b22c)  to specific ontologies (URL_TO_INSERT_TERM_3686 https://fairsharing.org/search?recordType=terminology_artefact)  or to specific parts of an ontology (URL_TO_INSERT_TERM_3685 https://fairsharing.org/search?recordType=terminology_artefact) ) or allow users to specify fine-grained patterns to aggregate or restrict the scope of search (URL_TO_INSERT_RECORD_3690 https://fairsharing.org/FAIRsharing.52b22c)  results.
* **Advanced browsing capabilities**, to explore the contents of a specific ontology (URL_TO_INSERT_TERM_3691 https://fairsharing.org/search?recordType=terminology_artefact)  by means of custom data navigation widgets such as tree-based views.
* **Managing distinct versions** of an ontology (URL_TO_INSERT_TERM_3692 https://fairsharing.org/search?recordType=terminology_artefact)  and alert its users when specific concepts become obsolete. 
* **Importing** user-provided ontologies (URL_TO_INSERT_TERM_3694 https://fairsharing.org/search?recordType=terminology_artefact) , giving consumers the ability to leverage a service for other terminologies (URL_TO_INSERT_TERM_3693 https://fairsharing.org/search?recordType=terminology_artefact)  beyond those included.
* Programmatic means to **access and deploy instances of the ontology (URL_TO_INSERT_TERM_3695 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3696 https://fairsharing.org/FAIRsharing.Mkl9RR)  in the premises of its users** represents another differentiating feature, using relevant documentation.
* **Recommending ontologies (URL_TO_INSERT_TERM_3697 https://fairsharing.org/search?recordType=terminology_artefact) ** based on the input of a given term, with ontologies (URL_TO_INSERT_TERM_3698 https://fairsharing.org/search?recordType=terminology_artefact)  ranked according to custom-weighted criteria.
* Access to an **active user community** that supports and exploits a specific ontology (URL_TO_INSERT_TERM_3699 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3700 https://fairsharing.org/FAIRsharing.Mkl9RR) , serving as an indication of widespread adoption and selection.

This recipe presents guideline (URL_TO_INSERT_TERM_3702 https://fairsharing.org/search?recordType=reporting_guideline) s and relevant considerations when choosing an ontology (URL_TO_INSERT_TERM_3701 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3703 https://fairsharing.org/FAIRsharing.Mkl9RR) , followed by
overview of existing public ontology (URL_TO_INSERT_TERM_3704 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3705 https://fairsharing.org/FAIRsharing.Mkl9RR) s and a comparison of their core (URL_TO_INSERT_RECORD_3706 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_3707 https://fairsharing.org/FAIRsharing.xMmOCL)  features.


## Selecting An Ontology Lookup Service

This section provides guideline (URL_TO_INSERT_TERM_3709 https://fairsharing.org/search?recordType=reporting_guideline) s and suggestions on how to select and leverage an ontology (URL_TO_INSERT_TERM_3708 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3710 https://fairsharing.org/FAIRsharing.Mkl9RR) , on the basis
of the knowledge needs and ontology (URL_TO_INSERT_TERM_3712 https://fairsharing.org/search?recordType=terminology_artefact)  use patterns that characterize a specific knowledge-intensive project (URL_TO_INSERT_TERM_3711 https://fairsharing.org/search?recordType=project) . 

Several aspects to consider when choosing an ontology (URL_TO_INSERT_TERM_3713 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3714 https://fairsharing.org/FAIRsharing.Mkl9RR)  are derived based on a series of commonly asked questions;



* **Is the set of ontologies (URL_TO_INSERT_TERM_3717 https://fairsharing.org/search?recordType=terminology_artefact)  incorporated in the ontology (URL_TO_INSERT_TERM_3716 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3718 https://fairsharing.org/FAIRsharing.Mkl9RR)  suitable to formally describe the knowledge domain my project (URL_TO_INSERT_TERM_3715 https://fairsharing.org/search?recordType=project)  is interested in?**

    Ontology (URL_TO_INSERT_TERM_3719 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3721 https://fairsharing.org/FAIRsharing.Mkl9RR) s usually provide access and enable users to search (URL_TO_INSERT_RECORD_3722 https://fairsharing.org/FAIRsharing.52b22c)  and reference classes and properties of _a specific set of ontologies (URL_TO_INSERT_TERM_3720 https://fairsharing.org/search?recordType=terminology_artefact)  related to a specific knowledge domain_ (i.e. biomedical knowledge).
    When choosing an ontology (URL_TO_INSERT_TERM_3724 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3726 https://fairsharing.org/FAIRsharing.Mkl9RR)  it is important to verify whether the ontologies (URL_TO_INSERT_TERM_3725 https://fairsharing.org/search?recordType=terminology_artefact)  covered by a specific service are suitable to describe the content of our knowledge-intensive project (URL_TO_INSERT_TERM_3723 https://fairsharing.org/search?recordType=project) . 
    Besides, a list of the ontologies (URL_TO_INSERT_TERM_3727 https://fairsharing.org/search?recordType=terminology_artefact)  covered, and interactive widgets to explore such ontologies (URL_TO_INSERT_TERM_3728 https://fairsharing.org/search?recordType=terminology_artefact)  (e.g. tree-based views), 
    some ontology (URL_TO_INSERT_TERM_3729 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3731 https://fairsharing.org/FAIRsharing.Mkl9RR) s also provide _ontology (URL_TO_INSERT_TERM_3730 https://fairsharing.org/search?recordType=terminology_artefact)  recommendation capabilities:_ given some “sample” 
    (i.e. text excerpt or list of keywords) of the knowledge we need to describe by means of available ontologies (URL_TO_INSERT_TERM_3732 https://fairsharing.org/search?recordType=terminology_artefact) , 
    the ontology (URL_TO_INSERT_TERM_3733 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3735 https://fairsharing.org/FAIRsharing.Mkl9RR)  ‘recommender’ suggests which are the best ontologies (URL_TO_INSERT_TERM_3734 https://fairsharing.org/search?recordType=terminology_artefact)  to use to this propose.

* **Do I need to consider / rely on private ontologies (URL_TO_INSERT_TERM_3737 https://fairsharing.org/search?recordType=terminology_artefact)  in my project (URL_TO_INSERT_TERM_3736 https://fairsharing.org/search?recordType=project) ? Do I need to use ontologies (URL_TO_INSERT_TERM_3738 https://fairsharing.org/search?recordType=terminology_artefact)  that are not already 
    imported and thus available in the ontology (URL_TO_INSERT_TERM_3739 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3740 https://fairsharing.org/FAIRsharing.Mkl9RR)  of my choice?**

    Some ontology (URL_TO_INSERT_TERM_3741 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3743 https://fairsharing.org/FAIRsharing.Mkl9RR) s enable users to import external (i.e. user-provided) ontologies (URL_TO_INSERT_TERM_3742 https://fairsharing.org/search?recordType=terminology_artefact)  in order to incorporate
    the content of these ontologies (URL_TO_INSERT_TERM_3744 https://fairsharing.org/search?recordType=terminology_artefact)  in their search (URL_TO_INSERT_RECORD_3745 https://fairsharing.org/FAIRsharing.52b22c)  and recommendation capabilities. 
    This feature could represent a key factor to consider when choosing an ontology (URL_TO_INSERT_TERM_3746 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3747 https://fairsharing.org/FAIRsharing.Mkl9RR)  since several 
    knowledge-intensive project (URL_TO_INSERT_TERM_3748 https://fairsharing.org/search?recordType=project) s rely on private ontologies (URL_TO_INSERT_TERM_3749 https://fairsharing.org/search?recordType=terminology_artefact)  or need to consider a set of additional ontologies (URL_TO_INSERT_TERM_3750 https://fairsharing.org/search?recordType=terminology_artefact)  not 
    natively covered by a specific ontology (URL_TO_INSERT_TERM_3751 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3752 https://fairsharing.org/FAIRsharing.Mkl9RR) .

* **Because of data privacy or data protection issues, do I need to use an instance of the ontology (URL_TO_INSERT_TERM_3753 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3754 https://fairsharing.org/FAIRsharing.Mkl9RR)  that
is deployed locally on my private computing infrastructure?**

    Several ontology (URL_TO_INSERT_TERM_3755 https://fairsharing.org/search?recordType=terminology_artefact) -lookup services provide the possibility to deploy the service on the private computing 
    infrastructure of its users. This feature would be particularly relevant when private ontologies (URL_TO_INSERT_TERM_3756 https://fairsharing.org/search?recordType=terminology_artefact)  are adopted in a 
    knowledge-intensive project (URL_TO_INSERT_TERM_3757 https://fairsharing.org/search?recordType=project) .

* **Which are the usage patterns I will rely on in order to exploit the ontology (URL_TO_INSERT_TERM_3758 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3759 https://fairsharing.org/FAIRsharing.Mkl9RR) ? Will the 1)
massive and systematic exploitation of the ontology (URL_TO_INSERT_TERM_3760 https://fairsharing.org/search?recordType=terminology_artefact)  search (URL_TO_INSERT_RECORD_3762 https://fairsharing.org/FAIRsharing.52b22c) , 2) the recommendation features of the ontology (URL_TO_INSERT_TERM_3761 https://fairsharing.org/search?recordType=terminology_artefact)  lookup
service or 3) the integration of its capabilities in more complex systems, require the possibility to programmatically 
access the service by means of an application programming interface (API)?**

    Ontology (URL_TO_INSERT_TERM_3763 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3764 https://fairsharing.org/FAIRsharing.Mkl9RR) s usually provide a (Web-based) user interface as the preferred way to interact with them to
    browse and search (URL_TO_INSERT_RECORD_3766 https://fairsharing.org/FAIRsharing.52b22c)  for ontologies (URL_TO_INSERT_TERM_3765 https://fairsharing.org/search?recordType=terminology_artefact) , or recommend relevant concepts to describe contents of interest. 
    In several scenarios, the possibility to programmatically interact with ontology (URL_TO_INSERT_TERM_3767 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3768 https://fairsharing.org/FAIRsharing.Mkl9RR) s would be extremely
    valuable; to this purpose, several ontology (URL_TO_INSERT_TERM_3769 https://fairsharing.org/search?recordType=terminology_artefact) -lookup services implement an API (mostly based on REST interactions)
    that enable the user to programmatically invoke the majority of ontology (URL_TO_INSERT_TERM_3770 https://fairsharing.org/search?recordType=terminology_artefact)  search (URL_TO_INSERT_RECORD_3771 https://fairsharing.org/FAIRsharing.52b22c)  features of the same service. 
    In order to simplify the integration of the ontology (URL_TO_INSERT_TERM_3772 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3773 https://fairsharing.org/FAIRsharing.Mkl9RR)  support into external applications,  
   several-ontology (URL_TO_INSERT_TERM_3774 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3775 https://fairsharing.org/FAIRsharing.Mkl9RR) s provide users with language-specific clients to interact with them through their API. 

* **Is the distribution license of the ontology (URL_TO_INSERT_TERM_3776 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3777 https://fairsharing.org/FAIRsharing.Mkl9RR)  compatible with the way I plan to exploit the 
features provided the same service in my project (URL_TO_INSERT_TERM_3778 https://fairsharing.org/search?recordType=project)  or with the way I plan to integrate the same service in my project (URL_TO_INSERT_TERM_3779 https://fairsharing.org/search?recordType=project) ?**

    The licencing terms of the ontology (URL_TO_INSERT_TERM_3780 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3781 https://fairsharing.org/FAIRsharing.Mkl9RR)  of choice intended for use in a given context and 
    knowledge-intensive project (URL_TO_INSERT_TERM_3782 https://fairsharing.org/search?recordType=project) , is a key consideration when selecting an ontology (URL_TO_INSERT_TERM_3783 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3784 https://fairsharing.org/FAIRsharing.Mkl9RR) : available 
    ontology (URL_TO_INSERT_TERM_3785 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3786 https://fairsharing.org/FAIRsharing.Mkl9RR) s range from open-source applications to commercial tools, and it is best to choose one with funding in mind.

* **Does the ontology (URL_TO_INSERT_TERM_3787 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3790 https://fairsharing.org/FAIRsharing.Mkl9RR)  manage ontology (URL_TO_INSERT_TERM_3788 https://fairsharing.org/search?recordType=terminology_artefact)  versioning and updates so that I can easily reflect any ontology (URL_TO_INSERT_TERM_3789 https://fairsharing.org/search?recordType=terminology_artefact)  
update into my knowledge-intensive project (URL_TO_INSERT_TERM_3791 https://fairsharing.org/search?recordType=project) ? **

    Ontologies (URL_TO_INSERT_TERM_3794 https://fairsharing.org/search?recordType=terminology_artefact)  and terminologies (URL_TO_INSERT_TERM_3792 https://fairsharing.org/search?recordType=terminology_artefact)  usually evolve over time: when a new, updated version of an ontology (URL_TO_INSERT_TERM_3793 https://fairsharing.org/search?recordType=terminology_artefact)  used in a 
    knowledge-intensive project (URL_TO_INSERT_TERM_3795 https://fairsharing.org/search?recordType=project)  becomes available, best practice suggests that we should also update the part of our 
    project (URL_TO_INSERT_TERM_3796 https://fairsharing.org/search?recordType=project) s that rely on such ontology (URL_TO_INSERT_TERM_3797 https://fairsharing.org/search?recordType=terminology_artefact) . Some ontology (URL_TO_INSERT_TERM_3798 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3799 https://fairsharing.org/FAIRsharing.Mkl9RR) s implement specific procedures and tools to manage
    and propagate ontology (URL_TO_INSERT_TERM_3800 https://fairsharing.org/search?recordType=terminology_artefact)  updates; the availability of such tools would simplify the implementation of changes deriving
    from ontology (URL_TO_INSERT_TERM_3802 https://fairsharing.org/search?recordType=terminology_artefact)  updates in the project (URL_TO_INSERT_TERM_3801 https://fairsharing.org/search?recordType=project) s under consideration.

* **Is the ontology (URL_TO_INSERT_TERM_3803 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3804 https://fairsharing.org/FAIRsharing.Mkl9RR)  supported by an active community of developers
or by an active company? Which are the available channels I can rely on to receive support on the usage and integration 
of the ontology (URL_TO_INSERT_TERM_3805 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3806 https://fairsharing.org/FAIRsharing.Mkl9RR) ?**

    The support of an active community of developers and users is a key aspect to take into account when choosing an 
    ontology (URL_TO_INSERT_TERM_3807 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3809 https://fairsharing.org/FAIRsharing.Mkl9RR) . This could be quantified by evaluating several factors of an ontology (URL_TO_INSERT_TERM_3808 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3810 https://fairsharing.org/FAIRsharing.Mkl9RR)  including:
    (i) availability of mailing or support lists; (ii) for open-source project (URL_TO_INSERT_TERM_3812 https://fairsharing.org/search?recordType=project) s, using metric (URL_TO_INSERT_TERM_3811 https://fairsharing.org/search?recordType=metric) s such as the star-rating,
    the number of forks and followers and the frequency of commits of the project (URL_TO_INSERT_TERM_3813 https://fairsharing.org/search?recordType=project)  on the code-sharing platform used 
    (e.g. GitHub (URL_TO_INSERT_RECORD_3816 https://fairsharing.org/FAIRsharing.c55d5e) ); (iii) size of the community of users of the ontology (URL_TO_INSERT_TERM_3814 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3815 https://fairsharing.org/FAIRsharing.Mkl9RR)  (e.g. how many followers on social
    media accounts, how many clients advertised on the Website).

## Key Selection Criteria

The above questions have highlighted 20 factors which should be taken into account when choosing a service. 
These factors can be categorised into 3 groups; **ontology (URL_TO_INSERT_TERM_3818 https://fairsharing.org/search?recordType=terminology_artefact)  informat (URL_TO_INSERT_TERM_3817 https://fairsharing.org/search?recordType=model_and_format) ion, functionality** and **interfaces**, and include;

### **Ontology Information**



1. **URL (URL_TO_INSERT_RECORD_3821 https://fairsharing.org/FAIRsharing.9d38e2) **: the main URL (URL_TO_INSERT_RECORD_3822 https://fairsharing.org/FAIRsharing.9d38e2)  where the ontology (URL_TO_INSERT_TERM_3819 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3820 https://fairsharing.org/FAIRsharing.Mkl9RR)  can be accessed
2. **Latest version of service / data / code (where applicable**): the most recent version of both the content (i.e. ontologies (URL_TO_INSERT_TERM_3824 https://fairsharing.org/search?recordType=terminology_artefact) ) and the code of the ontology (URL_TO_INSERT_TERM_3823 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3825 https://fairsharing.org/FAIRsharing.Mkl9RR) 
3. **Host Organisation**: the organisation responsible for the maintenance of the ontology (URL_TO_INSERT_TERM_3826 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3827 https://fairsharing.org/FAIRsharing.Mkl9RR) 
4. **Public / private**: is the ontology (URL_TO_INSERT_TERM_3828 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3829 https://fairsharing.org/FAIRsharing.Mkl9RR)  a public or private infrastructure?
5. **Licence**: the licence that regulates the use and cost of the ontology (URL_TO_INSERT_TERM_3830 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3831 https://fairsharing.org/FAIRsharing.Mkl9RR) 
6. **Domain**: which is the knowledge domain covered by the ontologies (URL_TO_INSERT_TERM_3833 https://fairsharing.org/search?recordType=terminology_artefact)  referenced in the ontology (URL_TO_INSERT_TERM_3832 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3834 https://fairsharing.org/FAIRsharing.Mkl9RR) ?
7. **Quantification of community of users**: objective measures to quantify the community of users supporting and consuming an ontology (URL_TO_INSERT_TERM_3835 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3836 https://fairsharing.org/FAIRsharing.Mkl9RR) , including: number of stars and forks on GitHub (URL_TO_INSERT_RECORD_3837 https://fairsharing.org/FAIRsharing.c55d5e) , number of social media followers

### **Functionality**



8. **Number and complexity of ontologies (URL_TO_INSERT_TERM_3839 https://fairsharing.org/search?recordType=terminology_artefact)  covered**: how many ontologies (URL_TO_INSERT_TERM_3840 https://fairsharing.org/search?recordType=terminology_artefact)  does the ontology (URL_TO_INSERT_TERM_3838 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3841 https://fairsharing.org/FAIRsharing.Mkl9RR)  cover and how complex are they?
9. **Ontology (URL_TO_INSERT_TERM_3844 https://fairsharing.org/search?recordType=terminology_artefact)  format (URL_TO_INSERT_TERM_3842 https://fairsharing.org/search?recordType=model_and_format) s supported**: which ontology (URL_TO_INSERT_TERM_3845 https://fairsharing.org/search?recordType=terminology_artefact)  format (URL_TO_INSERT_TERM_3843 https://fairsharing.org/search?recordType=model_and_format) s are supported by the ontology (URL_TO_INSERT_TERM_3846 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3847 https://fairsharing.org/FAIRsharing.Mkl9RR) ?
10. **Ontology (URL_TO_INSERT_TERM_3848 https://fairsharing.org/search?recordType=terminology_artefact)  importing capabilities**: if and how ontologies (URL_TO_INSERT_TERM_3850 https://fairsharing.org/search?recordType=terminology_artefact)  can be imported and thus indexed by the ontology (URL_TO_INSERT_TERM_3849 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3851 https://fairsharing.org/FAIRsharing.Mkl9RR) ?
11. **Ontology (URL_TO_INSERT_TERM_3852 https://fairsharing.org/search?recordType=terminology_artefact)  browsing capabilities**: which interaction patterns are available to browse the set of ontologies (URL_TO_INSERT_TERM_3854 https://fairsharing.org/search?recordType=terminology_artefact)  contemplated by the ontology (URL_TO_INSERT_TERM_3853 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3855 https://fairsharing.org/FAIRsharing.Mkl9RR) ?
12. **Ontology (URL_TO_INSERT_TERM_3856 https://fairsharing.org/search?recordType=terminology_artefact)  search (URL_TO_INSERT_RECORD_3861 https://fairsharing.org/FAIRsharing.52b22c)  capabilities**: which search (URL_TO_INSERT_RECORD_3862 https://fairsharing.org/FAIRsharing.52b22c)  patterns are provided by the ontology (URL_TO_INSERT_TERM_3857 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3860 https://fairsharing.org/FAIRsharing.Mkl9RR)  to identify the best concept useful to represent the semantic of a term? When search (URL_TO_INSERT_RECORD_3863 https://fairsharing.org/FAIRsharing.52b22c) ing against a term, does the ontology (URL_TO_INSERT_TERM_3858 https://fairsharing.org/search?recordType=terminology_artefact)  give an indication of whether the term has been derived from a different ontology (URL_TO_INSERT_TERM_3859 https://fairsharing.org/search?recordType=terminology_artefact) ?
13. **Ontology (URL_TO_INSERT_TERM_3864 https://fairsharing.org/search?recordType=terminology_artefact)  recommendation capabilities**: does the ontology (URL_TO_INSERT_TERM_3865 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3867 https://fairsharing.org/FAIRsharing.Mkl9RR)  provide users with a recommendation concerning the most suitable ontologies (URL_TO_INSERT_TERM_3866 https://fairsharing.org/search?recordType=terminology_artefact)  to semantically characterize the contents of some text / a set of keywords? 
14. **Ontology (URL_TO_INSERT_TERM_3868 https://fairsharing.org/search?recordType=terminology_artefact)  update capabilities**: how are terms and/or relationships updated in a given ontology (URL_TO_INSERT_TERM_3869 https://fairsharing.org/search?recordType=terminology_artefact)  and how is this governed? Is this an automatic or manual update and what happens to terms that are considered obsolete?
15. **Ontology (URL_TO_INSERT_TERM_3870 https://fairsharing.org/search?recordType=terminology_artefact)  versioning capabilities**: are there predefined patterns to identify, manage and compare distinct versions of an ontology (URL_TO_INSERT_TERM_3871 https://fairsharing.org/search?recordType=terminology_artefact) ? 

### **Interfaces**



16. **Description of Web-based access to service**: which ontology (URL_TO_INSERT_TERM_3872 https://fairsharing.org/search?recordType=terminology_artefact)  browsing  and search (URL_TO_INSERT_RECORD_3877 https://fairsharing.org/FAIRsharing.52b22c)  patterns are available to the (Web-based) user interface of the ontology (URL_TO_INSERT_TERM_3873 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3875 https://fairsharing.org/FAIRsharing.Mkl9RR) ? Does the ontology (URL_TO_INSERT_TERM_3874 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3876 https://fairsharing.org/FAIRsharing.Mkl9RR)  also provide programmatic access to its data and services (e.g. by means of a REST API)?
17. **Description of API**: reference to the documentation of the (REST) API provided by the ontology (URL_TO_INSERT_TERM_3878 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3879 https://fairsharing.org/FAIRsharing.Mkl9RR) , if any
18. **Developer resources**: description of resources provided to developers in order to ease the programmatic access to the features of the ontology (URL_TO_INSERT_TERM_3880 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3881 https://fairsharing.org/FAIRsharing.Mkl9RR)  (i.e. libraries to query the REST API from a specific programming language).
19. **Local deploy of service**: possibility to locally deploy the ontology (URL_TO_INSERT_TERM_3882 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3883 https://fairsharing.org/FAIRsharing.Mkl9RR) 
20. **Source code reference**: if available, link to the source code of the ontology (URL_TO_INSERT_TERM_3884 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3885 https://fairsharing.org/FAIRsharing.Mkl9RR) 
4. **Overview of Widespread Ontology (URL_TO_INSERT_TERM_3886 https://fairsharing.org/search?recordType=terminology_artefact)  Lookup Service (URL_TO_INSERT_RECORD_3887 https://fairsharing.org/FAIRsharing.Mkl9RR) s**

---

Here, we have used the selection criteria above to provide an overview and comparison of four widespread ontology (URL_TO_INSERT_TERM_3888 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3889 https://fairsharing.org/FAIRsharing.Mkl9RR) s, namely:



-  [EBI Ontology (URL_TO_INSERT_TERM_3890 https://fairsharing.org/search?recordType=terminology_artefact)  Lookup Service (URL_TO_INSERT_RECORD_3891 https://fairsharing.org/FAIRsharing.Mkl9RR) ](https://www.ebi.ac.uk/ols/index (URL_TO_INSERT_RECORD_3892 https://fairsharing.org/FAIRsharing.Mkl9RR) )
-  [BioPortal (URL_TO_INSERT_RECORD_3893 https://fairsharing.org/FAIRsharing.4m97ah) ](https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_3894 https://fairsharing.org/FAIRsharing.4m97ah) )
-  [OHD (URL_TO_INSERT_RECORD_3895 https://fairsharing.org/FAIRsharing.bg7bb6) SI Athena](https://athena.ohdsi.org/search-terms/start)
-  [Ontobee (URL_TO_INSERT_RECORD_3897 https://fairsharing.org/FAIRsharing.q8fx1b)  and the OBO Foundry (URL_TO_INSERT_RECORD_3896 https://fairsharing.org/FAIRsharing.847069) ](http://www.ontobee.org (URL_TO_INSERT_RECORD_3898 https://fairsharing.org/FAIRsharing.q8fx1b) )

The results of the analysis can be found below, else in tabular format (URL_TO_INSERT_TERM_3899 https://fairsharing.org/search?recordType=model_and_format)  [here](https://docs.google.com/spreadsheets/d/1kn1oEhsYJPiLI5gA12B1UsbLBRoSLGbOYcOMDG4614o/edit#gid=0).

Note, the _‘last update of this table_’ field provides the date on which the ontology (URL_TO_INSERT_TERM_3900 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_3901 https://fairsharing.org/FAIRsharing.Mkl9RR)  was last assessed.

### **The EBI Ontology Lookup Service** {footcite}`pmid20460452`

<!-- **Overview by Francesco** -->


<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td>Ontology (URL_TO_INSERT_TERM_3902 https://fairsharing.org/search?recordType=terminology_artefact)  Lookup Service (URL_TO_INSERT_RECORD_3903 https://fairsharing.org/FAIRsharing.Mkl9RR) 
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
   <td><strong>URL (URL_TO_INSERT_RECORD_3904 https://fairsharing.org/FAIRsharing.9d38e2) </strong>
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/index (URL_TO_INSERT_RECORD_3905 https://fairsharing.org/FAIRsharing.Mkl9RR) ">https://www.ebi.ac.uk/ols/index (URL_TO_INSERT_RECORD_3906 https://fairsharing.org/FAIRsharing.Mkl9RR) </a>
   </td>
  </tr>
  <tr>
   <td><strong>Latest version of service / data / code (where applicable)</strong>
   </td>
   <td>Content: last update 12 Apr 2020 11:39
<p>
Code: Maven PO (URL_TO_INSERT_RECORD_3907 https://fairsharing.org/FAIRsharing.3ngg40) V version (from GitHub (URL_TO_INSERT_RECORD_3908 https://fairsharing.org/FAIRsharing.c55d5e) ): 3.2.1-SNAPSHOT
<p>
<a href="https://github.com (URL_TO_INSERT_RECORD_3909 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/OLS">https://github.com (URL_TO_INSERT_RECORD_3910 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/OLS</a>
<p>
Last commit on GitHub (URL_TO_INSERT_RECORD_3911 https://fairsharing.org/FAIRsharing.c55d5e) : April 2020
   </td>
  </tr>
  <tr>
   <td><strong>Host organisation</strong>
   </td>
   <td><a href="http://www.ebi.ac.uk/about/spot-team">Samples, Phenotypes and Ontologies (URL_TO_INSERT_TERM_3912 https://fairsharing.org/search?recordType=terminology_artefact)  Team</a> at EMBL-EBI
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
   <td>A repository (URL_TO_INSERT_TERM_3913 https://fairsharing.org/search?recordType=repository)  for biomedical ontologies (URL_TO_INSERT_TERM_3915 https://fairsharing.org/search?recordType=terminology_artefact)  that aims to provide a single point of access to the latest ontology (URL_TO_INSERT_TERM_3914 https://fairsharing.org/search?recordType=terminology_artefact)  versions
   </td>
  </tr>
  <tr>
   <td><strong>Set of ontologies (URL_TO_INSERT_TERM_3916 https://fairsharing.org/search?recordType=terminology_artefact)  covered</strong>
   </td>
   <td>245 ontologies (URL_TO_INSERT_TERM_3917 https://fairsharing.org/search?recordType=terminology_artefact)  / 6,119,228 terms / 27,778 properties / 485,541 individuals
<p>
Whole list at: <a href="https://www.ebi.ac.uk/ols/ontologies">https://www.ebi.ac.uk/ols/ontologies</a>
   </td>
  </tr>
  <tr>
   <td><strong>Onto. format (URL_TO_INSERT_TERM_3918 https://fairsharing.org/search?recordType=model_and_format) s supported</strong>
   </td>
   <td>OWL (URL_TO_INSERT_RECORD_3919 https://fairsharing.org/FAIRsharing.atygwy)  2 and OBO (URL_TO_INSERT_RECORD_3920 https://fairsharing.org/FAIRsharing.847069) 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. importing capabilities</strong>
   </td>
   <td>By means of a local installation it is possible to import ontologies (URL_TO_INSERT_TERM_3922 https://fairsharing.org/search?recordType=terminology_artefact)  in OWL (URL_TO_INSERT_RECORD_3923 https://fairsharing.org/FAIRsharing.atygwy)  2 and OBO (URL_TO_INSERT_RECORD_3924 https://fairsharing.org/FAIRsharing.847069)  format (URL_TO_INSERT_TERM_3921 https://fairsharing.org/search?recordType=model_and_format) 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. browsing capabilities</strong>
   </td>
   <td>Tree-view based browsing of hierarch (URL_TO_INSERT_RECORD_3928 https://fairsharing.org/FAIRsharing.52b22c) ies of classes and properties of ontologies (URL_TO_INSERT_TERM_3927 https://fairsharing.org/search?recordType=terminology_artefact) . The modifications added by different version of each ontology (URL_TO_INSERT_TERM_3925 https://fairsharing.org/search?recordType=terminology_artefact)  are shown by means of distinct background colors in ontology (URL_TO_INSERT_TERM_3926 https://fairsharing.org/search?recordType=terminology_artefact)  browsing tree-views
   </td>
  </tr>
  <tr>
   <td><strong>Onto. search (URL_TO_INSERT_RECORD_3929 https://fairsharing.org/FAIRsharing.52b22c)  capabilities</strong>
   </td>
   <td>Search (URL_TO_INSERT_RECORD_3932 https://fairsharing.org/FAIRsharing.52b22c)  by term to gather all the ontologies (URL_TO_INSERT_TERM_3930 https://fairsharing.org/search?recordType=terminology_artefact)  where the term is found. It is possible to restrict search (URL_TO_INSERT_RECORD_3933 https://fairsharing.org/FAIRsharing.52b22c)  results to one or more ontologies (URL_TO_INSERT_TERM_3931 https://fairsharing.org/search?recordType=terminology_artefact) , to a specific type of result (i.e. class, property or individual) or to exact or partial term match
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
   <td>OLS (URL_TO_INSERT_RECORD_3935 https://fairsharing.org/FAIRsharing.Mkl9RR)  updates nightly to always provide the latest ontology (URL_TO_INSERT_TERM_3934 https://fairsharing.org/search?recordType=terminology_artefact)  versions
   </td>
  </tr>
  <tr>
   <td><strong>Onto. versioning capabilities</strong>
   </td>
   <td>Obsoleted ontology (URL_TO_INSERT_TERM_3936 https://fairsharing.org/search?recordType=terminology_artefact)  terms are spotted by means of a boolean flag (is_obsolete)
   </td>
  </tr>
  <tr>
   <td><strong>Description of Web-based access to service</strong>
   </td>
   <td>Besides a Web-based user interface useful to browse ontologies (URL_TO_INSERT_TERM_3938 https://fairsharing.org/search?recordType=terminology_artefact)  and search (URL_TO_INSERT_RECORD_3939 https://fairsharing.org/FAIRsharing.52b22c)  for ontology (URL_TO_INSERT_TERM_3937 https://fairsharing.org/search?recordType=terminology_artefact)  concepts, free-access by means of a REST API is provided to the users
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
   <td><a href="https://github.com (URL_TO_INSERT_RECORD_3940 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/OLS">https://github.com (URL_TO_INSERT_RECORD_3941 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/OLS</a>
   </td>
  </tr>
  <tr>
   <td><strong>Quantification of community of users</strong>
   </td>
   <td>GitHub (URL_TO_INSERT_RECORD_3942 https://fairsharing.org/FAIRsharing.c55d5e) : 49 stars and 19 forks
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
   <td>Bioportal (URL_TO_INSERT_RECORD_3943 https://fairsharing.org/FAIRsharing.4m97ah)  
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
   <td><strong>URL (URL_TO_INSERT_RECORD_3944 https://fairsharing.org/FAIRsharing.9d38e2) </strong>
   </td>
   <td><a href="https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_3945 https://fairsharing.org/FAIRsharing.4m97ah) /">https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_3946 https://fairsharing.org/FAIRsharing.4m97ah) /</a>
   </td>
  </tr>
  <tr>
   <td><strong>Latest version of service / data / code (where applicable)</strong>
   </td>
   <td><em>Content</em>: last update 12 Apr 2020 11:39
<p>
<em>Code</em>: 
<ul>

<li>Web UI: <a href="https://github.com (URL_TO_INSERT_RECORD_3947 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/bioportal_web_ui">https://github.com (URL_TO_INSERT_RECORD_3948 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/bioportal_web_ui</a>

<li>REST API: <a href="https://github.com (URL_TO_INSERT_RECORD_3949 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_api">https://github.com (URL_TO_INSERT_RECORD_3950 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_api</a>

<li>Linked Data: <a href="https://github.com (URL_TO_INSERT_RECORD_3951 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_linked_data">https://github.com (URL_TO_INSERT_RECORD_3952 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_linked_data</a>

<p>
Latest commit on GitHub (URL_TO_INSERT_RECORD_3953 https://fairsharing.org/FAIRsharing.c55d5e) : April 2020
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td><strong>Host organisation</strong>
   </td>
   <td><a href="https://ncbo.bioontology.org/about-ncbo">U.S. National Center for Biomedical Ontology (URL_TO_INSERT_TERM_3954 https://fairsharing.org/search?recordType=terminology_artefact) </a>
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
   <td>Available at: <a href="https://github.com (URL_TO_INSERT_RECORD_3955 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_api/blob/master/LICENSE.txt">https://github.com (URL_TO_INSERT_RECORD_3956 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_api/blob/master/LICENSE.txt</a>
   </td>
  </tr>
  <tr>
   <td><strong>Domain</strong>
   </td>
   <td>A Web-based application for search (URL_TO_INSERT_RECORD_3961 https://fairsharing.org/FAIRsharing.52b22c) ing, sharing, visualizing, and analyzing a large repository (URL_TO_INSERT_TERM_3957 https://fairsharing.org/search?recordType=repository)  of biomedical ontologies (URL_TO_INSERT_TERM_3960 https://fairsharing.org/search?recordType=terminology_artefact) , terminologies (URL_TO_INSERT_TERM_3958 https://fairsharing.org/search?recordType=terminology_artefact) , and ontology (URL_TO_INSERT_TERM_3959 https://fairsharing.org/search?recordType=terminology_artefact) -based annotations
   </td>
  </tr>
  <tr>
   <td><strong>Set of ontologies (URL_TO_INSERT_TERM_3962 https://fairsharing.org/search?recordType=terminology_artefact)  covered</strong>
   </td>
   <td>Ontologies (URL_TO_INSERT_TERM_3963 https://fairsharing.org/search?recordType=terminology_artefact) : 842 / Classes: 11,324,508 
<p>
Whole list at: <a href="https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_3964 https://fairsharing.org/FAIRsharing.4m97ah) /ontologies">https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_3965 https://fairsharing.org/FAIRsharing.4m97ah) /ontologies</a>
   </td>
  </tr>
  <tr>
   <td><strong>Onto. format (URL_TO_INSERT_TERM_3966 https://fairsharing.org/search?recordType=model_and_format) s supported</strong>
   </td>
   <td>OWL (URL_TO_INSERT_RECORD_3967 https://fairsharing.org/FAIRsharing.atygwy) , OBO (URL_TO_INSERT_RECORD_3968 https://fairsharing.org/FAIRsharing.847069) , SKOS (URL_TO_INSERT_RECORD_3969 https://fairsharing.org/FAIRsharing.48e326) 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. importing capabilities</strong>
   </td>
   <td>It is possible to upload / submit new ontologies (URL_TO_INSERT_TERM_3972 https://fairsharing.org/search?recordType=terminology_artefact)  or new versions of existing ontologies (URL_TO_INSERT_TERM_3973 https://fairsharing.org/search?recordType=terminology_artefact)  that will be indexed in BioPortal (URL_TO_INSERT_RECORD_3974 https://fairsharing.org/FAIRsharing.4m97ah) . Ontology (URL_TO_INSERT_TERM_3971 https://fairsharing.org/search?recordType=terminology_artefact)  metadata will be provided in the <a href="http://omv.ontoware.org">Ontology Metadata Vocabulary</a> (OMV (URL_TO_INSERT_RECORD_3975 https://fairsharing.org/FAIRsharing.wqy605) ) format (URL_TO_INSERT_TERM_3970 https://fairsharing.org/search?recordType=model_and_format) 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. browsing capabilities</strong>
   </td>
   <td>For each ontology (URL_TO_INSERT_TERM_3978 https://fairsharing.org/search?recordType=terminology_artefact)  / terminology (URL_TO_INSERT_TERM_3976 https://fairsharing.org/search?recordType=terminology_artefact)  an overview of its content is provided together with separate tree-views tailored to explore its hierarch (URL_TO_INSERT_RECORD_3981 https://fairsharing.org/FAIRsharing.52b22c) ies of classes and properties. The set of available map (URL_TO_INSERT_RECORD_3980 https://fairsharing.org/FAIRsharing.53edcc) pings to other ontologies (URL_TO_INSERT_TERM_3979 https://fairsharing.org/search?recordType=terminology_artefact)  / terminologies (URL_TO_INSERT_TERM_3977 https://fairsharing.org/search?recordType=terminology_artefact)  can be explored by a custom view
   </td>
  </tr>
  <tr>
   <td><strong>Onto. search (URL_TO_INSERT_RECORD_3982 https://fairsharing.org/FAIRsharing.52b22c)  capabilities</strong>
   </td>
   <td>Search (URL_TO_INSERT_RECORD_3985 https://fairsharing.org/FAIRsharing.52b22c)  by term to gather all the ontologies (URL_TO_INSERT_TERM_3983 https://fairsharing.org/search?recordType=terminology_artefact)  where the term is found. It is possible to restrict search (URL_TO_INSERT_RECORD_3986 https://fairsharing.org/FAIRsharing.52b22c)  results to one or more ontologies (URL_TO_INSERT_TERM_3984 https://fairsharing.org/search?recordType=terminology_artefact) , to a specific type of result (i.e. class, property or individual) or to exact or partial term match
   </td>
  </tr>
  <tr>
   <td><strong>Onto. recommendation capabilities</strong>
   </td>
   <td>An ontology (URL_TO_INSERT_TERM_3987 https://fairsharing.org/search?recordType=terminology_artefact)  recommender is available: it retrieves recommendations for the most relevant ontologies (URL_TO_INSERT_TERM_3988 https://fairsharing.org/search?recordType=terminology_artefact)  based on an excerpt from a biomedical text or a list of keywords.
<p>
Recommendations are based on: (i) <em>coverage</em> of the input text / set of keywords; (ii) <em>acceptance</em> of the ontologies (URL_TO_INSERT_TERM_3991 https://fairsharing.org/search?recordType=terminology_artefact) ; (iii) <em>detail of knowledge</em> available in the ontology (URL_TO_INSERT_TERM_3989 https://fairsharing.org/search?recordType=terminology_artefact)  to describe input data and (iv) <em>specialization</em> of the ontology (URL_TO_INSERT_TERM_3990 https://fairsharing.org/search?recordType=terminology_artefact)  to the specific domain under consideration
   </td>
  </tr>
  <tr>
   <td><strong>Onto. update capabilities</strong>
   </td>
   <td>Each ontology (URL_TO_INSERT_TERM_3992 https://fairsharing.org/search?recordType=terminology_artefact)  can be manually updated by accessing the BioPortal (URL_TO_INSERT_RECORD_3994 https://fairsharing.org/FAIRsharing.4m97ah)  or automatically updated by BioPortal (URL_TO_INSERT_RECORD_3995 https://fairsharing.org/FAIRsharing.4m97ah)  by continuously monitoring a URL (URL_TO_INSERT_RECORD_3996 https://fairsharing.org/FAIRsharing.9d38e2)  where the ontology (URL_TO_INSERT_TERM_3993 https://fairsharing.org/search?recordType=terminology_artefact)  and its new versions are published
   </td>
  </tr>
  <tr>
   <td><strong>Onto. versioning capabilities</strong>
   </td>
   <td>Each ontology (URL_TO_INSERT_TERM_3997 https://fairsharing.org/search?recordType=terminology_artefact)  is characterized by a version number in its metadata, useful to track distinct versions of the same ontology (URL_TO_INSERT_TERM_3998 https://fairsharing.org/search?recordType=terminology_artefact) 
   </td>
  </tr>
  <tr>
   <td><strong>Description of Web based access to service</strong>
   </td>
   <td>Besides a Web-based interface that supports ontology (URL_TO_INSERT_TERM_3999 https://fairsharing.org/search?recordType=terminology_artefact)  search (URL_TO_INSERT_RECORD_4001 https://fairsharing.org/FAIRsharing.52b22c) , annotation, recommendation and map (URL_TO_INSERT_RECORD_4000 https://fairsharing.org/FAIRsharing.53edcc) ping, also a free-after-registration access by means of a REST API is provided to the users
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
   <td>Sample code to access REST API in distinct languages is available at: <a href="https://github.com (URL_TO_INSERT_RECORD_4002 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ncbo_rest_sample_code">https://github.com (URL_TO_INSERT_RECORD_4003 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ncbo_rest_sample_code</a>
   </td>
  </tr>
  <tr>
   <td><strong>Local deploy of service</strong>
   </td>
   <td>In principle, local deploy of services is possible, even if not extensively documented. Source code (Rails) for Web UI, REST API and Linked Data management is available on NCBO (URL_TO_INSERT_RECORD_4006 https://fairsharing.org/FAIRsharing.y2dt83)  GiHub account, <a href="https://github.com (URL_TO_INSERT_RECORD_4004 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo">https://github.com (URL_TO_INSERT_RECORD_4005 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo</a>
   </td>
  </tr>
  <tr>
   <td><strong>Source code reference</strong>
   </td>
   <td><a href="https://github.com (URL_TO_INSERT_RECORD_4007 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo">https://github.com (URL_TO_INSERT_RECORD_4008 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo</a>
   </td>
  </tr>
  <tr>
   <td><strong>Quantification of community of users</strong>
   </td>
   <td>GitHub (URL_TO_INSERT_RECORD_4009 https://fairsharing.org/FAIRsharing.c55d5e) : 
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
   <td><strong>URL (URL_TO_INSERT_RECORD_4010 https://fairsharing.org/FAIRsharing.9d38e2) </strong>
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
<em>Code</em>: Maven PO (URL_TO_INSERT_RECORD_4011 https://fairsharing.org/FAIRsharing.3ngg40) V version (from GitHub (URL_TO_INSERT_RECORD_4012 https://fairsharing.org/FAIRsharing.c55d5e) ): 1.10.0
<p>
<a href="https://github.com (URL_TO_INSERT_RECORD_4013 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena">https://github.com (URL_TO_INSERT_RECORD_4014 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena</a>
<p>
Latest commit on GitHub (URL_TO_INSERT_RECORD_4015 https://fairsharing.org/FAIRsharing.c55d5e) : September 2019
   </td>
  </tr>
  <tr>
   <td><strong>Host organisation</strong>
   </td>
   <td><a href="https://www.ohdsi.org/">Observational Health Data Sciences and Informat (URL_TO_INSERT_TERM_4016 https://fairsharing.org/search?recordType=model_and_format) ics (OHD (URL_TO_INSERT_RECORD_4017 https://fairsharing.org/FAIRsharing.bg7bb6) SI) initiative</a>
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
   <td>Useful to browse the set of Standard (URL_TO_INSERT_TERM_4018 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabularies which are part of the OMOP (URL_TO_INSERT_RECORD_4021 https://fairsharing.org/FAIRsharing.mct09a)  Common Data Model (URL_TO_INSERT_TERM_4019 https://fairsharing.org/search?recordType=model_and_format)  (CDM), version 5.x. They are maintained by the Observational Health Data Science and Informat (URL_TO_INSERT_TERM_4020 https://fairsharing.org/search?recordType=model_and_format) ics (OHD (URL_TO_INSERT_RECORD_4022 https://fairsharing.org/FAIRsharing.bg7bb6) SI, pronounced “Odyssey”) initiative
   </td>
  </tr>
  <tr>
   <td><strong>Set of ontologies (URL_TO_INSERT_TERM_4023 https://fairsharing.org/search?recordType=terminology_artefact)  covered</strong>
   </td>
   <td>Standard (URL_TO_INSERT_TERM_4024 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabularies which are part of the<a href="https://www.ohdsi.org/web/wiki/doku.php?id=documentation:vocabulary_etl"> OMOP (URL_TO_INSERT_RECORD_4030 https://fairsharing.org/FAIRsharing.mct09a)  Common Data Model (URL_TO_INSERT_TERM_4025 https://fairsharing.org/search?recordType=model_and_format)  (CDM)</a>, version 5.x. It integrates several source vocabularies including UMLS, SNOME (URL_TO_INSERT_RECORD_4026 https://fairsharing.org/3502) D, RxNorm (URL_TO_INSERT_RECORD_4031 https://fairsharing.org/FAIRsharing.36pf8q) , NDF (URL_TO_INSERT_RECORD_4027 https://fairsharing.org/FAIRsharing.cfcd4r) R (URL_TO_INSERT_RECORD_4029 https://fairsharing.org/FAIRsharing.e7e609) T (URL_TO_INSERT_RECORD_4032 https://fairsharing.org/FAIRsharing.901nkj) , VA Product, VA Class, ATC (URL_TO_INSERT_RECORD_4033 https://fairsharing.org/FAIRsharing.1a27h8) , MeSH, ICD10, GCN (URL_TO_INSERT_RECORD_4028 https://fairsharing.org/FAIRsharing.b7gm54) _SEQNO, ETC, Indication, ICD9CM, ICD9Proc, ICD10CM, LOiNC, etc.
   </td>
  </tr>
  <tr>
   <td><strong>Onto. format (URL_TO_INSERT_TERM_4034 https://fairsharing.org/search?recordType=model_and_format) s supported</strong>
   </td>
   <td>Not a specific format (URL_TO_INSERT_TERM_4036 https://fairsharing.org/search?recordType=model_and_format) , a collection (URL_TO_INSERT_TERM_4035 https://fairsharing.org/search?recordType=collection)  of ontology (URL_TO_INSERT_TERM_4037 https://fairsharing.org/search?recordType=terminology_artefact)  concepts / classes assigned to a specific domain and imported from a specific source vocabulary 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. importing capabilities</strong>
   </td>
   <td>Tailored to browse the Standard (URL_TO_INSERT_TERM_4038 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabularies which are part of the OMOP (URL_TO_INSERT_RECORD_4040 https://fairsharing.org/FAIRsharing.mct09a)  Common Data Model (URL_TO_INSERT_TERM_4039 https://fairsharing.org/search?recordType=model_and_format)  (CDM)
   </td>
  </tr>
  <tr>
   <td><strong>Onto. browsing capabilities</strong>
   </td>
   <td>Table based views are available to browse all the concepts belonging to a specific source vocabulary 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. search (URL_TO_INSERT_RECORD_4041 https://fairsharing.org/FAIRsharing.52b22c)  capabilities</strong>
   </td>
   <td>Search (URL_TO_INSERT_RECORD_4042 https://fairsharing.org/FAIRsharing.52b22c)  by term to gather all the source vocabularies where the term is found. It is possible to restrict search (URL_TO_INSERT_RECORD_4043 https://fairsharing.org/FAIRsharing.52b22c)  results by domain, class and source vocabulary
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
   <td>Each time a new version of the Standard (URL_TO_INSERT_TERM_4044 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabularies which are part of the OMOP (URL_TO_INSERT_RECORD_4048 https://fairsharing.org/FAIRsharing.mct09a)  Common Data Model (URL_TO_INSERT_TERM_4045 https://fairsharing.org/search?recordType=model_and_format)  (CDM) is available an updated the core (URL_TO_INSERT_RECORD_4046 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_4047 https://fairsharing.org/FAIRsharing.xMmOCL)  set of concept is available
   </td>
  </tr>
  <tr>
   <td><strong>Onto. versioning capabilities</strong>
   </td>
   <td>The latest version of the Standard (URL_TO_INSERT_TERM_4049 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabulary is V5.0
   </td>
  </tr>
  <tr>
   <td><strong>Description of Web-based access to service</strong>
   </td>
   <td>Athena is a Web interface available to browse concepts of the Standard (URL_TO_INSERT_TERM_4050 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabulary (V5.0). Both search (URL_TO_INSERT_RECORD_4051 https://fairsharing.org/FAIRsharing.52b22c)  results and the whole dataset can be downloaded after registration
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
   <td>In principle, local deploy of services is possible, even if not extensively documented. Source code on GitHub (URL_TO_INSERT_RECORD_4052 https://fairsharing.org/FAIRsharing.c55d5e)  account <a href="https://github.com (URL_TO_INSERT_RECORD_4053 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena">https://github.com (URL_TO_INSERT_RECORD_4054 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena</a> 
   </td>
  </tr>
  <tr>
   <td><strong>Source code reference</strong>
   </td>
   <td><a href="https://github.com (URL_TO_INSERT_RECORD_4055 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena">https://github.com (URL_TO_INSERT_RECORD_4056 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena</a>
   </td>
  </tr>
  <tr>
   <td><strong>Quantification of community of users</strong>
   </td>
   <td>GitHub (URL_TO_INSERT_RECORD_4057 https://fairsharing.org/FAIRsharing.c55d5e) : 29 stars and 6 forks
<p>
Twitter: 1.284 followers of the Observational Health Data Sciences and Informat (URL_TO_INSERT_TERM_4058 https://fairsharing.org/search?recordType=model_and_format) ics (OHD (URL_TO_INSERT_RECORD_4059 https://fairsharing.org/FAIRsharing.bg7bb6) SI) account
   </td>
  </tr>
</table>


### **Ontobee and the OBO Foundry** {footcite}`pmid27733503ontobee`

<!-- **Overview by Francesco** -->



<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td>OBO Foundry (URL_TO_INSERT_RECORD_4060 https://fairsharing.org/FAIRsharing.847069) 
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
   <td><strong>URL (URL_TO_INSERT_RECORD_4061 https://fairsharing.org/FAIRsharing.9d38e2) </strong>
   </td>
   <td><a href="http://www.ontobee.org (URL_TO_INSERT_RECORD_4062 https://fairsharing.org/FAIRsharing.q8fx1b) /">http://www.ontobee.org (URL_TO_INSERT_RECORD_4063 https://fairsharing.org/FAIRsharing.q8fx1b) /</a> (<a href="http://obofoundry.org/">http://obofoundry.org/</a>)
   </td>
  </tr>
  <tr>
   <td><strong>Latest version of service / data / code (where applicable)</strong>
   </td>
   <td><em>Content (OBO Foundry (URL_TO_INSERT_RECORD_4064 https://fairsharing.org/FAIRsharing.847069) )</em>: last update April 2020
<p>
<em>Code (Ontobee (URL_TO_INSERT_RECORD_4065 https://fairsharing.org/FAIRsharing.q8fx1b) )</em>: <a href="https://github.com (URL_TO_INSERT_RECORD_4066 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee">https://github.com (URL_TO_INSERT_RECORD_4067 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee</a>
<p>
Latest commit on GitHub (URL_TO_INSERT_RECORD_4068 https://fairsharing.org/FAIRsharing.c55d5e) : August 2018
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
   <td>Ontobee (URL_TO_INSERT_RECORD_4075 https://fairsharing.org/FAIRsharing.q8fx1b)  has been used as the default ontology (URL_TO_INSERT_TERM_4069 https://fairsharing.org/search?recordType=terminology_artefact)  Linked Data server for most <a href="http://obofoundry.org/">Open Biological and Biomedical Ontology (URL_TO_INSERT_TERM_4070 https://fairsharing.org/search?recordType=terminology_artefact)  (OBO (URL_TO_INSERT_RECORD_4074 https://fairsharing.org/FAIRsharing.847069) ) Foundry</a> library ontologies (URL_TO_INSERT_TERM_4072 https://fairsharing.org/search?recordType=terminology_artefact) . The OBO Foundry (URL_TO_INSERT_RECORD_4073 https://fairsharing.org/FAIRsharing.847069)  is a collective of ontology (URL_TO_INSERT_TERM_4071 https://fairsharing.org/search?recordType=terminology_artefact)  developers that are committed to collaboration and adherence to shared principles
   </td>
  </tr>
  <tr>
   <td><strong>Set of ontologies (URL_TO_INSERT_TERM_4076 https://fairsharing.org/search?recordType=terminology_artefact)  covered</strong>
   </td>
   <td>164 active ontologies (URL_TO_INSERT_TERM_4077 https://fairsharing.org/search?recordType=terminology_artefact) , 5 orphaned ontologies (URL_TO_INSERT_TERM_4078 https://fairsharing.org/search?recordType=terminology_artefact)  and 57 inactive ontologies (URL_TO_INSERT_TERM_4079 https://fairsharing.org/search?recordType=terminology_artefact)  (in OBO Foundry (URL_TO_INSERT_RECORD_4080 https://fairsharing.org/FAIRsharing.847069) )
   </td>
  </tr>
  <tr>
   <td><strong>Onto. format (URL_TO_INSERT_TERM_4081 https://fairsharing.org/search?recordType=model_and_format) s supported</strong>
   </td>
   <td>OWL (URL_TO_INSERT_RECORD_4082 https://fairsharing.org/FAIRsharing.atygwy)  and OBO (URL_TO_INSERT_RECORD_4083 https://fairsharing.org/FAIRsharing.847069) 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. importing capabilities</strong>
   </td>
   <td>Ontobee (URL_TO_INSERT_RECORD_4092 https://fairsharing.org/FAIRsharing.q8fx1b)  can import both OWL (URL_TO_INSERT_RECORD_4088 https://fairsharing.org/FAIRsharing.atygwy)  and OBO (URL_TO_INSERT_RECORD_4091 https://fairsharing.org/FAIRsharing.847069)  ontologies (URL_TO_INSERT_TERM_4085 https://fairsharing.org/search?recordType=terminology_artefact) . New ontologies (URL_TO_INSERT_TERM_4086 https://fairsharing.org/search?recordType=terminology_artefact)  can be proposed tired to the set of OBO Foundry (URL_TO_INSERT_RECORD_4089 https://fairsharing.org/FAIRsharing.847069)  ontologies (URL_TO_INSERT_TERM_4087 https://fairsharing.org/search?recordType=terminology_artefact) ; a committee will review the ontology (URL_TO_INSERT_TERM_4084 https://fairsharing.org/search?recordType=terminology_artefact)  to check if it adheres to all the OBO Foundry (URL_TO_INSERT_RECORD_4090 https://fairsharing.org/FAIRsharing.847069)  principles
   </td>
  </tr>
  <tr>
   <td><strong>Onto. browsing capabilities</strong>
   </td>
   <td>The OBO Foundry (URL_TO_INSERT_RECORD_4099 https://fairsharing.org/FAIRsharing.847069)  portal provides a set of metadata describing each ontology (URL_TO_INSERT_TERM_4094 https://fairsharing.org/search?recordType=terminology_artefact)  together with the possibility to download the same ontology (URL_TO_INSERT_TERM_4095 https://fairsharing.org/search?recordType=terminology_artefact)  in several format (URL_TO_INSERT_TERM_4093 https://fairsharing.org/search?recordType=model_and_format) s. To browse ontologies (URL_TO_INSERT_TERM_4097 https://fairsharing.org/search?recordType=terminology_artefact) , the OBO Foundry (URL_TO_INSERT_RECORD_4100 https://fairsharing.org/FAIRsharing.847069)  portal points to the ontology (URL_TO_INSERT_TERM_4096 https://fairsharing.org/search?recordType=terminology_artefact)  browsing pages of other Web platforms including <a href="http://www.ontobee.org (URL_TO_INSERT_RECORD_4101 https://fairsharing.org/FAIRsharing.q8fx1b) /">Ontobee</a>, <a href="https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_4098 https://fairsharing.org/FAIRsharing.4m97ah) /">BioPortal</a> and the <a href="https://www.ebi.ac.uk/ols">Ontology Lookup Service</a>.
   </td>
  </tr>
  <tr>
   <td><strong>Onto. search (URL_TO_INSERT_RECORD_4102 https://fairsharing.org/FAIRsharing.52b22c)  capabilities</strong>
   </td>
   <td>The OBO Foundry (URL_TO_INSERT_RECORD_4106 https://fairsharing.org/FAIRsharing.847069)  portal exploits <a href="http://www.ontobee.org (URL_TO_INSERT_RECORD_4108 https://fairsharing.org/FAIRsharing.q8fx1b) /">Ontobee</a> to provide users with ontology (URL_TO_INSERT_TERM_4103 https://fairsharing.org/search?recordType=terminology_artefact)  search (URL_TO_INSERT_RECORD_4109 https://fairsharing.org/FAIRsharing.52b22c)  capabilities.Ontobee (URL_TO_INSERT_RECORD_4107 https://fairsharing.org/FAIRsharing.q8fx1b)  enables users to search (URL_TO_INSERT_RECORD_4110 https://fairsharing.org/FAIRsharing.52b22c)  ontology (URL_TO_INSERT_TERM_4104 https://fairsharing.org/search?recordType=terminology_artefact)  concepts by term, eventually restricting the search (URL_TO_INSERT_RECORD_4111 https://fairsharing.org/FAIRsharing.52b22c)  to a specific ontology (URL_TO_INSERT_TERM_4105 https://fairsharing.org/search?recordType=terminology_artefact) 
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
   <td>An established <a href="http://obofoundry.org/principles/fp-004-versioning.html">PURL system to publish new versions / updates of an ontology (URL_TO_INSERT_TERM_4113 https://fairsharing.org/search?recordType=terminology_artefact) </a> is defined; new versions of an ontologies (URL_TO_INSERT_TERM_4114 https://fairsharing.org/search?recordType=terminology_artefact)  should be accessible at PURL (URL_TO_INSERT_RECORD_4115 https://fairsharing.org/FAIRsharing.3e603c)  (URL_TO_INSERT_RECORD_4116 https://fairsharing.org/FAIRsharing.9d38e2) s with the following format (URL_TO_INSERT_TERM_4112 https://fairsharing.org/search?recordType=model_and_format) : <code>http://purl.obolibrary.org/obo/idspace/YYYY-MM-DD/idspace.owl</code> or <code>.obo</code>, for instance: <code><a href="https://raw.githubusercontent.com/BiodiversityOntologies/bco/2020-03-27/bco.owl">https://raw.githubusercontent.com/BiodiversityOntologies/bco/2020-03-27/bco.owl</a></code>
   </td>
  </tr>
  <tr>
   <td><strong>Onto. versioning capabilities</strong>
   </td>
   <td>The OBO (URL_TO_INSERT_RECORD_4121 https://fairsharing.org/FAIRsharing.847069)  principles, implemented by the ontologies (URL_TO_INSERT_TERM_4118 https://fairsharing.org/search?recordType=terminology_artefact)  available in OBO Foundry (URL_TO_INSERT_RECORD_4120 https://fairsharing.org/FAIRsharing.847069) , enforces a system of versioning systems, with each ontology (URL_TO_INSERT_TERM_4117 https://fairsharing.org/search?recordType=terminology_artefact)  version receiving an unique identifier (URL_TO_INSERT_TERM_4119 https://fairsharing.org/search?recordType=identifier_schema)  (by means of numbers, dates, tags)
   </td>
  </tr>
  <tr>
   <td><strong>Description of Web-based access to service</strong>
   </td>
   <td>Ontobee (URL_TO_INSERT_RECORD_4123 https://fairsharing.org/FAIRsharing.q8fx1b)  provides a web interface that supports, besides search (URL_TO_INSERT_RECORD_4125 https://fairsharing.org/FAIRsharing.52b22c) ing for ontology (URL_TO_INSERT_TERM_4122 https://fairsharing.org/search?recordType=terminology_artefact)  concepts, the execution of SP (URL_TO_INSERT_RECORD_4126 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_4124 https://fairsharing.org/FAIRsharing.87ccfd)  queries and the annotation of text excerpts
   </td>
  </tr>
  <tr>
   <td><strong>Description of API</strong>
   </td>
   <td>No specific REST API is provided; users can retrieve both HTML (URL_TO_INSERT_RECORD_4130 https://fairsharing.org/FAIRsharing.YugnuL)  and RDF (URL_TO_INSERT_RECORD_4128 https://fairsharing.org/FAIRsharing.p77ph9)  descriptions of concepts that belongs to Ontobee (URL_TO_INSERT_RECORD_4129 https://fairsharing.org/FAIRsharing.q8fx1b)  ontologies (URL_TO_INSERT_TERM_4127 https://fairsharing.org/search?recordType=terminology_artefact) , in adherence to the principles of Linked Data community
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
   <td>In principle, local deploy of services is possible, even if not extensively documented. Source code on GiHub account <a href="https://github.com (URL_TO_INSERT_RECORD_4131 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee">https://github.com (URL_TO_INSERT_RECORD_4132 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee</a>
   </td>
  </tr>
  <tr>
   <td><strong>Source code reference</strong>
   </td>
   <td><a href="https://github.com (URL_TO_INSERT_RECORD_4133 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee">https://github.com (URL_TO_INSERT_RECORD_4134 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee</a>
   </td>
  </tr>
  <tr>
   <td><strong>Quantification of community of users</strong>
   </td>
   <td>GitHub (URL_TO_INSERT_RECORD_4135 https://fairsharing.org/FAIRsharing.c55d5e) : 12 stars and 4 forks
<p>
Twitter OBO (URL_TO_INSERT_RECORD_4136 https://fairsharing.org/FAIRsharing.847069) F (URL_TO_INSERT_RECORD_4137 https://fairsharing.org/FAIRsharing.t6y94s) oundry account: 220 followers
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
