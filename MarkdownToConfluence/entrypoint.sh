#!/bin/bash
echo "$(git diff --name-only origin/${GITHUB_BASE_REF} './documentation')"
#echo $(printenv)