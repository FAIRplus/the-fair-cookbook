(fcb-intro-imi-dmgnt)=
# IMI and Data Management

+++
<br/>

----

````{panels}
:container: container-lg pb-3
:column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-1
:card: rounded

<i class="fa fa-qrcode fa-2x" style="color:#7e0038;"></i>
^^^
<h4><b>Recipe metadata</b></h4>
 identifier: <a href="">RX.X</a> 
 version: <a href="">v1.0</a>

---
<i class="fa fa-fire fa-2x" style="color:#7e0038;"></i>
^^^
<h4><b>Difficulty level</b></h4>
<i class="fa fa-fire fa-lg" style="color:#7e0038;"></i>
<i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
<i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
<i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
<i class="fa fa-fire fa-lg" style="color:lightgrey"></i>

---
<i class="fas fa-clock fa-2x" style="color:#7e0038;"></i>
^^^
<h4><b>Reading Time</b></h4>
<i class="fa fa-clock fa-lg" style="color:#7e0038;"></i> 15 minutes
<h4><b>Recipe Type</b></h4>
<i class="fa fa-laptop fa-lg" style="color:#7e0038;"></i> Background Information
<h4><b>Executable Code</b></h4>
<i class="fa fa-play-circle fa-lg" style="color:#7e0038;"></i> No

---
<i class="fa fa-users fa-2x" style="color:#7e0038;"></i>
^^^
<h4><b>Intended Audience</b></h4>
<p><i class="fa fa-user-md fa-lg" style="color:#7e0038;"></i> Principal Investigator</p>
<p><i class="fa fa-database fa-lg" style="color:#7e0038;"></i> Data Manager</p>
<p><i class="fa fa-wrench fa-lg" style="color:#7e0038;"></i> Data Scientist</p>
<p><i class="fa fa-money fa-lg" style="color:#7e0038;"></i> Funder</p>
````

---

Starting with IMI2 and the stipulation of article 29.2 of the new [IMI-JU Grant Agreement](https://www.imi.europa.eu/sites/default/files/uploads/documents/apply-for-funding/call-documents/imi2/Annotated_Model_Grant_Agreement-AGA.pdf) [1], **if they elect to disseminate results**, rather than patent and exploit them, IMI2 grant awardees must ensure that all published peer reviewed publications produced using data generated during IMI projects must be made open access. 

From Call 11 onwards, **all IMI2 projects participate `by default` in the `Horizon 2020 Open Research Data Pilot (ORDP)`**, covered by Article 29.3 of the IMI2 Grant Agreement.
Although IMI2 encourages grant awardees to remain part of the ORDP, grant awardees retain the right to opt-out if necessary.
The reasons for withdrawing from the ORDP should however be documented in the Data Management Plan.

## Publication and Open Access Dissemination 


If the publication route is following, awardees must comply with the following protocol:

1. deposit publications in repositories (online archive);
2. provide open access to publications and related bibliographic metadata.


- The European Commission guidelines encourage authors to retain their copyright and grant adequate licences to publishers. Creative Commons offers useful licensing solutions (e.g. CC BY). This type of licence is a good legal tool for providing open access in its broadest sense.

- The bibliographic metadata must be in a `standard format` and must include all of the following:
    - the terms `Innovative Medicines Initiative 2 Joint Undertaking`, `European Union (EU)`, `Horizon 2020`, and `[insert names of the JU members other than the EU]` and `[insert name(s) of the associated partner(s)]`
    - the `name`, `acronym` and `grant number` of the IMI action/project
    - the `publication date`, and `length of embargo period` if applicable
    - a `persistent identifier`.

The IMI also requires participants to ensure that all projects related publication output is kept up to date via the IMI Participant Portal using 3 possible routes:

1. by registering the publication in the [Open Access Infrastructure for Research in Europe (OpenAIRE)](https://www.openaire.eu/). Each project has its own page on OpenAIRE, featuring project information, related project publications and data sets, and a statistics section.

<!-- ![](https://i.imgur.com/74g21gr.png) -->
<!-- 
<div style="justify-content: center;">
<img src="https://i.imgur.com/xKNIuWl.png" width="750" style="border:1px solid black"/>
</div>

**Figure 1**: The IMI FAIRplus page as viewed from the [OpenAIRE Explore](https://explore.openaire.eu/search/project?projectId=corda__h2020::c856d93d6e57aef0701866afb1876d1b) site -->


<!-- 

```{figure} https://i.imgur.com/xKNIuWl.png
---
height: 650px
name: 
alt: The IMI FAIRplus page as viewed from the OpenAIRE Explore
---
_Open AIRE_ The IMI FAIRplus page as viewed from the site.
```
 -->



3. by encoding the publication’s Digital Object Identifier (DOI)
4. by entering manually the full reference data.

## IMI projects and Data Management Plan (DMP)

When an `IMI grant awardee` elects to remain part of the `Open Research Data Pilot`, the awardee should take all necessary measures to enable third parties to access, mine, exploit, reproduce and disseminate (free of charge for any user) this research data. 
This starts with devising a `Data Management Plan (DMP)` and keeping it up to date throughout the projects, for instance by providing regular (every 6 months) updates.

The initial version of the DMP should be submitted within the first 6 months of start of the project. 

### How to organise the DMP?

- An example of an annotated Horizon 2020 DMP template for Health projects is available [3].

<!-- ![](https://i.imgur.com/WQxwuCn.png) -->
<!-- <div style="flex; justify-content: center;">
<img src="https://i.imgur.com/WQxwuCn.png" width="750" style="border:1px solid black"/>
</div> -->


```{figure} https://i.imgur.com/WQxwuCn.png
---
height: 650px
name: 
alt: An example of an annotated Horizon 2020 DMP template for Health project
---
_DMP_ An example of an annotated Horizon 2020 DMP template for Health project.
```



The DMP should be augmented as the project progresses. Updates should be made whenever significant changes occur, and, at a minimum, in line with project reviews.

Ideally, DMP produced by IMI projects should identify:
> - all the different `data types` (e.g. medical images, gene expression profiles, safety data)
> - a set of well established, community `data standards` (syntax and semantic solutions) 
> - the `data repositories` vetted by the community or endorsed by the funding agencies or required by the regulators to ensure data archival and data review.


--- 

### Resources to use to help build a DMP for an IMI project


**1. FAIRsharing:**


This is an Elixir UK resources acting as a one stop shop for finding out about Data Standards, Vocabularies, Ontologies and Data repositories implementing those standards. A highly curated resources, it provides powerful search capabilities and a powerful API which can be used to build DMP.

<!-- <div style="justify-content: center;"><img src="https://i.imgur.com/forEgHB.png" width="750" style="border:1px solid black"/></div> -->

```{figure} https://i.imgur.com/forEgHB.png
---
height: 650px
name: FAIRsharing
alt: the FAIRsharing catalogue of data management resources
---
_FAIRsharing_ The FAIRsharing catalogue of data management resources.
```



---


**2. ELIXIR Deposition Databases for Biomolecular Data**

<!-- <div style="justify-content: center;">
<img src="https://i.imgur.com/glgIArj.png" width="750" style="border:1px solid black"/>
</div> -->

```{figure} https://i.imgur.com/glgIArj.png
---
height: 650px
name: ELIXIR Deposition Databases
alt: the ELIXIR Deposition Databases for Biomolecular Data
---
_Elixir_ The ELIXIR Deposition Databases for Biomolecular Data.
```



---


**3. Data Stewardship Wizard**

This is an example of a tool produced by Elixir-CZ to help Scientists and Researchers create a Data Management Plan.

<!-- <div style="justify-content: center;">
<img src="https://i.imgur.com/k74XsJ6.png" width="750" style="border:1px solid black"/>
</div> -->


```{figure} https://i.imgur.com/k74XsJ6.png
---
height: 650px
name: Data Stewardship Wizard
alt: Data Stewardship Wizard
---
_DSW_ Data Stewardship Wizard
```


---


**4. Existing Data Management Plans: the IMI Resolute example**

Since DMP are now a default deliverable of IMI2 projects, Zenodo repository offers a good source of such documents. Among all the DMPs deposited to the repository, [IMI RESOLUTE]() has produced a very robust document, of which 2 screenshots are provided below:

<!-- <div style="justify-content: center;">
<img src="https://i.imgur.com/eTVZjq4.png" width="750" style="border:1px solid black"/>
</div>
 -->

```{figure} https://i.imgur.com/eTVZjq4.png
---
height: 650px
name: Data Management Plan by IMI Resolute
alt:  Data Management Plan by IMI Resolute
---
_DMP Resolute_  Data Management Plan by IMI Resolute
```


The following screenshot provides a good example of layout which could be exploited owing the structure is provides for including critical information describing a data type and data assets generated by an IMI project.

<!-- <div style="justify-content: center;">
<img src="https://i.imgur.com/s156swK.png" width="750" style="border:1px solid black"/>
</div> -->



```{figure} https://i.imgur.com/s156swK.png
---
height: 650px
name: Data Stewardship Wizard detail
alt: Data Stewardship Wizard detail
---
_DMP Resolute 2_ Data Management Plan by IMI Resolute detail
```

---

## Conclusion

This piece aimed to provide some background to Data Management activities in the context of Innovative Medicine Initiative funded projects.
Key resources have been highlighted as well as examples of Data Management Plans.

> ### What to read read next?
> * [FAIR in the context of IMI]()
> * [Preparing to engage with FAIRplus]()


---


## Reference

1. https://www.imi.europa.eu/resources-projects/open-access-and-data-management-projects
2. https://www.imi.europa.eu/sites/default/files/uploads/documents/apply-for-funding/call-documents/imi2/Annotated_Model_Grant_Agreement-AGA.pdf
3. https://ec.europa.eu/research/participants/data/ref/h2020/other/gm/reporting/h2020-tpl-oa-data-mgt-plan-annotated_en.pdf
4. FAIRsharing.org

---

## Authors

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Philippe Rocca-Serra |  University of Oxford, Data Readiness Group| [0000-0001-9853-5668](https://orcid.org/orcid.org/0000-0001-9853-5668) | Writing - Original Draft|
|Susanna Assunta Sansone|University of Oxford, Data Readiness Group| [0000-0001-5306-5690](https://orcid.org/orcid.org/0000-0001-5306-5690)|Writing - Original Draft|
||||Review|
||||Review|

---

## License

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png" height="20"/></a>

