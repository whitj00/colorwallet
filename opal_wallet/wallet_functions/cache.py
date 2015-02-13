import redis

from wallet_functions import wallet_functions

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def test_set(bal):
    r.set('balance', bal)
    print r.get('balance')
