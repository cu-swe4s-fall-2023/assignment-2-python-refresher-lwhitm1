import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('Agg')

data_file = sys.argv[1]
out_file = sys.argv[2]
title = sys.argv[3]
x = sys.argv[4]
y = sys.argv[5]

D = []
with open(data_file, 'r') as file:
    for line in file:
        D.append(float(line))

fig, ax = plt.subplots()
ax.hist(D)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel(x)
ax.set_ylabel(y)
ax.set_title(title)

plt.savefig(out_file, bbox_inches='tight')
