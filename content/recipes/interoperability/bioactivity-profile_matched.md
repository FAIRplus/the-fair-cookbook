(fcb-bioactivity-profile)=
# Bioactivity data profile


````{panels_fairplus}
:identifier_text: FCB057
:identifier_link: 'https://w3id.org/faircookbook/FCB057'
:difficulty_level: 2
:recipe_type: hands_on
:reading_time_minutes: 30
:intended_audience: principal_investigator, data_manager, data_scientist  
:maturity_level: 3
:maturity_indicator: 30, 31
:has_executable_code: nope
:recipe_name: Outlining a metadata profile for Bioactivity data
```` 

## Main objective
This recipe shows how to prepare `bioactivity data`, defined as the measurable effects of a chemical compound in a biological system monitored with a specific assay, to meet the ChEMBL (URL_TO_INSERT_RECORD_5180 https://fairsharing.org/FAIRsharing.m3jtpg)  (URL_TO_INSERT_RECORD_5181 https://fairsharing.org/FAIRsharing.m3jtpg)  submission criteria, focusing on data format (URL_TO_INSERT_TERM_5179 https://fairsharing.org/search?recordType=model_and_format) s, structures, and vocabularies. 
This recipe is meant to address the Findability and Interoperability of such type of data.

## Graphical overview of the Recipe FAIRification Objectives


<!-- ```{figure} bioactivity-figure1.mmd.png -->
<!-- --- -->
<!-- name: bioactivity-figure1 -->
<!-- alt:  bioactivity data FAIR overview -->
<!-- --- -->
<!-- bioactivity data FAIR overview -->
<!-- --- -->
<!-- ``` -->
<!-- -->


## Introduction
Bioactivity data, as stored in public arch (URL_TO_INSERT_RECORD_5185 https://fairsharing.org/FAIRsharing.52b22c) ives such as the European repository (URL_TO_INSERT_TERM_5182 https://fairsharing.org/search?recordType=repository)  [CHEMBL](https://www.ebi.ac.uk/chembl (URL_TO_INSERT_RECORD_5184 https://fairsharing.org/FAIRsharing.m3jtpg) /) or its US counterpart [PubChem](https://pubchem.ncbi.nlm.nih.gov (URL_TO_INSERT_RECORD_5187 https://fairsharing.org/FAIRsharing.qt3w7z) /) in together with chemical data and omics data, can be used to search (URL_TO_INSERT_RECORD_5186 https://fairsharing.org/FAIRsharing.52b22c)  for new `hits`(compounds with desired property in drug screening), for example by using cell line informat (URL_TO_INSERT_TERM_5183 https://fairsharing.org/search?recordType=model_and_format) ion, compound ID as input to queries over such resources.

Early-stage bioactivity dataset includes compound molecular structure, molecular production details, assay data and, pharmacokinetic study informat (URL_TO_INSERT_TERM_5188 https://fairsharing.org/search?recordType=model_and_format) ion.

The FAIR (URL_TO_INSERT_RECORD_5190 https://fairsharing.org/FAIRsharing.WWI10U)  principles (URL_TO_INSERT_RECORD_5189 https://fairsharing.org/FAIRsharing.WWI10U)  for data management can guide the improvements of pharmacokinetic properties of compounds and the identification of drug targets by enhancing the reporting of `bioactivity data`.

Among the FAIR (URL_TO_INSERT_RECORD_5194 https://fairsharing.org/FAIRsharing.WWI10U)  principles (URL_TO_INSERT_RECORD_5193 https://fairsharing.org/FAIRsharing.WWI10U) , the `use of  rich metadata` (F2. data are described with rich metadata and R1. meta(data) are richly described with a plurality of accurate and relevant attributes) and the reliance on `community standard (URL_TO_INSERT_TERM_5191 https://fairsharing.org/search?fairsharingRegistry=Standard) s`  (R1.3. (meta)data meet domain-relevant community standard (URL_TO_INSERT_TERM_5192 https://fairsharing.org/search?fairsharingRegistry=Standard) s) are essential.

In the context of `bioactivity data`, we have on the one hand the [Minimum informat (URL_TO_INSERT_TERM_5195 https://fairsharing.org/search?recordType=model_and_format) ion about a bioactive entity (URL_TO_INSERT_RECORD_5197 https://fairsharing.org/FAIRsharing.dt7hn8)  (MIABE)](https://www.nature.com/articles/nrd3503) checklist recommend attributes, format (URL_TO_INSERT_TERM_5196 https://fairsharing.org/search?recordType=model_and_format) s and vocabularies for the reuse of such datasets. 

On the other hand, public bioactivity data arch (URL_TO_INSERT_RECORD_5200 https://fairsharing.org/FAIRsharing.52b22c) ives, such as [ChEMBL](https://www.ebi.ac.uk/chembl (URL_TO_INSERT_RECORD_5198 https://fairsharing.org/FAIRsharing.m3jtpg) /), [PubChem](https://pubchem.ncbi.nlm.nih.gov (URL_TO_INSERT_RECORD_5201 https://fairsharing.org/FAIRsharing.qt3w7z) /), and [ECBD](https://ecbd.eu (URL_TO_INSERT_RECORD_5199 https://fairsharing.org/3717) /) also have their own requirements for data submission.


### Data content

<table>
  <tr>
   <td><strong>Content</strong>
   </td>
   <td><strong>Details</strong>
   </td>
   <td><strong>Data types</strong>
   </td>
  </tr>
  <tr>
   <td>Chemistry (URL_TO_INSERT_RECORD_5202 https://fairsharing.org/3524)  (URL_TO_INSERT_RECORD_5203 https://fairsharing.org/3524)  (SDF (URL_TO_INSERT_RECORD_5204 https://fairsharing.org/FAIRsharing.ew26v7) )
   </td>
   <td>Structure ID
   </td>
   <td>
<ul>

<li>SDF (URL_TO_INSERT_RECORD_5205 https://fairsharing.org/FAIRsharing.ew26v7) 

<li>SMILE

<li>InChI (URL_TO_INSERT_RECORD_5206 https://fairsharing.org/FAIRsharing.ddk9t9) 

<li>CID
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Target 
   </td>
   <td>Protein (URL_TO_INSERT_RECORD_5207 https://fairsharing.org/FAIRsharing.rtndct) /GENE ID
   </td>
   <td>PN_ or SwissProt ID
   </td>
  </tr>
  <tr>
   <td>Assay
   </td>
   <td>Typology
   </td>
   <td>Binding, FR (URL_TO_INSERT_RECORD_5208 https://fairsharing.org/FAIRsharing.e7e609) ET, SP (URL_TO_INSERT_RECORD_5209 https://fairsharing.org/FAIRsharing.s63y3p) R, Inhibition, phenotypic cellular
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
<li>OME (URL_TO_INSERT_RECORD_5210 https://fairsharing.org/3502) TIFF
<li>Matrix Format (URL_TO_INSERT_TERM_5211 https://fairsharing.org/search?recordType=model_and_format) -Zarr
</li>
</ul>
   </td>
  </tr>
</table>

### Minimum metadata 

A **minimum metadata set** represents a collection (URL_TO_INSERT_TERM_5212 https://fairsharing.org/search?recordType=collection)  of metadata items that should ideally be systematically supplied to support interpretation by humans or machines within a specific domain, for instance bioactivity experimental data. The minimum metadata set includes three parts: 

1. Assay and project (URL_TO_INSERT_TERM_5213 https://fairsharing.org/search?recordType=project)  bibliographic references (mainly links to literature and protocol or summary)
    - Project (URL_TO_INSERT_TERM_5214 https://fairsharing.org/search?recordType=project)  level metadata
    - Common sample-level metadata, such as species, tissue, cell type and so on.
2. Chemical compounds reference, including chemical structures
3. Assay results 

![](https://i.imgur.com/aU2KYV1.png)

For ChEMBL (URL_TO_INSERT_RECORD_5216 https://fairsharing.org/FAIRsharing.m3jtpg)  (URL_TO_INSERT_RECORD_5217 https://fairsharing.org/FAIRsharing.m3jtpg)  submission, molecular structures and assay description as depicted in the scheme above are suggested as essential metadata. This is a subset of the following [schema](https://www.ebi.ac.uk/chembl (URL_TO_INSERT_RECORD_5218 https://fairsharing.org/FAIRsharing.m3jtpg) /db_schema). In case mutated cell lines and/or mutated target proteins have been used in the assay, additional desirable metadata should be added in the proper group. MIABE (URL_TO_INSERT_RECORD_5215 https://fairsharing.org/FAIRsharing.dt7hn8)  also lists detailed bioassay description requirements.

Besides metadata, the diagram below also shows how to prepare numeric assay data.

<!--  ```{figure} bioactivity-figure2.mmd.png -->
<!-- --- -->
<!-- name: bioactivity-figure2 -->
<!-- alt: Preparing numeric assay data for bioactivity -->
<!-- --- -->
<!-- Preparing numeric assay data for bioactivity -->
<!-- ```  -->



### Data vocabularies

[A set of well-established standard (URL_TO_INSERT_TERM_5219 https://fairsharing.org/search?fairsharingRegistry=Standard) s and **minimum metadata checklists**](https://chembl.gitbook.io/chembl-loader/untitled-10) exist for various aspects of ChEMBL (URL_TO_INSERT_RECORD_5221 https://fairsharing.org/FAIRsharing.m3jtpg)  (URL_TO_INSERT_RECORD_5222 https://fairsharing.org/FAIRsharing.m3jtpg)  format (URL_TO_INSERT_TERM_5220 https://fairsharing.org/search?recordType=model_and_format) ting.  

* **Chemical informat (URL_TO_INSERT_TERM_5223 https://fairsharing.org/search?recordType=model_and_format) ion ontology (URL_TO_INSERT_TERM_5224 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_5225 https://fairsharing.org/FAIRsharing.sjhvyy)  (CHEMINF (URL_TO_INSERT_RECORD_5226 https://fairsharing.org/FAIRsharing.sjhvyy) )** [http://semanticchemistry.github.io/semanticchemistry/ontology/cheminf.owl](http://semanticchemistry.github.io/semanticchemistry/ontology/cheminf.owl) 

    CHEMINF (URL_TO_INSERT_RECORD_5229 https://fairsharing.org/FAIRsharing.sjhvyy)  covers informat (URL_TO_INSERT_TERM_5227 https://fairsharing.org/search?recordType=model_and_format) ion about chemical entities and defines descriptors commonly used in cheminformat (URL_TO_INSERT_TERM_5228 https://fairsharing.org/search?recordType=model_and_format) ics software applications and to denote algorithms used to generate those chemicals.

* **BioAssay Ontology (URL_TO_INSERT_TERM_5230 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_5232 https://fairsharing.org/FAIRsharing.mye76w) **(BAO (URL_TO_INSERT_RECORD_5231 https://fairsharing.org/FAIRsharing.k2dq5j)  (URL_TO_INSERT_RECORD_5233 https://fairsharing.org/FAIRsharing.mye76w) )

    [http://www.bioassayontology.org (URL_TO_INSERT_RECORD_5234 https://fairsharing.org/FAIRsharing.farr39)  (URL_TO_INSERT_RECORD_5236 https://fairsharing.org/FAIRsharing.mye76w) /bao/bao_complete.owl](http://www.bioassayontology.org (URL_TO_INSERT_RECORD_5235 https://fairsharing.org/FAIRsharing.farr39)  (URL_TO_INSERT_RECORD_5237 https://fairsharing.org/FAIRsharing.mye76w) /bao/bao_complete.owl) 

    The BioAssay Ontology (URL_TO_INSERT_TERM_5238 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_5244 https://fairsharing.org/FAIRsharing.mye76w)  (BAO (URL_TO_INSERT_RECORD_5242 https://fairsharing.org/FAIRsharing.k2dq5j)  (URL_TO_INSERT_RECORD_5245 https://fairsharing.org/FAIRsharing.mye76w) ) describes biological screening assays and their results, including high-throughput screening (HTS) data for the purpose of categorising assays and data analysis. BAO (URL_TO_INSERT_RECORD_5243 https://fairsharing.org/FAIRsharing.k2dq5j)  (URL_TO_INSERT_RECORD_5246 https://fairsharing.org/FAIRsharing.mye76w)  is an extensible, knowledge-based, highly expressive description of biological assays {footcite}`pmid21702939` making use of descriptive logic based features of the [Web Ontology (URL_TO_INSERT_TERM_5239 https://fairsharing.org/search?recordType=terminology_artefact)  Language (URL_TO_INSERT_RECORD_5240 https://fairsharing.org/FAIRsharing.atygwy)  (OWL (URL_TO_INSERT_RECORD_5241 https://fairsharing.org/FAIRsharing.atygwy) )](https://www.w3.org/TR/owl2-syntax/)

* **Ontology (URL_TO_INSERT_TERM_5247 https://fairsharing.org/search?recordType=terminology_artefact)  of units of Measure (OM)**
 [http://www.ontology-of-units-of-measure.org/resource/om-2](http://www.ontology-of-units-of-measure.org/resource/om-2) 
 The OM ontology (URL_TO_INSERT_TERM_5248 https://fairsharing.org/search?recordType=terminology_artefact)  provides classes, instances, and properties that represent the different concepts used for defining and using measures and units.
 It includes, for instance, common units such as the SI units meter and kilogram, and a wide range of units of significance for the field of Chemistry (URL_TO_INSERT_RECORD_5250 https://fairsharing.org/3524)  (URL_TO_INSERT_RECORD_5251 https://fairsharing.org/3524)  and related informat (URL_TO_INSERT_TERM_5249 https://fairsharing.org/search?recordType=model_and_format) ion.
It can be easily map (URL_TO_INSERT_RECORD_5252 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_5254 https://fairsharing.org/FAIRsharing.31385c)  to other resources such as [Unit Ontology](https://www.ebi.ac.uk/ols/ontologies/om), with tools such as [OXO](https://www.ebi.ac.uk/spot/oxo (URL_TO_INSERT_RECORD_5253 https://fairsharing.org/FAIRsharing.0c6fea) /)

More informat (URL_TO_INSERT_TERM_5255 https://fairsharing.org/search?recordType=model_and_format) ion on annotating data with ontologies (URL_TO_INSERT_TERM_5256 https://fairsharing.org/search?recordType=terminology_artefact)  using tools like [Zooma](https://www.ebi.ac.uk/spot/zooma/), can be found in Section 7.7.3.3. of [this recipe](https://w3id.org (URL_TO_INSERT_RECORD_5257 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB023)

### Exemplar Bioactivity datasets

[SARS (URL_TO_INSERT_RECORD_5259 https://fairsharing.org/FAIRsharing.vajn3f)  CoV2 phenotypic assay from Caco2 cell line](https://www.ebi.ac.uk/chembl (URL_TO_INSERT_RECORD_5258 https://fairsharing.org/FAIRsharing.m3jtpg) /assay_report_card/CHEMBL4303806/)

The present dataset is a subset of [IMI CARE](https://www.imi.europa.eu/projects-results/project-factsheets/care) dataset with compounds tested on the Caco-2 cell line. The dataset can be downloaded and, besides structural informat (URL_TO_INSERT_TERM_5260 https://fairsharing.org/search?recordType=model_and_format) ion, it will contain readout numbers for activity (e.g. either `percentage of cellular cytopathic inhibition at a given concentration` or corresponding extracted `dose-response IC50 `(Half-maximal inhibitory concentration)).

> Recommendations above are based on ChEMBL (URL_TO_INSERT_RECORD_5263 https://fairsharing.org/FAIRsharing.m3jtpg)  (URL_TO_INSERT_RECORD_5265 https://fairsharing.org/FAIRsharing.m3jtpg)  ontology (URL_TO_INSERT_TERM_5261 https://fairsharing.org/search?recordType=terminology_artefact)  requirements. The US counterpart to ChEMBL (URL_TO_INSERT_RECORD_5264 https://fairsharing.org/FAIRsharing.m3jtpg)  (URL_TO_INSERT_RECORD_5266 https://fairsharing.org/FAIRsharing.m3jtpg) , the  PubChem (URL_TO_INSERT_RECORD_5267 https://fairsharing.org/FAIRsharing.qt3w7z)  (URL_TO_INSERT_RECORD_5268 https://fairsharing.org/FAIRsharing.qt3w7z)  data bank have different ontology (URL_TO_INSERT_TERM_5262 https://fairsharing.org/search?recordType=terminology_artefact)  requirements for upload but provide a wizard-based upload process described in [this blog](https://pubchemblog.ncbi.nlm.nih.gov/tag/pubchem-upload/)

## Glossary
|Term|Definition|
|--|--|
|Experiment|Bioc (URL_TO_INSERT_RECORD_5269 https://fairsharing.org/FAIRsharing.81ettx) hamical Assay, Cellular Activity Assay, Cellular Toxicity Assay|
|Readout|Quantitive measurements of a biophysical event followed by assay (e.g. change in fluorescence)|
|EC50|Half maximal Effective Concentration|
|IC50|Half maximal Inhibition Concentration|
|AC (URL_TO_INSERT_RECORD_5270 https://fairsharing.org/FAIRsharing.md3e78) 50|Half maximal Activation Concentration|
|CC50|Half maximal Cytotoxic Concentration|

### What to read next?
- [InChI (URL_TO_INSERT_RECORD_5274 https://fairsharing.org/FAIRsharing.ddk9t9)  and SMILES (URL_TO_INSERT_RECORD_5273 https://fairsharing.org/FAIRsharing.qv4b3c)  identifier (URL_TO_INSERT_TERM_5271 https://fairsharing.org/search?recordType=identifier_schema) s for chemical structures](https://w3id.org (URL_TO_INSERT_RECORD_5272 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB007)
- [ChEMBL (URL_TO_INSERT_RECORD_5275 https://fairsharing.org/FAIRsharing.m3jtpg)  (URL_TO_INSERT_RECORD_5276 https://fairsharing.org/FAIRsharing.m3jtpg)  interface documentation](https://chembl.gitbook.io/chembl-interface-documentation/)



## References
````{dropdown} **References**
```{footbibliography}
```
````
<!-- Visser, U., Abeyruwan, S., Vempati, U. et al. BioAssay Ontology (BAO): a semantic description of bioassays and high-throughput screening results. BMC Bioinformatics 12, 257 (2011). https://doi.org/10.1186/1471-2105-12-257 -->



## Authors

```{authors_fairplus}
AndreaZaliani: Writing - Original Draft, Editing, Conceptualization
Fuqi: Writing - Writing - Original Draft, Editing, Conceptualization
Philippe: Writing - Review & Editing
```

## Licence

````{license_fairplus}
CC-BY-4.0
````

