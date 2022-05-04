#!/bin/bash
git init
git config --global --add safe.directory /github/workspace
git config --global core.pager "less -FRSX"
git fetch -q
printenv
chmod -x ${GITHUB_EVENT_PATH}
before=$(jq .before ${GITHUB_EVENT_PATH} | tr -d '"')
after=${GITHUB_SHA} | tr -d '"'
git fetch origin ${before} --depth=1
#git pull
git diff --name-status ${before}..${after} -- './documentation'
#echo ${GITHUB_EVENT_PATH} |  python3 -c "import sys, json; print(json.load(sys.stdin)['before'])"
#cat ${GITHUB_EVENT_PATH} |  python3 -c "import sys, json; print(json.load(sys.stdin)['after'])"