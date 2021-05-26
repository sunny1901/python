#同样首先，我们调用模块
#matplotlib是python专门用于画图的库
import matplotlib.pyplot as plt

# SK 样本数据
from sklearn import datasets

# 调用线性回归函数
from sklearn.linear_model import LinearRegression

# 导入【数据集】（波士顿房间数据）
loaded_data = datasets.load_boston()

# 1. 准备数据 （高手应把数据集合在大脑中展示成一条 X 轴， 结果集展示成 Y 轴）
data_X = loaded_data.data               # 1.a 准备【训练集】 ， 训练样本
data_y = loaded_data.target             # 1.b 准备【结果集】 ， 已存在的结果

# 2. 准备【模型】 <线性回归模块 >
model = LinearRegression()

# 3. 训练数据，得出参数
model.fit( data_X , data_y)

# 4. 结果
# 利用模型，对新数据，进行预测，与原标签进行比较
print(model.predict(data_X[:4,:]))
print(data_y[:4]) 