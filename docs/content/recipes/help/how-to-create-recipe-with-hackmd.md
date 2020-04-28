# How to use HackMD to write a FAIR Cookbook Recipe 

**[The FAIR cookbook](https://fairplus.github.io/the-fair-cookbook/intro)**


# Table of Contents
1. [Main Objectives](#Main%20FAIRification%20Objectives)
2. [Authors](#Authors)
8. [License](#License)

---

## Main Objectives

>**This document aims to guide users through the process of getting set up to contribute content to the [the FAIR cookbok](https://fairplus.github.io/the-fair-cookbook/intro) using HackMD.io online editor.
The document contains a checklist taking you point by point through the installation process and through the 2 main ways of using HackMD.**



- [x] 1. create a github account and obtain your github handle (e.g. [@proccaserra](https://github.com/proccaserra)) 

- [x] 2. request to be added to the [FAIR Cookbook github repository](https://github.com/FAIRplus/the-fair-cookbook) and accept the invitation.
![](https://i.imgur.com/wyTn5aS.png)

- [x] 3. create a new issue in the [issue tracker](https://github.com/FAIRplus/the-fair-cookbook/issues).

![](https://i.imgur.com/frsBwqc.png =750x)>
    :information_source:  remember to assign yourself or a team member to the issue
    :information_source:  remember to assign the issue to a milestone
    :information_source: remember to tag the issue with relevant label

- [x] 4. create a new branch under the FAIR Cookbook github repository using the following command:
> git checkout -b recipe_xx master

- [x] 5. create a [HackMD.io](https://hackmd.io) account, simply using your github credentials
![](https://i.imgur.com/E2ok5ni.png =450x)

- [x] 6. :warning: **IMPORTANT: Install HackMD browser extension ([Chrome](https://chrome.google.com/webstore/detail/hackmd-it/cnephjboabhkldgfpdokefccdofncdjh), [Firefox](https://addons.mozilla.org/en-US/firefox/addon/hackmd-it/?src=search))**.

At the current time, the `HackMD-it` browser extension is only available for Chrome and Firefox and [this tutorial](https://hackmd.io/s/hackmd-it) details the installation procedure. 
Once you've carried the extension installation, any github repository for which you have access and for which HackMD app has been authorized (which is already the case for all FAIRplus github repositories), any `Markdown` document will be readily editable using 'HackMD' and you should see the following *icon* 

![](https://i.imgur.com/k79IQUA.png =145x)


in the github repository bar as shown in the figure below:


![](https://i.imgur.com/yI8TRNM.png)

:warning: This button will only be visible from Chrome or Firefox once the `HackMD` browser extension has been installed. 
:octopus: This will not be visible from Safari, Brave or Internet Explorer browsers *even if* you have HackMD activated for your repository.


- [x] 7. Getting familiar with MarkDown with a [good tutorial provided by Gitlab](https://about.gitlab.com/handbook/engineering/ux/technical-writing/markdown-guide/)
![](https://i.imgur.com/Kt3d9eo.png)


- [x] 8. Build confidence using HackMD

![](https://i.imgur.com/bt012cm.png)

use the split view to have what you type immediately rendered.

- [x] 9. Use the FAIRplus Recipe Template as guide


## There are 2 main ways to use HackMD.io:

1. From a Github repository, by editing an existing Markdown 

:warning: In order to be able to `push` a change to github from HackMD.io, it is **required** to first create a placeholder `markdown` file in the targeted github repository.

For instance, you want to create an new recipe, you first need to create `my_new_recipe.md` file under a branch of the FAIRcookbook repository.

```bash
touch my_new_recipe.md
git add my_new_recipe.md
git push origin my_recipe_branch
```

In a browser (one with the hackMD browser extension enabled), navigate to the recipe page on the github repository and click on the `hackMD` button ![](https://i.imgur.com/k79IQUA.png =145x)

This will launch the HackMD.io editor in a separate tab.

:warning: Toggling back to the github page, notice the following message, which highlights 2 options, one allowing to switch back to the editor view, one allowing to end it. 

![](https://i.imgur.com/3uqMaT3.png)

By pressing `Stop Editing`, HackMD.io tab closes and the user is taken back to Github page. The user is now offered to either `commit changes` or `cancel`

:radioactive_sign: Pressing `cancel` will lose any changes made during the editing phase.

:information_source: Pressing `commit change` offers two options. We **strongly recommend** using the `create a new branch for this commit and start a pull request` option when choosing to commit changes. This is good practice and always remember to assign a reviewer and set a milestone when sending the `pull request`


2. Directly from HackMD by creating a new note from the tool itself

To do so, open HackMD and go the `New Note`
![](https://i.imgur.com/KMsANJL.png =345x)

This will open a empty HackMD page and if one presses `pull from Github`, a pop-up will open and allow users to select: 
- a github repository
- a branch in the repository
- a file in that branch

Fill in the relevant information (all required) before it is possible to hit the blue `pull` button.

![](https://i.imgur.com/Bccq6OD.png)


If the `pull` is successful, the user can now edit the document.

When the edits are completed, the user can push the file back to github. To do so, one needs to hit the '...' icon in the top right-hand corner of the HackMD menu bar, as show below:

![](https://i.imgur.com/0TdXGl0.png =400x)

Navigate to `Versions`. This will bring the following window:

![](https://i.imgur.com/6AUdRLo.png)

Press the blue 'Push to Github' button to bring up the following menu:

![](https://i.imgur.com/zSMLtMU.png)

The process is very similar to that described when pulling a file. Except that is now possible to create a branch for the commit, an option we recommend using.

![](https://i.imgur.com/rheX0ib.png)

Fill all the necessary information and press the blue `Push` button.

:radioactive_sign: If unsure about these steps, contact the FAIRPlus editorial team for assistance, using the dedicated email or via our slack channel.


___
## Authors:

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Philippe Rocca-Serra |  University of Oxford, Data Readiness Group| [0000-0001-9853-5668](https://orcid.org/orcid.org/0000-0001-9853-5668) | Writing - Original Draft |
| Susanna-Assunta Sansone |  University of Oxford, Data Readiness Group | | Writing - Review & Editing, Funding acquisition | 

___
## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>
