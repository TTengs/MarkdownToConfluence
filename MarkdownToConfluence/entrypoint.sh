#!/bin/bash
git init
git config --global --add safe.directory /github/workspace
git config --global core.pager "less -FRSX"
git fetch -q
git pull
printenv
chmod -x ${GITHUB_EVENT_PATH}
before=$(jq .before ${GITHUB_EVENT_PATH} | tr -d '"')
after=$(jq .after ${GITHUB_EVENT_PATH} | tr -d '"')
git diff --name-status ${before}..${after} -- './documentation'
#echo ${GITHUB_EVENT_PATH} |  python3 -c "import sys, json; print(json.load(sys.stdin)['before'])"
#cat ${GITHUB_EVENT_PATH} |  python3 -c "import sys, json; print(json.load(sys.stdin)['after'])"