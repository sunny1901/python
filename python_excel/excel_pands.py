import pandas as pd

# DataFrame.to_excel(excel_writer, sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, encoding=None, inf_rep='inf', verbose=True, freeze_panes=No


# pd.read_excel(io, sheet_name=0, header=0, names=None, index_col=None,
#               usecols=None, squeeze=False,dtype=None, engine=None,
#               converters=None, true_values=None, false_values=None,
#               skiprows=None, nrows=None, na_values=None, parse_dates=False,
#               date_parser=None, thousands=None, comment=None, skipfooter=0,
#               convert_float=True, **kwds)


# df.drop(['Name'], axis=1) # 删除列
# df1.drop(labels=[1,3],axis=0)   #删除行
# df.drop([0, 1]) # 删除行
# df.drop_duplicates() # 删除重复值
# df.fillna('missing')# 使用字符串填补
# df.replace('old', 'new') # old替换成new
# df.rename(columns={'old_name': 'new_name'}) # 选择性更改列名
# df.columns = ['a','b','c'] # 重命名列名
# df.dropna(axis = 0) # 删除有缺失的行
# df.dropna(axis = 1) # 删除有缺失的列

df = pd.read_excel("2.xlsx" , sheet_name='uat')


# 打印头部数据，仅查看数据示例时常用
print("# head---------------------")
print(df.head())

# 打印列标题
print("# columns---------------------")
print(df.columns)


# 打印行
print("# index---------------------")
print(df.index)



# 描述数据
print("# describe---------------------")
print(df.describe())

# df.columns = df.columns.str.replace('Unnamed.*', 'col_label')
# print(df.columns)

# df = df.drop([0, 1, 2] , axis=0) # 删除行
a = [ x for x in range(49)]
df = df.drop(a , axis=0) # 删除行
columns = df.columns.values.tolist()
i = 0
print("\n\n")

# 测试表名
# tabName = "dict_config_type_test1"
# 正式表名
# tabName = "dict_config_type"
for idx, row in df.iterrows(): ### 迭代数据 以键值对的形式 获取 每行的数据
    i += 1
    d_row = {}
    # for column in columns:
    #     d_row[column] = row[column]
    id =  i if i > 10 else "0"+str(i)
    sql  =row['字段1"'].replace("'" , '"')
    expire = x if not pd.isnull(row['redis缓存时间，-1为不过期']) else -1
    s2 = "insert into 表名称( `id` ,`dict_type` ,`system`,`datasource`,`table_name`,`statement`,`redis_expire_time`) values ( 440{0} , '{1}' , '{2}' , '{3}' ,'{4}' ,'{5}' , '{6}' );".format(
            id,
            row['字段1'],
            row['字段2'],
            row['字段3'] ,
            row['字段4'] ,
            sql,
            expire
    )
    print(s2 )

print("\n\n")

