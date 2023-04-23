def moji(x,y,z)：
SyntaxError: invalid character '：' (U+FF1A)
def moji(x,y,z):
    return 'a時のbはc'.format(a=x, b=y, c=z)

x=12
y='気温'
z=22.4
print(moji(x,y,z))
a時のbはc
