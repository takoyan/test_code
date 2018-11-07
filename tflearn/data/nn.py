import tensorflow as tf
import tflearn
import tflearn.datasets.mnist as mnist
from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np

tf.reset_default_graph()

net = tflearn.input_data(shape=[None, 784])

net = tflearn.fully_connected(net, 128, activation='relu')
net = tflearn.dropout(net, 0.5)

net =tflearn.fully_connected(net, 10, activation='softmax')
net = tflearn.regression(net, optimizer='sgd', learning_rate=0.5, loss='categorical_crossentropy')
