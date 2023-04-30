with open("popular-names.txt", "r") as f:
    popular_names = f.read().replace("\t", " ")

# 確認
with open("popular-names-knock11.txt") as f:
    popular_names_knock11 = f.read()
print(popular_names == popular_names_knock11)
