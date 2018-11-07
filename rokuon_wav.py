import numpy as np
import wave
import pyaudio

time=5
index=0

FORMAT=pyaudio.paInt16
CHANNELS=2
RATE=16000
CHUNK=16000
audio=pyaudio.PyAudio()


stream=audio.open(format=FORMAT,
                  channels=CHANNELS,
                  rate=RATE,
                  input=True,
                  input_device_index=index,
                  frames_per_buffer=CHUNK)

print('start!!!!!!')
frames=[]
count=0
while(count<8):
    name='sound_'+str(45*count)+'/'+'sound_11'+'.wav'
    for i in range(0, int(RATE / CHUNK * time)):
        data=stream.read(CHUNK)
        frames.append(data)
    print(name)
    waveFile = wave.open(name, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    count+=1
waveFile.close()
stream.stop_stream()
stream.close()
audio.terminate()

