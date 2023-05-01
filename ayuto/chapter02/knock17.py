with open("popular-names.txt", "r") as f:
    popular_names_list = f.readlines()
popular_names_1st_line = []
for popular_name in popular_names_list:
    popular_names_1st_line.append(popular_name.split("\t")[0])
ans = set()
for popular_names_1st_line_str in popular_names_1st_line:
    ans.add(popular_names_1st_line_str)
print(ans)

# 確認
with open("uniq-sorted-cut-popular-names.txt", "r") as f:
    unix_ans_list = f.readlines()
unix_ans_list = map(lambda X: X[:-2], unix_ans_list)
unix_ans = set(unix_ans_list)
print(unix_ans_list == ans) # どっかバグってるけどどこがバグってるかわかりませんでした...orz
# print(ans - unix_ans)