# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 10:19:38 2017

@author: admin
"""

import numpy as np 
import cv2
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    # 从摄像头读取一帧，ret是表明成功与否
    ret, frame = cap.read() 
#    cap.set(3,200)
#    cap.set(4,200)
    print("%g*%g"%(cap.get(3),cap.get(4)))
    if ret:
        #处理得到的帧，这里0将其翻转
#        frame = cv2.flip(frame,0)
        frame = cv2.flip(frame,1)
#        cv2.imshow('frame',frame)
        cv2.imshow('image',frame)
    else:
        break
    # 监听键盘，按下q键退出
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 
##释放
cap.release()
cv2.destroyAllWindows()