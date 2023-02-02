(fcp-infra-openrefine)=
# Using OpenRefine and Karma for FAIRification


````{panels_fairplus}
:identifier_text: FCB075
:identifier_link: 'https://w3id.org/faircookbook/FCB075'
:difficulty_level: 3
:recipe_type: background_information
:reading_time_minutes: 20
:intended_audience: principal_investigator, data_manager, data_scientist  
:maturity_level: 1
:maturity_indicator: 1, 2
:has_executable_code: nope
:recipe_name: Using OpenRefine and Karma for FAIRification
```` 


## Introduction

FAIR (URL_TO_INSERT_RECORD_3678 https://fairsharing.org/FAIRsharing.WWI10U) ification is a multi-step process that can be performed via different workflows and at different levels of completeness.

Here, we focus on “fully FAIR (URL_TO_INSERT_RECORD_3679 https://fairsharing.org/FAIRsharing.WWI10U) ifying” data “*a posteriori*”. 

That is to express the content of the informat (URL_TO_INSERT_TERM_3680 https://fairsharing.org/search?recordType=model_and_format) ion (entities, attributes, relations, values) via ontologies (URL_TO_INSERT_TERM_3681 https://fairsharing.org/search?recordType=terminology_artefact)  
(when applicable) and, in particular, through URI (URL_TO_INSERT_RECORD_3682 https://fairsharing.org/FAIRsharing.d261e1) s.

The processed informat (URL_TO_INSERT_TERM_3683 https://fairsharing.org/search?recordType=model_and_format) ion results in an RDF (URL_TO_INSERT_RECORD_3684 https://fairsharing.org/FAIRsharing.p77ph9) /Linked Data graph, that can be seen as a specific implementation
of a Knowledge Graph (KG in short).
By virtue of using coherent URI (URL_TO_INSERT_RECORD_3685 https://fairsharing.org/FAIRsharing.d261e1) s, different datasets are automatically (logically) merged when represented as a graph.

For simplicity, we focus here on "input" data that is represented as tables.

Two fundamental steps are needed to perform such transformat (URL_TO_INSERT_TERM_3686 https://fairsharing.org/search?recordType=model_and_format) ion:

* **Reconcile entities**. 

That is assigning the same URI (URL_TO_INSERT_RECORD_3687 https://fairsharing.org/FAIRsharing.d261e1) s to the same entities, even when these are referred to by different names.

```{note}
In practice, we could have different but related URIs.
It remains that in this step, we should go beyond names (labels) and use **coherent identifiers** to point 
to the entities names refer to.
```

* **Map (URL_TO_INSERT_RECORD_3689 https://fairsharing.org/FAIRsharing.53edcc)  the structure of the data to an ontology (URL_TO_INSERT_TERM_3688 https://fairsharing.org/search?recordType=terminology_artefact) **.

This is akin to reconciling properties (referred by a name, e.g.: a column name) to relations, attributes, and classes in an ontology (URL_TO_INSERT_TERM_3690 https://fairsharing.org/search?recordType=terminology_artefact) .
Except for simple cases, such map (URL_TO_INSERT_RECORD_3692 https://fairsharing.org/FAIRsharing.53edcc) pings go beyond simple names to URI (URL_TO_INSERT_RECORD_3691 https://fairsharing.org/FAIRsharing.d261e1)  relations and generally include **small graph patterns**.

```{note}
As for many data cleansing exercises, we may need extra steps that are not specific to the transformation to a KG, 
but often necessary. For instance, split an "address" in "Country", "Street", "City").
```

We mentioned that we assume here that source data is represented as one or more CSV (URL_TO_INSERT_RECORD_3693 https://fairsharing.org/FAIRsharing.1943d4)  files.
There are some considerations to be taken if files are in multiple tables (as extra attention can be paid to "linking keys") or
in complex data structures such as XML (URL_TO_INSERT_RECORD_3694 https://fairsharing.org/FAIRsharing.b5cc91) , JSO (URL_TO_INSERT_RECORD_3696 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_3695 https://fairsharing.org/FAIRsharing.5bbab9)  etc.
Tabular data covers a prominent use case for data FAIR (URL_TO_INSERT_RECORD_3697 https://fairsharing.org/FAIRsharing.WWI10U) ification and is a building block for complex conversions.

We focus here on data (rather than metadata), though the distinction between the two vanishes when informat (URL_TO_INSERT_TERM_3698 https://fairsharing.org/search?recordType=model_and_format) ion is 
expressed as a KG.


### Reconciliation

An essential element of FAIR (URL_TO_INSERT_RECORD_3700 https://fairsharing.org/FAIRsharing.WWI10U) ification is **the ability to identify entities via ontology (URL_TO_INSERT_TERM_3699 https://fairsharing.org/search?recordType=terminology_artefact)  terms**.
In general by "reconciliation", we mean the **capability to identify an entity (via an ID from a knowledge base) given one 
or more references** and eventually additional informat (URL_TO_INSERT_TERM_3701 https://fairsharing.org/search?recordType=model_and_format) ion.


#### Ingredients for reconciliation

We generally need:

1. A **source of knowledge** to reconcile to. This could be expressed as a knowledge graph (KG), see {ref}`fcb-public-kg`.
2. A **system implementing some logic to reconcile** a dataset to such a knowledge base, that is ideally automated. 
Such a system would receive as input at least a reference (e.g.: name) to the entity, but could also receive additional
attributes or context for the name.
3. Ideally a system to perform *Quality Assessment (QA)* and curation (especially if point 2 is automated).


### Reconciliation with OpenRefine

OpenRefine is a Desktop tool to cleanse data that proposes a simple workflow for data reconciliation {footcite}`openrefine`. 
In particular, users can load data as a table, and for a column, they can call a “reconciliation service”:
this will suggest what are the types of entity in a column (e.g.: drugs, treatments) and the user can then ask to
reconcile to entities of one or more of these types. OpenRefine will then present candidates URI (URL_TO_INSERT_RECORD_3702 https://fairsharing.org/FAIRsharing.d261e1) s, together with a preview 
(when URI (URL_TO_INSERT_RECORD_3703 https://fairsharing.org/FAIRsharing.d261e1) s are resolvable) and confidence so that the user can control the proper reconciliation.


````{dropdown}
:open:
```{figure} ../../../images/openrefine.png
---
width: 800px
name: openrefine-screenshot
alt: OpenRefine
---
OpenRefine
```
````

OpenRefine: [https://docs.openrefine.org/manual/reconciling](https://docs.openrefine.org/manual/reconciling)

In practice, OpenRefine presents an interface for QA and curation on a set of reconciliation proposals. 
Such proposals are provided by reconciliation services: systems that implement a set of OpenRefine compatible APIs.

There are publicly available reconciliation services, but it is also possible to implement *ad-hoc* services (e.g.: on top of an MDM (URL_TO_INSERT_RECORD_3704 https://fairsharing.org/FAIRsharing.wnk2eq)  system).
Via a plugin called **grefine-rdf-extension** [https://github.com (URL_TO_INSERT_RECORD_3705 https://fairsharing.org/FAIRsharing.c55d5e) /fadmaa/grefine-rdf-extension](https://github.com (URL_TO_INSERT_RECORD_3706 https://fairsharing.org/FAIRsharing.c55d5e) /fadmaa/grefine-rdf-extension) 

It is also possible to use a generic triple-store as a reconciliation service.

```{note}
In that case, the triple-store should contain a list of entities, with labels in one or more languages and the corresponding classes. 
The triple-store should also be accessible on the network where OpenRefine is running.
(no authorisation is possible, except via extensions).
```

### Reconciliation toward public knowledge-bases


#### Reconciliation toward wikidata

One of the best developed (URL_TO_INSERT_RECORD_3709 https://fairsharing.org/FAIRsharing.31385c)  systems supporting reconciliation APIs is Wikidata (URL_TO_INSERT_RECORD_3707 https://fairsharing.org/FAIRsharing.6s749p)  (URL_TO_INSERT_RECORD_3708 https://fairsharing.org/FAIRsharing.6s749p)  (https://wikidata.reconci.link).
By specifying the URI (URL_TO_INSERT_RECORD_3710 https://fairsharing.org/FAIRsharing.d261e1) : [https://wikidata.reconci.link/en/api](https://wikidata.reconci.link/en/api) as a reconciliation
service, OpenRefine will help users to normalise entity references to Wikidata (URL_TO_INSERT_RECORD_3712 https://fairsharing.org/FAIRsharing.6s749p)  (URL_TO_INSERT_RECORD_3713 https://fairsharing.org/FAIRsharing.6s749p)  URI (URL_TO_INSERT_RECORD_3711 https://fairsharing.org/FAIRsharing.d261e1) s.


````{dropdown}
:open:
```{figure} ../../../images/openrefine-wiki-reconci.png
---
width: 800px
name: openrefine-wiki.reconci
alt: Wikidata (URL_TO_INSERT_RECORD_3714 https://fairsharing.org/FAIRsharing.6s749p)  (URL_TO_INSERT_RECORD_3715 https://fairsharing.org/FAIRsharing.6s749p)  Reconcile for OpenRefine
---
Wikidata (URL_TO_INSERT_RECORD_3716 https://fairsharing.org/FAIRsharing.6s749p)  (URL_TO_INSERT_RECORD_3717 https://fairsharing.org/FAIRsharing.6s749p)  Reconcile for OpenRefine
```
````


```{warning}
The drawback of using Wikidata is obviously that not all entities exist in Wikidata,
in particular entities which may be not public, as in a company setting.
```

#### Other public reconciliation services

Several public resources provide support for OpenRefine reconciliation services.



```{note}
in OpenRefine, users can use various reconciliation services over the same dataset.
The reconciliation is column specific.
```

### Reconciliation toward private knowledge bases

OpenRefine can also be used for internal data (e.g.: MDM (URL_TO_INSERT_RECORD_3718 https://fairsharing.org/FAIRsharing.wnk2eq)  systems), by providing “internal” reconciliation services.

This can be done in several ways:


#### Wikidata as a local instance

One way of providing reconciliation services for OpenRefine on internal data is to leverage the Wikibase system 
(the system at the basis of Wikidata (URL_TO_INSERT_RECORD_3719 https://fairsharing.org/FAIRsharing.6s749p)  (URL_TO_INSERT_RECORD_3720 https://fairsharing.org/FAIRsharing.6s749p) ). 

We could implement a local “empty” version of Wikidata (URL_TO_INSERT_RECORD_3722 https://fairsharing.org/FAIRsharing.6s749p)  (URL_TO_INSERT_RECORD_3724 https://fairsharing.org/FAIRsharing.6s749p) , and populate it with internal data (represented using the Wikidata (URL_TO_INSERT_RECORD_3723 https://fairsharing.org/FAIRsharing.6s749p)  (URL_TO_INSERT_RECORD_3725 https://fairsharing.org/FAIRsharing.6s749p)  format (URL_TO_INSERT_TERM_3721 https://fairsharing.org/search?recordType=model_and_format) ).

Dedicated deployment scripts can help in installing and administering an empty Wikibase system. 
These scripts are available from [https://github.com (URL_TO_INSERT_RECORD_3726 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/WikiDraftWorks](https://github.com (URL_TO_INSERT_RECORD_3727 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/WikiDraftWorks)


````{dropdown}
:open:
```{figure} ../../../images/wikidraftworks.png
---
width: 800px
name: WikiDraftWorks
alt: WikiDraftWorks
---
WikiDraftWorks
```
````


#### Reconciling toward a triplestore

When reference data and ontology (URL_TO_INSERT_TERM_3728 https://fairsharing.org/search?recordType=terminology_artefact)  exist in a triplestore, a simpler way to support OpenRefine is via 
its [grefine RDF (URL_TO_INSERT_RECORD_3729 https://fairsharing.org/FAIRsharing.p77ph9)  extension plugin](https://github.com (URL_TO_INSERT_RECORD_3730 https://fairsharing.org/FAIRsharing.c55d5e) /fadmaa/grefine-rdf-extension). 
This allows to specify any triplestore as a reconciliation service, provided it contains suitable content
(e.g.: instances with labels and their categorisation in classes).
This extension graphical user interface (GUI) for exporting data of Google Refine project (URL_TO_INSERT_TERM_3731 https://fairsharing.org/search?recordType=project) s in RDF (URL_TO_INSERT_RECORD_3733 https://fairsharing.org/FAIRsharing.p77ph9)  format (URL_TO_INSERT_TERM_3732 https://fairsharing.org/search?recordType=model_and_format) . 
The export is based on map (URL_TO_INSERT_RECORD_3734 https://fairsharing.org/FAIRsharing.53edcc) ping the data to a template graph using the GUI.

The [RDF (URL_TO_INSERT_RECORD_3735 https://fairsharing.org/FAIRsharing.p77ph9)  transform extension](https://github.com (URL_TO_INSERT_RECORD_3736 https://fairsharing.org/FAIRsharing.c55d5e) /AtesComp/rdf-transform) now replaces 'grefine' 

```{note}
Note that this is not equivalent to the Wikidata services: 
as the plugin works over SPARQL, it has fewer capabilities in terms of ranking of results.
```


##### Authentication

One limitation of the above approach is that OpenRefine does not support authentication.
Any services or triple stores it reconciles to need to be accessible on the same network where the OpenRefine client is working. 
In an enterprise setting, this is a serious limitation, as data is protected by access policies (URL_TO_INSERT_TERM_3737 https://fairsharing.org/search?fairsharingRegistry=Policy) .

A possible workaround is an OpenRefine extension that implements authentication (tested with AllegroGraph based reconciliation services).

[[https://github.com (URL_TO_INSERT_RECORD_3738 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/OpenRefine_Authenticator](https://github.com (URL_TO_INSERT_RECORD_3739 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/OpenRefine_Authenticator)


#### Implementing reconciliation APIs

Finally, it is possible to implement reconciliation APIs on top of proprietary systems (e.g.: MDM (URL_TO_INSERT_RECORD_3740 https://fairsharing.org/FAIRsharing.wnk2eq) ):
[https://reconciliation-api.github.io/specs/latest/](https://reconciliation-api.github.io/specs/latest/)

In this case, more complex reconciliation logic can be implemented. 
OpenRefine APIs could be one of the possible interfaces for more fundamental reconciliation services 
(e.g.: made available in R, Python,...).


## PROs and CONs of reconciliation in OpenRefine


### Limitations


#### Client tool

OpenRefine is a DeskTop tool. Though implemented as a web C/S system, it does not support concurrent users. 
Therefore, what can be done on OpenRefine is limited by the technical specification of the client, which is typically 
an edge device in modern enterprise environments.

One way to circumvent this limitation is to make OpenRefine accessible in a virtual desktop that can reside on a 
remote desktop. 
When doing so, it would be useful if data could be loaded from some shared central filesystem, as OpenRefine by default
will consider the file system of the virtual desktop environment it is running on.

An extension of OpenRefine implements this kind of network access

[https://github.com (URL_TO_INSERT_RECORD_3741 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/OpenRefine_local_file_extension](https://github.com (URL_TO_INSERT_RECORD_3742 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/OpenRefine_local_file_extension)

(to connect to a shared drive)

_possibly extended by_

[https://github.com (URL_TO_INSERT_RECORD_3743 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/OpenRefine_Docker](https://github.com (URL_TO_INSERT_RECORD_3744 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/OpenRefine_Docker)

(embed ways to tune configuration when starting OpenRefine in a server way)


#### Authentication

As previously mentioned, OpenRefine does not support access to restricted reconciliation services.

An extension providing such capability (tested on AllegroGraph) is available at:

[https://github.com (URL_TO_INSERT_RECORD_3745 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/OpenRefine_Authenticator](https://github.com (URL_TO_INSERT_RECORD_3746 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/OpenRefine_Authenticator)


#### Performance

Reconciliation in OpenRefine is not suitable for high data load, in that it is implemented via API calls and
the performance is very limited.
Recent development of OR maye have improved performance.
A Lot depends also on the implementation of the reconciliation APIs (in terms of parallelism). 
It is advisable to use reconciliation functions for datasets in the hundreds rows range.
Furthermore, there is limited value in using OpenRefine in ETL processes where its interactive capabilities are not used.


### When to use OpenRefine

OpenRefine is a simple user oriented tool, useful for low curation loads where the aspects of reconciliation are prominent. 
It is particularly good as first tool to introduce reconciliation concepts in an organisation.

```{note}
OpenRefine can be used in more complex scenarios when its overall data cleansing capabilities are used. 
We focus here only on some FAIRification related capabilities.
```


#### Mapping the structure of data to an ontology {#mapping-the-structure-of-data-to-an-ontology}

The other essential step when transforming a dataset to a KG is map (URL_TO_INSERT_RECORD_3747 https://fairsharing.org/FAIRsharing.53edcc) ping its structure to a graph. 
Let’s introduce this notion via a very simple example.


<table>
  <tr>
   <td>Person
   </td>
   <td>Father
   </td>
  </tr>
  <tr>
   <td>Albert Einstein
   </td>
   <td>Hermann Einstein
   </td>
  </tr>
</table>


After reconciliation, we could imagine this data to look like:


<table>
  <tr>
   <td>Person
   </td>
   <td>Father
   </td>
  </tr>
  <tr>
   <td>http://www.wikidata.org (URL_TO_INSERT_RECORD_3748 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q937
   </td>
   <td>http://www.wikidata.org (URL_TO_INSERT_RECORD_3749 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q88665
   </td>
  </tr>
</table>


[PUT CO (URL_TO_INSERT_RECORD_3751 https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD_3752 https://fairsharing.org/FAIRsharing.thskvr) RRECT URI (URL_TO_INSERT_RECORD_3750 https://fairsharing.org/FAIRsharing.d261e1) s ABOVE]

To express the above as a graph, we need to make the structure or this table explicit, referring to an ontology (URL_TO_INSERT_TERM_3753 https://fairsharing.org/search?recordType=terminology_artefact) , example, for people and relations.

```{admonition} Tip
:class: tip

Wikidata uses 2 sets of uri 

[https://www.wikidata.org/wiki/Q937](https://www.wikidata.org/wiki/Q937) (does not work in the wikidata sparql endpoint)  
 vs [http://www.wikidata.org/entity/Q937](http://www.wikidata.org/entity/Q937)
  (should be used for the sparql: these uri redirect to the html link above)

Important point to bear in mind when using Wikidata.

```

Note that first we could map (URL_TO_INSERT_RECORD_3754 https://fairsharing.org/FAIRsharing.53edcc) :


<table>
  <tr>
   <td>Person => <a href="http://www.wikidata.org (URL_TO_INSERT_RECORD_3755 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q5">http://www.wikidata.org (URL_TO_INSERT_RECORD_3756 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q5</a> (Human, the type of the entity in the column)
   </td>
   <td>Father =>
<p>
<a href="http://www.wikidata.org (URL_TO_INSERT_RECORD_3757 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q5">http://www.wikidata.org (URL_TO_INSERT_RECORD_3758 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q5</a> (Human, the type of the entity in the column)
<p>
=> <a href="http://www.wikidata.org (URL_TO_INSERT_RECORD_3759 https://fairsharing.org/FAIRsharing.6s749p) /entity/P22">http://www.wikidata.org (URL_TO_INSERT_RECORD_3760 https://fairsharing.org/FAIRsharing.6s749p) /entity/P22</a> (father, the relation to the other entity)
   </td>
  </tr>
  <tr>
   <td>http://www.wikidata.org (URL_TO_INSERT_RECORD_3761 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q937
   </td>
   <td>http://www.wikidata.org (URL_TO_INSERT_RECORD_3762 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q88665
   </td>
  </tr>
</table>



Note that we need to have a way to express how “columns are linked together”. The full graph from the above example would look like [PSEUDO RDF (URL_TO_INSERT_RECORD_3763 https://fairsharing.org/FAIRsharing.p77ph9) , TO (URL_TO_INSERT_RECORD_3764 https://fairsharing.org/FAIRsharing.w69t6r)  CO (URL_TO_INSERT_RECORD_3765 https://fairsharing.org/FAIRsharing.wgfrmg)  (URL_TO_INSERT_RECORD_3766 https://fairsharing.org/FAIRsharing.thskvr) RRECT]:

[http://www.wikidata.org (URL_TO_INSERT_RECORD_3767 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q937](http://www.wikidata.org (URL_TO_INSERT_RECORD_3768 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q937) instanceOf [http://www.wikidata.org (URL_TO_INSERT_RECORD_3769 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q5](http://www.wikidata.org (URL_TO_INSERT_RECORD_3770 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q5)

[http://www.wikidata.org (URL_TO_INSERT_RECORD_3771 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q937](http://www.wikidata.org (URL_TO_INSERT_RECORD_3772 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q937) rdfs:label “Albert Einstein”

[http://www.wikidata.org (URL_TO_INSERT_RECORD_3773 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q88665](http://www.wikidata.org (URL_TO_INSERT_RECORD_3774 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q88665) instanceOf [http://www.wikidata.org (URL_TO_INSERT_RECORD_3775 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q5](http://www.wikidata.org (URL_TO_INSERT_RECORD_3776 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q5)

[http://www.wikidata.org (URL_TO_INSERT_RECORD_3777 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q88665](http://www.wikidata.org (URL_TO_INSERT_RECORD_3778 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q88665) rdfs:label “Hermann Einstein”

[http://www.wikidata.org (URL_TO_INSERT_RECORD_3779 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q5](http://www.wikidata.org (URL_TO_INSERT_RECORD_3780 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q5) [http://www.wikidata.org (URL_TO_INSERT_RECORD_3781 https://fairsharing.org/FAIRsharing.6s749p) /entity/P22](http://www.wikidata.org (URL_TO_INSERT_RECORD_3782 https://fairsharing.org/FAIRsharing.6s749p) /entity/P22)  [http://www.wikidata.org (URL_TO_INSERT_RECORD_3783 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q88665](http://www.wikidata.org (URL_TO_INSERT_RECORD_3784 https://fairsharing.org/FAIRsharing.6s749p) /entity/Q88665)




Property: [http://www.wikidata.org (URL_TO_INSERT_RECORD_3785 https://fairsharing.org/FAIRsharing.6s749p) /entity/P18](http://www.wikidata.org (URL_TO_INSERT_RECORD_3786 https://fairsharing.org/FAIRsharing.6s749p) /entity/P18)

Vs

[https://www.wikidata.org (URL_TO_INSERT_RECORD_3787 https://fairsharing.org/FAIRsharing.6s749p) /wiki/Property:P18](https://www.wikidata.org (URL_TO_INSERT_RECORD_3788 https://fairsharing.org/FAIRsharing.6s749p) /wiki/Property:P18)

[http://www.wikidata.org (URL_TO_INSERT_RECORD_3789 https://fairsharing.org/FAIRsharing.6s749p) /prop/direct/P18](http://www.wikidata.org (URL_TO_INSERT_RECORD_3790 https://fairsharing.org/FAIRsharing.6s749p) /prop/direct/P18)

```{warning}
Check documentation about the wikidata model to understand the various identifier patterns and their meaning/effect
````


#### Mapping in OpenRefine

The RDF (URL_TO_INSERT_RECORD_3791 https://fairsharing.org/FAIRsharing.p77ph9)  plugin in OpenRefine allows to map (URL_TO_INSERT_RECORD_3792 https://fairsharing.org/FAIRsharing.53edcc)  a table in OpenRefine to a graph pattern where the content of other columns can be added.

[BRIEF SCREE (URL_TO_INSERT_RECORD_3793 https://fairsharing.org/FAIRsharing.0b711a) NSHOT FR (URL_TO_INSERT_RECORD_3796 https://fairsharing.org/FAIRsharing.e7e609) O (URL_TO_INSERT_RECORD_3794 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_3795 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_3797 https://fairsharing.org/FAIRsharing.cp0ybc) M THE WEB]

[ADD LINK TO (URL_TO_INSERT_RECORD_3798 https://fairsharing.org/FAIRsharing.w69t6r)  TUTO (URL_TO_INSERT_RECORD_3799 https://fairsharing.org/FAIRsharing.w69t6r) RIALS]



````{dropdown}
:open:
```{figure} ../../../images/rdf-align-openrefine.png
---
width: 800px
name: RDF (URL_TO_INSERT_RECORD_3800 https://fairsharing.org/FAIRsharing.p77ph9)  schema alignment in OpenRefine
alt: RDF (URL_TO_INSERT_RECORD_3801 https://fairsharing.org/FAIRsharing.p77ph9)  schema alignment in OpenRefine
---
RDF (URL_TO_INSERT_RECORD_3802 https://fairsharing.org/FAIRsharing.p77ph9)  schema alignment in OpenRefine
```
````



The system assists the users in defining how the table should look like in RDF (URL_TO_INSERT_RECORD_3803 https://fairsharing.org/FAIRsharing.p77ph9) , fundamentally providing a template editor.

[MA (URL_TO_INSERT_RECORD_3807 https://fairsharing.org/FAIRsharing.pdwqcr) YBE ADD RUN EXAMP (URL_TO_INSERT_RECORD_3804 https://fairsharing.org/FAIRsharing.kg1x4z) LE FR (URL_TO_INSERT_RECORD_3809 https://fairsharing.org/FAIRsharing.e7e609) O (URL_TO_INSERT_RECORD_3806 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_3808 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_3810 https://fairsharing.org/FAIRsharing.cp0ybc) M THE SIMP (URL_TO_INSERT_RECORD_3805 https://fairsharing.org/FAIRsharing.kg1x4z) LE TABLE ABOVE HERE].

[TO (URL_TO_INSERT_RECORD_3811 https://fairsharing.org/FAIRsharing.w69t6r)  REMEMBER/CHECK: does it make blank nodes? Where does auto-suggest fish from?]


#### Mapping in Karma 

Karma ([https://usc-isi-i2.github.io/karma/](https://usc-isi-i2.github.io/karma/)) is a Desktop tool specifically
designed to map (URL_TO_INSERT_RECORD_3813 https://fairsharing.org/FAIRsharing.53edcc)  data to RDF (URL_TO_INSERT_RECORD_3812 https://fairsharing.org/FAIRsharing.p77ph9) . 
It covers different input format (URL_TO_INSERT_TERM_3814 https://fairsharing.org/search?recordType=model_and_format) s (e.g.: JSO (URL_TO_INSERT_RECORD_3816 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_3815 https://fairsharing.org/FAIRsharing.5bbab9)  and hierarch (URL_TO_INSERT_RECORD_3817 https://fairsharing.org/FAIRsharing.52b22c) ical content).
In terms of functionality, it is different from OpenRefine in some fundamental ways:


* **Use of ontologies (URL_TO_INSERT_TERM_3818 https://fairsharing.org/search?recordType=terminology_artefact) **. When map (URL_TO_INSERT_RECORD_3821 https://fairsharing.org/FAIRsharing.53edcc) ping a dataset to RDF (URL_TO_INSERT_RECORD_3820 https://fairsharing.org/FAIRsharing.p77ph9) , one can create the required classes and properties URI (URL_TO_INSERT_RECORD_3819 https://fairsharing.org/FAIRsharing.d261e1) s “while doing the map (URL_TO_INSERT_RECORD_3822 https://fairsharing.org/FAIRsharing.53edcc) ping”.
Karma requires the full ontology (URL_TO_INSERT_TERM_3823 https://fairsharing.org/search?recordType=terminology_artefact)  to map (URL_TO_INSERT_RECORD_3824 https://fairsharing.org/FAIRsharing.53edcc)  to to be present a-priori.
* **Map (URL_TO_INSERT_RECORD_3826 https://fairsharing.org/FAIRsharing.53edcc) ping suggestions**. Thanks to knowing the target ontology (URL_TO_INSERT_TERM_3825 https://fairsharing.org/search?recordType=terminology_artefact) , Karma can learn from previous map (URL_TO_INSERT_RECORD_3827 https://fairsharing.org/FAIRsharing.53edcc) pings and provide increasingly accurate suggestions.
* **User interface**. Karma allows to paint the graph pattern over the table, while OpenRefine has a more crude text-based interface.
* **Data reconciliation**. This is very limited in Karma (limited to three entity types only!).
* **Generic data transformat (URL_TO_INSERT_TERM_3828 https://fairsharing.org/search?recordType=model_and_format) ion**. Both tools can apply simple data transformat (URL_TO_INSERT_TERM_3829 https://fairsharing.org/search?recordType=model_and_format) ions (e.g.: via javascript function).  
However, OpenRefine is far more complete in these functionalities.
* **Batch processing**. Karma is an editor that saves a specification file that can then be invoked via the 
web interface but also via command line and eventually in a high performance spark environment. 
OpenRefine batch capabilities are very limited (In the latest version, OpenRefine is also implementing a spark arch (URL_TO_INSERT_RECORD_3830 https://fairsharing.org/FAIRsharing.52b22c) itecture, albeit locally on the Desktop machine).
Karma expresses map (URL_TO_INSERT_RECORD_3832 https://fairsharing.org/FAIRsharing.53edcc) pings in the KARMA (URL_TO_INSERT_RECORD_3833 https://fairsharing.org/FAIRsharing.pdwqcr)  language, that is an extension of [R2R (URL_TO_INSERT_RECORD_3831 https://fairsharing.org/FAIRsharing.ZEbjok) ML](https://www.w3.org/TR/r2rml/).

An example of a map (URL_TO_INSERT_RECORD_3834 https://fairsharing.org/FAIRsharing.53edcc) ping session in Karma:

````{dropdown}
:open:
```{figure} ../../../images/rdf-align-karma.png
---
width: 800px
name: RDF (URL_TO_INSERT_RECORD_3835 https://fairsharing.org/FAIRsharing.p77ph9)  schema alignment in Karma
alt: RDF (URL_TO_INSERT_RECORD_3836 https://fairsharing.org/FAIRsharing.p77ph9)  schema alignment in Karma
---
RDF (URL_TO_INSERT_RECORD_3837 https://fairsharing.org/FAIRsharing.p77ph9)  schema alignment in Karma
```
````



[[https://github.com (URL_TO_INSERT_RECORD_3838 https://fairsharing.org/FAIRsharing.c55d5e) /szeke/karma-tcdl-tutorial/wiki](https://github.com (URL_TO_INSERT_RECORD_3839 https://fairsharing.org/FAIRsharing.c55d5e) /szeke/karma-tcdl-tutorial/wiki)]

[SHOULD HAVE A STEP (URL_TO_INSERT_RECORD_3842 https://fairsharing.org/FAIRsharing.w7kfdn)  BY STEP (URL_TO_INSERT_RECORD_3843 https://fairsharing.org/FAIRsharing.w7kfdn)  EXAMP (URL_TO_INSERT_RECORD_3840 https://fairsharing.org/FAIRsharing.kg1x4z) LE WITH THE ABOVE SIMP (URL_TO_INSERT_RECORD_3841 https://fairsharing.org/FAIRsharing.kg1x4z) LE TABLE]


#### R2RML 

When source data exists in a relational structure, a map (URL_TO_INSERT_RECORD_3846 https://fairsharing.org/FAIRsharing.53edcc) ping to a graph can be expressed via the standard (URL_TO_INSERT_TERM_3844 https://fairsharing.org/search?fairsharingRegistry=Standard)  language R2R (URL_TO_INSERT_RECORD_3845 https://fairsharing.org/FAIRsharing.ZEbjok) ML (https://www.w3.org/TR/r2rml/).


### Notes on the FAIRification (as a KG) workflow


#### What comes first 

Reconciliation and map (URL_TO_INSERT_RECORD_3847 https://fairsharing.org/FAIRsharing.53edcc) ping to a graph are to a degree two independent steps.
The Typical OpenRefine workflow would first do reconciliation and then map (URL_TO_INSERT_RECORD_3848 https://fairsharing.org/FAIRsharing.53edcc) ping. 
In general, it makes sense to follow these steps in this order: when map (URL_TO_INSERT_RECORD_3849 https://fairsharing.org/FAIRsharing.53edcc) ping to a graph, one could take specific 
actions depending on whether an identifier (URL_TO_INSERT_TERM_3850 https://fairsharing.org/search?recordType=identifier_schema)  was found or not. 
And predictive approaches could be made more precise.

It is however possible to map (URL_TO_INSERT_RECORD_3851 https://fairsharing.org/FAIRsharing.53edcc)  data to a graph without performing any reconciliation step (in general the resulting graph will not be fully FAIR (URL_TO_INSERT_RECORD_3852 https://fairsharing.org/FAIRsharing.WWI10U) ).


#### QA and staging 

OpenRefine is an interactive tool and the user explicitly needs to select which “reconciliation proposal” to 
select among a few presented. 
In general automated reconciliation processes will provide suggestions with a confidence level. 
It is important to design systems where a QA can be put in place.
One approach could be to have staging area where map (URL_TO_INSERT_RECORD_3853 https://fairsharing.org/FAIRsharing.53edcc) pings are reviewed, and only approved ones can be merged in an overall KG.


### Working on the graph

A useful set of tools for KG manipulation is the KGTK: [https://kgtk.readthedocs.io/en/latest/](https://kgtk.readthedocs.io/en/latest/)

This provides Import/Export between different format (URL_TO_INSERT_TERM_3854 https://fairsharing.org/search?recordType=model_and_format) s, operators (e.g.: as joins, sub-setting) and useful analytical functions.

[NOTE: NVS (URL_TO_INSERT_RECORD_3857 https://fairsharing.org/FAIRsharing.Ckg0bl)  (URL_TO_INSERT_RECORD_3858 https://fairsharing.org/FAIRsharing.LSUZRp)  ENGAGED IN A PRO (URL_TO_INSERT_RECORD_3856 https://fairsharing.org/FAIRsharing.3e88d6)  (URL_TO_INSERT_RECORD_3860 https://fairsharing.org/FAIRsharing.9w8ea0)  (URL_TO_INSERT_RECORD_3861 https://fairsharing.org/FAIRsharing.504c6c)  (URL_TO_INSERT_RECORD_3862 https://fairsharing.org/FAIRsharing.4ndncv)  (URL_TO_INSERT_RECORD_3863 https://fairsharing.org/FAIRsharing.cp0ybc) JECT (URL_TO_INSERT_TERM_3855 https://fairsharing.org/search?recordType=project)  FO (URL_TO_INSERT_RECORD_3864 https://fairsharing.org/FAIRsharing.ca63ce) R KGTK EXTENSIO (URL_TO_INSERT_RECORD_3859 https://fairsharing.org/FAIRsharing.dpkb5f) N]


### Closed loop FAIRification [very draft, but we did have some architectures here]

We can use OpenRefine to `FAIR (URL_TO_INSERT_RECORD_3867 https://fairsharing.org/FAIRsharing.WWI10U) ify` data using a KG as a source of “reference informat (URL_TO_INSERT_TERM_3865 https://fairsharing.org/search?recordType=model_and_format) ion” or ontologies (URL_TO_INSERT_TERM_3866 https://fairsharing.org/search?recordType=terminology_artefact) . 
At the same time we can export data via OpenRefine into a KG.

We therefore have a system that can be used to generate a KG that improves the performance of the system itself.

A particular aspect of (automated) FAIR (URL_TO_INSERT_RECORD_3868 https://fairsharing.org/FAIRsharing.WWI10U) ification would then be to have systems able to automatically link data to an overall knowledge graph.

[[https://github.com (URL_TO_INSERT_RECORD_3869 https://fairsharing.org/FAIRsharing.c55d5e) /usc-isi-i2/table-linker](https://github.com (URL_TO_INSERT_RECORD_3870 https://fairsharing.org/FAIRsharing.c55d5e) /usc-isi-i2/table-linker)]


### Exploring the graph 


#### RelFinder 

Once we have informat (URL_TO_INSERT_TERM_3871 https://fairsharing.org/search?recordType=model_and_format) ion as a KG, it is useful to have tools to explore it.
One such simple tool is [RelFinder](http://www.visualdataweb.org/relfinder.php) ).

The tool can be pointed to a triplestore and allows discovering connections between two or more entities.
Its capabilities are very limited, and it does not perform an exhaustive search (URL_TO_INSERT_RECORD_3872 https://fairsharing.org/FAIRsharing.52b22c) , and being implemented in Flash, it is now obsolete.
However, it is a useful tool to demonstrate why a KG is useful.

An implementation on a more modern technology stack is available at [https://github.com (URL_TO_INSERT_RECORD_3873 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/RelFinderNG](https://github.com (URL_TO_INSERT_RECORD_3874 https://fairsharing.org/FAIRsharing.c55d5e) /FAIRplus/RelFinderNG),

and many more tools and libraries exist to provide visual insights over KG
https://graphdb.ontotext.com/documentation/free/devhub/custom-graph-views.html

## Conclusion:

This content provides a basic overview of reconciliation tools for dealing with relative lightweight processes to convert tabular data to an RDF (URL_TO_INSERT_RECORD_3875 https://fairsharing.org/FAIRsharing.p77ph9)  Linked Data graph.
It complements content related to ETL to RDF (URL_TO_INSERT_RECORD_3876 https://fairsharing.org/FAIRsharing.p77ph9) .
While a lot of material already exists about using OpenRefine for performing such tasks, the value added by the recipe 
rests on the setting up of a Wikibase instance to provide the reconciliation reference.


### What to read next? 

* [An inventory of tools for converting data to RDF (URL_TO_INSERT_RECORD_3878 https://fairsharing.org/FAIRsharing.p77ph9) ](https://w3id.org (URL_TO_INSERT_RECORD_3877 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB051)
* [Creating Linked Data with OpenRefine](https://medium.com/wallscope/creating-linked-data-31c7dd479a9e)
* [Using OntoRefine to Transform Tabular Data into Linked Data](https://medium.com/wallscope/creating-linked-data-31c7dd479a9e
* [OntoRefine](https://graphdb.ontotext.com/documentation/free/loading-data-using-ontorefine.html) tutorial by [OntoText](https://www.ontotext.com/knowledgehub/fundamentals/ontorefine-2/)

````{rdmkit_panel}
````

## References

````{dropdown} **Reference**
```{footbibliography}
```
````


## Authors
````{authors_fairplus}
AndreaSplendiani: Writing - Original Draft
Philippe: Review & Editing
Yojana: Review & Editing
````

<!-- 
Andraa Waagmeester: Review & Editing 
Martin Magdinier: (RefinePro) 
-->

## License
````{license_fairplus}
CC-BY-4.0
````


     
