#!/usr/bin/env python
#实验性程序：
#   生成数据，生成矩阵，谱聚类，画图
#生成数据放入文件
import random
import numpy as np
import math

index = 0
pointlist = []
fd = open("points.txt", 'w')

for x in np.arange(0.1, 10., 0.5) :
    for y in np.arange(0., 10., 0.1) :
        print >> fd, str(index)+'\t'+str(x)+'\t'+str(y)
        pointlist.append((index, (x, y)))
        index += 1

for x in np.arange(-10.0, -0.1, 0.5) :
    for y in np.arange(0., 10., 0.1) :
        print >> fd, str(index)+'\t'+str(x)+'\t'+str(y)
        pointlist.append((index, (x, y)))
        index += 1

for x in np.arange(-10.0, -0.1, 0.5) :
    for y in np.arange(-10.0, 0., 0.1) :
        print >> fd, str(index)+'\t'+str(x)+'\t'+str(y)
        pointlist.append((index, (x, y)))
        index += 1
fd.close()

def get_dist(pnt1, pnt2) :
    return math.sqrt((pnt1[1][0] - pnt2[1][0])**2 + (pnt1[1][1] - pnt2[1][1])**2)

simfd = open("sim_pnts.txt", 'w')
#print pointlist

for pnt1 in pointlist :
    #print ("pnt1:",pnt1)
    for pnt2 in pointlist :
        #print ("pnt2:",pnt2)
        index1, index2 = pnt1[0], pnt2[0]
        dist = get_dist(pnt1, pnt2)
        if dist <=0.00001 :
            print >> simfd, str(index1) + "\t"+str(index2) + "\t" + "10"
            continue
        sim = 1.0 / dist
        print >> simfd, str(index1) + "\t"+str(index2) + "\t" + str(sim)
simfd.close()
