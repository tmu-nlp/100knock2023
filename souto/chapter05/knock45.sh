#!/bin/zsh
cat ./ans45.txt | sort | uniq -c | sort -nr
cat ./ans45.txt | sort | uniq -c | sort -nr | grep '行う'
cat ./ans45.txt | sort | uniq -c | sort -nr | grep 'なる'
cat ./ans45.txt | sort | uniq -c | sort -nr | grep '与える'