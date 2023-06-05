import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, make_scorer


#学習データ
X_train = pd.read_table("train.feature.txt", header=None)
Y_train = pd.read_table("train.txt", header=None)[1]
#検証データ
X_valid = pd.read_table("valid.feature.txt", header=None)
Y_valid = pd.read_table("valid.txt", header=None)[1]
#評価データ
X_test = pd.read_table("test.feature.txt", header=None)
Y_test = pd.read_table("test.txt", header=None)[1]
params = {"solver": ["newton-cg", "lbfgs", "liblinear", "sag"]}
gscv = GridSearchCV(LogisticRegression(random_state=0, max_iter=1000), params, scoring="accuracy")
gscv.fit(X_train, Y_train)
gs_result = pd.DataFrame.from_dict(gscv.cv_results_)
gs_result.to_csv("gs_result.csv")

print(gscv.best_score_)
print(gscv.best_params_)
#最も精度が良いモデルを取得し，評価データの正解率を出力
best_lr = gscv.best_estimator_
print(accuracy_score(Y_test, best_lr.predict(X_test)))