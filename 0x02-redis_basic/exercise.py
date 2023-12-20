#!/usr/bin/env python3
"""Defines a class Cache"""
import redis
import uuid
from functools import wraps
from typing import Any, Union, Callable


def count_calls(method: Callable) -> Callable:
    """defines a callable wrapper"""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """counts how many times the Cache class
        is called"""
        if isinstance(self._redis, redis.Redis):
            key = method.__qualname__
            self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """defines Callable wrapper"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """stores the history of inputs and
        outputs for a particular function"""
        input_ky = '{}:inputs'.format(method.__qualname__)
        output_ky = '{}:outputs'.format(method.__qualname__)
        self._redis.rpush(input_ky, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_ky, str(output))
        return output
    return wrapper
    
    
def replay(self, func: Callable):
    """Display the history of calls for a given function"""
    input_key = f"{func.__qualname__}:inputs"
    output_key = f"{func.__qualname__}:outputs"

    input_list = self._redis.lrange(input_key, 0, -1)
    output_list = self._redis.lrange(output_key, 0, -1)

    num_calls = len(input_list)
    print(f"{func.__qualname__} was called {num_calls} times:")

    for inputs, output in zip(input_list, output_list):
        inputs_str = inputs.decode('utf-8')
        output_str = output.decode('utf-8')
        print(f"{func.__qualname__}(*{inputs_str}) -> {output_str}")


class Cache:
    """"""
    def __init__(self):
        """stores an instance of redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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

    def get_str(self, key: str) -> str:
        """retrieves a string from the Cache"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """retrieves an integer from the cache"""
        return self.get(key, fn=lambda d: int(d))
