(fcb-reusability-provenance)=
# Provenance Information

+++
<br/>

````{panels_fairplus}
:identifier_text: RX.X
:identifier_link: 'https://example.com'
:difficulty_level: 3
:recipe_type: hands_on
:reading_time_minutes: 30
:intended_audience: principal_investigator, data_manager, data_scientist  
:has_executable_code: yeah
:recipe_name: Provenance Information
```` 

## Main Objectives

In all tasks of data integration, especially in the area of Pharma, ensuring trust in data sources is essentially. The steps taken to ensure new datasets or sources of information meet a number of criteria ascertaining some level of quality are many. One of them is a check on the origin of the information, in other words, its Provenance. Provenance covers the elements detailing how the data was produced by identifying the agents (human, software, workflows) so a certain level of tracability and accountability can be established. The notions of `audit and trail` as well as `versioning` and `authorshipt` are essential to be able, should any distortion be identified in downstream analysis, to trace back to possible sources of error.

## Introduction

Data provenance https://en.wikipedia.org/wiki/Data_lineage

## PROV vocabulary

The W3C vetted a specification for an RDF vocabulary to express provenance information. Implementation can be made in RDF or JSON, since JSON-LD is now an official serialization of RDF.
The [W3C PROV ](https://www.w3.org/TR/prov-overview/)

[!image](https://www.w3.org/TR/prov-overview/)

## CamFLow

[CamFlow](https://camflow.org/#output_format) is a Linux Security Module (LSM) designed to capture data provenance for the purpose of system audit {cite}`Pasquier2017Camflow`.

CamFlow support 2 output formats.

-W3C PROV-JSON format

```json
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
```json
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

## Workflow information:





## Conclusion

### What to read next?
	> * [How to meet community standards for annotation](./community-standards)


## References

```{bibliography}
:filter: docname in docnames
```

___

## Authors

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Philippe Rocca-Serra |  University of Oxford, Data Readiness Group| [0000-0001-9853-5668](https://orcid.org/orcid.org/0000-0001-9853-5668) | Writing - Original Draft, Shex expression, ontology mapping |


___

## License

This page is released under the Creative Commons 4.0 BY license.

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png" height="20"/></a>
