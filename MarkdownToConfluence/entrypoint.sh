#!/bin/bash
/usr/bin/git init
/usr/bin/git config --global --add safe.directory /github/workspace
/usr/bin/git config --global core.pager "less -FRSX"
/usr/bin/git fetch
/usr/bin/git diff --name-only origin/${GITHUB_BASE_REF} './documentation'
#echo $(printenv)