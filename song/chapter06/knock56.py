from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from knock54 import y_test, y_test_pred

print ('pre score is \n',precision_score(y_test, y_test_pred, average=None, labels=['b','t','e','m']))
print ('recall score is \n', recall_score(y_test, y_test_pred, average=None, labels=['b','t','e','m']))
print ('f1 score is \n', f1_score(y_test, y_test_pred, average=None, labels=['b','t','e','m']), '\n')

print ('pre score is \n',precision_score(y_test, y_test_pred, average='micro', labels=['b','t','e','m']))
print ('recall score is \n',recall_score(y_test, y_test_pred, average='micro', labels=['b','t','e','m']))
print ('f1 score is \n',f1_score(y_test, y_test_pred, average='micro', labels=['b','t','e','m']), '\n')

print ('pre score is \n',precision_score(y_test, y_test_pred, average='macro', labels=['b','t','e','m']))
print ('recall score is \n',recall_score(y_test, y_test_pred, average='macro', labels=['b','t','e','m']))
print ('f1 score is \n',f1_score(y_test, y_test_pred, average='macro', labels=['b','t','e','m']), '\n')