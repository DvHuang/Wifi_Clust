# -*- coding: utf-8 -*-

import numpy as np
from sklearn.cluster import spectral_clustering
from sklearn.cluster import AffinityPropagation
from scipy.sparse import coo_matrix

def clust(vectorfile,matrixfile,clusted):

    fid2fname = {}
    for line in open(vectorfile) :
        line = line.strip().split('\t')
        fid2fname.setdefault(int(line[0]), line[1:])

    N = len(fid2fname)
    rowlist = []
    collist = []
    datalist = []
    for line in open(matrixfile) :
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
    labels = spectral_clustering(graph, n_clusters=550, eigen_solver='arpack')

    cluster2fid = {}
    for index, lab in enumerate(labels) :
        cluster2fid.setdefault(lab, [])
        cluster2fid[lab].append(index)

    normal_data = open("normal-data.txt", 'w')
    easy_data=open("spectal_easy-data-550.txt", 'w')
    for index, lab in enumerate(cluster2fid) :
        for fid in cluster2fid[lab] :
            strx=""
            for i in range(0, len(fid2fname[fid])):
                strx+=str(fid2fname[fid][i])+"\t"
            print >> normal_data,strx+'\t'+str(index)
            print >> easy_data,strx+'\t'+str(fid)+'\t'+str(index)




