from torch.utils.data import Dataset

class NewsDataset(Dataset): # torch.utils.data.Datasetクラスを継承
  def __init__(self, X, y):  # datasetの構成要素を指定
    self.X = X
    self.y = y

  def __len__(self):  # ラベルデータの長さを返す
    return len(self.y)

  def __getitem__(self, idx):  #　datasetのインデックスidxに対応するデータを返す
    return [self.X[idx], self.y[idx]]
  
from torch.utils.data import DataLoader

#Datasetの作成
dataset_train = NewsDataset(X_train, y_train)
dataset_valid = NewsDataset(X_valid, y_valid)
dataset_test = NewsDataset(X_test, y_test)

#Dataloaderの作成（datasetをバッチごとにイテレーションできる）
dataloader_train = DataLoader(dataset_train, batch_size=1, shuffle=True) # バッチサイズは1でデータがエポックごとにシャッフルされる
dataloader_valid = DataLoader(dataset_valid, batch_size=len(dataset_valid), shuffle=False)
dataloader_test = DataLoader(dataset_test, batch_size=len(dataset_test), shuffle=False)

model = SLPNet(300, 4) # モデルの定義, 入力サイズが300, 出力サイズが4

criterion = nn.CrossEntropyLoss() # クロスエントロピー損失関数を定義

optimizer = torch.optim.SGD(model.parameters(), lr=0.1) # 確率的勾配降下法（SGD）を使用してモデルのパラメータを最適化するためのオプティマイザを定義

# 学習
num_epochs = 20 # 20エポックで終了
for epoch in range(num_epochs):
  model.train() # 訓練モードに設定
  loss_train = 0.0 # 訓練データの累積損失を初期化

  # 訓練データセットをバッチごとにイテレーション
  for i, (inputs, labels) in enumerate(dataloader_train):
    optimizer.zero_grad() # 勾配をゼロで初期化
    outputs = model(inputs) # 入力データをモデルに与えて予測結果を得る
    loss = criterion(outputs, labels) # 予測結果と正解ラベルを用いて損失を計算
    loss.backward() # 損失を用いて誤差逆伝播を行い、勾配を計算
    optimizer.step() # 計算された勾配を使用してモデルのパラメータを更新
    loss_train += loss.item() # バッチごとの損失を累積

  loss_train = loss_train / i # バッチ単位の平均損失を計算

  model.eval()  #モデルを評価モードに切り替え

  with torch.no_grad(): # 評価中に勾配計算が行われないようにする
    inputs, labels = next(iter(dataloader_valid)) # 検証データセットの最初のバッチを取得
    outputs = model(inputs) # 検証データに対するモデルの予測結果を得る
    loss_valid = criterion(outputs, labels) # 予測結果と正解ラベルを用いて検証データの損失を計算

  # ログを出力
  print("epoch: {}, loss_train: {}, loss_valid: {}".format(epoch + 1, loss_train, loss_valid))  



  loss_train = loss_train / i # バッチ単位の平均損失を計算

  model.eval()  #モデルを評価モードに切り替え

  with torch.no_grad(): # 評価中に勾配計算が行われないようにする
    inputs, labels = next(iter(dataloader_valid)) # 検証データセットの最初のバッチを取得
    outputs = model(inputs) # 検証データに対するモデルの予測結果を得る
    loss_valid = criterion(outputs, labels) # 予測結果と正解ラベルを用いて検証データの損失を計算

"""
epoch: 1, loss_train: 0.4845655953308674, loss_valid: 0.33650335669517517
epoch: 2, loss_train: 0.3191676711362813, loss_valid: 0.30125585198402405
epoch: 3, loss_train: 0.288399726330275, loss_valid: 0.29060083627700806
epoch: 4, loss_train: 0.2719642098555502, loss_valid: 0.27853715419769287
epoch: 5, loss_train: 0.26097624336385955, loss_valid: 0.279220849275589
epoch: 6, loss_train: 0.2539790986876866, loss_valid: 0.27914634346961975
epoch: 7, loss_train: 0.24758436675324139, loss_valid: 0.2757430672645569
epoch: 8, loss_train: 0.24291566821817068, loss_valid: 0.2724910080432892
epoch: 9, loss_train: 0.23938845990347396, loss_valid: 0.27468445897102356
epoch: 10, loss_train: 0.23583272897827137, loss_valid: 0.29380103945732117
epoch: 11, loss_train: 0.23399379912843232, loss_valid: 0.2734271287918091
epoch: 12, loss_train: 0.23195550796670691, loss_valid: 0.2834618091583252
epoch: 13, loss_train: 0.22978527944132782, loss_valid: 0.27542680501937866
epoch: 14, loss_train: 0.22811020829712383, loss_valid: 0.27869537472724915
epoch: 15, loss_train: 0.2262318554891655, loss_valid: 0.28086286783218384
epoch: 16, loss_train: 0.22532035282106158, loss_valid: 0.27694863080978394
epoch: 17, loss_train: 0.22471221787308562, loss_valid: 0.27877405285835266
epoch: 18, loss_train: 0.22378620380049596, loss_valid: 0.279419869184494
epoch: 19, loss_train: 0.22216435255128383, loss_valid: 0.27973657846450806
epoch: 20, loss_train: 0.22166590356902793, loss_valid: 0.27944284677505493
"""