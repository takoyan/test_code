#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tflearn
import tensorflow as tf
import numpy as np
import wave
from scipy import fromstring, int16



sound=[]
answer=[]
list0=[1,0,0,0,0,0,0,0]
list1=[0,1,0,0,0,0,0,0]
list2=[0,0,1,0,0,0,0,0]
list3=[0,0,0,1,0,0,0,0]
list4=[0,0,0,0,1,0,0,0]
list5=[0,0,0,0,0,1,0,0]
list6=[0,0,0,0,0,0,1,0]
list7=[0,0,0,0,0,0,0,1]
i=0
j=1
k=0

###学習用データセット
while(i<=315):
    while(j<=44):
        wr=wave.open('./sound_'+str(i)+'/output/'+str(j)+'.wav', 'rb')
        data=wr.readframes(wr.getnframes())
        num_data=fromstring(data, dtype='int16')/32768.0
        sound.append(num_data)
        j+=1
    i+=45
    j=1



    
###学習用解答データセット
while(k<=352):
    if(k<=43):
        answer.append(list0)
    elif(k>=44 and k<=87):
        answer.append(list1)
    elif(k>=88 and k<=131):
        answer.append(list2)
    elif(k>=132 and k<=175):
        answer.append(list3)
    elif(k>=176 and k<=219):
        answer.append(list4)
    elif(k>=220 and k<=263):
        answer.append(list5)
    elif(k>=264 and k<=307):
        answer.append(list6)
    elif(k>=308 and k<=351):
        answer.append(list7)
    k+=1

sound=np.array(sound)
answer=np.array(answer)



###学習すっぞ
tf.reset_default_graph()

net=tflearn.input_data(shape=[None, 32000])

net=tflearn.fully_connected(net, 128, activation='relu')
net=tflearn.dropout(net, 0.8)

net=tflearn.fully_connected(net, 8, activation='softmax')
net=tflearn.regression(net, optimizer='sgd', learning_rate=0.5, loss='categorical_crossentropy')

model=tflearn.DNN(net)
model.fit(sound, answer, n_epoch=20, batch_size=100, validation_set=0.1, show_metric=True)


"""
j=1
sound2=[]
answer2=[]
while(j<=44):
    wr2=wave.open('./sound_0/output/'+str(j)+'.wav', 'rb')
    data2=wr2.readframes(wr2.getnframes())
    num_data2=fromstring(data2, dtype='int16')
    sound2.append(num_data2)
    j+=1

k=0
while(k<=43):
        answer2.append(list0)
        k+=1

sound2=np.array(sound2)
answer2=np.array(answer2)
        
print(len(sound2), len(answer2))
"""

pred=np.array(model.predict(sound)).argmax(axis=1)
label=answer.argmax(axis=1)

accuracy=np.mean(pred==label, axis=0)
print(accuracy)
