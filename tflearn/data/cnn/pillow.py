#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tensorflow as tf
import tflearn

from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression

import tflearn.datasets.mnist as mnist

from PIL import Image
from PIL import ImageEnhance

import numpy as np
import os

train_dirs=['pos', 'neg']

trainX =[]
trainY =[]


for i, d in enumerate(train_dirs):
    files=os.listdir('./pict/' +d)
    #+print (str(files) +'aaaaaaaaaaaaaa')
    for f in files:
        #print(f) #各ファイル名
        image =Image.open('./pict/' + d + '/' + f, 'r')
        gray_image=image.convert('L')
        gray_image_px=np.array(gray_image)
        gray_image_flatten=gray_image_px.flatten().astype(np.float32)/255.0
        trainX.append(gray_image_flatten)

        tmp=np.zeros(2)
        tmp[i]=1
        trainY.append(tmp)

trainX = np.asarray(trainX)
trainY = np.array(trainY)

trainX = trainX.reshape([-1, 32, 32, 1])
print(trainX[0])
