def cipher(sentence):
    return_sentence = ""
    for char in sentence:
        if char.islower():
            return_sentence += chr(219 - ord(char))
        else:
            return_sentence += char
    return return_sentence

sentence = "I am Yamamoto"
sentence = cipher(sentence)
print(sentence)
sentence = cipher(sentence)
print(sentence)