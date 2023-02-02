(fcb-intro-cro)=

# Practical Considerations for CROs to play FAIR

+++

````{panels_fairplus}
:identifier_text: FCB056
:identifier_link: http://w3id.org/faircookbook/FCB056
:difficulty_level: 2
:recipe_type: background_information
:reading_time_minutes: 15
:intended_audience: procurement_officer, principal_investigator, data_curator, data_manager, data_scientist  
:has_executable_code: nope
:maturity_level: 2
:maturity_indicator: 1, 2
:recipe_name: Practical Considerations for CROs to play FAIR
```` 


## Main Objective 

### Background
It is undeniable that there is an ever-growing need to manage data in terms of both volume and complexity within the life sciences sector. Technological advances have certainly paved the way to handle (URL_TO_INSERT_RECORD_7123 https://fairsharing.org/FAIRsharing.0b7e54)  large volumes of data in the past decade or so. However, the ability to `semantically` connect and exchange informat (URL_TO_INSERT_TERM_7122 https://fairsharing.org/search?recordType=model_and_format) ion within and between organizations remains a challenge to most part even today. Coupled with the need to manage compliances, regulations, newer discoveries in disease areas and audits, the ability to manage, store and access data is certainly an uphill task.
### Goals
This recipe intends to enumerate ideas that one should consider within the context of Contract Research (URL_TO_INSERT_RECORD_7127 https://fairsharing.org/FAIRsharing.52b22c)  Organizations (CRO) and how adopting and applying FAIR (URL_TO_INSERT_RECORD_7126 https://fairsharing.org/FAIRsharing.WWI10U)  principles will generate a higher RO (URL_TO_INSERT_RECORD_7124 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_7125 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_7128 https://fairsharing.org/FAIRsharing.cp0ybc) I over the long run. We also will explore key scenarios in mitigating some of the repeated ETL pains that CROs face on a regular basis when managing data in the life sciences sector.
While the recipe tries to encompass research (URL_TO_INSERT_RECORD_7129 https://fairsharing.org/FAIRsharing.52b22c)  topics, the focus remains within the clinical landscape.

---


## Origins, purpose and evolution:
CROs have their roots dating back to early 1980s and even earlier in some cases. Providing services to pharmaceuticals companies in the broader areas of animal testing eventually panned out to a full-blown suite of services including `data collection (URL_TO_INSERT_TERM_7130 https://fairsharing.org/search?recordType=collection) `, `data management` and `statistical consulting`. However, with decades of expertise under their belts, these niche organizations have evolved into a dominant force that is more or less capable of doing all the work of the sponsor with oversight as needed.

### Challenges:
One must recall the promises of lower execution costs, high data quality and ability to scale on demand in terms of resources without any (or slight) budget constraints (largely) has made CROs a go-to service provider. With the burden of proof lying on the shoulders of CROs, we run into the age-old question of cost versus time analysis, which sets in motion a series of events. Recall that CROs are not sponsor specific but rather service providers. Having said the above, listed below are a few challenges faced by CROs from a data management standpoint:

1.	Time to delivery versus cost Ratio
2.	Expertise retention and turn cycles
3.	Poor data quality and inadequate validation frameworks (at source)
4.	Lack of metadata  or lack of metadata enrichment thereof
5.	Poorly constructed or mis-handle (URL_TO_INSERT_RECORD_7131 https://fairsharing.org/FAIRsharing.0b7e54) d `data management plans` (DMP)
6.	Lack of resources or lack of understanding of data itself.
7.	Infrastructure problems
8.	Delivery model (URL_TO_INSERT_TERM_7132 https://fairsharing.org/search?recordType=model_and_format) s
    - Functional Services Provider (FSP) (almost extinct) 
    - Consulting resources that are time limited
9.	Issues with Extraction-Transform-Load (ETL) setups and pain areas for mitigation, moving towards FAIR (URL_TO_INSERT_RECORD_7133 https://fairsharing.org/FAIRsharing.WWI10U) 
    -	Data un-availability either due to poor `Data Handling Plan` (DHP) policies (URL_TO_INSERT_TERM_7134 https://fairsharing.org/search?fairsharingRegistry=Policy)  or set-ups
    -	Lack of coherence when it comes to data types across a portfolio of studies
    -	Lack of adherence to standard (URL_TO_INSERT_TERM_7135 https://fairsharing.org/search?fairsharingRegistry=Standard) ized metadata or poorly defined metadata
    -	Lack of data persistence (metadata outliving the data)
    -	Infrastructure and legacy programming techniques
    -	Lack of adherence to controlled terminologies (URL_TO_INSERT_TERM_7136 https://fairsharing.org/search?recordType=terminology_artefact)  or ontologies (URL_TO_INSERT_TERM_7137 https://fairsharing.org/search?recordType=terminology_artefact) 
    -	Change in metadata model (URL_TO_INSERT_TERM_7138 https://fairsharing.org/search?recordType=model_and_format)  over time to accommodate complex business decisions (variability)

### Considerations:
1.	**Understanding cost versus time**: Data FAIR (URL_TO_INSERT_RECORD_7142 https://fairsharing.org/FAIRsharing.WWI10U) ification is still a topic that is gaining traction within scientific communities since most of its roots come from research (URL_TO_INSERT_RECORD_7144 https://fairsharing.org/FAIRsharing.52b22c) . Research (URL_TO_INSERT_RECORD_7145 https://fairsharing.org/FAIRsharing.52b22c)  organizations working with Pharma are very cost-driven and tend to skim out topics, which do not provide a strong RO (URL_TO_INSERT_RECORD_7140 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_7141 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_7146 https://fairsharing.org/FAIRsharing.cp0ybc) I in the near short term. Multiply this by the fact that such organizations come in all sizes and are located globally to primarily drive down cost. The ability to employ or divert resources to engage in data FAIR (URL_TO_INSERT_RECORD_7143 https://fairsharing.org/FAIRsharing.WWI10U) ification may not justify the cost vs time metric (URL_TO_INSERT_TERM_7139 https://fairsharing.org/search?recordType=metric) . We also need to consider that CROs are driven by sponsor demands and it would be more prudent to have a top-down approach to empower them to build a cultural and process shift towards such endeavors. 

2.	**Partner with Standard (URL_TO_INSERT_TERM_7147 https://fairsharing.org/search?fairsharingRegistry=Standard)  Developing Organisations and contribute towards open tooling**: Building and managing ontologies (URL_TO_INSERT_TERM_7149 https://fairsharing.org/search?recordType=terminology_artefact)  are a key driver in enabling a FAIR (URL_TO_INSERT_RECORD_7151 https://fairsharing.org/FAIRsharing.WWI10U)  data environment since the very essence of binding domains (topics of interest) rely heavily on uniform and shared concepts that can be map (URL_TO_INSERT_RECORD_7150 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_7152 https://fairsharing.org/FAIRsharing.31385c)  and linked across in a systematic method between siloed data entities. Open Tooling and working with Standard (URL_TO_INSERT_TERM_7148 https://fairsharing.org/search?fairsharingRegistry=Standard) s Data Organizations (SDOs) enables CROs in the context of data management to develop a deeper understanding of the industry workings and demonstrate industry expertise within such domains of interest.

    - Precompetitive initiatives, examples of which can be found under the [Pistoia Alliance initiative](https://pistoiaalliance.org) represent an outstanding value for money. Efforts such as OpenTargets, CTTV about target identifications are successful examples, as are initiatives in the area of semantics resources. Indeed, needs for shared vocabularies are huge in domain such as biological reagents (antibodies, cell lines, constructs) but also standard (URL_TO_INSERT_TERM_7153 https://fairsharing.org/search?fairsharingRegistry=Standard) ized ways to describe assays. Resources such as [Antibody Registry (URL_TO_INSERT_RECORD_7154 https://fairsharing.org/FAIRsharing.3wdd17) ](https://antibodyregistry.org (URL_TO_INSERT_RECORD_7155 https://fairsharing.org/FAIRsharing.3wdd17) ), [Cellosaurus](https://web.expasy.org/cellosaurus/), [addgene](https://addgene.org), but also [bioassayexpress](https://www.bioassayexpress.com/) represent areas where Pharma and CRO cooperating on these topics would be considerable gains.

    - Test data Factory tool (TDF) from PHUSE’s Shared Code Analyses Working Group (SCAWG) is yet another initiative; dynamically build synthetic datasets for testing out solutions driven by CDI (URL_TO_INSERT_RECORD_7158 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_7160 https://fairsharing.org/3525)  data standard (URL_TO_INSERT_TERM_7156 https://fairsharing.org/search?fairsharingRegistry=Standard) s particularly SDTM and ADaM. This is a very novel concept and can enable research (URL_TO_INSERT_RECORD_7159 https://fairsharing.org/FAIRsharing.52b22c)  organizations and others as a whole to test out varied scenarios with clearly documented deviations from data standard (URL_TO_INSERT_TERM_7157 https://fairsharing.org/search?fairsharingRegistry=Standard) s.

    - FAIR (URL_TO_INSERT_RECORD_7162 https://fairsharing.org/FAIRsharing.WWI10U)  toolkit (https://fairtoolkit.pistoiaalliance.org/) & [FAIR Evaluator](https://w3id.org (URL_TO_INSERT_RECORD_7161 https://fairsharing.org/FAIRsharing.S6BoUk) /AmIFAIR) are both excellent resources to gain a deeper perspective on the “HOW” aspect of data FAIR (URL_TO_INSERT_RECORD_7163 https://fairsharing.org/FAIRsharing.WWI10U) ification. The toolkit can enable service providers such as CROs to utilize real world use cases implemented by Pharmaceuticals and research (URL_TO_INSERT_RECORD_7166 https://fairsharing.org/FAIRsharing.52b22c)  alike. It also encompasses methods such as tools and trainings allowing one to deep-dive into implementation aspects of FAIR (URL_TO_INSERT_RECORD_7164 https://fairsharing.org/FAIRsharing.WWI10U)  principles. More Details on FAIR (URL_TO_INSERT_RECORD_7165 https://fairsharing.org/FAIRsharing.WWI10U)  Evaluator can be found at https://fairsharing.github.io/FAIR-Evaluator-FrontEnd/#!/about 

3.	**The case for cultural mindset shift**:
It is evident that with changes comes challenges and the move towards being FAIR (URL_TO_INSERT_RECORD_7170 https://fairsharing.org/FAIRsharing.WWI10U)  is no exception. Cost versus time ratio is possibly not the only factor that could prove to be a hurdl (URL_TO_INSERT_RECORD_7175 https://fairsharing.org/FAIRsharing.vm4688) e. Resistance to data sharing, existing infrastructure that may be FAIR (URL_TO_INSERT_RECORD_7171 https://fairsharing.org/FAIRsharing.WWI10U)  to some degree (in most cases ‘F’) or use cases that may be specific enough to not require adopting FAIR (URL_TO_INSERT_RECORD_7172 https://fairsharing.org/FAIRsharing.WWI10U)  are other factors that need to be considered. Collaborative effort between stakeholders and CRO’s combined with a top-down mandate can enable us to realize a stronger RO (URL_TO_INSERT_RECORD_7168 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_7169 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_7176 https://fairsharing.org/FAIRsharing.cp0ybc) I, ability to share data and a measurable metric (URL_TO_INSERT_TERM_7167 https://fairsharing.org/search?recordType=metric)  to show pre and post FAIR (URL_TO_INSERT_RECORD_7173 https://fairsharing.org/FAIRsharing.WWI10U) ification combined with visible benefits will pave the way for easier adoption and implementation of FAIR (URL_TO_INSERT_RECORD_7174 https://fairsharing.org/FAIRsharing.WWI10U)  principles. 

4.	**Emphasize on building critical in-house data skills**:
There is an upward growth trend of skills deficit not due the lack of resources rather; the role of data service providers are usually limited to a fixed scope of deliverables, which is time, constrained. While the current skills can manifest a set of experts in their own rights, the vision to build a FAIR (URL_TO_INSERT_RECORD_7181 https://fairsharing.org/FAIRsharing.WWI10U)  future requires constant collaboration and up-skilling. It is therefore vital to have a deeper understanding of topics such as open standard (URL_TO_INSERT_TERM_7177 https://fairsharing.org/search?fairsharingRegistry=Standard) s protocols (http, w3c), role that ontologies (URL_TO_INSERT_TERM_7178 https://fairsharing.org/search?recordType=terminology_artefact)  play in describing data, scope of URI (URL_TO_INSERT_RECORD_7179 https://fairsharing.org/FAIRsharing.d261e1) ’s and IRI’s in the clinical context, RDF (URL_TO_INSERT_RECORD_7180 https://fairsharing.org/FAIRsharing.p77ph9)  and what linked data means and how it binds it all to-gether in the semantic landscape. This requires a lot of time and investment but is a necessity for a FAIR (URL_TO_INSERT_RECORD_7182 https://fairsharing.org/FAIRsharing.WWI10U) er future.


5.	**Scope and Data Cleansing**: 
It may be a worthwhile effort to narrow down scope of data that requires FAIR (URL_TO_INSERT_RECORD_7187 https://fairsharing.org/FAIRsharing.WWI10U) ification prior to embarking on this journey. This can also mean that we can identify the list of potential studies that require additional curation which can range from metadata enrichment, handling missing values and applying necessary terminologies (URL_TO_INSERT_TERM_7184 https://fairsharing.org/search?recordType=terminology_artefact)  as agreed (based on prior decided set such as UCUM (URL_TO_INSERT_RECORD_7188 https://fairsharing.org/FAIRsharing.27w8k0) ).The scope can also be limited to a group of indications or TA (leverage TAUGs from CDI (URL_TO_INSERT_RECORD_7185 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_7189 https://fairsharing.org/3525)  CFAST (URL_TO_INSERT_RECORD_7186 https://fairsharing.org/FAIRsharing.p5df9c) ) and then bind with the data model (URL_TO_INSERT_TERM_7183 https://fairsharing.org/search?recordType=model_and_format)  for machine readability (key stone for interoperability). 

6.	**Machine Readable Data Management Plans**:
The DMP is probably the most vital document that containing key informat (URL_TO_INSERT_TERM_7191 https://fairsharing.org/search?recordType=model_and_format) ion regarding how data will be created, collected, transferred and utilized. It also entails out detailed descriptions about the collection (URL_TO_INSERT_TERM_7190 https://fairsharing.org/search?recordType=collection)  mechanisms, audit procedures and key study protocol related informat (URL_TO_INSERT_TERM_7192 https://fairsharing.org/search?recordType=model_and_format) ion. Having a machine readable DMP can show immediate and significant cost savings and in the process aim for ‘FAIR (URL_TO_INSERT_RECORD_7193 https://fairsharing.org/FAIRsharing.WWI10U)  by design’, which also is a living document throughout the lifecycle of the data.
Utilizing existing data exchange standard (URL_TO_INSERT_TERM_7194 https://fairsharing.org/search?fairsharingRegistry=Standard) s such as CDI (URL_TO_INSERT_RECORD_7199 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_7203 https://fairsharing.org/3525)  ODM (URL_TO_INSERT_RECORD_7201 https://fairsharing.org/FAIRsharing.ajdxzx)  (Operational data model (URL_TO_INSERT_TERM_7196 https://fairsharing.org/search?recordType=model_and_format) ) and CDI (URL_TO_INSERT_RECORD_7200 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_7204 https://fairsharing.org/3525)  SDM (URL_TO_INSERT_RECORD_7202 https://fairsharing.org/FAIRsharing.mvbjrq) -XML (Study data model (URL_TO_INSERT_TERM_7197 https://fairsharing.org/search?recordType=model_and_format) ) can prove to be very useful. It would be valuable to see what common data elements exist that is utilized in the DMP such as study title, phase, database (URL_TO_INSERT_TERM_7195 https://fairsharing.org/search?fairsharingRegistry=Database) s and protocol version. The key would be to ensure over time we can mine for existing DMP’s and possibly (hopefully) come up with a set of common data elements that can be re-purposed. Since, CROs are a goldmine for such informat (URL_TO_INSERT_TERM_7198 https://fairsharing.org/search?recordType=model_and_format) ion it would be a valuable endeavor to pursue.
7.	**Scoring Mechanisms using Data Maturity Indicators**: 
Start with harmonized data model (URL_TO_INSERT_TERM_7206 https://fairsharing.org/search?recordType=model_and_format) s to leverage standard (URL_TO_INSERT_TERM_7205 https://fairsharing.org/search?fairsharingRegistry=Standard)  terminologies (URL_TO_INSERT_TERM_7207 https://fairsharing.org/search?recordType=terminology_artefact)  and a fixed set of studies for a given therapeutic area. By having a closed environment with a fixed set of variables (list of studies) it will be easier to show FAIR (URL_TO_INSERT_RECORD_7208 https://fairsharing.org/FAIRsharing.WWI10U) ification.
b.	Score (URL_TO_INSERT_RECORD_7209 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_7210 https://fairsharing.org/FAIRsharing.xMmOCL)  at dataset level and eventually by source (if multiple sources are utilized) against the FAIR (URL_TO_INSERT_RECORD_7212 https://fairsharing.org/FAIRsharing.WWI10U)  principles (URL_TO_INSERT_RECORD_7211 https://fairsharing.org/FAIRsharing.WWI10U)  – using a scale range as needed (binary or limits (0 -5) ) 
c.	Persist score (URL_TO_INSERT_RECORD_7213 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_7214 https://fairsharing.org/FAIRsharing.xMmOCL) s over time to understand and detect a change of state and show baseline.
d.	Expand scope to see if scoring can be calculated for ETL pipelines on the fly as ingestion happens across sources. 
e.	Revisit and improvise if needed. This can also act as a KPI to show value of FAIR (URL_TO_INSERT_RECORD_7215 https://fairsharing.org/FAIRsharing.WWI10U) ification

8.	**Ontologies (URL_TO_INSERT_TERM_7216 https://fairsharing.org/search?recordType=terminology_artefact)  and Interoperability**:
 Building, managing, sharing and using ontologies (URL_TO_INSERT_TERM_7220 https://fairsharing.org/search?recordType=terminology_artefact)  are one of the cornerstone principles to enable high quality data and interoperability. ETL processes suffer largely due to poorly defined ontologies (URL_TO_INSERT_TERM_7221 https://fairsharing.org/search?recordType=terminology_artefact)  rule sets. This in part may be due to lack of data understanding, values that were either not map (URL_TO_INSERT_RECORD_7222 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_7225 https://fairsharing.org/FAIRsharing.31385c)  or incorrectly map (URL_TO_INSERT_RECORD_7223 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_7226 https://fairsharing.org/FAIRsharing.31385c) . Even in standard (URL_TO_INSERT_TERM_7217 https://fairsharing.org/search?fairsharingRegistry=Standard) ized systems, using controlled terminologies (URL_TO_INSERT_TERM_7218 https://fairsharing.org/search?recordType=terminology_artefact)  cited at (https://datascience.cancer.gov/resources/cancer-vocabulary/cdisc-terminology) mixed flavors of data values created at the study source can cause confusion. Example a patient’s final treatment disposition status presented as “CP” instead of “COMPLETED”.  Utilizing units of measure have their own set of challenges. It is therefore paramount to understand an ontology (URL_TO_INSERT_TERM_7219 https://fairsharing.org/search?recordType=terminology_artefact)  driven data will not only enable us to align closer to FAIR (URL_TO_INSERT_RECORD_7224 https://fairsharing.org/FAIRsharing.WWI10U)  principles but also mitigate quirky data issues.
In the context of clinical data landscape, the SHARE API facilitated by CDI (URL_TO_INSERT_RECORD_7228 https://fairsharing.org/FAIRsharing.yzagph) SC (URL_TO_INSERT_RECORD_7229 https://fairsharing.org/3525)  harmonizes controlled terminologies (URL_TO_INSERT_TERM_7227 https://fairsharing.org/search?recordType=terminology_artefact)  can be utilized to bind biomedical concepts that describe relationships between data values and both within and across disease areas.

9.	**Dashboards, Persistence and monitoring**:
The ability to visualize data maturity and persist informat (URL_TO_INSERT_TERM_7230 https://fairsharing.org/search?recordType=model_and_format) ion over time to detect or present a positive change in state can add tremendous value; both to sponsors and service providers. Several open-source tools are readily available that can build dynamic charts to present data with fine granularity. An example from the sponsor’s end may be the ability to visualize various CRO / vendor data sources and clearly infer what needs to be improved any by how much. Persistence (of data) pays and in this case can tell us over time which guiding principles will need attention. Note, not all principles or indicators may apply and we may need to build custom indicators depending on business decisions.

## Returns on Investments - Benefits: 

It is important to keep in mind the potential benefits brought about FAIR (URL_TO_INSERT_RECORD_7231 https://fairsharing.org/FAIRsharing.WWI10U) ification processes. We list below just a few of those:

- Capability in quickly adjusting to changing business demands and improvised search (URL_TO_INSERT_RECORD_7232 https://fairsharing.org/FAIRsharing.52b22c)  capabilities, *e.g. a subset of population within a disease area across a specific age group being administered a certain concomitant medications*.
- Enhanced methodology for target identification and drug repurposing.
- Ability to pool data and perform ad-hoc analysis in an effective method. 
- Reduction in study set-up times, high data quality and annotations can provide significant cost savings in the long term.
- Increased capabilities for Artificial Intelligence and Machine Learning applications, as data scientists who rely on high quality search (URL_TO_INSERT_RECORD_7233 https://fairsharing.org/FAIRsharing.52b22c) able data which can be more easily mobilized and re-used to build algorithms – either to screen for compounds or run simulations to understand the drug’s mechanism of action (MOA).

## Key Performance Indicators:

Of course, when considering enacting a policy (URL_TO_INSERT_TERM_7234 https://fairsharing.org/search?fairsharingRegistry=Policy)  change such as rolling out FAIR (URL_TO_INSERT_RECORD_7236 https://fairsharing.org/FAIRsharing.WWI10U)  data management practice and implementing the necessary infrastructure and associated roles, one may wish to define a number of metric (URL_TO_INSERT_TERM_7235 https://fairsharing.org/search?recordType=metric)  or performance indicators to track the effect of such implementation on business operations. In the context of engagement with CROs, the following measurements may be considered to gauge trends and effects.

- **Number of datasets that are empty at source over a specified time interval**, either due to updates to rule definitions or other factors.
-	**Time taken for making data available to end-user** `post patient enrollment` and `data collection (URL_TO_INSERT_TERM_7237 https://fairsharing.org/search?recordType=collection)  at site(s)`.
-	**Number of missing values for `consent data`** especially, when a protocol amendment is completed and secondary consents are not registered. 
-	**Number of patients who have incorrect visit description at treatment or study discontinuation stage** that causes ambiguity in data interpretation.
-	**Scoring values for FAIR (URL_TO_INSERT_RECORD_7238 https://fairsharing.org/FAIRsharing.WWI10U)  data** that indicate:
    -	 what has changed 
    -	 rate of change (*for instance, time taken to achieve score (URL_TO_INSERT_RECORD_7239 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_7240 https://fairsharing.org/FAIRsharing.xMmOCL)  of 3 to 4 on a scale of 5 for Findability*)

---
## Conclusion

With this content, we intended to bring forward the experience gained *"from the trenches"* of data management by highlighting how the FAIR (URL_TO_INSERT_RECORD_7242 https://fairsharing.org/FAIRsharing.WWI10U)  practice could inform key decisions when engaging with Contract Research (URL_TO_INSERT_RECORD_7244 https://fairsharing.org/FAIRsharing.52b22c)  Organizations, from defining tasks, identifying required capabilities to defining metric (URL_TO_INSERT_TERM_7241 https://fairsharing.org/search?recordType=metric) s of performance for tracking trends and effects. This goes beyond the notion of FAIR (URL_TO_INSERT_RECORD_7243 https://fairsharing.org/FAIRsharing.WWI10U)  data and touches on the need to also track and assess the quality of data and processes.

### What to read next?

- {ref}`fcb-assess`
- {ref}`fcb-assess-fair-fairshake`
- {ref}`fcb-assess-fair-automatic-evaluator`
- {ref}`fcb-interop-etl`
- [FAIR+Q: FAIR data and data quality by the Pistoia Alliance](https://doi.org/10.1016/j.drudis.2022.01.006)

````{rdmkit_panel}
````

## Reference
````{dropdown} **Reference**
````

## Authors
````{authors_fairplus}
Gabriel: Writing - Original Draft, Conceptualization
Philippe: Writing - Review & Writing
````

## License
````{license_fairplus}
CC-BY-4.0
````
