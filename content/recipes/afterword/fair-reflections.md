# Lessons learned from the FAIR journey and project outlook

## A collective of experiences and a collective experience

The FAIR cookbook consolidates knowledge from a pool of expertise and experience collected over several years of practice and development. 
It is also the result of the work of a group of FAIR experts, data producers, research software engineers, from both 
academia and industry, who have learned to work together to make data FAIR, documenting their experience along the way. 
It was also a training ground for developing models and tools to measure progress along the FAIR path. 
In that sense, the contributors and authors of this book have now developed a unique expertise and 'savoir FAIR', 
which we will seek to maintain and accrue. 

With this closing chapter, the authors want to acknowledge all the contributions and highlight how the outputs of
the IMI FAIRplus project have been woven together in a coherent framework to enable **a culture change around data management**.

In the following sections, we will summarize the key outputs and components `FAIR doers` can rely on, try out or get inspiration from.


### Walking the talk: the FAIRness of the recipes.

While building our content, we realized early on that there was an opportunity to apply the FAIR principles to our recipes 
but also use directly some recipes to the recipes themselves.

* w3id.org based persistent resolvable identifiers, implements recipe [FCB077](https://w3id.org/faircookbook/FCB077)
* accessible via http protocol, implements recipe [FCB077](https://w3id.org/faircookbook/FCB077)
* schema.org markup embedded in the html pages to improve findability by search engine, implements recipe [FCB010](https://w3id.org/faircookbook/FCB010)
* accessibility clarified by the specification of a license for code and content,  implements recipe [FCB032](https://w3id.org/faircookbook/FCB032)
* semantic markup with terms4FAIR skills and EDAM terms, implements recipe [FCB020](https://w3id.org/faircookbook/FCB020) 
* linking to FAIRsharing and Biotools


Could we do better?

FAIR is a journey and a continuum where improvements can be made. 
These changes can be planned by following the FAIRification framework and quantified thanks to the dataset maturity model (DSM).
We will highlight those now.


### A FAIRification Framework: To get organized

The FAIRification framework is detailed in a dedicated recipe: [FCB079](https://w3id.org/faircookbook/FCB079).
The reader will find methodological cues to get organized in the most efficient way to identify and achieve a FAIRification objective.
Reaching clarity about the actual task to implement is key to a successful action and the recipe details a few rules and checks to perform 
prior to hacking away.


### FAIR Dataset Maturity Model: To quantify and plan FAIRness 

A specific challenge to the FAIRification task is to assess the FAIR status of a specific digital object (a dataset, a service, an API).
Thanks to the [FAIR Dataset Maturity Model](https://fairplus.github.io/Data-Maturity/), it is possible to devise tools, such as the 
[DSM assessment tool](https://github.com/FAIRplus/FAIR-DSM-Assessment-Tool), to do so.
The service is able to generate automatically a report based on the answers provided by a user about their dataset.
By identifying strengths and weaknesses in the FAIR status of a dataset, the software component provides guidance on
which steps to consider for progressing along the FAIR maturity scale.

The following figure shows the first part of the report, which provides quantified results against the different maturity scales
defined by the Dataset Maturity Model.

````{dropdown} 
:open:
```{figure} ../../../images/fair-dsm-assess-report1.png
---
width: 800px
name: fair-dsm-assess
alt: fair-dsm-assess
---
fair-dsm-assess
```
````

And the figure below shows the second part of the report, which lists met and unmet needs.


````{dropdown} 
:open:
```{figure} ../../../images/fair-dsm-assess-report2.png
---
width: 800px
name: fair-dsm-assess-report2
alt: fair-dsm-assess-report2
---
fair-dsm-assess-report2
```
````

Several rounds of interactions with real projects have established the reliability and efficiency of the approach.
For more details about this, please see [here](https://github.com/TODO).



### FAIR Wizard: To obtain guidance on which recipe to use

The content of the FAIR cookbook is also powering a [FAIR guidance wizard](https://www.ebi.ac.uk/ait/fair-wizard/) hosted 
at the EMBL-EBI, the function of which is to suggest FAIRification recipes to a project owner based on needs identified 
by the decision tree algorithm implemented by the FAIR wizard.


````{dropdown} 
:open:
```{figure} ../../../images/fair-wizard.png
---
width: 800px
name: fair-wizard
alt: FAIR Wizard
---
FAIR Wizard.
```
````

The software is available under an open source license at [this GitHub repository]().

### FAIR Training Program and FAIR fellowship: To train and build a FAIR curriculum.

Finally, the FAIR Cookbook served as basis to shape a FAIR training curriculum, known as the 
[FAIRplus Fellowship program](https://ilias.fraunhofer.de/goto.php?target=crs_15173&client_id=fraunhofer&lang=en).
The syllabus builds on hands-on, practical content developed by the FAIR cookbook team. 
It is available from the [Fraunhofer Institute dedicated site](https://ilias.fraunhofer.de/goto.php?target=crs_15173&client_id=fraunhofer&lang=en)
The first contingent of 25 PhD levels students successfully completed the program and are currently working at documenting their own individual 
FAIRification journeys and hopefully will contribute back to the cookbook and augment its content.

Further, based on this success, new collaborations to develop FAIR training content are ongoing with academic partners,
such as the ELIXIR-UK node and the UKRI-DASH program or Sweden's [ScifileLab initiative](https://www.scilifelab.se/)  or
with industrial partners in the Pharmaceutical industry (e.g. Novartis AG, Boehringer-Ingelheim, AstraZeneca...).


````{dropdown} 
:open:
```{figure} ../../../images/fair-fellowship-program.png
---
width: 800px
name: fair-fellowship
alt: fair-fellowship
---
fair-fellowship.
```
````








## Conclusion

We hope the readers will find this book useful for getting started on their journey to FAIR. 

FAIR is a tool in the process of the digital transformation. 
It requires a new mindset, new ways to look at the data and
also new ways to deliver change in the data management practice. 

Does the FAIR cookbook end here with the end of IMI FAIRplus project?

Of course not! We'll outline now how future development will take place.

### Sustainability through collaborations: the Hub and Spoke model 

Many initiatives exist (the Pistoia Alliance, Elixir-EU, RDMkit sister project, Elixir-UK RMD bites) and productive 
connections with industry and academia have already been established. There are still huge Data 
Management training needs and this means resources will be available to refine, augment, adapt the FAIR cookbook.

A great outcome of our efforts is that the FAIR cookbook is now an Elixir-Europe backed resource and 
several Elixir European Nodes are committed to sustain the resources and contribute to its content. 
Furthermore, collaborators beyond the European Union have already joined and have been onboarded, such as the US NIH
Data Office for Science Strategies. 
Finally, our close ties with EFPIA / Industry partners can mature into further fruitful collaborations. 
All these efforts are anchored in the clear necessity of reducing friction to data integration and make organizations 
is critical to enable efficient and responsive decision-making.


## References
````{dropdown} **References**
````


## Authors

````{authors_fairplus}
Philippe: Writing - Review & Editing
Susanna: Writing - Review & Editing
Ibrahim: Writing - Review & Editing
Danielle: Writing - Review & Editing
Wei: Writing - Review & Editing
Vassilios: Writing - Review & Editing
Tony: Writing - Review & Editing
Herman: Writing - Review & Editing
Yojana: Writing - Review & Editing
Tooba: Writing - Review & Editing
NickJuty: Writing - Review & Editing
````


## License

````{license_fairplus}
CC-BY-4.0
````
