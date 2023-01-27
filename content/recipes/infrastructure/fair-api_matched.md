# Developing FAIR API for the Web

````{panels_fairplus}
```` 



---

````{note} 

```{image} ../../../images/logos/CFDE-logo.png 
:width: 100px
:align: right
```






````

## Background

An [Application Programming Interface (API)](https://cfde-published-documentation.readthedocs-hosted.com/en/latest/CFDE-glossary/#api)  refers to a mechanism 
for interfacing with a web service programmatically. Unlike a Graphical User Interface (GUI) designed to be used by an 
end-user, API are designed to be used by other computer programs. Designing and documenting an API for an application 
enables your application to be more interoperable with, and ultimately more reused, by other applications. 
Depending on the type of application, there are different ways to design APIs. Most important is that APIs should be 
documented well. We will not cover [FAIR](https://cfde-published-documentation.readthedocs-hosted.com/en/latest/CFDE-glossary/#fair) 
APIs of software libraries, but instead focus on developing FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) APIs for the web.

More and more web-based applications are becoming available every day. These applications typically perform complex 
operations on large database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)s. While web-based applications provide users with the capacity to access a tool, a database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database), 
or other resource programmatically, they are not always able to interoperate with other independent web applications. 
A web-based application that offers a FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) API is more accessible to operating as part of workflows, or integration 
systems such as semantic search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/) engines. This makes FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/) API development very relevant for data catalogs or web tools 
developed(URL_TO_INSERT_RECORD https://www.cog-genomics.org/plink2/formats#ped) by the CF DC(URL_TO_INSERT_RECORD http://dublincore.org/documents/dces/)(URL_TO_INSERT_RECORD https://doi.org/10.25504/FAIRsharing.3nx7t)Cs.

While a slew of standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s exist for web API development and documentation, each has their own level of FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)ness. 
Here we are going to focus on [RESTful APIs](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm), 
which can be described with [OpenAPI](https://www.openapis.org/) (previously Swagger) to take advantage of RESTful API 
flexibility while still permitting machine readable introspection. Several other standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s are machine readable by
default, including [SOAP](https://www.w3.org/TR/soap/), [SPARQL](https://www.w3.org/TR/sparql11-overview(URL_TO_INSERT_RECORD http://www.w3.org/TR/sparql11-overview/)/) or
[GraphQL](https://graphql.org/) among many others, but despite this, RESTful APIs are the most widely used because of
their low barrier to entry. Some standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s exist for RESTful APIs, in many cases, these can also be described by OpenAPI.
We will consider a specific extension of OpenAPI: [Smart-API](https://smart-api.info(URL_TO_INSERT_RECORD http://smart-api.info)/), which adds a few additional 
fields and also has its own [get-started guide](https://smart-api.info(URL_TO_INSERT_RECORD http://smart-api.info)/guide).

## Motivation
Documenting APIs or building them from the ground up with SmartAPI in mind have a number of advantages:

- Human readable documentation of that API with a number of packages that can generate it from the OpenAPI schema
- Server/client libraries from a number of packages that can generate them for numerous programming languages based on the OpenAPI schema
    - People can access your application features using their favorite programming language
    - People can create an application that shares the same API as another application for interoperability
- [Interoperability with GraphQL](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/IBM/openapi-to-graphql)
- Enabling simple use cases like enhancing findability with [API Catalogs](https://apis.guru/browse-apis/)
- Enabling future use cases

SmartAPI specification(URL_TO_INSERT_RECORD http://smart-api.info)s inherit all of the benefits of OpenAPI, while adding the potential for interoperability with RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/)
semantically linked data. This can help enable future use cases like [BioThings API](https://biothings.io/), powering
semantically linked APIs for biomedical knowledge exploration.

## Ingredients
- Web Application
- Existing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) API Documentation
- OpenAPI/SmartAPI Editor (see step 1)

## Objectives
We will look at the existing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) REST service provided by the Metabolomics Workbench(URL_TO_INSERT_RECORD https://www.metabolomicsworkbench.org/) catalog: <https://www.metabolomicsworkbench.org(URL_TO_INSERT_RECORD https://www.metabolomicsworkbench.org/)/tools/mw_rest.php>.
This API is described for human consumption, including examples for each endpoint. We will tackle some of the endpoints using OpenAPI.

Although OpenAPI can be edited by most standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)s editors because it is typically written in [YAML](https://yaml.org/spec/1.2/spec.html)
(a slightly 'nicer' version of [JSON](https://cfde-published-documentation.readthedocs-hosted.com/en/latest/CFDE-glossary/#json) that is equivalent),
it is helpful to use an OpenAPI editor like <https://app.swaggerhub.com/home>. 
This will catch errors as you edit, and permit testing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) of the endpoints as you encode immediately.


An example endpoint in an OpenAPI Editor:

````{dropdown}
```{figure} ../../../images/ss1.png
---
width: 800px
name: An example endpoint in an OpenAPI Editor
alt: An example endpoint in an OpenAPI Editor
---
An example endpoint in an OpenAPI Editor
```
````

A real response in an OpenAPI Editor:

````{dropdown}
```{figure} ../../../images/ss2.png
---
width: 800px
name: A real response in an OpenAPI Editor
alt: A real response in an OpenAPI Editor
---
A real response in an OpenAPI Editor
```
````


## Recipe

The complete `swagger.yaml` constructed in this recipe is available [here](https://gist.github.com(URL_TO_INSERT_RECORD https://github.com/)/u8sand/292c363274ff6e609fadb369c26ca9b6) for your reference, 
it will be valuable to follow the tutorial and construct it iteratively.


### Step 1: Setting up the OpenAPI Editor
Several options exist, including the [Swagger Editor](https://swagger.io/tools/swagger-editor/), especially with APIs 
that are enabled to support CO(URL_TO_INSERT_RECORD http://www.cropontology.org/)(URL_TO_INSERT_RECORD https://codeocean.com)RS(URL_TO_INSERT_RECORD http://rgd.mcw.edu/rgdweb/ontology/view.html?acc_id=RS:0000457).
Unfortunately, the API we will work with here **does not**, so we will need to obtain a Swagger Editor that can operate
even when CO(URL_TO_INSERT_RECORD http://www.cropontology.org/)(URL_TO_INSERT_RECORD https://codeocean.com)RS(URL_TO_INSERT_RECORD http://rgd.mcw.edu/rgdweb/ontology/view.html?acc_id=RS:0000457) is not enabled. Because the de-facto swagger editor is a web-app, most editors have this issue.
We specifically modified [an Open Source Visual Studio Code Extension](https://marketplace.visualstudio.com/items?itemName=Arjun.swagger-viewer) so 
that it supports this specific use case.

Until our pull request is merged, the modified extension can be accessed [here](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/MaayanLab/vs-swagger-viewer/releases). 
The `vsix` file can be installed with [Visual Studio Code](https://code.visualstudio.com/).

It can be installed from `Ctrl+Shift+P` with the action "Install from VSIX"

````{dropdown}
```{figure} ../../../images/ss3.png
---
width: 800px
name: Install from VSIX dialog
alt: Install from VSIX dialog
---
Install from VSIX dialog
```
````


And selecting the `.vsix` file you downloaded.

Once installed, a swagger file can be edited by opening the swagger.yaml (that we will be writing throughout the rest of
the recipe), using `Ctrl+Shift+P` again and choosing the action "Preview Swagger".



````{dropdown}
```{figure} ../../../images/ss4.png
---
width: 800px
name: Previewing swagger
alt: Previewing swagger
---
Previewing swagger
```
````

The result will be a webview that opens to the side with the Swagger Editor.


````{dropdown}
```{figure} ../../../images/ss5.png
---
width: 1100px
name: Swagger Editor
alt: Swagger Editor
---
Swagger Editor
```
````

Edits to the file will update the view **in real time**, and the view may be used to craft/test API requests.

### Step 2: Beginning an OpenAPI specification
We start by annotating useful descriptions for the API in the `info` field, this includes adding descriptors, version, license, and contact informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion. This gives your API an identity and this way it can be used in OpenAPI catalogs, for which there are several including [SmartAPI](https://smart-api.info(URL_TO_INSERT_RECORD http://smart-api.info)/), making it possible to find your own APIs.

The `servers` field has the base url(s) for accessing the API we're about to describe.

```yaml
```

### Step 3: Describing a path
The Metabolomics API offers several examples, let's tackle one of them:

|Example request|Example URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)|
|-|-|
|Show all publicly available studies (Project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project), Study, Analysis ID)|https://www.metabolomicsworkbench.org(URL_TO_INSERT_RECORD https://www.metabolomicsworkbench.org/)/rest/study/study_id/ST/available|

This tells us what the endpoint does to an extent; let's add that to our API under the `paths`.

```yaml
```

The path is relative to the server url, and `get` refers to the REST method (`GET` as opposed to `PO(URL_TO_INSERT_RECORD http://plantontology.org/)ST`, `PUT`, `DELETE`, ...), in REST `GET` refers to reading a resource and is what happens when you send the following packet to a web server. These packets can be crafted using `curl`, the `-v` flag helps see input and output packets and the `-X` flag allows you to set the method (`GET`, `PO(URL_TO_INSERT_RECORD http://plantontology.org/)ST`, ...), the `-H` flag lets you specify headers.

```bash
```

```
```

Note that your web browser does the same, albeit with a few different headers for end-to-end compression and browser informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion for webpage optimization.

```bash

```

The `GET` at the start is changed to `PO(URL_TO_INSERT_RECORD http://plantontology.org/)ST` or another value when sending actual data (in the body of the packet). (`curl -v -X PO(URL_TO_INSERT_RECORD http://plantontology.org/)ST ... -d "packet data"`)

We did not know what the response would be by the webpage, but OpenAPI provides a means to describe this as well.

```yaml
```

The `200` here refers to the HTTP status code, these are standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)ized by HTTP but the gist is:

|Code|Meaning|
|-|-|
|2xx|OK (created, no content, ...) |
|3xx|Redirect (temporary, permanent, ...)|
|4xx|Not OK (not found, permission denied, ...)|
|5xx|Server Error|

We can explicitly describe what the response means for our application in the `description` under the response code. The `content -> application/json` refers to the `Content-Type` returned on the response header. This header tells you that the body will be json, and not i.e. `text/html` which we view most webpages as.

Finally, the `schema` is JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259)-Schema describing how the JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) should look. It also supports describing each field individually in depth, and specifying optional or mandatory fields. We use `additionalProperties` to refer to the `values` in the object, and `properties` on a `type: object` to refer to the `key` specific description.

The benefit of fully describing and endpoint like this is that a developer can fully understand what to expect from an endpoint, enabling them to determine code logic validity prior to having to test it at runtime. Furthermore, the SmartAPI initiative has an extension for relating those types to RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) for visions like the [BioThings](https://biothings.io/).

### Step 4: Adding a path with parameters
Let's tackle our next endpoint:

|Example request|Example URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)|
|-|-|
|Fetch analysis informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)ion for a study|https://www.metabolomicsworkbench.org(URL_TO_INSERT_RECORD https://www.metabolomicsworkbench.org/)/rest/study/study_id/ST000001/analysis|

While the example shows `ST000001` in reality, the idea is that this can be any study ID, such as those coming out of the previous endpoint.

```yaml
```

We see some new concepts here, the first is the path which has a variable in it delineated by `{study_id}` where we would want the `study_id` to go. Paired with this we add an entry into the `parameters` array and state the same name `study_id` is `in: path` referring to this path-style variable substitution.

Parameters can be added in other places as well. Google, for instance, describes search(URL_TO_INSERT_RECORD https://arch.library.northwestern.edu/)es like so: `https://www.google.com/search?q=smartapi&sourceid=chrome&ie=UTF-8`, the `?q=...&sourceid=...` are referred to as query parameters and they are in the form: `?{name}={value}&{name}={value}&...`. You could describe these in OpenAPI as well by using `in: query`.

In the case of a `PO(URL_TO_INSERT_RECORD http://plantontology.org/)ST` you might use, `in: body` referring to the content you send with your request.

Again, every parameter is validatable with JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259)S(URL_TO_INSERT_RECORD https://github.com/enpadasi/Ontology-for-Nutritional-Studies)chema. In our current example, we have used a JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259)S(URL_TO_INSERT_RECORD https://github.com/enpadasi/Ontology-for-Nutritional-Studies)chema pattern to constrain the type of string(URL_TO_INSERT_RECORD https://string-db.org/) acceptable by the endpoint. In the case of a body, it could be an elaborate JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) object such as our response schema.

Finally, we have included an `example` which will help developers with rapid testing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) of endpoints given valid examples. Using this example, we can use our OpenAPI Editor to trigger a new request:


````{dropdown}
```{figure} ../../../images/ss2.png
---
width: 800px
name: fair-api-images/ss2
alt: fair-api-images/ss2
---
fair-api-images/ss2s.
```
````



With the output, we can complete our path by annotating the response:

```yaml
```

### Step 5: Identifying components
In some cases, a common set of JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) objects are reused throughout the API. It is often meaningful to turn these into their own 'component' and reference them. It is also extremely helpful to include descriptions especially for fields that are not directly interpretable.


```yaml
```

Under `components`, as many individual components can be specified, and they can be referenced using `$ref` with [JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259)-Schema pointers](https://json-schema.org(URL_TO_INSERT_RECORD http://schema.org/)/draft/2019-09/relative-json-pointer.html) as shown above.

### Step 6: SmartAPI extension
When it comes to *automatic* interoperability, the [SmartAPI extension](https://smart-api.info(URL_TO_INSERT_RECORD http://smart-api.info)/guide) to OpenAPI is almost essential. It provides mechanisms for adding RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) annotations to parameters or responses. We will demonstrate it on a new endpoint:

|Example request|Example URL(URL_TO_INSERT_RECORD https://tools.ietf.org/html/rfc1630)|
|-|-|
|Fetch all protein fields from Entrez gene id|https://www.metabolomicsworkbench.org(URL_TO_INSERT_RECORD https://www.metabolomicsworkbench.org/)/rest/protein/gene_id/19/all/|

```yaml
```

Here we see our usual path setup with a new section: `x-responseValueType`, this is the smartAPI(URL_TO_INSERT_RECORD http://smart-api.info) extension. 
Each `x-path` refers to the path in the JSO(URL_TO_INSERT_RECORD http://www.sequenceontology.org/)N(URL_TO_INSERT_RECORD http://dx.doi.org/10.17487/RFC8259) object (using `.` on nested keys). 
For instance, the `gene_id` does not need any `.` because it is the root of the response object. 
The `x-valueType` here identifies the id namespace or context for which that value has meaning.
Typically, this is a prefix path, in other words, you would produce a full URI(URL_TO_INSERT_RECORD https://www.rfc-editor.org/rfc/rfc3986) with: `{x-valueType}/{actual_value}`.

[identifiers.org](http://identifiers.org/) is a public resource cataloging actual identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) schemes making it an ideal
way to namespace a given identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema). 
It has the added benefit of providing an API for accessing additional metadata such as 
cached [schema.org(URL_TO_INSERT_RECORD http://schema.org/)](https://schema.org(URL_TO_INSERT_RECORD http://schema.org/)/) annotations on the landing page of the resulting identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema).

With the annotations fully described here, it becomes possible to eventually utilize your API for federated RDF(URL_TO_INSERT_RECORD http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/) queries 
without any additional effort. 
This was demonstrated by the [BioThings](https://biothings.io/), which can integrate SmartAPI APIs with proper annotations.
It also permits end users to find your APIs knowing their identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)s (i.e. ncbigenes).

### Step 7: Publishing and utilizing your OpenAPI/SmartAPI
Once you have a working OpenAPI document, this open up numerous possibilities that you can now do. 
Firstly, your API can be published on [smart-api.info(URL_TO_INSERT_RECORD http://smart-api.info)](https://smart-api.info(URL_TO_INSERT_RECORD http://smart-api.info)/), permitting people and machines to locate
it and potentially utilize it.

But you can also produce interactive documentation much like the output seen in the OpenAPI editor to publish on your webpage.

It is even possible to automatically generate statically or dynamically code in many different programming languages for
API clients or Server stubs (i.e. for API first or compatibility) with the [openapi-generator](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/OpenAPITools/openapi-generator).

An [initiative by IBM](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/IBM/openapi-to-graphql) provides a mechanism for interoperating an 
OpenAPI documented endpoint with [GraphQL](https://graphql.org/).

These various capabilities make an API extremely accessible, lowering many barriers to entry for interoperability and
reusability of your API.

## Conclusion

We've walked you through a case study where we documented an API using OpenAPI and SmartAPI extensions to build a 
document that will vastly improve the FAIR(URL_TO_INSERT_RECORD https://www.go-fair.org/fair-principles/)ness of your API. 
After registering your API on an API catalog platform, such as [smart-api.info(URL_TO_INSERT_RECORD http://smart-api.info)](https://smart-api.info(URL_TO_INSERT_RECORD http://smart-api.info)/) you will enable
developers and programs to find, introspect and interoperate with our API.
Furthermore, existing(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) tooling around OpenAPI can enable the accessibility and reusability of your APIs in many 
programming languages and other standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)ized systems.


### What to read next?

This content type focus on using OpenAPI.

- [Grlc](http://grlc.io/): "converting your SP(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/SP)ARQL(URL_TO_INSERT_RECORD http://www.w3.org/TR/sparql11-overview/) queries into RESTful APIs"
- [GraphQL](https://graphql.org/):  "a Query Language for your API"
- [OpenAPI-to-GraphQL](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/IBM/openapi-to-graphql) "From OpenAPI-to-GraphQL "
- [ISA-graphql](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/ISA-tools/isa-api/tree/develop/isatools/graphQL) "an example of a GraphQL querying mechanism built to interrogate ISA metadata".

````{rdmkit_panel}
````

## References

````{dropdown} **Reference**
``` -->git stat
````


## Authors
````{authors_fairplus}
Daniel: Conceptualization, Writing - Original Draft
````


## License
````{license_fairplus}
CC0-1.0
````
