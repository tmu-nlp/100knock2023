#!/bin/zsh
cut -f 1 popular-names.txt | sort | uniq -c | sort -k 1 -r
