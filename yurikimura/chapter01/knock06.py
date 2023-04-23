# 06. 集合Permalink
# “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．

def letter_ngram(src: str, n: int):
    dst = [src[i:i+n] for i in range(len(src)-n+1)]
    return(dst)


src1 = 'paraparaparadise'
src2 = 'paragraph'

X = letter_ngram(src1, 2)
Y = letter_ngram(src2, 2)

setX, setY = set(X), set(Y)
print('setX:', setX)
print('setY : ', setY)

# 和集合
union = setX | setY
print('union : ', union)

# 積集合
intersec = setX & setY
print('intersection : ', intersec)

# 差集合
diff = setX - setY
print('difference : ', diff)

# 内在判定
if 'se' in X:
    print('se in X')
if 'se' in Y:
    print('se in Y')


# setX: {'pa', 'ar', 'ap', 'ra', 'ad', 'di', 'se', 'is'}
# setY :  {'pa', 'ar', 'gr', 'ph', 'ag', 'ra', 'ap'}
# union :  {'pa', 'ar', 'gr', 'ph', 'ag', 'ap', 'ra', 'ad', 'di', 'se', 'is'}
# intersection :  {'ar', 'ap', 'pa', 'ra'}
# difference :  {'di', 'ad', 'se', 'is'}
# se in X
