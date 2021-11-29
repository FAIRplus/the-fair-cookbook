(fcb-help-recipe-hackmd)=
# Add via HackMD 

<!-- **[The FAIR cookbook](https://fairplus.github.io/the-fair-cookbook/intro)**

**identifier:** [RX.X](RX.X)

**version:** [v1.0](v1.0)

---

**_Difficulty level:_** moderate :triangular_flag_on_post: :triangular_flag_on_post: :white_circle:  :white_circle: :white_circle:

**_Reading time:_** 30 minutes 

**_Intended Audience:_** 

> :heavy_check_mark: FAIR Cookbook Contributors

> :heavy_check_mark: Data Managers

> :heavy_check_mark: Data Scientists



**_Recipe Type_**: Hands on

**_Executable code_**: No

--- -->

## Main Objectives

>**This document aims to guide users through the process of getting set up to contribute content to [the FAIR cookbook](https://fairplus.github.io/the-fair-cookbook/intro) using HackMD.io online editor.
The document contains a checklist taking you point by point through the installation process and through the 2 main ways of using HackMD.**


```{warning}
 ⚡ **IMPORTANT: Install the HackMD browser extension ([Chrome](https://chrome.google.com/webstore/detail/hackmd-it/cnephjboabhkldgfpdokefccdofncdjh), [Firefox](https://addons.mozilla.org/en-US/firefox/addon/hackmd-it/?src=search))!**
```

At the current time, the `HackMD-it` browser extension is only available for Chrome and Firefox and [this tutorial](https://hackmd.io/s/hackmd-it) details the installation procedure. 
Once you've carried the extension installation, any github repository for which you have access and for which HackMD app has been authorized (which is already the case for all FAIRplus github repositories), any `Markdown` document will be readily editable using 'HackMD' and you should see the following *icon* 

<div> <img src="/images/k79IQUA.png" alt="drawing" style="width:145px;" border="1px solid black" align="top" /></div>

in the github repository bar as shown in the figure below:

<div> <img src="/images/yI8TRNM.png" alt="drawing" style="width:750px;" border="1px solid black" align="top" /></div>


</br>

⚡ This button will only be visible from Chrome or Firefox once the `HackMD` browser extension has been installed.

🐙 This will not be visible from Safari, Brave or Internet Explorer browsers *even if* you have HackMD activated for your repository.



## Create a github account and obtain your github handle

## Request to be added to the [FAIR Cookbook github repository](https://github.com/FAIRplus/the-fair-cookbook) and accept the invitation.
<div> <img src="/images/wyTn5aS.png" alt="drawing" style="width:750px;" border="1px solid black" align="top" /></div>

## Create a new recipe
### Create a new issue in the [issue tracker](https://github.com/FAIRplus/the-fair-cookbook/issues)

<div> <img src="/images/frsBwqc.png" alt="drawing" style="width:750px;" border="1px solid black" align="top" /></div>

</br>

ℹ️  remember to assign yourself or a team member to the issue
ℹ️  remember to assign the issue to a milestone
ℹ️ remember to tag the issue with relevant label

## Create a new branch under the FAIR Cookbook github repository using the following command:
> git checkout -b recipe_xx master

## Create a [HackMD.io](https://hackmd.io) account, simply using your github credentials
<div> <img src="/images/E2ok5ni.png" alt="drawing" style="width:450px;" border="1px solid black" align="top" /></div>



## Getting familiar with MarkDown

Here is a [good tutorial provided by Gitlab](https://about.gitlab.com/handbook/engineering/ux/technical-writing/markdown-guide/)
![](/images/Kt3d9eo.png)


## Build confidence using HackMD

![](/images/bt012cm.png)

use the split view to have what you type immediately rendered.

## Use the FAIRplus Recipe Template as guide

FAIRPlus Cookbook Team is working at establishing a standard layout for easing the creation of a new recipe. The template contains key sections and outlines, which will help boostrap the process.

[recipe template](https://github.com/FAIRplus/the-fair-cookbook/edit/dev/docs/content/recipes/help/recipe-template.md)


## Writing notes with HackMD.io:

1. From a Github repository, by editing an existing Markdown 

⚡  In order to be able to `push` a change to github from HackMD.io, it is **required** to first create a placeholder `markdown` file in the targeted github repository.

For instance, you want to create an new recipe, you first need to create `my_new_recipe.md` file under a branch of the FAIRcookbook repository.

```bash
touch my_new_recipe.md
git add my_new_recipe.md
git push origin my_recipe_branch
```

In a browser (one with the hackMD browser extension enabled), navigate to the recipe page on the github repository and click on the `hackMD` button ![](/images/k79IQUA.png =145x)

This will launch the HackMD.io editor in a separate tab.

⚡  Toggling back to the github page, notice the following message, which highlights 2 options, one allowing to switch back to the editor view, one allowing to end it. 

![](/images/3uqMaT3.png)

By pressing `Stop Editing`, HackMD.io tab closes and the user is taken back to Github page. The user is now offered to either `commit changes` or `cancel`

☢️ Pressing `cancel` will lose any changes made during the editing phase.

ℹ️  Pressing `commit change` offers two options. We **strongly recommend** using the `create a new branch for this commit and start a pull request` option when choosing to commit changes. This is good practice and always remember to assign a reviewer and set a milestone when sending the `pull request`


2. Directly from HackMD by creating a new note from the tool itself

To do so, open HackMD and go the `New Note`
![](/images/KMsANJL.png =345x)

This will open a empty HackMD page and if one presses `pull from Github`, a pop-up will open and allow users to select: 
- a github repository
- a branch in the repository
- a file in that branch

Fill in the relevant information (all required) before it is possible to hit the blue `pull` button.

![](/images/Bccq6OD.png)


If the `pull` is successful, the user can now edit the document.

When the edits are completed, the user can push the file back to github. To do so, one needs to hit the '...' icon in the top right-hand corner of the HackMD menu bar, as show below:

![](/images/0TdXGl0.png =400x)

Navigate to `Versions`. This will bring the following window:

![](/images/6AUdRLo.png)


Press the blue 'Push to Github' button to bring up the following menu:

![](/images/zSMLtMU.png)

The process is very similar to that described when pulling a file. Except that is now possible to create a branch for the commit, an option we recommend using.

![](/images/rheX0ib.png)

Fill all the necessary information and press the blue `Push` button.



## Conclusion:

>This recipe should get you started to contribute content, writing markdown documents, following the FAIRplus guidance and FAIRplus recipe template.
>
>☢ If unsure about these steps, contact the FAIRPlus editorial team for assistance, using the [dedicated email](mailto:FAIRplus-cookbook@elixir-europe.org) or via our [github issue tracker](https://github.com/FAIRplus/the-fair-cookbook/issues).
> ### What should I read next?
> * [HackMD & MarkDown Tips and Tricks](fcb-help-tips)
> * [How to create jupyter notebook?](https://jupyter-notebook.readthedocs.io/en/stable/)
> * [FAIRplus recipe template](https://the-fair-cookbook.netlify.app/recipes/help/recipe-template)


---

## Authors:

| Name                                                                                                                                                                            | Orcid                                                                                                         | Affiliation              | Type                                                                              |                                                              Elixir Node                                                              | Credit Role
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|--------------------------|-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------:|:----------------:|
| <div class="firstCol"><a target="_blank" href='https://github.com/proccaserra'><img class='avatar-style' src='https://avatars.githubusercontent.com/proccaserra'></img><div class="d-block">Philippe Rocca-Serra</div></a>  </div>         | <a target="_blank" href='https://orcid.org/0000-0001-9853-5668'><i class='fab fa-orcid fa-2x text--orange'></i></a> | University of Oxford     | <i class="fas fa-graduation-cap fa-1x text--orange" alt="Academic"></i> | <img class='elixir-style' src='/the-fair-cookbook/_static/images/logo/Elixir/ELIXIR-UK.svg' ></img> | Writing - Original Draft|
| <div class="firstCol"><a target="_blank" href='https://github.com/susannasansone'><img class='avatar-style' src='https://avatars.githubusercontent.com/susannasansone'></img><div class="d-block">Susanna-Assunta Sansone</div></a> </div> | <a target="_blank" href='https://orcid.org/0000-0001-5306-5690'><i class='fab fa-orcid fa-2x text--orange'></i></a> | University of Oxford     | <i class="fas fa-graduation-cap fa-1x text--orange" alt="Academic"></i> | <img class='elixir-style' src='/the-fair-cookbook/_static/images/logo/Elixir/ELIXIR-UK.svg' ></img> | Writing - Review & Editing, Funding acquisition |

---


## License:

This page is released under the Creative Commons 4.0 BY license.

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png" height="20"/></a>
