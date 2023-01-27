(fcb-interop-text2graph)=

# Creating knowledge graphs from unstructured text


<br/>
<br/>

````{panels_fairplus}

```` 


## Main Objectives

If you ever had to do a literature search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) for a project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project), you probably can appreciate the great effort behind traversing 
the ever-expanding volumes of texts and trying to organise the extracted informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion.
In the past two decades, noticeable progress has been made, harnessing the power of machine-learning (ML) and 
artificial intelligence (AI) based approaches to extract knowledge from large corpora of scientific literature.
Modern ML algorithms aim to identify, extract, and store important informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion from unstructured text. 
Among the most popular structured representations, knowledge graphs, in the form of RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) linked data graphs are rapidly
becoming a dominant form. This is chiefly due to it being a favourite form of  `active metadata` and `FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) data`.

In simplified terms, the overall pipeline for informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion extraction can be broken down in the following key steps:

- Collecting the text data and assembling the data corpus
- Performing entity disambiguation using a technique such as co-reference resolution
- Performing entity recognition and named entity linking (NER step)
- Performing relationship detection and extraction
- Creating and storing the data in a knowledge graph (an RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) linked data graph in our example).


## Graphical Overview

This recipe will cover the highlighted topics

````{dropdown} 
```{figure} nlp-ner-2-kg-figure.svg
---
width: 450px
name: nlp-ner-2-kg-figure
alt: Overview of NLP/NER to KG process
---
Overview of natural language processing to knowledge graph creation workflow
```
````

---

```{tabbed} Requirements




```
```{tabbed} FAIRification Objectives, Inputs and Outputs

```



## Tools

The table below lists the software that is used to execute the examples in this recipe.

| Software                                            | Description|
| --------------------------------------------------- | --------------------------|
| [biopython](https://biopython.org/wiki/Download)| The biopython project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project) is an open-source collection (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=collection) of non-commercial Python tools for computational biology and bioinformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ics, created by an international association of developers|
| [spacy](https://spacy.io/) | Spacy is a beginner level industry strength natural language processing library|
| [crosslingual coreference](https://spacy.io/universe/project/crosslingualcoreference)  | A multi-lingual approach to AllenNLP CoRe(URL_TO_INSERT_RECORD https://core.ac.uk)ference Resolution along with a wrapper for spaCy|
| [rebel](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/Babelscape/rebel) | REBEL(URL_TO_INSERT_RECORD https://bel.bio) is a seq2seq model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) that simplifies Relation Extraction  |
| [rdflib](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/RDFLib)| RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/)Lib is a Python library for working with RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/), a framework for representing informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion|
| [networkx python library](https://networkx.org/)| NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks. |
| [matplotlib library](https://matplotlib.org/)| Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.|



## Generation of textual corpora

First, one collects the text to extract the data from. Text may come from the internal documents, articles, online content (web scraping), 
patents, or even be a result of picture descriptions produced by image-to-text algorithms.


In our example, we created a dataset of articles' abstracts (corpora) on the topic "cardiac amyloidosis". In the biological domain,
articles can be collected from the [PubMed(URL_TO_INSERT_RECORD http://www.ncbi.nlm.nih.gov/pubmed/)(URL_TO_INSERT_RECORD http://www.ncbi.nlm.nih.gov/pubmed/) database](https://pubmed.ncbi.nlm.nih.gov/) using [biopython](https://biopython.org/wiki/Download). 
For the sake of simplicity, we retained only the first 5 articles that come up in the search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/).


```python
#importing libraries

```

## Entity disambiguation using co-reference resolution

The text corpus prepared in the previous step is now processed to replace all ambiguous words found in a sentence so 
that the text does not need any extra context to be understood. 
Although a number of approaches to perform this task exists, one of the most recently developed(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) is a method known as 
[crosslingual coreference](https://spacy.io/universe/project/crosslingualcoreference) from the
[spaCy python library](https://spacy.io/) {footcite}`crosslingualcore(URL_TO_INSERT_RECORD http://purl.uniprot.org/core/)(URL_TO_INSERT_RECORD https://core.ac.uk)ference`. 
spaCy is a python library providing a comprehensive yet accessible way to 
create pipelines for natural language processing.  
In a nutshell, applying this procedure will, for example, replace personal pronouns with a referred person's name.



```python


# Add coreference resolution model
```

## Entity recognition and named entity linking

The next step is known as Named Entity Recognition (NER).
Here, we want to detect and extract all domain relevant entities from the sentences. 
Depending on the use case, one may have to specifically train a model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) to recognise entities of a specific type. 
For example, in [this tutorial](https://towardsdatascience.com/clinical-named-entity-recognition-using-spacy-5ae9c002e86f),
one can find a way to train a model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) to recognise some entities from a biomedical domain. 
However, the spaCy library also provides a number of pre-trained model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s and, we will be using those in our example.

Following the entity recognition, one needs to standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)ise the entities and map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map) them to an existing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) controlled terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)/ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact). 
The process is known as `Entity Linking` (EL). 
With this step, entities recognized from the text are map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ped(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) to one or more corresponding unique resolvable identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s 
from a target knowledge base, for example, Wikiped(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped)ia or semantic resource (e.g. an ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) such as 
[disease ontology(URL_TO_INSERT_RECORD http://www.disease-ontology.org)](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/DiseaseOntology)) {footcite}`pmid34755882`.
One may also use resolvable identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s minted by database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)s and relevant to the specific topic of the texts. 

In this example, we will map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map) our entities to the [NCI Thesaurus(URL_TO_INSERT_RECORD https://ncit.nci.nih.gov)](https://bioportal.bioontology.org(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/)/ontologies/NCIT) and 
for simplicity, we will by default choose the first match as a map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping.

```{warning}
```

```{note}
```

## Relationship Extraction

Following the step of entity linking, we now need to extract the relationships between the identified
entities. This is necessary to be able to generate canonical RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) triples, also known as RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) subject predicate object 
statements, and build a knowledge graph, 
To perform the relation identification, we will use the python [Rebel project](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/Babelscape/rebel), which is
also available as a spaCy component, and allows extracting both entities and relations in one step {footcite}`huguet-cabot-navigli-2021-rebel-relation`. 
We will now use it in our pipeline. 

To implement our approach of linking the entities to NCIT, we can rewrite the `set_annotations function` from the Rebel
code as specified [here](https://towardsdatascience.com/extract-knowledge-from-text-end-to-end-information-extraction-pipeline-with-spacy-and-neo4j-502b2b1e0754)
and alter the `call_wiki_api function` into `call_ncit function`.

```python

```

After redefining the `Rebel` spaCy component, we include it into our pipeline:

```python
```

Now, we can test the pipeline on two simple sentences:
```python

#coreference model
#output: 'High fever is very dangerous. High fever can be treated with paracetamol.'

#entity and relations extraction


#output:
#0440ea848947d2677bc11443f99f20f67ce0a1bc: {'relation': 'subclass of', 'head_span': {'text': 'High fever', 'id': 'High Grade Fever'}, 'tail_span': {'text': 'dangerous', 'id': 'DRRI-2 - A: Dangerous Military Duties'}}
#8aa25d264897bd007d389890b2239c2b9c07fa0b: {'relation': 'drug used for treatment', 'head_span': {'text': 'High fever', 'id': 'High Grade Fever'}, 'tail_span': {'text': 'paracetamol', 'id': 'Acetaminophen Measurement'}}
#d91bef9bfc94439523675b5d6a62e1f4635c0cdd: {'relation': 'medical condition treated', 'head_span': {'text': 'paracetamol', 'id': 'Acetaminophen Measurement'}, 'tail_span': {'text': 'High fever', 'id': 'High Grade Fever'}}
```
Following the disambiguation step (using co-reference),  the "it" pronoun in the second sentence is replaced by the 
unambiguous "High fever" entity. 
After that step, the `Rebel` model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) extracted the subject, relation, object triples and map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ped(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) them to the NCIT model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format). 

```{warning}
```

## Storing the results

The final subject, predicate, object triples can either be stored as a `labeled property graph` or as an `RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) graph`.

Here, we will outline an approach to store the results as an RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) graph by using the python [rdflib](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/RDFLib) library.

rdflib allows the creation of entities with known URI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)s with the URI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986)Ref command.

Also, one can create a custom namespace with new entities and relations. 

```{note}
```


```python



#create the graph

#dataframe storing the trios for visual clarity



```

Finally, we can export the resulting graph in turtle (.ttl) format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ...
library.

```python
```

...and visualise it using the well known [networkx python library](https://networkx.org/) and [matplotlib library](https://matplotlib.org/).


```python



#for id-less set the identified entity as the id

#bring all entities to upper case


#select colors for edges
#map relations to colors
#create the list of edge colors

## PLOT


##add graph elements

# generate proxies
#create legend labels

```

````{dropdown} 
```{figure} storing-text-data-in-KG-final-graph.png
---
height: 800px
name: Final knowledge graph visualisation. The relations names are omitted.
alt: Final knowledge graph visualisation. The relations names are omitted.
---
Viewing the knowledge graph with networks and matplotlib
```
````

## Conclusion

Modern AI/ML algorithms allow processing large corpus of unstructured text and extract informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion to structure it. 
For instance, informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion can be organised in a form of knowledge graphs, e.g. RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) linked open data (LOD) graphs.
The present document provides a typical text processing pipeline to achieve this task, even if in a simplified form.
In more realistic cases, large text corpora will require more advanced techniques to be deployed, from model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) training to
the development of specific algorithms, and the inclusion of expert curators to assist in the creation of the final knowledge graphs.
Still, we hope this will provide our readership with a basic understanding of the techniques available to move from 
unstructured text to generating knowledge graphs.

```{warning}

```

> ###  What to read next?
> - [Introduction to Named Entity Recognition by Dr. W.J.B. Mattingly](https://ner.pythonhumanities.com/01_02_introduction_to_spacy.html)
> - [spacy](https://spacy.io/)
> - {ref}`fcb-interop-covid-metadata`
> - [FCB006: Unique persistent identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s](https://w3id.org(URL_TO_INSERT_RECORD https://w3id.org/)/faircookbook/FCB006)
> - [FCB032: Licensing](https://w3id.org(URL_TO_INSERT_RECORD https://w3id.org/)/faircookbook/FCB032)
> - [How to deploy an RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) triple store](https://www.mkbergman.com/2409/cwpk-59-adding-a-sparql-endpoint-part-i/)
> - [How to query Wikidata(URL_TO_INSERT_RECORD http://wikidata.org/)(URL_TO_INSERT_RECORD http://wikidata.org/) with SP(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/SP)ARQL(URL_TO_INSERT_RECORD http://www.w3.org/TR/sparql11-overview/)](https://www.wikidata.org(URL_TO_INSERT_RECORD http://wikidata.org/)/wiki/Wikidata:SPARQL_tutorial)
> - [How to perform federated queries with SPARQL](https://graphdb.ontotext.com/documentation/10.0/sparql-federation.html) 

<!--
````{panels}
````
-->

## References

````{dropdown} **references**
```{footbibliography}
```
````

## Authors

````{authors_fairplus}
````


## License

````{license_fairplus}
````


   
