import numpy as np

info = """
Numpy 属性
"""

# .ndim

arr = np.array([3])
print(arr.ndim)

arr = np.array(3)
print(arr.ndim)

arr = np.arange(24)
print(arr)
print(arr.ndim)

arr = np.arange(0,24,1)
print(arr)
print(arr.ndim)

arr = arr.reshape(2,4,3)
print(arr)
print(arr.ndim)
print(arr.shape)

arr = np.array([ [1,2,3] , [4,5,6]])
print(arr)

arr.shape = (3,2)
print(arr)

b = arr.reshape( 2, 3 )
print(b)

print( arr.size)
print( arr.itemsize )

# 数组的 dtype 为 int8（一个字节）
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(x.itemsize)

# 数组的 dtype 现在为 float64（八个字节）
y = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print(y.itemsize)

print(x.flags)