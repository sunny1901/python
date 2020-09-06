import numpy as np
"""
数组创建
"""

"""
数组创建
A 一维数组
B 多维度数组

numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
"""

# A1 base
arr = np.array([1,2,3])

print(arr)
print(arr[1])

# A2 dtype
arr = np.array([1,2,3] , dtype=complex)
print(arr)

# A2 zeros

arr = np.zeros(10)
print(arr)

# B1

arr1 = np.array([
        [1,2] ,
        [3,4]
])
print(arr1)
print(arr1[1][1])

# B2 最小维度
arr1 = np.array([1,2,3,4,5,6] , ndmin = 1)
arr2 = np.array([1,2,3,4,5,6] , ndmin = 2)

print(arr1)
print(arr2)

