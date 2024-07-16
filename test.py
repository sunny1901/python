# encoding=gbk

import redis

# edis-cli -c -h 10.2.108.40 -p 7001 -a QTNCaTJXNlRVNA== KEYS "070*" | xargs redis-cli -c -h 10.2.108.40 -p 7005 -a QTNCaTJXNlRVNA== DEL

# 连接到 Redis 服务器
redis_client = redis.StrictRedis(host='10.2.108.40', port=7001, password="QTNCaTJXNlRVNA==" , db=0)

# 获取匹配某个前缀的所有键
prefix = "070*"  # 替换成你要删除的前缀
keys_to_delete = redis_client.keys(f"{prefix}*")
print(keys_to_delete)

# # 批量删除匹配的键
# if keys_to_delete:
#     redis_client.delete(*keys_to_delete)

for i in keys_to_delete:
    redis_client.delete(i)
