# How to enable flow diagrams in Github from gh-pages:

- github pages are served by jekyll and more information can be found in the following document [github pages & jekyll](https://jekyllrb.com/docs/github-pages/)

- flow and sequence diagrams are popular mean to provide a graphical overview of processes. Since FAIRification recipes are processes at the core, it is a strong requirement to enhance the recipes with such graphical overview

- [mermaid](https://github.com/mermaid-js/mermaid) is a javascript library allowing to generate diagrams, charts, graphs or flows from markdown-like text via javascript. 

	- mermaid documentation is extensive, [see here](https://mermaid-js.github.io/mermaid/#/)
	- mermaid is compatible with jekyll via a [gem plugin](https://github.com/jasonbellamy/jekyll-mermaid/blob/master/readme.md)

- The following steps need to be performed to enable a github repository to serve mermaid defined diagrams.

	1. install the `jekyll mermaid plugin`: 

    	To do so, open a terminal, and run the following command in the suitable virtual environment
    
    	```bash
    	> gem install jekyll-mermaid
    	```

	2. edit the the Jekyll `_config.yml` file:

		- declare the plugin to the Jekyll `_config.yml` file by adding the following line:

        	```ruby
        	gems: [jekyll-mermaid]
        	```
		
	       see the [Jekyll documentation](http://jekyllrb.com/docs/plugins/#installing-a-plugin) for more installation options.

		- add the path the mermaid javascript library. Note this should be the distribution .js file, not the source files.
		- The distribution file for the mermaid javascript library can be obtained from:

    		```ruby
    	    mermaid.js
    		mermaid.core.js
    		mermaid.min.js
    		```

		By default, the path the js library is set in the `_config.file` to `js_url: /assets/js`.
		Therefore, to indicate the path to the `mermaid.js` library, simply add the following:

        ```ruby
        mermaid:
           src: '/js/mermaid.js'
           src_config: '/js/config.js'
        ```

	   - in order to have mermaid to work with jekyll on github, you need to obtain the library from the following site.
	   [mermaid library distribution](https://unpkg.com/mermaid@7.1.0/dist/)
	   
        ```bash
    	curl -O https://unpkg.com/mermaid@7.1.0/dist/mermaid.js
        curl -O https://unpkg.com/mermaid@7.1.0/dist/mermaid.core.js
        curl -O https://unpkg.com/mermaid@7.1.0/dist/mermaid.min.js
        ```


    3. edit the `head.html` template under `_include` folder
    
    Since Jekyll build every page served by include the head.html template, it will also load by default the mermaid library,
        which is then able to process the relevant section defining the diagrams:
    	```
       	<!-- using mermaid for rendering Diagram and flow chart -->
        	<script src="{{ site.js_url | relative_url }}/mermaid.min.js"></script>
        	<script>mermaid.initialize({startOnLoad:true});</script>
            ```
	
    4. testing:

        - Does this state diagram work?
<div class="mermaid">
stateDiagram
    [*] --> Still
    Still --> [*]
    Still --> Moving
    Moving --> Still
    Moving --> Crash
    Crash --> [*]
</div>        
        - Does this Gantt chart display?  
<div class="mermaid">
gantt
    title A Gantt Diagram
    dateFormat  YYYY-MM-DD
    section Section
    A task           :a1, 2014-01-01, 30d
    Another task     :after a1  , 20d
    section Another
    Task in sec      :2014-01-12  , 12d
    another task      : 24d
</div>
        - Does this flowchart display?
<div class="mermaid">
graph LR;
    A["input data"]-->B["conversion to open format"];
    A["input data"]-->C["automatic annotation"];
    B["conversion to open format"]-->D(("output data"));
    C["automatic annotation"]-->D(("output data"));  
    style A fill:#FF5733,stroke:#333,stroke-width:2px
    style D fill:#0A749B,stroke:#333,stroke-width:2px
</div>


if you cannot view the Gantt chart or the State Diagram, it means you  are running an outdated version of the mermaid distribution.
try upgrading by download the files from [here](https://unpkg.com/browse/mermaid@8.4.8/dist/)
