fcb-?????)=
# Storing text data in a knowledge graph

<br/>
<br/>

````{panels_fairplus}
:identifier_text: 
:identifier_link: 'https://w3id.org/faircookbook/??????'
:difficulty_level: 
:recipe_type: hands_on
:reading_time_minutes: 10
:intended_audience: principal_investigator, data_manager, data_scientist 
:maturity_level: 0
:maturity_indicator: 0
:has_executable_code: yeah
:recipe_name: Creating a metadata profile
```` 


## Introduction

If you ever had to do a literature search for a project, you probably could appreciate the great effort behind traversing the ever-expanding volumes of texts and trying to organize the extracted information. Throughout the last decades, some noticeable progress was made in using AI to automize the process. The modern machine learning approaches aim to identify, extract and store important information from unstructured texts. To make the extracted metadata active and FAIR, one often stores it in the form of a knowledge graph.

The pipeline for information extraction could be seen as a path of several steps:

- Collecting the text data
- Avoiding ambiguity of entities with coreference resolution
- Entity recognition and named entity linking
- Relationship extraction
- Storing the data in a knowledge graph

## Collecting the text data

First, one collects the text to extract the data from. Text may be the collection of internal documents, articles, online content, or the result of picture descriptions produced by image-to-text algorithms.

Here as an example, we will collect a dataset of articles' abstracts on the topic "cardiac amyloidosis". In the biological domain, articles can be collected from the PubMed database using biopython, for the sake of simplicity we will only go through the first 20 articles that come up in the search.

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

## Avoiding ambigiuity of entities with coreference resolution
The prepared text should go through the coreference resolution model. In a nutshell, this process should replace all ambiguous words in a sentence so that the text does not need any extra context to be understood. For example, personal pronounsare being replaced with a referred person’s name. Athough there is a number of approaches to do that, one of the most recently developed is crosslingual coreference [https://spacy.io/universe/project/crosslingualcoreference] from the spaCy universe. spaCy is a python library that provides an easy way to create pipelines for natural language processing. 

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
Nest step is named entity recognition. Here we want to extract all important entities from the sentences. Depending on a use case, one can train a model to recognize entities of a specific type. For example, in this tutorial [https://towardsdatascience.com/clinical-named-entity-recognition-using-spacy-5ae9c002e86f] you can find a way to train a model to recognize some entities from a biomedical domain. However, the spaCy universe also provides some pre-trained models to recognize entities, which we are going to use in our example.
Then one intends to standardize the entities and map them to an existing ontology. The process is known as entity linking. Here we map entities from the text to corresponding unique ids from a target knowledge base, for example, Wikipedia. One can also use some databases, relevant to the specific topic of the texts. While mapping to the Wikipedia terms is performed in this tutorial [https://towardsdatascience.com/extract-knowledge-from-text-end-to-end-information-extraction-pipeline-with-spacy-and-neo4j-502b2b1e0754], we will try to map our entities to the NCI Thesaurus [https://bioportal.bioontology.org/ontologies/NCIT], for simplicity choosing the first match as a mapping. Note, that in principle that is not always the best choice and one can use different similarity metrics to identify the best matching term in the ontology. 

## Relationship Extraction
After entity linking to get standard trios (object, relation, subject) for a knowledge graph, we extract the relationships between the identified entities. 
The Rebel project [https://github.com/Babelscape/rebel], which is also available as a spaCy component, allows extracting both entities and relations in one step, which we can use in our pipeline. 

To implement our approach of linking the entities to NCIT, we can rewrite the set_annotations function from rebel as specified here [https://towardsdatascience.com/extract-knowledge-from-text-end-to-end-information-extraction-pipeline-with-spacy-and-neo4j-502b2b1e0754] and turn call_wiki_api function into call_ncit function.

```python
import pandas as pd
import requests

def call_ncit_api(item):
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
One can observe, that on the coreference step the "it" pronoun in the second sentance was replaced by the unambiguous "High fever" entity. 
After that the rebel model has extracted the trios of subject, relation and object and mapped them to the NCIT model. One can note, that the mapping is far from perfect. For example, the entity 'dangerous' was mapped to the 'DRRI-2 - A: Dangerous Military Duties' in NCIT. this is because in our mapping procedure for simplisity we have chosen the first result for the term in the NCIT database. To improve this, one would need to develop a more complex mapping algorithm.

## Storing the results

The final subject, relation, and object trios can be stored as either a labeled property graph or as an RDF graph. The guidelines to store the results as a neo4j labeled property graph are given here [https://towardsdatascience.com/extract-knowledge-from-text-end-to-end-information-extraction-pipeline-with-spacy-and-neo4j-502b2b1e0754]. Here we will give an approach to store the results as an RDF graph by using rdflib library.

Rdflib allows the creation of entities with known URIs with the URIRef command. Also, one can create a custom namespace with new entities and relations. 

```python
from rdflib import Graph
from rdflib import URIRef, BNode, Literal, Namespace
import json

def Capitalise_underscore(relation):
  return relation.capitalize().replace(' ','_')

def ncit_iri(item):
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
Modern AI approaches allow to traverse big chunks of unstructured text, extract information and order it in a form of a knowledge graph, making it FAIR. The details of the pipeline would vary depending on the specific usecase, but the final result would definately make your life easier!

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
