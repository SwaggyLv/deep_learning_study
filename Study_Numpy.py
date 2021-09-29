import numpy as np

#创建
x=np.array([10,20])#一维
y=np.array([[1,1],[3,4]])#二维

#相同shape的numpy数组可以进行加减乘除

#广播---不同维度的numpy数组也可以进行运算 会对小的numpy数组进行‘扩展’

#访问元素

#转换
y=y.flatten()
print(type(y))#<class 'numpy.ndarray'>

#条件筛选
print(y>2)
print(y[y>2])