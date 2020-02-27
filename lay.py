# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 22:09:46 2019

@author: sunwf1114
"""
# import tensorflow as tf
from tensorflow import keras
from tensorflow import nn
#3层
def get_threelaiers():
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(90, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(1, activation=nn.relu))
    return model

#4层
def get_fourlaiers():
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(90, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(1, activation=nn.relu))
    return model

#5层
def get_fivelaiers():
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(90, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(1, activation=nn.relu))
    return model
#6层
def get_sixlaiers():
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(90, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(1, activation=nn.relu))
    return model
#7层
def get_sevenlaiers():
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(90, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(1, activation=nn.relu))
    return model
#8层
def get_eightlaiers():
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(90, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(1, activation=nn.relu))
    return model
#9层
def get_ninelaiers():
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(90, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(1, activation=nn.relu))
    return model
#10层
def get_tenlaiers():
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(90, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(1, activation=nn.relu))
    return model
#3层
def get_default():
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(90, activation=nn.relu))
    model.add(keras.layers.Dense(40, activation=nn.relu))
    model.add(keras.layers.Dense(1, activation=nn.relu))
    return model

