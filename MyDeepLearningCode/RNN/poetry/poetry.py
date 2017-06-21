# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 21:30:54 2017

@author: admin
"""

import collections  
import numpy as np  

import keras  
from keras.utils import plot_model  
from keras.preprocessing.image import ImageDataGenerator  
from keras.models import *  
from keras.layers import *  
from keras.callbacks import *  
from keras import backend as K  
import h5py 
#-------------------------------数据预处理---------------------------#  
   
poetry_file ='poetry.txt'  
   
# 诗集  
poetrys = []  
with open(poetry_file, "r", encoding='utf-8',) as f:  
    for line in f:  
        try:  
            title, content = line.strip().split(':')  
            content = content.replace(' ','')  
            if '_' in content or '(' in content or '（' in content or '《' in content or '[' in content:  
                continue  
            if len(content) < 5 or len(content) > 79:  
                continue  
            content = '[' + content + ']'  
            poetrys.append(content)  
        except Exception as e:   
            pass  
   
# 按诗的字数排序  
poetrys = sorted(poetrys,key=lambda line: len(line))  
print('唐诗总数: ', len(poetrys))  
   
# 统计每个字出现次数  
all_words = []  
for poetry in poetrys:  
    all_words += [word for word in poetry]  
counter = collections.Counter(all_words)  
count_pairs = sorted(counter.items(), key=lambda x: -x[1])  
words, _ = zip(*count_pairs)  
   
# 取前多少个常用字  
words = words[:len(words)] + (' ',)  
# 每个字映射为一个数字ID  
word_num_map = dict(zip(words, range(len(words))))  
# 把诗转换为向量形式，参考TensorFlow练习1  
to_num = lambda word: word_num_map.get(word, len(words))  
poetrys_vector = [ list(map(to_num, poetry)) for poetry in poetrys]  

#print(poetrys_vector)
batch_size = 1  
n_chunk = len(poetrys_vector) // batch_size  
x_batches = []  
y_batches = []  
for i in range(n_chunk):  
    start_index = i * batch_size  
    end_index = start_index + batch_size  
   
    batches = poetrys_vector[start_index:end_index]  
    length = max(map(len,batches))  
    xdata = np.full((batch_size,length), word_num_map[' '], np.int32)  
    for row in range(batch_size):  
        xdata[row,:len(batches[row])] = batches[row]  
    ydata = np.copy(xdata)  
    ydata[:,:-1] = xdata[:,1:]  
    """ 
    xdata             ydata 
    [6,2,4,6,9]       [2,4,6,9,9] 
    [1,4,2,8,5]       [4,2,8,5,5] 
    """  
    x_batches.append(xdata)  
    y_batches.append(ydata)  

dataX = x_batches 
dataY = y_batches
n_patterns = len(dataX) 
print ("Total Patterns: ", n_patterns)
seq_length = batch_size
X = np.reshape(dataX, (n_patterns, seq_length, 1))  
Y = [] 
n_vocab = len(words)
for i in range(n_patterns):  
    y = np.zeros((n_vocab, 1))  
    y[dataY[i]] = 1  
    Y.append(y)  
Y = np.reshape(Y, (n_patterns, n_vocab))  
print(Y.shape)

#设置检查点，保存权重  
filepath="weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"  
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')  
callbacks_list = [checkpoint]  
model = Sequential()  
model.add(LSTM(64, input_shape=(X.shape[1], X.shape[2]),return_sequences=True)) 

model.add(Dense(n_vocab,activation='softmax'))  
adam=keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08)  
adagrad=keras.optimizers.Adagrad(lr=0.001, epsilon=1e-06)  
model.compile(loss='categorical_crossentropy', optimizer='adam')  
  
print (model.layers[1].input)  #use the index of layer to find the input and output shape  
print (model.layers[1].output) 
  
plot_model(model, to_file='model.png')  