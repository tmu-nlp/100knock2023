import knock51
from knock51 import x_train
from knock51 import train

from sklearn.linear_model import LogisticRegression

#回帰
model = LogisticRegression()
model.fit(x_train, train['CATEGORY'])
