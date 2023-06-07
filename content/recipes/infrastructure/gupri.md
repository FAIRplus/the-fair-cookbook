(fcb-infra-gupri)=
# Creating resolvable identifiers

````{panels_fairplus}
:identifier_text: FCB077
:identifier_link: 'https://w3id.org/faircookbook/FCB077'
:difficulty_level: 2
:recipe_type: hands_on
:reading_time_minutes: 30
:intended_audience: data_manager, data_scientist  
:maturity_level: 1
:maturity_indicator: 1
:has_executable_code: nope
:recipe_name: Creating resolvable identifiers
```` 


## Requirements

* Technical requirements:
  * Hypertext Transfer Protocol (HTTP)
  * Uniform Resource Locator (URL)
  * Domain Name System (DNS)
* Knowledge requirement:
    * understanding of [identifiers](../findability/identifiers.md).


    

## Abstract

With this recipe, we will reinforce the notion and importance of Globally Unique, Persistent, Resolvable Identifier (GUPRI) by 
introducing several public services for minting such identifiers. For each service, we will highlight the strengths and weaknesses.


## Background information

In the ideal linked data world, best practice is to provide a URL which can be accessed via HTTP, more specifically the HTTP GET command.
> (Learn more on HTTP GET here: [https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods)) 

To make this work, you have to guarantee that the HTTP GET command is answered.

### How can you do that?


HTTP uses Domain Name System (DNS) to decide which computer (i.e. which [IP address](https://en.wikipedia.org/wiki/IP_address))
to contact and ask for content regarding the URL you want to resolve.

DNS uses the concept of hierarchical domains to resolve URLs. 
> (Learn more about subdomains here: [https://en.wikipedia.org/wiki/Subdomain](https://en.wikipedia.org/wiki/Subdomain)) 

For example, you might want to resolve the following URL:

http://en.wikipedia.org/wiki/Enzyme_Commission_number

This will make your computer first look up who is responsible for managing "org" (the top-level domain), 
and ask there who is responsible for managing the domain "wikipedia.org",
and finally who is responsible for managing "en.wikipedia.org". 
All responses might yield different computer systems, i.e. IP addresses. 

This principle can thus be used to delegate authority.
In an enterprise context, this might be used to delegate authority within hierarchy:

http://my-department.my-enterprise.com/my-resource

can be understood  in the following sense: "my-enterprise" allowed "my-department" to "mint", i.e. generate / provide / resolve, URLs over the internet. 

If even more granularity / hierarchy is desired, an URL may also look like this:

http://my-team.my-department.my-enterprise.com/my-resource

This can also be understood in the context of accountability / responsibility:

"my-team" is responsible for ensuring that "http://my-team.my-department.my-enterprise.com/my-resource" is accessible and resolvable via the internet.


As all of this resolution practice is organized by DNS, this allows system administrators to hook in and generate `inaccessible subnets`.

Probably you know this phenomenon in the form of an "intranet", which is only available via VPN if you’re at home, or only available on-site. 
Typical domain names look like this, then:

http://internal-system.intranet.cnb

Here, your computer is configured in a specific way to resolve "intranet.cnb",
which is not accessible from the public internet, to specialized computer systems.




## How to realize a GUPRI?

A Globally Unique, Persistent, Resolvable Identifier (GUPRI) can be realized by implementing all the above. 
Some consider a GUPRI to be equivalent with PID (persistent identifier) or PURL (persistent URL). 
If intended for public use, your GUPRI must be accessible from the public internet; if intended for closed use, 
you would probably use specialized DNS rules and domain names to exclude the public from resolving your identifier.


## Public services for realizing a GUPRI

Most likely, you don’t want to set up a specialized HTTP web server at home. This would in principle be an option,
but introduces enormous debt on your side: you have to guarantee it is running all the time, 
and secure it against malicious intents (finally, you have to pay the bill for electricity and internet access as well).
You have to rent a domain name. You have to be quite an expert to set the system up and keep it running. 

So, what are your options? A public service for realizing GUPRIs sounds like it would be a good idea!

In the following recipe you will learn about w3id.org, purl.org, and the DOI / handle system, 
all of which are (or can be accessed as) free-of-cost services. 


### Purl.org

Although being the oldest and supposedly easiest-to-use service, purl.org is known by some veterans for having been 
offline for a long time.
This was especially bad as a "persistent" identifier should be resolvable at all times. 
This service is run by the non-profit [Internet Archive](https://archive.org).


To access the graphical user interface / web frontend, you need to register with archive.org. 
The frontend is easy to work with, although it is known for sometimes throwing errors or reacting in unexpected ways. 

Using purl.org, you can add custom redirects, with [HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) 
301, 302, 303, 307, or errors encoded as HTTP status codes 404 and 410. It also allows "partial redirects",
i.e. it would attach all the string behind a known part to redirect you 

```{note} example
deposited URL for the partial redirect is `http://example.com/one` and intended to be routed 
from `http://purl.org/example` . 
When you call `http://purl.org/example/two`, it will route you to `http://example.com/one/two`.
If there was no partial redirect in place, you would receive an error when calling `http://purl.org/example/two`
because this URL would not be known to the purl.org server).
```


A typical implementation route goes like this: 
1.	Register on `archive.org`
2.	Log-in to `purl.org`
3.	Create your domain, e.g. `purl.org/faircookbook`
4.	Create your individual redirect, e.g. `purl.org/faircookbook/recipe1` with status 302 redirecting to `http://example.org/faircookbook/recipe/1`

```{note}
Take home: 
Quick and easy solution; but not the most reliable. You have to register one purl "domain" to one user; 
if multiple users want to manage a common GUPRI space, they have to share the same credentials.
```

### w3id.org 

The service `w3id.org` emerged when `purl.org` was down {footcite}`w3id`. 
It is run by multiple stakeholders (see self-description on w3id.org) bound by a "social contract". 

Management is more difficult than purl.org, because w3id.org does not have a graphical user interface / frontend, 
but relies on "raw" `.htaccess` files deposited on GitHub.com. 

You need to have some knowledge about Apache .htaccess redirect rules though. 

> To learn more about Apache .htaccess redirect rules, refer to this [documentation](https://httpd.apache.org/docs/current/en/rewrite/flags.html)

A clear advantage is that it gives you more freedom in the implementation.

After making a proposal to change the redirection rules via a GitHub Pull Request, maintainers of the w3id.org team
have to (manually!) accept your changes. 
This is (normally) happening very fast, though (turnaround time < 1 day). 
If you make changes very often though, you will annoy the maintainers, and you should think about using another service.

A typical implementation route goes like this:

1.	Register to github.com
2.	Fork the GitHub repository at https://github.com/perma-id/w3id.org 
3.	Copy e.g. the folder "faircookbook" to your desired path (if you name the folder "faircookbook", you can resolve everything that goes like http://w3id.org/ faircookbook /*)
4.	Change the README and .htaccess
5.	Create a Pull Request
6.	Wait for acceptance of the Pull Request, and/or answer questions from the maintainers

```{note}
Take home:
Possibly quick and easy solution. 
If no maintainer reacts on your pull request, you can’t act yourself (but our experience is maintainers always act diligently).
Bound by social contract, but no formal / legal one. 
You decide yourself how you share the maintenance load within your namespace, and can only hope that the maintainers
of the w3id.org repo act in accordance with your wishes (e.g. don’t allow "outsiders" to change identifiers in your namespace).
```


### Free services which provide access to the Handle system

The Handle System (also known as `Handle.Net` or `HDL.NET`) is a globally distributed system to resolve "handles" (which are local identifiers per se).
The Handle System forms also the basis of DOIs (Digital Object Identifiers). 
DOIs add a layer of policies and specifications on top of The Handle System. 
Unfortunately, it is quite expensive (approx. 5000 €/$ per year) to join the DOI system 
(which would go via a Registration Agency, see here: https://www.doi.org/registration_agencies.html
-- well known Registration Agencies are DataCite and Crossref), 
whereas The Handle System is quite inexpensive (approx. 50 €/$ per year). 

There is also a way to get handles for free, which is described here:

You can reach out to `http://grnet.gr` – e.g. through the subpage `https://epic.grnet.gr/` where there is a Contact form. 

An alternative is http://www.pidconsortium.net/ (of which grnet is a member).

The author of this recipe managed to get access to both services for free.

A typical implementation goes like this:

1.	Request an account for hdl.grnet.gr
2.	Make yourself familiar with the API (no easy-to-use graphical user interface available as of now) – see http://www.handle.net/tech_manual/HN_Tech_Manual_9.pdf 
3.	Make the API call to register a handle

---

## Conclusion

This recipe provided several options for generated globally unique persistent resolvable identifiers. 
Furthermore, our audience can see how we used the w3id service to generate the identifiers for the recipes and how effective this is.
One has to bear in mind that the service works well for projects like this one where the expected number of objects remains small.
However, if scale-up is required and millions of GUPRIs are needed, a different service may be needed.


### What to read next?

- {ref}`fcb-find-identifiers` 
- {ref}`fcb-find-id-minid` 
- http://web.mit.edu/handle/www/purl-eval.html

````{rdmkit_panel}
````



## References
````{dropdown} **References**
```{footbibliography}
```
````

## Authors

````{authors_fairplus}
Robert: Writing - Original Draft
Tooba: Reviewing & Editing
Philippe: Reviewing & Editing
````


---

## License

````{license_fairplus}
CC-BY-4.0
````
