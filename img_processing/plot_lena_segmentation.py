print(__doc__)

import time

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


from sklearn.feature_extraction import image
from sklearn.cluster import spectral_clustering
from scipy import misc
import numpy
from PIL import Image


# gray_img = misc.imread('lena_3d.jpg')
# gray_img = sp.misc.lena()
# sp.misc.imsave("net_lena.jpg",gray_img)

gray_img = numpy.array(Image.open('lena_3d.jpg').convert('L'))
# rgb = numpy.array(Image.open('small.jpg'))

# print ("robot.shape",robot.shape)
# print ("lena.shape",lena.shape)
print("gray_img.shape",gray_img.shape,type(gray_img))

# print("rgb.shape",rgb.shape)


# gray_img=misc.imresize(gray_img, [256,256], interp='bilinear', mode=None)
print("have imresize gray_img.shape",gray_img.shape,type(gray_img))
# lena = lena[::2, ::2] + lena[1::2, ::2] + lena[::2, 1::2] + lena[1::2, 1::2]
# lena = lena[::2, ::2] + lena[1::2, ::2] + lena[::2, 1::2] + lena[1::2, 1::2]

def compression (lena):
    lena = lena[::2, ::2] + lena[1::2, ::2] + lena[::2, 1::2] + lena[1::2, 1::2]
    return  lena


# gray_img=compression(gray_img)
# gray_img=compression(gray_img)
# gray_img=compression(gray_img)

print("have compression gray_img.shape",gray_img.shape,type(gray_img))

# Convert the image into a graph with the value of the gradient on the
# edges.
# graph = image.img_to_graph(lena)
graph2 = image.img_to_graph(gray_img)
# graph3 = image.img_to_graph(rgb)



# Take a decreasing function of the gradient: an exponential
# The smaller beta is, the more independent the segmentation is of the
# actual image. For beta=1, the segmentation is close to a voronoi
beta = 5
eps = 1e-6
# graph.data = np.exp(-beta * graph.data / lena.std()) + eps
graph2.data = np.exp(-beta * graph2.data / gray_img.std()) + eps
# graph3.data = np.exp(-beta * graph3.data / rgb.std()) + eps

# Apply spectral clustering (this step goes much faster if you have pyamg
# installed)
N_REGIONS = 11

###############################################################################
# Visualize the resulting regions

for assign_labels in ( 'kmeans','discretize'):
    t0 = time.time()
    labels = spectral_clustering(graph2, n_clusters=N_REGIONS,
                                 assign_labels=assign_labels,
                                 random_state=1)
    t1 = time.time()
    labels = labels.reshape(gray_img.shape)

    plt.figure(figsize=(5, 5))
    plt.imshow(gray_img,   cmap=plt.cm.gray)
    for l in range(N_REGIONS):
        plt.contour(labels == l, contours=1,
                    colors=[plt.cm.spectral( l / float(N_REGIONS)), ])
    plt.xticks(())
    plt.yticks(())
    plt.title('Spectral clustering: %s, %.2fs' % (assign_labels, (t1 - t0)))
    numpy.nan

plt.show()
