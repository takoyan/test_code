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
              channels=2,
              rate=44100,
              frames_per_buffer=CHUNK,
              input=True)

input=stream.read(CHUNK)
print 'input:'+str(len(input))
num_data=fromstring(input, dtype='int16')/32768.0
print 'num_data:'+str(len(num_data))
