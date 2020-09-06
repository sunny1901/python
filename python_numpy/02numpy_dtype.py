import numpy as np

info = """
数据类型
"""

print( info )

dt = np.dtype( np.int32 )
print(dt)

dt = np.dtype( np.int64 )
print(dt)

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

# B 结构化数据构建
dt = np.dtype( [('age',np.int8)] )
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