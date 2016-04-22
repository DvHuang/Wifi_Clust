# -*- coding: utf-8 -*-

import numpy as np
from scipy.sparse import coo_matrix
from sklearn import cluster


def clust(X,vectorfile,clust_file,clust_number):

    fid2fname = {}
    for line in open(vectorfile) :
        line = line.strip().split('\t')
        fid2fname.setdefault(int(line[0]), line[1:])

    # Force the solver to be arpack, since amg is numerically
    # unstable on this example
    # labels = spectral_clustering(graph, n_clusters=160, eigen_solver='arpack')

    a, labels,inertia = cluster.k_means(X,n_clusters=clust_number)

    print ("inertia=",inertia)
    C=np.column_stack((X,labels))

    easy_data=open(clust_file, 'w')
    for pnt1 in C :
        strx=""
        for charest in pnt1:
            strx+=str(int(charest))+"\t"
        print >> easy_data, strx
    easy_data.close()

    return inertia




    # cluster2fid = {}
    # for index, lab in enumerate(labels) :
    #     cluster2fid.setdefault(lab, [])
    #     cluster2fid[lab].append(index)
    #
    # for index, lab in enumerate(cluster2fid) :
    #     for fid in cluster2fid[lab] :
    #         strx=""
    #         for i in range(0, len(fid2fname[fid])):
    #             strx+=str(fid2fname[fid][i])+"\t"
    #         print >> easy_data,strx+'\t'+str(fid)+'\t'+str(index)





