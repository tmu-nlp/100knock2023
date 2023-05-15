import knock35
from knock35 import words

from collections import Counter
freq = Counter(words)

import matplotlib.pyplot as plt

plt.hist(freq.values(), bins=10, range=(1,10))
plt.show();