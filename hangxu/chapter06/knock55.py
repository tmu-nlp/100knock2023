#混同行列: 予測とその予想の正解かどうかの組み分けを表にまとめたもの

import knock51
from knock51 import x_train
from knock51 import x_test
from knock51 import train
from knock51 import test
import knock52
from knock52 import model
import knock54
from knock54 import train1
from knock54 import test1

from sklearn.metrics import confusion_matrix
print(confusion_matrix(train['CATEGORY'], train1))
print(confusion_matrix(test['CATEGORY'], test1))