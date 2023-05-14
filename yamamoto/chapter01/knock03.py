sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
sentence = sentence.replace(",", "")
sentence = sentence.replace(".", "")
word = sentence.split()
count_character = []
for i in word:
    print(i)
    count_character.append(len(i))

for i in count_character:
    print(i)