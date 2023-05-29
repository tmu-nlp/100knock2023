import knock51
from knock51 import x_train
from knock51 import x_test
from knock51 import train
from knock51 import test
import knock52
from knock52 import model

from sklearn.metrics import accuracy_score

train1 = model.predict(x_train)
test1 = model.predict(x_test)

print(accuracy_score(train['CATEGORY'], train1))
print(accuracy_score(test['CATEGORY'], test1))

