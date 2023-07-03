def calculate_accuracy(model, loader): # modelは評価するモデル, loaderはデータを提供するデータローダー
  model.eval() # モデルを評価モードに設定
  total = 0 # 全体のデータ数と正解数を初期化
  correct = 0
  with torch.no_grad(): # 勾配計算が行われないようにする
    for inputs, labels in loader:
      outputs = model(inputs) # 入力データに対するモデルの予測結果を取得
      pred = torch.argmax(outputs, dim=-1) # 予測結果の中で最大値を持つクラスを取得
      total += len(inputs)
      correct += (pred == labels).sum().item()
      
  return correct / total # 正解数を全体のデータ数で割ることで, 正解率を計算て返す

acc_train = calculate_accuracy(model, dataloader_train)
acc_test = calculate_accuracy(model, dataloader_test)
print("正解率（学習データ）：{}".format(round(acc_train, 3)))
print("正解率（評価データ）：{}".format(round(acc_test, 3)))

"""
acc_train = calculate_accuracy(model, dataloader_train)
acc_test = calculate_accuracy(model, dataloader_test)
print("正解率（学習データ）：{}".format(round(acc_train, 3)))
print("正解率（評価データ）：{}".format(round(acc_test, 3)))
正解率（学習データ）：0.926
正解率（評価データ）：0.903
"""