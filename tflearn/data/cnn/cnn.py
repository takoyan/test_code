#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tensorflow as tf
import tflearn

from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression

import tflearn.datasets.mnist as mnist

import numpy as np

trainX, trainY, testX, testY=mnist.load_data('../mnist/', one_hot=True)

trainX =trainX.reshape([-1, 28, 28, 1])
testX =testX.reshape([-1, 28, 28, 1])
print(trainX[0])

tf.reset_default_graph()

net=input_data(shape=[None, 28, 28, 1])


net=conv_2d(net, 32, 5, activation='relu')

net=max_pool_2d(net, 2)

net=conv_2d(net, 64, 5, activation='relu')

net=max_pool_2d(net, 2)

net=fully_connected(net, 128, activation='relu')

net=dropout(net, 0.5)


net=tflearn.fully_connected(net, 10, activation='softmax')
net=tflearn.regression(net, optimizer='sgd', learning_rate=0.5, loss='categorical_crossentropy')

model=tflearn.DNN(net)
model.fit(trainX, trainY, n_epoch=20, batch_size=100, validation_set=0.1, show_metric=True)
