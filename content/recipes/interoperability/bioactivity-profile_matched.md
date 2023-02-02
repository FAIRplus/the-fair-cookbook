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
This recipe shows how to prepare `bioactivity data`, defined as the measurable effects of a chemical compound in a biological system monitored with a specific assay, to meet the ChEMBL (URL_TO_INSERT_RECORD_3752 https://fairsharing.org/FAIRsharing.m3jtpg)  submission criteria, focusing on data format (URL_TO_INSERT_TERM_3751 https://fairsharing.org/search?recordType=model_and_format) s, structures, and vocabularies. 
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
Bioactivity data, as stored in public arch (URL_TO_INSERT_RECORD_3755 https://fairsharing.org/FAIRsharing.52b22c) ives such as the European repository (URL_TO_INSERT_TERM_3753 https://fairsharing.org/search?recordType=repository)  [CHEMBL](https://www.ebi.ac.uk/chembl/) or its US counterpart [PubChem](https://pubchem.ncbi.nlm.nih.gov/) in together with chemical data and omics data, can be used to search (URL_TO_INSERT_RECORD_3756 https://fairsharing.org/FAIRsharing.52b22c)  for new `hits`(compounds with desired property in drug screening), for example by using cell line informat (URL_TO_INSERT_TERM_3754 https://fairsharing.org/search?recordType=model_and_format) ion, compound ID as input to queries over such resources.

Early-stage bioactivity dataset includes compound molecular structure, molecular production details, assay data and, pharmacokinetic study informat (URL_TO_INSERT_TERM_3757 https://fairsharing.org/search?recordType=model_and_format) ion.

The FAIR (URL_TO_INSERT_RECORD_3759 https://fairsharing.org/FAIRsharing.WWI10U)  principles (URL_TO_INSERT_RECORD_3758 https://fairsharing.org/FAIRsharing.WWI10U)  for data management can guide the improvements of pharmacokinetic properties of compounds and the identification of drug targets by enhancing the reporting of `bioactivity data`.

Among the FAIR (URL_TO_INSERT_RECORD_3763 https://fairsharing.org/FAIRsharing.WWI10U)  principles (URL_TO_INSERT_RECORD_3762 https://fairsharing.org/FAIRsharing.WWI10U) , the `use of  rich metadata` (F2. data are described with rich metadata and R1. meta(data) are richly described with a plurality of accurate and relevant attributes) and the reliance on `community standard (URL_TO_INSERT_TERM_3760 https://fairsharing.org/search?fairsharingRegistry=Standard) s`  (R1.3. (meta)data meet domain-relevant community standard (URL_TO_INSERT_TERM_3761 https://fairsharing.org/search?fairsharingRegistry=Standard) s) are essential.

In the context of `bioactivity data`, we have on the one hand the [Minimum information about a bioactive entity (MIABE)](https://www.nature.com/articles/nrd3503) checklist recommend attributes, format (URL_TO_INSERT_TERM_3764 https://fairsharing.org/search?recordType=model_and_format) s and vocabularies for the reuse of such datasets. 

On the other hand, public bioactivity data arch (URL_TO_INSERT_RECORD_3765 https://fairsharing.org/FAIRsharing.52b22c) ives, such as [ChEMBL](https://www.ebi.ac.uk/chembl/), [PubChem](https://pubchem.ncbi.nlm.nih.gov/), and [ECBD](https://ecbd.eu/) also have their own requirements for data submission.


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
   <td>Chemistry (URL_TO_INSERT_RECORD_3766 https://fairsharing.org/3524)  (SDF)
   </td>
   <td>Structure ID
   </td>
   <td>
<ul>

<li>SDF

<li>SMILE

<li>InChI (URL_TO_INSERT_RECORD_3767 https://fairsharing.org/FAIRsharing.ddk9t9) 

<li>CID
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Target 
   </td>
   <td>Protein (URL_TO_INSERT_RECORD_3768 https://fairsharing.org/FAIRsharing.rtndct) /GENE ID
   </td>
   <td>PN_ or SwissProt ID
   </td>
  </tr>
  <tr>
   <td>Assay
   </td>
   <td>Typology
   </td>
   <td>Binding, FR (URL_TO_INSERT_RECORD_3769 https://fairsharing.org/FAIRsharing.e7e609) ET, SP (URL_TO_INSERT_RECORD_3770 https://fairsharing.org/FAIRsharing.s63y3p) R, Inhibition, phenotypic cellular
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
<li>Matrix Format (URL_TO_INSERT_TERM_3771 https://fairsharing.org/search?recordType=model_and_format) -Zarr
</li>
</ul>
   </td>
  </tr>
</table>

### Minimum metadata 

A **minimum metadata set** represents a collection (URL_TO_INSERT_TERM_3772 https://fairsharing.org/search?recordType=collection)  of metadata items that should ideally be systematically supplied to support interpretation by humans or machines within a specific domain, for instance bioactivity experimental data. The minimum metadata set includes three parts: 

1. Assay and project (URL_TO_INSERT_TERM_3773 https://fairsharing.org/search?recordType=project)  bibliographic references (mainly links to literature and protocol or summary)
    - Project (URL_TO_INSERT_TERM_3774 https://fairsharing.org/search?recordType=project)  level metadata
    - Common sample-level metadata, such as species, tissue, cell type and so on.
2. Chemical compounds reference, including chemical structures
3. Assay results 

![](https://i.imgur.com/aU2KYV1.png)

For ChEMBL (URL_TO_INSERT_RECORD_3776 https://fairsharing.org/FAIRsharing.m3jtpg)  submission, molecular structures and assay description as depicted in the scheme above are suggested as essential metadata. This is a subset of the following [schema](https://www.ebi.ac.uk/chembl/db_schema). In case mutated cell lines and/or mutated target proteins have been used in the assay, additional desirable metadata should be added in the proper group. MIABE (URL_TO_INSERT_RECORD_3775 https://fairsharing.org/FAIRsharing.dt7hn8)  also lists detailed bioassay description requirements.

Besides metadata, the diagram below also shows how to prepare numeric assay data.

<!--  ```{figure} bioactivity-figure2.mmd.png -->
<!-- --- -->
<!-- name: bioactivity-figure2 -->
<!-- alt: Preparing numeric assay data for bioactivity -->
<!-- --- -->
<!-- Preparing numeric assay data for bioactivity -->
<!-- ```  -->



### Data vocabularies

[A set of well-established standards and **minimum metadata checklists**](https://chembl.gitbook.io/chembl-loader/untitled-10) exist for various aspects of ChEMBL (URL_TO_INSERT_RECORD_3778 https://fairsharing.org/FAIRsharing.m3jtpg)  format (URL_TO_INSERT_TERM_3777 https://fairsharing.org/search?recordType=model_and_format) ting.  

* **Chemical informat (URL_TO_INSERT_TERM_3779 https://fairsharing.org/search?recordType=model_and_format) ion ontology (URL_TO_INSERT_TERM_3780 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_3781 https://fairsharing.org/FAIRsharing.sjhvyy)  (CHEMINF (URL_TO_INSERT_RECORD_3782 https://fairsharing.org/FAIRsharing.sjhvyy) )** [http://semanticchemistry.github.io/semanticchemistry/ontology/cheminf.owl](http://semanticchemistry.github.io/semanticchemistry/ontology/cheminf.owl) 

    CHEMINF (URL_TO_INSERT_RECORD_3785 https://fairsharing.org/FAIRsharing.sjhvyy)  covers informat (URL_TO_INSERT_TERM_3783 https://fairsharing.org/search?recordType=model_and_format) ion about chemical entities and defines descriptors commonly used in cheminformat (URL_TO_INSERT_TERM_3784 https://fairsharing.org/search?recordType=model_and_format) ics software applications and to denote algorithms used to generate those chemicals.

* **BioAssay Ontology (URL_TO_INSERT_TERM_3786 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_3787 https://fairsharing.org/FAIRsharing.mye76w) **(BAO)

    [http://www.bioassayontology.org/bao/bao_complete.owl](http://www.bioassayontology.org/bao/bao_complete.owl) 

    The BioAssay Ontology (URL_TO_INSERT_TERM_3788 https://fairsharing.org/search?recordType=terminology_artefact)  (URL_TO_INSERT_RECORD_3789 https://fairsharing.org/FAIRsharing.mye76w)  (BAO) describes biological screening assays and their results, including high-throughput screening (HTS) data for the purpose of categorising assays and data analysis. BAO (URL_TO_INSERT_RECORD_3790 https://fairsharing.org/FAIRsharing.mye76w)  is an extensible, knowledge-based, highly expressive description of biological assays {footcite}`pmid21702939` making use of descriptive logic based features of the [Web Ontology Language (OWL)](https://www.w3.org/TR/owl2-syntax/)

* **Ontology (URL_TO_INSERT_TERM_3791 https://fairsharing.org/search?recordType=terminology_artefact)  of units of Measure (OM)**
 [http://www.ontology-of-units-of-measure.org/resource/om-2](http://www.ontology-of-units-of-measure.org/resource/om-2) 
 The OM ontology (URL_TO_INSERT_TERM_3792 https://fairsharing.org/search?recordType=terminology_artefact)  provides classes, instances, and properties that represent the different concepts used for defining and using measures and units.
 It includes, for instance, common units such as the SI units meter and kilogram, and a wide range of units of significance for the field of Chemistry (URL_TO_INSERT_RECORD_3794 https://fairsharing.org/3524)  and related informat (URL_TO_INSERT_TERM_3793 https://fairsharing.org/search?recordType=model_and_format) ion.
It can be easily map (URL_TO_INSERT_RECORD_3795 https://fairsharing.org/FAIRsharing.53edcc) ped (URL_TO_INSERT_RECORD_3796 https://fairsharing.org/FAIRsharing.31385c)  to other resources such as [Unit Ontology](https://www.ebi.ac.uk/ols/ontologies/om), with tools such as [OXO](https://www.ebi.ac.uk/spot/oxo/)

More informat (URL_TO_INSERT_TERM_3797 https://fairsharing.org/search?recordType=model_and_format) ion on annotating data with ontologies (URL_TO_INSERT_TERM_3798 https://fairsharing.org/search?recordType=terminology_artefact)  using tools like [Zooma](https://www.ebi.ac.uk/spot/zooma/), can be found in Section 7.7.3.3. of [this recipe](https://w3id.org/faircookbook/FCB023)

### Exemplar Bioactivity datasets

[SARS CoV2 phenotypic assay from Caco2 cell line](https://www.ebi.ac.uk/chembl/assay_report_card/CHEMBL4303806/)

The present dataset is a subset of [IMI CARE](https://www.imi.europa.eu/projects-results/project-factsheets/care) dataset with compounds tested on the Caco-2 cell line. The dataset can be downloaded and, besides structural informat (URL_TO_INSERT_TERM_3799 https://fairsharing.org/search?recordType=model_and_format) ion, it will contain readout numbers for activity (e.g. either `percentage of cellular cytopathic inhibition at a given concentration` or corresponding extracted `dose-response IC50 `(Half-maximal inhibitory concentration)).

> Recommendations above are based on ChEMBL (URL_TO_INSERT_RECORD_3802 https://fairsharing.org/FAIRsharing.m3jtpg)  ontology (URL_TO_INSERT_TERM_3800 https://fairsharing.org/search?recordType=terminology_artefact)  requirements. The US counterpart to ChEMBL (URL_TO_INSERT_RECORD_3803 https://fairsharing.org/FAIRsharing.m3jtpg) , the  PubChem (URL_TO_INSERT_RECORD_3804 https://fairsharing.org/FAIRsharing.qt3w7z)  data bank have different ontology (URL_TO_INSERT_TERM_3801 https://fairsharing.org/search?recordType=terminology_artefact)  requirements for upload but provide a wizard-based upload process described in [this blog](https://pubchemblog.ncbi.nlm.nih.gov/tag/pubchem-upload/)

## Glossary
|Term|Definition|
|--|--|
|Experiment|Bioc (URL_TO_INSERT_RECORD_3805 https://fairsharing.org/FAIRsharing.81ettx) hamical Assay, Cellular Activity Assay, Cellular Toxicity Assay|
|Readout|Quantitive measurements of a biophysical event followed by assay (e.g. change in fluorescence)|
|EC50|Half maximal Effective Concentration|
|IC50|Half maximal Inhibition Concentration|
|AC50|Half maximal Activation Concentration|
|CC50|Half maximal Cytotoxic Concentration|

### What to read next?
- [InChI and SMILES identifiers for chemical structures](https://w3id.org/faircookbook/FCB007)
- [ChEMBL interface documentation](https://chembl.gitbook.io/chembl-interface-documentation/)



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

