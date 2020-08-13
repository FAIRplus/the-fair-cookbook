## ------------ first stage: --------------
## 

# Use a small linux with Python
FROM python:3.7.8-slim-buster AS jupyterbookbuilder-base-image

# Install dos2unix
RUN apt-get update && apt-get install -y dos2unix

# Copy installation requirements & expected versions
COPY ./docker/requirements.txt /requirements.txt

# Install 
RUN pip install -r /requirements.txt

# Document
RUN pip freeze > /pip_freeze_actual.txt

# Print
RUN cat /pip_freeze_actual.txt

# Copy expected pip freeze
COPY ./docker/pip_freeze.txt /pip_freeze_expected.txt

# Convert line endings
RUN dos2unix /pip_freeze_expected.txt

# Compare ; the whole container exits if files differ (because exit code -> 1)
RUN diff /pip_freeze_expected.txt /pip_freeze_actual.txt

## ------------ next stage: --------------
## load the content

FROM jupyterbookbuilder-base-image AS jupyterbookbuilder

# Set the working directory.
WORKDIR /app/

# Copy strictly necessary files 
COPY ./docs/_config.yml  ./
COPY ./docs/_data        ./_data
COPY ./docs/content      ./content

# Start the actual build
RUN jupyter-book build --overwrite /app
## ... all content was converted to html now and sits in /app/_build

## ------------ next stage: --------------
## prepare a customized jekyll 
## 

FROM jekyll/jekyll:3.8.5 AS jekyll-build-and-serve-base-image

## change the working directory to evade auto-mounting of pre-defined volume
WORKDIR /app/server/
RUN chown jekyll:jekyll /app/server
RUN pwd

## install bundler
RUN gem install bundler

## install the bundle from Gemfile, compare result with Gemfile.lock
COPY ./docs/Gemfile .
COPY ./docs/Gemfile.lock .
RUN pwd
RUN bundle install
RUN cat ./Gemfile.lock
##... container is prepared


## ------------ next stage: --------------
## load the content
##

FROM jekyll-build-and-serve-base-image as jekyll-build-and-serve

## copy additional files
COPY --chown=jekyll:jekyll ./docs       ./docs
RUN bash -c "pwd && ls"

## fetch the built html from the previous stage
COPY --from=jupyterbookbuilder /app/_build ./docs/_build
RUN bash -c "pwd && ls -alh"

## run the build process
RUN pwd && bundle exec jekyll build --source /app/server/docs

## serve the pre-built site
ENTRYPOINT pwd && bundle exec jekyll serve --source /app/server/docs --host 0.0.0.0 --skip-initial-build
