import collections
with open("popular-names.txt", "r") as f:
    popular_names_list = f.readlines()
popular_names_1st_line = []
for popular_name in popular_names_list:
    popular_names_1st_line.append(popular_name.split("\t")[0])
ans = list()
for popular_names_1st_line_str in popular_names_1st_line:
    ans.append(popular_names_1st_line_str)

hind = dict(collections.Counter(ans))
ans = list(set(ans))
sorted_by_hind = sorted(ans, key=lambda x: hind[x])
print(*sorted_by_hind, sep="\n")

# for i in sorted_by_hind:
#     print(i, hind[i])