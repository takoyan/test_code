import tensorflow as tf
import tflearn
import tflearn.datasets.mnist as mnist
from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np
#saver = tf.train.Saver()
#sess = tf.InteractiveSession()
#init = tf.initialize_all_variables()
#sess.run(init)
#学習用データを指定
trainX, trainY, testX, testY = mnist.load_data('./mnist/', one_hot=True)

tf.reset_default_graph()

#層の作成

net = tflearn.input_data(shape=[None, 784])

net = tflearn.fully_connected(net, 180, activation='relu')
net = tflearn.dropout(net, 0.5)


net =tflearn.fully_connected(net, 10, activation='softmax')
net = tflearn.regression(net, optimizer='sgd', learning_rate=0.5, loss='categorical_crossentropy')

#学習の設定

model = tflearn.DNN(net)
#model.fit(trainX, trainY, n_epoch=20, batch_size=100, validation_set=0.1, show_metric=True)
#model.save("model.tfl")
#テストの設定

model.load("model.tfl")

"""
モデルのセーブはモデル作成後にmodel.save("ファイル名")
モデルのロードは
model = tflearn.DNN(net)
model.load("model.fit")
"""


pred = np.array(model.predict(testX)).argmax(axis=1)
print(pred)

label = testY.argmax(axis=1)
print(label)

accuracy = np.mean(pred == label, axis=0)
print(accuracy)
#saver.save(sess, './model.tflearn')
