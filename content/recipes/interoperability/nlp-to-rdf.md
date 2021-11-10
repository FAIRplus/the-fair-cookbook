(fcb-unstructuredtoKG)=
# From unstructured text to knowledge graph

````{panels_fairplus}
:identifier_text: FCB***
:identifier_link: 'https://w3id.org/faircookbook/FCB***'
:difficulty_level: 4
:recipe_type: inventory
:reading_time_minutes: 30
:intended_audience: data_producer, data_engineer
:has_executable_code: yeah
:recipe_name: From unstructured text to knowledge graph
```` 

## Main Objectives

The main purpose of this recipe is:

> to provide an overview of key steps required to set up a natural language processing pipeline to collect facts in a knowledge graph.
> to highlight a number of tools and resources of relevance in the field
> to help new comers to extracting knowledge from unstructured text.
> to show how these techniques can be applied in clinical context to extract knowledge from electronic health records

---


## Graphical Overview of the FAIRification Recipe Objectives

Figure {numref}`rdf-conversion-figure1` shows an example ETL workflow.


```{figure} nlp-pipline.md-figure1.mmd.png
---
name: nlp-pipline-figure1
alt: 
---
overview of an NLP/NLU pipeline.
```

---


## Requirements

  * basic understanding of: command line syntax, basic knowledge of python and knowledge graph representation as RDF graphs.
  * availability of a corpus of unstructured text. The corpus could be:
      - a subset of pubmed abstracts
      - a public collection such as the MIMIC-III datasets of electronic medical notes.
      - a synthetic dataset produced by a software.
      * We recommmend the readership to review the [following content from the FAIR cookbook](TODO:insert/link/here), which details a number of public datasets available for training and teaching

---

## Table of Data Standards

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| [RDF]()<!-- TODO needs a link -->    |   |   |

---

## Table of Tools

| Tool Name  | URI |   |
| :------------- | :------------- | :------------- |
| [MIMIC-III](https://www.nature.com/articles/sdata201635#citeas)|{footcite}`Johnson2016`| |
| [spacy](https://spacy.io/)<!-- TODO needs a link -->    |   |   |
| [AWS comprehend](https://aws.amazon.com/comprehend/medical/)<!-- TODO needs a link -->    |   |   |
| [BERT](TODO:link)| {footcite}'Mu.2021'    |   |   |
| [BioBERT](TODO:link)<!-- TODO needs a link -->    |   |   |
| [SciBERT](TODO:link)<!-- TODO needs a link -->    |   |   |
| [BioClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT)|{footcite}`https://arxiv.org/abs/1904.03323`|  |
---

## Introduction

Despite the progress in organizing scientific knowledge in specialized databases as evidenced by the ever expanding number of resources available from 
[FAIRsharing.org](https://www.fairsharing.org), unstructured text remains in many areas how domain knowledge is held in a field. 
`Unstructured text` refers simply to natural language text as found in journal articles, scientific reports or medical notes. The qualifier `unstructured` refers to the fact that the information is available simply as a sequence of words, without any markup or annotation.
While these documents are meaningful to humans, it presents two challenges. To the humans, reading and synthesizing the volumes of texts available is impossible. To computers and software agents, it was, until recently, extremely difficult to **extract meaning** from **unstructured text.**
However, in recent years, the fields of computational linguistics and machine learning have seen breakthroughs in 'natural language processing', which enable researchers and scientists to tap into the knowledge mines that constitutes unstructured text.  Tools such as `BERT`, short for Bidirectional Entity Recognition Transformers,  now known collectively as `Transformers` have transformed our ability to exploit unstructured text.
The tasks of Named Entity Recognition (NER) and Relation Recognition, critical to accomplishing 'natural language understanding' (NLU) can now be done with higher confidence and, as evidenced by the increasing number of publications, is delivering advances in biomedicine and healthcase which benefit to patients and science advancement.

Therefore, the purpose of this content is to introduce some of the solutions that exist and provide easy to follow examples as well as direct users to more advanced/specialized resources


## Step by step process

### Step 1: consider requirements

assemble a corpus of data.

### Step 2: select a NLP framework

for instance, spacy

### Step 3: select a model

While a lot of science is available in english, when dealing with electronic medical notes (EMN) or electronic health records (EHR), making sure that models are available in the relevant language is something to bear in mind.
For a framework such as as Spacy, `models` exist for 19 languages.  By `models`, we refer here to the availability of word embeddings identified following a training procedure on reference body of text of a given language.
One needs to understand that, owing to the nature of the training procedure and training datasets, the 'default models' may lack specificity and sensitivity to pick up entities belonging to a specialized domain.
This is why a number of specialized models have been devised to support NER tasks in specific domains.
Following on our example of the `Spacy` library, specific components can be added to augment the capabilities of the default tool. For instance, `[medSpacy](https://spacy.io/universe/category/biomedical)` can be used to support task such as detecting family history or asserting negation.

### Step 4: analysing the results

### Step 5: post processing and predicate formation

  marking up with ontology terms -> term lookup against domain vocabularies

### Step 6: creation of Linked Data Fragments & persistence




---

#### What should I read next?

> - [INTRODUCTION TO SPACY 3](http://spacy.pythonhumanities.com/intro.html)  
{footcite}`Mattingly`

> The Reference Index https://archive.org/details/GeneralIndex -
https://doi.org/10.1038/d41586-021-02895-8
https://doi.org/10.1038/d41586-019-02142-1


Mu, Y., Tizhoosh, H.R., Tayebi, R.M. et al. A BERT model generates diagnostically relevant semantic embeddings from pathology synopses with active learning. Commun Med 1, 11 (2021). https://doi.org/10.1038/s43856-021-00008-0


https://colab.research.google.com/drive/1wLzsaWWgPkoRgrUsL94Iv8_FiSiA7sKF?usp=sharing


EMB-NLP: https://github.com/bepnye/EBM-NLP

Sequence Tagging with Tensor Flow: https://guillaumegenthial.github.io/sequence-tagging-with-tensorflow.html

---
AWS related solutions:

Amazon Comprehend: https://aws.amazon.com/comprehend/medical/

Novartis AG uses Amazon SageMaker and Amazon Neptune to build and enrich a knowledge graph using BERT: https://aws.amazon.com/blogs/industries/novartis-ag-uses-amazon-to-build-knowledge-graph-using-bert/

Build a medical sentence matching application using BERT and Amazon SageMaker: https://aws.amazon.com/blogs/machine-learning/build-a-medical-sentence-matching-application-using-bert/
---

Publicly Available Clinical BERT Embeddings: https://arxiv.org/abs/1904.03323


NLP2FHIR: A FHIR-based Clinical Data Normalization Pipeline and Its Applications: https://github.com/BD2KOnFHIR/NLP2FHIR
Hong N, Wen A, Shen F, Sohn S, Liu S, Liu H, Jiang G. Integrating Structured and Unstructured EHR Data Using an FHIR-based Type System: A Case Study with Medication Data. AMIA Jt Summits Transl Sci Proc. 2018 May 18;2017:74-83. PubMED

Developing a FHIR-based EHR phenotyping framework: A case study for identification of patients with obesity and multiple comorbidities from discharge summaries, Hong et al, 2019. https://doi.org/10.1016/j.jbi.2019.103310


Clinical BERT application on Medium: https://medium.com/nwamaka-imasogie/clinicalbert-using-deep-learning-transformer-model-to-predict-hospital-readmission-c82ff0e4bb03

NER and Relation Extraction from EHR: https://github.com/smitkiri/ehr-relation-extraction

---
## References

```{footbibliography}
```

1. Mattingly, William. Introduction to spaCy 3, 2021 (1st ed.). spacy.pythonhumanities.com.


---

## Authors


````{authors_fairplus}
Philippe: Writing - Conceptualization, Original Draft
Yojana: Writing - Conceptualization, Original Draft
````

---


## License

````{license_fairplus}
CC-BY-4.0
````
