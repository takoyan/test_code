#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyaudio
from pyaudio import PyAudio

import multiprocessing
from multiprocessing import Process
from scipy import fromstring, int16


# 音源定位を行うクラス
class SearchSoundSource():
    def __init__(self, numUseChannel):
        # PyAudioを初期化
        self.audio = PyAudio()

        # setup関数が呼ばれたらAudio機器関連のデータが格納される
        self.streams = {}

        # 使用するマイクの数
        self.numUseChannel = numUseChannel + 1

        # マイクの固有値を定義
        self.chunk = 1024
        self.FORMAT = pyaudio.paInt16
        self.Rate = 16000
        self.RECORD_SECONDS = 1
        self.device_index = None

        # Tamagoマイクを特定
        for num in range(0, self.audio.get_device_count()):
            if "TAMAGO" in self.audio.get_device_info_by_index(num)["name"]:
                print("[*] Found Device!")
                print(self.audio.get_device_info_by_index(num)["name"])
                self.device_index = self.audio.get_device_info_by_index(num)["index"]

        # デバッグ用
        print(self.audio.get_device_info_by_index(self.device_index))

        # たまごマイクの初期化
        self.audioSetup()


    def audioSetup(self):
        # 使用するたまごマイクの設定
        for num in range(1, self.numUseChannel):
            self.streams[num] = (
                    self.audio.open(
                    format = self.FORMAT,
                    channels = num,
                    rate = self.Rate,
                    input = True,
                    #input_device_index = self.device_index,
                    frames_per_buffer = self.chunk
                )
            )
        
        # 使用するたまごマイクが格納されているかの
        # print(self.streams)

        self.processSetup()


    # 複数プロセスの設定
    def processSetup(self):
        # デバッグ
        #for num in range(1, 9):
        #    process = Process(target=self.Power, args=(num, ))
        #    process.start()

        for num in range(1, self.numUseChannel):
            process = Process(target=self.readWave, args=(self.streams[num], ))
            process.run()
            process.terminate()

    # デバッグ用
    def Power(self, num):
        for i in range(1, num):
            for j in range(1, num):
                for k in range(1, num):
                    print(i*j*k)


    # 波形読み込み
    def readWave(self, stream):
        while True:
            #print(stream.read(1024))
            num_data=fromstring(stream.read(1024), dtype='int16')/32768.0
            print(num_data)


if __name__ == "__main__":
    test = SearchSoundSource(8)
