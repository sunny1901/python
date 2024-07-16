import pandas as pd

a = [1,2,3 ]

# 1. 加入索引
myvar = pd.Series(a)
print( myvar  )


# 2.

a = ['google' , 'runoob' , 'wiki']
b = pd.Series(a , index = ['x' , 'y' , 'z'])
print(b)

# 3.
sites = { 1:'google' , 2 :'runoob' , 3: 'wiki' } 
b = pd.Series(sites)
print(b)

# 4.

b  = pd.Series(sites , index=[1,2] , name='RUNOOB-Series-')
print(b)

