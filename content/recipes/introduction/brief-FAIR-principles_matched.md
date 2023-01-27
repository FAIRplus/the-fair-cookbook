(fcb-fair-principles)=
# What are the FAIR Principles?



<!-- ````{panels_fairplus}
:identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)_text: RX.X
:identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)_link: 'https://example.com'
:difficulty_level: 1
:recipe_type: background_informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion
:reading_time_minutes: 15
:intended_audience: principal_investigator, data_manager, data_scientist, funder (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=funder)
:maturity_level: 2 
:maturity_indicator: 1, 2
:has_executable_code: nope
:recipe_name: Introducing the FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) Principles(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)
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

>F1. (meta)data are assigned a **`globally unique and persistent identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)`**
>
>F2. data are described with **`rich metadata`** (defined by R1 below)
>
>F3. metadata **`clearly and explicitly include the identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) of the data it describes`**
>
>F4. (meta)data are registered or **`indexed in a search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)able resource`**
````

````{dropdown} **Accessibility**
:open:

> **To be Accessible:**

>A1. (meta)data are retrievable by their identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) using **`a standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)ized communications protocol`**
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
>I2. (meta)data use **`vocabularies that follow FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) principles`**
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
>R1.3. (meta)data meet domain-relevant **`community standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s`**

````



<!-- ````{panels}
:container: container-lg pb-3
:column: col-lg-12 p-2
:card: rounded


```{tabbed} F. 

> To be Findable:

>F1. (meta)data are assigned a **globally unique and persistent identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)**
>
>F2. data are described with **rich metadata** (defined by R1 below)
>
>F3. metadata clearly and explicitly include the identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) of the data it describes
>
>F4. (meta)data are registered or **indexed in a search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)able resource**
```

```{tabbed} A.
> To be Accessible:

>A1. (meta)data are retrievable by their identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) using **a standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)ized communications protocol**
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
>I2. (meta)data use **vocabularies that follow FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) principles**
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
>R1.3. (meta)data meet domain-relevant **community standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s**
```
```` -->




## The FAIR principles and FAIRplus

The principles will be the organizing principle for the FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)plus Cookbook(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059). While the book(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059) itself can be search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) in
various ways and its content exposed through a number of angles, personas and facets, 
the main `Table of Content` organizes a number of atomic recipes around of the principles and their associated sub themes. 




---
 
## Conclusions

This section should be seen as a refresher for anyone unclear about the FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) principles(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/). 
Now that key background informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion has been provided, shining a light on a number of ethical issues driving 
both the development and implementation of the FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) principles(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) in the context of Life Science data
as well as learning about the overall FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)ification process represent a natural progression 
in the content of the FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) Cookbook(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059).

### What to read next?
* [The ethical values of FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)](./FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)plus-values)
* [Assessing FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)ness](../assessing-fairness)

````{rdmkit_panel}
````

---

## References

````{dropdown} **Reference**
<!-- ```{bibliography} ./fair.bib
  :style: alpha
``` -->
1. Wilkinson, M., Dumontier, M., Aalbersberg, I. et al. The FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) Guiding Principles for scientific data management and stewardship. Sci Data 3, 160018 (2016). https://doi.org/10.1038/sdata.2016.18
2. Wilkinson, M.D., Dumontier, M., Jan Aalbersberg, I. et al. Addendum: The FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) Guiding Principles for scientific data management and stewardship. Sci Data 6, 6 (2019). https://doi.org/10.1038/s41597-019-0009-6 

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


