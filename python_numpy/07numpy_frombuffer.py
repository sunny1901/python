import numpy as np

info = """
从流的中创建数组（动态数组创建）

numpy.frombuffer(buffer,           可以是任意对象，会以流的形式读入。 buffer 是字符串的时候，Python3 默认 str 是 Unicode 类型，所以要转成 bytestring 在原 str 前加上 b。
                dtype = float,     返回数组的数据类型，可选  
                count = -1,        读取的数据数量，默认为-1，读取所有数据。 
                offset = 0         读取的起始位置，默认为0。  
)
"""


str = b'Hello Sunny'
arr = np.frombuffer( str , dtype='S1' )
print( arr )


str1 = 'Hello Sunny2'
print (type(str1))
arr = np.frombuffer( str1   )
print( arr )


