from sklearn.linear_model import LogisticRegression
from knock51 import X_train, train_df

clf = LogisticRegression(max_iter=10000)
clf.fit(X_train, train_df['CATEGORY'])
