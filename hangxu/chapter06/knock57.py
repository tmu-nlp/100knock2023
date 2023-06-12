import knock51
from knock51 import x_train
import knock52
from knock52 import model
import knock54
from knock54 import train1
from knock54 import test1

import numpy as np
import pandas as pd

features = x_train.columns.values ##列名
for c, coef in zip(model.classes_, model.coef_):
    ##np.argsort(-coef):降順, 
    top10 = pd.DataFrame(features[np.argsort(-coef)[:10]], columns=[f"重みの高い特徴量トップ10(クラス名:{c})"])
    worst10 = pd.DataFrame(features[np.argsort(coef)[:10]], columns=[f"重みの低い特徴量トップ10(クラス名:{c})"])
    print(top10, "\n"),
    print(worst10, "\n")

