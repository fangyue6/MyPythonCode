# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 18:29:39 2017

@author: admin
"""

import os
from PIL import Image
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
# from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.advanced_activations import PReLU
# from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import SGD, Adadelta, Adagrad
from keras.utils import np_utils, generic_utils
from six.moves import range

from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense

from keras import backend as K
import cv2

nb_train_samples = 4000
nb_validation_samples = 1600
img_width, img_height = 150, 150
nclass = 4;#类别数量

train_data_dir = 'data1/train'
validation_data_dir = 'data1/validation'
epochs = 50
batch_size = 16


print(K.image_data_format())
if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

#按照指定图像大小调整尺寸
def resize_image(image, height = img_width, width = img_height):
    top, bottom, left, right = (0, 0, 0, 0)
    
    #获取图像尺寸
    h, w, _ = image.shape
    
    #对于长宽不相等的图片，找到最长的一边
    longest_edge = max(h, w)    
    
    #计算短边需要增加多上像素宽度使其与长边等长
    if h < longest_edge:
        dh = longest_edge - h
        top = dh // 2
        bottom = dh - top
    elif w < longest_edge:
        dw = longest_edge - w
        left = dw // 2
        right = dw - left
    else:
        pass 
    
    #RGB颜色
    BLACK = [0, 0, 0]
    
    #给图像增加边界，是图片长、宽等长，cv2.BORDER_CONSTANT指定边界颜色由value指定
    constant = cv2.copyMakeBorder(image, top , bottom, left, right, cv2.BORDER_CONSTANT, value = BLACK)
    
    #调整图像大小并返回
    return cv2.resize(constant, (height, width))

def load_data():
    manys = os.listdir(train_data_dir)
    num = 0
    data = np.empty((nb_train_samples,img_width, img_height,3),dtype="float32")
    label = np.empty((nb_train_samples,),dtype="uint8")
#    nclass = len(manys)
    labelInfo = []
    for i in range(len(manys)):
        imgs = os.listdir(train_data_dir+'/'+manys[i])
        labelInfo.append(manys[i])
        for j in range(len(imgs)):
            img = cv2.imread(train_data_dir+'/'+manys[i]+"/"+imgs[j])
            arr = np.asarray(resize_image(img),dtype="float32")
            data[num,:,:,:] = arr
            label[num] = int(i)
            num=num+1
        
    return data,label,labelInfo
    
def load_testData(test_file_path):
    testImg = cv2.imread(test_file_path)
    imgArr = np.asarray(resize_image(testImg),dtype="float32")
    # print(imgArr.shape)
    testData = np.empty((1,img_width, img_height, 3),dtype="float32")
    testData[0,:,:,:] = imgArr
    return testData
    



if __name__ == '__main__':
    testData = load_testData('save/fangyue/validation/1016.jpg')
    
    #保存模型数据的文件
    modelfilename = 'model/cat_dog_fang_li.h5'
    
    #加载数据
    data, label, _ = load_data()
    labelInfo = ['liyonggang', 'fangyue', 'dogs', 'cats']
    print(data.shape[0], ' samples')
    
    #label为nclass个类别，转化格式
    print(label.shape)
    label = np_utils.to_categorical(label, nclass)
    print(label.shape)
    
    ###############
    #开始建立CNN模型
    ###############
    
    #生成一个model
    model = Sequential()
    
    #第一个卷积层，4个卷积核，每个卷积核大小5*5。1表示输入的图片的通道,灰度图为1通道。
    #激活函数用tanh
    #你还可以在model.add(Activation('tanh'))后加上dropout的技巧: model.add(Dropout(0.5))
    # model.add(Convolution2D(nb_filter=4,nb_row=5,nb_col=5,border_mode='valid',input_shape=(1,28,28))) 
    model.add(Conv2D(4, (5, 5), border_mode='valid',input_shape=input_shape))
    model.add(Activation('tanh'))
    
    #第二个卷积层，8个卷积核，每个卷积核大小3*3。4表示输入的特征图个数，等于上一层的卷积核个数
    # model.add(Convolution2D(nb_filter=8,nb_row=3,nb_col=3,border_mode='valid')) 
    model.add(Conv2D(8, (3, 3), border_mode='valid'))
    model.add(Activation('tanh'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    #第三个卷积层，16个卷积核，每个卷积核大小3*3
    # model.add(Convolution2D(nb_filter=16,nb_row=3,nb_col=3,border_mode='valid')) 
    model.add(Conv2D(16, (3, 3), border_mode='valid'))
    model.add(Activation('tanh'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    #全连接层，先将前一层输出的二维特征图flatten为一维的。
    #Dense就是隐藏层。16就是上一层输出的特征图个数。4是根据每个卷积层计算出来的：(28-5+1)得到24,(24-3+1)/2得到11，(11-3+1)/2得到4
    model.add(Flatten())
    model.add(Dense(128))
    model.add(Activation('tanh'))
    
    #Softmax分类，输出是nclass类别
    model.add(Dense(nclass))
    model.add(Activation('softmax'))
    
    #############
    #开始训练模型
    ##############
    model.compile(loss='categorical_crossentropy',
                  optimizer='adadelta',
                  class_mode="categorical",
                  metrics=["accuracy"])
    
    #validation_split=0.2，将20%的数据作为验证集。
    
    f = os.path.exists(modelfilename)
    if f == False:
        print('Training................')
        # model.fit(data, label, batch_size=100,nb_epoch=1,shuffle=True,verbose=1,show_accuracy=True,validation_split=0.2)
        model.fit(data, label, 
                  batch_size=nb_train_samples // batch_size,
                  epochs=epochs,
                  shuffle=True,
                  verbose=1,
                  validation_split=0.2)
        model.save(modelfilename)
    else:
        print('Loading Data............')
        model.load_weights(modelfilename)
    #数据测试
    #print(labelInfo)
    print(model.predict(testData))
    classes = model.predict_classes(testData)
    print(classes)
    print(labelInfo[classes[0]])





    
    