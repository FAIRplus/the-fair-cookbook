#!/bin/sh
BUILDKIT_PROGRESS=plain docker build -t fcb . && docker run --name asdf fcb && docker cp asdf:/out.tar.gz . && docker rm asdf && tar -xzf out.tar.gz && rm out.tar.gz 