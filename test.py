# encoding=gbk

import redis

# edis-cli -c -h 10.2.108.40 -p 7001 -a QTNCaTJXNlRVNA== KEYS "070*" | xargs redis-cli -c -h 10.2.108.40 -p 7005 -a QTNCaTJXNlRVNA== DEL

# ���ӵ� Redis ������
redis_client = redis.StrictRedis(host='10.2.108.40', port=7001, password="QTNCaTJXNlRVNA==" , db=0)

# ��ȡƥ��ĳ��ǰ׺�����м�
prefix = "070*"  # �滻����Ҫɾ����ǰ׺
keys_to_delete = redis_client.keys(f"{prefix}*")
print(keys_to_delete)

# # ����ɾ��ƥ��ļ�
# if keys_to_delete:
#     redis_client.delete(*keys_to_delete)

for i in keys_to_delete:
    redis_client.delete(i)
