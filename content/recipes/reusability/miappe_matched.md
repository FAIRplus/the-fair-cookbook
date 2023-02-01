# Plant genomic and genetic variation data submission to EMBL-EBI databases



````{panels_fairplus}
:identifier_text: FCB061
:identifier_link: 'https://w3id.org/faircookbook/FCB061'
:difficulty_level: 3
:recipe_type: guidance
:reading_time_minutes: 30
:intended_audience:  everyone 
:has_executable_code: nope
:maturity_level: 3
:maturity_indicator: 15,20
:recipe_name: Improving dataset maturity - the MIAPPE use case
```` 

## Main Objective

Plant genotyping and phenotyping data are often used in combination to make evidence-based inferences about different 
trait expressions. 
A challenge here is not necessarily to collect the data, but to offer them in a stable way over the
long term in public repositories (URL_TO_INSERT_TERM_10769 https://fairsharing.org/search?recordType=repository)  with sufficient metadata informat (URL_TO_INSERT_TERM_10770 https://fairsharing.org/search?recordType=model_and_format) ion to make conclusions about them, in line with FAIR (URL_TO_INSERT_RECORD_10771 https://fairsharing.org/FAIRsharing.WWI10U) 
principles. 
Since these repositories (URL_TO_INSERT_TERM_10772 https://fairsharing.org/search?recordType=repository)  are often not linked directly, it is even more important to provide metadata that
allows users to recognise these links by their identifier (URL_TO_INSERT_TERM_10773 https://fairsharing.org/search?recordType=identifier_schema) s.
A key point here is sample management:  the identifier (URL_TO_INSERT_TERM_10774 https://fairsharing.org/search?recordType=identifier_schema) s assigned here help both humans and machines to understand
which experimental data are linked.

The main objective of the recipe is to provide a means of submitting to public repositories (URL_TO_INSERT_TERM_10775 https://fairsharing.org/search?recordType=repository)  and tracking genotyping
data, with a particular focus on plants.  This includes:

    1) Submission of sample data and metadata informat (URL_TO_INSERT_TERM_10776 https://fairsharing.org/search?recordType=model_and_format) ion to BioSample (URL_TO_INSERT_RECORD_10777 https://fairsharing.org/FAIRsharing.qr6pqk) s.
    2) Submission of sequencing data and metadata to ENA (URL_TO_INSERT_RECORD_10778 https://fairsharing.org/FAIRsharing.dj8nt8) .
    3) Retrieval of the correct genome assembly for the genotyping experiment
    4) Conversion of the resulting analysis file (in VCF (URL_TO_INSERT_RECORD_10781 https://fairsharing.org/FAIRsharing.cfzz0h)  format (URL_TO_INSERT_TERM_10779 https://fairsharing.org/search?recordType=model_and_format) ) to be FAIR (URL_TO_INSERT_RECORD_10780 https://fairsharing.org/FAIRsharing.WWI10U) 
    5) Submission of the genotyping results to EVA (URL_TO_INSERT_RECORD_10782 https://fairsharing.org/FAIRsharing.6824pv) .

In terms of FAIR (URL_TO_INSERT_RECORD_10784 https://fairsharing.org/FAIRsharing.WWI10U) ification goals, this means obtaining stable, resolvable  identifier (URL_TO_INSERT_TERM_10783 https://fairsharing.org/search?recordType=identifier_schema) s for the datasets and meeting
community annotation requirements as expressed in the MIAPP (URL_TO_INSERT_RECORD_10787 https://fairsharing.org/FAIRsharing.tghhc4) E (URL_TO_INSERT_RECORD_10785 https://fairsharing.org/FAIRsharing.b403jy)  (URL_TO_INSERT_RECORD_10786 https://fairsharing.org/FAIRsharing.nd9ce9)  requirements. 

## Summary

This recipe provides guidance for submitting plant genotyping data to public repositories (URL_TO_INSERT_TERM_10788 https://fairsharing.org/search?recordType=repository) . It explains in a step-wise
fashion which work should be done and when. Special attention should be paid to the metadata maintenance of the data
that will be deposited in different repositories (URL_TO_INSERT_TERM_10789 https://fairsharing.org/search?recordType=repository)  as part of this recipe. A prerequisite for fully understanding
this recipe is a basic knowledge of the [MIAPP (URL_TO_INSERT_RECORD_10794 https://fairsharing.org/FAIRsharing.tghhc4) E (URL_TO_INSERT_RECORD_10790 https://fairsharing.org/FAIRsharing.b403jy)  (URL_TO_INSERT_RECORD_10791 https://fairsharing.org/FAIRsharing.nd9ce9)  standard](https://fairsharing.org (URL_TO_INSERT_RECORD_10792 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_10793 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_10795 https://fairsharing.org/3538) /bsg-s000543/). 

The exact listing (URL_TO_INSERT_RECORD_10796 https://fairsharing.org/FAIRsharing.q7bkqr)  of the metadata fields required for a FAIR (URL_TO_INSERT_RECORD_10797 https://fairsharing.org/FAIRsharing.WWI10U) ification of the genotyping data set within a VCF (URL_TO_INSERT_RECORD_10798 https://fairsharing.org/FAIRsharing.cfzz0h)  file is 
also part of this recipe with examples and explanations (See details in Section 4.2).

## Graphical overview of the FAIRification Objectives


[comment]: <> (<!-- ![]&#40;https://i.imgur.com/iqdjWqo.png&#41; -->)

````{dropdown} **FAIRification Objectives**
:open:

```{figure} ../../../images/iqdjWqo.png
---
width: 700px
name: FAIR (URL_TO_INSERT_RECORD_10799 https://fairsharing.org/FAIRsharing.WWI10U) ification Objectives
alt: FAIR (URL_TO_INSERT_RECORD_10800 https://fairsharing.org/FAIRsharing.WWI10U) ification Objectives
---
FAIR (URL_TO_INSERT_RECORD_10801 https://fairsharing.org/FAIRsharing.WWI10U) ification Objectives
```
````


## FAIRification Objectives, Inputs and Outputs

|Actions.Objectives.Tasks|Input|Output|
|--- |--- |--- |
|[text annotation](http://edamontology.org (URL_TO_INSERT_RECORD_10802 https://fairsharing.org/FAIRsharing.a6r7zs) /operation_3778)|[MIAPPE](https://fairsharing.org (URL_TO_INSERT_RECORD_10804 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_10805 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_10806 https://fairsharing.org/3538) /FAIRsharing.nd9ce9)|[annotated text](http://edamontology.org (URL_TO_INSERT_RECORD_10803 https://fairsharing.org/FAIRsharing.a6r7zs) /data_3779)|
|[conversion](http://edamontology.org (URL_TO_INSERT_RECORD_10808 https://fairsharing.org/FAIRsharing.a6r7zs) /operation_3434)|[Variant File Format (URL_TO_INSERT_TERM_10807 https://fairsharing.org/search?recordType=model_and_format)  (.vcf)](https://fairsharing.org (URL_TO_INSERT_RECORD_10810 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_10811 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_10812 https://fairsharing.org/3538) /FAIRsharing.cfzz0h)|[annotated text](http://edamontology.org (URL_TO_INSERT_RECORD_10809 https://fairsharing.org/FAIRsharing.a6r7zs) /data_3779)|
|[format (URL_TO_INSERT_TERM_10813 https://fairsharing.org/search?recordType=model_and_format)  validation](http://edamontology.org (URL_TO_INSERT_RECORD_10815 https://fairsharing.org/FAIRsharing.a6r7zs) /operation_0336)|[Variant File Format (URL_TO_INSERT_TERM_10814 https://fairsharing.org/search?recordType=model_and_format)  (.vcf)](https://fairsharing.org (URL_TO_INSERT_RECORD_10817 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_10818 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_10819 https://fairsharing.org/3538) /FAIRsharing.cfzz0h)|[report](http://edamontology.org (URL_TO_INSERT_RECORD_10816 https://fairsharing.org/FAIRsharing.a6r7zs) /data_2048)|
|[format (URL_TO_INSERT_TERM_10820 https://fairsharing.org/search?recordType=model_and_format)  validation](http://edamontology.org (URL_TO_INSERT_RECORD_10821 https://fairsharing.org/FAIRsharing.a6r7zs) /operation_0336)|[MIAPPE](https://fairsharing.org (URL_TO_INSERT_RECORD_10823 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_10824 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_10825 https://fairsharing.org/3538) /FAIRsharing.nd9ce9)|[report](http://edamontology.org (URL_TO_INSERT_RECORD_10822 https://fairsharing.org/FAIRsharing.a6r7zs) /data_2048)|


## Table of Data Standards

|Data Format (URL_TO_INSERT_TERM_10827 https://fairsharing.org/search?recordType=model_and_format) s|Terminologies (URL_TO_INSERT_TERM_10828 https://fairsharing.org/search?recordType=terminology_artefact) |Model (URL_TO_INSERT_TERM_10826 https://fairsharing.org/search?recordType=model_and_format) |
|--- |--- |--- |
|[FAST (URL_TO_INSERT_RECORD_10829 https://fairsharing.org/FAIRsharing.p5df9c) Q](https://fairsharing.org (URL_TO_INSERT_RECORD_10830 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_10831 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_10832 https://fairsharing.org/3538) /FAIRsharing.r2ts5t)|||
|[FAST (URL_TO_INSERT_RECORD_10833 https://fairsharing.org/FAIRsharing.p5df9c) A (URL_TO_INSERT_RECORD_10834 https://fairsharing.org/FAIRsharing.rz4vfg) ](https://fairsharing.org (URL_TO_INSERT_RECORD_10835 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_10836 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_10837 https://fairsharing.org/3538) /FAIRsharing.rz4vfg)|||
|[MIAPP (URL_TO_INSERT_RECORD_10842 https://fairsharing.org/FAIRsharing.tghhc4) E (URL_TO_INSERT_RECORD_10838 https://fairsharing.org/FAIRsharing.b403jy)  (URL_TO_INSERT_RECORD_10839 https://fairsharing.org/FAIRsharing.nd9ce9) ](https://fairsharing.org (URL_TO_INSERT_RECORD_10840 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_10841 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_10843 https://fairsharing.org/3538) /FAIRsharing.nd9ce9)|||
|[Variant File Format (URL_TO_INSERT_TERM_10844 https://fairsharing.org/search?recordType=model_and_format)  (.vcf)](https://fairsharing.org (URL_TO_INSERT_RECORD_10845 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_10846 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_10847 https://fairsharing.org/3538) /FAIRsharing.cfzz0h)|||
|[BioSample (URL_TO_INSERT_RECORD_10851 https://fairsharing.org/FAIRsharing.qr6pqk) s - Plant MIAPP (URL_TO_INSERT_RECORD_10852 https://fairsharing.org/FAIRsharing.tghhc4) E (URL_TO_INSERT_RECORD_10849 https://fairsharing.org/FAIRsharing.b403jy)  (URL_TO_INSERT_RECORD_10850 https://fairsharing.org/FAIRsharing.nd9ce9)  checklist](https://www.ebi.ac.uk/biosamples (URL_TO_INSERT_RECORD_10848 https://fairsharing.org/FAIRsharing.ewjdq6) /schemas/certification/plant-miappe.json)|||


## Table of Software and Tools

|Tool Name|
|--- |
|[BioSample (URL_TO_INSERT_RECORD_10854 https://fairsharing.org/FAIRsharing.qr6pqk) s](https://www.ebi.ac.uk/biosamples (URL_TO_INSERT_RECORD_10853 https://fairsharing.org/FAIRsharing.ewjdq6) /)|
|[European Nucleotide Arch (URL_TO_INSERT_RECORD_10858 https://fairsharing.org/FAIRsharing.52b22c) ive (URL_TO_INSERT_RECORD_10855 https://fairsharing.org/FAIRsharing.dj8nt8) , ENA (URL_TO_INSERT_RECORD_10856 https://fairsharing.org/FAIRsharing.dj8nt8) ](https://www.ebi.ac.uk/ena (URL_TO_INSERT_RECORD_10857 https://fairsharing.org/FAIRsharing.dj8nt8) /browser/home)|
|[European Variation Arch (URL_TO_INSERT_RECORD_10862 https://fairsharing.org/FAIRsharing.52b22c) ive (URL_TO_INSERT_RECORD_10859 https://fairsharing.org/FAIRsharing.6824pv) ,EVA (URL_TO_INSERT_RECORD_10860 https://fairsharing.org/FAIRsharing.6824pv) ](https://www.ebi.ac.uk/eva (URL_TO_INSERT_RECORD_10861 https://fairsharing.org/FAIRsharing.6824pv) /)|
|[International Nucleotide Sequence Database (URL_TO_INSERT_TERM_10863 https://fairsharing.org/search?fairsharingRegistry=Database)  Collaboration](https://www.insdc.org/)
|[VCF (URL_TO_INSERT_RECORD_10865 https://fairsharing.org/FAIRsharing.cfzz0h)  Validator](https://github.com (URL_TO_INSERT_RECORD_10864 https://fairsharing.org/FAIRsharing.c55d5e) /EBIvariation/vcf-validator/wiki/User's-Guide)|
|[Curl](https://curl.se/)|

## Step-by-Step Process


<!-- ### Step 1: Take DNA sample and register sample material at BioSample (URL_TO_INSERT_RECORD_10866 https://fairsharing.org/FAIRsharing.qr6pqk) s -->


### Step 1: Take DNA sample

The experimentalist takes a sample of plant biological material. 
The sample metadata are collected according to 
_the [MIAPPE](https://github.com (URL_TO_INSERT_RECORD_10867 https://fairsharing.org/FAIRsharing.c55d5e) /MIAPPE/MIAPPE/tree/master/MIAPPE_Checklist-Data-Model-v1.1) specifications,
Biological Material section_. 
It enriches minimal [MCPD](https://www.bioversityinternational.org/e-library/publications/detail/faobioversity-multi-crop-passport-descriptors-v21-mcpd-v21/) 
fields with sample traceability informat (URL_TO_INSERT_TERM_10868 https://fairsharing.org/search?recordType=model_and_format) ion.


### Step 2: Register sample material at BioSamples

This is done in general through JSO (URL_TO_INSERT_RECORD_10870 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_10869 https://fairsharing.org/FAIRsharing.5bbab9)  API ([Python](https://github.com (URL_TO_INSERT_RECORD_10871 https://fairsharing.org/FAIRsharing.c55d5e) /PBR/elixir-fondue-datathon/tree/master/test_data_set/BioSamples/scripts/python) 
and [Shell](https://github.com (URL_TO_INSERT_RECORD_10872 https://fairsharing.org/FAIRsharing.c55d5e) /PBR/elixir-fondue-datathon/tree/master/test_data_set/BioSamples/scripts/shell) commands are also available).
Refer to the official [documentation](https://www.ebi.ac.uk/biosamples (URL_TO_INSERT_RECORD_10873 https://fairsharing.org/FAIRsharing.ewjdq6) /docs/references/api/submit (URL_TO_INSERT_RECORD_10874 https://fairsharing.org/FAIRsharing.NYAjYd) #_submit_a_sample) for 
the complete details, for training material and slides regarding this, refer to {footcite}`fondue_datathon`. 
Here is the proposed procedure:

1. Create a user account

First you need an account to submit samples to EMB (URL_TO_INSERT_RECORD_10877 https://fairsharing.org/FAIRsharing.a1rp4c) L-EBI BioSample (URL_TO_INSERT_RECORD_10876 https://fairsharing.org/FAIRsharing.qr6pqk) s database (URL_TO_INSERT_TERM_10875 https://fairsharing.org/search?fairsharingRegistry=Database) . We recommend new users, or those planning 
to make downstream submissions to ENA (URL_TO_INSERT_RECORD_10878 https://fairsharing.org/FAIRsharing.dj8nt8) , to use the Webin Authentication service. You can create a Webin account using 
[Webin web interface](https://www.ebi.ac.uk/ena (URL_TO_INSERT_RECORD_10879 https://fairsharing.org/FAIRsharing.dj8nt8) /submit/sra/#home). 
Please refer to [ENA (URL_TO_INSERT_RECORD_10880 https://fairsharing.org/FAIRsharing.dj8nt8)  documentation](https://ena-docs.readthedocs.io/en/latest/submit/general-guide/registration.html) 
for more details about creating an account. 

2. Login to the system and get a JSO (URL_TO_INSERT_RECORD_10882 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_10881 https://fairsharing.org/FAIRsharing.5bbab9)  Web Token (JWT)

Webin uses JSO (URL_TO_INSERT_RECORD_10884 https://fairsharing.org/FAIRsharing.6bc7h9) N (URL_TO_INSERT_RECORD_10883 https://fairsharing.org/FAIRsharing.5bbab9)  Web Token (JWT) for authentication. Use your login credentials to retrieve a JWT. You can either use 
the Webin [Swagger interface](https://www.ebi.ac.uk/ena (URL_TO_INSERT_RECORD_10885 https://fairsharing.org/FAIRsharing.dj8nt8) /submit/webin/auth/swagger-ui/index.html?configUrl=/ena/submit/webin/auth/v3/api-docs/swagger-config) 
(A) or a programmatic method (B):

A: Go to [Webin Swagger](https://www.ebi.ac.uk/ena (URL_TO_INSERT_RECORD_10886 https://fairsharing.org/FAIRsharing.dj8nt8) /submit/webin/auth/swagger-ui/index.html?configUrl=/ena/submit/webin/auth/v3/api-docs/swagger-config#/AuthenticationAPI/getToken) 
and use PO (URL_TO_INSERT_RECORD_10887 https://fairsharing.org/FAIRsharing.3ngg40) ST /token endpoint to retrieve a JWT.

B: Use CURL (URL_TO_INSERT_RECORD_10888 https://fairsharing.org/FAIRsharing.9d38e2)  or a programmatic method.

```bash
`TOKEN=$(curl -X POST "https://www.ebi.ac.uk/ena/submit/webin/auth/token" -H "accept: */*" 
-H "Content-Type: application/json" -d "{\"authRealms\":[\"ENA\"],\"password\":\"PASSWORD\",\"username\":\"WEBIN_ID\"}")`
```

3. Allocate accessions via the pre-accessioning endpoint.

Use the pre-accessioning endpoint to reserve BioSample (URL_TO_INSERT_RECORD_10889 https://fairsharing.org/FAIRsharing.qr6pqk) s ID. This will create  private, empty samples with future 
release dates. The only mandatory field for pre-accessioning is the sample name.

The following CURL (URL_TO_INSERT_RECORD_10890 https://fairsharing.org/FAIRsharing.9d38e2)  command returns 3 accessions as the body contains names for 3 samples.
```bash
`curl 'https://www.ebi.ac.uk/biosamples/samples/bulk-accession?authProvider=WEBIN' 
-i -X POST -H "Content-Type: application/json;charset=UTF-8" -H "Accept: application/hal+json" 
-H "Authorization: Bearer $TOKEN" -d '[{  "name" : "FakeSample 1"}, { "name" : "FakeSample 2"}, {  "name" : "FakeSample 3"}]'`
```

Please refer to the [BioSample (URL_TO_INSERT_RECORD_10892 https://fairsharing.org/FAIRsharing.qr6pqk) s documentation](https://www.ebi.ac.uk/biosamples (URL_TO_INSERT_RECORD_10891 https://fairsharing.org/FAIRsharing.ewjdq6) /docs/references/api/submit (URL_TO_INSERT_RECORD_10893 https://fairsharing.org/FAIRsharing.NYAjYd) #_submit_a_sample). 



More general informat (URL_TO_INSERT_TERM_10894 https://fairsharing.org/search?recordType=model_and_format) ion is available on the RDMkit {footcite}`rdmkit_plant_genomics_assembly`. 
A specific checklist is used: [BioSample (URL_TO_INSERT_RECORD_10898 https://fairsharing.org/FAIRsharing.qr6pqk) s - Plant MIAPP (URL_TO_INSERT_RECORD_10899 https://fairsharing.org/FAIRsharing.tghhc4) E (URL_TO_INSERT_RECORD_10896 https://fairsharing.org/FAIRsharing.b403jy)  (URL_TO_INSERT_RECORD_10897 https://fairsharing.org/FAIRsharing.nd9ce9)  checklist](https://www.ebi.ac.uk/biosamples (URL_TO_INSERT_RECORD_10895 https://fairsharing.org/FAIRsharing.ewjdq6) /schemas/certification/plant-miappe.json).


<!-- ### Step 2: Sequence DNA sample and submit reads to ENA (URL_TO_INSERT_RECORD_10900 https://fairsharing.org/FAIRsharing.dj8nt8)  -->


### Step 3: Perform sequencing of DNA sample

The sequencing staff performs the sequencing of the DNA sample, which is followed by a quality control. The reads are 
then arch (URL_TO_INSERT_RECORD_10903 https://fairsharing.org/FAIRsharing.52b22c) ived in the institution (URL_TO_INSERT_TERM_10901 https://fairsharing.org/search?recordType=institution) al Laboratory Informat (URL_TO_INSERT_TERM_10902 https://fairsharing.org/search?recordType=model_and_format) ion Management System (LIMS).


### Step 4: Register and submit sequencing reads to ENA 

Submit Sequencing reads to ENA (URL_TO_INSERT_RECORD_10904 https://fairsharing.org/FAIRsharing.dj8nt8) , using BioSample (URL_TO_INSERT_RECORD_10905 https://fairsharing.org/FAIRsharing.qr6pqk) s IDs to identify material.


#### 4.1 The Study

To begin, you should register a study. Recall that a study describes the purpose of the work you have done, groups other
objects beneath it, and controls when the data becomes public. A study is required for all submissions to ENA (URL_TO_INSERT_RECORD_10906 https://fairsharing.org/FAIRsharing.dj8nt8) .

1. Log in to the [Webin Submission Portal](https://www.ebi.ac.uk/ena (URL_TO_INSERT_RECORD_10907 https://fairsharing.org/FAIRsharing.dj8nt8) /submit/sra/#home) with your Webin credentials.
 
2. Click the '**New Submission**' tab and find the '**Register study (project (URL_TO_INSERT_TERM_10908 https://fairsharing.org/search?recordType=project) )**' radio button. Click '**Next**' to see 
the study registration interface


````{dropdown} **EMBL-EBI Webin Submission Interface**
:open:

```{figure} ../../../images/JrDztCg.png
---
width: 650px
name: EMB (URL_TO_INSERT_RECORD_10909 https://fairsharing.org/FAIRsharing.a1rp4c) L-EBI Webin Submission Interface
alt: EMB (URL_TO_INSERT_RECORD_10910 https://fairsharing.org/FAIRsharing.a1rp4c) L-EBI Webin Submission Interface
---
EMB (URL_TO_INSERT_RECORD_10911 https://fairsharing.org/FAIRsharing.a1rp4c) L-EBI Webin Submission Interface
```
````

3. The '**Short Name**' field should be filled in with something brief and meaningful, e.g.:*barley_study_2021*


4. You should take time to provide a descriptive title and informat (URL_TO_INSERT_TERM_10912 https://fairsharing.org/search?recordType=model_and_format) ive abstract for your own studies, but these can be 
edited later if needed. For now, use as your title: *GBS Study of Barley from &lt;Your Town/Lab>*

5. When you have completed all required fields, click '**Submit**' and then confirm.
6. Now navigate to the '**Studies**' tab to see the study you just registered. You might need to refresh the page!  
Make a note of its accession numbers (_ERP#####_, _PRJEB#####_), which will resemble. For a submission, these would be 
the numbers you would cite in any publications involving the data.

#### 4.2 The Sample

The next step is to register the sample, which will give other users essential context for the sequence data you are
submitting. The sample describes the source biological material of your sequencing work.

As discussed above, **samples are best submitted through BioSample (URL_TO_INSERT_RECORD_10913 https://fairsharing.org/FAIRsharing.qr6pqk) s**.

In ENA (URL_TO_INSERT_RECORD_10914 https://fairsharing.org/FAIRsharing.dj8nt8) , samples are required to conform to a checklist of values. Checklists define a set of mandatory and recommended 
descriptor fields for a given type of sample. It is recommended that you look at these early and make sure you collect 
all required metadata items for the type of sample you will be registering.

The selection of available checklists can be browsed at: [https://www.ebi.ac.uk/ena (URL_TO_INSERT_RECORD_10915 https://fairsharing.org/FAIRsharing.dj8nt8) /browser/checklists](https://www.ebi.ac.uk/ena (URL_TO_INSERT_RECORD_10916 https://fairsharing.org/FAIRsharing.dj8nt8) /browser/checklists). 
Currently, three plant specific checklists are available: [ERC000020](https://www.ebi.ac.uk/ena (URL_TO_INSERT_RECORD_10917 https://fairsharing.org/FAIRsharing.dj8nt8) /browser/view/ERC000020), [ERC000035](https://www.ebi.ac.uk/ena (URL_TO_INSERT_RECORD_10918 https://fairsharing.org/FAIRsharing.dj8nt8) /browser/view/ERC000035) and [ERC000037](https://www.ebi.ac.uk/ena (URL_TO_INSERT_RECORD_10919 https://fairsharing.org/FAIRsharing.dj8nt8) /browser/view/ERC000037). 



1. Return to the '**New Submission**' tab in the submission service. You may need to click the '**Restart Submission**' 
button at the bottom of the page.
2. Find the '**Register samples**' radio button and click **'Next'**.
3. You must choose an appropriate checklist of values to be provided for your sample: click '**Select checklist**' and
expand the '**Other checklists**' group to browse checklists of this type.
4. Select the appropriate checklist. For general purposes ERC000037 (**‘ENA (URL_TO_INSERT_RECORD_10920 https://fairsharing.org/FAIRsharing.dj8nt8)  Plant Sample Checklist’**) should be the 
default when submitting plant sequencing data. Now click '**Next**'.
add an image of the web ui for https://www.ebi.ac.uk/ena (URL_TO_INSERT_RECORD_10921 https://fairsharing.org/FAIRsharing.dj8nt8) /browser/view/ERC000037
5. Submitters now have the option of including additional fields in their checklist. It is not necessary to include any 
additional fields, but you can take this opportunity to see which fields are included by default, what requirements they have, and what else is available.

    Click '**Next**'.


6. Now you have the opportunity to construct a template for a submission of many samples: notice the phrase 
'**Template Basic Details**' at the top of the interface. This allows you to define values which are common to all 
samples in your submission. 

    Since we are only submitting one sample, skip this screen by clicking '**Next**'.

7. On the next screen, click the '**+ Add**' button to create your sample.

8. Give a 'Unique name' to your sample:

        barley_sample_1


    **Hint:** This value must always be unique among all samples submitted by your account!

9. Give your sample a title, e.g.:

        Barley sample from <Your Town/Lab> greenhouse

10. Write a brief description for your sample.
11. Find the appropriate taxon for your sample: For example enter '**Hordeum vulgare**' into the box and select it 
when it appears. 

    Further taxonomic details are automatically filled below this box. This box will only accept values which match with 
a species-rank entry in the [NCBI Taxonomy (URL_TO_INSERT_RECORD_10923 https://fairsharing.org/FAIRsharing.fj07xj)  database (URL_TO_INSERT_TERM_10922 https://fairsharing.org/search?fairsharingRegistry=Database) ](https://www.ncbi.nlm.nih.gov/taxonomy (URL_TO_INSERT_RECORD_10924 https://fairsharing.org/FAIRsharing.fj07xj) ).

12. Fill out the remaining details by reference to the values to the best of your knowledge. Only fields marked with 
a ***** are required, but it is best to fill as many fields as possible.

Use a markdown directive (note: not supported by hackMD but supported by jupyter notebook (URL_TO_INSERT_RECORD_10925 https://fairsharing.org/FAIRsharing.cbz72b) )

``` {note}
You can always find out more about what a field means and what information it accepts by hovering over the blue 'i'.
```

13. By the time you have completed this, your sample will be well-annotated and     understandable to people finding it 
in the database (URL_TO_INSERT_TERM_10926 https://fairsharing.org/search?fairsharingRegistry=Database)  later. 

    You are ready to submit when all the checks on the right of the page are green ticks, and none are red crosses.


    Click '**Submit**'.

14. Now navigate to the 'Samples' tab to see the sample you just registered. You might need to refresh the page.

	Make a note of its accession numbers as you will need these later:

		 ERS (URL_TO_INSERT_RECORD_10928 https://fairsharing.org/FAIRsharing.vajn3f) ####### and SAM (URL_TO_INSERT_RECORD_10927 https://fairsharing.org/FAIRsharing.k97xzh) EA####### 


#### 4.3 The Read Data

Now that study and sample metadata have been registered, it is time to submit the read data you have produced.



1. Return to the '**New Submission**' tab in the submission service. You may need to click the '**Restart Submission**'
button at the bottom of the page.
2. Find the '**Submit sequence reads and experiments**' radio button and click
3. Next, you are asked to choose which study these reads should be added to. Select the study you registered earlier and
click '**Next**'.
4. Now, you have the opportunity to register samples as part of this submission. However, you already registered a 
sample, so click '**Skip**'.
5. Now, select '**One Fastq file (Single)**' from the list of file options.
6. Fill out the form to describe your experiments and register the files. Ordinarily, you would need to upload the files
to a staging area before submitting them through this interface, refer to the [ENA (URL_TO_INSERT_RECORD_10929 https://fairsharing.org/FAIRsharing.dj8nt8)  upload guidelines](https://ena-docs.readthedocs.io/en/latest/submit/fileprep/upload.html). 

    Appropriate metadata for your read data submission should look similar to this:


    * **Sample reference:** *<enter the BioSample (URL_TO_INSERT_RECORD_10930 https://fairsharing.org/FAIRsharing.qr6pqk) s accession here>*
    * **Instrument Model (URL_TO_INSERT_TERM_10931 https://fairsharing.org/search?recordType=model_and_format) :** Illumina HiSeq 2500
    * **Library Name:** barley_library_1
    * **Library Source:** GENO (URL_TO_INSERT_RECORD_10932 https://fairsharing.org/FAIRsharing.kpbna7) MIC
    * **Library Selection:** Restriction Digest
    * **Library Strategy:** GBS
    * **Library Layout:** SINGLE
    * **First File Name:** HOR_1361_BRG.fastq.gz


```{note}
 If you did not note down your sample accession, you can safely visit the ‘**Samples**’ tab, copy the accession, 
 then return to the New Submission tab: your progress will be saved.
```

7. Click '**Submit**' and see if your submission validates successfully. If you encounter errors, try using the 
'**Download Template Spreadsheet'** button, open the file and check it in this plain text format (URL_TO_INSERT_TERM_10933 https://fairsharing.org/search?recordType=model_and_format) ; 
it can be easier to fix errors this way than in the interface. 


```{note}
Note that the use of template spreadsheets is the best way to submit multiple datasets through this interface.
```

8. If you manage to complete your submission, visit the 'Runs' tab to review your submission.

### Step 5: Check if used reference genome assembly is available

Is a GCF / GCA accession number available ? Check on [https://www.ebi.ac.uk/ena (URL_TO_INSERT_RECORD_10934 https://fairsharing.org/FAIRsharing.dj8nt8) /browser](https://www.ebi.ac.uk/ena (URL_TO_INSERT_RECORD_10935 https://fairsharing.org/FAIRsharing.dj8nt8) /browser).


* If yes, proceed directly to VCF (URL_TO_INSERT_RECORD_10936 https://fairsharing.org/FAIRsharing.cfzz0h)  submission at step 4.
* If no, [submit reference genome assembly](https://ena-docs.readthedocs.io/en/latest/submit/assembly/genome.html) 
to [INSDC](https://www.insdc.org/) (NCBI Genbank / EMB (URL_TO_INSERT_RECORD_10939 https://fairsharing.org/FAIRsharing.a1rp4c) L-EBI ENA (URL_TO_INSERT_RECORD_10937 https://fairsharing.org/FAIRsharing.dj8nt8)  / DDBJ (URL_TO_INSERT_RECORD_10938 https://fairsharing.org/FAIRsharing.k337f0) ) and wait until accession number is issued,
 then proceed to step 4.


<!-- ### Step 6: Analyse sequencing results and submit VCF (URL_TO_INSERT_RECORD_10941 https://fairsharing.org/FAIRsharing.cfzz0h)  file to EVA (URL_TO_INSERT_RECORD_10940 https://fairsharing.org/FAIRsharing.6824pv)  -->


### Step 6: Analyse sequencing results

The bioinformat (URL_TO_INSERT_TERM_10942 https://fairsharing.org/search?recordType=model_and_format) ician performs the computational analysis, then the genotyping results are arch (URL_TO_INSERT_RECORD_10943 https://fairsharing.org/FAIRsharing.52b22c) ived into the LIMS.


### Step 7: Prepare genotyping dataset for submission of VCF file to EVA

In order to ensure interoperability of VCF (URL_TO_INSERT_RECORD_10944 https://fairsharing.org/FAIRsharing.cfzz0h)  files, in accordance with the good practice outlined in 
{footcite}`beier_f1000r_2022`, the following VCF (URL_TO_INSERT_RECORD_10946 https://fairsharing.org/FAIRsharing.cfzz0h)  meta-informat (URL_TO_INSERT_TERM_10945 https://fairsharing.org/search?recordType=model_and_format) ion lines should be used:


#### Obligatory meta-information line :

**##fileformat (URL_TO_INSERT_TERM_10947 https://fairsharing.org/search?recordType=model_and_format) ** : file format (URL_TO_INSERT_TERM_10948 https://fairsharing.org/search?recordType=model_and_format) . 

> Example:
>  `##fileformat (URL_TO_INSERT_TERM_10949 https://fairsharing.org/search?recordType=model_and_format) =VCF (URL_TO_INSERT_RECORD_10950 https://fairsharing.org/FAIRsharing.cfzz0h) v4.3  `


#### Recommended meta-information lines :

**##fileDate(Date)**: creation date of the VCF (URL_TO_INSERT_RECORD_10951 https://fairsharing.org/FAIRsharing.cfzz0h)  in the basic form without separator: YYYYMMDD 

> Example:
>  `##fileDate=20120921` 

**##bioinformat (URL_TO_INSERT_TERM_10952 https://fairsharing.org/search?recordType=model_and_format) ics_source (URL (URL_TO_INSERT_RECORD_10955 https://fairsharing.org/FAIRsharing.9d38e2)  or URI (URL_TO_INSERT_RECORD_10954 https://fairsharing.org/FAIRsharing.d261e1) )**: Analytic approach usually consisting (URL_TO_INSERT_RECORD_10956 https://fairsharing.org/FAIRsharing.q7bkqr)  of chains of bioinformat (URL_TO_INSERT_TERM_10953 https://fairsharing.org/search?recordType=model_and_format) ics tools for 
creating the VCF (URL_TO_INSERT_RECORD_10961 https://fairsharing.org/FAIRsharing.cfzz0h)  file specified as the DOI (URL_TO_INSERT_RECORD_10959 https://fairsharing.org/FAIRsharing.hFLKCn)  of a publication, or more generally as URL (URL_TO_INSERT_RECORD_10960 https://fairsharing.org/FAIRsharing.9d38e2) /URI (URL_TO_INSERT_RECORD_10958 https://fairsharing.org/FAIRsharing.d261e1) , like a public repository (URL_TO_INSERT_TERM_10957 https://fairsharing.org/search?recordType=repository)  for
the scripts used. The preferred way to describe this would be to use WorkflowHub (URL_TO_INSERT_RECORD_10964 https://fairsharing.org/FAIRsharing.07cf72)  (URL_TO_INSERT_RECORD_10965 https://fairsharing.org/FAIRsharing.07cf72) .eu (possibly in CWL (URL_TO_INSERT_RECORD_10963 https://fairsharing.org/FAIRsharing.8y5ayx)  format (URL_TO_INSERT_TERM_10962 https://fairsharing.org/search?recordType=model_and_format) ) and to be
fully transparent about the bioinformat (URL_TO_INSERT_TERM_10966 https://fairsharing.org/search?recordType=model_and_format) ics toolchain used to generate the results.

> Example:
> `##bioinformat (URL_TO_INSERT_TERM_10967 https://fairsharing.org/search?recordType=model_and_format) ics_source="doi.org/10.1038/s41588-018-0266-x"` 


**##reference_ac (assembly_accession)**: accession number, including the version, of the reference sequence on 
which the variation data of the present VCF (URL_TO_INSERT_RECORD_10968 https://fairsharing.org/FAIRsharing.cfzz0h)  is based. 

> Example: 
> ` ##reference_ac=GCA_902498975.1  `

**##reference_url (DOI (URL_TO_INSERT_RECORD_10971 https://fairsharing.org/FAIRsharing.hFLKCn) )**: a DOI (URL_TO_INSERT_RECORD_10972 https://fairsharing.org/FAIRsharing.hFLKCn)  (or URL (URL_TO_INSERT_RECORD_10973 https://fairsharing.org/FAIRsharing.9d38e2) /URI (URL_TO_INSERT_RECORD_10969 https://fairsharing.org/FAIRsharing.d261e1) ) for downloading of this reference genome, preferably from one INSD (URL_TO_INSERT_RECORD_10970 https://fairsharing.org/FAIRsharing.mKDii0) C (URL_TO_INSERT_RECORD_10974 https://fairsharing.org/FAIRsharing.3nx7t)  (URL_TO_INSERT_RECORD_10976 https://fairsharing.org/3547)  arch (URL_TO_INSERT_RECORD_10975 https://fairsharing.org/FAIRsharing.52b22c) ive. 

> Example: 
> `##reference_url="ftp.ncbi.nlm.nih.gov/genomes/all/GCA/902/498/975/GCA_902498975.1_Morex_v2.0/GCA_902498975.1_Morex_v2.0_genomic.fna.gz"` 


**##contig (&lt;ID=ctg1, length=sequence_length, assembly=gca_accession, md5=md5_hash, species=NCBITaxon:id>)** :
The individual sequence(s) of the reference genome. 

> Example: 
> `##contig=<ID=chr1H,length=522466905,assembly=GCA_902498975.1,md5=8d21a35cc68340ecf40e2a8dec9428fa,species=NCBITaxon:4513>`

**##SAM (URL_TO_INSERT_RECORD_10982 https://fairsharing.org/FAIRsharing.k97xzh) P (URL_TO_INSERT_RECORD_10978 https://fairsharing.org/FAIRsharing.kg1x4z)  (URL_TO_INSERT_RECORD_10980 https://fairsharing.org/FAIRsharing.dkKf7I) LE(<ID=$BioSample (URL_TO_INSERT_RECORD_10981 https://fairsharing.org/FAIRsharing.qr6pqk) _accession, DOI (URL_TO_INSERT_RECORD_10979 https://fairsharing.org/FAIRsharing.hFLKCn) =$url, ext_ID=$registry:identifier (URL_TO_INSERT_TERM_10977 https://fairsharing.org/search?recordType=identifier_schema) >)** : Describe the material whose variants 
are given in the genotype call columns in greater detail and can be extended using the specifications of the VCF (URL_TO_INSERT_RECORD_10984 https://fairsharing.org/FAIRsharing.cfzz0h)  format (URL_TO_INSERT_TERM_10983 https://fairsharing.org/search?recordType=model_and_format) .

In case no DOI (URL_TO_INSERT_RECORD_10985 https://fairsharing.org/FAIRsharing.hFLKCn)  exists and the material is held by a FAO (URL_TO_INSERT_RECORD_10986 https://fairsharing.org/FAIRsharing.k2dq5j)  (URL_TO_INSERT_RECORD_10987 https://fairsharing.org/FAIRsharing.xs6t67) -WIEWS ([https://www.fao.org/wiews/background/en/](https://www.fao.org/wiews/background/en/)) 
recognised institution (URL_TO_INSERT_TERM_10988 https://fairsharing.org/search?recordType=institution) , the external ID consists of the FAO (URL_TO_INSERT_RECORD_10989 https://fairsharing.org/FAIRsharing.k2dq5j)  (URL_TO_INSERT_RECORD_10990 https://fairsharing.org/FAIRsharing.xs6t67) -WIEWS instcode, the genus and the accession number (see example 2).
If the database (URL_TO_INSERT_TERM_10991 https://fairsharing.org/search?fairsharingRegistry=Database)  is not registered with FAO (URL_TO_INSERT_RECORD_10994 https://fairsharing.org/FAIRsharing.k2dq5j)  (URL_TO_INSERT_RECORD_10995 https://fairsharing.org/FAIRsharing.xs6t67) -WIEWS and is not available under a DOI (URL_TO_INSERT_RECORD_10993 https://fairsharing.org/FAIRsharing.hFLKCn) , the DNS of the holding institution (URL_TO_INSERT_TERM_10992 https://fairsharing.org/search?recordType=institution) ,
the database (URL_TO_INSERT_TERM_10996 https://fairsharing.org/search?fairsharingRegistry=Database)  identifier (URL_TO_INSERT_TERM_10997 https://fairsharing.org/search?recordType=identifier_schema) , the identifier (URL_TO_INSERT_TERM_10998 https://fairsharing.org/search?recordType=identifier_schema)  scheme and the identifier (URL_TO_INSERT_TERM_10999 https://fairsharing.org/search?recordType=identifier_schema)  value should be provided (see example 3).
For multiple external IDs the field should be used multiple times (delimited by commas). 

> Examples:
>
> * One genotype from a barley (_Hordeum vulgare_) GBS experiment with a DOI (URL_TO_INSERT_RECORD_11000 https://fairsharing.org/FAIRsharing.hFLKCn)  registered.
>
>       `##SAM (URL_TO_INSERT_RECORD_11004 https://fairsharing.org/FAIRsharing.k97xzh) P (URL_TO_INSERT_RECORD_11001 https://fairsharing.org/FAIRsharing.kg1x4z)  (URL_TO_INSERT_RECORD_11003 https://fairsharing.org/FAIRsharing.dkKf7I) LE=<ID=SAM (URL_TO_INSERT_RECORD_11005 https://fairsharing.org/FAIRsharing.k97xzh) EA104646767,DOI (URL_TO_INSERT_RECORD_11002 https://fairsharing.org/FAIRsharing.hFLKCn) ="doi.org/10.25642/IPK/GBIS/7811152">`
>
> 
> * One genotype from a barley (_Hordeum vulgare_) GBS experiment with the FAO (URL_TO_INSERT_RECORD_11007 https://fairsharing.org/FAIRsharing.k2dq5j)  (URL_TO_INSERT_RECORD_11008 https://fairsharing.org/FAIRsharing.xs6t67) -WIEWS code available but no DOI (URL_TO_INSERT_RECORD_11006 https://fairsharing.org/FAIRsharing.hFLKCn) .
>
>       `##SAM (URL_TO_INSERT_RECORD_11011 https://fairsharing.org/FAIRsharing.k97xzh) P (URL_TO_INSERT_RECORD_11009 https://fairsharing.org/FAIRsharing.kg1x4z)  (URL_TO_INSERT_RECORD_11010 https://fairsharing.org/FAIRsharing.dkKf7I) LE=<ID=SAM (URL_TO_INSERT_RECORD_11012 https://fairsharing.org/FAIRsharing.k97xzh) EA104646767,ext_ID="DEU146:Hordeum:HOR 1361 BRG">`
> 
> 
> * One genotype from a barley (_Hordeum vulgare_) GBS experiment with no DOI (URL_TO_INSERT_RECORD_11013 https://fairsharing.org/FAIRsharing.hFLKCn)  and no FAO (URL_TO_INSERT_RECORD_11014 https://fairsharing.org/FAIRsharing.k2dq5j)  (URL_TO_INSERT_RECORD_11015 https://fairsharing.org/FAIRsharing.xs6t67) -WIEWS code available.
> 
>       ##SAM (URL_TO_INSERT_RECORD_11018 https://fairsharing.org/FAIRsharing.k97xzh) P (URL_TO_INSERT_RECORD_11016 https://fairsharing.org/FAIRsharing.kg1x4z)  (URL_TO_INSERT_RECORD_11017 https://fairsharing.org/FAIRsharing.dkKf7I) LE=<ID=SAM (URL_TO_INSERT_RECORD_11019 https://fairsharing.org/FAIRsharing.k97xzh) EA104646767,ext_ID="ipk-gatersleben.de:GBIS:akzessionId:7811152">
> 

#### In case of adding new fields : 

Please check the official format (URL_TO_INSERT_TERM_11020 https://fairsharing.org/search?recordType=model_and_format)  specifications to avoid redundancy and possible incompatibilities.

### Step 8: Submit VCF file to EVA

Once the metadata and data has been format (URL_TO_INSERT_TERM_11021 https://fairsharing.org/search?recordType=model_and_format) ted according to the specifications above, make sure that the resulting VCF (URL_TO_INSERT_RECORD_11022 https://fairsharing.org/FAIRsharing.cfzz0h)  
file complies with VCF (URL_TO_INSERT_RECORD_11023 https://fairsharing.org/FAIRsharing.cfzz0h)  specifications. 
For that purpose, we propose the [VCF (URL_TO_INSERT_RECORD_11025 https://fairsharing.org/FAIRsharing.cfzz0h)  validator tool on GitHub](https://github.com (URL_TO_INSERT_RECORD_11024 https://fairsharing.org/FAIRsharing.c55d5e) /EBIvariation/vcf-validator)  

```bash
vcf_validator -i /path/to/file.vcf
```

```bash
vcf_validator -i /path/to/compressed_file.vcf.gz
```

Once the file has been fully validated without any error messages, you can submit the VCF (URL_TO_INSERT_RECORD_11027 https://fairsharing.org/FAIRsharing.cfzz0h)  file to EVA (URL_TO_INSERT_RECORD_11026 https://fairsharing.org/FAIRsharing.6824pv) , using 
BioSample (URL_TO_INSERT_RECORD_11029 https://fairsharing.org/FAIRsharing.qr6pqk) s IDs to identify the material, GCF/GCA accession for the reference genome assembly, and ENA (URL_TO_INSERT_RECORD_11028 https://fairsharing.org/FAIRsharing.dj8nt8)  accession numbers
for the sequencing reads of the material used. Refer to the official [documentation](https://www.ebi.ac.uk/eva (URL_TO_INSERT_RECORD_11030 https://fairsharing.org/FAIRsharing.6824pv) /?Submit-Data).
   
 
## Conclusion
At this point, the VCF (URL_TO_INSERT_RECORD_11032 https://fairsharing.org/FAIRsharing.cfzz0h)  contains metadata and data format (URL_TO_INSERT_TERM_11031 https://fairsharing.org/search?recordType=model_and_format) ted for the purpose of better discoverability and higher 
interoperability. 
Data could thus be more easily read and evaluated automatically by machines, and it is made easier to 
connect different data sources with each other, so that in general a higher degree of FAIR (URL_TO_INSERT_RECORD_11033 https://fairsharing.org/FAIRsharing.WWI10U)  has been achieved.

### What to read next? 

- [Learn to move through maturity levels with ISA metadata model](https://faircookbook.elixir-europe.org (URL_TO_INSERT_RECORD_11034 https://fairsharing.org/3531) /content/recipes/maturity/isa-maturity-progression.html) 
- [Learn to move expression allowed data use with ODR (URL_TO_INSERT_RECORD_11038 https://fairsharing.org/FAIRsharing.1sfhp3) L and DUO (URL_TO_INSERT_RECORD_11035 https://fairsharing.org/FAIRsharing.5dnjs2)  (URL_TO_INSERT_RECORD_11037 https://fairsharing.org/FAIRsharing.mjnypw) ](https://w3id.org (URL_TO_INSERT_RECORD_11036 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB035)
- [Learn to make computational workflows FAIR](https://w3id.org (URL_TO_INSERT_RECORD_11039 https://fairsharing.org/FAIRsharing.S6BoUk) /faircookbook/FCB062) 
- [Check the following resources:]()

````{rdmkit_panel}
````


## Reference

````{dropdown} **References**
```{footbibliography}
```
````


## Authors
````{authors_fairplus}
Sebastian: Writing - Original Draft
Cyril: Writing
Erwan: Writing
Isuru: Writing
Fuqi: Review & Editing
Philippe: Review & Editing
````



## Licence
````{license_fairplus}
CC-BY-4.0
````
