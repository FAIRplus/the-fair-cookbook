# ND4BB dataset FAIRification recipe

__Version:__ 2, this recipe is extracted from [Version 1](https://docs.google.com/document/d/1LOQAkDZY91Y-5aFCDSlwP-PUeufFavx4Jprnbnl1Hi4/edit)


## Ingredients

* Raw Data: [AMR Compounds Database](https://www.dsf.unica.it/translocation/abdb/)

* Metadata Model

* Vocabularies and Terminologies 

* Data Format:

	* Excel spreadsheet
	
<table>
  <tr>
   <td>PropertyGroup
   </td>
   <td>Property
   </td>
   <td>Value
   </td>
  </tr>
</table>

* Tools and  Software:

	* Data curation tools: Excel, JAVA
	* FAIRification pipeline tools: KNIME workflow
	* Ontology recommender: ZOOMA, NCBO
	* FAIR assessment: [RDA indicator V0.03](https://docs.google.com/spreadsheets/d/1zFcmllpD0loX_yi9NE56vFxbH_RaW-Z1/edit?dls=true#gid=1320380260)


    		


## Objectives

The current AMR dataset is stored in a local webpage at UNICA. We make the AMR data more accessible by extracting the data to a public repository using machine readable format. Also generic improvement of the FAIR parameters.


## Step by Step Process


### Dataset description

The AMR database consists of several nested static HTML pages. The information is well structured, results are mainly quantitative numeric data, and for all compounds a complete set of data is available. Thus, it should be easily linkable to other public sources (e.g. [PubChem](https://pubchem.ncbi.nlm.nih.gov/)) and a machine-readable data set should be easily created.

To get a good understanding of the AMR dataset, the AMR metadata shall be extracted. The AMR metadata includes four types of metadata: structural metadata, administrative metadata, and descriptive metadata. The structural metadata describes the structure of the dataset, for examples, column names and/or IDs. Administrative metadata contains the author, organization, and other provenance information. The descriptive metadata includes the procedure, usually protocols, in generating the experimental results. The descriptive metadata is always stored in a free-text format without data structure. 

Figure 1 is an example of the simplified schematic workflow of FAIRification, which includes the extraction, transform, annotation, licensing and identifier assigning process. Due to the limit of time, we ere, we focus on the extraction and annotation of structural metadata, the administrative metadata, descriptive metadata will be added in the future.


![alt_text](image_0.png "image_tooltip")


_Figure 1:  Schematic workflow of the general FAIRification pipeline. some steps need repetitions (yellow arrows)._ 


### Data extraction

Data are extracted using a[ KNIME workflow](https://owncloud.lcsb.uni.lu/remote.php/webdav/ND4BB/AMR_DB/AMR_DB_AnnotationProcess/20190122_ANTIMICROBIAL_COMPOUNDS_DATABASE_Cagliari_V4.knwf), which can visualize the data extraction steps, handle complex data extraction workflows and be easily reproduced. 

Figure 2 is a snapshot of the ND4BB website, which is structured into a central part (the blue section) with data and two side columns with additional information. Here, we focus on data extraction from the central part. The central part of the home page consists of a single table with compound class names as table data configured as heading level 3 (\<h3\>, shown in the red box in Figure 3) and compounds as an unsorted list (\<ul\>, shown in the yellow box in Figure 3).  



![alt_text](image_1.jpg "image_tooltip")


_Figure 2: Snapshot of AMR compound database home page. The blue area listed all compound data to be extracted._


![alt_text](image_2.jpg "image_tooltip")


_Figure 3: Snapshot of the AMR compound database home page source code. The red box shows the compound class header. The yellow box lists one compound._

We first identified all websites that contain the project data. The homepage (Figure 2) describes the compound names, the compound class and links to the compound subpage. Such information was generated using the Xpath nodes in the workflow in Figure 4. 

Data structure discrepancy was found in the extraction. In the compound class extraction, unlike the usual compound class structure, which is listed as a table and separated by <td>…</td>, chemical “Oxazolidinones” and “Tetracyclines” uses different data structure. Therefore the extracted XML document was updated before applying further nodes to the XML document. In the subpage link extraction, compound Amikacin and ampicillin have multiple subpages for differently charged molecules. The green boxes in Figure 4 highlighted the discrepancies we found in the original dataset.


![alt_text](image_3.png "image_tooltip")


_Figure 4: Workflow to extract antimicrobial classes and compound with their corresponding subpages_


Links to all content in the sub-page are also extracted. Figure 5 is an example of the subpage of one compound, which consists of table selection with the compound name, a 2D and 3D image of the compound structures, two tables with links to related files and properties and one table with links to external sources. (See the green boxes in Figure 5). External links were excluded from current data extraction.

The complete workflow to extract the data from the compound/charge webpage is provided in [supplementary figure 1](#heading=h.q7ozvs96azbw).


![alt_text](image_4.jpg "image_tooltip")


_Figure 5: Example of one ND4BB raw data_


### Data transform

The data were extracted following the schema to facilitate future data annotation: PropertyGroup – Property – Value where PropertyGroup is the heading of the table, Property is the type of property and Value is the corresponding value of the property which will be not part of the annotation process. If the propert is an image, then the “PropertyGroup” is image, “Property” is “2D/3D image”. (See the red box in Figure 6. For each property, the corresponding values in a controlled vocabulary list are collected into a[ spreadsheet](https://owncloud.lcsb.uni.lu/remote.php/webdav/ND4BB/AMR_DB/AMR_DB_AnnotationProcess/ExtractedMetadata_20190124_NCBOREC_0347.xlsx). Missing values were fixed in this transform as well. 

One limitation of this schema is that Excel does not explicitly describe the relations between the entities (e.g. Property Group and Property). Therefore predicates between concepts cannot be expressed (e.g. Property hasA PropertyGroup). 



<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/ND4BB-raw5.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](image_5.png "image_tooltip")


_Figure 7: Example data set for +3 charged Amikacin _


### Extract and annotate structural metadata

To prepare for the ontology annotation, we first generated lists of different types of attributes, which include “AMRclass”, “AMR compound”, “PropertyGroup”, etc. In each spreadsheet, the values are listed as separate rows for ontology annotation. 

The strings went through additional parsing to improve mapping confidence. Duplicated or missing attributes were removed. Stemming and lemmatization were implemented to map the keyword to its root form to avoid mismatch because of spelling/form variations.  

all the strings were sent through ZOOMA/NCBO API to search for ontology annotation. The ontology annotation results are listed here ([ZOOMA](https://owncloud.lcsb.uni.lu/remote.php/webdav/ND4BB/AMR_DB/AMR_DB_AnnotationProcess/ExtractedMetadata_20190124_TP%2BZOOMA_1019.xlsx), [NCBO](https://owncloud.lcsb.uni.lu/remote.php/webdav/ND4BB/AMR_DB/AMR_DB_AnnotationProcess/ExtractedMetadata_20190124_TP%2BNCBOREC_1021.xlsx)). The ontology annotations were ranked and selected based on its confidence. For strings that didn’t find proper ontology mapping, the original values were kept. The ontology annotation preparation workflow is [here](https://owncloud.lcsb.uni.lu/remote.php/webdav/ND4BB/AMR_DB/AMR_DB_AnnotationProcess/20190122_EBI_ZOOMA_requests_V5.knwf). 

Both ZOOMA and NCBO ontology recommenders returned the nearly same number of annotated terms, also the number searched ontologies for the NCBO Recommender (313) was much higher than the number of searched ontologies for the ZOOMA (11) service. For only few cases the NCBO Recommender showed results (e.g. BAL29880 and MBX2319) were ZOOMA did not find a corresponding ontology. 

One difference between these two ontology mappers is they process special characters (e.g. -_#) and spaces differently. For example, in NCBO, among “ ‘beta-lactamase inhibitors’, ‘beta lactamase inhibitors’ and ‘betalactamase inhibitors’ only the ontology annotation of the first item was found. While ZOOMA returned ontology annotation results for all three descriptions. Another example would be Aminonucleosides, Aminonucleoside, Amino nucleoside. While NCBO Recommender found no result, ZOOMA found at least a result for the terms ‘Aminonucleoside’, ‘Amino nucleoside’. This proves the necessity of running stemming or lemmatizing prior to ontology mapping service.

Provenance metadata about the ontology annotation pipeline implementation are stored here in the same file. 


## Results

Both generated files ‘ExtractedMetadata_20190124_ZOOMA_0329.xlsx’ and ‘ExtractedMetadata_20190124_NCBOREC_0347.xlsx’ show nearly same number of annotated terms, also the number searched ontologies for the NCBO Recommender (313) was much higher than the number of searched ontologies for the ZOOMA (11) service. For only few cases the NCBO Recommender showed results (e.g. BAL29880 and MBX2319) were ZOOMA did not find a corresponding ontology. 

The proposed workflow is insufficient to extract adequate and consistent semantic annotations for the structural metadata. In addition the retrieved links do not reflect the used version of the ontology. 


## FAIR assessment

The FAIRness of the ND4BB was also assessed based on the [RDA indicators (v0.03)](https://docs.google.com/spreadsheets/d/1zFcmllpD0loX_yi9NE56vFxbH_RaW-Z1/edit#gid=1320380260). Although there are a few indicators that are not applicable to the ND4BB dataset because of data type limitations, and some indicators are too ambiguous to provide a objective assessment. We got different data curators evaluating the FAIRness seperately and compared and discussed the conflicting assessment. In general, the FAIRness score against RDA FAIR indicator is 36%, of which the mandatory indicator score is 47% and the recommended indicator score is 32%. 


## Future plan


1. Extract administrative metadata, provenance information, e.g. owner, date of creation
2. Add license to data set
3. Store data (=experimental results) together with administrative, structural, and descriptive metadata in a repository
4. Add PID to data set (=digital object)
5. Add metadata together with PID to a public catalog
6. Add metrics according to CMMI and add to the public catalog
7. Add checksums for all files for QC and integrity checks
8. Expand the ontology annotation to all terms


## Summary

The AMR dataset was provided as a first example as it was immediately available. A generic FAIRification workflow was also provided. We reviewed the workflow and derived general principles for the cookbook. However (as for the principles we learnt) the lack of a context for the data, and of goals for the FAIRification process made the actual action of FAIRification not valuable.

As a result or our work on the AMR dataset, we  identified useful general principles, including the need for license, availability of the data, the importance of context (e.g.: what ontologies to map to) and other details included in our report.

We also identified key FAIRification steps in the proposed process, some of which non obvious (e.g.: capture modifications done to ingest data). On this basis we started to sketch a generic workflow. 

Overall this dataset has been very useful to start our overall process and team activities.


## Supplementary information


![alt_text](image_6.png "image_tooltip")

_Supplement figure 1: _Workflow to extract the data from compound/charge webpage_