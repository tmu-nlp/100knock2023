import knock52
from knock52 import model
import knock51
from knock51 import x_test
import numpy as np

def predict(model, data):
##predict_proba: returns the predicted probabilities, predict method: the predicted class labels
##axis=1: 列
    return [np.max(model.predict_proba(data),axis = 1), model.predict(data)]

print(predict(model, x_test))
