"""
Numpy 切片(Slicing):
arr  = arr[ slice( 2, 7, 2 ) ] , # 写法1
arr  = arr[ 2 ： 7 : 2]  # 写法2 ， 从索引 2 开始到索引 7 停止，间隔为 2
"""


nums = list(range(5))     # range is a built-in function that creates a list of integers
print(nums)               # Prints "[0, 1, 2, 3, 4]"

print("--常规操作-------------")

# index Min to Max 或者 0 ~ Max
print(nums[:])            # [0, 1, 2, 3, 4]

# index 2 to 4
print(nums[2:4])          # [2, 3]

# index 2 to Max
print(nums[2:])           # [2, 3, 4]

# index Min to 2  或者 0 ~ 2
print(nums[:2])           # [0, 1]

# index Min to Max-1
#        ‘无符号” 情况为索引下标，
#        ‘有 - 符号’情况为最大下标 - 去的值，逆推）
print(nums[:-1])          # [0, 1, 2, 3]

# 赋值
nums[2:4] = [8, 9]        # Assign a new sublist to a slice
print(nums)               # Prints "[0, 1, 8, 9, 4]"


print("--常规操作( 二维)-------------")
# index 2 to 4
# print(nums[ 第一维 ,第二维]  )
# print(nums[ :3 , : ]  ) # 所有

print("--非常规( `-` 代表从后向前计算位置 )-------------")
nums = list(range(5))
print(nums[:-1])          # [0, 1, 2, 3]
print(nums[:-2])          # [0, 1, 2]
print(nums[:-3])          # [0, 1]
print(nums[:-4])          # [0]
print(nums[:-5])          # []


print("--非常规-------------")
print(nums[-1:])          # [4]
print(nums[-2:])          # [3, 4]
print(nums[-3:])          # [2, 3, 4]
print(nums[-4:])          # [1, 2, 3, 4]
print(nums[-5:])          # [0, 1, 2, 3, 4]