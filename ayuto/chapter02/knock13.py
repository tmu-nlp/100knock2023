with open("col1.txt", "r") as f:
    col1_list = f.readlines()
with open("col2.txt", "r") as f:
    col2_list = f.readlines()
with open("col1-2.txt", "w") as f:
    for i in range(len(col2_list)):
        f.write(col1_list[i].replace("\n", "")) # 末尾の改行文字コードを削除
        f.write("\t")
        f.write(col2_list[i])
# paste col1.txt col2.txt > col1-2-unix.txt
# 確認
with open("col1-2.txt", "r") as f:
    col1_2 = f.read()
with open("col1-2-unix.txt", "r") as f:
    col1_2_unix = f.read()
print(col1_2 == col1_2_unix)