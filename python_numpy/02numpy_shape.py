import numpy as np


info = """
# .shape 数组的矩阵结构 , 矩阵变换
"""

arr = np.array([3])
print("维度" ,arr.ndim  , arr)
print("矩阵结构" ,arr.shape )

arr = np.array(3)
print("维度" ,arr.ndim  , arr )
print("矩阵结构" ,arr.shape )

arr = np.arange(6)
print("维度" ,arr.ndim  , arr )
print("矩阵结构" ,arr.shape )

arr.shape = (3,2)
print("# 结构变换" , arr)
print("维度" ,arr.ndim )
print("矩阵结构" ,arr.shape )


b = arr.reshape( 2, 3 )
print("# 结构变换2" , arr)
print("维度" ,arr.ndim )
print("矩阵结构" ,arr.shape )