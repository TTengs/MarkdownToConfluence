#!/bin/bash
for i in ${{ steps.getfile.outputs.files }}
          do
              echo $i
          done