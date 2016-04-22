#!/usr/bin/env python

#生成矩阵
import sys
import numpy as np

from sklearn.cluster import spectral_clustering
from scipy.sparse import coo_matrix

###############################################################################

fid2fname = {}
for line in open("points.txt") :
    line = line.strip().split('\t')
    fid2fname.setdefault(int(line[0]), (float(line[1]), float(line[2])))

N = len(fid2fname)
rowlist = []
collist = []
datalist = []
for line in open("sim_pnts.txt") :
    line = line.strip().split('\t')
    if len(line) < 3 : continue
    f1, f2, sim = line[:3]
    rowlist.append(int(f1))
    collist.append(int(f2))
    datalist.append(float(sim))

for id in fid2fname :
    rowlist.append(int(id))
    collist.append(int(id))
    datalist.append(1.0)

row = np.array(rowlist)
col = np.array(collist)
data = np.array(datalist)
graph = coo_matrix((data, (row, col)), shape=(N, N))

###############################################################################

# Force the solver to be arpack, since amg is numerically
# unstable on this example
labels = spectral_clustering(graph, n_clusters=3, eigen_solver='arpack')

#print labels
cluster2fid = {}
for index, lab in enumerate(labels) :
    cluster2fid.setdefault(lab, [])
    cluster2fid[lab].append(index)

for index, lab in enumerate(cluster2fid) :
    fd = open("cluster_%s" % index, "w")
    for fid in cluster2fid[lab] :
        print >> fd , fid2fname[fid]
