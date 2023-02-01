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
This recipe shows how to prepare `bioactivity data`, defined as the measurable effects of a chemical compound in a biological system monitored with a specific assay, to meet the ChEMB (URL_TO_INSERT_RECORD_5583 https://fairsharing.org/FAIRsharing.a1rp4c) L (URL_TO_INSERT_RECORD_5581 https://fairsharing.org/FAIRsharing.m3jtpg)  (URL_TO_INSERT_RECORD_5582 https://fairsharing.org/FAIRsharing.m3jtpg)  submission criteria, focusing on data format (URL_TO_INSERT_TERM_5580 https://fairsharing.org/search?recordType=model_and_format) s, structures, and vocabularies. 
This recipe is meant to address the Findability and Interoperability of such type of data.

## Graphical overview of the Recipe FAIRification Objectives


<!-- ```{figure} bioactivity-figure1.mmd.png -->
<!-- --- -->
<!-- name: bioactivity-figure1 -->
<!-- alt:  bioactivity data FAIR (URL_TO_INSERT_RECORD_5584 https://fairsharing.org/FAIRsharing.WWI10U)  overview -->
<!-- --- -->
<!-- bioactivity data FAIR (URL_TO_INSERT_RECORD_5585 https://fairsharing.org/FAIRsharing.WWI10U)  overview -->
<!-- --- -->
<!-- ``` -->
<!-- -->


## Introduction
Bioactivity data, as stored in public arch (URL_TO_INSERT_RECORD_5589 https://fairsharing.org/FAIRsharing.52b22c) ives such as the European repository (URL_TO_INSERT_TERM_5586 https://fairsharing.org/search?recordType=repository)  [CHEMBL](https://www.ebi.ac.uk/chembl (URL_TO_INSERT_RECORD_5588 https://fairsharing.org/FAIRsharing.m3jtpg) /) or its US counterpart [PubChem](https://pubchem.ncbi.nlm.nih.gov (URL_TO_INSERT_RECORD_5591 https://fairsharing.org/FAIRsharing.qt3w7z) /) in together with chemical data and omics data, can be used to search (URL_TO_INSERT_RECORD_5590 https://fairsharing.org/FAIRsharing.52b22c)  for new `hits`(compounds with desired property in drug screening), for example by using cell line informat (URL_TO_INSERT_TERM_5587 https://fairsharing.org/search?recordType=model_and_format) ion, compound ID as input to queries over such resources.

Early-stage bioactivity dataset includes compound molecular structure, molecular production details, assay data and, pharmacokinetic study informat (URL_TO_INSERT_TERM_5592 https://fairsharing.org/search?recordType=model_and_format) ion.

The FAIR (URL_TO_INSERT_RECORD_5594 https://fairsharing.org/FAIRsharing.WWI10U)  principles (URL_TO_INSERT_RECORD_5593 https://fairsharing.org/FAIRsharing.WWI10U)  for data management can guide the improvements of pharmacokinetic properties of compounds and the identification of drug targets by enhancing the reporting of `bioactivity data`.

Among the FAIR (URL_TO_INSERT_RECORD_5598 https://fairsharing.org/FAIRsharing.WWI10U)  principles (URL_TO_INSERT_RECORD_5597 https://fairsharing.org/FAIRsharing.WWI10U) , the `use of  rich metadata` (F2. data are described with rich metadata and R1. meta(data) are richly described with a plurality of accurate and relevant attributes) and the reliance on `community standard (URL_TO_INSERT_TERM_5595 https://fairsharing.org/search?fairsharingRegistry=Standard) s`  (R1.3. (meta)data meet domain-relevant community standard (URL_TO_INSERT_TERM_5596 https://fairsharing.org/search?fairsharingRegistry=Standard) s) are essential.

In the context of `bioactivity data`, we have on the one hand the [Minimum informat (URL_TO_INSERT_TERM_5599 https://fairsharing.org/search?recordType=model_and_format) ion about a bioactive entity (URL_TO_INSERT_RECORD_5601 https://fairsharing.org/FAIRsharing.dt7hn8)  (MIABE)](https://www.nature.com/articles/nrd3503) checklist recommend attributes, format (URL_TO_INSERT_TERM_5600 https://fairsharing.org/search?recordType=model_and_format) s and vocabularies for the reuse of such datasets. 

On the other hand, public bioactivity data arch (URL_TO_INSERT_RECORD_5604 https://fairsharing.org/FAIRsharing.52b22c) ives, such as [ChEMBL](https://www.ebi.ac.uk/chembl (URL_TO_INSERT_RECORD_5602 https://fairsharing.org/FAIRsharing.m3jtpg) /), [PubChem](https://pubchem.ncbi.nlm.nih.gov (URL_TO_INSERT_RECORD_5605 https://fairsharing.org/FAIRsharing.qt3w7z) /), and [ECBD](https://ecbd.eu (URL_TO_INSERT_RECORD_5603 https://fairsharing.org/3717) /) also have their own requirements for data submission.


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
   <td>Chemistry (URL_TO_INSERT_RECORD_5606 https://fairsharing.org/3524)  (URL_TO_INSERT_RECORD_5607 https://fairsharing.org/3524)  (SDF (URL_TO_INSERT_RECORD_5608 https://fairsharing.org/FAIRsharing.ew26v7) )
   </td>
   <td>Structure ID
   </td>
   <td>
<ul>

<li>SDF (URL_TO_INSERT_RECORD_5609 https://fairsharing.org/FAIRsharing.ew26v7) 

<li>SMILE

<li>InChI (URL_TO_INSERT_RECORD_5610 https://fairsharing.org/FAIRsharing.ddk9t9) 

<li>CID (URL_TO_INSERT_RECORD_5611 https://fairsharing.org/FAIRsharing.g63c77) 
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Target 
   </td>
   <td>Protein (URL_TO_INSERT_RECORD_5612 https://fairsharing.org/FAIRsharing.rtndct) /GENE ID
   </td>
   <td>PN_ or SwissProt ID
   </td>
  </tr>
  <tr>
   <td>Assay
   </td>
   <td>Typology
   </td>
   <td>Binding, FR (URL_TO_INSERT_RECORD_5613 https://fairsharing.org/FAIRsharing.e7e609) ET, SP (URL_TO_INSERT_RECORD_5614 https://fairsharing.org/FAIRsharing.s63y3p) R, Inhibition, phenotypic cellular
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
<li>OME (URL_TO_INSERT_RECORD_5615 https://fairsharing.org/3502) TIFF
<li>Matrix Format (URL_TO_INSERT_TERM_5616 https://fairsharing.org/search?recordType=model_and_format) -Zarr
</li>
</ul>
   </td>
  </tr>
</table>

### Minimum metadata 

A **minimum metadata set** represents a collection (URL_TO_INSERT_TERM_5617 https://fairsharing.org/search?recordType=collection)  of metadata items that should ideally be systematically supplied to support interpretation by humans or machines within a specific domain, for instance bioactivity experimental data. The minimum metadata set includes three parts: 

1. Assay and project (URL_TO_INSERT_TERM_5618 https://fairsharing.org/search?recordType=project)  bibliographic references (mainly links to literature and protocol or summary)
    - Project (URL_TO_INSERT_TERM_5619 https://fairsharing.org/search?recordType=project)  level metadata
    - Common sample-level metadata, such as species, tissue, cell type and so on.
2. Chemical compounds reference, including chemical structures
3. Assay results 

![](https://i.imgur.com/aU2KYV1.png)

For ChEMB (URL_TO_INSERT_RECORD_5624 https://fairsharing.org/FAIRsharing.a1rp4c) L (URL_TO_INSERT_RECORD_5621 https://fairsharing.org/FAIRsharing.m3jtpg)  (URL_TO_INSERT_RECORD_5622 https://fairsharing.org/FAIRsharing.m3jtpg)  submission, molecular structures and assay description as depicted in the scheme above are suggested as essential metadata. This is a subset of the following [schema](https://www.ebi.ac.uk/chembl (URL_TO_INSERT_RECORD_5623 https://fairsharing.org/FAIRsharing.m3jtpg) /db_schema). In case mutated cell lines and/or mutated target proteins have been used in the assay, additional desirable metadata should be added in the proper group. MIABE (URL_TO_INSERT_RECORD_5620 https://fairsharing.org/FAIRsharing.dt7hn8)  also lists detailed bioassay description requirements.

Besides metadata, the diagram below also shows how to prepare numeric assay data.

<!--  ```{figure} bioactivity-figure2.mmd.png -->
<!-- --- -->
<!-- name: bioactivity-figure2 -->
<!-- alt: Preparing numeric assay data for bioactivity -->
<!-- --- -->
<!-- Preparing numeric assay data for bioactivity -->
<!-- ```  -->



### Data vocabularies

[A set of well-established standard (URL_TO_INSERT_TERM_5625 https://fairsharing.org/search?fairsharingRegistry=Standard) s and **minimum metadata checklists**](https://chembl.gitbook.io/chembl-loader/untitled-10) exist for various aspects of ChEMB (URL_TO_INSERT_RECORD_5629 https://fairsharing.org/FAIRsharing.a1rp4c) L (URL_TO_INSERT_RECORD_5627 https://fairsharing.org/FAIRsharing.m3jtpg)  (URL_TO_INSERT_RECORD_5628 https://fairsharing.org/FAIRsharing.m3jtpg)  format (URL_TO_INSERT_TERM_5626 https://fairsharing.org/search?recordType=model_and_format) ting.  

* **Chemical informat (URL_TO_INSERT_TERM_5630 https://fairsharing.org/search?recordType=model_and_format) ion ontology (URL_TO_INSERT_TERM_5631 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_5632 https://fairsharing.org/FAIRsharing.sjhvyy)  (CHEMINF (URL_TO_INSERT_RECORD_5633 https://fairsharing.org/FAIRsharing.sjhvyy) )** [http://semanticchemistry.github.io/semanticchemistry/ontology/cheminf.owl](http://semanticchemistry.github.io/semanticchemistry/ontology/cheminf.owl) 

    CHEMINF (URL_TO_INSERT_RECORD_5636 https://fairsharing.org/FAIRsharing.sjhvyy)  covers informat (URL_TO_INSERT_TERM_5634 https://fairsharing.org/search?recordType=model_and_format) ion about chemical entities and defines descriptors commonly used in cheminformat (URL_TO_INSERT_TERM_5635 https://fairsharing.org/search?recordType=model_and_format) ics software applications and to denote algorithms used to generate those chemicals.

* **BioAssay Ontology (URL_TO_INSERT_TERM_5637 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_5639 https://fairsharing.org/FAIRsharing.mye76w) **(BAO (URL_TO_INSERT_RECORD_5638 https://fairsharing.org/FAIRsharing.k2dq5j)  (URL_TO_INSERT_RECORD_5640 https://fairsharing.org/FAIRsharing.mye76w) )

    [http://www.bioassayontology.org (URL_TO_INSERT_RECORD_5641 https://fairsharing.org/FAIRsharing.farr39)  (URL_TO_INSERT_RECORD_5643 https://fairsharing.org/FAIRsharing.mye76w) /bao/bao_complete.owl](http://www.bioassayontology.org (URL_TO_INSERT_RECORD_5642 https://fairsharing.org/FAIRsharing.farr39)  (URL_TO_INSERT_RECORD_5644 https://fairsharing.org/FAIRsharing.mye76w) /bao/bao_complete.owl) 

    The BioAssay Ontology (URL_TO_INSERT_TERM_5645 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_5651 https://fairsharing.org/FAIRsharing.mye76w)  (BAO (URL_TO_INSERT_RECORD_5649 https://fairsharing.org/FAIRsharing.k2dq5j)  (URL_TO_INSERT_RECORD_5652 https://fairsharing.org/FAIRsharing.mye76w) ) describes biological screening assays and their results, including high-throughput screening (HTS) data for the purpose of categorising assays and data analysis. BAO (URL_TO_INSERT_RECORD_5650 https://fairsharing.org/FAIRsharing.k2dq5j)  (URL_TO_INSERT_RECORD_5653 https://fairsharing.org/FAIRsharing.mye76w)  is an extensible, knowledge-based, highly expressive description of biological assays {footcite}`pmid21702939` making use of descriptive logic based features of the [Web Ontology (URL_TO_INSERT_TERM_5646 https://fairsharing.org/search?recordType=terminology_artefact)  Language (URL_TO_INSERT_RECORD_5647 https://fairsharing.org/FAIRsharing.atygwy)  (OWL (URL_TO_INSERT_RECORD_5648 https://fairsharing.org/FAIRsharing.atygwy) )](https://www.w3.org/TR/owl2-syntax/)

* **Ontology (URL_TO_INSERT_TERM_5654 https://fairsharing.org/search?recordType=terminology_artefact)  of units of Measure (OM)**
 [http://www.ontology-of-units-of-measure.org/resource/om-2](http://www.ontology-of-units-of-measure.org/resource/om-2) 
 The OM ontology (URL_TO_INSERT_TERM_5655 https://fairsharing.org/search?recordType=terminology_artefact)  provides classes, instances, and properties that represent the different concepts used for defining and using measures and units.
 It includes, for instance, common units such as the SI units meter and kilogram, and a wide range of units of significance for the field of Chemistry (URL_TO_INSERT_RECORD_5657 https://fairsharing.org/3524)  (URL_TO_INSERT_RECORD_5658 https://fairsharing.org/3524)  and related informat (URL_TO_INSERT_TERM_5656 https://fairsharing.org/search?recordType=model_and_format) ion.
It can be easily map (URL_TO_INSERT_RECORD_5659 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_5661 https://fairsharing.org/FAIRsharing.31385c)  to other resources such as [Unit Ontology](https://www.ebi.ac.uk/ols/ontologies/om), with tools such as [OXO](https://www.ebi.ac.uk/spot/oxo (URL_TO_INSERT_RECORD_5660 https://fairsharing.org/FAIRsharing.0c6fea) /)

More informat (URL_TO_INSERT_TERM_5662 https://fairsharing.org/search?recordType=model_and_format) ion on annotating data with ontologies (URL_TO_INSERT_TERM_5663 https://fairsharing.org/search?recordType=terminology_artefact)  using tools like [Zooma](https://www.ebi.ac.uk/spot/zooma/), can be found in Section 7.7.3.3. of [this recipe](https://w3id.org (URL_TO_INSERT_RECORD_5664 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB023)

### Exemplar Bioactivity datasets

[SARS (URL_TO_INSERT_RECORD_5666 https://fairsharing.org/FAIRsharing.vajn3f)  CoV2 phenotypic assay from Caco2 cell line](https://www.ebi.ac.uk/chembl (URL_TO_INSERT_RECORD_5665 https://fairsharing.org/FAIRsharing.m3jtpg) /assay_report_card/CHEMBL4303806/)

The present dataset is a subset of [IMI CARE](https://www.imi.europa.eu/projects-results/project-factsheets/care) dataset with compounds tested on the Caco-2 cell line. The dataset can be downloaded and, besides structural informat (URL_TO_INSERT_TERM_5667 https://fairsharing.org/search?recordType=model_and_format) ion, it will contain readout numbers for activity (e.g. either `percentage of cellular cytopathic inhibition at a given concentration` or corresponding extracted `dose-response IC50 `(Half-maximal inhibitory concentration)).

> Recommendations above are based on ChEMB (URL_TO_INSERT_RECORD_5674 https://fairsharing.org/FAIRsharing.a1rp4c) L (URL_TO_INSERT_RECORD_5670 https://fairsharing.org/FAIRsharing.m3jtpg)  (URL_TO_INSERT_RECORD_5672 https://fairsharing.org/FAIRsharing.m3jtpg)  ontology (URL_TO_INSERT_TERM_5668 https://fairsharing.org/search?recordType=terminology_artefact)  requirements. The US counterpart to ChEMB (URL_TO_INSERT_RECORD_5675 https://fairsharing.org/FAIRsharing.a1rp4c) L (URL_TO_INSERT_RECORD_5671 https://fairsharing.org/FAIRsharing.m3jtpg)  (URL_TO_INSERT_RECORD_5673 https://fairsharing.org/FAIRsharing.m3jtpg) , the  PubChem (URL_TO_INSERT_RECORD_5676 https://fairsharing.org/FAIRsharing.qt3w7z)  (URL_TO_INSERT_RECORD_5677 https://fairsharing.org/FAIRsharing.qt3w7z)  data bank have different ontology (URL_TO_INSERT_TERM_5669 https://fairsharing.org/search?recordType=terminology_artefact)  requirements for upload but provide a wizard-based upload process described in [this blog](https://pubchemblog.ncbi.nlm.nih.gov/tag/pubchem-upload/)

## Glossary
|Term|Definition|
|--|--|
|Experiment|Bioc (URL_TO_INSERT_RECORD_5678 https://fairsharing.org/FAIRsharing.81ettx) hamical Assay, Cellular Activity Assay, Cellular Toxicity Assay|
|Readout|Quantitive measurements of a biophysical event followed by assay (e.g. change in fluorescence)|
|EC50|Half maximal Effective Concentration|
|IC50|Half maximal Inhibition Concentration|
|AC (URL_TO_INSERT_RECORD_5679 https://fairsharing.org/FAIRsharing.md3e78) 50|Half maximal Activation Concentration|
|CC50|Half maximal Cytotoxic Concentration|

### What to read next?
- [InChI (URL_TO_INSERT_RECORD_5683 https://fairsharing.org/FAIRsharing.ddk9t9)  and SMILES (URL_TO_INSERT_RECORD_5682 https://fairsharing.org/FAIRsharing.qv4b3c)  identifier (URL_TO_INSERT_TERM_5680 https://fairsharing.org/search?recordType=identifier_schema) s for chemical structures](https://w3id.org (URL_TO_INSERT_RECORD_5681 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB007)
- [ChEMB (URL_TO_INSERT_RECORD_5686 https://fairsharing.org/FAIRsharing.a1rp4c) L (URL_TO_INSERT_RECORD_5684 https://fairsharing.org/FAIRsharing.m3jtpg)  (URL_TO_INSERT_RECORD_5685 https://fairsharing.org/FAIRsharing.m3jtpg)  interface documentation](https://chembl.gitbook.io/chembl-interface-documentation/)



## References
````{dropdown} **References**
```{footbibliography}
```
````
<!-- Visser, U., Abeyruwan, S., Vempati, U. et al. BioAssay Ontology (URL_TO_INSERT_TERM_5688 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_5690 https://fairsharing.org/FAIRsharing.mye76w)  (BAO (URL_TO_INSERT_RECORD_5689 https://fairsharing.org/FAIRsharing.k2dq5j)  (URL_TO_INSERT_RECORD_5691 https://fairsharing.org/FAIRsharing.mye76w) ): a semantic description of bioassays and high-throughput screening results. BMC Bioinformat (URL_TO_INSERT_TERM_5687 https://fairsharing.org/search?recordType=model_and_format) ics 12, 257 (2011). https://doi.org/10.1186/1471-2105-12-257 -->



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

