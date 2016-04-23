# Wifi_Clust
Wifi_Clust

在wifi定位问题中，采用聚类的方法省去去除噪音的滤波过程

经过均值和方差筛选强度大且稳定（强度小的方差也可以很大，所以取交集，且默认方差正比于信息熵）的信号，

聚类这一步仅仅是因为懒，当然也可以站在场景里四五个小时去采集数据....

分别用了spectal、k-means、ap 三种方法对其进行聚类操作。

从以下结果来看，spectal和ap的结果都不好解释，这里其实我们事先是大体知道有多少类的，所以k-means足够了

三种方法的"误差"，均不存在指导意义，都是自说自话。

k-means

![image](https://github.com/DvHuang/Wifi_Clust/blob/master/davy_library_project/d_ap/k-means.png)

spectal

![image](https://github.com/DvHuang/Wifi_Clust/blob/master/davy_library_project/d_ap/spectal.png)




