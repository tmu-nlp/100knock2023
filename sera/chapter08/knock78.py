def calculate_loss_and_accuracy(model, criterion, loader, device):
  model.eval()
  loss = 0
  total = 0
  correct = 0
  with torch.no_grad():
    for inputs, labels in loader:
      inputs = inputs.to(device)
      labels = labels.to(device)
      outputs = model(inputs)
      loss += criterion(outputs, labels).item()
      pred = torch.argmax(outputs, dim=-1)
      total += len(inputs)
      correct += (pred == labels).sum().item()
      
  return loss / len(loader), correct / total
  

def train_model(dataset_train, dataset_valid, batch_size, model, criterion, optimizer, num_epochs, device=None):
  model.to(device) # GPUに送る

  dataloader_train = DataLoader(dataset_train, batch_size=batch_size, shuffle=True)
  dataloader_valid = DataLoader(dataset_valid, batch_size=len(dataset_valid), shuffle=False)

  log_train = []
  log_valid = []
  for epoch in range(num_epochs):
    s_time = time.time()
    model.train()
    for inputs, labels in dataloader_train:
      optimizer.zero_grad()
      inputs = inputs.to(device)
      labels = labels.to(device)
      outputs = model.forward(inputs)
      loss = criterion(outputs, labels)
      loss.backward()
      optimizer.step()
    
    loss_train, acc_train = calculate_loss_and_accuracy(model, criterion, dataloader_train, device)
    loss_valid, acc_valid = calculate_loss_and_accuracy(model, criterion, dataloader_valid, device)
    log_train.append([loss_train, acc_train])
    log_valid.append([loss_valid, acc_valid])

    torch.save({"epoch": epoch, "model_state_dict": model.state_dict(), "optimizer_state_dict": optimizer.state_dict()}, f"checkpoint{epoch + 1}.pt")
    
    e_time = time.time()

    print("epoch: {}, loss_train: {}, accuracy_train: {}, loss_valid: {}, accuracy_valid: {}".format(epoch+1, loss_train, acc_train, loss_valid, acc_valid)) 

  return {"train": log_train, "valid": log_valid}

dataset_train = CreateDataset(X_train, y_train)
dataset_valid = CreateDataset(X_valid, y_valid)

model = SLPNet(300, 4)

criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.SGD(model.parameters(), lr=1e-1)

device = torch.device("cuda")

for batch_size in [2 ** i for i in range(11)]:
  print("バッチサイズ: {}".format(batch_size))
  log = train_model(dataset_train, dataset_valid, batch_size, model, criterion, optimizer, 1, device=device)