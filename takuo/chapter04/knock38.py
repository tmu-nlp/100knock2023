import knock35
from matplotlib import pyplot
import japanize_matplotlib

max_freq = knock35.word_freq[0][1]
freqs = range(1, max_freq+1)

freq_count = [0 for i in freqs]

for tupl in knock35.word_freq:
    freq_count[tupl[1]-1] += 1

pyplot.hist(freq_count, bins=300, range=(1, max_freq))
pyplot.savefig("chapter04/out_knock38.png", dpi=500)
