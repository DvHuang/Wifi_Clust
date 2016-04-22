#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction import image
from sklearn.cluster import spectral_clustering
from PIL import Image
import numpy


filename = 'robot.jpg'
img_robot = Image.open(filename)

img_ndarray = numpy.asarray(img_robot, dtype='float64')/256
# 生成原始图片信息
###################################################
#####################################################
####################################################
l = 100
x, y = np.indices((l, l))

center1 = (28, 24)
center2 = (40, 50)
center3 = (77, 58)

radius1, radius2, radius3 = 16, 14, 15

circle1 = (x - center1[0]) ** 2 + (y - center1[1]) ** 2 < radius1 ** 2
circle2 = (x - center2[0]) ** 2 + (y - center2[1]) ** 2 < radius2 ** 2
circle3 = (x - center3[0]) ** 2 + (y - center3[1]) ** 2 < radius3 ** 2

# 生成包括3个圆的图片
img = circle1 + circle2 + circle3
print ("img_processing.size=",img.size)
mask = img.astype(bool)
img = img.astype(float)
print ("img_processing.size=",img.size)
img += 1 + 0.2 * np.random.randn(*img.shape)
print ("img_processing.size=",img.size)

graph = image.img_to_graph(img, mask=mask)
graph.data = np.exp(-graph.data / graph.data.std())
#########################################################
##########################################################
#imgrobot operation

print ("robotsize=",img_ndarray.size)
mask_robot = img_ndarray.astype(bool)
img_robot = img_ndarray.astype(float)
print ("robotsize=",img_ndarray.size)

graph_robot = image.img_to_graph(img_ndarray, mask=mask_robot)
#graph_robot.data = np.exp(-img_ndarray.data / img_ndarray.data.std())



# 聚类输出
labels = spectral_clustering(graph_robot, n_clusters=3)
label_im = -np.ones(mask_robot.shape)
label_im[mask_robot] = labels


plt.matshow(img_robot)
plt.matshow(label_im)

plt.show()