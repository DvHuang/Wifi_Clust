# -*- coding: utf-8 -*-
import math

def cos_dist(a, b):
    if len(a) != len(b):
        return None
    part_up = 0.0
    a_sq = 0.0
    b_sq = 0.0
    for a1, b1 in zip(a,b):
        part_up += a1*b1
        a_sq += a1**2
        b_sq += b1**2
    part_down = math.sqrt(a_sq*b_sq)
    if part_down == 0.0:
        return None
    else:
        return part_up / part_down

def list_marix(pointlist,matrixfile):
    simfd = open(matrixfile, 'w')
    for pnt1 in pointlist :
        for pnt2 in pointlist :
            index1, index2 = pnt1[0], pnt2[0]
            dist = cos_dist(pnt1[1], pnt2[1])
            print >> simfd, str(index1) + "\t"+str(index2) + "\t" + str(dist)
    simfd.close()



