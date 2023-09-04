(fcb-interop-metadataprofile)=
# Creating a metadata profile


````{panels_fairplus}
:identifier_text: FCB026
:identifier_link: 'https://w3id.org/faircookbook/FCB026'
:difficulty_level: 4
:recipe_type: hands_on
:reading_time_minutes: 20
:intended_audience: principal_investigator, data_manager, data_scientist 
:maturity_level: 0
:maturity_indicator: 0
:has_executable_code: nope
:recipe_name: Creating a metadata profile
```` 


## Graphical Overview



````{dropdown} 
:open:
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
Without a set of competency questions, important variables may easily be forgotten. It is equally possible to collect too much metadata, making the resulting metadata model opaque and difficult to navigate. Competency questions serve as a guide to identify the most relevant experimental factors.

### Step 2: Define a Minimal Set Of Metadata (MSOM) according to these questions
- Compile metadata from different sources
- Generate a consolidated view on metadata by merging attributes as far as possible
- Differentiate metadata available for most of the studies from metadata occurring rarely (sparse matrix)
- Identify gaps in the metadata available for most of the studies comprising data that is considered important but has not been captured in the past
- Define a MSOM to be captured in the future from the metadata that is available for most of the studies and the metadata considered to be important
- Identify available community standards regarding minimal sets of metadata
- Add metadata attributes from those community standards to the MSOM, if they are not yet included
- Assign cardinality to the MSOM (identify mandatory metadata and how many times the attributes may be reported. Some metadata might not be mandatory but are still important to capture, if available)
- Identify appropriate ontologies representing your data and establish an application ontology (see recipe 4 of UC3)
- Assign, as far as possible, ontologies to the MSOM and the sparse matrix 

### Step 3: Introduce semantics into the template
- Identify most important objects to be represented in the model (e.g. study, sample, treatment, result, etc.)
- Make sure to have an appropriate naming strategy for the objects (e.g. an NGSstudy is an OMICSstudy is a Study; do not call an NGSstudy a Study; make sure the granularity fits your purposes)
- Assign MSOM and sparse matrix attributes to the respective objects
- Identify and introduce relationships among the identified objects (e.g. “an NGSstudy contains samples”, “a result is derived from a sample”) 
- Identify dependencies to data not represented as objects at this point in time, but, e.g. as termlists
- Make sure that your model can be expanded subsequently to represent those data as objects, as well
- Integrate the sparse matrix of metadata not contained in the MSOM in the model

### Step 4:  Reality check
- Introduce measures allowing to identify errors in reported data according to your model
- Expose your model to actual data delivered by independent colleagues and capture the errors and gaps that occurred
- Identify errors and gaps that are related to the model and not occurring due to errors in the data
- Adjust the model according to these errors and gaps
- Re-iterate the reality check until no more severe errors and gaps are occurring that are relevant for the previously defined competency questions


##  What to read next?

- {ref}`fcb-interop-covid-metadata`

````{rdmkit_panel}
````



## Authors

````{authors_fairplus}
Danielle: Writing - Original Draft
````


## License

````{license_fairplus}
CC-BY-4.0
````



