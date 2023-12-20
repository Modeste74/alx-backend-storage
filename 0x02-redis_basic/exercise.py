#!/usr/bin/env python3
"""Defines a class Cache"""
import redis
import uuid
from typing import Union, Callable


class Cache:
    """"""
    def __init__(self):
        """stores an instance of redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and
        returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Callable = None
            ) -> Union[str, bytes, int, None]:
        """get the data from an already existing data in redis"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """retrieves a string from the Cache"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """retrieves an integer from the cache"""
        return self.get(key, fn=lambda d: int(d))
