from knock54 import y_train, y_test, y_train_pred, y_test_pred
from sklearn.metrics import confusion_matrix

print (confusion_matrix(y_train, y_train_pred, labels=['b','t','e','m']))
print (confusion_matrix(y_test, y_test_pred, labels=['b','t','e','m']))