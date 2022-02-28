from function import readPoints, unFence
from matplotlib import pyplot as plt
import numpy as np

data = readPoints('1645131920130.csv')


fig, ax = plt.subplots(nrows=1, ncols=2, sharex=False, sharey=True, figsize=(6, 6))
fig.add_subplot(111, frameon=False)
plt.gca().axes.yaxis.set_visible(False)
unFence

ax[0].hist(data['data_measured'][8],bins=20, rwidth=0.8, density=True, color='black', alpha=0.8)
# fig.add_subplot(122, frameon=False)
plt.gca().axes.yaxis.set_visible(False)
ax[1].hist(data['data_measured'][10],bins=20, rwidth=0.8 ,density=True, color = 'black', alpha=0.8)
