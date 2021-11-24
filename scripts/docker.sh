#!/bin/sh

## a total fresh run needs first (decide on your needs!): 
# rm -rf _build
## continue with this:
docker build --progress plain -t fcb . && docker run --name asdf fcb && docker cp asdf:/out.tar . && docker rm asdf && tar -xf out.tar && rm out.tar