src = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

src_alpha = src.replace(",", "").replace(".", "")
words = {}
for i in src_alpha.split(" "):
    words[i] = len(i)

dst = [v for k, v in words.items()]

print(dst)
