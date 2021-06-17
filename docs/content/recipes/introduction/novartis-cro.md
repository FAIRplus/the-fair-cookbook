# Practical Considerations for CROs to align with FAIR data principles (and tips to mitigate ETL issues)

___

<div class="row">

  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-qrcode fa-2x" style="color:#7e0038;"></i>
        <h4><b>Recipe metadata</b></h4>
        <p> identifier: <a href="">TBA</a> </p>
        <p> version: <a href="">v0.1</a> </p>
      </div>
    </div>
  </div>
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-fire fa-2x" style="color:#7e0038;"></i>
        <h4><b>Difficulty level: *****</b></h4>
        <i class="fa fa-fire fa-lg" style="color:#7e0038;"></i>
        <i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
        <i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
        <i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
        <i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
  <!--       <p><span data-v-013baba1="" title="" class=""><svg data-v-013baba1="" viewBox="0 0 16 16" width="1em" height="1em" focusable="false" role="img" alt="icon" xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi-bar-chart-fill b-icon bi medium-level"><g data-v-013baba1=""><rect width="4" height="5" x="1" y="10" rx="1"></rect><rect width="4" height="9" x="6" y="6" rx="1"></rect><rect width="4" height="14" x="11" y="1" rx="1"></rect></g></svg> Medium </span></p> -->
      </div>
    </div>
  </div>  
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-clock-o fa-2x" style="color:#7e0038;"></i>
        <h4><b>Reading Time</b></h4>
        <p><i class="fa fa-clock-o fa-lg" style="color:#7e0038;"></i> 15 minutes</p>
        <h4><b>Recipe Type</b></h4>
        <p><i class="fa fa-globe fa-lg" style="color:#7e0038;"></i> Perspective</p>
        <h4><b>Executable Code</b></h4>
        <p><i class="fa fa-play-circle" style="color:#fc7a4a;"></i> No</p>
      </div>
    </div>
  </div>
  <div class="column">
    <div class="card">
      <div class="container">
        <i class="fa fa-group fa-2x" style="color:#7e0038;"></i>
        <h4><b>Intended Audience</b></h4>
        <p> <i class="fa fa-database fa-lg" style="color:#7e0038;"></i> Data Managers </p>
        <p> <i class="fa fa-wrench fa-lg" style="color:#7e0038;"></i> Business Analysts </p>
<p> <i class="fa fa-cogs fa-lg" style="color:#7e0038;"></i> Data Scientists </p>     <p> <i class="fa fa-cogs fa-lg" style="color:#7e0038;"></i> Scientific Product Managers </p> 
<!--         <p> <i class="fa fa-terminal fa-lg" style="color:#7e0038;"></i> System Administrators</p>  -->       
      </div>
    </div>
  </div>
</div>


## Main Objective: 

### Background
It is undeniable that there is an ever-growing need to manage data in terms of both volume and complexity within the life sciences sector. Technological advances have certainly paved the way to handle large volumes of data in the past decade or so. However, the ability to `semantically` connect and exchange information within and between  organizations remains a challenge to most part even today. Coupled with the need to manage compliances, regulations, newer discoveries in disease areas and audits, the ability to manage, store and access data is certainly an uphill task.
### Goals
This recipe intends to enumerate ideas that one should consider within the context of Contract Research Organizations (CRO) and how adopting and applying FAIR principles will generate a higher ROI over the long run. We also will explore key scenarios in mitigating some of the repeated ETL pains that CROs face on a regular basis when managing data in the life sciences sector.
While the recipe tries to encompass research topics, the focus remains within the clinical landscape.

---


## Origins, purpose and evolution:
CROs have their roots dating back to early 1980s and even earlier in some cases. Providing services to pharmaceuticals companies in the broader areas of animal testing eventually panned out to a full-blown suite of services including `data collection`, `data management` and `statistical consulting`. However, with decades of expertise under their belts, these niche organizations have evolved into a dominant force that is more or less capable of doing all the work of the sponsor with oversight as needed.

### Challenges:
One must recall the promises of lower execution costs, high data quality and ability to scale on demand in terms of resources without any (or slight) budget constraints (largely) has made CROs a go-to service provider. With the burden of proof lying on the shoulders of CROs, we run into the age-old question of cost versus time analysis, which sets in motion a series of events. Recall that CROs are not sponsor specific but rather service providers. Having said the above, listed below are a few challenges faced by CROs from a data management standpoint:

1.	Time to delivery vs cost Ratio
2.	Expertise retention and turn cycles
3.	Poor data quality and inadequate validation frameworks (at source)
4.	Lack of metadata  or lack of metadata enrichment thereof
5.	Poorly constructed or mis-handled data management plans (DMP)
6.	Lack of resources or lack of understanding of data itself.
7.	Infrastructure problems
8.	Delivery models
    -	FSP – Functional Services Provider (almost extinct) 
    - Consulting resources that are time limited
9.	Issues with (extraction transform load (ETL) ) setups and pain areas for mitigation, moving towards FAIR
    -	Data un-availability either due to poor DHP (Data Handling Plan) policies or set up
    -	Lack of coherence when it comes to data types across a portfolio of studies
    -	Lack of adherence to standardized metadata or poorly defined metadata
    -	Lack of data persistence (metadata outliving the data)
    -	Infrastructure and legacy programming techniques
    -	Lack of adherence to controlled terminologies or ontologies
    -	Change in metadata model over time to accommodate complex business decisions (variability)

### Considerations:
1.	Understanding cost versus time: Data FAIRification is still a topic that is gaining traction within scientific communities since most of its roots come from research. Research organizations working with Pharma are very cost-driven and tend to skim out topics, which do not provide a strong ROI in the near short term. Multiply this by the fact that such organizations come in all sizes and are located globally to primarily drive down cost. The ability to employ or divert resources to engage in data FAIRification may not justify the cost vs time metric. We also need to consider that CROs are driven by sponsor demands and it would be more prudent to have a top-down approach to empower them to build a cultural and process shift towards such endeavors. 

2.	Partner with Standard Developing Organisation’s and contribute towards open tooling: Building and managing ontologies are a key driver in enabling a FAIR data environment since the very essence of binding domains (topics of interest) rely heavily on uniform and shared concepts that can be mapped and linked across in a systematic method between siloed data entities. Open Tooling and working with Standards Data Organizations (SDOs) enables CROs in the context of data management to develop a deeper understanding of the industry workings and demonstrate industry expertise within such domains of interest.

    - Precompetitive initiatives, examples of which can be found under Pistoia Alliance initiative represent an outstanding value for money. Efforts such as OpenTargets, CTTV about target identifications are successful examples, as are initiatives in the area of semantics resources. Indeed, needs for shared vocabularies are huge in domain such as biological reagents (antibodies, cell lines, constructs) but also standardized ways to describe assays. Resources such as antibody registry, Cellosaurus, addgene, but also bioassayexpress (https://www.bioassayexpress.com/) represent areas where Pharma and CRO cooperating on these topics would be considerable gains.

    - TDF tool (Test data Factory) from PHUSE’s Shared Code Analyses Working Group (SCAWG) is yet another initiative; dynamically build synthetic datasets for testing out solutions driven by CDISC data standards particularly SDTM and ADaM. This is a very novel concept and can enable research organizations and others as a whole to test out varied scenarios with clearly documented deviations from data standards.

    - FAIR toolkit (https://fairtoolkit.pistoiaalliance.org/) & FAIR Evaluator are both excellent resources to gain a deeper perspective on the “HOW” aspect of data FAIRification. The toolkit can enable service providers such as CRO’s to utilize real world use cases implemented by Pharmaceuticals and research alike. It also encompasses methods such as tools and trainings allowing one to deep-dive into implementation aspects of FAIR principles. More Details on FAIR Evaluator can be found at https://fairsharing.github.io/FAIR-Evaluator-FrontEnd/#!/about 

3.	The case for cultural mindset shift:
It is evident that with changes comes challenges and the move towards being FAIR is no exception. Cost versus time ratio is possibly not the only factor that could prove to be a hurdle. Resistance to data sharing, existing infrastructure that may be FAIR to some degree (in most cases ‘F’) or use cases that may be specific enough to not require adopting FAIR are other factors that need to be considered. Collaborative effort between stakeholders and CRO’s combined with a top-down mandate can enable us to realize a stronger ROI, ability to share data and a measurable metric to show pre and post FAIRification combined with visible benefits will pave the way for easier adoption and implementation of FAIR principles. 

4.	Emphasize on building critical in-house data skills:
There is an upward growth trend of skills deficit not due the lack of resources rather; the role of data service providers are usually limited to a fixed scope of deliverables, which is time, constrained. While the current skills can manifest a set of experts in their own rights, the vision to build a FAIR future requires constant collaboration and up-skilling. It is therefore vital to have a deeper understanding of topics such as open standards protocols (http, w3c), role that ontologies play in describing data, scope of URI’s and IRI’s in the clinical context, RDF and what linked data means and how it binds it all to-gether in the semantic landscape. This requires a lot of time and investment but is a necessity for a FAIRer future.


5.	Scope and Data Cleansing: 
It may be a worthwhile effort to narrow down scope of data that requires FAIRification prior to embarking on this journey. This can also mean that we can identify the list of potential studies that require additional curation which can range from metadata enrichment, handling missing values and applying necessary terminologies as agreed (based on prior decided set such as UCUM).The scope can also be limited to a group of indications or TA (leverage TAUG’s from CFAST) and then bind with the data model for machine readability (key stone for interoperability). 

6.	Machine Readable DMP (Data Management Plans):
The DMP is probably the most vital document that containing key information regarding how data will be created, collected, transferred and utilized. It also entails out detailed descriptions about the collection mechanisms, audit procedures and key study protocol related information. Having a machine readable DMP can show immediate and significant cost savings and in the process aim for ‘FAIR by design’, which also is a living document throughout the lifecycle of the data.
Utilizing existing data exchange standards such as ODM (Operational data model) and SDM-XML (Study data model) can prove to be very useful. It would be valuable to see what common data elements exist that is utilized in the DMP such as study title, phase, databases and protocol version. The key would be to ensure over time we can mine for existing DMP’s and possibly (hopefully) come up with a set of common data elements that can be re-purposed. Since, CRO’s are a goldmine for such information it would be a valuable endeavor to pursue.

7.	Utilizing Data Maturity Indicators as Scoring Mechanisms:There are a series of indicators designed by both IMI FAIRplus WG and RDA-WG (Research Data Alliance - Working group). One can in essence define these as principles wherein; each principle is mapped to one or more indicator/s. An example would be as referenced here (https://fairplus.github.io/the-fair-cookbook/content/recipes/findability/identifiers.html#fcb-find-identifiers). Each dataset or digital object in essence will contain a persistent identifier that one can use to retrieve information about that dataset perpetually. However, what identifiers are to be chosen or implementation depends on the community. A binary value can be assigned to indicate whether the datasets have passed or failed the indicator test or it can be measured as levels of maturity (0...5) . A collection of such tests can be mapped as scores for a given data asset (dataset, digital object, images etc..) that can be persisted to show maturity over time. Note: The term "maturity" here applies to the maturity of the dataset and not how data is managed within an enterprise. Data Stewardship, Data Governance, Data Operations and other process drivers would still be present as a foundational layers to define what "maturity" means within an organization. An example of an use case can be as follows:

a. Start with known harmonized data models to leverage standard terminologies for a small subset of studies for a therapeutic area. 
b. Measure score at dataset level for each indicator/s as applicable and eventually by source. 
c. Persist scores over time to understand and detect a change of state and show baseline. 
d. Expand scope to see if this scoring mechanism can be calculated for ETL pipelines on the fly at ingestion.
e. Revisit and improvise if needed.
f. Use scores to understand where remedial actions are needed to improve overall data quality.

In essence, we are enriching the data asset/s with rich metadata (community defined) for machine readability to support knowledge discovery. 

8.	Ontologies and Interoperability:
 Building, managing, sharing and using ontologies are one of the cornerstone principles to enable high quality data and interoperability. ETL processes suffer largely due to poorly defined ontologies rule sets. This in part may be due to lack of data understanding, values that were either not mapped or incorrectly mapped. Even in standardized systems, using controlled terminologies cited at (https://datascience.cancer.gov/resources/cancer-vocabulary/cdisc-terminology) mixed flavors of data values created at the study source can cause confusion. Example a patient’s final treatment disposition status presented as “CP” instead of “COMPLETED”.  Utilizing units of measure have their own set of challenges. It is therefore paramount to understand an ontology driven data will not only enable us to align closer to FAIR principles but also mitigate quirky data issues.
In the context of clinical data landscape, the SHARE API facilitated by CDISC harmonizes controlled terminologies can be utilized to bind biomedical concepts that describe relationships between data values and both within and across disease areas.

9.	Dashboards, Persistence and monitoring:
The ability to visualize data maturity and persist information over time to detect or present a positive change in state can add tremendous value; both to sponsors and service providers. Several open-source tools are readily available that can build dynamic charts to present data with fine granularity. An example from the sponsor’s end may be the ability to visualize various CRO / vendor data sources and clearly infer what needs to be improved any by how much. Persistence (of data) pays and in this case can tell us over time which guiding principles will need attention. Note, not all principles or indicators may apply and we may need to build custom indicators depending on business decisions.

## Returns on Investments / Benefits: 

 - Legacy repository of semi-curated or not well formed data assets are a goldmine of information un-used. Strategic partnerships between research organizations and    Pharmaceutical R&D to align with FAIR principles can unlock true value of these data assets. This however; requires significant time and careful evaluation is recommended.
 - Enables scientists to develop associations between data assets between or within trial drug products with knowledge graphs more swiftly. 
 - Reduced clinical study set up times, high data quality and annotations to convert corpus to structured data can provide significant cost savings in the long term.
 - Increased capabilities for AI and ML applications for data scientists who rely on high quality searchable data which can be re-used to build algorithms – either to screen    for compounds or run simulations to understand the drug’s MOA (mechanism of action).
 - Target identification and drug re-purposing cycle times can be reduced.


## Key Performance Indicators:

- Measured reduction in cycle times for patient enrollment and study setup. 
- Surveyed results indicating awareness of FAIR adoption and implementation across organization. These surveys could be designed specifically to accomodate domain specific results to have better audience reachability.
- Increased data quality avoiding some of the common pitfalls when it comes to regular ETL problems.
       - a. Patient Informed consent and protocol amendments that involves secondary consents with missing values.
       - b. Incorrect visit description at treatment or study discontinuation stage that causes ambiguity in data interpretation.
       - c. Missing or incorrect controlled vocabularies
       - d. Ambiguosly described Patient Identifiers causing potential downstream issues for analytics. 

- Clear description of maturity levels that are governed by data management principles and which are in turn are mapped to FAIR indicators.
- Change of state in FAIRness of digital assets between maturity levels.
- Rate of change of FAIRness to indicate how, when are where data quality is being improved.

---
## Conclusion

TODO 
### What to read next

https://fairplus.github.io/the-fair-cookbook/content/recipes/findability/identifiers.html#fcb-find-identifiers


___
## Authors:

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Gabriel N Backinathan |  Novartis | [0000-0001-6283-1166](https://orcid.org/0000-0001-6283-1166) | Writing - Original Draft |


___


## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
