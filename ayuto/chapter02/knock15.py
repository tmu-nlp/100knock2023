N=int(input())
with open("popular-names.txt", "r") as f:
    popular_names_list = f.readlines()
for popular_names in popular_names_list[-N:]:
    print(popular_names, end="")