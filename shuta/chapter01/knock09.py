import random #randomモジュール

def Typoglycemia(x):
  code = []
  for i in x.split():
    if len(i) > 4: 
      i = i[0] + ''.join(random.sample(i[1:-1], len(i)-2))+ i[-1] #単語の先頭と末尾はそのままで、間のみランダムランダム
      '''
      random.sample()関数は、第一引数に変換したいオブジェクト、第二引数に取得したい要素の個数を指定する。
      str.join()メソッドは、文字列のリスト間をstrで結合する。''の場合、文字無しで要素を結合出来る。
      '''
    code.append(i) #elseを省略可 / append()メソッドでリストに要素を追加出来る。
  
  return ' '.join(code) #単語間に半角空白を挿入し表示

sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
Typoglycemia(sentence)