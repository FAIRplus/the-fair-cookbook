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

The goal of this section is to go over each of the principles for FAIR data management as described by Wilkinson and coworkers in their Nature Springer Scientific Data manuscript published in 2016
<!-- {cite}`Wilkinson2016FAIR,Wilkinson2019Evaluation`. -->
Owing to the success of the principles, now endorsed by funding agencies (IMI, Wellcome Trust to name only two), but also by the G20 and by industry leaders, it is essential to remind the reader about those.



## The FAIR Guiding Principles



````{dropdown} **The FAIR principles manuscript**

```{figure} https://i.imgur.com/RxkoNed.png
---
height: 650px
name: the FAIR principles
alt: the cover page for the FAIR principle article as published in Scientific Data. https://doi.org/10.1038/sdata.2016.18
---
_The FAIR Principles_ the cover pages for the FAIR principle articles as published in Scientific Data. https://doi.org/10.1038/sdata.2016.18.
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

The principles will be the organizing principle for the FAIRplus Cookbook. While the book itself can be search in
various ways and its content exposed through a number of angles, personas and facets, 
the main `Table of Content` organizes a number of atomic recipes around of the principles and their associated sub themes. 




---
 
## Conclusions

This section should be seen as a refresher for anyone unclear about the FAIR principles. 
Now that key background information has been provided, shining a light on a number of ethical issues driving 
both the development and implementation of the FAIR principles in the context of Life Science data
as well as learning about the overall FAIRification process represent a natural progression 
in the content of the FAIR Cookbook.

### What to read next?
* [The ethical values of FAIR](./FAIRplus-values)
* [Assessing FAIRness](../assessing-fairness)

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


