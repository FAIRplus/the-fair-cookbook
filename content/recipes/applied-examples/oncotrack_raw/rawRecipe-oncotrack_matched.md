(fcb-fairify-examples-oncotrack)=
# Oncotrack - observational clinical cohort datasets


````{panels_fairplus}
:identifier_text: FCB044
:identifier_link: http://w3id.org/faircookbook/FCB044
:difficulty_level: 4
:recipe_type: applied_example
:reading_time_minutes: 10
:intended_audience: data_manager, data_curator, ontologist
:maturity_level: 2
:maturity_indicator: 1, 2
:has_executable_code: nope
:recipe_name: Readying IMI Oncotrack - clinical cohort datasets for deposition to EBI Biosamples
```` 


## Ingredients


```{tabbed} Data Standards
*   Metadata model
    *   [Oncotrack cohort metadata](https://drive.google.com/open?id=13xmazrUUWaCZVooL8d3HXZg7URfVlupM)
    *   [Oncotrack drug sensitivity data](https://drive.google.com/file/d/166IlLr-kZLBPoGLkxEyp7cLw8KFKtN1_/view?usp=sharing) 
    *   [Oncotrack metadata template](https://docs.google.com/document/d/1OXSQsZbw2EEZOZrrXJIaJpsb60Y3-4N4W-wu9LX5oa8/edit?usp=sharing)
*   Vocabularies and terminologies
    *   Pharmaceutical drug names follow the nomenclature of [ChEBI](https://www.ebi.ac.uk/chebi/) and [ChEMBL](https://www.ebi.ac.uk/chembl/) database. All drug ontologies are listed [here](https://drive.google.com/open?id=1kYH76-3K3mkz6wfTydFoT_UPf8WP0fe_). 
    *   All abbreviations and acronyms used in OncoTrack cohort metadata are listed in the [OncoTrack public metadata acronym table](https://drive.google.com/open?id=1voD6FGHVyHUgZEHFRfzh_HlTQa7CvW5-MtheGhydDAg).
*   Data format
    *   Input data: Excel
    *   Output data: 
        *   tab-delimited text file
        *   JSON file (JSON schema: [BioSamples databases JSON schema](https://drive.google.com/open?id=1DoyOZ1uMFv0aPpAQUPkf7mS8vAoS6DCY))
```

```{tabbed} Tools and software
*   Tools and software
    *   Metadata extract and transform tool: R (Version 3.6.1)
        *   String parsing: R package stringi_1.4.3, stringr_1.4.0
        *   Excel file Loading: readxl_1.3.1
        *   Data structure transform:plyr_1.8.4  
        *   JSON format parsing: rjson_0.2.20 
    *   JSON schema validator: [Elixir JSON schema validator](https://github.com/elixir-europe/json-schema-validator)
    *   Ontology mapping: [ZOOMA](https://www.ebi.ac.uk/spot/zooma/)
    *   File Integrity check: md5sum (GNU coreutils) 8.28
```




 	 	 	


## Objective

This FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)ification pipeline converts the OncoTrack sample metadata to a structured and consistent data format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format), improves the findability, interoperability, and reusability of the metadata. 
The FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)ified metadata provides an enriched context to other Oncotrack derived datasets {footcite}`pmid26978244`.


## Step-by-Step Process

The FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)ification of Oncotrack metadata includes four steps: 
1) accessing the data
2) metadata extraction, transform and load (ETL) pipeline,
3) data curation and
4) data sharing. (Figure 1)


<!-- ![alt_text](image_0.png "image_tooltip")
_Figure 1: OncoTrack metadata FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)ification pipeline_ -->	

````{dropdown}
:open:
```{figure} image_0.png
---
width: 800px
name: OncoTrack metadata FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)ification pipeline.
alt: OncoTrack metadata FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)ification pipeline.
---
OncoTrack metadata FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)ification pipeline.
```
````

### Data Description

The OncoTrack colorectal carcinoma (CRC) biobank includes patient tumour samples, patient derived xenograft model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s (PDX) and patient-derived 3D  cell model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s (PDO(URL_TO_INSERT_RECORD http://mdb.bio.titech.ac.jp/pdo)) from 106 patients. Multi-omics experiments and various drug sensitivity studies have been performed on the CRC biobank.

The[ OncoTrack](http://www.oncotrack.eu/home/index.html) sample metadata includes published sample metadata, drug sensitivity experiment results, and private cohort informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion. Here, we focus on the FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)ification of the public sample metadata. Drug sensitivity, as an important property of the patient-derived 3D cell culture model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s, is also included. The metadata is published on[ Schütte, et al](https://www.nature.com/articles/ncomms14262#Sec54). Annotations to the metadata are stored in[FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)plus OwnCloud](https://owncloud.lcsb.uni.lu/apps/files/?dir=/ONCOTRACK&fileid=10738223) with controlled access.

The original cohort metadata is stored in an Excel spreadsheet. Figure 2 is an example of the cohort metadata. Each sample is listed as a separate row in the spreadsheet. Sample attributes are listed in columns. The sample names follow the[ OncoTrack identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) system guidelines](https://drive.google.com/file/d/1qTQ4cYsmD3AN9XYRxpwayOerc78LUzq6/view?usp=sharing), which consist of patient ID, tumour type, and patient-derived cell culture model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ID. For example, Sample _“150_MET1_XEN2”_ represents _“The second xenograft culture of the first metastatic tumour sample in Patient 150.”_ 


<!-- ![alt_text](image_1.png "image_tooltip")
_Figure 2: Example of OncoTrack public cohort metadata -->_

````{dropdown}
:open:
```{figure} image_1.png
---
width: 800px
name: Example of OncoTrack public cohort metadata.
alt: Example of OncoTrack public cohort metadata.
---
Example of OncoTrack public cohort metadata.
```
````


The drug sensitivity data is also provided in Excel spreadsheets. Seventeen drugs are tested on patient-derived organoid(PDO(URL_TO_INSERT_RECORD http://mdb.bio.titech.ac.jp/pdo)) and patient-derived xenografts(PDX) model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s in five sets of experiments. Different sets have their unique measurement methods, drug response scales. For example, in _Sheet 1: PDO(URL_TO_INSERT_RECORD http://mdb.bio.titech.ac.jp/pdo) drug response_ experiment, IC50 value is measured and defines the drug _response category_ (Figure 3a). In _Sheet 2: PDX drug response test_, the _response evaluation criteria in solid tumours (**RECIST**)_ scales defines the _drug response category_ (Figure 3b). In both examples, the _drug response category_ is marked by colour codes.


<!-- ![alt_text](image_2.png "image_tooltip") -->

````{dropdown}
:open:
```{figure} image_2.png
---
width: 800px
name: Example of OncoTrack.
alt: .
---
```
````

<!-- ![alt_text](image_3.png "image_tooltip")
_Figure 3: Example of Oncotrack drug response data_ -->

````{dropdown}
:open:
```{figure} image_3.png
---
width: 900px
name: Example of Oncotrack drug response data.
alt: Example of Oncotrack drug response data.
---
Example of Oncotrack drug response data.
```
````

### Metadata ETL pipeline

The frequent use of acronyms and abbreviations in Oncotrack metadata and the inconsistent metadata structures make it difficult to interpret and reuse. To extract and annotate the metadata, the data owner and data curators first agreed on the structure and content of the FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)ified metadata, as well as the principles in metadata extraction.

Firstly, all missing values in the metadata shall be marked with _NAs_ instead of being removed, to facilitate cross-sample comparisons. Secondly, all acronyms and abbreviations shall be expanded to their full forms to avoid ambiguity. Thirdl(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/RDL)y, the sample attribute values shall correspond to ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) terms if applicable. The final sample metadata template can be found[ here](https://docs.google.com/document/d/1OXSQsZbw2EEZOZrrXJIaJpsb60Y3-4N4W-wu9LX5oa8/edit).

The cohort metadata was converted to a[ tab-delimited table](https://docs.google.com/document/d/1pBjRe7rWO4xsUIVecIgxOm_SJaMWeWf8KBrsDTDVAmg/edit?usp=sharing), of which each row represents one sample, and each column represents one sample attribute. 144 samples from 106 patients were extracted, including 35 organoids and 59 xenografts. Tumour type and sample origin informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion was retrieved from the sample name. The disease name _“colon and rectal cancer”_ was replaced with ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) term[ “Colorectal cancer”](http://www.ebi.ac.uk/efo(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/)/EFO_0005842). Figure 4 is an example of the extracted cohort metadata.


<!-- ![alt_text](image_4.png "image_tooltip")
_Figure 4: Example of the extracted cohort metadata_ -->

````{dropdown}
:open:
```{figure} image_4.png
---
width: 800px
name: Example of the extracted cohort metadata.
alt: Example of the extracted cohort metadata.
---
Example of the extracted cohort metadata.
```
````

Drug sensitivity data were also extracted from the original spreadsheets. Each drug test per sample was listed as one entry. To coordinate different measurement approaches and response category scales, all drug sensitivity data were converted to a unified representation. All the measurement results were stored in Attribute _“Value”_, the drug response categorizes criteria were stored in Attribute _“Unit”,_ and the _drug response category_ was recalculated and stored in Attribute _“Response”._ Figure 5 is an example of the extracted drug sensitivity data. 1829 drug tests were extracted in total. The drug response summary is [here](https://drive.google.com/file/d/1BNkuLtKUsqoAPJqDKqdhj2xYAhuxhQkf/view?usp=sharing). 


<!-- ![alt_text](image_5.png "image_tooltip")
_Figure 5: Example of extracted drug sensitivity data_	 -->

````{dropdown}
:open:
```{figure} image_5.png
---
width: 800px
name: Example of extracted drug sensitivity data.
alt: Example of extracted drug sensitivity data.
---
Example of extracted drug sensitivity data.
```
````

 	 	

To associate drug sensitivity data with related sample cohort metadata and convert them to machine-readable format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s, we combined cohort metadata and drug sensitivity data to JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) files. The [BioSample(URL_TO_INSERT_RECORD https://www.ncbi.nlm.nih.gov/biosample)s JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) schema](https://drive.google.com/file/d/1DoyOZ1uMFv0aPpAQUPkf7mS8vAoS6DCY/view) was used as the sample metadata template, allowing direct submissions to[ BioSample(URL_TO_INSERT_RECORD https://www.ncbi.nlm.nih.gov/biosample)s database](https://www.ebi.ac.uk/biosamples(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/biosamples/)/) and can be easily converted to other format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s, like XML(URL_TO_INSERT_RECORD https://www.w3.org/TR/xml/), spreadsheets, etc.

The BioSample(URL_TO_INSERT_RECORD https://www.ncbi.nlm.nih.gov/biosample)s JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) schema includes four blocks, submission metadata (e.g. submission domain, release date, update date), administrative metadata, (e.g. contacts, affiliations), general sample metadata (sample names, species, etc) and sample characteristics. All informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion is stored in key: value pairs. In sample characteristics, only data with flatten structure is accepted. 

All cohort metadata and drug sensitivity data of each sample were combined into separate JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) files, named after the original sample identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema).

BioSample(URL_TO_INSERT_RECORD https://www.ncbi.nlm.nih.gov/biosample)s JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) schema only supports string(URL_TO_INSERT_RECORD https://string-db.org/)s as value types. Therefore, complex data, for example, drug sensitivity data, need additional parsing to fit into the schema. For each drug response experiments, four descriptive attributes were “_Drug Name_”, “_Value_”, “_Unit_” and “_Drug response level_” provided. To convert them to key: value pairs, the “_drug name_” was kept as part of the attribute key. “Value”, “Unit” and “Drug response level” informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion were joint into one string(URL_TO_INSERT_RECORD https://string-db.org/). For example, the drug response of _regorafenib in Sample 302_MET_CELL_XEN_ (Figure 6) was converted to _“Drug response(regorafenib): Minor response, IC50(µM) = 29”._ For drugs that were tested more than once, a replicate ID was added to the attribute key.



Administrative informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion was also added to each JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) object, including institute, project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project) name, and project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project) website. Contact details were not provided, which needs further confirmation from the data owners.

All transformed metadata was validated against BioSample(URL_TO_INSERT_RECORD https://www.ncbi.nlm.nih.gov/biosample)s schema with the[ Elixir JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) validator](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/elixir-europe/json-schema-validator), which is based on [AJV](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/ajv-validator/ajv) with additional life science keyword validation.


### Data curation

Data curation was implemented to increase the findability of the extracted metadata, including ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping, encoding, and fixing data discrepancy.


#### Drug name ontology

Different types of drug names were used in the original drug sensitivity data, including generic names, trade names and their chemical names. Some in-development drugs were labelled by their company code. All drug names were map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ped(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) to a standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)ized nomenclature, together with ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) annotations, to increase the findability of drug response results.

The popular drug nomenclatures include International Nonproprietary Names (INN(URL_TO_INSERT_RECORD http://braininfo.org/Nnont.aspx)s), [DrugBank](https://www.drugbank.ca(URL_TO_INSERT_RECORD http://www.drugbank.ca/)/) names, Chemical Entities of Biological Interest(URL_TO_INSERT_RECORD http://www.ebi.ac.uk/chebi/) ([ChEBI](https://www.ebi.ac.uk/chebi(URL_TO_INSERT_RECORD http://www.ebi.ac.uk/chebi/)/)) database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database) identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s, and bioactivity database,[ChEMBL](https://www.ebi.ac.uk/chembl(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/chembl)/) identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s. Among them, the ChEBI(URL_TO_INSERT_RECORD http://www.ebi.ac.uk/chebi/) database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database) covers most drugs in OncoTrack, is easy to access and has been curated as an ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) source in Open Biomedical Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) (OBO(URL_TO_INSERT_RECORD http://www.obofoundry.org/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059)). Hence, the drug names in ChEBI(URL_TO_INSERT_RECORD http://www.ebi.ac.uk/chebi/) were selected as the primary drug names. For drugs or active compounds that were not included in ChEBI(URL_TO_INSERT_RECORD http://www.ebi.ac.uk/chebi/), their names in ChEMB(URL_TO_INSERT_RECORD http://www.Metabase.net)L(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/chembl)(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/chembl) were selected.

The OncoTrack drug names were map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ped(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) to corresponding ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) terms in ChEBI(URL_TO_INSERT_RECORD http://www.ebi.ac.uk/chebi/) and ChEMB(URL_TO_INSERT_RECORD http://www.Metabase.net)L(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/chembl)(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/chembl) using ZOOMA(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/gxd/ma_ontology/)(URL_TO_INSERT_RECORD http://omabrowser.org/oma/about/). ZOOMA(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/gxd/ma_ontology/)(URL_TO_INSERT_RECORD http://omabrowser.org/oma/about/) is an ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) annotation tool, which map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)s free texts to ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) terms based on a curated repository (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository) of annotation knowledge. In OncoTrack drug name map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping, only ChEBI(URL_TO_INSERT_RECORD http://www.ebi.ac.uk/chebi/) and ChEMB(URL_TO_INSERT_RECORD http://www.Metabase.net)L(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/chembl)(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/chembl) were selected as ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) sources, and all curation sources except GWAS(URL_TO_INSERT_RECORD https://h3africa.org/) were selected to improve the coverage and increase the map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping confidence. Figure 6 is an example of the ZOOMA(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/gxd/ma_ontology/)(URL_TO_INSERT_RECORD http://omabrowser.org/oma/about/) map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping output. Only entries with high map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping confidences were selected. The other entries were map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ped(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) manually to terms in ChEBI(URL_TO_INSERT_RECORD http://www.ebi.ac.uk/chebi/). Among all 17 drugs, Drug “BI 860585” didn’t map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map) to any pharmaceutical terms, so the original name was kept. The complete map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping results are listed [here](https://drive.google.com/open?id=1kYH76-3K3mkz6wfTydFoT_UPf8WP0fe_). 

<!-- 
![alt_text](image_6.jpg "image_tooltip")
_Figure 6: Example of  ZOOMA(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/gxd/ma_ontology/)(URL_TO_INSERT_RECORD http://omabrowser.org/oma/about/) ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping results_
 -->

````{dropdown}
:open:
```{figure} image_6.jpg
---
width: 600px
name: Example of ZOOMA(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/gxd/ma_ontology/)(URL_TO_INSERT_RECORD http://omabrowser.org/oma/about/) ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping results.
alt: Example of ZOOMA(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/gxd/ma_ontology/)(URL_TO_INSERT_RECORD http://omabrowser.org/oma/about/) ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping results.
---
Example of ZOOMA(URL_TO_INSERT_RECORD http://www.informatics.jax.org/vocab/gxd/ma_ontology/)(URL_TO_INSERT_RECORD http://omabrowser.org/oma/about/) ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) map(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#map)ping results.
```
````

#### Data discrepancy

Discrepancy and errors were found in the published metadata. In the cohort metadata, the tumour purity of sample “150_MET1”, “208_MET1”, “209_MET2” and “209_T2” were wrongly labelled. We compared these entries with the original records in the OncoTrack database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database) and found discrepancies between the published metadata and Oncotrack database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database) records. Those values were removed from extracted data until further confirmation from the data owner. The updated cohort metadata is [here](https://drive.google.com/open?id=13xmazrUUWaCZVooL8d3HXZg7URfVlupM).  In drug response metadata extraction, we recalculated the drug response level and found one error in _cetuximab_ drug response level. The corrected drug response data is [here](https://drive.google.com/open?id=166IlLr-kZLBPoGLkxEyp7cLw8KFKtN1_). 


#### Data encoding

Special letters were converted to ASCII encoding to avoid [mojibake](https://en.wikipedia.org/wiki/Mojibake). All the “µM”s in drug sensitivity data were converted to “microM”.


### Data sharing

The curated metadata, both in summary spreadsheet format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) and JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format), were uploaded to Owncloud and Google drive. The OncoTrack sample metadata can be submitted directly to the EMB(URL_TO_INSERT_RECORD http://www.Metabase.net)L BioSample(URL_TO_INSERT_RECORD https://www.ncbi.nlm.nih.gov/biosample)s database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database) upon request. Supplementary figure 1 is an example of how the metadata will be displayed in the BioSample(URL_TO_INSERT_RECORD https://www.ncbi.nlm.nih.gov/biosample)s database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database). Checksums were also provided to verify metadata integrity. 


## Summary

The public cohort metadata and drug sensitivity data were converted to tab-delimited summary files. For each sample, corresponding cohort metadata and drug data were combined to a separate JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) file, which can be later loaded to EBI BioSample(URL_TO_INSERT_RECORD https://www.ncbi.nlm.nih.gov/biosample)s database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database). Metadata were translated to consistent terminologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) and linked with ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) terms.


## Future plan

The current ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) annotation is limited to drug names. Other ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) can be added upon request. More detailed administrative metadata will be added once getting permission from the OncoTrack consortium. The license will be added according to the drug release policy (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Policy).



## Supplementary materials
````{dropdown} **Supplementary materials**
Script 1: [Extract_cohort_metadata.R](https://drive.google.com/file/d/1bbMMKZnygZ8kccdnSj2R_BRLDhd0vAS-/view?usp=sharing)

Script 2: [Extract_drugResponse_metadata.R](https://drive.google.com/open?id=1eNxdNFGN7GAw7Z0Cmk0k2BJiMMZ7wbel)

Script 3: [Transform to JSON.R](https://drive.google.com/file/d/18Ik3RryhWVFq9_2IIy6k8N-qpnP9Wgm3/view?usp=sharing)

Supplementary figure 1: [Example of Sample 150-MET1-XEN2 in BioSamples database](https://drive.google.com/open?id=1ALOwGwB2RpWksH4TuGeye8qEnUm0ULVH)
````


## References
`````{dropdown} **References**
```{footbibliography}
```
`````



## Authors

````{authors_fairplus}
Fuqi: Writing - Original Draft
````



## License

````{license_fairplus}
CC-BY-4.0
````

