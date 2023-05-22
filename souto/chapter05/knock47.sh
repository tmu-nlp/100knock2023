#!/bin/zsh
cat ./ans47.txt | sort | uniq -c | sort -nr
cat ./ans47.txt | sort | cut  -f 1 | uniq -c | sort -nr
