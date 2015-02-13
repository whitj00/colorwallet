import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

# def test_set(user, balance):
#     r.hmset(user, {'balance':balance})
#     print(r.hmget(user, 'balance'))


def set_stats(user, stats):
    r.hmset(user, stats)
    return True

def get_stats(user):
    keys = ['balance']
    return r.hmget(user, keys)
    
