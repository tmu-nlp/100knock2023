from sklearn.linear_model import LogisticRegression
import os
import numpy as np

import knock51

predictor = LogisticRegression(max_iter=2000)
train_features = np.array(knock51.title_wordvec_train)
train_labels = np.array(knock51.class_train)
print("Start fitting predictor.")
predictor.fit(train_features, train_labels)
