'''
from sklearn.manifold import TSNE

tsne = TSNE(n_components=2, random_state=64)
X_reduced = tsne.fit_transform(np.array(cs_v))
plt.figure(figsize=(10, 10))
for x, country, color in zip(X_reduced, cs, kmeans.labels_):
    plt.text(x[0], x[1], country, color='C{}'.format(color))
plt.xlim([-12, 15])
plt.ylim([-15, 15])
plt.savefig('k69.png')
plt.show()
'''