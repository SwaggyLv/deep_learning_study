# -*- coding = utf-8 -*- 
# @Author:SwaggyLv
# @time:2021/9/6 20:23
# @File:Nerual_Network.py
# @Software:PyCharm

import numpy as np
import matplotlib.pylab as plt
import os


#阶跃函数1
def step_function_1(x):
    y = x > 0
    return y.astype(np.int)

#阶跃函数2
def step_function(x):
    return np.array(x>0,dtype=np.int)

os.system('export DISPLAY=:0.0')
#阶跃函数图像
# x = np.arange(-5,5,0.1)
# y = step_function(x)
# plt.plot(x,y)
# plt.ylim(-0.1,1.1)
# plt.show()

def sigmoid(x):
    return 1/(1+np.exp(-x))

#sigmoid函数图像
# x = np.arange(-5,5,0.1)
# y = sigmoid(x)
# plt.plot(x,y)
# plt.ylim(-0.1,1.1)
# plt.show()

def relu(x):
    return np.maximum(0,x)

#ReLu函数图像
# x = np.arange(-6,6,0.1)
# y = relu(x)
# plt.plot(x,y)
# plt.ylim(-1,6)
# plt.show()