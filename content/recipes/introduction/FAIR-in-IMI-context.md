(fcb-intro-fair-imi)=
# FAIR in the context of IMI

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

___

## Introduction

In the recipes leading to this section, the IMI organization and mode of operation has been outlined. The overview also highlighted the `default opt-in` to the `Open Research Data Pilot` of the IMI for all new funded projects, from call 11 and onwards.
At this stage, the `Open Research Data Pilot` essentially means ensuring the Research Data Management Plans are put in place and that publications are made available under `open access` conditions, if projects have agreed to disseminate their results.
As far as data are concerned, the adoption of the FAIR principles is aspirational and therefore procedures for realization such ambitions are being tested and evaluating. This section details some of these plans.



## IMI and the FAIR principles


IMI builds on the [Guidelines on FAIR Data Management in Horizon 2020](https://ec.europa.eu/research/participants/data/ref/h2020/grants_manual/hi/oa_pilot/h2020-hi-oa-data-mgt_en.pdf) to articulate its suppport and endorsement of the FAIR principles (Wilkinson et al, 2016).

Briefly, IMI states the following:
> Research data should be:
> - identified in a persistent manner using community conventions
> - described using sufficiently rich metadata;
> - stored in such a way that they can be accessed by humans and machines;
> - structured in such a way that they can be combined with other data sets;
>- [x] licensed or have terms-of-use that spell out how they can be used by others.


## What does it mean in practice?

Implementing the FAIR principles is no mean feat and will most certainly represents a significant investment to change the current practice and the prevalent culture of non-disclosure/non-release.
It is therefore important to contrast the projected expenditure to the estimated costs of not having FAIR data in the first place. A report by the European Commission, back in 2018, estimated that failing to have FAIR data costs the European economy at least **€10.2bn every year** [ref].
    

With IMI funding such a diverse variety of projects, ranging from `drug discovery` or `vaccine development`, to `drug safety assessment` and to `clinical trials` and `observational studdies`, it is obvious that a `one size fits all` approach can not work and that **context aware FAIRification processes** have to be developed, to meet the specifics of IMI projects and their needs.

___

### FAIRification: Data Readiness and Big Data

With IMI2 under way, the EU is consenting a significant effort towards supporting research and discovery in the context of health and healthcare, for the benefit of the EU citizen but also in support of EU industry.
Owing to their objective and size, some IMI projects are emblematic and illustrative of the challenges ahead. 

* In the context of `drug discovery`, the [IMI OpenPhacts project](http://www.openphacts.org), obtaining €20.1 Million, trailblazed the use to RDF/Linked Data to represent chemical and drug information knowledge to achieve 	Semantic interoperability for drug discovery and to `design methods for common standards and sharing of data for more efficient drug development and patient treatment in the future`


* For instance, in the context of `health data`, the [IMI European Health Data and Evidence Network (EHDEN) project](https://www.ehden.eu/), with a dotation of €28.9 Million,  ambitions to make available to researchers the data of over 100 millions european patients, in a privacy preserving fashion. To this end, an `Harmonization fund` of €18 Million is available so standardized against [OMOP](https://www.ohdsi.org/data-standardization/the-common-data-model/).

<!-- ![](https://i.imgur.com/Z9eiWHL.png) -->


<!-- <div style="justify-content: center;">
<img src="https://i.imgur.com/Z9eiWHL.png" style="border:1px solid black"/>
</div> -->


```{figure} https://i.imgur.com/Z9eiWHL.png
---
height: 450px
name: Innovative Medicine Initiative
alt: Innovative Medicine Initiative.
---
_IMI_ Innovative Medicine Initiative.
```


* In the context of 'blood cancer', the [IMI Harmony](https://www.imi.europa.eu/projects-results/project-factsheets/harmony) received €42 Million to harmonize data from over 45000 patients affected by common blood cell malignancies using standards such as [OMOP](https://www.ohdsi.org/data-standardization/the-common-data-model/), [LOINC]() and [SNOMED]().


<!-- ![](https://i.imgur.com/pNgpTA1.jpg) -->

<!-- <div style="justify-content: center;">
<img src="https://i.imgur.com/mXKjpAR.jpg"  style="border:1px solid black"/>
</div>
 -->

```{figure} https://i.imgur.com/mXKjpAR.jpg
---
height: 450px
name: IMI Harmony
alt: 
---
_IMI Harmony_ received €42 Million to harmonize data from patients affected by common blood cell malignancies using standards.
```

___

    
### The IMI FAIRplus project

In 2019, the IMI awarded funds to a project whose sole purpose is to devise, define and document FAIRification protocols for IMI funded project. The [IMI FAIRplus](https://fairplus-project.eu) received €7.8 Mn (0.22% of the total IMI2 budget) to support the goal of documenting the FAIRification of 20 IMI project generated datasets.

The main outcome of the FAIRplus project is the present [FAIRplus Cookbook](https://fairplus.github.io/the-fair-cookbook/intro.html), which aims to provide a set of representative FAIRification process supporting various context and showing cases how data standardization operates.

The so-called `recipes` will ranges from simple protocols (e.g. computing hash function for file fingerprinting) to very advanced ones allowed code execution, carrying an ETL process and a data integration challenge using semantic web technologies such SPARQL federated querying to perform a `semantic mash up` against a well documented `query case`.

___


## Conclusion

This piece covered how the FAIR principles can be harnessed in the context of IMI funding programs and what it means for IMI funded projects which will elect to collaborate with IMI FAIRplus.
The section also outlined how IMI FAIRplus can leverage sister projects to scale up and reach out to standardization domains located outside its immediate field of action.

> ### What to read read next?
> * [the IMI FAIRplus FAIRification Process overview](https://www.TODO.todo)


___

## Reference

1. https://www.imi.europa.eu/news-events/newsroom/when-data-fair-citizens-ultimately-reap-benefit
2. [Guidelines on FAIR Data Management in Horizon 2020](https://ec.europa.eu/research/participants/data/ref/h2020/grants_manual/hi/oa_pilot/h2020-hi-oa-data-mgt_en.pdf)
3. Wilkinson, M., Dumontier, M., Aalbersberg, I. et al. The FAIR Guiding Principles for scientific data management and stewardship. Sci Data 3, 160018 (2016). https://doi.org/10.1038/sdata.2016.18
4. https://FAIRplus-project.eu
5. [OMOP](https://www.ohdsi.org/data-standardization/the-common-data-model/)
6. [LOINC](https://loinc.org/)
7. [SNOMED](https://www.snomed.org)

___

## Authors

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Philippe Rocca-Serra |  University of Oxford, Data Readiness Group| [0000-0001-9853-5668](https://orcid.org/orcid.org/0000-0001-9853-5668) | Writing - Original Draft|
|Susanna Assunta Sansone|University of Oxford, Data Readiness Group| [0000-0001-5306-5690](https://orcid.org/orcid.org/0000-0001-5306-5690)|Writing - Original Draft|
||||Review|
||||Review|

___

## License

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>



