#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import usb.core
import usb.util
from tuning import Tuning


fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111)
#c = pat.Circle(xy = (0, 0), radius = 1,fc = "white", ec = "blue")
#ax.add_patch(c)
#x_line=(0, 1.5, 0.1)
#y_line=(0, 1.5, 0.1)
#lines, =plt.plot(x_line, y_line)

dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)



while(1):
    Mic_tuning=Tuning(dev)
    theta=np.pi*Mic_tuning.direction/180
    x=np.cos(theta)
    y=np.sin(theta)

    #lines.set_data(x_line, y_line)
    c = plt.Circle(xy = (0, 0), radius = 1,fc = "white", ec = "blue")
    plt.plot([0, x], [0,y], c='red')
    ax.add_patch(c)
    plt.pause(0.01)

