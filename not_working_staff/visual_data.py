import csv
import matplotlib.pyplot as plt
import numpy as np
import random
from mpl_toolkits.mplot3d import Axes3D

file = open('1641591959435.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
rows = []
for row in csvreader:
        rows.append(row)
file.close()

#fig = plt.figure(figsize=(12, 12))
#ax = fig.add_subplot(tight_layout=True)

longitude = []
latitude = []
vertical = []
horizontal = []
for i in range(len(rows)-3):
    longitude.append(rows[i][6])
    latitude.append(rows[i][7])
    vertical.append(rows[i][8])
    horizontal.append(rows[i][10])

# longitude = map(lambda x: float(x),longitude)
# latitude = map(lambda x: float(x),latitude)
# vertical = map(lambda x: float(x),vertical)
# horizontal = map(lambda x: float(x),horizontal)

# sequence_containing_x_vals = list(longitude)
# sequence_containing_y_vals = list(latitude)
# sequence_containing_z_vals = list(vertical)

# # im1 = fig.figimage(sequence_containing_z_vals, xo=50, yo=0, origin='lower')
# # im2 = fig.figimage(Z, xo=100, yo=100, alpha=.8, origin='lower')

# plt.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals, cmap='viridis')
# plt.show()

# a = np.random.random((16, 16))
# plt.imshow(a, cmap='hot', interpolation='nearest')
# plt.show()
z = np.array(vertical)
x = np.array(longitude)
y = np.array(latitude)

# y, x = np.meshgrid(y, x)
# z, d = np.meshgrid(z, np.ones(len(z)))
# z_min, z_max = -45, -38

# fig, ax = plt.subplots()

# c = ax.pcolormesh(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)
# ax.set_title('pcolormesh')
# # set the limits of the plot to the limits of the data
# #ax.axis([x.min(), x.max(), y.min(), y.max()])
# fig.colorbar(c, ax=ax)

plt.scatter(x,y,alpha=0.3,s=(-0.01)*np.array([float(i) for i in z]),cmap='viridis')




plt.show()