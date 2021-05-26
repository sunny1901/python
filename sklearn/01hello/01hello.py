#同样首先，我们调用模块
#matplotlib是python专门用于画图的库
import matplotlib.pyplot as plt

# SK 样本数据
from sklearn import datasets

#调用线性回归函数
from sklearn.linear_model import LinearRegression

# 导入 数据集（波士顿房间数据）
loaded_data = datasets.load_boston()


# 输出 波士顿房价数据
print( loaded_data )
print("--类型---")

print( type(loaded_data) )
print( "【KEYS】\t",            (loaded_data.keys()) )
print( "【filename】\t",        (loaded_data.filename) )
print( "【data】\t",            type(loaded_data.data) )
print( "【feature_names】\t",   type(loaded_data.feature_names) )
print( "【target】\t",          type(loaded_data.target) )


print("--摘要---")

print( "【特征名称】" ,(loaded_data.feature_names) )
print( "【特征数据】" , len(loaded_data.data) )
print( "【目标数据】" , len(loaded_data.target) )

print("--摘要---")
print( (loaded_data.DESCR) )
print( (loaded_data.target) )

print("---------")


# 这里将全部数据用于训练，并没有对数据进行划分，上例中
# 将数据划分为训练和测试数据，后面会讲到交叉验证
data_X = loaded_data.data
data_y = loaded_data.target

# 创建模型 <线性回归模块 >
model = LinearRegression()
# 训练数据，得出参数
model.fit(data_X, data_y)

# 利用模型，对新数据，进行预测，与原标签进行比较
print(model.predict(data_X[:4,:]))
print(data_y[:4]) 