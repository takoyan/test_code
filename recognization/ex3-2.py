#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction
#from sklearn.feature_selection import SelectPercentile
#from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import scipy.stats


plt.xlim(-2, 2)
plt.ylim(-2, 2)

ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

list_x=np.array([3,3,5,5])
list_y=np.array([2,4,4,6])



"""
ave_x=np.average(list_x)
ave_y=np.average(list_y)

std_x=np.std(list_x)
std_y=np.std(list_y)


for index, i in enumerate(list_x):
    list_x[index]=(i-ave_x)/std_x

for index, i in enumerate(list_y):
    list_y[index]=(i-ave_y)/std_y

print('\n')
print(list_x)
print(list_y)
print('\n')
array=np.vstack((list_x, list_y))
print(array)
"""


#sc=StandardScaler()
X=np.array([[-1, -np.sqrt(2)], [-1, 0], [1,0], [1, np.sqrt(2)]])
pca=PCA()
pca.fit(X)
SX=pca.fit_transform(X)


#array=np.array(([3,2], [3,4], [5,4], [5,6]))
array_std=scipy.stats.zscore(X)#標準化
array_cov=np.cov(array_std, rowvar=False, ddof=0)#共分散行列化

#plt.plot(list_x, list_y, 'o') //配列2つ版

#print(array)
print('SX:')
print(SX)
print('\n')
print('array_std:')
print(array_std)
print('\n')
print('array_cov')
print(array_cov)
print('\n')

array_vals, array_vecs = np.linalg.eig(array_cov)

print(array_vals)
print(array_vecs)


plt.scatter(array_std[:, 0], array_std[:, 1]) #行列版
plt.plot([-2,2], array_vecs[:,0], "r")
#plt.scatter(SX[:,0], np.zeros(len(SX)))


plt.show()
