# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 18:29:39 2017

@author: admin
"""

from PIL import Image
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
# from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.advanced_activations import PReLU
# from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import SGD, Adadelta, Adagrad
from keras.utils import np_utils, generic_utils

from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.models import load_model

from keras import backend as K
from MyUtil import MyUtil

nb_train_samples = 2000
nb_validation_samples = 800
img_width, img_height = 128, 128
nclass = 2;#类别数量

MODEL_PATH = 'model/fang.li.cat.dog.model.h5'
train_data_dir = 'data1/train'
validation_data_dir = 'data1/validation'
epochs = 50
batch_size = 16


#CNN网络模型类            
class Model:
    def __init__(self):
        self.model = None 
        
    #建立模型
    def build_model(self, dataset, nb_classes = 2):
        #构建一个空的网络模型，它是一个线性堆叠模型，各神经网络层会被顺序添加，专业名称为序贯模型或线性堆叠模型
        self.model = Sequential() 
        
        #以下代码将顺序添加CNN网络需要的各层，一个add就是一个网络层
        self.model.add(Conv2D(32, 3, 3, border_mode='same', 
                                     input_shape = dataset.input_shape))    #1 2维卷积层
        self.model.add(Activation('relu'))                                  #2 激活函数层
        
        self.model.add(Conv2D(32, 3, 3))                             #3 2维卷积层                             
        self.model.add(Activation('relu'))                                  #4 激活函数层
        
        self.model.add(MaxPooling2D(pool_size=(2, 2)))                      #5 池化层
        self.model.add(Dropout(0.25))                                       #6 Dropout层

        self.model.add(Conv2D(64, 3, 3, border_mode='same'))         #7  2维卷积层
        self.model.add(Activation('relu'))                                  #8  激活函数层
        
        self.model.add(Conv2D(64, 3, 3))                             #9  2维卷积层
        self.model.add(Activation('relu'))                                  #10 激活函数层
        
        self.model.add(MaxPooling2D(pool_size=(2, 2)))                      #11 池化层
        self.model.add(Dropout(0.25))                                       #12 Dropout层

        self.model.add(Flatten())                                           #13 Flatten层
        self.model.add(Dense(512))                                          #14 Dense层,又被称作全连接层
        self.model.add(Activation('relu'))                                  #15 激活函数层   
        self.model.add(Dropout(0.5))                                        #16 Dropout层
        self.model.add(Dense(nb_classes))                                   #17 Dense层
        self.model.add(Activation('softmax'))                               #18 分类层，输出最终结果
        
        #输出模型概况
        self.model.summary()
        
    #训练模型
    def train(self, dataset, batch_size = 20, nb_epoch = 10, data_augmentation = True):        
        sgd = SGD(lr = 0.01, decay = 1e-6, 
                  momentum = 0.9, nesterov = True) #采用SGD+momentum的优化器进行训练，首先生成一个优化器对象  
        self.model.compile(loss='categorical_crossentropy',
                           #optimizer=sgd,
                           optimizer='adadelta',
                           metrics=['accuracy'])   #完成实际的模型配置工作
        
        #不使用数据提升，所谓的提升就是从我们提供的训练数据中利用旋转、翻转、加噪声等方法创造新的
        #训练数据，有意识的提升训练数据规模，增加模型训练量
        if not data_augmentation:            
            self.model.fit(dataset.train_images,
                           dataset.train_labels,
                           batch_size = batch_size,
                           nb_epoch = nb_epoch,
                           validation_data = (dataset.valid_images, dataset.valid_labels),
                           shuffle = True)
        #使用实时数据提升
        else:            
            #定义数据生成器用于数据提升，其返回一个生成器对象datagen，datagen每被调用一
            #次其生成一组数据（顺序生成），节省内存，其实就是python的数据生成器
            datagen = ImageDataGenerator(
                featurewise_center = False,             #是否使输入数据去中心化（均值为0），
                samplewise_center  = False,             #是否使输入数据的每个样本均值为0
                featurewise_std_normalization = False,  #是否数据标准化（输入数据除以数据集的标准差）
                samplewise_std_normalization  = False,  #是否将每个样本数据除以自身的标准差
                zca_whitening = False,                  #是否对输入数据施以ZCA白化
                rotation_range = 20,                    #数据提升时图片随机转动的角度(范围为0～180)
                width_shift_range  = 0.2,               #数据提升时图片水平偏移的幅度（单位为图片宽度的占比，0~1之间的浮点数）
                height_shift_range = 0.2,               #同上，只不过这里是垂直
                horizontal_flip = True,                 #是否进行随机水平翻转
                vertical_flip = False)                  #是否进行随机垂直翻转

            #计算整个训练样本集的数量以用于特征值归一化、ZCA白化等处理
            datagen.fit(dataset.train_images)                        

            #利用生成器开始训练模型
            self.model.fit_generator(datagen.flow(dataset.train_images, dataset.train_labels,
                                                   batch_size = batch_size),
                                     samples_per_epoch = dataset.train_images.shape[0],
                                     nb_epoch = nb_epoch,
                                     validation_data = (dataset.valid_images, dataset.valid_labels))
            
    def save_model(self, file_path = MODEL_PATH):
        self.model.save(file_path)

    def load_model(self, file_path = MODEL_PATH):
        self.model = load_model(file_path)
        
    def evaluate(self, dataset):
        score = self.model.evaluate(dataset.test_images, dataset.test_labels, verbose = 1)
        print("%s: %.2f%%" % (self.model.metrics_names[1], score[1] * 100))
        
    #识别人脸
    def face_predict(self, image):   
        dataset = MyUtil(train_data_dir,validation_data_dir,img_width=img_width,img_height=img_height)
        #依然是根据后端系统确定维度顺序
        if K.image_dim_ordering() == 'th' and image.shape != (1, 3, img_width, img_height):
            image = dataset.resize_image(image)                             #尺寸必须与训练集一致都应该是IMAGE_SIZE x IMAGE_SIZE
            image = image.reshape((1, 3, img_width, img_height))   #与模型训练不同，这次只是针对1张图片进行预测    
        elif K.image_dim_ordering() == 'tf' and image.shape != (1, img_width, img_height, 3):
            image = dataset.resize_image(image)
            image = image.reshape((1, img_width, img_height, 3))                    
        
        #浮点并归一化
        image = image.astype('float32')
        image /= 255
        
        #给出输入属于各个类别的概率，我们是二值类别，则该函数会给出输入图像属于0和1的概率各为多少
        result = self.model.predict_proba(image)
        print('result:', result)
        
        #给出类别预测：0或者1
        result = self.model.predict_classes(image)        

        #返回类别预测结果
        return result[0]


if __name__ == '__main__':
    dataset = MyUtil(train_data_dir,validation_data_dir,img_width=img_width,img_height=img_height)
    dataset.load(nb_classes = nclass,
                 nb_train_samples=nb_train_samples,
                 nb_test_samples=nb_validation_samples)
    
    print(dataset.labelsInfo)
    train = 0
    if train==1:
        #训练模型
        model = Model()
        model.build_model(dataset,nb_classes=nclass)
        model.train(dataset,
                    batch_size=batch_size ,
                    nb_epoch = epochs)
        model.save_model()
    else:
        #评估模型
        model = Model()
        model.load_model()
        model.evaluate(dataset)







    
    