model = SLPNet(300, 4)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

num_epochs = 20
log_train = []
log_valid = []
for epoch in range(num_epochs):
  model.train()
  for inputs, labels in dataloader_train:
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs, labels)
    loss.backward()
    optimizer.step()
    
  loss_train, acc_train = calculate_loss_and_accuracy(model, criterion, dataloader_train)
  loss_valid, acc_valid = calculate_loss_and_accuracy(model, criterion, dataloader_valid)
  log_train.append([loss_train, acc_train])
  log_valid.append([loss_valid, acc_valid])

  # チェックポイントの保存
  torch.save({"epoch": epoch, "model_state_dict": model.state_dict(), "optimizer_state_dict": optimizer.state_dict()}, f"checkpoint{epoch + 1}.pt")

  # ログを出力
  print("epoch: {}, loss_train: {}, accuracy_train: {}, loss_valid: {}, accuracy_valid: {}".format(epoch+1, loss_train, acc_train, loss_valid, acc_valid))