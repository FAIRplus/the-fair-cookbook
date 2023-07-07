# Publication of plant experimental data in generic data repositories

````{panels_fairplus}
:identifier_text: TODO
:identifier_link: TODO
:difficulty_level: 3
:recipe_type: guidance
:reading_time_minutes: 30
:intended_audience:  everyone 
:has_executable_code: nope
:maturity_level: TODO
:maturity_indicator: TODO
:recipe_name: TODO
```` 

## Main Objective
Generic data repositories offer high level metadata, but they are not sufficient to **guarantee interoperability and the possibility to reuse your data later**. They must be completed by the Minimum Information About Plant Phenotyping Experiments ([MIAPPE](https://www.miappe.org/)) international standard. The [Plant Sciences domain page](https://rdmkit.elixir-europe.org/plant_sciences) of the RDMkit describes how MIAPPE is needed and used to clearly document the biological material used as well as the traits, environmental and phenotypical, recorded and computed. Those MIAPPE metadata can be stored using: MIAPPE full template, selected sheets from the full template (recommended since it can be stored as CSV), and ISA Tab archives. The first is the easiest to use, while the latter require a certain level of automation and toolsets.

The main objective of the recipe is to guide plant scientists during the submission of experimental data to generic repositories such as Dataverses, e!Dal-PGP, or Zenodo.
This includes:
1. Dataset creation
2. Addition of mandatory metadata to the dataset
3. Publication of the dataset.

## Summary
This recipe describes best practices for submitting plant experimentation data to generic data repositories (e.g. [e!DAL-PGP](https://edal-pgp.ipk-gatersleben.de/), Dataverses such as [recherche.data.gouv](https://entrepot.recherche.data.gouv.fr/), [dmportal.biodata.pt](https://dmportal.biodata.pt/) and [Jülich DATA](https://data.fz-juelich.de/)).  This will allow data reuse according to [FAIR](https://en.wikipedia.org/wiki/FAIR_data) principles, and especially :
* Ensure visibility and reuse of genetic and phenomic datasets via minimal and sufficient description: data type, organism, list of plant material used, experimental metadata including methods and protocols, etc.
* Maximize data visibility by allowing their indexation in international portals
* Ensure the interoperability of data sets in relation to a coherent identification of plant material used in experiments of various kinds (phenotyping, genotyping, genomics, etc.)

## Graphical overview of the FAIRification Objectives
TODO

## FAIRification Objectives, Inputs and Outputs

|Actions.Objectives.Tasks|Input|Output|
|--- |--- |--- |
|[text annotation](http://edamontology.org/operation_3778)|[MIAPPE](https://fairsharing.org/FAIRsharing.nd9ce9)|[annotated text](http://edamontology.org/data_3779)|

## Table of Data Standards

|Data Formats|Terminologies|Model|
|--- |--- |--- |
|[MIAPPE](https://fairsharing.org/FAIRsharing.nd9ce9)|||

## Table of Software and Tools

|Tool Name|
|--- |
|[Dataverse](https://dataverse.org/)|
|[e!DAL](https://edal.ipk-gatersleben.de/)|

## Step-by-Step process for data submission and publication in Dataverses

````{dropdown} **Example of global dataset management scheme for dataverses**
:open:

```{figure} ../../../images/global_dataset_management_scheme.png
---
width: 700px
name: The global dataset management scheme for Recherche Data Gouv
alt: The global dataset management scheme for Recherche Data Gouv
---
The global dataset management scheme for Recherche Data Gouv ([Source](https://recherche.data.gouv.fr/en/category/9/guide/publication-process-schemas-for-a-dataset))
```
````

### Step 1: Dataset creation

#### Find an appropriate dataverse
You need first to select the appropriate dataverse and/or sub-dataverse for your use case depending on the constraints of your consortium or institute. The guidelines explained below are applicable to all of those dataverse instance. You will find below a non -exhaustive list of dataverse instances.
Also, find the right sub-dataverse for your submission, like the one of the research group or the project you belong to: dataverses can contain dataverses.

* [recherche.data.gouv.fr](https://recherche.data.gouv.fr) (FR)
   * Open to submission from any consortium involving at least one member of a french research institution.
   * Examples: [Data INRAE](https://entrepot.recherche.data.gouv.fr/dataverse/inrae) and [CIRAD](https://entrepot.recherche.data.gouv.fr/dataverse/cirad).

* [Jülich DATA](https://data.fz-juelich.de) (NRW - DE)
   * Open to submission from any research activity done from partners at Forschungszentrum Jülich.
   * Meant for data and software submissions.
   * Maintained by the central library of FZJ.
   * Examples under subject ["Agricultural Sciences"](https://data.fz-juelich.de/dataverse/fzj?q=&fq1=subject_ss%3A%22Agricultural+Sciences%22&fq0=dvObjectType%3A%28dataverses+OR+datasets%29&types=dataverses%3Adatasets).

* [dmportal.biodata.pt](https://dmportal.biodata.pt/) (PT)
   * TODO: who is it open to ?
   * Example: [Plant BioDataVerse](https://dmportal.biodata.pt/dataverse/plant_biodataverse).

#### Authenticate 
Click on "Log in" in the top right corner, and choose the right authentication mechanism. Use your institutional login if it is present:
* in recherche.data.gouv: LDAP of your institute (only french institutes available)
* in Jülich DATA: Helmholtz AAI (federated, non-german institutes are also available)
* in dmportal.biodata.pt: registration form.

Connecting with an [ORCID](https://en.wikipedia.org/wiki/ORCID), Github account, or Google login can also be available, depending on the dataverse instance.

#### Create a new dataset

````{dropdown} **Create a new dataset**
:open:

```{figure} ../../../images/new_dataset.png
---
width: 1000px
name: Create a new dataset in a dataverse
alt: Create a new dataset in a dataverse
---
Create a new dataset in a dataverse
```
````

If you have permissions issues, ask for support from the dataverse owner (data.inrae: urgi-data@inrae.fr ; Jülich DATA: ask for support from central library team (forschungsdaten@fz-juelich.de or via [chat](https://chat.fz-juelich.de/channel/fdm). You might need account validation or specific permissions to create datasets.

#### Fill in the metadata

````{dropdown} **Fill in the metadata**
:open:

```{figure} ../../../images/fill_in_metadata.png
---
width: 1000px
name: Fill in the metadata
alt: Fill in the metadata
---
Fill in the metadata of the dataset
```
````

For a generic template, the required fields of this form are Title, Contact, Author, Description, Subject, Kind of Data. 
Metadata Tip: After adding the dataset, click the Edit Dataset button to add more metadata. 

#### Save the dataset

The DOI will be automatically generated but the dataset will remain in draft mode (with the "Draft" and "Unpublished" tags) until it is voluntarily published.

#### Manage collaborative editing and access rights

It is possible to ask partners to complete certain metadata by giving them the appropriate rights.
* Ask the partner to create an account on the Dataverse containing the dataset, and to give you its username.
* On the dataset, click on Edit > Permissions > Dataset.
* Click on the Assign Roles to Users/Groups button.
* Fill in the name of the producer and assign the role of Contributor
* Save changes

### Step 2: Add mandatory metadata for plant phenotyping data

``` {note}
This section is also applicable to Zenodo.
```

```{note}
Some dataverse instances (such as dmportal.biodata.pt) have a MIAPPE metadata section that allows the use of dataverse web pages to store Biological material, Observation Variable and Study metadata. In that case you can use your dataverse's MIAPPE metadata instead of the MIAPPE metadata files described in this step.
```

The description of the plant material used in the experimentation proposed by MIAPPE is common to all types of experimentation (phenotypic, genetic, omic, etc…) and enables long-term reuse and interoperability between data sets.
You can either use the full [MIAPPE template](https://github.com/MIAPPE/MIAPPE/tree/master/MIAPPE_Checklist-Data-Model-v1.1/MIAPPE_templates) or only selected sheets, available as individual file templates which can be found below. 

#### Biological material
Use [BiologicalMaterial.xlsx](https://doi.org/10.15454/BWJVVG/KUJNCM). This spreadsheet contains the following fields:
Mandatory fields:
* “Biological material ID” (ex: INRA:W95115_inra_2001): Lot number or material identifier in the data files
* “Material source ID” (ex: INRA:B73_usda) OR “Accession_number” (B73_usda) + “Holding_institute” (ex: INRA)
* Accession Number
* Genus
* Species
Optional fields:
* “Material source DOI”: accession DOI
* Organism: NCBITAXON:4577
* “Infraspecific name”: variety names, cultivar names, etc...
* Genealogy: 
   * Parent1or2_AccessionNumber
   * Parent1or2_TaxonGroup
   * Parent1or2_HoldingInstitutionName
   * Parent1or2_Type (father/mother/undefined)
* All MIAPPE Biological Material fields ([DM-40 to DM-56](https://github.com/MIAPPE/MIAPPE/blob/master/MIAPPE_Checklist-Data-Model-v1.1/MIAPPE_Checklist-Data-Model-v1.1.tsv#L42))
* Free input: synonyms, project IDs, any relevant information on the plant material.

#### Observed variables
Use [ObservedVariables.xlsx](https://doi.org/10.15454/BWJVVG/60VCZT). This file is needed for the description of phenotyping experiments traits and methods.

#### Studies or experiments
It is recommended to list the experimentation done in this dataset, including in particular the GPS location, the site name and the environmental parameters which characterize the experimental sites. Use [Studies.xlsx](https://doi.org/10.57745/DVGDRV )

#### How to add metadata files in a Dataverse
* Click on "+ Upload Files" in the "Files" tab
* Add the file(s). Please note that :
   * the file size is limited to 15.0 GB
   * compressed files are automatically decompressed at the time of import
   * tabbed files must use the "," separator and "UTF-8" encoding to avoid problems during import (see the dedicated section in the [user guide](https://ist.blogs.inrae.fr/datainrae-guide/creer-editer-publier-un-dataset/#Fichiers_de_donnees_tabulees))
* Fill in the "Description" field for each added file
* Update the file labels by selecting "File options" > "Tags" for each file

````{dropdown} **Update the file labels**
:open:

```{figure} ../../../images/update_labels.png
---
width: 1000px
name: Update the file labels
alt: Update the file labels
---
Update the file labels
```
````

* Add a custom label, "Biological_Material" or "Observed_Variable" depending on the file type. If the label exists, it will be available in the "File labels" section, otherwise you will have to create it in the "Customize file label" section and apply it.

````{dropdown} **Add a custom label**
:open:

```{figure} ../../../images/add_label.png
---
width: 1000px
name: Add a custom label
alt: Add a custom label
---
Add a custom label
```
````

* Save your modifications

### Step 3: Add generic metadata to the dataset 

These are the metadata that are not specific to plant sciences.
Select the "Metadata" tab then click on the "add + edit metadata" button

````{dropdown} **Add and edit generic metadata**
:open:

```{figure} ../../../images/generic_metadata.png
---
width: 1000px
name: Add and edit generic metadata
alt: Add and edit generic metadata
---
Add and edit generic metadata
```
````

Mandatory metadata:
* Language: in section “Citation Metadata” > “Language” : dataset language
* Organism: in section “life science metadata” > “Organism” : species name

Recommended metadata:
* Contributor
* Keywords: In the list of Dataverses, Datasets and Files of your Dataverse, looking at existing entries for “Keyword Term” can help you find appropriate keywords.
* Related publication
* Grant Information
* Project Information
* Time Period Covered (start and end date)
* Geospatial Metadata > Geographic Coverage

### Step 4: Publish the dataset

#### Private publication: temporary
Give access to an unpublished dataset (private URL): Edit dataset > Private URL

````{dropdown} **Give access to an unpublished dataset**
:open:

```{figure} ../../../images/private_url.png  
---
width: 1000px
name: Give access to an unpublished dataset
alt: Give access to an unpublished dataset
---
Give access to an unpublished dataset
```
````

The submitter of a dataset can generate a private URL, to give access to a dataset not yet published to a person who has no access rights on it.

````{dropdown} **Create a private URL**
:open:

```{figure} ../../../images/create_private_url.png
---
width: 1000px
name: Create a private URL
alt: Create a private URL
---
Create a private URL
```
````

````{dropdown} **Unpublished dataset private URL**
:open:

```{figure} ../../../images/unpublished_dataset_private_url.png
---
width: 1000px
name: Unpublished dataset private URL
alt: Unpublished dataset private URL
---
Unpublished dataset private URL
```
````

#### Publication: definitive, with unlimited updates possible

Publish the dataset:

````{dropdown} **Publish the dataset**
:open:

```{figure} ../../../images/publish_dataset.png
---
width: 1000px
name: Publish the dataset
alt: Publish the dataset
---
Publish the dataset
```
````

#### Add an existing dataset to a specific dataverse
Open your dataset page and login, then choose “Link Dataset”:

````{dropdown} **Add an existing dataset to a specific dataverse**
:open:

```{figure} ../../../images/link_dataset.png
---
width: 1000px
name: Add an existing dataset to a specific dataverse
alt: Add an existing dataset to a specific dataverse
---
Add an existing dataset to a specific dataverse
```
````

Find the dataverse in which you want to add your dataset, select it and click on "Save Linked Dataset".

````{dropdown} **Save Linked dataset**
:open:

```{figure} ../../../images/save_linked_dataset.png
---
width: 1000px
name: Save linked dataset
alt: Save linked dataset
---
Save linked dataset
```
````

## Step-by-Step process for data submission and publication in e!DAL-PGP

### Step 1: Dataset creation
Major aim of the eDAL-PGP repository is FAIR sharing plant related research data, which do not fit into domain-specific repositories and databases due to scope or volume. All available datasets are FAIR compliant and can be referenced via a persistent DOI. The submission procedure is open for all ELIXIR associated users over the LS AAI. The key feature of e!DAL-PGP is its user-friendly and simple data submission and internal review procedure

#### Authentication
The eDAL-PGP repository currently provides a local desktop application (Win/Unix/Mac) as well as a simple web-based submission tool to upload research data and initiate the intern review procedure. Both can be downloaded or rather accessed on the [main project website](https://edal-pgp.ipk-gatersleben.de). 

````{dropdown} **The PGP repository**
:open:

```{figure} ../../../images/the_PGP_repository.png
---
width: 1000px
name: The PGP repository
alt: The PGP repository
---
The PGP repository
```
````

To authenticate for the submission process the LS AAI (formerly known as ELIXIR AAI) is used. Every user can select the identity provider of his home organization. If the home organization is not connected and therefore not in the selection list, the login is alternatively possible by using a third party provider like ORCID or Google. After successful login it is necessary to read the "Deposition and License Agreement" once.

#### Submit a new Dataset
For submitting a new dataset some technical metadata are necessary to describe the data and provide the opportunity for assigning a DOI later. Therefore the submission client provides a simple form-based user interface guiding the user through the different attributes and gives feedback in case of missing attributes. Some of the fields like “Description” are simple free text fields, while others like “Authors” provide more options  when clicking into the field like the linkage to the ORCID registry to select the ORCID for every author.

````{dropdown} **Submit a new dataset**
:open:

```{figure} ../../../images/submit_new_dataset.png
---
width: 1000px
name: Submit a new dataset
alt: Submit a new dataset
---
Submit a new dataset
```
````

A dataset can contain single files as well as comprehensive folder structure. Compressed files like \*.zip should be avoided, because this would prevent a later navigation on the content page for the published datasets. After entering all necessary metadata, it is necessary to accept the “Deposition and License Agreement” to start the submission process.

````{dropdown} **Start the submission process**
:open:

```{figure} ../../../images/start_submission_process.png
---
width: 1000px
name: Start the submission process
alt: Start the submission process
---
Start the submission process
```
````

After finishing the upload process the submission is ready for the integrated review process. The data provider will receive an email to confirm, that his submission was successful and that the internal review war initiated.The reviewers will also automatically receive an email with a link providing a restricted access to the given dataset. After successfully checking some general requirement, such as a complete metadata or the use of open formats the data provider will receive an additional mail with the opportunity to assign the final DOI to publish and reference his datasets or alternatively cancel the submission. Usually there is an additional review necessary, because the data belongs to a corresponding research publication. Therefore the last email also contains a temporary preview link which the data provider can use to share the data with colleagues or additional reviewers and decide later if and when he wants to assign the final and immutable DOI.

### Step 2: Add mandatory metadata for plant phenotyping data
Due to the generic concept of the underlying e!DAL infrastructure software the e!DAL-PGP repository requires only a standardized set of technical metadata inspired by the DublinCore metadata schema as well as the derived DataCite schema, which is needed to assign DOIs. Because of the scope of e!DAL-PGP on sharing mainly plant genotypic and phenotypic datasets the internal review focuses on providing corresponding semantic metadata and domain-specific. To add these metadata files, the data provider can directly add them using a suitable format, such as ISA-Tab or ISA-JSON for MIAPPE-compliant metadata. 

````{dropdown} **Use the metadata folder to integrate metadata to the dataset**
:open:

```{figure} ../../../images/dataset_landing_page.png
---
width: 1000px
name: Landing page for a phenotypic dataset in e!DAL-PGP
alt: Landing page for a phenotypic dataset in e!DAL-PGP
---
Landing page for a phenotypic dataset in e!DAL-PGP
```
````

### Step 3: Publish the dataset
Every uploaded dataset will get at the end of the submission and review process a DOI, which resolves to a landing page providing access to the datasets and the corresponding metadata. This DOI is immutable and can be used to reference and cite the datasets persistently. Before the final publication every data provider will receive a temporary preview link and decide on his own if and when he makes his datasets public. The preview link allows sharing the data before for additional review and communication with colleagues, but it is not intended to be used for permanent sharing. Additionally the mail contains two links to assign the final DOI or cancel the submission in case of any necessary changes.

````{dropdown} **Final approval email for data provider**
:open:

```{figure} ../../../images/confirm_dataset_publication.png
---
width: 1000px
name: Final approval email
alt: Final approval email
---
Final approval email
```
````

## Conclusion

In this recipe we have seen how to publish plant experimental data to generic data repositories in a MIAPPE-compliant way. 

### What to read next? 

Documentation specific to:
* the command-line tool DV Uploader:
   * [git repository](https://github.com/GlobalDataverseCommunityConsortium/dataverse-uploader)
   * [user documentation](https://recherche.data.gouv.fr/en/category/33/guide/dv-uploader-1)
* Recherche Data Gouv:
   * [general guide](https://recherche.data.gouv.fr/en/category/9/guide/all-you-need-to-know-about-the-recherche-data-gouv-repository)
   * [FAQ](https://recherche.data.gouv.fr/en/faq)
* Jülich DATA:
   * [repository details](https://doi.org/10.17616/R31NJMYC)
   * [guide](https://data.fz-juelich.de/guide/juelich/)
* DMPortal BioData Pt:
    * TODO
* e!DAL-PGP:
    * [manual](https://edal-pgp.ipk-gatersleben.de/document/manual.html)

````{rdmkit_panel}
````

## Reference

````{dropdown} **References**
```{footbibliography}
```
````

## Authors:
````{authors_fairplus}
Erwan: Writing - Original Draft
Vanita: Writing - Original Draft
Nicolas: Writing - Original Draft
Celia: Writing - Original Draft
Daniel: Writing - Original Draft
Daniel: Writing - Original Draft
Inês: Writing - Original Draft
Cyril: Review & Editing
````

## Licence
````{license_fairplus}
CC-BY-4.0
````
