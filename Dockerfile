## ------------ first stage: --------------
## 

# Use a small linux with Python
FROM python:3.7.8-slim-buster AS jupyterbookbuilder-base-image

RUN pip install                                  \
            alabaster==0.7.12                    \
            anyio==2.2.0                         \
            argon2-cffi==20.1.0                  \
            async-generator==1.10                \
            attrs==20.3.0                        \
            Babel==2.9.0                         \
            backcall==0.2.0                      \
            beautifulsoup4==4.9.3                \
            bleach==3.3.0                        \
            certifi==2020.12.5                   \
            cffi==1.14.5                         \
            chardet==4.0.0                       \
            click==7.1.2                         \
            colorama==0.4.4                      \
            decorator==5.0.7                     \
            defusedxml==0.7.1                    \
            deprecation==2.1.0                   \
            docutils==0.16                       \
            entrypoints==0.3                     \
            gitdb==4.0.7                         \
            GitPython==3.1.14                    \
            idna==2.10                           \
            imagesize==1.2.0                     \
            importlib-metadata==4.0.1            \
            ipykernel==5.5.3                     \
            ipython==7.31.1                      \
            ipython-genutils==0.2.0              \
            ipywidgets==7.6.3                    \
            jedi==0.18.0                         \
            Jinja2==2.11.3                       \
            jsonschema==3.2.0                    \
            jupyter-book==0.10.2                 \
            jupyter-cache==0.4.2                 \
            jupyter-client==6.1.12               \
            jupyter-core==4.7.1                  \
            jupyter-packaging==0.9.2             \
            jupyter-server==1.6.4                \
            jupyter-server-mathjax==0.2.2        \
            jupyter-sphinx==0.3.1                \
            jupyterbook-latex==0.2.0             \
            jupyterlab-widgets==1.0.0            \
            jupytext==1.10.3                     \
            latexcodec==2.0.1                    \
            linkify-it-py==1.0.1                 \
            markdown-it-py==0.6.2                \
            MarkupSafe==1.1.1                    \
            mdit-py-plugins==0.2.6               \
            mistune==0.8.4                       \
            myst-nb==0.12.0                      \
            myst-parser==0.13.6                  \
            nbclient==0.5.3                      \
            nbconvert==5.6.1                     \
            nbdime==3.1.1                        \
            nbformat==5.1.3                      \
            nest-asyncio==1.5.1                  \
            nested-lookup==0.2.22                \
            notebook>=6.4.1                      \
            packaging==20.9                      \
            pandocfilters==1.4.3                 \
            parso==0.8.2                         \
            pexpect==4.8.0                       \
            pickleshare==0.7.5                   \
            prometheus-client==0.10.1            \
            prompt-toolkit==3.0.18               \
            ptyprocess==0.7.0                    \
            pybtex==0.24.0                       \
            pybtex-docutils==1.0.0               \
            pycparser==2.20                      \
            pydata-sphinx-theme==0.4.3           \
            Pygments==2.8.1                      \
            pyparsing==2.4.7                     \
            pyrsistent==0.17.3                   \
            python-dateutil==2.8.1               \
            pytz==2021.1                         \
            PyYAML==5.4.1                        \
            pyzmq==22.0.3                        \
            requests==2.25.1                     \
            Send2Trash==1.5.0                    \
            six==1.15.0                          \
            smmap==4.0.0                         \
            sniffio==1.2.0                       \
            snowballstemmer==2.1.0               \
            soupsieve==2.2.1                     \
            Sphinx==3.5.4                        \
            sphinx-book-theme==0.0.42            \
            sphinx-comments==0.0.3               \
            sphinx-copybutton==0.3.1             \
            sphinx-panels==0.5.2                 \
            sphinx-thebe==0.0.8                  \
            sphinx-togglebutton==0.2.3           \
            sphinxcontrib-applehelp==1.0.2       \
            sphinxcontrib-bibtex==2.1.0          \
            sphinxcontrib-devhelp==1.0.2         \
            sphinxcontrib-htmlhelp==1.0.3        \
            sphinxcontrib-jsmath==1.0.1          \
            sphinxcontrib-qthelp==1.0.3          \
            sphinxcontrib-serializinghtml==1.1.4 \
            sphinx-sitemap==2.2.0                \
            SQLAlchemy==1.3.24                   \
            terminado==0.9.4                     \
            testpath==0.4.4                      \
            toml==0.10.2                         \
            tomlkit==0.7.0                       \
            tornado==6.1                         \
            traitlets==5.0.5                     \
            uc-micro-py==1.0.1                   \
            urllib3==1.26.4                      \
            wcwidth==0.2.5                       \
            webencodings==0.5.1                  \
            widgetsnbextension==3.5.1            \
            zipp==3.4.1                          \
            pygments-csv-lexer==0.1.3             

# Document
RUN pip freeze > /pip_freeze_actual.txt

# Print
RUN cat /pip_freeze_actual.txt

## ------------ next stage: --------------
## build the images from mermaid files

FROM alpine as orchestrator

COPY ./ ./

RUN find . -iname "*.mmd" > list_of_all_mermaid_files.txt
RUN tar c -f all_mermaid_files.tar -T list_of_all_mermaid_files.txt
RUN ls -lh all_mermaid_files.tar

## ------------ next stage: --------------
## build the images from mermaid files

FROM minlag/mermaid-cli:8.13.4 as imageconverter
WORKDIR /home/mermaidcli

RUN echo "{\"args\": [ \"--no-sandbox\" ] }" > puppeteer-config.json

COPY --from=orchestrator all_mermaid_files.tar list_of_all_mermaid_files.txt .
RUN tar -xf all_mermaid_files.tar
RUN cat list_of_all_mermaid_files.txt | while read line; do echo $line && ./node_modules/.bin/mmdc -p puppeteer-config.json -i $line -w 800 -o $line.png ; done
RUN cat list_of_all_mermaid_files.txt | while read line; do echo $line && ./node_modules/.bin/mmdc -p puppeteer-config.json -i $line -w 1600 -o $line.hi-res.png ; done
RUN cat list_of_all_mermaid_files.txt | while read line; do echo $line && ./node_modules/.bin/mmdc -p puppeteer-config.json -i $line -w 400 -o $line.lo-res.png  ; done
RUN cat list_of_all_mermaid_files.txt | while read line; do echo $line && ./node_modules/.bin/mmdc -p puppeteer-config.json -i $line -o $line.svg                ; done

RUN cp list_of_all_mermaid_files.txt list_of_files_to_copy.txt
RUN sed 's/$/.png/' list_of_all_mermaid_files.txt >> list_of_files_to_copy.txt
RUN sed 's/$/.hi-res.png/' list_of_all_mermaid_files.txt >> list_of_files_to_copy.txt
RUN sed 's/$/.lo-res.png/' list_of_all_mermaid_files.txt >> list_of_files_to_copy.txt
RUN sed 's/$/.svg/' list_of_all_mermaid_files.txt >> list_of_files_to_copy.txt
RUN tar -cf ./all_raw_and_converted_mermaid_images.tar -T list_of_files_to_copy.txt


## ------------ next stage: --------------
## load the content

FROM jupyterbookbuilder-base-image AS jupyterbookbuilder

# Set the working directory. You can customize this path to be equivalent to your computer's
# directory structure, e.g. if you use an Integrated Development Environment (IDE) which allows you 
# to click on file names from a terminal...   
WORKDIR /Users/robert/git/the-fair-cookbook

# Create an empty folder to prevent failure later on
RUN mkdir -p ./_build/html

# Copy files 
COPY ./   ./
COPY --from=imageconverter /home/mermaidcli/all_raw_and_converted_mermaid_images.tar .
RUN tar -xf all_raw_and_converted_mermaid_images.tar

# Start the actual build
RUN python -u -c "import jupyter_book.commands; jupyter_book.commands.main()" build ./ 2>&1 | tee ./_build/build.log

# Let the build fail if there are errors in the build of the jupyter_book 
RUN grep "There was an error in building your book. Look above for the cause." ./_build/build.log; test $? -eq 1

# Clean the build log from all escape characters used for highlighting text (e.g. bold, red) and the 
# "interactive" feel (i.e. going back to start of line and overwrite to create a up-counting progress bar)
RUN sed "s,\x1B\[[0-9;]*[a-zA-Z],,g" ./_build/build.log > ./_build/cleaned_build.log

# pack the whole build folder into a gzipped tar file
RUN tar -cf /out.tar ./_build

# output what's in the _build folder, just for the sake of it.
RUN ls -alh ./_build

## ... all content was converted to html now and sits in WORKDIR/_build
## ... a build log can be found in WORKDIR/_build/build.log
