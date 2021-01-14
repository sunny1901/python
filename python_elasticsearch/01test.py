
import time

from elasticsearch import Elasticsearch

es = Elasticsearch(
    ['10.1.110.75:9200'],
    # 认证信息
    # http_auth=('elastic', 'changeme')
)

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print('共耗时约 {:.2f} 秒'.format(time.time() - start))
        return res
    return wrapper

@timer
def create_data():
    """ 写入数据 """
    for line in range(100):
        es.index(index='idx_core_user', doc_type='doc', body={'title': line})

if __name__ == '__main__':
    create_data()   # 执行结果大约耗时 7.79 秒