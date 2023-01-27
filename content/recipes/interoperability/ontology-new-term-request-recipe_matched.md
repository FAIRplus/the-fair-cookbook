(fcb-interop-ontorequest)=
# Requesting new terms


````{panels_fairplus}
:identifier_text: FCB021
:identifier_link: 'https://w3id.org/faircookbook/FCB021'
:difficulty_level: 1
:recipe_type: guidance
:reading_time_minutes: 15
:intended_audience: terminology_manager, data_manager, data_scientist, ontologist 
:maturity_level: 3
:maturity_indicator: 33
:has_executable_code: nope
:recipe_name: Requesting new terms from terminologies and ontologies
```` 

## Main Objective

Terms could be missing from public ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  of choice. Where needed, new terms can be requested for these ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) . The objective of this recipe is to provide a general guidline on how to request new terms, as well as to give some examples for specific ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) .

Requesting(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) new terms in public (biomedical) ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  might be a structured, streamlined process or completely undocumented, depending on the actual ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) . Also, the process can take somewhere between days and up to a year, depending on the implemented release cycles of the target ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) .

Some ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) , often large project (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=project) s organized by consortia, have a detailed formal request process, maybe even with a dedicated ticketing and tracking system. A big number of ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  rely on [GitHub](https://github.com(URL_TO_INSERT_RECORD https://github.com/)) as a publicly accessible ticketing system for reporting issues on the ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  and also for requesting(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) new terms. They might provide explicit guideline (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=reporting_guideline) s on how to create an issue for a new term request, or they rely on GitHub(URL_TO_INSERT_RECORD https://github.com/)(URL_TO_INSERT_RECORD https://github.com/) issues without guideline (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=reporting_guideline) s. And there are also ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  relying on email for requesting(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) new terms. These different request processes can be summarized as follows:
* Formal request process
* Request via GitHub(URL_TO_INSERT_RECORD https://github.com/)(URL_TO_INSERT_RECORD https://github.com/) with explicit guideline (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=reporting_guideline) s
* Request via GitHub(URL_TO_INSERT_RECORD https://github.com/)(URL_TO_INSERT_RECORD https://github.com/) without guideline (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=reporting_guideline) s
* Request via email

In most ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) , everybody can request new terms. However, in some ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  only members have access to the request process. In case of a request process organized via GitHub(URL_TO_INSERT_RECORD https://github.com/)(URL_TO_INSERT_RECORD https://github.com/), a free [GitHub(URL_TO_INSERT_RECORD https://github.com/)(URL_TO_INSERT_RECORD https://github.com/) account](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/join) is required.


## Ingredients
* List of new terms
* Target ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) 
    * E.g. SNOME(URL_TO_INSERT_RECORD https://openmicroscopy.org)D CT, MedDR(URL_TO_INSERT_RECORD http://data.donders.ru.nl)A(URL_TO_INSERT_RECORD https://www.ddbj.nig.ac.jp/dra/index-e.html)(URL_TO_INSERT_RECORD http://www.meddra.org/), OBI(URL_TO_INSERT_RECORD http://obi-ontology.org/), EFO(URL_TO_INSERT_RECORD https://www.ebi.ac.uk/efo/)(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/FO), BAO(URL_TO_INSERT_RECORD http://bioportal.bioontology.org/ontologies/AO)(URL_TO_INSERT_RECORD http://bioassayontology.org), CL(URL_TO_INSERT_RECORD https://github.com/obophenotype/cell-ontology), RxNorm(URL_TO_INSERT_RECORD https://www.nlm.nih.gov/research/umls/rxnorm/), BT(URL_TO_INSERT_RECORD http://biotopontology.github.io/)O(URL_TO_INSERT_RECORD http://www.brenda-enzymes.info)(URL_TO_INSERT_RECORD http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab) - BRENDA(URL_TO_INSERT_RECORD https://www.brenda-enzymes.org/)(URL_TO_INSERT_RECORD https://nda.nih.gov), DC(URL_TO_INSERT_RECORD http://dublincore.org/documents/dces/)(URL_TO_INSERT_RECORD https://doi.org/10.25504/FAIRsharing.3nx7t)AT(URL_TO_INSERT_RECORD https://www.w3.org/TR/vocab-dcat/)(URL_TO_INSERT_RECORD http://cat.aii.caas.cn/) 2
    
## Graphical Overview


````{dropdown} 
:open:
```{figure} onto-new-term.png
---
width: 650px
name: Process for requesting(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) an new term to a terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) 
alt: Process for requesting(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) an new term to a terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) 
---
Process for requesting(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) an new term to a terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) .
```
````


## FAIRification Objectives, Inputs and Outputs
| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| [text annotation](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/operation_3778)  | new term(s), [ontology](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/data_0582) | [ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  term](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/data_0966), [annotated text](http://edamontology.org(URL_TO_INSERT_RECORD http://edamontology.org)/data_3779)  |

## Table of Data Standards

| Data Format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) s  | Ontologies (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  |
| :------------- | :------------- |
| [OWL](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.atygwy)  | [OBI](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.284e1z), [Cell Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) (URL_TO_INSERT_RECORD https://github.com/obophenotype/cell-ontology)](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.j9y503)|
| [OBO](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.aa0eat)  | [Cell Ontology(URL_TO_INSERT_RECORD https://github.com/obophenotype/cell-ontology)](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.j9y503)  |
| Release Format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)  2 | [SNOME(URL_TO_INSERT_RECORD https://openmicroscopy.org)D CT](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.d88s6e)|
| Rich Release Format (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format)  |[RxNorm(URL_TO_INSERT_RECORD https://www.nlm.nih.gov/research/umls/rxnorm/)](https://fairsharing.org(URL_TO_INSERT_RECORD https://fairsharing.org/)(URL_TO_INSERT_RECORD https://fairsharing.org)(URL_TO_INSERT_RECORD https://fairsharing.org/)/FAIRsharing.36pf8q)|

## Step-by-Step process

**Step 1**
Identify and describe relevant terms not included in public ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  of choice.

**Step 2**
Identify request process of the public ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  (i.e. formal request process, GitHub(URL_TO_INSERT_RECORD https://github.com/)(URL_TO_INSERT_RECORD https://github.com/) request with guideline (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=reporting_guideline) s, GitHub(URL_TO_INSERT_RECORD https://github.com/)(URL_TO_INSERT_RECORD https://github.com/) request without guideline (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=reporting_guideline) s, email request).

**Step 3**
Prepare at least the following informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion for requesting(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) a new term:
* justification for the request
* preferred term label: a unique, unambiguous label for the term
* potential alternative terms: common synonyms or translations
* textual definition: expresses the meaning of the term, add sources and fully expand abbreviations
* logical definition: suggest parent and child terms
* example of usage: propose a use case
* attribution: contributor names (and ORCID(URL_TO_INSERT_RECORD https://cid.curie.fr)(URL_TO_INSERT_RECORD http://orcid.org/)s)

**Step 4**
Finalize and submit term request. Depending on the ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) , it can take up to a year to have the new term incorporated in the ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) , or to have the request rejected.


## Examples

### Formal request process

**Example ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) :**
[SNOME(URL_TO_INSERT_RECORD https://openmicroscopy.org)D CT - Systematized Nomenclature of Medicine](http://www.snomed.org/)

**Scope of the ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) :**
conditions, clinical findings, procedures, body structures, substances, pharmaceuticals, devices, specimen

**Informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion about requesting(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) changes or additions:**
SNOME(URL_TO_INSERT_RECORD https://openmicroscopy.org)D CT has a [Content Request Service (CRS)](https://confluence.ihtsdotools.org/display/SCTCR/CRS+User+Guide). Requests can be submitted by members of SNOME(URL_TO_INSERT_RECORD https://openmicroscopy.org)D International, Nationale Release Centers or other authorized users, and must align with the [Editorial guide](https://confluence.ihtsdotools.org/display/DOCEG). 
When submitting a request, it is important to follow the aspects mentioned in **Step 3** of the **Step-by-Step process**. In addition to these aspects, the following is important to provide as well:
* Reference(s) from a scientific or professional journal (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=journal) , or professional society (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=society) 
* Fully expanded abbreviations

When submitting to the CRS(URL_TO_INSERT_RECORD http://rgd.mcw.edu/rgdweb/ontology/view.html?acc_id=RS:0000457), a request can have one of the sixteen possible statuses ('New', 'Draft', 'Accepted', 'Under Authoring', 'Ready for Release', 'In Inception', 'Clarification Needed', 'Pending Internal Input', 'On Hold', 'Forwarded', 'Withdrawn', 'Rejected', 'Completed', 'Appeal','Appeal rejected', 'In Appeal Clarification'). Within CRS(URL_TO_INSERT_RECORD http://rgd.mcw.edu/rgdweb/ontology/view.html?acc_id=RS:0000457), submitters are notified when a status has been changed.

More informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion can be found [here](https://www.snomed.org/snomed-ct/change-or-add) and in this [guide](https://www.snomed.org/SNOMED/media/SNOMED/documents/Version-8-0-CRS-Customer-Guidance-20191024.pdf).

### Request via GitHub with explicit guidelines

**Example ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) :**
[OBI(URL_TO_INSERT_RECORD http://obi-ontology.org/) - Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  for Biomedical Investigations(URL_TO_INSERT_RECORD http://obi-ontology.org/)](http://obi-ontology.org(URL_TO_INSERT_RECORD http://obi-ontology.org/)/)

**Scope of the ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) :**
assays, devices, objectives in scientific investigations

**Informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion about requesting(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) changes or additions:** 
OBI(URL_TO_INSERT_RECORD http://obi-ontology.org/) provides a [GitHub(URL_TO_INSERT_RECORD https://github.com/)(URL_TO_INSERT_RECORD https://github.com/) repository](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/obi-ontology/obi) and a mailing list. New-term requests are handle(URL_TO_INSERT_RECORD http://handle.net)d as GitHub(URL_TO_INSERT_RECORD https://github.com/)(URL_TO_INSERT_RECORD https://github.com/) issues. There is an explicit [guideline (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=reporting_guideline)  document](http://obi-ontology.org(URL_TO_INSERT_RECORD http://obi-ontology.org/)/page/OBI_term_guidelines) on how to request new terms.

For a proposed new term, they ask for the following informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion:
* editor preferred term: a unique, unambiguous label for the term in American English
* alternative terms: common synonyms or translations
* textual definition
* definition source for the textual definition
* logical definition (or parent term)
* example of usage
* term editor: your name, and that of any collaborators, as it should appear in OBI(URL_TO_INSERT_RECORD http://obi-ontology.org/)

### Request via GitHub without guidelines

**Example ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) :**
[CL(URL_TO_INSERT_RECORD https://github.com/obophenotype/cell-ontology) - Cell Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) (URL_TO_INSERT_RECORD https://github.com/obophenotype/cell-ontology)](http://obofoundry.org/ontology/cl.html)

**Scope of the ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) :**
cell types

**Informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion about requesting(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) changes or additions**:
The Cell Ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) (URL_TO_INSERT_RECORD https://github.com/obophenotype/cell-ontology) provides a [GitHub(URL_TO_INSERT_RECORD https://github.com/)(URL_TO_INSERT_RECORD https://github.com/) repository](https://github.com(URL_TO_INSERT_RECORD https://github.com/)/obophenotype/cell-ontology(URL_TO_INSERT_RECORD https://github.com/obophenotype/cell-ontology)), a contact email, and a mail list. New-term requests (NTR(URL_TO_INSERT_RECORD https://www.trialregister.nl/)) are formulated as issues on the GitHub(URL_TO_INSERT_RECORD https://github.com/)(URL_TO_INSERT_RECORD https://github.com/) repository (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=repository) . 

### Request via email

**Example ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) :**
[RxNorm(URL_TO_INSERT_RECORD https://www.nlm.nih.gov/research/umls/rxnorm/)](https://www.nlm.nih.gov/research/umls/rxnorm(URL_TO_INSERT_RECORD https://www.nlm.nih.gov/research/umls/rxnorm/)/index.html)

**Scope of the ontology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact) :**
drugs

**Informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion about requesting(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) changes or additions**:
Informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion about requesting(URL_TO_INSERT_RECORD http://sms.cbi.cnptia.embrapa.br/SMS/index_s.html) terms can be found in the [FAQ section](https://www.nlm.nih.gov/research/umls/faq_main.html) of the Unified Medical Language System (UMLS) where RxNorm(URL_TO_INSERT_RECORD https://www.nlm.nih.gov/research/umls/rxnorm/) is part of.  

Changes or additions to UMLS can be requested by contacting [NLM Customer Support](https://support.nlm.nih.gov). The NLM Customer Support can be contacted through a [form](https://support.nlm.nih.gov/support/create-case/). If additions are specific to the source, you should contact the terminology (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=terminology_artefact)  source provider. Contact informat (URL_TO_INSERT_TERM https://fairsharing.org/search?recordType=model_and_format) ion is available in [Appendix 1](https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/license_agreement_appendix.html) of the Licence agreement.

UMLS is updated in May and November of each year.



## References
````{dropdown} **References**
````

## Authors

````{authors_fairplus}
Ulrich: Writing - Original Draft
Emma: Writing - Original Draft
Philippe: Writing - Review & Editing, Conceptualization 
````

## License

````{license_fairplus}
CC-BY-4.0
````




