(fcb-find-identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s)=
# Unique, persistent identifiers



````{panels_fairplus}
:identifier_text: FCB006
:identifier_link: https://w3id.org/faircookbook/FCB006
:difficulty_level: 3
:recipe_type: background_information
:reading_time_minutes: 30
:intended_audience: principal_investigator, data_manager, data_scientist 
:maturity_level: 1
:maturity_indicator: 1
:has_executable_code: nope
:recipe_name: Introducing unique, persistent identifiers
```` 


The **FAIR (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.WWI10U)  principles**, under the `Findability` and the `Accessibility` chapters respectively, state that: 
> F1. (Meta)data are assigned a globally unique and persistent identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) 
> 
>A1. (Meta)data are retrievable by their identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  using a standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) ised communications protocol 

## Main Objectives

The main goals of this recipe are therefore:

> To understand the purpose of a globally unique and persistent identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  and how they can be used to retrieve the associated (meta)data using a standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) ized communication protocol.
> To provide explanations on how to generate globaly unique identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s, explain what IRIs are and how they can be generated, retrieved and resolved.


From these principles, it is necessary to explain three key processes, which are: 

### Identifier minting
```{admonition} Tip
:class: tip 
 **`Identifier minting`** is fundamentally about the **`authority deciding identity`**. 
``` 
 - the tax office
 - the HR department
 - the company registry
 - the EMB (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.a1rp4c) L-EBI

### URI construction
```{admonition} Tip
:class: tip 
**`URI construction`** is fundamentally about **`scoping the authority`**.
```
> for example, should the web address be:
> http://organization/people/1123 
> or
> http://organization/commercial/people/1123


### URI Resolution: 
```{admonition} Tip
:class: tip 
**`URI resolution`** is fundamentally about **`directing requests to the relevant identified entity`**
```
The standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)  approach would be resolving a `HTTP GET` request using content negotiation to choose between different representations of the resource.

All these key points will be developed (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.31385c)  in this recipe.

---


````{dropdown} Identifier services
:open:  
```{figure} ./identifiers-fig1.svg
---
width: 700px
name: 
alt: identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  services
---
Key Processes to sustain Globally Unique Persistent Resolvable Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s (GUPRID) .
```
````

---
<!-- 
## FAIRification Objectives, Inputs and Outputs

| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [Identifier](http://edamontology.org (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.a6r7zs) /data_0842) |   |   |
 -->

## Table of Data Standards

| Data Format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) s  | Terminologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  | Model (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) s  |
| :------------- | :------------- | :------------- |
| [IRI](https://tools.ietf.org/html/rfc3987) |   |   |
| [CURIE](https://www.w3.org/TR/2010/NOTE-curie-20101216 (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.af21db) /) |   |   |
| [URL](https://tools.ietf.org/html/rfc1738) |  |  |
| HTTP<!-- TO (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.w69t6r) DO add a link to corresponding document --> |  |  |
| RDF (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.p77ph9) <!-- TO (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.w69t6r) DO add a link to corresponding document --> |  |  |

---


## Minting identifiers


```{admonition} Tip
:class: tip 

 **Identifier minting is fundamentally about the *authority deciding identity.**
```


Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s are used to tag, identify, find and retrieve entities which are part of a collection (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=collection)  or a resource maintained by some organization. This organization is the `authority` which rules over that area of knowledge. The core (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.m283c)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.xMmOCL)  assumption is that identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s must be unique, that is they can not be shared and there is a 1 to 1 relation between the 'identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) ' and the entity it identifies.

With isolated systems, disconnected from any other system, the risk of identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  collision is null but two isolated systems can create local identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s which could be completely identical but which denote completely different entities. In fact, this happens all the time.

So these identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s are said to be locally unique, as there is no guarantee these are unique to all other systems that exist, in other words, that they are globally unique.


## How to produce globally unique identifiers?

There are 2 ways to produce non-resolvable, globally unique identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s:

### UUID based identifiers

With this approach, the notion of `universally unique` is a probabilistic one. *The probability to find a duplicate within 103 trillion version-4 UUIDs is one in a billion*. The likelihood of collision (generation of the exact same identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) ) is extremely small but not null. Therefore, with an ever increasing number of digital resources to index, collisions should not be ruled out.
According to the [RFC4122 specifications](https://tools.ietf.org/html/rfc4122), a UUID is an identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  that is unique across both space and time, with respect to the space of all UUIDs.  Since a UUID is a fixed  size and contains a time field, it is possible for values to rollover (around A.D. 3400, depending on the specific algorithm  used).  A UUID can be used for multiple purposes, from tagging objects with an extremely short lifetime, to reliably identifying very persistent objects across a network.


---

```{note}

Key Fact about UUID: 
> - `no centralized authority is required to administer them`
> - `content independent, entirely disconnected from the identify they can be associated with for identification purpose`
> - `generation on demand can be completely automated`
> - `non resolvable`
> - `completely semantic free (opaque) identifier`
```

---


* Generation in Python
The following code snippet shows the generation of a UUID using the Python uuid package.


```python
import uuid
id = uuid.uuid4() 

print(id)
5b6d0be2-d47f-11e8-9f9d-ccaf789d94a0
```



### Hash based identifiers

This approach uses 2 inputs: 
- a cryptographic hashing algorithm implemented as a software function
- a digital resource (e.g. a file)

Indeed, the approach generates an identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  by using all or some of the content of the digital resource as input to the cryptographic hashing function to compute a unique string (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9b7wvk) , which is therefore a signature (or fingerprint) of the digital resource {footcite}`Retter-1`, {footcite}`Retter-2`.
A number of algorithms can be used and some are already widely used such as *Message Digest algorithm MD5* specified by the RFC1321 {footcite}`MD5`, the *Secure Hash Algorithm (SHA1)*,  *Secure Hash Algorithm 2 (SHA256)*, *Secure Hash Algorithm 3 (SHA3)* or *BLAKE2b-256* (RFC 7693) {footcite}`Blake2`. 
The first two are considered obsolete, while the latter two are most advanced and approved by NIST.

---

```{note} 
>Key fact about hash identifiers: It is not possible to reconstruct the original data from these hash strings. These are only **fingerprints**, which can therefore only be used to do the following tasks:
>- message authentication
>- digital signature
>- public key encryption
```


---

#### Generation in Python
The following code snippet shows the generation of a hash for a string (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9b7wvk)  using the Python hashlib package:

```python
import hashlib

# encode it to bytes using UTF-8 encoding
message = "creating globally unique identifiers for FAIR data".encode()

# hash with MD5 (not recommended)
print("MD5:", hashlib.md5(message).hexdigest())

# hash with SHA-2 (SHA-256 bits & SHA-512 bits long)
print("SHA-256:", hashlib.sha256(message).hexdigest())
print("SHA-512:", hashlib.sha512(message).hexdigest())

# hash with SHA-3
print("SHA-3-256:", hashlib.sha3_256(message).hexdigest())
print("SHA-3-512:", hashlib.sha3_512(message).hexdigest())

# hash with BLAKE2 (256-bits BLAKE2s & 512-bits BLAKE2c)
print("BLAKE2s:", hashlib.blake2s(message).hexdigest())
print("BLAKE2b:", hashlib.blake2b(message).hexdigest())
```

#### Generation of hashes using curl
The following snippet shows how a b2sum hash can be generated using [`curl`](https://curl.haxx.se/)

```bash
curl https://fairplus.github.io/cookbook-dev/intro | b2sum --length 256 --binary

24d470987fda1278c63c3f97ab30869b821906449f3ecf290ee48086b8215668
```




In our context, the use of the hashing function is to generate a unique key which may be used to generate a URL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2) . This simply indicates a technical option for generating opaque URL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2) , not that it is necessarily the most widespread approach.


## Understanding Uniform Resource Locators (URLs)

```{admonition} Tip
:class: tip

 **URI construction is fundamentally about scoping the authority**.
```

Having covered the technical details to generated globally unique identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s, it is now necessary to discuss the issue making identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s *resolvable (a notion also known as `dereferenceable`)*.

In other words, in order to create globally unique identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s `for the web`, it is necessary to understand what Uniform Resource Locator (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2) s<!-- TO (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.w69t6r) DO add a link to corresponding document --> (a.k.a `URL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2) `) are and how to construct them for use with the Hypertext Transfer Protocol<!-- TO (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.w69t6r) DO add a link to corresponding document -->.

This results in URL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2) s of the following form

````bash
        userinfo       host      port
        ┌──┴───┐ ┌──────┴──────┐ ┌┴┐
https://john.doe@www.example.com:123/forum/questions/?tag=networking&order=newest#top
└─┬─┘   └───────────┬──────────────┘└───────┬───────┘ └───────────┬─────────────┘ └┬┘
scheme          authority                  path                 query           fragment
````
source:[https://en.wikipedia.org/wiki/Uniform_Resource_Identifier](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier)


The structure of `URL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2) `, according to the World Wide Web Consortium (W3C) specification, is as follows:

```bash
URI = scheme:[//authority]path[?query][#fragment]
```

### `scheme`:
In this structure, the `scheme` defines the protocol or application to use to obtain the resource. The list of official `scheme` is maintained by the **Internet Assigned Numbers Authority** and the following link (https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml) holds the most up to date version.

The most relevant `URI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d261e1)  scheme` in the context of FAIR (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.WWI10U)  data and Linked Open Data are `http` and `https` which denote the `Hypertext Transfer Protocol` and the `Hypertext Tranfer Protocol Secure`.

### `authority`:

Besides setting the `scheme`, the other essential fragment of a URI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d261e1)  is the `authority`, which according to the Internet Engineering Task Force (IETF) specifications, presents the following characteristics:
```
authority = [userinfo@]host[:port]
```
Note how the required part is the `host`, with `userinfo` and `port` informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion being optional and should be avoided in identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s for data.

### `host`:

In the `authority`, the notion of `host` corresponds to the `Internet Protocol (IP) address` of a server hosting (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.q7bkqr)  a resource. Often, the IP address corresponding to the `host` is given a `host name` such as `www.example.org`. The `host name` should be a `Qualified Domain Name` at minima, or a `Fully Qualified Domain Name (FQDN)` ideally and registered with the `Domain Name Service (DNS)` which allows the resolution (lookup) between the `ip address` and the `hostname`.

---

```{note} Tip

it is often the case the `authority` is reduced to the `host` , which is then referred to as a 'namespace' or 'domain name' in an abuse of language.
`host` is in fact further specified by 3 element
>  - top-level domain , `com` in the www.example.com web address
>  - second-level domain,  `example` in the www.example.com web address
> - hostname subdomain,`www` in the www.example.com web address
```

---


```{note} Tip

>`subdomain` can be defined in the Domain Name Service and belong to the main domain.  Technically, to add a subdomain pointing to the domain name, one needs to create/add a CNAME to the DNS for a registered domain name
```

---

### `path`: 
The `path` defines the directory on the `host` where the resource is located and consists of a sequence of zero or more path segements separated by a `/`.

### `query`:
The `query` is an optional part of the URL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2)  syntax that starts with a `?`. Typically the `query` component consists of a service of key-value pairs separated by an `&` deliminator.

In the context resolvable identiers, `query` components should be avoided.

### `fragment`
The `fragement` is an optional part of the URL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2)  syntax that starts with a `#`. It identifies a component within the returned resource and is used for client side processing, e.g. to scroll to a particular section within a webpage.

## Generating Resolvable URLs

In the context of FAIR (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.WWI10U)  data, resources on the web must have **unique**, **persistent**, and **resolvable** identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s.
In order to achieve the capability of `persistence`, it is necessary for the resource identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s to comply to the RFC 3986 IETF standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)  for URI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d261e1) s (and IRIs, which are URI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d261e1)  extended to cope with unicode). This means that it must comprise the following components:

1. scheme: https
2. an authority: www.example.com
3. optionally a path: `/dataset-name/`
4. a local identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  (such as database (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Database)  accession number, such as P12133 from uniprot) or a globally unique identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  (such as a UUID or hash code).

In a virtual example which uses a UUID for the local identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  and does not use a path, it looks like this:

```bash
https://www.example.com/5b6d0be2-d47f-11e8-9f9d-ccaf789d94a0
```

Taking a real life example, to make the `UniProt accession number` globally unique, one needs to provide the context in which the accession number is unique. This can be done by converting it into an `International Resource Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) ` (IRI - commonly referred to as a URL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2) ) by appending the local identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  onto a namesapce.

---

```{admonition} Tip
:class: tip
> You should only use a `namespace` over which you have ownership (the authority), otherwise you cannot guarantee that the minted IRI will be **globally unique**; the organization or person who owns the namespace may already, or at some point in the future, use the IRI that you created for some other purpose.
```

In the case of UniProt, the resource has provided IRIs for each page about a protein as well as separate IRIs for the protein itself; this is because the page is not the concept of the protein by a document that describes properties of the protein. This separation of identities is achieved by using different namespaces for the different types of resource.

- UniProt P38398 web page IRI: https://www.uniprot.org (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.s1ne3g) /uniprot/P38398
- UniProt protein P38398 IRI: http://purl.uniprot.org/uniprot/P38398

Once such URI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d261e1) s are available, one may also turn them into compact identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s called CURI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.af21db) s. This will be discussed further in the next section.

## Identifier Resolution - Enabling persistence through indirection


This relates to the following FAIR (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.WWI10U)  principle mentioned in the introduction:

> A1. (Meta)data are retrievable by their identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  using a standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) ised communications protocol.


```{admonition} Tip
:class: tip
 **`URI resolution` is fundamentally about directing requests to the relevant identified entity.** 
```

The standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard)  approach would be resolving a `HTTP GET` request using content negotiation to choose between different representations of the resource.

A PURL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.3e603c)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2)  is a **`persistent URL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2) `**, meaning that it provides a **permanent address to access a resource on the web**.

To understand the notion of PURL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.3e603c)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2) , one needs to first get fam (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d0886a) iliar with the notion of `url indirection` (also known as `url redirect` or `url forwarding` ), which refers to the practice of providing a stable, fixed web address/url, but setting it up so that it points to another content, which may be periodically modified. 

When a user retrieves a PURL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.3e603c)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2) , they will be **`redirected`** to the current location of the resource.
When an author needs to move a page, they can update the PURL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.3e603c)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2)  to point to the new location.

```{admonition} Tip
:class: tip
The practice of **indirection** comes handy as it ensures invariant url address for resources which are known to change, owing to version changes for instance or owing to change in ownership. 
```

We can see this practice in action with the reliance on purl.org url for identifying OBO (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.847069)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.cbz72b)  Foundry (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.847069)  resources. For instance, the following url [`http://purl.obolibrary.org/obo/stato.owl`](http://purl.obolibrary.org/obo/stato.owl) is a redirect to the latest release of the file, which is [https://raw.githubusercontent.com/ISA-tools/stato/dev/releases/latest_release/stato.owl](https://raw.githubusercontent.com/ISA-tools/stato/dev/releases/latest_release/stato.owl).

PURL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.3e603c)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2) s with a `common prefix` are grouped (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.31385c)  together into **domains**. Each domain has a single maintainer who can add new PURL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.3e603c)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2) s to the domain and make changes to existing (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.q7bkqr)  PURL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.3e603c)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2) s within the domain.


FAIR (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.WWI10U)  Principle A1 states that:
>(meta)data should be retrievable by its identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) .

When the identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  is not a resolvable URL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2) , then `Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  Resolution Services` are required that know how to map (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.53edcc)  an IRI to a location for the data. 



### Introducing CURIES or Compact URIs
CURI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.af21db) s (short for compact URI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d261e1)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.af21db) s) are defined by a World Wide Web Consortium Working Group Note [CURI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.af21db)  Syntax 1.0](https://www.w3.org/TR/2010/NOTE-curie-20101216 (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.af21db) /), and provide a human readable shortening of IRIs. 

The CURI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.af21db)  consists of a **`namespace prefix`** followed by the **`local identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) `**.

There are some widely used and defined CURI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.af21db) s such as DOI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.hFLKCn) s and ISBN numbers. For example the DOI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.hFLKCn)  `[doi:10.1038/sdata.2016.18]` refers to the FAIR (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.WWI10U)  Principles (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.WWI10U)  paper. The Digital Object Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.hFLKCn)  System web site (https://www.doi.org (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.hFLKCn) /) provides a resolution service for DOI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.hFLKCn) s. The service is available as a web form on the site or can be used by appending a DOI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.hFLKCn)  to the website.The client will be redirected to the URL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2)  where the resource about the concept is located, e.g. for the FAIR (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.WWI10U)  Data Principles paper we can use the URL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2)  https://www.doi.org (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.hFLKCn) /10.1038/sdata.2016.18 to resolve the paper's DOI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.hFLKCn) . This results in the client being taken to the page at https://www.nature.com/articles/sdata201618.

`Namespaces` can be defined *by convention*, such as the case with `doi`, and registered with services to allow for the resolution of CURI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.af21db) s (see [Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  Resolution Services](##identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) -resolution-services) below). These are extensively used to map (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.53edcc)  CURI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.af21db) s to URL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2) s that can be resolved.

Going back to our *Life Science context*, we can use the following CURI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.af21db)  `[uniprot:P38398]` to refer to the UniProt record for the protein. 

This is very useful for including unambiguous, global identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s in scientific articles.

[^safe-CURI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.af21db) ]: The CURI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.af21db) S are included in square brackets to make them *safe CURI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.af21db) s*, meaning that they should not be confused for URI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d261e1) s.

 



### Identifier Resolution services

* [purl.org](https://archive.org/services/purl/)

    > The PURL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.3e603c)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2)  system is a service of the Internet Arch (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.52b22c) ive, which provides an interface to administer domain. For more informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion about the service, visit https://archive.org/services/purl/help
    >

* [w3id (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.S6BoUk) s](https://w3id.org (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.S6BoUk) /)
    
    > Permanent Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s for the Web. Secure, permanent URL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2) s for your Web application that will stand the test of time.
    > - authority registration service
    > - resolution service
    > - redirection service:
    > 
    > Send a request to add a redirect to the public-perma-id@w3.org mailing list. Make sure to include the URL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2)  that you want on w3id (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.S6BoUk) .org (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.S6BoUk) , the URL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2)  that you want to redirect to, and the HTTP code that you want to use when redirecting. An administrator will then create the redirect for you.


* [Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s.org](http://identifiers.org/)

    > [Identifiers.org](https://identifiers.org) is a **Resolution Service** provides consistent access to life science data using [`Compact Uniform Resource Identifier (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d261e1) s`](https://www.w3.org/TR/2010/NOTE-curie-20101216 (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.af21db) /), hosted by the EBI provides a resolution service, both as a web form and through the URL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2)  pattern {footcite}`Juty2012`. 
    >`Compact Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s` consist of an `assigned`, `unique` `prefix` and a `local provider designated` **`accession number`** (prefix:accession).
    > The resolving location of `Compact Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s` is determined using informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion that is stored in the [Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s.org Registry](http://identifiers.org/).
    > Datasets can register their *namespace `prefix`* together with their `identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  pattern`. The service can then be used in the same way as the DOI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.hFLKCn)  resolution service. So for the UniProt page about BRCA1, we can resolve the CURI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d261e1) E (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.af21db)  `[uniprot:P38938]` using Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s.org. This means that the URL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2)  https://identifiers.org/uniprot:P38938 resolves to the UniProt page https://www.uniprot.org (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.s1ne3g) /uniprot/P38938.



* [Name2Things](https://n2t.net/)

    > [Name2Things](https://n2t.net/) (N2T) is a **Resolution Service**, maintained at the California Digital Library (CDL) within the University of California (UC) Office of the President. CDL supports electronic library services for ten UC campuses and affiliated law schools, medical centers, and national laboratories, as well as hundreds of museums, herbaria, botanical gardens, etc. Similar to URL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2)  shorteners like bit.ly, N2T serves content **indirectly**.
    > N2T can store more than one "target" (forwarding link) for an identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) , as well as any kind or amount of metadata (descriptive informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion)
        > N2T.net is also a "meta-resolver". In collaboration with identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s.org, it recognizes over 600 well-known identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  types and knows where their respective servers are. Failing to find forwarding informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion for a specific individual identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) , it uses the identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) 's type to look for an overall target rule.



* [Bioregistry (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.250a8c) ](https://bioregistry.io (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.250a8c) /)

    > [Bioregistry](https://bioregistry.io (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.250a8c) /) is a **Resolution Service**, developed (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.31385c)  in a [GitHub (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.c55d5e)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.c55d5e)  repository](https://github.com (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.c55d5e) /biopragmatics/bioregistry). Like Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s.org it has a registry, but also a registry of registries, and it imports data from Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s.org and Name-to-Thing but extends beyond identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s for things but also supports, for example, ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) . As a community effort, new namespace prefixes and their identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  patterns can be [registered via GitHub (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.c55d5e)  (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.c55d5e)  issues](https://github.com (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.c55d5e) /biopragmatics/bioregistry/issues/new/choose). Compact identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s are supported and the URL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2)  https://bioregistry.io (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.250a8c) /chebi:138488 resolves to the ChEBI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.62qk8w)  page https://www.ebi.ac.uk/chebi (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.62qk8w) /searchId.do?chebiId=CHEBI:138488. Bioregistry (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.250a8c)  provides an [API to query the registry](https://bioregistry.io (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.250a8c) /apidocs/) itself.



*For more details, see the [Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  Resolution Services recipe](fcb-infra-idres).*

---

## Conclusion

In this recipe, we have given an overview of globally unique and persistent identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  {footcite}`McMurry2017`, {footcite}`Ananthakrishnan2020`, i.e. FAIR (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.WWI10U)  principle F1. We have covered:

- The difference between global and local identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s;
- How to convert a local identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  into a global one;
- Opaque and transparent identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s

We have given an overview of the different services available for handling identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s.
 
But we can not conclude this section on persistent identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s without stressing how central they are to the production of Linked Data or Linked Open Data, which rely on 3 W3C standard (URL_TO_INSERT_TERM https://fairsharing.org/search?fairsharingRegistry=Standard) s: URI (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.d261e1) {footcite}`URL (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.9d38e2) `,{footcite}`cool-uri`,{footcite}`cool-urisemweb`, RDF (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.p77ph9) {footcite}`RDF (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.p77ph9) concepts` and HTTP.

### What to read next?
<!-- > * [Why resolvable identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) s matter?](https://www.TODO.org/findability/why-identifiers.html) -->
* [Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  Minting with Minid Client](fcb-find-id-minid)
* [Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  Resolution Services](fcb-infra-idres)
* [Identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema)  Map (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.53edcc) ping Services](fcb-identifier (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=identifier_schema) -map (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.53edcc) ping)

````{panels}
:column: col-md-4
:card: border-2
:header: bg-primary pa_dark
```{image} ../../../images/logos/pistoia_logo.png
:height: 40px
:align: center
:name: FAIR (URL_TO_INSERT_RECORD http://127.0.0.1:8080/FAIRsharing.WWI10U) toolkit_logo
```
^^^
- [The Pistoia Alliance FAIRtoolkit use cases: Adoption and Impact of an identifier policy at Astra-Zeneca](https://fairtoolkit.pistoiaalliance.org/use-cases/adoption-and-impact-of-an-identifier-policy-astrazeneca/)
---
:body: p-0
```{rdmkit_panel}
:inline: true
```
````



## References
`````{dropdown} **References**
```{footbibliography}
```
`````


## Authors

````{authors_fairplus}
AndreaSplendiani: Conceptualization
Alasdair: Writing - Original Draft
Chris: Writing - Original Draft
Egon: Writing - Original Draft
Philippe: Writing - Review & Editing, Conceptualization
````

## License

````{license_fairplus}
CC-BY-4.0
````
