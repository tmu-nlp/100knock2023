from torch.utils.data import DataLoader
import time
from torch import optim
import numpy as np
from matplotlib import pyplot as plt

def calculate_loss_and_accuracy(model, dataset, device=None, criterion=None):
  """損失・正解率を計算"""
  dataloader = DataLoader(dataset, batch_size=1, shuffle=False)
  loss = 0.0
  total = 0
  correct = 0
  with torch.no_grad():
    for data in dataloader:
      inputs = data["inputs"].to(device)
      labels = data["labels"].to(device)

      outputs = model(inputs)

      if criterion != None:
        loss += criterion(outputs, labels).item()

      pred = torch.argmax(outputs, dim=-1)
      total += len(inputs)
      correct += (pred == labels).sum().item()
      
  return loss / len(dataset), correct / total
  

def train_model(dataset_train, dataset_valid, batch_size, model, criterion, optimizer, num_epochs, collate_fn=None, device=None):
  """モデルの学習を実行し、損失・正解率のログを返す"""
  model.to(device)

  dataloader_train = DataLoader(dataset_train, batch_size=batch_size, shuffle=True, collate_fn=collate_fn)
  dataloader_valid = DataLoader(dataset_valid, batch_size=1, shuffle=False)

  scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, num_epochs, eta_min=1e-5, last_epoch=-1)

  # 学習
  log_train = []
  log_valid = []
  for epoch in range(num_epochs):

    s_time = time.time()

    model.train()
    for data in dataloader_train:
      optimizer.zero_grad()
      inputs = data["inputs"].to(device)
      labels = data["labels"].to(device)
      outputs = model(inputs)
      loss = criterion(outputs, labels)
      loss.backward()
      optimizer.step()
    
    model.eval()

    # 損失と正解率の算出
    loss_train, acc_train = calculate_loss_and_accuracy(model, dataset_train, device, criterion=criterion)
    loss_valid, acc_valid = calculate_loss_and_accuracy(model, dataset_valid, device, criterion=criterion)
    log_train.append([loss_train, acc_train])
    log_valid.append([loss_valid, acc_valid])

    # チェックポイントの保存
    torch.save({"epoch": epoch, "model_state_dict": model.state_dict(), "optimizer_state_dict": optimizer.state_dict()}, f"checkpoint{epoch + 1}.pt")

    e_time = time.time()

    # ログを出力
    print(f"epoch: {epoch + 1}, loss_train: {loss_train:.4f}, accuracy_train: {acc_train:.4f}, loss_valid: {loss_valid:.4f}, accuracy_valid: {acc_valid:.4f}, {(e_time - s_time):.4f}sec") 

    # 検証データの損失が3エポック連続で低下しなかった場合は学習終了
    if epoch > 2 and log_valid[epoch - 3][0] <= log_valid[epoch - 2][0] <= log_valid[epoch - 1][0] <= log_valid[epoch][0]:
      break
      
    scheduler.step()

  return {"train": log_train, "valid": log_valid}

def visualize_logs(log):
  fig, ax = plt.subplots(1, 2, figsize=(15, 5))
  ax[0].plot(np.array(log["train"]).T[0], label="train")
  ax[0].plot(np.array(log["valid"]).T[0], label="valid")
  ax[0].set_xlabel("epoch")
  ax[0].set_ylabel("loss")
  ax[0].legend()
  ax[1].plot(np.array(log["train"]).T[1], label="train")
  ax[1].plot(np.array(log["valid"]).T[1], label="valid")
  ax[1].set_xlabel("epoch")
  ax[1].set_ylabel("accuracy")
  ax[1].legend()
  plt.show()

# パラメータの設定
VOCAB_SIZE = len(set(word2id.values())) + 1 
EMB_SIZE = 300
PADDING_IDX = len(set(word2id.values()))
OUTPUT_SIZE = 4
HIDDEN_SIZE = 50
LEARNING_RATE = 1e-3
BATCH_SIZE = 1
NUM_EPOCHS = 10

model = RNN(VOCAB_SIZE, EMB_SIZE, PADDING_IDX, OUTPUT_SIZE, HIDDEN_SIZE)

criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.SGD(model.parameters(), lr=LEARNING_RATE)

log = train_model(dataset_train, dataset_valid, BATCH_SIZE, model, criterion, optimizer, NUM_EPOCHS)

# ログの可視化
visualize_logs(log)

# 正解率の算出
bar, acc_train = calculate_loss_and_accuracy(model, dataset_train)
bar, acc_test = calculate_loss_and_accuracy(model, dataset_test)
print(f"正解率（学習データ）：{acc_train:.3f}")
print(f"正解率（評価データ）：{acc_test:.3f}")