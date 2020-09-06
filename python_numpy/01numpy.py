import numpy as np
"""
数组创建
"""

"""
数组创建

numpy.array(
        object, 
        dtype = None,   数据类型
        copy = True,    对象是否需要复制        
        order = None,   数组样式， C行，F列，A任意（默认）
        subok = False,  默认返回一个与基类类型一致的数组
        ndmin = 0 ，    指定生成数组的最小维度
)
        

A 一维数组，创建
B 多维度数组，创建
"""

"""
一维数组
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


"""
多维数组
"""

# B2 最小维度
arr1 = np.array([1,2,3,4,5,6] , ndmin = 1 , order = 'F')
arr2 = np.array([1,2,3,4,5,6] , ndmin = 2)
print("  多维数组。。。。。。。。。。 ")
print(arr1)
print(arr2)

