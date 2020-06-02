# Recipe 1: How to assess FAIRness

**identifier:**

**version:** [v0.1](v0.1)

___

**_Difficulty level:_** :triangular_flag_on_post: :triangular_flag_on_post: :white_circle:  :white_circle: :white_circle:

**_Reading time:_** 15 minutes 

**_Intended Audience:_** 

> :heavy_check_mark: Data Managers

> :heavy_check_mark: Data Scientists

**_Recipe Type_**: Practical

**_Executable code_**: Yes

___


## Ingredients:
	
| Ingredient | Type| Comment|
|:-----| :----|:-----|
|[HTTP1.1 protocol](https://tools.ietf.org/html/rfc2616)| data communication protocol | |
|[guidance on persistent resolvable identifiers](https://www.gov.uk/government/publications/open-standards-for-government/persistent-resolvable-identifiers)| policy| |
|[Persistent Uniform Resource Locators - PURL](https://archive.org/services/purl/)|redirection service| |
|[Archival Resource Key](https://n2t.net/e/ark_ids.html)| identifier minting service; identifier resolution service| |
|[Handle system](http://www.rfc-editor.org/rfc/rfc3650.txt)|identifier minting service; identifier resolution service| |
|[DOI](https://doi.org/)| identifier minting service| based on Handle system |
|[identifiers.org](https://identifiers.org/)|identifier resolution service||
|[EZID resolution service](https://ezid.cdlib.org/)|identifier resolution service||
|[name2things rsolution service](http://n2t.net/)|identifier resolution service||
|[FAIREvaluator](https://W3id.org/AmIFAIR)|FAIR assessment||
|[FAIRShake](https://fairshake.cloud/)| FAIR assessment||
|[RDF/Linked Data](https://www.w3.org/standards/semanticweb/data)| model | |



| Actions.Objectives.Tasks  | Input | Output  |
| :------------- | :------------- | :------------- |
| []()  | []() | []() |
| []()  | []() | []() |
| []()  | []() | []() |
| []()  | []() | []() |
| []()  | []() | []() |
| []()  | []() | []() |

        

## Objectives:

Perform an automatic assessment of the status of a dataset with respect to the FAIR principles.
Obtain human and machine readable reports highlighting the main 

## Step by Step Process:

### Step1: 
     
Navigate the FAIREvaluator tool, which can be accessed via the following 2 addresses:

- [https://w3id.org/AmIFAIR](https://w3id.org/AmIFAIR)

- [https://fairsharing.github.io/FAIR-Evaluator-FrontEnd](https://fairsharing.github.io/FAIR-Evaluator-FrontEnd/#!/#%2F!)


![the FAIREvaluator Home page](../assets/fair-eval-img1.png)

### Step2:

In order the run the FAIREvaluator, it is important to understand to notion of FAIR indicators (formerly referred to as FAIR metrics).
One may browse the list of currently community defined indicators from the `Collections` page 

![Select a 'FAIR Maturity Indicator - Collections'](../assets/fair-eval-img2.png)     

### Step3:

To run an evaluation, the FAIREvaluator needs to following 5 inputs from users:

1. a collection of FAIR indicators, selected from the list described above.
2. a globally unique, persistent, resolveable identifier for the resource to be evaluated.
3. a title for the evaluation. Enforce a naming convention to make future searches easiers as these evaluations are saved.
4. a person identifier in the form of an ORCID

![Running the FAIREvaluator - part 1: setting the input](../assets/fair-eval-img4.png)

### Step4:

Hit the 'Run Evaluation' button from 'https://fairsharing.github.io/FAIR-Evaluator-FrontEnd/#!/collections/new/evaluate' page



![Running the FAIREvaluator - part 2: execution ](../assets/fair-eval-img5.png)
     
### Step5:

Analyze the report:

![FAIREvaluator report - overall report ](../assets/fair-eval-img6.png)

Time to dig into the details and figure out the reasons why some indicators are reporting a failure:

![apparently a problem with identifier persistence if using DOI, which are URN rather than URL *stricto-sensu*](../assets/fair-eval-img7.png)



## Reference:

Wilkinson, M.D., Dumontier, M., Sansone, S. et al. Evaluating FAIR maturity through a scalable, automated, community-governed framework. Sci Data 6, 174 (2019). [doi:10.1038/s41597-019-0184-5](https://doi.org/10.1038/s41597-019-0184-5)

Clarke et al. FAIRshake: Toolkit to Evaluate the FAIRness of Research Digital Resources, Cell Systems (2019),[doi:10.1016/j.cels.2019.09.011](https://doi.org/10.1016/j.cels.2019.09.011)



## Authors:

| Name | Affiliation  | orcid | CrediT role  |
| :------------- | :------------- | :------------- |:------------- |
| Philippe Rocca-Serra |  University of Oxford, Data Readiness Group| [0000-0001-9853-5668](https://orcid.org/orcid.org/0000-0001-9853-5668) | Writing - Original Draft | 

___


## License:

<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a>