S = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
S = S.replace(",", "").replace(".", "")
S = list(S.split())
print([len(s) for s in S])