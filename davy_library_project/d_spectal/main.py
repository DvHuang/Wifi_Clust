# -*- coding: utf-8 -*-
import a_N_dimension
import a_extra
import b


def main():

    feature_map = a_extra.android_txt("libary6.txt")

    pointlist= a_extra.normal_txt(feature_map, "libary6.txt", "vector.txt")
    a_N_dimension.list_marix(pointlist, "matrix.txt")
    b.clust("vector.txt", "matrix.txt", "clusted.txt")

if __name__=="__main__":
    main()