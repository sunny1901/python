import time
from elasticsearch import Elasticsearch

es = Elasticsearch(
    ['10.1.110.75:9200' , '10.1.110.76:9200' , '10.1.110.77:9200'],
    # 认证信息
    # http_auth=('elastic', 'changeme')
)

#插入数据,(这里省略插入其他两条数据，后面用)
# es.index(index="my-index",doc_type="test-type",id=01,body={"any":"data01","timestamp":datetime.now()})
def add( _index , data ):
    # es.index( index= _index , doc_type= 'doc', body=data )
    es.index( index= _index , body=data )
    # es.create(  index= _index ,   doc_type='doc',   body=data  )

# Get
#res = es.get(index="my-index", doc_type="test-type", id=01)
#      es.get(index='indexName', doc_type='typeName', id='idValue')
def get( idx , type , doc_id ):
    return es.get(index= idx , doc_type= type , id= doc_id )

# es.delete(index='indexName', doc_type='typeName', id='idValue')
# delete_by_query：删除满足条件的所有数据，查询条件必须符合DLS格式
# query = {'query': {'match': {'sex': 'famale'}}}# 删除性别为女性的所有文档
# query = {'query': {'range': {'age': {'lt': 11}}}}# 删除年龄小于11的所有文档
# es.delete_by_query(index='indexName', body=query, doc_type='typeName')
