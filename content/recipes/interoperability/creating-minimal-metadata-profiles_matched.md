(fcb-interop-metadataprofile)=
# Creating a metadata profile


````{panels_fairplus}
```` 


## Graphical Overview



````{dropdown} 
```{figure} creating-minimal-metadata-profiles-mermaid.png
---
height: 1000px
name: Building a minimal metadata profile
alt: Building a minimal metadata profile
---
Building a minimal metadata profile.
```
````

---


## How to generate a metadata template

The following steps are intended as a starting point to guide the generation of a metadata template. 

### Step 1: Define competency questions
- What are the questions you would like to address with the template?
Without a set of competency questions, important variables may easily be forgotten. It is equally possible to collect too much metadata, making the resulting metadata model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) opaque and difficult to navigate. Competency questions serve as a guide to identify the most relevant experimental factors.

### Step 2: Define a Minimal Set Of Metadata (MSOM) according to these questions
- Compile metadata from different sources
- Generate a consolidated view on metadata by merging attributes as far as possible
- Differentiate metadata available for most of the studies from metadata occurring rarely (sparse matrix)
- Identify gaps in the metadata available for most of the studies comprising data that is considered important but has not been captured in the past
- Define a MSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)(URL_TO_INSERT_RECORD http://www.scai.fraunhofer.de/de/geschaeftsfelder/bioinformatik/downloads.html)M to be captured in the future from the metadata that is available for most of the studies and the metadata considered to be important
- Identify available community standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s regarding minimal sets of metadata
- Add metadata attributes from those community standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s to the MSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)(URL_TO_INSERT_RECORD http://www.scai.fraunhofer.de/de/geschaeftsfelder/bioinformatik/downloads.html)M, if they are not yet included
- Assign cardinality to the MSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)(URL_TO_INSERT_RECORD http://www.scai.fraunhofer.de/de/geschaeftsfelder/bioinformatik/downloads.html)M (identify mandatory metadata and how many times the attributes may be reported. Some metadata might not be mandatory but are still important to capture, if available)
- Identify appropriate ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) representing your data and establish an application ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) (see recipe 4 of UC3)
- Assign, as far as possible, ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) to the MSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)(URL_TO_INSERT_RECORD http://www.scai.fraunhofer.de/de/geschaeftsfelder/bioinformatik/downloads.html)M and the sparse matrix 

### Step 3: Introduce semantics into the template
- Identify most important objects to be represented in the model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) (e.g. study, sample, treatment, result, etc.)
- Make sure to have an appropriate naming strategy for the objects (e.g. an NGSstudy is an OMICSstudy is a Study; do not call an NGSstudy a Study; make sure the granularity fits your purposes)
- Assign MSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)(URL_TO_INSERT_RECORD http://www.scai.fraunhofer.de/de/geschaeftsfelder/bioinformatik/downloads.html)M and sparse matrix attributes to the respective objects
- Identify and introduce relationships among the identified objects (e.g. “an NGSstudy contains samples”, “a result is derived from a sample”) 
- Identify dependencies to data not represented as objects at this point in time, but, e.g. as termlists
- Make sure that your model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) can be expanded subsequently to represent those data as objects, as well
- Integrate the sparse matrix of metadata not contained in the MSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)(URL_TO_INSERT_RECORD http://www.scai.fraunhofer.de/de/geschaeftsfelder/bioinformatik/downloads.html)M in the model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)

### Step 4:  Reality check
- Introduce measures allowing to identify errors in reported data according to your model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)
- Expose your model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) to actual data delivered by independent colleagues and capture the errors and gaps that occurred
- Identify errors and gaps that are related to the model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) and not occurring due to errors in the data
- Adjust the model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) according to these errors and gaps
- Re-iterate the reality check until no more severe errors and gaps are occurring that are relevant for the previously defined competency questions


##  What to read next?

- {ref}`fcb-interop-covid-metadata`

````{rdmkit_panel}
````



## Authors

````{authors_fairplus}
````


## License

````{license_fairplus}
````



