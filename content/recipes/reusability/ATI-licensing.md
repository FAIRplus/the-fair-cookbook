(rr-licensing)=
# Licensing


````{panels_fairplus}
:identifier_text: FCB032
:identifier_link: 'https://w3id.org/faircookbook/FCB032'
:difficulty_level: 3
:recipe_type: guidance
:reading_time_minutes: 15
:intended_audience: everyone  
:maturity_level: 0
:maturity_indicator: 0
:has_executable_code: nope
:recipe_name: Licensing
```` 


````{note} 
<!-- 
<a href="https://the-turing-way.netlify.app/welcome"><img src="../../../_images/turing-way-logo.jpg" alt="ati" width="60px"></a> -->
```{image} images/turing-way-logo.jpg 
:width: 60px
:align: right
```
[The sections about licensing are original content from The Turing Way](https://the-turing-way.netlify.app/welcome) and are included in the FAIRCookbook for convenience. Please cite keeping this in mind.
> The Turing Way Community, Becky Arnold, Louise Bowler, Sarah Gibson, Patricia Herterich, Rosie Higman, … Kirstie Whitaker. (2019, March 25). The Turing Way: A Handbook for Reproducible Data Science (Version v0.0.4). Zenodo. [http://doi.org/10.5281/zenodo.3233986](http://doi.org/10.5281/zenodo.3233986)
````




(rr-licensing-prerequisites)=

## Prerequisites

No previous knowledge is needed, but it is important to understand how licensing can affect your project.

(rr-licensing-summary)=
## Summary

> This chapter was written using American English, in which the word **license** is a noun **_and_** a verb.
> With British English, however, **licence** is a noun (as in, _to issue a licence_), while **license** is a verb (as in, _they licensed the event_).  

As with anything else in society, some of what you can and cannot do in software development is determined by the law.
Most of the constraints in this particular domain stem from intellectual property laws: laws that make abstract things like designs, stories, or computer programs resemble physical objects by allowing them to be owned.

This chapter aims to give a brief summary of relevant intellectual property laws (enough to be able to read most software licenses), explain free and open source software licensing, and explain how combining software from different sources works from a legal perspective.
It also gives some rules we have worked out to deal with common situations.

*Disclaimer: Good legal advice is timely, specific, and given by an expert; this chapter is none of these.
It was written by an engineer, not by a lawyer, and it is a heavily simplified overview of a very complex field.
The intent is to give you an overview of the basics so that you will know when to check whether something you want to do has potential legal ramifications.
Do not make any important decisions based solely on the contents of this chapter.*

(rr-licensing-useful)=
## Why This is Useful

Without a license, all rights are with the author of the code, and that means nobody else can use, copy, distribute, or modify the work without consent.
A license gives this consent.
If you do not have a license for your software, it is effectively unusable by the whole research community.



````{panels}
:column: col-md-4
:card: border-2
:header: bg-primary pa_dark
```{image} ../../../images/logos/TTW.svg
:height: 40px
:align: center
:name: Turing-Way-logo
```
^^^
[The Turing Way Book of Data Sciences](https://the-turing-way.netlify.app/reproducible-research/licensing.html)
````

