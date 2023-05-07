sed "s/\t/ /g" popular-names.txt > popular-names-sed.txt
tr -s '\t' ' ' < popular-names.txt > popular-names-tr.txt
expand -t 1 popular-names.txt > popular-names-expand.txt