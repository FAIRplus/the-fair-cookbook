(fcb-reusability-provenance)=
# Provenance information


````{panels_fairplus}
```` 





## Main Objectives

In all tasks of data integration, especially in the area of Pharma, ensuring trust in data sources is essential.
The steps taken to ensure new datasets or sources of informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion meet a number of criteria ascertaining some level of 
quality are many. One of them is a check on the origin of the informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion, in other words, its **Provenance**. 
Provenance covers the elements detailing how the data was produced by identifying the agents 
(human, software, workflows) so a certain level of traceability and accountability can be established. 
The notions of **audit and trail** as well as **versioning** and **authorship** are essential to be able, 
should any distortion be identified in downstream analysis, to trace back to possible sources of error.


## Provenance: a definition

**"Provenance is informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion about entities, activities, and people involved in producing a piece of data or thing, 
which can be used to form assessments about its quality, reliability or trustworthiness"**. 
Provenance has been an active field of academic research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) and several model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s have been developed(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) over the year to cover the domain.
The next section will introduce the most known model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s as well as detail how their overlap and what are the differences between these.

**Data provenance** is also referred to as **data lineage** 


### OPM Open Provenance Model

Published in 2011, the Open Provenance Model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)(URL_TO_INSERT_RECORD https://doi.org/10.1016/j.future.2010.07.005) (OPM(URL_TO_INSERT_RECORD https://doi.org/10.1016/j.future.2010.07.005)) {footcite}`MO(URL_TO_INSERT_RECORD http://mged.sourceforge.net/ontologies/MGEDontology.php)REAU2011743` was the first formal model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) developed(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped)
to cater for the reporting of provenance informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion with several main goals in mind:
- provide a domain agnostic, formal and actionable definition of provenance
- enable sharing of provenance informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion between systems, an issue of interoperability
- support tool development and implementation
- enable validation of provenance messages.

The work was well-received and several workshops and working groups refined the specification which resulting in a
specification being submitted to the World Wide Web Consortium.
The following sections provides further insights into these efforts.


### The PROV Data Model
This definition is taken from the W3C Provenance Data Model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)(URL_TO_INSERT_RECORD http://www.w3.org/TR/prov-dm/) specifications {footcite}`provdm`.

````{dropdown}
```{figure} prov-dm-overview.png
---
width: 800px
name: prov-dm-overview
alt: Overview of the Provenance Data Model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) main classes
---
Overview of the Provenance Data Model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) main classes.
```
````

### PROV vocabulary:

The PRO(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD http://www.sparontologies.net/ontologies/pro)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD https://proconsortium.org/)(URL_TO_INSERT_RECORD https://w3id.org/ro/)V-O(URL_TO_INSERT_RECORD http://www.w3.org/TR/prov-o/) Provenance Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) {footcite}`provo` is a W3C-vetted specification of the Provenance Data Model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) as an OWL(URL_TO_INSERT_RECORD http://www.w3.org/TR/owl-overview/) ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact).
The namespace for PRO(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD http://www.sparontologies.net/ontologies/pro)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD https://proconsortium.org/)(URL_TO_INSERT_RECORD https://w3id.org/ro/)V-O(URL_TO_INSERT_RECORD http://www.w3.org/TR/prov-o/) is [http://www.w3.org/ns/prov#](http://www.w3.org/ns/prov#).
It is meant to allow expressing provenance informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion as model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ed in the provenance model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)
[W3C PROV-DM](https://www.w3.org/TR/prov-o(URL_TO_INSERT_RECORD http://www.w3.org/TR/prov-o/)verview/) with Classes, Properties and relations defined in the W3C 
Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) Web Language (OWL(URL_TO_INSERT_RECORD http://www.w3.org/TR/owl-overview/)). Instances can therefore be represented in RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) and distributed in any of the official 
serialization, e.g. JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259)-LD(URL_TO_INSERT_RECORD https://json-ld.org/spec/latest/json-ld/), RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/)/XML(URL_TO_INSERT_RECORD https://www.w3.org/TR/xml/)(URL_TO_INSERT_RECORD http://www.w3.org/TR/rdf-syntax-grammar/), Turtle(URL_TO_INSERT_RECORD http://www.w3.org/TR/turtle/).


````{dropdown}
```{figure} prov-o-overview.svg
---
width: 800px
name: prov-o-overview
alt: Overview of the Provenance Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) main classes
---
Overview of the Provenance Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) main classes.
```
````


Below is an example of provenance informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion represented using the PRO(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD http://www.sparontologies.net/ontologies/pro)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD https://proconsortium.org/)(URL_TO_INSERT_RECORD https://w3id.org/ro/)V-O(URL_TO_INSERT_RECORD http://www.w3.org/TR/prov-o/) ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and serialized as RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) statements
using turtle representation.

````bash









````





## Tools for creating provenance metadata

In the previous section, we have detailed the landscape of formal model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s to represent provenance informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion.
In this section, we will show how tools have implemented these model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s, or domain-specific extension of them as in the
case of computation workflow provenance informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion.

### CamFLow

[CamFlow](https://camflow.org/#output_format) is a Linux Security Module (LSM(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/1520)) designed to capture data provenance for
the purpose of system audit {footcite}`Pasquier2017Camflow` and aims at capture informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion flow.


CamFlow support 2 output format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s.

- W3C PRO(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD http://www.sparontologies.net/ontologies/pro)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD https://proconsortium.org/)(URL_TO_INSERT_RECORD https://w3id.org/ro/)V-JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)

```bash

```


Example of a write edge in W3C PRO(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD http://www.sparontologies.net/ontologies/pro)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD https://proconsortium.org/)(URL_TO_INSERT_RECORD https://w3id.org/ro/)V format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format):
```bash
```

```{note}
```

While this tool is probably of limited use to Life Sciences and bioinformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ics applications, we mention it for two reasons:
* it provides one of the first example of an implementation (even if very basic) making use of the W3C Prov-O model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format).
* it provides an insight on how computational tool can deal with provenance informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion in ways which allow assessing 
systems health from a security point of view. 


### Computational workflows and Provenance information:


As seen when introducing the W3C Provenance Data Model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)(URL_TO_INSERT_RECORD http://www.w3.org/TR/prov-dm/) and Provenance Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact), three key entities are necessary to 
record and track lineage informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion:

- The Entity the origin of which we are concerned with.
- The Activity which resulted in the creation of the Entity
- The Agent which performed the Activity aforementioned.

Because the PRO(URL_TO_INSERT_RECORD https://github.com/oborel/obo-relations/)(URL_TO_INSERT_RECORD http://www.sparontologies.net/ontologies/pro)(URL_TO_INSERT_RECORD https://github.com/albytrav/RadiomicsOntologyIBSI)(URL_TO_INSERT_RECORD https://proconsortium.org/)(URL_TO_INSERT_RECORD https://w3id.org/ro/)V model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) is domain agnostic and very generic, it can be either applied as is, to any situation 
or it can also be extended and specialized to suit a particular domain on knowledge.
To give an example, tracking provenance informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion in the field of bioinformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ics shares features with provenance
tracking as used in manufacturing, but it also has a number of specific features.
In the field of bioinformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ics, where computational pipelines, known as workflows, are assembled to process ever larger
datasets on high performance computing infrastructure and cloud infrastructure, having the ability to access data 
lineage matters for a number for reasons, such as:

- audit and trail tasks for regulator(URL_TO_INSERT_RECORD http://www.bioinformatics.org/regulator)y compliance, where every step of the data processing needs to be documented for submission.
- resource optimization and energy savings (e.g. should a workflow be executed again or not)

It is those features which have been the focus of an extension as part of the work on computational biology workflows with CWL(URL_TO_INSERT_RECORD http://www.commonwl.org)Prov {footcite}`10.1093/gigascience/giz095`, and which we will now cover.

#### Example of CWLProv document

The infobox below shows an example of CWL(URL_TO_INSERT_RECORD http://www.commonwl.org)Prov RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) document which details how provenance informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion about the execution 
of CWL(URL_TO_INSERT_RECORD http://www.commonwl.org) coded workflow may be represented.
This document is take from the [CWL(URL_TO_INSERT_RECORD http://www.commonwl.org)Prov github(URL_TO_INSERT_RECORD https://github.com/) repository (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository)](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/common-workflow-language/cwlprov/blob/main/prov.md).
Such documents are generated and consumed by a feasibility demonstrator tool such as [CWL(URL_TO_INSERT_RECORD http://www.commonwl.org)tool]()


```bash





```



````{note}
````

````{note}



````

#### CWLtool: a component to manage workflow information and generate CWLProv information


'cwltool' for Common Workflow Language(URL_TO_INSERT_RECORD http://www.commonwl.org) tool is a python reference implementation for the
[Common Workflow Language(URL_TO_INSERT_RECORD http://www.commonwl.org)](https://www.commonwl.org(URL_TO_INSERT_RECORD http://www.commonwl.org)/), which means that it supports the full set of CWL(URL_TO_INSERT_RECORD http://www.commonwl.org) specifications
and provides validation functions to check CWL(URL_TO_INSERT_RECORD http://www.commonwl.org) documents.


```bash
```

cwltool is not the only implementation of the CWL(URL_TO_INSERT_RECORD http://www.commonwl.org) specifications, others such as [Arvados](https://arvados.org/) and 
[Toil](https://toil.ucsc-cgl.org/) exist. 
In case these distinct implementations are also installed on the system, one needs to make sure a helper tool known as
'cwl-runner' is also installed. The *key* function of 'cwl-runner' is to allow users to select which CWL(URL_TO_INSERT_RECORD http://www.commonwl.org) implementation
will be executed.

```bash
```

For the purpose of this recipe, which is to show how provenance informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion can be generated by a tool such as 
cwltool {footcite}`cwltool`, users will need to make sure that a workflow is available before performing this conversion.


```bash
```

#### CWLProv-py

This tool, also an output from the Common Workflow Language(URL_TO_INSERT_RECORD http://www.commonwl.org) consortium, is solely intended as a validator for provenance
informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion when available from Research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) Objects {footcite}`cwlprov-py`. 
It is a standalone python package, which provides a command line interface (CL(URL_TO_INSERT_RECORD https://github.com/obophenotype/cell-ontology)I) to read, inspect research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) objects 
capturing workflow execution informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion using the CWL(URL_TO_INSERT_RECORD http://www.commonwl.org) syntax.

To install the package, simply run the standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) python install package pip: 

```python
```

To run 'cwlprov' following installation and using an exemplar CWL(URL_TO_INSERT_RECORD http://www.commonwl.org) file, run the following command:


```python
```

### Provenance and distributed ledger technology

With this section, we intend to cover another aspect associated with provenance informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion. It is the issue of 
trustworthiness of the informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion and how to ascertain that even if a provenance informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion message is valid, 
it actually contains authentic and untempered informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion. 

The raise of digital currencies such as bitcoin or ethereum has popularized the notion of 'blockchain', which is a type
of what is known as "distributing ledger technology" (DLT).  Blockchains and DLT in general represent technological 
solution to the problem of trust in provenance. To achieve this goal, DLT relies on three key principles:

- distribution of informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion: in other words, the system is decentralized, meaning that no single entity holds the database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database).
Instead, a multitude of copies of the informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion are available from a myriad of independent nodes. 

- transparency:  this is a consequence of the distributed nature of the arch(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)itecture. Transparency is understood as the
availability of means of verification by being able to access independent sources of the reference informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion. 
This allows consistency checks to be performed and therefore provides the means of tempering detection. 

````{note}
````

- immutability: this is the last tenet of DLT and refers to the fact that once an entry has been to the distributed
ledger, it is digitally signed and synchronized in the network by adding a new element (the block) to the blockchain.
Each of the new is digitally signed via some cryptographic algorithm (e.g. Blake2). Any attempt to modify a particular
block would result in changing its signature. This can be done but the cost could be prohibitively high as it would 
entail modifying all subsequent blocks in the chain. This arch(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)itecture ensures the stability or immutability of the ledger.

````{admonition} Important
````   



## Conclusion

With this FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) Cookbook(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059) content, we have introduced the notion of Provenance informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion, providing a brief historical 
review of the domain model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) and given a few examples of tools implementing provenance informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion tracking.

For a more in depth exploration of provenance informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion, we encourage our readers to follow up with more detailed 
material listed below:


### What to read next?

* [Generating ISA based metadata and packaging it as a research(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) object programmatically](https://w3id.org(URL_TO_INSERT_RECORD https://w3id.org/)/faircookbook/FCB___)
* [Making workflow informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) and depositing to Workflowhub(URL_TO_INSERT_RECORD https://workflowhub.eu)](https://w3id.org(URL_TO_INSERT_RECORD https://w3id.org/)/faircookbook/FCB___)
* [How to meet community standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s for annotation](fcb-interop-txmetadata) {ref}`fcb-interop-txmetadata`
* [FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) data matrix](fcb-fairify-examples-datamatrix) {ref}`fcb-fairify-examples-datamatrix`
* [Minid identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s](https://w3id.org(URL_TO_INSERT_RECORD https://w3id.org/)/faircookbook/FCB008)


````{panels}
```{image} ../../../images/logos/pistoia_logo.png
:height: 40px
:align: center
:name: FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)toolkit_logo
```
```{rdmkit_panel}
:inline: true
```
````

<!--
> :header: bg-primary pa_dark
> ```{image} ./../../../../../../_static/images/logo/TTW.svg
> :height: 40px
> :align: center
> :name: Turing-Way-logo
> ```
> ^^^
> [The Turing Way Book(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059) of Data Sciences](https://the-turing-way.netlify.app/welcome.html/)
> ---
-->



## References

````{dropdown} **Reference**
```{footbibliography}
```
````


## Authors
````{authors_fairplus}
````

    
## License
````{license_fairplus}
````
