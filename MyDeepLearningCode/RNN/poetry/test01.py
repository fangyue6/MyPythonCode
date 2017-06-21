# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 22:00:57 2017

@author: admin
"""

import keras  
  
import numpy as np   
from keras.utils import plot_model  
from keras.preprocessing.image import ImageDataGenerator  
from keras.models import *  
from keras.layers import *  
from keras.callbacks import *  
from keras import backend as K  
from keras.utils import np_utils
import h5py  
  
filename = "input.txt"  
raw_text = open(filename,'r', encoding='UTF-8').read()  
raw_text = raw_text.lower()  
  
chars = sorted(list(set(raw_text)))  
char_to_int = dict((c, i) for i, c in enumerate(chars))  
int_to_char = dict((i, c) for i, c in enumerate(chars))  
  
n_chars = len(raw_text)  
n_vocab = len(chars)  
  
print ('vocal: ',n_vocab)  
# data = open('input.txt','r').read()  
# data=data.lower()  
#上面基本都是仿照课堂上老师给的源码  
seq_length = 32  
dataX = []  
dataY = []  
for i in range(0, n_chars - seq_length, 1):  
    seq_in = raw_text[i:i + seq_length]  
    seq_out = raw_text[i + seq_length]  
    dataX.append([char_to_int[char] for char in seq_in])  
    dataY.append(char_to_int[seq_out])  
  
n_patterns = len(dataX)  
  
print ("Total Patterns: ", n_patterns)  
  
#处理数据，后端不同维度顺序修改
if K.image_dim_ordering() == 'th':
    X = np.reshape(dataX, (1, n_patterns, seq_length))
else:
    X = np.reshape(dataX, (n_patterns, seq_length, 1))  
    
# reshape X to be [samples, time steps, features]  
#X = np.reshape(dataX, (n_patterns, seq_length, 1))  

# X = X / n_vocab #归一化后效果不好  
#下面可以用函数直接转成多元分类的 ，例如:valY = np_utils.to_categorical(valY, num_classes=NUM_CLASS)  
#Y = []  
#for i in range(n_patterns):  
#    y = np.zeros((n_vocab, 1))  
#    y[dataY[i]] = 1  
#    Y.append(y)  
#Y = np.reshape(Y, (n_patterns, n_vocab))  
Y = np_utils.to_categorical(dataY, num_classes=n_vocab)




print(X.shape)  
print (Y.shape)  
  
#设置检查点，保存权重  
filepath="weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"  
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')  
callbacks_list = [checkpoint]  
  
  
model = Sequential()  
model.add(LSTM(64, input_shape=(X.shape[1], X.shape[2]),return_sequences=True))  
# # model.add(LSTM(32,return_sequences=True))  
# model.add(LSTM(8))  
  
# model.add(LSTM(  
#     batch_input_shape=(None, TIME_STEPS, INPUT_SIZE),       # Or: input_dim=INPUT_SIZE, input_length=TIME_STEPS,  
#     output_dim=CELL_SIZE,  
#     return_sequences=True,      # True: output at all steps. False: output as last step.  
#     stateful=True,              # True: the final state of batch1 is feed into the initial state of batch2  
# ))  
  
# model.add(Dropout(0.2))  
  
  
model.add(Dense(n_vocab))  
model.add(Activation('softmax'))  
adam=keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08)  
adagrad=keras.optimizers.Adagrad(lr=0.001, epsilon=1e-06)  
model.compile(loss='categorical_crossentropy', optimizer='adam',metrics=['accuracy'])  
  
print (model.layers[1].input)  #use the index of layer to find the input and output shape  
print (model.layers[1].output)  
model.summary()  

#plot_model(model, to_file='model.png')  
#plot(model, to_file='model1.png',show_shapes=True)
#尝试过多层rnn和单层不同宽度，效果都不怎么好，而且收敛很慢，而且这样的实现和老师的代码算法上还是有很大区别的，最终效果loss在0.1以下会生产一些单词，句子基本不可读  
#model.fit(X, Y, nb_epoch=20, batch_size=128, callbacks=callbacks_list)  
model.fit(X, Y, epochs=500, batch_size=64)  
#model.save('word_pre.h5')  