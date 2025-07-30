#!/usr/bin/env python3
"""Module to create a cache with Redis"""

import redis
import uuid
from typing import Union


class Cache:
    """Redis client class"""
    def __init__(self) -> None:
        """Instantiate the redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str | bytes | int | float]) -> str:
        """Store data in Redis with a random key."""
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key
