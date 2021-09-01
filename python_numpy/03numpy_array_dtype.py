import numpy as np

info = """
数据类型
numpy.dtype(object, 
            align, 
            copy
)
https://www.runoob.com/numpy/numpy-dtype.html
"""
print( info )

dt = np.dtype( np.int32 )
print(dt)

dt = np.dtype( np.int64 )
print(dt)

info = """
# 简写形式
# int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
        b	    布尔型
        i	    (有符号) 整型
        u	    无符号整型 integer （正整形）
        f	    浮点型
        c	    复数浮点型
        m	    timedelta（时间间隔）
        M	    datetime（日期时间）
        O	    (Python) 对象
        S, a	(byte-)字符串
        U	    Unicode
        V	    原始数据 (void)
"""
print(info)

dt = np.dtype( "i1")
print(dt)

dt = np.dtype( "i2")
print(dt)

dt = np.dtype( "i4" )
print(dt)

dt = np.dtype( "i8")
print(dt)

dt = np.dtype( "<i4" )
print(dt)

info = """
# B '结构化' 数据类型， 构建
"""
print(info)

dt = np.dtype( [  ('age',np.int8) ] )
print(dt)

arr = np.array([
        (10,),
        (20,),
        (30,)
    ]
    ,dtype=dt
)
print(arr)
print(arr['age'])

student = np.dtype([ ('name','S20'), ( 'age' , 'i1' ), ( 'marks' , 'f4' )  ])
print( student)

arr = np.array( [('xiaoxiao', 11 , 40) ,
           ('xiao2', 22 , 50) ,
           ('xiao3', 33, 60)
          ]
          ,dtype=student )
print(arr)

print(arr['name'])
print(arr['age'])