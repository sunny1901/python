import numpy as np

info = """
创建一个指定形状shape，的空数组
numpy.empty(shape, dtype = float, order = 'C')

shape 规定了，数据的矩阵结构
dtype 规定了，数据的类型，可以是对象，元数据
"""
print( info )
arr = np.empty([3,2] , dtype=int)
print( arr )


info = """
numpy.zeros 创建指定大小的数组，数组元素以 0 来填充：
numpy.zeros(shape, 
            dtype = float, 
            order = 'C'
)
"""

print( info )
arr = np.zeros( 5 )
print( ".zerors 默认浮点类型" , arr )

arr = np.zeros( (5,) , dtype=np.int   )
print( ".zerors 结构化" , arr )

arr = np.zeros( (3,2) , dtype=np.int)
print( ".zerors 结构化2  比较 1 !! \n" , arr )
arr = np.zeros( (3,2) , dtype=[( 'x' , int ),])
print( ".zerors 结构化2  比较 2 !! \n" , arr )
arr = np.zeros( (3,2) , dtype=[( 'x' , int ),( 'y' , 'i4')])
print( ".zerors 结构化2  比较 3 !! \n" , arr )