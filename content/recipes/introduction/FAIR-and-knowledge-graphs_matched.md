(fcb-intro-kr)=

# FAIR and Knowledge graphs 


````{panels_fairplus}
:identifier_text: FCB070
:identifier_link: 'https://w3id.org/faircookbook/FCB070'
:difficulty_level: 2
:recipe_type: guidance
:reading_time_minutes: 10
:intended_audience:  everyone 
:has_executable_code: nope
:maturity_level: 0
:maturity_indicator: 0
:recipe_name: Understanding the relation between FAIR and Knowledge Graphs
```` 

## Main Objectives

In the following sections, we will cover the following topics:

1. the relation between FAIR (URL_TO_INSERT_RECORD_8093 https://fairsharing.org/FAIRsharing.WWI10U)  and KGs.
2. the typology of knowledge graphs (KG).
3. the different technologies supporting them.
4. the methods to generate knowledge graphs.
5. the impact of graph-based representations on what it means to deliver FAIR (URL_TO_INSERT_RECORD_8094 https://fairsharing.org/FAIRsharing.WWI10U)  data and services.
<!-- 6. the impact for Pharma industry and EFPIA more broadly -->



## FAIR and Knowledge Graphs

FAIR (URL_TO_INSERT_RECORD_8095 https://fairsharing.org/FAIRsharing.WWI10U)  is chiefly about three things: metadata, metadata and metadata. 

Not only that, but metadata which should be **active**, that is usable by software agents without the need of human intervention,
thanks to the resolvable links found in the electronic documents and the associated semantics available to the agent.
The goal is to speed up data handling by ensuring enough informat (URL_TO_INSERT_TERM_8096 https://fairsharing.org/search?recordType=model_and_format) ion is provided to machines.

In this context, the availability of semantic web technologies completely aligns with the key requirements defined by 
the FAIR (URL_TO_INSERT_RECORD_8098 https://fairsharing.org/FAIRsharing.WWI10U)  principles (URL_TO_INSERT_RECORD_8097 https://fairsharing.org/FAIRsharing.WWI10U) . 
Thus, providing metadata about a dataset in the form of Linked Data Graph is a significant path towards making data FAIR (URL_TO_INSERT_RECORD_8099 https://fairsharing.org/FAIRsharing.WWI10U) .
Furthermore, the availability of knowledge representation in a graph data structure, or knowledge graphs, 
provides contextual informat (URL_TO_INSERT_TERM_8100 https://fairsharing.org/search?recordType=model_and_format) ion about the dataset and shows the relationship between data and curated domain knowledge,
which is particularly useful for machine learning and artificial intelligence approach. 

> But `FAIR (URL_TO_INSERT_RECORD_8101 https://fairsharing.org/FAIRsharing.WWI10U)  data` and `knowledge graphs` are not equivalent. Not all FAIR (URL_TO_INSERT_RECORD_8102 https://fairsharing.org/FAIRsharing.WWI10U)  data is a knowledge graph and not all knowledge graphs are FAIR (URL_TO_INSERT_RECORD_8103 https://fairsharing.org/FAIRsharing.WWI10U) .

## What are knowledge graph and graph databases?

Knowledge Graph (KG) and graph database (URL_TO_INSERT_TERM_8104 https://fairsharing.org/search?fairsharingRegistry=Database) s constitute a new approach to representation, storage and querying of data.

To understand the notion of `knowledge graphs`, we need to remind ourselves about some elements of informat (URL_TO_INSERT_TERM_8106 https://fairsharing.org/search?recordType=model_and_format) ion theory, data structure, and data storage, as well as some geometric (URL_TO_INSERT_TERM_8105 https://fairsharing.org/search?recordType=metric)  interpretation of relationship between entities, which is often what turns data into knowledge.

Informat (URL_TO_INSERT_TERM_8110 https://fairsharing.org/search?recordType=model_and_format) ion, in digital forms, relies on formal representations and an array of methods to store and retrieve informat (URL_TO_INSERT_TERM_8111 https://fairsharing.org/search?recordType=model_and_format) ion. Up until the last 10 years, Relational DataBase (URL_TO_INSERT_TERM_8107 https://fairsharing.org/search?fairsharingRegistry=Database)  Management Systems (RDBMS) have been provided the backbone of informat (URL_TO_INSERT_TERM_8112 https://fairsharing.org/search?recordType=model_and_format) ion storage solutions, and still do so today. However, advances in both theoretical informat (URL_TO_INSERT_TERM_8113 https://fairsharing.org/search?recordType=model_and_format) ion representation model (URL_TO_INSERT_TERM_8108 https://fairsharing.org/search?recordType=model_and_format) s and technical solutions led to the development of so-called `NO-SQL` solutions (for 'Not-only Structured Query language'), supporting the onset of **graph-based representations of informat (URL_TO_INSERT_TERM_8114 https://fairsharing.org/search?recordType=model_and_format) ion**, in contrast to **relational-model (URL_TO_INSERT_TERM_8109 https://fairsharing.org/search?recordType=model_and_format)  based representation**. Knowledge graphs are knowledge bases which use graph-based data structure or topology to represent entities and the relationships between them.

```{admonition} **So how does graph theory come to meet knowledge representation?**

We need here to introduce the definition of a graph:

A graph is a set of nodes (also known as vertex) connected via edges. 
When the edges connected any two nodes carry a direction information, they defined a specific and important subfamily of graphs known as `directed graphs`. On the other hand, if there is absence of directionality information on the edges, such graphs are known as `undirected graphs`.

A graph can also contain cycles. This means that when traversing the graph from a starting or source node to an ending or target node (terminologically referred to as a path), in case of cycles, the sorurce and target node are the same. Such graphs are commonly known as `cyclic graphs`.

When cycles aren't allowed, a new subtype of graph is defined. Such graphs are known as `directed acyclic graphs` (DAG).

Volumes have been written about what graphs are and the underlying mathematical theories describing their properties. The readership can refer to the following resources for a complete overview and training. The purpose of this section is simply to provide a rapid overview of what knowledge graphs are and their typology, as one needs to be aware of the differences that exist between the different kinds of graphs and also understand the consequences both theoretical and technical to fully appreciate the pros and cons of the various implementations
available out there.

The following sections intend to provide a compact review and guide newcomers through the jargon and the various acronyms founds in the literature on the topic.
```
### Relational Databases and Graph Databases

Until fairly recently, the storage of informat (URL_TO_INSERT_TERM_8115 https://fairsharing.org/search?recordType=model_and_format) ion mainly relied on RDBMS, 
which have been to work-horse of database (URL_TO_INSERT_TERM_8116 https://fairsharing.org/search?fairsharingRegistry=Database)  building. With relational database (URL_TO_INSERT_TERM_8117 https://fairsharing.org/search?fairsharingRegistry=Database)  approach, informat (URL_TO_INSERT_TERM_8121 https://fairsharing.org/search?recordType=model_and_format) ion is model (URL_TO_INSERT_TERM_8118 https://fairsharing.org/search?recordType=model_and_format) led according to an `Entity Relationship Model (URL_TO_INSERT_TERM_8119 https://fairsharing.org/search?recordType=model_and_format)  (ER model (URL_TO_INSERT_TERM_8120 https://fairsharing.org/search?recordType=model_and_format) /ER diagram)`, the development of which undergoes a series of formal steps. 

One of these steps involves a process known as `schema normalization` to ensure that key entities and their attributes can be stored in `tables` in the most parsimonious way. This step is necessary to ensure query performance and optimization. 

Relational database (URL_TO_INSERT_TERM_8122 https://fairsharing.org/search?fairsharingRegistry=Database)  approaches track and store relations between entities using what is known as `linking tables`. When interrogating a database (URL_TO_INSERT_TERM_8123 https://fairsharing.org/search?fairsharingRegistry=Database)  operating under this paradigm (e.g. MySQL, PostgreSQL, Oracle DB, to name a few), the database (URL_TO_INSERT_TERM_8124 https://fairsharing.org/search?fairsharingRegistry=Database)  engine needs to run `JOIN` operations, a type of SQL queries hitting the table of entities and any linking table holding the informat (URL_TO_INSERT_TERM_8125 https://fairsharing.org/search?recordType=model_and_format) ion about the relations between entities. 

While sophisticated optimization methods exist to ensure query performance does not suffer as both data volume grows or complexity of the underlying model (URL_TO_INSERT_TERM_8126 https://fairsharing.org/search?recordType=model_and_format)  increases, this form of informat (URL_TO_INSERT_TERM_8127 https://fairsharing.org/search?recordType=model_and_format) ion storage may suffer from performance issue in certain situations.

An added criticism often leveled to RDBMS based database (URL_TO_INSERT_TERM_8128 https://fairsharing.org/search?fairsharingRegistry=Database)  is the rigidity, which manifests itself in the difficulty and complexity of changing the underlying model (URL_TO_INSERT_TERM_8129 https://fairsharing.org/search?recordType=model_and_format) , leading to potentially complex migration tasks. 
This can become a limitation when knowledge representation in a particular domain requires frequent changes for whatever reason.

So it is in this context that the advent of `graph (oriented) database (URL_TO_INSERT_TERM_8130 https://fairsharing.org/search?fairsharingRegistry=Database) s` (sometimes referred to as NoSQL database (URL_TO_INSERT_TERM_8131 https://fairsharing.org/search?fairsharingRegistry=Database) , for 'Not Only SQL database (URL_TO_INSERT_TERM_8132 https://fairsharing.org/search?fairsharingRegistry=Database) '), came about, with a new paradigm and bold claims. 
Over the last 20 years, the idea of storing knowledge as a graph `G=(v for vertex, e for edge)`,
even if not new at all from a theoretical perspective, has undergone tremendous progress to the point that a transition,
in some sectors of the industry, is taking place.

KGs and graph database (URL_TO_INSERT_TERM_8133 https://fairsharing.org/search?fairsharingRegistry=Database) s claim to be capable of offering new insights with better performance, 
owning to the optimization of their query engine for fast traversals. 
With description logics (DL), knowledge graphs represent knowledge to allow "intelligent" machines and algorithms to reason over and work with.
Hence, for some domain specific representations and tasks, `Knowledge Graphs` (KG)
and graph database (URL_TO_INSERT_TERM_8134 https://fairsharing.org/search?fairsharingRegistry=Database) s are seen as more suited than RDBMS storage.

These benefits warrant the significant investments made to develop tools and frameworks to support KG storage solutions. 
It also means that KG are becoming mainstream.

 It is not that graph-oriented data storage is replacing RDBMS storage. As always, with all technologies and tooling, one needs to understand the task at hand and choose the most suitable 
solutions for addressing a specific challenge. 

## The different types of knowledge graphs

````{dropdown} **The 2 main types of Knowledge Graph - Graphical Overview**
:open:

```{figure} kg-typology.png
---
width: 1000px
name: kg-typology
alt: Knowledge Graph Types
---
Data Use
```

RDF Graph and Labeled Property graphs
````

### 1. RDF graphs

#### i. Defining RDF, Resource Description Framework
Here, we need to introduce the notion of representing statements as a predicate of the following form:
`<subject><predicate><object>`, such as: `'P53 protein' 'interacts_with' 'DNA'`.

This statement can be formally expressed using a dedicated syntax called [RDF](https://www.w3.org/TR/rdf11-concepts/), 
standing for "Resource Description Framework (URL_TO_INSERT_RECORD_8136 https://fairsharing.org/FAIRsharing.p77ph9) ", one of the World Wide Web Consortium (W3C) standard (URL_TO_INSERT_TERM_8135 https://fairsharing.org/search?fairsharingRegistry=Standard) s supporting the vision of a **Semantic Web** as 
outlined by Sir Tim Berners-Lee and colleagues {footcite}`bernerslee2001semantic`.
In this instance, because the relation `'interacts_with'` is directional, we are creating the simplest form of directed graph,
by establishing an `edge` between two `nodes`.

``````{admonition} **When does a RDF Graph become a Linked Data Graph?**
:class: tip
When all the entities in an RDF statement are identified and available as `Universal Resource Identifiers(URI)`,
the RDF graph then becomes a `Linked Data Graph`, since each entity is no longer an `plain literal` and can now be 
**looked up by means of HTTP requests** .

```bash
`P53 protein` `physically interacts with` `DNA`.
```

using Wikidata identifiers can be expressed as: 

````markdown
"@wdt": "https://www.wikidata.org (URL_TO_INSERT_RECORD_8137 https://fairsharing.org/FAIRsharing.6s749p) /wiki/"
[wdt:Q283350](https://www.wikidata.org (URL_TO_INSERT_RECORD_8138 https://fairsharing.org/FAIRsharing.6s749p) /wiki/Q283350) [wdt:Property:P129](https://www.wikidata.org (URL_TO_INSERT_RECORD_8139 https://fairsharing.org/FAIRsharing.6s749p) /wiki/Property:P129) 
[wdt:Q7430](https://www.wikidata.org (URL_TO_INSERT_RECORD_8140 https://fairsharing.org/FAIRsharing.6s749p) /wiki/Q7430)
````
``````

The `RDF (URL_TO_INSERT_RECORD_8141 https://fairsharing.org/FAIRsharing.p77ph9)  syntax` allows the expression of `RDF (URL_TO_INSERT_RECORD_8142 https://fairsharing.org/FAIRsharing.p77ph9)  statements`, which can be built and grouped (URL_TO_INSERT_RECORD_8144 https://fairsharing.org/FAIRsharing.31385c)  in an `RDF (URL_TO_INSERT_RECORD_8143 https://fairsharing.org/FAIRsharing.p77ph9)  graph`.

So let’s go back to the statement about the gene product of the P53 gene. 
The formal and structured representation of a fact about that gene is now a well established technique.
Therefore, one can see that natural fit between the data structure and knowledge gathered and accumulated by scientists.
This is why knowledge graphs have gained so much traction in recent years. 
In fact, a number of developments converged to make this form of representation effective and above all useful
for computational work.



##### ii. Persisting RDF graphs: RDF triple Stores

RDF (URL_TO_INSERT_RECORD_8147 https://fairsharing.org/FAIRsharing.p77ph9)  graph objects can be persisted in specialized database (URL_TO_INSERT_TERM_8145 https://fairsharing.org/search?fairsharingRegistry=Database) s, `RDF (URL_TO_INSERT_RECORD_8148 https://fairsharing.org/FAIRsharing.p77ph9)  graph database (URL_TO_INSERT_TERM_8146 https://fairsharing.org/search?fairsharingRegistry=Database) s` also known as `RDF (URL_TO_INSERT_RECORD_8149 https://fairsharing.org/FAIRsharing.p77ph9)  triple stores`. 
Some of the most performant and successful solutions are:
- [Allegrograph](https://allegrograph.com/products/allegrograph/)
- [Blazegraph](https://github.com (URL_TO_INSERT_RECORD_8150 https://fairsharing.org/FAIRsharing.c55d5e) /blazegraph)
- [GraphDB](https://www.ontotext.com/products/graphdb)
- [Stardog](https://www.stardog.com/)
- [Virtuoso](https://virtuoso.openlinksw.com)


##### iii. Validating and controlling the quality of the RDF data being loaded - 

To validate and control the quality of the fast emerging RDF (URL_TO_INSERT_RECORD_8151 https://fairsharing.org/FAIRsharing.p77ph9)  triples.
The W3C has produced a specification detailing a constraint language which allows data managers to control the so-called
`shape` of the RDF (URL_TO_INSERT_RECORD_8152 https://fairsharing.org/FAIRsharing.p77ph9)  graph coming in. The W3C SHAC (URL_TO_INSERT_RECORD_8156 https://fairsharing.org/FAIRsharing.md3e78) L (URL_TO_INSERT_RECORD_8153 https://fairsharing.org/FAIRsharing.j9y503)  (URL_TO_INSERT_RECORD_8154 https://fairsharing.org/FAIRsharing.f1449d)  SHApe Constraint Language, known as [SHACL](https://www.w3.org/TR/shacl (URL_TO_INSERT_RECORD_8155 https://fairsharing.org/FAIRsharing.f1449d) /) (pronounced `shackle`),
allow to express a set of conditions to validate RDF (URL_TO_INSERT_RECORD_8157 https://fairsharing.org/FAIRsharing.p77ph9)  graphs/RDF (URL_TO_INSERT_RECORD_8158 https://fairsharing.org/FAIRsharing.p77ph9)  statements. SHAC (URL_TO_INSERT_RECORD_8162 https://fairsharing.org/FAIRsharing.md3e78) L (URL_TO_INSERT_RECORD_8160 https://fairsharing.org/FAIRsharing.j9y503)  (URL_TO_INSERT_RECORD_8161 https://fairsharing.org/FAIRsharing.f1449d)  expressions are RDF (URL_TO_INSERT_RECORD_8159 https://fairsharing.org/FAIRsharing.p77ph9)  statements 
and the constraint profiles can be stored in an RDF (URL_TO_INSERT_RECORD_8163 https://fairsharing.org/FAIRsharing.p77ph9)  triple store. 
SHAC (URL_TO_INSERT_RECORD_8166 https://fairsharing.org/FAIRsharing.md3e78) L (URL_TO_INSERT_RECORD_8164 https://fairsharing.org/FAIRsharing.j9y503)  (URL_TO_INSERT_RECORD_8165 https://fairsharing.org/FAIRsharing.f1449d)  specifications are implemented in the [TopQuadrant TopBraid Composer tool](https://www.topquadrant.com/products/topbraid-composer/).

A competing specification, know as [SHEX](https://shex.io/) for `Shape Expression`, provides a similar functionality,
but isn't a W3C approved specifications, even though SHEX is proving quite popular and with a strong following.

##### iv. Querying an RDF graph - the W3C SPARQL Query Language

RDF (URL_TO_INSERT_RECORD_8167 https://fairsharing.org/FAIRsharing.p77ph9)  graphs stored in RDF (URL_TO_INSERT_RECORD_8168 https://fairsharing.org/FAIRsharing.p77ph9)  triple stores can be queried using a dedicated query language defined by a W3C specification known as 
[SP (URL_TO_INSERT_RECORD_8170 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_8169 https://fairsharing.org/FAIRsharing.87ccfd)  1.1](https://www.w3.org/TR/sparql11-query/).
SP (URL_TO_INSERT_RECORD_8173 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_8171 https://fairsharing.org/FAIRsharing.87ccfd)  stands for `SP (URL_TO_INSERT_RECORD_8174 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_8172 https://fairsharing.org/FAIRsharing.87ccfd)  Query Language`, (pronounced `sparkle`) {footcite}`sparql`. 
The results of a SP (URL_TO_INSERT_RECORD_8179 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_8178 https://fairsharing.org/FAIRsharing.87ccfd)  query are a `result set` or `RDF (URL_TO_INSERT_RECORD_8176 https://fairsharing.org/FAIRsharing.p77ph9)  graph` and is therefore **a collection (URL_TO_INSERT_TERM_8175 https://fairsharing.org/search?recordType=collection)  of RDF (URL_TO_INSERT_RECORD_8177 https://fairsharing.org/FAIRsharing.p77ph9)  triples**.

An impressive feature of the SP (URL_TO_INSERT_RECORD_8181 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_8180 https://fairsharing.org/FAIRsharing.87ccfd)  query language is its ability to perform `mashups` by performing federated queries
over a number of 'SERVICES', i.e. RDF (URL_TO_INSERT_RECORD_8182 https://fairsharing.org/FAIRsharing.p77ph9)  triple store endpoints and return an RDF (URL_TO_INSERT_RECORD_8183 https://fairsharing.org/FAIRsharing.p77ph9)  graph which contains triples assembled
from a number of resources.

We still need to introduce several key concepts to provide a fuller picture of knowledge graph, how they are generated
and why they matter.

````{dropdown} **SPARQL query example: Metabolites and the species they are found in**
:open:
```{figure} ../../../images/wikidata-sparql.jpg
---
width: 1000px
name: wikidata (URL_TO_INSERT_RECORD_8184 https://fairsharing.org/FAIRsharing.6s749p)  sparql
alt: wikidata (URL_TO_INSERT_RECORD_8185 https://fairsharing.org/FAIRsharing.6s749p)  sparql
---
A SP (URL_TO_INSERT_RECORD_8189 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_8188 https://fairsharing.org/FAIRsharing.87ccfd)  query over Wikidata (URL_TO_INSERT_RECORD_8187 https://fairsharing.org/FAIRsharing.6s749p)  RDF (URL_TO_INSERT_RECORD_8186 https://fairsharing.org/FAIRsharing.p77ph9)  endpoint
```
````


````{dropdown} **SPARQL query example on WikiData: Cell lines with names that could also be URLs**
:open:
```{figure} ../../../images/wikidata-sparql-celllines.jpg
---
width: 1000px
name: wikidata (URL_TO_INSERT_RECORD_8190 https://fairsharing.org/FAIRsharing.6s749p)  sparql endpoint
alt: wikidata (URL_TO_INSERT_RECORD_8191 https://fairsharing.org/FAIRsharing.6s749p)  sparql endpoint
---
A SP (URL_TO_INSERT_RECORD_8196 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_8195 https://fairsharing.org/FAIRsharing.87ccfd)  query over Wikidata (URL_TO_INSERT_RECORD_8193 https://fairsharing.org/FAIRsharing.6s749p)  RDF (URL_TO_INSERT_RECORD_8192 https://fairsharing.org/FAIRsharing.p77ph9)  endpoint: Cell lines with names that could also be URL (URL_TO_INSERT_RECORD_8194 https://fairsharing.org/FAIRsharing.9d38e2) s (Internet of Cell Lines)
```
````

Wikidata (URL_TO_INSERT_RECORD_8197 https://fairsharing.org/FAIRsharing.6s749p)  provides a list of SP (URL_TO_INSERT_RECORD_8199 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_8198 https://fairsharing.org/FAIRsharing.87ccfd)  query examples,
see [here](https://www.wikidata.org (URL_TO_INSERT_RECORD_8200 https://fairsharing.org/FAIRsharing.6s749p) /wiki/Wikidata:SPARQL_query_service/queries/examples#Cell_lines_with_names_that_could_also_be_URLs_\(Internet_of_Cell_Lines\)).


### 2. Property graphs
    
Like `RDF (URL_TO_INSERT_RECORD_8201 https://fairsharing.org/FAIRsharing.p77ph9)  graphs`, `property graphs(PG)` are also used to build `knowledge graphs`.
However, unlike `RDF (URL_TO_INSERT_RECORD_8202 https://fairsharing.org/FAIRsharing.p77ph9)  graphs`, `property graphs` allows the vertices (aka the `edge`) to carry *annotations*,
which can be queried. These `annotations` are called `properties` hence the denomination `Property graphs`,
also referred to as **`Labeled Property Graphs`** or **`LPG`**.

`Property graphs` have inherent interesting properties which set them aside from `RDF (URL_TO_INSERT_RECORD_8203 https://fairsharing.org/FAIRsharing.p77ph9)  graphs`.
For instance, in PG/LPG, both `nodes` and `edges` have:
- `(1..1) identifier (URL_TO_INSERT_TERM_8204 https://fairsharing.org/search?recordType=identifier_schema) `        
- `(1..n) annotations`, in the form of sets of `{key:value}` pairs    

In addition, `edges` have a `Type`. 

```{admonition} Important
:class: tip
The main thing to remember is that what distinguishes RDF graphs from Labeled Property graphs is that fact that the 
edges in a LPG can carry annotations. 
This allows for interesting properties which affect the querying options available to developers and data miners.
It is this difference that has been exploited to develop an entire environment of software solutions supported LPG 
based knowledge representation and exploitation.
```

These `property graphs` constitute the main **data structure** supported by two key resources which have gain notoriety
and visibility: one open-source and one commercial. In the following sections, we will provide a brief summary of their
salient points and also, limitations.

#### 2.1 Apache Tinkerpop framework and Gremlin graph traversal language

The Apache foundation released in 2009 the [Apache Tinkerpop framework](http://tinkerpop.apache.org/) as an open source
initiative, licensed under Apache License 2.0 terms.
* [Apache Tinkerpop](http://tinkerpop.apache.org/) is a **vendor agnostic graph database (URL_TO_INSERT_TERM_8205 https://fairsharing.org/search?fairsharingRegistry=Database)  storage framework** using on `property graphs` as 
underlying data structure.  As a framework, Tinkerpop is developed (URL_TO_INSERT_RECORD_8206 https://fairsharing.org/FAIRsharing.31385c)  as an abstract layer, meant to ensure vendor 
neutrality, allowing developers to decide about arch (URL_TO_INSERT_RECORD_8208 https://fairsharing.org/FAIRsharing.52b22c) itecture choices and tests while coding against a standard (URL_TO_INSERT_TERM_8207 https://fairsharing.org/search?fairsharingRegistry=Standard) ized
interface.
* [Apache Gremlin](https://tinkerpop.apache.org/docs/3.6.0/tutorials/gremlins-anatomy/) is the **query language** powering Tinkerpop and its interactions with the underlying data stored
as property graphs. Gremlin is a `graph traversal language` optimized for speed and fast access. 
Defined by Marko Rodrigues, Gremlin language specifications are detailed in the following publication 
{footcite}`10.1145/2815072.2815073` and is supported by libraries available in the most popular programming
language. Extensive documentation and training is available from the dedicated Apache project (URL_TO_INSERT_TERM_8209 https://fairsharing.org/search?recordType=project)  pages, 
including a set of [`recipes`](https://tinkerpop.apache.org/docs/current/recipes/) to make the most of the 
Gremlin language.

Below is an example of a Gremlin instruction as coded in python:

```python
from gremlin_python.process.traversal import T
from gremlin_python.process.traversal import Cardinality

id = T.id
single = Cardinality.single

def create_vertex(vid, vlabel):
    # default database cardinality is used when Cardinality argument is not specified
    g.addV(vlabel).property(id, vid). \
      property(single, 'name', 'Apache'). \
      property('lastname', 'Tinkerpop'). \
      next()
```


A Gremlin query to answer a request such `Get the names of the people vertex "1" knows who are over the age of 30`.

```groovy
g.V() 
g.V(1) 
g.V(1).values('name') 
g.V(1).outE('knows')
g.V(1).outE('knows').inV().values('name') 
g.V(1).out('knows').values('name') 
g.V(1).out('knows').has('age', gt(30)).values('name') 
```



#### 2.2 Neo4j property graph database and Cypher Query Language

[Neo4j](https://neo4j.com) is a commercial offering for building knowledge graphs relying on property graphs. 
Backing the approach, the team developed (URL_TO_INSERT_RECORD_8210 https://fairsharing.org/FAIRsharing.31385c)  a dedicated query language for `Labeled property graphs`. 
This language is known as `CYPHER`.

Neo4j database (URL_TO_INSERT_TERM_8211 https://fairsharing.org/search?fairsharingRegistry=Database) s have shown promises in biology and bioinformat (URL_TO_INSERT_TERM_8212 https://fairsharing.org/search?recordType=model_and_format) ics for its ability to allow for fast graph traversals, 
which matches the requirements of cell biologists, model (URL_TO_INSERT_TERM_8213 https://fairsharing.org/search?recordType=model_and_format) ers, and computational scientists who need to explore a growing
ensembl (URL_TO_INSERT_RECORD_8214 https://fairsharing.org/FAIRsharing.fx0mw7) e of molecular pathways, that is to say graphs of interactions and reactions.
An illustration of that natural fit is the uptake of the Neo4j technology by a project (URL_TO_INSERT_TERM_8215 https://fairsharing.org/search?recordType=project)  such as ` Disease Map (URL_TO_INSERT_RECORD_8216 https://fairsharing.org/FAIRsharing.53edcc) s`, 
Reactome (URL_TO_INSERT_RECORD_8217 https://fairsharing.org/FAIRsharing.tf6kj8)  {footcite}`pmid29377902` and KnetMiner (URL_TO_INSERT_RECORD_8218 https://fairsharing.org/FAIRsharing.826b4a) s {footcite}`pmid30085931`.

* The [Reactome (URL_TO_INSERT_RECORD_8219 https://fairsharing.org/FAIRsharing.tf6kj8)  database](https://reactome.org (URL_TO_INSERT_RECORD_8220 https://fairsharing.org/FAIRsharing.tf6kj8) /) builds on Neo4j to allow navigation of reactions and pathways.

A complete tutorial to query Reactome (URL_TO_INSERT_RECORD_8221 https://fairsharing.org/FAIRsharing.tf6kj8)  using the `Cypher language` to interrogate the underlying Neo4j store is
available [here](https://reactome.org (URL_TO_INSERT_RECORD_8222 https://fairsharing.org/FAIRsharing.tf6kj8) /dev/graph-database/extract-participating-molecules).

```bash
//All reactions for the pathway with stable identifier R-HSA-198933
MATCH (p:Pathway{stId:"R-HSA-983169"})-[:hasEvent*]->(rle:ReactionLikeEvent)
RETURN p.stId AS Pathway, rle.stId AS Reaction, rle.displayName AS ReactionName
```


````{dropdown} **CYPHER query example on Reactome: Comparison with SQL**
:open:
```{figure} ../../../images/pcbi.1005968.g001.jpg
---
width: 600px
name: reactome (URL_TO_INSERT_RECORD_8223 https://fairsharing.org/FAIRsharing.tf6kj8)  cypher query
alt: reactome (URL_TO_INSERT_RECORD_8224 https://fairsharing.org/FAIRsharing.tf6kj8)  cypher query
---
CYPHER query example on Reactome (URL_TO_INSERT_RECORD_8226 https://fairsharing.org/FAIRsharing.tf6kj8) : Comparison with SQL. From Fabregat et al,2018. 10.1371/journal (URL_TO_INSERT_TERM_8225 https://fairsharing.org/search?recordType=journal) .pcbi.1005968
```
````

* The [PDB (URL_TO_INSERT_RECORD_8230 https://fairsharing.org/FAIRsharing.9y4cqw) e (URL_TO_INSERT_RECORD_8227 https://fairsharing.org/FAIRsharing.26ek1v) -KB (URL_TO_INSERT_RECORD_8232 https://fairsharing.org/FAIRsharing.sFzdV7) ](PDB (URL_TO_INSERT_RECORD_8231 https://fairsharing.org/FAIRsharing.9y4cqw) e (URL_TO_INSERT_RECORD_8228 https://fairsharing.org/FAIRsharing.26ek1v) -KG https://www.ebi.ac.uk/pdbe (URL_TO_INSERT_RECORD_8229 https://fairsharing.org/FAIRsharing.26ek1v) /pdbe-kb/graph-download) is another relevant resources in the fields of
bioinformat (URL_TO_INSERT_TERM_8234 https://fairsharing.org/search?recordType=model_and_format) ics which is available as a Neo4j graph database (URL_TO_INSERT_TERM_8233 https://fairsharing.org/search?fairsharingRegistry=Database) . PDB (URL_TO_INSERT_RECORD_8237 https://fairsharing.org/FAIRsharing.9y4cqw) e (URL_TO_INSERT_RECORD_8235 https://fairsharing.org/FAIRsharing.26ek1v) -KB (URL_TO_INSERT_RECORD_8239 https://fairsharing.org/FAIRsharing.sFzdV7)  is a community-driven resource managed by the PDB (URL_TO_INSERT_RECORD_8238 https://fairsharing.org/FAIRsharing.9y4cqw) e (URL_TO_INSERT_RECORD_8236 https://fairsharing.org/FAIRsharing.26ek1v) 
team, collating functional annotations and predictions for structure data in the PDB (URL_TO_INSERT_RECORD_8240 https://fairsharing.org/FAIRsharing.9y4cqw)  arch (URL_TO_INSERT_RECORD_8241 https://fairsharing.org/FAIRsharing.52b22c) ive, the content of which is distributed
under CC-BY-4 license. PDFe-KB can be downloaded [here](PDB (URL_TO_INSERT_RECORD_8244 https://fairsharing.org/FAIRsharing.9y4cqw) e (URL_TO_INSERT_RECORD_8242 https://fairsharing.org/FAIRsharing.26ek1v) -KG https://www.ebi.ac.uk/pdbe (URL_TO_INSERT_RECORD_8243 https://fairsharing.org/FAIRsharing.26ek1v) /pdbe-kb/graph-download).



While Neo4j origin dates back to 2000, the company recently grabbed headlines for a [very successful IPO](https://neo4j.com/press-releases/neo4j-announces-seriesf-funding/) 
which netted circa 350 millions USD of venture capital funding. Such a success is testament to the robustness and 
validity of the approach taken by the group of computer scientists who built the solutions from the ground up to
deliver one of the most successful solution for property graph based knowledge representation and querying making 
full use of Neo4j representation and infrastructure capabilities.

Neo4J open-sourced the Cypher query language and made it available via GitHub (URL_TO_INSERT_RECORD_8246 https://fairsharing.org/FAIRsharing.c55d5e)  as part of the [open-cypher](https://github.com (URL_TO_INSERT_RECORD_8247 https://fairsharing.org/FAIRsharing.c55d5e) /opencypher) project (URL_TO_INSERT_TERM_8245 https://fairsharing.org/search?recordType=project) 
 
 
A [large body of documentation and training material is available](https://neo4j.com/developer/cypher/), 
supporting developers in getting up to speed with the language.
 
More recently, Neo4j also joined the [graphQL foundation](https://graphql.org/foundation/), 
*"a neutral, non-profit home for the GraphQL assets and ongoing collaboration, and hosted by The Linux Foundation"* to
quote the landing page of the organization.

>**Why this matters?**
> 
> It matters because [GraphQL specification](https://graphql.org/) allows building robust Application Programming 
> Interface and make it easier to build full stack applications from scratch while offering great flexibility in 
> interfacing with the data. 
> But the main idea here is that the `GraphQL` way of representing data is a natural fit to database (URL_TO_INSERT_TERM_8248 https://fairsharing.org/search?fairsharingRegistry=Database)  systems
> which are natively `graph database (URL_TO_INSERT_TERM_8249 https://fairsharing.org/search?fairsharingRegistry=Database) s`, such as Neo4j.
> 

### 3. RDF graphs or Labeled Property graphs, which has the upper hand?

Sometimes, nothing beats a diagram to drive forward the strengths and the weaknesses of technical stacks.
In the diagram presented in figure 4, which provides an overview of the specifications and standard (URL_TO_INSERT_TERM_8250 https://fairsharing.org/search?fairsharingRegistry=Standard) s available to support the
knowledge graph, two things strike the keen reader:

1. RDF (URL_TO_INSERT_RECORD_8252 https://fairsharing.org/FAIRsharing.p77ph9)  graphs technology is backed by a large number of W3C standard (URL_TO_INSERT_TERM_8251 https://fairsharing.org/search?fairsharingRegistry=Standard) s for the **semantic web**.
    >- W3C RDF (URL_TO_INSERT_RECORD_8253 https://fairsharing.org/FAIRsharing.p77ph9) 
    >- WC3 RDF (URL_TO_INSERT_RECORD_8255 https://fairsharing.org/FAIRsharing.p77ph9) S (URL_TO_INSERT_RECORD_8254 https://fairsharing.org/FAIRsharing.v9n3gk) 
    >- W3C OWL (URL_TO_INSERT_RECORD_8256 https://fairsharing.org/FAIRsharing.atygwy) 
    >- W3C SHAC (URL_TO_INSERT_RECORD_8259 https://fairsharing.org/FAIRsharing.md3e78) L (URL_TO_INSERT_RECORD_8257 https://fairsharing.org/FAIRsharing.j9y503)  (URL_TO_INSERT_RECORD_8258 https://fairsharing.org/FAIRsharing.f1449d) 
    >- W3C SP (URL_TO_INSERT_RECORD_8261 https://fairsharing.org/FAIRsharing.s63y3p) ARQL (URL_TO_INSERT_RECORD_8260 https://fairsharing.org/FAIRsharing.87ccfd)  1.1

2. Content Validation
    >- RDF (URL_TO_INSERT_RECORD_8262 https://fairsharing.org/FAIRsharing.p77ph9)  graphs content can be validated (i.e. checked) with 2 equally functional `constraint` languages,
    SHEX and SHAC (URL_TO_INSERT_RECORD_8265 https://fairsharing.org/FAIRsharing.md3e78) L (URL_TO_INSERT_RECORD_8263 https://fairsharing.org/FAIRsharing.j9y503)  (URL_TO_INSERT_RECORD_8264 https://fairsharing.org/FAIRsharing.f1449d) . 
    Using these languages, the "shape" of the RDF (URL_TO_INSERT_RECORD_8266 https://fairsharing.org/FAIRsharing.p77ph9)  graph can be controlled.
    >- With property graphs, until the introduction of an adapter in the Neo4j library, this task proved hard to achieve.
    This becomes a drawback as it means a property graph database (URL_TO_INSERT_TERM_8267 https://fairsharing.org/search?fairsharingRegistry=Database)  may become `contaminated` with incorrect data.

Besides this point, two additional features can give RDF (URL_TO_INSERT_RECORD_8268 https://fairsharing.org/FAIRsharing.p77ph9)  graphs the edge (no pun intended!) over labeled property graphs
(even if it also depends on the use cases and ultimate goal):

3. IRI support and Linked data
    >- the RDF (URL_TO_INSERT_RECORD_8269 https://fairsharing.org/FAIRsharing.p77ph9)  specification by construction allows the use of IRI to uniquely identify nodes
    and have globally unique resolvable identifier (URL_TO_INSERT_TERM_8270 https://fairsharing.org/search?recordType=identifier_schema) s for resources.

4. Native semantics and the possibility of inference
    >- Backed by RDF (URL_TO_INSERT_RECORD_8273 https://fairsharing.org/FAIRsharing.p77ph9) S (URL_TO_INSERT_RECORD_8271 https://fairsharing.org/FAIRsharing.v9n3gk)  and OWL (URL_TO_INSERT_RECORD_8272 https://fairsharing.org/FAIRsharing.atygwy)  semantics, RDF (URL_TO_INSERT_RECORD_8274 https://fairsharing.org/FAIRsharing.p77ph9)  graphs are built on a technology stack developed (URL_TO_INSERT_RECORD_8275 https://fairsharing.org/FAIRsharing.31385c)  to deliver the
    `the semantic web` as envisioned by Sir Tim Berners-Lee. Tools known as *reasoners* , use first order logic to
    perform type and instance classification but also generate `entailments`, which correspond to new statements 
    resulting from inference made from the explicit assertions in the underlying ontologies (URL_TO_INSERT_TERM_8276 https://fairsharing.org/search?recordType=terminology_artefact)  or graph.
 
Worth of notice, comparisons between the two approaches do exist. For instance, Alocci and colleagues ran a comparison
of between RDF (URL_TO_INSERT_RECORD_8277 https://fairsharing.org/FAIRsharing.p77ph9)  triple stores and Property graph in the context of Glycan substructure and their assessment can serve as
basis for deciding to go for on or the other {footcite}`pmid26656740`.


### 4. Towards a unified standard for querying LPG: GQL specifications

What now? 
In the previous 2 sections, we have highlighted 2 of the most successful project (URL_TO_INSERT_TERM_8278 https://fairsharing.org/search?recordType=project) s leveraging the power of 
Property Graphs as data structure for storing informat (URL_TO_INSERT_TERM_8279 https://fairsharing.org/search?recordType=model_and_format) ion and building knowledge graphs. 
However, none of these implementations are officially an approved W3C standard (URL_TO_INSERT_TERM_8280 https://fairsharing.org/search?fairsharingRegistry=Standard) s. While it does not really matter
at this stage, it was realized that such fragmentation was hurting and in 2019, the `open Graph Query Language` (oGQL) 
working group released an initial specification.



## Conclusion

Knowledge graphs are a powerful and flexible way to represent informat (URL_TO_INSERT_TERM_8281 https://fairsharing.org/search?recordType=model_and_format) ion. 
Their properties and features lend themselves to data driven approaches and make them a data structure of choice for 
certain types of artificial intelligence and machine learning applications. 
As with all technical solutions, it is no panacea, no silver bullet.
They however are a technology which can greatly enhance certain tasks and are of particular relevance for representing
metadata, data about the data  in a FAIR (URL_TO_INSERT_RECORD_8282 https://fairsharing.org/FAIRsharing.WWI10U)  way.


### What to read next:

> Having read about what knowledge graphs are and their typology, the next key thing is to learn about how are knowledge graphs generated.
> This is when we need to introduce the notion of semantic model (URL_TO_INSERT_TERM_8283 https://fairsharing.org/search?recordType=model_and_format) s and ontologies (URL_TO_INSERT_TERM_8284 https://fairsharing.org/search?recordType=terminology_artefact)  and when knowledge engineers step in.
>
> The main concerns are to 1) provide foundational domain model (URL_TO_INSERT_TERM_8285 https://fairsharing.org/search?recordType=model_and_format) s as well as 2) instantiations of data under these model (URL_TO_INSERT_TERM_8286 https://fairsharing.org/search?recordType=model_and_format) s. 
> To take a simple example, let's consider converting natural text into a data structure which can be easily manipulated by software agents.
>
> ```bash
> `P53 gene transcript` `binds to` `DNA`.
> ```
> In order to do this, several steps are necessary and some requires specific resources to be available. 
> One step is known as 'Name Entity Recognition' (NER), which as the name says aims to cast string (URL_TO_INSERT_RECORD_8287 https://fairsharing.org/FAIRsharing.9b7wvk) s into specific bins such 'noun', 'verb', 'qualifier', etc.
> Another step, following the NER step would be the anchoring of these entities to a semantic framework and this step is known as 'semantic mark-up' or sometimes 'map (URL_TO_INSERT_RECORD_8289 https://fairsharing.org/FAIRsharing.53edcc) ping to ontologies (URL_TO_INSERT_TERM_8288 https://fairsharing.org/search?recordType=terminology_artefact) '.
>
> Ontologies (URL_TO_INSERT_TERM_8290 https://fairsharing.org/search?recordType=terminology_artefact)  are the resources which provide this layer of semantics which make it possible to integrate data in
> knowledge graphs. Ontologies (URL_TO_INSERT_TERM_8291 https://fairsharing.org/search?recordType=terminology_artefact)  are **formal resources developed (URL_TO_INSERT_RECORD_8292 https://fairsharing.org/FAIRsharing.31385c)  by experts in a domain**.
> Ontologies (URL_TO_INSERT_TERM_8293 https://fairsharing.org/search?recordType=terminology_artefact)  also rely on RDF (URL_TO_INSERT_RECORD_8294 https://fairsharing.org/FAIRsharing.p77ph9)  language for their representation but their purpose is different.
> 
> These ontologies (URL_TO_INSERT_TERM_8295 https://fairsharing.org/search?recordType=terminology_artefact)  set the rules and constraints grounded in first order logic to define a type.
> 
> The representation is neat and tidy but one can not help noticing that all the string (URL_TO_INSERT_RECORD_8296 https://fairsharing.org/FAIRsharing.9b7wvk) s are stored as free text.
> A problem arises when trying to accumulate knowledge from different sources.
> One needs to add a layer of semantics to `type` each of the element of an RDF (URL_TO_INSERT_RECORD_8297 https://fairsharing.org/FAIRsharing.p77ph9)  statement.
> 
>```bash
>@prefix go: <go:>
>@prefix uniprot: <uniprot:>
>@prefix chebi: <chebi:>
> P53 gene transcript a RDF (URL_TO_INSERT_RECORD_8298 https://fairsharing.org/FAIRsharing.p77ph9) :type go:Transcript;
> DNA a RDF (URL_TO_INSERT_RECORD_8299 https://fairsharing.org/FAIRsharing.p77ph9) :type chebi:molecularEntity
> binds_to
>```
>
>This taster is really meant to encourage our readers to dive into the following contents, which range from how to build controlled terminology (URL_TO_INSERT_TERM_8300 https://fairsharing.org/search?recordType=terminology_artefact) , 
>how to select ontologies (URL_TO_INSERT_TERM_8301 https://fairsharing.org/search?recordType=terminology_artefact)  or how to perform NER.
> Check out those content and  recipes!
>
>- Constructing knowledge graphs and their biomedical applications {footcite}`pmid32637040`, a review by Nicholson & Greene
>- {ref}`fcb-introduction-terminologies (URL_TO_INSERT_TERM_8302 https://fairsharing.org/search?recordType=terminology_artefact) -ontologies (URL_TO_INSERT_TERM_8303 https://fairsharing.org/search?recordType=terminology_artefact) `
<!-- >- {ref}`fcb-skos-terminology`
>- {ref}`fcb-ner`
>- {ref}`fcb-ontologies`
-->
>- {ref}`fcb-interop-covid-metadata`
>- {ref}`fcb-interop-etl`


````{rdmkit_panel}
````

## References

````{dropdown} **References** 
```{footbibliography}
```

````

<!--

[1]. https://www.turing.ac.uk/research/interest-groups/knowledge-graphs

[2]. https://web.stanford.edu/class/cs520/

[3]. http://ai.stanford.edu/blog/introduction-to-knowledge-graphs/

[4].https://www.ontotext.com/knowledgehub/fundamentals/what-is-a-knowledge-graph/

[5]. https://www.futurelearn.com/courses/linked-data

[6]. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7327409/ (Constructing knowledge graphs and their biomedical applications)

[7]. https://douroucouli.wordpress.com/2019/03/14/biological-knowledge-graph-modeling-design-patterns/

[8]. wikidata

[9]. monarch knowledge graph

[10]. NCATS biomedical data translator

[11]. Google graph

[12].https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-020-00940-y

-->

 
## Authors
````{authors_fairplus}
Philippe: Writing - Original Draft, Editing, Conceptualization
Dominique: Writing - Review & Editing
Susanna: Writing - Review & Editing
Fuqi: Review & Editing
Yojana: Review & Editing
````


## License
````{license_fairplus}
CC-BY-4.0
````

