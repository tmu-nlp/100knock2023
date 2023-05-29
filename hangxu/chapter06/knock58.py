import knock51
from knock51 import x_train
from knock51 import x_valid
from knock51 import x_test
from knock51 import train
from knock51 import valid
from knock51 import test

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np

#正則化パラメータ
c_list = np.linspace(0.0001, 0.1, 10)

#学習
acc = []
for c in c_list:
    model1 = LogisticRegression(C=c)
    model1.fit(x_train, train['CATEGORY'])

    #予測
    train2 = model1.predict(x_train)
    valid2 = model1.predict(x_valid)
    test2 = model1.predict(x_test)

    #正解率
    train_acc = accuracy_score(train['CATEGORY'], train2)
    valid_acc = accuracy_score(valid['CATEGORY'], valid2)
    test_acc = accuracy_score(test['CATEGORY'], test2)
    acc.append([c, train_acc, valid_acc, test_acc])
accs = np.array(acc).T

#グラフを作る
plt.plot(accs[0], accs[1], label = 'train', marker = 'o')
plt.plot(accs[0], accs[2], label = 'valid', marker = 'o')
plt.plot(accs[0], accs[3], label = 'test', marker = 'o')
plt.legend()
plt.xlabel('C')
plt.ylabel('Accuracy')
plt.show()
