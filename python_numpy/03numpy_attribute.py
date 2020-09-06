import numpy as np

info = """
Numpy 属性
"""
print(info)

info = """
# .ndim 数组的维度
"""
print( info )

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

info = """
# .shape 数组的维度
"""
print( info )
print(arr.shape)

arr = np.array([ [1,2,3] , [4,5,6]])
print(arr)

info = """
# .shape 进行数组维度，变换
"""
print( info )
arr.shape = (3,2)
print(arr)

info = """
# .reshape 进行数组维度，变换
"""
print( info )
b = arr.reshape( 2, 3 )
print(b)


print( ".size 数组的大小" , arr.size )
print( ".itemsize 对象空间大小" , arr.itemsize )

# 数组的 dtype 为 int8（一个字节）
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print( ".itemsize 对象空间大小" , x.itemsize)

# 数组的 dtype 现在为 float64（八个字节）
y = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print( ".itemsize 对象空间大小" , y.itemsize)

print( ".flags 对象的内存信息  \n" , x.flags)