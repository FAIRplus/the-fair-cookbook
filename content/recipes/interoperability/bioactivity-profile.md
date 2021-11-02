## Bioactivity data profile

[TOC]



## Main Objective

To provide guidance on the minimum set of metadata and semantics required to describe any chemical biology experiments, and how to translate bioactivity data to CHEMBL standards. This recipe also applies to binding, functional and ADME or toxicological assay types.


## Graphical overview of the Recipe FAIRification Objectives

```mermaid
graph TD
    A[Primary data at one concentration]-->B{Number of readouts per molecules?}
    B-->|one|V{Which unit?}
    V-->|percentage|D
    V-->|value|F
    B-->|multi|C[valid ones]
    C-->|experiments|D{if triplicates}
    D-->|aggregating or filtering|E[validated ones]
    E--> |calculating|G[One average readout value <br> per concentration]
    G-->F[CC/AC/IC50/IC90 curves]
```

### BioActivity data

In the chemical biology domain (CBD), bioactivity data refers to datasets coming from high- to low-throughput biochemical and cellular screenings, hit confirmatory assay and profiling assays. Such datasets usually contain IC/AC/CC/EC50 (where 50 can be any number referring to the percent effect of the readout results). 

Public CBD datasets are released in archives such as [ChEMBL](https://www.ebi.ac.uk/chembl/), [PubChem](https://pubchem.ncbi.nlm.nih.gov/), and [ECBD](https://ecbd.eu/).  They include general project- and sample-level information (like assay summaries or protocols), which will be briefly covered in this recipe but will also be covered in more depth elsewhere.

A specific of this guideline is that they are referring mainly to ChEMBL formatting for uploading, so the covered suggested ontologies are intrinsically linked to “ChEMBL supported” ontologies ([https://www.ebi.ac.uk/ols/index](https://www.ebi.ac.uk/ols/index))


#### Bioactivity data formats and standards


<table>
  <tr>
   <td><strong>Data format</strong>
   </td>
   <td><strong>Terminology</strong>
   </td>
   <td><strong>Data models</strong>
   </td>
  </tr>
  <tr>
   <td>Chemistry (SDF)
   </td>
   <td>Structure ID
   </td>
   <td>
<ul>

<li>SDF

<li>SMILE

<li>InChI

<li>CID
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Target 
   </td>
   <td>Protein/GENE ID
   </td>
   <td>PN_ or SwissProt ID
   </td>
  </tr>
  <tr>
   <td>Assay
   </td>
   <td>Typology
   </td>
   <td>Binding, FRET, SPR, Inhibition, phenotypic cellular
   </td>
  </tr>
  <tr>
   <td>Result Type
   </td>
   <td>Potency/Tox 
   </td>
   <td>CC50/IC50/EC50/%
   </td>
  </tr>
  <tr>
   <td>Unit
   </td>
   <td>Result unit
   </td>
   <td>Concentration/ratio/SI
   </td>
  </tr>
  <tr>
   <td>Image
   </td>
   <td>
   </td>
   <td>
<ul>

<li>OMETIFF

<li>Matrix Format-Zarr
</li>
</ul>
   </td>
  </tr>
</table>



#### Minimum metadata 
![](https://i.imgur.com/aU2KYV1.png)


Minimum metadata set constitutes metadata items that always need to be supplied with any experimental data. For ChEMBL submission, molecular structures and assay description as depicted in the scheme above are suggested as essential metadata. This is basically a subset of the following [schema](https://www.ebi.ac.uk/chembl/db_schema). In case mutated cell lines and/or mutated target proteins have been used in the assay, desirable metadata should be added in the proper group.

The minimum dataset includes three parts: 

1. Assay and project references (mainly literature link and protocol or summary)
    1. Project level metadata
    2. Common sample level metadata such as species, tissue, cell type etc.
2. Compounds reference with structures
3. Assay results 


### Bioactivity data vocabularies

A set of well-established standards and minimum metadata checklists exist for various aspects of CheMBL formatting:



* **Chemical information ontology (CHEMINF)** [http://semanticchemistry.github.io/semanticchemistry/ontology/cheminf.owl](http://semanticchemistry.github.io/semanticchemistry/ontology/cheminf.owl) 

    CHEMINF covers information about chemical entities. It includes terms for the descriptors commonly used in cheminformatics software applications and the algorithms which generate them.

* **BioAssay Ontology**(BAO)

    [http://www.bioassayontology.org/bao/bao_complete.owl](http://www.bioassayontology.org/bao/bao_complete.owl) 


    The BioAssay Ontology (BAO) describes biological screening assays and their results including high-throughput screening (HTS) data for the purpose of categorizing assays and data analysis. BAO is an extensible, knowledge-based, highly expressive (currently SHOIQ(D)) description of biological assays making use of descriptive logic based features of the Web Ontology Language (OWL). 

* __Ontology of units of Measure (OM)__
 [http://www.ontology-of-units-of-measure.org/resource/om-2](http://www.ontology-of-units-of-measure.org/resource/om-2) 
 The OM ontology provides classes, instances, and properties that represent the different concepts used for defining and using measures and units. It includes, for instance, common units such as the SI units meter and kilogram, but also units from other systems of units such as the mile or nautical mile.


### Annotation with vocabularies

With the vocabularies above, it’s possible to annotate some metadata fields automatically. For example, the script below annotates “organism: Homo sapiens” with ZOOMA.


    ```python


    import requests
    zooma_root = "https://www.ebi.ac.uk/spot/zooma/v2/api/services/annotate?propertyValue="
    query_keyword = "Homo sapiens"
    vocab_filter = "&filter=ontology:["
    vocab_target = "ncbitaxon"
    query_api = zooma_root + query_keyword + vocab_filter + vocab_target + "]"
    request_details = requests.get(query_api)
    request_details.json()
    ```


### Exemplar Bioactivity datasets

[SARS CoV2 phenotypic assay from Caco2 cell line](https://www.ebi.ac.uk/chembl/assay_report_card/CHEMBL4303806/)

The present dataset is a subset of CARE dataset with compounds tested on the Caco2 cell line instead of on the VERO-E6 cell like in the CARE dataset. The dataset can be downloaded and beside structural information it will contain readout numbers for activity (e.g. either percentage of cellular cytopathic inhibition at one concentration or corresponding dose-response extracted IC50 (inhibition concentration at 50% inhibition)).

> These recommendations are based on ChEMBL ontology requirements; similar US data bank PubChem have different ontology requirements for upload but provide a wizard-based upload process described in this blog:  [https://pubchemblog.ncbi.nlm.nih.gov/tag/pubchem-upload/](https://pubchemblog.ncbi.nlm.nih.gov/tag/pubchem-upload/)


## Authors:
<table>
  <tr>
   <td>Name
   </td>
   <td>Affiliation
   </td>
   <td>orcid
   </td>
   <td> CrediT role
   </td>
  </tr>
  <tr>
   <td>Andrea Zaliani
   </td>
   <td>Fraunhofer ITMP Hamburg
   </td>
   <td><a href="https://orcid.org/0000-0002-1740-8390">0000-0002-1740-8390</a>
   </td>
   <td>Writing - Original Draft
   </td>
  </tr>
  <tr>
   <td>Fuqi
   </td>
   <td>EBI
   </td>
   <td><a href="http://europepmc.org/search?query=AUTHORID:%220000-0002-5923-3859%22&sortby=Date">0000-0002-5923-3859</a>
   </td>
   <td>Writing - Original Draft
   </td>
  </tr>
</table>



## Licence:

[https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)