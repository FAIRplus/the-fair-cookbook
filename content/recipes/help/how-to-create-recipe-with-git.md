(fcb-help-recipe-git)=
# Add via Git

## Main Objectives 

The main purpose of this recipe is:

> Learn how to set up git to commit to the FAIR Cookbook

---

## Graphical Overview of the FAIRification Recipe Objectives 

<div class="mermaid">
graph TD;
    A[Data FAIRification] -->B(Write-up FAIRification experience)
    B --> C{know markdown?}
    C -->|Yes| D(use the markdown recipe template)
    C -->|No| E(use Google doc recipe template instead)
</div>


## Prequisites and Getting Set up 

We rely on github infrastructure for hosting the documents making up the cookbook. The reliance of git subversion system ensures robust data provenance tracking as well as traceability of authors contributions.

To make the most of the github infrastructure, we *strongly* advise about following the git flow process, which we will detail now.

Clone the repo, enter the directory, and test that you are in the master branch by issuing the following command from the terminal:

```bash
git clone http://github.com/FAIRplus/the-fair-cookbook/
cd the-fair-cookbook
git branch 
```

should show:
 
```bash
master 
```

then issue the following git command:

```bash
git checkout -b my_username-my_recipe_branch master
git branch
```

should show:

```bash
my_recipe
```


This means you are working on the dedicated copy of the master branch, any change made there will not affect the master files. 

When you are done with your edits, use:

```bash
git add .
git commit -m 'some meaninful message, possibly indicated that would be closing an issue'
```

followed by:

```bash
git push origin my_recipe_branch
```


If you are done with all the edits, you are now ready to send a "Pull Request" to the `master` branch. In github speak and jargon, a `pull request` always specifies a repository and a branch to merge into from a development branch on a repo (forked from a repo and simple cloned from the master as we are currently doing)


When sending a `Pull Request` aslo known as `PR`, you will have to specify a `reviewer` known as an `assignee` in the github  world. This optimally ensures that someone will review the contribution before `merging` it with the main `master` branch of the repository.
You should **NEVER** merge into the master branch without a review (unless you are the master owner / editor in chielf / benevolent dictator for life).



Upon this `pull request`, the `assignee` will perform a review of the contribution. The contribution will either be merged in the master if all the quality control checks have passed or will be sent for correction to the submitter. the submitter will carry out the correction and send a new pull request for revision, following the same pattern of revision, submission acceptance merge.



**Key ideas:**
- Each recipe should be developed in its own branch from the main github repository or from a branch in a forked version of the said repository.
more information from the 
- commit often
- remember to pull before committing in order to incorporate the latest changes from the master.


### test, test and test again before pushing!

So you just wrote a new recipe and you'd like to see how it looks in the FAIRplus cookbook, what do you need to know ?

 1. Make sure your new recipe is listed in the **`_data/toc.yml`** file  where toc.yml is a YAML formatted file defining the Table of Content of the FAIR Cookbook.

 2. Make sure you have python virtualenv running and where you have installed the jupyter-book python module. If you don't know what I am talking about, do the following:

	1. install pyenv
	2. once done, run `pyenv install <python version>`, for instance 
```bash
pyenv install 3.7.5
```

	3. then you need to create the virtual environment by invoking:
```bash
pyenv virtualenv faircb375 3.7.5
```
	4. to use the virtual environment, you'll have to call it using the following command:
```bash
pyenv activate faircb375
```
		if all goes well, your terminal prompt should give you the status, indicate you are running in a virtualenv:
 ```bash
(venv372) hodr-MacBook-Pro-3:docs bob$
 ```

	5. Now install the python module **`jupyter-book`**. to do so, simply issue the following command:
```bash
pip install jupyter-book
```

		NOTE: you may have to update `pip` if the system complains, sending a message looking like this 
```
to update pip, issue `pip install pip --upgrade'
```
		**Huzza!** You are now reading te test if yuor recipe can be built in the jupyter-book. To just do this, you need to run the following command from the root of the github branch.
```bash
jupyter-book build docs --overwrite
```
<p style='text-align: justify;'>
	where
		- `build` is one of the command available from jupier-book package
		- `docs` is the name of the target book (it has to be that string)
		- `--overwrite` is an parameter to the `'buils'` 
The command telling it to ...well discard all previously generated files by writing over them...pretty seff explanatory so far.
if all goes well, you should have a green banner. If the process fails, your terminal will display a stack trace, indicateing that there is an error in your markdown files or your toc.yml.
if all is well, test locally by start a jekyll server. To do so, you'll have to do:
</p>

```bash
cd docs
make serve
```
Open a new tab in your favourite browser and point to the url `http://127.0.0.1:4000/the-fair-cookbook/` 


## Option 1: Writing the recipe in Markdown syntax

 - use the recipe template available from the issue tracker ["create new recipe"](https://github.com/FAIRplus/the-fair-cookbook/issues/new/choose)
 - the template uses the [Markdown syntax], for which guidelines are available [here](https://guides.github.com/features/mastering-markdown/)
 - the recipe template provides key sections for consistently structuring information about the process you want to document.
 - briefly, you will need to fill in the following 5 sections:

 1. licence information:
 	you may use the default information which is provided or provide the terms of use of your liking.

 2. goal and objective of the recipe
 	you need to summerize the task using keywords, ideally expressing them in terms of `process` or `capability`.
 	you should also annotate the terms with an ontology term, coming from resources such as. `EDAM.action` or `OBI.planned_process` or `OBI.data_transformation`

 3. declare and list the input information types (data files, data types) and the expected output datatypes.
 	you should use the table provided to structure the information and annotate those input. & output to indicate the file formats. 

 	 For doing so, we strongly recommend performing a mark up by linking to either a [FAIRsharing record about standards](https://www.fairsharing.org) and with and [EDAM.datatype](https://www.ebi.ac.uk/ols/ontologies/edam)

 4. provide an overall graphical representation of the flow of actions required to accomplish the objectives set considering the set of input data elements.

 	the representation may be done using the markdown syntax defined by the [mermaid project](https://mermaid-js.github.io/mermaid/#/)*

 	graphic representation currently encompass visual representatiion such as Gantt chart, Flow Chart, Flow Diagram and Sequence Diagram. These diagrammtic represntations are particularly useful to indicate key decision processes, action to perform and data transfrormation path which may be considered in various contexts.

 5. provide executable code in the form a notebook. the code could be organized according to the cookie cutter templates for data science, which enhances the replicability of the process.

 	you may also provide a machine actionable workflow and associated containers for execution in a safe environment or as microservice.

 6. don't forget to fill in the table of authors and contributors, by making sure you provide the orcid for each of contributors and the contribution by using the [CredIT role](https://casrai.org/credit/)

 7. consider minting a DOI for the new recipe, so it is citeable and versionned.


## Option 2: Writing the recipe as a Google document

The main benefits are the collaborative editing feature capabilities this allows.
The main drawbacks are the conversion losses that are bound to happen when using add-ons such as:

- [https://github.com/supreetpal/gdoc-markdown-converter/](https://github.com/supreetpal/gdoc-markdown-converter/blob/develop/README.md)

- [https://github.com/mangini/gdocs2md](https://github.com/mangini/gdocs2md)


:zap: this add-ons may create security concerns and may not run on the FAIRplus googledrive, meaning the conversion would have to happen outside that private drive. 



## Dealing with merge conflicts

See [Resolving a merge conflict using the command line](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/resolving-a-merge-conflict-using-the-command-line)





````{dropdown} **References**
````

## Authors

````{authors_fairplus}
Philippe: Writing - Review & Editing
Susanna: Writing - Review & Editing
````


## License

````{license_fairplus}
CC-BY-4.0
````


