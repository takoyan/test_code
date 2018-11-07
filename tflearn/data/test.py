import tensorflow as tf
import tflearn
import tflearn.datasets.mnist as mnist
from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np

trainX, trainY, testX, testY = mnist.load_data('./mnist/', one_hot=True)
"""
print(len(trainX), len(trainY))
print(len(testX), len(testY))
print(trainX)
print(trainY)
"""
print(len(trainX), len(trainY))
print(len(trainX[120]))
#plt.imshow(trainY[54999].reshape(28,28), cmap=cm.gray_r, interpolation='nearest')
#plt.show()
print('trainX:'+str(trainX[10]))
print('trainY:'+str(trainY[10]))
