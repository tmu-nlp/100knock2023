import pickle


lr = pickle.load(open("model.pkl", "rb"))
vocabulary = pickle.load(open(r"vocabulary.pkl", "rb"))
weights_dic = lr.coef_
categories = ["business", "entertainment", "health", "science and technology"]

for i, weights in enumerate(weights_dic):
    features = dict()
    for word, index in vocabulary.items():
        features[word] = weights[index]
    for word, weight in sorted(features.items(), key=lambda x:x[1], reverse=True)[:10]:
        print(f"{word}\t{weight}")
    for word, weight in sorted(features.items(), key=lambda x:x[1])[:10]:
        print(f"{word}\t{weight}")
    print("\n")