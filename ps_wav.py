#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyaudio
import wave
import numpy as np
from scipy import fromstring, int16
from pocketsphinx import AudioFile, get_model_path, Decoder
import os

dic_path='/home/takoyan/catkin_ws/src/onsei'
dic_name='ziso.dict'
wav_path='/home/takoyan/test'
model_dir='/usr/local/lib/python2.7/dist-packages/pocketsphinx/model/en-us'
hmm = os.path.join(model_dir, "/usr/local/lib/python2.7/dist-packages/pocketsphinx/model/en-us/en-us")
lm = os.path.join(model_dir, "/usr/local/lib/python2.7/dist-packages/pocketsphinx/model/en-us.lm.bin")





wavf='test.wav'
wr=wave.open(wavf, 'r')
num_data=wr.readframes(wr.getnframes())


#data=AudioFile(dic=os.path.join(dic_path, dic_name),
#lm=os.path.join(wav_path, wavf))
config = Decoder.default_config()
config.set_string('-hmm', hmm)
config.set_string('-lm', lm)
config.set_string('-dict', dic_path)
config.set_string('-logfn', '/dev/null')
decoder = Decoder(config)
decoder.start_utt()

decoder.process_raw(num_data, False, False)


print(decoder.process_raw)

