def cipher(x):
  code = ''
  for i in x:
    if i.islower():
      code += chr(219-ord(i))
    else:
      code += i
  return code

sentence = "I Love You"
sentence2 = cipher(sentence)
sentence3 = cipher(sentence2)

print(sentence2)
print(sentence3)