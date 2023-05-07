import json

with open("chapter03/jawiki-country.json", 'r') as jsof:
    lines = jsof.readlines()
    pages = {}  # "title:text"
    for line in lines:
        dicted = json.loads(line)
        pages.setdefault(dicted["title"], dicted["text"])

    # print(pages["イギリス"])
    with open("chapter03/uk_text.txt", 'w') as out:
        out.write(pages["イギリス"])
