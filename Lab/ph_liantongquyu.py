#coding:utf-8
import cv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from skimage import data,filter,segmentation,measure,morphology,color,io

#加载并裁剪硬币图片
#image = data.coins()[50:-50, 50:-50]

image=io.imread('d:/D-python/picture_res/9.png',as_grey=True)
#image=io.imread('robot.jpg',as_grey=True)


thresh =filter.threshold_otsu(image) #阈值分割
print "阈值：" ,thresh

bw =morphology.closing(image < thresh, morphology.square(3)) #闭运算

cleared = bw.copy()  #复制
segmentation.clear_border(cleared)  #清除与边界相连的目标物

label_image =measure.label(cleared)  #连通区域标记
borders = np.logical_xor(bw, cleared) #异或
label_image[borders] = -1
image_label_overlay =color.label2rgb(label_image, image=image) #不同标记用不同颜色显示

fig,(ax0,ax1)= plt.subplots(1,2, figsize=(8, 6))
ax0.imshow(cleared,plt.cm.gray)
ax1.imshow(image_label_overlay)

print "区域个数：",len(measure.regionprops(label_image))
for region in measure.regionprops(label_image): #循环得到每一个连通区域属性集

    #忽略小区域
    if region.area < 10:
        continue
    else:
        print "外接边界:",region.bbox
        print "像 素 点:",region.area
        print "区域周长:",region.perimeter
        print "质心坐标:",region.centroid
        print "凸包内像素点总数:",region.convex_area
        #print "离心率:",region.Eccentricity
        print "区域面积和边界外接框面积的比率:",region.extent     #外接边界
        print "区域和外接框之间填充的像素点总数:",region.filled_area
        print "\n\n"




    #绘制外包矩形
    minr, minc, maxr, maxc = region.bbox
    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                              fill=False, edgecolor='red', linewidth=2)
    ax1.add_patch(rect)
fig.tight_layout()
plt.show()