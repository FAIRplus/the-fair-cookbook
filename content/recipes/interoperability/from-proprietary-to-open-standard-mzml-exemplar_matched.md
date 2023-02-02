(fcb-interop-convertopen)=
# Converting from proprietary to open format



````{panels_fairplus}
:identifier_text: FCB029
:identifier_link: 'https://w3id.org/faircookbook/FCB029'
:difficulty_level: 3
:recipe_type: hands_on
:reading_time_minutes: 20
:intended_audience: principal_investigator, data_manager, data_scientist 
:maturity_level: 3
:maturity_indicator: 44
:has_executable_code: yeah
:recipe_name: Converting from proprietary to open format
```` 


## Main Objectives

- Document how to convert raw data from a propriatory, vendor specific format (URL_TO_INSERT_TERM_4890 https://fairsharing.org/search?recordType=model_and_format)  to an open standard (URL_TO_INSERT_TERM_4889 https://fairsharing.org/search?fairsharingRegistry=Standard)  format (URL_TO_INSERT_TERM_4891 https://fairsharing.org/search?recordType=model_and_format) .
- Apply the approach to a targeted metabolic profiling using Bioc (URL_TO_INSERT_RECORD_4893 https://fairsharing.org/FAIRsharing.81ettx) rates kit produced by IMI Resolute project (URL_TO_INSERT_TERM_4892 https://fairsharing.org/search?recordType=project) .


---



## Graphical Overview


````{dropdown} 
:open:
```{figure} from-proprietary.png
---
width: 450px
name: Converting to an open standard (URL_TO_INSERT_TERM_4894 https://fairsharing.org/search?fairsharingRegistry=Standard)  file format (URL_TO_INSERT_TERM_4895 https://fairsharing.org/search?recordType=model_and_format) 
alt: Converting to an open standard (URL_TO_INSERT_TERM_4896 https://fairsharing.org/search?fairsharingRegistry=Standard)  file format (URL_TO_INSERT_TERM_4897 https://fairsharing.org/search?recordType=model_and_format) 
---
Converting to an open standard (URL_TO_INSERT_TERM_4898 https://fairsharing.org/search?fairsharingRegistry=Standard)  file format (URL_TO_INSERT_TERM_4899 https://fairsharing.org/search?recordType=model_and_format) .
```
````

---


## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [formatting](http://edamontology.org/operation_3438)  | Waters MS format<!-- TODO add a link to corresponding document -->  | [mzML](https://fairsharing.org/FAIRsharing.26dmba)  |
| [text annotation](http://edamontology.org (URL_TO_INSERT_RECORD_4900 https://fairsharing.org/FAIRsharing.a6r7zs) /operation_3778)  | [PSI-MS](https://fairsharing.org (URL_TO_INSERT_RECORD_4902 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_4903 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_4904 https://fairsharing.org/3538) /FAIRsharing.284e1z)  | [annotated text](http://edamontology.org (URL_TO_INSERT_RECORD_4901 https://fairsharing.org/FAIRsharing.a6r7zs) /data_3779)  |



## Table of Data Standards

| Data Format (URL_TO_INSERT_TERM_4906 https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM_4907 https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM_4905 https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
| [mzML](https://fairsharing.org (URL_TO_INSERT_RECORD_4908 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_4910 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_4912 https://fairsharing.org/3538) /FAIRsharing.26dmba)  | [PSI-MS](https://fairsharing.org (URL_TO_INSERT_RECORD_4909 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_4911 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_4913 https://fairsharing.org/3538) /FAIRsharing.284e1z)  |   |



---


## Ingredients

 Tools and  Software:

- [github](https://github.com (URL_TO_INSERT_RECORD_4914 https://fairsharing.org/FAIRsharing.c55d5e) /)
- [docker](https://www.docker.com/)
- [python](https://www.python.org/)
<!-- - [zenodo API](https://developers.zenodo.org/) -->

<!-- - [pandas](https://pandas.pydata.org/) -->

<!-- - [rdflib](https://rdflib.readthedocs.io/en/stable/)
- [jupyter notebook](https://jupyter.org/)
- [sparql](https://www.w3.org/TR/sparql11-query/) -->


## Converting Mass Spectrometry data to mzML format: a Step by Step Process.

### Step 1: obtain the dataset

In the case of the IMI RESOLUTE<!-- TODO add a link to corresponding document --> project, the data is released via the University of Luxembourg<!-- TODO add a link to corresponding document --> server (assuming you have access resolved):

```bash
$> sftp fairplus@NNN.000.000.NNN
>get RESOLUTE_Targted_Metabolomics_of_parental_cell_lines.tar.gz
>exit
$>
```
:warning: `NNN.000.000.NNN` should be replaced with the proper IP address to the University of Luxembourg server once users have obtained data access clearance.

### Step 2: inspect the content of the archive

#### i. copying the archive to a working directory
```bash
$>mv RESOLUTE_Targted_Metabolomics_of_parental_cell_lines.tar.gz /IMI-FAIR+/RESOLUTE
$>cd /IMI-FAIR+/RESOLUTE/
```
#### ii. expand the archive

```bash
$>gunzip RESOLUTE_Targted_Metabolomics_of_parental_cell_lines.tar.gz
$>tar -xvf RESOLUTE_Targted_Metabolomics_of_parental_cell_lines.tar
$>cd RESOLUTE_Targted_Metabolomics_of_parental_cell_lines
```
#### iii. inspect the folder

```bash
>$anaconda3-2019.10) bob-MacBook-3:RESOLUTE_Targted_Metabolomics_of_parental_cell_lines philippe$ ls -la
total 1400
drwxr-xr-x   10 bob  staff     320 14 Jan 16:05 .
drwxr-xr-x    8 bob  staff     256 14 Jan 10:29 ..
-rwxr-xr-x@   1 bob  staff  520170 15 Nov 14:02 Data_Release_Proposal_20191115_Metabolome_of_parental_cell_lines.docx
-rw-r--r--@   1 bob  staff   72868  5 Nov 20:49 EX0003_processed_data.txt
-rw-r--r--@   1 bob  staff    6907 23 Oct 16:06 EX0003_sample_metadata.tsv
drwxr-xr-x@   7 bob  staff     224 14 Jan 10:43 Raw
drwxr-xr-x  118 bob  staff    3776 14 Jan 15:53 data
-rw-r--r--@   1 bob  staff   95677  7 Nov 11:02 p180_metabolites_metadata.tsv
-rw-r--r--@   1 bob  staff     162 14 Jan 10:59 ~$ta_Release_Proposal_20191115_Metabolome_of_parental_cell_lines.doc
```

> :octopus: The arch (URL_TO_INSERT_RECORD_4915 https://fairsharing.org/FAIRsharing.52b22c) ive would have benefited from having a manifest file listing all the files and their associated checksums. In so doing, it would have allowed validation and verification that no corruption happened during file transfer.

> :octopus: Refer to the recipe: "How to calculate file checksums<!-- TODO add a link to corresponding document -->"

> :octopus: Refer to the recipe: "How to package data for shipping with BDbags<!-- TODO add a link to corresponding document -->"



### Step 3: Convert vendor specific format to an open format

One can consult the Elixir-UK [FAIRsharing catalog](https://fairsharing.org (URL_TO_INSERT_RECORD_4921 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_4923 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_4925 https://fairsharing.org/3538) /) of standard (URL_TO_INSERT_TERM_4916 https://fairsharing.org/search?fairsharingRegistry=Standard) s and resources to discover if an open specification exists in the domain of mass spectrometry. In this case, there is as shown below. Note that every records in the catalog has a digital object identifier (URL_TO_INSERT_TERM_4917 https://fairsharing.org/search?recordType=identifier_schema)  (URL_TO_INSERT_RECORD_4918 https://fairsharing.org/FAIRsharing.hFLKCn)  (DOI), https://fairsharing.org (URL_TO_INSERT_RECORD_4922 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_4924 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_4926 https://fairsharing.org/3538) /FAIRsharing.26dmba for HUPO-PSI (URL_TO_INSERT_RECORD_4920 https://fairsharing.org/3514)  mzML (URL_TO_INSERT_RECORD_4919 https://fairsharing.org/FAIRsharing.26dmba)  specifications.

<!-- <div>
  <img src="/images/AWOWTbr.png" width="750" link="https://fairsharing.org/FAIRsharing.26dmba">
</div> -->


````{dropdown} 
:open:
```{figure} /images/AWOWTbr.png
---
width: 750px
name: A Standard (URL_TO_INSERT_TERM_4927 https://fairsharing.org/search?fairsharingRegistry=Standard)  Record in the FAIR (URL_TO_INSERT_RECORD_4929 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_4928 https://fairsharing.org/FAIRsharing.2abjs5)  catalog of resources
alt: A Standard (URL_TO_INSERT_TERM_4930 https://fairsharing.org/search?fairsharingRegistry=Standard)  Record in the FAIR (URL_TO_INSERT_RECORD_4932 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_4931 https://fairsharing.org/FAIRsharing.2abjs5)  catalog of resources
---
The [HUPI-PSI mzML Standard Record](https://fairsharing.org (URL_TO_INSERT_RECORD_4935 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_4937 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_4939 https://fairsharing.org/3538) /FAIRsharing.26dmba) in the [Elixir FAIR (URL_TO_INSERT_RECORD_4934 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_4933 https://fairsharing.org/FAIRsharing.2abjs5)  catalog](https://fairsharing.org (URL_TO_INSERT_RECORD_4936 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_4938 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_4940 https://fairsharing.org/3538) /) of resources.
```
````


The objective here is to conversion raw data in manufacturer format (URL_TO_INSERT_TERM_4941 https://fairsharing.org/search?recordType=model_and_format)  to an open format (URL_TO_INSERT_TERM_4942 https://fairsharing.org/search?recordType=model_and_format) , which would allow data to be used without restrictions. To achieve this, we rely on a `containerized` version of the [Proteowizard](https://github.com (URL_TO_INSERT_RECORD_4943 https://fairsharing.org/FAIRsharing.c55d5e) /ProteoWizard/pwiz) {footcite}`Chambers2012`.

> **requirements**:

#### 1. install docker:

on a MacOS system, invoke the following:

```bash
>brew update
>brew install docker
```

#### 2. start and sign in to docker

```bash
>docker start
>docker login
```

#### 3. sign-up and/or login to https://hub.docker.com/

#### 4. pull the docker container for ProteoWizard

:warning: be sure to sign-up and login to https://hub.docker.com (URL_TO_INSERT_RECORD_4944 https://fairsharing.org/FAIRsharing.afc2b3) /

```bash
>docker pull chambm/pwiz-i-agree-to-the-vendor-licenses
```

* In order to be able to reach

https://hub.docker.com (URL_TO_INSERT_RECORD_4945 https://fairsharing.org/FAIRsharing.afc2b3) /r/chambm/pwiz-skyline-i-agree-to-the-vendor-licenses


* Run the Proteowizard `pwiz tool` from the container over the WATERS raw data, by issueing the following command from the terminal:

```bash
>docker run -it --rm -e WINEDEBUG=-all -v /Users/bob/Documents/IMI-FAIR+/Resolute/RESOLUTE_Targted_Metabolomics_of_parental_cell_lines/Raw/MCC025_p180_102024_102059_20190125/raw\ data/KIT2-0-8015_1024503073/:/data chambm/pwiz-skyline-i-agree-to-the-vendor-licenses wine msconvert /data/KIT2-0-8015_1024503073_01_0_1_1_10_11000002.raw --mzML
```

The command explained:


By essence, the resulting mzML (URL_TO_INSERT_RECORD_4946 https://fairsharing.org/FAIRsharing.26dmba)  files generated during the conversion are syntactically valid documents as the `pwiz` performs validation against the mzml xml schema during the serialization.

In some situations, the conversion will fails and no mzML (URL_TO_INSERT_RECORD_4947 https://fairsharing.org/FAIRsharing.26dmba)  output will be generated. Various reasons can explain failure to convert. The most common ones are corrupted:
 - raw data files 
 - unsupported vendor format (URL_TO_INSERT_TERM_4948 https://fairsharing.org/search?recordType=model_and_format) 

To address the former, it is good practice to compute a hash (md5, sha2) checksum fingerprinting each of the files. This allows to ensure that no file corruption has occurred during transfer and copy.

To address the latter, one should consult the table of compatibility:


|          Format (URL_TO_INSERT_TERM_4949 https://fairsharing.org/search?recordType=model_and_format)          |    Status   |
|:----------------------- |:----------- |
| ABI T2D                 | not working |
| Agilent MHDAC (non-IMS) | working     |
| Agilent MIDAC (IMS)     | working     |
| Bruker BAF              | working     |
| Bruker FID/YEP          | not working |
| Bruker TDF              | working     |
| Sciex WIFF              | working     |
| Sciex WIFF2             | working     |
| Shimadzu QQQ            | working     |
| Shimadzu QTOF           | working     |
| Thermo RAW              | working     |
| Waters RAW              | working     |
| Waters UNIFI            | not working |



#### 5. Testing and processing the resulting mzML files

For users unfam (URL_TO_INSERT_RECORD_4951 https://fairsharing.org/FAIRsharing.d0886a) iliar with format (URL_TO_INSERT_TERM_4950 https://fairsharing.org/search?recordType=model_and_format) , a search (URL_TO_INSERT_RECORD_4952 https://fairsharing.org/FAIRsharing.52b22c)  via popular search (URL_TO_INSERT_RECORD_4953 https://fairsharing.org/FAIRsharing.52b22c)  engine will yield options. Alternately, users may consult the Elixir Biotools registry for suggestions.

A number of libraries are available for parsing (reading and writing) `mzML (URL_TO_INSERT_RECORD_4957 https://fairsharing.org/FAIRsharing.26dmba) ` document. `mzML (URL_TO_INSERT_RECORD_4958 https://fairsharing.org/FAIRsharing.26dmba) ` is a king of `XML` format (URL_TO_INSERT_TERM_4955 https://fairsharing.org/search?recordType=model_and_format)  for which an XML (URL_TO_INSERT_RECORD_4956 https://fairsharing.org/FAIRsharing.b5cc91)  schema has been defined and allows syntactic validation through standard (URL_TO_INSERT_TERM_4954 https://fairsharing.org/search?fairsharingRegistry=Standard)  library in languages such as java, c++ or python. The top hit corresponds the the `pymzml` library {footcite}`Bald2012`.

<!-- <div>
<img src="/images/BTs0GUS.png" width="750" border="1"/>
</div> -->


````{dropdown} 
:open:
```{figure} /images/BTs0GUS.png
---
width: 750px
name: pymzml in Biotools registry
alt: pymzml in Biotools registry
---
The Python `pymzml` library entry in the [Elixir Biotools catalog](https://bio.tools (URL_TO_INSERT_RECORD_4959 https://fairsharing.org/FAIRsharing.63520c) /) of resources.
```
````




```bash
import os
import sys
import pymzml
from pymzml.plot import Factory

mzml_file ="KIT3-0-8015_1024503088_42_0_1_1_00_1024502932.mzML"
msrun = pymzml.run.Reader(mzml_file)

mzml_basename = os.path.basename(mzml_file)
pf = Factory()
pf.new_plot()
pf.add(msrun["TIC"].peaks(), color=(0, 0, 0), style="lines", title=mzml_basename)
pf.save(
        "chromatogram_{0}.html".format(mzml_basename),
        layout={"xaxis": {"title": "Retention time"}, "yaxis": {"title": "TIC"}},
)

```

<!-- <div>
<img src="/images/caaqwFo.png" width="650"/>
</div> -->


````{dropdown} 
:open:
```{figure} /images/caaqwFo.png
---
width: 650px
name: pymzml rendered msrun profile
alt: pymzml rendered msrun profile
---
The Python `pymzml` library rendering of a spectrum as extracted from an mzml format (URL_TO_INSERT_TERM_4960 https://fairsharing.org/search?recordType=model_and_format) ted mass spectrum data file.
```
````

In the follow-up recipe, we will show how to boostrap the creation of an ISA metadata file from a bag of mzML (URL_TO_INSERT_RECORD_4961 https://fairsharing.org/FAIRsharing.26dmba)  documents. But in the following, we'll show how to read an mzML (URL_TO_INSERT_RECORD_4962 https://fairsharing.org/FAIRsharing.26dmba)  file using a python library.

## Conclusion

In this recipe, we have shown how to convert a proprietary file format (URL_TO_INSERT_TERM_4964 https://fairsharing.org/search?recordType=model_and_format)  to an open standard (URL_TO_INSERT_TERM_4963 https://fairsharing.org/search?fairsharingRegistry=Standard)  format (URL_TO_INSERT_TERM_4965 https://fairsharing.org/search?recordType=model_and_format) , using the exemplar situation of mass spectrometry data. Of course, there are many domain specific data format (URL_TO_INSERT_TERM_4966 https://fairsharing.org/search?recordType=model_and_format) s and unfortunately not all benefit from the support of open source / open format (URL_TO_INSERT_TERM_4967 https://fairsharing.org/search?recordType=model_and_format)  communities. However by consulting the [Elixir UK](https://elixir-europe.org (URL_TO_INSERT_RECORD_4969 https://fairsharing.org/3531) /about-us/who-we-are/nodes/uk) [FAIR (URL_TO_INSERT_RECORD_4971 https://fairsharing.org/FAIRsharing.WWI10U) sharing (URL_TO_INSERT_RECORD_4970 https://fairsharing.org/FAIRsharing.2abjs5)  registry](https://fairsharing.org (URL_TO_INSERT_RECORD_4972 https://fairsharing.org/3518)  (URL_TO_INSERT_RECORD_4973 https://fairsharing.org/3536)  (URL_TO_INSERT_RECORD_4974 https://fairsharing.org/3538) ), it is possible to identify if such open format (URL_TO_INSERT_TERM_4968 https://fairsharing.org/search?recordType=model_and_format)  specifications are available.
Then, interrogating the [Biotools catalog](https://bio.tools (URL_TO_INSERT_RECORD_4976 https://fairsharing.org/FAIRsharing.63520c) /), it may well be also possible to retrieve libraries and software components allowing manipulations of such format (URL_TO_INSERT_TERM_4975 https://fairsharing.org/search?recordType=model_and_format) .



### What to read next?
- [How to calculate file checksums](fcb-checksum-create)<!-- TODO add a link to corresponding document -->
- How to package data for shipping with BDbags<!-- TODO add a link to corresponding document -->
- How to produce an ISA metadata file from a set of mzML fles<!-- TODO add a link to corresponding document -->
- [How to deposit data to Zenodo](fcb-find-zenodo)<!-- TODO add a link to corresponding document -->

````{rdmkit_panel}
````


## References

```{footbibliography}
```

<!-- 1. Chambers, M., Maclean, B., Burke, R. et al. A cross-platform toolkit for mass spectrometry and proteomics. Nat Biotechnol 30, 918-920 (2012). https://doi.org/10.1038/nbt.237
2. Bald T, Barth J, Niehues A, et al. pymzML--Python module for high-throughput bioinformatics on mass spectrometry data. Bioinformatics (Oxford, England). 2012 Apr;28(7):1052-1053. DOI: 10.1093/bioinformatics/bts066. -->


## Authors

````{authors_fairplus}
Philippe: Writing - Original Draft
Susanna: Writing - Review & Editing, Funding acquisition
Robert: Writing - Review & Editing
````


---

## License

````{license_fairplus}
CC-BY-4.0
````
