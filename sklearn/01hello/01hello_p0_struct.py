"""
SKlern 数据可视化
"""
#matplotlib是python专门用于画图的库
import matplotlib.pyplot as plt

# SK 样本数据
from sklearn import datasets

#调用线性回归函数
from sklearn.linear_model import LinearRegression

# 导入 数据集（波士顿房间数据）
loaded_data = datasets.load_boston()


# 输出 波士顿房价数据
print("--摘要---")

print( "【特征名称】" ,(loaded_data.feature_names) )
print( "【特征数据】" , len(loaded_data.data) )
print( "【目标数据】" , len(loaded_data.target) )

print("--摘要---")
print( (loaded_data.DESCR) )
print( (loaded_data.target) )

print("---------")


