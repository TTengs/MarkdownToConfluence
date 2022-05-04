#!/bin/bash
git init
git config --global --add safe.directory /github/workspace
git config --global core.pager "less -FRSX"
git fetch -q
#git diff --name-status origin/${GITHUB_BASE_REF} './documentation'
printenv
chmod -x ${GITHUB_EVENT_PATH}
echo ${GITHUB_EVENT_PATH} |  python3 -c "import sys, json; print(json.load(sys.stdin)['before'])"
echo ${GITHUB_EVENT_PATH} |  python3 -c "import sys, json; print(json.load(sys.stdin)['after'])"