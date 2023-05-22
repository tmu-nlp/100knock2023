import knock41
import os

with open(f"{os.path.dirname(__file__)}/ai.ja.txt.parsed", "r") as parsed_file:
    chunked = knock41.getChunksList_paragraph(parsed_file.readlines())
    with open(f"{os.path.dirname(__file__)}/k45_out.txt", "w") as outfile:
        
        
        for parag in chunked:
            for chunk in parag:
                outstr=""
                for morph in chunk.morphs:
                    paired = False
                    if(morph.pos=="動詞"):
                        outstr=morph.base+'\t'
                        for srcid in chunk.srcs:
                            for mo in parag[srcid-1].morphs:
                                if(mo.pos=="助詞"):
                                    paired=True
                                    outstr+=mo.base+'\t'
                    outstr=outstr[:-1]
                    if(paired):
                        outfile.write(outstr+'\n')
                
                
# cat k45_out.txt | sort | uniq -c | sort -k 1n
# grep -P "^(行う|なる|与える)\t" k45_out.txt
