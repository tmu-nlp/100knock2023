from knock52 import clf
from knock50 import train_df, test_df
from knock51 import X_train, X_test
from sklearn.metrics import accuracy_score

y_train_pred = clf.predict(X_train)
y_test_pred = clf.predict(X_test)
y_train = train_df['CATEGORY']
y_test = test_df['CATEGORY']
print (accuracy_score(y_train, y_train_pred))
print (accuracy_score(y_test, y_test_pred))
