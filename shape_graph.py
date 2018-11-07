# -*-coding:utf-8 -*-
import wave
import numpy as np
import matplotlib.pyplot as plt

wf=wave.open('/home/takoyan/test/sound_90/sound_3.wav')
buf=wf.readframes(wf.getnframes())

data=np.frombuffer(buf, dtype='int16')
plt.plot(data)
plt.show()
