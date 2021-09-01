"""
NumPy 高级索引 ， 使用数组做为索引的输入
https://www.runoob.com/numpy/numpy-advanced-indexing.html
"""

print("1 高级索引 [[1,2] , [3,4] , [5,6]]")
import numpy as np
# get （0，0） ， （1，1） ， （2，0）
arr = np.array([
    [1,2] ,
    [3,4] ,
    [5,6]
])
y = arr[
    [0,1,2] , [0,1,0]
]

# 解释索引图
#  0 | 0  => (0,0)
#  1 | 1  => (1,1)
#  2 | 0  => (2,0)

print(y)

print("2 高级索引 x[rows,cols]  ")

arr = np.array([
    [  0,  1,  2],
    [  3,  4,  5],
    [  6,  7,  8],
    [  9,  10,  11]
])

rows_idx = np.array([ [0,0] , [3,3] ])
print("rows\n " ,rows_idx)

cols_idx = np.array([ [0,2] , [0,2] ])
print("cols\n " ,cols_idx)
y = arr[ rows_idx , cols_idx ]

print("高级索引结果\n" , y )


"""
0,1,2
3,4,5
6,7,8
9,10,11
=>
rows =    0_ ,0_ ,3_ ,3_
cols =    _0 ,_2 ,_0 ,_2
index =   00 ,02 ,30 ,32
=> 结果
0 , 2 , 9 , 11
"""

print("高级索引解释sunny\n" , y )
print(arr[ [ 0 ,0 ,3, 3 ], [ 0, 2, 0, 2] ])
