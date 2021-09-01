"""
NumPy 迭代
"""

import numpy as np


print ('-- Part A ------------------------------')

a = np.arange(6).reshape( 2, 3 )        # 2 行，3列
print( a )

print(" 普通迭代 for x in a : ")
for x in a :
    print(x , end=" | ")
print("\n")

print(" 多维迭代 for x in np.nditer(a) : ")
for x in np.nditer(a) :
    print(x , end=",")
print("\n")

print(" 多维迭代 for x in np.nditer(a.T): ")
for x in np.nditer(a.T):
    print(x, end=", ")
print('\n')

print(" 多维迭代 for x in np.nditer(a.T.copy(order='C')):  ，和之前的顺序不同")
for x in np.nditer(a.T.copy(order='C')):
    print(x, end=", ")
print('\n')


print ('-- Part B   顺序------------------------------')
print ('原始数组')
a = np.arange(6).reshape( 2, 3 )
print(a)

print ('原始数组的转置是：b = a.T ')

b = a.T
print(b)

print ('以 C 风格顺序排序：')
c = b.copy(order='C')
print(c)
for x in np.nditer(c):
    print (x, end=", " )
print  ('\n')

print  ('以 F 风格顺序排序：')
c = b.copy(order='F')
print(c)
for x in np.nditer(c):
    print (x, end=", " )
print  ('\n')

print ('-- Part C nditer 参数 op_flags------------------------------')

a = np.arange( 0 , 60 , 5 )
print(a)
a = a.reshape( 3, 4 )
print(a)

print  ("迭代参数 op_flags ，for x in np.nditer( a , op_flags=['readwrite']) : ")
for x in np.nditer( a , op_flags=['readwrite']) :
    x[...] = 2 * x

print(a)

print  ("迭代参数 op_flags ，for x in np.nditer( a , op_flags=['external_loop']) : ")
for x in np.nditer(a, flags =  ['external_loop'], order =  'F'):
   print (x, end=", " )

print ('\n-- Part D nditer 广播迭代------------------------------')

a = np.arange( 0 , 60 , 5 )
a = a.reshape( 3, 4 )
print(a)
b = np.array([1,  2,  3,  4], dtype =  int)
print(b)

for x,y in np.nditer([a,b]):
    print ("%d:%d"  %  (x,y), end=", " )