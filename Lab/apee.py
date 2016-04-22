#!/usr/bin/env python
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
        print ((index, (x, y)))