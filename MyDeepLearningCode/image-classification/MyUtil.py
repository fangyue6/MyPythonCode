# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 10:23:15 2017

@author: admin
"""
import random
import cv2
import os
import numpy as np
from sklearn.cross_validation import train_test_split
from keras import backend as K
from keras.utils import np_utils
class MyUtil:
    def __init__(self,train_path_name,test_path_name,img_width=150,img_height=150):
        #训练集
        self.train_images = None
        self.train_labels = None
        
        #验证集
        self.valid_images = None
        self.valid_labels = None
        
        #测试集
        self.test_images  = None            
        self.test_labels  = None
        
        #标签
        self.labelsInfo = None
        
        #数据集加载路径
        self.train_path_name    = train_path_name
        self.test_path_name    = test_path_name
        
        #当前库采用的维度顺序
        self.input_shape = None
        
        self.img_width = img_width
        self.img_height = img_height
        
    #按照指定图像大小调整尺寸
    def resize_image(self,image, height = 150, width = 150):
        height = self.img_height
        width = self.img_width
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
    
    def load_data(self,train_data_dir,nb_train_samples):
        manys = os.listdir(train_data_dir)
        num = 0
        data = np.empty((nb_train_samples,self.img_width, self.img_height,3),dtype="float32")
        label = np.empty((nb_train_samples,),dtype="uint8")
    #    nclass = len(manys)
        labelInfo = []
        for i in range(len(manys)):
            imgs = os.listdir(train_data_dir+'/'+manys[i])
            labelInfo.append(manys[i])
            for j in range(len(imgs)):
                img = cv2.imread(train_data_dir+'/'+manys[i]+"/"+imgs[j])
                arr = np.asarray(self.resize_image(img),dtype="float32")
                data[num,:,:,:] = arr
                label[num] = int(i)
                num=num+1
            
        return data,label,labelInfo
    #加载数据集并按照交叉验证的原则划分数据集并进行相关预处理工作
    def load(self, img_channels = 3, nb_classes = 2,
             nb_train_samples=2000,
             nb_test_samples=800):
        img_rows = self.img_width
        img_cols = self.img_height
        #加载数据集到内存
        images, labels, labelsInfo = self.load_data(self.train_path_name,nb_train_samples)        
        
        train_images, valid_images, train_labels, valid_labels = train_test_split(images, labels, test_size = 0.3, random_state = random.randint(0, 100))        
        
        test_images, test_labels, _ = self.load_data(self.test_path_name,nb_test_samples)
#        _, test_images, _, test_labels = train_test_split(images, labels, test_size = 0.5, random_state = random.randint(0, 100))                
        
        #当前的维度顺序如果为'th'，则输入图片数据时的顺序为：channels,rows,cols，否则:rows,cols,channels
        #这部分代码就是根据keras库要求的维度顺序重组训练数据集
        if K.image_dim_ordering() == 'th':
            train_images = train_images.reshape(train_images.shape[0], img_channels, img_rows, img_cols)
            valid_images = valid_images.reshape(valid_images.shape[0], img_channels, img_rows, img_cols)
            test_images = test_images.reshape(test_images.shape[0], img_channels, img_rows, img_cols)
            self.input_shape = (img_channels, img_rows, img_cols)            
        else:
            train_images = train_images.reshape(train_images.shape[0], img_rows, img_cols, img_channels)
            valid_images = valid_images.reshape(valid_images.shape[0], img_rows, img_cols, img_channels)
            test_images = test_images.reshape(test_images.shape[0], img_rows, img_cols, img_channels)
            self.input_shape = (img_rows, img_cols, img_channels)            
            
            #输出训练集、验证集、测试集的数量
            print(train_images.shape[0], 'train samples')
            print(valid_images.shape[0], 'valid samples')
            print(test_images.shape[0], 'test samples')
        
            #我们的模型使用categorical_crossentropy作为损失函数，因此需要根据类别数量nb_classes将
            #类别标签进行one-hot编码使其向量化，在这里我们的类别只有两种，经过转化后标签数据变为二维
            train_labels = np_utils.to_categorical(train_labels, nb_classes)                        
            valid_labels = np_utils.to_categorical(valid_labels, nb_classes)            
            test_labels = np_utils.to_categorical(test_labels, nb_classes)                        
        
            #像素数据浮点化以便归一化
            train_images = train_images.astype('float32')            
            valid_images = valid_images.astype('float32')
            test_images = test_images.astype('float32')
            
            #将其归一化,图像的各像素值归一化到0~1区间
            train_images /= 255
            valid_images /= 255
            test_images /= 255            
        
            self.train_images = train_images
            self.valid_images = valid_images
            self.test_images  = test_images
            self.train_labels = train_labels
            self.valid_labels = valid_labels
            self.test_labels  = test_labels
            self.labelsInfo   = labelsInfo