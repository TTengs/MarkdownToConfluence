#!/bin/sh

find ./documentation -type d -not -path "./documentation" -print0 | xargs -0 -I file bash ./src/convert.sh file

#Skulle bare lige teste outputs, men her kan vi eventuelt smidde status koder ind f.eks
status=done
echo "::set-output name=status::$status"
#Det her er action syntax til at sende outputs