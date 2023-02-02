(fcb-fair-principles)=
# What are the FAIR Principles?



<!-- ````{panels_fairplus}
:identifier_text: RX.X
:identifier_link: 'https://example.com'
:difficulty_level: 1
:recipe_type: background_information
:reading_time_minutes: 15
:intended_audience: principal_investigator, data_manager, data_scientist, funder
:maturity_level: 2 
:maturity_indicator: 1, 2
:has_executable_code: nope
:recipe_name: Introducing the FAIR Principles
```` -->

## Introduction

The goal of this section is to go over each of the principles for FAIR (URL_TO_INSERT_RECORD_7352 https://fairsharing.org/FAIRsharing.WWI10U)  data management as described by Wilkinson and coworkers in their Nature Springer Scientific Data (URL_TO_INSERT_RECORD_7351 https://fairsharing.org/FAIRsharing.w4k4nr)  manuscript published in 2016
<!-- {cite}`Wilkinson2016FAIR,Wilkinson2019Evaluation`. -->
Owing to the success of the principles, now endorsed by funding agencies (IMI, Wellcome Trust to name only two), but also by the G20 and by industry leaders, it is essential to remind the reader about those.



## The FAIR Guiding Principles



````{dropdown} **The FAIR principles manuscript**

```{figure} https://i.imgur.com/RxkoNed.png
---
height: 650px
name: the FAIR (URL_TO_INSERT_RECORD_7354 https://fairsharing.org/FAIRsharing.WWI10U)  principles (URL_TO_INSERT_RECORD_7353 https://fairsharing.org/FAIRsharing.WWI10U) 
alt: the cover page for the FAIR (URL_TO_INSERT_RECORD_7356 https://fairsharing.org/FAIRsharing.WWI10U)  principle article as published in Scientific Data (URL_TO_INSERT_RECORD_7355 https://fairsharing.org/FAIRsharing.w4k4nr) . https://doi.org/10.1038/sdata.2016.18
---
_The FAIR (URL_TO_INSERT_RECORD_7359 https://fairsharing.org/FAIRsharing.WWI10U)  Principles (URL_TO_INSERT_RECORD_7358 https://fairsharing.org/FAIRsharing.WWI10U) _ the cover pages for the FAIR (URL_TO_INSERT_RECORD_7360 https://fairsharing.org/FAIRsharing.WWI10U)  principle articles as published in Scientific Data (URL_TO_INSERT_RECORD_7357 https://fairsharing.org/FAIRsharing.w4k4nr) . https://doi.org/10.1038/sdata.2016.18.
```

````


<!-- <div>
	<img src="https://i.imgur.com/RxkoNed.png" width="550" style="border:1px solid black;align:center"/>
</div>

doi: 10.1038/sdata.2016.18
 -->

````{dropdown} **Findability**
:open:
> **To be Findable:**

>F1. (meta)data are assigned a **`globally unique and persistent identifier`**
>
>F2. data are described with **`rich metadata`** (defined by R1 below)
>
>F3. metadata **`clearly and explicitly include the identifier of the data it describes`**
>
>F4. (meta)data are registered or **`indexed in a searchable resource`**
````

````{dropdown} **Accessibility**
:open:

> **To be Accessible:**

>A1. (meta)data are retrievable by their identifier using **`a standardized communications protocol`**
>
>A1.1 the protocol is **`open, free, and universally implementable`**
>
>A1.2 the protocol allows for an **`authentication and authorization procedure`**, where necessary
>
>A2. **`metadata are accessible`**, even when the data are no longer available

````

````{dropdown} **Interoperability**
:open:

> **To be Interoperable:**

>I1. (meta)data use a **`formal, accessible, shared, and broadly applicable language for knowledge representation`**.
>
>I2. (meta)data use **`vocabularies that follow FAIR principles`**
>
>I3. (meta)data include **`qualified references to other (meta)data`**
````

````{dropdown} **Reusability**
:open:

> **To be Reusable:**

>R1. meta(data) are **`richly described with a plurality of accurate and relevant attributes`**
>
>R1.1. (meta)data are released with a **`clear and accessible data usage license`**
>
>R1.2. (meta)data are associated with **`detailed provenance`**
>
>R1.3. (meta)data meet domain-relevant **`community standards`**

````



<!-- ````{panels}
:container: container-lg pb-3
:column: col-lg-12 p-2
:card: rounded


```{tabbed} F. 

> To be Findable:

>F1. (meta)data are assigned a **globally unique and persistent identifier (URL_TO_INSERT_TERM_7361 https://fairsharing.org/search?recordType=identifier_schema) **
>
>F2. data are described with **rich metadata** (defined by R1 below)
>
>F3. metadata clearly and explicitly include the identifier (URL_TO_INSERT_TERM_7362 https://fairsharing.org/search?recordType=identifier_schema)  of the data it describes
>
>F4. (meta)data are registered or **indexed in a search (URL_TO_INSERT_RECORD_7363 https://fairsharing.org/FAIRsharing.52b22c) able resource**
```

```{tabbed} A.
> To be Accessible:

>A1. (meta)data are retrievable by their identifier (URL_TO_INSERT_TERM_7365 https://fairsharing.org/search?recordType=identifier_schema)  using **a standard (URL_TO_INSERT_TERM_7364 https://fairsharing.org/search?fairsharingRegistry=Standard) ized communications protocol**
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
>I2. (meta)data use **vocabularies that follow FAIR (URL_TO_INSERT_RECORD_7366 https://fairsharing.org/FAIRsharing.WWI10U)  principles**
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
>R1.3. (meta)data meet domain-relevant **community standard (URL_TO_INSERT_TERM_7367 https://fairsharing.org/search?fairsharingRegistry=Standard) s**
```
```` -->




## The FAIR principles and FAIRplus

The principles will be the organizing principle for the FAIR (URL_TO_INSERT_RECORD_7368 https://fairsharing.org/FAIRsharing.WWI10U) plus Cookbook. While the book itself can be search (URL_TO_INSERT_RECORD_7369 https://fairsharing.org/FAIRsharing.52b22c)  in
various ways and its content exposed through a number of angles, personas and facets, 
the main `Table of Content` organizes a number of atomic recipes around of the principles and their associated sub themes. 




---
 
## Conclusions

This section should be seen as a refresher for anyone unclear about the FAIR (URL_TO_INSERT_RECORD_7371 https://fairsharing.org/FAIRsharing.WWI10U)  principles (URL_TO_INSERT_RECORD_7370 https://fairsharing.org/FAIRsharing.WWI10U) . 
Now that key background informat (URL_TO_INSERT_TERM_7372 https://fairsharing.org/search?recordType=model_and_format) ion has been provided, shining a light on a number of ethical issues driving 
both the development and implementation of the FAIR (URL_TO_INSERT_RECORD_7374 https://fairsharing.org/FAIRsharing.WWI10U)  principles (URL_TO_INSERT_RECORD_7373 https://fairsharing.org/FAIRsharing.WWI10U)  in the context of Life Science data
as well as learning about the overall FAIR (URL_TO_INSERT_RECORD_7375 https://fairsharing.org/FAIRsharing.WWI10U) ification process represent a natural progression 
in the content of the FAIR (URL_TO_INSERT_RECORD_7376 https://fairsharing.org/FAIRsharing.WWI10U)  Cookbook.

### What to read next?
* [The ethical values of FAIR (URL_TO_INSERT_RECORD_7377 https://fairsharing.org/FAIRsharing.WWI10U) ](./FAIR (URL_TO_INSERT_RECORD_7378 https://fairsharing.org/FAIRsharing.WWI10U) plus-values)
* [Assessing FAIR (URL_TO_INSERT_RECORD_7379 https://fairsharing.org/FAIRsharing.WWI10U) ness](../assessing-fairness)

````{rdmkit_panel}
````

---

## References

````{dropdown} **Reference**
<!-- ```{bibliography} ./fair.bib
  :style: alpha
``` -->
1. Wilkinson, M., Dumontier, M., Aalbersberg, I. et al. The FAIR Guiding Principles for scientific data management and stewardship. Sci Data 3, 160018 (2016). https://doi.org/10.1038/sdata.2016.18
2. Wilkinson, M.D., Dumontier, M., Jan Aalbersberg, I. et al. Addendum: The FAIR Guiding Principles for scientific data management and stewardship. Sci Data 6, 6 (2019). https://doi.org/10.1038/s41597-019-0009-6 

````


## Authors

````{authors_fairplus}
Philippe: Writing - Original Draft
Susanna: Writing - Original Draft
````



## License

````{license_fairplus}
CC-BY-4.0
````


