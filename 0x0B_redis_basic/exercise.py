#!/usr/bin/env python3
"""Module to create a cache with Redis"""

import redis
import uuid


class Cache(redis.Redis):
    """Redis client class"""
    def __init__(self):
        """Instatiate the redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """Method to store data in Redis"""
        rand_key = str(uuid.uuid1())
        self._redis.set(rand_key, data)
        return rand_key
