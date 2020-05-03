from app import redis_q


class RedisClient:
    HASH = "flask_setup_hash"
    DEFAULT_TTL = 3600

    def __init__(self):
        self.conn = redis_q.connection

    def isert_into_hash(self, key_, value_, hash_=None, ttl=3 * 3600):
        if hash_ is None:
            hash_ = RedisClient.HASH
        try:
            self.conn.hset(name=hash_, key=key_, value=value_)
            self.conn.expire(hash_, ttl)
        except Exception as e:
            raise e

    def get_from_hash(self, key_, hash_=None):
        if hash_ is None:
            hash_ = RedisClient.HASH
        try:
            return self.conn.hget(name=hash_, key=str(key_))
        except Exception as e:
            raise e

    def set(self, key_, value_, ttl=None):
        if ttl is None:
            ttl = RedisClient.DEFAULT_TTL
        try:
            self.conn.set(key_, value_, ex=ttl)
        except Exception as e:
            raise e

    def get(self, key_):
        try:
            return self.conn.get(str(key_))
        except Exception as e:
            raise e