import knock35
from knock35 import words

from collections import Counter
f1 = [f[1] for f in Counter(words).most_common()]  #most_common:出現回数が多い順

import matplotlib.pyplot as plt
import numpy as np
plt.scatter(np.log(range(1, len(f1)+1)), np.log(f1))  #(x,y)
plt.show();
