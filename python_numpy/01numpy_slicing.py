"""
Numpy 切片(Slicing):
"""


nums = list(range(5))     # range is a built-in function that creates a list of integers
print(nums)               # Prints "[0, 1, 2, 3, 4]"

print("--常规操作-------------")

# index 2 to 4 (
print(nums[2:4])          # [2, 3]
# index 2 to Max
print(nums[2:])           # [2, 3, 4]
# index 2 to Max
print(nums[:2])           # [0, 1]
# index Min to Max
print(nums[:])            # [0, 1, 2, 3, 4]
# index Min to Max-1
print(nums[:-1])          # [0, 1, 2, 3]
# 赋值
nums[2:4] = [8, 9]        # Assign a new sublist to a slice
print(nums)               # Prints "[0, 1, 8, 9, 4]"


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