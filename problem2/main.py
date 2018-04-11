import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


rbf = lambda x, y, sigma: np.exp(-(x**2 + y**2) / (2 * sigma ** 2)) + 1

n = 1000
scale = 4
shift = 0.5
r_0 = 1
r_1 = 1.3
sigma = 1
area = np.array(list((zip(scale * (np.random.rand(n) - shift), scale * (np.random.rand(n) - shift)))))
circle = area[(area[:, 0] ** 2 + area[:, 1] ** 2) <= r_0 ** 2]
out_of_circle = area[(area[:, 0] ** 2 + area[:, 1] ** 2) > r_1 ** 2]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
z = rbf(circle[:, 0], circle[:, 1], sigma)
ax.scatter(circle[:, 0], circle[:, 1], z, marker='x', color='r', alpha=0.7)
z = rbf(out_of_circle[:, 0], out_of_circle[:, 1], sigma)
ax.scatter(out_of_circle[:, 0], out_of_circle[:, 1], z, marker='o', color='b', alpha=0.7)
# Projection
ax.scatter(circle[:, 0], circle[:, 1], np.zeros(circle[:, 1].shape), marker='x', color='r', alpha=0.2)
ax.scatter(out_of_circle[:, 0], out_of_circle[:, 1], np.zeros(out_of_circle[:, 1].shape), marker='o', color='b',
           alpha=0.2)
plt.show()

# Noise point
x_0 = -0.5
y_0 = -1.3
r_0 = 0.4

a = 1
b = 2
c = 1
des_bound = lambda x, y: a * x + y * b + c
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
line_more = np.array(area[des_bound(area[:, 0], area[:, 1]) >= 0])
line_less = np.array(area[
    np.logical_and(
        des_bound(area[:, 0], area[:, 1]) < 0,
        (area[:, 0] - x_0) ** 2 + (area[:, 1] - y_0) ** 2 > r_0 ** 2
    )])
noise = np.array(area[(area[:, 0] - x_0) ** 2 + (area[:, 1] - y_0) ** 2 < r_0 ** 2])
z = rbf(line_more[:, 0], line_more[:, 1], sigma)
ax.scatter(line_more[:, 0], line_more[:, 1], z, marker='x', color='r', alpha=0.7)
z = rbf(line_less[:, 0], line_less[:, 1], sigma)
ax.scatter(line_less[:, 0], line_less[:, 1], z, marker='o', color='b', alpha=0.7)
z = rbf(noise[:, 0], noise[:, 1], sigma)
ax.scatter(noise[:, 0], noise[:, 1], z, marker='o', color='r', alpha=0.7)
z = rbf(x_0, y_0, sigma)
ax.scatter(x_0, y_0, z, marker='o', color='k', s=50)
# Projection
ax.scatter(line_more[:, 0], line_more[:, 1], np.zeros(line_more[:, 1].shape), marker='x', color='r', alpha=0.2)
ax.scatter(line_less[:, 0], line_less[:, 1], np.zeros(line_less[:, 1].shape), marker='o', color='b',
           alpha=0.2)
ax.scatter(noise[:, 0], noise[:, 1], np.zeros(noise[:, 1].shape), marker='o', color='r', alpha=0.2)
ax.scatter(x_0, y_0, 0, marker='o', color='k', s=20)
plt.show()
