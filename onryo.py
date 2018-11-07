#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pyaudio
from scipy import fromstring, int16
from matplotlib import pyplot as pl

CHUNK=1024
p=pyaudio.PyAudio()
input_device_index=0
stream=p.open(format=pyaudio.paInt16,
              channels=1,
              rate=44100,
              frames_per_buffer=CHUNK,
              input=True)
i=0
while stream.is_active():
    try:
        input=stream.read(CHUNK)
        num_data=fromstring(input, dtype="int16")/32768.0
        #print(num_data)
        #print('最大値:'+str(num_data.max()))
        if(num_data.max()>=0.25):
            print('BIG!!!!!!!!'+str(i))
            i+=1
        #pl.plot(num_data)
        
        #pl.draw()
        #pl.pause(0.01)
        #pl.cla()
    except KeyboardInterrupt:
        #pl.close()
        break
