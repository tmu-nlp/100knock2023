from torch import nn

class SLPNet(nn.Module): # SLPNetクラスはnn.Moduleを継承している
  def __init__(self, input_size, output_size): # ネットワークの初期化, input_sizeは入力の次元数, output_sizeは出力の次元数
    super().__init__()
    self.fc = nn.Linear(input_size, output_size, bias=False) # 全結合層を定義
    nn.init.normal_(self.fc.weight, 0.0, 1.0)  # 正規分布の乱数で重みを初期化

  def forward(self, x):
    x = self.fc(x) # 線形変換を行う
    return x
  
model = SLPNet(300, 4)  # SLPNetクラスのインスタンスを作成
y_hat_1 = torch.softmax(model(X_train[:1]), dim=-1) # modelに入力データX_train[:1]を与えて予測結果を計算する
print(y_hat_1)

Y_hat = torch.softmax(model.forward(X_train[:4]), dim=-1)
print(Y_hat)

"""
model = SLPNet(300, 4)  # SLPNetクラスのインスタンスを作成
"""

"""
tensor([[0.0309, 0.3568, 0.2114, 0.4009],
        [0.0283, 0.1080, 0.0739, 0.7898],
        [0.0652, 0.1887, 0.0227, 0.7234],
        [0.0032, 0.0993, 0.0539, 0.8436]], grad_fn=<SoftmaxBackward0>)
"""