(fcb-misc-contribute)=
# How to contribute

Welcome to the `FAIR cookbook` repository! We're excited you're here and want to contribute.

These guidelines are designed to make it as easy as possible to get involved.
If you have any questions that aren't discussed below, please let us know by opening an [issue][link_issues]!

Before you start you'll need to set up a free [GitHub][link_github] account and sign in.
Here are some [instructions][link_signupinstructions].

Already know what you're looking for in this guide? Jump to the following sections:

* {ref}`fcb-joining-the-conversation`
* {ref}`fcb-contributing-through-github`
* {ref}`fcb-understanding-issues-milestones-and-project-boards`
* {ref}`fcb-making-a-change`
* {ref}`fcb-recognizing-contributions`

(fcb-joining-the-conversation)=
## Joining the conversation

`FAIR cookbook` is a young project maintained by a growing group of enthusiastic developers&mdash; and we're excited to have you join!
Most of our discussions will take place on open [issues][link_issues].

As a reminder, we expect all contributors to `FAIR cookbook` to adhere to the [FAIR cookbook Code of Conduct][link_coc] in these conversations.

(fcb-contributing-through-github)=
## Contributing through GitHub

- [git][link_git] is a really useful tool for version control.
- [GitHub][link_github] sits on top of git and supports collaborative and distributed working.

You'll use [Markdown][markdown] to chat in issues and pull requests on GitHub.
You can think of Markdown as a few little symbols around your text that will allow GitHub
to render the text with formatting.
For example you could write words as bold (`**bold**`), or in italics (`*italics*`).
<!-- ,
or as a [link][rick_roll] (`[link](https://https://youtu.be/dQw4w9WgXcQ)`) to another webpage. -->

GitHub has a helpful page on
[getting started with writing and formatting Markdown on GitHub][writing_formatting_github].

(fcb-understanding-issues-milestones-and-project-boards)=
## Understanding issues, milestones and project boards

Every project on GitHub uses [issues][link_issues] slightly differently.

The following outlines how the `FAIR cookbook` developers think about these tools.

**Issues** are individual pieces of work that need to be completed to move the project forwards.
A general guideline: if you find yourself tempted to write a great big issue that
is difficult to describe as one unit of work, please consider splitting it into two or more issues.

Issues are assigned [labels](#issue-labels) which explain how they relate to the overall project's
goals and immediate next steps.


### Issue labels

The current list of labels are [here][link_labels].

(fcb-making-a-change)=
## Making a change

We appreciate all contributions to `FAIR cookbook`, but those accepted fastest will follow a workflow similar to the following:

**1. Comment on an existing issue or open a new issue referencing your addition.**

This allows other members of the jupyter-book development team to confirm that you aren't overlapping with work that's currently underway and that everyone is on the same page with the goal of the work you're going to carry out.

[This blog][link_pushpullblog] is a nice explanation of why putting this work in up front is so useful to everyone involved.

**2. [Fork][link_fork] the [jupyter-book repository][link_jupyter-book] to your profile.**

This is now your own unique copy of `FAIR cookbook`.
Changes here won't effect anyone else's work, so it's a safe space to explore edits to the code!

Make sure to [keep your fork up to date][link_updateupstreamwiki] with the master repository.

**3. Make the changes you've discussed.**

Try to keep the changes focused.
We've found that working on a [new branch][link_branches] makes it easier to keep your changes targeted.

**4. Submit a [pull request][link_pullrequest].**

A member of the development team will review your changes to confirm that they can be merged into the main code base.
When opening the pull request, we ask that you follow some [specific conventions](#pull-requests).
We outline these below.

### Pull Requests

To improve understanding pull requests "at a glance", we encourage the use of several standardized tags.
When opening a pull request, please use at least one of the following prefixes:

* **[BRK]** for changes which break existing builds or tests
* **[DOC]** for new or updated documentation
* **[ENH]** for enhancements
* **[FIX]** for bug fixes
* **[REF]** for refactoring existing code
* **[STY]** for stylistic changes
* **[TST]** for new or updated tests, and

You can also combine the tags above, for example if you are updating both a test and
the documentation: **[TST, DOC]**.

Pull requests should be submitted early and often!

If your pull request is not yet ready to be merged, please open your pull request as a draft.
More information about doing this is [available in GitHub's documentation][link_drafts].
This tells the development team that your pull request is a "work-in-progress",
and that you plan to continue working on it.

When your pull request is Ready for Review, you can select this option on the PR's page,
and a project maintainer will review your proposed changes.

(fcb-recognizing-contributions)=
## Recognizing contributors

We welcome and recognize all contributions from documentation to testing to code development.
You can see a list of current contributors in the [contributors tab][link_contributors].

## Thank you!

You're awesome. 👋 😃

<br>

*&mdash; Based on contributing guidelines from the [STEMMRoleModels][link_stemmrolemodels] project.*

[link_git]: https://git-scm.com
[link_github]: https://github.com/
[link_FAIR-cookbook]: https://github.com/fair-cookbook/the-fair-cookbook
[link_signupinstructions]: https://help.github.com/articles/signing-up-for-a-new-github-account

[writing_formatting_github]: https://help.github.com/articles/getting-started-with-writing-and-formatting-on-github
[markdown]: https://daringfireball.net/projects/markdown

[restructuredtext]: http://docutils.sourceforge.net/rst.html#user-documentation
[sphinx]: http://www.sphinx-doc.org/en/master/index.html
[readthedocs]: https://docs.readthedocs.io/en/latest/index.html

[link_issues]: https://github.com/FAIRplus/the-fair-cookbook/issues
[link_coc]: https://fairplus.github.io/the-fair-cookbook/content/recipes/boilerplate/code_of_conduct.html

[link_labels]: https://github.com/FAIRplus/the-fair-cookbook/labels


[link_pullrequest]: https://help.github.com/articles/creating-a-pull-request/
[link_fork]: https://help.github.com/articles/fork-a-repo/
[link_pushpullblog]: https://www.igvita.com/2011/12/19/dont-push-your-pull-requests/
[link_updateupstreamwiki]: https://help.github.com/articles/syncing-a-fork/
[link_branches]: https://help.github.com/articles/creating-and-deleting-branches-within-your-repository/

[link_drafts]: https://help.github.com/articles/about-pull-requests/#draft-pull-requests

[link_contributors]: https://github.com/FAIRplus/the-fair-cookbook/graphs/contributors
[link_stemmrolemodels]: https://github.com/KirstieJane/STEMMRoleModels
