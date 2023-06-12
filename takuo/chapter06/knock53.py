from knock51 import predictor, title_wordvec_test

# 53
test_ans = predictor.predict(title_wordvec_test)
proba = predictor.predict_proba(title_wordvec_test)
for idx in range(len(title_wordvec_test)):
    print(f"label:{test_ans[idx]}, proba:{proba[idx]}")


# https://colab.research.google.com/drive/1Jk8mlNb2xNSK9C0KpG66WHgclQQP1HiS?authuser=2&hl=ja#scrollTo=--Dip-EuekpZ