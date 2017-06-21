# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 12:58:03 2017

@author: admin
"""

import cv2
import sys
import os
from script_1_3 import Model
from voice import BaiduRest
import pygame

miniSize = 128  #32
if __name__ == '__main__':
#    if len(sys.argv) != 2:
#        print("Usage:%s camera_id\r\n" % (sys.argv[0]))
#        sys.exit(0)
        
    #加载模型
    model = Model()
    model.load_model(file_path = 'model/data3.fang.lei.yang.model.h5')   
    labelInfo = ['yanglifeng', 'fangyue', 'leicong']
              
    #框住人脸的矩形边框颜色       
    color = (0, 255, 0)
    
    #捕获指定摄像头的实时视频流
#    cap = cv2.VideoCapture(int(sys.argv[1]))
    cap = cv2.VideoCapture(0)
    
    #人脸识别分类器本地存储路径   OpenCV/haarcascades/haarcascade_frontalface_alt2.xml
    cascade_path = "haarcascade_frontalface_alt2.xml"   
    
    #百度语音播放
    bdr = BaiduRest()
    
    voicetime=0
    pygame.mixer.init()
    
    #循环检测识别人脸
    while True:
        _, frame = cap.read()   #读取一帧视频
        
        #图像灰化，降低计算复杂度
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        #使用人脸识别分类器，读入分类器
        cascade = cv2.CascadeClassifier(cascade_path)                

        #利用分类器识别出哪个区域为人脸
        faceRects = cascade.detectMultiScale(frame_gray, scaleFactor = 1.2, minNeighbors = 3, minSize = (miniSize, miniSize))        
        if len(faceRects) > 0:                 
            for faceRect in faceRects: 
                x, y, w, h = faceRect
                
                #截取脸部图像提交给模型识别这是谁
                image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                faceID = model.face_predict(image)   
                print(faceID)
                
                #如果是“我”
                showText = ''
                voicefile = ''
                if faceID == 1:
                    showText = 'fangyue'
                    voicefile = "voice/fangyue.mp3"
                    f = os.path.exists(voicefile)
                    if f==False:
                        bdr.getVoice("他是方月", "voice/fangyue.mp3")
                if faceID == 2:                                                        
                    showText = 'leicong'
                    voicefile = "voice/leicong.mp3"
                    f = os.path.exists(voicefile)
                    if f==False:
                        bdr.getVoice("他是雷聪", voicefile)
                if faceID == 0:
                    showText = 'yanglifeng'
                    voicefile = "voice/yanglifeng.mp3"
                    f = os.path.exists(voicefile)
                    if f==False:
                        bdr.getVoice("他是杨李峰", voicefile)
                if faceID == 3:
                    showText = 'cat'
                    voicefile = "voice/cat.mp3"
                    f = os.path.exists(voicefile)
                    if f==False:
                        bdr.getVoice("他是猫", voicefile)
                if voicetime > 30:
                    voicetime = 0
                    track = pygame.mixer.music.load(voicefile)
                    pygame.mixer.music.play()
                    #pygame.mixer.music.stop()
                    
                voicetime = voicetime+1
                    
#                else:
#                    pass
                
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, thickness = 2)
                    
                #文字提示是谁
                cv2.putText(frame,showText, 
                                (x + 30, y + 30),                      #坐标
                                cv2.FONT_HERSHEY_SIMPLEX,              #字体
                                1,                                     #字号
                                (255,0,255),                           #颜色
                                2)                                     #字的线宽
                            
        cv2.imshow("face", frame)
        
        #等待10毫秒看是否有按键输入
        k = cv2.waitKey(10)
        #如果输入q则退出循环
        if k & 0xFF == ord('q'):
            break

    #释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()
    
    
