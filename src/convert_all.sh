#!/bin/sh

find ./docs -type d -not -path "./docs" -print0 | xargs -0 -I file bash ./scripts/convert.sh file

#Skulle bare lige teste outputs, men her kan vi eventuelt smidde status koder ind f.eks
status=done
echo "::set-output name=status::$status"
#Det her er action syntax til at sende outputs