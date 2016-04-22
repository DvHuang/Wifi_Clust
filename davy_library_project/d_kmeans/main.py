# -*- coding: utf-8 -*-
import a_N_dimension
import a_extra
import b


def main():

    #建立特征表
    feature_map = a_extra.android_txt("libary6.txt")
    #根据原始数据生成特征向量表
    a_extra.normal_txt(feature_map, "libary6.txt", "vector.txt")
    len_feature=len(feature_map)

    print ("len_feature:",len_feature)
    #读入到规范矩阵
    X= a_N_dimension.load_np("vector.txt", len_feature)


    b.clust(X, "vector.txt")

if __name__=="__main__":
    main()