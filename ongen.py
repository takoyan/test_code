#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pyaudio
from scipy import fromstring, int16
from matplotlib import pyplot as pl


CHUNK=1024
p=pyaudio.PyAudio()
input_device_index=0


def search(CHANNELS):
    stream=p.open(format=pyaudio.paInt16,
              channels=1,
              rate=44100,
              frames_per_buffer=CHUNK,
              input=True)

    input=stream.read(CHUNK)
    num_data=fromstring(input, dtype='int16')/32768.0
    
    if(num_data.max()<=0.02):
        return 0
    p.close(stream)
    stream.close()
    print "ch:" + str(CHANNELS)+ ": "+ str(num_data[:, CHANNELS].max())
    return num_data[:, CHANNELS].max()



if __name__ == '__main__':
    
    count=0
    data1=[0]
    data2=[0]
    data3=[0]
    data4=[0]
    data6=[0]
    data7=[0]
    data8=[0]
    data9=[0]
    while(count<=5):

        data1.append(search(0))#0
        data2.append(search(1))#45
        data3.append(search(2))#90
        data4.append(search(3))#135
        data6.append(search(4))#180
        data7.append(search(5))#225
        data8.append(search(6))#280
        data9.append(search(7))#325

        count+=count+1

    data=[np.average(data1),
    np.average(data2), np.average(data3), np.average(data4),
    np.average(data6), np.average(data7), np.average(data8), np.average(data9)]
    if(np.argmax(data)==0):
        print str(0)+"度"
    elif(np.argmax(data)==1):
        print str(45)+"度"
    elif(np.argmax(data)==2):
        print str(90)+"度"
    elif(np.argmax(data)==3):
        print str(135)+"度"
    elif(np.argmax(data)==4):
        print str(180)+"度"
    elif(np.argmax(data)==5):
        print str(225)+"度"
    elif(np.argmax(data)==6):
        print str(280)+"度"
    elif(np.argmax(data)==7):
        print str(325)+"度"
