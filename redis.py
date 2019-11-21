import redis

r = redis.Redis(host = '10.165.12.221', port = 9093, db = 0)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
# r.set('name', 'junxi')  # key是"foo" value是"bar" 将键值对存入redis缓存
print(r['nftr_40961'])
print(r.get('nftr_40961'))  # 取出键name对应的值
print(type(r.get('nftr_40961')))
print(r.mget('nftr_40961','nftr_49061'))