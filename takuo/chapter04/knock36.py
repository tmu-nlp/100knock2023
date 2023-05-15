import knock35
from matplotlib import pyplot
import japanize_matplotlib

head10 = knock35.word_freq[0:10]
words = [tup[0] for tup in head10]
freqs = [tup[1] for tup in head10]

barplt = pyplot.bar(words, freqs)
pyplot.bar_label(barplt, label_type="edge")
pyplot.savefig("chapter04/out_knock36_.png")
