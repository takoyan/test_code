#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import usb.core
import usb.util
from tuning import Tuning
from time import sleep
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import re
import numpy as np


#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('172.31.141.31', 11451))
s.listen(1)
pub=rospy.init_node('ControlTurtleBot', anonymous=False)
cmd_vel=rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
r=rospy.Rate(10)
twist=Twist()
before_angular=0

while(1):
    #cliant = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #cliant.connect((HOST,PORT))

    conn, addr=s.accept()
    while(1):
        data=conn.recv(1024)
        if not data:
            break
        twist.linear.x=0
        twist.angular.z=float(np.pi*int(data)/180)-before_angular
        before_angular=twist.angular.z
        
        cmd_vel.publish(twist)
        print('data: {}, addr: {}'.format(data, addr))
        #conn.sendall(b'Recived: '+data)
