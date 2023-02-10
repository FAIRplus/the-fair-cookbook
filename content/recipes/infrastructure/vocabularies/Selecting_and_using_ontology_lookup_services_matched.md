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

This recipe provides **guidance on the selection and exploitation of ontology (URL_TO_INSERT_TERM_2089 https://fairsharing.org/search?recordType=terminology_artefact)  lookup services** . 

>* **[Objective of the recipe: introduction to ontology lookup services](#heading=h.bb3h294tvdau)**
>
>* **[Selecting an ontology lookup service](#bookmark=id.okwm6u2vsbft)**
>
>* **[Overview of widespread ontology lookup services](#bookmark=id.x42hawpkzgd3)**

An ***ontology (URL_TO_INSERT_TERM_2090 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2091 https://fairsharing.org/FAIRsharing.Mkl9RR) *** 
refers to *any type of application, standalone or Web-based, that enables the use of existing ontologies (URL_TO_INSERT_TERM_2092 https://fairsharing.org/search?recordType=terminology_artefact)  to support knowledge 
formalization and sharing, by fostering ontology (URL_TO_INSERT_TERM_2093 https://fairsharing.org/search?recordType=terminology_artefact) -based descriptions of knowledge*. 




Tools useful to build, edit or maintain ontologies (URL_TO_INSERT_TERM_2095 https://fairsharing.org/search?recordType=terminology_artefact)  are not considered ontology (URL_TO_INSERT_TERM_2094 https://fairsharing.org/search?recordType=terminology_artefact)  lookup services and thus are out of the scope of this recipe. 

In essence, an ontology (URL_TO_INSERT_TERM_2096 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2097 https://fairsharing.org/FAIRsharing.Mkl9RR)  is a platform that provides users with the possibility to **search in a set of
ontologies (URL_TO_INSERT_TERM_2098 https://fairsharing.org/search?recordType=terminology_artefact) , the most suitable concepts to describe the semantics of a piece of knowledge of interest,
usually available in the form of one or more keywords or a text excerpt**. 

Most ontology (URL_TO_INSERT_TERM_2099 https://fairsharing.org/search?recordType=terminology_artefact)  lookup services are available as Web applications: most of them also support programmatic access to their 
capabilities by means of (REST) APIs. Ontology (URL_TO_INSERT_TERM_2100 https://fairsharing.org/search?recordType=terminology_artefact)  lookup services can vary in the features that are provided, but often include:



* **Complex searching for concepts of interest**: most services implement advanced search features (i.e. scoping the search to specific ontologies (URL_TO_INSERT_TERM_2102 https://fairsharing.org/search?recordType=terminology_artefact)  or to specific parts of an ontology (URL_TO_INSERT_TERM_2101 https://fairsharing.org/search?recordType=terminology_artefact) ) or allow users to specify fine-grained patterns to aggregate or restrict the scope of search results.
* **Advanced browsing capabilities**, to explore the contents of a specific ontology (URL_TO_INSERT_TERM_2103 https://fairsharing.org/search?recordType=terminology_artefact)  by means of custom data navigation widgets such as tree-based views.
* **Managing distinct versions** of an ontology (URL_TO_INSERT_TERM_2104 https://fairsharing.org/search?recordType=terminology_artefact)  and alert its users when specific concepts become obsolete. 
* **Importing** user-provided ontologies (URL_TO_INSERT_TERM_2106 https://fairsharing.org/search?recordType=terminology_artefact) , giving consumers the ability to leverage a service for other terminologies (URL_TO_INSERT_TERM_2105 https://fairsharing.org/search?recordType=terminology_artefact)  beyond those included.
* Programmatic means to **access and deploy instances of the ontology (URL_TO_INSERT_TERM_2107 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2108 https://fairsharing.org/FAIRsharing.Mkl9RR)  in the premises of its users** represents another differentiating feature, using relevant documentation.
* **Recommending ontologies (URL_TO_INSERT_TERM_2109 https://fairsharing.org/search?recordType=terminology_artefact) ** based on the input of a given term, with ontologies (URL_TO_INSERT_TERM_2110 https://fairsharing.org/search?recordType=terminology_artefact)  ranked according to custom-weighted criteria.
* Access to an **active user community** that supports and exploits a specific ontology (URL_TO_INSERT_TERM_2111 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2112 https://fairsharing.org/FAIRsharing.Mkl9RR) , serving as an indication of widespread adoption and selection.

This recipe presents guideline (URL_TO_INSERT_TERM_2114 https://fairsharing.org/search?recordType=reporting_guideline) s and relevant considerations when choosing an ontology (URL_TO_INSERT_TERM_2113 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2115 https://fairsharing.org/FAIRsharing.Mkl9RR) , followed by
overview of existing public ontology (URL_TO_INSERT_TERM_2116 https://fairsharing.org/search?recordType=terminology_artefact)  lookup services and a comparison of their core (URL_TO_INSERT_RECORD-NAME_2117 https://fairsharing.org/FAIRsharing.xMmOCL)  (URL_TO_INSERT_RECORD-ABBREV_2118 https://fairsharing.org/FAIRsharing.m283c)  features.


## Selecting An Ontology Lookup Service

This section provides guideline (URL_TO_INSERT_TERM_2120 https://fairsharing.org/search?recordType=reporting_guideline) s and suggestions on how to select and leverage an ontology (URL_TO_INSERT_TERM_2119 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2121 https://fairsharing.org/FAIRsharing.Mkl9RR) , on the basis
of the knowledge needs and ontology (URL_TO_INSERT_TERM_2123 https://fairsharing.org/search?recordType=terminology_artefact)  use patterns that characterize a specific knowledge-intensive project (URL_TO_INSERT_TERM_2122 https://fairsharing.org/search?recordType=project) . 

Several aspects to consider when choosing an ontology (URL_TO_INSERT_TERM_2124 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2125 https://fairsharing.org/FAIRsharing.Mkl9RR)  are derived based on a series of commonly asked questions;



* **Is the set of ontologies (URL_TO_INSERT_TERM_2128 https://fairsharing.org/search?recordType=terminology_artefact)  incorporated in the ontology (URL_TO_INSERT_TERM_2127 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2129 https://fairsharing.org/FAIRsharing.Mkl9RR)  suitable to formally describe the knowledge domain my project (URL_TO_INSERT_TERM_2126 https://fairsharing.org/search?recordType=project)  is interested in?**

    Ontology (URL_TO_INSERT_TERM_2130 https://fairsharing.org/search?recordType=terminology_artefact)  lookup services usually provide access and enable users to search and reference classes and properties of _a specific set of ontologies (URL_TO_INSERT_TERM_2131 https://fairsharing.org/search?recordType=terminology_artefact)  related to a specific knowledge domain_ (i.e. biomedical knowledge).
    When choosing an ontology (URL_TO_INSERT_TERM_2133 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2135 https://fairsharing.org/FAIRsharing.Mkl9RR)  it is important to verify whether the ontologies (URL_TO_INSERT_TERM_2134 https://fairsharing.org/search?recordType=terminology_artefact)  covered by a specific service are suitable to describe the content of our knowledge-intensive project (URL_TO_INSERT_TERM_2132 https://fairsharing.org/search?recordType=project) . 
    Besides, a list of the ontologies (URL_TO_INSERT_TERM_2136 https://fairsharing.org/search?recordType=terminology_artefact)  covered, and interactive widgets to explore such ontologies (URL_TO_INSERT_TERM_2137 https://fairsharing.org/search?recordType=terminology_artefact)  (e.g. tree-based views), 
    some ontology (URL_TO_INSERT_TERM_2138 https://fairsharing.org/search?recordType=terminology_artefact)  lookup services also provide _ontology (URL_TO_INSERT_TERM_2139 https://fairsharing.org/search?recordType=terminology_artefact)  recommendation capabilities:_ given some “sample” 
    (i.e. text excerpt or list of keywords) of the knowledge we need to describe by means of available ontologies (URL_TO_INSERT_TERM_2140 https://fairsharing.org/search?recordType=terminology_artefact) , 
    the ontology (URL_TO_INSERT_TERM_2141 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2143 https://fairsharing.org/FAIRsharing.Mkl9RR)  ‘recommender’ suggests which are the best ontologies (URL_TO_INSERT_TERM_2142 https://fairsharing.org/search?recordType=terminology_artefact)  to use to this propose.

* **Do I need to consider / rely on private ontologies (URL_TO_INSERT_TERM_2145 https://fairsharing.org/search?recordType=terminology_artefact)  in my project (URL_TO_INSERT_TERM_2144 https://fairsharing.org/search?recordType=project) ? Do I need to use ontologies (URL_TO_INSERT_TERM_2146 https://fairsharing.org/search?recordType=terminology_artefact)  that are not already 
    imported and thus available in the ontology (URL_TO_INSERT_TERM_2147 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2148 https://fairsharing.org/FAIRsharing.Mkl9RR)  of my choice?**

    Some ontology (URL_TO_INSERT_TERM_2149 https://fairsharing.org/search?recordType=terminology_artefact)  lookup services enable users to import external (i.e. user-provided) ontologies (URL_TO_INSERT_TERM_2150 https://fairsharing.org/search?recordType=terminology_artefact)  in order to incorporate
    the content of these ontologies (URL_TO_INSERT_TERM_2151 https://fairsharing.org/search?recordType=terminology_artefact)  in their search and recommendation capabilities. 
    This feature could represent a key factor to consider when choosing an ontology (URL_TO_INSERT_TERM_2152 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2153 https://fairsharing.org/FAIRsharing.Mkl9RR)  since several 
    knowledge-intensive project (URL_TO_INSERT_TERM_2154 https://fairsharing.org/search?recordType=project) s rely on private ontologies (URL_TO_INSERT_TERM_2155 https://fairsharing.org/search?recordType=terminology_artefact)  or need to consider a set of additional ontologies (URL_TO_INSERT_TERM_2156 https://fairsharing.org/search?recordType=terminology_artefact)  not 
    natively covered by a specific ontology (URL_TO_INSERT_TERM_2157 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2158 https://fairsharing.org/FAIRsharing.Mkl9RR) .

* **Because of data privacy or data protection issues, do I need to use an instance of the ontology (URL_TO_INSERT_TERM_2159 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2160 https://fairsharing.org/FAIRsharing.Mkl9RR)  that
is deployed locally on my private computing infrastructure?**

    Several ontology (URL_TO_INSERT_TERM_2161 https://fairsharing.org/search?recordType=terminology_artefact) -lookup services provide the possibility to deploy the service on the private computing 
    infrastructure of its users. This feature would be particularly relevant when private ontologies (URL_TO_INSERT_TERM_2162 https://fairsharing.org/search?recordType=terminology_artefact)  are adopted in a 
    knowledge-intensive project (URL_TO_INSERT_TERM_2163 https://fairsharing.org/search?recordType=project) .

* **Which are the usage patterns I will rely on in order to exploit the ontology (URL_TO_INSERT_TERM_2164 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2165 https://fairsharing.org/FAIRsharing.Mkl9RR) ? Will the 1)
massive and systematic exploitation of the ontology (URL_TO_INSERT_TERM_2166 https://fairsharing.org/search?recordType=terminology_artefact)  search, 2) the recommendation features of the ontology (URL_TO_INSERT_TERM_2167 https://fairsharing.org/search?recordType=terminology_artefact)  lookup
service or 3) the integration of its capabilities in more complex systems, require the possibility to programmatically 
access the service by means of an application programming interface (API)?**

    Ontology (URL_TO_INSERT_TERM_2168 https://fairsharing.org/search?recordType=terminology_artefact)  lookup services usually provide a (Web-based) user interface as the preferred way to interact with them to
    browse and search for ontologies (URL_TO_INSERT_TERM_2169 https://fairsharing.org/search?recordType=terminology_artefact) , or recommend relevant concepts to describe contents of interest. 
    In several scenarios, the possibility to programmatically interact with ontology (URL_TO_INSERT_TERM_2170 https://fairsharing.org/search?recordType=terminology_artefact)  lookup services would be extremely
    valuable; to this purpose, several ontology (URL_TO_INSERT_TERM_2171 https://fairsharing.org/search?recordType=terminology_artefact) -lookup services implement an API (mostly based on REST interactions)
    that enable the user to programmatically invoke the majority of ontology (URL_TO_INSERT_TERM_2172 https://fairsharing.org/search?recordType=terminology_artefact)  search features of the same service. 
    In order to simplify the integration of the ontology (URL_TO_INSERT_TERM_2173 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2174 https://fairsharing.org/FAIRsharing.Mkl9RR)  support into external applications,  
   several-ontology (URL_TO_INSERT_TERM_2175 https://fairsharing.org/search?recordType=terminology_artefact)  lookup services provide users with language-specific clients to interact with them through their API. 

* **Is the distribution license of the ontology (URL_TO_INSERT_TERM_2176 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2177 https://fairsharing.org/FAIRsharing.Mkl9RR)  compatible with the way I plan to exploit the 
features provided the same service in my project (URL_TO_INSERT_TERM_2178 https://fairsharing.org/search?recordType=project)  or with the way I plan to integrate the same service in my project (URL_TO_INSERT_TERM_2179 https://fairsharing.org/search?recordType=project) ?**

    The licencing terms of the ontology (URL_TO_INSERT_TERM_2180 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2181 https://fairsharing.org/FAIRsharing.Mkl9RR)  of choice intended for use in a given context and 
    knowledge-intensive project (URL_TO_INSERT_TERM_2182 https://fairsharing.org/search?recordType=project) , is a key consideration when selecting an ontology (URL_TO_INSERT_TERM_2183 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2184 https://fairsharing.org/FAIRsharing.Mkl9RR) : available 
    ontology (URL_TO_INSERT_TERM_2185 https://fairsharing.org/search?recordType=terminology_artefact)  lookup services range from open-source applications to commercial tools, and it is best to choose one with funding in mind.

* **Does the ontology (URL_TO_INSERT_TERM_2186 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2189 https://fairsharing.org/FAIRsharing.Mkl9RR)  manage ontology (URL_TO_INSERT_TERM_2187 https://fairsharing.org/search?recordType=terminology_artefact)  versioning and updates so that I can easily reflect any ontology (URL_TO_INSERT_TERM_2188 https://fairsharing.org/search?recordType=terminology_artefact)  
update into my knowledge-intensive project (URL_TO_INSERT_TERM_2190 https://fairsharing.org/search?recordType=project) ? **

    Ontologies (URL_TO_INSERT_TERM_2193 https://fairsharing.org/search?recordType=terminology_artefact)  and terminologies (URL_TO_INSERT_TERM_2191 https://fairsharing.org/search?recordType=terminology_artefact)  usually evolve over time: when a new, updated version of an ontology (URL_TO_INSERT_TERM_2192 https://fairsharing.org/search?recordType=terminology_artefact)  used in a 
    knowledge-intensive project (URL_TO_INSERT_TERM_2194 https://fairsharing.org/search?recordType=project)  becomes available, best practice suggests that we should also update the part of our 
    project (URL_TO_INSERT_TERM_2195 https://fairsharing.org/search?recordType=project) s that rely on such ontology (URL_TO_INSERT_TERM_2196 https://fairsharing.org/search?recordType=terminology_artefact) . Some ontology (URL_TO_INSERT_TERM_2197 https://fairsharing.org/search?recordType=terminology_artefact)  lookup services implement specific procedures and tools to manage
    and propagate ontology (URL_TO_INSERT_TERM_2198 https://fairsharing.org/search?recordType=terminology_artefact)  updates; the availability of such tools would simplify the implementation of changes deriving
    from ontology (URL_TO_INSERT_TERM_2200 https://fairsharing.org/search?recordType=terminology_artefact)  updates in the project (URL_TO_INSERT_TERM_2199 https://fairsharing.org/search?recordType=project) s under consideration.

* **Is the ontology (URL_TO_INSERT_TERM_2201 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2202 https://fairsharing.org/FAIRsharing.Mkl9RR)  supported by an active community of developers
or by an active company? Which are the available channels I can rely on to receive support on the usage and integration 
of the ontology (URL_TO_INSERT_TERM_2203 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2204 https://fairsharing.org/FAIRsharing.Mkl9RR) ?**

    The support of an active community of developers and users is a key aspect to take into account when choosing an 
    ontology (URL_TO_INSERT_TERM_2205 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2207 https://fairsharing.org/FAIRsharing.Mkl9RR) . This could be quantified by evaluating several factors of an ontology (URL_TO_INSERT_TERM_2206 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2208 https://fairsharing.org/FAIRsharing.Mkl9RR)  including:
    (i) availability of mailing or support lists; (ii) for open-source project (URL_TO_INSERT_TERM_2210 https://fairsharing.org/search?recordType=project) s, using metric (URL_TO_INSERT_TERM_2209 https://fairsharing.org/search?recordType=metric) s such as the star-rating,
    the number of forks and followers and the frequency of commits of the project (URL_TO_INSERT_TERM_2211 https://fairsharing.org/search?recordType=project)  on the code-sharing platform used 
    (e.g. GitHub (URL_TO_INSERT_RECORD-NAME_2214 https://fairsharing.org/FAIRsharing.c55d5e) ); (iii) size of the community of users of the ontology (URL_TO_INSERT_TERM_2212 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2213 https://fairsharing.org/FAIRsharing.Mkl9RR)  (e.g. how many followers on social
    media accounts, how many clients advertised on the Website).

## Key Selection Criteria

The above questions have highlighted 20 factors which should be taken into account when choosing a service. 
These factors can be categorised into 3 groups; **ontology (URL_TO_INSERT_TERM_2216 https://fairsharing.org/search?recordType=terminology_artefact)  informat (URL_TO_INSERT_TERM_2215 https://fairsharing.org/search?recordType=model_and_format) ion, functionality** and **interfaces**, and include;

### **Ontology Information**



1. **URL (URL_TO_INSERT_RECORD-ABBREV_2219 https://fairsharing.org/FAIRsharing.9d38e2) **: the main URL (URL_TO_INSERT_RECORD-ABBREV_2220 https://fairsharing.org/FAIRsharing.9d38e2)  where the ontology (URL_TO_INSERT_TERM_2217 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2218 https://fairsharing.org/FAIRsharing.Mkl9RR)  can be accessed
2. **Latest version of service / data / code (where applicable**): the most recent version of both the content (i.e. ontologies (URL_TO_INSERT_TERM_2222 https://fairsharing.org/search?recordType=terminology_artefact) ) and the code of the ontology (URL_TO_INSERT_TERM_2221 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2223 https://fairsharing.org/FAIRsharing.Mkl9RR) 
3. **Host Organisation**: the organisation responsible for the maintenance of the ontology (URL_TO_INSERT_TERM_2224 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2225 https://fairsharing.org/FAIRsharing.Mkl9RR) 
4. **Public / private**: is the ontology (URL_TO_INSERT_TERM_2226 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2227 https://fairsharing.org/FAIRsharing.Mkl9RR)  a public or private infrastructure?
5. **Licence**: the licence that regulates the use and cost of the ontology (URL_TO_INSERT_TERM_2228 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2229 https://fairsharing.org/FAIRsharing.Mkl9RR) 
6. **Domain**: which is the knowledge domain covered by the ontologies (URL_TO_INSERT_TERM_2231 https://fairsharing.org/search?recordType=terminology_artefact)  referenced in the ontology (URL_TO_INSERT_TERM_2230 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2232 https://fairsharing.org/FAIRsharing.Mkl9RR) ?
7. **Quantification of community of users**: objective measures to quantify the community of users supporting and consuming an ontology (URL_TO_INSERT_TERM_2233 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2234 https://fairsharing.org/FAIRsharing.Mkl9RR) , including: number of stars and forks on GitHub (URL_TO_INSERT_RECORD-NAME_2235 https://fairsharing.org/FAIRsharing.c55d5e) , number of social media followers

### **Functionality**



8. **Number and complexity of ontologies (URL_TO_INSERT_TERM_2237 https://fairsharing.org/search?recordType=terminology_artefact)  covered**: how many ontologies (URL_TO_INSERT_TERM_2238 https://fairsharing.org/search?recordType=terminology_artefact)  does the ontology (URL_TO_INSERT_TERM_2236 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2239 https://fairsharing.org/FAIRsharing.Mkl9RR)  cover and how complex are they?
9. **Ontology (URL_TO_INSERT_TERM_2242 https://fairsharing.org/search?recordType=terminology_artefact)  format (URL_TO_INSERT_TERM_2240 https://fairsharing.org/search?recordType=model_and_format) s supported**: which ontology (URL_TO_INSERT_TERM_2243 https://fairsharing.org/search?recordType=terminology_artefact)  format (URL_TO_INSERT_TERM_2241 https://fairsharing.org/search?recordType=model_and_format) s are supported by the ontology (URL_TO_INSERT_TERM_2244 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2245 https://fairsharing.org/FAIRsharing.Mkl9RR) ?
10. **Ontology (URL_TO_INSERT_TERM_2246 https://fairsharing.org/search?recordType=terminology_artefact)  importing capabilities**: if and how ontologies (URL_TO_INSERT_TERM_2248 https://fairsharing.org/search?recordType=terminology_artefact)  can be imported and thus indexed by the ontology (URL_TO_INSERT_TERM_2247 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2249 https://fairsharing.org/FAIRsharing.Mkl9RR) ?
11. **Ontology (URL_TO_INSERT_TERM_2250 https://fairsharing.org/search?recordType=terminology_artefact)  browsing capabilities**: which interaction patterns are available to browse the set of ontologies (URL_TO_INSERT_TERM_2252 https://fairsharing.org/search?recordType=terminology_artefact)  contemplated by the ontology (URL_TO_INSERT_TERM_2251 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2253 https://fairsharing.org/FAIRsharing.Mkl9RR) ?
12. **Ontology (URL_TO_INSERT_TERM_2254 https://fairsharing.org/search?recordType=terminology_artefact)  search capabilities**: which search patterns are provided by the ontology (URL_TO_INSERT_TERM_2255 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2258 https://fairsharing.org/FAIRsharing.Mkl9RR)  to identify the best concept useful to represent the semantic of a term? When searching against a term, does the ontology (URL_TO_INSERT_TERM_2256 https://fairsharing.org/search?recordType=terminology_artefact)  give an indication of whether the term has been derived from a different ontology (URL_TO_INSERT_TERM_2257 https://fairsharing.org/search?recordType=terminology_artefact) ?
13. **Ontology (URL_TO_INSERT_TERM_2259 https://fairsharing.org/search?recordType=terminology_artefact)  recommendation capabilities**: does the ontology (URL_TO_INSERT_TERM_2260 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2262 https://fairsharing.org/FAIRsharing.Mkl9RR)  provide users with a recommendation concerning the most suitable ontologies (URL_TO_INSERT_TERM_2261 https://fairsharing.org/search?recordType=terminology_artefact)  to semantically characterize the contents of some text / a set of keywords? 
14. **Ontology (URL_TO_INSERT_TERM_2263 https://fairsharing.org/search?recordType=terminology_artefact)  update capabilities**: how are terms and/or relationships updated in a given ontology (URL_TO_INSERT_TERM_2264 https://fairsharing.org/search?recordType=terminology_artefact)  and how is this governed? Is this an automatic or manual update and what happens to terms that are considered obsolete?
15. **Ontology (URL_TO_INSERT_TERM_2265 https://fairsharing.org/search?recordType=terminology_artefact)  versioning capabilities**: are there predefined patterns to identify, manage and compare distinct versions of an ontology (URL_TO_INSERT_TERM_2266 https://fairsharing.org/search?recordType=terminology_artefact) ? 

### **Interfaces**



16. **Description of Web-based access to service**: which ontology (URL_TO_INSERT_TERM_2267 https://fairsharing.org/search?recordType=terminology_artefact)  browsing  and search patterns are available to the (Web-based) user interface of the ontology (URL_TO_INSERT_TERM_2268 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2270 https://fairsharing.org/FAIRsharing.Mkl9RR) ? Does the ontology (URL_TO_INSERT_TERM_2269 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2271 https://fairsharing.org/FAIRsharing.Mkl9RR)  also provide programmatic access to its data and services (e.g. by means of a REST API)?
17. **Description of API**: reference to the documentation of the (REST) API provided by the ontology (URL_TO_INSERT_TERM_2272 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2273 https://fairsharing.org/FAIRsharing.Mkl9RR) , if any
18. **Developer resources**: description of resources provided to developers in order to ease the programmatic access to the features of the ontology (URL_TO_INSERT_TERM_2274 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2275 https://fairsharing.org/FAIRsharing.Mkl9RR)  (i.e. libraries to query the REST API from a specific programming language).
19. **Local deploy of service**: possibility to locally deploy the ontology (URL_TO_INSERT_TERM_2276 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2277 https://fairsharing.org/FAIRsharing.Mkl9RR) 
20. **Source code reference**: if available, link to the source code of the ontology (URL_TO_INSERT_TERM_2278 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2279 https://fairsharing.org/FAIRsharing.Mkl9RR) 
4. **Overview of Widespread Ontology (URL_TO_INSERT_TERM_2280 https://fairsharing.org/search?recordType=terminology_artefact)  Lookup Services**

---

Here, we have used the selection criteria above to provide an overview and comparison of four widespread ontology (URL_TO_INSERT_TERM_2281 https://fairsharing.org/search?recordType=terminology_artefact)  lookup services, namely:



-  [EBI Ontology Lookup Service](https://www.ebi.ac.uk/ols/index)
-  [BioPortal](https://bioportal.bioontology.org)
-  [OHDSI Athena](https://athena.ohdsi.org/search-terms/start)
-  [Ontobee and the OBO Foundry](http://www.ontobee.org)

The results of the analysis can be found below, else in tabular format (URL_TO_INSERT_TERM_2282 https://fairsharing.org/search?recordType=model_and_format)  [here](https://docs.google.com/spreadsheets/d/1kn1oEhsYJPiLI5gA12B1UsbLBRoSLGbOYcOMDG4614o/edit#gid=0).

Note, the _‘last update of this table_’ field provides the date on which the ontology (URL_TO_INSERT_TERM_2283 https://fairsharing.org/search?recordType=terminology_artefact)  lookup service (URL_TO_INSERT_RECORD-NAME_2284 https://fairsharing.org/FAIRsharing.Mkl9RR)  was last assessed.

### **The EBI Ontology Lookup Service** {footcite}`pmid20460452`

<!-- **Overview by Francesco** -->


<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td>Ontology (URL_TO_INSERT_TERM_2285 https://fairsharing.org/search?recordType=terminology_artefact)  Lookup Servic (URL_TO_INSERT_RECORD-NAME_2286 https://fairsharing.org/FAIRsharing.Mkl9RR) e
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
   <td><strong>UR (URL_TO_INSERT_RECORD-ABBREV_2287 https://fairsharing.org/FAIRsharing.9d38e2) L</strong>
   </td>
   <td><a href="https://www.ebi.ac.uk/ols/index (URL_TO_INSERT_RECORD-HOMEPAGE_2288 https://fairsharing.org/FAIRsharing.Mkl9RR) ">https://www.ebi.ac.uk/ols/index (URL_TO_INSERT_RECORD-HOMEPAGE_2289 https://fairsharing.org/FAIRsharing.Mkl9RR) </a>
   </td>
  </tr>
  <tr>
   <td><strong>Latest version of service / data / code (where applicable)</strong>
   </td>
   <td>Content: last update 12 Apr 2020 11:39
<p>
Code: Maven POV version (from GitHub (URL_TO_INSERT_RECORD-NAME_2290 https://fairsharing.org/FAIRsharing.c55d5e) ): 3.2.1-SNAPSHOT
<p>
<a href="https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2291 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/OLS">https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2292 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/OLS</a>
<p>
Last commit on GitHub (URL_TO_INSERT_RECORD-NAME_2293 https://fairsharing.org/FAIRsharing.c55d5e) : April 2020
   </td>
  </tr>
  <tr>
   <td><strong>Host organisation</strong>
   </td>
   <td><a href="http://www.ebi.ac.uk/about/spot-team">Samples, Phenotypes and Ontologies (URL_TO_INSERT_TERM_2294 https://fairsharing.org/search?recordType=terminology_artefact)  Team</a> at EMBL-EBI
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
   <td>A repository (URL_TO_INSERT_TERM_2295 https://fairsharing.org/search?recordType=repository)  for biomedical ontologies (URL_TO_INSERT_TERM_2297 https://fairsharing.org/search?recordType=terminology_artefact)  that aims to provide a single point of access to the latest ontology (URL_TO_INSERT_TERM_2296 https://fairsharing.org/search?recordType=terminology_artefact)  versions
   </td>
  </tr>
  <tr>
   <td><strong>Set of ontologies (URL_TO_INSERT_TERM_2298 https://fairsharing.org/search?recordType=terminology_artefact)  covered</strong>
   </td>
   <td>245 ontologies (URL_TO_INSERT_TERM_2299 https://fairsharing.org/search?recordType=terminology_artefact)  / 6,119,228 terms / 27,778 properties / 485,541 individuals
<p>
Whole list at: <a href="https://www.ebi.ac.uk/ols/ontologies">https://www.ebi.ac.uk/ols/ontologies</a>
   </td>
  </tr>
  <tr>
   <td><strong>Onto. format (URL_TO_INSERT_TERM_2300 https://fairsharing.org/search?recordType=model_and_format) s supported</strong>
   </td>
   <td>OW (URL_TO_INSERT_RECORD-ABBREV_2301 https://fairsharing.org/FAIRsharing.atygwy) L 2 and OBO (URL_TO_INSERT_RECORD-ABBREV_2302 https://fairsharing.org/FAIRsharing.847069) 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. importing capabilities</strong>
   </td>
   <td>By means of a local installation it is possible to import ontologies (URL_TO_INSERT_TERM_2304 https://fairsharing.org/search?recordType=terminology_artefact)  in OWL (URL_TO_INSERT_RECORD-ABBREV_2305 https://fairsharing.org/FAIRsharing.atygwy)  2 and OBO (URL_TO_INSERT_RECORD-ABBREV_2306 https://fairsharing.org/FAIRsharing.847069)  format (URL_TO_INSERT_TERM_2303 https://fairsharing.org/search?recordType=model_and_format) 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. browsing capabilities</strong>
   </td>
   <td>Tree-view based browsing of hierarchies of classes and properties of ontologies (URL_TO_INSERT_TERM_2309 https://fairsharing.org/search?recordType=terminology_artefact) . The modifications added by different version of each ontology (URL_TO_INSERT_TERM_2307 https://fairsharing.org/search?recordType=terminology_artefact)  are shown by means of distinct background colors in ontology (URL_TO_INSERT_TERM_2308 https://fairsharing.org/search?recordType=terminology_artefact)  browsing tree-views
   </td>
  </tr>
  <tr>
   <td><strong>Onto. search capabilities</strong>
   </td>
   <td>Search by term to gather all the ontologies (URL_TO_INSERT_TERM_2310 https://fairsharing.org/search?recordType=terminology_artefact)  where the term is found. It is possible to restrict search results to one or more ontologies (URL_TO_INSERT_TERM_2311 https://fairsharing.org/search?recordType=terminology_artefact) , to a specific type of result (i.e. class, property or individual) or to exact or partial term match
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
   <td>OL (URL_TO_INSERT_RECORD-ABBREV_2313 https://fairsharing.org/FAIRsharing.Mkl9RR) S updates nightly to always provide the latest ontology (URL_TO_INSERT_TERM_2312 https://fairsharing.org/search?recordType=terminology_artefact)  versions
   </td>
  </tr>
  <tr>
   <td><strong>Onto. versioning capabilities</strong>
   </td>
   <td>Obsoleted ontology (URL_TO_INSERT_TERM_2314 https://fairsharing.org/search?recordType=terminology_artefact)  terms are spotted by means of a boolean flag (is_obsolete)
   </td>
  </tr>
  <tr>
   <td><strong>Description of Web-based access to service</strong>
   </td>
   <td>Besides a Web-based user interface useful to browse ontologies (URL_TO_INSERT_TERM_2316 https://fairsharing.org/search?recordType=terminology_artefact)  and search for ontology (URL_TO_INSERT_TERM_2315 https://fairsharing.org/search?recordType=terminology_artefact)  concepts, free-access by means of a REST API is provided to the users
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
   <td><a href="https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2317 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/OLS">https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2318 https://fairsharing.org/FAIRsharing.c55d5e) /EBISPOT/OLS</a>
   </td>
  </tr>
  <tr>
   <td><strong>Quantification of community of users</strong>
   </td>
   <td>GitHu (URL_TO_INSERT_RECORD-NAME_2319 https://fairsharing.org/FAIRsharing.c55d5e) b: 49 stars and 19 forks
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
   <td>Bioporta (URL_TO_INSERT_RECORD-NAME_2320 https://fairsharing.org/FAIRsharing.4m97ah) l 
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
   <td><strong>UR (URL_TO_INSERT_RECORD-ABBREV_2321 https://fairsharing.org/FAIRsharing.9d38e2) L</strong>
   </td>
   <td><a href="https://bioportal.bioontology.org (URL_TO_INSERT_RECORD-HOMEPAGE_2322 https://fairsharing.org/FAIRsharing.4m97ah) /">https://bioportal.bioontology.org (URL_TO_INSERT_RECORD-HOMEPAGE_2323 https://fairsharing.org/FAIRsharing.4m97ah) /</a>
   </td>
  </tr>
  <tr>
   <td><strong>Latest version of service / data / code (where applicable)</strong>
   </td>
   <td><em>Content</em>: last update 12 Apr 2020 11:39
<p>
<em>Code</em>: 
<ul>

<li>Web UI: <a href="https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2324 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/bioportal_web_ui">https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2325 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/bioportal_web_ui</a>

<li>REST API: <a href="https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2326 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_api">https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2327 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_api</a>

<li>Linked Data: <a href="https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2328 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_linked_data">https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2329 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_linked_data</a>

<p>
Latest commit on GitHub (URL_TO_INSERT_RECORD-NAME_2330 https://fairsharing.org/FAIRsharing.c55d5e) : April 2020
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td><strong>Host organisation</strong>
   </td>
   <td><a href="https://ncbo.bioontology.org/about-ncbo">U.S. National Center for Biomedical Ontology (URL_TO_INSERT_TERM_2331 https://fairsharing.org/search?recordType=terminology_artefact) </a>
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
   <td>Available at: <a href="https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2332 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_api/blob/master/LICENSE.txt">https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2333 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ontologies_api/blob/master/LICENSE.txt</a>
   </td>
  </tr>
  <tr>
   <td><strong>Domain</strong>
   </td>
   <td>A Web-based application for searching, sharing, visualizing, and analyzing a large repository (URL_TO_INSERT_TERM_2334 https://fairsharing.org/search?recordType=repository)  of biomedical ontologies (URL_TO_INSERT_TERM_2337 https://fairsharing.org/search?recordType=terminology_artefact) , terminologies (URL_TO_INSERT_TERM_2335 https://fairsharing.org/search?recordType=terminology_artefact) , and ontology (URL_TO_INSERT_TERM_2336 https://fairsharing.org/search?recordType=terminology_artefact) -based annotations
   </td>
  </tr>
  <tr>
   <td><strong>Set of ontologies (URL_TO_INSERT_TERM_2338 https://fairsharing.org/search?recordType=terminology_artefact)  covered</strong>
   </td>
   <td>Ontologies (URL_TO_INSERT_TERM_2339 https://fairsharing.org/search?recordType=terminology_artefact) : 842 / Classes: 11,324,508 
<p>
Whole list at: <a href="https://bioportal.bioontology.org (URL_TO_INSERT_RECORD-HOMEPAGE_2340 https://fairsharing.org/FAIRsharing.4m97ah) /ontologies">https://bioportal.bioontology.org (URL_TO_INSERT_RECORD-HOMEPAGE_2341 https://fairsharing.org/FAIRsharing.4m97ah) /ontologies</a>
   </td>
  </tr>
  <tr>
   <td><strong>Onto. format (URL_TO_INSERT_TERM_2342 https://fairsharing.org/search?recordType=model_and_format) s supported</strong>
   </td>
   <td>OW (URL_TO_INSERT_RECORD-ABBREV_2343 https://fairsharing.org/FAIRsharing.atygwy) L, OBO (URL_TO_INSERT_RECORD-ABBREV_2344 https://fairsharing.org/FAIRsharing.847069) , SKOS (URL_TO_INSERT_RECORD-ABBREV_2345 https://fairsharing.org/FAIRsharing.48e326) 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. importing capabilities</strong>
   </td>
   <td>It is possible to upload / submit new ontologies (URL_TO_INSERT_TERM_2348 https://fairsharing.org/search?recordType=terminology_artefact)  or new versions of existing ontologies (URL_TO_INSERT_TERM_2349 https://fairsharing.org/search?recordType=terminology_artefact)  that will be indexed in BioPortal (URL_TO_INSERT_RECORD-NAME_2350 https://fairsharing.org/FAIRsharing.4m97ah) . Ontology (URL_TO_INSERT_TERM_2347 https://fairsharing.org/search?recordType=terminology_artefact)  metadata will be provided in the <a href="http://omv.ontoware.org">Ontology Metadata Vocabulary</a> (OMV (URL_TO_INSERT_RECORD-ABBREV_2351 https://fairsharing.org/FAIRsharing.wqy605) ) format (URL_TO_INSERT_TERM_2346 https://fairsharing.org/search?recordType=model_and_format) 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. browsing capabilities</strong>
   </td>
   <td>For each ontology (URL_TO_INSERT_TERM_2354 https://fairsharing.org/search?recordType=terminology_artefact)  / terminology (URL_TO_INSERT_TERM_2352 https://fairsharing.org/search?recordType=terminology_artefact)  an overview of its content is provided together with separate tree-views tailored to explore its hierarchies of classes and properties. The set of available mappings to other ontologies (URL_TO_INSERT_TERM_2355 https://fairsharing.org/search?recordType=terminology_artefact)  / terminologies (URL_TO_INSERT_TERM_2353 https://fairsharing.org/search?recordType=terminology_artefact)  can be explored by a custom view
   </td>
  </tr>
  <tr>
   <td><strong>Onto. search capabilities</strong>
   </td>
   <td>Search by term to gather all the ontologies (URL_TO_INSERT_TERM_2356 https://fairsharing.org/search?recordType=terminology_artefact)  where the term is found. It is possible to restrict search results to one or more ontologies (URL_TO_INSERT_TERM_2357 https://fairsharing.org/search?recordType=terminology_artefact) , to a specific type of result (i.e. class, property or individual) or to exact or partial term match
   </td>
  </tr>
  <tr>
   <td><strong>Onto. recommendation capabilities</strong>
   </td>
   <td>An ontology (URL_TO_INSERT_TERM_2358 https://fairsharing.org/search?recordType=terminology_artefact)  recommender is available: it retrieves recommendations for the most relevant ontologies (URL_TO_INSERT_TERM_2359 https://fairsharing.org/search?recordType=terminology_artefact)  based on an excerpt from a biomedical text or a list of keywords.
<p>
Recommendations are based on: (i) <em>coverage</em> of the input text / set of keywords; (ii) <em>acceptance</em> of the ontologies (URL_TO_INSERT_TERM_2362 https://fairsharing.org/search?recordType=terminology_artefact) ; (iii) <em>detail of knowledge</em> available in the ontology (URL_TO_INSERT_TERM_2360 https://fairsharing.org/search?recordType=terminology_artefact)  to describe input data and (iv) <em>specialization</em> of the ontology (URL_TO_INSERT_TERM_2361 https://fairsharing.org/search?recordType=terminology_artefact)  to the specific domain under consideration
   </td>
  </tr>
  <tr>
   <td><strong>Onto. update capabilities</strong>
   </td>
   <td>Each ontology (URL_TO_INSERT_TERM_2363 https://fairsharing.org/search?recordType=terminology_artefact)  can be manually updated by accessing the BioPortal (URL_TO_INSERT_RECORD-NAME_2365 https://fairsharing.org/FAIRsharing.4m97ah)  or automatically updated by BioPortal (URL_TO_INSERT_RECORD-NAME_2366 https://fairsharing.org/FAIRsharing.4m97ah)  by continuously monitoring a URL (URL_TO_INSERT_RECORD-ABBREV_2367 https://fairsharing.org/FAIRsharing.9d38e2)  where the ontology (URL_TO_INSERT_TERM_2364 https://fairsharing.org/search?recordType=terminology_artefact)  and its new versions are published
   </td>
  </tr>
  <tr>
   <td><strong>Onto. versioning capabilities</strong>
   </td>
   <td>Each ontology (URL_TO_INSERT_TERM_2368 https://fairsharing.org/search?recordType=terminology_artefact)  is characterized by a version number in its metadata, useful to track distinct versions of the same ontology (URL_TO_INSERT_TERM_2369 https://fairsharing.org/search?recordType=terminology_artefact) 
   </td>
  </tr>
  <tr>
   <td><strong>Description of Web based access to service</strong>
   </td>
   <td>Besides a Web-based interface that supports ontology (URL_TO_INSERT_TERM_2370 https://fairsharing.org/search?recordType=terminology_artefact)  search, annotation, recommendation and mapping, also a free-after-registration access by means of a REST API is provided to the users
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
   <td>Sample code to access REST API in distinct languages is available at: <a href="https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2371 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ncbo_rest_sample_code">https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2372 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo/ncbo_rest_sample_code</a>
   </td>
  </tr>
  <tr>
   <td><strong>Local deploy of service</strong>
   </td>
   <td>In principle, local deploy of services is possible, even if not extensively documented. Source code (Rails) for Web UI, REST API and Linked Data management is available on NCBO GiHub account, <a href="https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2373 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo">https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2374 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo</a>
   </td>
  </tr>
  <tr>
   <td><strong>Source code reference</strong>
   </td>
   <td><a href="https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2375 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo">https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2376 https://fairsharing.org/FAIRsharing.c55d5e) /ncbo</a>
   </td>
  </tr>
  <tr>
   <td><strong>Quantification of community of users</strong>
   </td>
   <td>GitHu (URL_TO_INSERT_RECORD-NAME_2377 https://fairsharing.org/FAIRsharing.c55d5e) b: 
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
   <td><strong>UR (URL_TO_INSERT_RECORD-ABBREV_2378 https://fairsharing.org/FAIRsharing.9d38e2) L</strong>
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
<em>Code</em>: Maven POV version (from GitHub (URL_TO_INSERT_RECORD-NAME_2379 https://fairsharing.org/FAIRsharing.c55d5e) ): 1.10.0
<p>
<a href="https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2380 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena">https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2381 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena</a>
<p>
Latest commit on GitHub (URL_TO_INSERT_RECORD-NAME_2382 https://fairsharing.org/FAIRsharing.c55d5e) : September 2019
   </td>
  </tr>
  <tr>
   <td><strong>Host organisation</strong>
   </td>
   <td><a href="https://www.ohdsi.org/">Observational Health Data Sciences and Informat (URL_TO_INSERT_TERM_2383 https://fairsharing.org/search?recordType=model_and_format) ics (OHDSI) initiative</a>
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
   <td>Useful to browse the set of Standard (URL_TO_INSERT_TERM_2384 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabularies which are part of the OMOP Common Data Model (URL_TO_INSERT_TERM_2385 https://fairsharing.org/search?recordType=model_and_format)  (CDM), version 5.x. They are maintained by the Observational Health Data Science and Informat (URL_TO_INSERT_TERM_2386 https://fairsharing.org/search?recordType=model_and_format) ics (OHDSI, pronounced “Odyssey”) initiative
   </td>
  </tr>
  <tr>
   <td><strong>Set of ontologies (URL_TO_INSERT_TERM_2387 https://fairsharing.org/search?recordType=terminology_artefact)  covered</strong>
   </td>
   <td>Standard (URL_TO_INSERT_TERM_2388 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabularies which are part of the<a href="https://www.ohdsi.org/web/wiki/doku.php?id=documentation:vocabulary_etl"> OMOP Common Data Model (URL_TO_INSERT_TERM_2389 https://fairsharing.org/search?recordType=model_and_format)  (CDM)</a>, version 5.x. It integrates several source vocabularies including UMLS, SNOMED, RxNorm (URL_TO_INSERT_RECORD-NAME_2390 https://fairsharing.org/FAIRsharing.36pf8q) , NDFRT (URL_TO_INSERT_RECORD-ABBREV_2391 https://fairsharing.org/FAIRsharing.901nkj) , VA Product, VA Class, ATC (URL_TO_INSERT_RECORD-ABBREV_2392 https://fairsharing.org/FAIRsharing.1a27h8) , MeSH, ICD10, GCN_SEQNO, ETC, Indication, ICD9CM, ICD9Proc, ICD10CM, LOiNC, etc.
   </td>
  </tr>
  <tr>
   <td><strong>Onto. format (URL_TO_INSERT_TERM_2393 https://fairsharing.org/search?recordType=model_and_format) s supported</strong>
   </td>
   <td>Not a specific format (URL_TO_INSERT_TERM_2395 https://fairsharing.org/search?recordType=model_and_format) , a collection (URL_TO_INSERT_TERM_2394 https://fairsharing.org/search?recordType=collection)  of ontology (URL_TO_INSERT_TERM_2396 https://fairsharing.org/search?recordType=terminology_artefact)  concepts / classes assigned to a specific domain and imported from a specific source vocabulary 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. importing capabilities</strong>
   </td>
   <td>Tailored to browse the Standard (URL_TO_INSERT_TERM_2397 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabularies which are part of the OMOP Common Data Model (URL_TO_INSERT_TERM_2398 https://fairsharing.org/search?recordType=model_and_format)  (CDM)
   </td>
  </tr>
  <tr>
   <td><strong>Onto. browsing capabilities</strong>
   </td>
   <td>Table based views are available to browse all the concepts belonging to a specific source vocabulary 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. search capabilities</strong>
   </td>
   <td>Search by term to gather all the source vocabularies where the term is found. It is possible to restrict search results by domain, class and source vocabulary
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
   <td>Each time a new version of the Standard (URL_TO_INSERT_TERM_2399 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabularies which are part of the OMOP Common Data Model (URL_TO_INSERT_TERM_2400 https://fairsharing.org/search?recordType=model_and_format)  (CDM) is available an updated the core (URL_TO_INSERT_RECORD-NAME_2401 https://fairsharing.org/FAIRsharing.xMmOCL)  (URL_TO_INSERT_RECORD-ABBREV_2402 https://fairsharing.org/FAIRsharing.m283c)  set of concept is available
   </td>
  </tr>
  <tr>
   <td><strong>Onto. versioning capabilities</strong>
   </td>
   <td>The latest version of the Standard (URL_TO_INSERT_TERM_2403 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabulary is V5.0
   </td>
  </tr>
  <tr>
   <td><strong>Description of Web-based access to service</strong>
   </td>
   <td>Athena is a Web interface available to browse concepts of the Standard (URL_TO_INSERT_TERM_2404 https://fairsharing.org/search?fairsharingRegistry=Standard) ized Vocabulary (V5.0). Both search results and the whole dataset can be downloaded after registration
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
   <td>In principle, local deploy of services is possible, even if not extensively documented. Source code on GitHub (URL_TO_INSERT_RECORD-NAME_2405 https://fairsharing.org/FAIRsharing.c55d5e)  account <a href="https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2406 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena">https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2407 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena</a> 
   </td>
  </tr>
  <tr>
   <td><strong>Source code reference</strong>
   </td>
   <td><a href="https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2408 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena">https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2409 https://fairsharing.org/FAIRsharing.c55d5e) /OHDSI/Athena</a>
   </td>
  </tr>
  <tr>
   <td><strong>Quantification of community of users</strong>
   </td>
   <td>GitHu (URL_TO_INSERT_RECORD-NAME_2410 https://fairsharing.org/FAIRsharing.c55d5e) b: 29 stars and 6 forks
<p>
Twitter: 1.284 followers of the Observational Health Data Sciences and Informat (URL_TO_INSERT_TERM_2411 https://fairsharing.org/search?recordType=model_and_format) ics (OHDSI) account
   </td>
  </tr>
</table>


### **Ontobee and the OBO Foundry** {footcite}`pmid27733503ontobee`

<!-- **Overview by Francesco** -->



<table>
  <tr>
   <td><strong>Name</strong>
   </td>
   <td>OBO Foundr (URL_TO_INSERT_RECORD-NAME_2412 https://fairsharing.org/FAIRsharing.847069) y
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
   <td><strong>UR (URL_TO_INSERT_RECORD-ABBREV_2413 https://fairsharing.org/FAIRsharing.9d38e2) L</strong>
   </td>
   <td><a href="http://www.ontobee.org (URL_TO_INSERT_RECORD-HOMEPAGE_2414 https://fairsharing.org/FAIRsharing.q8fx1b) /">http://www.ontobee.org (URL_TO_INSERT_RECORD-HOMEPAGE_2415 https://fairsharing.org/FAIRsharing.q8fx1b) /</a> (<a href="http://obofoundry.org/">http://obofoundry.org/</a>)
   </td>
  </tr>
  <tr>
   <td><strong>Latest version of service / data / code (where applicable)</strong>
   </td>
   <td><em>Content (OBO Foundry (URL_TO_INSERT_RECORD-NAME_2416 https://fairsharing.org/FAIRsharing.847069) )</em>: last update April 2020
<p>
<em>Code (Ontobee (URL_TO_INSERT_RECORD-NAME_2417 https://fairsharing.org/FAIRsharing.q8fx1b) )</em>: <a href="https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2418 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee">https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2419 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee</a>
<p>
Latest commit on GitHub (URL_TO_INSERT_RECORD-NAME_2420 https://fairsharing.org/FAIRsharing.c55d5e) : August 2018
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
   <td>Ontobe (URL_TO_INSERT_RECORD-NAME_2427 https://fairsharing.org/FAIRsharing.q8fx1b) e has been used as the default ontology (URL_TO_INSERT_TERM_2421 https://fairsharing.org/search?recordType=terminology_artefact)  Linked Data server for most <a href="http://obofoundry.org/">Open Biological and Biomedical Ontology (URL_TO_INSERT_TERM_2422 https://fairsharing.org/search?recordType=terminology_artefact)  (OBO (URL_TO_INSERT_RECORD-ABBREV_2426 https://fairsharing.org/FAIRsharing.847069) ) Foundry</a> library ontologies (URL_TO_INSERT_TERM_2424 https://fairsharing.org/search?recordType=terminology_artefact) . The OBO Foundry (URL_TO_INSERT_RECORD-NAME_2425 https://fairsharing.org/FAIRsharing.847069)  is a collective of ontology (URL_TO_INSERT_TERM_2423 https://fairsharing.org/search?recordType=terminology_artefact)  developers that are committed to collaboration and adherence to shared principles
   </td>
  </tr>
  <tr>
   <td><strong>Set of ontologies (URL_TO_INSERT_TERM_2428 https://fairsharing.org/search?recordType=terminology_artefact)  covered</strong>
   </td>
   <td>164 active ontologies (URL_TO_INSERT_TERM_2429 https://fairsharing.org/search?recordType=terminology_artefact) , 5 orphaned ontologies (URL_TO_INSERT_TERM_2430 https://fairsharing.org/search?recordType=terminology_artefact)  and 57 inactive ontologies (URL_TO_INSERT_TERM_2431 https://fairsharing.org/search?recordType=terminology_artefact)  (in OBO Foundry (URL_TO_INSERT_RECORD-NAME_2432 https://fairsharing.org/FAIRsharing.847069) )
   </td>
  </tr>
  <tr>
   <td><strong>Onto. format (URL_TO_INSERT_TERM_2433 https://fairsharing.org/search?recordType=model_and_format) s supported</strong>
   </td>
   <td>OW (URL_TO_INSERT_RECORD-ABBREV_2434 https://fairsharing.org/FAIRsharing.atygwy) L and OBO (URL_TO_INSERT_RECORD-ABBREV_2435 https://fairsharing.org/FAIRsharing.847069) 
   </td>
  </tr>
  <tr>
   <td><strong>Onto. importing capabilities</strong>
   </td>
   <td>Ontobe (URL_TO_INSERT_RECORD-NAME_2444 https://fairsharing.org/FAIRsharing.q8fx1b) e can import both OWL (URL_TO_INSERT_RECORD-ABBREV_2440 https://fairsharing.org/FAIRsharing.atygwy)  and OBO (URL_TO_INSERT_RECORD-ABBREV_2443 https://fairsharing.org/FAIRsharing.847069)  ontologies (URL_TO_INSERT_TERM_2437 https://fairsharing.org/search?recordType=terminology_artefact) . New ontologies (URL_TO_INSERT_TERM_2438 https://fairsharing.org/search?recordType=terminology_artefact)  can be proposed tired to the set of OBO Foundry (URL_TO_INSERT_RECORD-NAME_2441 https://fairsharing.org/FAIRsharing.847069)  ontologies (URL_TO_INSERT_TERM_2439 https://fairsharing.org/search?recordType=terminology_artefact) ; a committee will review the ontology (URL_TO_INSERT_TERM_2436 https://fairsharing.org/search?recordType=terminology_artefact)  to check if it adheres to all the OBO Foundry (URL_TO_INSERT_RECORD-NAME_2442 https://fairsharing.org/FAIRsharing.847069)  principles
   </td>
  </tr>
  <tr>
   <td><strong>Onto. browsing capabilities</strong>
   </td>
   <td>The OBO Foundry (URL_TO_INSERT_RECORD-NAME_2451 https://fairsharing.org/FAIRsharing.847069)  portal provides a set of metadata describing each ontology (URL_TO_INSERT_TERM_2446 https://fairsharing.org/search?recordType=terminology_artefact)  together with the possibility to download the same ontology (URL_TO_INSERT_TERM_2447 https://fairsharing.org/search?recordType=terminology_artefact)  in several format (URL_TO_INSERT_TERM_2445 https://fairsharing.org/search?recordType=model_and_format) s. To browse ontologies (URL_TO_INSERT_TERM_2449 https://fairsharing.org/search?recordType=terminology_artefact) , the OBO Foundry (URL_TO_INSERT_RECORD-NAME_2452 https://fairsharing.org/FAIRsharing.847069)  portal points to the ontology (URL_TO_INSERT_TERM_2448 https://fairsharing.org/search?recordType=terminology_artefact)  browsing pages of other Web platforms including <a href="http://www.ontobee.org (URL_TO_INSERT_RECORD-HOMEPAGE_2453 https://fairsharing.org/FAIRsharing.q8fx1b) /">Ontobee</a>, <a href="https://bioportal.bioontology.org (URL_TO_INSERT_RECORD-HOMEPAGE_2450 https://fairsharing.org/FAIRsharing.4m97ah) /">BioPortal</a> and the <a href="https://www.ebi.ac.uk/ols">Ontology Lookup Service</a>.
   </td>
  </tr>
  <tr>
   <td><strong>Onto. search capabilities</strong>
   </td>
   <td>The OBO Foundry (URL_TO_INSERT_RECORD-NAME_2457 https://fairsharing.org/FAIRsharing.847069)  portal exploits <a href="http://www.ontobee.org (URL_TO_INSERT_RECORD-HOMEPAGE_2459 https://fairsharing.org/FAIRsharing.q8fx1b) /">Ontobee</a> to provide users with ontology (URL_TO_INSERT_TERM_2454 https://fairsharing.org/search?recordType=terminology_artefact)  search capabilities.Ontobe (URL_TO_INSERT_RECORD-NAME_2458 https://fairsharing.org/FAIRsharing.q8fx1b) e enables users to search ontology (URL_TO_INSERT_TERM_2455 https://fairsharing.org/search?recordType=terminology_artefact)  concepts by term, eventually restricting the search to a specific ontology (URL_TO_INSERT_TERM_2456 https://fairsharing.org/search?recordType=terminology_artefact) 
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
   <td>An established <a href="http://obofoundry.org/principles/fp-004-versioning.html">PURL system to publish new versions / updates of an ontology (URL_TO_INSERT_TERM_2461 https://fairsharing.org/search?recordType=terminology_artefact) </a> is defined; new versions of an ontologies (URL_TO_INSERT_TERM_2462 https://fairsharing.org/search?recordType=terminology_artefact)  should be accessible at PURLs with the following format (URL_TO_INSERT_TERM_2460 https://fairsharing.org/search?recordType=model_and_format) : <code>http://purl.obolibrary.org/obo/idspace/YYYY-MM-DD/idspace.owl</code> or <code>.obo</code>, for instance: <code><a href="https://raw.githubusercontent.com/BiodiversityOntologies/bco/2020-03-27/bco.owl">https://raw.githubusercontent.com/BiodiversityOntologies/bco/2020-03-27/bco.owl</a></code>
   </td>
  </tr>
  <tr>
   <td><strong>Onto. versioning capabilities</strong>
   </td>
   <td>The OBO (URL_TO_INSERT_RECORD-ABBREV_2467 https://fairsharing.org/FAIRsharing.847069)  principles, implemented by the ontologies (URL_TO_INSERT_TERM_2464 https://fairsharing.org/search?recordType=terminology_artefact)  available in OBO Foundry (URL_TO_INSERT_RECORD-NAME_2466 https://fairsharing.org/FAIRsharing.847069) , enforces a system of versioning systems, with each ontology (URL_TO_INSERT_TERM_2463 https://fairsharing.org/search?recordType=terminology_artefact)  version receiving an unique identifier (URL_TO_INSERT_TERM_2465 https://fairsharing.org/search?recordType=identifier_schema)  (by means of numbers, dates, tags)
   </td>
  </tr>
  <tr>
   <td><strong>Description of Web-based access to service</strong>
   </td>
   <td>Ontobe (URL_TO_INSERT_RECORD-NAME_2469 https://fairsharing.org/FAIRsharing.q8fx1b) e provides a web interface that supports, besides searching for ontology (URL_TO_INSERT_TERM_2468 https://fairsharing.org/search?recordType=terminology_artefact)  concepts, the execution of SPARQL (URL_TO_INSERT_RECORD-ABBREV_2470 https://fairsharing.org/FAIRsharing.87ccfd)  queries and the annotation of text excerpts
   </td>
  </tr>
  <tr>
   <td><strong>Description of API</strong>
   </td>
   <td>No specific REST API is provided; users can retrieve both HTML (URL_TO_INSERT_RECORD-ABBREV_2472 https://fairsharing.org/FAIRsharing.YugnuL)  and RDF (URL_TO_INSERT_RECORD-ABBREV_2473 https://fairsharing.org/FAIRsharing.p77ph9)  descriptions of concepts that belongs to Ontobee (URL_TO_INSERT_RECORD-NAME_2474 https://fairsharing.org/FAIRsharing.q8fx1b)  ontologies (URL_TO_INSERT_TERM_2471 https://fairsharing.org/search?recordType=terminology_artefact) , in adherence to the principles of Linked Data community
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
   <td>In principle, local deploy of services is possible, even if not extensively documented. Source code on GiHub account <a href="https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2475 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee">https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2476 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee</a>
   </td>
  </tr>
  <tr>
   <td><strong>Source code reference</strong>
   </td>
   <td><a href="https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2477 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee">https://github.com (URL_TO_INSERT_RECORD-HOMEPAGE_2478 https://fairsharing.org/FAIRsharing.c55d5e) /OntoZoo/ontobee</a>
   </td>
  </tr>
  <tr>
   <td><strong>Quantification of community of users</strong>
   </td>
   <td>GitHu (URL_TO_INSERT_RECORD-NAME_2479 https://fairsharing.org/FAIRsharing.c55d5e) b: 12 stars and 4 forks
<p>
Twitter OBOFoundry account: 220 followers
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
