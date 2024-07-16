#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

# MySQL 数据库连接参数
db_config = {
    'host': '10.1.23.10',
    'port': 6033,
    'db_name': 'e_contract_dev',

    'user': 'e_contract_user',
    'passwd': 'e_contract_123456'
}


# url: jdbc:mysql://10.1.23.10:6033/e_contract_test?useUnicode=true&allowMultiQueries=true&autoReconnect=true&characterEncoding=UTF-8&serverTimezone=Asia/Shanghai
# username: e_contract_user
# password: e_contract_123456

class MysqlFactory:

    # 初始化方法
    # def __init__(self, host, port, user, passwd, dbName, charsets):
    #     self.host = host
    #     self.port = port
    #     self.user = user
    #     self.passwd = passwd
    #     self.dbName = dbName
    #     self.charsets = charsets

    def __init__(self, _config=db_config):
        self.host = _config.get('host')
        self.port = _config.get('port')
        self.db_name = _config.get('db_name')

        self.user = _config.get('user')
        self.passwd = _config.get('passwd')
        # self.charsets = _config.charsets


        # 链接数据库
    def connection(self):
        self.db = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            db=self.db_name,
            # charset=self.charsets
            cursorclass=pymysql.cursors.DictCursor
        )
        self._cursor = self.db.cursor()


    # 关闭链接
    def close(self):
        try:
            self._cursor.close()
            self.db.close()
        except BaseException as e:
            print("数据库关闭失败！")
            print(str(e))


    # 插入数据
    def insert(self, sql):
        count = 0
        try:
            self.connection()
            count = self._cursor.execute(sql  )
            self.db.commit()
            self.close()
        except BaseException as e:
            print("MysqlDao insert() 操作失败！: \n" + sql  + "\n")
            self.db.rollback()
            print( e )
        return count

    # 删除数据
    def delete(self, sql):
        return self.insert(sql)

    # 更新数据
    def update(self, sql):
        return self.insert(sql)


    # 查询列表数据
    def query(self, sql):
        res = None
        try:
            self.connection()
            self._cursor.execute(sql)
            res = self._cursor.fetchall()
            self.close()
        except BaseException as e:
            print("MysqlDao 查询失败！")
            print(str(e))

        if isinstance(res, tuple):
            if len(res) == 0 :
                return None
        return res

    # 查询单行记录
    def get(self, sql):
        print( sql )
        res = None
        try:
            # res = self.cursor.fetchone()
            self.connection()
            self._cursor.execute(sql)
            res = self._cursor.fetchone()

            if res is None:
                return None

            if isinstance(res, tuple):
                if len(res) == 0:
                    return None

            return res[0]
        except BaseException as e:
            print("MysqlDao.get() 查询失败  ")
            print(str(e))
        return res

    def databaseVersion(self) :
        data = self.query("select version()")
        # data = self.query("select 1")
        print ('>>>>>>>>>>>>>' , data)





# 打开文件
file_path = r'D:\tmp\spy\9.sql'  # 替换为实际的文件路径
name = '批改/提交核保'
db1 = MysqlFactory()

# 打开文件并逐行读取内容
with open(file_path, 'r') as file:
    i = 0
    for line in file:
        if i == 1 :
            i = 0
            continue
        i = 1

        # 使用 | 分割每一行的字符串
        result_list = line.strip().split('|')
        length = len(result_list)

        if length < 2:
            # print(line)
            continue

        print(result_list[0])
        print(result_list[1])

        cost_time = result_list[1].replace("耗时","").replace("ms","").strip()
        print('cost_time >' + result_list[2])
        try:
            cost_time = int(cost_time)
        except Exception as e:
            cost_time = -1


        exp_info = result_list[2][8:]
        exp_info= exp_info.replace('"','\"')
        print(result_list[2][8:])

        # db1.databaseVersion()

        sql  = "INSERT INTO t_ply_nonauto_log_analysis (log_time, module_name, infos, cost_type,cost_time,exp_info) VALUES ('%s','%s',\"%s\",'%s','%s',\"%s\")" \
               % (result_list[0], 'oldnoauto', name , 'DB',cost_time ,exp_info)

        db1.insert(sql)

        # 处理分割后的数据，这里只是简单地打印每个子字符串
        # for item in result_list:
        #     print(item)



