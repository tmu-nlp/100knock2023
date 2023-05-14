import knock35
from matplotlib import pyplot
import japanize_matplotlib

idx = range(1, len(knock35.word_freq)+1)
freqs = [tup[1] for tup in knock35.word_freq]

plot = pyplot.scatter(idx, freqs)
pyplot.xscale("log")
pyplot.yscale("log")
pyplot.savefig("chapter04/out_knock39.png")
