from Structs import Morph
import re
import os

with open(f"{os.path.dirname(__file__)}/ai.ja.txt.parsed", "r") as parsed_file:
    lines = parsed_file.readlines()
    morphed_txt = []
    buff = []
    for line in lines:
        line = line.rstrip('\n')
        if (re.match(r"\* .*", line) != None):
            continue
        if (line == "EOS"):
            if (buff != []):
                morphed_txt.append(buff)
            buff = []
        else:
            m = Morph()
            m.build(line)
            buff.append(m)

    for item in morphed_txt[1]:
        print(item)
