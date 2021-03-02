(fcb-interop-convertopen)=
# From proprietary to open standard data format

+++
<br/>

----

````{panels}
:container: container-lg pb-3
:column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-1
:card: rounded

<i class="fa fa-qrcode fa-2x" style="color:#7e0038;"></i>
^^^
<h4><b>Recipe metadata</b></h4>
 identifier: <a href="">RX.X</a> 
 version: <a href="">v1.0</a>

---
<i class="fa fa-fire fa-2x" style="color:#7e0038;"></i>
^^^
<h4><b>Difficulty level</b></h4>
<i class="fa fa-fire fa-lg" style="color:#7e0038;"></i>
<i class="fa fa-fire fa-lg" style="color:#7e0038;"></i>
<i class="fa fa-fire fa-lg" style="color:l#7e0038;"></i>
<i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
<i class="fa fa-fire fa-lg" style="color:lightgrey"></i>

---
<i class="fas fa-clock fa-2x" style="color:#7e0038;"></i>
^^^
<h4><b>Reading Time</b></h4>
<i class="fa fa-clock fa-lg" style="color:#7e0038;"></i> 20 minutes
<h4><b>Recipe Type</b></h4>
<i class="fa fa-laptop fa-lg" style="color:#7e0038;"></i> Hands-on
<h4><b>Executable Code</b></h4>
<i class="fa fa-play-circle fa-lg" style="color:#7e0038;"></i> Yes

---
<i class="fa fa-users fa-2x" style="color:#7e0038;"></i>
^^^
<h4><b>Intended Audience</b></h4>
<p> <i class="fa fa-user-md fa-lg" style="color:#7e0038;"></i> Principal Investigator </p>
<p> <i class="fa fa-database fa-lg" style="color:#7e0038;"></i> Data Manager </p>
<p> <i class="fa fa-wrench fa-lg" style="color:#7e0038;"></i> Data Scientist </p>
````

---


## Main Objectives

- Document how to convert raw data from a propriatory, vendor specific format to an open standard format.
- Apply the approach to an IMI dataset, more specifically  a targeted metabolic profiling using Biocrates kit produced by IMI Resolute project.


___



## Graphical Overview


```{figure} from-proprietary.png
---
width: 450px
name: Converting to an open standard file format
alt: Converting to an open standard file format
---
Converting to an open standard file format.
```

___

## Capability & Maturity Table

| Capability  | Initial Maturity Level | Final Maturity Level  |
| :------------- | :------------- | :------------- |
| Interoperability | minimal | repeatable |

----

## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [formatting](http://edamontology.org/operation_3438)  | [Waters MS format]()  | [mzML](https://fairsharing.org/FAIRsharing.26dmba)  |
| [text annotation](http://edamontology.org/operation_3778)  | [PSI-MS](https://fairsharing.org/FAIRsharing.284e1z)  | [annotated text](http://edamontology.org/data_3779)  |



## Table of Data Standards

| Data Formats  | Terminologies | Models  |
| :------------- | :------------- | :------------- |
| [mzML](https://fairsharing.org/FAIRsharing.26dmba)  | [PSI-MS](https://fairsharing.org/FAIRsharing.284e1z)  |   |



___


## Ingredients

 Tools and  Software:

- [github](https://github.com/)
- [docker](https://www.docker.com/)
- [python](https://www.python.org/)
<!-- - [zenodo API](https://developers.zenodo.org/) -->

<!-- - [pandas](https://pandas.pydata.org/) -->

<!-- - [rdflib](https://rdflib.readthedocs.io/en/stable/)
- [jupyter notebook](https://jupyter.org/)
- [sparql](https://www.w3.org/TR/sparql11-query/) -->


## Converting Mass Spectrometry data to mzML format: a Step by Step Process.

### Step 1: obtain the dataset

In the case of the [IMI RESOLUTE]() project, the data is released via the [University of Luxembourg]() server (assuming you have access resolved):

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

> :octopus: The archive would have benefitted from having a manifest file listing all the files and their associated checksums. In so doing, it would have allowed validation and verification that no corruption happened during file transfer.

> :octopus: Refer to the recipe: "[How to calculate file checksums]()"

> :octopus: Refer to the recipe: "[How to package data for shipping with BDbags]()"



### Step 3: Convert vendor specific format to an open format

One can consult the Elixir-UK [FAIRsharing catalog](https://fairsharing.org/) of standards and resources to discover if an open specification exists in the domain of mass spectrometry. In this case, there is as shown below. Note that every records in the catalog has a digital object identifier (DOI), https://fairsharing.org/FAIRsharing.26dmba for HUPO-PSI mzML specifications.

<!-- <div>
  <img src="https://i.imgur.com/AWOWTbr.png" width="750" link="https://fairsharing.org/FAIRsharing.26dmba">
</div> -->

```{figure} https://i.imgur.com/AWOWTbr.png
---
width: 750px
name: A Standard Record in the FAIRsharing catalog of resources
alt: A Standard Record in the FAIRsharing catalog of resources
---
The [HUPI-PSI mzML Standard Record](https://fairsharing.org/FAIRsharing.26dmba) in the [Elixir FAIRsharing catalog](https://fairsharing.org/) of resources.
```



The objective here is to conversion raw data in manufacturer format to an open format, which would allow data to be used without restrictions. To achieve this, we rely on a `containerized` version of the [Proteowizard](https://github.com/ProteoWizard/pwiz).

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

#### 4. pull the docker container for ProteoWizard:

:warning: be sure to sign-up and login to https://hub.docker.com/

```bash
>docker pull chambm/pwiz-i-agree-to-the-vendor-licenses
```

* In order to be able to reach

https://hub.docker.com/r/chambm/pwiz-skyline-i-agree-to-the-vendor-licenses


* Run the Proteowizard `pwiz tool` from the container over the WATERS raw data, by issueing the following command from the terminal:

```bash
>docker run -it --rm -e WINEDEBUG=-all -v /Users/bob/Documents/IMI-FAIR+/Resolute/RESOLUTE_Targted_Metabolomics_of_parental_cell_lines/Raw/MCC025_p180_102024_102059_20190125/raw\ data/KIT2-0-8015_1024503073/:/data chambm/pwiz-skyline-i-agree-to-the-vendor-licenses wine msconvert /data/KIT2-0-8015_1024503073_01_0_1_1_10_11000002.raw --mzML
```

The command explained:


By essence, the resulting mzML files generated during the conversion are syntactically valid documents as the `pwiz` performs validation against the mzml xml schema during the serialization.

In some situations, the conversion will fails and no mzML output will be generated. Various reasons can explain failure to convert. The most common ones are corrupted:
 - raw data files 
 - unsupported vendor format

To address the former, it is good practice to compute a hash (md5, sha2) checksum fingerprinting each of the files. This allows to ensure that no file corruption has occurred during transfer and copy.

To address the latter, one should consult to table of compatibility:


|          Format         |    Status   |
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



#### 5. Testing and processing the resulting mzML files:

for users unfamiliar with format, a search via popular search engine will yield options. Alternately, users may consult the Elixir Biotools registry for suggestions.

A number of libraries are available for parsing (reading and writing) `mzML` document. `mzML` is a king of `XML` format for which an XML schema has been defined and allows syntactic validation through standard library in languages such as java, c++ or python. The top hit corresponds the the `pymzml` library.

<!-- <div>
<img src="https://i.imgur.com/BTs0GUS.png" width="750" border="1"/>
</div> -->

```{figure} https://i.imgur.com/BTs0GUS.png
---
width: 750px
name: pymzml in Biotools registry
alt: pymzml in Biotools registry
---
The Python `pymzml` library entry in the [Elixir Biotools catalog](https://biotools.org/) of resources.
```




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
<img src="https://i.imgur.com/caaqwFo.png" width="650"/>
</div> -->

```{figure} https://i.imgur.com/caaqwFo.png
---
width: 650px
name: pymzml rendered msrun profile
alt: pymzml rendered msrun profile
---
The Python `pymzml` library rendering of a spectrum as extracted from an mzml formatted mass spectrum data file.
```


In the follow-up recipe, we will show how to boostrap the creation of an ISA metadata file from a bag of mzML documents. But in the following, we'll show how to read an mzML file using a python library.

## Conclusion

In this recipe, we have shown how to convert a proprietary file format to an open standard format, using the exemplar situation of mass spectrometry data. Of course, there are many domain specific data formats and unfortunately not all benefit from the support of open source / open format communities. However by consulting the [Elixir UK](https://Elixirhug.org) [FAIRsharing registry](https://fairsharing.org), it is possible to identify if such open format specifications are available.
Then, interrogating the [Biotools catalog](https://bio.tools/), it may well be also possible to retrieve libraries and software components allowing manipulations of such format.



> ### What to read next
  >  - [How to calculate file checksums]()
  >  - [How to package data for shipping with BDbags]()
  >  - [How to produce an ISA metadata file from a set of mzML fles]()
  >  - [How to deposit data to Zenodo]()

___


## References
1. Chambers, M., Maclean, B., Burke, R. et al. A cross-platform toolkit for mass spectrometry and proteomics. Nat Biotechnol 30, 918–920 (2012). https://doi.org/10.1038/nbt.237
2. Bald T, Barth J, Niehues A, et al. pymzML--Python module for high-throughput bioinformatics on mass spectrometry data. Bioinformatics (Oxford, England). 2012 Apr;28(7):1052-1053. DOI: 10.1093/bioinformatics/bts066.


## Authors

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Philippe Rocca-Serra |  University of Oxford, Data Readiness Group| [0000-0001-9853-5668](https://orcid.org/orcid.org/0000-0001-9853-5668) | Writing - Original Draft |
| Susanna-Assunta Sansone |  University of Oxford, Data Readiness Group | | Writing - Review & Editing, Funding acquisition | 
||||Review|
||||Contribution|

___

## License

This page is released under the Creative Commons 4.0 BY license.

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png" height="20"/></a>
