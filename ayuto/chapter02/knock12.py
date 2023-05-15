with open("popular-names.txt", "r") as f:
    popular_names_list = f.readlines()
with open("col1.txt", "w") as f:
    for popular_name in popular_names_list:
        f.write(popular_name.split("\t")[0])
        f.write("\n")
with open("col2.txt", "w") as f:
    for popular_name in popular_names_list:
        f.write(popular_name.split("\t")[1])
        f.write("\n")
# cut -f 1 popular-names.txt > col1-unix.txt
# cut -f 2 popular-names.txt > col2-unix.txt
# 確認

with open("col1.txt", "r") as f:
    col1 = f.read()
with open("col2.txt", "r") as f:
    col2 = f.read()
with open("col1-unix.txt", "r") as f:
    col1_unix = f.read()
with open("col2-unix.txt", "r") as f:
    col2_unix = f.read()
print(col1 == col1_unix and col2 == col2_unix)
print((col1 == col1_unix) & (col2 == col2_unix)) # ちなみに and と & は優先順位が違ったりします
