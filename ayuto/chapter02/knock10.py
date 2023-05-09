with open("popular-names.txt", "r") as f:
    popular_names_list = f.readlines()
    print(len(popular_names_list))

# wc -l popular-names.txt
# 2780 popular-names.txt