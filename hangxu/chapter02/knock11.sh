#!/bin/bash

#sed s:置換　g:全部
sed 's/\t//g' popular-names.txt

#tr 
cat popular-names.txt | tr \t ' '

#Expand
expand popular-names.txt