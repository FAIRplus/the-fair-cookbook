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

This recipe provides **guidance on the selection and exploitation of ontology (URL_TO_INSERT_TERM_2723 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2724 https://fairsharing.org/FAIRsharing.Mkl9RR) s** . 

>* **[Objective of the recipe: introduction to ontology lookup services](#heading=h.bb3h294tvdau)**
>
>* **[Selecting an ontology lookup service](#bookmark=id.okwm6u2vsbft)**
>
>* **[Overview of widespread ontology lookup services](#bookmark=id.x42hawpkzgd3)**

An ***ontology (URL_TO_INSERT_TERM_2725 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2726 https://fairsharing.org/FAIRsharing.Mkl9RR) *** 
refers to *any type of application, standalone or Web-based, that enables the use of existing ontologies (URL_TO_INSERT_TERM_2727 https://fairsharing.org/search?recordType=terminology_artefact)  to support knowledge 
formalization and sharing, by fostering ontology (URL_TO_INSERT_TERM_2728 https://fairsharing.org/search?recordType=terminology_artefact) -based descriptions of knowledge*. 




Tools useful to build, edit or maintain ontologies (URL_TO_INSERT_TERM_2730 https://fairsharing.org/search?recordType=terminology_artefact)  are not considered ontology (URL_TO_INSERT_TERM_2729 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2731 https://fairsharing.org/FAIRsharing.Mkl9RR) s and thus are out of the scope of this recipe. 

In essence, an ontology (URL_TO_INSERT_TERM_2732 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2733 https://fairsharing.org/FAIRsharing.Mkl9RR)  is a platform that provides users with the possibility to **search (URL_TO_INSERT_RECORD_2734 https://fairsharing.org/FAIRsharing.52b22c)  in a set of
ontologies (URL_TO_INSERT_TERM_2735 https://fairsharing.org/search?recordType=terminology_artefact) , the most suitable concepts to describe the semantics of a piece of knowledge of interest,
usually available in the form of one or more keywords or a text excerpt**. 

Most ontology (URL_TO_INSERT_TERM_2736 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2737 https://fairsharing.org/FAIRsharing.Mkl9RR) s are available as Web applications: most of them also support programmatic access to their 
capabilities by means of (REST) APIs. Ontology (URL_TO_INSERT_TERM_2738 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2739 https://fairsharing.org/FAIRsharing.Mkl9RR) s can vary in the features that are provided, but often include:



* **Complex search (URL_TO_INSERT_RECORD_2742 https://fairsharing.org/FAIRsharing.52b22c) ing for concepts of interest**: most services implement advanced search (URL_TO_INSERT_RECORD_2743 https://fairsharing.org/FAIRsharing.52b22c)  features (i.e. scoping the search (URL_TO_INSERT_RECORD_2744 https://fairsharing.org/FAIRsharing.52b22c)  to specific ontologies (URL_TO_INSERT_TERM_2741 https://fairsharing.org/search?recordType=terminology_artefact)  or to specific parts of an ontology (URL_TO_INSERT_TERM_2740 https://fairsharing.org/search?recordType=terminology_artefact) ) or allow users to specify fine-grained patterns to aggregate or restrict the scope of search (URL_TO_INSERT_RECORD_2745 https://fairsharing.org/FAIRsharing.52b22c)  results.
* **Advanced browsing capabilities**, to explore the contents of a specific ontology (URL_TO_INSERT_TERM_2746 https://fairsharing.org/search?recordType=terminology_artefact)  by means of custom data navigation widgets such as tree-based views.
* **Managing distinct versions** of an ontology (URL_TO_INSERT_TERM_2747 https://fairsharing.org/search?recordType=terminology_artefact)  and alert its users when specific concepts become obsolete. 
* **Importing** user-provided ontologies (URL_TO_INSERT_TERM_2749 https://fairsharing.org/search?recordType=terminology_artefact) , giving consumers the ability to leverage a service for other terminologies (URL_TO_INSERT_TERM_2748 https://fairsharing.org/search?recordType=terminology_artefact)  beyond those included.
* Programmatic means to **access and deploy instances of the ontology (URL_TO_INSERT_TERM_2750 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2751 https://fairsharing.org/FAIRsharing.Mkl9RR)  in the premises of its users** represents another differentiating feature, using relevant documentation.
* **Recommending ontologies (URL_TO_INSERT_TERM_2752 https://fairsharing.org/search?recordType=terminology_artefact) ** based on the input of a given term, with ontologies (URL_TO_INSERT_TERM_2753 https://fairsharing.org/search?recordType=terminology_artefact)  ranked according to custom-weighted criteria.
* Access to an **active user community** that supports and exploits a specific ontology (URL_TO_INSERT_TERM_2754 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2755 https://fairsharing.org/FAIRsharing.Mkl9RR) , serving as an indication of widespread adoption and selection.

This recipe presents guideline (URL_TO_INSERT_TERM_2757 https://fairsharing.org/search?recordType=reporting_guideline) s and relevant considerations when choosing an ontology (URL_TO_INSERT_TERM_2756 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2758 https://fairsharing.org/FAIRsharing.Mkl9RR) , followed by
overview of existing public ontology (URL_TO_INSERT_TERM_2759 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2760 https://fairsharing.org/FAIRsharing.Mkl9RR) s and a comparison of their core (URL_TO_INSERT_RECORD_2761 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_2762 https://fairsharing.org/FAIRsharing.xMmOCL)  features.


## Selecting An Ontology Lookup Service

This section provides guideline (URL_TO_INSERT_TERM_2764 https://fairsharing.org/search?recordType=reporting_guideline) s and suggestions on how to select and leverage an ontology (URL_TO_INSERT_TERM_2763 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2765 https://fairsharing.org/FAIRsharing.Mkl9RR) , on the basis
of the knowledge needs and ontology (URL_TO_INSERT_TERM_2767 https://fairsharing.org/search?recordType=terminology_artefact)  use patterns that characterize a specific knowledge-intensive project (URL_TO_INSERT_TERM_2766 https://fairsharing.org/search?recordType=project) . 

Several aspects to consider when choosing an ontology (URL_TO_INSERT_TERM_2768 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2769 https://fairsharing.org/FAIRsharing.Mkl9RR)  are derived based on a series of commonly asked questions;



* **Is the set of ontologies (URL_TO_INSERT_TERM_2772 https://fairsharing.org/search?recordType=terminology_artefact)  incorporated in the ontology (URL_TO_INSERT_TERM_2771 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2773 https://fairsharing.org/FAIRsharing.Mkl9RR)  suitable to formally describe the knowledge domain my project (URL_TO_INSERT_TERM_2770 https://fairsharing.org/search?recordType=project)  is interested in?**

    Ontology (URL_TO_INSERT_TERM_2774 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2776 https://fairsharing.org/FAIRsharing.Mkl9RR) s usually provide access and enable users to search (URL_TO_INSERT_RECORD_2777 https://fairsharing.org/FAIRsharing.52b22c)  and reference classes and properties of _a specific set of ontologies (URL_TO_INSERT_TERM_2775 https://fairsharing.org/search?recordType=terminology_artefact)  related to a specific knowledge domain_ (i.e. biomedical knowledge).
    When choosing an ontology (URL_TO_INSERT_TERM_2779 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2781 https://fairsharing.org/FAIRsharing.Mkl9RR)  it is important to verify whether the ontologies (URL_TO_INSERT_TERM_2780 https://fairsharing.org/search?recordType=terminology_artefact)  covered by a specific service are suitable to describe the content of our knowledge-intensive project (URL_TO_INSERT_TERM_2778 https://fairsharing.org/search?recordType=project) . 
    Besides, a list of the ontologies (URL_TO_INSERT_TERM_2782 https://fairsharing.org/search?recordType=terminology_artefact)  covered, and interactive widgets to explore such ontologies (URL_TO_INSERT_TERM_2783 https://fairsharing.org/search?recordType=terminology_artefact)  (e.g. tree-based views), 
    some ontology (URL_TO_INSERT_TERM_2784 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2786 https://fairsharing.org/FAIRsharing.Mkl9RR) s also provide _ontology (URL_TO_INSERT_TERM_2785 https://fairsharing.org/search?recordType=terminology_artefact)  recommendation capabilities:_ given some “sample” 
    (i.e. text excerpt or list of keywords) of the knowledge we need to describe by means of available ontologies (URL_TO_INSERT_TERM_2787 https://fairsharing.org/search?recordType=terminology_artefact) , 
    the ontology (URL_TO_INSERT_TERM_2788 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2790 https://fairsharing.org/FAIRsharing.Mkl9RR)  ‘recommender’ suggests which are the best ontologies (URL_TO_INSERT_TERM_2789 https://fairsharing.org/search?recordType=terminology_artefact)  to use to this propose.

* **Do I need to consider / rely on private ontologies (URL_TO_INSERT_TERM_2792 https://fairsharing.org/search?recordType=terminology_artefact)  in my project (URL_TO_INSERT_TERM_2791 https://fairsharing.org/search?recordType=project) ? Do I need to use ontologies (URL_TO_INSERT_TERM_2793 https://fairsharing.org/search?recordType=terminology_artefact)  that are not already 
    imported and thus available in the ontology (URL_TO_INSERT_TERM_2794 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2795 https://fairsharing.org/FAIRsharing.Mkl9RR)  of my choice?**

    Some ontology (URL_TO_INSERT_TERM_2796 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2798 https://fairsharing.org/FAIRsharing.Mkl9RR) s enable users to import external (i.e. user-provided) ontologies (URL_TO_INSERT_TERM_2797 https://fairsharing.org/search?recordType=terminology_artefact)  in order to incorporate
    the content of these ontologies (URL_TO_INSERT_TERM_2799 https://fairsharing.org/search?recordType=terminology_artefact)  in their search (URL_TO_INSERT_RECORD_2800 https://fairsharing.org/FAIRsharing.52b22c)  and recommendation capabilities. 
    This feature could represent a key factor to consider when choosing an ontology (URL_TO_INSERT_TERM_2801 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2802 https://fairsharing.org/FAIRsharing.Mkl9RR)  since several 
    knowledge-intensive project (URL_TO_INSERT_TERM_2803 https://fairsharing.org/search?recordType=project) s rely on private ontologies (URL_TO_INSERT_TERM_2804 https://fairsharing.org/search?recordType=terminology_artefact)  or need to consider a set of additional ontologies (URL_TO_INSERT_TERM_2805 https://fairsharing.org/search?recordType=terminology_artefact)  not 
    natively covered by a specific ontology (URL_TO_INSERT_TERM_2806 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2807 https://fairsharing.org/FAIRsharing.Mkl9RR) .

* **Because of data privacy or data protection issues, do I need to use an instance of the ontology (URL_TO_INSERT_TERM_2808 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2809 https://fairsharing.org/FAIRsharing.Mkl9RR)  that
is deployed locally on my private computing infrastructure?**

    Several ontology (URL_TO_INSERT_TERM_2810 https://fairsharing.org/search?recordType=terminology_artefact) -lookup services provide the possibility to deploy the service on the private computing 
    infrastructure of its users. This feature would be particularly relevant when private ontologies (URL_TO_INSERT_TERM_2811 https://fairsharing.org/search?recordType=terminology_artefact)  are adopted in a 
    knowledge-intensive project (URL_TO_INSERT_TERM_2812 https://fairsharing.org/search?recordType=project) .

* **Which are the usage patterns I will rely on in order to exploit the ontology (URL_TO_INSERT_TERM_2813 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2814 https://fairsharing.org/FAIRsharing.Mkl9RR) ? Will the 1)
massive and systematic exploitation of the ontology (URL_TO_INSERT_TERM_2815 https://fairsharing.org/search?recordType=terminology_artefact)  search (URL_TO_INSERT_RECORD_2817 https://fairsharing.org/FAIRsharing.52b22c) , 2) the recommendation features of the ontology (URL_TO_INSERT_TERM_2816 https://fairsharing.org/search?recordType=terminology_artefact)  lookup
service or 3) the integration of its capabilities in more complex systems, require the possibility to programmatically 
access the service by means of an application programming interface (API)?**

    Ontology (URL_TO_INSERT_TERM_2818 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2819 https://fairsharing.org/FAIRsharing.Mkl9RR) s usually provide a (Web-based) user interface as the preferred way to interact with them to
    browse and search (URL_TO_INSERT_RECORD_2821 https://fairsharing.org/FAIRsharing.52b22c)  for ontologies (URL_TO_INSERT_TERM_2820 https://fairsharing.org/search?recordType=terminology_artefact) , or recommend relevant concepts to describe contents of interest. 
    In several scenarios, the possibility to programmatically interact with ontology (URL_TO_INSERT_TERM_2822 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2823 https://fairsharing.org/FAIRsharing.Mkl9RR) s would be extremely
    valuable; to this purpose, several ontology (URL_TO_INSERT_TERM_2824 https://fairsharing.org/search?recordType=terminology_artefact) -lookup services implement an API (mostly based on REST interactions)
    that enable the user to programmatically invoke the majority of ontology (URL_TO_INSERT_TERM_2825 https://fairsharing.org/search?recordType=terminology_artefact)  search (URL_TO_INSERT_RECORD_2826 https://fairsharing.org/FAIRsharing.52b22c)  features of the same service. 
    In order to simplify the integration of the ontology (URL_TO_INSERT_TERM_2827 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2828 https://fairsharing.org/FAIRsharing.Mkl9RR)  support into external applications,  
   several-ontology (URL_TO_INSERT_TERM_2829 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2830 https://fairsharing.org/FAIRsharing.Mkl9RR) s provide users with language-specific clients to interact with them through their API. 

* **Is the distribution license of the ontology (URL_TO_INSERT_TERM_2831 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2832 https://fairsharing.org/FAIRsharing.Mkl9RR)  compatible with the way I plan to exploit the 
features provided the same service in my project (URL_TO_INSERT_TERM_2833 https://fairsharing.org/search?recordType=project)  or with the way I plan to integrate the same service in my project (URL_TO_INSERT_TERM_2834 https://fairsharing.org/search?recordType=project) ?**

    The licencing terms of the ontology (URL_TO_INSERT_TERM_2835 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2836 https://fairsharing.org/FAIRsharing.Mkl9RR)  of choice intended for use in a given context and 
    knowledge-intensive project (URL_TO_INSERT_TERM_2837 https://fairsharing.org/search?recordType=project) , is a key consideration when selecting an ontology (URL_TO_INSERT_TERM_2838 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2839 https://fairsharing.org/FAIRsharing.Mkl9RR) : available 
    ontology (URL_TO_INSERT_TERM_2840 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2841 https://fairsharing.org/FAIRsharing.Mkl9RR) s range from open-source applications to commercial tools, and it is best to choose one with funding in mind.

* **Does the ontology (URL_TO_INSERT_TERM_2842 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2845 https://fairsharing.org/FAIRsharing.Mkl9RR)  manage ontology (URL_TO_INSERT_TERM_2843 https://fairsharing.org/search?recordType=terminology_artefact)  versioning and updates so that I can easily reflect any ontology (URL_TO_INSERT_TERM_2844 https://fairsharing.org/search?recordType=terminology_artefact)  
update into my knowledge-intensive project (URL_TO_INSERT_TERM_2846 https://fairsharing.org/search?recordType=project) ? **

    Ontologies (URL_TO_INSERT_TERM_2849 https://fairsharing.org/search?recordType=terminology_artefact)  and terminologies (URL_TO_INSERT_TERM_2847 https://fairsharing.org/search?recordType=terminology_artefact)  usually evolve over time: when a new, updated version of an ontology (URL_TO_INSERT_TERM_2848 https://fairsharing.org/search?recordType=terminology_artefact)  used in a 
    knowledge-intensive project (URL_TO_INSERT_TERM_2850 https://fairsharing.org/search?recordType=project)  becomes available, best practice suggests that we should also update the part of our 
    project (URL_TO_INSERT_TERM_2851 https://fairsharing.org/search?recordType=project) s that rely on such ontology (URL_TO_INSERT_TERM_2852 https://fairsharing.org/search?recordType=terminology_artefact) . Some ontology (URL_TO_INSERT_TERM_2853 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2854 https://fairsharing.org/FAIRsharing.Mkl9RR) s implement specific procedures and tools to manage
    and propagate ontology (URL_TO_INSERT_TERM_2855 https://fairsharing.org/search?recordType=terminology_artefact)  updates; the availability of such tools would simplify the implementation of changes deriving
    from ontology (URL_TO_INSERT_TERM_2857 https://fairsharing.org/search?recordType=terminology_artefact)  updates in the project (URL_TO_INSERT_TERM_2856 https://fairsharing.org/search?recordType=project) s under consideration.

* **Is the ontology (URL_TO_INSERT_TERM_2858 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2859 https://fairsharing.org/FAIRsharing.Mkl9RR)  supported by an active community of developers
or by an active company? Which are the available channels I can rely on to receive support on the usage and integration 
of the ontology (URL_TO_INSERT_TERM_2860 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2861 https://fairsharing.org/FAIRsharing.Mkl9RR) ?**

    The support of an active community of developers and users is a key aspect to take into account when choosing an 
    ontology (URL_TO_INSERT_TERM_2862 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2864 https://fairsharing.org/FAIRsharing.Mkl9RR) . This could be quantified by evaluating several factors of an ontology (URL_TO_INSERT_TERM_2863 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2865 https://fairsharing.org/FAIRsharing.Mkl9RR)  including:
    (i) availability of mailing or support lists; (ii) for open-source project (URL_TO_INSERT_TERM_2867 https://fairsharing.org/search?recordType=project) s, using metric (URL_TO_INSERT_TERM_2866 https://fairsharing.org/search?recordType=metric) s such as the star-rating,
    the number of forks and followers and the frequency of commits of the project (URL_TO_INSERT_TERM_2868 https://fairsharing.org/search?recordType=project)  on the code-sharing platform used 
    (e.g. GitHub (URL_TO_INSERT_RECORD_2871 https://fairsharing.org/FAIRsharing.c55d5e) ); (iii) size of the community of users of the ontology (URL_TO_INSERT_TERM_2869 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2870 https://fairsharing.org/FAIRsharing.Mkl9RR)  (e.g. how many followers on social
    media accounts, how many clients advertised on the Website).

## Key Selection Criteria

The above questions have highlighted 20 factors which should be taken into account when choosing a service. 
These factors can be categorised into 3 groups; **ontology (URL_TO_INSERT_TERM_2873 https://fairsharing.org/search?recordType=terminology_artefact)  informat (URL_TO_INSERT_TERM_2872 https://fairsharing.org/search?recordType=model_and_format) ion, functionality** and **interfaces**, and include;

### **Ontology Information**



1. **URL**: the main URL (URL_TO_INSERT_RECORD_2876 https://fairsharing.org/FAIRsharing.9d38e2)  where the ontology (URL_TO_INSERT_TERM_2874 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2875 https://fairsharing.org/FAIRsharing.Mkl9RR)  can be accessed
2. **Latest version of service / data / code (where applicable**): the most recent version of both the content (i.e. ontologies (URL_TO_INSERT_TERM_2878 https://fairsharing.org/search?recordType=terminology_artefact) ) and the code of the ontology (URL_TO_INSERT_TERM_2877 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2879 https://fairsharing.org/FAIRsharing.Mkl9RR) 
3. **Host Organisation**: the organisation responsible for the maintenance of the ontology (URL_TO_INSERT_TERM_2880 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2881 https://fairsharing.org/FAIRsharing.Mkl9RR) 
4. **Public / private**: is the ontology (URL_TO_INSERT_TERM_2882 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2883 https://fairsharing.org/FAIRsharing.Mkl9RR)  a public or private infrastructure?
5. **Licence**: the licence that regulates the use and cost of the ontology (URL_TO_INSERT_TERM_2884 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2885 https://fairsharing.org/FAIRsharing.Mkl9RR) 
6. **Domain**: which is the knowledge domain covered by the ontologies (URL_TO_INSERT_TERM_2887 https://fairsharing.org/search?recordType=terminology_artefact)  referenced in the ontology (URL_TO_INSERT_TERM_2886 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2888 https://fairsharing.org/FAIRsharing.Mkl9RR) ?
7. **Quantification of community of users**: objective measures to quantify the community of users supporting and consuming an ontology (URL_TO_INSERT_TERM_2889 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2890 https://fairsharing.org/FAIRsharing.Mkl9RR) , including: number of stars and forks on GitHub (URL_TO_INSERT_RECORD_2891 https://fairsharing.org/FAIRsharing.c55d5e) , number of social media followers

### **Functionality**



8. **Number and complexity of ontologies (URL_TO_INSERT_TERM_2893 https://fairsharing.org/search?recordType=terminology_artefact)  covered**: how many ontologies (URL_TO_INSERT_TERM_2894 https://fairsharing.org/search?recordType=terminology_artefact)  does the ontology (URL_TO_INSERT_TERM_2892 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2895 https://fairsharing.org/FAIRsharing.Mkl9RR)  cover and how complex are they?
9. **Ontology (URL_TO_INSERT_TERM_2898 https://fairsharing.org/search?recordType=terminology_artefact)  format (URL_TO_INSERT_TERM_2896 https://fairsharing.org/search?recordType=model_and_format) s supported**: which ontology (URL_TO_INSERT_TERM_2899 https://fairsharing.org/search?recordType=terminology_artefact)  format (URL_TO_INSERT_TERM_2897 https://fairsharing.org/search?recordType=model_and_format) s are supported by the ontology (URL_TO_INSERT_TERM_2900 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2901 https://fairsharing.org/FAIRsharing.Mkl9RR) ?
10. **Ontology (URL_TO_INSERT_TERM_2902 https://fairsharing.org/search?recordType=terminology_artefact)  importing capabilities**: if and how ontologies (URL_TO_INSERT_TERM_2904 https://fairsharing.org/search?recordType=terminology_artefact)  can be imported and thus indexed by the ontology (URL_TO_INSERT_TERM_2903 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2905 https://fairsharing.org/FAIRsharing.Mkl9RR) ?
11. **Ontology (URL_TO_INSERT_TERM_2906 https://fairsharing.org/search?recordType=terminology_artefact)  browsing capabilities**: which interaction patterns are available to browse the set of ontologies (URL_TO_INSERT_TERM_2908 https://fairsharing.org/search?recordType=terminology_artefact)  contemplated by the ontology (URL_TO_INSERT_TERM_2907 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2909 https://fairsharing.org/FAIRsharing.Mkl9RR) ?
12. **Ontology (URL_TO_INSERT_TERM_2910 https://fairsharing.org/search?recordType=terminology_artefact)  search (URL_TO_INSERT_RECORD_2915 https://fairsharing.org/FAIRsharing.52b22c)  capabilities**: which search (URL_TO_INSERT_RECORD_2916 https://fairsharing.org/FAIRsharing.52b22c)  patterns are provided by the ontology (URL_TO_INSERT_TERM_2911 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2914 https://fairsharing.org/FAIRsharing.Mkl9RR)  to identify the best concept useful to represent the semantic of a term? When search (URL_TO_INSERT_RECORD_2917 https://fairsharing.org/FAIRsharing.52b22c) ing against a term, does the ontology (URL_TO_INSERT_TERM_2912 https://fairsharing.org/search?recordType=terminology_artefact)  give an indication of whether the term has been derived from a different ontology (URL_TO_INSERT_TERM_2913 https://fairsharing.org/search?recordType=terminology_artefact) ?
13. **Ontology (URL_TO_INSERT_TERM_2918 https://fairsharing.org/search?recordType=terminology_artefact)  recommendation capabilities**: does the ontology (URL_TO_INSERT_TERM_2919 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2921 https://fairsharing.org/FAIRsharing.Mkl9RR)  provide users with a recommendation concerning the most suitable ontologies (URL_TO_INSERT_TERM_2920 https://fairsharing.org/search?recordType=terminology_artefact)  to semantically characterize the contents of some text / a set of keywords? 
14. **Ontology (URL_TO_INSERT_TERM_2922 https://fairsharing.org/search?recordType=terminology_artefact)  update capabilities**: how are terms and/or relationships updated in a given ontology (URL_TO_INSERT_TERM_2923 https://fairsharing.org/search?recordType=terminology_artefact)  and how is this governed? Is this an automatic or manual update and what happens to terms that are considered obsolete?
15. **Ontology (URL_TO_INSERT_TERM_2924 https://fairsharing.org/search?recordType=terminology_artefact)  versioning capabilities**: are there predefined patterns to identify, manage and compare distinct versions of an ontology (URL_TO_INSERT_TERM_2925 https://fairsharing.org/search?recordType=terminology_artefact) ? 

### **Interfaces**



16. **Description of Web-based access to service**: which ontology (URL_TO_INSERT_TERM_2926 https://fairsharing.org/search?recordType=terminology_artefact)  browsing  and search (URL_TO_INSERT_RECORD_2931 https://fairsharing.org/FAIRsharing.52b22c)  patterns are available to the (Web-based) user interface of the ontology (URL_TO_INSERT_TERM_2927 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2929 https://fairsharing.org/FAIRsharing.Mkl9RR) ? Does the ontology (URL_TO_INSERT_TERM_2928 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2930 https://fairsharing.org/FAIRsharing.Mkl9RR)  also provide programmatic access to its data and services (e.g. by means of a REST API)?
17. **Description of API**: reference to the documentation of the (REST) API provided by the ontology (URL_TO_INSERT_TERM_2932 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2933 https://fairsharing.org/FAIRsharing.Mkl9RR) , if any
18. **Developer resources**: description of resources provided to developers in order to ease the programmatic access to the features of the ontology (URL_TO_INSERT_TERM_2934 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2935 https://fairsharing.org/FAIRsharing.Mkl9RR)  (i.e. libraries to query the REST API from a specific programming language).
19. **Local deploy of service**: possibility to locally deploy the ontology (URL_TO_INSERT_TERM_2936 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2937 https://fairsharing.org/FAIRsharing.Mkl9RR) 
20. **Source code reference**: if available, link to the source code of the ontology (URL_TO_INSERT_TERM_2938 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2939 https://fairsharing.org/FAIRsharing.Mkl9RR) 
4. **Overview of Widespread Ontology (URL_TO_INSERT_TERM_2940 https://fairsharing.org/search?recordType=terminology_artefact)  Lookup Service (URL_TO_INSERT_RECORD_2941 https://fairsharing.org/FAIRsharing.Mkl9RR) s**

---

Here, we have used the selection criteria above to provide an overview and comparison of four widespread ontology (URL_TO_INSERT_TERM_2942 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2943 https://fairsharing.org/FAIRsharing.Mkl9RR) s, namely:



-  [EBI Ontology Lookup Service](https://www.ebi.ac.uk/ols/index)
-  [BioPortal](https://bioportal.bioontology.org)
-  [OHDSI Athena](https://athena.ohdsi.org/search-terms/start)
-  [Ontobee and the OBO Foundry](http://www.ontobee.org)

The results of the analysis can be found below, else in tabular format (URL_TO_INSERT_TERM_2944 https://fairsharing.org/search?recordType=model_and_format)  [here](https://docs.google.com/spreadsheets/d/1kn1oEhsYJPiLI5gA12B1UsbLBRoSLGbOYcOMDG4614o/edit#gid=0).

Note, the _‘last update of this table_’ field provides the date on which the ontology (URL_TO_INSERT_TERM_2945 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD_2946 https://fairsharing.org/FAIRsharing.Mkl9RR)  was last assessed.

### **The EBI Ontology Lookup Service** {footcite}`pmid20460452`

<!-- **Overview by Francesco** -->


<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td>Ontology (URL_TO_INSERT_TERM_2947 https://fairsharing.org/search?recordType=terminology_artefact)  Lookup Service (URL_TO_INSERT_RECORD_2948 https://fairsharing.org/FAIRsharing.Mkl9RR) 
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
   <td><strong>URL</strong>
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/index (URL_TO_INSERT_RECORD_2949 https://fairsharing.org/FAIRsharing.Mkl9RR) ">https://www.ebi.ac.uk/ols/index (URL_TO_INSERT_RECORD_2950 https://fairsharing.org/FAIRsharing.Mkl9RR) </a>
   </td>
  </tr>
  <tr>
   <td><strong>Latest version of service / data / code (where applicable)</strong>
   </td>
   <td>Content: last update 12 Apr 2020 11:39
<p>
Code: Maven PO (URL_TO_INSERT_RECORD_2951 https://fairsharing.org/FAIRsharing.3ngg40) V version (from GitHub (URL_TO_INSERT_RECORD_2952 https://fairsharing.org/FAIRsharing.c55d5e) ): 3.2.1-SNAPSHOT
<p>
<a href="https://github.com (URL_TO_INSERT_RECORD_2953 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/OLS">https://github.com (URL_TO_INSERT_RECORD_2954 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/OLS</a>
<p>
Last commit on GitHub (URL_TO_INSERT_RECORD_2955 https://fairsharing.org/FAIRsharing.c55d5e) : April 2020
   </td>
  </tr>
  <tr>
   <td><strong>Host organisation</strong>
   </td>
   <td><a href="http://www.ebi.ac.uk/about/spot-team">Samples, Phenotypes and Ontologies (URL_TO_INSERT_TERM_2956 https://fairsharing.org/search?recordType=terminology_artefact)  Team</a> at EMBL-EBI
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
   <td>A repository (URL_TO_INSERT_TERM_2957 https://fairsharing.org/search?recordType=repository)  for biomedical ontologies (URL_TO_INSERT_TERM_2959 https://fairsharing.org/search?recordType=terminology_artefact)  that aims to provide a single point of access to the latest ontology (URL_TO_INSERT_TERM_2958 https://fairsharing.org/search?recordType=terminology_artefact)  versions
   </td>
  </tr>
  <tr>
   <td><strong>Set of ontologies (URL_TO_INSERT_TERM_2960 https://fairsharing.org/search?recordType=terminology_artefact)  covered</strong>
   </td>
   <td>245 ontologies (URL_TO_INSERT_TERM_2961 https://fairsharing.org/search?recordType=terminology_artefact)  / 6,119,228 terms / 27,778 properties / 485,541 individuals
<p>
Whole list at: <a href="https://www.ebi.ac.uk/ols/ontologies">https://www.ebi.ac.uk/ols/ontologies</a>
   </td>
  </tr>
  <tr>
   <td><strong>Onto. format (URL_TO_INSERT_TERM_2962 https://fairsharing.org/search?recordType=model_and_format) s supported</strong>
   </td>
   <td>OWL 2 and OBO (URL_TO_INSERT_RECORD_2963 https://fairsharing.org/FAIRsharing.847069) 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. importing capabilities</strong>
   </td>
   <td>By means of a local installation it is possible to import ontologies (URL_TO_INSERT_TERM_2965 https://fairsharing.org/search?recordType=terminology_artefact)  in OWL (URL_TO_INSERT_RECORD_2966 https://fairsharing.org/FAIRsharing.atygwy)  2 and OBO (URL_TO_INSERT_RECORD_2967 https://fairsharing.org/FAIRsharing.847069)  format (URL_TO_INSERT_TERM_2964 https://fairsharing.org/search?recordType=model_and_format) 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. browsing capabilities</strong>
   </td>
   <td>Tree-view based browsing of hierarch (URL_TO_INSERT_RECORD_2971 https://fairsharing.org/FAIRsharing.52b22c) ies of classes and properties of ontologies (URL_TO_INSERT_TERM_2970 https://fairsharing.org/search?recordType=terminology_artefact) . The modifications added by different version of each ontology (URL_TO_INSERT_TERM_2968 https://fairsharing.org/search?recordType=terminology_artefact)  are shown by means of distinct background colors in ontology (URL_TO_INSERT_TERM_2969 https://fairsharing.org/search?recordType=terminology_artefact)  browsing tree-views
   </td>
  </tr>
  <tr>
   <td><strong>Onto. search (URL_TO_INSERT_RECORD_2972 https://fairsharing.org/FAIRsharing.52b22c)  capabilities</strong>
   </td>
   <td>Search (URL_TO_INSERT_RECORD_2975 https://fairsharing.org/FAIRsharing.52b22c)  by term to gather all the ontologies (URL_TO_INSERT_TERM_2973 https://fairsharing.org/search?recordType=terminology_artefact)  where the term is found. It is possible to restrict search (URL_TO_INSERT_RECORD_2976 https://fairsharing.org/FAIRsharing.52b22c)  results to one or more ontologies (URL_TO_INSERT_TERM_2974 https://fairsharing.org/search?recordType=terminology_artefact) , to a specific type of result (i.e. class, property or individual) or to exact or partial term match
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
   <td>OLS updates nightly to always provide the latest ontology (URL_TO_INSERT_TERM_2977 https://fairsharing.org/search?recordType=terminology_artefact)  versions
   </td>
  </tr>
  <tr>
   <td><strong>Onto. versioning capabilities</strong>
   </td>
   <td>Obsoleted ontology (URL_TO_INSERT_TERM_2978 https://fairsharing.org/search?recordType=terminology_artefact)  terms are spotted by means of a boolean flag (is_obsolete)
   </td>
  </tr>
  <tr>
   <td><strong>Description of Web-based access to service</strong>
   </td>
   <td>Besides a Web-based user interface useful to browse ontologies (URL_TO_INSERT_TERM_2980 https://fairsharing.org/search?recordType=terminology_artefact)  and search (URL_TO_INSERT_RECORD_2981 https://fairsharing.org/FAIRsharing.52b22c)  for ontology (URL_TO_INSERT_TERM_2979 https://fairsharing.org/search?recordType=terminology_artefact)  concepts, free-access by means of a REST API is provided to the users
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
   <td><a href="https://github.com (URL_TO_INSERT_RECORD_2982 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/OLS">https://github.com (URL_TO_INSERT_RECORD_2983 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/OLS</a>
   </td>
  </tr>
  <tr>
   <td><strong>Quantification of community of users</strong>
   </td>
   <td>GitHub (URL_TO_INSERT_RECORD_2984 https://fairsharing.org/FAIRsharing.c55d5e) : 49 stars and 19 forks
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
   <td>Bioportal (URL_TO_INSERT_RECORD_2985 https://fairsharing.org/FAIRsharing.4m97ah)  
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
   <td><strong>URL</strong>
   </td>
   <td><a href="https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_2986 https://fairsharing.org/FAIRsharing.4m97ah) /">https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_2987 https://fairsharing.org/FAIRsharing.4m97ah) /</a>
   </td>
  </tr>
  <tr>
   <td><strong>Latest version of service / data / code (where applicable)</strong>
   </td>
   <td><em>Content</em>: last update 12 Apr 2020 11:39
<p>
<em>Code</em>: 
<ul>

<li>Web UI: <a href="https://github.com (URL_TO_INSERT_RECORD_2988 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/bioportal_web_ui">https://github.com (URL_TO_INSERT_RECORD_2989 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/bioportal_web_ui</a>

<li>REST API: <a href="https://github.com (URL_TO_INSERT_RECORD_2990 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_api">https://github.com (URL_TO_INSERT_RECORD_2991 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_api</a>

<li>Linked Data: <a href="https://github.com (URL_TO_INSERT_RECORD_2992 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_linked_data">https://github.com (URL_TO_INSERT_RECORD_2993 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_linked_data</a>

<p>
Latest commit on GitHub (URL_TO_INSERT_RECORD_2994 https://fairsharing.org/FAIRsharing.c55d5e) : April 2020
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td><strong>Host organisation</strong>
   </td>
   <td><a href="https://ncbo.bioontology.org/about-ncbo">U.S. National Center for Biomedical Ontology (URL_TO_INSERT_TERM_2995 https://fairsharing.org/search?recordType=terminology_artefact) </a>
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
   <td>Available at: <a href="https://github.com (URL_TO_INSERT_RECORD_2996 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_api/blob/master/LICENSE.txt">https://github.com (URL_TO_INSERT_RECORD_2997 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_api/blob/master/LICENSE.txt</a>
   </td>
  </tr>
  <tr>
   <td><strong>Domain</strong>
   </td>
   <td>A Web-based application for search (URL_TO_INSERT_RECORD_3002 https://fairsharing.org/FAIRsharing.52b22c) ing, sharing, visualizing, and analyzing a large repository (URL_TO_INSERT_TERM_2998 https://fairsharing.org/search?recordType=repository)  of biomedical ontologies (URL_TO_INSERT_TERM_3001 https://fairsharing.org/search?recordType=terminology_artefact) , terminologies (URL_TO_INSERT_TERM_2999 https://fairsharing.org/search?recordType=terminology_artefact) , and ontology (URL_TO_INSERT_TERM_3000 https://fairsharing.org/search?recordType=terminology_artefact) -based annotations
   </td>
  </tr>
  <tr>
   <td><strong>Set of ontologies (URL_TO_INSERT_TERM_3003 https://fairsharing.org/search?recordType=terminology_artefact)  covered</strong>
   </td>
   <td>Ontologies (URL_TO_INSERT_TERM_3004 https://fairsharing.org/search?recordType=terminology_artefact) : 842 / Classes: 11,324,508 
<p>
Whole list at: <a href="https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_3005 https://fairsharing.org/FAIRsharing.4m97ah) /ontologies">https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_3006 https://fairsharing.org/FAIRsharing.4m97ah) /ontologies</a>
   </td>
  </tr>
  <tr>
   <td><strong>Onto. format (URL_TO_INSERT_TERM_3007 https://fairsharing.org/search?recordType=model_and_format) s supported</strong>
   </td>
   <td>OWL, OBO (URL_TO_INSERT_RECORD_3008 https://fairsharing.org/FAIRsharing.847069) , SKOS (URL_TO_INSERT_RECORD_3009 https://fairsharing.org/FAIRsharing.48e326) 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. importing capabilities</strong>
   </td>
   <td>It is possible to upload / submit new ontologies (URL_TO_INSERT_TERM_3012 https://fairsharing.org/search?recordType=terminology_artefact)  or new versions of existing ontologies (URL_TO_INSERT_TERM_3013 https://fairsharing.org/search?recordType=terminology_artefact)  that will be indexed in BioPortal (URL_TO_INSERT_RECORD_3014 https://fairsharing.org/FAIRsharing.4m97ah) . Ontology (URL_TO_INSERT_TERM_3011 https://fairsharing.org/search?recordType=terminology_artefact)  metadata will be provided in the <a href="http://omv.ontoware.org">Ontology Metadata Vocabulary</a> (OMV) format (URL_TO_INSERT_TERM_3010 https://fairsharing.org/search?recordType=model_and_format) 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. browsing capabilities</strong>
   </td>
   <td>For each ontology (URL_TO_INSERT_TERM_3017 https://fairsharing.org/search?recordType=terminology_artefact)  / terminology (URL_TO_INSERT_TERM_3015 https://fairsharing.org/search?recordType=terminology_artefact)  an overview of its content is provided together with separate tree-views tailored to explore its hierarch (URL_TO_INSERT_RECORD_3020 https://fairsharing.org/FAIRsharing.52b22c) ies of classes and properties. The set of available map (URL_TO_INSERT_RECORD_3019 https://fairsharing.org/FAIRsharing.53edcc) pings to other ontologies (URL_TO_INSERT_TERM_3018 https://fairsharing.org/search?recordType=terminology_artefact)  / terminologies (URL_TO_INSERT_TERM_3016 https://fairsharing.org/search?recordType=terminology_artefact)  can be explored by a custom view
   </td>
  </tr>
  <tr>
   <td><strong>Onto. search (URL_TO_INSERT_RECORD_3021 https://fairsharing.org/FAIRsharing.52b22c)  capabilities</strong>
   </td>
   <td>Search (URL_TO_INSERT_RECORD_3024 https://fairsharing.org/FAIRsharing.52b22c)  by term to gather all the ontologies (URL_TO_INSERT_TERM_3022 https://fairsharing.org/search?recordType=terminology_artefact)  where the term is found. It is possible to restrict search (URL_TO_INSERT_RECORD_3025 https://fairsharing.org/FAIRsharing.52b22c)  results to one or more ontologies (URL_TO_INSERT_TERM_3023 https://fairsharing.org/search?recordType=terminology_artefact) , to a specific type of result (i.e. class, property or individual) or to exact or partial term match
   </td>
  </tr>
  <tr>
   <td><strong>Onto. recommendation capabilities</strong>
   </td>
   <td>An ontology (URL_TO_INSERT_TERM_3026 https://fairsharing.org/search?recordType=terminology_artefact)  recommender is available: it retrieves recommendations for the most relevant ontologies (URL_TO_INSERT_TERM_3027 https://fairsharing.org/search?recordType=terminology_artefact)  based on an excerpt from a biomedical text or a list of keywords.
<p>
Recommendations are based on: (i) <em>coverage</em> of the input text / set of keywords; (ii) <em>acceptance</em> of the ontologies (URL_TO_INSERT_TERM_3030 https://fairsharing.org/search?recordType=terminology_artefact) ; (iii) <em>detail of knowledge</em> available in the ontology (URL_TO_INSERT_TERM_3028 https://fairsharing.org/search?recordType=terminology_artefact)  to describe input data and (iv) <em>specialization</em> of the ontology (URL_TO_INSERT_TERM_3029 https://fairsharing.org/search?recordType=terminology_artefact)  to the specific domain under consideration
   </td>
  </tr>
  <tr>
   <td><strong>Onto. update capabilities</strong>
   </td>
   <td>Each ontology (URL_TO_INSERT_TERM_3031 https://fairsharing.org/search?recordType=terminology_artefact)  can be manually updated by accessing the BioPortal (URL_TO_INSERT_RECORD_3033 https://fairsharing.org/FAIRsharing.4m97ah)  or automatically updated by BioPortal (URL_TO_INSERT_RECORD_3034 https://fairsharing.org/FAIRsharing.4m97ah)  by continuously monitoring a URL (URL_TO_INSERT_RECORD_3035 https://fairsharing.org/FAIRsharing.9d38e2)  where the ontology (URL_TO_INSERT_TERM_3032 https://fairsharing.org/search?recordType=terminology_artefact)  and its new versions are published
   </td>
  </tr>
  <tr>
   <td><strong>Onto. versioning capabilities</strong>
   </td>
   <td>Each ontology (URL_TO_INSERT_TERM_3036 https://fairsharing.org/search?recordType=terminology_artefact)  is characterized by a version number in its metadata, useful to track distinct versions of the same ontology (URL_TO_INSERT_TERM_3037 https://fairsharing.org/search?recordType=terminology_artefact) 
   </td>
  </tr>
  <tr>
   <td><strong>Description of Web based access to service</strong>
   </td>
   <td>Besides a Web-based interface that supports ontology (URL_TO_INSERT_TERM_3038 https://fairsharing.org/search?recordType=terminology_artefact)  search (URL_TO_INSERT_RECORD_3040 https://fairsharing.org/FAIRsharing.52b22c) , annotation, recommendation and map (URL_TO_INSERT_RECORD_3039 https://fairsharing.org/FAIRsharing.53edcc) ping, also a free-after-registration access by means of a REST API is provided to the users
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
   <td>Sample code to access REST API in distinct languages is available at: <a href="https://github.com (URL_TO_INSERT_RECORD_3041 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ncbo_rest_sample_code">https://github.com (URL_TO_INSERT_RECORD_3042 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ncbo_rest_sample_code</a>
   </td>
  </tr>
  <tr>
   <td><strong>Local deploy of service</strong>
   </td>
   <td>In principle, local deploy of services is possible, even if not extensively documented. Source code (Rails) for Web UI, REST API and Linked Data management is available on NCBO GiHub account, <a href="https://github.com (URL_TO_INSERT_RECORD_3043 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo">https://github.com (URL_TO_INSERT_RECORD_3044 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo</a>
   </td>
  </tr>
  <tr>
   <td><strong>Source code reference</strong>
   </td>
   <td><a href="https://github.com (URL_TO_INSERT_RECORD_3045 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo">https://github.com (URL_TO_INSERT_RECORD_3046 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo</a>
   </td>
  </tr>
  <tr>
   <td><strong>Quantification of community of users</strong>
   </td>
   <td>GitHub (URL_TO_INSERT_RECORD_3047 https://fairsharing.org/FAIRsharing.c55d5e) : 
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
   <td><strong>URL</strong>
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
<em>Code</em>: Maven PO (URL_TO_INSERT_RECORD_3048 https://fairsharing.org/FAIRsharing.3ngg40) V version (from GitHub (URL_TO_INSERT_RECORD_3049 https://fairsharing.org/FAIRsharing.c55d5e) ): 1.10.0
<p>
<a href="https://github.com (URL_TO_INSERT_RECORD_3050 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena">https://github.com (URL_TO_INSERT_RECORD_3051 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena</a>
<p>
Latest commit on GitHub (URL_TO_INSERT_RECORD_3052 https://fairsharing.org/FAIRsharing.c55d5e) : September 2019
   </td>
  </tr>
  <tr>
   <td><strong>Host organisation</strong>
   </td>
   <td><a href="https://www.ohdsi.org/">Observational Health Data Sciences and Informat (URL_TO_INSERT_TERM_3053 https://fairsharing.org/search?recordType=model_and_format) ics (OHDSI) initiative</a>
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
   <td>Useful to browse the set of Standard (URL_TO_INSERT_TERM_3054 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabularies which are part of the OMOP Common Data Model (URL_TO_INSERT_TERM_3055 https://fairsharing.org/search?recordType=model_and_format)  (CDM), version 5.x. They are maintained by the Observational Health Data Science and Informat (URL_TO_INSERT_TERM_3056 https://fairsharing.org/search?recordType=model_and_format) ics (OHDSI, pronounced “Odyssey”) initiative
   </td>
  </tr>
  <tr>
   <td><strong>Set of ontologies (URL_TO_INSERT_TERM_3057 https://fairsharing.org/search?recordType=terminology_artefact)  covered</strong>
   </td>
   <td>Standard (URL_TO_INSERT_TERM_3058 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabularies which are part of the<a href="https://www.ohdsi.org/web/wiki/doku.php?id=documentation:vocabulary_etl"> OMOP Common Data Model (URL_TO_INSERT_TERM_3059 https://fairsharing.org/search?recordType=model_and_format)  (CDM)</a>, version 5.x. It integrates several source vocabularies including UMLS, SNOMED, RxNorm (URL_TO_INSERT_RECORD_3061 https://fairsharing.org/FAIRsharing.36pf8q) , NDF (URL_TO_INSERT_RECORD_3060 https://fairsharing.org/FAIRsharing.cfcd4r) RT (URL_TO_INSERT_RECORD_3062 https://fairsharing.org/FAIRsharing.901nkj) , VA Product, VA Class, ATC (URL_TO_INSERT_RECORD_3063 https://fairsharing.org/FAIRsharing.1a27h8) , MeSH, ICD10, GCN_SEQNO, ETC, Indication, ICD9CM, ICD9Proc, ICD10CM, LOiNC, etc.
   </td>
  </tr>
  <tr>
   <td><strong>Onto. format (URL_TO_INSERT_TERM_3064 https://fairsharing.org/search?recordType=model_and_format) s supported</strong>
   </td>
   <td>Not a specific format (URL_TO_INSERT_TERM_3066 https://fairsharing.org/search?recordType=model_and_format) , a collection (URL_TO_INSERT_TERM_3065 https://fairsharing.org/search?recordType=collection)  of ontology (URL_TO_INSERT_TERM_3067 https://fairsharing.org/search?recordType=terminology_artefact)  concepts / classes assigned to a specific domain and imported from a specific source vocabulary 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. importing capabilities</strong>
   </td>
   <td>Tailored to browse the Standard (URL_TO_INSERT_TERM_3068 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabularies which are part of the OMOP Common Data Model (URL_TO_INSERT_TERM_3069 https://fairsharing.org/search?recordType=model_and_format)  (CDM)
   </td>
  </tr>
  <tr>
   <td><strong>Onto. browsing capabilities</strong>
   </td>
   <td>Table based views are available to browse all the concepts belonging to a specific source vocabulary 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. search (URL_TO_INSERT_RECORD_3070 https://fairsharing.org/FAIRsharing.52b22c)  capabilities</strong>
   </td>
   <td>Search (URL_TO_INSERT_RECORD_3071 https://fairsharing.org/FAIRsharing.52b22c)  by term to gather all the source vocabularies where the term is found. It is possible to restrict search (URL_TO_INSERT_RECORD_3072 https://fairsharing.org/FAIRsharing.52b22c)  results by domain, class and source vocabulary
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
   <td>Each time a new version of the Standard (URL_TO_INSERT_TERM_3073 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabularies which are part of the OMOP Common Data Model (URL_TO_INSERT_TERM_3074 https://fairsharing.org/search?recordType=model_and_format)  (CDM) is available an updated the core (URL_TO_INSERT_RECORD_3075 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_3076 https://fairsharing.org/FAIRsharing.xMmOCL)  set of concept is available
   </td>
  </tr>
  <tr>
   <td><strong>Onto. versioning capabilities</strong>
   </td>
   <td>The latest version of the Standard (URL_TO_INSERT_TERM_3077 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabulary is V5.0
   </td>
  </tr>
  <tr>
   <td><strong>Description of Web-based access to service</strong>
   </td>
   <td>Athena is a Web interface available to browse concepts of the Standard (URL_TO_INSERT_TERM_3078 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabulary (V5.0). Both search (URL_TO_INSERT_RECORD_3079 https://fairsharing.org/FAIRsharing.52b22c)  results and the whole dataset can be downloaded after registration
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
   <td>In principle, local deploy of services is possible, even if not extensively documented. Source code on GitHub (URL_TO_INSERT_RECORD_3080 https://fairsharing.org/FAIRsharing.c55d5e)  account <a href="https://github.com (URL_TO_INSERT_RECORD_3081 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena">https://github.com (URL_TO_INSERT_RECORD_3082 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena</a> 
   </td>
  </tr>
  <tr>
   <td><strong>Source code reference</strong>
   </td>
   <td><a href="https://github.com (URL_TO_INSERT_RECORD_3083 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena">https://github.com (URL_TO_INSERT_RECORD_3084 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena</a>
   </td>
  </tr>
  <tr>
   <td><strong>Quantification of community of users</strong>
   </td>
   <td>GitHub (URL_TO_INSERT_RECORD_3085 https://fairsharing.org/FAIRsharing.c55d5e) : 29 stars and 6 forks
<p>
Twitter: 1.284 followers of the Observational Health Data Sciences and Informat (URL_TO_INSERT_TERM_3086 https://fairsharing.org/search?recordType=model_and_format) ics (OHDSI) account
   </td>
  </tr>
</table>


### **Ontobee and the OBO Foundry** {footcite}`pmid27733503ontobee`

<!-- **Overview by Francesco** -->



<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td>OBO Foundry (URL_TO_INSERT_RECORD_3087 https://fairsharing.org/FAIRsharing.847069) 
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
   <td><strong>URL</strong>
   </td>
   <td><a href="http://www.ontobee.org (URL_TO_INSERT_RECORD_3088 https://fairsharing.org/FAIRsharing.q8fx1b) /">http://www.ontobee.org (URL_TO_INSERT_RECORD_3089 https://fairsharing.org/FAIRsharing.q8fx1b) /</a> (<a href="http://obofoundry.org/">http://obofoundry.org/</a>)
   </td>
  </tr>
  <tr>
   <td><strong>Latest version of service / data / code (where applicable)</strong>
   </td>
   <td><em>Content (OBO Foundry (URL_TO_INSERT_RECORD_3090 https://fairsharing.org/FAIRsharing.847069) )</em>: last update April 2020
<p>
<em>Code (Ontobee (URL_TO_INSERT_RECORD_3091 https://fairsharing.org/FAIRsharing.q8fx1b) )</em>: <a href="https://github.com (URL_TO_INSERT_RECORD_3092 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee">https://github.com (URL_TO_INSERT_RECORD_3093 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee</a>
<p>
Latest commit on GitHub (URL_TO_INSERT_RECORD_3094 https://fairsharing.org/FAIRsharing.c55d5e) : August 2018
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
   <td>Ontobee (URL_TO_INSERT_RECORD_3101 https://fairsharing.org/FAIRsharing.q8fx1b)  has been used as the default ontology (URL_TO_INSERT_TERM_3095 https://fairsharing.org/search?recordType=terminology_artefact)  Linked Data server for most <a href="http://obofoundry.org/">Open Biological and Biomedical Ontology (URL_TO_INSERT_TERM_3096 https://fairsharing.org/search?recordType=terminology_artefact)  (OBO) Foundry</a> library ontologies (URL_TO_INSERT_TERM_3098 https://fairsharing.org/search?recordType=terminology_artefact) . The OBO (URL_TO_INSERT_RECORD_3100 https://fairsharing.org/FAIRsharing.847069)  Foundry (URL_TO_INSERT_RECORD_3099 https://fairsharing.org/FAIRsharing.847069)  is a collective of ontology (URL_TO_INSERT_TERM_3097 https://fairsharing.org/search?recordType=terminology_artefact)  developers that are committed to collaboration and adherence to shared principles
   </td>
  </tr>
  <tr>
   <td><strong>Set of ontologies (URL_TO_INSERT_TERM_3102 https://fairsharing.org/search?recordType=terminology_artefact)  covered</strong>
   </td>
   <td>164 active ontologies (URL_TO_INSERT_TERM_3103 https://fairsharing.org/search?recordType=terminology_artefact) , 5 orphaned ontologies (URL_TO_INSERT_TERM_3104 https://fairsharing.org/search?recordType=terminology_artefact)  and 57 inactive ontologies (URL_TO_INSERT_TERM_3105 https://fairsharing.org/search?recordType=terminology_artefact)  (in OBO (URL_TO_INSERT_RECORD_3107 https://fairsharing.org/FAIRsharing.847069)  Foundry (URL_TO_INSERT_RECORD_3106 https://fairsharing.org/FAIRsharing.847069) )
   </td>
  </tr>
  <tr>
   <td><strong>Onto. format (URL_TO_INSERT_TERM_3108 https://fairsharing.org/search?recordType=model_and_format) s supported</strong>
   </td>
   <td>OWL and OBO (URL_TO_INSERT_RECORD_3109 https://fairsharing.org/FAIRsharing.847069) 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. importing capabilities</strong>
   </td>
   <td>Ontobee (URL_TO_INSERT_RECORD_3120 https://fairsharing.org/FAIRsharing.q8fx1b)  can import both OWL (URL_TO_INSERT_RECORD_3114 https://fairsharing.org/FAIRsharing.atygwy)  and OBO (URL_TO_INSERT_RECORD_3117 https://fairsharing.org/FAIRsharing.847069)  ontologies (URL_TO_INSERT_TERM_3111 https://fairsharing.org/search?recordType=terminology_artefact) . New ontologies (URL_TO_INSERT_TERM_3112 https://fairsharing.org/search?recordType=terminology_artefact)  can be proposed tired to the set of OBO (URL_TO_INSERT_RECORD_3118 https://fairsharing.org/FAIRsharing.847069)  Foundry (URL_TO_INSERT_RECORD_3115 https://fairsharing.org/FAIRsharing.847069)  ontologies (URL_TO_INSERT_TERM_3113 https://fairsharing.org/search?recordType=terminology_artefact) ; a committee will review the ontology (URL_TO_INSERT_TERM_3110 https://fairsharing.org/search?recordType=terminology_artefact)  to check if it adheres to all the OBO (URL_TO_INSERT_RECORD_3119 https://fairsharing.org/FAIRsharing.847069)  Foundry (URL_TO_INSERT_RECORD_3116 https://fairsharing.org/FAIRsharing.847069)  principles
   </td>
  </tr>
  <tr>
   <td><strong>Onto. browsing capabilities</strong>
   </td>
   <td>The OBO (URL_TO_INSERT_RECORD_3129 https://fairsharing.org/FAIRsharing.847069)  Foundry (URL_TO_INSERT_RECORD_3127 https://fairsharing.org/FAIRsharing.847069)  portal provides a set of metadata describing each ontology (URL_TO_INSERT_TERM_3122 https://fairsharing.org/search?recordType=terminology_artefact)  together with the possibility to download the same ontology (URL_TO_INSERT_TERM_3123 https://fairsharing.org/search?recordType=terminology_artefact)  in several format (URL_TO_INSERT_TERM_3121 https://fairsharing.org/search?recordType=model_and_format) s. To browse ontologies (URL_TO_INSERT_TERM_3125 https://fairsharing.org/search?recordType=terminology_artefact) , the OBO (URL_TO_INSERT_RECORD_3130 https://fairsharing.org/FAIRsharing.847069)  Foundry (URL_TO_INSERT_RECORD_3128 https://fairsharing.org/FAIRsharing.847069)  portal points to the ontology (URL_TO_INSERT_TERM_3124 https://fairsharing.org/search?recordType=terminology_artefact)  browsing pages of other Web platforms including <a href="http://www.ontobee.org (URL_TO_INSERT_RECORD_3131 https://fairsharing.org/FAIRsharing.q8fx1b) /">Ontobee</a>, <a href="https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_3126 https://fairsharing.org/FAIRsharing.4m97ah) /">BioPortal</a> and the <a href="https://www.ebi.ac.uk/ols">Ontology Lookup Service</a>.
   </td>
  </tr>
  <tr>
   <td><strong>Onto. search (URL_TO_INSERT_RECORD_3132 https://fairsharing.org/FAIRsharing.52b22c)  capabilities</strong>
   </td>
   <td>The OBO (URL_TO_INSERT_RECORD_3137 https://fairsharing.org/FAIRsharing.847069)  Foundry (URL_TO_INSERT_RECORD_3136 https://fairsharing.org/FAIRsharing.847069)  portal exploits <a href="http://www.ontobee.org (URL_TO_INSERT_RECORD_3139 https://fairsharing.org/FAIRsharing.q8fx1b) /">Ontobee</a> to provide users with ontology (URL_TO_INSERT_TERM_3133 https://fairsharing.org/search?recordType=terminology_artefact)  search (URL_TO_INSERT_RECORD_3140 https://fairsharing.org/FAIRsharing.52b22c)  capabilities.Ontobee (URL_TO_INSERT_RECORD_3138 https://fairsharing.org/FAIRsharing.q8fx1b)  enables users to search (URL_TO_INSERT_RECORD_3141 https://fairsharing.org/FAIRsharing.52b22c)  ontology (URL_TO_INSERT_TERM_3134 https://fairsharing.org/search?recordType=terminology_artefact)  concepts by term, eventually restricting the search (URL_TO_INSERT_RECORD_3142 https://fairsharing.org/FAIRsharing.52b22c)  to a specific ontology (URL_TO_INSERT_TERM_3135 https://fairsharing.org/search?recordType=terminology_artefact) 
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
   <td>An established <a href="http://obofoundry.org/principles/fp-004-versioning.html">PURL system to publish new versions / updates of an ontology (URL_TO_INSERT_TERM_3144 https://fairsharing.org/search?recordType=terminology_artefact) </a> is defined; new versions of an ontologies (URL_TO_INSERT_TERM_3145 https://fairsharing.org/search?recordType=terminology_artefact)  should be accessible at PURL (URL_TO_INSERT_RECORD_3146 https://fairsharing.org/FAIRsharing.3e603c) s with the following format (URL_TO_INSERT_TERM_3143 https://fairsharing.org/search?recordType=model_and_format) : <code>http://purl.obolibrary.org/obo/idspace/YYYY-MM-DD/idspace.owl</code> or <code>.obo</code>, for instance: <code><a href="https://raw.githubusercontent.com/BiodiversityOntologies/bco/2020-03-27/bco.owl">https://raw.githubusercontent.com/BiodiversityOntologies/bco/2020-03-27/bco.owl</a></code>
   </td>
  </tr>
  <tr>
   <td><strong>Onto. versioning capabilities</strong>
   </td>
   <td>The OBO (URL_TO_INSERT_RECORD_3151 https://fairsharing.org/FAIRsharing.847069)  principles, implemented by the ontologies (URL_TO_INSERT_TERM_3148 https://fairsharing.org/search?recordType=terminology_artefact)  available in OBO (URL_TO_INSERT_RECORD_3152 https://fairsharing.org/FAIRsharing.847069)  Foundry (URL_TO_INSERT_RECORD_3150 https://fairsharing.org/FAIRsharing.847069) , enforces a system of versioning systems, with each ontology (URL_TO_INSERT_TERM_3147 https://fairsharing.org/search?recordType=terminology_artefact)  version receiving an unique identifier (URL_TO_INSERT_TERM_3149 https://fairsharing.org/search?recordType=identifier_schema)  (by means of numbers, dates, tags)
   </td>
  </tr>
  <tr>
   <td><strong>Description of Web-based access to service</strong>
   </td>
   <td>Ontobee (URL_TO_INSERT_RECORD_3154 https://fairsharing.org/FAIRsharing.q8fx1b)  provides a web interface that supports, besides search (URL_TO_INSERT_RECORD_3156 https://fairsharing.org/FAIRsharing.52b22c) ing for ontology (URL_TO_INSERT_TERM_3153 https://fairsharing.org/search?recordType=terminology_artefact)  concepts, the execution of SP (URL_TO_INSERT_RECORD_3157 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_3155 https://fairsharing.org/FAIRsharing.87ccfd)  queries and the annotation of text excerpts
   </td>
  </tr>
  <tr>
   <td><strong>Description of API</strong>
   </td>
   <td>No specific REST API is provided; users can retrieve both HTML (URL_TO_INSERT_RECORD_3161 https://fairsharing.org/FAIRsharing.YugnuL)  and RDF (URL_TO_INSERT_RECORD_3159 https://fairsharing.org/FAIRsharing.p77ph9)  descriptions of concepts that belongs to Ontobee (URL_TO_INSERT_RECORD_3160 https://fairsharing.org/FAIRsharing.q8fx1b)  ontologies (URL_TO_INSERT_TERM_3158 https://fairsharing.org/search?recordType=terminology_artefact) , in adherence to the principles of Linked Data community
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
   <td>In principle, local deploy of services is possible, even if not extensively documented. Source code on GiHub account <a href="https://github.com (URL_TO_INSERT_RECORD_3162 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee">https://github.com (URL_TO_INSERT_RECORD_3163 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee</a>
   </td>
  </tr>
  <tr>
   <td><strong>Source code reference</strong>
   </td>
   <td><a href="https://github.com (URL_TO_INSERT_RECORD_3164 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee">https://github.com (URL_TO_INSERT_RECORD_3165 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee</a>
   </td>
  </tr>
  <tr>
   <td><strong>Quantification of community of users</strong>
   </td>
   <td>GitHub (URL_TO_INSERT_RECORD_3166 https://fairsharing.org/FAIRsharing.c55d5e) : 12 stars and 4 forks
<p>
Twitter OBO (URL_TO_INSERT_RECORD_3167 https://fairsharing.org/FAIRsharing.847069) Foundry account: 220 followers
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
