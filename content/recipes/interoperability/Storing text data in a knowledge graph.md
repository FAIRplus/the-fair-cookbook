(fcb-interop-text2graph)=

# Creating knowledge graphs from unstructured text using NLP, NER and language models


<br/>
<br/>

````{panels_fairplus}
:identifier_text: FCB081

:identifier_link: 'https://w3id.org/faircookbook/FCB081'

:difficulty_level: 4

:recipe_type: hands_on
:reading_time_minutes: 45

:intended_audience: principal_investigator, data_manager, data_scientist 
:maturity_level: 0
:maturity_indicator: 0
:has_executable_code: yeah
:recipe_name:  Creating knowledge graphs from unstructured text using NLP, NER and language models

```` 


## Introduction

If you ever had to do a literature search for a project, you probably can appreciate the great effort behind traversing the ever-expanding volumes of texts and trying to organise the extracted information.
In the past two decades, noticeable progress has been made, harnessing the power of machine-learning (ML) and artificial intelligence (AI) approaches  to extract knowledge from large corpora of scientific literature.
Modern machine-learning approaches aim to identify, extract and store important information from unstructured text. 
Among the most popular structured representations, knowledge graphs, in the form of RDF linked data graphs are fast becoming a dominant form. This is chiefly due to it being a favourite form of  `active metadata` and `FAIR data`.


The pipeline for information extraction could be broken down in the following key steps:


- Collecting the text data and assembling the data corpus
- Performing entity disambiguation using a technique such as coreference resolution
- Performing Entity Recognition and named entity linking (NER step)
- Relationship extraction
- Creation and Storage of the data in a knowledge graph, RDF linked data graph in our example


## Collecting the text data

First, one collects the text to extract the data from. Text may come from the internal documents, articles, online content (web scraping), patents or even be a result of picture descriptions produced by image-to-text algorithms.


In our example, we created a dataset of articles' abstracts on the topic "cardiac amyloidosis". In the biological domain, articles can be collected from the [PubMed database](https://pubmed.ncbi.nlm.nih.gov/) using [biopython](https://biopython.org/wiki/Download). 
For the sake of simplicity, we retained only the first 20 articles that come up in the search.


```python
#importing libraries
from Bio import Entrez

def search(query, max_papers=20):
    """
    Get IDs of papers on the given topic from the pubmed database.
    """
    handle = Entrez.esearch(db='pubmed',
                            sort='relevance',
                            retmax=max_papers,
                            retmode='xml',
                            term=query)
    results = Entrez.read(handle)
    return results
    
def fetch_details(id_list):
    """
    Get details on each paper (including the abstract).
    """
    ids = ','.join(id_list)
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    return results
    
results = search('cardiac amyloidosis')
id_list = results['IdList']
papers = fetch_details(id_list)
```

## Entity disambiguation using coreference resolution


The text corpus prepared in the earlier step is now processed to replaces all ambiguous words in a sentence so that the text does not need any extra context to be understood. 
Although there are a number of approaches to perform this task, one of the most recently developed is a method known as [crosslingual coreference](https://spacy.io/universe/project/crosslingualcoreference) from the [spaCy python library](https://spacy.io/). spaCy is  a python library providing a comprehensive yet accessible way to create pipelines for natural language processing.  
In a nutshell, applying this procedure will, for example, replace personal pronouns with a referred person name.



```python
import spacy
import crosslingual_coreference

DEVICE = -1 # Number of the GPU, -1 if want to use CPU

# Add coreference resolution model
coref = spacy.load('en_core_web_sm', disable=['ner', 'tagger', 'parser', 'attribute_ruler', 'lemmatizer'])
coref.add_pipe(
    "xx_coref", config={"chunk_size": 2500, "chunk_overlap": 2, "device": DEVICE})
```

## Entity recognition and named entity linking

The next step is known as Named Entity Recognition (NER).
Here, we want to detect and extract all important entities from the sentences. 
Depending on the use case, one may have to specifically train a model to recognise entities of a specific type. For example, in [this tutorial](https://towardsdatascience.com/clinical-named-entity-recognition-using-spacy-5ae9c002e86f), one can find a way to train a model to recognise some entities from a biomedical domain. However, the spaCy library also provides a number of pre-trained models and we will be using those in our example.


Then, one needs to standardise the entities and map them to an existing ontology. The process is known as `Entity Linking` (EL). 
With this step, we map entities from the text to corresponding unique resolvable identifiers from a target knowledge base, for example, Wikipedia or semantic resource (e.g. an ontology such as [disease ontology](DOID).
One may also use some databases, relevant to the specific topic of the texts. 
While mapping to Wikipedia terms is demonstrated in [this tutorial](https://towardsdatascience.com/extract-knowledge-from-text-end-to-end-information-extraction-pipeline-with-spacy-and-neo4j-502b2b1e0754), we will  map our entities to the [NCI Thesaurus](https://bioportal.bioontology.org/ontologies/NCIT).
For simplicity, we will by default choose the first match as a mapping.

```{warning}
Note, that in principle that is not always the best choice and one may wish to use different similarity metrics to identify the best matching term in the ontology. 

## Relationship Extraction

Following the step of entity linking, in order to be able to generate  canonical triples, aka RDF predicates (object, relation, subject) for a knowledge graph, we now need to extract the relationships between the identified entities.

To do so, we will use the [Rebel project](https://github.com/Babelscape/rebel), which is also available as a spaCy component, allows extracting both entities and relations in one step, which we can use in our pipeline. 

To implement our approach of linking the entities to NCIT, we can rewrite the `set_annotations function` from the Rebel code as specified [here](https://towardsdatascience.com/extract-knowledge-from-text-end-to-end-information-extraction-pipeline-with-spacy-and-neo4j-502b2b1e0754) and turn `call_wiki_api function` into `call_ncit function`.


```python
import pandas as pd
import requests

def call_ncit_api(item):
  """
  Get the first mapping term from the NCIT
  """
  try:
    url = f"https://www.ebi.ac.uk/ols/api/search?q={item}&ontology=ncit"
    data = pd.DataFrame(requests.get(url).json().get('response').get('docs'))
    # Return the first id (A simplistic non-perfect way for mapping)
    return data["label"][0]
  except:
    return 'id-less'
```
After redifining the Rebel spaCy component, we include it into our pipeline:

```python
rel_ext = spacy.load('en_core_web_sm', disable=['ner', 'lemmatizer', 'attribute_rules', 'tagger'])
rel_ext.add_pipe("rebel", config={
    'device':DEVICE, # Number of the GPU, -1 if want to use CPU
    'model_name':'Babelscape/rebel-large'} # Model used
    )
```

Now we can text the pipeline on two simple sentances:
```python
input_text = "High fever is very dangerous. It can be treated with paracetamol."

#coreference model
coref_text = coref(input_text)._.resolved_text
print(coref_text)
#output: High fever is very dangerous. High fever can be treated with paracetamol.

#entity and relations extraction
doc = rel_ext(coref_text)

for value, rel_dict in doc._.rel.items():
    print(f"{value}: {rel_dict}")

#output:
#0440ea848947d2677bc11443f99f20f67ce0a1bc: {'relation': 'subclass of', 'head_span': {'text': 'High fever', 'id': 'High Grade Fever'}, 'tail_span': {'text': 'dangerous', 'id': 'DRRI-2 - A: Dangerous Military Duties'}}
#8aa25d264897bd007d389890b2239c2b9c07fa0b: {'relation': 'drug used for treatment', 'head_span': {'text': 'High fever', 'id': 'High Grade Fever'}, 'tail_span': {'text': 'paracetamol', 'id': 'Acetaminophen Measurement'}}
#d91bef9bfc94439523675b5d6a62e1f4635c0cdd: {'relation': 'medical condition treated', 'head_span': {'text': 'paracetamol', 'id': 'Acetaminophen Measurement'}, 'tail_span': {'text': 'High fever', 'id': 'High Grade Fever'}}
```
Following the coreference step (for disambiguation),  the "it" pronoun in the second sentence is replaced by the unambiguous "High fever" entity. 
After that step, the Rebel model extracted the  subject, relation, object triples and mapped them to the NCIT model. 

```{warning}
Note that the mapping here is far from perfect.
For example, the entity 'dangerous' was mapped to the 'DRRI-2 - A: Dangerous Military Duties' in NCIT. 
This is a consequence of our unrefined mapping procedure in which, for simplicity, we have chosen the first result for the term in the NCIT database. 
To improve over this simplistic approach, one would need to develop a more advanced mapping heuristic, but this is out of the scope of this recipe. Having said that, a key learning point is that a 'man in the loop' approach is probably still needed to review the mapping resulting from automated approaches.
```

## Storing the results

The final subject, predicate, object triples can either be stored as a labeled property graph or as an RDF graph.

Here, we will give an approach to store the results as an RDF graph by using [rdflib]() library in python.

rdflib allows the creation of entities with known URIs with the URIRef command.
Also, one can create a custom namespace with new entities and relations. 

```{note}
For our audience interesting in labeled property graphs, the guidelines to store the results as a neo4j labeled property graph are available from  [this tutorial](https://towardsdatascience.com/extract-knowledge-from-text-end-to-end-information-extraction-pipeline-with-spacy-and-neo4j-502b2b1e0754).
```


```python
from rdflib import Graph
from rdflib import URIRef, BNode, Literal, Namespace
import json

def Capitalise_underscore(relation):
  """
  Write the relations in Capitalized_And_Underscored_form
  """
  return relation.capitalize().replace(' ','_')

def ncit_iri(item):
  """
  Get an iri of the first matching term from NCIT
  """
  try:
    url = f"https://www.ebi.ac.uk/ols/api/search?q={item}&ontology=ncit"
    data = pd.DataFrame(requests.get(url).json().get('response').get('docs'))
    # Return the first id
    return data["iri"][0]
  except:
    return 'id-less'

#create the graph
g=Graph()
EX = Namespace('http://example.org./')

#dataframe storing the trios for visual clarity
relations = pd.DataFrame()

for i, paper in enumerate(papers['PubmedArticle']):
    print("{}) {}".format(i+1, paper['MedlineCitation']['Article']['ArticleTitle']))
    #get abstract
    abstract_text_json = json.dumps(papers['PubmedArticle'][i]['MedlineCitation']['Article']['Abstract']['AbstractText'])
    abstract_text = ' '.join(json.loads(abstract_text_json))
    
    #take through coreference model
    coref_text = coref(abstract_text)._.resolved_text
    
    #entity extraction and linking
    doc = rel_ext(coref_text)
    
    #adding trios to the graph
    for value, rel_dict in doc._.rel.items():
      subject_iri = ncit_iri(rel_dict['head_span']['text'])
      object_iri = ncit_iri(rel_dict['head_span']['text'])
      if subject_iri != 'id=less':
        subj = URIRef(subject_iri)
      else:
        subj = EX[rel_dict['head_span']['text']]
      if object_iri != 'id=less':
        obj = URIRef(object_iri)
      else:
        subj = EX[rel_dict['head_span']['text']]  
      pred = EX[Capitalise_underscore(rel_dict['relation'])]
      g.add((subj, pred, obj))        
    df = pd.DataFrame.from_dict(doc._.rel).transpose()
    df['subject_text'] = df.head_span.apply(lambda x: x['text'])
    df['subject_id'] = df.head_span.apply(lambda x: x['id'])
    df['object_text'] = df.tail_span.apply(lambda x: x['text'])
    df['object_id'] = df.tail_span.apply(lambda x: x['id'])

    df = df.drop(["head_span", "tail_span"], axis = 1)

    relations = pd.concat([relations, df])
```

Finally, we can visualize the resulting graph and export it in .ttl format.

```python
g.serialize(format = 'ttl')
```

```python
import networkx as ntx
import matplotlib.pyplot as plot

graph = ntx.from_pandas_edgelist(relations, "subject_text", "object_text", edge_attr=True, create_using=ntx.MultiDiGraph())

plot.figure(figsize=(10, 10))
posn = ntx.spring_layout(graph)
ntx.draw(graph, with_labels=True, node_color='green', edge_cmap=plot.cm.Blues, pos = posn)
plot.show()
```

````{dropdown} 
:open:
```{figure} storing-text-data-in-KG-final-graph.png
---
height: 1000px
name: Final knowledge graph visualiyation. The relations names are omitted.
alt: Final knowledge graph visualiyation. The relations names are omitted.
---
Storing text data in the knowledge graph.
```
````

## Conclusion
Modern AI approaches allow us to traverse big chunks of unstructured text, extract information and order it in a form of a knowledge graph, making it FAIR. The details of the pipeline would vary depending on the specific use case, but the final result would definitely make your life easier!

> ###  What to read next?
>
> - {ref}`fcb-interop-covid-metadata`
> 
> ````{panels}
> :column: col-4
> :card: border-2
> :header: bg-primary pa_dark
> :body: grey
> ```{image} ../../../images/logos/RDMkit_logo.svg
> :height: 40px
> :name: rdmkit_logo
> ```
> ^^^
> [More about `Metadata Management` from the `RDMkit`](https://rdmkit.elixir-europe.org/metadata_management.html)
> ````


## Authors

````{authors_fairplus}
Liubov: Writing - Original Draft
````


## License

````{license_fairplus}
CC-BY-4.0
````


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
