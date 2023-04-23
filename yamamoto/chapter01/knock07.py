def makesentence(x, y, z):
    sentence = ""
    sentence = str(x) + "時の" + str(y) + "は" + str(z)
    return sentence

print(makesentence(12, "気温", 22.4))