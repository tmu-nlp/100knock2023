sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = sentence.replace(',','').replace('.','') #カンマやピリオドを削除
words = words.split() #空白ごとに語を区切る
pi = [len(i) for i in words] #文字数を取得
print(pi)