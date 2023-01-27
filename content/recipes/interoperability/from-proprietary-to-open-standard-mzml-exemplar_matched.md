(fcb-interop-convertopen)=
# Converting from proprietary to open format



````{panels_fairplus}
```` 


## Main Objectives

- Document how to convert raw data from a propriatory, vendor specific format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) to an open standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format).
- Apply the approach to a targeted metabolic profiling using Bioc(URL_TO_INSERT_RECORD https://bioconductor.org)rates kit produced by IMI Resolute project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project).


---



## Graphical Overview


````{dropdown} 
```{figure} from-proprietary.png
---
width: 450px
name: Converting to an open standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) file format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)
alt: Converting to an open standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) file format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)
---
Converting to an open standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) file format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format).
```
````

---


## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [formatting](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/operation_3438)  | Waters MS format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)<!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO add a link to corresponding document -->  | [mzML](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.26dmba)  |
| [text annotation](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/operation_3778)  | [PSI-MS](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.284e1z)  | [annotated text](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/data_3779)  |



## Table of Data Standards

| Data Format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s  | Terminologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) | Model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s  |
| :------------- | :------------- | :------------- |
| [mzML](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.26dmba)  | [PSI-MS](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.284e1z)  |   |



---


## Ingredients

 Tools and  Software:

- [github(URL_TO_INSERT_RECORD https://github.com/)](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/)
- [docker](https://www.docker.com/)
- [python](https://www.python.org/)
<!-- - [zenodo(URL_TO_INSERT_RECORD https://www.zenodo.org) API](https://developers.zenodo.org/) -->

<!-- - [pandas](https://pandas.pydata.org/) -->

<!-- - [rdflib](https://rdflib.readthedocs.io/en/stable/)
- [jupyter notebook(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/3059)](https://jupyter.org/)
- [sparql](https://www.w3.org/TR/sparql11-query/) -->


## Converting Mass Spectrometry data to mzML format: a Step by Step Process.

### Step 1: obtain the dataset

In the case of the IMI RESO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)LUTE<!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO add a link to corresponding document --> project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project), the data is released via the University of Luxembourg<!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO add a link to corresponding document --> server (assuming you have access resolved):

```bash
```
:warning: `NN(URL_TO_INSERT_RECORD http://braininfo.org/Nnont.aspx)N.000.000.NN(URL_TO_INSERT_RECORD http://braininfo.org/Nnont.aspx)N` should be replaced with the proper IP address to the University of Luxembourg server once users have obtained data access clearance.

### Step 2: inspect the content of the archive

#### i. copying the archive to a working directory
```bash
```
#### ii. expand the archive

```bash
```
#### iii. inspect the folder

```bash
```

> :octopus: The arch(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)ive would have benefited from having a manifest file listing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) all the files and their associated checksums. In so doing, it would have allowed validation and verification that no corruption happened during file transfer.

> :octopus: Refer to the recipe: "How to calculate file checksums<!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO add a link to corresponding document -->"

> :octopus: Refer to the recipe: "How to package data for shipping with BDbags<!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO add a link to corresponding document -->"



### Step 3: Convert vendor specific format to an open format

One can consult the Elixir-UK [FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)sharing(URL_TO_INSERT_RECORD https://www.FAIRsharing.org)(URL_TO_INSERT_RECORD https://www.FAIRsharing.org) catalog](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/) of standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s and resources to discover if an open specification exists in the domain of mass spectrometry. In this case, there is as shown below. Note that every records in the catalog has a digital object identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)(URL_TO_INSERT_RECORD https://www.doi.org) (DOI(URL_TO_INSERT_RECORD https://www.doi.org)), https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.26dmba for HUPO(URL_TO_INSERT_RECORD http://plantontology.org/)-PSI(URL_TO_INSERT_RECORD http://www.psidev.info/) mzML(URL_TO_INSERT_RECORD http://www.psidev.info/mzml) specifications.

<!-- <div>
  <img src="/images/AWOWTbr.png" width="750" link="https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.26dmba">
</div> -->


````{dropdown} 
```{figure} /images/AWOWTbr.png
---
width: 750px
name: A Standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) Record in the FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)sharing(URL_TO_INSERT_RECORD https://www.FAIRsharing.org)(URL_TO_INSERT_RECORD https://www.FAIRsharing.org) catalog of resources
alt: A Standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) Record in the FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)sharing(URL_TO_INSERT_RECORD https://www.FAIRsharing.org)(URL_TO_INSERT_RECORD https://www.FAIRsharing.org) catalog of resources
---
The [HUPI-PSI mzML(URL_TO_INSERT_RECORD http://www.psidev.info/mzml) Standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) Record](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.26dmba) in the [Elixir FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)sharing(URL_TO_INSERT_RECORD https://www.FAIRsharing.org)(URL_TO_INSERT_RECORD https://www.FAIRsharing.org) catalog](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/) of resources.
```
````


The objective here is to conversion raw data in manufacturer format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) to an open format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format), which would allow data to be used without restrictions. To achieve this, we rely on a `containerized` version of the [Proteowizard](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/ProteoWizard/pwiz) {footcite}`Chambers2012`.

> **requirements**:

#### 1. install docker:

on a MacOS system, invoke the following:

```bash
```

#### 2. start and sign in to docker

```bash
```

#### 3. sign-up and/or login to https://hub.docker.com/

#### 4. pull the docker container for ProteoWizard

:warning: be sure to sign-up and login to https://hub.docker.com(URL_TO_INSERT_RECORD https://hub.docker.com/)/

```bash
```

* In order to be able to reach

https://hub.docker.com(URL_TO_INSERT_RECORD https://hub.docker.com/)/r/chambm/pwiz-skyline-i-agree-to-the-vendor-licenses


* Run the Proteowizard `pwiz tool` from the container over the WATERS(URL_TO_INSERT_RECORD http://rgd.mcw.edu/rgdweb/ontology/view.html?acc_id=RS:0000457) raw data, by issueing the following command from the terminal:

```bash
```

The command explained:


By essence, the resulting mzML(URL_TO_INSERT_RECORD http://www.psidev.info/mzml) files generated during the conversion are syntactically valid documents as the `pwiz` performs validation against the mzml xml schema during the serialization.

In some situations, the conversion will fails and no mzML(URL_TO_INSERT_RECORD http://www.psidev.info/mzml) output will be generated. Various reasons can explain failure to convert. The most common ones are corrupted:
 - raw data files 
 - unsupported vendor format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)

To address the former, it is good practice to compute a hash (md5, sha2) checksum fingerprinting each of the files. This allows to ensure that no file corruption has occurred during transfer and copy.

To address the latter, one should consult the table of compatibility:


|          Format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)         |    Status   |
|:----------------------- |:----------- |
| ABI T2D                 | not working |
| Agilent MHDAC(URL_TO_INSERT_RECORD https://ac.tdwg.org/introduction/) (non-IMS) | working     |
| Agilent MIDA(URL_TO_INSERT_RECORD https://ida.loni.usc.edu/)C(URL_TO_INSERT_RECORD https://ac.tdwg.org/introduction/) (IMS)     | working     |
| Bruker BAF              | working     |
| Bruker FID/YEP(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/1142)          | not working |
| Bruker TDF              | working     |
| Sciex WIFF              | working     |
| Sciex WIFF2             | working     |
| Shimadzu QQQ            | working     |
| Shimadzu QTO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)F(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/OF)           | working     |
| Thermo RAW              | working     |
| Waters RAW              | working     |
| Waters UNIF(URL_TO_INSERT_RECORD https://neuinfo.org)I            | not working |



#### 5. Testing and processing the resulting mzML files

For users unfam(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#fam)iliar with format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format), a search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) via popular search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) engine will yield options. Alternately, users may consult the Elixir Biotools registry for suggestions.

A number of libraries are available for parsing (reading and writing) `mzML(URL_TO_INSERT_RECORD http://www.psidev.info/mzml)` document. `mzML(URL_TO_INSERT_RECORD http://www.psidev.info/mzml)` is a king of `XML(URL_TO_INSERT_RECORD https://www.w3.org/TR/xml/)` format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) for which an XML(URL_TO_INSERT_RECORD https://www.w3.org/TR/xml/) schema has been defined and allows syntactic validation through standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) library in languages such as java, c++ or python. The top hit corresponds the the `pymzml` library {footcite}`Bald2012`.

<!-- <div>
<img src="/images/BT(URL_TO_INSERT_RECORD http://biotopontology.github.io/)s0GUS.png" width="750" border="1"/>
</div> -->


````{dropdown} 
```{figure} /images/BTs0GUS.png
---
width: 750px
name: pymzml in Biotools registry
alt: pymzml in Biotools registry
---
The Python `pymzml` library entry in the [Elixir Biotools catalog](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/) of resources.
```
````




```bash



```

<!-- <div>
<img src="/images/caaqwFo.png" width="650"/>
</div> -->


````{dropdown} 
```{figure} /images/caaqwFo.png
---
width: 650px
name: pymzml rendered msrun profile
alt: pymzml rendered msrun profile
---
The Python `pymzml` library rendering of a spectrum as extracted from an mzml format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ted mass spectrum data file.
```
````

In the follow-up recipe, we will show how to boostrap the creation of an ISA metadata file from a bag of mzML(URL_TO_INSERT_RECORD http://www.psidev.info/mzml) documents. But in the following, we'll show how to read an mzML(URL_TO_INSERT_RECORD http://www.psidev.info/mzml) file using a python library.

## Conclusion

In this recipe, we have shown how to convert a proprietary file format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) to an open standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format), using the exemplar situation of mass spectrometry data. Of course, there are many domain specific data format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)s and unfortunately not all benefit from the support of open source / open format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) communities. However by consulting the [Elixir UK](https://elixir-europe.org(URL_TO_INSERT_RECORD https://elixir-europe.org/)/about-us/who-we-are/nodes/uk) [FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)sharing(URL_TO_INSERT_RECORD https://www.FAIRsharing.org)(URL_TO_INSERT_RECORD https://www.FAIRsharing.org) registry](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)), it is possible to identify if such open format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) specifications are available.
Then, interrogating the [Biotools catalog](https://bio.tools(URL_TO_INSERT_RECORD https://bio.tools/)/), it may well be also possible to retrieve libraries and software components allowing manipulations of such format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format).



### What to read next?
- [How to calculate file checksums](fcb-checksum-create)<!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO add a link to corresponding document -->
- How to package data for shipping with BDbags<!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO add a link to corresponding document -->
- How to produce an ISA metadata file from a set of mzML(URL_TO_INSERT_RECORD http://www.psidev.info/mzml) fles<!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO add a link to corresponding document -->
- [How to deposit data to Zenodo(URL_TO_INSERT_RECORD https://www.zenodo.org)(URL_TO_INSERT_RECORD https://www.zenodo.org)](fcb-find-zenodo(URL_TO_INSERT_RECORD https://www.zenodo.org))<!-- TO(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab)DO add a link to corresponding document -->

````{rdmkit_panel}
````


## References

```{footbibliography}
```

<!-- 1. Chambers, M., Maclean, B., Burke, R. et al. A cross-platform toolkit for mass spectrometry and proteomics. Nat Biotechnol 30, 918-920 (2012). https://doi.org/10.1038/nbt.237
2. Bald T, Barth J, Niehues A, et al. pymzML(URL_TO_INSERT_RECORD http://www.psidev.info/mzml)--Python module for high-throughput bioinformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ics on mass spectrometry data. Bioinformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ics (Oxford, England). 2012 Apr;28(7):1052-1053. DOI(URL_TO_INSERT_RECORD https://www.doi.org): 10.1093/bioinformat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ics/bts066. -->


## Authors

````{authors_fairplus}
````


---

## License

````{license_fairplus}
````
