'''
DCGAN on MNIST using Keras
Author: Rowel Atienza
Project: https://github.com/roatienza/Deep-Learning-Experiments
Dependencies: tensorflow 1.0 and keras 2.0
Usage: python3 dcgan_mnist.py
'''

import numpy as np
import time
import cv2
import os
from tensorflow.examples.tutorials.mnist import input_data

from keras.models import Sequential 
from keras.layers import Dense, Activation, Flatten, Reshape
from keras.layers import Conv2D, Conv2DTranspose, UpSampling2D
from keras.layers import LeakyReLU, Dropout
from keras.layers import BatchNormalization
from keras.optimizers import Adam, RMSprop

import matplotlib.pyplot as plt
#按照指定图像大小调整尺寸
def resize_image(image, height = 150, width = 150):
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
class ElapsedTimer(object):
    def __init__(self):
        self.start_time = time.time()
    def elapsed(self,sec):
        if sec < 60:
            return str(sec) + " sec"
        elif sec < (60 * 60):
            return str(sec / 60) + " min"
        else:
            return str(sec / (60 * 60)) + " hr"
    def elapsed_time(self):
        print("Elapsed: %s " % self.elapsed(time.time() - self.start_time) )

class DCGAN(object):
    def __init__(self, img_rows=28, img_cols=28, channel=1):

        self.img_rows = img_rows
        self.img_cols = img_cols
        self.channel = channel
        self.D = None   # discriminator
        self.G = None   # generator
        self.AM = None  # adversarial model
        self.DM = None  # discriminator model

    # (W−F+2P)/S+1
    def discriminator(self):
        if self.D:
            return self.D
        self.D = Sequential()
        depth = 64
        dropout = 0.4
        
        #SAME for padding
        #out_width = ceil(float(in_width)/float(strides[2]))
        
        #VALID for padding
        #out_width = ceil(float(in_width - filter_width + 1)/float(strides[2]))
        
        # In: 28 x 28 x 1, depth = 1
        # Out: 10 x 10 x 1, depth=64
        
        # my comment   
        # out_width = ceil(28 / 2) = 14
        # Out: 14 x 14 x 1, depth=64
        input_shape = (self.img_rows, self.img_cols, self.channel)
        self.D.add(Conv2D(depth*1, 5, strides=2, input_shape=input_shape,\
            padding='same', activation=LeakyReLU(alpha=0.2)))
        self.D.add(Dropout(dropout))

        # my comment  
        # In: 14*14*1  depth = 64
        # Out: 7 x 7 x 1, depth=128
        # out_width = ceil(14 / 2) = 7
        self.D.add(Conv2D(depth*2, 5, strides=2, padding='same',\
                activation=LeakyReLU(alpha=0.2)))
        self.D.add(Dropout(dropout))

        
        # my comment  
        # In: 7*7*1  depth = 128
        # Out: 4 x 4 x 1, depth=256
        # out_width = ceil(7 / 2) = 4
        self.D.add(Conv2D(depth*4, 5, strides=2, padding='same',\
                activation=LeakyReLU(alpha=0.2)))
        self.D.add(Dropout(dropout))

        
        # my comment  
        # In: 4*4*1  depth = 256
        # Out: 4 x 4 x 1, depth=512
        # out_width = ceil(4 / 1) = 4
        self.D.add(Conv2D(depth*8, 5, strides=1, padding='same',\
                activation=LeakyReLU(alpha=0.2)))
        self.D.add(Dropout(dropout))

        # Out: 1-dim probability
        self.D.add(Flatten())
        self.D.add(Dense(1))
        self.D.add(Activation('sigmoid'))
        self.D.summary()
        return self.D

    def generator(self):
        if self.G:
            return self.G
        self.G = Sequential()
        dropout = 0.4
        depth = 64+64+64+64
#        dim = 7 
        dim = 20
        # In: 100
        # Out: dim x dim x depth
        self.G.add(Dense(dim*dim*depth, input_dim=100))
        self.G.add(BatchNormalization(momentum=0.9))
        self.G.add(Activation('relu'))
        self.G.add(Reshape((dim, dim, depth)))
        self.G.add(Dropout(dropout))

        # In: dim x dim x depth   7*7*256
        # Out: 2*dim x 2*dim x depth/2  14*14*128
        self.G.add(UpSampling2D()) #size=(2, 2)  Repeats the rows and columns of the data by size[0] and size[1] respectively.
        self.G.add(Conv2DTranspose(int(depth/2), 5, padding='same'))#filters: Integer, the dimensionality of the output space 
        self.G.add(BatchNormalization(momentum=0.9))
        self.G.add(Activation('relu'))

        #my comment
        # In: 2*dim x 2*dim x depth/2    14*14*128
        # Out: 4*dim x 4*dim x depth/4   28*28*64
        self.G.add(UpSampling2D())
        self.G.add(Conv2DTranspose(int(depth/4), 5, padding='same'))
        self.G.add(BatchNormalization(momentum=0.9))
        self.G.add(Activation('relu'))

        #my comment
        # In: 4*dim x 4*dim x depth/4    28*28*64
        # Out: 4*dim x 4*dim x depth/8   28*28*32
        self.G.add(Conv2DTranspose(int(depth/8), 5, padding='same'))
        self.G.add(BatchNormalization(momentum=0.9))
        self.G.add(Activation('relu'))
        
        
        #my comment
        # In: 4*dim x 4*dim x depth/8    28*28*32
        # Out: 4*dim x 4*dim x 1         28*28*1

        # Out: 28 x 28 x 1 grayscale image [0.0,1.0] per pix
        print(self.channel)
        self.G.add(Conv2DTranspose(self.channel, 5, padding='same'))
        self.G.add(Activation('sigmoid'))
        self.G.summary()
        return self.G

    def discriminator_model(self):
        if self.DM:
            return self.DM
        optimizer = RMSprop(lr=0.0008, clipvalue=1.0, decay=6e-8)
        self.DM = Sequential()
        self.DM.add(self.discriminator())
        self.DM.compile(loss='binary_crossentropy', optimizer=optimizer,\
            metrics=['accuracy'])
        return self.DM

    def adversarial_model(self):
        if self.AM:
            return self.AM
        optimizer = RMSprop(lr=0.0004, clipvalue=1.0, decay=3e-8)
        self.AM = Sequential()
        self.AM.add(self.generator())
        self.AM.add(self.discriminator())
        self.AM.compile(loss='binary_crossentropy', optimizer=optimizer,\
            metrics=['accuracy'])
        return self.AM

class MNIST_DCGAN(object):
    
    def load_data(self,data_dir):
        manys = os.listdir(data_dir)
        num = len(manys)
        data = np.empty((num,self.img_rows, self.img_cols,self.channel),dtype="float32")
        for i in range(num):
            img = cv2.imread(data_dir + "/"+ manys[i])
            arr = np.asarray(resize_image(img,
                                          height = self.img_rows,
                                          width = self.img_cols),dtype="float32")
            data[i,:,:,:] = arr
        return data
        
    
    def __init__(self):
        self.img_rows = 80#28
        self.img_cols = 80#28
        self.channel = 3#1

        '''
        self.x_train = input_data.read_data_sets("mnist",\
                one_hot=True).train.images
        self.x_train = self.x_train.reshape(-1, self.img_rows,\
                self.img_cols, 1).astype(np.float32)
        '''
        
        '''
        img = cv2.imread('cat.9.jpg')
        img = cv2.resize(img,(80,80))
        shapes = img.shape
        self.x_train = np.reshape(img,[1,80,80,3])
        self.img_rows = shapes[0]
        self.img_cols = shapes[1]
        self.channel  = shapes[2]
        '''

        self.x_train = self.load_data('data/cat')
#        self.x_train = self.x_train.reshape(-1, self.img_rows,\
#                self.img_cols, self.channel).astype(np.float32)
        
        self.DCGAN = DCGAN(img_rows = self.img_rows,
                           img_cols = self.img_cols,
                           channel = self.channel)
        self.discriminator =  self.DCGAN.discriminator_model()
        self.adversarial = self.DCGAN.adversarial_model()
        self.generator = self.DCGAN.generator()

        '''
        self.x_train = self.x_train[1:1000,:,:,:]

        print(self.x_train.shape)
        print(self.x_train.shape[0])
        '''
    
    def train(self, train_steps=2000, batch_size=256, save_interval=0):
        noise_input = None
        if save_interval>0:
            noise_input = np.random.uniform(-1.0, 1.0, size=[16, 100])#16*100
        for i in range(train_steps):
            images_train = self.x_train[np.random.randint(0,
                self.x_train.shape[0], size=batch_size), :, :, :]#256*28*28*1  0到x_train.shape[0]之间的数
            print(images_train.shape)
            noise = np.random.uniform(-1.0, 1.0, size=[batch_size, 100])#256*100
            images_fake = self.generator.predict(noise)#256*28*28*1
            print(images_fake.shape)
            x = np.concatenate((images_train, images_fake)) # 512*28*28*1
            y = np.ones([2*batch_size, 1]) # 512*1
            y[batch_size:, :] = 0
            d_loss = self.discriminator.train_on_batch(x, y)#len(d_loss)=2

            y = np.ones([batch_size, 1])#256*1
            noise = np.random.uniform(-1.0, 1.0, size=[batch_size, 100])#256*100
            a_loss = self.adversarial.train_on_batch(noise, y) #len(a_loss)=2

            log_mesg = "%d: [D loss: %f, acc: %f]" % (i, d_loss[0], d_loss[1])
            log_mesg = "%s  [A loss: %f, acc: %f]" % (log_mesg, a_loss[0], a_loss[1])
            print(log_mesg)
            if save_interval>0:
                if (i+1)%save_interval>-1:#==0
                    self.plot_images(save2file=True, samples=noise_input.shape[0],\
                        noise=noise_input, step=(i+1))
                    

    def plot_images(self, save2file=False, fake=True, samples=16, noise=None, step=0):
        filename = 'mnist.png'
        if fake:
            if noise is None:
                noise = np.random.uniform(-1.0, 1.0, size=[samples, 100])#16*100
            else:
                filename = "mnist_%d.png" % step
            images = self.generator.predict(noise)
        else:
            i = np.random.randint(0, self.x_train.shape[0], samples)
            images = self.x_train[i, :, :, :]

        #print(images.shape)#16 28 28 1
        plt.figure(figsize=(10,10))
        for i in range(images.shape[0]):
            plt.subplot(4, 4, i+1)
            image = images[i, :, :, :]
            print(image.shape)
            #image = np.reshape(image, [self.img_rows, self.img_cols])
            plt.imshow(image, cmap='gray')
            plt.axis('off')
        plt.tight_layout()
        if save2file:
            plt.savefig(filename)
            plt.close('all')
        else:
            plt.show()

if __name__ == '__main__':
    mnist_dcgan = MNIST_DCGAN()
    timer = ElapsedTimer()
    mnist_dcgan.train(train_steps=5, batch_size=2, save_interval=500)#10000 256
#    timer.elapsed_time()
#    mnist_dcgan.plot_images(fake=True)
#    mnist_dcgan.plot_images(fake=False, save2file=True)