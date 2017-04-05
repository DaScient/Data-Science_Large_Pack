# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 08:19:35 2017

@author: don
"""
import os
os.chdir('C:\\Users\don\Desktop\kNN classifiers\Giant Table')


import numpy as np
np.set_printoptions(threshold=np.inf)




from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
iris = datasets.load_iris()
X = iris.data
y = iris.target
rf = RandomForestClassifier(n_estimators=80)
rf.fit(X, y)