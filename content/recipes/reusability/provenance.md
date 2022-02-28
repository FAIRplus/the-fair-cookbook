(fcb-reusability-provenance)=
# Provenance information

````{panels_fairplus}
:identifier_text: FCB036
:identifier_link: 'https://w3id.org/faircookbook/FCB036'
:difficulty_level: 3
:recipe_type: hands_on
:reading_time_minutes: 20
:intended_audience: principal_investigator, data_manager, data_scientist  
:has_executable_code: nope
:recipe_name: Provenance information
```` 

<!-- 
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
<i class="fa fa-fire fa-lg" style="color:#7e0038;"></i>
<i class="fa fa-fire fa-lg" style="color:lightgrey"></i>
<i class="fa fa-fire fa-lg" style="color:lightgrey"></i>

---
<i class="fas fa-clock fa-2x" style="color:#7e0038;"></i>
^^^
<h4><b>Reading Time</b></h4>
<i class="fa fa-clock fa-lg" style="color:#7e0038;"></i> 30 minutes
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
 -->

## Main Objectives

In all tasks of data integration, especially in the area of Pharma, ensuring trust in data sources is essential. The steps taken to ensure new datasets or sources of information meet a number of criteria ascertaining some level of quality are many. One of them is a check on the origin of the information, in other words, its `Provenance`. Provenance covers the elements detailing how the data was produced by identifying the agents (human, software, workflows) so a certain level of traceability and accountability can be established. The notions of `audit and trail` as well as `versioning` and `authorship` are essential to be able, should any distortion be identified in downstream analysis, to trace back to possible sources of error.

## Introduction

Data provenance https://en.wikipedia.org/wiki/Data_lineage

## PROV vocabulary

The W3C vetted a specification for an RDF vocabulary to express provenance information, the [W3C PROV](https://www.w3.org/TR/prov-overview/). Implementation can be made in RDF or JSON, since JSON-LD is now an official serialization of RDF.


## CamFLow

[CamFlow](https://camflow.org/#output_format) is a Linux Security Module (LSM) designed to capture data provenance for the purpose of system audit {footcite}`Pasquier2017Camflow`.

CamFlow support 2 output formats.

- W3C PROV-JSON format

```bash
"ABAAAAAAACAe9wIAAAAAAE7aeaI+200UAAAAAAAAAAA=": {
    "cf:id": "194334",
    "prov:type": "fifo",
    "cf:boot_id": 2725894734,
    "cf:machine_id": 340646718,
    "cf:version": 0,
    "cf:date": "2017:01:03T16:43:30",
    "cf:jiffies": "4297436711",
    "cf:uid": 1000,
    "cf:gid": 1000,
    "cf:mode": "0x1180",
    "cf:secctx": "unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023",
    "cf:ino": 51964,
    "cf:uuid": "32b7218a-01a0-c7c9-17b1-666f200b8912",
    "prov:label": "[fifo] 0"
}

```



Example of a write edge in W3C PROV format:
```bash
"QAAAAAAAQIANAAAAAAAAAE7aeaI+200UAAAAAAAAAAA=": {
    "cf:id": "13",
    "prov:type": "write",
    "cf:boot_id": 2725894734,
    "cf:machine_id": 340646718,
    "cf:date": "2017:01:03T16:43:30",
    "cf:jiffies": "4297436711",
    "prov:label": "write",
    "cf:allowed": "true",
    "prov:activity": "AQAAAAAAAEAf9wIAAAAAAE7aeaI+200UAQAAAAAAAAA=",
    "prov:entity": "ABAAAAAAACAe9wIAAAAAAE7aeaI+200UAQAAAAAAAAA=",
    "cf:offset": "0"
}
```
<!-- 
## Workflow information: -->





## Conclusion

### What to read next?
	> * [How to meet community standards for annotation](./community-standards)


<!--## References

``{bibliography} ./../../_bibliography/bibliography-identifier-mapping.bib
:filter: docname in docnames
``` -->

<!-- {download}`bibliography-identifier-mapping.bib <../interoperability/bibref/bibliography-identifier-mapping.bib>` -->

## References

```{footbibliography}
```


---

## Authors

````{authors_fairplus}
Philippe: Writing - Original Draft
````


---

## License

````{license_fairplus}
CC-BY-4.0
````
