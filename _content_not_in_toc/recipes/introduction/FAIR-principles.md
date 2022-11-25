(fcb-intro-fair-principles)=
# What are the FAIR Principles?



---

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

## Introduction

The goal of this section is to go over each of the principles for FAIR data management as described by Wilkinson and coworkers in their Nature Springer Scientific Data manuscript published in 2016
<!-- {cite}`Wilkinson2016FAIR,Wilkinson2019Evaluation`. -->
Owing to the success of the principles, now endorsed by funding agencies (IMI, Wellcome Trust to name only two), but also by the G20 and by industry leaders, it is essential to remind the reader about those.



## The FAIR Guiding Principles

<!-- <div>
	<img src="https://i.imgur.com/RxkoNed.png" width="550" style="border:1px solid black;align:center"/>
</div>

doi: 10.1038/sdata.2016.18
 -->

```{figure} https://i.imgur.com/RxkoNed.png
---
height: 650px
name: the FAIR principles
alt: the cover page for the FAIR principle article as published in Scientific Data. https://doi.org/10.1038/sdata.2016.18
---
_The FAIR Principles_ the cover pages for the FAIR principle articles as published in Scientific Data. https://doi.org/10.1038/sdata.2016.18.
```


<!-- 
````{panels}
:container: container-lg pb-3
:column: col-lg-12 p-2
:card: rounded


```{tabbed} F. 

> To be Findable:
>F1. (meta)data are assigned a **globally unique and persistent identifier**
>
>F2. data are described with **rich metadata** (defined by R1 below)
>
>F3. metadata clearly and explicitly include the identifier of the data it describes
>
>F4. (meta)data are registered or **indexed in a searchable resource**
```

```{tabbed} A.
> To be Accessible:
>A1. (meta)data are retrievable by their identifier using **a standardized communications protocol**
>
>A1.1 the protocol is **open, free, and universally implementable**
>
>A1.2 the protocol allows for an authentication and authorization procedure, where necessary
>
>A2. **metadata are accessible**, even when the data are no longer available
```

```{tabbed} I. 
> To be Interoperable:
>I1. (meta)data use a **formal, accessible, shared, and broadly applicable language for knowledge representation**.
>
>I2. (meta)data use **vocabularies that follow FAIR principles**
>
>I3. (meta)data include **qualified references** to other (meta)data
```

```{tabbed} R.
> To be Reusable:
>R1. meta(data) are richly described with a **plurality of accurate and relevant attributes**
>
>R1.1. (meta)data are released with a **clear and accessible data usage license**
>
>R1.2. (meta)data are associated with **detailed provenance**
>
>R1.3. (meta)data meet domain-relevant **community standards**
```
```` -->


## The FAIR principles and FAIRplus

The principles will be the organizing principle for the FAIRplus Cookbook. While the book itself can be search in many different ways and its content exposed through a number of angles, personas and facets, the main `Table of Content` organizes a number of atomic recipes around of the principles and their associated sub themes. 


## FAIRplus Recipe & FAIR principles

<!-- ````{panels}
:container: container-lg pb-3
:column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-1
:card: rounded

<i class="fa fa-search fa-2x" style="color:#fc7a4a;"></i>
^^^
<h4><b>FINDABILITY</b></h4>
<p>TODO: add text here</p>
---

<i class="fa fa-cog fa-lg" style="color:#fc7a4a;"></i>
^^^
<h4><b>Search Engine Optimitization</b></h4>
<p>TODO: add text here</p>
---

<i class="fa fa-cog fa-lg" style="color:#fc7a4a;"></i>
^^^
<h4><b>Open Archive Deposition</b></h4>
<p>TODO: add text here </p>
---
<i class="fa fa-cog fa-lg" style="color:#fc7a4a;"></i>
^^^
<h4><b>Annotation</b></h4>
<p>TODO: add text here</p>
````

````{panels}
:container: container-lg pb-3
:column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-1
:card: rounded

<i class="fa fa-cloud fa-2x" style="color:#8038d1;"></i>
^^^
<h4><b>ACCESSIBILITY</b></h4>
<p>TODO: add text here</p>
---

<i class="fa fa-cog fa-lg" style="color:#8038d1;"></i>
^^^
<h4><b>Access condition</b></h4>
<p>TODO: add text here</p>
---

<i class="fa fa-cog fa-lg" style="color:#8038d1;"></i>
^^^
<h4><b>License selection</b></h4>
<p>TODO: add text here</p>
---

<i class="fa fa-cog fa-lg" style="color:#8038d1;"></i>
^^^
<h4><b>Standards</b></h4>
<p>TODO: add text here</p>
````


````{panels}
:container: container-lg pb-3
:column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-1
:card: rounded
---

<i class="fa fa-puzzle-piece fa-2x" style="color:#300861;"></i>
^^^
<h4><b>INTEROPERABILITY</b></h4>
<p>TODO: add text here</p>
---

<i class="fa fa-cog fa-lg" style="color:#300861;"></i>
^^^
<h4><b>Access condition</b></h4>
<p>TODO: add text here</p>
---

<i class="fa fa-cog fa-lg" style="color:#300861;"></i>
^^^
<h4><b>License selection</b></h4>
<p>TODO: add text here</p>
---

<i class="fa ffa-cog fa-lg" style="color:#300861;"></i>
^^^
<h4><b>Standards</b></h4>
<p>TODO: add text here</p>
````

````{panels}
:container: container-lg pb-3
:column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-1
:card: rounded
---

<i class="fa fa-recycle fa-2x" style="color:#7e0038;"></i>
^^^
<h4><b>REUSABILITY</b></h4>
<p>TODO: add text here</p>
---

<i class="fa fa-cog fa-lg" style="color:#7e0038;"></i>
^^^
<h4><b>Access condition</b></h4>
<p>TODO: add text here</p>
---

<i class="fa fa-cog fa-lg" style="color:#7e0038;"></i>
^^^
<h4><b>License selection</b></h4>
<p>TODO: add text here</p>
---

<i class="fa fa-cog fa-lg" style="color:#7e0038;"></i>
^^^
<h4><b>Standards</b></h4>
<p>TODO: add text here</p>
```` -->

---
 
## Conclusions

This section should be seen as a refresher for any one unclear about the FAIR principles. Now that key background information has been provided, shining a light on an number of ethical issues driving both the development and implementation of the FAIR principles in the context of Life Science data as well as learning about the overall FAIRification process represent a natural progression in the content of the FAIR Cookbook.

> ### What to read read next?
> * [The ethical values of FAIR](./FAIRplus-values)
> * [Assessing FAIRness](../assessing-fairness)
> * [What is IMI](./what-is-IMI.md)

---

## Reference


<!-- ```{bibliography} ./fair.bib
  :style: alpha
``` -->

<!-- 
1. Wilkinson, M., Dumontier, M., Aalbersberg, I. et al. The FAIR Guiding Principles for scientific data management and stewardship. Sci Data 3, 160018 (2016). https://doi.org/10.1038/sdata.2016.18
2. Wilkinson, M.D., Dumontier, M., Jan Aalbersberg, I. et al. Addendum: The FAIR Guiding Principles for scientific data management and stewardship. Sci Data 6, 6 (2019). https://doi.org/10.1038/s41597-019-0009-6 -->

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

````{license_fairplus}
CC-BY-4.0
````



