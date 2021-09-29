# -*- coding = utf-8 -*- 
# @Author:SwaggyLv
# @time:2021/9/1 20:11
# @File:Perceptron.py
# @Software:PyCharm

import numpy as np

def AND_1(x1,x2):
    w1,w2,theta = 0.5,0.5,0.7
    temp =w1*x1+w2*x2
    if temp>theta:
        return 1
    elif temp<=theta:
        return 0

#引入偏置值
#与门
def AND(x1,x2):
    x=np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = 0.7
    temp = np.sum(w*x)+b
    if temp > 0:
        return 1
    elif temp <= 0:
        return 0

#与非门
def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = -0.7
    temp = np.sum(w*x) + b
    if temp > 0:
        return 1
    elif temp <= 0:
        return 0

#或门
def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])#权重
    b = -0.2#偏置
    temp = np.sum(w*x) + b
    if temp > 0:
        return 1
    elif temp <= 0:
        return 0

#异或门
def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y



