# The FAIR Cookbook :construction:

## A brief overview

This is the github repository for the `FAIR Cookbook`, assembled by the [IMI FAIRplus project](https://fairplus-project.eu/), an EU funded project running from *2018 to 2022*. The repository hosts  documentation, known as `FAIR recipes`, and supporting code in the form of `jupyter notebooks` about **`FAIRification processes`** and the content will be released regularly (quarterly) in order to reflect the work progress made by the project and the various working groups bringing together `academic` and `industry` partners.

---
## The official site

Visit [https://fairplus.github.io/the-fair-cookbook](https://fairplus.github.io/the-fair-cookbook) to see the web friendly **draft** version of the **FAIR Cookbook**.

:oil_drum::construction: **This project is still in early phase and this is work in progress** :construction::oil_drum:

---

## Roadmap and Timeline

The FAIRcookbook development process currently operates on a quarterly release cycle. Each cycle sees 2 `scrums` where specific `use cases` or `themes` are chosen and task forces assigned. The outcome of these efforts are new `FAIRification protocols`, or `FAIR recipes`, which after review are integrated to the main FAIRCookbook are tagged for release to the master branch, which is used to build the web-friendly version of the book.




---

- [x] FAIRcookbook development roadmap Gantt chart for the year 2020
<kbd>
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ2FudHRcblx0dGl0bGUgRkFJUiBDb29rYm9vayBEZXZlbG9wbWVudCBSb2FkbWFwIGFuZCBQcm9qZWN0ZWQgUmVsZWFzZSBDeWNsZXNcblx0ZGF0ZUZvcm1hdCAgWVlZWS1NTS1ERFxuXG5cdHNlY3Rpb24gSW5pdGlhbCBEcmFmdFxuICAgIGYyZiBIaW54dG9uICA6YTAsIDIwMjAtMDEtMjcsIDNkXG4gIFx0c2NydW0gMSAgICAgIDphZnRlciBhMCwgOTBkXG5cdFxuICBzZWN0aW9uIFNwcmluZyAyMDIwIFJlbGVhc2VcbiAgICBmMmYgQmFyY2Vsb25hICA6YTEsIDIwMjAtMDQtMjgsIDNkXG4gICAgc2NydW0gMiAgICAgICAgOmFmdGVyIGExLCA5MGRcblxuICBzZWN0aW9uIFN1bW1lciAyMDIwIFJlbGVhc2VcbiAgICBmMmYgVXRyZWNodDogYTIsIDIwMjAtMDctMjgsIDNkXG4gICAgc2NydW0gMyAgICAgICA6IGFmdGVyIGEyLCA5MGRcblxuICBzZWN0aW9uIEZhbGwgMjAyMDIgUmVsZWFzZVxuXHQgIGYyZiBNYW5jaGVzdGVyPyAgIDphMywgMjAyMC0xMC0yOCwgM2RcbiAgICBzY3J1bSA0ICAgICAgIDogYWZ0ZXIgYTMsIDkwZFxuXG5cdFx0XHRcdFx0IiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ2FudHRcblx0dGl0bGUgRkFJUiBDb29rYm9vayBEZXZlbG9wbWVudCBSb2FkbWFwIGFuZCBQcm9qZWN0ZWQgUmVsZWFzZSBDeWNsZXNcblx0ZGF0ZUZvcm1hdCAgWVlZWS1NTS1ERFxuXG5cdHNlY3Rpb24gSW5pdGlhbCBEcmFmdFxuICAgIGYyZiBIaW54dG9uICA6YTAsIDIwMjAtMDEtMjcsIDNkXG4gIFx0c2NydW0gMSAgICAgIDphZnRlciBhMCwgOTBkXG5cdFxuICBzZWN0aW9uIFNwcmluZyAyMDIwIFJlbGVhc2VcbiAgICBmMmYgQmFyY2Vsb25hICA6YTEsIDIwMjAtMDQtMjgsIDNkXG4gICAgc2NydW0gMiAgICAgICAgOmFmdGVyIGExLCA5MGRcblxuICBzZWN0aW9uIFN1bW1lciAyMDIwIFJlbGVhc2VcbiAgICBmMmYgVXRyZWNodDogYTIsIDIwMjAtMDctMjgsIDNkXG4gICAgc2NydW0gMyAgICAgICA6IGFmdGVyIGEyLCA5MGRcblxuICBzZWN0aW9uIEZhbGwgMjAyMDIgUmVsZWFzZVxuXHQgIGYyZiBNYW5jaGVzdGVyPyAgIDphMywgMjAyMC0xMC0yOCwgM2RcbiAgICBzY3J1bSA0ICAgICAgIDogYWZ0ZXIgYTMsIDkwZFxuXG5cdFx0XHRcdFx0IiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)</kbd>



- [x] The envisioned table of content for the  FAIR cookbook can be found [here](https://docs.google.com/spreadsheets/d/13B2aLm5ZXFUwAu6DlcL7soWL8yzX6juR4ijgUpzIsv4/edit?usp=sharing)     This Google Document is publicly available in `view mode`, and with `edit mode` for all FAIRplus members.

---

## Technology stack

The `FAIRcoobook` is built using [jupyter-book](https://jupyterbook.org/intro.html), following the practice used by the Alan Turing's Instute Book of Data Science.

* **[github](https://github.com)** is used to version control and hosting
* **[Markdown](https://guides.github.com/features/mastering-markdown/)** is used for the write-up
* **[HackMD](https://hackmd.io)** is used as Markdown Editor thanks to its integration with `github` and its [`browser extensions`](https://hackmd.io/s/hackmd-it)
* **[jupyter notebook](https://jupyter.org/)** can be used to provide executable code
* **[binder](https://mybinder.org)** is enabled which allows in web execution of any jupyter notebook distributed with the `FAIRCookbook`
* **[mermaid](https://mermaid-js.github.io/mermaid/#/)** javascript library is used to produce flowcharts, Gantt charts and pie charts used in the book.
<!--* **[netlify]()** is being tested for web hosting and deployment -->

* **[Jekyll Themes]()** provide the style for the web friendly version. The name of this theme is saved in the Jekyll `_config.yml` configuration file found in. [repository settings](https://github.com/fair-cookbook/the-fair-cookbook/settings).

### Support or Contact

Having trouble with Pages? Check out our [issue tracker](https://github.com/FAIRplus/the-fair-cookbook/issues) or [contact support](https://fairplus.github.io/the-fair-cookbook/People.html) and we’ll help you sort it out.
