#!/bin/bash
git init
git config --global --add safe.directory /github/workspace
git config --global core.pager "less -FRSX"
git fetch
git diff --name-only origin/${GITHUB_BASE_REF} './documentation'
#echo $(printenv)