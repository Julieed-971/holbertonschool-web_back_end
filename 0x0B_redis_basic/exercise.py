#!/usr/bin/env python3
"""Module to create a cache with Redis"""

import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """Redis client class"""
    def __init__(self) -> None:
        """Instantiate the redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis with a random key."""
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[
                str, bytes, int, float, None]:
        """Retrieve data from Redis and
        convert data back to the desired format"""
        data = self._redis.get(key)

        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """Retrieve data as string"""
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        """Retrieve data as int"""
        return self.get(key, fn=int)
