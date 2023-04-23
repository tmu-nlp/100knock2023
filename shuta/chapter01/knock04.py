elements = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
elements = elements.split() # 空白ごとに語を区切る
dictionary ={}

# iが値、eがキーに対応している
for i, e in enumerate(elements): # enumerate()関数を利用することで、for文内のループ処理にインデックス番号を付与出来る
  if i + 1 in [1,5,6,7,8,9,15,16,19]:
    dictionary[e[:1]] = i + 1 #　辞書オブジェクト[キー] =　値　で辞書の要素を追加出来る / 1文字目まで表示
  else:
    dictionary[e[:2]] = i + 1 # 2文字目まで表示

print(dictionary)