#同样首先，我们调用模块
# matplotlib是python专门用于画图的库
import matplotlib.pyplot as plt

# SK 样本数据
from sklearn import datasets


# 导入 数据集（波士顿房间数据）
loaded_data = datasets.load_boston()

x_data    = loaded_data.data            # 导入所有特征变量
y_data    = loaded_data.target          # 导入目标值（房价）
name_data = loaded_data.feature_names

print("--类型---")

# 看过 sunny的有道笔记，能够更好的理解。
for i in range(13):
    plt.subplot(7,2,i+1)
    plt.scatter(x_data[:,i],y_data,s = 20)
    plt.title(name_data[i])
    plt.show()
