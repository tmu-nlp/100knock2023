sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"

rm_comma = sentence.replace(",","")

splited = rm_comma.split()

listing_length_of_words = [len(i) for i in splited]

print(listing_length_of_words)
