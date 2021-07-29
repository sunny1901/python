#!/usr/bin/python
# -*- coding: UTF-8 -*-

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
print("--摘要---------------------------------------------------------------------------------------------")
# print( (loaded_data.DESCR) )

print( "【特征数据】" , len(loaded_data.data)   , '条' )
print( "【目标数据】" , len(loaded_data.target) , '条')
print("--特征量--------------------------------------------------------------------------------------------")

print( "【特征名称】")
feature_names_cn = {
    'CRIM'  : '犯罪率' ,
    'ZN'    : '住宅用地比率(超2万5)',
    'INDUS' : '城镇中非住宅用地所占比例',
    'CHAS'  : '是否穿过查尔斯河',
    'NOX'   : '环保指数（氮氧化物浓度）' ,
    'RM'    : '房间数' ,
    'AGE'   : '1940 年以前建成的自住单位的比例' ,
    'DIS'   : '距离5个就业中心的加权距离' ,
    'RAD'   : ' 高速路便利指数' ,
    'TAX'   : ' 每一万美元的不动产税率' ,
    'PTRATIO'   : '城镇中的教师学生比例' ,
    'B'     : '城镇中的黑人比例' ,
    'LSTAT' : '地区中有多少房东属于低收入人群' ,
    'PRICE' : '价格'
}
# feature_names_cn['CRIM'] = "犯罪率"
# print( loaded_data.feature_names )

for key in loaded_data.feature_names :
    print("\t - ", key , '\t' , feature_names_cn.get( key , '- ') )

print("--特征数据--", len(loaded_data.data)   , '条')
num = 3
data_X = loaded_data.data
data_X_test = data_X[: num ]

for row in data_X_test :
    for i in range(len( row )) :
        print( row[i] , "\t", end=' ')
    print('')

print("--结果集---------------------------------------------------------------------------------------------")
print("预测房价")

data_Y = loaded_data.target
data_Y_test = data_Y[: num]
n = 10  # 每10个数换一行

for i in range(len(data_Y_test)) :
    print(data_Y_test[i] , "\t\t", end=' ')
    if ( (i+1)%n == 0 ):
        print('')

print('\n')


print("--训练Start---------------------------------------------------------------------------------------------")

# 创建模型 <线性回归模块 >
model = LinearRegression()
# 训练数据，得出参数
model.fit( data_X , data_Y )


# 利用模型，对新数据，进行预测，与原标签进行比较
y1 = model.predict( data_X_test[ :4 , : ] )
y2 = data_Y_test[ :4]
print( '预测Y值' , y1 )
print( '真实Y值' , y2 )