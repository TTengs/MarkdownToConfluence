#!/bin/bash
git init
git config --global --add safe.directory /github/workspace
git config --global core.pager "less -FRSX"
git fetch -q
#git diff --name-status origin/${GITHUB_BASE_REF} './documentation'
printenv
cat ${GITHUB_EVENT_PATH}