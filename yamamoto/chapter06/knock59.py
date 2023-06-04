# knock59
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
import pandas as pd

param = {"C": [5,10, 20, 30]}
model = GridSearchCV(LogisticRegression(max_iter=1000), param, cv=2, verbose=1)
model.fit(X_train, train["CATEGORY"])

bestmodel = model.best_estimator_
print("score: ", model.best_score_)
print("C: ", model.best_params_)
print(bestmodel.score(X_valid, valid["CATEGORY"]))