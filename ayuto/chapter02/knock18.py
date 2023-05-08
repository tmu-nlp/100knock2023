with open("popular-names.txt", "r") as f:
    popular_names_list = f.readlines()
popular_names_list = list(map(lambda x: x.split("\t"), popular_names_list))

popular_names_list=sorted(popular_names_list, key = lambda x: x[2], reverse=True)
with open("knock18-python.txt", "w") as f:
    for popular_name in popular_names_list:
        f.write("\t".join(popular_name))