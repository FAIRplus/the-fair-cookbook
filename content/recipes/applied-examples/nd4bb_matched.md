(fcb-nd4bb)=
# ND4BB - chemical activities datasets

<!-- 
TO (URL_TO_INSERT_RECORD_1274 https://fairsharing.org/FAIRsharing.w69t6r) DO: check whether all files can be put on Zenodo (URL_TO_INSERT_RECORD_1275 https://fairsharing.org/FAIRsharing.wy4egf)  (URL_TO_INSERT_RECORD_1276 https://fairsharing.org/FAIRsharing.wy4egf) 
TO (URL_TO_INSERT_RECORD_1277 https://fairsharing.org/FAIRsharing.w69t6r) DO: clarify authors
-->

````{panels_fairplus}
:identifier_text: FCB043
:identifier_link: https://w3id.org/faircookbook/FCB043
:difficulty_level: 4
:recipe_type: applied_example
:recipe_name: ND4BB - chemical activities datasets
:reading_time_minutes: 20
:intended_audience: data_manager, data_curator
:maturity_level: 2
:maturity_indicator: 1, 2
:has_executable_code: nope
```` 

````{admonition} Editor's summary

The authors of this recipe start with data spread over well structured web pages. 

They use a [KNIME](https://www.knime.com/) workflow to extract the data into an Excel spreadsheet. 

The authors encounter inconsistencies in the web pages, and fix them. 

In a separate step, the collected strings were sent through two different ontology annotation APIs. The results are compared.

This is one of the first recipes within the FAIRplus project, and served as a pilot to develop a structured FAIRification process.
````

## Ingredients

* Raw Data: [AMR Compounds Database (URL_TO_INSERT_TERM_1278 https://fairsharing.org/search?fairsharingRegistry=Database) ](https://www.dsf.unica.it/translocation/abdb/)

* Metadata Model (URL_TO_INSERT_TERM_1279 https://fairsharing.org/search?recordType=model_and_format) 

* Vocabularies and Terminologies (URL_TO_INSERT_TERM_1280 https://fairsharing.org/search?recordType=terminology_artefact)  

* Data Format (URL_TO_INSERT_TERM_1281 https://fairsharing.org/search?recordType=model_and_format) :
	* Excel spreadsheet

* Tools and Software:
	* Data curation tools: Excel, Java
	* FAIR (URL_TO_INSERT_RECORD_1282 https://fairsharing.org/FAIRsharing.WWI10U) ification pipeline tools: KNIME workflow
	* Ontology (URL_TO_INSERT_TERM_1283 https://fairsharing.org/search?recordType=terminology_artefact)  recommender: [ZOOMA](https://www.ebi.ac.uk/spot/zooma/), [NCBO (URL_TO_INSERT_RECORD_1285 https://fairsharing.org/FAIRsharing.cbz72b)  (URL_TO_INSERT_RECORD_1286 https://fairsharing.org/FAIRsharing.y2dt83) ](https://bioportal.bioontology.org (URL_TO_INSERT_RECORD_1284 https://fairsharing.org/FAIRsharing.4m97ah) /)
	* FAIR (URL_TO_INSERT_RECORD_1288 https://fairsharing.org/FAIRsharing.WWI10U)  assessment: RDA (URL_TO_INSERT_RECORD_1287 https://fairsharing.org/FAIRsharing.2g5kcb)  indicators


## Objectives

The current AMR dataset is stored in a local webpage at UNIC (URL_TO_INSERT_RECORD_1291 https://fairsharing.org/FAIRsharing.s6zfkg) A. We make the AMR data more accessible by extracting the data into a public repository (URL_TO_INSERT_TERM_1289 https://fairsharing.org/search?recordType=repository)  using machine readable format (URL_TO_INSERT_TERM_1290 https://fairsharing.org/search?recordType=model_and_format) , as well as improvement of some FAIR (URL_TO_INSERT_RECORD_1292 https://fairsharing.org/FAIRsharing.WWI10U)  parameters.


## Step by Step Process


### Dataset description

The AMR database (URL_TO_INSERT_TERM_1293 https://fairsharing.org/search?fairsharingRegistry=Database)  consists of several nested static HTML (URL_TO_INSERT_RECORD_1295 https://fairsharing.org/FAIRsharing.YugnuL)  pages. The informat (URL_TO_INSERT_TERM_1294 https://fairsharing.org/search?recordType=model_and_format) ion is well structured, results are mainly quantitative numeric data, and for all compounds a complete set of data is available. Thus, it should be easily linkable to other public sources (e.g. [PubChem](https://pubchem.ncbi.nlm.nih.gov (URL_TO_INSERT_RECORD_1296 https://fairsharing.org/FAIRsharing.qt3w7z) /)) and a machine-readable data set should be easily created.

To get a good understanding of the AMR dataset, the AMR metadata shall be extracted. The AMR metadata includes three types of metadata: structural metadata, administrative metadata, and descriptive metadata. The structural metadata describes the structure of the dataset, for examples, column names and/or IDs. Administrative metadata contains the author, organization, and other provenance informat (URL_TO_INSERT_TERM_1297 https://fairsharing.org/search?recordType=model_and_format) ion. The descriptive metadata includes the procedure, usually protocols, in generating the experimental results (URL_TO_INSERT_RECORD_1299 https://fairsharing.org/FAIRsharing.QlUiql) . The descriptive metadata is always stored in a free-text format (URL_TO_INSERT_TERM_1298 https://fairsharing.org/search?recordType=model_and_format)  without data structure. 

{numref}`nd4bb-figure1` is an example of the simplified schematic workflow of FAIR (URL_TO_INSERT_RECORD_1302 https://fairsharing.org/FAIRsharing.WWI10U) ification, which includes the extraction, the transformat (URL_TO_INSERT_TERM_1300 https://fairsharing.org/search?recordType=model_and_format) ion, the annotation, the licensing and the identifier (URL_TO_INSERT_TERM_1301 https://fairsharing.org/search?recordType=identifier_schema)  assigning process. Due to time constraint, we focussed on the extraction and annotation of structural metadata. The administrative and the descriptive metadata will be added in the future.

````{dropdown}
:open:
```{figure} nd4bb.md-figure1.png
---
width: 650px
name: nd4bb-figure1
alt: Schematic workflow of the general FAIR (URL_TO_INSERT_RECORD_1303 https://fairsharing.org/FAIRsharing.WWI10U) ification pipeline. Some steps need repetitions (yellow arrows).
---
Schematic workflow of the general FAIR (URL_TO_INSERT_RECORD_1304 https://fairsharing.org/FAIRsharing.WWI10U) ification pipeline. Some steps need repetitions (yellow arrows).
```
````


### Data extraction

Data are extracted using a [KNIME workflow provided here](https://owncloud.lcsb.uni.lu/remote.php/webdav/ND4BB/AMR_DB/AMR_DB_AnnotationProcess/20190122_ANTIMICROBIAL_COMPOUNDS_DATABASE_Cagliari_V4.knwf), with which we can visualize the data extraction steps, handle (URL_TO_INSERT_RECORD_1305 https://fairsharing.org/FAIRsharing.0b7e54)  complex data extraction workflows and be easily reproduced. 

{numref}`nd4bb-figure2` is a screenshot of the ND4BB website, which is structured into a central part (the blue section) with data and two side columns with additional informat (URL_TO_INSERT_TERM_1306 https://fairsharing.org/search?recordType=model_and_format) ion. Here, we focus on data extraction from the central part. The central part of the home page consists of a single table with compound class names as table data configured as HTML (URL_TO_INSERT_RECORD_1307 https://fairsharing.org/FAIRsharing.YugnuL)  heading level 3 (\<h3\>, shown in the red box in {numref}`nd4bb-figure3`) and compounds as an unordered list (\<ul\>, shown in the yellow box in {numref}`nd4bb-figure3`).

````{dropdown}
:open:
```{figure} nd4bb.md-figure2.jpg
---
width: 750px
name: nd4bb-figure2
alt: Snapshot of AMR compound database (URL_TO_INSERT_TERM_1308 https://fairsharing.org/search?fairsharingRegistry=Database)  home page. The blue area listed all compound data to be extracted.
---
Snapshot of AMR compound database (URL_TO_INSERT_TERM_1309 https://fairsharing.org/search?fairsharingRegistry=Database)  home page. The blue area listed all compound data to be extracted.
```
````

````{dropdown}
:open:
```{figure} nd4bb.md-figure3.jpg
---
width: 450px
name: nd4bb-figure3
alt: Snapshot of the AMR compound database (URL_TO_INSERT_TERM_1310 https://fairsharing.org/search?fairsharingRegistry=Database)  home page source code. The red box shows the compound class header. The yellow box lists one compound.
---
Snapshot of the AMR compound database (URL_TO_INSERT_TERM_1311 https://fairsharing.org/search?fairsharingRegistry=Database)  home page source code. The red box shows the compound class header. The yellow box lists one compound.
```
````


We first identified all websites that contain the project (URL_TO_INSERT_TERM_1312 https://fairsharing.org/search?recordType=project)  data. The homepage ({numref}`nd4bb-figure2`) describes the compound name, the compound class and links to the compound subpage. Such informat (URL_TO_INSERT_TERM_1313 https://fairsharing.org/search?recordType=model_and_format) ion was generated using the Xpath nodes in the workflow in {numref}`nd4bb-figure4`. 

Data structure discrepancy was found in the extraction. In the compound class extraction, unlike the usual compound class structure, which is listed as a table and separated by HTML (URL_TO_INSERT_RECORD_1316 https://fairsharing.org/FAIRsharing.YugnuL)  \<td\>…\</td\>, chemical “Oxazolidinones” and “Tetracyclines” use different data structure. Therefore the extracted XML (URL_TO_INSERT_RECORD_1314 https://fairsharing.org/FAIRsharing.b5cc91)  document was updated before applying further nodes to the XML (URL_TO_INSERT_RECORD_1315 https://fairsharing.org/FAIRsharing.b5cc91)  document. In the subpage link extraction, compound Amikacin and ampicillin have multiple subpages for differently charged molecules. 

````{dropdown}
:open:
```{figure} nd4bb.md-figure4.png
---
width: 650px
name: nd4bb-figure4
alt: Workflow to extract antimicrobial classes and compounds with their corresponding subpages.
---
Workflow to extract antimicrobial classes and compounds with their corresponding subpages.
```
````

Links to all content in the sub-page are also extracted. {numref}`nd4bb-figure5` is an example of the subpage of one compound, which consists of table section with the compound name, a 2D and 3D image of the compound structures, two tables with links to related files and properties and one table with links to external sources. External links were excluded from current data extraction.

The complete workflow to extract the data from the compound/charge webpage is depicted in {numref}`nd4bb-figure7`.

````{dropdown}
:open:
```{figure} nd4bb.md-figure5.jpg
---
width: 550px
name: nd4bb-figure5
alt: Example of one ND4BB raw data.
---
Example of one ND4BB raw data. Marked in green boxes are a table section with the compound name, a 2D and 3D image of the compound structures, two tables with links to related files and properties and one table with links to external sources.
```
````

````{dropdown}
:open:
```{figure} nd4bb.md-figure7.png
---
width: 550px
name: nd4bb-figure7
alt: Workflow to extract the data from compound/charge webpage.
---
Workflow to extract the data from compound/charge webpage.
```
````


### Data transformation

The data were extracted following the following schema to facilitate future data annotation: "PropertyGroup - Property - Value" where PropertyGroup is the heading of the table, Property is the type of property and Value is the corresponding value of the property which will be not part of the annotation process. If the property is an image, then the “PropertyGroup” is image, “Property” is “2D/3D image”. (See the red box in {numref}`nd4bb-figure6`. For each property, the corresponding values in a controlled vocabulary list are collected into a [spreadsheet](https://owncloud.lcsb.uni.lu/remote.php/webdav/ND4BB/AMR_DB/AMR_DB_AnnotationProcess/ExtractedMetadata_20190124_NCBOREC_0347.xlsx). Missing values were fixed in this step as well. 

One limitation of this schema is that Excel does not explicitly describe the relations between the entities (e.g. Property Group and Property). Therefore predicates between concepts cannot be expressed (e.g. Property hasA PropertyGroup). 

````{dropdown}
:open:
```{figure} nd4bb.md-figure6.png
---
width: 650px
name: nd4bb-figure6
alt: Example data set for +3 charged Amikacin.
---
Example data set for +3 charged Amikacin.
```
````


### Extraction and annotation of structural metadata

To prepare for the ontology (URL_TO_INSERT_TERM_1317 https://fairsharing.org/search?recordType=terminology_artefact)  annotation, we first generated lists of different types of attributes, which include “AMRclass”, “AMR compound”, “PropertyGroup”, etc. In each spreadsheet, the values are listed as separate rows for ontology (URL_TO_INSERT_TERM_1318 https://fairsharing.org/search?recordType=terminology_artefact)  annotation. 

The string (URL_TO_INSERT_RECORD_1321 https://fairsharing.org/FAIRsharing.9b7wvk) s went through additional parsing to improve map (URL_TO_INSERT_RECORD_1319 https://fairsharing.org/FAIRsharing.53edcc) ping confidence. Duplicated or missing attributes were removed. Stemming and lemmatization were implemented to map (URL_TO_INSERT_RECORD_1320 https://fairsharing.org/FAIRsharing.53edcc)  the keyword to its root form to avoid mismatch due to spelling or form variations.

All the string (URL_TO_INSERT_RECORD_1333 https://fairsharing.org/FAIRsharing.9b7wvk) s were sent through ZOOMA (URL_TO_INSERT_RECORD_1329 https://fairsharing.org/FAIRsharing.pdwqcr)  (URL_TO_INSERT_RECORD_1331 https://fairsharing.org/FAIRsharing.g3j5qj) /NCBO (URL_TO_INSERT_RECORD_1327 https://fairsharing.org/FAIRsharing.cbz72b)  (URL_TO_INSERT_RECORD_1330 https://fairsharing.org/FAIRsharing.y2dt83)  API to search (URL_TO_INSERT_RECORD_1332 https://fairsharing.org/FAIRsharing.52b22c)  for ontology (URL_TO_INSERT_TERM_1322 https://fairsharing.org/search?recordType=terminology_artefact)  annotation. The ontology (URL_TO_INSERT_TERM_1323 https://fairsharing.org/search?recordType=terminology_artefact)  annotation results are listed here ([result Excel file for querying ZOOMA](https://owncloud.lcsb.uni.lu/remote.php/webdav/ND4BB/AMR_DB/AMR_DB_AnnotationProcess/ExtractedMetadata_20190124_TP%2BZOOMA_1019.xlsx), [result Excel file for querying NCBO](https://owncloud.lcsb.uni.lu/remote.php/webdav/ND4BB/AMR_DB/AMR_DB_AnnotationProcess/ExtractedMetadata_20190124_TP%2BNCBOREC_1021.xlsx)). The ontology (URL_TO_INSERT_TERM_1324 https://fairsharing.org/search?recordType=terminology_artefact)  annotations were ranked and selected based on its confidence. For string (URL_TO_INSERT_RECORD_1334 https://fairsharing.org/FAIRsharing.9b7wvk) s that didn’t find proper ontology (URL_TO_INSERT_TERM_1325 https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD_1328 https://fairsharing.org/FAIRsharing.53edcc) ping, the original values were kept. The ontology (URL_TO_INSERT_TERM_1326 https://fairsharing.org/search?recordType=terminology_artefact)  annotation preparation workflow is [here](https://owncloud.lcsb.uni.lu/remote.php/webdav/ND4BB/AMR_DB/AMR_DB_AnnotationProcess/20190122_EBI_ZOOMA_requests_V5.knwf). 

Both ZOOMA (URL_TO_INSERT_RECORD_1342 https://fairsharing.org/FAIRsharing.pdwqcr)  (URL_TO_INSERT_RECORD_1348 https://fairsharing.org/FAIRsharing.g3j5qj)  and NCBO (URL_TO_INSERT_RECORD_1339 https://fairsharing.org/FAIRsharing.cbz72b)  (URL_TO_INSERT_RECORD_1345 https://fairsharing.org/FAIRsharing.y2dt83)  ontology (URL_TO_INSERT_TERM_1335 https://fairsharing.org/search?recordType=terminology_artefact)  recommenders returned the nearly same number of annotated terms, also the number search (URL_TO_INSERT_RECORD_1351 https://fairsharing.org/FAIRsharing.52b22c) ed ontologies (URL_TO_INSERT_TERM_1337 https://fairsharing.org/search?recordType=terminology_artefact)  for the NCBO (URL_TO_INSERT_RECORD_1340 https://fairsharing.org/FAIRsharing.cbz72b)  (URL_TO_INSERT_RECORD_1346 https://fairsharing.org/FAIRsharing.y2dt83)  Recommender (313) was much higher than the number of search (URL_TO_INSERT_RECORD_1352 https://fairsharing.org/FAIRsharing.52b22c) ed ontologies (URL_TO_INSERT_TERM_1338 https://fairsharing.org/search?recordType=terminology_artefact)  for the ZOOMA (URL_TO_INSERT_RECORD_1343 https://fairsharing.org/FAIRsharing.pdwqcr)  (URL_TO_INSERT_RECORD_1349 https://fairsharing.org/FAIRsharing.g3j5qj)  (11) service. For only a few cases did the NCBO (URL_TO_INSERT_RECORD_1341 https://fairsharing.org/FAIRsharing.cbz72b)  (URL_TO_INSERT_RECORD_1347 https://fairsharing.org/FAIRsharing.y2dt83)  Recommender show results (e.g. BAL29880 and MB (URL_TO_INSERT_RECORD_1353 https://fairsharing.org/FAIRsharing.a1rp4c) X2319) where ZOOMA (URL_TO_INSERT_RECORD_1344 https://fairsharing.org/FAIRsharing.pdwqcr)  (URL_TO_INSERT_RECORD_1350 https://fairsharing.org/FAIRsharing.g3j5qj)  did not find a corresponding ontology (URL_TO_INSERT_TERM_1336 https://fairsharing.org/search?recordType=terminology_artefact) . 

One important difference between these two ontology (URL_TO_INSERT_TERM_1354 https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD_1360 https://fairsharing.org/FAIRsharing.53edcc) pers is that they process special characters (e.g. -_#) and spaces differently. For example, in NCBO (URL_TO_INSERT_RECORD_1358 https://fairsharing.org/FAIRsharing.cbz72b)  (URL_TO_INSERT_RECORD_1364 https://fairsharing.org/FAIRsharing.y2dt83) , among “ ‘beta-lactamase inhibitors’, ‘beta lactamase inhibitors’ and ‘betalactamase inhibitors’ only the ontology (URL_TO_INSERT_TERM_1355 https://fairsharing.org/search?recordType=terminology_artefact)  annotation of the first item was found. While ZOOMA (URL_TO_INSERT_RECORD_1362 https://fairsharing.org/FAIRsharing.pdwqcr)  (URL_TO_INSERT_RECORD_1366 https://fairsharing.org/FAIRsharing.g3j5qj)  returned ontology (URL_TO_INSERT_TERM_1356 https://fairsharing.org/search?recordType=terminology_artefact)  annotation results for all three descriptions. Another example would be Aminonucleosides, Aminonucleoside, Amino nucleoside. While NCBO (URL_TO_INSERT_RECORD_1359 https://fairsharing.org/FAIRsharing.cbz72b)  (URL_TO_INSERT_RECORD_1365 https://fairsharing.org/FAIRsharing.y2dt83)  Recommender found no result, ZOOMA (URL_TO_INSERT_RECORD_1363 https://fairsharing.org/FAIRsharing.pdwqcr)  (URL_TO_INSERT_RECORD_1367 https://fairsharing.org/FAIRsharing.g3j5qj)  found at least a result for the terms ‘Aminonucleoside’, ‘Amino nucleoside’. This proves the necessity of running stemming or lemmatizing prior to ontology (URL_TO_INSERT_TERM_1357 https://fairsharing.org/search?recordType=terminology_artefact)  map (URL_TO_INSERT_RECORD_1361 https://fairsharing.org/FAIRsharing.53edcc) ping service.

Provenance metadata about the ontology (URL_TO_INSERT_TERM_1368 https://fairsharing.org/search?recordType=terminology_artefact)  annotation pipeline implementation are stored here in the same file. 


### Evaluation of the ontology annotation

Both generated files ‘ExtractedMetadata_20190124_ZOOMA (URL_TO_INSERT_RECORD_1375 https://fairsharing.org/FAIRsharing.pdwqcr)  (URL_TO_INSERT_RECORD_1381 https://fairsharing.org/FAIRsharing.g3j5qj) _0329.xlsx’ and ‘ExtractedMetadata_20190124_NCBO (URL_TO_INSERT_RECORD_1372 https://fairsharing.org/FAIRsharing.cbz72b)  (URL_TO_INSERT_RECORD_1378 https://fairsharing.org/FAIRsharing.y2dt83) REC_0347.xlsx’ show nearly same number of annotated terms, also the number search (URL_TO_INSERT_RECORD_1384 https://fairsharing.org/FAIRsharing.52b22c) ed ontologies (URL_TO_INSERT_TERM_1370 https://fairsharing.org/search?recordType=terminology_artefact)  for the NCBO (URL_TO_INSERT_RECORD_1373 https://fairsharing.org/FAIRsharing.cbz72b)  (URL_TO_INSERT_RECORD_1379 https://fairsharing.org/FAIRsharing.y2dt83)  Recommender (313) was much higher than the number of search (URL_TO_INSERT_RECORD_1385 https://fairsharing.org/FAIRsharing.52b22c) ed ontologies (URL_TO_INSERT_TERM_1371 https://fairsharing.org/search?recordType=terminology_artefact)  for the ZOOMA (URL_TO_INSERT_RECORD_1376 https://fairsharing.org/FAIRsharing.pdwqcr)  (URL_TO_INSERT_RECORD_1382 https://fairsharing.org/FAIRsharing.g3j5qj)  (11) service. For only few cases the NCBO (URL_TO_INSERT_RECORD_1374 https://fairsharing.org/FAIRsharing.cbz72b)  (URL_TO_INSERT_RECORD_1380 https://fairsharing.org/FAIRsharing.y2dt83)  Recommender showed results (e.g. BAL29880 and MB (URL_TO_INSERT_RECORD_1386 https://fairsharing.org/FAIRsharing.a1rp4c) X2319) were ZOOMA (URL_TO_INSERT_RECORD_1377 https://fairsharing.org/FAIRsharing.pdwqcr)  (URL_TO_INSERT_RECORD_1383 https://fairsharing.org/FAIRsharing.g3j5qj)  did not find a corresponding ontology (URL_TO_INSERT_TERM_1369 https://fairsharing.org/search?recordType=terminology_artefact) . 

The proposed workflow is insufficient to extract adequate and consistent semantic annotations for the structural metadata. In addition the retrieved links do not reflect the used version of the ontology (URL_TO_INSERT_TERM_1387 https://fairsharing.org/search?recordType=terminology_artefact) . 


## FAIR assessment

We conducted an assessment of the FAIR (URL_TO_INSERT_RECORD_1395 https://fairsharing.org/FAIRsharing.WWI10U) ness of the dataset, with the results stored [here](https://docs.google.com/spreadsheets/d/1zFcmllpD0loX_yi9NE56vFxbH_RaW-Z1/edit#gid=1320380260). Although there are a few indicators that are not applicable to the ND4BB dataset because of data type limitations, and some indicators are too ambiguous to provide a objective assessment. We got different data curators evaluating the FAIR (URL_TO_INSERT_RECORD_1396 https://fairsharing.org/FAIRsharing.WWI10U) ness separately and compared and discussed the conflicting assessment. In general, the FAIR (URL_TO_INSERT_RECORD_1397 https://fairsharing.org/FAIRsharing.WWI10U) ness score (URL_TO_INSERT_RECORD_1388 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_1392 https://fairsharing.org/FAIRsharing.xMmOCL)  against RDA (URL_TO_INSERT_RECORD_1391 https://fairsharing.org/FAIRsharing.2g5kcb)  FAIR (URL_TO_INSERT_RECORD_1398 https://fairsharing.org/FAIRsharing.WWI10U)  indicator is 36%, of which the mandatory indicator score (URL_TO_INSERT_RECORD_1389 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_1393 https://fairsharing.org/FAIRsharing.xMmOCL)  is 47% and the recommended indicator score (URL_TO_INSERT_RECORD_1390 https://fairsharing.org/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD_1394 https://fairsharing.org/FAIRsharing.xMmOCL)  is 32%. 


## Possible next steps

1. Extract administrative metadata, provenance informat (URL_TO_INSERT_TERM_1399 https://fairsharing.org/search?recordType=model_and_format) ion, e.g. owner, date of creation
2. Add a license to data set
3. Store data (=experimental results (URL_TO_INSERT_RECORD_1401 https://fairsharing.org/FAIRsharing.QlUiql) ) together with administrative, structural, and descriptive metadata in a public repository (URL_TO_INSERT_TERM_1400 https://fairsharing.org/search?recordType=repository) 
4. Add PID (URL_TO_INSERT_RECORD_1402 https://fairsharing.org/FAIRsharing.ncgh1j)  to data set (=digital object)
5. Add metadata together with PID (URL_TO_INSERT_RECORD_1403 https://fairsharing.org/FAIRsharing.ncgh1j)  to a public catalog
6. Add metric (URL_TO_INSERT_TERM_1404 https://fairsharing.org/search?recordType=metric) s according to CMMI and add to the public catalog
7. Add checksums for all files for QC and integrity checks
8. Expand the ontology (URL_TO_INSERT_TERM_1405 https://fairsharing.org/search?recordType=terminology_artefact)  annotation to all terms


## Conclusion

The AMR dataset was provided as a first example as it was immediately available. A generic FAIR (URL_TO_INSERT_RECORD_1407 https://fairsharing.org/FAIRsharing.WWI10U) ification workflow was also provided. We reviewed the workflow and derived general principles for the cookbook (URL_TO_INSERT_RECORD_1406 https://fairsharing.org/FAIRsharing.cbz72b) . However (as for the principles we learnt) the lack of a context for the data, and the lack of goals for the FAIR (URL_TO_INSERT_RECORD_1408 https://fairsharing.org/FAIRsharing.WWI10U) ification process made the actual action of FAIR (URL_TO_INSERT_RECORD_1409 https://fairsharing.org/FAIRsharing.WWI10U) ification not valuable.

As a result of our work on the AMR dataset, we identified useful general principles, including the need for license, availability of the data, the importance of context (e.g.: what ontologies (URL_TO_INSERT_TERM_1410 https://fairsharing.org/search?recordType=terminology_artefact)  to map (URL_TO_INSERT_RECORD_1411 https://fairsharing.org/FAIRsharing.53edcc)  to) and other details included in our report.

We also identified key FAIR (URL_TO_INSERT_RECORD_1412 https://fairsharing.org/FAIRsharing.WWI10U) ification steps in the proposed process, some of which are non-obvious (e.g.: capture modifications done to ingest data). On this basis we started to sketch a generic workflow. 

Overall this dataset has been very useful to start our overall process and team activities.


## References
````{dropdown} **References**
````

## Authors
````{authors_fairplus}
Manfred: Writing - Original Draft
````


## License
````{license_fairplus}
CC-BY-4.0
````
