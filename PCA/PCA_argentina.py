# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 12:09:59 2017

@author: don
"""
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA, IncrementalPCA
"""
io1 = pd.read_csv('arg-ld_tv.csv',sep=",",usecols=range(0,116)) # To read 1st,2nd and 4th columns
target = np.array(io1)
y = target[:,0]

io2 = pd.read_csv('arg-ld_tv.csv',sep=",",usecols=range(5,85))
X = np.array(io2)
"""
"""
Tachs=pd.read_csv('arg-ld_tv.csv', sep=',',header=1, usecols = range(4,85))
Target=pd.read_csv('arg-ld_tv.csv', sep=',',header=1, usecols = (0))
#Legits=pd.read_csv('arg-ld_tv.csv', sep=',',header=1, usecols = range(4,85), skiprows = range(1,25))
#Counterfeits=pd.read_csv('arg-ld_tv.csv', sep=',',header=1, usecols = range(4,85), skiprows = range(26,145))

al1 = np.array(Tachs)
X = al1.data

al2 = np.array(Target)
y = al2.target
"""
"""
x = np.array(Legits)
c = np.array(Counterfeits)
"""
"""
n_components = 2
ipca = IncrementalPCA(n_components=n_components, batch_size=10)
X_ipca = ipca.fit_transform(X)

pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X)

colors = ['navy', 'turquoise', 'darkorange']


for X_transformed, title in [(X_ipca, "Incremental PCA"), (X_pca, "PCA")]:
    plt.figure(figsize=(8, 8))
    for color, i, target_name in zip(colors, [0, 1, 2], X.target_names):
        plt.scatter(X_transformed[y == i, 0], X_transformed[y == i, 1],
                    color=color, lw=2, label=target_name)

    if "Incremental" in title:
        err = np.abs(np.abs(X_pca) - np.abs(X_ipca)).mean()
        plt.title(title + " of iris dataset\nMean absolute unsigned error "
                  "%.6f" % err)
    else:
        plt.title(title + " of iris dataset")
    plt.legend(loc="best", shadow=False, scatterpoints=1)
    plt.axis([-4, 4, -1.5, 1.5])

plt.show()
"""

"""
pca = PCA(n_components=2)

pca.fit(X)

PCA(copy=True, iterated_power='auto', n_components=2, random_state=None,
  svd_solver='auto', tol=0.0, whiten=False)

print(pca.explained_variance_ratio_)
#[ 0.99244...  0.00755...]



pca = PCA(n_components=2, svd_solver='full')

pca.fit(X)  

PCA(copy=True, iterated_power='auto', n_components=2, random_state=None,
  svd_solver='full', tol=0.0, whiten=False)

print(pca.explained_variance_ratio_) 
#[ 0.99244...  0.00755...]



pca = PCA(n_components=1, svd_solver='arpack')

pca.fit(X)

PCA(copy=True, iterated_power='auto', n_components=1, random_state=None,
  svd_solver='arpack', tol=0.0, whiten=False)

print(pca.explained_variance_ratio_) 
#[ 0.99244...]

"""
###############################################################################
class1_sample = 



































