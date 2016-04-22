# -*- coding: utf-8 -*-
#该本本较main 版本的改动
# .1 加入均值和方差滤波选择。
#。2 加入方向信息，davy——oriention
#

import a_N_dimension
import a_extra
import pylab as pl
import numpy as np
import b


def main():

    old_datafile="libary21.txt"
    new_datafile="new_datafile.txt"
    first_vector="first_vector.txt"
    second_vector="second_vector.txt"
    clust_file="clust_file.txt"
    clust_number=30

    #建立特征表
    feature_map = a_extra.android_txt(old_datafile)
    feature_map_resove={}
    #建立反向映射 特征表
    for k,v in feature_map.iteritems():
        feature_map_resove[v]=k

    #根据原始数据生成特征向量表
    a_extra.normal_txt(feature_map,old_datafile, "vector.txt")
    len_feature=len(feature_map)

    print ("len_feature:",len_feature)
    #读入到规范矩阵
    X= a_N_dimension.load_np("vector.txt", len_feature)


    #初始矩阵信息
    print "len dimension:",len(np.mean(X,axis=0))
    print "mean：",np.mean(X,axis=0)
    print "var:",np.var(X,axis=0)

    # 3.0 生成新的特征映射表
    # 3.0.1 平均合格加入
    feature_map_new={}
    value_feature_map_new=0
    # for index, item in enumerate(np.mean(X,axis=0)):
    #     if item>6:
    #
    #         #                反向映射，根据数值找到mac，
    #         #                然后mac作为新表的键
    #         #      新表
    #         if feature_map_resove[index] not in feature_map_new:
    #             feature_map_new[feature_map_resove[index]]=value_feature_map_new
    #             value_feature_map_new+=1
    #
    # print "均值特征选取：" , len(feature_map_new)
    # 3.0.2 方差合格加入
    for index_2, item_2 in enumerate(np.var(X,axis=0)):
        if item_2>100:
            if feature_map_resove[index_2] not in feature_map_new:
                feature_map_new[feature_map_resove[index_2]]=value_feature_map_new
                value_feature_map_new+=1

    print "方差特征选取：" , len(feature_map_new)

    for index, item in enumerate(np.mean(X,axis=0)):
        if item>6:

            #                反向映射，根据数值找到mac，
            #                然后mac作为新表的键
            #      新表
            if feature_map_resove[index] not in feature_map_new:
                feature_map_new[feature_map_resove[index]]=value_feature_map_new
                value_feature_map_new+=1

    print "均值特征选取：" , len(feature_map_new),value_feature_map_new

    #添加方向信息：
    # feature_map_new["zz:zz:zz:zz:zz"]=value_feature_map_new
    # print "feature_map_new......",len(feature_map_new),feature_map_new

    #利用新的feature_map 去重写 原始数据文件，（该文件在这里改写是为了可以直接给后面的分类器使用）
    a_extra.new_original_file(old_datafile,new_datafile,feature_map_new)

    #得到新的数据文件之后，把main文件中做过的事情再做一遍
    #建立特征表
    feature_map_new_new = a_extra.android_txt(new_datafile)

    #执行一次，获取map文件
    fileWriteObj = open("mapfile.txt", 'w')
    for i,k in feature_map_new_new.iteritems():
        fileWriteObj.writelines(str(i)+"#####"+str(k))

    #根据原始数据生成特征向量表
    print "feature new:::",feature_map_new_new
    a_extra.normal_txt(feature_map_new_new, new_datafile, second_vector)
    len_feature=len(feature_map_new_new)

    print ("len_feature:",len_feature)
    #读入到规范矩阵
    second_X= a_N_dimension.load_np(second_vector, len_feature)


    inertia=b.clust(second_X, second_vector,clust_file,clust_number)







#     row_number = np.arange(X.shape[0])
#
#     flag=0
#     for i in range(1, X.shape[1]):
#         single_i=i%10
# #         b---blue   c---cyan  g---green    k----black
# # m---magenta r---red  w---white    y----yellow
#
#         if single_i==1:
#           pl.plot(row_number, X[:,i],'cx')
#         if single_i==2:
#           pl.plot(row_number, X[:,i],'bx')
#         if single_i==3:
#           pl.plot(row_number, X[:,i],'gx')
#         if single_i==4:
#           pl.plot(row_number, X[:,i],'kx')
#         if single_i==2:
#           pl.plot(row_number, X[:,i],'mx')
#         if single_i==2:
#           flag=1
#           pl.plot(row_number, X[:,i],'yx')
#
#         #if flag==1:
#         pl.xlabel('x')
#         pl.ylabel('y')
#         pl.show()
#         flag=0



if __name__=="__main__":
    main()