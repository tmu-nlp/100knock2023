import knock41
import re

chunk_list = knock41.read_text_chunk()
code_regex = re.compile(r"[。、「」（）『』〈〉]")
for i in range(len(chunk_list)):
    L1 = [[list(map(knock41.surface_map ,o.morphs)), o.dst, o.srcs] for o in chunk_list[i]]
    D = dict()
    for j in range(len(L1)):
        D[j] = int(L1[j][1][0][:-1])
    for d in D:
        print(code_regex.sub("", "".join(L1[d][0]))+ "\t" + code_regex.sub("", "".join(L1[D[d]][0])))
    print("")