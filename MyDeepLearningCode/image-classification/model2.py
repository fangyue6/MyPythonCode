# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 23:44:03 2017

@author: admin
"""

#import keras
from keras.models import load_model
from keras.models import Sequential
import cv2
import numpy as np 
import os
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
model = Sequential()

model =load_model('my_model4.h5')
model.compile(loss='sparse_categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy']
              )#,class_mode="categorical"
testpath = 'test1'
images = os.listdir(testpath)
for i in range(len(images)):
    img = cv2.imread(testpath+'/'+images[i])
#    print(img.shape)
    img = cv2.resize(img,(150,150))
    #cv2.imshow('image',img)
    img = np.reshape(img,[1,150,150,3])
    classes = model.predict_classes(img)
    print(classes)
    classes = model.predict(img)
    #if(classes==0):
    #	print("it is cat")
    #if(classes==1):
    #	print("it is dog")
#    print(classes)



