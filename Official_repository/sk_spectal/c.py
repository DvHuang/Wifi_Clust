#!/usr/bin/env python

#画图
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))

cluster_list = []

cluster_0_x = []
cluster_0_y = []
for line in open("cluster_0"):
    line = line.strip().split(',')
    x = float(line[0][1:].strip())
    y = float(line[1][:-1].strip())
    cluster_0_x.append(x)
    cluster_0_y.append(y)

plt.plot(cluster_0_x, cluster_0_y, 'or')


cluster_1_x = []
cluster_1_y = []
for line in open("cluster_1"):
    line = line.strip().split(',')
    x = float(line[0][1:].strip())
    y = float(line[1][:-1].strip())
    cluster_1_x.append(x)
    cluster_1_y.append(y)

plt.plot(cluster_1_x, cluster_1_y, 'xb')

cluster_2_x = []
cluster_2_y = []
for line in open("cluster_2"):
    line = line.strip().split(',')
    x = float(line[0][1:].strip())
    y = float(line[1][:-1].strip())
    cluster_2_x.append(x)
    cluster_2_y.append(y)

plt.plot(cluster_2_x, cluster_2_y, '+g')

plt.show()
