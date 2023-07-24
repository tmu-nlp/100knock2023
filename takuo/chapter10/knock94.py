import matplotlib.pyplot as plt
import re
import os

def read_score(filename):
    with open(filename) as f:
        x = f.readlines()[1]
        x = re.search(r'(?<=BLEU4 = )\d*\.\d*(?=,)', x)
        return float(x.group())

xs = range(1, 12)
ys = [read_score(f'{os.path.dirname(__file__)}/94.{x}.score') for x in xs]
plt.plot(xs, ys)
plt.show()
