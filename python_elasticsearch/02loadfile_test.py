# -*- coding: utf-8 -*-
import json,time,datetime
from python_elasticsearch import  EsUtils
import traceback
import sys

def getJsonObj(jsonStr):
    jsonObj = json.loads(jsonStr)
    # jsonObj["add_time"] = time.time()
    # jsonObj["add_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # jsonObj["add_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    jsonObj["add_time"] = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]
    return jsonObj


def addJsonStr( str ):
    jsonObj = {}
    str = str.strip()
    if str == "" or len(str) <= 1 :
        print( "跳过字符：`" + str +"`")
        return



    try:
        c1 = str[-1]
        # print(c1)

        if c1 == ","  :
           str = str[:-1]

        jsonObj = getJsonObj( str )
    except Exception as e:
        print(str)
        error_(e)
        raise TypeError('脏数据跳过：') from e

    try:
        EsUtils.add( "idx_core_user_test3" , jsonObj )
    except Exception as e :
        print(str)
        error_(e)
        # raise TypeError('插入ES报错：') from e


def loadFile():
    # file.path
    # path = 'G:/log_core/data/1000.log'
    path = 'G:/log_core/data/10W_jihuoka.txt'
    # path = 'G:/log_core/data/10W_yijianxian.txt'
    # path = 'G:/log_core/data/10W_feiche.txt'
    # path = 'G:/log_core/data/10W_che.txt'

    # file.encoding
    # encoding = 'utf-8'
    encoding = 'gbk'
    # encoding = 'unicode_escape'

    # open , run
    f = open(path, 'r', encoding= encoding )
    str = ""
    i = 0
    for line in f.readlines():
        # line = line.replace("\n"," ")
        str += line
        i = i + 1
        print ( "run " + repr(i)  )
        # print(line)
        try:
            addJsonStr( line )
        except Exception as e:
            print('str(e):\t\t', e )

    f.close()




if __name__ == "__main__" :
    try:
        for i in range(400000):
            loadFile()
    except Exception as e:
        print('str(Exception):\t', str(Exception))
        error_(e)