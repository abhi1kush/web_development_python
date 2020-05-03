import functools

from flask import request
from flask_restful import reqparse

from app.api.base import BaseAPIResource
from app.redis.redis_client import RedisClient


class HealthCheckAPIView(BaseAPIResource):
    def get(self):
        return {
                "status": "success",
                "version": 0.1
        }


class RedisDemoAPIView(BaseAPIResource):
    def test_post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('key', required=True, type=str)
        parser.add_argument('value', required=True, type=str)
        self.data = parser.parse_args()
        return True

    def post(self):
        redis_client = RedisClient()
        redis_client.isert_into_hash(key_=self.data['key'], value_=self.data['value'])

    def test_get(self):
        key_ = request.args.get('key')
        if key_ is None:
            return False
        self.key = key_

    def get(self):
        redis_client = RedisClient()
        value = redis_client.get_from_hash(self.key)
        return {"key": self.key, "value": value}


class AddAPIView(BaseAPIResource):
    def test_get(self):
        self.arg1 = request.args.get('arg1')
        if self.arg1 is None:
            self.error = "arg1 is misssing"
            return False
        self.arg2 = request.args.get('arg2')

        if self.arg2 is None:
            self.error = "arg2 is misssing"
            return False
        return True

    def get(self):
        return {"sum": int(self.arg1) + int(self.arg2)}

    def test_post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('numbers', required=True, type=list, location='json')
        self.data = parser.parse_args()
        return True

    def post(self):
        return {"sum": sum(self.data['numbers'])}