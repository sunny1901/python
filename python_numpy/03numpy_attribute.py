"""
Numpy 对象的属性
- np.size 数组的大小
- np.itemsize 对象空间大小
- np.flags 对象的内存信息
- np.ndim 维度的数量
- np.shape 数组的维度，对于矩阵， n 行 m 列
- np.real 元素的实部
"""

import numpy as np

arr = np.arange(6)
print(arr)
print( ".size 数组的大小" , arr.size )
print( ".itemsize 对象空间大小（int）" , arr.itemsize )

# 数组的 dtype 为 int8（一个字节）
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print( ".itemsize 对象空间大小（int8）" , x.itemsize)

# 数组的 dtype 现在为 float64（八个字节）
y = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print( ".itemsize 对象空间大小（float64）" , y.itemsize)

print( ".flags 对象的内存信息  \n" , x.flags)

print(".ndim 数组轴的数量 np.array(3)")
arr = np.array(3)
print("ndim=" ,arr.ndim)

print(".ndim 数组轴的数量 np.array([3])")
arr = np.array([3])
print("ndim=" , arr.ndim)

print(".ndim 数组轴的数量 np.arange(6)")
arr = np.arange(6)
print(arr)
print(arr.ndim)

print(".ndim 数组轴的数量 np.arange(0,24 )")
arr = np.arange(0,24 )
print(arr)
print(arr.ndim)

print(".ndim 数组轴的数量  arr.reshape(2,4,3)")
arr = arr.reshape(2,4,3)
print(arr)
print(arr.ndim)


print(".shape 数组的维度 arr.shape ")
print(arr.shape)

print(".shape 数组维度 arr.shape ")
arr = np.array([ [1,2,3] , [4,5,6]])
print(arr)

print( ".shape 数组维度，变换 arr.shape = (3,2)" )
arr.shape = (3,2)
print(arr)


print( ".reshape 数组维度，变换 arr.reshape( 2, 3 )" )
b = arr.reshape( 2, 3 )
print(b)


