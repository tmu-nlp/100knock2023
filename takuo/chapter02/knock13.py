col1 = open("chapter02/col1.txt")
col2 = open("chapter02/col2.txt")

col1s = [item.rstrip('\n') for item in col1.readlines()]
col2s = [item.rstrip('\n') for item in col2.readlines()]

marged = ""
for i in range(len(col1s)):  # len(col1s)==len(col2s)
    marged += "{}\t{}\n".format(col1s[i], col2s[i])
with open("chapter02/marged.txt", "w")as out:
    out.write(marged)

col1.close()
col2.close()
