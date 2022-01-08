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



longitude = []
latitude = []
vertical = []
horizontal = []
for i in range(len(rows)-3):
    longitude.append(rows[i][6])
    latitude.append(rows[i][7])
    vertical.append(rows[i][8])
    horizontal.append(rows[i][10])

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')

xx = map(lambda x: float(x),longitude)
y = map(lambda x: float(x),latitude)
z = map(lambda x: float(x),vertical)
d = map(lambda x: float(x),horizontal)

sequence_containing_x_vals = list(xx)
sequence_containing_y_vals = list(y)
sequence_containing_z_vals = list(d)

plt.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals)
plt.show()
