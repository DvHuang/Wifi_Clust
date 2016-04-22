# -*- coding: utf-8 -*-
import numpy as np
import urllib
from sklearn import preprocessing
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import metrics
from sklearn.linear_model import LogisticRegression



def load_np(path,int_feature):


    # load the CSV file as a numpy matrix
    dataset = np.loadtxt(path, delimiter="\t", usecols=range(int_feature))
    # separate the data from the target attributes
    print ("dataset:",dataset)

    X = dataset[:,0:int_feature]
    # Y = dataset[:,int_category]


    return X

