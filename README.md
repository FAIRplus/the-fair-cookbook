# The FAIR Cookbook

[![Jupyter Book Badge](https://jupyterbook.org/badge.svg)](https://faircookbook.elixir-europe.org/content/home.html)    
![license](https://img.shields.io/badge/license-CC--BY--4.0-blue)
![build](https://github.com/FAIRplus/the-fair-cookbook/actions/workflows/build-migrating.yml/badge.svg?branch=main)
[![contribute content](https://img.shields.io/badge/contribute-content-blueviolet)](https://github.com/FAIRplus/the-fair-cookbook/issues/new?assignees=proccaserra&labels=issue+type%3A+meta+checklist%2Cauthor%27s+task%3A+write+abstract%2Ceditor%27s+task%3A+identify+author&template=meta-checklist.md&title=TitleOfRecipe)



FAIR is for **F**indable, **A**ccessible, **I**nteroperable and **R**eusable. 

This means: 
  - your data and services can be cited
  - the impact and visibility of your research will be increased
  - you benefit the public good
  - your data is more useful because it is easier to compare with other data
  
This FAIR cookbook gives you step-by-step recipes for making your data FAIR.


## For readers

You are probably looking for [https://fairplus.github.io/the-fair-cookbook](https://fairplus.github.io/the-fair-cookbook). Or do you want to leave feedback? If so, please see below.


## For authors, editors, and developers 

More information about the authors of the FAIRPlus Cookbook is available here: [Info For Authors](https://fairplus.github.io/the-fair-cookbook/content/home.html)


## Feedback, support or contact

Having trouble with the page? Want to give feedback? 

- Option 1: Drop us a line at: FAIRplus-cookbook@elixir-europe.org 
- Option 2: File an Issue here on [GitHub tracker](https://github.com/FAIRplus/the-fair-cookbook/issues). Looking forward to hear from you!


## Deploy locally:


- Using Docker:

`zsh ./scripts/docker.sh` # for MacOS users 

or 

`bash ./scripts/docker.sh` # for unix users

- From outside the project:
`jupyter-book build -W -n --keep-going the-fair-cookbook`
