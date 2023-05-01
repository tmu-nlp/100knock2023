'''
00. 文字列の逆順Permalink
文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
'''

src = "stressed"

dst = ""

for i in range(len(src)):
    dst += src[-1-i]

print(dst)

# desserts
