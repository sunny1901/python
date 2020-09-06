import numpy as np

info = """
从迭代器中，创建数组
numpy.fromiter(iterable,        迭代器输入 
            dtype,              返回，数据类型
            count=-1            读取数量
)
"""

list = np.arange( 5 )

it = iter( list )

arr = np.fromiter( it , dtype=float , count=3 )

print( arr )